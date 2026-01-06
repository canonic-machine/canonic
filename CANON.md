
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
**Pure governance repositories contain only: repository specification file, CANON.md, VOCABULARY.md, README.md, and examples.**

**Repository specification files:**
- Named after repository: `<REPO>.md` (e.g., `CANONIC.md` for canonic repository)
- Define the paradigm/specification being governed

**Violation:** Repository contains executable code, tools, or implementation-specific references

## Semantic Constraints

### Terminology discipline
**All technical terms must be defined in VOCABULARY.md (same directory or inherited).**

**Violation:** Using undefined terms in governed artifacts

### Reference integrity
**All references must resolve to existing artifacts.**

**Violation:** Broken reference to non-existent artifact

### Artifact naming
**CANONIC files use UPPERCASE base names with lowercase .md extensions to indicate human-readable plain English artifacts.**

**Naming conventions:**
- Base filename: UPPERCASE (indicates CANON artifact in plain English)
- Extension: lowercase (.md)
- Examples: `CANON.md`, `CANONIC.md`, `README.md`, `MACHINE.md`

**Violation:** File uses lowercase base name or uppercase extension in CANONIC repository

## Introspective Properties

### Self-validating
**Systems must implement dual validation: syntactic (structure) + semantic (constraints).**

**Violation:** Missing validation layer

### Self-optimizing
**CANON.md files must be kept lean: no explanatory content, redundant constraints, or bloat.**

**Violation:** CANON contains non-constraint content, duplication, or unnecessary verbosity

### Self-healing
**Systems must detect violations through git history patterns and trigger validation.**

**Git commits ARE FSM state transitions:**
- Each commit proposes a state transition
- Pre-commit validation acts as gate (accept/reject)
- Rejected commits trigger backflow to source state
- Git history records the complete FSM transition log
- Commits must be atomic: one logical change, one constraint addressed
- Multiple unrelated changes must be separate commits

**Git violation signals:**
- Commit → Revert → Reapply pattern indicates failed validation attempt
- Rapid commit cycles on CANON files indicate drift
- Fix/violation keywords in commit messages indicate constraint failures

**Response:** Trigger comprehensive validation and require human approval before allowing transition

**Violation:** Git history shows violation patterns but validation was not triggered

### Atomic commits
**Each commit must address exactly one logical change or constraint.**

**Atomic commit requirements:**
- Single concern: One fix, one feature, one constraint update
- Self-contained: Includes all necessary changes for that concern
- Independently revertible: Can be undone without breaking other changes
- Clear commit message: Describes the single logical change

**Violation:** Commit mixes multiple unrelated changes (e.g., fixing CANON.md + updating README.md + adding new constraint)

## Protocol References

### Documentation protocol
**README.md automatically generated from CANON.md + VOCABULARY.md constraints.**

### Mermaid governance protocol
**Diagrams use consistent Mermaid styling for professional appearance.**

### Validation protocol
**Systems implement dual validation: syntactic (structure) + semantic (constraints).**
