# VOCABULARY (examples/simple-fsm/)

**Simple-FSM-specific term definitions.**

Inherits all terms from canonic-programming/examples/VOCABULARY.md

---

## Simple FSM Terms

### state.txt
File containing current FSM state. Must contain exactly one of: "draft", "review", or "published". Represents the single source of truth for system state.

### draft.txt
Content artifact being governed by the FSM. Starts empty, gets populated during draft state, validated during review state, immutable in published state.

### draft (state)
Initial state. Content can be freely edited. Transition to review requires non-empty content.

### review (state)
Validation state. Content is checked against publication requirements. Successful validation transitions to published. Failed validation backflows to draft.

### published (state)
Terminal state. Content is immutable and compliant. No transitions allowed from this state.

### validation gate
Check performed during state transition. Binary pass/fail. Pass advances to next state. Fail triggers backflow to previous state.

### backflow
Return to previous state when validation fails. Demonstrates rejection mechanism in CANONIC FSMs. Example: review → draft when content validation fails.

### terminal state
State with no outgoing transitions. Represents final, immutable system state. In this FSM: "published" is terminal.

---

End of simple-fsm VOCABULARY.
