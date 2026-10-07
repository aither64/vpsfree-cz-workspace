# Archive reliability rollout — 2026-10-05

The simplified implementation is deployed on aitherdev and all registered exact
final feature heads are merged into their remote default branches. The user
requested deployment, verification and then integration; the later instruction
“you can deploy aitherdev at will” released the deployment hold. Feature refs
remain retained and the session stays open.

## Deployed versions

| Component | Revision or output |
| --- | --- |
| Generic runtime | `e05915986227af41ececea55e498dc07ea1bc219` |
| Workspace | `96b0eec987f1b53059ac6be7f9cf207112caacf2` |
| Configuration | `e52b1b14224599c2ffa80650d7906861a5a730ed` |
| Composed extension, unchanged | `0ff827df13e82dfab4b536ff29979280f264e8f5` |
| Application user profile | `/nix/store/vnxvq3nspzdd0xifxhsihhbh1r9ylm64-dev-workspace-0.2.0` |
| Confctl generation | `2026-10-05--19-49-11` |
| NixOS system | `/nix/store/j0gg2zg327acbl5vs5hd7arpywwsxyhv-nixos-system-aitherdev-26.05.20261004.0d9e9b8` |

The application remains in its user profile. Configuration selects the matching
host module/runtime contract. Codex0.160.0, catalog, extension and persisted
cluster/protocol contracts are unchanged.

## Verification and result

The complete simplified source/history review and its bounded final corrections
have no unresolved source findings. The final native query correction passed
43focused tests and exact-head CI37348346642; CI's host job was skipped. The full
composed package build passed. The actual scoped host configuration built, then
normal dry activation and switch passed both host health checks.

The ordinary application switch succeeded, preserving normal generation and
quiescence rules. Portal health, session/operation endpoints, four runtime
services and the enabled hourly timer pass. Earlier compatibility checks and
package/extension tests remain documented in their linked evidence.

The first fresh worker run exposed repeated60second saved-list timeouts; only
that owned manual invocation was stopped. A measured indexed native query
returned the retained set in7ms. The reviewed correction uses it for positive
retained discovery and final proved-root retirement, preserving loaded-ID and
metadata checks. Negative/threadless discovery remains unchanged. This query
does not certify unknown saved records that are both unindexed and unloaded.

The corrected installed worker finished successfully in129.707seconds. Its fresh
scan at17:54:42UTC observed216rows and obtained known activity for43sessions,
with zero observation_unavailable diagnostics. This session has known activity
and no diagnostics. No sessions were eligible or archived. The scan reports
deferred remaining records, principally149invalid legacy lifecycle records and
150missing normalized manifests; diagnostics overlap. The original infra-monitoring,
newadmin-exception and newadmin-http-check examples currently report unverified
creation/operation evidence. A successful scan does not certify those records
or prove a live archive completed.

All three changed masters were fast-forward merged and pushed. The unchanged
registered extension feature head is already an ancestor of its remote master.
Exact feature/default proofs cover all four registrations. Shared modified files
and the empty index were preserved; temporary integration worktrees are removed.

## Historical maintenance and coverage limits

The permanent installed migration subsystem is removed. The dated source-only
repair program and [maintenance procedure](../../docs/maintenance/repair-legacy-sessions-2026-10-04.md)
are available, but no real historical repair/archive selection was applied.
Keep dirty, unmerged, busy or unknown records intact until their exact selection
and recovery evidence are handled. The enabled worker retains its normal policy.

Remove the dated tool when no active/archive/recovery record or supported
restore/revival path depends on it. The runtime recovery guide owns separate
removal criteria for temporary predecessor readers. Ordinary supported unknown-base
manifests and archive journals remain supported; a date alone is insufficient.

The user requested proportionate verification for development tooling. The
expanded private installed/native/browser matrix was stopped; all nine owned
fixture units have empty cgroups and are stopped. Initial native smoke passed,
but previews produced blockers and no private repair/archive apply or full
browser acceptance completed. Those limits are retained without another matrix.

[Final source review](simplification-final-review-report.md),
[correction review](indexed-correction-review-report.md),
[package build](indexed-final-package-build-result.json),
[host build and actual generation](indexed-host-generation.json),
[host switch](indexed-host-switch-result.json),
[application switch](indexed-application-switch-result.json),
[live smoke](indexed-live-smoke-result.json),
[worker result](indexed-installed-worker-result.json),
[exact merge proofs](indexed-final-integration-result.json),
[private coverage limits](simplification-installed-preview-limits.json).
