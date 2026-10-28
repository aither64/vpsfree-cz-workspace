# Archive watcher fix rollout — superseded first candidate

## Authorization and current status

User approved implementation and selected deploy-and-recover. Aitherdev may be
deployed using vpsfree-cz-configuration. No default-branch integration approval.
This record is preparation only until execution results below say otherwise.

## Candidates and predecessor

- Runtime db9578e2e195d2a86873e49bcdcfb1cf28bf62d8.
- Workspace afc2c144c7cea241b71ff425b5a455a1db060c15.
- Configuration 2c738ac851f43545272579a96cf836f99876eefb.
- Current application: /nix/store/a3r70kgqaf46185cjmjgalza67vpg0hd-dev-workspace-0.2.0.
- Current live and system-profile path:
  /nix/store/zyz7pvg8mzq1aiifhxpg6yhl7nknph4j-nixos-system-aitherdev-26.05.20261026.718f670.
- Native service active, PID156049 before activation. Capture again immediately
  before switching; ongoing unrelated sessions may change this baseline.

## Prepared sequence

After independent final review, build runtime package/archive lifecycle VM,
workspace default+deployment-contract, and exact configuration aitherdev generation.
Retain output roots and generation metadata. Observe exact runtime CI40713491647.
Copy generation before machine claim, then acquire machine:vpsfree:aitherdev and
verify held ownership. Ordinary confctl deploy selects that exact generation,
--dry-activate-first --no-reboot --yes; preserve health checks and auto-rollback.
System activation precedes guarded application workspace-host switch --source at
the reviewed workspace worktree with exact session and claim identity.

Verify terminal unit outcomes, exact live/system-profile/application paths, portal
health, native continuity and normal naming/conversation availability. No native
model request is needed to retry the existing archive. Do not restart the daemon
or weaken transition checks to bypass a refusal. Retain predecessor roots; recover
forward through ordinary package commands after any failure.

## Target archive receipt

Target 2026-10-28-observer-progress-guidance is still active with failed archive
attempt1. Receipt 8ef38791646bb344d6d0880a414e7c9b88f44d72a4f12831ef52ebb06cfc18c7;
journal ID eee092a6346cbc1e5e2def280080477fc0528fc837eec3a382b0489aa33fb004;
target identity d0b4d31d8b3e9638ceb9e2d5c5c64a56ca96edfc0a5cdf5da7fb80b27b3a2ae9;
root 01a181a7-2ddc-7852-a8c7-56c27709c461. No archive journal or cleanup sidecar
exists yet. Read current identity again before retry. Use the same public portal
POST /api/sessions/SLUG/operation/retry endpoint as Retry archive, with current
receiptId/journalId and canonical Origin via the local Unix socket. Never edit
receipts/holds or invoke an unrelated replacement operation.

Observe the independent archive worker; verify complete receipt, archive tracking,
removed exact owned worktrees, retained branches and conversations. Tracking sync
may finish separately. No other session lifecycle action is authorized.

## Release and integration

Do not release deployed machine ownership until effects and complete deployed
lineage integration are verified under installed machine-retention policy. Ask
for explicit runtime/workspace/configuration master integration only with concrete
reviewed results. Do not hold repository claims during builds, records or waits.

## Verification checkpoint

Runtime package checks passed locally. GitHub run 40713491647 passed at
db9578e2, including the exact archive VM derivation
qghxkwk9wf9kgpjr605rwcx1aygwdckc-vm-test-run-dev-workspace-session-archive-lifecycle.drv.
The first local VM attempt timed out during initial browser hydration before
archive submission; retain that failed result alongside the successful exact-input
CI evidence (details in state.md). Remaining workspace/system builds are pending.
At 15:39 UTC the selected application and system paths still matched the baseline
above. The original failed receipt still had attempt 1 and unchanged target,
journal and root identities. No deployment or archive retry has run.

## Built candidates

Composed application: /nix/store/0zyz4sxhk2p0pvfl0abw6ixq3asll083-dev-workspace-0.2.0.
Deployment-contract derivation passed. Exact confctl generation:
2026-10-28--16-51-07; system output:
/nix/store/wqz6zkd7850nvawp9gcv1rp2vpfhi5mn-nixos-system-aitherdev-26.05.20261026.718f670.
Build receipts and logs remain under verification/. Before activation after
a reservation wait, recheck actual baseline and preserve any intervening deployed
lineage; refresh candidates if required. Add selected-package disposable
archive/revive verification before claiming the runtime usable.

## Copy and reservation result

Copy-only of generation 2026-10-28--16-51-07 passed (exit 0). At
2026-10-28 15:54:42 UTC acquire returned waiting for claim
0863838f-bef9-4fe0-8a5e-f6db26a4a1b5; foreign holder is
2026-10-28-cross-session-messaging. No system/application activation or original
archive retry has run. Check claim-status on resumption; the threadless initiative
has no notification destination. Reuse this claim, not a replacement request.
