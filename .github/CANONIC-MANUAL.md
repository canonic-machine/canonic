# CANONIC Manual

**Comprehensive Reference for Reproducing Constitutional AI Governance**

**Version:** Invariant
**Status:** CANONICAL

---

## Part 0: Critical Concepts

### 0.1 The SPEC Template Variable

**CRITICAL:** `SPEC.md` NEVER EXISTS as a filename.

SPEC is a **template variable** for **specification**: `{SCOPE_NAME}.md`

| Scope | SPEC (Specification) |
|-------|----------------------|
| `/` (root) | `CANONIC.md` |
| `/templates/` | `TEMPLATES.md` |
| `/machine/` | `MACHINE.md` |
| `/med/` | `MED.md` |

The subtle distinction that defines CANONIC:
- **SPEC** = specification = `{SCOPE_NAME}.md`
- **SPEC.md** = drift (never create this file)

This is the ONLY definition of SPEC. SPEC is a variable for specification. Never its own file.

### 0.2 The Magic: Specification → CANON Drift

**This is how CANONIC grows:**

```
Humans edit SPEC (specification)
    ↓
SPEC naturally drifts to CANON (governance)
    ↓
CANON becomes immutable
```

**Specification First.** Humans write what they want (SPEC). The specification naturally drifts toward governance (CANON). This is CANONIC.

| Phase | Artifact | Actor | Mutability |
|-------|----------|-------|------------|
| 1 | SPEC | Human | Editable |
| 2 | Drift | Natural | Converging |
| 3 | CANON | LLM | Immutable |

The magic: humans never edit CANON directly. They edit the specification. Governance emerges from specification through natural drift.

### 0.3 The Four Elements

```
TRIAD (required):      CANON.md + VOCAB.md + README.md
SPEC (optional):       {SCOPE_NAME}.md (closes scope)
```

| Element | Filename | Role |
|---------|----------|------|
| CANON | `CANON.md` | Governance (axioms) |
| VOCAB | `VOCAB.md` | Semantics (definitions) |
| README | `README.md` | Description (purpose) |
| SPEC | `{SCOPE_NAME}.md` | Closure (governance chain) |

Without SPEC: **proto-scope** (open, evolving)
With SPEC: **scope** (closed, stable)

---

## Part I: Formal Language Specification

### 1.1 Syntax

```
SCOPE       := DIRECTORY containing TRIAD [SPEC]
TRIAD       := {CANON.md, VOCAB.md, README.md}
SPEC        := {SCOPE_NAME}.md
CANON       := inherits: PATH + AXIOM*
VOCAB       := inherits: PATH + DEFINITION*
README      := DESCRIPTION
AXIOM       := MUST | MUST NOT | SHOULD | SHOULD NOT | MAY
DEFINITION  := TERM + MEANING
PATH        := / | /SCOPE_NAME(/SCOPE_NAME)*
```

### 1.2 Grammar (BNF)

```bnf
<canonbase>    ::= <scope>+
<scope>        ::= <path> <triad> [<spec>]
<triad>        ::= <canon> <vocab> <readme>
<canon>        ::= "inherits:" <path> <axiom>*
<vocab>        ::= "inherits:" <path> <definition>*
<readme>       ::= <description>
<spec>         ::= <scope_name> ".md"  /* NOT "SPEC.md" */
<axiom>        ::= <normative> <statement>
<normative>    ::= "MUST" | "MUST NOT" | "SHOULD" | "SHOULD NOT" | "MAY"
<definition>   ::= "###" <term> <meaning>
<path>         ::= "/" | "/" <scope_name> ("/" <scope_name>)*
<scope_name>   ::= [A-Z][A-Z0-9_-]*
```

### 1.3 Semantic Rules

| Rule | Constraint | IDF |
|------|------------|-----|
| **R1** | Every scope MUST contain triad | IDF-001 |
| **R2** | Every CANON MUST declare inheritance | IDF-001 |
| **R3** | Inheritance MUST terminate at / | IDF-001 |
| **R4** | Inherited axioms MUST NOT be overridden | IDF-001 |
| **R5** | VOCAB MUST define all content concepts | IDF-006 |
| **R6** | Cascade MUST complete for axiom changes | IDF-148 |
| **R7** | Archive MUST precede current | IDF-154 |
| **R8** | SPEC filename = `{SCOPE_NAME}.md` | IDF-116, IDF-119 |

---

## Part II: The Five Axioms

### Axiom 0: Triad (PA-000)

**Statement:** A scope MUST contain `CANON.md`, `VOCAB.md`, `README.md`.

