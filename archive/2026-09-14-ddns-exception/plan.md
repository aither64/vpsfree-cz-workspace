# Fast-track the DDNS fix

## Goal and delivery

Restore token-only DDNS updates for active user-owned zones, pass targeted
local specs, and fast-forward both vpsAdmin and configuration master branches.
The user explicitly accepted targeted local verification as sufficient for
merging, replacing the separate reviewer-agent stage. Do not wait for long CI,
run long VM integration tests, deploy production, or close this session.

## Repositories and commits

Reuse initiative and branch `2026-09-14-ddns-exception` in `vpsadmin` and
`vpsfree-cz-configuration`, with registered worktrees under the matching group.
Create one functional vpsAdmin commit with the fix and regression coverage,
then one generated configuration input-pin commit.

## Implementation

Change the lifetime helper administrator guard to
`next if current_user&.role == :admin`. Keep record-token lookup and owner-state
enforcement. Add real HTTP regression coverage for token-only A and AAAA
updates in user-owned zones, unchanged refreshes, and rejection of non-active
owners without record mutations or transaction chains. Retain system-zone and
invalid-token coverage. Add focused shared-helper regressions for anonymous,
regular-user, and administrator behavior.

## Verification and review decision

Demonstrate the user-zone regression fails before the fix. Run targeted DDNS
request, DDNS operation, shared-helper, and existing lifecycle-bypass specs in
the API Nix shell with isolated MariaDB. Run targeted lint and normal hooks.
Rebase onto current upstream before final verification; resolve failures before
integration. Per the explicit fast-track instruction, omit separate review
agents, the full suite, VM integration tests, and waiting for long CI. Inspect
already available CI results and record running workflows as pending.

## Integration and channel update

Fetch, capture the final comparison, and use a fresh target worktree for each
fast-forward merge and SSH push to master. Keep feature refs. After merging
vpsAdmin, run `confctl inputs channel set --commit vpsadmin vpsadmin <merged-sha>`
in the configuration worktree. Verify vpsadminServices resolves to the exact
merged fix; preserve unrelated inputs and the generated commit message. Capture
its comparison, fast-forward configuration master and push. Remove only the
fresh temporary integration worktrees. Keep the session and feature worktrees.

## Compatibility and deployment

No database schema, persisted format, client contract, URL/token, node protocol,
configuration option, or vpsAdminOS change. No coordinated node rollout.
API instances can be updated independently; old instances retain the bug during
a rolling upgrade. A rollback requires no state conversion but restores the
bug. Updating the channel does not deploy it. Production deployment is outside
this implementation. The email remains external to Git and its token must not
be copied into source, notes, or output.
