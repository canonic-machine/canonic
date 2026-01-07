# CANON (examples/simple-fsm/)

**Inherits from:** canonic-programming/examples/

## Invariants

### Required artifacts
**Directory must contain:**
- CANON.md
- VOCABULARY.md
- README.md
- draft.txt
- state.txt

**Violation:** Missing any required artifact

### State constraints
**state.txt must:**
- Contain exactly one of: "draft", "review", or "published"
- Contain no additional whitespace or characters
- Use UTF-8 encoding

**Violation:** state.txt contains invalid state value

### State transition constraints
**Transitions must:**
- Start from current state in state.txt
- Follow valid FSM transitions only
- Update state.txt atomically with content changes

**Valid transitions:**
- draft → review (when draft.txt is not empty)
- review → published (when draft.txt passes validation)
- review → draft (on validation failure, backflow)

**Invalid transitions:**
- draft → published (must pass through review)
- published → any state (published is terminal)

**Violation:** Attempted invalid state transition

### Content validation constraints
**Transition draft → review requires:**
- draft.txt is not empty
- draft.txt contains at least 10 characters

**Transition review → published requires:**
- draft.txt starts with capital letter
- draft.txt ends with period
- draft.txt contains no profanity (basic check)

**Violation:** Content fails validation requirements for requested transition

### Example constraints
**Example must:**
- Be understandable in < 5 minutes
- Run without external dependencies
- Demonstrate state transitions, validation gates, and backflow

**Violation:** Example violates simplicity or demonstration requirements

---

End of simple-fsm CANON.
