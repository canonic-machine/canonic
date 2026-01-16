# VOCAB (/)

inherits: /

---

## Content Concepts

### AI

Artificial intelligence; a collaborator in CANONIC governance operating under human authority.

---

### artifact

A file governed by CANON.

---

### axiom

A normative rule declared in CANON.

---

### CANON

The governance artifact of a scope.

---

### CANONIC

The constitutional governance paradigm defined by the root scope; establishes the minimal structural and semantic rules all scopes must satisfy.

---

### CANONBASE

The complete multi-repository governance stack; the parent directory containing all governed scopes.

---

### canonification

The process of evolving artifacts toward the canonical structural form defined by CANONIC templates.

---

### content concept

A term defined in VOCAB and used in CANON or VOCAB.

---

### governance chain

The inheritance path from a scope through its parents to the root scope.

---

### inheritance

The relationship by which a scope adopts axioms from a parent scope.

---

### README

The descriptive artifact of a scope.

---

### root scope

The scope at `/` from which all other scopes inherit; the termination point of inheritance.

---

### scope

A directory governed by a triad AND closed by a SPEC. Without SPEC, a directory is a **proto-scope** (triad-compliant but not closed). SCOPE = TRIAD + SPEC. CS domain term for computational boundaries and namespace contexts.

---

### layer

IDF domain term for architectural strata and governance levels; distinct from scope which operates in CS domain.

---

### stack isolation boundary

The parent directory containing all stack members, which must not be a git repository to prevent cross-repo coupling.

---

### triad

The set of artifacts (`CANON.md`, `VOCAB.md`, `README.md`) required for a valid scope.

---

### validity

The state of a scope that satisfies all applicable axioms.

---

### VOCAB

The vocabulary artifact of a scope.

---

### SPEC

Optional fourth element (beyond triad). Named `{SCOPE_NAME}.md` (e.g., `TEMPLATES.md`, `MACHINE.md`). SPEC closes CANON by defining the governance chain relative to that scope. Can extend with generation details or future plans. Not constrained by Axiom 3. The root SPEC (`CANONIC.md`) is special: it closes itself and exposes the full CANONBASE. (IDF-116, IDF-119)

---

### closure

The constraint relationship between artifacts. VOCAB closes **semantics** (Axiom 3). SPEC closes the **scope** (governance chain + generation details). A directory with triad but no SPEC is a proto-scope (open). A directory with triad AND SPEC is a scope (closed). At root, CANONIC is closed: VOCAB self-defines, SPEC (`CANONIC.md`) defines the full CANONBASE. (IDF-116, IDF-119)

---

### proto-scope

A directory that satisfies triad (CANON.md, VOCAB.md, README.md) but lacks SPEC. Proto-scopes are open—they can evolve. Adding SPEC closes the proto-scope into a scope.

---

### introspection

The axiom requiring VOCAB to define every content concept used by CANON and VOCAB itself; ensures semantic completeness within each scope. (IDF-006)

---

### episode

A unit of epistemic work in WRITING; a session that produces transcript evidence.

---

### IDF

Invention Disclosure Form; a patent disclosure document.

---

### IP

Intellectual property.

---

### WRITING

The epistemic scope governing episode production.

---

### ROOT

The root scope (/) from which all inheritance terminates.

---

### GATE

An axiom that gates validity; the three root axioms (Triad, Inheritance, Introspection) are the constitutional gates. VALIDATORS implement gating axiomatically.

---

### VALIDATORS

Pure, axiomatic enforcement implementations that implement the gating of axioms across the governance chain. No bloat. IP secure. MACHINE orchestrates validators to determine validity.

---

### VaaS

Validators as a Service; the CANONIC composition pattern where pure validators are composed into complete enforcement. (IDF-118)

---

## Stack Scopes

### machine

The enforcement scope that evaluates candidate states against CANON.

---

### os

The operational scope defining procedures, rules, and automation protocols.

---

### ledger

The immutable record scope providing git-based evidence storage.

---

### stack

The composition scope defining multi-repo composition rules.

---

### templates

The templates scope containing placeholder scaffolds for governance artifacts.

---

### transcript

The transcript scope recording episode evidence.

---

### paper

The paper scope for manuscript production.

---

### patents

The patents scope for IP production and disclosure.

---

### publishing

The publishing scope for release management.

---

## Nomenclature

CANONIC uses prefixed identifiers for artifact enumeration. (IDF-091, IDF-093)

### Prefix Registry

| Prefix | Expansion | Domain | Format | Ordering |
|--------|-----------|--------|--------|----------|
| IDF | Invention Disclosure Form | patents | `IDF-NNN` | chronological |
| TE | Template Element | templates | `TE-NNN` | closure precedence |
| EP | Episode | transcript | `EP-NNN` | chronological |

### Format Rules

- Prefix: uppercase, 2–3 characters
- Separator: hyphen (`-`)
- Number: zero-padded, 3 digits (001–999)
- Identifier: `{PREFIX}-{NNN}` (e.g., `IDF-001`, `TE-001`, `EP-001`)
- Filename: `{prefix}-{nnn}-{description}.md` (lowercase prefix)

### Ordering Semantics

Template ordering reflects **closure precedence**:

| Template | Artifact | Role |
|----------|----------|------|
| TE-001 | SPEC | Closure |
| TE-002 | CANON | Governance |
| TE-003 | VOCAB | Semantics |
| TE-004 | README | Description |

Episode and IDF ordering is **chronological** (creation order).

---

## IDF Closure

| Concept | IDF | Title |
|---------|-----|-------|
| CANONIC governance | IDF-001 | Constitutional Governance Paradigm |
| introspection | IDF-006 | Literal Introspection |
| nomenclature | IDF-091 | Portfolio Coverage Standardization |
| prefix canonicity | IDF-093 | Prefix Canonicity Constraint |
| directory discriminant | IDF-094 | Directory Discriminant Pattern |
| structural bootstrapping | IDF-095 | Structural Bootstrapping Pattern |
| layer drift | IDF-096 | Layer Drift Validator |
| CANONBASE architecture | IDF-114 | CANONBASE Multi-Repository Architecture |
| SPEC closure model | IDF-116 | Four-Element Structure |
| GATE architecture | IDF-118 | Axiomatic Validator Architecture |
| SPEC self-closure | IDF-119 | Root SPEC Self-Closure Pattern |

---
