# Canonic README Example

Document governance demonstrating nested triads and inheritance.

## What This Demonstrates

- **Nested triad structure**: project/ subdirectory has its own triad
- **Inheritance chains**: project/CANON.md inherits from ./CANON.md
- **Constraint composition**: Child constraints specialize parent constraints
- **Document governance**: CANONs govern documentation, not just code

This example shows how CANONIC systems compose through inheritance.

## Structure

```
canonic-readme/
├── CANON.md          (root constraints: engagement, accuracy, references)
├── DICTIONARY.md     (term definitions)
├── README.md         (this file)
└── project/
    ├── CANON.md      (inherits from ../, adds project-specific constraints)
    ├── DICTIONARY.md (inherits terms, adds project-specific terms)
    ├── README.md     (project documentation)
    └── example.py    (runnable code demonstrating concepts)
```

## Inheritance Chain

1. **examples/CANON.md** (grandparent)
   - Defines: Example progression requirement

2. **canonic-readme/CANON.md** (parent)
   - Inherits: Example requirements
   - Adds: Document engagement, technical accuracy, reference resolution

3. **canonic-readme/project/CANON.md** (child)
   - Inherits: All document constraints
   - Adds: Project-specific code quality requirements

Each level adds constraints without contradicting upstream invariants.

## How Inheritance Works

### Parent Constraints (from ./CANON.md)

- Documentation must be engaging
- Code examples must be runnable
- References must resolve

### Child Specialization (in project/CANON.md)

- Inherits all parent constraints (via `**Inherits from:** ../CANON.md`)
- Adds Python-specific requirements
- Cannot contradict parent constraints

This demonstrates **inheritance without contradiction** - the core principle of CANONIC composition.

## Validation

To validate this example:

```bash
cd project/
python example.py
```

The code runs successfully, demonstrating:
1. Runnable code requirement satisfied
2. Technical accuracy validated
3. References resolve (example.py exists)

## Files

- [CANON.md](CANON.md) - Root document constraints
- [DICTIONARY.md](DICTIONARY.md) - Term definitions
- [README.md](README.md) - This guide
- [project/](project/) - Nested triad with inheritance

---

Generated from CANON.md + DICTIONARY.md + structure
