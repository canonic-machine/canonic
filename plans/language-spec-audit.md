# LANGUAGE Specification Audit: Closure Definitions

**Date:** 2026-01-21  
**Auditor:** Architect Mode  
**Scope:** Closure semantics in LANGUAGE.md  
**Focus:** ROADMAP vs COVERAGE definitions

---

## Executive Summary

**CRITICAL FINDING:** The LANGUAGE specification contains **INVERTED** closure definitions that contradict the actual usage in ROADMAP.md and COVERAGE.md.

**Actual Usage:**
- **ROADMAP.md** = External closure (outward-facing, public commitments, strategic roadmap)
- **COVERAGE.md** = Internal closure (inward-facing, implementation tracking, gap analysis)

**Current LANGUAGE Spec (INCORRECT):**
- Defines COVERAGE as "ExternalClosure"
- Defines ROADMAP as part of internal tracking
- Contradicts actual file semantics and usage

---

## 1. Current State Analysis

### 1.1 LANGUAGE.md Closure Definitions

#### Line 31: Self-Closure Statement
```
Rule: LANGUAGE_SELF_CLOSURE
LANGUAGE closes itself internally via COVERAGE and externally via ROADMAP.
```

**Analysis:** This statement is **AMBIGUOUS** but suggests:
- COVERAGE = internal closure ✓ (correct)
- ROADMAP = external closure ✓ (correct)

**Status:** ✓ CORRECT (but needs clarification)

---

#### Lines 943-944: Primitive Roles
```
Role(COVERAGE) = ExternalClosure — tracks external completeness (gaps + roadmap)
```

**Analysis:** This is **INCORRECT**. The definition states:
- COVERAGE = ExternalClosure ✗ (wrong)
- "tracks external completeness" ✗ (wrong)

**Actual COVERAGE.md Usage:**
- Tracks **internal** axiom coverage
- Maps axioms → validators/implementations
- Identifies **internal** gaps
- Proves **internal** completeness

**Status:** ✗ INCORRECT - INVERTED DEFINITION

---

#### Lines 1012-1029: COVERAGE Semantics
```
Rule: COVERAGE_STRUCTURE
COVERAGE.md MUST track internal completeness.

COVERAGE ::= InternalClosure

Structure(COVERAGE) = {
  - Internal axiom coverage matrix
  - Gap analysis (what's not covered internally)
  - Closure proof (when internal gaps = ∅)
}
```

**Analysis:** This is **CORRECT**. Clearly states:
- COVERAGE = InternalClosure ✓
- Tracks internal axiom coverage ✓
- Internal gap analysis ✓

**Status:** ✓ CORRECT

---

#### Lines 1031-1049: ROADMAP Semantics
```
Rule: ROADMAP_STRUCTURE
ROADMAP.md MUST track external integration and roadmap to dominance.

ROADMAP ::= ExternalClosure

Structure(ROADMAP) = {
  - External reference survey
  - Integration roadmap with version targets
  - Competitive analysis
  - External validation metrics
  - Risks and mitigation
}
```

**Analysis:** This is **CORRECT**. Clearly states:
- ROADMAP = ExternalClosure ✓
- Tracks external integration ✓
- External reference survey ✓

**Status:** ✓ CORRECT

---

#### Lines 1052-1069: Closure Types
```
Rule: CLOSURE_TYPES
CANONIC distinguishes internal and external closure.

InternalClosure  = COVERAGE satisfaction (all internal requirements covered)
ExternalClosure  = ROADMAP satisfaction (external integration complete)
CompleteClosure  = InternalClosure ∧ ExternalClosure

Rule: ROADMAP_EXTERNAL_CLOSURE
ROADMAP.md defines external closure for a scope.

ExternalClosure(scope) = HasROADMAP(scope) ∧ Gaps(ROADMAP(scope)) = ∅
```

**Analysis:** This is **CORRECT**. Clearly states:
- InternalClosure = COVERAGE ✓
- ExternalClosure = ROADMAP ✓

**Status:** ✓ CORRECT

---

### 1.2 Actual File Usage Analysis

