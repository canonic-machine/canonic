#!/usr/bin/env python3
"""
CANONIC Self-Validator

Syntactic validation for canonic/ repository governance structure.
Checks triad presence, file naming, and reference integrity.

This validator demonstrates CANONIC programming principles by:
- Validating structure (syntactic), not semantics
- Binary pass/fail with no subjective judgment
- Self-validating the governance repository itself
"""

import os
import re
import sys
from pathlib import Path

class CanonicValidator:
    def __init__(self, root_path='.'):
        self.root = Path(root_path).resolve()
        self.violations = []
        self.checks_passed = 0

    def check(self, condition, message, violation_message=None):
        """Binary validation check."""
        if condition:
            self.checks_passed += 1
            print(f"✓ {message}")
            return True
        else:
            violation = violation_message or message
            self.violations.append(f"✗ {violation}")
            return False

    def validate_triad(self, directory):
        """Check if directory contains required triad files."""
        canon = directory / 'CANON.md'
        vocab = directory / 'VOCABULARY.md'
        readme = directory / 'README.md'

        dir_rel = directory.relative_to(self.root)

        self.check(
            canon.exists(),
            f"Triad: {dir_rel}/CANON.md exists",
            f"Triad violation: {dir_rel}/CANON.md missing"
        )
        self.check(
            vocab.exists(),
            f"Triad: {dir_rel}/VOCABULARY.md exists",
            f"Triad violation: {dir_rel}/VOCABULARY.md missing"
        )
        self.check(
            readme.exists(),
            f"Triad: {dir_rel}/README.md exists",
            f"Triad violation: {dir_rel}/README.md missing"
        )

    def validate_file_naming(self):
        """Check file naming conventions."""
        # Governance files should use UPPERCASE base names
        for md_file in self.root.rglob('*.md'):
            rel_path = md_file.relative_to(self.root)

            # Skip git and hidden directories
            if any(part.startswith('.') for part in rel_path.parts):
                continue

            base_name = md_file.stem

            # Core governance files must be UPPERCASE
            if base_name in ['CANON', 'VOCABULARY', 'README', 'CANONIC']:
                self.check(
                    base_name.isupper(),
                    f"Naming: {rel_path} uses uppercase base name",
                    f"Naming violation: {rel_path} should use uppercase base name"
                )

    def validate_reference_integrity(self):
        """Check that markdown links resolve to existing files."""
        # Pattern for markdown links: [text](path)
        link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

        for md_file in self.root.rglob('*.md'):
            # Skip git and hidden directories
            rel_path = md_file.relative_to(self.root)
            if any(part.startswith('.') for part in rel_path.parts):
                continue

            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            for match in link_pattern.finditer(content):
                link_text = match.group(1)
                link_path = match.group(2)

                # Skip external links (http, https, mailto, etc.)
                if link_path.startswith(('http://', 'https://', 'mailto:', '#')):
                    continue

                # Resolve relative link
                target = md_file.parent / link_path

                # Remove anchor if present
                if '#' in str(target):
                    target = Path(str(target).split('#')[0])

                # Check if target exists
                if not target.exists():
                    self.violations.append(
                        f"✗ Reference integrity: {rel_path} links to non-existent {link_path}"
                    )
                else:
                    self.checks_passed += 1

    def validate_repository_specification(self):
        """Check that CANONIC.md exists as repository specification."""
        canonic_file = self.root / 'CANONIC.md'

        self.check(
            canonic_file.exists(),
            "Repository specification: CANONIC.md exists",
            "Repository specification missing: CANONIC.md required"
        )

    def validate_file_termination(self):
        """Check that CANON.md and VOCABULARY.md files terminate cleanly."""
        # Pattern: "End of [name] CANON." or "End of [name] VOCABULARY."
        termination_patterns = [
            (r'End of .+ CANON\.', 'CANON'),
            (r'End of .+ VOCABULARY\.', 'VOCABULARY'),
        ]

        for md_file in self.root.rglob('*.md'):
            rel_path = md_file.relative_to(self.root)

            # Skip hidden directories
            if any(part.startswith('.') for part in rel_path.parts):
                continue

            # Only check CANON.md and VOCABULARY.md files
            if md_file.name not in ['CANON.md', 'VOCABULARY.md']:
                continue

            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Find which pattern applies
            for pattern, file_type in termination_patterns:
                if md_file.name == f'{file_type}.md':
                    match = re.search(pattern, content)
                    if match:
                        # Check if there's content after the termination marker
                        end_pos = match.end()
                        after_marker = content[end_pos:].strip()

                        if after_marker:
                            self.violations.append(
                                f"✗ File termination: {rel_path} has content after termination marker"
                            )
                        else:
                            self.checks_passed += 1
                            # Don't print individual passes for termination to reduce noise
                    break

    def validate_governance_purity(self):
        """Check that no executable code exists (pure governance)."""
        # Allow .py files (validation tools per examples)
        # But check they're in examples or root validation

        for py_file in self.root.rglob('*.py'):
            rel_path = py_file.relative_to(self.root)

            # Skip hidden directories
            if any(part.startswith('.') for part in rel_path.parts):
                continue

            # Allowed: validation scripts in examples and root validator
            allowed_locations = [
                'validate_canonic.py',
                'examples/hello-world/validate.py',
                'examples/simple-fsm/transition.py'
            ]

            if str(rel_path) in allowed_locations or 'examples' in rel_path.parts:
                self.checks_passed += 1
            else:
                self.violations.append(
                    f"✗ Governance purity: {rel_path} is executable code in pure governance repository"
                )

    def run(self):
        """Run all validations."""
        print("Validating canonic/ repository governance structure...")
        print()

        print("=== Repository Specification ===")
        self.validate_repository_specification()
        print()

        print("=== Triad Requirements ===")
        # Root triad
        self.validate_triad(self.root)

        # Examples triad
        examples_dir = self.root / 'examples'
        if examples_dir.exists():
            self.validate_triad(examples_dir)

            # Example subdirectories
            for example_dir in examples_dir.iterdir():
                if example_dir.is_dir() and not example_dir.name.startswith('.'):
                    self.validate_triad(example_dir)

        print()

        print("=== File Naming Conventions ===")
        self.validate_file_naming()
        print()

        print("=== Reference Integrity ===")
        self.validate_reference_integrity()
        print()

        print("=== File Termination ===")
        self.validate_file_termination()
        print()

        print("=== Governance Purity ===")
        self.validate_governance_purity()
        print()

        # Report
        print("=" * 50)
        print(f"Checks passed: {self.checks_passed}")
        print(f"Violations found: {len(self.violations)}")
        print()

        if self.violations:
            print("VALIDATION: FAIL")
            print()
            print("Violations:")
            for v in self.violations:
                print(v)
            return 1
        else:
            print("VALIDATION: PASS")
            print()
            print("Repository governance structure is compliant.")
            return 0

def main():
    # Detect if we're in canonic/ root
    if not Path('CANONIC.md').exists():
        print("Error: This validator must be run from canonic/ repository root")
        print("(Directory containing CANONIC.md)")
        sys.exit(1)

    validator = CanonicValidator()
    exit_code = validator.run()
    sys.exit(exit_code)

if __name__ == '__main__':
    main()
