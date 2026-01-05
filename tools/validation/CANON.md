# CANON (tools/validation/)

Inherits: root → tools → tools/validation

---

## Purpose

This tool codifies the validation automation that ensures the entire writing machine remains compliant. It translates the CANON constraints into a repeatable check that reports compliance or violation details.

## Invariants

- The validation tool must inspect the triad (CANON, VOCABULARY, README) for every directory involved in the run.
- The tool reports whether the root invariants (triad existence, vocabulary completeness, governance inheritance) pass or fail.
- Any violation reported must reference the CANON that required the constraint.
- The tool documents how its output should be interpreted by humans and agents.

## Validation

The tool is valid when:

- Its README explains how to run it (even if the automation lives elsewhere) and how to interpret the results.
- Its CANON enumerates the invariant checks performed, along with their pass/fail signals.
- All terminology used is defined in `tools/validation/VOCABULARY.md`.

