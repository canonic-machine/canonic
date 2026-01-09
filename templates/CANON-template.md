# CANON Template

Use this blueprint for any CANON scope. Replace placeholders with statements specific to the scope you are governing. For the root CANON, set `<NAME>` to the repository name and keep `inherits: /`.

```mermaid
graph TD
    A["{{NAME}} ({{scope path}})"] --> B["{{short identity line}}"]
    B --> C["inherits: {{parent scope path}}"]
    C --> D["axioms"]
    D --> D1["1. triad: {{description}}"]
    D --> D2["2. inheritance: {{parent link explanation}}"]
    D --> D3["3. coherence: {{semantic expectations}}"]
    D --> D4["4. compliance: {{structural requirements}}"]
    D --> D5["5. governance: {{coherence ∧ compliance}}"]
    D --> D6["6. invalidity: {{invalid scope description}}"]
    D --> D7["7. introspection: {{self-documentation loop}}"]
```
