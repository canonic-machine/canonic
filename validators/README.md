# VALIDATORS

Validator-as-a-Service (VALIDATORaaS) — Enforcement layer.

## Structure

```
/validators/
├── MACHINE (6 axioms) — Validation logic
├── OS (1 axiom) — Packaging
└── LEDGER (4 axioms) — Storage
```

## Axiom Count

| Layer | Axioms |
|-------|--------|
| MACHINE | 6 |
| OS | 1 |
| LEDGER | 4 |
| **Total** | **11** |

## Relationship to SERVICES

```
VALIDATORS ◄─────────► SERVICES
    │                      │
    │   validates          │
    └──────────────────────┘
```

All SERVICES artifacts must pass VALIDATORaaS validation.

## Implementation

- Python validators in `/validators/`
- Pre-commit hooks via OS packaging
- Git as LEDGER (immutable, authoritative)

---
