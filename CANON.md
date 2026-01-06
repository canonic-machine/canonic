# CANON (canonic-programming/)

**Governance for the CANONIC programming paradigm repository.**

This CANON defines the root invariants for all CANONIC programming implementations.

---

## Inheritance

**Inherits from:** None (this is the root CANON)

**This is the root CANON.**

All downstream implementations (repositories, directories, systems) inherit these invariants.

Downstream CANONs may:
- Specialize defaults for their scope
- Add domain-specific constraints
- Reference protocols defined here

Downstream CANONs must not:
- Contradict invariants defined here
- Override triad requirements
- Bypass validation gates

**Cross-repository inheritance:**
- Uses markdown links to GitHub repositories only
- Format: `**Inherits from:** [repo-name](https://github.com/org/repo)`
- Root CANON must state: `**Inherits from:** None (this is the root CANON)`
- No git submodules, no scripts, no package managers, no tooling
- LLM follows links to load CANON chain
- Violation: Adding executable code or tooling for inheritance
- Violation: Missing explicit inheritance statement (must be present in every CANON)

---

## Invariants

### Triad requirement

**All directories must contain the triad:**
- `CANON.md` — Constraints the LLM enforces
- `VOCABULARY.md` — Term definitions
- `README.md` — Human-readable guidance

**Triad audience:**
- `CANON.md`: LLM/agent first (constraints, validation, enforcement)
- `VOCABULARY.md`: Both (precise definitions, shared vocabulary)
- `README.md`: Human first (explanation, context, examples)

**Violation:** Directory missing any triad file

**Exception:** Root directory of a repository may have a GitHub-optimized README.md that does not follow triad conventions, provided a canonical README exists elsewhere or the repository clearly signals paradigm adoption.

### Terminology discipline

**All technical terms must be defined in VOCABULARY:**
- Terms used in CANON.md must be defined in VOCABULARY.md (same directory or inherited)
- Terms used in README.md must be defined in VOCABULARY.md (same directory or inherited)
- Undefined terms constitute violations

**Violation:** Using undefined terms in governed artifacts

### Validation gates

**All artifacts must pass validation before acceptance:**
- Invalid states are rejected
- Output exists only when compliant
- Fluency never substitutes for validity

**Violation:** Accepting artifacts that fail validation

### Traceability

**All derived content must trace to source material:**
- Claims trace to evidence
- Entities trace to episodes or observations
- Structure traces to requirements

**Violation:** Invented content without documented origin

### Reference integrity

**All references must resolve:**
- File references must point to existing files
- Protocol references must resolve to defined protocols
- Pattern references must resolve to defined patterns
- Repository URLs must be consistent and correct

**Violation:** Broken reference to non-existent artifact
**Violation:** Inconsistent repository URLs across documentation

---

## Defaults

These may be specialized by downstream CANONs.

### Markdown conventions

- Headers: ATX-style (`#` `##` `###`)
- Diagrams: Mermaid for all visual representations
- Line length: 100 characters (soft limit, not enforced)

### File naming

- CANON files: `CANON.md` (uppercase, exact)
- Vocabulary files: `VOCABULARY.md` (uppercase, exact)
- README files: `README.md` (uppercase, exact)

### Validation behavior

- Report violations with: artifact path, line number, requirement reference, details
- Exit codes: 0 (success), 1 (failure), 130 (user interrupt)
- Accept `--root` parameter to override auto-detection

---

## Protocols

Reusable validation patterns referenced by downstream CANONs.

### triad_protocol

**Purpose:** Verify directory contains required governance files.

**Check:**
1. Directory must contain `CANON.md`
2. Directory must contain `VOCABULARY.md`
3. Directory must contain `README.md`

**Violation:** Missing any required file

### terminology_protocol

**Purpose:** Verify terms are defined before use.

**Check:**
1. Extract technical terms from artifact
2. Look up each term in VOCABULARY.md (local or inherited)
3. Flag undefined terms

**Violation:** Term used but not defined in accessible VOCABULARY

### inheritance_protocol

**Purpose:** Build CANON chain from root to target.

**Check:**
1. Start at target directory
2. Traverse up to repository root
3. Collect all CANON.md files in order
4. Verify no contradictions between child and parent invariants
5. Verify every CANON has explicit inheritance statement

**Violation:** Child CANON contradicts parent invariant
**Violation:** CANON missing inheritance statement

### reference_integrity_protocol

**Purpose:** Verify all references resolve correctly.

**Check:**
1. Extract all file references (PROTOCOLS.md, PATTERNS.md, etc.)
2. Extract all protocol/pattern references
3. Extract all repository URLs
4. Verify each reference resolves to existing artifact
5. Verify repository URLs are consistent

**Violation:** Reference to non-existent file
**Violation:** Reference to undefined protocol or pattern
**Violation:** Inconsistent repository URL (different org/repo names for same entity)

---

## Meta

This CANON defines the minimal CANONIC programming paradigm.

Specific applications (Writing Machine, validation systems, FSM implementations) build on this foundation.

**This CANON is durable.** It should rarely change once established.

---

End of root CANON.

---

## Canonbase Optimization

### Protocol/Pattern Reuse

**Constraint:**
All new constraints that are reusable across directories or domains must be encoded as protocols or patterns in the root CANON or referenced from a shared PROTOCOLS.md or PATTERNS.md.

**Violation:** Duplicating constraint logic in multiple CANONs without protocol/pattern abstraction.

### Override Discipline

**Constraint:**
Only defaults may be overridden by downstream CANONs, and only via explicit CANON statements. Invariants must never be restated or contradicted downstream.

**Violation:** Overriding or restating invariants in downstream CANONs.

### Minimal Triad Canonification

**Constraint:**
The minimal triad (CANON.md, VOCABULARY.md, README.md) must be the canonical starting point for all new governed directories. Downstream CANONs should reference root protocols and patterns rather than duplicating logic.

**Violation:** Creating governed directories without the triad or with redundant constraint logic.
