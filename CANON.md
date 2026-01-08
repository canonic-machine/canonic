
# CANON (canonic/)

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

**Maturity signals:**
- High producer ratio → Constitutional language still forming
- Low producer ratio → Constitutional language stabilized
- Static root CANON → Constitution complete

**Violation:** Consumer commit precedes producer commit, implementation produces without consuming upstream constraints, or root CANON shows continuous churn after paradigm stabilization

## Core Invariants

### Triad requirement
**All governed directories must contain the minimal triad: CANON.md, VOCAB.md, README.md.**

**VOCAB.md must contain alphabetically ordered term definitions.**

**VOCAB is chronological with SPEC** - SPEC term is first entry, vocabulary evolves with specification.

**Violation:** Directory missing any triad file, VOCAB.md terms not alphabetically ordered, or SPEC term not first entry

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
