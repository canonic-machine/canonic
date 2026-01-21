# VOCAB (/canonic/)

inherits: /

---

## Core Concepts

### scope

A directory containing `CANON.md` that defines governance boundaries.
Scopes inherit from parent scopes via explicit declaration.

### triad

The three required governance artifacts: `CANON.md`, `VOCAB.md`, `README.md`.
Absence of any triad artifact renders the scope invalid.

### inheritance

The governance chain from scope to root.
Every `CANON.md` MUST declare `inherits:`. Terminates at `/`.

### introspection

Vocabulary closure: all concepts in CANON and VOCAB must be defined.
Undefined concepts render the scope invalid.

---

## Artifacts

### CANON

The normative governance artifact (`CANON.md`) declaring axioms and inheritance.
Validity is defined exclusively by CANON.

### VOCAB

The vocabulary artifact (`VOCAB.md`) defining all concepts used by the scope.
MUST define every content concept used by CANON and VOCAB.

### README

The human-readable description (`README.md`) of the scope's purpose and usage.
Required by triad but not validated for content.

---

**This VOCAB defines terms for the CANONIC root scope.**

---
