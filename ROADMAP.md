# CANONIC ROADMAP

**Status:** CANONICAL
**Created:** 2026-01-18

---

## 1. Vision

3 repos. Clean layers. Independent. Interoperable.

---

## 2. Multi-Repo Stack

```
canonic-domains/     (inherits: canonic-services/)
    ↑ instantiates
canonic-services/    (inherits: canonic/)
    ↑ implements
canonic/             (OS: 5 axioms)
```

---

## 3. Repos

| Repo | Layer | Inherits |
|------|-------|----------|
| `canonic/` | OS | / (self) |
| `canonic-services/` | Services | canonic/ |
| `canonic-domains/` | Domains | canonic-services/ |

---

## 4. OS Layer (canonic/)

| Axiom | Name | Mathematical Statement |
|-------|------|------------------------|
| 0 | Triad | ∃{CANON.md, VOCAB.md, README.md} ∈ s |
| 1 | Inheritance | I(s,p) ∧ terminates(/) |
| 2 | Introspection | ∀c ∈ concepts(s): defined(VOCAB, c) |
| 3 | Cascade | change → IDF → VALIDATORaaS → Downstream → Closure |
| 4 | Closure | ∃{SCOPE}.md closes CANON(s) |

**Status:** CLOSED

---

## 5. Services Layer (canonic-services/)

| Service | Function | Status |
|---------|----------|--------|
| VALIDATORaaS | Validation | CLOSED |
| TaaS | Transcript | CLOSED |
| TOKEN | Reputation | CLOSED |
| COIN | Currency | CLOSED |
| CHAT | Interface | CLOSED |

**Status:** CLOSED

---

## 6. Domains Layer (canonic-domains/)

| Domain | Sector | Status |
|--------|--------|--------|
| MED | Healthcare | DEFINED |
| LAW | Legal | DEFINED |
| GRANTS | Research | DEFINED |
| FIN | Finance | DEFINED |
| EDU | Education | DEFINED |
| GOV | Government | DEFINED |
| MIL | Military | DEFINED |

**Status:** OPEN

---

## 7. Success Criteria

- [x] 3 repos created
- [x] Inheritance chain complete
- [x] All scopes have triad + closure
- [x] All axioms provable
- [x] All services composable
- [x] All domains instantiable

---

**Status:** CLOSED
**Closed:** 2026-01-18

**This roadmap closes CANONIC.**

---

## 8. Open Source IP Claims

All work product derived from funded grants **MUST** be released to public domain per funder terms.

### MammoChat FCIF Grant 354

| Claim | Commitment | Evidence |
|-------|------------|----------|
| Public Domain | All work, invention, discovery, development | [Award Letter](services/products/grants/mammochat/2-grant-354-fcif-rd-2-award-letter.txt) |
| No Patents | Without prior FDOH approval | [Award Letter](services/products/grants/mammochat/2-grant-354-fcif-rd-2-award-letter.txt) |
| Public Results | Shared to further FL cancer research | [Award Letter](services/products/grants/mammochat/2-grant-354-fcif-rd-2-award-letter.txt) |
| AdventHealth Subaward | Same terms flow to subcontractor | [Subaward](services/products/grants/mammochat/4-subaward_adventhealth_not-fully-executed-os1178_redacted-per-119.0713.txt) |

### IP Separation

| Asset | Owner | License | Status |
|-------|-------|---------|--------|
| MammoChat™ | Foundation | Trademark retained | Not-for-profit |
| MammoChat Development | UCF | Public domain per grant | Open source |
| MammoChat Code | Open Source | Per FDOH terms | Public domain |

UCF executes grant-funded development. Foundation retains MammoChat™ trademark.

**MammoChat™ MUST remain not-for-profit.**

**Future Claims:** All grant-funded IP flows to open source under this ledger.

---
