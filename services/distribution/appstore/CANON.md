# APPSTORE (/services/distribution/appstore/)

inherits: /services/distribution/

---

## Axioms

### 1. Packaged

APPSTORE distributes only VaaS-validated packages.

---

### 2. Versioned

Each release **MUST** be freeze-tagged and immutable.

---

### 3. Public

APPSTORE is the public interface to SERVICES.

---

### 4. State declared

Each product **MUST** declare its state dimensions: LOCALITY, VISIBILITY, ENCRYPTION.

---

### 5. Hash anchored

Products **SHOULD** be hash-anchored on BLOCKCHAIN for immutable proof.

---

## Roadmap

- **v0.1**: GIT LEDGER (current) - VaaS on GitHub
- **v0.2**: BLOCKCHAIN LEDGER - Hash anchoring service
- **v0.3**: CLOSURE - All products anchored with state declarations

---
