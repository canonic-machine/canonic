# NOMENCLATURE — SPEC

inherits: /CANONIC/language/

---

## Purpose

Defines identity and naming rules for all governed artifacts.

Prevents ambiguity, aliasing, and cross-domain authority leakage.

---

## Identity

An artifact's identity IS its full inheritance path:

```
/CANONIC/language/nomenclature/
```

This path is:
- Unique (no two artifacts share a path)
- Authoritative (the path determines governance)
- Immutable (renaming changes identity)

---

## Naming Rules

| Rule | Rationale |
|------|-----------|
| No abbreviations | "D" has no authority; "Declarative" does |
| No aliases | "DETROS" is mnemonic, not authoritative |
| No synonyms | One name per concept |
| Path-scoped authority | `/a/foo` and `/b/foo` are unrelated |
| No quotation authority | Citing doesn't inherit |

---

## Authority Leakage

Authority leakage occurs when:
- A name is used outside its path
- An alias is treated as authoritative
- Quotation is mistaken for inheritance

The nomenclature rules prevent all three.

---

## Namespace Organization

Artifacts are organized into namespaces following `{org}/{REPO}` convention:

| Component | Case | Role |
|-----------|------|------|
| org | lower | Namespace owner (e.g., `canonic-domains`) |
| REPO | UPPER | Independently versioned artifact |
| path | lower | Directory within repo |

Example disambiguation:

| Full Path | Meaning |
|-----------|---------|
| `canonic-appstore/MAMMOCHAT` | Certified app listing |
| `canonic-adventhealth/MAMMOCHAT` | Enterprise deployment |
| `canonic-papers/MAMMOCHAT` | Publication |

Same repo name across orgs = distinct artifacts with no shared authority.

The org prefix establishes:
- Ownership boundary
- Version independence
- Access control scope

---

## Validation

A nomenclature violation occurs when:
- An artifact uses undefined terms
- An artifact uses abbreviated terms
- An artifact claims authority outside its path

---
