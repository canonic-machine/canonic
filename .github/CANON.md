# APPSTORE (/.github/)

inherits: /

---

## Axioms

### 1. GitHub IS the App Store

GitHub provides:
- User management (100M+ developers)
- Billing (Marketplace)
- Discovery (search + topics)
- CI/CD (Actions)
- Certification (badges)

We build VaaS only.

---

### 2. Zero Infrastructure

APPSTORE MUST NOT require custom infrastructure.

```
GitHub builds: Everything
We build: Validators only
```

---

### 3. Validator Distribution

Validators MUST be distributed via GitHub Actions.

```yaml
- uses: canonic/vaas-triad@v1
- uses: canonic/vaas-inheritance@v1
- uses: canonic/vaas-introspection@v1
```

---

## Components

| GitHub Feature | APPSTORE Use |
|----------------|--------------|
| Actions | VaaS validators |
| Marketplace | Billing |
| Badges | Certification |
| Topics | Discovery |
| Sponsors | Funding |

---

**GitHub IS the App Store. Zero infrastructure.**

---
