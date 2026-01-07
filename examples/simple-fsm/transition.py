#!/usr/bin/env python3
"""
Simple FSM Transition Validator

Demonstrates CANONIC FSM pattern:
- State transitions with validation gates
- Backflow on validation failure
- Clear constraint checking
"""

import sys
from pathlib import Path
from typing import Tuple


def validate_draft_to_review(content: str) -> Tuple[bool, str]:
    """
    Validate draft → review transition.

    Constraints:
    - Must contain at least one complete sentence
    - Must start with capital letter
    - Must end with period

    Args:
        content: Content to validate

    Returns:
        (valid, error_message) tuple
    """
    if not content:
        return False, "Content is empty"

    if not content[0].isupper():
        return False, "Must start with capital letter"

    if not content.rstrip().endswith('.'):
        return False, "Must end with period"

    return True, ""


def validate_review_to_published(content: str) -> Tuple[bool, str]:
    """
    Validate review → published transition.

    Constraints:
    - Must satisfy draft → review constraints
    - Must contain no obvious spelling errors (simplified)
    - Line count must be ≥ 3

    Args:
        content: Content to validate

    Returns:
        (valid, error_message) tuple
    """
    # First check draft → review constraints
    valid, error = validate_draft_to_review(content)
    if not valid:
        return False, f"Failed draft constraint: {error}"

    # Check line count
    lines = [line for line in content.strip().split('\n') if line.strip()]
    if len(lines) < 3:
        return False, f"Must have at least 3 lines (got {len(lines)})"

    # Simplified spelling check: ensure common words
    # In real implementation, use proper spell checker
    words = content.lower().split()
    suspicious = [w for w in words if len(w) > 15]  # Very long words might be typos
    if suspicious:
        return False, f"Suspicious words detected: {suspicious}"

    return True, ""


def transition(from_state: str, to_state: str) -> bool:
    """
    Attempt state transition with validation.

    Args:
        from_state: Source state name (draft/review)
        to_state: Target state name (review/published)

    Returns:
        True if transition succeeded, False otherwise
    """
    source_file = Path(f"{from_state}.txt")
    target_file = Path(f"{to_state}.txt")

    # Check source file exists
    if not source_file.exists():
        print(f"✗ Transition failed: {source_file} does not exist")
        return False

    # Read content
    content = source_file.read_text()

    # Validate based on transition type
    if from_state == "draft" and to_state == "review":
        valid, error = validate_draft_to_review(content)
    elif from_state == "review" and to_state == "published":
        valid, error = validate_review_to_published(content)
    else:
        print(f"✗ Invalid transition: {from_state} → {to_state}")
        return False

    # Check validation result
    if not valid:
        print(f"✗ Validation failed: {error}")
        print(f"  Content remains in {from_state}.txt (backflow)")
        return False

    # Validation passed - perform transition
    target_file.write_text(content)
    source_file.unlink()  # Remove source file

    print(f"✓ Transition succeeded: {from_state} → {to_state}")
    print(f"  Content moved to {target_file}")
    return True


def main() -> int:
    """
    Run state transition from command line.

    Usage: python transition.py <from_state> <to_state>

    Returns:
        0 if valid, 1 if invalid
    """
    if len(sys.argv) != 3:
        print("Usage: python transition.py <from_state> <to_state>")
        print("Valid transitions:")
        print("  draft → review")
        print("  review → published")
        return 1

    from_state = sys.argv[1]
    to_state = sys.argv[2]

    success = transition(from_state, to_state)
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