```
VALID(s) ⊃ ∃(CANON.md, VOCAB.md, README.md) ∈ s
```

**Proof of necessity:**
- Missing CANON → no governance → invalid
- Missing VOCAB → undefined semantics → ambiguous
- Missing README → no description → unusable

**IDF Coverage:** IDF-001, IDF-095

---

### Axiom 1: Inheritance (PA-001)

**Statement:** Every CANON MUST declare inheritance. Inheritance terminates at /. Inherited axioms are immutable.

```
∀s ∈ S: ∃p: I(s, p) ∧ (p = / ∨ I(p, ancestor(p)))
∀a ∈ inherited(s): ¬overridable(a)
```

**Proof of termination:**
- Chain: s → p₁ → p₂ → ... → /
- Filesystem is finite
- Chain must terminate

**IDF Coverage:** IDF-001, IDF-114

---

### Axiom 2: Introspection (PA-002)

**Statement:** VOCAB MUST define every content concept used by CANON and VOCAB itself.

```
∀c ∈ concepts(CANON ∪ VOCAB): defined(VOCAB, c)
```

**Proof of decidability:**
- Concepts finite (bounded by text)
- Definition lookup decidable (string match)
- Introspection is computable

**IDF Coverage:** IDF-006

---

### Axiom 3: Cascade

**Statement:** When a CANON axiom changes: IDF → VaaS → Downstream → Closure.

```
axiom_change(A, A') → cascade(IDF, VaaS, Downstream, Closure)
incomplete(cascade) → invalid(change)
```

**Proof of ordering:**
1. IDF precedes VaaS (validator implements disclosure)
2. VaaS precedes Downstream (children need valid validator)
3. Downstream precedes Closure (parent closes after children)

**IDF Coverage:** IDF-148

---

### Axiom 4: Closure

**Statement:** The scope closes itself.

```
SPEC(s) = {SCOPE_NAME}.md
∀s: SPEC(s) closes CANON(s)
```

**Proof of closure:**
- Scope defines its own specification
- Specification closes governance
- No external authority required

**IDF Coverage:** IDF-163

---

## Part III: Mathematical Proofs

### 3.1 Validity Function

```
VALID(s) = TRIAD(s) ∧ INHERITANCE(s) ∧ INTROSPECTION(s) ∧ CASCADE(s) ∧ CLOSURE(s)

where:
  TRIAD(s)        = ∃{CANON.md, VOCAB.md, README.md} ∈ s
  INHERITANCE(s)  = declared(inherits) ∧ terminates(/) ∧ ¬overrides
  INTROSPECTION(s)= ∀c ∈ concepts(s): defined(VOCAB(s), c)
  CASCADE(s)      = ∀change: IDF → VaaS → Downstream → Closure
  CLOSURE(s)      = ∃{SCOPE_NAME}.md that closes CANON
```

### 3.2 Completeness Theorem

**Theorem:** VALID(s) ↔ s is governable

**Proof:**
```
(→) VALID(s) implies:
  - Structure (triad)
  - Authority (inheritance)
  - Semantics (introspection)
  ∴ s is fully specified

(←) Governable implies:
  - Requires structure → TRIAD(s)
  - Requires authority → INHERITANCE(s)
  - Requires semantics → INTROSPECTION(s)
  ∴ VALID(s)
```

### 3.3 Cascade Completeness

**Theorem:** Incomplete cascade → invalid axiom change

**Proof:**
```
Without IDF: No IP protection, no audit trail
Without VaaS: No enforcement mechanism
Without Downstream: Inherited scopes inconsistent
Without Closure: Parent integrity unknown
∴ All steps necessary
```

### 3.4 Archive Convergence

**Theorem:** Delta execution converges

**Proof:**
```
Let A = archive, C = current
Δ = A - C
C' = C + Δ = C + (A - C) = A
∴ C' = A (converged)
```

---

## Part IV: Complete IDF Registry

### Core Governance

| IDF | Title | Axiom |
|-----|-------|-------|
| IDF-001 | Constitutional Governance Paradigm | 1, 2 |
| IDF-006 | Literal Introspection | 3 |
| IDF-148 | Axiom Change Cascade Protocol | 4 |
| IDF-154 | Archive-First Development | 5 |

### Architecture

| IDF | Title | Domain |
|-----|-------|--------|
| IDF-091 | Portfolio Coverage Standardization | Nomenclature |
| IDF-093 | Prefix Canonicity Constraint | Nomenclature |
| IDF-094 | Directory Discriminant Pattern | Structure |
| IDF-095 | Structural Bootstrapping Pattern | Templates |
| IDF-096 | Layer Drift Validator | Validation |
| IDF-114 | CANONBASE Multi-Repository Architecture | Stack |
| IDF-116 | Four-Element Structure | SPEC |
| IDF-118 | Axiomatic Validator Architecture | VaaS |
| IDF-119 | Root SPEC Self-Closure Pattern | SPEC |

