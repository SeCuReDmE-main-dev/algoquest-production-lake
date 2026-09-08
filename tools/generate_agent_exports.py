from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENT = ROOT / "docs" / "agent"


def canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def export() -> None:
    AGENT.mkdir(parents=True, exist_ok=True)
    slots = json.loads((ROOT / "content/shared/image-slots.json").read_text(encoding="utf-8"))
    packets = json.loads((ROOT / "prompts/packets/index.json").read_text(encoding="utf-8"))
    jobs = json.loads((ROOT / "jobs/definitions/jobs.json").read_text(encoding="utf-8"))
    sources = json.loads((ROOT / "research/sources/catalog.json").read_text(encoding="utf-8"))
    books = [json.loads(path.read_text(encoding="utf-8")) for path in sorted((ROOT / "content" / "books").glob("*/book.json"))]
    packet_details = {}
    for packet in packets["packets"]:
        packet_path = ROOT / packet["path"] / "packet.json"
        packet_details[packet["packet_id"]] = json.loads(packet_path.read_text(encoding="utf-8"))
    exports = {
        "image-slots.json": slots,
        "packets.json": packets,
        "packet-details.json": {"schema": "securedme.education.algoquest.packet-details.v1", "packets": packet_details},
        "jobs.json": jobs,
        "books.json": {"schema": "securedme.education.algoquest.book-registry.v1", "books": books},
    }
    for name, value in exports.items():
        (AGENT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    shutil.copyfile(ROOT / "research/sources/catalog.jsonl", AGENT / "research-sources.jsonl")
    index = {
        "schema": "securedme.education.algoquest.agent-index.v1",
        "counts": {"packets": packets["count"], "image_slots": slots["count"], "research_sources": sources["total"], "jobs": len(jobs["jobs"])},
        "resources": {name.removesuffix(".json"): f"./{name}" for name in exports},
        "research_sources": "./research-sources.jsonl",
        "digests": {name: "sha256:" + hashlib.sha256(canonical_json(value).encode()).hexdigest() for name, value in exports.items()},
        "write_policy": "read-only-public; persistent changes require authenticated Git review",
    }
    (AGENT / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    shutil.copyfile(ROOT / "webmcp" / "algoquest-tools.js", AGENT / "algoquest-tools.js")
    print(f"Generated {len(exports) + 3} agent artifacts in {AGENT}")


if __name__ == "__main__":
    export()
