#!/usr/bin/env python3
"""Canonical validator for the writing machine."""

import os
import re
import sys
from pathlib import Path

TRIAD_FILES = ("CANON.md", "VOCABULARY.md", "README.md")
TRIAD_REQUIREMENT = "CANON.md:134-145 (Triad requirement)"
REQUIRED_ARTIFACTS_REQUIREMENT = "CANON.md:248-278 (Required artifacts)"
USER_GUIDE_ASSET_REQ = "user-guide/CANON.md:60-63 (FSM Validation Details)"
USER_GUIDE_STRUCTURE_REQ = "user-guide/CANON.md:64-66 (FSM Validation Details)"


def parse_required_artifacts(canon_path: Path):
    required = []
    section_open = False
    if not canon_path.exists():
        return required
    with canon_path.open(encoding="utf-8") as fp:
        for line_number, line in enumerate(fp, start=1):
            stripped = line.strip()
            if stripped == "## Required Artifacts (root level)":
                section_open = True
                continue
            if not section_open:
                continue
            if stripped.startswith("## "):
                break
            if line.startswith("- "):
                name_part = line[2:].split()[0] if len(line) > 2 else ""
                if name_part:
                    required.append({"name": name_part, "line": line_number})
    return required


def parse_vocab_terms(vocab_path: Path):
    terms = {}
    if not vocab_path.exists():
        return terms
    with vocab_path.open(encoding="utf-8") as fp:
        for line_number, line in enumerate(fp, start=1):
            if line.startswith("### "):
                term = line[4:].strip()
                if term:
                    terms[term] = line_number
    return terms


def parse_asset_ledger(ledger_path: Path, violations: list = None, root: Path = None):
    asset_ids = set()
    asset_sources = {}
    if not ledger_path.exists():
        return asset_ids, asset_sources

    expected_next_id = 1
    with ledger_path.open(encoding="utf-8") as fp:
        for line_number, line in enumerate(fp, start=1):
            stripped = line.strip()
            if not stripped.startswith("| asset-"):
                continue
            columns = [col.strip() for col in stripped.strip("|").split("|")]
            if not columns:
                continue
            asset_id = columns[0]

            # Validate asset ID format
            if violations is not None and root is not None:
                if not re.match(r"^asset-\d{4}$", asset_id):
                    violations.append({
                        "artifact": format_artifact_path(ledger_path, root),
                        "line": line_number,
                        "requirement": USER_GUIDE_ASSET_REQ,
                        "details": f"Asset ID '{asset_id}' has invalid format (expected: asset-NNNN with 4 digits).",
                    })
                else:
                    # Check sequential numbering
                    id_num = int(asset_id.split("-")[1])
                    if id_num != expected_next_id:
                        violations.append({
                            "artifact": format_artifact_path(ledger_path, root),
                            "line": line_number,
                            "requirement": USER_GUIDE_ASSET_REQ,
                            "details": f"Asset ID {asset_id} breaks sequential order (expected: asset-{expected_next_id:04d}).",
                        })
                    expected_next_id = id_num + 1

            source_value = columns[3] if len(columns) > 3 else ""
            sources = [segment.strip() for segment in source_value.split(",") if segment.strip()]
            asset_ids.add(asset_id)
            asset_sources[asset_id] = {"line": line_number, "sources": sources}
    return asset_ids, asset_sources


def list_episode_ids(episodes_dir: Path, violations: list = None, root: Path = None):
    ids = set()
    if not episodes_dir.exists():
        return ids
    for entry in episodes_dir.iterdir():
        if not entry.is_file():
            continue
        name = entry.name

        # Skip triad files
        if name in TRIAD_FILES:
            continue

        # Validate episode naming
        if violations is not None and root is not None:
            if not re.match(r"^episode-\d{2}\.md$", name):
                violations.append({
                    "artifact": format_artifact_path(entry, root),
                    "line": None,
                    "requirement": USER_GUIDE_ASSET_REQ,
                    "details": f"Episode filename '{name}' has invalid format (expected: episode-NN.md with 2 digits).",
                })

        if not name.startswith("episode-") or not name.endswith(".md"):
            continue
        id_part = name[len("episode-") : -len(".md")]
        if id_part:
            ids.add(id_part)
    return ids


