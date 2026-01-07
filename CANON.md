
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
