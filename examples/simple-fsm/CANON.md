
# CANON (canonic-programming/examples/simple-fsm/)

**Inherits from:** ../CANON.md

## FSM structure

**Three states: draft → review → published**

**State definitions:**
- draft: Content exists in draft.txt, may be incomplete
- review: Content in review.txt, must be complete and properly formatted
- published: Content in published.txt, must satisfy all quality gates

## Transition constraints

### draft → review

**Content requirements:**
- Must contain at least one complete sentence
- Must start with capital letter
- Must end with period

**Violation:** Content incomplete, no capitalization, or missing period

### review → published

**Content requirements:**
- Must satisfy all draft → review constraints
- Must contain no spelling errors (basic check)
- Line count must be ≥ 3

**Violation:** Failed draft constraints, spelling errors detected, or insufficient content

### Backflow on failure

**Invalid transitions return to source state.**

**Pattern:**
- Attempt review → published
- Validation fails
- Content returns to review.txt
- Fix violations before retry

**Violation:** Failed validation proceeds to next state instead of backflow
