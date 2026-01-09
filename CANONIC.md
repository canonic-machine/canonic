# CANONIC Spec

1. Purpose
   - Define how the paradigm governs the triad and inheritance while keeping the root minimal.
   - Describe the full paradigm; SPEC is the first artifact and the source for CANON and VOCAB.
   - Humans direct the SPECs; CANONIC machines propagate those specifications to get work done.

2. Scope
   - Applies to `/canonic` and informs downstream layers (e.g., `/machine`).

3. Constraints
   - Root CANON includes triad, inheritance, coherence, compliance, governance, invalidity, and introspection; these axioms are final.
   - VOCAB defines the terms used by CANON and this SPEC, including its own role.
   - SPEC is primary; CANON and VOCAB are co-equal canonical artifacts derived from it and must cover its terminology.
   - Machine layers apply SPEC constraints downstream to produce governed work.
   - README describes the triad and points to machine templates.
   - Machine hosts reusable templates for CANON, VOCAB, README, and SPEC.

4. Validation
   - Each governed directory contains the triad.
   - Template files remain generic and reusable.
   - Machine enforces finality, ordering, and correction (history-preserving fixes).

5. Consumption notes
   - Downstream layers inherit this spec and may add constraints without contradicting the root CANON.
   - When terms are added here, downstream VOCABs must include them.

This SPEC inherits the root triad and references VOCAB for definitions.