#### ROADMAP.md Analysis
```markdown
# CANONIC ROADMAP

## 1. Vision
3 repos. Clean layers. Independent. Interoperable.

## 2. Multi-Repo Stack
canonic-domains/     (inherits: canonic-services/)
    ↑ instantiates
canonic-services/    (inherits: canonic/)
    ↑ implements
canonic/             (OS: 5 axioms)

## 7. Success Criteria
- [x] 3 repos created
- [x] Inheritance chain complete
- [x] All scopes have triad + closure
- [x] All axioms provable
- [x] All services composable
- [x] All domains instantiable

**Status:** CLOSED
```

**Characteristics:**
- **External-facing:** Public commitments and strategic vision
- **Outward-looking:** Multi-repo architecture, layer composition
- **Integration-focused:** How components work together
- **Success criteria:** External milestones and deliverables
- **Closure statement:** "This roadmap closes CANONIC"

**Semantic Role:** External closure (strategic roadmap to completion)

---

#### COVERAGE.md Analysis
```markdown
# COVERAGE (/canonic/)

**Purpose:** Track CANONIC root governance coverage against external standards and close gaps.

## 1. External Survey
| Standard | Spec | Authority |
| RFC 2119 | https://www.rfc-editor.org/rfc/rfc2119 | rfc-editor.org |

## 2. RFC 2119 Comparison
| Feature | RFC 2119 | CANONIC | Gap | Roadmap |

## 4. Coverage Matrix
| Feature | RFC 2119 | CANONIC |
| Normative language | Yes | Yes |
| Governance model | No | Yes |

## 6. Conclusion
CANONIC root coverage is closed for the current scope.
```

**Characteristics:**
- **Internal-facing:** Implementation tracking and gap analysis
- **Inward-looking:** What's covered vs. what's missing internally
- **Comparison-focused:** CANONIC features vs. external standards
- **Coverage matrix:** Internal feature completeness
- **Gap tracking:** What needs to be implemented

**Semantic Role:** Internal closure (implementation completeness)

**CRITICAL NOTE:** The "External Survey" section is **MISLEADING**. It surveys external standards for **comparison purposes** to track **internal** coverage gaps, NOT to track external integration. This is internal closure work.

---

## 2. Identified Issues

### Issue 1: Inverted Definition at Line 943
**Location:** [`LANGUAGE.md:943`](../language/LANGUAGE.md:943)

**Current (INCORRECT):**
```
Role(COVERAGE) = ExternalClosure — tracks external completeness (gaps + roadmap)
```

**Problem:**
- Defines COVERAGE as "ExternalClosure" (wrong)
- States it "tracks external completeness" (wrong)
- Contradicts Rule: COVERAGE_STRUCTURE at line 1012
- Contradicts actual COVERAGE.md usage

**Impact:** HIGH - Creates fundamental semantic confusion

---

### Issue 2: Ambiguous Self-Closure Statement
**Location:** [`LANGUAGE.md:31`](../language/LANGUAGE.md:31)

**Current:**
```
Rule: LANGUAGE_SELF_CLOSURE
LANGUAGE closes itself internally via COVERAGE and externally via ROADMAP.
```

**Problem:**
- Statement is correct but lacks clarity
- Could be misinterpreted without context
- Needs explicit semantic definitions

**Impact:** MEDIUM - Ambiguity could lead to misinterpretation

---

### Issue 3: Inconsistent Terminology
**Location:** Multiple sections

**Problem:**
- Line 943: "ExternalClosure" for COVERAGE
- Line 1017: "InternalClosure" for COVERAGE
- Line 1035: "ExternalClosure" for ROADMAP
- Inconsistent use of same term for different artifacts

**Impact:** HIGH - Creates logical contradiction

---

### Issue 4: COVERAGE "External Survey" Naming Confusion
**Location:** COVERAGE.md structure

**Problem:**
- Section titled "External Survey" suggests external closure
- Actually tracks internal coverage against external standards
- Naming creates semantic confusion about closure type

**Impact:** MEDIUM - Misleading section naming

---

