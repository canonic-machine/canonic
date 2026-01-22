# CANONIC (/)

inherits: /
status: FROZEN

---

## Compliance

**Level:** ENTERPRISE

This scope **MUST** maintain ENTERPRISE compliance:
- Triad (CANON, VOCAB, README)
- SPEC (CANONIC.md)
- COVERAGE (internal closure)
- ROADMAP (external closure)

---

## Axioms

### 1. Triad

A scope **MUST** contain: `CANON.md`, `VOCAB.md`, `README.md`.

Absence of any triad artifact renders the scope invalid.

---

### 2. Inheritance

Every `CANON.md` **MUST** declare `inherits:`.

Inheritance **MUST** terminate at `/`.

Inherited axioms are final and **MUST NOT** be overridden.

---

### 3. Introspection

`VOCAB.md` **MUST** define every concept used by CANON and VOCAB.

Undefined concepts render the scope invalid.

---
