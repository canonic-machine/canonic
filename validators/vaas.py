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
import subprocess
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

    inherits = match.group(1).strip()
    if not inherits.startswith('/'):
        return False, f"INHERITANCE FAIL: {scope}/CANON.md inherits path must be absolute"

    if inherits != '/' and not inherits.endswith('/'):
        return False, f"INHERITANCE FAIL: {scope}/CANON.md inherits must terminate with '/'"

    return True, f"INHERITANCE PASS: {scope} inherits {inherits}"


TERM_HEADING_RE = re.compile(r'^###\s+(.+)$', re.MULTILINE)
ALT_HEADING_RE = re.compile(r'^##\s+(.+)$', re.MULTILINE)
CANON_HEADING_RE = re.compile(r'^###\s+(.+)$', re.MULTILINE)
BACKTICK_RE = re.compile(r'`([^`]+)`')

SECTION_HEADINGS = {
    'content concepts', 'terms', 'grammar concepts', 'semantic primitives',
    'language constructs', 'core concepts', 'test concepts',
}


def _normalize(term: str) -> str:
    return ' '.join(term.strip().lower().split())


def _extract_vocab_terms(path: Path) -> set[str]:
    if not path.exists():
        return set()
    text = path.read_text()
    terms = {_normalize(m.group(1)) for m in TERM_HEADING_RE.finditer(text)}
    if terms:
        return terms
    # Fallback for legacy VOCAB files using ## headings.
    terms = set()
    for match in ALT_HEADING_RE.finditer(text):
        heading = _normalize(match.group(1))
        if heading in SECTION_HEADINGS:
            continue
        terms.add(heading)
    return terms


def _extract_used_concepts(path: Path) -> set[str]:
    if not path.exists():
        return set()
    text = path.read_text()
    concepts = set()
    for match in CANON_HEADING_RE.finditer(text):
        heading = re.sub(r'^\s*\d+\.\s*', '', match.group(1)).strip()
        if heading:
            concepts.add(_normalize(heading))
    for match in BACKTICK_RE.finditer(text):
        token = match.group(1).strip()
        if '/' in token or '{' in token or '}' in token or '|' in token:
            continue
        if token.endswith('.md'):
            token = token[:-3]
        if re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]*', token):
            concepts.add(_normalize(token))
    return concepts


def validate_introspection(scope: Path) -> tuple[bool, str]:
    """
    Rule: INTROSPECTION_REQUIRED
    All concepts in CANON.md MUST be defined in VOCAB.md
    """
    vocab = scope / "VOCAB.md"
    canon = scope / "CANON.md"
    if not vocab.exists():
        return False, f"INTROSPECTION FAIL: {scope} missing VOCAB.md"

    terms = _extract_vocab_terms(vocab)
    if not terms:
        return False, f"INTROSPECTION FAIL: {scope}/VOCAB.md has no term definitions"

    used = _extract_used_concepts(canon)
    undefined = used - terms
    if undefined:
        return False, f"INTROSPECTION FAIL: {scope} undefined concepts {sorted(undefined)}"

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


# =============================================================================
# PART-OF-SPEECH VALIDATION (LANGUAGE.md Section 5.2.2)
# =============================================================================

# Known nouns (templates/artifacts)
KNOWN_NOUNS = {
    # Primitives
    "canon", "vocab", "readme", "coverage", "appstore", "ledger",
    # Products
    "paper", "book", "grant", "patent", "disclosure",
    # Infrastructure
    "machine", "os", "token", "coin", "company", "foundation",
    # Extensions
    "validator", "template", "service", "product",
}

# Known verbs (process scopes)
KNOWN_VERBS = {
    "writing", "publishing", "protection", "distribution",
    "validation", "compilation", "economics",
}

# Reserved structural names
RESERVED_NAMES = {
    "services", "products", "validators", "templates",
    "applications", "disclosures", "episodes",
}


