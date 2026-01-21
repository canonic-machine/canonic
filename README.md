# CANONIC

The constitutional foundation of the CANONIC paradigm.

---

## Purpose

Define the minimal structural and semantic laws that govern all downstream scopes.

---

## Axioms

| # | Name | Constraint |
|---|------|------------|
| 0 | Triad | Scope MUST contain: `CANON.md`, `VOCAB.md`, `README.md` |
| 1 | Inheritance | Every `CANON.md` MUST declare `inherits:`. Terminates at `/` |
| 2 | Introspection | `VOCAB.md` MUST define every concept used by CANON and VOCAB |

---

## Validation

```bash
python validator_as_a_service.py /path/to/scope
```

Returns `VALIDITY: PASS` or `VALIDITY: FAIL`.

---

## Structure

```
canonic/
├── CANON.md          # Normative governance (3 axioms)
├── VOCAB.md          # Term definitions
├── README.md         # This file
├── CANONIC.md        # Paradigm specification (non-normative)
├── COVERAGE.md       # External standard coverage
├── ROADMAP.md        # Development roadmap
├── .github/          # GitHub integration
├── .githooks/        # Git hooks (pre-commit validation)
└── plans/            # Planning documents
```

---

## Governance

This scope is the root. All other scopes inherit from `/`.

---

*Governed by: CANON.md*

---
