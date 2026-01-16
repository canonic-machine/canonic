# CANONIC (/)

inherits: /

---

## Axioms

### 1. Triad

A scope **MUST** contain the following artifacts:

- `CANON.md`
- `VOCAB.md`
- `README.md`

Absence of any triad artifact renders the scope invalid.

---

### 2. Inheritance

Every `CANON.md` **MUST** declare the scope it inherits from.

- Inheritance **MUST** terminate at `/`.
- Inherited axioms are final and **MUST NOT** be overridden.

---

### 3. Introspection

`VOCAB.md` **MUST** define every content concept used by:

- this CANON, and
- `VOCAB.md` itself.

Undefined content concepts render the scope invalid.

---

## CANONBASE Architecture

The CANONBASE is organized into six layers:

```
┌─────────────────────────────────────────────────────────────┐
│                    CANONBASE ROOT                            │
│              /Canonic/ (parent directory)                    │
│         NOT a git repo - stack isolation boundary            │
└─────────────────────────────────────────────────────────────┘

╔═══════════════════════════════════════════════════════════════╗
║ LAYER 1: GOVERNANCE (Constitutional Core)                     ║
║  canonic/     ─── Root CANON (Triad, Inheritance, Introspect) ║
║  templates/   ─── Template patterns                           ║
╚═══════════════════════════════════════════════════════════════╝
                           │
                           ▼
╔═══════════════════════════════════════════════════════════════╗
║ LAYER 2: MACHINE (Execution Semantics)                        ║
║  machine/     ─── MACHINE (Authority, Input, Eval, Decision)  ║
╚═══════════════════════════════════════════════════════════════╝
                           │
                           ▼
╔═══════════════════════════════════════════════════════════════╗
║ LAYER 3: OPERATIONAL (Procedures & Rules)                     ║
║  os/          ─── OS (operational rules + automation protos)  ║
║  ledger/      ─── LEDGER (git-based immutable record)         ║
║  validators/  ─── VALIDATORS (enforcement implementations)    ║
╚═══════════════════════════════════════════════════════════════╝
                           │
                           ▼
╔═══════════════════════════════════════════════════════════════╗
║ LAYER 4: COMPOSITION (Stack Management)                       ║
║  stack/       ─── STACK (multi-repo composition rules)        ║
║  .github/     ─── GitHub org meta-repo (infra, NO CANON)      ║
╚═══════════════════════════════════════════════════════════════╝
                           │
                           ▼
╔═══════════════════════════════════════════════════════════════╗
║ LAYER 5: PRODUCTION (Artifact Generation)                     ║
║  writing/     ─── WRITING (epistemic layer)                   ║
║  transcript/  ─── TRANSCRIPT (episode records)                ║
║  paper/       ─── PAPER (manuscript production)               ║
║  publishing/  ─── PUBLISHING (release management)             ║
║  patents/     ─── PATENTS (IP production)                     ║
╚═══════════════════════════════════════════════════════════════╝
                           │
                           ▼
╔═══════════════════════════════════════════════════════════════╗
║ LAYER 6: DOMAIN (Application Instances)                       ║
║  atulisms/    ─── Book domain                                 ║
║  dividends/   ─── Book domain                                 ║
║  companies/   ─── Business domain                             ║
║  grants/      ─── Funding domain                              ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## Governance Chain

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
│    └── inherits: / (composition layer)
│
├──► /canonic/transcript/
│    └── inherits: / (direct from root)
│
└──► [Domain repos]
     └── inherits: / (direct from root + domain axioms)
```

---

## Lifecycle

**Origin:** Constitutional governance paradigm discovered through iterative refinement of AI-assisted documentation workflows. Formalized as IDF-001 (Constitutional Governance Paradigm).

**Current state:** AI-assisted. Human authority defines axioms; AI assists with validation, introspection checking, and canonification.

**Automation drift:** Axiom definition remains human-governed. Validation and introspection checking are automatable via VaaS. Governance evolution requires human deliberation; automation bounded by constitutional structure.

---

## References

- IDF-001: Constitutional Governance Paradigm
- IDF-006: Literal Introspection
- IDF-096: Layer Drift Validator
- IDF-114: CANONBASE Architecture

---

**This CANON defines constitutional validity for all CANONIC scopes.**

---
