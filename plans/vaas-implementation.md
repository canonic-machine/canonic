# VaaS Implementation Plan

**Version:** 0.1.0 (Draft)
**Date:** 2026-01-21
**Objective:** Wire existing VaaS validators to LEDGER commits
**Status:** INVESTIGATION

---

## Discovery

VaaS already exists at `/validators/` (CANONBASE level):

```
/Canonic/validators/
├── CANON.md
├── COVERAGE.md
├── VALIDATORS.md
├── VOCAB.md
├── README.md
├── canonic/
│   ├── validator_as_a_service.py  ← Orchestrator
│   ├── triad.py                   ← Axiom 0
│   ├── inheritance.py             ← Axiom 1
│   ├── introspection.py           ← Axiom 2
│   ├── compliance.py              ← Enterprise tier
│   ├── language.py                ← LANGUAGE validation
│   └── language_canon.py          ← LANGUAGE CANON
├── coin_validators/
├── token_validators/
└── tests/
```

**Status:** VaaS runs successfully. Found 64 scopes, 2 pass, 62 fail (incomplete TRIADs).

---

## The Problem

Git hooks in `/canonic/.githooks/` search for validators but can't find them:

```bash
# Hook search paths:
$REPO_ROOT/canonic/validators/validator_as_a_service.py  # NOT FOUND
$REPO_ROOT/validators/validator_as_a_service.py          # NOT FOUND (different repo)
```

The hooks are in `/canonic/` repo, but validators are in `/validators/` repo.
They're siblings at CANONBASE level, not nested.

---

## Investigation Needed

### Question 1: Validators repo structure
- Is `/validators/` its own git repo?
- What's the remote? Where does it push?
- Is it part of CANONBASE multi-repo or standalone?

### Question 2: Hook wiring options

**Option A: Environment variable**
```bash
export CANONIC_VALIDATORS_ROOT="/path/to/Canonic/validators"
```
Hooks already support `$CANONIC_VALIDATORS_ROOT` override.

**Option B: Symlink**
```bash
ln -s ../validators /canonic/validators
```
Git won't track symlink target, but hooks will find it.

**Option C: Modify hook search**
Update hooks to search parent directory (CANONBASE level).

**Option D: Submodule**
Add `/validators/` as git submodule in `/canonic/`.

### Question 3: CANONBASE validation scope
- Should VaaS validate entire CANONBASE or just the committing repo?
- 62/64 scopes fail - is that expected WIP state?
- What's the minimum viable LEDGER commit validation?

---

## Current Test Results

```
python3 validators/canonic/validator_as_a_service.py /Canonic

Found 64 scopes
PASS: 2 (language, language/templates)
FAIL: 62 (missing VOCAB.md, README.md, or introspection gaps)
```

Notable:
- `/transcript/` fails on INTROSPECTION (16 undefined terms in VOCAB.md)
- `/validators/` fails on INTROSPECTION (19 undefined terms in VOCAB.md)
- Most scopes missing VOCAB.md and README.md entirely

---

## Next Steps

1. Investigate `/validators/` repo structure
2. Decide on hook wiring approach (A, B, C, or D)
3. Decide on validation scope (repo vs CANONBASE)
4. Fix `/transcript/VOCAB.md` to pass introspection
5. Document decision in this plan

---

*Governed by: /canonic/CANON.md*
