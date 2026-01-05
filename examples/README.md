# Examples

**Demonstrations of CANONIC programming in action.**

This directory contains self-contained examples showing the paradigm from simple to complex.

---

## Available Examples

### hello-world/ (Coming Soon)
The simplest CANONIC system.
- One file: `hello.txt`
- One constraint: Content must be exactly "Hello, world."
- Demonstrates: Core validation loop

### canonical-readme/ (Coming Soon)
A governed README with structural requirements.
- Demonstrates: Document structure validation
- Shows: Required sections, heading hierarchy, format rules

### simple-fsm/ (Coming Soon)
Basic finite state machine with validation gates.
- Demonstrates: State transitions, validation gates, backflow
- Shows: How CANONIC FSMs work

---

## How to Use Examples

Each example is self-contained:

1. **Read the README** — Understand what it demonstrates
2. **Check the CANON** — See the constraints
3. **Run validation** — Execute the example
4. **Modify and re-validate** — Learn by experimenting

**General validation command:**
```bash
python3 ../tools/validation/run_validation.py example-name/
```

---

## Example Structure

Every example follows the same pattern:

```
example-name/
├── CANON.md          # Constraints
├── VOCABULARY.md     # Terms
├── README.md         # Explanation
└── [artifacts]       # Files being validated
```

---

## Learning Path

**Start here:** hello-world/ — Core concepts  
**Then:** canonical-readme/ — Document governance  
**Finally:** simple-fsm/ — State machines

For complex applications, see [Writing Machine](https://github.com/iDrDex/writing-machine)

---

## Creating Your Own

To create a CANONIC system based on these examples:

1. Copy an example directory
2. Modify CANON.md with your constraints
3. Update VOCABULARY.md with your terms
4. Create your artifacts
5. Run validation
6. Fix violations until compliant

---

## Notes

Examples are intentionally minimal. They demonstrate concepts, not production systems.

For real-world usage, see the Writing Machine repository which uses CANONIC programming for complex document workflows.

---

End of examples README.
