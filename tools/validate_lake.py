from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    slots_doc = json.loads((ROOT / "content/shared/image-slots.json").read_text(encoding="utf-8"))
    packets_doc = json.loads((ROOT / "prompts/packets/index.json").read_text(encoding="utf-8"))
    sources_doc = json.loads((ROOT / "research/sources/catalog.json").read_text(encoding="utf-8"))
    jobs_doc = json.loads((ROOT / "jobs/definitions/jobs.json").read_text(encoding="utf-8"))

    slots = slots_doc["slots"]
    packets = packets_doc["packets"]
    sources = sources_doc["sources"]
    jobs = jobs_doc["jobs"]
    check(len(slots) == 390 == slots_doc["count"], "expected exactly 390 image slots")
    check(len(packets) == 39 == packets_doc["count"], "expected exactly 39 packets")
    check(len(sources) == 125 == sources_doc["total"], "expected exactly 125 research sources")
    check(sum(1 for s in sources if s["source_id"][0] != "L") == 100, "expected 100 game sources")
    check(sum(1 for s in sources if s["source_id"][0] == "L") == 25, "expected 25 lake sources")

    for field, values in {
        "slot IDs": [s["slot_id"].casefold() for s in slots],
        "filenames": [s["filename"].casefold() for s in slots],
        "packet IDs": [p["packet_id"].casefold() for p in packets],
        "source IDs": [s["source_id"].casefold() for s in sources],
        "source URLs": [unquote(s["url"]).rstrip("/").casefold() for s in sources],
        "job IDs": [j["job_id"].casefold() for j in jobs],
    }.items():
        check(len(values) == len(set(values)), f"duplicate {field}")

    packet_ids = {p["packet_id"] for p in packets}
    slot_packet_ids = {s["packet_id"] for s in slots}
    check(slot_packet_ids == packet_ids, "slot registry and packet registry disagree")
    for packet in packets:
        path = ROOT / packet["path"]
        for required in ["PROMPT.md", "DROP-HERE.md", "packet.json", "expected-files.json"]:
            check((path / required).is_file(), f"missing {packet['packet_id']}/{required}")
        expected = json.loads((path / "expected-files.json").read_text(encoding="utf-8"))
        check(len(expected["files"]) == 10, f"{packet['packet_id']} does not contain ten files")

    job_ids = {j["job_id"] for j in jobs}
    for job in jobs:
        for dependency in job["depends_on"]:
            check(dependency in job_ids, f"{job['job_id']} references unknown dependency {dependency}")

    tracked_text_extensions = {".md", ".json", ".jsonl", ".yaml", ".yml", ".py", ".js", ".txt"}
    secret_pattern = re.compile(r"(?i)(api[_-]?key|access[_-]?token|client[_-]?secret)\s*[:=]\s*['\"]?[A-Za-z0-9_-]{16,}")
    private_path = re.compile(r"(?i)(C:\\Users\\|/Users/|Z:\\)")
    for path in ROOT.rglob("*"):
        relative_parts = path.relative_to(ROOT).parts
        if any(part in {".git", "site", "build", ".venv", ".venv-docs", "__pycache__"} for part in relative_parts) or not path.is_file() or path.suffix not in tracked_text_extensions:
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        text = path.read_text(encoding="utf-8")
        check(not secret_pattern.search(text), f"possible secret in {path.relative_to(ROOT)}")
        if path.name not in {"START-HERE.md"}:
            check(not private_path.search(text), f"private/local path in {path.relative_to(ROOT)}")

    if errors:
        print("Lake validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Lake valid: {len(packets)} packets, {len(slots)} slots, {len(sources)} sources, {len(jobs)} jobs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
