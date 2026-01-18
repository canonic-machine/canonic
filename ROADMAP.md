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
| 3 | Cascade | change → IDF → VaaS → Downstream → Closure |
| 4 | Closure | ∃{SCOPE}.md closes CANON(s) |

**Status:** CLOSED

---

## 5. Services Layer (canonic-services/)

| Service | Function | Status |
|---------|----------|--------|
| VaaS | Validation | CLOSED |
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