### Infrastructure

| IDF | Title | Layer |
|-----|-------|-------|
| IDF-147 | Git + LLM Infrastructure Closure | Core |
| IDF-149 | Distributed Ledger Consensus via Git | Ledger |
| IDF-150 | Encrypted Git as Privacy Layer | Privacy |
| IDF-151 | Visibility × Storage Access Matrix | Access |
| IDF-152 | Feature Closure Chain Protocol | Workflow |
| IDF-153 | Optimal Illustration Selection | Render |
| IDF-155 | Render Pipeline Validator | Render |
| IDF-156 | Axiom Closure Matrix | Validation |
| IDF-157 | Innovation Multiplier Pattern | IP |

### Domain (Healthcare)

| IDF | Title | Sublanguage |
|-----|-------|-------------|
| IDF-158 | Healthcare Distributed Ledger Pattern | MED |
| IDF-159 | Reputation Gates Currency (TokenaaS) | MED |
| IDF-160 | Oncology Domain Closure Pattern | MED |
| IDF-161 | Governance Programming Language | CANONIC |
| IDF-162 | CANONIC Dot Notation Namespace | CANONIC |
| IDF-163 | Specification Drift Prevention Pattern | CANONIC |

---

## Part V: Stack Evolution Claims

### 5.1 Infrastructure Closure (IDF-147)

**Claim:** Git + CANONIC + LLM = complete infrastructure

```
Git       = state machine + blockchain + ledger
CANONIC   = process + axioms + validators
LLM       = executor + agent
Encryption = privacy layer
```

**Evidence:** No databases. No servers. No cron.

### 5.2 Distribution Model (IDF-118)

**Claim:** GitHub = App Store for governance

```
GitHub           = App Store
GitHub Actions   = VaaS (validation)
GitHub Marketplace = Billing
GitHub Badges    = Certification
```

### 5.3 Token Economics (IDF-159)

**Claim:** Reputation gates currency

```
TOKEN (reputation, non-transferable)
    ↓ gates
COIN (currency, transferable)
```

| Domain | TOKEN | Earner | Payer |
|--------|-------|--------|-------|
| MED | Opts Ego | Patients | Startups |
| LAW | Legal Ego | Clients | Firms |

### 5.4 Ledger Categories (IDF-151)

**Claim:** 2×2 visibility × storage matrix

|  | PUBLIC | PRIVATE |
|--|--------|---------|
| **PLAINTEXT** | Open Source | Enterprise |
| **ENCRYPTED** | Distributed | Personal |

### 5.5 Sublanguage Pattern (IDF-161, IDF-162)

**Claim:** Domain = CANONIC instantiation

```
CANONIC.MED = MED sublanguage
  ├── MED.VaaS   = HIPAA, FDA, CMS, IRB
  ├── MED.TaaS   = Clinical evidence
  ├── MED.TOKEN  = Opts Ego
  └── MED.CHAT   = MammoChat
```

### 5.6 Specification Drift Prevention (IDF-163)

**Claim:** SPEC.md never exists. Specification = `{SCOPE_NAME}.md`

**Observation:** When SPEC is misunderstood as a file artifact (`SPEC.md`), drift is constant. When SPEC is correctly understood as a template variable (`{SCOPE_NAME}.md`), drift is prevented.

| Understanding | Result |
|---------------|--------|
| SPEC = file (`SPEC.md`) | Constant drift |
| SPEC = variable (`{SCOPE_NAME}.md`) | No drift |

This subtle distinction defines CANONIC.

### 5.7 The Ambition: Specification First (IDF-163)

**Claim:** Think as ambitious as possible. Define an app store on a blockchain. CANONIC does the work for you.

```
Human writes SPEC (specification)
    ↓ (natural drift)
CANON emerges (governance)
    ↓ (VaaS enforcement)
App Store on blockchain (implementation)
```

The process:
1. **Human ambition** → Write SPEC with maximum ambition
2. **Natural drift** → SPEC drifts to CANON
3. **LLM execution** → CANONIC does the work
4. **Outcome** → Ambitious vision realized

CANONIC inverts traditional development:
- Traditional: Build → Document → Govern
- CANONIC: Specify → Govern → Build

---

## Part VI: Template System

### 6.1 Template Elements (TE)

