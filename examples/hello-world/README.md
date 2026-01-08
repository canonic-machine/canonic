# Hello World Example

The simplest possible CANONIC system.

## What This Demonstrates

- **One file**: `hello.txt`
- **One constraint**: Content must be exactly "Hello, world."
- **One validator**: Python script checking exact match

This example shows the fundamental CANONIC pattern: constraint + validation.

## The Constraint

From [CANON.md](CANON.md):

> hello.txt must contain exactly: "Hello, world."

This is declarative governance. The CANON states what must be true.

## How to Run

1. Create `hello.txt` with content:
   ```
   Hello, world.
   ```

2. Run validation:
   ```bash
   python validate.py
   ```

3. Expected output:
   ```
   ✓ hello.txt validates successfully
   ```

## What Happens on Failure

Try modifying `hello.txt` to contain `Hello, World!` (capital W) and run validation again.

The validator will reject the change:
```
✗ Validation failed: Content must be exactly "Hello, world."
```

This demonstrates the enforcement layer: constraints define validity, validation gates acceptance.

## Files

- [CANON.md](CANON.md) - The constraint specification
- [VOCAB.md](VOCAB.md) - Term definitions
- [README.md](README.md) - This guide
- `validate.py` - Validation implementation
- `hello.txt` - The artifact under governance

---

Generated from CANON.md + VOCAB.md
