# Simple FSM Example

State machine demonstrating validation gates and backflow.

## What This Demonstrates

- **Three states**: draft → review → published
- **Validation gates**: Constraints checked at each transition
- **Backflow pattern**: Failed validation returns to source state
- **Git-FSM concept**: State transitions map to file movements

This example shows how CANONIC systems enforce state machine constraints through validation.

## State Machine

```
draft → review → published
  ↑       ↓
  └───────┘ (backflow on validation failure)
```

## States

### draft
- File: `draft.txt`
- Purpose: Initial content creation
- Requirements: Content exists (may be incomplete)

### review
- File: `review.txt`
- Purpose: Content ready for validation
- Requirements: Complete sentences, proper capitalization, ends with period

### published
- File: `published.txt`
- Purpose: Validated, accepted output
- Requirements: All review requirements + no spelling errors + ≥3 lines

## How to Run

### Transition: draft → review

1. Create `draft.txt`:
   ```
   This is a draft.
   ```

2. Run transition:
   ```bash
   python transition.py draft review
   ```

3. If valid, content moves to `review.txt`

### Transition: review → published

1. Ensure `review.txt` has valid content:
   ```
   This is complete content.
   It has multiple sentences.
   All requirements are satisfied.
   ```

2. Run transition:
   ```bash
   python transition.py review published
   ```

3. If valid, content moves to `published.txt`

## Backflow Demonstration

1. Create invalid content in `review.txt`:
   ```
   incomplete
   ```

2. Attempt transition to published:
   ```bash
   python transition.py review published
   ```

3. Validation fails, content remains in `review.txt`

4. Fix violations and retry

This demonstrates the enforcement layer: you cannot transition to published with invalid content.

## Files

- [CANON.md](CANON.md) - FSM constraints
- [DICTIONARY.md](DICTIONARY.md) - Term definitions
- [README.md](README.md) - This guide
- `transition.py` - State transition implementation
- `draft.txt` - Draft state content
- `review.txt` - Review state content (after transition)
- `published.txt` - Published state content (after transition)

---

Generated from CANON.md + DICTIONARY.md
