# CANONIC (/)

**Version:** 0.3.0
**Date:** 2026-01-21
**Status:** ACTIVE

inherits: /

---

## 0. Results

| Metric | Status |
|--------|--------|
| Triad | Complete |
| Inheritance | Self-terminating at `/` |
| Introspection | All concepts defined |
| Compliance | ENTERPRISE |

---

## 1. Purpose

Define the constitutional foundation of the CANONIC paradigm.

CANONIC establishes the minimal structural and semantic laws that govern all downstream scopes. This specification is the root from which all governance inherits.

---

## 2. CANONBASE Architecture

The CANONBASE defines allowed scope placement. Scopes **MUST NOT** exist outside declared paths.

```
╔═══════════════════════════════════════════════════════════════╗
║ LAYER 1: GOVERNANCE (Constitutional Core)                     ║
║  /               ─── Root scope (this)                        ║
║  /templates/     ─── Template patterns                        ║
╚═══════════════════════════════════════════════════════════════╝
                           │
                           ▼
╔═══════════════════════════════════════════════════════════════╗
║ LAYER 2: LANGUAGE (Formal Specification)                      ║
║  /language/      ─── LANGUAGE specification                   ║
╚═══════════════════════════════════════════════════════════════╝
                           │
                           ▼
╔═══════════════════════════════════════════════════════════════╗
║ LAYER 3: MACHINE (Execution Semantics)                        ║
║  /machine/       ─── MACHINE (Authority, Eval, Decision)      ║
║  /machine/os/    ─── OS (operational rules)                   ║
╚═══════════════════════════════════════════════════════════════╝
                           │
                           ▼
╔═══════════════════════════════════════════════════════════════╗
║ LAYER 4: OPERATIONAL (Infrastructure)                         ║
║  /ledger/        ─── LEDGER (Git = immutable record)          ║
║  /validators/    ─── VALIDATORS (VaaS enforcement)            ║
║  /stack/         ─── STACK (multi-repo composition)           ║
║  /.github/       ─── APPSTORE (infra only, NO SCOPE)          ║
╚═══════════════════════════════════════════════════════════════╝
                           │
                           ▼
╔═══════════════════════════════════════════════════════════════╗
║ LAYER 5: PRODUCTION (Artifact Generation)                     ║
║  /writing/       ─── WRITING (epistemic layer)                ║
║  /paper/         ─── PAPER (manuscript production)            ║
║  /transcript/    ─── TRANSCRIPT (episode records)             ║
║  /publishing/    ─── PUBLISHING (release management)          ║
║  /patents/       ─── PATENTS (IP production)                  ║
╚═══════════════════════════════════════════════════════════════╝
                           │
                           ▼
╔═══════════════════════════════════════════════════════════════╗
║ LAYER 6: DOMAIN (Application Instances)                       ║
║  /companies/     ─── Business domain                          ║
║  /grants/        ─── Funding domain                           ║
║  /mammochat/     ─── Product domain                           ║
╚═══════════════════════════════════════════════════════════════╝
```

### 2.1 Blocked Paths

The following paths **MUST NOT** contain scopes (CANON.md):

| Path | Reason |
|------|--------|
| `/.github/` | Platform reserved (APPSTORE infra only) |
| `/.git/` | Git internals |
| `/.archive/` | Archived content (immutable) |
| `/node_modules/` | Dependencies |

### 2.2 Root Artifact Closure

Root scope artifacts are **closed** by compliance level:

| Artifact | Required By |
|----------|-------------|
| CANON.md | TRIAD |
| VOCAB.md | TRIAD |
| README.md | TRIAD |
| CANONIC.md | ENTERPRISE (SPEC) |
| COVERAGE.md | ENTERPRISE |
| ROADMAP.md | ENTERPRISE |

New artifacts at root **MUST NOT** be added without CANON amendment.

---

## 3. Normative Language

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as described in RFC 2119.

Statements using these key words are normative. Examples and diagrams are non-normative unless explicitly marked otherwise.

---

## 4. Principles

### 4.1 Structural Minimality

CANONIC defines the minimal structure required for a valid scope.

No constraints beyond those required for structure, inheritance, and semantic closure are imposed at this layer.

### 4.2 Governance Separation

CANONIC defines governance only.

- Enforcement is defined in MACHINE
- Execution is defined in OS
- Recording is defined in LEDGER
- Distribution is defined in APPSTORE

### 4.3 Abstraction

CANONIC defines semantic roles, not implementations.

Concrete tools and workflows are non-normative at this layer.

---

## 5. Constraints

### 5.1 Triad (Axiom 1)

A scope **MUST** contain: `CANON.md`, `VOCAB.md`, `README.md`.

Absence of any triad artifact renders the scope invalid.

### 5.2 Inheritance (Axiom 2)

Every `CANON.md` **MUST** declare `inherits:`.

- Inheritance **MUST** terminate at `/`
- Inherited axioms are final and **MUST NOT** be overridden

### 5.3 Introspection (Axiom 3)

`VOCAB.md` **MUST** define every concept used by CANON and VOCAB.

Undefined concepts render the scope invalid.

---

## 6. Validation

A CANONIC scope is valid if and only if:

```
VALID(scope) = triad(scope) ∧ inheritance(scope) ∧ introspection(scope)
```

Where:
- `triad(scope)` = CANON.md ∧ VOCAB.md ∧ README.md exist
- `inheritance(scope)` = inherits declared ∧ chain terminates at /
- `introspection(scope)` = all concepts in CANON/VOCAB are defined in VOCAB

---

## 7. Lifecycle

| Phase | State | Transition |
|-------|-------|------------|
| Draft | Mutable | Edit freely |
| Active | Mutable | Changes require validation |
| Frozen | Immutable | No changes permitted |

This scope is **ACTIVE**.

---

## 8. Consumption Notes

- Downstream scopes inherit these constraints without contradiction
- Additional constraints may be introduced downstream but must not violate CANONIC
- The LANGUAGE specification provides the complete grammar for all artifacts

---

**This SPEC defines the constitutional semantics of CANONIC.**
**Validity is defined exclusively by CANON.**

---
