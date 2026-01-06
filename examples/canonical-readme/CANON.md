# CANON: Canonical README Example

## Purpose
Demonstrate CANONIC programming applied to a simple README generation project.

## Inherits From
- `../../CANON.md` (Root canonical constraints)
- `../CANON.md` (Examples governance)

## Required Artifacts

1. **CANON.md** (this file)
   - Defines constraints for this example

2. **VOCABULARY.md**
   - Defines example-specific terms

3. **README.md**
   - Explains what this example demonstrates
   - Provides usage instructions

4. **project/CANON.md**
   - Sample project canon for a hypothetical "Hello World" library

5. **project/VOCABULARY.md**
   - Sample vocabulary for the hypothetical project

6. **project/README.md**
   - The README artifact that would be validated

## Constraints

### C1: Simplicity
This example must remain simple enough to understand in under 5 minutes.

### C2: Self-Contained
The example must be runnable without external dependencies beyond Python 3.7+.

### C3: Demonstrates Core Concepts
The example must demonstrate:
- Triad requirement
- Constraint definition
- Validation gate
- Pass/fail output

## Validation
Run validation from repository root:
```bash
python tools/validation/run_validation.py
```
