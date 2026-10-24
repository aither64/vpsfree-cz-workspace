# C7 Git-cache publication handoff

All seven exact reviewed consumer heads are published over SSH, after provider
`822c0e35dbe2549111912f539116b4225dfd3035` and its remote R evidence ref were
verified. [Publication summary](verification/c7-git-cache-publication/published.json)
binds fresh per-repository SSH refs, previous R leases, source/tree/lock/clean
state, ordinary declared-shell push commands and comparison records. Its SHA256
is `1e86735d1416c586d3ea667a9711ce0832b3c104b7f7a2a42d7899fe6b096042`.
All eight source ranges passed [independent final review](review-git-cache-report.md),
SHA256 `6bb7afca1cd0b1794fb97bb3f8bcd20453a6ed94ae346fc0d375d4a27d4e92dd`.
No integration, deployment, claim, lifecycle action or cleanup occurred.

| Repository | Exact published feature head | Final branch commits |
| --- | --- | --- |
| haveapi | `c7bfc1aa5af956b6057be8e623f9035c00ccb268` | 1 |
| terraform-provider-vpsadmin | `c3f20203a5ba6200d0ff6b77f500bff6473f2c11` | 1 |
| vpsadminos | `889f14e5f964c85eac0dbffdff96909a46ab35c6` | 1 |
| vpsf-status | `018b700f06cf216a125a70ac9bfedddaabf07b92` | 3 |
| vpsfree-irc-bot | `0a160463a4ee12ec5f6c45e38eaba11592787d9f` | 1 |
| vpsfree-cz-configuration | `5f0f4466adb175ed4fcac9b6d5c8909e87a1fec1` | 1 |
| vpsadminos-org-configuration | `ca96c95a1fee04793468785d8323a759615b2b4e` | 1 |

[Authoritative source inventory](package-c7-final-source-inventory.json),
[source report](package-c7-final-source-report.md) and
[full ranges/R deltas](package-c7-final-source/) retain every base/head, path,
commit series, comparison, previous lease and backup ref. One adoption stream
per repository; status retains its independent vendor/Perl and metrics fixes
with unchanged stable patch IDs. No obsolete pins/fixups or migrations remain.
No consumer lock, deployment-tool pin or application code changed in this rework.
HaveAPI master `1103a3a1` divergence from feature base `7ac977a2` is accepted and
consciously deferred; no further target movement appeared during publication.
Other targets matched their recorded bases.

All seven ordinary declared-shell exact-lease pushes returned0 with active
hooks. HaveAPI's first push stopped at Overcommit's configuration signature
check. Fresh SSH still showed old feature74f/master1103, the local tree was
clean, and PG3315340 had exited. Reviewed configuration/custom hook bytes were
re-read and identical. Normal `overcommit --sign`, `--sign pre-commit` and
`--sign pre-push` passed; separately recorded `haveapi-signatures-2.json` then
published under the same74f lease. The original failed receipt/log and normal
repair log are preserved. No hook bypass or source/history correction occurred.

Quick/static/hook evidence is unchanged in [final quick receipt](package-c7-final-quick.json):
C40 shell cases, D20 shell cases, all7 cache checks with98 modeled scheduling
cases and14 negative controls, selected syntax and normal source commit hooks.
[Action evidence](package-c7-cache-actions.json) retains official current-ref and
runner compatibility checks. Owning user guidance is in HaveAPI development
docs plus the four ordinary project READMEs; they explain shared mirror retention
and per-update ancestry checks and link the exact provider guide. TF/IRC helper
help removes only the obsolete API-token requirement. Lead completed the prose
pass. Configuration workflow behavior is covered by the same shared contract;
no new project documentation was needed there.

## Bounded CI observation

[Snapshot](verification/c7-git-cache-publication/ci-snapshot.json) is one bounded
read after publication. No failure was observed on a final head. No run was
cancelled: no superseded same-branch queued/in-progress run was found. No waits,
dispatches, reruns or current-head cancellations occurred.

