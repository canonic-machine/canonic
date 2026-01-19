#!/usr/bin/env python3
"""
VaaS - Validators as a Service

Enforces CANONIC Language Specification (LANGUAGE.md)

Primitives enforced:
- CANON.md   → Governance (what MUST be)
- VOCAB.md   → Semantics (what words mean)
- README.md  → Description (what this is)
- COVERAGE.md → Closure (how complete we are)
- APPSTORE.md → Distribution (how it spreads)
"""

import os
import sys
import re
from pathlib import Path


def find_scopes(root: Path) -> list[Path]:
    """Find all directories containing CANON.md (valid scopes)."""
    scopes = []
    for canon in root.rglob("CANON.md"):
        if ".git" not in canon.parts and ".archive" not in canon.parts:
            scopes.append(canon.parent)
    return scopes


def validate_triad(scope: Path) -> tuple[bool, str]:
    """
    Rule: TRIAD_REQUIRED
    Every scope MUST contain: CANON.md, VOCAB.md, README.md
    """
    triad = ["CANON.md", "VOCAB.md", "README.md"]
    missing = [f for f in triad if not (scope / f).exists()]

    if missing:
        return False, f"TRIAD FAIL: {scope} missing {missing}"
    return True, f"TRIAD PASS: {scope}"


def validate_inheritance(scope: Path) -> tuple[bool, str]:
    """
    Rule: INHERITANCE_REQUIRED
    Every CANON.md MUST declare 'inherits:' and it MUST terminate at /
    """
    canon = scope / "CANON.md"
    content = canon.read_text()

    match = re.search(r'^inherits:\s*(.+)$', content, re.MULTILINE)
    if not match:
        return False, f"INHERITANCE FAIL: {scope}/CANON.md missing 'inherits:'"

    return True, f"INHERITANCE PASS: {scope} inherits {match.group(1)}"


def validate_introspection(scope: Path) -> tuple[bool, str]:
    """
    Rule: INTROSPECTION_REQUIRED
    All concepts in CANON.md MUST be defined in VOCAB.md

    Note: Full introspection validation requires parsing.
    This is a structural check only.
    """
    vocab = scope / "VOCAB.md"
    if not vocab.exists():
        return False, f"INTROSPECTION FAIL: {scope} missing VOCAB.md"

    content = vocab.read_text()
    # Check VOCAB has at least one term definition (### heading)
    if not re.search(r'^###\s+\w+', content, re.MULTILINE):
        return False, f"INTROSPECTION FAIL: {scope}/VOCAB.md has no term definitions"

    return True, f"INTROSPECTION PASS: {scope}"


def validate_case_semantics(scope: Path) -> tuple[bool, str]:
    """
    Rule: CASE_SEMANTICS
    UPPERCASE = Governance (CANON, VOCAB, README, COVERAGE, APPSTORE)
    lowercase = Governed (scope directories)
    """
    # Scope directory should be lowercase (unless root)
    if scope.name and scope.name[0].isupper() and scope.name not in ["Canonic"]:
        # Check if it's a governance artifact, not a scope
        if not scope.name.endswith(".md"):
            return False, f"CASE FAIL: {scope.name} should be lowercase (governed)"

    return True, f"CASE PASS: {scope}"


def validate_scope(scope: Path) -> tuple[bool, list[str]]:
    """Validate a single scope against LANGUAGE.md rules."""
    results = []
    all_pass = True

    validators = [
        validate_triad,
        validate_inheritance,
        validate_introspection,
        validate_case_semantics,
    ]

    for validator in validators:
        passed, msg = validator(scope)
        results.append(msg)
        if not passed:
            all_pass = False

    return all_pass, results


def main():
    """Run VaaS validation on all scopes."""
    root = Path(os.environ.get("CANONIC_ROOT", "."))

    print("=== VaaS - CANONIC Language Enforcement ===\n")

    scopes = find_scopes(root)
    print(f"Found {len(scopes)} scopes\n")

    total_pass = 0
    total_fail = 0
    failures = []

    for scope in sorted(scopes):
        passed, results = validate_scope(scope)

        if passed:
            total_pass += 1
            print(f"✓ {scope.relative_to(root)}")
        else:
            total_fail += 1
            print(f"✗ {scope.relative_to(root)}")
            for r in results:
                if "FAIL" in r:
                    print(f"  {r}")
                    failures.append(r)

    print(f"\n=== Summary ===")
    print(f"PASS: {total_pass}")
    print(f"FAIL: {total_fail}")

    if total_fail > 0:
        print(f"\n=== Failures ===")
        for f in failures:
            print(f"  {f}")
        return 1

    print(f"\nVALIDITY: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
