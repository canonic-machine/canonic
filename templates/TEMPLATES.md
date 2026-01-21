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

## 5. Template Ordering

Templates are indexed as `TEMPLATE-###-stub.md` to reflect **closure precedence**:

| Template | Artifact | Role |
|----------|----------|------|
| TEMPLATE-000 | SPEC | Closure — closes governance chain, defines scope boundary |
| TEMPLATE-001 | CANON | Governance — defines axioms and validity |
| TEMPLATE-002 | VOCAB | Semantics — defines content concepts |
| TEMPLATE-003 | README | Description — non-normative documentation |
| TEMPLATE-004 | COVERAGE | Closure tracking — external completeness (optional) |
| TEMPLATE-005 | ROADMAP | Planning — gap closure plan (optional) |

### Rationale

SPEC is first because closure defines the scope.

Without SPEC, a directory with CANON + VOCAB + README is a **proto-scope** — open, evolving, not yet closed.

With SPEC, the scope is **closed** — governance chain terminates, validity is decidable.

The ordering reflects authority:
1. **SPEC** closes CANON (authority)
2. **CANON** governs VOCAB (governance)
3. **VOCAB** defines README terms (semantics)
4. **README** describes the scope (documentation)
5. **COVERAGE** tracks external completeness (optional)
6. **ROADMAP** plans gap closure (optional)

---

## 6. Constraints

- Templates **MUST** exist for the following artifacts:
  - `SPEC.md` (TEMPLATE-000)
  - `CANON.md` (TEMPLATE-001)
  - `VOCAB.md` (TEMPLATE-002)
  - `README.md` (TEMPLATE-003)
- Templates **SHOULD** exist for the following artifacts:
  - `COVERAGE.md` (TEMPLATE-004)
  - `ROADMAP.md` (TEMPLATE-005)

- Templates **MUST** be placeholder-only.
- Templates **MUST NOT** introduce scope-specific governance or behavior.
- Templates **MUST** be flat within this directory (no subfolders).

---

## 7. Validation

A TEMPLATES scope is valid if and only if:

- templates exist for SPEC, CANON, VOCAB, and README (TEMPLATE-000–TEMPLATE-003), and
- templates contain no enforceable governance or executable behavior.

---

## 8. Consumption notes

- Downstream scopes instantiate templates to create local governance artifacts.
- Instantiated artifacts are governed by their local CANON, not by these templates.

---

**This SPEC is descriptive and non-authoritative.**  
**Governance is defined exclusively by CANON.**

---