- haveapi servers/ruby RSpec: completed/success; [40119250404](https://github.com/vpsfreecz/haveapi/actions/runs/40119250404).
- terraform-provider-vpsadmin Go Tests: completed/success; [40119322279](https://github.com/vpsfreecz/terraform-provider-vpsadmin/actions/runs/40119322279).
- vpsadminos: no matching exact-head run observed.
- vpsf-status Integration Tests: in_progress; [40119441548](https://github.com/vpsfreecz/vpsf-status/actions/runs/40119441548).
- vpsf-status i18n health: completed/success; [40119441601](https://github.com/vpsfreecz/vpsf-status/actions/runs/40119441601).
- vpsfree-irc-bot RSpec: completed/success; [40119496297](https://github.com/vpsfreecz/vpsfree-irc-bot/actions/runs/40119496297).
- vpsfree-cz-configuration: no matching exact-head run observed.
- vpsadminos-org-configuration: no matching exact-head run observed.

Status Integration Tests remained in progress at this observation; this is an
unfinished CI result, not a passing claim. No second poll or CI wait was added.

## Prepared runtime boundary

Lead accepted [corrected sealed v2 packet](package-c7-git-cache-verification-brief.md).
[Manifest](package-c7-git-cache-manifest.json) SHA256
`3e88cb2425376729392535dd894d8c5240747784ebf1d3937eee1b2b7c6f19d2`;
[preflight](package-c7-git-cache-sealed-preflight-v2.json) records static checks.
The unexecuted first prepared packet and its unsupported outer bundle-exec probe
are preserved under `package-c7-git-cache-prelaunch-v1/`; v2 uses the exact plain
workflow invocation inside the actual caller shell and preserves Ruby/BUNDLE.
No credential loader or API-only token prerequisite exists in the new packet.
All original R scripts/receipts/roots remain untouched.

B's exact published package exported203 passed0/0pending under root's watcher;
provider/check/source graphs and owned links remain at
`/tmp/flake-update-guard-b-git-cache-rspec-2026-10-24-1`.
Its accepted `identities.json` hash is
`5e177aa68c1572ca828d207b43f6f7033e9df0bf77955d75201d410ff5c4ba19` and
`status.json` hash is
`b013d4aac3c13c5757c5e22aee3c9ad889ce012f7bedd9360d44ce49dc9e4222`.
No duplicate suite/package run is needed.

Remaining: root launches the selected seven updater/commit/final-HEAD-lock and
caller-shell/hook paths with one owned cache (real cold nixpkgs then warm reuse),
then the strict local Git target race. These are selected paths, not seven full
workflow reruns. Standalone dependency refresh/application build stages and
TF8VM are omitted, retaining source-bound R evidence. HaveAPI's unchanged
`utils/update-nixpkgs.sh` retains its conditional `nix flake check` after a
revision change and before commit; equality exits before that gate. Lead
authorized retaining this existing in-helper behavior in the selected path.
The completed HaveAPI receipt shows equality at nixpkgs `02c087f3`; its inline
check and commit arm did not run. See the
[accepted scope correction](verification/git-cache-haveapi-inline-check-scope.json)
and [completed-path facts](package-c7-git-cache-completed-path-facts.json).
The frozen driver, manifest and earlier preparation evidence remain unchanged.
C launched none of these operations and owns no running command. Source
ownership and diagnosis/fix responsibility remain C; root owns watcher
serialization and acceptance.

The selected-path launcher completed with six successful paths and org's
postflight fixture failure2: only the tools shell's untracked `.bundle/config`
remained, with HEAD/index/lock unchanged and all149 child commands0. The
[read-only reconciliation](package-c7-git-cache-selected-failure-reconciliation.json)
retains the exact effects and confirms no recorded process group remained.
The [org-only successor](package-c7-git-cache-org-brief-2.md) is prepared, not run;
it adds an exact local exclude before snapshots and preserves strict final
checks. Original receipts and all six successful paths remain unchanged.
Status supplied the single real cold nixpkgs mirror; IRC and vpsFree reused
the same directory with unchanged warm final checks. These are recorded local
cache facts, not GitHub Actions cache transport results. Final acceptance of
org and the independently root-owned race remains separate.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
