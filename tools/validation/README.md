# tools/validation/

The validation tool implements syntactic validation—mechanical checking of structural constraints that can be verified without semantic understanding.

---

## Validation Layers

### Syntactic Validation (This Tool)

Automated checking of mechanical constraints:
- File existence and naming patterns
- ID format and sequencing
- Reference integrity (assets, episodes)
- Structural ordering (sections)
- Triad completeness

**Implementation**: Python scripts using regex, file I/O, and parsing.

### Semantic Validation (LLM-Required)

Constraint checking requiring interpretation:
- CANON coherence and consistency
- VOCABULARY term usage correctness
- README accuracy against CANONs
- Prose quality and coherence
- True constraint satisfaction (intent vs syntax)

**Implementation**: LLM reads CANONs and evaluates artifacts for compliance.

---

## Governance Chain
```
root/CANON.md
  ↓
tools/CANON.md (defines validation requirements)
  ↓
tools/validation/CANON.md (specializes for syntactic checks)
```

---

## Invocation

### Direct Execution
```bash
# Run syntactic validation
python3 tools/validation/run_validation.py

# Run tests
python3 tools/validation/test_validation.py
```

### Via CLI
```bash
# Full validation (syntactic checks)
python3 tools/wm validate

# Quick format checks
python3 tools/wm check
```

---

## What This Tool Checks

### Syntactic Checks (Implemented)

1. **Triad completeness**: Every directory has CANON.md, VOCABULARY.md, README.md
2. **Required artifacts**: Files listed in root CANON.md exist
3. **Asset ID format**: `asset-\d{4}` (exactly 4 digits)
4. **Asset ID sequencing**: Sequential numbering from 0001
5. **Episode filename format**: `episode-\d{2}\.md` (exactly 2 digits)
6. **Prose asset references**: All asset-NNNN exist in LEDGER.md
7. **Asset source episodes**: Referenced episodes exist in episodes/
8. **Structure section order**: Prose sections match outline.md order

### What This Tool Cannot Check

These require LLM semantic validation:

- Whether CANON constraints are internally consistent
- Whether VOCABULARY terms are used correctly in context
- Whether README guidance accurately reflects CANONs
- Whether prose is coherent and well-written
- Whether artifacts satisfy CANON intent (beyond syntax)

For semantic validation, use an LLM agent to read CANONs and evaluate compliance.

---

## Output Format

```
COMPLIANCE REPORT
Status: compliant | invalid
Violations: N

1. Artifact: path/to/file
   Line: N
   Requirement: CANON.md:X-Y (Section name)
   Details: Specific violation description

...
```

Exit codes:
- 0: Compliant (all syntactic checks pass)
- 1: Invalid (violations found)

---

## Test Coverage

11 automated tests covering:
- Asset ledger parsing (format, sequencing)
- Episode validation (naming)
- Prose reference checking
- Structure validation (parsing, ordering)
- Asset source validation

Run with: `python3 tools/validation/test_validation.py`

---

## Limitations

This tool performs **syntactic validation only**. It verifies:
- Structure exists
- Formats match patterns
- References resolve

It does NOT verify:
- Meaning is correct
- Content is high quality
- CANONs are well-designed
- Intent is satisfied

For comprehensive compliance, combine syntactic validation (this tool) with semantic validation (LLM review).
