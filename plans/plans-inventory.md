# Plans Inventory

**Version:** 0.1.0
**Date:** 2026-01-21
**Session:** tx020
**Status:** ACTIVE

---

## Summary

| Scope | Plans | Total Size | Sessions |
|-------|-------|------------|----------|
| `/transcript/plans/` | 3 | ~14KB | tx020 |
| `/language/plans/` | 10 | ~560KB | tx016-tx018 |
| `/canonic/plans/` | 5 | ~70KB | tx019-tx020 |

---

## /transcript/plans/ (tx020)

| File | Status | Purpose |
|------|--------|---------|
| `multirepo-duplicate-resolution.md` | DECIDED | TypeScript vs Python - Python wins |
| `transcript-drift-analysis.md` | COMPLETE | Session indexing architecture |
| `vibe-signal-design.md` | DESIGN | Sentiment signal extraction |

---

## /language/plans/ (tx016-tx018, KiloCode)

| File | Size | Status | Purpose |
|------|------|--------|---------|
| `canonic-workflow-methodology.md` | 58KB | SPEC | Workflow principles |
| `canonical-workflow-implementation-roadmap.md` | 90KB | SPEC | Adoption roadmap |
| `canonverse-coverage-analysis.md` | 45KB | COMPLETE | LANGUAGE generative capacity |
| `formal-sufficiency-verification.md` | 67KB | COMPLETE | 100% formal sufficiency verified |
| `kilocode-rules-evaluation.md` | 35KB | ANALYSIS | .kilocode/rules need assessment |
| `language-audit-report.md` | 33KB | COMPLETE | LANGUAGE v0.1 redundancies |
| `language-v0.2-validation-report.md` | 52KB | COMPLETE | LANGUAGE v0.2 validated |
| `multi-repo-workflow-architecture.md` | 102KB | SPEC | Multi-repo system design |
| `system-validation-report.md` | 25KB | PARTIAL | TypeScript system validation |
| `template-architecture-analysis.md` | 52KB | COMPLETE | Template generative capacity |

**Note:** These plans reference TypeScript code in `/language/src/` which is now archived at `/language/.archive/src-tx016/`.

---

## /canonic/plans/ (tx019-tx020)

| File | Size | Status | Purpose |
|------|------|--------|---------|
| `language-refinement-plan.md` | 10KB | DRAFT | LANGUAGE CANON refinement |
| `language-spec-audit.md` | 14KB | CRITICAL | Closure definition INVERSION found |
| `template-architecture-analysis.md` | 39KB | IN_PROGRESS | Template restructuring |
| `vaas-implementation.md` | 3KB | INVESTIGATION | VaaS wiring to LEDGER |
| `plans-inventory.md` | - | ACTIVE | This file |

---

## Archive Candidates

Plans that reference archived code should be reviewed:

1. `/language/plans/system-validation-report.md` - References TypeScript system
2. `/language/plans/multi-repo-workflow-architecture.md` - 102KB architecture for archived code

These may need:
- Archival alongside the TypeScript code
- Update to reference Python implementation
- Status change to SUPERSEDED

---

## Critical Findings

### language-spec-audit.md
**INVERTED closure definitions** in LANGUAGE.md:
- ROADMAP defined as InternalClosure (should be ExternalClosure)
- COVERAGE defined as ExternalClosure (should be InternalClosure)

**Status:** Needs fix in LANGUAGE.md

### vaas-implementation.md
**Validators exist** at `/validators/` but hooks can't find them:
- `/canonic/.githooks/` searches wrong paths
- Need wiring solution (env var, symlink, or hook update)

---

## Vibe Signals

- `bloat: bad` - `/language/plans/` has 560KB of plans for archived TypeScript
- `drift: bad` - Plans reference code that no longer exists at those paths

---

*Governed by: /canonic/CANON.md*
