
# CANON (/)

**Inherits from:** None

## Constitutional Nature

### Root CANON as constitution
**The root CANON is the constitution of CANONIC programming.**

**Constitutional properties:**
- Defines fundamental governance principles (not domain-specific rules)
- Is the deduplication point (triad, inheritance, separation of concerns defined once)
- Enables composition (all downstream implementations inherit these principles)
- Must be stable (constitutional law does not churn after paradigm matures)

**The root CANON is the vocabulary:**
- Defines what governance terms mean (definitive source of truth)
- Provides canonical definitions used by all implementations
- Mandates VOCAB.md in triad (vocabularies all the way down)
- Serves as lexicon for the paradigm
- VOCAB is temporal - evolves with the machine (not static dictionary)

**Violation:** Root CANON contains domain-specific patterns, shows high commit frequency after stabilization, or allows constitutional principles to drift

### Producer/consumer as legislative process
**Producer commits canonify new patterns. Consumer commits apply canonical constraints.**

**Producer commits (legislative):**
- Add definitions to the constitutional dictionary
- Expand the governance language
- Use pattern: `Canonify [what was learned]`
- Occur in governance repository (CANONIC)

**Consumer commits (executive):**
- Apply constitutional requirements
- Speak the governance language correctly
- Use patterns: `Apply [constraint]` or `Fix [violation]`
- Occur in implementation repositories (MACHINE, domain applications)

**Legislative flow:**
```
CANONIC produces → MACHINE consumes
MACHINE produces → Domain applications consume
Domain applications produce → Artifacts consume
```

Each layer is consumer of the layer above, producer for the layer below.

### Cross-repo atomic coordination
**Producer/consumer episodes must coordinate commits across every affected repository.**

The four-repo stack (CANONIC, MACHINE, WRITING, PAPER) already obeys canonical signals, but the “multi-repo disconnect” analysis revealed that atomic actions must land in each repository to make an episode traceable.

**Constraint:** Before declaring an insight canonified or applied, ensure each repo records its own commit referencing the same episode, insight number, and vocabulary so the evidence path remains unbroken.

**Violation:** A repo shows no edits while others advance a shared insight, or a documentation episode references an insight that lacks corresponding producer/consumer commits elsewhere.

### Compliance proof
**Compliance is a commitment to the canon backed by git proof.**

Every compliance claim must appear as a git commit whose message references the relevant constraint/episode and whose diff contains the validation or documentation evidence that proves the system obeys the constraint. The commit must either be:
- A producer-style `Canonify …` entry that introduces a new insight with linked episodes or test commands.
- A consumer-style `Apply …`/`Fix …` entry that records the validation run (logs, outputs, exit codes) confirming compliance.

**Constraint:** No compliance claim can exist outside of git history. Reviewers must be able to rerun the recorded commands or inspect the artifact mentioned in the commit to verify compliance.

**Violation:** Describing compliance without a corresponding commit message or producing artifacts that lack git-proven validation.

### Episode alignment
**Future insights must tie to numbered PAPER episodes with matching git commits in all affected repositories.**

Every time a new insight emerges (producer or consumer), create or update the next sequential `paper/episodes/0XX-*.md` entry summarizing the context, action, and proof. Each repository that participates in that insight must reference the same episode number in its commit message and diff so the documentary chain stays intact.

**Constraint:** No insight is complete until the episode and all participating repos signal the same episode number in their commits. Episode numbers must be sequential and never reused.

**Violation:** Adding an episode without matching commits in the repos, or making commits that reference an insight without updating the episode log. This breaks the evidence trail.

### Agentized git signals
**Every git signal must explicitly name the agent or agent role along with the episode reference.**

Commits are the canonical signal of compliance: they are the place the agent explains what constraint it addressed and why. Every commit message must mention the agent (e.g., “Agent08”, “Canon Agent”, “Machine Agent”) or repeat the agent role (“producer agent”, “consumer agent”) and the same episode number referenced in the linked episode file.

**Constraint:** A commit that doesn’t mention an agent role or episode number is incomplete. Use the format `Episode 0XX – Agent [role] …` for the commit summary, so the agent presence is obvious to reviewers.

**Violation:** Commits that omit both the agent role and episode number; these commits fail the compliance-proof requirement because they lack an explicit agent signal.

### Proper git compliance
**Proper git compliance means issuing a redo commit (never rewriting history) when earlier evidence lacks the required agent/episode signal.**

If you discover a past insight that predates the agentized signal, do not reset `HEAD` or amend history. Instead, add a follow-up commit that references the same episode number and states “redo signal” or similar, explicitly describing how the new commit restores compliance. This redo commit becomes part of the canonical proof chain.

**Constraint:** Every redo or compliance-restoring commit must mention the episode (e.g., `Episode 024 – Agent02 Apply compliance redo signal`) and describe the missing evidence it replaces. The commit message and episode document combine to explain why the redo occurred and how the compliance trail was fixed.

**Violation:** Resetting history to retroactively fix messages, or adding redo commits without referencing the episode/agent (the evidence trail still breaks).

**Maturity signals:**
- High producer ratio → Constitutional language still forming
- Low producer ratio → Constitutional language stabilized
- Static root CANON → Constitution complete

**Violation:** Consumer commit precedes producer commit, implementation produces without consuming upstream constraints, or root CANON shows continuous churn after paradigm stabilization

## Core Invariants

### Triad requirement
**All governed directories must contain the minimal triad: CANON.md, VOCAB.md, README.md.**

**SPEC vs VOCAB vs CANON:**
- **SPEC files** (CANONIC.md, WRITING.md, PAPER.md, etc.): Human-iterated source of truth. What the system IS.
- **VOCAB.md**: LLM-generated alphabetically ordered term definitions. What terms mean.
- **CANON.md**: LLM-generated constraints and requirements. How the system must work.

**VOCAB is chronological with SPEC** - SPEC term is first VOCAB entry, vocabulary evolves with specification.

**Violation:** Directory missing any triad file, VOCAB.md terms not alphabetically ordered, or SPEC term not first VOCAB entry

### Implementation inheritance
**Implementation repositories inherit from protocol specifications via markdown links.**

**Violation:** Implementation claims to inherit from non-existent files

### Examples requirement
**Governance repositories must include examples directory demonstrating the paradigm.**

**Violation:** Governance repository missing examples directory

### LICENSE requirement
**All CANONIC repositories must include Apache License 2.0 with full attribution.**

**Constitutional properties:**
- Full open source (freedom to use, modify, distribute)
- Full attribution (copyright notice, license text, NOTICE file required)
- Patent grant (contributors grant patent rights)
- Trademark protection (no trademark rights granted)

**Required files:**
- LICENSE (Apache 2.0 full text)
- NOTICE (attribution to original author)

**Violation:** Repository missing LICENSE file, LICENSE not Apache 2.0, missing NOTICE file, or missing copyright attribution

### Abstraction layers
**CANONIC implementations must separate paradigm, validation engine, and domain applications.**

**Three-layer architecture:**
- **CANONIC** (paradigm layer): Defines constraints, validation, inheritance, triad
- **MACHINE** (validation engine layer): Implements constraint checking, git-FSM, self-* properties
- **Domain applications** (application layer): Inherit from MACHINE, add domain-specific patterns

**Violation:** Validation engine contains domain-specific patterns, or domain application reimplements validation logic
Episode 030 – Producer Canonify cross-repo coordination requirement
