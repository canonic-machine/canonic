# VOCABULARY (canonic-programming/)

**Term definitions for the CANONIC programming paradigm.**

All terms defined here are inherited by downstream implementations.

---

## Core Paradigm Terms

### CANONIC programming
Programming paradigm that uses plain-English constraints + validation gates instead of executable code to govern system behavior. Named for "canon" (body of rules).

### canon
A written set of constraints that define what must be true and what must not occur in a system. The governance layer.

### constraint
A rule that narrows outcomes to a checkable set. Must be verifiable through validation.

### validation
A pass/fail decision procedure that checks artifacts against canon constraints. Not subjective judgment—binary compliance check.

### artifact
Any output under governance. Examples: documents, diagrams, indices, references, ledgers, code files.

### state
A stable condition defined by which artifacts exist and which constraints they satisfy.

### invariant
A constraint that cannot be overridden by downstream CANONs. Must hold true across entire inheritance chain.

### default
A constraint that can be specialized by downstream CANONs. Provides baseline but allows local adaptation.

### protocol
A named, reusable validation pattern that can be referenced by multiple CANONs. Defined once, applied many times.

---

## Governance Terms

### triad
The three required files in every directory: CANON.md (constraints), VOCABULARY.md (definitions), README.md (human guide).

### inheritance
The mechanism by which downstream CANONs acquire constraints from upstream CANONs. Forms a chain from root to target.

### inheritance chain
The ordered sequence of CANON files from repository root to target directory. Each level adds or specializes constraints.

### violation
A failure to satisfy a canon constraint. Must be fixed before artifacts can be accepted.

### compliance
State of satisfying all applicable canon constraints. Required for artifact acceptance.

### reference integrity
The property that all references (file, protocol, pattern, URL) resolve to existing, valid targets. Prevents broken links and inconsistent documentation.

---

## Agent Terms

### LLM
Large Language Model. AI system that can interpret CANON constraints and generate/validate artifacts.

### agent
Automated system (often LLM-based) that operates on artifacts under CANON governance. Enforces constraints without human intervention.

### AI slop
Fluent but invalid output from AI systems. Text that sounds correct but violates requirements, invents references, or drifts from constraints.

---

## Validation Terms

### syntactic validation
Checking that artifacts match structural requirements (file exists, IDs sequential, references resolve). Fast, cheap.

### semantic validation
Checking that artifacts satisfy intent and meaning requirements (claim coherence, purpose alignment). Slower, token-intensive.

### validation gate
A point where validation determines whether work proceeds. Invalid artifacts cannot pass gate.

### backflow
Returning to an earlier state when validation fails. Ensures fixes happen upstream, not through downstream polish.

---

## Structural Terms

### root CANON
The top-level CANON in a repository or system. Defines invariants all other CANONs inherit.

### downstream CANON
A CANON that inherits from an upstream CANON. May specialize defaults but not contradict invariants.

### scope
The portion of a system governed by a specific CANON. Usually defined by directory boundaries.

---

## Document Terms

### LLM-first artifact
Document optimized for machine interpretation. Examples: CANON.md, protocols, constraint specifications.

### human-first artifact  
Document optimized for comprehension and teaching. Examples: README.md, guides, tutorials.

### either artifact
Document that must serve both LLM and human audiences. Examples: VOCABULARY.md, specifications.

---

## Meta Terms

### paradigm
The foundational approach or model. CANONIC programming is a paradigm for governance without executable code.

### durability
Property of systems that remain stable and valid across time, edits, and collaborators. Primary goal of CANONIC programming.

### traceability
Ability to trace every artifact back to its source material or requirement. Prevents drift and hallucination.

### self-optimizing
System that automatically maintains optimal performance and efficiency. Prevents bloat and enforces lean operation.

### self-healing
System that automatically detects and corrects violations of its own constraints. Invalid states are rejected and must be fixed.

### self-documenting
System that contains all necessary documentation within its governance structure. Triad files provide complete self-description.

### self-validating
System that validates itself against its own constraints. Tools and agents check their own compliance.

### self-sustaining governance
Governance that maintains and improves itself through canonification. Every fix strengthens the system by encoding lessons learned.

### Mermaid governance
Consistent styling standards for all Mermaid diagrams in CANONIC systems. Ensures professional, readable visualizations that follow paradigm conventions.

### diagram direction
The flow orientation of Mermaid diagrams. LR (left-to-right) for process flows, TB (top-bottom) for hierarchical structures.

### node shapes
Standardized shapes used in diagrams: rectangles for processes, diamonds for decisions, circles for states.

---

End of VOCABULARY.
