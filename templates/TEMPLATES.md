# TEMPLATES

## 1. Purpose

Define the TEMPLATES scope for CANONIC.

TEMPLATES provide canonical placeholder structures for instantiating CANONIC governance artifacts in downstream scopes.

---

## 2. Scope

- Applies to `/canonic/templates/`.
- Inherits from `/`.
- Governs template structure only.

---

## 3. Normative language

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as described in RFC 2119.

Statements using these key words are normative. Examples are non-normative unless explicitly marked otherwise.

---

## 4. Principles

### 4.1 Structural bootstrapping

Templates exist to bootstrap CANONIC scopes with correct file structure.

Templates define shape and presence, not meaning.

---

### 4.2 Non-authority

Templates are non-authoritative.

They do not define governance, enforcement, execution semantics, or interpretation.

---

## 5. Constraints

- Templates **MUST** exist for the following artifacts:
  - `CANON.md`
  - `SPEC.md`
  - `VOCAB.md`
  - `README.md`

- Templates **MUST** be placeholder-only.
- Templates **MUST NOT** introduce scope-specific governance or behavior.
- Templates **MUST** be flat within this directory (no subfolders).

---

## 6. Validation

A TEMPLATES scope is valid if and only if:

- templates exist for CANON, SPEC, VOCAB, and README, and
- templates contain no enforceable governance or executable behavior.

---

## 7. Consumption notes

- Downstream scopes instantiate templates to create local governance artifacts.
- Instantiated artifacts are governed by their local CANON, not by these templates.

---

**This SPEC is descriptive and non-authoritative.**  
**Governance is defined exclusively by CANON.**

---
