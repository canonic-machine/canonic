# CANONIC Spec

1. Purpose
   - Define how the paradigm governs the triad and inheritance while keeping the root minimal.

2. Scope
   - Applies to `/canonic` and informs downstream layers (e.g., `/machine`).

3. Constraints
   - Root CANON includes triad, inheritance, coherence, compliance, governance, invalidity, and introspection.
   - VOCAB defines the terms used by CANON and this SPEC, including its own role.
   - README describes the triad and points to `templates/`.
   - `templates/` contains reusable templates for CANON, VOCAB, README, and SPEC.

4. Validation
   - Each governed directory contains the triad.
   - Template files remain generic and reusable.
   - Machine performs mechanical checks and correction (ordering, history-preserving fixes).

5. Consumption notes
   - Downstream layers inherit this spec and may add constraints without contradicting the root CANON.
   - When terms are added here, downstream VOCABs must include them.

This SPEC inherits the root triad and references VOCAB for definitions.
