# Session Learnings: 2026-01-06

**Insights discovered during implementation of examples and tools.**

These learnings should be canonified into future CANON constraints.

---

## Validator Gaps Discovered

### 1. Content After Termination Markers
**Issue:** Validator failed to detect garbage content appended after "End of [file] CANON." statements.

**Example:** tools/CANON.md had TODO list content after "End of tools CANON."

**Learning:** Syntactic validation must check:
- No content after "End of [name] CANON." or "End of [name] VOCABULARY."
- File must terminate cleanly
- Any content after termination marker is a violation

**Impact:** This was caught by human review, not validator - validator gap.

**Canonify as:** 
```
### File termination
**CANON.md and VOCABULARY.md files must terminate after end marker.**
- No content allowed after "End of [name] CANON."
- No content allowed after "End of [name] VOCABULARY." 
- Blank lines after termination marker are allowed

**Violation:** Content exists after file termination marker
```

---

## 2. Reference Integrity Patterns

### Cross-Repository References
**Pattern:** Implementation repositories reference governance specifications.

**Correct:**
- `machine/AGENTS.md` → implements `CANONIC.md` protocols
- `machine/README.md` → references `MACHINE.md` (repository spec)

**Incorrect:**
- `machine/AGENTS.md` → inherits from `canonic/AGENTS.md` (doesn't exist)
- `machine/README.md` → references `FSM_SPECIFICATION.md` (doesn't exist)

**Learning:** Implementation inheritance constraint needs examples showing correct vs incorrect patterns.

**Canonify as:** Add to CANON.md examples section showing reference patterns.

---

## 3. Validation Precedence

### Syntactic Before Semantic
**Insight:** The validator can run syntactic checks without LLM, but semantic checks require expensive LLM tokens.

**Pattern Observed:**
1. Syntactic validation is free (structure checks)
2. Semantic validation is expensive (LLM token cost)
3. System should converge: semantic violations → syntactic constraints
4. This shifts cost from expensive to free over time

**Already Canonified:** This pattern was added to CANON.md as "Validation Convergence" during this session.

---

## 4. Violation Statement Completeness

### Every Constraint Needs Violation
**Discovery:** 20 constraints across machine/ CANONs were missing `**Violation:**` statements.

**Pattern:** Constraints without violation statements cannot be:
- Automatically validated
- Clearly understood by implementers
- Converted to syntactic checks

**Learning:** Violation statements are not optional - they are required for validation convergence.

**Canonical Form:**
```
### [Constraint Name]
**Description of what must be true.**

**Violation:** Specific description of what violation looks like
```

**Impact:** Adding violation statements reduced violations from 23 → 3 (87%).

---

## 5. FSM Tool Requirements

### State Visualization is Critical
**Learning:** Without `fsm_status` tool, users cannot see current FSM state.

**Tools Needed for FSM (discovered during implementation):**
1. **fsm_status** - Show current state, suggest next steps (IMPLEMENTED)
2. **reindex** - Coordinate multi-state changes (IMPLEMENTED)
3. **trace_asset** - Follow traceability chain (IMPLEMENTED)
4. **validate_state** - Check individual state compliance (NEEDED)
5. **transition** - Guide state transitions with validation (NEEDED)

**Pattern:** FSM without visualization tools is opaque to users.

**Canonify as:** Tools CANON should require FSM visualization tooling.

---

## 6. LEDGER Format Flexibility

### Multiple Valid Formats
**Discovery:** Asset ledgers can use different markdown formats:

**Format 1 (Observed in examples/minimal):**
```markdown
## asset-0001
- **Name:** POST /users
- **Type:** endpoint
- **Source:** 001
```

**Format 2 (Expected by initial parser):**
```markdown
**asset-0001**: POST /users
- type: endpoint
- source: 001
```

**Learning:** CANON should specify LEDGER format or validator must handle both.

**Issue:** trace_asset.py parser couldn't handle Format 1 due to `**Field**:` pattern.

**Canonify as:** Add LEDGER format specification to assets/CANON.md template.

---

## 7. Example Progression

### Learning Path Matters
**Pattern Discovered:** Examples should progress:
1. **hello-world** - Single file, single constraint (exact match)
2. **simple-fsm** - Multiple states, validation gates, backflow
3. **canonic-readme** - Document structure, inheritance chains
4. **minimal** (machine) - Complete 4-state FSM

**Learning:** Each example should build on previous concepts.

**Canonify as:** Examples CANON should specify progression order.

---

## 8. Producer/Consumer Ratio

### Maturity Signal
**Pattern:** Git history producer/consumer ratio shows system maturity.

**This Session:**
- Producer commits: 2/12 (17%) - System learned new patterns
- Consumer commits: 7/12 (58%) - Enforced existing constraints
- Implementation: 3/12 (25%) - New tools

**Learning:** Healthy maturing system has decreasing producer ratio over time.

**Canonical Threshold:** 
- New system: >40% producer commits (rapid learning)
- Maturing: 10-30% producer commits (refinement)
- Mature: <10% producer commits (stable enforcement)

**Canonify as:** Add ratio thresholds to CANON.md producer/consumer section.

---

## 9. Self-Validation Loop

### Validators Must Validate Themselves
**Insight:** canonic_validator.py includes self-validation check.

**Pattern:**
```python
# First validate that validator complies with CANON
if not self.validate_self():
    raise ValidationError("Validator violates CANON")

# Then validate target repository
```

**Learning:** Tools that validate CANON must first prove they comply with CANON.

**Canonify as:** Add self-validation requirement to tools/CANON.md.

---

## 10. Atomic Commit Discipline

### One Logical Change Per Commit
**Pattern Used:**
- ✓ "Add violation statements" (one concern: missing violations)
- ✓ "Fix reference integrity" (one concern: broken reference)
- ✓ "Add fsm_status tool" (one concern: new tool)
- ✗ "Fix violations and add tools" (mixed concerns)

**Learning:** Atomic commits enable:
- Clean git history
- Easy revert if needed
- Clear producer vs consumer signal
- Better code review

**Already Canonical:** This is in VOCABULARY.md as "atomic commit".

---

## 11. Introspection Triggers Learning

### Self-Reflection Finds Gaps
**Process This Session:**
1. Ran validator → found 23 violations
2. Fixed violations → reduced to 3
3. Noticed garbage in CANON → validator didn't catch it
4. **Introspection:** Why didn't validator catch it?
5. **Learning:** Need "content after termination" check
6. **Canonify:** Document the learning for next iteration

**Pattern:** Introspection → Learning → Canonification → Stronger System

**Learning:** The act of using the system reveals its gaps.

**Canonify as:** Introspection should be a documented phase in FSM workflow.

---

## 12. Todo List Management

### Track Progress During Complex Tasks
**Usage Pattern:** TodoWrite tool used to:
- Break down 19 recommendations into trackable tasks
- Mark progress as work completed
- Keep user informed of progress
- Demonstrate thoroughness

**Learning:** Complex multi-step tasks benefit from explicit todo tracking.

**Canonical Practice:** Use TodoWrite when task has >3 steps.

---

## Summary

**Total Learnings:** 12 distinct patterns discovered

**Canonified 2026-01-06 session:**
- Learning #3: Validation convergence (CANON.md validation protocol)
- Learning #10: Atomic commits (CANON.md introspective properties)
- Producer/consumer pattern (CANON.md CANON production vs consumption)

**Canonified 2026-01-07 session:**
- Learning #1: File termination check (validate_canonic.py + validator)
- Learning #8: Producer/consumer ratio thresholds (CANON.md maturity thresholds)
- Learning #9: Self-validation requirement (CANON.md validator requirement)
- Learning #11: Introspection requirement (CANON.md introspection cycle) ← **Meta-pattern canonified**

**Still Need Canonification:**
- Learning #2: Reference integrity patterns (examples needed)
- Learning #4: Violation statement completeness (already practice, needs constraint)
- Learning #5: FSM tool requirements (tools CANON needed)
- Learning #6: LEDGER format flexibility (specify format or handle both)
- Learning #7: Example progression order (examples/CANON.md)
- Learning #12: Todo list management (already practice, no constraint needed)

---

**Session Date:** 2026-01-06
**Session Focus:** Examples, validators, FSM tools
**Producer/Consumer Ratio:** 17% producer (healthy for refinement phase)
**Violations Reduced:** 23 → 3 (87%)

---

**Update 2026-01-07:**
**Canonification Progress:** 7/12 learnings now canonified (58%)
**Key Achievement:** Meta-pattern canonified - introspection cycle itself is now enforceable
**Status:** Introspection requirement (Learning #11) makes session learnings interrupt mechanism mandatory

