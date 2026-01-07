#!/usr/bin/env python3
"""
Hello World Validator

Demonstrates minimal CANONIC validation:
- Single file check
- Exact content match
- Binary pass/fail outcome
"""

import sys
from pathlib import Path


def validate_hello() -> bool:
    """
    Validate hello.txt against CANON constraints.

    Returns:
        True if valid, False otherwise
    """
    hello_file = Path("hello.txt")

    # Constraint: File must exist
    if not hello_file.exists():
        print("✗ Validation failed: hello.txt does not exist")
        return False

    # Constraint: Content must match exactly
    content = hello_file.read_text()
    expected = "Hello, world."

    if content != expected:
        print(f"✗ Validation failed: Content must be exactly \"{expected}\"")
        print(f"  Got: \"{content}\"")
        return False

    # All constraints satisfied
    print("✓ hello.txt validates successfully")
    return True


def main() -> int:
    """
    Run validation and return exit code.

    Returns:
        0 if valid, 1 if invalid
    """
    valid = validate_hello()
    return 0 if valid else 1


if __name__ == "__main__":
    sys.exit(main())
