# Examples

**Demonstrations of CANONIC programming in action.**

This directory contains self-contained examples showing the paradigm from simple to complex.

---

## Available Examples

### hello-world/
The simplest CANONIC system.
- One file: `hello.txt`
- One constraint: Content must be exactly "Hello, world."
- Demonstrates: Core validation loop
- **Status:** Complete and runnable

### canonic-readme/
A governed README with structural requirements.
- Demonstrates: Document structure validation, inheritance chains
- Shows: Required sections, heading hierarchy, format rules
- **Status:** Complete and runnable

### simple-fsm/
Basic finite state machine with validation gates.
- Demonstrates: State transitions, validation gates, backflow
- Shows: How CANONIC FSMs work in practice
- **Status:** Complete and runnable

---

## How to Use Examples

Each example is self-contained:

1. **Read the README** — Understand what it demonstrates
2. **Check the CANON** — See the constraints
3. **Run validation** — Execute the example
4. **Modify and re-validate** — Learn by experimenting

**Example-specific validation:**
```bash
cd hello-world/ && python3 validate.py
cd simple-fsm/ && python3 transition.py review
```

See each example's README for detailed usage instructions.

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
**Then:** simple-fsm/ — State machines and validation gates
**Finally:** canonic-readme/ — Document governance with inheritance

For complex applications, see [Writing Machine](https://github.com/canonic-machine/writing)

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
