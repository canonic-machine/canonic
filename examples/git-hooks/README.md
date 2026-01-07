# Git Hooks for CANONIC Systems

**Self-healing and self-documenting automation.**

---

## Installation

To activate these hooks in your local repository:

```bash
# Copy hooks to .git/hooks/ directory
cp hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

---

## Available Hooks

### pre-commit

**Purpose:** Enforce README regeneration when governance files change

**Trigger:** Before git commit completes

**Behavior:**
1. Detects if `CANON.md` or `VOCABULARY.md` are staged
2. If yes, checks if `README.md` is also staged
3. If `README.md` not staged, blocks commit with violation message
4. If `README.md` is staged, allows commit to proceed

**Implements:** Self-documenting protocol from CANON.md

**Validation type:** Syntactic (checks staging status, not content)

---

## Usage

### Normal workflow (no governance changes)

```bash
git add prose/draft.md
git commit -m "Apply composition constraints"
# ✅ Commit proceeds normally
```

### Governance change workflow

```bash
# Edit CANON.md
git add CANON.md

# Attempt commit
git commit -m "Canonify README generation protocol"
# ❌ Hook blocks: README.md not staged

# Regenerate README.md
generate-readme  # or manually update

# Stage README
git add README.md

# Commit both
git commit -m "Canonify README generation protocol"
# ✅ Commit proceeds with both CANON.md and README.md
```

---

## Validation Script

Complementary validation for README staleness:

```bash
#!/bin/bash
# validate-readme-freshness.sh
# Syntactic check: README timestamp vs source timestamps

CANON_TIME=$(stat -f %m CANON.md)
VOCAB_TIME=$(stat -f %m VOCABULARY.md)
README_TIME=$(stat -f %m README.md)

if [ $README_TIME -lt $CANON_TIME ] || [ $README_TIME -lt $VOCAB_TIME ]; then
  echo "❌ README.md is stale"
  echo "   README modified: $(date -r $README_TIME)"
  echo "   CANON modified:  $(date -r $CANON_TIME)"
  echo "   VOCAB modified:  $(date -r $VOCAB_TIME)"
  exit 1
else
  echo "✅ README.md is fresh"
  exit 0
fi
```

---

## Semantic Validation

The pre-commit hook performs **syntactic validation** (staging status).

For **semantic validation** (content completeness), use an LLM-based validator:

```bash
# Semantic README validator (requires LLM)
validate-readme-completeness \
  --canon CANON.md \
  --vocabulary VOCABULARY.md \
  --readme README.md
```

This checks:
- All CANON constraints represented in README
- All VOCABULARY terms explained in README
- Primary outputs documented in README
- No undefined terms used in README

---

## Self-Healing Integration

These hooks implement the **self-healing** property by detecting governance change patterns and triggering validation.

Git violation signals:
- CANON changed without README → blocked
- VOCABULARY changed without README → blocked
- README stale → flagged by validation

---

## Repository-Specific Hooks

Different repository types may need specialized hooks:

**Governance repos (canonic/):**
- Pre-commit: README regeneration check
- Pre-push: Protocol validation

**Implementation repos (machine/):**
- Pre-commit: README + LEARNINGS synchronization
- Pre-push: FSM validation

**Domain repos (writing/):**
- Pre-commit: Output artifact validation
- Pre-push: Traceability checks

---

End of hooks README.
