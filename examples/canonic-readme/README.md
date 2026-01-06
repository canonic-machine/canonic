# Canonic README Example

## What This Example Demonstrates

This example shows how to use CANONIC programming to govern a simple project README. It demonstrates:

1. **The Triad Pattern** - Every directory has CANON.md, VOCABULARY.md, and README.md
2. **Constraint Definition** - How to write clear, enforceable constraints
3. **Validation Gates** - How validation enforces constraints
4. **Inheritance** - How constraints cascade from parent to child

## Example Structure

```
canonic-readme/
├── CANON.md           # Governance for this example
├── VOCABULARY.md      # Terms (inherits from parent)
├── README.md          # This file
└── project/           # Sample project being governed
    ├── CANON.md       # Sample project constraints
    ├── VOCABULARY.md  # Sample project terms
    └── README.md      # The artifact being validated
```

## How to Use This Example

### Step 1: Understand the Constraint
Read `project/CANON.md` to see what constraints govern the sample README.

### Step 2: Review the Artifact
Read `project/README.md` to see the compliant README.

### Step 3: Run Validation
From the repository root:
```bash
python tools/validation/run_validation.py
```

This validates that all triads are present and properly structured.

### Step 4: Experiment
Try modifying `project/README.md` to violate constraints, then re-run validation to see it fail.

## What Makes This "CANONIC"

- **Constraints are declarative**: The CANON.md states what must be true, not how to achieve it
- **Validation is automatic**: The validator checks compliance mechanically
- **Work is traced**: The README artifact must comply with stated constraints
- **No executable code in governance**: CANON.md contains only English constraints

## Key Takeaway

CANONIC programming separates "what must be true" (CANON) from "the work" (README). This separation makes the system durable - constraints persist even as tools and authors change.
