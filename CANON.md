
# CANON (canonic-programming/)

**Inherits from:** None

## Paradigm Definition

### Programming governance
**CANONIC programming is programming governance itself, not artifacts.**

**The paradigm:**
- Traditional programming: write instructions → toolchain executes
- CANONIC programming: write constraints → validation enforces
- You program what must be true, not how to make it true
- CANONs are the program; artifacts are the output

**Power of CANONIC:**
- Governance is declarative and portable across LLMs/tools
- Validation cost decreases over time (convergence to syntactic)
- System becomes more durable as constraints accumulate
- AI focuses on genuinely complex tasks, not repetitive validation

**Violation:** Treating CANONIC as documentation instead of executable governance

## Core Invariants

### Triad requirement
**All governed directories must contain the triad: CANON.md, VOCABULARY.md, README.md.**

**Violation:** Directory missing any triad file

### File naming convention
**Governance markdown files use single-word UPPERCASE names.**

**Naming pattern:**
- Repository specification: `<REPO>.md` (e.g., CANONIC.md, MACHINE.md)
- Core governance files: CANON.md, VOCABULARY.md, README.md
- Domain files: AGENTS.md, PATTERNS.md, PROTOCOLS.md, LEARNINGS.md
- Use single words, not compound names with underscores or hyphens
- UPPERCASE for consistency and discoverability

**Stack ordering for implementation repositories:**
- Implementation repositories MAY use numeric prefixes to show architectural stack
- Prefix format: `NN-FILENAME.md` where NN is zero-padded (00, 01, 02, etc.)
- Canonical stack order: 00-CANON (truth) → 01-VOCABULARY (language) → 02-<SPEC> (architecture) → subsequent layers defined by spec
- Pure governance repositories (canonic/) use unprefixed names
- Stack ordering makes dependency layers immediately visible in directory listings

**Violation:** Governance file uses multi-word name (e.g., SESSION_LEARNINGS.md instead of LEARNINGS.md), non-uppercase name, or violates spec-defined stack ordering

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

**Tool placement:**
- Governance repositories: No executable tools (pure governance)
- Implementation repositories: Canonical tool implementations
- Consumer repositories: May implement own tools that consume governance

**Violation:** Repository contains executable code, tools, session state, or implementation-specific references

### Implementation inheritance
**Implementation repositories inherit from protocol specifications (CANONIC.md, CANON.md), not from non-existent implementation files in governance repositories.**

**Violation:** Implementation claims to inherit from non-existent files in governance repository (e.g., `canonic/AGENTS.md`)

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

**Validator requirement:**
- Validation tools must validate themselves before validating other artifacts
- If validator violates CANON, it must fail with error before running checks
- Self-validation proves validator complies with governance it enforces

**Violation:** Missing validation layer or validator doesn't self-validate

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

### Introspection requirement
**Sessions must capture learnings that trigger producer commits.**

**Introspection cycle:**
- Work reveals gaps in validation or constraints
- Introspection asks: "Why wasn't this caught?"
- Learning captured in session artifacts
- Learning canonified into constraints (producer commit)
- System becomes stronger each cycle

**Pattern discovery requirement:**
- Git history analysis must identify meta-patterns
- Session boundaries reveal canonification clusters
- Backflow patterns indicate self-healing events
- Terminology drift triggers convergence opportunities
- Burst enforcement patterns signal constraint adoption
- Meta-patterns themselves must be canonified

**Introspection depth levels:**
- Level 1: Fix violations in work artifacts
- Level 2: Fix gaps in validation tools
- Level 3: Fix architectural violations in validators themselves
- Continue introspection until root cause found and canonified

**Pattern:** Introspection → Learning → Canonification → Meta-Pattern Discovery → Recursive Strengthening

**Violation:** System operates without capturing learnings for canonification, fails to identify and canonify meta-patterns from git history, or stops introspection before reaching root cause

### Atomic commits
**Each commit must address exactly one logical change or constraint.**

**Atomic commit requirements:**
- Single concern: One fix, one feature, one constraint update
- Self-contained: Includes all necessary changes for that concern
- Independently revertible: Can be undone without breaking other changes
- Clear commit message: Describes the single logical change

**Violation:** Commit mixes multiple unrelated changes (e.g., fixing CANON.md + updating README.md + adding new constraint)

### CANON production vs consumption
**Git commits signal whether work produces or consumes CANON.**

**Producer commits (canonification):**
- Add new constraints to CANON.md
- Extract patterns into protocols
- Capture discovered violations
- Message pattern: "Canonify [what was learned]"
- These commits strengthen governance

**Consumer commits (implementation):**
- Apply existing CANON constraints
- Fix violations detected by validation
- Generate artifacts per CANON rules
- Message pattern: "Apply [constraint]" or "Fix [violation]"
- These commits follow governance

**Feedback signal:**
- Producer commits → system learned something new
- Consumer commits → system enforced existing rules
- Git history shows learning curve (producer → consumer ratio decreases over time)
- Mature systems have few producers, many consumers

**Maturity thresholds:**
- New system: >40% producer commits (rapid learning phase)
- Maturing system: 10-30% producer commits (refinement phase)
- Mature system: <10% producer commits (stable enforcement)

**Violation:** Commit message doesn't indicate producer vs consumer action

## Protocol References

### Documentation protocol
**README.md automatically generated from CANON.md + VOCABULARY.md constraints.**

**Violation:** README generated without incorporating CANON.md + VOCABULARY.md content

### Mermaid governance protocol
**Diagrams use consistent Mermaid styling for professional appearance.**

**Violation:** Diagrams violate Mermaid governance standards

### Validation protocol
**Systems implement dual validation: syntactic (structure) + semantic (constraints).**

**Validation precedence:**
- Syntactic validation is preferred over semantic validation
- Syntactic validation is free (structural checks)
- Semantic validation is expensive (LLM token cost)
- CANONs must converge: semantic violations become syntactic constraints over time
- This shifts validation cost from expensive LLM to free syntax checking
- This fine-tunes AI focus to genuinely complex tasks

**Convergence pattern:**
1. Semantic validator detects violation (expensive)
2. Violation gets canonified as syntactic constraint (one-time cost)
3. Future violations caught syntactically (free)
4. System becomes cheaper and faster over time

**Validation completeness:**
Constraints requiring exhaustive checking must use allowlist validation.

**Allowlist pattern:**
- Define complete set of permitted items
- Reject anything not explicitly allowed
- Ensures no gaps in coverage
- Use for: purity, completeness, exhaustive requirements

**Blocklist pattern:**
- Define set of prohibited items
- Only catches explicitly forbidden items
- New violation types pass silently
- Use for: negative constraints only

**Violation:** Validation missing either syntactic or semantic layer, or purity/completeness constraint implemented with blocklist instead of allowlist
