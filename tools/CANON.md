# CANON (canonic-programming/tools/)

**Inherits from:** canonic-programming/

## Invariants

### Required artifacts
**Directory must contain validation/ with:**
- CANON.md, VOCABULARY.md, README.md
- Python implementation files
- Test files

**Violation:** Missing required validation components

### Tool constraints
**Tools must:**
- Use Python 3.7+ with minimal dependencies
- Be read-only (not modify artifacts)
- Be deterministic (same input → same output)
- Work across platforms without installation
- Accept `--root` parameter for path override

**Violation:** Tool violates implementation or behavior requirements

### Validation output
**Tools must report:**
- Status: compliant or invalid
- Violation count
- Artifact path, line number, requirement reference, details

**Violation:** Tool output does not match required format

---

End of tools CANON.
