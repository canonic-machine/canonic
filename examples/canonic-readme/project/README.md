# Project Example

Demonstrates inheritance chain and code governance.

## What This Code Does

The `example.py` script demonstrates:
1. Runnable Python code (satisfies parent constraint)
2. Type annotations (satisfies local constraint)
3. Docstrings (satisfies local constraint)
4. Practical CANONIC validation pattern

## Inheritance Chain

This directory inherits constraints from:

1. `../../CANON.md` (examples root)
   - Progressive complexity requirement

2. `../CANON.md` (canonic-readme root)
   - Engagement requirement
   - Technical accuracy requirement
   - Reference resolution requirement

3. `./CANON.md` (this directory)
   - Python type checking requirement
   - Docstring requirement
   - Example execution requirement

All constraints compose - this code must satisfy ALL levels.

## How to Run

```bash
python example.py
```

Expected output:
```
✓ Demonstrating CANONIC constraint validation
✓ All inherited constraints satisfied
```

## Type Checking

```bash
mypy example.py
```

Should produce no errors (satisfies type checking constraint).

## Files

- [CANON.md](CANON.md) - Project-specific constraints
- [DICTIONARY.md](DICTIONARY.md) - Project-specific terms
- [README.md](README.md) - This guide
- `example.py` - Runnable Python example

## Constraint Satisfaction

| Constraint | Source | Status |
|-----------|---------|---------|
| Progressive complexity | examples/CANON.md | ✓ Part of 3-example progression |
| Engaging documentation | ../CANON.md | ✓ Clear structure, examples |
| Technical accuracy | ../CANON.md | ✓ Correct descriptions |
| Reference resolution | ../CANON.md | ✓ All files exist |
| Type checking | ./CANON.md | ✓ Passes mypy |
| Docstrings | ./CANON.md | ✓ All functions documented |
| Runs without errors | ./CANON.md | ✓ Executes successfully |

---

Generated from CANON.md + DICTIONARY.md + example.py
