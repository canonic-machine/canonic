# CANONIC Spec

1. Purpose
   - Define the structure and intent of the CANONIC scope.
   - Specify how SPEC, CANON, VOCAB and README relate.

2. Scope
   - Applies to `/canonic` and informs inherited scopes (`/machine`).

3. Constraints
   - SPEC is first; CANON and VOCAB are co-equal and must cover SPEC terms.
   - VOCAB defines the terms used by CANON, SPEC, and README and defines itself.
   - CANON states paradigm axioms for the scope: triad, inheritance, and introspection.
   - Machine applies this SPEC to inherited scopes and provides templates for CANON, VOCAB, README, and SPEC.
   - CANON and VOCAB define README which describes the scope and points to machine templates.

4. Validation
   - Confirm that SPEC is first and that CANON and VOCAB are co-equal.
   - Verify that VOCAB defines all terms used by CANON, SPEC, and README.
   - Validate that the triad exists and inheritance is declared.
   - Ensure that CANON and VOCAB define README which describes the scope and points to machine templates.

5. Consumption notes
   - Downstream layers inherit these constraints without contradicting the root CANON.
   - Downstream VOCABs must include terms added in this layer

6. Inheritance notes
   - Downstream layers inherit this spec and may add constraints without contradicting the root CANON.
   - When terms are added in this scope, downstream VOCABs must include them.
   

This SPEC is part of the CANONIC triad and references VOCAB for definitions.
