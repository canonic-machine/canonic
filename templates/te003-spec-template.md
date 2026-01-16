# <SCOPE_NAME> SPEC

**Status:** CANONICAL
**Closed:** <DATE>

---

## 1. Purpose

<State the purpose of this scope.>

---

## 2. Governance Path

```
<ROOT_PATH>
├── inherits: / (self-terminating)
│
└──► <PARENT_PATH>
     ├── inherits: <GRANDPARENT_PATH>
     │
     └──► <SCOPE_PATH> (THIS SCOPE)
          └── inherits: <PARENT_PATH>
```

| Field | Value |
|-------|-------|
| Path | `<SCOPE_PATH>` |
| Inherits | `<PARENT_PATH>` |
| Closes | CANON.md |

---

## 3. Normative language

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as described in RFC 2119.

---

## 4. Principles

<State high-level design principles.>

---

## 5. Constraints

<State what this SPEC explicitly does not govern.>

---

## 6. Validation

```
VALIDITY = triad(scope) ∧ inheritance(scope) ∧ introspection(scope)
```

---

**This SPEC closes CANON. Governance is defined exclusively by CANON.**

---
