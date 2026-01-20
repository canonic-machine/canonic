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

A directory governed by a triad AND closed by a SPEC. Without SPEC, a directory is a **proto-scope** (triad-compliant but not closed). SCOPE = TRIAD + SPEC.

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

### closure

The scope closes itself. Scoped specifications. (Axiom 6, IDF-163)

---

### cascade

The mandatory sequence executed when a CANON axiom changes: IDF → VALIDATORaaS → Downstream → Closure. The LLM executes the cascade; incomplete cascade renders the axiom change invalid. (IDF-148)

---

### closure

The constraint relationship between artifacts. VOCAB closes **semantics** (Axiom 3). SPEC closes the **scope** (governance chain + generation details). A directory with triad but no SPEC is a proto-scope (open). A directory with triad AND SPEC is a scope (closed). At root, CANONIC is closed: VOCAB self-defines, SPEC (`CANONIC.md`) defines the full CANONBASE. (IDF-116, IDF-119)

---

### archive

The reference implementation; the endpoint state from which development works backward. Archives are not historical—they define "done." (IDF-154)

---

### delta

The computed difference between archive (endpoint) and current (state). Delta = Archive - Current. Executing delta moves current toward archive quality.

---

### archive-first

The development pattern where work begins at the archive (what we want), compares to current (what we have), and executes delta (what to do). Opposite of forward development. (Axiom 5, IDF-154)

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

### EP

Episode; series prefix for transcript episodes (EP-NNN format).

---

### PA

Patent Application; series prefix for patent applications (PA-NNN format).

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

### VALIDATORaaS

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

### DISCLOSURES

The invention disclosure registry scope within patents; the destination for IDF filings during cascade.

---

### publishing

The publishing scope for release management.

---

## Nomenclature

CANONIC uses prefixed identifiers for artifact enumeration. (IDF-091, IDF-093)

### Prefix Registry

| Prefix | Expansion | Domain | Format | Ordering |
|--------|-----------|--------|--------|----------|
| IDF | Invention Disclosure Form | patents/disclosures | `IDF-NNN` | chronological |
| PA | Patent Application | patents/applications | `PA-NNN` | gate precedence |
| TE | Template Element | templates | `TE-NNN` | closure precedence |
| EP | Episode | transcript | `EP-NNN` | chronological |

### Format Rules

- Prefix: uppercase, 2–3 characters
- Separator: hyphen (`-`)
- Number: zero-padded, 3 digits (000–999)
- Identifier: `{PREFIX}-{NNN}` (e.g., `IDF-000`, `TE-000`, `EP-000`)
- Filename: `{prefix}-{nnn}-{description}.md` (lowercase prefix)

### Ordering Semantics

**Precedence-ordered** (semantic dependency):

| Prefix | Ordering | Rationale |
|--------|----------|-----------|
| TE | closure precedence | SPEC → CANON → VOCAB → README |
| PA | gate precedence | TRIAD → INHERITANCE → INTROSPECTION |

| TE | Artifact | Role |
|----|----------|------|
| TE-000 | SPEC | Closure |
| TE-001 | CANON | Governance |
| TE-002 | VOCAB | Semantics |
| TE-003 | README | Description |

| PA | Gate | Blocks |
|----|------|--------|
| PA-000 | TRIAD | Structural foundation |
| PA-001 | INHERITANCE | Authority hierarchy |
| PA-002 | INTROSPECTION | Semantic closure |

**Chronologically-ordered** (creation order):

| Prefix | Ordering |
|--------|----------|
| IDF | creation order |
| EP | creation order |

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
| Git + LLM infrastructure | IDF-147 | Git + LLM Infrastructure Closure |
| cascade | IDF-148 | Axiom Change Cascade Protocol |
| distributed ledger consensus | IDF-149 | Distributed Ledger Consensus via Git |
| encrypted git | IDF-150 | Encrypted Git as Privacy Layer |
| visibility × storage | IDF-151 | Visibility × Storage Access Matrix |
| feature closure chain | IDF-152 | Feature Closure Chain Protocol |
| illustration selection | IDF-153 | Optimal Illustration Selection |
| archive-first | IDF-154 | Archive-First Development |
| render pipeline | IDF-155 | Render Pipeline Validator |
| axiom closure matrix | IDF-156 | Axiom Closure Matrix |
| innovation multiplier | IDF-157 | Innovation Multiplier Pattern |
| healthcare distributed ledger | IDF-158 | Healthcare Distributed Ledger Pattern |
| TOKENaaS | IDF-159 | Reputation Gates Currency |
| OncoChat domain closure | IDF-160 | Oncology Domain Closure Pattern |
| CANONIC sublanguage | IDF-161 | Governance Programming Language |
| dot notation namespace | IDF-162 | CANONIC Dot Notation Namespace |
| SPEC template variable | IDF-163 | Specification Drift Prevention Pattern |

---
