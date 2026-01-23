# CANONIC

Fixed governance operating system.

---

## Boundary

This repo contains **ONLY** the fixed kernel. Nothing here is domain-defined.

```
/CANONIC/                    ← THIS REPO (fixed)
/DOMAINS/                    ← Separate repo (extensible)
/ENTERPRISE/                 ← Separate repo (instances)
```

---

## Kernel Structure

```
/CANONIC/os/kernel/
├── canonic/                 ← Governance mechanics
├── language/                ← DETROS dimensions
│   └── nomenclature/        ← Identity and naming
└── machine/                 ← Enforcement runtime
```

---

## What's Fixed

- How governance works
- What dimensions governance may reason over (DETROS)
- How identity and naming work
- How enforcement works

---

## What's NOT Here

- Clinical truth
- Domain semantics
- Business rules
- Application logic

Those belong in `/DOMAINS/`.

---

## Inheritance

Domains inherit from the kernel:

```markdown
# In /DOMAINS/oncology/CANON.md

inherits: /CANONIC/os/kernel/machine/
```

Downstream may extend, never contradict.

---