def is_plural(name: str) -> bool:
    """Check if a name is plural (ends with 's')."""
    return name.endswith("s") and len(name) > 1


def get_singular(name: str) -> str:
    """Get singular form of a plural name."""
    if name.endswith("ies"):
        return name[:-3] + "y"
    elif name.endswith("es"):
        return name[:-2]
    elif name.endswith("s"):
        return name[:-1]
    return name


def validate_scope_name_pos(scope: Path) -> tuple[bool, str]:
    """
    Rule: POS_NOUN, POS_VERB
    Scope names MUST be nouns or verbs (gerunds).

    LANGUAGE.md Section 5.2.2
    """
    name = scope.name.lower()

    # Skip root and special directories
    if not name or name in [".", ".."]:
        return True, f"POS PASS: {scope} (root)"

    # Check if it's a known noun
    if name in KNOWN_NOUNS:
        return True, f"POS PASS: {scope} (noun)"

    # Check if it's a known verb
    if name in KNOWN_VERBS:
        return True, f"POS PASS: {scope} (verb/gerund)"

    # Check if it's a reserved structural name
    if name in RESERVED_NAMES:
        return True, f"POS PASS: {scope} (reserved)"

    # Check if it's a plural of a known noun
    if is_plural(name):
        singular = get_singular(name)
        if singular in KNOWN_NOUNS:
            return True, f"POS PASS: {scope} (plural of {singular})"

    # Check if it's a version directory (v1, v2, etc.)
    if re.match(r'^v\d+$', name):
        return True, f"POS PASS: {scope} (version)"

    # Domain-specific names are allowed (they inherit from templates)
    # e.g., mammochat, genomics, atulisms, dividends
    # These are instance names, not governed by POS rules
    return True, f"POS PASS: {scope} (instance name)"


def validate_plural_inheritance(scope: Path, root: Path) -> tuple[bool, str]:
    """
    Rule: SINGULAR_PLURAL_BIJECTION
    Plural scopes MUST contain instances that inherit from the singular template.

    LANGUAGE.md Section 5.2.3
    """
    name = scope.name.lower()

    # Only check plural scope directories
    if not is_plural(name):
        return True, f"BIJECTION PASS: {scope} (not plural)"

    # Skip reserved names like "services", "validators"
    if name in RESERVED_NAMES:
        return True, f"BIJECTION PASS: {scope} (reserved)"

    singular = get_singular(name)

    # Check if instances in this collection have CANON.md with inherits
    instances_checked = 0
    instances_valid = 0

    for item in scope.iterdir():
        if item.is_dir() and not item.name.startswith("."):
            canon = item / "CANON.md"
            if canon.exists():
                instances_checked += 1
                content = canon.read_text()
                # Check if it inherits from the singular template
                if re.search(rf'{singular}', content, re.IGNORECASE):
                    instances_valid += 1

    if instances_checked == 0:
        # No instances yet, that's OK
        return True, f"BIJECTION PASS: {scope} (no instances)"

    if instances_valid < instances_checked:
        return False, f"BIJECTION FAIL: {scope} has {instances_checked - instances_valid} instances not inheriting from {singular}"

    return True, f"BIJECTION PASS: {scope} ({instances_valid}/{instances_checked} inherit {singular})"


def validate_scope(scope: Path, root: Path = None) -> tuple[bool, list[str]]:
    """Validate a single scope against LANGUAGE.md rules."""
    results = []
    all_pass = True

    # Basic validators
    basic_validators = [
        validate_triad,
        validate_inheritance,
        validate_introspection,
        validate_case_semantics,
        validate_scope_name_pos,
    ]

    for validator in basic_validators:
        passed, msg = validator(scope)
        results.append(msg)
        if not passed:
            all_pass = False

    # Validators that need root context
    if root:
        passed, msg = validate_plural_inheritance(scope, root)
        results.append(msg)
        if not passed:
            all_pass = False

    return all_pass, results