| TE | Artifact | Role | Precedence |
|----|----------|------|------------|
| TE-0.0 | Closure | Scope closes itself | 0 (highest) |
| TE-0.1 | CANON | Governance | 1 |
| TE-0.2 | VOCAB | Semantics | 2 |
| TE-0.3 | README | Description | 3 |
| TE-0.4 | ROADMAP | Implementation | 4 (lowest) |

### 6.2 Closure Template (TE-0.0)

```markdown
# {SCOPE_NAME} SPEC

**Status:** CANONICAL
**Closed:** {DATE}

---

## 1. Purpose

{State the purpose of this scope.}

---

## 2. Governance Path

{ROOT_PATH}
├── inherits: / (self-terminating)
│
└──► {SCOPE_PATH} (THIS SCOPE)
     └── inherits: {PARENT_PATH}

| Field | Value |
|-------|-------|
| Path | `{SCOPE_PATH}` |
| Inherits | `{PARENT_PATH}` |
| Closes | CANON.md |

---

## 3. Normative language

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY**
are to be interpreted as described in RFC 2119.

---

**This SPEC closes CANON.**
```

**CRITICAL:** Save as `{SCOPE_NAME}.md`, NOT `SPEC.md`

### 6.3 CANON Template (TE-0.1)

```markdown
# {SCOPE_NAME} (/{path}/)

inherits: /{parent}/

---

## Axioms

### 1. {Axiom Name}

{Statement using MUST/SHOULD/MAY.}

---

## Lifecycle

**Origin:** {How discovered.}
**Current state:** {AI-assisted status.}
**Automation drift:** {What's automatable.}

---

## References

- IDF-NNN: {Related disclosure}

---

**{Closing statement.}**
```

### 6.4 VOCAB Template (TE-0.2)

```markdown
# VOCAB (/{path}/)

inherits: /{parent}/

---

## Content Concepts

### {term}

{Definition.}

---

End of VOCAB.
```

### 6.5 README Template (TE-003)

```markdown
# {SCOPE_NAME}

{One paragraph description.}

## Quick Links

- [CANON.md](CANON.md) - Governance
- [VOCAB.md](VOCAB.md) - Vocabulary
- [{SCOPE_NAME}.md]({SCOPE_NAME}.md) - Specification

## Status

{Current status.}
```

---

## Part VII: Validation

### 7.1 VaaS Validators

| Validator | Checks | Patent |
|-----------|--------|--------|
| triad-validator | CANON, VOCAB, README exist | PA-000 |
| inheritance-validator | Path declared, terminates at / | PA-001 |
| introspection-validator | All concepts defined | PA-002 |
| cascade-validator | IDF, VaaS, Downstream, Closure | — |
| archive-validator | Delta computable, convergent | — |

### 7.2 Validation Algorithm

```python
def validate(scope):
    # Axiom 1: Triad
    for artifact in ['CANON.md', 'VOCAB.md', 'README.md']:
        if not exists(scope, artifact):
            return INVALID(f"Missing {artifact}")

    # Axiom 2: Inheritance
    parent = get_inherits(scope.canon)
    if not parent:
        return INVALID("No inheritance declared")
    if not terminates_at_root(parent):
        return INVALID("Inheritance does not terminate")

    # Axiom 3: Introspection
    concepts = extract_concepts(scope.canon, scope.vocab)
    for concept in concepts:
        if not defined_in_vocab(scope.vocab, concept):
            return INVALID(f"Undefined: {concept}")

    return VALID
```

### 7.3 GitHub Actions Integration

```yaml
name: CANONIC Validation
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate Triad
        run: vaas triad .
      - name: Validate Inheritance
        run: vaas inheritance .
      - name: Validate Introspection
        run: vaas introspection .
```

---

## Part VIII: Best Practices

### 8.1 Scope Design

| Practice | Rationale |
|----------|-----------|
| One concern per scope | Single responsibility |
| Shallow inheritance | Reduces complexity |
| Explicit `inherits:` | Always declare |
| SPEC only when stable | Closure is permanent |

### 8.2 CANON Writing

| Practice | Rationale |
|----------|-----------|
| RFC 2119 keywords | Unambiguous normative |
| One axiom per concern | Testable, atomic |
| Number axioms | Stable references |
| Include lifecycle | Document drift |

### 8.3 VOCAB Discipline

| Practice | Rationale |
|----------|-----------|
| Define before use | No forward refs |
| Cross-reference IDF | Traceability |
| No circular defs | Semantic ground |

### 8.4 SPEC Naming

