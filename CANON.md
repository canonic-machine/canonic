
# CANON (canonic-programming/)

**Inherits from:** None

## Core Invariants

### Triad requirement
**All governed directories must contain the triad: CANON.md, VOCABULARY.md, README.md.**

**Violation:** Directory missing any triad file

### Validation gates
**All artifacts must pass validation before acceptance.**

**Violation:** Accepting invalid artifacts

### Traceability
**All derived content must trace to source material.**

**Violation:** Invented content without documented origin

### Governance purity
**Pure governance repositories contain only: CANON.md, VOCABULARY.md, README.md, and examples.**

**Violation:** Repository contains executable code, tools, or implementation-specific references

## Semantic Constraints

### Terminology discipline
**All technical terms must be defined in VOCABULARY.md (same directory or inherited).**

**Violation:** Using undefined terms in governed artifacts

### Reference integrity
**All references must resolve to existing artifacts.**

**Violation:** Broken reference to non-existent artifact

### Artifact naming
**Repository and artifact names use lowercase with hyphens for multi-word names.**

**Naming conventions:**
- Repositories: lowercase (e.g., `canonic`, `machine`)
- Artifacts: lowercase with hyphens (e.g., `hello-world`, `user-guide`)
- Triad files: exact case (CANON.md, VOCABULARY.md, README.md)

**Violation:** Artifact uses uppercase, underscores, or incorrect case

## Introspective Properties

### Self-validating
**Systems must implement dual validation: syntactic (structure) + semantic (constraints).**

**Violation:** Missing validation layer

### Self-optimizing
**CANON.md files must be kept lean: no explanatory content, redundant constraints, or bloat.**

**Violation:** CANON contains non-constraint content, duplication, or unnecessary verbosity

## Protocol References

**All protocols defined in:** ../machine/PROTOCOLS.md

### Documentation protocol
**README.md automatically generated from CANON.md + VOCABULARY.md constraints.**

### Mermaid governance protocol
**Diagrams use consistent Mermaid styling for professional appearance.**

### Validation protocol
**Systems implement dual validation: syntactic (structure) + semantic (constraints).**
