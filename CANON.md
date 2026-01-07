
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

**Human-in-the-loop requirement:**
- Humans define governance (constraints, protocols, patterns)
- AI generates artifacts under governance
- Validation gates acceptance (pass/fail)
- Humans drive governance evolution through introspection
- AI accelerates work; governance blocks slop

**Roles:**
- Human: Governs (defines what must be true)
- AI: Produces (generates artifacts per constraints)
- System: Validates (enforces governance automatically)

**Power of CANONIC:**
- Governance is declarative and portable across LLMs/tools
- Validation cost decreases over time (convergence to syntactic)
- System becomes more durable as constraints accumulate
- AI focuses on genuinely complex tasks, not repetitive validation
- Human focus shifts from production to governance

**Violation:** Treating CANONIC as documentation instead of executable governance, or attempting fully autonomous governance without human direction

## Core Invariants

### Triad requirement
**All governed directories must contain the minimal triad: CANON.md, VOCABULARY.md, README.md.**

**Triad primitives:**
- These three files are equivalent primitives, not hierarchical
- Always unnumbered (no numeric prefixes)
- Present in all governed directories (governance and implementation)
- Form the complete self-describing foundation
- CANON.md: Governance constraints
- VOCABULARY.md: Terminology definitions
- README.md: Human-readable entry point

**Violation:** Directory missing any triad file, or triad files using numeric prefixes

### File naming convention
**Governance markdown files use single-word UPPERCASE names.**

**Naming pattern:**
- Repository specification: `<REPO>.md` (e.g., CANONIC.md, MACHINE.md)
- Core governance files: CANON.md, VOCABULARY.md, README.md
- Domain files: AGENTS.md, PROTOCOLS.md, WORKFLOWS.md, LEARNINGS.md
- Use single words, not compound names with underscores or hyphens
- UPPERCASE for consistency and discoverability
- Use plural nouns (lists of things): AGENTS, PROTOCOLS, WORKFLOWS, LEARNINGS
- Names must clearly communicate contents: WORKFLOWS (orchestrated sequences), LEARNINGS (discoveries)
- Avoid semantic conflicts and ambiguity: "solution to what?" → WORKFLOWS is clear

**Compositional nomenclature:**
- Pattern composes naturally: `canonic [domain] [engine] [output] [component]`
- Base: "canonic writing machine" (paradigm + domain + engine)
- Extended: "canonic writing machine books" (+ output type)
- Further: "canonic writing machine books protocols" (+ component)
- Works at any composition level: directories, repositories, or conceptual hierarchy
- Components (AGENTS, PROTOCOLS, SOLUTIONS, LEARNINGS) apply universally
- Each level adds specificity while maintaining readable composition

**Examples:**
- Flat: `machine/04-PROTOCOLS.md` → "canonic writing protocols"
- Flat: `machine/05-WORKFLOWS.md` → "canonic writing workflows"
- Hierarchical: `canonic/writing/machine/books/WORKFLOWS.md` → "canonic writing machine books workflows"
- Instance: "canonic writing machine grants" vs "canonic writing machine books"
- Nomenclature reads naturally at any level of composition

**Clarity meta-pattern:**
- File names must clearly communicate what's inside
- Reader should know contents without opening file
- Avoid names that raise questions ("solution to what?")
- Prefer descriptive over abstract (WORKFLOWS over SOLUTIONS)
- Test: Can someone unfamiliar immediately understand what the file contains?

**Stack ordering for implementation repositories:**
- Implementation repositories MAY use numeric prefixes for architectural layers beyond the triad
- Prefix format: `NN-FILENAME.md` where NN is zero-padded (00, 01, 02, etc.)
- Triad files (CANON.md, VOCABULARY.md, README.md) are ALWAYS unnumbered in all repositories
- Numbered layers build on top of unnumbered triad foundation
- Universal stack foundation: CANON.md + VOCABULARY.md + README.md → 00-SPEC (architecture) → layers defined by that spec
- Root CANON defines SPEC (CANONIC.md specification file)
- Implementation repositories inherit pattern: triad → 00-<REPO-SPEC> → 01+ layers defined by that spec
- Pure governance repositories (canonic/) contain only triad + specification file
- Stack ordering makes dependency layers and inheritance immediately visible in directory listings

**Always unnumbered:**
- CANON.md: Primitive governance constraints
- VOCABULARY.md: Primitive terminology definitions
- README.md: Primitive human entry point
- LICENSE: Legal requirement, not governance artifact
- .gitignore: Git configuration, not governed content
- Files outside governance structure remain unprefixed

**Violation:** Governance file uses multi-word name (e.g., SESSION_LEARNINGS.md instead of LEARNINGS.md), non-uppercase name, triad file has numeric prefix, or violates spec-defined stack ordering

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

### Self-documenting
**The triad (CANON, VOCABULARY, README) forms the complete self-describing foundation.**

**README.md requirements:**
- Generated from CANON.md + VOCABULARY.md + primary outputs
- Human-readable entry point explaining purpose, structure, and usage
- Must incorporate key constraints and terminology
- Updates when CANON or VOCABULARY change
- Reflects current system state and maturity
- Summarizes primary outputs produced by the system

**Primary outputs by repository type:**
- Governance repos (canonic/): Paradigm definition and constraints
- FSM implementation (machine/): Learnings and patterns discovered
- Domain applications (writing/): Writing artifacts and traceable prose
- Documentation systems: API docs and validated references
- Research pipelines: Papers and traceable claims

