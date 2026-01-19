# CANONIC Language Specification

The formal grammar and semantics of the CANONIC governance language.

## Purpose

Define the complete language specification for CANONIC, enabling:
- Deterministic parsing of governance artifacts
- Automated validation of well-formedness
- Interoperability across implementations
- Version-controlled evolution

## Current Version

**v0.1** — Core Language (draft)

## Structure

```
/canonic/language/
├── CANON.md          # Language axioms (governance)
├── VOCAB.md          # Language vocabulary (semantics)
├── README.md         # This file (description)
├── LANGUAGE.md       # THE specification (closes scope)
└── COVERAGE.md       # Cross-language comparison & roadmap
```

**Note:** Following Go, Python, and Julia best practices, the specification is a single document ([LANGUAGE.md](LANGUAGE.md)) with inline version annotations, not a directory of files.

## Specification

**[LANGUAGE.md](LANGUAGE.md)** — The complete CANONIC Language Specification v0.1

Contents:
1. **Comparison with Other Languages** — Go, Python, Rust, C, Julia
2. **Lexical Grammar** — Tokens, identifiers, composition constraint
3. **Syntactic Grammar** — CANON, VOCAB, README, Series structure
4. **Semantic Rules** — Inheritance, introspection, closure
5. **Composition Rules** — Namespaces, scopes, series, stack
6. **Errors** — Lexical, syntactic, semantic, composition
7. **Validation** — Python pseudocode for validators
8. **Version History** — Changelog

## Coverage

**[COVERAGE.md](COVERAGE.md)** — How CANONIC compares to major language specifications

- Gap analysis vs. Go, Python, Rust, C, Julia
- What CANONIC uniquely contributes
- Roadmap to exceed them

## Version Roadmap

| Version | Scope | Status |
|---------|-------|--------|
| **v0.1** | Core language: lexical, syntactic, semantic, composition | Draft |
| **v0.2** | Domain extensions + rule identifiers + test suite | Planned |
| **v0.3** | Token economics: TOKEN, COIN grammar | Planned |
| **v1.0** | Stable release: conformance levels, formal proofs | Planned |

## Version History

| Version | Date | Freeze Tag | Status |
|---------|------|------------|--------|
| v0.1 | 2026-01-19 | `lang-v0.1` | Draft |

## v0.2 Preview: Domain Extensions

v0.2 will introduce domain-specific language extensions:

```
CANONIC.MED     → Healthcare governance (HIPAA, FDA, CMS)
CANONIC.LAW     → Legal governance (privilege, evidence)
CANONIC.FIN     → Financial governance (SEC, SOX, GAAP)
CANONIC.EDU     → Educational governance
CANONIC.GOV     → Government governance
```

Domain extensions inherit the core language and add domain-specific:
- Keywords (regulatory terms)
- Validators (compliance rules)
- Series prefixes (domain artifacts)

---

*CANONIC is closed.*
