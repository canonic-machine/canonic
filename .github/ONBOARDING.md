# CANONIC Team Onboarding

**End-to-end guide for governing via Git.**

---

## Multi-Repo Stack

```
canonic-domains/     (inherits: canonic-services/)
    ↑ instantiates
canonic-services/    (inherits: canonic/)
    ↑ implements
canonic/             (OS: 5 axioms)
```

---

## Team

| Role | Name | Domain | Repo |
|------|------|--------|------|
| Founder/CEO/CSO | Dexter Hadley | MED | canonic-domains/ |
| Co-Founder/ED | Fatima Boukrim | FOUNDATION | canonic/ |
| Co-Founder/CTO | Anurag Chatterjee | Infrastructure | canonic-services/ |
| Co-Founder/Counsel | David Slonim | LAW | canonic-domains/ |
| IP Law | Fitch Gabriel | LAW.IP | canonic-domains/ |
| Chairman | Neville Calleja | MED.EU | canonic-domains/ |

---

## Step 1: Get Git Access

```bash
# Clone all 3 repos
git clone https://github.com/canonic/canonic.git
git clone https://github.com/canonic/canonic-services.git
git clone https://github.com/canonic/canonic-domains.git
```

---

## Step 2: Understand Your Scope

| Domain | Path | Governs |
|--------|------|---------|
| FOUNDATION | `/companies/foundation/` | All operations, EU expansion |
| MED | `/canonic/med/` | Healthcare sublanguage |
| MED.EU | `/companies/onconex/eu/` | European medical operations |
| LAW | `/canonic/` (root) | CANONIC legal counsel |
| LAW.IP | `/patents/` | Intellectual property |
| Infrastructure | `/canonic/` | Technical stack |

---

## Step 3: The CANONIC Way

### Read First

Before making changes, read the relevant files:
- `CANON.md` — Governance (axioms, rules)
- `VOCAB.md` — Vocabulary (definitions)
- `README.md` — Description (current state)
- `{SCOPE_NAME}.md` — Specification (closes scope)

### Write to SPEC

**Never edit CANON directly.** Edit the specification (`{SCOPE_NAME}.md`).

```
You write SPEC (what you want)
    ↓
SPEC drifts to CANON (governance emerges)
    ↓
LLM validates (CANONIC does the work)
```

### Commit Everything

Every decision is a commit:

```bash
git add .
git commit -m "DECISION: description of what changed"
git push
```

The git history IS the ledger.

---

## Step 4: Domain-Specific Guides

### Fatima (FOUNDATION)

Your scope: `/companies/foundation/`

Key files:
- [CANON.md](/companies/foundation/CANON.md) — Foundation axioms
- [FOUNDATION.md](/companies/foundation/FOUNDATION.md) — Master plan
- [assets/](/companies/foundation/assets/) — Asset registry

Your responsibilities:
- Coordinate EU expansion with Neville
- Manage Foundation operations
- Oversee all sublanguage domains

```bash
# Example: Update Foundation operations
cd companies/foundation
# Edit FOUNDATION.md with your changes
git add FOUNDATION.md
git commit -m "FOUNDATION: updated EU expansion timeline"
git push
```

---

### Neville (MED.EU, OncoNex.EU)

Your scope: `/companies/onconex/eu/`

Key files:
- [CANON.md](/companies/onconex/eu/CANON.md) — EU governance
- [ONCONEX-EU.md](/companies/onconex/eu/ONCONEX-EU.md) — EU specification

Your responsibilities:
- Chair OncoNex.EU board
- Coordinate with Fatima on Foundation matters
- Govern MED.EU operations

```bash
# Example: Board decision
cd companies/onconex/eu
# Edit ONCONEX-EU.md with board decision
git add ONCONEX-EU.md
git commit -m "BOARD: decision on EU clinical partnerships"
git push
```

---

### David (LAW)

Your scope: Root CANONIC + `/companies/`

Key files:
- [CANON.md](/canonic/CANON.md) — Root governance
- [/companies/CANON.md](/companies/CANON.md) — Company governance

Your responsibilities:
- CANONIC legal counsel
- Foundation legal matters
- Contract review

```bash
# Example: Legal review
# Edit relevant SPEC with legal guidance
git add .
git commit -m "LEGAL: reviewed partnership agreement terms"
git push
```

---

### Fitch (LAW.IP)

Your scope: `/patents/`

Key files:
- [IP-REGISTRY.md](/patents/IP-REGISTRY.md) — Full IP portfolio
- IDF files — Invention disclosures

Your responsibilities:
- IP strategy
- Patent applications
- IDF review

```bash
# Example: New IDF
cd patents/disclosures
# Create new IDF file
git add idf-164-*.md
git commit -m "IDF-164: new invention disclosure"
git push
```

---

### Anurag (Infrastructure)

Your scope: `/canonic/` technical stack

Key files:
- [/.github/](/canonic/.github/) — APPSTORE (GitHub = App Store)
- [/language/templates/](/canonic/language/templates/) — Governance templates
- Validators

Your responsibilities:
- Technical infrastructure
- VaaS implementation
- GitHub Actions / CI

```bash
# Example: Validator update
# Edit validator code
git add .
git commit -m "INFRA: updated triad validator"
git push
```

---

## Step 5: Communication

All team communication happens through:

1. **Git commits** — Decisions are ledgered
2. **GitHub Issues** — Discussions tracked
3. **GitHub PRs** — Changes reviewed

No decisions in email/Slack/etc. that aren't committed.

---

## Step 6: Validation

Before pushing, validate:

```bash
# Check triad exists
ls CANON.md VOCAB.md README.md

# Check inheritance
grep "inherits:" CANON.md

# Check SPEC exists (for closed scopes)
ls {SCOPE_NAME}.md
```

GitHub Actions will run VaaS validators automatically.

---

## Quick Reference

| Action | Command |
|--------|---------|
| Get latest | `git pull` |
| See changes | `git status` |
| Stage changes | `git add .` |
| Commit | `git commit -m "TYPE: description"` |
| Push | `git push` |
| View history | `git log --oneline` |

Commit types:
- `DECISION:` — Governance decision
- `LEGAL:` — Legal review/guidance
- `BOARD:` — Board decision
- `INFRA:` — Infrastructure change
- `IDF-NNN:` — Invention disclosure
- `FOUNDATION:` — Foundation operations

---

## The Magic

Think as ambitious as possible. Write what you want in SPEC. CANONIC does the work.

```
Human ambition → SPEC
Natural drift → CANON
LLM execution → Implementation
```

No databases. No servers. No cron. Just Git + CANONIC + LLM.

---

## Support

- Manual: [/.github/CANONIC-MANUAL.md](CANONIC-MANUAL.md)
- Archive: [/.archive/CANONIC.md](../.archive/CANONIC.md)
- Endpoint state: What "done" looks like

---

**Welcome to CANONIC. Govern via Git.**

---
