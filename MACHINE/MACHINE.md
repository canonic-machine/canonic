# ENFORCEMENT MACHINE — SPEC

inherits: /CANONIC/

---

## Purpose

Implements enforcement of inherited canon through validation and execution gating.

Provides the runtime that makes governance non-optional.

---

## Core Principle

```
VALIDATION MUST PRECEDE EXISTENCE
```

An artifact that fails validation does not exist in the governed system.
It may exist in user-space, but it has no authority.

---

## Execution Model

| State | Meaning |
|-------|---------|
| Default | Execution denied |
| Permitted | Explicit grant required |
| Revoked | Permission withdrawn |
| Overridden | Human bypass (logged) |

---

## Enforcement Properties

| Property | Requirement |
|----------|-------------|
| Deny by default | No implicit permissions |
| Explicit grant | Permission must be declared |
| Revocable | Any permission can be withdrawn |
| Traceable | All enforcement actions logged |
| Human override | Humans may bypass (with logging) |

---

## Validation Flow

```
Artifact → Validator → Pass? → Exists
                    → Fail? → Blocked
```

Validators check:
- Inheritance chain valid
- Required dimensions present
- Nomenclature rules followed
- Upstream constraints satisfied

---

## Non-Properties

The machine does NOT define:
- What dimensions are required (see /CANONIC/language/)
- What names are valid (see /CANONIC/language/nomenclature/)
- Domain-specific validation rules

It only enforces what upstream canon declares.

---
