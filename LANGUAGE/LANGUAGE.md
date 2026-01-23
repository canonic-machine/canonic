# GOVERNANCE LANGUAGE — SPEC

inherits: /CANONIC/

---

## Purpose

Defines the fixed dimensions along which governance may reason.

These dimensions represent the minimum conditions under which automation may exist.

This layer defines axes, not rules.

---

## The Six Dimensions (DETROS)

| Dimension | Symbol | Function |
|-----------|--------|----------|
| Declarative | D | Assertions of truth, claims |
| Evidential | E | Proof, testimony, verification |
| Temporal | T | Time-ordering, sequence, history |
| Relational | R | Boundaries, scope, jurisdiction |
| Operational | O | Enforcement, execution, permissions |
| Structural | S | Form, shape, institutional pattern |

---

## Lattice

The six dimensions combine into 2^6 = 64 possible configurations:

```
|P(6)| = 64 = 63 primitives + ∅
```

Each configuration is a governance formula (e.g., D∩E∩T = #22).

---

## Completeness

These six dimensions are:
- **Fixed**: No dimension may be added
- **Complete**: All governance can be expressed through these
- **Orthogonal**: No dimension derives from another
- **Minimal**: Removing any breaks the system

---

## Validation

An artifact is valid against a formula iff it satisfies all required dimensions.

```
VALIDATE(artifact, formula) = ∧ { dimension(i) | i ∈ formula }
```

---
