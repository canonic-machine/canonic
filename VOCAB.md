# VOCAB (/)

inherits: /

---

## Core Concepts

### scope

A directory containing `CANON.md` that defines governance boundaries.
Scopes inherit from parent scopes via explicit declaration.

### triad

The minimum governance artifact set: `CANON.md`, `VOCAB.md`, `README.md`.
Absence of any triad artifact renders the scope invalid.

### inheritance

The governance chain from scope to root.
Every `CANON.md` MUST declare `inherits:`. Terminates at `/`.

### introspection

Vocabulary closure: all concepts in CANON and VOCAB must be defined.
Undefined concepts render the scope invalid.

### axiom

A normative governance rule declared in CANON.
Axioms use RFC 2119 keywords (MUST, SHOULD, MAY) to express requirements.

### final

An inherited constraint that cannot be overridden by downstream scopes.

### invalid

A scope state that fails validation against its governing axioms.

---

## Artifacts

### CANON

The normative governance artifact (`CANON.md`) declaring axioms and inheritance.
Validity is defined exclusively by CANON.

### VOCAB

The vocabulary artifact (`VOCAB.md`) defining all concepts used by the scope.
MUST define every concept used by CANON and VOCAB.

### README

The descriptive artifact (`README.md`) documenting the scope's purpose and usage.
Required by triad but not validated for content.

### SPEC

The formal specification artifact (`{SCOPE_NAME}.md`) that closes a scope.
Required for BUSINESS and ENTERPRISE compliance.

### COVERAGE

The internal closure artifact tracking axiom coverage and implementation status.
Required for ENTERPRISE compliance.

### ROADMAP

The external closure artifact tracking strategic milestones and integration targets.
Required for ENTERPRISE compliance.

---

## Compliance

### compliance

The level of governance completeness a scope maintains.
Ordered tiers: COMMUNITY, BUSINESS, ENTERPRISE.

### COMMUNITY

Compliance tier requiring only the TRIAD (CANON, VOCAB, README).

### BUSINESS

Compliance tier requiring TRIAD + SPEC.

### ENTERPRISE

Compliance tier requiring TRIAD + SPEC + COVERAGE + ROADMAP.

### concept

A term used in CANON or VOCAB that must be defined in VOCAB for introspection.

### artifact

A governed file within a scope (CANON.md, VOCAB.md, README.md, SPEC, etc.).

---
