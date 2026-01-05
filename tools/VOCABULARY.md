# VOCABULARY (canonic-programming/tools/)

**Tool-specific term definitions.**

Inherits all terms from canonic-programming/VOCABULARY.md

---

## Tool Terms

### syntactic validation
Fast, cheap validation that checks structural requirements: file existence, naming conventions, ID formatting, reference resolution. Does not assess meaning or intent.

### validation engine
The core implementation that loads CANONs, checks artifacts, and reports violations. Located in tools/validation/

### exit code
Integer returned by a command-line tool. 0 = success, 1 = failure, 130 = user interrupt (Ctrl+C).

### violation report
Structured output listing all constraint failures with artifact path, line number, requirement reference, and details.

### deterministic tool
Tool that produces identical output for identical input. No randomness, no time-dependent behavior (except timestamps in metadata).

### read-only validation
Validation that examines artifacts without modifying them. All CANONIC validation must be read-only.

---

End of tools VOCABULARY.