def parse_structure_sections(structure_path: Path):
    sections = []
    if not structure_path.exists():
        return sections
    with structure_path.open(encoding="utf-8") as fp:
        for line_number, line in enumerate(fp, start=1):
            stripped = line.strip()
            if not stripped.startswith("## Section"):
                continue
            title = stripped.split(":", 1)[1].strip() if ":" in stripped else stripped[len("## Section") :].strip()
            sections.append({"name": title, "line": line_number})
    return sections


def parse_prose_sections(prose_path: Path):
    sections = []
    if not prose_path.exists():
        return sections
    with prose_path.open(encoding="utf-8") as fp:
        for line_number, line in enumerate(fp, start=1):
            stripped = line.strip()
            if stripped.startswith("## "):
                sections.append({"name": stripped[3:].strip(), "line": line_number})
    return sections


def validate_prose_asset_references(root: Path, prose_path: Path, asset_ids, violations: list):
    if not prose_path.exists():
        violations.append(
            {
                "artifact": format_artifact_path(prose_path, root),
                "line": None,
                "requirement": USER_GUIDE_ASSET_REQ,
                "details": "Missing prose/draft.md; FSM validation requires prose to exist.",
            }
        )
        return
    pattern = re.compile(r"asset-\d{4}")
    missing = set()
    with prose_path.open(encoding="utf-8") as fp:
        for line_number, line in enumerate(fp, start=1):
            for match in pattern.finditer(line):
                asset_id = match.group(0)
                if asset_id not in asset_ids and asset_id not in missing:
                    missing.add(asset_id)
                    violations.append(
                        {
                            "artifact": format_artifact_path(prose_path, root),
                            "line": line_number,
                            "requirement": USER_GUIDE_ASSET_REQ,
                            "details": f"Prose references {asset_id} which is not registered in assets/LEDGER.md.",
                        }
                    )


def validate_asset_sources(root: Path, asset_sources, episode_ids, violations: list, ledger_path: Path):
    for asset_id, meta in asset_sources.items():
        line_number = meta["line"]
        sources = meta["sources"]
        if not sources:
            violations.append(
                {
                    "artifact": format_artifact_path(ledger_path, root),
                    "line": line_number,
                    "requirement": USER_GUIDE_ASSET_REQ,
                    "details": f"Asset {asset_id} lists no Source Episode in LEDGER.md.",
                }
            )
            continue
        for episode_id in sources:
            if episode_id not in episode_ids:
                violations.append(
                    {
                        "artifact": format_artifact_path(ledger_path, root),
                        "line": line_number,
                        "requirement": USER_GUIDE_ASSET_REQ,
                        "details": f"Asset {asset_id} references episode {episode_id} but no such episode file exists.",
                    }
                )


def validate_structure_sections(
    root: Path,
    structure_sections,
    prose_sections,
    violations: list,
    structure_path: Path,
    prose_path: Path,
):
    if not structure_path.exists():
        violations.append(
            {
                "artifact": format_artifact_path(structure_path, root),
                "line": None,
                "requirement": USER_GUIDE_STRUCTURE_REQ,
                "details": "Missing structure/outline.md; cannot verify section order.",
            }
        )
        return
    if not prose_path.exists():
        # Prose existence is checked elsewhere; skip order check when no prose.
        return
    last_index = -1
    for section in structure_sections:
        name = section["name"]
        structure_line = section["line"]
        found_index = None
        found_line = None
        for idx, entry in enumerate(prose_sections):
            if entry["name"] == name:
                found_index = idx
                found_line = entry["line"]
                break
        if found_index is None:
            violations.append(
                {
                    "artifact": format_artifact_path(structure_path, root),
                    "line": structure_line,
                    "requirement": USER_GUIDE_STRUCTURE_REQ,
                    "details": f"Structure section '{name}' cannot be found in prose/draft.md.",
                }
            )
            continue
        if found_index <= last_index:
            violations.append(
                {
                    "artifact": format_artifact_path(prose_path, root),
                    "line": found_line,
                    "requirement": USER_GUIDE_STRUCTURE_REQ,
                    "details": f"Section '{name}' appears out of order relative to structure/outline.md.",
                }
            )
        last_index = found_index


