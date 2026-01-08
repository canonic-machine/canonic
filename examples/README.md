# CANONIC Programming Examples

This directory contains three examples demonstrating CANONIC programming concepts through progressive complexity.

## Examples Overview

### 1. hello-world/
**Simplest possible CANONIC system**

- Single file (`hello.txt`)
- Single constraint ("Hello, world.")
- Minimal Python validator (56 lines)
- Demonstrates: Basic constraint validation

**Use this to understand:** How constraints define validity, how validation enforces constraints.

### 2. simple-fsm/
**State machine with validation gates**

- Three states: draft → review → published
- Transition validation at each gate
- Backflow on validation failure
- Python FSM implementation (177 lines)
- Demonstrates: Git-FSM pattern, validation gates, state transitions

**Use this to understand:** How commits are state transitions, how validation gates work, how backflow corrects violations.

### 3. canonic-readme/
**Document governance with nested structure**

- Nested triad structure (project/ subdirectory)
- Inheritance demonstration
- Rich constraints (engagement, structure, code quality)
- Demonstrates: Triad composition, inheritance chains, governance layers

**Use this to understand:** How triads nest, how inheritance works, how constraints compose.

## Pedagogical Progression

Each example teaches specific concepts:

1. **hello-world**: Constraint + validation fundamentals
2. **simple-fsm**: State machines + git-FSM implementation
3. **canonic-readme**: Triad composition + inheritance

Start with hello-world, proceed to simple-fsm, finish with canonic-readme.

## Running Examples

- Each example directory contains:
- Complete triad (CANON.md, VOCAB.md, README.md)
- Validation implementation (Python scripts)
- Example artifacts to validate

See individual example README.md files for specific instructions.

---

Generated from CANON.md + VOCAB.md + examples structure
