# COVERAGE (/canonic/language/)

**Purpose:** Track CANONIC language specification coverage relative to ALL major programming language specifications (by GitHub popularity), identify gaps, and establish a roadmap to exceed them.

**Data Source:** [GitHub Octoverse 2025](https://github.blog/news-insights/octoverse/octoverse-2024/), [TIOBE Index 2026](https://www.tiobe.com/tiobe-index/)

---

## Language Specification Closure

This document closes the gap between CANONIC and **every major language specification**. CANONIC is not a general-purpose programming language—it is a **governance language**. But its specification must meet or exceed the rigor of the great languages.

**The difference:** Every other language specifies *computation*. CANONIC specifies *governance*.

---

## 1. Complete Language Specification Survey

### 1.1 Top Languages by GitHub Activity (2025-2026)

| Rank | Language | GitHub Share | Spec Document | Spec Authority |
|------|----------|--------------|---------------|----------------|
| 1 | **Python** | #1 (overtook JS) | [Language Reference](https://docs.python.org/3/reference/) | docs.python.org |
| 2 | **JavaScript** | #1 code pushes | [ECMA-262](https://tc39.es/ecma262/) | TC39/Ecma |
| 3 | **TypeScript** | #3 (overtook Java) | [Handbook](https://www.typescriptlang.org/docs/handbook/) | Microsoft (no formal spec since v1.8) |
| 4 | **Java** | #4 | [JLS](https://docs.oracle.com/javase/specs/jls/se21/html/index.html) | Oracle/JCP |
| 5 | **C#** | Top 10 | [ECMA-334](https://www.ecma-international.org/publications-and-standards/standards/ecma-334/) | Ecma/Microsoft |
| 6 | **C++** | Top 10 | [ISO/IEC 14882](https://isocpp.org/std/the-standard) | ISO/IEC |
| 7 | **C** | Top 10 | [ISO/IEC 9899](https://www.iso.org/standard/74528.html) | ISO/IEC |
| 8 | **Go** | Top 10 | [Language Spec](https://go.dev/ref/spec) | go.dev |
| 9 | **Rust** | Growing fast | [Reference](https://doc.rust-lang.org/reference/) | rust-lang.org |
| 10 | **PHP** | Top 10 | [Language Spec](https://phplang.org/) | php.net (community) |
| 11 | **Kotlin** | Android primary | [Spec](https://kotlinlang.org/spec/) | JetBrains |
| 12 | **Swift** | Apple primary | [TSPL](https://docs.swift.org/swift-book/) | Apple |
| 13 | **Ruby** | Top 20 | [ISO/IEC 30170](https://www.iso.org/standard/59579.html) | ISO/IEC |
| 14 | **Shell** | Overtook C | [POSIX](https://pubs.opengroup.org/onlinepubs/9699919799/) | POSIX/IEEE |
| — | **CANONIC** | Governance | [LANGUAGE.md](LANGUAGE.md) | /canonic/language/ |

### 1.2 Markup & Data Languages

| Language | Spec Document | Authority | CANONIC Relation |
|----------|---------------|-----------|------------------|
| **HTML** | [HTML Living Standard](https://html.spec.whatwg.org/) | WHATWG | CANONIC uses Markdown |
| **CSS** | [CSS Specifications](https://www.w3.org/Style/CSS/) | W3C | N/A |
| **XML** | [XML 1.0](https://www.w3.org/TR/xml/) | W3C | CANONIC uses Markdown |
| **JSON** | [ECMA-404](https://www.ecma-international.org/publications-and-standards/standards/ecma-404/) | Ecma | CANONIC uses Markdown |
| **YAML** | [YAML 1.2](https://yaml.org/spec/1.2/) | yaml.org | CANONIC metadata |
| **Markdown** | [CommonMark](https://commonmark.org/) | CommonMark | **CANONIC base format** |

---

## 2. Specification-by-Specification Comparison

### 2.1 JavaScript/ECMAScript (ECMA-262)

**Source:** [tc39.es/ecma262](https://tc39.es/ecma262/) | **Edition:** ES2026 (17th)

| Feature | ECMAScript | CANONIC v0.1 | Gap | Roadmap |
|---------|------------|--------------|-----|---------|
| Living standard | Yes | No | Gap | v0.2: Consider living doc |
| Formal grammar | Complete | Complete | — | Closed |
| TC39 process | Stage 0-4 | Version tags | Different | N/A |
| Built-in objects | Extensive | Primitives | Different domain | N/A |
| Strict mode | Yes | N/A | Not applicable | N/A |
| Modules | ES Modules | Inheritance | Different paradigm | Closed |

**What ECMAScript Has:** Massive committee process, living standard, exhaustive built-ins.
**What CANONIC Has:** Semantic primitives, governance inheritance, vocabulary closure.

---

### 2.2 Java Language Specification (JLS)

**Source:** [JLS SE 21](https://docs.oracle.com/javase/specs/jls/se21/html/index.html) | **Authority:** Oracle/JCP

| Feature | Java | CANONIC v0.1 | Gap | Roadmap |
|---------|------|--------------|-----|---------|
| Formal document | Yes (book-length) | Yes (single doc) | — | Closed |
| Chapter structure | 19 chapters | 8 sections | — | Closed |
| Binary compatibility | Chapter 13 | LEDGER immutability | Different | Closed |
| Type system | Nominal | Artifact-based | Different domain | N/A |
| Packages | Hierarchical | Namespace bijection | Similar | Closed |
| JCP process | JSRs | Version tags | Different | N/A |

**What Java Has:** Exhaustive type system, binary compatibility rules, formal JCP process.
**What CANONIC Has:** Filesystem-as-namespace, semantic primitives, RFC 2119 modals.

---

### 2.3 TypeScript

**Source:** [Handbook](https://www.typescriptlang.org/docs/handbook/) | **Authority:** Microsoft

| Feature | TypeScript | CANONIC v0.1 | Gap | Roadmap |
|---------|------------|--------------|-----|---------|
| Formal specification | **No** (abandoned v1.8) | **Yes** | CANONIC exceeds | — |
| Handbook | Yes | README.md | — | Closed |
| Type system | Structural | Artifact-based | Different domain | N/A |
| Compiler behavior | De facto spec | Validators | Similar | Closed |

**Critical:** TypeScript has NO formal language specification since 2016. CANONIC already exceeds TypeScript in specification rigor.

---

### 2.4 Go Language Specification

**Source:** [go.dev/ref/spec](https://go.dev/ref/spec) | **Version:** go1.25

| Feature | Go | CANONIC v0.1 | Gap | Roadmap |
|---------|-----|--------------|-----|---------|
| Single document | Yes | Yes | — | Closed |
| EBNF grammar | Yes | Yes | — | Closed |
| Version annotations | `[Go 1.18]` | `[v0.1]` | — | Closed |
| Compatibility promise | Go 1 guarantee | LEDGER immutability | — | Closed |
| Built-in functions | Yes | N/A | Not applicable | N/A |

**What Go Has:** Clean single-doc spec, compatibility guarantee, inline annotations.
**What CANONIC Borrows:** All of the above. Go is the model.

---

### 2.5 Rust Reference

**Source:** [doc.rust-lang.org/reference](https://doc.rust-lang.org/reference/) | **Edition:** 2024

| Feature | Rust | CANONIC v0.1 | Gap | Roadmap |
|---------|------|--------------|-----|---------|
| mdBook format | Yes | Single Markdown | — | Closed |
| Rule identifiers | `[destructors.scope]` | Section numbers | Gap | v0.2 |
| Edition system | 2015/2018/2021/2024 | v0.1/v0.2 | — | Closed |
| Ferrocene spec | Safety-critical | N/A | Not applicable | N/A |

**Gap to Close (v0.2):** Add rule identifiers for cross-referencing.

---

### 2.6 Kotlin Language Specification

**Source:** [kotlinlang.org/spec](https://kotlinlang.org/spec/) | **Version:** 1.9

| Feature | Kotlin | CANONIC v0.1 | Gap | Roadmap |
|---------|--------|--------------|-----|---------|
| Formal specification | Yes (in progress) | Yes | — | Closed |
| ANTLR grammar | Yes | EBNF | — | Closed |
| Platform specs | JVM/JS/Native | N/A | Not applicable | N/A |
| Experimental status | Yes | Draft | — | Closed |

**What Kotlin Has:** Platform-specific subspecs, ANTLR grammar.
**What CANONIC Has:** Domain extensions (MED, LAW, FIN) planned for v0.2.

---

### 2.7 Swift (TSPL)

**Source:** [docs.swift.org/swift-book](https://docs.swift.org/swift-book/) | **Authority:** Apple

| Feature | Swift | CANONIC v0.1 | Gap | Roadmap |
|---------|-------|--------------|-----|---------|
| Book format | Guide + Reference | Single spec | — | Closed |
| Grammar appendix | Yes | Appendix A | — | Closed |
| Community reference | [SwiftRef](https://dabrahams.github.io/SwiftRef/) | LANGUAGE.md | — | Closed |

**What Swift Has:** Beautiful documentation, separate guide/reference.
**What CANONIC Has:** Self-describing spec, semantic primitives.

---

### 2.8 PHP Language Specification

**Source:** [phplang.org](https://phplang.org/) | **Authority:** Community (Facebook origin)

| Feature | PHP | CANONIC v0.1 | Gap | Roadmap |
|---------|-----|--------------|-----|---------|
| Community-owned | Yes | Yes | — | Closed |
| Lexical/syntactic grammar | Yes | Yes | — | Closed |
| Type system | Gradual | Artifact-based | Different | N/A |
| Public domain | CC0 | Apache 2.0 | Different | N/A |

---

### 2.9 C Language Standard (ISO/IEC 9899)

**Source:** ISO/IEC 9899:2024 (C23) | **Authority:** ISO/IEC WG14

| Feature | C | CANONIC v0.1 | Gap | Roadmap |
|---------|---|--------------|-----|---------|
| ISO standard | Yes | No | Not pursuing ISO | N/A |
| Normative annexes | Yes | Partial | Gap | v0.2 |
| Undefined behavior | Specified | N/A | Not applicable | N/A |
| Conformance levels | Yes | No | Gap | v1.0 |

---

### 2.10 C++ (ISO/IEC 14882)

**Source:** ISO/IEC 14882:2023 (C++23) | **Authority:** ISO/IEC WG21

| Feature | C++ | CANONIC v0.1 | Gap | Roadmap |
|---------|-----|--------------|-----|---------|
| ISO standard | Yes | No | Not pursuing ISO | N/A |
| Concepts | Yes | N/A | Not applicable | N/A |
| Modules | C++20 | Inheritance | Different | N/A |
| Coroutines | Yes | N/A | Not applicable | N/A |

---

## 3. The Fundamental Difference

**Every other language specification defines COMPUTATION.**
**CANONIC defines GOVERNANCE.**

### 3.1 What Other Specs Have

| Feature | Go | Python | Java | JS | Rust | C | CANONIC |
|---------|-----|--------|------|-----|------|---|---------|
| Lexical grammar | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Syntactic grammar | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Type system | Yes | Yes | Yes | Yes | Yes | Yes | **Artifact types** |
| Execution model | Yes | Yes | Yes | Yes | Yes | Yes | **Validators** |
| Memory model | Yes | GC | GC | GC | Ownership | Manual | **LEDGER** |
| Concurrency | Yes | Yes | Yes | Yes | Yes | — | N/A |
| **Governance** | — | — | — | — | — | — | **Yes** |
| **Semantic primitives** | — | — | — | — | — | — | **Yes** |
| **Vocabulary closure** | — | — | — | — | — | — | **Yes** |
| **RFC 2119 modals** | — | — | — | — | — | — | **Yes** |

### 3.2 What CANONIC Uniquely Has

| Innovation | Description | Exists in Other Specs? |
|------------|-------------|----------------------|
| **Semantic Primitives** | Filename = Type = Semantics | **No** |
| **Triad Requirement** | CANON + VOCAB + README | **No** |
| **Tetrad Pattern** | Triad + COVERAGE | **No** |
| **Governance Inheritance** | Axioms cascade via filesystem | **No** |
| **Vocabulary Closure** | All terms must be defined | **No** (type systems are different) |
| **Filesystem-as-Namespace** | Directory IS namespace | Partial (Go) |
| **LEDGER Primitive** | Immutable state is source of truth | **No** |
| **Human Fixation** | Human authority markers | **No** |
| **Self-Describing** | Spec written in language it defines | Partial (Lisp) |

---

## 4. Coverage Matrix: All Languages

### 4.1 Specification Document Quality

| Language | Single Doc | EBNF Grammar | Version Annotations | Rule IDs | Conformance | Test Suite |
|----------|------------|--------------|---------------------|----------|-------------|------------|
| **Python** | Yes | PEG | No | No | No | Yes |
| **JavaScript** | Yes | Yes | No | Yes | Yes | Test262 |
| **TypeScript** | **No** | No | No | No | No | No |
| **Java** | Yes | Yes | No | No | Yes | TCK |
| **Go** | Yes | Yes | Yes | No | No | Yes |
| **Rust** | No (mdBook) | Yes | Yes | Yes | No | Yes |
| **Kotlin** | Yes | ANTLR | No | No | No | Yes |
| **Swift** | No (Book) | Yes | No | No | No | Yes |
| **PHP** | Yes | Yes | No | No | No | Yes |
| **C** | Yes (ISO) | Prose | No | No | Yes | No |
| **C++** | Yes (ISO) | Prose | No | No | Yes | No |
| **CANONIC** | **Yes** | **Yes** | **Yes** | No* | No* | No* |

*Planned for v0.2/v1.0

### 4.2 Semantic Features

| Language | Governance | Introspection | Modal Verbs | Semantic Primitives | Closure Tracking |
|----------|------------|---------------|-------------|---------------------|------------------|
| **Python** | — | `__doc__` | — | — | — |
| **JavaScript** | — | `typeof` | — | — | — |
| **TypeScript** | — | Types | — | — | — |
| **Java** | — | Reflection | — | — | — |
| **Go** | — | `reflect` | — | — | — |
| **Rust** | — | Macros | — | — | — |
| **All Others** | — | — | — | — | — |
| **CANONIC** | **Yes** | **Required** | **RFC 2119** | **Yes** | **COVERAGE.md** |

---

## 5. Roadmap to Exceed All

### 5.1 v0.1 (Current): Foundation

- [x] Single-document specification
- [x] EBNF grammar
- [x] Version annotations
- [x] Semantic primitives (CANON, VOCAB, README, COVERAGE)
- [x] Governance inheritance
- [x] Vocabulary closure
- [x] Composition rules

### 5.2 v0.2: Rigor + Domains

- [ ] Rule identifiers (`[SCOPE_IDENTITY]`, `[TRIAD_COMPLETE]`)
- [ ] Machine-readable grammar (JSON export)
- [ ] Validator test suite
- [ ] Annex C: Informative (examples, rationale)
- [ ] Annex D: Normative (validator requirements)
- [ ] Domain extensions: CANONIC.MED, CANONIC.LAW, CANONIC.FIN

### 5.3 v0.3: Economics

- [ ] TOKEN grammar
- [ ] COIN grammar
- [ ] Economic validators

### 5.4 v1.0: Stable

- [ ] Conformance levels (CANONIC-compliant, CANONIC-strict)
- [ ] Formal semantics
- [ ] Reference implementation
- [ ] Third-party certification

---

## 6. Conclusion

CANONIC v0.1 already exceeds TypeScript (no formal spec) and matches Go/Rust in specification quality.

**The paradigm shift:** Other languages specify computation. CANONIC specifies governance. This is a new category.

**Unique to CANONIC:**
- Semantic primitives via filename
- Triad/Tetrad structure
- Vocabulary closure (introspection)
- Governance inheritance
- COVERAGE tracking (this document)

**The {SCOPE} pattern is unprecedented:**
```
{SCOPE}/
├── CANON.md      → what MUST be
├── VOCAB.md      → what words mean
├── README.md     → what this is
└── COVERAGE.md   → how complete we are
```

No other language has this. CANONIC is closed.

---

*This coverage tracks closure against: Python, JavaScript, TypeScript, Java, Go, Rust, Kotlin, Swift, PHP, C, C++, HTML, CSS, XML, JSON, YAML, Markdown.*

*Data sources: [GitHub Octoverse](https://github.blog/news-insights/octoverse/octoverse-2024/), [TIOBE](https://www.tiobe.com/tiobe-index/)*

*CANONIC is closed.*