def validate_identifier(name: str) -> tuple[bool, str]:
    """
    Rule: SINGLE_WORD
    All identifiers MUST be single words (no hyphens, underscores, or spaces).

    LANGUAGE.md Section 5.2.1:
    ValidIdentifier ::= Letter (Letter | Digit)*
    """
    if not re.fullmatch(r'[A-Za-z][A-Za-z0-9]*', name):
        return False, f"IDENTIFIER FAIL: '{name}' violates ValidIdentifier"
    return True, f"IDENTIFIER PASS: '{name}'"


def validate_repo_name(root: Path) -> tuple[bool, str]:
    """
    Rule: REPO_NAMING
    Repository names follow scope naming rules.

    LANGUAGE.md Section 5.5.2:
    VALID:   canonic, validators, paper, patents
    INVALID: canonic-services (hyphen)
    """
    repo_name = root.resolve().name
    return validate_identifier(repo_name)


# =============================================================================
# GARBAGE COLLECTION (OS = GIT)
# =============================================================================

# Allowed file patterns in a governed scope
ALLOWED_PATTERNS = {
    # Governance primitives (UPPERCASE.md)
    r'^[A-Z]+\.md$',
    # Scope spec (lowercase.md matching directory name)
    r'^[a-z]+\.md$',
    # License files
    r'^LICENSE$', r'^NOTICE$',
    # Git
    r'^\.git$', r'^\.gitignore$', r'^\.gitattributes$',
    # Archive (hidden)
    r'^\.archive$',
    # Generated artifacts (regenerable from source)
    r'^.*\.pdf$',
    # Assets directory
    r'^assets$',
    # Build configs
    r'^Makefile$', r'^\.github$',
}

# Directories that should not exist (garbage)
GARBAGE_DIRS = {
    'output', 'build', 'dist', 'tmp', 'temp', '__pycache__',
    'node_modules', '.cache', '.vscode', '.idea',
}

# File patterns that are always garbage
GARBAGE_PATTERNS = [
    r'.*\.pyc$',
    r'.*\.pyo$',
    r'.*~$',
    r'^\.DS_Store$',
    r'^Thumbs\.db$',
    r'.*\.swp$',
    r'.*\.swo$',
]


def is_garbage_file(name: str) -> bool:
    """Check if a file matches garbage patterns."""
    for pattern in GARBAGE_PATTERNS:
        if re.match(pattern, name):
            return True
    return False


def is_allowed_file(name: str, scope_name: str) -> bool:
    """Check if a file is allowed in a governed scope."""
    for pattern in ALLOWED_PATTERNS:
        if re.match(pattern, name):
            return True
    # Allow scope-specific spec file (e.g., paper.md in paper/)
    if name == f"{scope_name.lower()}.md":
        return True
    return False