def validate_user_guide_fsm(root: Path, violations: list):
    user_guide = root / "user-guide"
    if not user_guide.exists():
        return
    ledger_path = user_guide / "assets" / "LEDGER.md"
    episodes_dir = user_guide / "episodes"
    prose_path = user_guide / "prose" / "draft.md"
    structure_path = user_guide / "structure" / "outline.md"

    ledger_exists = ledger_path.exists()
    if not ledger_exists:
        violations.append(
            {
                "artifact": format_artifact_path(ledger_path, root),
                "line": None,
                "requirement": USER_GUIDE_ASSET_REQ,
                "details": "Missing assets/LEDGER.md; cannot validate asset references.",
            }
        )
    asset_ids, asset_sources = parse_asset_ledger(ledger_path, violations, root)
    episode_ids = list_episode_ids(episodes_dir, violations, root)
    structure_sections = parse_structure_sections(structure_path)
    prose_sections = parse_prose_sections(prose_path)

    if ledger_exists:
        validate_prose_asset_references(root, prose_path, asset_ids, violations)
        validate_asset_sources(root, asset_sources, episode_ids, violations, ledger_path)
    else:
        if not prose_path.exists():
            # Without a ledger we still want to flag missing prose separately.
            validate_prose_asset_references(root, prose_path, asset_ids, violations)
    validate_structure_sections(root, structure_sections, prose_sections, violations, structure_path, prose_path)


def format_artifact_path(path: Path, root: Path):
    rel = path.relative_to(root)
    rel_str = str(rel)
    return rel_str if rel_str else "."



def check_required_artifacts(root: Path, required, violations: list):
    for entry in required:
        name = entry["name"]
        artifact_path = root / name
        if not artifact_path.exists():
            violations.append(
                {
                    "artifact": format_artifact_path(artifact_path, root),
                    "line": entry["line"],
                    "requirement": REQUIRED_ARTIFACTS_REQUIREMENT,
                    "details": f"Required artifact '{name}' is missing.",
                }
            )


def scan_directories(root: Path, violations: list):
    aggregated_terms = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        dirnames.sort()
        path = Path(dirpath).resolve()
        if path == root:
            parent_terms = set()
        else:
            parent_terms = aggregated_terms.get(path.parent, set())
        missing = [name for name in TRIAD_FILES if name not in filenames]
        if missing:
            violations.append(
                {
                    "artifact": format_artifact_path(path, root),
                    "line": 136,
                    "requirement": TRIAD_REQUIREMENT,
                    "details": f"Directory is missing triad files: {', '.join(missing)}.",
                }
            )
        vocab_path = path / "VOCABULARY.md"
        terms = parse_vocab_terms(vocab_path)
        aggregated = parent_terms.union(terms.keys())
        aggregated_terms[path] = aggregated
        for doc in ("CANON.md", "README.md"):
            doc_path = path / doc
            if doc_path.exists():
                doc_path.read_text(encoding="utf-8")
    return aggregated_terms


def print_report(violations: list):
    status = "compliant" if not violations else "invalid"
    print("COMPLIANCE REPORT")
    print(f"Status: {status}")
    print(f"Violations: {len(violations)}")
    if violations:
        print()
        for index, violation in enumerate(violations, start=1):
            print(f"{index}. Artifact: {violation['artifact']}")
            if violation.get("line"):
                print(f"   Line: {violation['line']}")
            print(f"   Requirement: {violation['requirement']}")
            print(f"   Details: {violation['details']}")
            print()


def main():
    root = Path(__file__).resolve().parents[2]
    violations = []
    canon_path = root / "CANON.md"
    required_artifacts = parse_required_artifacts(canon_path)
    check_required_artifacts(root, required_artifacts, violations)
    scan_directories(root, violations)
    validate_user_guide_fsm(root, violations)
    print_report(violations)
    sys.exit(1 if violations else 0)


if __name__ == "__main__":
    main()
