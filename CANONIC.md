# CANONIC

## 1. Purpose

Define the constitutional foundation of the CANONIC paradigm.

CANONIC establishes the minimal structural and semantic laws that govern all downstream scopes.

---

## 2. Scope

- This artifact (`CANONIC.md`) is the paradigm specification; it is non-normative prose.
- `CANON.md` is the normative governance artifact; validity is defined exclusively there.
- Applies to the root scope (`/`) and governs all inherited scopes.
- Defines constitutional constraints only; it does not define enforcement, execution, or behavior.

---

## 3. Normative language

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as described in RFC 2119.

Statements using these key words are normative. Examples and diagrams are non-normative unless explicitly marked otherwise.

---

## 4. Principles

### 4.1 Structural minimality

CANONIC defines the minimal structure required for a valid scope.

No constraints beyond those required for structure, inheritance, and semantic closure are imposed at this layer.

---

### 4.2 Governance separation

CANONIC defines governance only.

- Enforcement is defined in MACHINE.
- Execution is defined in downstream scopes.
- Interpretation and insight are defined outside CANONIC.

---

### 4.3 Abstraction

CANONIC defines semantic roles, not implementations.

Concrete tools and workflows are non-normative at this layer.

---

## 5. Constraints

### 5.1 Triad

A scope **MUST** contain the following artifacts:

- `CANON.md`
- `VOCAB.md`
- `README.md`

Absence of any triad artifact renders the scope invalid.

---

### 5.2 Inheritance

Every `CANON.md` **MUST** declare the scope it inherits from.

- Inheritance **MUST** terminate at `/`.
- Inherited axioms are final and **MUST NOT** be overridden.

---

### 5.3 Introspection

`VOCAB.md` **MUST** define every content concept used by:

- its corresponding `CANON.md`, and
- `VOCAB.md` itself.

Undefined content concepts render the scope invalid.

---

## 6. Validation

### 6.1 Validity Definition

A CANONIC scope is valid if and only if:

```
VALIDITY = triad(scope) ∧ inheritance(scope) ∧ introspection(scope)
```

### 6.2 Formal Semantics

CANONIC is a formal language. Validators are predicates. Composition is conjunction.

```
Atomic:       script.py : Scope → {0, 1}
Orchestrator: axiom.py  = atomic₁ ∧ atomic₂ ∧ ... ∧ atomicₙ
VALIDATORaaS:         validator_as_a_service.py   = triad.py ∧ inheritance.py ∧ introspection.py
```

Exit code 0 = true (PASS). Exit code non-zero = false (FAIL).

### 6.3 Characteristic Function

The set of valid states is mathematically defined:

```
VALID = { σ ∈ CANONBASE | vaas(σ) = 0 }
```

The atomic validators ARE the formal specification of CANONIC validity.

### 6.4 Axiom Decomposition

**Axiom 1 (Triad):**
```
triad.py = canon.py ∧ vocab.py ∧ readme.py
```

**Axiom 2 (Inheritance):**
```
inheritance.py = declaration.py ∧ termination.py ∧ cycle.py
```

**Axiom 3 (Introspection):**
```
introspection.py = canon_concepts.py ∧ vocab_concepts.py ∧ closure.py ∧ locality.py ∧ drift.py ∧ gap.py
```

### 6.5 VALIDATORaaS Execution Layer

VALIDATORaaS (Validators as a Service) is the execution layer for CANONIC.

```
CANONIC = Language (specification)
VALIDATORaaS    = Runtime (execution)
```

```bash
python validator_as_a_service.py <canonbase>
```

Returns VALIDITY: PASS or VALIDITY: FAIL.

The atomics ARE the mathematical definition of validity. VALIDATORaaS IS the interpreter.

### 6.6 Axiomatic Closure

CANONIC is a **closed formal system**:

```
∀σ ∈ CANONBASE: vaas(σ) = PASS
```

| Property | Status |
|----------|--------|
| Triad | 45/45 scopes closed |
| Inheritance | 45/45 chains terminate at / |
| Introspection | 45/45 vocabularies complete |

The system validates itself. Validators are scopes. They satisfy their own axioms.

---

## 7. CANONBASE

The complete governance stack:

```
┌─────────────────────────────────────────────────────────────┐
│                    CANONBASE ROOT                           │
│              /Canonic/ (parent directory)                   │
│         NOT a git repo - stack isolation boundary           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ GOVERNANCE (Constitutional Core)                            │
│  canonic/     ─── Root CANON (Triad, Inheritance, Introspect)│
│  templates/   ─── Template patterns                         │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ MACHINE (Execution Semantics)                               │
│  machine/     ─── MACHINE (Authority, Input, Eval, Decision)│
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ OPERATIONAL (Procedures & Rules)                            │
│  os/          ─── OS (operational rules + automation protos)│
│  ledger/      ─── LEDGER (git-based immutable record)       │
│  validators/  ─── VALIDATORS (enforcement implementations)  │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ COMPOSITION (Stack Management)                              │
│  stack/       ─── STACK (multi-repo composition rules)      │
│  .github/     ─── GitHub org meta-repo (infra, NO CANON)    │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ PRODUCTION (Artifact Generation)                            │
│  writing/     ─── WRITING (epistemic scope)                 │
│  transcript/  ─── TRANSCRIPT (episode records)              │
│  paper/       ─── PAPER (manuscript production)             │
│  publishing/  ─── PUBLISHING (release management)           │
│  patents/     ─── PATENTS (separate scope)                  │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ DOMAIN (Application Instances)                              │
│  atulisms/    ─── Book domain                               │
│  dividends/   ─── Book domain                               │
│  companies/   ─── Business domain                           │
│  grants/      ─── Funding domain                            │
└─────────────────────────────────────────────────────────────┘
```

---

## 8. Governance Chain

```
/canonic/ (ROOT)
├── inherits: / (self-terminating)
│
├──► /canonic/machine/
│    ├── inherits: /canonic
│    │
│    ├──► /canonic/machine/os/
│    │    ├── inherits: /canonic/machine/
│    │    │
│    │    ├──► /canonic/machine/os/ledger/
│    │    └──► /canonic/machine/os/writing/
│    │         └──► /canonic/machine/os/writing/paper/
│    │
│    └──► /canonic/machine/validators/
│         └──► [specific validators]
│
├──► /canonic/stack/
│    └── inherits: / (composition scope)
│
├──► /canonic/transcript/
│    └── inherits: / (direct from root)
│
└──► [Domain repos]
     └── inherits: / (direct from root + domain axioms)
```

---

## 9. Consumption notes

- Downstream scopes inherit these constraints without contradiction.
- Additional constraints may be introduced downstream but must not violate CANONIC.

---

**This SPEC defines the constitutional semantics of CANONIC.**
**Validity is defined exclusively by CANON.**

---