## 3. Root Cause Analysis

### Primary Cause
**Copy-paste error or conceptual inversion** at line 943 where COVERAGE was incorrectly labeled as "ExternalClosure" instead of "InternalClosure".

### Contributing Factors
1. **Semantic drift:** Early draft may have had different closure semantics
2. **Incomplete refactoring:** Later sections (1012-1069) were corrected but line 943 was missed
3. **Lack of cross-validation:** No systematic check between primitive roles and detailed semantics

### Evidence
- Lines 1012-1069 are internally consistent and correct
- Line 943 is an outlier that contradicts later definitions
- Actual file usage (ROADMAP.md, COVERAGE.md) aligns with lines 1012-1069, NOT line 943

---

## 4. Required Corrections

### Correction 1: Fix Line 943 (CRITICAL)
**Location:** [`LANGUAGE.md:943`](../language/LANGUAGE.md:943)

**Current:**
```
Role(COVERAGE) = ExternalClosure — tracks external completeness (gaps + roadmap)
```

**Corrected:**
```
Role(COVERAGE) = InternalClosure — tracks internal completeness (axiom coverage + gaps)
```

**Rationale:**
- Aligns with Rule: COVERAGE_STRUCTURE (line 1012)
- Matches actual COVERAGE.md usage
- Removes logical contradiction

---

### Correction 2: Add ROADMAP to Primitive Roles
**Location:** [`LANGUAGE.md:943-944`](../language/LANGUAGE.md:943)

**Current:**
```
Role(CANON)    = Governance    — declares normative rules (axioms)
Role(VOCAB)    = Semantics     — defines vocabulary (terms)
Role(README)   = Description   — provides documentation (prose)
Role(COVERAGE) = ExternalClosure — tracks external completeness (gaps + roadmap)
```

**Corrected:**
```
Role(CANON)    = Governance       — declares normative rules (axioms)
Role(VOCAB)    = Semantics        — defines vocabulary (terms)
Role(README)   = Description      — provides documentation (prose)
Role(COVERAGE) = InternalClosure  — tracks internal completeness (axiom coverage + gaps)
Role(ROADMAP)  = ExternalClosure  — tracks external integration (roadmap + milestones)
```

**Rationale:**
- ROADMAP is a narrative artifact with defined role
- Should be listed alongside COVERAGE for symmetry
- Makes closure distinction explicit

---

### Correction 3: Clarify LANGUAGE_SELF_CLOSURE
**Location:** [`LANGUAGE.md:31`](../language/LANGUAGE.md:31)

**Current:**
```
Rule: LANGUAGE_SELF_CLOSURE
LANGUAGE closes itself internally via COVERAGE and externally via ROADMAP.
```

**Enhanced:**
```
Rule: LANGUAGE_SELF_CLOSURE
LANGUAGE achieves complete closure through two orthogonal mechanisms:
- Internal closure via COVERAGE (axiom coverage, implementation tracking)
- External closure via ROADMAP (strategic milestones, integration targets)

InternalClosure(LANGUAGE) = COVERAGE satisfaction
ExternalClosure(LANGUAGE) = ROADMAP satisfaction
CompleteClosure(LANGUAGE) = InternalClosure ∧ ExternalClosure
```

**Rationale:**
- Makes closure types explicit
- Provides formal definitions
- Removes ambiguity

---

### Correction 4: Add Closure Distinction Section
**Location:** New section after line 1069

