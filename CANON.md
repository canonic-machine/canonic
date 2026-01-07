
# CANON (canonic-programming/)

**Inherits from:** None

## Core Invariants

### Triad requirement
**All governed directories must contain the minimal triad: CANON.md, DICTIONARY.md, README.md.**

**DICTIONARY.md must contain alphabetically ordered term definitions.**

**Violation:** Directory missing any triad file, or DICTIONARY.md terms not alphabetically ordered

### Implementation inheritance
**Implementation repositories inherit from protocol specifications via markdown links.**

**Violation:** Implementation claims to inherit from non-existent files

### Examples requirement
**Governance repositories must include examples directory demonstrating the paradigm.**

**Violation:** Governance repository missing examples directory

### Abstraction layers
**CANONIC implementations must separate paradigm, validation engine, and domain applications.**

**Three-layer architecture:**
- **CANONIC** (paradigm layer): Defines constraints, validation, inheritance, triad
- **MACHINE** (validation engine layer): Implements constraint checking, git-FSM, self-* properties
- **Domain applications** (application layer): Inherit from MACHINE, add domain-specific patterns

**Violation:** Validation engine contains domain-specific patterns, or domain application reimplements validation logic
