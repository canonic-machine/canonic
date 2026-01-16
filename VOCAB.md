# VOCAB (/)

inherits: /

---

## Content Concepts

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

The complete multi-repository governance stack organized into six layers: Governance, Machine, Operational, Composition, Production, and Domain.

---

### content concept

A term defined in VOCAB and used in CANON or VOCAB.

---

### governance chain

The inheritance path from a scope through its parents to the root scope.

---

### governance layer

One of six architectural layers in the CANONBASE: Governance, Machine, Operational, Composition, Production, Domain.

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

A directory governed by a triad.

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

Optional fourth element (beyond triad). SPEC closes the CANON and can extend it with generation details or future plans. Not constrained by Axiom 3. (IDF-116)

---

### closure

The constraint relationship between artifacts. CANON and VOCAB have mutual closure (Axiom 3). README spans VOCAB but can extend. SPEC closes CANON but can extend. (IDF-116)

---

### introspection

The axiom requiring VOCAB to define every content concept used by CANON and VOCAB itself; ensures semantic completeness within each scope. (IDF-006)

---

## Layer Definitions

### Governance layer

Layer 1: Constitutional core containing root CANON and templates.

---

### Machine layer

Layer 2: Execution semantics defining how enforcement works.

---

### Operational layer

Layer 3: Procedures and rules including OS, LEDGER, and VALIDATORS.

---

### Composition layer

Layer 4: Stack management including STACK and .github infrastructure.

---

### Production layer

Layer 5: Artifact generation including writing, paper, patents.

---

### Domain layer

Layer 6: Application instances that inherit root and add domain-specific axioms.

---

## IDF Closure

| Concept | IDF | Title |
|---------|-----|-------|
| CANONIC governance | IDF-001 | Constitutional Governance Paradigm |
| introspection | IDF-006 | Literal Introspection |
| layer drift | IDF-096 | Layer Drift Validator |
| CANONBASE architecture | IDF-114 | CANONBASE Multi-Repository Architecture |
| SPEC closure model | IDF-116 | Four-Element Structure |

---