def validate_gc(root: Path) -> tuple[bool, list[str]]:
    """
    Rule: OS_IS_GIT
    Everything derives from the ledger. If git can regenerate it, it's garbage.

    Checks:
    1. No untracked files outside .archive/
    2. No garbage directories (output/, build/, etc.)
    3. No garbage files (.DS_Store, *.pyc, etc.)
    """
    garbage = []

    # Check for untracked files when git is available
    git_dir = root / ".git"
    if git_dir.exists():
        try:
            result = subprocess.run(
                ["git", "status", "--porcelain", "--untracked-files=normal"],
                cwd=root,
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                for line in result.stdout.splitlines():
                    if line.startswith("?? "):
                        rel = line[3:]
                        if rel.startswith(".archive/"):
                            continue
                        garbage.append(f"GC: {rel} (untracked)")
        except FileNotFoundError:
            pass

    # Walk the tree
    for item in root.rglob("*"):
        # Skip .git and .archive
        if ".git" in item.parts or ".archive" in item.parts:
            continue

        name = item.name

        # Check for garbage directories
        if item.is_dir() and name in GARBAGE_DIRS:
            garbage.append(f"GC: {item.relative_to(root)} (garbage directory)")
            continue

        # Check for garbage files
        if item.is_file() and is_garbage_file(name):
            garbage.append(f"GC: {item.relative_to(root)} (garbage file)")
            continue

    if garbage:
        return False, garbage
    return True, ["GC PASS: No garbage detected"]


def gc_clean(root: Path, dry_run: bool = True) -> list[str]:
    """
    Clean garbage from the repository.

    dry_run=True: Report what would be deleted
    dry_run=False: Actually delete garbage
    """
    import shutil

    cleaned = []

    for item in root.rglob("*"):
        if ".git" in item.parts or ".archive" in item.parts:
            continue

        name = item.name
        should_clean = False

        if item.is_dir() and name in GARBAGE_DIRS:
            should_clean = True
        elif item.is_file() and is_garbage_file(name):
            should_clean = True

        if should_clean:
            rel_path = item.relative_to(root)
            if dry_run:
                cleaned.append(f"Would remove: {rel_path}")
            else:
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()
                cleaned.append(f"Removed: {rel_path}")

    return cleaned


def main():
    """Run VaaS validation on all scopes."""
    import argparse

    parser = argparse.ArgumentParser(description="VaaS - CANONIC Language Enforcement")
    parser.add_argument("--gc", action="store_true", help="Run garbage collection check")
    parser.add_argument("--gc-clean", action="store_true", help="Clean garbage (dry-run)")
    parser.add_argument("--gc-clean-force", action="store_true", help="Clean garbage (actually delete)")
    parser.add_argument("path", nargs="?", default=".", help="Root path to validate")
    args = parser.parse_args()

    root = Path(args.path if args.path != "." else os.environ.get("CANONIC_ROOT", "."))

    print("=== VaaS - CANONIC Language Enforcement ===\n")

    # GC mode
    if args.gc_clean or args.gc_clean_force:
        print("=== Garbage Collection ===\n")
        dry_run = not args.gc_clean_force
        cleaned = gc_clean(root, dry_run=dry_run)
        if cleaned:
            for item in cleaned:
                print(f"  {item}")
            print(f"\n{'Would clean' if dry_run else 'Cleaned'}: {len(cleaned)} items")
        else:
            print("  No garbage found")
        return 0

    # First: validate repo name itself
    repo_valid, repo_msg = validate_repo_name(root)
    if not repo_valid:
        print(f"✗ REPO NAME VIOLATION")
        print(f"  {repo_msg}")
        print(f"\n=== Summary ===")
        print(f"PASS: 0")
        print(f"FAIL: 1")
        print(f"\n=== Failures ===")
        print(f"  {repo_msg}")
        print(f"\nREPO NAME MUST comply with LANGUAGE.md")
        print(f"Rename directory to remove hyphens/underscores.")
        return 1

    print(f"✓ Repo name: {root.resolve().name}\n")

    scopes = find_scopes(root)
    print(f"Found {len(scopes)} scopes\n")

    total_pass = 0
    total_fail = 0
    failures = []

    for scope in sorted(scopes):
        passed, results = validate_scope(scope, root)

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

    # GC check (if requested)
    gc_pass = True
    gc_failures = []
    if args.gc:
        print(f"\n=== Garbage Collection ===")
        gc_pass, gc_results = validate_gc(root)
        for r in gc_results:
            print(f"  {r}")
            if "GC:" in r:
                gc_failures.append(r)

    print(f"\n=== Summary ===")
    print(f"PASS: {total_pass}")
    print(f"FAIL: {total_fail}")
    if args.gc:
        print(f"GC: {'PASS' if gc_pass else 'FAIL'}")

    if total_fail > 0 or not gc_pass:
        print(f"\n=== Failures ===")
        for f in failures:
            print(f"  {f}")
        for f in gc_failures:
            print(f"  {f}")
        return 1

    print(f"\nVALIDITY: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