**Addition:**
```markdown
#### 4.6.9 Closure Distinction

Rule: CLOSURE_ORTHOGONALITY
Internal and external closure are orthogonal dimensions.

InternalClosure:
  - Artifact: COVERAGE.md
  - Focus: Implementation completeness
  - Question: "Are all axioms covered by validators?"
  - Metrics: Axiom coverage %, gap count
  - Audience: Internal (developers, maintainers)

ExternalClosure:
  - Artifact: ROADMAP.md
  - Focus: Strategic completeness
  - Question: "Are all external milestones achieved?"
  - Metrics: Milestone completion %, integration status
  - Audience: External (users, stakeholders)

Rule: COVERAGE_INTERNAL_FOCUS
COVERAGE.md tracks internal implementation against internal requirements.
External standards may be surveyed for comparison, but the closure
tracked is internal (what we've implemented vs. what we need to implement).

Rule: ROADMAP_EXTERNAL_FOCUS
ROADMAP.md tracks external integration and strategic positioning.
It defines public commitments and outward-facing milestones.

Rule: CLOSURE_INDEPENDENCE
A scope may achieve internal closure without external closure, and vice versa.
Complete closure requires both.

Examples:
  - Internal closed, external open: All axioms validated, but roadmap incomplete
  - External closed, internal open: All milestones met, but gaps in coverage
  - Complete closure: Both COVERAGE and ROADMAP gaps = ∅
```

**Rationale:**
- Provides clear semantic distinction
- Addresses confusion about "external survey" in COVERAGE
- Establishes orthogonality principle

---

## 5. Verification Checklist

After corrections, verify:

- [ ] Line 943 defines COVERAGE as InternalClosure
- [ ] Line 943 includes ROADMAP as ExternalClosure
- [ ] Line 31 explicitly defines closure types
- [ ] New section 4.6.9 clarifies distinction
- [ ] No contradictions between sections
- [ ] Terminology is consistent throughout
- [ ] Actual file usage (ROADMAP.md, COVERAGE.md) aligns with spec
- [ ] Closure types are orthogonal and independent

---

## 6. Recommendations

### Immediate Actions (Required)
1. **Apply Correction 1** (line 943) - CRITICAL
2. **Apply Correction 2** (add ROADMAP to primitive roles)
3. **Apply Correction 3** (clarify LANGUAGE_SELF_CLOSURE)
4. **Apply Correction 4** (add closure distinction section)

### Follow-up Actions (Recommended)
1. **Rename COVERAGE sections:** Consider renaming "External Survey" to "Reference Survey" or "Comparative Analysis" to avoid confusion
2. **Add examples:** Include concrete examples of internal vs. external closure in different scopes
3. **Cross-reference validation:** Add validator to check consistency between primitive roles and detailed semantics
4. **Documentation:** Update any external documentation that references closure semantics

### Long-term Improvements
1. **Formal verification:** Develop automated checks for semantic consistency
2. **Template updates:** Ensure COVERAGE and ROADMAP templates reflect correct semantics
3. **Training materials:** Create clear guidance on when to use COVERAGE vs. ROADMAP

---

## 7. Impact Assessment

### Severity: HIGH
- Fundamental semantic inversion in core specification
- Affects understanding of closure mechanics
- Could lead to incorrect implementation

### Scope: LANGUAGE specification only
- Issue is confined to LANGUAGE.md documentation
- Actual ROADMAP.md and COVERAGE.md usage is correct
- No code changes required

### Urgency: HIGH
- Should be corrected before v0.1.0 freeze
- Prevents propagation of incorrect semantics
- Ensures specification accuracy

---

## 8. Conclusion

The LANGUAGE specification contains a **critical inversion** at line 943 where COVERAGE is incorrectly defined as "ExternalClosure" when it should be "InternalClosure". This contradicts:

1. The detailed COVERAGE_STRUCTURE rule (line 1012)
2. The CLOSURE_TYPES definitions (line 1052)
3. The actual usage in COVERAGE.md
4. The actual usage in ROADMAP.md

**The correct semantics are:**
- **COVERAGE = InternalClosure** (implementation tracking, axiom coverage, internal gaps)
- **ROADMAP = ExternalClosure** (strategic milestones, external integration, public commitments)

**Four corrections are required** to align the specification with actual usage and remove logical contradictions. All corrections are straightforward and localized to the LANGUAGE.md file.

**Recommendation:** Apply all four corrections before freezing LANGUAGE v0.1.0 to ensure semantic accuracy and prevent confusion.

---

**Audit Status:** COMPLETE  
**Findings:** 4 issues identified  
**Corrections Required:** 4  
**Priority:** HIGH  
**Next Step:** Apply corrections to LANGUAGE.md
