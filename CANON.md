# CANONIC (/)

inherits: /

---

## Axioms

### 0. Triad

A scope **MUST** contain the following artifacts:

- `CANON.md`
- `VOCAB.md`
- `README.md`

Absence of any triad artifact renders the scope invalid.

---

### 1. Inheritance

Every `CANON.md` **MUST** declare the scope it inherits from.

- Inheritance **MUST** terminate at `/`.
- Inherited axioms are final and **MUST NOT** be overridden.

---

### 2. Introspection

`VOCAB.md` **MUST** define every content concept used by:

- this CANON, and
- `VOCAB.md` itself.

Undefined content concepts render the scope invalid.

---

### 3. Cascade

When a CANON axiom changes, the LLM **MUST** execute the cascade:

1. **IDF** — File the discovery to IP-REGISTRY
2. **VaaS** — Create or update the validator
3. **Downstream** — Update scopes that inherit
4. **Closure** — Verify the parent scope closes

The cascade IS the validation. Incomplete cascade renders the change invalid.

---

### 4. Closure

The scope closes itself.

---

### 5. Minimal Fixed Point

`.git` **IS** the complete state of CANONIC.

- Everything outside `.git` is a derived view
- Delete all files, run `git checkout`, system restored
- Any immutable, cryptographically-verified ledger satisfies this axiom
- Git is one instantiation; blockchain is another

The ledger IS the system. Everything else is ceremony.

---

## Lifecycle

**Origin:** Constitutional governance paradigm discovered through iterative refinement of AI-assisted documentation workflows. Formalized as IDF-001 (Constitutional Governance Paradigm).

**Current state:** AI-assisted. Human authority defines axioms; AI assists with validation, introspection checking, and canonification.

**Automation drift:** Axiom definition remains human-governed. Validation and introspection checking are automatable via VaaS. Governance evolution requires human deliberation; automation bounded by constitutional structure.

---

## Workflows

### Archive-First

Development **SHOULD** work backward from the archive (endpoint) to the current state.

- **Archive** = The product (what "done" looks like)
- **Current** = The state (what we have)
- **Delta** = The work (archive - current)
- **Closure** = Current achieves archive quality

Archives are reference implementations. Drift from archive = non-compliance.

---

## References

- IDF-001: Constitutional Governance Paradigm
- IDF-006: Literal Introspection
- IDF-096: Layer Drift Validator
- IDF-114: CANONBASE Architecture
- IDF-148: Axiom Change Cascade Protocol (Axiom 3)
- IDF-149: Git IS the Blockchain (Axiom 5)
- IDF-154: Archive-First Development (Workflow)
- IDF-163: Specification Drift Prevention Pattern (Axiom 4)

---

**This CANON defines constitutional validity for all CANONIC scopes.**

---
