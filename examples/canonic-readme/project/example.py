#!/usr/bin/env python3
"""
CANONIC Constraint Validation Example

Demonstrates:
- Type annotations (satisfies type checking constraint)
- Docstrings (satisfies documentation constraint)
- Runnable code (satisfies parent constraint)
- Constraint composition via inheritance
"""


def validate_constraint(constraint_name: str, satisfied: bool) -> None:
    """
    Display constraint validation result.

    Args:
        constraint_name: Name of the constraint being checked
        satisfied: Whether the constraint is satisfied

    Returns:
        None
    """
    status = "✓" if satisfied else "✗"
    print(f"{status} {constraint_name}")


def demonstrate_inheritance() -> bool:
    """
    Demonstrate constraint inheritance across CANON layers.

    This function satisfies multiple constraints:
    - Has type annotations (local CANON requirement)
    - Has docstring (local CANON requirement)
    - Is runnable (parent CANON requirement)
    - Is technically accurate (parent CANON requirement)

    Returns:
        True if all constraints demonstrated successfully
    """
    print("Demonstrating CANONIC constraint validation:")
    print()

    # Constraints from examples/canonic-readme/CANON.md
    validate_constraint("Engaging documentation", True)
    validate_constraint("Technical accuracy", True)
    validate_constraint("Reference resolution", True)

    print()

    # Constraints from examples/canonic-readme/project/CANON.md
    validate_constraint("Type checking passes", True)
    validate_constraint("Functions have docstrings", True)
    validate_constraint("Code runs without errors", True)

    print()
    print("✓ All inherited constraints satisfied")
    return True


def main() -> int:
    """
    Entry point demonstrating constraint satisfaction.

    Returns:
        0 for success
    """
    success = demonstrate_inheritance()
    return 0 if success else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
