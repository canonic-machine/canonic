# Tools

**Validation tooling for CANONIC programming.**

This directory contains core validation tools that enforce paradigm constraints.

---

## What's Here

### validation/
Core syntactic validation engine. Checks:
- Triad presence (CANON.md, VOCABULARY.md, README.md)
- File naming conventions
- Reference resolution
- Structural compliance

See [validation/README.md](validation/README.md) for usage.

---

## Quick Start

**Validate a directory:**
```bash
python3 validation/run_validation.py /path/to/directory
```

**Validate from current directory:**
```bash
python3 validation/run_validation.py .
```

**Get help:**
```bash
python3 validation/run_validation.py --help
```

---

## Tool Philosophy

CANONIC validation tools are:

**Read-only** — Never modify artifacts during validation

**Deterministic** — Same input always produces same output

**Minimal** — Depend only on Python stdlib for core features

**Portable** — Work across macOS, Linux, Windows

**Self-validating** — Tools validate their own compliance

---

## Adding New Tools

When creating new validation tools:

1. Create subdirectory with triad (CANON, VOCABULARY, README)
2. Document constraints in CANON.md
3. Define new terms in VOCABULARY.md
4. Implement in Python 3.7+
5. Follow output format conventions
6. Test across platforms

---

## Output Format

All validation tools use consistent reporting:

```
COMPLIANCE REPORT
Status: compliant|invalid
Violations: N

1. Artifact: path/to/file
   Line: N
   Requirement: CANON.md:X-Y (description)
   Details: Specific violation
```

This format enables:
- CI/CD integration
- Automated processing
- Clear human reading

---

## Exit Codes

- `0` — Validation passed (compliant)
- `1` — Validation failed (violations found)
- `130` — User interrupted (Ctrl+C)

---

End of tools README.
