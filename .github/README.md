# APPSTORE (/.github/)

GitHub integration for CANONIC distribution.

---

## Principle

**GitHub IS the App Store.**

We build validators only. GitHub provides everything else.

---

## Distribution

Validators are distributed via GitHub Actions:

```yaml
- uses: canonic/vaas-triad@v1
- uses: canonic/vaas-inheritance@v1
- uses: canonic/vaas-introspection@v1
```

---

## GitHub Features Used

| Feature | APPSTORE Use |
|---------|--------------|
| Actions | VaaS validators |
| Marketplace | Billing |
| Badges | Certification |
| Topics | Discovery |
| Sponsors | Funding |

---

## Zero Infrastructure

APPSTORE MUST NOT require custom infrastructure.

```
GitHub builds: Everything
We build: Validators only
```

---

*Governed by: CANON.md*

---