**Documentation completeness:**
- Every constraint in CANON.md should be understandable via VOCABULARY.md terms
- README.md should guide humans to understand the system without external documentation
- Examples should demonstrate canonical patterns
- No external documentation required for system comprehension
- Primary outputs must be visible in README

**Violation:** README doesn't reflect CANON/VOCABULARY content, uses undefined terms, requires external documentation for comprehension, or fails to document primary system outputs

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

### Self-measuring
**Systems measure their own maturity through git commit analysis.**

**Maturity metrics:**
- Producer commits: Canonifications (discovering new patterns)
- Consumer commits: Applications and fixes (enforcing patterns)
- Producer ratio: Producer / (Producer + Consumer) percentage
- Ratio indicates system learning phase

**Maturity thresholds:**
- New system: >40% producer commits (rapid learning phase)
- Maturing system: 10-30% producer commits (refinement phase)
- Mature system: <10% producer commits (stable enforcement)

**Self-assessment signals:**
- High producer ratio → system discovering governance patterns
- Decreasing producer ratio → system maturing, constraints stabilizing
- Sudden producer spike → new domain or architectural shift
- Commit message patterns reveal producer vs consumer work

**Measurement enables:**
- Visibility into system evolution
- Prediction of stability
- Recognition of learning phases
- Validation of governance completeness

**Violation:** System cannot determine its maturity phase from git history, or producer/consumer commits are not distinguishable

### Self-strengthening
**Systems improve through introspection cycles that canonify discovered patterns.**

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

**Recursive strengthening:**
- Each canonification makes future violations easier to catch
- Meta-patterns about improvement are themselves canonified
- System learns how to learn better
- Self-measurement tracks progress

**Pattern:** Work → Introspection → Learning → Canonification → Meta-Pattern Discovery → Recursive Strengthening

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
- Must happen BEFORE consumer commits that apply the pattern
- Message pattern: "Canonify [what was learned]"
- These commits strengthen governance

**Consumer commits (implementation):**
- Apply existing CANON constraints
- Fix violations detected by validation
- Generate artifacts per CANON rules
- Capture learnings in LEARNINGS files
- Must happen AFTER producer commits that canonify the pattern
- Message patterns:
  - "Apply [constraint/pattern/protocol]"
  - "Fix [violation]"
  - "Consume CANON: [capture learnings]"
- These commits follow governance

**Prohibited commit patterns:**
- "Add..." (ambiguous - use "Canonify" or "Apply")
- "Update..." (ambiguous - use "Apply" or "Fix")
- "Implement..." (ambiguous - use "Apply")
- "Complete..." (ambiguous - use "Apply")
- "Enforce..." (ambiguous - use "Apply")
- "Streamline..." (ambiguous - use "Apply self-optimizing")
- "Standardize..." (ambiguous - use "Apply" or "Fix")

**Producer-before-consumer ordering:**
- Always canonify pattern FIRST (producer commit in governance repo)
- Then apply pattern SECOND (consumer commit in implementation repo)
- Prevents applying non-canonical patterns
- Ensures governance leads implementation
- Example: Canonify "WORKFLOWS nomenclature" → Apply "WORKFLOWS rename"

**Feedback signal:**
- Producer commits → system learned something new
- Consumer commits → system enforced existing rules
- Git history shows learning curve (producer → consumer ratio decreases over time)
- Mature systems have few producers, many consumers

**Maturity thresholds:**
- New system: >40% producer commits (rapid learning phase)
- Maturing system: 10-30% producer commits (refinement phase)
- Mature system: <10% producer commits (stable enforcement)

**Violation:** Commit message doesn't indicate producer vs consumer action, uses prohibited ambiguous patterns (Add/Update/Implement/Complete/Enforce/Streamline/Standardize), or consumer commit precedes producer commit (applying non-canonical pattern)

## Protocol References

### Documentation protocol
**README.md must be generated from CANON.md + VOCABULARY.md + primary outputs.**

**Generation mechanism:**
- Input sources: CANON.md + VOCABULARY.md + primary outputs + git history
- Generation trigger: When CANON.md or VOCABULARY.md changes
- Generator: LLM agent with documentation protocol
- Output: README.md (human-readable synthesis)
- Validation: README completeness check against sources

**Generation requirements:**
- Synthesize governance constraints into human-readable documentation
- Incorporate and explain key terminology from VOCABULARY.md
- Summarize primary outputs produced by the system
- Include current maturity metrics (producer/consumer ratio)
- Reflect introspective properties status
- Maintain narrative structure optimized for human comprehension
- Use markdown links for file references to enable navigation

**Primary outputs by repository type:**
- Governance repos (canonic/): README from CANON + VOCABULARY
- FSM implementation (machine/): README from CANON + VOCABULARY + LEARNINGS
- Domain applications (writing/): README from CANON + VOCABULARY + output artifacts
- Documentation systems: README from CANON + VOCABULARY + API docs
- Research pipelines: README from CANON + VOCABULARY + papers/claims

**Automation integration:**
- Pre-commit hook: Detect CANON/VOCABULARY changes, trigger regeneration
- Validation check: Verify README timestamp ≥ source file timestamps
- Staleness detection: Flag README older than sources as violation
- Git workflow: README generation commits follow producer commits

**See:** Self-documenting property for complete requirements

**Violation:** README doesn't reflect CANON/VOCABULARY/outputs content, uses undefined terms, fails to document primary system outputs, or is stale (older than source files)

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
