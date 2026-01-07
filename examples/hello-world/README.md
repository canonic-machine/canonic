# Hello World

**The simplest CANONIC system.**

This example demonstrates the core validation loop with minimal complexity.

---

## What This Demonstrates

**Core Concept:** Binary validation (pass/fail)

The system has:
- **One file:** `hello.txt`
- **One constraint:** Content must be exactly "Hello, world."
- **One validation:** Check if content matches

This is CANONIC programming at its simplest:

```
CANON.md defines: "hello.txt must contain exactly 'Hello, world.'"
↓
hello.txt exists with content
↓
Validation checks: Does content match exactly?
↓
Pass → Accept | Fail → Reject
```

---

## How to Use

### 1. Read the CANON
Open [CANON.md](CANON.md) to see the constraints.

### 2. Check the artifact
Look at [hello.txt](hello.txt) to see the governed content.

### 3. Run validation
```bash
python3 validate.py
```

Expected output:
```
✓ hello.txt exists
✓ Content matches exactly
Validation: PASS
```

### 4. Experiment
Try modifying `hello.txt`:
- Add a space: "Hello, world. "
- Remove the period: "Hello, world"
- Change capitalization: "hello, world."

Then re-run validation to see it fail.

---

## What You Learn

1. **Binary validation**: Either compliant or not, no subjective judgment
2. **Exact constraints**: CANON specifies precisely what must be true
3. **Validation gates**: Invalid artifacts are rejected, not accepted
4. **No execution**: The file doesn't "run" — it's validated

This is the foundation. All CANONIC systems follow this pattern:
- Define constraints (CANON)
- Create artifacts (work)
- Validate compliance (gate)
- Accept or reject (enforcement)

---

## Next Steps

After understanding this example:
- Try [canonic-readme/](../canonic-readme/) for document structure validation
- Try [simple-fsm/](../simple-fsm/) for state machine governance

---

End of hello-world README.
