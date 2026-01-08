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

## Core Invariants

### Triad requirement
**All governed directories must contain the minimal triad: CANON.md, VOCAB.md, README.md.**

**SPEC vs VOCAB vs CANON:**
- **SPEC files** (CANONIC.md, WRITING.md, PAPER.md, etc.): Human-iterated source of truth. What the system IS.
- **VOCAB.md**: LLM-generated alphabetically ordered term definitions. What terms mean.
- **CANON.md**: LLM-generated constraints and requirements. How the system must work.

**VOCAB is chronological with SPEC** - SPEC term is first VOCAB entry, vocabulary evolves with specification.

**Violation:** Directory missing any triad file, VOCAB.md terms not alphabetically ordered, or SPEC term not first VOCAB entry

### VOCAB self-governance
**The VOCAB itself must be fully governed.**

VOCAB is not just a governance artifact—it must demonstrate governance properties. The vocabulary that defines coherent, compliant, and fully governed must itself be coherent, compliant, and fully governed.

**Coherence requirements:**
- All term definitions must be logically consistent (no contradictions)
- Cross-references must be accurate and complete
- Categories must be mutually exclusive and collectively exhaustive

**Compliance requirements:**
- Alphabetical ordering within each section (case-insensitive)
- Proper header hierarchy (## for sections, ### for terms)
- Consistent formatting (bold for key terms, backticks for code)

**Violation:** VOCAB contains contradictions, ordering violations, broken references, or inconsistent formatting

### VOCAB terminology consumption
**All VOCAB.md files must use correct terminology in footer.**

The footer must say "End of VOCAB" not "End of DICTIONARY" or any other inherited terminology. Violation indicates failed consumption.

**Violation:** VOCAB.md footer uses incorrect terminology

### Multi-repo synchronization
**All repositories must be regularly synchronized with origin.**

Repositories should not accumulate commits ahead of origin/main. Regular push/pull cycles ensure all repos share same governance state.

**Violation:** Repository is more than 5 commits ahead of origin, or repositories have divergent commit histories

### Governance vocabulary completeness
**Root VOCAB must define essential governance quality terms.**

At minimum, VOCAB must include:
- coherent: semantic property of logical constraint consistency
- compliant: syntactic property of structural requirement matching
- fully governed: the ideal state (both coherent AND compliant)

**Violation:** Root VOCAB missing essential governance quality terms

### Multi-repo vocabulary synchronization
**When new governance terms are canonified, all repos must consume them.**

New terms defined in root VOCAB must be added to:
- MACHINE VOCAB
- WRITING VOCAB
- PAPER VOCAB

This ensures all agents at all layers learn the same vocabulary.

**Violation:** New term in root VOCAB not present in downstream VOCABs

### Three-layer architecture
**CANONIC implementations must separate paradigm, validation engine, and domain applications.**

**Three-layer architecture:**
- **CANONIC** (paradigm layer): Defines constraints, validation, inheritance, triad
- **MACHINE** (validation engine layer): Implements constraint checking, git-FSM, self-* properties
- **Domain applications** (application layer): Inherit from MACHINE, add domain-specific patterns

**Violation:** Validation engine contains domain-specific patterns, or domain application reimplements validation logic

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
