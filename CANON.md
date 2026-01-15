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

### 2. Repository licensing (root only)

A repository root scope **MUST** contain:

- `LICENSE`
- `NOTICE`

Absence of either file renders the repository root scope invalid.

---

### 3. Inheritance

Every `CANON.md` **MUST** declare the scope it inherits from.

- Inheritance **MUST** terminate at `/`.
- Inherited axioms are final and **MUST NOT** be overridden.

---

### 4. Introspection

`VOCAB.md` **MUST** define every content concept used by:

- this CANON, and
- `VOCAB.md` itself.

Undefined content concepts render the scope invalid.

---

### 5. Root minimalism

Root CANON **MUST** contain only paradigm-level axioms.

- Implementation details belong in MACHINE scope
- Procedural rules belong in OS scope
- Narrative records belong in WRITING scope

Root scope establishes constitutional structure; downstream scopes specialize.

---

### 6. VOCAB closure at root

Root VOCAB definitions **MAY** be circular and minimal.

- Root concepts are self-grounding
- Meaning emerges from structure and canonical context
- Downstream scopes inherit and enrich definitions

This is structurally necessary, not a defect.

---

### 7. Layer discipline

Concepts belong in the scope that introduces them.

- Axioms **MUST** be placed in the scope that governs the action they constrain
- Concepts **MUST NOT** be defined in a downstream scope and referenced by an upstream scope
- Inheritance carries concepts downstream only

---

### 8. Lifecycle documentation

Each machine scope **SHOULD** document its automation lifecycle.

Lifecycle documentation **MUST** include:

- **Origin**: How the machine was discovered or created
- **Current state**: Human-driven, AI-assisted, or AI-automated
- **Automation drift**: The trajectory from manual to automated operation

This documents the evolution from human governance to AI execution while preserving human authority.

---

**This CANON defines constitutional validity for all CANONIC scopes.**

---
