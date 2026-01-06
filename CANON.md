
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

### README vocabulary accessibility
**All key technical terms used in README.md must be explained or linked to definitions.**

**Violation:** README uses technical terms without providing accessible explanations

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

### Introspective governance
**CANONIC systems must exhibit introspection through self-* properties: self-optimizing, self-healing, self-documenting, self-validating.**

**Introspection aspects:**
- **Self-optimizing**: Continuous improvement through constraint refinement
- **Self-healing**: Automatic correction of violations and inconsistencies
- **Self-documenting**: Governance artifacts that explain and validate themselves
- **Self-validating**: Built-in validation that enforces declared constraints

**Violation:** System lacks required introspective governance properties

### Mermaid governance
**All diagrams must use Mermaid with consistent styling:**
- Direction: LR (left-to-right) for flowcharts, TB (top-bottom) for hierarchies
- Node shapes: rectangles for processes, diamonds for decisions
- Colors: professional grays/blues, avoid bright colors
- Labels: concise, actionable verbs
- Layout: logical flow, minimal crossing lines

**Violation:** Diagram uses inconsistent styling, wrong direction, or unprofessional appearance

### Semantic constraints
**CANON.md must declare semantic validation rules for self-validation.**

**Semantic validation rules:**
- All technical terms in CANON.md and README.md must be defined in VOCABULARY.md
- README.md must explain key technical terms used

**Violation:** CANON.md lacks semantic constraint declarations

### Governance purity
**The canonic repository must contain only pure governance: CANON.md, VOCABULARY.md, README.md, and examples demonstrating the paradigm.**

**Purity requirements:**
- No executable code, tools, or protocols
- No references to specific implementations or tools
- Governance files must remain platform/tool-agnostic
- All implementation belongs in machine lineage and downstream

**Violation:** canonic repository contains tools, protocols, or implementation-specific references

### Documentation purity
**README.md and examples must not reference non-existent tools or protocols.**

**Violation:** Documentation contains references to tools/validation/ that don't exist in canonic repository

### Dual validation requirement
**CANONIC systems must implement both syntactic and semantic validation layers.**

**Validation layers:**
- **Syntactic validation**: Automated checks for file existence, structure, and basic format compliance
- **Semantic validation**: LLM-enhanced checks for constraint compliance, governance purity, and invariant adherence

**Violation:** System implements only syntactic validation without semantic constraint enforcement

### Self-documenting README
**README.md must be automatically generatable from CANON.md and VOCABULARY.md constraints through self-documenting introspection.**

**README generation requirements:**
- Title must match repository purpose from CANON context
- Tagline must summarize core paradigm from VOCABULARY.md
- Quick Start section must list: specification file, examples, related projects
- Core Idea section must explain paradigm vs traditional programming
- Triad section must show file purposes with examples
- Why This Matters section must explain paradigm benefits
- Core Concepts section must define all terms from VOCABULARY.md
- Examples section must reference all example directories
- Repository Structure must reflect actual directory contents
- How to Use section must provide learning path
- Applications section must list use cases from paradigm scope

**Violation:** README.md contains content not derivable from CANON.md and VOCABULARY.md constraints

---

End of root CANON.
