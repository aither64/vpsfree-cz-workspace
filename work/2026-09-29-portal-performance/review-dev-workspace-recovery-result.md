# Dev-workspace archive recovery review

## Scope

- Repository: `dev-workspace`
- Review base: `9db7bc844a0332b7e00d21536c3bebf835928ece`
- Reviewed head: `4999212df75216ccf93c010caecad46fc39c8061`
- Remediated head: `fbd7a9e390b563f83d1787e2cddbd516eefeb558`
- Risk: High
- Reviewer: retained `reviewer0`, `gpt-6-sol`, xhigh, read-only
- Lanes: General; Architecture and repetition; Scope and proportionality; Risk and compatibility

## Findings

1. **Blocking:** archived root retirement skipped the active-directory uniqueness check. Fixed by requiring active discovery to be empty before clearing an archived root's attempts; regressions cover different-ID and same-ID active candidates.
2. **Important:** root archive proof no longer enforced the existing `vscode` source rule. Fixed with a shared root-only proof entry that retains source validation while member proof remains source-agnostic.
3. **Important:** the private team archive preflight failed for valid root-only sessions after the service accepted an absent roster. Fixed with an absent-roster success result and CLI regression.

## Verification

- Full host `go test ./internal/workspacecodex ./internal/teamruntime ./cmd/workspace-portal` passed after remediation.
- Focused proof, roster, retry, source, active-sibling and root-only CLI tests passed.
- Five Ruby host recovery tests passed with 63 assertions.
- Four lifecycle archive retry tests passed with 83 assertions.
- Go formatting, Ruby syntax and `git diff --check` passed.

No review rerun was required because the fixes narrow behavior to the reviewed safety contract and introduce no new design or public boundary. There are no migrations and no superseded committed recovery approach. Long package builds, real candidate/predecessor replay and live recovery of the two authorized journals remain later gates.
