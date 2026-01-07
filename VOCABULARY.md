# VOCABULARY (canonic-programming/)

**Term definitions for the CANONIC programming paradigm.**

All terms defined here are inherited by downstream implementations.

---

## Core Paradigm Terms

### CANONIC programming
Programming paradigm that uses plain-English constraints + validation gates instead of executable code to govern system behavior. Named for "canon" (body of rules). Also referred to as "canonic programming" (lowercase when used as adjective). The term "canonical" is an acceptable alias but "canonic" is primary.

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
Checking that artifacts match structural and formal requirements (files exist, IDs are sequential, references resolve, terms are defined). Fast, cheap validation of form over function.

### semantic validation
Checking that the logical meaning and coherence of natural language constraints are valid (rules don't contradict, are enforceable, complete, and unambiguous). Validates the actual semantic content of CANON rules, not just their structure.

### validation gate
A point where validation determines whether work proceeds. Invalid artifacts cannot pass gate.

### backflow
Returning to an earlier state when validation fails. Ensures fixes happen upstream, not through downstream polish.

### git commit as FSM transition
Each git commit proposes a state transition in the CANONIC FSM. Pre-commit validation gates act as transition guards, accepting valid changes and rejecting invalid ones, triggering backflow.

### git history as FSM log
Git commit history serves as the complete execution trace of the CANONIC FSM. Each commit records an accepted state transition, each revert records a failed transition requiring backflow.

### git violation signal
Patterns in git history that indicate CANON violations: commit→revert→reapply sequences (failed validation), rapid commits to CANON files (constraint drift), or violation keywords in commit messages (acknowledged failures).

### atomic commit
A commit that addresses exactly one logical change or constraint. Must be single-concern, self-contained, independently revertible, with clear message. Opposite: mixing multiple unrelated changes in one commit.

### producer commit (canonification)
A git commit that adds new constraints to CANON.md, extracts patterns into protocols, or captures discovered violations. Strengthens governance by encoding new learning. Message pattern: "Canonify [what was learned]". Signals system discovered something new.

### consumer commit (implementation)
A git commit that applies existing CANON constraints, fixes detected violations, or generates artifacts per CANON rules. Follows existing governance. Message pattern: "Apply [constraint]" or "Fix [violation]". Signals system enforced existing rules.

### producer/consumer ratio
The proportion of producer commits to consumer commits in git history. High ratio early (learning phase), decreasing over time as system matures. Measures governance stability: mature systems need fewer new constraints, more enforcement of existing ones.

### validation convergence
The process by which semantic violations become syntactic constraints over time. Expensive LLM checks get canonified into free structural checks. System becomes faster and cheaper as it learns. Producer commits enable this convergence.

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
System that automatically detects and corrects violations of its own constraints through git history analysis. Invalid states are rejected and must be fixed. Git patterns trigger human review when violations recur.

### self-documenting
System that automatically generates its own documentation from governance artifacts. README.md is generated from CANON.md + VOCABULARY.md + primary outputs when sources change. Triad files provide complete self-description without external documentation.

### self-validating
System that validates itself against its own constraints. Tools and agents check their own compliance.

### introspection
The system's ability to examine and understand its own structure, behavior, and constraints. Unifies self-* properties as different aspects of self-awareness and self-regulation.

### introspection cycle
The repeating pattern where work reveals gaps, introspection captures why, learnings are documented, and learnings are canonified into constraints. Core mechanism for system improvement through producer commits.

### session learnings
Artifacts that capture discoveries, gaps, and patterns observed during work sessions. Act as interrupt mechanism triggering canonification. Enable the introspection cycle.

### meta-pattern
A pattern about patterns. Higher-order observation about how the system itself behaves, learns, or evolves. Meta-patterns must themselves be canonified to enable recursive strengthening.

### pattern discovery
The practice of analyzing git history, session artifacts, and system behavior to identify recurring structures, rhythms, and meta-patterns. Required part of introspection cycle.

### session boundary
The transition points between work sessions (start, end). Canonification commits cluster at boundaries, especially end-of-session when introspection naturally occurs.

### burst enforcement
Rapid sequence of consumer commits triggered by discovering a new constraint. System self-corrects in concentrated effort to achieve compliance across all artifacts.

### backflow pattern
Git commit sequence (commit → revert → reapply) indicating failed validation attempt. Signals self-healing event where system detected violation and corrected itself.

### recursive strengthening
Process where meta-patterns about system improvement are themselves canonified, creating self-referential governance that mandates its own evolution.

### self-sustaining governance
Governance that maintains and improves itself through canonification. Every fix strengthens the system by encoding lessons learned.

### Mermaid governance
Consistent styling standards for all Mermaid diagrams in CANONIC systems. Ensures professional, readable visualizations that follow paradigm conventions.

### diagram direction
The flow orientation of Mermaid diagrams. LR (left-to-right) for process flows, TB (top-bottom) for hierarchical structures.

### node shapes
Standardized shapes used in diagrams: rectangles for processes, diamonds for decisions, circles for states.

### README vocabulary accessibility
Requirement that README files make key technical terms understandable to readers, either by direct explanation or clear links to definitions.

### documentation generation
Automated process of synthesizing README.md from CANON.md, VOCABULARY.md, and primary outputs. Triggered when source files change, executed by LLM agent following documentation protocol.

### documentation protocol
Specification defining how README.md is generated from governance sources. Includes input requirements, generation process, validation checks, and trigger conditions.

### primary outputs
The main artifacts produced by a repository. Varies by type: paradigm definitions (governance), LEARNINGS (implementation), output artifacts (domain applications), API docs (documentation systems), papers (research).

### README staleness
Condition where README.md modification timestamp is older than CANON.md or VOCABULARY.md timestamps. Indicates documentation out of sync with governance. Detected by syntactic validation.

### README freshness
Condition where README.md timestamp is equal to or newer than source file timestamps. Indicates documentation reflects current governance state.

### generation trigger
Event that initiates automatic README regeneration. Primary trigger: changes to CANON.md or VOCABULARY.md detected by pre-commit hook.

### self-measuring
System that analyzes its own git history to determine maturity metrics. Calculates producer/consumer commit ratio to identify learning phase: new (>40%), maturing (10-30%), or mature (<10%).

### self-strengthening
System that improves through introspection cycles. Discovered patterns are canonified into constraints, including meta-patterns about improvement itself. Enables recursive strengthening where governance mandates its own evolution.

---

End of VOCABULARY.