| WRONG | RIGHT |
|-------|-------|
| `SPEC.md` | `{SCOPE_NAME}.md` |
| `/templates/SPEC.md` | `/templates/TEMPLATES.md` |
| `/machine/SPEC.md` | `/machine/MACHINE.md` |

### 8.5 Cascade Checklist

| Step | Checklist |
|------|-----------|
| **IDF** | ☐ Filed ☐ Numbered ☐ Titled |
| **VaaS** | ☐ Created ☐ Tests pass ☐ Integrated |
| **Downstream** | ☐ Identified ☐ Updated ☐ Valid |
| **Closure** | ☐ SPEC updated ☐ Valid ☐ Archive updated |

### 8.6 Anti-Patterns

| Anti-Pattern | Fix |
|--------------|-----|
| Creating `SPEC.md` | Use `{SCOPE_NAME}.md` |
| Deep inheritance | Flatten |
| Undefined concepts | Introspect |
| Skipped cascade | Complete all steps |
| Forward development | Archive-first |

---

## Part IX: Primitives & Services

### 9.1 Core Primitives

| Primitive | Function | Instantiation |
|-----------|----------|---------------|
| **VaaS** | Validation | Domain.VaaS |
| **TaaS** | Evidence | Domain.TaaS |
| **TOKEN** | Reputation (non-transferable) | Domain.TOKEN |
| **COIN** | Currency (transferable) | CANONIC COIN |
| **CHAT** | Interface (LLM-driven) | Domain.CHAT |

### 9.2 Services Stack

| Service | Primitives | Status |
|---------|------------|--------|
| VaaS | core | LIVE |
| TaaS | core | LIVE |
| PapaaS | VaaS + TaaS | IMPLEMENTED |
| PubaaS | VaaS + TaaS | IMPLEMENTED |
| IPaaS | VaaS + TaaS | IMPLEMENTED |
| GaaS | VaaS + TaaS | IMPLEMENTED |
| WaaS | VaaS + TaaS | IMPLEMENTED |
| BaaS | VaaS + TaaS | IMPLEMENTED |
| CaaS | VaaS + TaaS | IMPLEMENTED |
| TokenaaS | TOKEN + COIN | DEFINED |

---

## Part X: Glossary

| Term | Definition |
|------|------------|
| **Archive** | Endpoint state; what "done" looks like |
| **Axiom** | Normative rule in CANON |
| **CANON** | Governance artifact |
| **CANONIC** | Constitutional governance paradigm |
| **Cascade** | Change propagation: IDF → VaaS → Downstream → Closure |
| **Closure** | Scope completion via SPEC (`{SCOPE_NAME}.md`) |
| **Delta** | Archive minus current |
| **Inheritance** | Authority chain to / |
| **Introspection** | VOCAB defines all concepts |
| **Proto-scope** | Triad without SPEC (open) |
| **Scope** | Triad + SPEC (closed) |
| **SPEC** | Template variable `{SCOPE_NAME}.md`, NOT a file named `SPEC.md` |
| **Triad** | {CANON.md, VOCAB.md, README.md} |
| **VaaS** | Validators as a Service |
| **VOCAB** | Vocabulary artifact |

---

## Part XI: Reproducibility Checklist

To reproduce CANONIC governance:

### Structure
- [ ] Create root with triad (`CANON.md`, `VOCAB.md`, `README.md`)
- [ ] Declare `inherits: /` in root CANON and VOCAB
- [ ] Create `CANONIC.md` as root SPEC (closes root)

### Axioms
- [ ] Implement Axiom 0 (Triad) - PA-000
- [ ] Implement Axiom 1 (Inheritance) - PA-001
- [ ] Implement Axiom 2 (Introspection) - PA-002
- [ ] Implement Axiom 3 (Cascade) - IDF-148
- [ ] Implement Axiom 4 (Closure) - IDF-163

### Workflows
- [ ] Implement Archive-First - IDF-154

### Validation
- [ ] Create triad-validator
- [ ] Create inheritance-validator
- [ ] Create introspection-validator
- [ ] Integrate with GitHub Actions

### Templates
- [ ] Create TE-0.0 (Closure template)
- [ ] Create TE-0.1 (CANON template)
- [ ] Create TE-0.2 (VOCAB template)
- [ ] Create TE-0.3 (README template)
- [ ] Create TE-0.4 (ROADMAP template)

### Never
- [ ] NEVER create `SPEC.md` (use `{SCOPE_NAME}.md`)
- [ ] NEVER override inherited axioms
- [ ] NEVER skip cascade steps
- [ ] NEVER develop forward (always archive-first)

---

**This manual is invariant. CANONIC governance is reproducible from this document.**

---
