# APPSTORE Roadmap to Closure

**Status:** OPEN
**Target:** Complete service stack via GitHub Actions

---

## Current State

| Asset | Status |
|-------|--------|
| Validators (local) | WORKING |
| GitHub Actions | 2 of 12 |
| Service CANONs | INCOMPLETE (missing VOCAB) |

---

## Phase 1: VaaS Actions

Wrap existing validators as GitHub Actions.

| Action | Validator | Status |
|--------|-----------|--------|
| `canonic/vaas-triad` | `validators/canonic/triad/` | PLANNED |
| `canonic/vaas-inheritance` | `validators/canonic/inheritance/` | PLANNED |
| `canonic/vaas-introspection` | `validators/canonic/introspection/` | PLANNED |
| `canonic/vaas-language` | `validators/canonic/language.py` | PLANNED |

**Deliverable:** Users can add VaaS to their repos via:
```yaml
- uses: canonic/vaas-triad@v1
- uses: canonic/vaas-inheritance@v1
- uses: canonic/vaas-introspection@v1
- uses: canonic/vaas-language@v1
```

---

## Phase 2: TaaS Action

Transcript as a Service - evidence production.

| Action | Function | Status |
|--------|----------|--------|
| `canonic/taas` | Transcript generation | PLANNED |

**Pattern:**
```
Input → Transcript → Evidence (timestamped, immutable)
```

**Dependency:** VaaS (validates transcripts)

---

## Phase 3: ToKaaS Action

Token as a Service - reputation/ego system.

| Action | Function | Status |
|--------|----------|--------|
| `canonic/tokaas` | Token management | PLANNED |

**Pattern:**
```
Participation → TOKEN (Ego) → gates → COIN
```

**Properties:**
- Non-transferable
- Earned through participation
- Gates COIN access

**Dependency:** TaaS (participation evidence)

---

## Phase 4: COIN Action

Currency service - transferable, git-based ledger.

| Action | Function | Status |
|--------|----------|--------|
| `canonic/coin` | Currency transactions | PLANNED |

**Pattern:**
```
TOKEN holders → COIN transactions → git commits
```

**Properties:**
- Transferable
- Gated by TOKEN
- Protocol governed (mint/burn)
- Git = LEDGER

**Dependency:** ToKaaS (gates access)

---

## Phase 5: CHAT Action

LLM interface to all services.

| Action | Function | Status |
|--------|----------|--------|
| `canonic/chat` | LLM-driven interface | PLANNED |

**Pattern:**
```
User → CHAT → VaaS + TaaS + ToKaaS + COIN → Evidence
```

**Dependency:** All above services

---

## Phase 6: WRITING Action

Artifact production service.

| Action | Function | Status |
|--------|----------|--------|
| `canonic/writing` | Document generation | PLANNED |

**Dependency:** VaaS (validates output)

---

## Domain Instantiation

Each service instantiates per domain:

| Domain | VaaS | TaaS | ToKaaS | CHAT |
|--------|------|------|--------|------|
| MED | HIPAA, FDA | Clinical records | Opts Ego | MammoChat |
| LAW | BAR, PRIVILEGE | Discovery logs | Legal Ego | ElderChat |
| GRANTS | NIH, NSF | Proposals | Grant Ego | GrantChat |
| FIN | SEC, SOX | Audit trails | Fin Ego | FinChat |
| EDU | FERPA | Credentials | Edu Ego | EduChat |
| GOV | FOIA, FEDRAMP | FOIA responses | Gov Ego | GovChat |
| MIL | ITAR, CMMC | Classified handling | Mil Ego | MilChat |

---

## Closure Criteria

APPSTORE closes when:

1. All 6 service Actions deployed
2. All Actions pass self-validation
3. At least one domain instantiation working
4. Documentation complete (README per Action)
5. GitHub Marketplace listing (billing)

---

## Dependency Graph

```
         VaaS (Phase 1)
        /     \
    TaaS       WRITING
   (Phase 2)   (Phase 6)
      |
   ToKaaS
   (Phase 3)
      |
    COIN
   (Phase 4)
      |
    CHAT
   (Phase 5)
```

---

## Timeline

| Phase | Service | Complexity | Dependency |
|-------|---------|------------|------------|
| 1 | VaaS | LOW | None (validators exist) |
| 2 | TaaS | MEDIUM | VaaS |
| 3 | ToKaaS | MEDIUM | TaaS |
| 4 | COIN | HIGH | ToKaaS |
| 5 | CHAT | HIGH | All |
| 6 | WRITING | LOW | VaaS |

**Critical path:** VaaS → TaaS → ToKaaS → COIN → CHAT

---

## Next Action

**Phase 1, Step 1:** Create `vaas-triad` GitHub Action

---
