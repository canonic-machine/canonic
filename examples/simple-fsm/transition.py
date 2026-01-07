#!/usr/bin/env python3
"""
Simple FSM Transition Tool

Demonstrates state transitions with validation gates and backflow.
"""

import sys
import os

# FSM Definition
VALID_STATES = {'draft', 'review', 'published'}

TRANSITIONS = {
    'draft': {'review'},
    'review': {'published', 'draft'},  # draft is backflow
    'published': set()  # terminal state
}

def read_state():
    """Read current state from state.txt."""
    if not os.path.exists('state.txt'):
        print("Error: state.txt not found")
        sys.exit(1)

    with open('state.txt', 'r') as f:
        state = f.read().strip()

    if state not in VALID_STATES:
        print(f"Error: Invalid state '{state}' in state.txt")
        sys.exit(1)

    return state

def write_state(state):
    """Write new state to state.txt."""
    with open('state.txt', 'w') as f:
        f.write(state)

def read_content():
    """Read draft.txt content."""
    if not os.path.exists('draft.txt'):
        return ""

    with open('draft.txt', 'r') as f:
        return f.read()

def validate_draft_to_review(content):
    """Validate transition from draft to review."""
    violations = []

    if not content:
        violations.append("✗ draft.txt is empty")
    else:
        print("✓ draft.txt is not empty")

    if len(content) < 10:
        violations.append(f"✗ Content too short (need >= 10 characters, got {len(content)})")
    else:
        print(f"✓ Content length >= 10 characters")

    return violations

def validate_review_to_published(content):
    """Validate transition from review to published."""
    violations = []

    if not content:
        violations.append("✗ draft.txt is empty")
        return violations

    # Check capitalization
    if not content[0].isupper():
        violations.append("✗ Content must start with capital letter")
    else:
        print("✓ Content starts with capital letter")

    # Check period
    if not content.rstrip().endswith('.'):
        violations.append("✗ Content must end with period")
    else:
        print("✓ Content ends with period")

    # Basic profanity check (simple demonstration)
    profanity_words = {'damn', 'hell', 'crap'}
    content_lower = content.lower()
    found_profanity = [word for word in profanity_words if word in content_lower]

    if found_profanity:
        violations.append(f"✗ Profanity detected: {', '.join(found_profanity)}")
    else:
        print("✓ No profanity detected")

    return violations

def transition(current_state, target_state):
    """Attempt state transition."""

    print(f"Current state: {current_state}")
    print(f"Validating transition: {current_state} → {target_state}")
    print()

    # Check if transition is valid
    if target_state not in TRANSITIONS[current_state]:
        if current_state == 'published':
            print(f"Error: No transitions allowed from terminal state '{current_state}'")
        else:
            print(f"Error: Invalid transition {current_state} → {target_state}")
            print(f"Valid transitions from {current_state}: {', '.join(TRANSITIONS[current_state])}")
        return False

    # Read content
    content = read_content()

    # Validate based on transition
    violations = []

    if current_state == 'draft' and target_state == 'review':
        violations = validate_draft_to_review(content)
    elif current_state == 'review' and target_state == 'published':
        violations = validate_review_to_published(content)
    elif current_state == 'review' and target_state == 'draft':
        # Backflow - no validation needed
        print("Backflow: Returning to draft state")

    # Report results
    print()

    if violations:
        print("Validation: FAIL")
        print()
        print("Violations:")
        for v in violations:
            print(v)
        print()

        # Backflow if failed from review
        if current_state == 'review':
            print("Backflow triggered: review → draft")
            write_state('draft')
            print("Fix violations and retry.")
        else:
            print(f"Transition blocked. Violations must be fixed.")
            print(f"State remains: {current_state}")

        return False
    else:
        print("Validation: PASS")
        print(f"Transition successful: {current_state} → {target_state}")
        write_state(target_state)
        return True

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 transition.py <target_state>")
        print(f"Valid states: {', '.join(VALID_STATES)}")
        sys.exit(1)

    target_state = sys.argv[1]

    if target_state not in VALID_STATES:
        print(f"Error: Invalid target state '{target_state}'")
        print(f"Valid states: {', '.join(VALID_STATES)}")
        sys.exit(1)

    current_state = read_state()

    if current_state == target_state:
        print(f"Already in state: {current_state}")
        sys.exit(0)

    success = transition(current_state, target_state)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
