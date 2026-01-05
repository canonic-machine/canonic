# CANON (canonic-programming/tools/)

**Governance for validation tooling.**

Inherits: canonic-programming/ → tools/

---

## Purpose

This directory contains core validation tools that enforce CANONIC programming paradigm constraints.

These tools implement syntactic validation: checking structural compliance, file existence, naming conventions, and reference resolution.

---

## Required Artifacts

### validation/
Core syntactic validation engine that checks artifacts against CANON constraints.

Must contain:
- Triad (CANON.md, VOCABULARY.md, README.md)
- Implementation files (Python scripts)
- Test files

---

## Tool Constraints

### Implementation requirements

- Language: Python 3.7+
- Dependencies: Minimal (avoid heavy frameworks)
- Output: Machine-readable (for CI/CD integration)
- Exit codes: 0 (success), 1 (failure), 130 (user interrupt)

### Validation behavior

- Accept `--root` parameter to override auto-detection
- Report violations with: artifact path, line number, requirement reference, details
- Support both single-file and directory validation
- Fail fast on critical errors, collect all violations otherwise

### Output format

```
COMPLIANCE REPORT
Status: [compliant|invalid]
Violations: N

1. Artifact: path/to/file
   Line: N
   Requirement: CANON.md:X-Y (description)
   Details: Specific violation description
```

---

## Invariants

### Tool stability

- Tools must not modify artifacts (read-only)
- Tools must be deterministic (same input → same output)
- Tools must handle missing files gracefully
- Tools must validate themselves (dogfooding)

### Portability

- Tools work across platforms (macOS, Linux, Windows)
- Tools require no installation beyond Python stdlib (for core features)
- Tools provide clear error messages
- Tools document their own CANON constraints

---

## Forbidden

- Tools that modify artifacts during validation
- Tools that require external services for basic checks
- Tools with hidden side effects
- Tools that bypass CANON constraints

---

End of tools CANON.
