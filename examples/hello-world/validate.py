#!/usr/bin/env python3
"""
Hello World Validator

Demonstrates syntactic validation: exact match check.
This is the simplest possible CANONIC validator.
"""

import os
import sys

def validate():
    """Validate hello.txt against CANON constraints."""

    print("Validating hello-world example...")
    print()

    violations = []

    # Check 1: File exists
    if not os.path.exists('hello.txt'):
        violations.append("✗ hello.txt does not exist")
    else:
        print("✓ hello.txt exists")

        # Check 2: Content matches exactly
        with open('hello.txt', 'r', encoding='utf-8') as f:
            content = f.read()

        expected = "Hello, world."

        if content == expected:
            print("✓ Content matches exactly")
        else:
            violations.append(f"✗ Content mismatch")
            violations.append(f"  Expected: {repr(expected)}")
            violations.append(f"  Got:      {repr(content)}")

    print()

    # Report results
    if violations:
        print("Validation: FAIL")
        print()
        print("Violations:")
        for v in violations:
            print(v)
        return 1
    else:
        print("Validation: PASS")
        return 0

if __name__ == '__main__':
    exit_code = validate()
    sys.exit(exit_code)
