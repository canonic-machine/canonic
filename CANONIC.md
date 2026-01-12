# CANONIC

## 1. Purpose

Define the constitutional foundation of the CANONIC paradigm.

CANONIC establishes the minimal structural and semantic laws that govern all downstream scopes.

---

## 2. Scope

- Applies to `/canonic`.
- Governs all inherited scopes.
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

A CANONIC scope is valid if and only if:

- the triad is present,
- inheritance is declared and non-contradictory, and
- all content concepts are defined in VOCAB.

---

## 7. Consumption notes

- Downstream scopes inherit these constraints without contradiction.
- Additional constraints may be introduced downstream but must not violate CANONIC.

---

**This SPEC defines the constitutional semantics of CANONIC.**
**Validity is defined exclusively by CANON.**

---