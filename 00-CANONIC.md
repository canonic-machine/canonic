# CANONIC

1. Purpose
   - Define the structure and intent of the CANONIC scope.

2. Scope
   - Applies to `/canonic` and informs inherited scopes (`/machine`).

3. Constraints
   - SPEC is human first and may define machine architecture without implementing it.
   - SPEC states how CANON, VOCAB, and README relate.
   - CANON states enforceable axioms for the scope: triad, inheritance, and introspection.
   - VOCAB is CANON-closed and defines the concepts referenced by CANON and itself.
   - VOCAB is concept-only: each concept is defined once; no duplicate entries for grammatical variation.
   - CANON -> VOCAB -> README: README uses concepts defined by VOCAB.
   - Generation method: derive CANON as minimal axioms from this SPEC; derive VOCAB from CANON and its concept set (CANON-closed); ensure README uses VOCAB concepts.
   - Fixed point: applying the generation method to this SPEC yields a triad that does not change on regeneration.
   - This SPEC defines constraints; machine applies them and provides templates for CANON, VOCAB, and README.

4. Validation
   - Confirm that SPEC is human first and may define machine architecture without implementing it.
   - Verify that SPEC states how CANON, VOCAB, and README relate.
   - Verify that CANON states enforceable axioms for triad, inheritance, and introspection.
   - Verify that VOCAB is CANON-closed and README uses VOCAB concepts.
   - Verify that VOCAB is concept-only with no duplicate entries for grammatical variation.
   - Verify that CANON and VOCAB can be regenerated from this SPEC using the generation method.
   - Verify that regeneration is a fixed point (no changes after regeneration).
   - Confirm that this SPEC defines constraints and that machine applies them with templates.

5. Consumption notes
   - Downstream layers inherit these constraints without contradicting the root CANON.
   - When concepts are added to CANON in this scope, downstream VOCABs must include them.

6. Inheritance notes
   - Downstream layers inherit this spec and may add constraints without contradicting the root CANON.

This SPEC is part of the CANONIC triad.
