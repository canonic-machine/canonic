# CANON (tools/validation/)

**Inherits from:** canonic-programming/tools/

## Invariants

### Validation scope
**Tool must inspect triad (CANON.md, VOCABULARY.md, README.md) for every directory.**

**Violation:** Tool fails to check required governance files

### Violation reporting
**Tool must report violations with CANON reference, artifact path, line number, and details.**

**Violation:** Tool output missing required violation information

### Tool validation
**Tool must validate itself against its own CANON constraints.**

**Violation:** Tool violates its own governance requirements

---

End of validation CANON.
