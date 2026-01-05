# CANON (canonic-programming/examples/)

**Governance for CANONIC programming examples.**

Inherits: canonic-programming/ → examples/

---

## Purpose

This directory contains demonstration examples of CANONIC programming systems, from simplest to most complex.

Examples show the paradigm in action, not just theory.

---

## Example Requirements

### Each example must:

- Contain complete triad (CANON, VOCABULARY, README)
- Be runnable without external dependencies (beyond Python stdlib)
- Demonstrate specific CANONIC concept clearly
- Include validation that can be executed
- Document what it teaches

### Example progression:

1. **hello-world/** — Minimal system (one file, one constraint)
2. **canonical-readme/** — Structured document governance
3. **simple-fsm/** — Basic finite state machine with validation gates

---

## Constraints

### Simplicity

- Examples must be understandable in < 5 minutes
- No unnecessary complexity
- Focus on one concept per example
- Clear input → validation → output flow

### Self-containment

- Each example is independent
- No cross-example dependencies
- Can be copied and modified standalone
- Works out of the box

### Traceability

- README explains what the example demonstrates
- CANON shows constraints being enforced
- VOCABULARY defines example-specific terms
- Clear connection to paradigm concepts

---

## Forbidden

- Examples that require installation steps
- Examples that depend on external services
- Examples that violate root CANON invariants
- Examples without clear learning objective

---

## Future Examples

Additional examples may be added:

- Multi-file document system
- Collaboration patterns (multiple authors)
- FSM with backflow
- Token-optimized CANONs
- Protocol composition

Each follows same structure: triad + runnable demo + clear concept.

---

End of examples CANON.
