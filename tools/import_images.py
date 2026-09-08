from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import struct
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"^AQ-(EX|SH|MAG|RON|MAR|ALC|NEU|CIT)-\d{3}__v\d{3}\.(png|jpe?g|webp)$", re.I)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def image_info(path: Path) -> tuple[str, int, int]:
    data = path.read_bytes()[:32]
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        width, height = struct.unpack(">II", data[16:24]); return "png", width, height
    if data.startswith(b"RIFF") and data[8:12] == b"WEBP":
        kind = data[12:16]
        if kind == b"VP8X":
            return "webp", 1 + int.from_bytes(data[24:27], "little"), 1 + int.from_bytes(data[27:30], "little")
        raise ValueError("WebP variant requires manual dimension review")
    if data.startswith(b"\xff\xd8"):
        raw = path.read_bytes(); cursor = 2
        while cursor + 9 < len(raw):
            if raw[cursor] != 0xFF: cursor += 1; continue
            marker = raw[cursor + 1]; cursor += 2
            if marker in {0xD8, 0xD9}: continue
            length = int.from_bytes(raw[cursor:cursor+2], "big")
            if marker in range(0xC0, 0xC4):
                return "jpeg", int.from_bytes(raw[cursor+5:cursor+7], "big"), int.from_bytes(raw[cursor+3:cursor+5], "big")
            cursor += length
        raise ValueError("JPEG dimensions not found")
    raise ValueError("unsupported or misleading file signature")


def locate_packet(packet_id: str) -> Path:
    index = json.loads((ROOT / "prompts/packets/index.json").read_text(encoding="utf-8"))
    match = next((p for p in index["packets"] if p["packet_id"].casefold() == packet_id.casefold()), None)
    if not match: raise SystemExit(f"Unknown packet: {packet_id}")
    return ROOT / match["path"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Preserve and register an AlgoQuest image submission")
    parser.add_argument("--packet", required=True)
    parser.add_argument("--operator", required=True)
    parser.add_argument("--producer-tool", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    packet_dir = locate_packet(args.packet)
    expected_doc = json.loads((packet_dir / "expected-files.json").read_text(encoding="utf-8"))
    expected = {item["filename"].casefold(): item for item in expected_doc["files"]}
    candidates = [p for p in packet_dir.iterdir() if p.is_file() and p.suffix.casefold() in {".png", ".jpg", ".jpeg", ".webp"}]
    records, errors = [], []
    for source in candidates:
        if not NAME.fullmatch(source.name) or source.name.casefold() not in expected:
            errors.append({"file": source.name, "error": "ambiguous-or-unexpected-filename"}); continue
        before = sha256(source)
        try: image_format, width, height = image_info(source)
        except ValueError as exc:
            errors.append({"file": source.name, "error": str(exc)}); continue
        after = sha256(source)
        if before != after:
            errors.append({"file": source.name, "error": "source-changed-during-read"}); continue
        records.append({"filename": source.name, "slot_id": expected[source.name.casefold()]["slot_id"], "sha256": before, "format": image_format, "width": width, "height": height, "bytes": source.stat().st_size})
    if errors or len(records) != 10:
        print(json.dumps({"status": "rework", "accepted": len(records), "expected": 10, "errors": errors}, ensure_ascii=False, indent=2))
        return 2
    submission_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
    target = ROOT / "images" / "submissions" / args.packet / submission_id
    if not args.dry_run:
        originals = target / "originals"; originals.mkdir(parents=True, exist_ok=False)
        for record in records:
            source = packet_dir / record["filename"]; destination = originals / record["filename"]
            with source.open("rb") as incoming, destination.open("xb") as outgoing: shutil.copyfileobj(incoming, outgoing)
            if sha256(destination) != record["sha256"]: raise RuntimeError(f"copy hash mismatch: {record['filename']}")
        manifest = {"schema": "securedme.education.algoquest.asset-submission.v1", "submission_id": submission_id, "packet_id": args.packet, "operator": args.operator, "producer_tool": args.producer_tool, "created_at": datetime.now(timezone.utc).isoformat(), "files": records, "art_reference_selected": False, "final_asset_approved": False}
        (target / "submission.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "validated" if args.dry_run else "received", "submission_id": submission_id, "files": len(records), "target": str(target.relative_to(ROOT))}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
