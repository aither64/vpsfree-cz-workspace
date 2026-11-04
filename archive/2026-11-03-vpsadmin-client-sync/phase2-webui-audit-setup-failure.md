# Initial WebUI documentation audit setup failure

Command: `nix develop --command npm run audit:design-docs` in the session-owned
WebUI worktree at base `1c8478bceb3943645ec06ccde895ee4b0985873f`, with draft
rule documentation. Exit1 before a valid inventory check, Node24.21.0.

Relevant captured output:

```text
> vpsadmin-webui@1.0.0 audit:design-docs
> node scripts/audit-design-docs.mjs
Error [ERR_MODULE_NOT_FOUND]: Cannot find package 'typescript' imported from
.../vpsadmin-webui/scripts/design-inventory.mjs
Error: Command failed: /nix/store/503mh0fj8j1cfvrxcavr76szbn4dk2r7-nodejs-slim-24.21.0/bin/node scripts/design-inventory.mjs
```

The fresh worktree had not run its documented root `npm ci`. The audit's link/
requirement phase reached its inventory subprocess, whose declared TypeScript
package was not installed. This is dependency preparation failure, not evidence
of a documentation defect. Do not change scripts or source to mask it. Lead
authorized one locked `npm ci --no-audit --no-fund` then the audit under a fresh
verification utility. Its separate success/failure evidence will follow.
