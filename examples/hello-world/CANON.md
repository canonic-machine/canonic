# CANON (examples/hello-world/)

**Inherits from:** canonic-programming/examples/

## Invariants

### Required artifacts
**Directory must contain:**
- CANON.md
- VOCABULARY.md
- README.md
- hello.txt

**Violation:** Missing any required artifact

### Content constraints
**hello.txt must:**
- Contain exactly the text "Hello, world."
- Include the period at the end
- Contain no additional whitespace or newlines before or after
- Use UTF-8 encoding

**Violation:** hello.txt content does not match exactly "Hello, world."

### Example constraints
**Example must:**
- Be understandable in < 5 minutes
- Run without external dependencies
- Demonstrate core validation loop: canon → artifact → validation → acceptance

**Violation:** Example violates simplicity or demonstration requirements

---

End of hello-world CANON.
