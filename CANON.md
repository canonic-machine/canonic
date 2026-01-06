
# CANON (canonic-programming/)

**Inherits from:** None

## Invariants

### Triad requirement
**All directories must contain the triad:**
- CANON.md
- VOCABULARY.md
- README.md

**Violation:** Directory missing any triad file

### Terminology discipline
**All technical terms must be defined in VOCABULARY.md (same directory or inherited).**

**Violation:** Using undefined terms in governed artifacts

### Validation gates
**All artifacts must pass validation before acceptance.**

**Violation:** Accepting invalid artifacts

### Traceability
**All derived content must trace to source material.**

**Violation:** Invented content without documented origin

### Reference integrity
**All references must resolve.**

**Violation:** Broken reference to non-existent artifact

### Specification file naming
**Repository specification files must be named <REPO>.md.**

**Violation:** Specification file does not match repository name

### Canon optimization
**CANON.md files must be kept lean and optimized: no explanatory content, redundant constraints, or bloat.**

**Violation:** CANON contains non-constraint content, duplication, or unnecessary verbosity

### Self-sustaining governance
**CANONIC systems must exhibit self-* properties: self-optimizing, self-healing, self-documenting, self-validating.**

**Violation:** System lacks required self-* governance properties

---

End of root CANON.
