# LANGUAGE (/canonic/language/)

**Version:** 0.1 (Draft)
**Date:** 2026-01-19
**Freeze:** `lang-v0.1` (pending)

inherits: /canonic/

---

## Preface

This document is the formal specification of the CANONIC governance language. It defines the complete lexical grammar, syntactic grammar, semantic rules, and composition rules that govern all CANONIC artifacts.

CANONIC is a **domain-specific language for governance**. Unlike general-purpose programming languages, CANONIC governs the structure, inheritance, and validity of governance artifacts stored in LEDGER (git is one instantiation; blockchain is another).

### Notation

This specification uses Extended Backus-Naur Form (EBNF) for grammar definitions:

```
Production  ::= Name '::=' Expression
Expression  ::= Term ('|' Term)*
Term        ::= Factor+
Factor      ::= Name | Literal | '(' Expression ')' | Factor ('*' | '+' | '?')
```

Version annotations like `[v0.1]` indicate when features were introduced.

---

## 1. Comparison with Other Language Specifications

### 1.1 Specification Landscape

| Language | Specification | Structure | Versioning | Authority |
|----------|--------------|-----------|------------|-----------|
| **Go** | [The Go Programming Language Specification](https://go.dev/ref/spec) | Single document | Inline annotations `[Go 1.18]` | go.dev |
| **Python** | [The Python Language Reference](https://docs.python.org/3/reference/) | Single document | By release (3.14, 3.15) | docs.python.org |
| **Rust** | [The Rust Reference](https://doc.rust-lang.org/reference/) | mdBook chapters | By edition (2021, 2024) | rust-lang.org |
| **C** | ISO/IEC 9899 | ISO standard document | By year (C99, C11, C23) | ISO/IEC |
| **Julia** | [Julia Documentation](https://docs.julialang.org/en/v1/) | Single manual | By major version | julialang.org |
| **CANONIC** | This document | Single document | Semantic (v0.1, v0.2) | /canonic/language/ |

### 1.2 Key Differences

**CANONIC vs. Go/Python/Rust/C:**

| Aspect | General-Purpose Languages | CANONIC |
|--------|--------------------------|---------|
| **Domain** | Computation | Governance |
| **Execution** | Runtime/compiled | Validation-time |
| **Artifacts** | Source files (.go, .py, .rs, .c) | Governance files (CANON.md, VOCAB.md) |
| **Type System** | Data types | Artifact types (Governance, Vocabulary, Description) |
| **Inheritance** | Classes/traits | Scope inheritance via filesystem |
| **Composition** | Modules/packages | Namespace composition (dot notation) |
| **Validation** | Compiler/interpreter | VALIDATORS |
| **Versioning** | Compiler versions | Ledger-frozen tags |

**What CANONIC Borrows:**

- **From Go**: Single-document specification, inline version annotations, composition via dot notation
- **From Python**: English prose for semantics (not purely formal), EBNF for syntax
- **From Rust**: Edition-based evolution, rule identifiers for cross-referencing
- **From C**: Normative vs. informative sections, undefined behavior specification
- **From RFC 2119**: Modal verb semantics (MUST, SHALL, SHOULD, MAY)

### 1.3 Unique to CANONIC

1. **Semantic Primitives**: Uppercase filenames have fixed meaning (CANON, VOCAB, README, COVERAGE)
2. **Triad Requirement**: Every scope requires three artifacts (CANON.md, VOCAB.md, README.md)
3. **Tetrad Pattern**: COVERAGE.md extends triad for external closure tracking
4. **Vocabulary Closure**: Terms must be defined before use (introspection)
5. **Filesystem-as-Namespace**: Directory structure IS the namespace hierarchy
6. **LEDGER Primitive**: Immutable state is the canonical source of truth
7. **Human Fixation**: Governance requires human authority markers

---

## 2. Lexical Grammar

### 2.1 Source Text

```
SourceCharacter ::= <any Unicode code point>
```

CANONIC source text is UTF-8 encoded Unicode. `[v0.1]`

```
LineTerminator ::= <LF> | <CR> | <CR><LF>
LF  ::= U+000A
CR  ::= U+000D

Whitespace ::= <SP> | <TAB>
SP  ::= U+0020
TAB ::= U+0009
```

### 2.2 Tokens

```
Token ::= Identifier | Keyword | Literal | Operator | Delimiter | Comment
```

#### 2.2.1 Identifiers

```
Identifier ::= ScopeIdentifier | ArtifactIdentifier | SeriesIdentifier | ConceptIdentifier

ScopeIdentifier    ::= LowerWord
ArtifactIdentifier ::= UpperWord
SeriesIdentifier   ::= Prefix '-' Number
ConceptIdentifier  ::= LowerWord | MixedWord

LowerWord ::= LowerLetter (LowerLetter | Digit)*
UpperWord ::= UpperLetter (UpperLetter | Digit)*
MixedWord ::= Letter (Letter | Digit)*

Prefix ::= UpperLetter UpperLetter UpperLetter?
Number ::= Digit Digit Digit

Letter      ::= UpperLetter | LowerLetter
UpperLetter ::= 'A'..'Z'
LowerLetter ::= 'a'..'z'
Digit       ::= '0'..'9'
```

**Examples:**
| Type | Examples |
|------|----------|
| ScopeIdentifier | `services`, `writing`, `paper`, `ledger` |
| ArtifactIdentifier | `CANON`, `VOCAB`, `README`, `SPEC` |
| SeriesIdentifier | `IDF-001`, `EP-042`, `PA-000`, `TE-003` |
| ConceptIdentifier | `axiom`, `scope`, `triad`, `canonification` |

#### 2.2.2 Keywords

```
Keyword ::= ModalKeyword | StructuralKeyword | InheritanceKeyword

ModalKeyword ::= 'MUST' | 'MUST NOT' | 'SHALL' | 'SHALL NOT'
              | 'SHOULD' | 'SHOULD NOT' | 'REQUIRED'
              | 'RECOMMENDED' | 'MAY' | 'OPTIONAL'

StructuralKeyword ::= 'inherits' | 'Axioms' | 'Canonical' | 'Aliases'

InheritanceKeyword ::= '/' | '..'
```

Modal keywords follow [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt) semantics. `[v0.1]`

#### 2.2.3 Literals

```
Literal ::= StringLiteral | NumberLiteral | PathLiteral

StringLiteral    ::= '"' StringCharacter* '"' | "'" StringCharacter* "'"
StringCharacter  ::= SourceCharacter - ('"' | "'" | '\' | LineTerminator)
                   | EscapeSequence

NumberLiteral    ::= Digit+

PathLiteral      ::= '/' (PathSegment '/')* PathSegment?
PathSegment      ::= (Letter | Digit)+
```

**Note:** PathSegment does NOT allow hyphens or underscores. `[v0.1]`

#### 2.2.4 Operators

```
Operator ::= CompositionOperator | RelationOperator | MarkdownOperator

CompositionOperator ::= '.'

RelationOperator    ::= ':' | '→' | '←' | '=' | '!='

MarkdownOperator    ::= '**' | '*' | '`' | '```' | '#'+ | '|' | '-'
```

#### 2.2.5 Delimiters

```
Delimiter ::= '(' | ')' | '[' | ']' | '{' | '}' | ',' | ';' | '---'
```

#### 2.2.6 Comments

```
Comment ::= LineComment | BlockComment | HTMLComment

LineComment  ::= '//' SourceCharacter* LineTerminator
BlockComment ::= '/*' CommentCharacter* '*/'
HTMLComment  ::= '<!--' CommentCharacter* '-->'

CommentCharacter ::= SourceCharacter - ('*/' | '-->')
```

### 2.3 Composition Tokens

```
Namespace ::= RootNamespace | QualifiedNamespace

RootNamespace      ::= 'CANONIC'
QualifiedNamespace ::= RootNamespace ('.' UpperWord)+
```

**Examples:**
- `CANONIC`
- `CANONIC.SERVICES`
- `CANONIC.SERVICES.WRITING`
- `CANONIC.MED.ONCO.MAMMO`

#### 2.3.1 Composition Constraint `[v0.1]`

```
CompositionConstraint ::= SingleWord | DotComposition

SingleWord     ::= Letter+
DotComposition ::= SingleWord ('.' SingleWord)*
```

**Critical Rule:** Identifiers **MUST NOT** contain hyphens, underscores, or spaces.

| Status | Example | Reason |
|--------|---------|--------|
| ✓ Valid | `services` | Single word |
| ✓ Valid | `CANONIC.SERVICES` | Dot composition |
| ✗ Invalid | `canonic-services` | Hyphen forbidden |
| ✗ Invalid | `canonic_services` | Underscore forbidden |
| ✗ Invalid | `canonic services` | Space forbidden |

### 2.4 Reserved Words

The following identifiers are reserved and **MUST NOT** be used as user-defined names:

**Structural:** `CANON`, `VOCAB`, `README`, `COVERAGE`, `SPEC`, `LANGUAGE`, `inherits`, `Axioms`, `Canonical`, `Aliases`

**Modal (RFC 2119):** `MUST`, `SHALL`, `SHOULD`, `MAY`, `REQUIRED`, `RECOMMENDED`, `OPTIONAL`

**Gate:** `TRIAD`, `INHERITANCE`, `INTROSPECTION`, `ROOT`, `VALIDATORS`, `SERVICES`, `MACHINE`, `OS`, `LEDGER`

---

## 3. Syntactic Grammar

### 3.1 Document Structure

```
GovernanceDocument ::= CANONDocument | VOCABDocument | READMEDocument | SPECDocument

CANONDocument  ::= Header InheritanceDeclaration '---' AxiomSection*
VOCABDocument  ::= Header InheritanceDeclaration '---' TermSection*
READMEDocument ::= Header DescriptionSection*
SPECDocument   ::= Header InheritanceDeclaration '---' SpecificationSection*
```

#### 3.1.1 Header

```
Header ::= '#' Whitespace ScopeName Whitespace? '(' PathLiteral ')' LineTerminator

ScopeName ::= UpperWord | MixedWord
```

**Examples:**
```markdown
# CANON (/canonic/services/)
# VOCAB (/canonic/language/)
# WRITING (/canonic/services/writing/)
```

#### 3.1.2 Inheritance Declaration

```
InheritanceDeclaration ::= 'inherits:' Whitespace PathLiteral LineTerminator
```

**Examples:**
```markdown
inherits: /
inherits: /canonic/
inherits: /canonic/services/
```

### 3.2 CANON Structure

```
AxiomSection ::= '---' LineTerminator
                 '##' Whitespace 'Axioms' LineTerminator
                 AxiomDefinition+

AxiomDefinition ::= '###' Whitespace AxiomNumber '.' Whitespace AxiomName LineTerminator
                    LineTerminator
                    AxiomBody
                    LineTerminator

AxiomNumber ::= Digit+
AxiomName   ::= Word (Whitespace Word)*
AxiomBody   ::= Statement+
```

#### 3.2.1 Statement

```
Statement ::= NormativeStatement | DescriptiveStatement

NormativeStatement ::= Subject Whitespace ModalVerb Whitespace Predicate '.'

ModalVerb ::= '**MUST**' | '**MUST NOT**' | '**SHALL**' | '**SHALL NOT**'
            | '**SHOULD**' | '**SHOULD NOT**' | '**MAY**'

Subject   ::= Identifier | 'A' Whitespace Identifier | 'The' Whitespace Identifier
Predicate ::= Word+
```

**Example:**
```markdown
### 1. Triad

A scope **MUST** contain: `CANON.md`, `VOCAB.md`, `README.md`.
```

### 3.3 VOCAB Structure

```
TermSection ::= '##' Whitespace CategoryName LineTerminator
                TermDefinition+

CategoryName ::= Word (Whitespace Word)*

TermDefinition ::= '###' Whitespace TermName LineTerminator
                   LineTerminator
                   TermBody
                   LineTerminator

TermName ::= ConceptIdentifier
TermBody ::= Paragraph+
```

#### 3.3.1 Canonical Form

```
CanonicalDeclaration ::= 'Canonical:' Whitespace TermName LineTerminator

AliasDeclaration ::= 'Aliases:' Whitespace AliasList LineTerminator
AliasList        ::= Alias (',' Whitespace Alias)*
Alias            ::= TermName (Whitespace '(deprecated)')?
```

**Example:**
```markdown
### axiom

Canonical: axiom
Aliases: rule (deprecated), constraint

A normative rule declared in CANON.
```

### 3.4 COVERAGE Structure `[v0.1]`

```
COVERAGEDocument ::= COVERAGEHeader Metadata? '---' SurveySection ComparisonSection*
                     DifferenceSection CoverageMatrix RoadmapSection Conclusion

COVERAGEHeader ::= '#' Whitespace 'COVERAGE' Whitespace '(' PathLiteral ')' LineTerminator

Metadata ::= '**Purpose:**' Whitespace Description LineTerminator
           ('**Data Source:**' Whitespace SourceList LineTerminator)?

SurveySection ::= '##' Whitespace SurveyTitle LineTerminator
                  ExternalReferenceTable+

ComparisonSection ::= '##' Whitespace ComparisonTitle LineTerminator
                      '**Source:**' Whitespace URL LineTerminator
                      FeatureTable
                      Analysis

DifferenceSection ::= '##' Whitespace 'The Fundamental Difference' LineTerminator
                      UniqueFeatureTable

CoverageMatrix ::= '##' Whitespace 'Coverage Matrix' LineTerminator
                   FeatureComparisonTable+

RoadmapSection ::= '##' Whitespace 'Roadmap' LineTerminator
                   VersionedTodoList+

Conclusion ::= '##' Whitespace 'Conclusion' LineTerminator
               ClosureStatement

FeatureTable ::= TableHeader TableSeparator TableRow+
TableRow ::= '|' Feature '|' External '|' Internal '|' Gap '|' Roadmap '|'
Gap ::= '—' | 'Gap' | 'Not applicable' | 'Different'
Roadmap ::= '—' | 'Closed' | 'v' Version | 'N/A'
```

**Example:**
```markdown
# COVERAGE (/canonic/language/)

**Purpose:** Track coverage relative to external standards.

---

## 1. External Survey

| Language | Spec | Authority |
|----------|------|-----------|
| Go | go.dev/ref/spec | go.dev |

## 2. Go Comparison

**Source:** go.dev/ref/spec

| Feature | Go | CANONIC | Gap | Roadmap |
|---------|-----|---------|-----|---------|
| EBNF | Yes | Yes | — | Closed |

## 3. The Fundamental Difference

| Feature | Others | CANONIC |
|---------|--------|---------|
| Governance | — | **Yes** |

## 4. Coverage Matrix

| Feature | Go | Python | CANONIC |
|---------|-----|--------|---------|
| Grammar | Yes | Yes | Yes |

## 5. Roadmap

### v0.2
- [ ] Rule identifiers

## 6. Conclusion

CANONIC is closed.
```

**COVERAGE Constraints:**
- Header **MUST** match `# COVERAGE (path)`
- **MUST** have at least one external reference table
- **MUST** have gap analysis (Gap column)
- **MUST** have roadmap with version targets
- **MUST** conclude with closure statement

---

### 3.5 Series Artifact Structure

```
SeriesDocument ::= SeriesHeader Metadata '---' Content

SeriesHeader     ::= '#' Whitespace SeriesIdentifier ':' Whitespace Title LineTerminator
SeriesIdentifier ::= Prefix '-' Number
Title            ::= Word (Whitespace Word)*

Metadata      ::= MetadataField+
MetadataField ::= '**' FieldName ':**' Whitespace FieldValue LineTerminator
```

**Example:**
```markdown
# IDF-001: Constitutional Governance Framework

**Status:** Filed
**Date:** 2026-01-12
**Freeze:** paper-freeze-2026-01-12

---
```

### 3.6 Syntactic Constraints

**CANON Constraints:**
- Header **MUST** match `# SCOPE_NAME (path)`
- InheritanceDeclaration **MUST** be present
- Axioms **MUST** be consecutively numbered starting from 0 or 1
- Modal verbs **MUST** be bold (`**MUST**`)

**VOCAB Constraints:**
- Header **MUST** match `# VOCAB (path)`
- InheritanceDeclaration **MUST** be present
- Terms **MUST** be `###` headings followed by definition

**COVERAGE Constraints:**
- Header **MUST** match `# COVERAGE (path)`
- **MUST** have external reference survey
- **MUST** have feature comparison tables with Gap column
- **MUST** have roadmap with version targets
- **MUST** conclude with closure statement

**Series Constraints:**
- Prefix **MUST** be 2-3 uppercase letters
- Number **MUST** be 3 digits, zero-padded
- Numbers **SHOULD** be sequential within a series

---

## 4. Semantic Rules

### 4.1 Scope Semantics

#### 4.1.1 Scope Identity

```
Rule: SCOPE_IDENTITY
A scope is uniquely identified by its path from root.

Identity(scope) = "/" + Join(ancestors(scope), "/") + name(scope)
```

**Example:** `Identity(writing) = /canonic/services/writing`

#### 4.1.2 Scope Validity

```
Rule: SCOPE_VALIDITY
A scope is valid iff it satisfies all axioms in its governance chain.

Valid(scope) = ∀ axiom ∈ Chain(scope): Satisfies(scope, axiom)
```

#### 4.1.3 Governance Chain

```
Rule: GOVERNANCE_CHAIN
The governance chain is the ordered sequence from scope to root.

Chain(scope) = [scope] ++ Chain(parent(scope))  if parent(scope) ≠ ∅
Chain(root)  = [root]
```

**Example:**
```
Chain(/canonic/services/writing) = [
  /canonic/services/writing,
  /canonic/services,
  /canonic,
  /
]
```

### 4.2 Inheritance Semantics

#### 4.2.1 Axiom Inheritance

```
Rule: AXIOM_INHERITANCE
A scope inherits all axioms from its governance chain.

Axioms(scope) = LocalAxioms(scope) ∪ Axioms(parent(scope))
Axioms(root)  = LocalAxioms(root)
```

#### 4.2.2 Inheritance Finality `[v0.1]`

```
Rule: INHERITANCE_FINAL
Child scopes cannot override parent axioms.

∀ axiom ∈ Axioms(parent): axiom ∈ Axioms(child)
```

#### 4.2.3 Inheritance Termination

```
Rule: INHERITANCE_TERMINATES
All inheritance chains terminate at root (/).

∀ scope: ∃ n ∈ ℕ: parent^n(scope) = root
```

### 4.3 Introspection Semantics

#### 4.3.1 Vocabulary Closure

```
Rule: VOCAB_CLOSURE
VOCAB MUST define every concept used by CANON and VOCAB.

Concepts(VOCAB) ⊇ UsedConcepts(CANON) ∪ UsedConcepts(VOCAB)
```

#### 4.3.2 Concept Resolution

```
Rule: CONCEPT_RESOLUTION
Concepts resolve through the vocabulary chain.

Resolve(concept, scope) =
  if concept ∈ Concepts(VOCAB(scope)) then Definition(concept, scope)
  else Resolve(concept, parent(scope))

Resolve(concept, root) =
  if concept ∈ Concepts(VOCAB(root)) then Definition(concept, root)
  else UNDEFINED
```

#### 4.3.3 Undefined Concept

```
Rule: UNDEFINED_BLOCKS
An undefined concept is a semantic error that blocks validity.

∀ concept ∈ UsedConcepts(scope):
  Resolve(concept, scope) ≠ UNDEFINED
```

### 4.4 Triad Semantics

#### 4.4.1 Structural Completeness

```
Rule: TRIAD_COMPLETE
A valid scope MUST contain all triad artifacts.

Triad(scope) = { CANON.md, VOCAB.md, README.md }
∀ artifact ∈ Triad(scope): Exists(scope / artifact)
```

#### 4.4.2 Artifact Roles

```
Rule: ARTIFACT_ROLES
Each triad artifact has a distinct semantic role.

Role(CANON)  = Governance (axioms)
Role(VOCAB)  = Semantics (definitions)
Role(README) = Description (documentation)
```

#### 4.4.3 Role Separation

```
Rule: ROLE_SEPARATION
Artifacts MUST NOT assume roles of other artifacts.

CANON  MUST NOT define terms (VOCAB's role)
VOCAB  MUST NOT declare axioms (CANON's role)
README MUST NOT govern (informational only)
```

### 4.5 Closure Semantics

#### 4.5.1 Scope Closure

```
Rule: SCOPE_CLOSURE
A scope is closed when it satisfies all axioms and has no undefined concepts.

Closed(scope) = Valid(scope) ∧ ∀ c ∈ UsedConcepts(scope): Defined(c, scope)
```

#### 4.5.2 Self-Closure

```
Rule: SELF_CLOSURE
The root VOCAB is self-closing: it defines its own terms.

SelfClosing(root) = ∀ c ∈ UsedConcepts(VOCAB(root)): c ∈ Concepts(VOCAB(root))
```

#### 4.5.3 Transitive Closure

```
Rule: TRANSITIVE_CLOSURE
If parent is closed and child satisfies local axioms, child is closed.

Closed(parent) ∧ LocalValid(child) → Closed(child)
```

### 4.6 Semantic Primitives `[v0.1]`

CANONIC defines meaning through **artifact naming**. Uppercase filenames are semantic primitives with fixed meaning across all scopes.

#### 4.6.1 SCOPE: The Meta-Primitive

```
Rule: SCOPE_META_PRIMITIVE
SCOPE is the meta-primitive that contains all other primitives.

SCOPE = { LEDGER, CANON, VOCAB, README, COVERAGE, APPSTORE }

SCOPE is not IN the set. SCOPE IS the set.
SCOPE is the type. The six are the instances.
```

**SCOPE provides:**
- Boundary (directory container)
- Governance (CANON axioms)
- Semantics (VOCAB definitions)
- Description (README documentation)
- Closure (COVERAGE completeness)
- Distribution (APPSTORE spread)
- Persistence (LEDGER state)
- Roadmap (narrative plan within scope)
- Full stack access (recursive containment)

```
Rule: SCOPE_RECURSION
SCOPE contains SCOPE. The pattern is recursive.

CANONIC (SCOPE)
└── APPSTORE (SCOPE)
    └── PAPER (SCOPE)
        └── manuscript (output)

Each SCOPE has full access to its primitives.
```

#### 4.6.2 The Hexad: Six Primitives

```
Rule: SEMANTIC_PRIMITIVES
The following artifact names are semantic primitives with defined roles.

Primitive ::= LEDGER | CANON | VOCAB | README | COVERAGE | APPSTORE

LEDGER.md    → Persistence    (where state lives: git)
CANON.md     → Governance     (what MUST be: axioms)
VOCAB.md     → Semantics      (what words mean: definitions)
README.md    → Description    (what this is: documentation)
COVERAGE.md  → Closure        (how complete we are: gap tracking)
APPSTORE.md  → Distribution   (how it spreads: products)
```

**The Hierarchy:**
```
LEDGER   → foundation (git is the ledger)
SCOPE    → container (directory is the scope)
CANON    → law (axioms govern)
VOCAB    → language (terms define)
README   → explanation (prose documents)
COVERAGE → completeness (gaps track)
APPSTORE → distribution (products spread)
```

#### 4.6.3 LEDGER: The Foundation Primitive

```
Rule: LEDGER_FOUNDATION
LEDGER is the foundation upon which all other primitives rest.

LEDGER = git (instantiation)
LEDGER = blockchain (alternative instantiation)
LEDGER = any immutable, cryptographically-verified state machine

Without LEDGER, no persistence. Without persistence, no governance.
```

#### 4.6.4 APPSTORE: The Distribution Primitive

```
Rule: APPSTORE_DISTRIBUTION
APPSTORE is the primitive that enables self-distribution.

APPSTORE = GitHub (instantiation)
APPSTORE = any platform providing:
  - Discovery (search, topics)
  - Delivery (clone, fork)
  - Validation (CI/CD, Actions)
  - Certification (badges, verification)

CANONIC is the first language specification with distribution
embedded in the grammar. No external infrastructure required.
```

**APPSTORE Composition:**
```
Rule: APPSTORE_PRODUCTS
Products in APPSTORE are governance templates that produce artifacts.

Product      ::= PAPER | BOOK | GRANT | ...
Output       ::= manuscript | book | proposal | ...

PAPER    → produces → manuscript.md
BOOK     → produces → book.md
GRANT    → produces → proposal.md

Products GOVERN production (UPPERCASE).
Outputs ARE GOVERNED (lowercase).
```

#### 4.6.2 Primitive Roles

```
Rule: PRIMITIVE_ROLES
Each primitive has a distinct semantic role that MUST NOT be violated.

Role(CANON)    = Governance    — declares normative rules (axioms)
Role(VOCAB)    = Semantics     — defines vocabulary (terms)
Role(README)   = Description   — provides documentation (prose)
Role(COVERAGE) = Closure       — tracks external completeness (gaps + roadmap)
```

#### 4.6.3 Triad vs. Tetrad

```
Rule: TRIAD_REQUIRED
Every scope MUST contain the triad: CANON.md, VOCAB.md, README.md.

Triad(scope) = { CANON.md, VOCAB.md, README.md }

Rule: COVERAGE_OPTIONAL
COVERAGE.md is OPTIONAL but RECOMMENDED for scopes with external references.

Tetrad(scope) = Triad(scope) ∪ { COVERAGE.md }

HasExternalReferences(scope) → SHOULD have COVERAGE.md
```

#### 4.6.4 COVERAGE Semantics

```
Rule: COVERAGE_STRUCTURE
COVERAGE.md MUST track closure against external standards.

COVERAGE ::= ExternalClosure

Structure(COVERAGE) = {
  - Comparison matrix (internal → external mapping)
  - Gap analysis (what's missing)
  - Roadmap (how gaps will be closed)
  - Closure proof (when gaps = ∅)
}

Constraint: COVERAGE MUST map internal features → external references
Constraint: COVERAGE MUST identify gaps
Constraint: COVERAGE MUST have roadmap with target versions
Constraint: When gaps = ∅, scope EXCEEDS external references
```

#### 4.6.5 Closure Types

```
Rule: CLOSURE_TYPES
CANONIC distinguishes internal and external closure.

InternalClosure  = Triad satisfaction + vocabulary closure (introspection)
ExternalClosure  = COVERAGE satisfaction (all gaps closed)
CompleteClosure  = InternalClosure ∧ ExternalClosure

Closed(scope) = Valid(scope) ∧ ∀ c ∈ UsedConcepts(scope): Defined(c, scope)
               ∧ (HasCOVERAGE(scope) → Gaps(COVERAGE(scope)) = ∅)
```

### 4.7 Type System

#### 4.7.1 Artifact Types

```
Type ::= Primitive | Specification | Series | Content

Primitive     = { CANON.md, VOCAB.md, README.md, COVERAGE.md }
Specification = { *.SPEC.md, CANONIC.md, MED.md, LAW.md, LANGUAGE.md, ... }
Series        = { IDF-*.md, EP-*.md, PA-*.md, TE-*.md }
Content       = { * }
```

#### 4.7.2 Type Checking

```
Rule: TYPE_CHECK
An artifact's type is determined by its name pattern.

Type(artifact) =
  if name(artifact) = "CANON.md" then Primitive.Governance
  if name(artifact) = "VOCAB.md" then Primitive.Vocabulary
  if name(artifact) = "README.md" then Primitive.Description
  if name(artifact) = "COVERAGE.md" then Primitive.Closure
  if name(artifact) matches /^[A-Z]+\.md$/ then Specification
  if name(artifact) matches /^[A-Z]{2,3}-\d{3}/ then Series
  else Content
```

---

## 5. Composition Rules

### 5.1 Namespace Composition

#### 5.1.1 Root Namespace

```
Rule: ROOT_NAMESPACE
The root namespace is CANONIC.

RootNamespace = "CANONIC"
```

#### 5.1.2 Qualified Namespace

```
Rule: QUALIFIED_NAMESPACE
Namespaces are composed using dot notation.

Namespace ::= RootNamespace ('.' Segment)*
Segment   ::= UpperWord

QualifiedName(scope) = "CANONIC" + Join(Ancestors(scope), ".").toUpperCase()
```

**Examples:**
- `CANONIC`
- `CANONIC.SERVICES`
- `CANONIC.SERVICES.WRITING`
- `CANONIC.VALIDATORS.MACHINE.OS.LEDGER`

#### 5.1.3 Namespace-to-Path Bijection

```
Rule: NAMESPACE_PATH_BIJECTION
Namespaces biject to filesystem paths.

Path(CANONIC)     = /canonic/
Path(CANONIC.X)   = /canonic/x/
Path(CANONIC.X.Y) = /canonic/x/y/

Namespace(/canonic/)     = CANONIC
Namespace(/canonic/x/)   = CANONIC.X
Namespace(/canonic/x/y/) = CANONIC.X.Y
```

### 5.2 Identifier Composition

#### 5.2.1 Single-Word Constraint `[v0.1]`

```
Rule: SINGLE_WORD
All identifiers MUST be single words (no hyphens, underscores, or spaces).

ValidIdentifier ::= Letter (Letter | Digit)*

INVALID: canonic-services  (hyphen)
INVALID: canonic_services  (underscore)
INVALID: canonic services  (space)
VALID:   services
VALID:   canonicservices   (if necessary, but discouraged)
```

#### 5.2.2 Case Convention `[v0.1]`

```
Rule: CASE_SEMANTICS
Case carries semantic meaning in CANONIC.

UPPERCASE = Governance (the governor)
lowercase = Governed (the governed)

This is the fundamental case distinction:
- UPPERCASE artifacts GOVERN (CANON, VOCAB, README, COVERAGE)
- lowercase scopes ARE GOVERNED (services, writing, paper)
```

```
Rule: CASE_CONVENTION
Derived from CASE_SEMANTICS:

- Scope identifiers: lowercase (services, writing, paper)
  → Scopes are governed by their CANON.md

- Artifact identifiers: UPPERCASE (CANON, VOCAB, README, COVERAGE)
  → Artifacts govern the scope they reside in

- Namespace components: UPPERCASE (CANONIC.SERVICES.WRITING)
  → Namespaces represent governance hierarchy

- Concept identifiers: lowercase (axiom, scope, triad)
  → Concepts are governed by VOCAB definitions

- Series prefixes: UPPERCASE (IDF, EP, PA)
  → Series are governance artifacts

- Series slugs: lowercase (idf-001-constitutional-governance.md)
  → Filenames are filesystem artifacts (governed by OS)
```

**The Hierarchy:**
```
CANON.md        ← UPPERCASE: governs the scope
  └── defines axioms for...
      services/ ← lowercase: governed by parent CANON
        └── CANON.md ← UPPERCASE: governs this subscope
```

#### 5.2.3 Composition Operator

```
Rule: DOT_COMPOSITION
The only valid composition operator is dot (.).

Composition ::= Identifier ('.' Identifier)*

VALID:   CANONIC.SERVICES
INVALID: CANONIC-SERVICES
INVALID: CANONIC/SERVICES
INVALID: CANONIC::SERVICES
```

### 5.3 Scope Composition

#### 5.3.1 Scope Hierarchy

```
Rule: SCOPE_HIERARCHY
Scopes compose into a tree rooted at /.

ScopeTree ::= Root | Root '/' Scope+
Scope     ::= ScopeIdentifier ('/' Scope)*
```

#### 5.3.2 Scope Naming

```
Rule: SCOPE_NAMING
Scope names MUST be:
1. Single lowercase words
2. Defined in VOCAB chain
3. Unique among siblings

ValidScopeName(name, parent) =
  SingleWord(name) ∧
  Lowercase(name) ∧
  Defined(name, VocabChain(parent)) ∧
  ¬∃ sibling ∈ Children(parent): name(sibling) = name
```

#### 5.3.3 Reserved Scope Names

```
Rule: RESERVED_SCOPES
The following scope names are reserved:

CORE:         canonic, validators, services
VALIDATORS:   machine, os, ledger
SERVICES:     writing, products, distribution, protection, economics
PRODUCTS:     paper, books, grants
DISTRIBUTION: publishing, appstore
PROTECTION:   patents, companies
ECONOMICS:    token, coin
```

### 5.4 Series Composition

#### 5.4.1 Series Identifier

```
Rule: SERIES_IDENTIFIER
Series identifiers follow PREFIX-NNN format.

SeriesId ::= Prefix '-' Number
Prefix   ::= UpperLetter{2,3}
Number   ::= Digit{3}
```

#### 5.4.2 Series Filename

```
Rule: SERIES_FILENAME
Series filenames follow prefix-nnn-slug.md format.

Filename    ::= LowerPrefix '-' Number '-' Slug '.md'
LowerPrefix ::= prefix.toLowerCase()
Slug        ::= LowerWord ('-' LowerWord)*
```

**Examples:**
| Series ID | Filename |
|-----------|----------|
| IDF-001 | `idf-001-constitutional-governance.md` |
| EP-042 | `ep-042-validator-bootstrap.md` |
| PA-000 | `pa-000-triad-gate.md` |

**Note:** Hyphens are allowed in series filenames (slug portion) as an exception to the single-word rule, because series filenames are not identifiers—they are human-readable labels.

#### 5.4.3 Series Scope

```
Rule: SERIES_SCOPE
Each series prefix is bound to a scope.

SeriesScope(IDF) = /canonic/services/protection/patents/disclosures/
SeriesScope(EP)  = /canonic/services/writing/episodes/
SeriesScope(PA)  = /canonic/services/protection/patents/applications/
SeriesScope(TE)  = /canonic/templates/
```

### 5.5 Stack Composition

#### 5.5.1 Multi-Repository Stack

```
Rule: STACK_COMPOSITION
The CANONBASE composes multiple git repositories.

CANONBASE/
├── canonic/         (git repo)
├── validators/      (git repo)
├── services/        (git repo) [if separate]
├── paper/           (git repo)
├── patents/         (git repo)
└── ...

Note: CANONBASE itself is NOT a git repo.
```

#### 5.5.2 Repository Naming

```
Rule: REPO_NAMING
Repository names follow scope naming rules.

VALID:   canonic, validators, paper, patents
INVALID: canonic-services (hyphen)
INVALID: CANONIC (uppercase for directory)
```

#### 5.5.3 Stack Isolation

```
Rule: STACK_ISOLATION
Repositories MUST NOT be nested.

∀ repo ∈ Stack:
  ¬∃ other ∈ Stack: IsDescendant(repo, other)
```

---

## 6. Errors

### 6.1 Lexical Errors

| Error | Cause | Example |
|-------|-------|---------|
| `INVALID_IDENTIFIER` | Identifier contains forbidden characters | `canonic-services` (hyphen) |
| `UNDEFINED_KEYWORD` | Modal verb used without RFC 2119 semantics | `must` (lowercase) |
| `MALFORMED_SERIES` | Series identifier does not match PREFIX-NNN | `IDF-1` (should be `IDF-001`) |

### 6.2 Syntactic Errors

| Error | Cause | Example |
|-------|-------|---------|
| `MISSING_INHERITANCE` | CANON/VOCAB lacks `inherits:` | Line 3 empty |
| `INVALID_AXIOM_FORMAT` | Axiom header malformed | `### Name` (missing number) |
| `UNBOLDED_MODAL` | Modal verb not bold | `MUST` instead of `**MUST**` |

### 6.3 Semantic Errors

| Error | Cause | Example |
|-------|-------|---------|
| `UNDEFINED_CONCEPT` | Concept not in vocabulary chain | `canonification` used but not defined |
| `INHERITANCE_CYCLE` | Scope inherits from itself | A inherits B, B inherits A |
| `MISSING_TRIAD` | Required triad artifact missing | Scope has CANON.md but no VOCAB.md |
| `ROLE_VIOLATION` | Artifact assumes wrong role | VOCAB.md contains `## Axioms` |

### 6.4 Composition Errors

| Error | Cause | Example |
|-------|-------|---------|
| `HYPHENATED_NAME` | Identifier contains hyphen | `canonic-services` |
| `INVALID_NAMESPACE` | Namespace doesn't start with CANONIC | `SERVICES.WRITING` |
| `CASE_MISMATCH` | Wrong case convention | `Services` directory, `canon.md` file |
| `UNDEFINED_SCOPE` | Scope name not in VOCAB chain | Directory `foobar` not in any VOCAB |

---

## 7. Validation

### 7.1 Validate Identifier

```python
def validate_identifier(name: str) -> Result:
    if '-' in name:
        return Error("HYPHENATED_NAME", f"'{name}' contains hyphen")
    if '_' in name:
        return Error("UNDERSCORED_NAME", f"'{name}' contains underscore")
    if ' ' in name:
        return Error("SPACED_NAME", f"'{name}' contains space")
    if not name.isalnum():
        return Error("INVALID_CHARS", f"'{name}' contains invalid characters")
    return Pass()
```

### 7.2 Validate Namespace

```python
def validate_namespace(namespace: str) -> Result:
    if not namespace.startswith("CANONIC"):
        return Error("INVALID_NAMESPACE", "Must start with CANONIC")

    parts = namespace.split(".")
    for part in parts:
        if not part.isupper():
            return Error("CASE_MISMATCH", f"'{part}' must be uppercase")
        if not part.isalnum():
            return Error("INVALID_CHARS", f"'{part}' contains invalid characters")

    return Pass()
```

### 7.3 Validate Scope Structure

```python
def validate_scope(path: Path) -> Result:
    # Check name
    name_result = validate_identifier(path.name)
    if not name_result.ok:
        return name_result

    # Check case
    if not path.name.islower():
        return Error("CASE_MISMATCH", f"Scope '{path.name}' must be lowercase")

    # Check triad
    for artifact in ["CANON.md", "VOCAB.md", "README.md"]:
        if not (path / artifact).exists():
            return Error("MISSING_TRIAD", f"Missing {artifact}")

    return Pass()
```

---

## 8. Version History

| Version | Date | Tag | Status | Changes |
|---------|------|-----|--------|---------|
| v0.1 | 2026-01-19 | `lang-v0.1` | Draft | Initial specification |
| v0.2 | — | — | Planned | Domain extensions (MED, LAW, FIN) |
| v0.3 | — | — | Planned | Token economics (TOKEN, COIN) |
| v1.0 | — | — | Planned | Stable release |

---

## Appendix A: Grammar Summary

```ebnf
(* Lexical *)
Identifier       ::= ScopeIdentifier | ArtifactIdentifier | SeriesIdentifier | ConceptIdentifier
ScopeIdentifier  ::= LowerWord
ArtifactIdentifier ::= UpperWord
SeriesIdentifier ::= Prefix '-' Number
Namespace        ::= 'CANONIC' ('.' UpperWord)*

(* Semantic Primitives *)
Primitive        ::= 'CANON' | 'VOCAB' | 'README' | 'COVERAGE'
PrimitiveFile    ::= Primitive '.md'
Triad            ::= { CANON.md, VOCAB.md, README.md }
Tetrad           ::= Triad ∪ { COVERAGE.md }

(* Syntactic *)
CANONDocument    ::= Header InheritanceDeclaration '---' AxiomSection*
VOCABDocument    ::= Header InheritanceDeclaration '---' TermSection*
COVERAGEDocument ::= Header '---' ComparisonMatrix GapAnalysis Roadmap
AxiomDefinition  ::= '###' Number '.' Name LineTerminator AxiomBody
TermDefinition   ::= '###' TermName LineTerminator TermBody

(* Semantic *)
Valid(scope)     = ∀ axiom ∈ Chain(scope): Satisfies(scope, axiom)
InternalClosure  = Valid(scope) ∧ ∀ c ∈ UsedConcepts(scope): Defined(c, scope)
ExternalClosure  = HasCOVERAGE(scope) → Gaps(COVERAGE(scope)) = ∅
CompleteClosure  = InternalClosure ∧ ExternalClosure

(* Composition *)
Namespace        ::= 'CANONIC' ('.' Segment)*
ValidIdentifier  ::= Letter (Letter | Digit)*   (* NO hyphen, underscore, space *)
```

---

## Appendix B: Comparison Matrix

| Feature | Go | Python | Rust | C | CANONIC |
|---------|-----|--------|------|---|---------|
| **Spec Document** | Single | Single | mdBook | ISO | Single |
| **Versioning** | Inline `[Go 1.x]` | By release | By edition | By year | Inline `[v0.x]` |
| **Grammar Notation** | EBNF | EBNF/PEG | EBNF | Prose | EBNF |
| **Formal Semantics** | Partial | English | Partial | Yes | Semi-formal |
| **Machine Readable** | No | No | In progress | No | Validators |
| **Normative Modal** | — | — | — | shall | RFC 2119 |
| **Self-Hosting** | Yes | Yes | Yes | Yes | Yes (introspection) |

---

*This specification is governed by [/canonic/language/CANON.md](CANON.md).*

*CANONIC is closed.*
