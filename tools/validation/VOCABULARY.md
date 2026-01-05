# VOCABULARY (tools/validation/)

Inherits: root → tools → tools/validation

---

## Terms

**validation tool**
A tool that automates the compliance checks described by CANONs. It reads CANON content, applies the invariants, and signals whether the system is compliant.

**compliance report**
The structured output a validation tool produces to show which invariants passed, which failed, and any guidance for remediation.

**violation detail**
An entry inside a compliance report that points to the artifact, line, and CANON requirement that failed.

**run**
A single invocation of the validation tool that produces a compliance report. Each run may result in `compliant` or `invalid`.

