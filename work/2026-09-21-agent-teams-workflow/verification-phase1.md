# Phase 1 verification

## Verified heads

- `dev-workspace`: `39bfa664298443334d12b08dd42a475eef1c38e4`
- `vpsfree-dev-workspace`: `583647dd998e5b4cb0e9fa6833e29bb5aec757b8`
- workspace: `0ccd1101f56499b69312c72de82f4171dde08762`

All worktrees were clean before the commands ran.

## Focused remediation checks

A fresh Luna/low operation watcher ran the focused portal Go tests on generic
head `b5eafc66498997e947054cae3145d09dde61a98c`:

```text
go test -mod=mod ./internal/workspacecodex ./internal/web ./cmd/workspace-portal
```

All packages passed. The same watcher validated the changed generic
`dev-session-monitor` skill with the canonical `quick_validate.py` in a PyYAML
Nix environment; it returned `Skill is valid!`. The final generic head differs
only by the Nix name-recomputation assertion, whose parse and drvPath evaluation
passed before commit.

Two earlier watcher invocations did not produce code evidence because they used
the repository root rather than the `portal` Go module. The first correct-module
run exposed stale slow-validation fixtures and a real unmanaged retry-validation
bug; both were fixed before the passing run. Its retained failure log is
`logs/portal-tests.log`.

## Long package/check batch

A new fresh Luna/low operation watcher ran the following related batch with
local path overrides and no lock-file or source publication changes:

1. Generic `checks.x86_64-linux.agent-team-catalog` — passed in 230 seconds.
2. Generic `checks.x86_64-linux.package` — passed in 6 seconds.
3. Organization `checks.x86_64-linux.package` with the generic feature worktree
   override — passed in 233 seconds.
4. Site `checks.x86_64-linux.agent-team-policy` with organization and generic
   feature worktree overrides — passed in 231 seconds.
5. Site `checks.x86_64-linux.agent-instructions` with both overrides — passed in
   5 seconds.

Every command exited 0 and no process remained running. Complete output is in
`logs/phase1-package-checks.log`.
