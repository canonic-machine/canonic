# VOCAB (/canonic/language/)

inherits: /canonic/

---

## Axiom Concepts

### Versioned

Semantic versioning required for LANGUAGE releases.

---

### Ledger-Frozen

Each LANGUAGE version must pin to a ledger commit tag.

---

### Complete

Specification must cover lexical, syntactic, semantic, and composition rules.

---

### Self-Describing

LANGUAGE must be expressible in itself.

---

### Validator-Enforced

Each grammar rule must have a corresponding validator.

---

## Grammar Concepts

### lexical grammar

The rules defining tokens: identifiers, keywords, literals, operators, delimiters.

---

### syntactic grammar

The rules defining structure: how tokens combine into valid constructs.

---

### semantic rules

The rules defining meaning: type checking, scope resolution, constraint satisfaction.

---

### composition rules

The rules defining combination: how scopes compose into namespaces.

---

### token

The atomic unit of lexical analysis; an indivisible sequence of characters with meaning.

---

### identifier

A token naming an entity: scope, artifact, concept, axiom.

---

### keyword

A reserved identifier with fixed meaning in the grammar.

---

### literal

A token representing a constant value.

---

### operator

A token representing an operation or relationship.

---

### delimiter

A token marking boundaries between constructs.

---

## Semantic Primitives

### semantic primitive

An uppercase filename with fixed meaning across all scopes. CANONIC derives meaning through artifact naming. UPPERCASE = governance, lowercase = governed.

---

### case semantics

The fundamental case distinction in CANONIC: UPPERCASE denotes governance (the governor), lowercase denotes governed (the governed). CANON.md governs; services/ is governed.

---

### SCOPE

The meta-primitive. SCOPE contains all other primitives. SCOPE is not IN the hexad—SCOPE IS the hexad. A directory with governance artifacts. Provides: boundary, governance, semantics, description, closure, distribution, persistence, roadmap, full stack access. SCOPE contains SCOPE recursively.

---

### hexad

The six semantic primitives contained by SCOPE: { LEDGER, CANON, VOCAB, README, COVERAGE, APPSTORE }.

---

### LEDGER

Semantic primitive for persistence. Where state lives. Git is the instantiation; blockchain is an alternative. The foundation upon which all other primitives rest. Without LEDGER, no persistence. Without persistence, no governance.

---

### CANON

Semantic primitive for governance. CANON.md declares axioms (what MUST be).

---

### VOCAB

Semantic primitive for semantics. VOCAB.md defines terms (what words mean).

---

### README

Semantic primitive for description. README.md documents (what this is).

---

### COVERAGE

Semantic primitive for external closure. COVERAGE.md tracks completeness against external references (gaps + roadmap).

---

### DISTRIBUTION

Canonical: DISTRIBUTION
Aliases: APPSTORE

Semantic primitive for distribution. How CANONIC spreads. The full SCOPE of what CANONIC has to offer. GitHub is the instantiation. CANONIC is the first language specification with distribution embedded in the grammar. No external infrastructure required.

Distribution includes:
- LEDGER channels (persistent): GIT, PUBLISHING, PATENT
- ADVERTISING channels (ephemeral): LinkedIn, Medium, Twitter

---

### aaS

Commercial label for APPSTORE products derived from scope names (e.g., PAPERaaS,
GRANTaaS, BOOKaaS, COMPANYaaS, PATENTaaS, VALIDATORaaS). The double "aa" encodes
validator semantics (VALIDATORaaS). Labels are descriptive and do not change scope
naming.

---

### aaS mapping

The rule that maps a scope name to its product label:
`Singular(UPPERCASE(scope)) + aaS`.

---

### PAPERaaS

Paper-as-a-Service product label for the paper scope.

---

### GRANTaaS

Grant-as-a-Service product label for the grants scope.

---

### COMPANYaaS

Company-as-a-Service product label for the companies scope.

---

### PATENTaaS

Patent-as-a-Service product label for the patents scope.

---

### BOOKaaS

Book-as-a-Service product label for the books scope.

---

### VALIDATORaaS

Validator-as-a-Service product label for the validators scope.

---

### IMPORTaaS

Import-as-a-Service product label. Canonicalized import of protocanonic work
into a governed CANONIC scope.

---

### IaaS

Shorthand alias for IMPORTaaS.

---

### triad

The three required artifacts for a valid scope: CANON.md, VOCAB.md, README.md. Triad provides internal closure.

---

### tetrad

The triad plus COVERAGE.md. Tetrad provides complete closure (internal + external).

---

### pentad

The tetrad plus APPSTORE.md. Pentad provides complete closure + distribution.

---

### hexad

The pentad plus LEDGER. The full set of semantic primitives. SCOPE = hexad.

---

### internal closure

Satisfaction of triad requirement and vocabulary closure (introspection). A scope is internally closed when all axioms are satisfied and all concepts are defined.

---

### external closure

Satisfaction of COVERAGE requirements. A scope is externally closed when all gaps against external standards are closed.

---

### complete closure

Internal closure AND external closure. A scope is completely closed when it satisfies all internal requirements AND exceeds external references.

---

## Language Constructs

### namespace

A dot-separated path identifying a scope: `CANONIC.SERVICES.WRITING`.

---

### composition

The pattern of combining single-word identifiers with dots: `A.B.C`.

---

### scope identifier

A single lowercase word naming a directory: `services`, `writing`, `paper`.

---

### artifact identifier

An uppercase or mixed-case word naming a file: `CANON`, `VOCAB`, `README`.

---

### series identifier

A prefixed enumeration: `IDF-001`, `EP-042`, `PA-000`.

---

### modal verb

RFC 2119 normative keywords: MUST, SHALL, SHOULD, MAY, MUST NOT, SHALL NOT, SHOULD NOT.

---

## Validation Concepts

### well-formed

A construct that satisfies lexical and syntactic rules.

---

### valid

A construct that satisfies semantic rules.

---

### closed

A scope that satisfies all axioms in its governance chain.

---

### parse error

A violation of syntactic grammar.

---

### semantic error

A violation of semantic rules.

---

### composition error

A violation of composition rules (e.g., hyphenated names).

---

## Version Concepts

### semantic version

A version number in MAJOR.MINOR.PATCH format.

---

### MAJOR

Incremented for breaking changes to the grammar.

---

### MINOR

Incremented for backwards-compatible additions.

---

### PATCH

Incremented for backwards-compatible fixes.

---

### freeze tag

A git tag marking a version: `lang-v1.0.0`.

---
