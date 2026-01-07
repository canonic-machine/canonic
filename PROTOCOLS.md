# PROTOCOLS

**Reusable validation and generation patterns for CANONIC systems.**

---

## Documentation Generation Protocol

**Purpose:** Generate README.md from CANON.md + VOCABULARY.md + primary outputs

**Type:** Self-documenting automation

### Inputs

1. **CANON.md** — Governance constraints
2. **VOCABULARY.md** — Term definitions
3. **Primary outputs** — Domain-specific artifacts (varies by repository type)
4. **Git history** — Producer/consumer commits, maturity metrics

### Process

1. **Extract constraints** from CANON.md
   - Core invariants
   - Key semantic constraints
   - Introspective properties status
   - Protocol references

2. **Extract terminology** from VOCABULARY.md
   - Core paradigm terms
   - Domain-specific terms
   - Meta-pattern terms

3. **Analyze git history**
   - Calculate producer/consumer ratio
   - Determine maturity phase
   - Identify recent canonifications

4. **Identify primary outputs**
   - Governance repos: Paradigm definitions
   - Implementation repos: LEARNINGS.md entries
   - Domain applications: Output artifacts
   - Documentation systems: API docs
   - Research pipelines: Papers and claims

5. **Synthesize documentation**
   - Human-friendly narrative structure
   - Clear sections with markdown headings
   - Code examples where relevant
   - Mermaid diagrams for visual concepts
   - Markdown links for file references
   - Explanation of key terminology
   - Current maturity status

### Outputs

**README.md** with required sections:

1. **Title and tagline** — What this system does
2. **Quick start** — Minimal path to understanding
3. **Core concepts** — Key terminology explained
4. **Structure** — Directory layout and file purposes
5. **Introspective properties** — Self-* capabilities status
6. **Maturity metrics** — Current learning phase
7. **Recent discoveries** — Latest canonifications
8. **References** — Related files and external links

### Validation

**Completeness checks:**
- All CANON.md invariants represented
- All VOCABULARY.md core terms explained
- Primary outputs documented
- Maturity metrics included
- All file references use markdown links

**Freshness checks:**
- README.md timestamp ≥ CANON.md timestamp
- README.md timestamp ≥ VOCABULARY.md timestamp
- If sources changed, README must regenerate

**Coherence checks:**
- No undefined terms used
- All references resolve
- Narrative flows logically
- Examples match current constraints

### Trigger Conditions

**Automatic regeneration when:**
- CANON.md is modified
- VOCABULARY.md is modified
- Primary outputs change significantly
- Manual regeneration requested

**Implementation via:**
- Pre-commit git hook
- CI/CD validation check
- Manual invocation via script/command

### Agent Specification

**Agent role:** Documentation generator

**Agent capabilities:**
- Read markdown files
- Parse CANON constraint structure
- Extract VOCABULARY definitions
- Analyze git commit history
- Identify file patterns (primary outputs)
- Synthesize human-readable prose
- Generate markdown with proper structure
- Create mermaid diagrams
- Validate output completeness

**Agent constraints:**
- Must follow documentation protocol exactly
- Must validate own output before completion
- Must use only defined terminology
- Must maintain triad coherence
- Must not invent content without source
- Must trace all claims to CANON/VOCABULARY

**Agent workflow:**
1. Read input files
2. Extract structured data
3. Analyze patterns
4. Generate README sections
5. Validate completeness
6. Validate freshness
7. Output README.md

### Example Usage

```bash
# Manual invocation
generate-readme --canon CANON.md --vocabulary VOCABULARY.md --output README.md

# Pre-commit hook
if [[ CANON.md or VOCABULARY.md changed ]]; then
  generate-readme
  git add README.md
fi

# Validation check
validate-readme-freshness --canon CANON.md --vocabulary VOCABULARY.md --readme README.md
```

### Repository-Specific Variations

**Governance repository (canonic/):**
- Input: CANON + VOCABULARY
- Focus: Paradigm explanation
- Examples: Minimal demonstrations

**Implementation repository (machine/):**
- Input: CANON + VOCABULARY + LEARNINGS
- Focus: FSM architecture and discoveries
- Examples: Protocol applications

**Domain repository (writing/):**
- Input: CANON + VOCABULARY + output artifacts
- Focus: Domain application and results
- Examples: Actual outputs produced

---

## Validation Convergence Protocol

**Purpose:** Migrate semantic validations to syntactic constraints over time

**Type:** Self-optimizing automation

### Pattern

1. Semantic validator detects violation (expensive LLM call)
2. Human analyzes why violation occurred
3. Pattern extracted as syntactic constraint
4. CANON updated with new syntactic rule (producer commit)
5. Future validations catch syntactically (free check)
6. Token cost decreases over time

### Metrics

- Track semantic validation frequency
- Track syntactic validation coverage
- Measure token cost reduction
- Identify high-frequency semantic violations for canonification

---

## Introspection Cycle Protocol

**Purpose:** Capture learnings and canonify discovered patterns

**Type:** Self-strengthening automation

### Cycle

1. **Work** — Perform tasks, generate artifacts
2. **Introspection** — Examine what went wrong/right
3. **Learning** — Capture discoveries in LEARNINGS.md
4. **Canonification** — Extract patterns into CANON.md (producer commit)
5. **Meta-pattern discovery** — Analyze learning patterns themselves
6. **Recursive strengthening** — Canonify meta-patterns

### Triggers

- Session boundaries (end of work session)
- Validation failures (backflow events)
- Manual introspection request
- Git violation signals (commit→revert→reapply)

---

End of PROTOCOLS.
