---
lifecycle: active
---

# Flake input ancestry guard

All eight approved default-branch merges are verified; final bounded CI/source
observation is pending. Session remains open. The cached-Git
rework is implemented, independently reviewed, published and verified. All eight
feature branches remain unmerged. Defaults are unchanged and nothing was deployed.
The session stays open.

[Current acceptance](verification/git-cache-acceptance.json) binds exact sources,
review, publication, packaged checks, selected runtime paths, cache reuse, local
race and final CI/source observations. [Reviewed inventory](git-rework-final-source-inventory.json)
contains complete base-to-head series, final diffs and migration conclusions.
Historical R/API records and output roots remain preserved as exact old evidence.

## Integration approval

The user explicitly directed: "ok, merge it to the default branches".
Approval covers confctl/master, haveapi/master,
terraform-provider-vpsadmin/master, vpsadminos/staging, vpsf-status/master,
vpsfree-irc-bot/master, vpsfree-cz-configuration/master and
vpsadminos-org-configuration/master. It covers patch-equivalent fresh-base
preparation; material conflict/scope changes return for direction. Lead will
integrate one repository at a time with a short claim, ordinary fast-forward
merge/hooks, nonforce SSH push, remote proof and immediate release. Feature
refs and the open session remain preserved. No deployment or cleanup is authorized.

Fresh preparation found vpsFree configuration master advanced from50d263d4
to bec5556f6c60414e482550dd735321ebe3c3703b. Feature5f0f4466 is unchanged;
implementer0 is classifying the upstream delta read-only before any refresh.
confctl/master is now integrated at exact822c0e35 with fresh remote proof;
claim d51fa03f-104d-4fe8-871c-5938933fdfdd released. Six of eight defaults are integrated: confctl, Terraform provider, vpsAdminOS/staging,
status, IRC and org configuration. Their claims are released. HaveAPI and vpsFree
configuration refreshes passed focused review; feature publication and final merges remain.

## Phase checklist

- [x] Architect design and compatibility/verification contract.
- [x] confctl Git provider, mirror locking and changelog reuse implemented.
- [x] All seven workflow caches and one exact final provider pin per consumer.
- [x] Owning docs/help/manual/main writing pass, quick checks and ordinary hooks.
- [x] Independent final all-four-lane review and complete eight-branch history assessment; no findings.
- [x] Published exact package: 203 examples, zero failures/pending.
- [x] Seven selected updater/caller/commit/final-lock paths; actual IRC and both old configuration shells.
- [x] One real cold canonical nixpkgs mirror and warm reuse of the same directory/objects.
- [x] Real local push race; stale push and stale regenerated candidate rejected, manual pin preserved.
- [x] Final bounded CI/source/SSH observations; every observed exact-head run successful.
- [ ] Explicit repository/target integration approval, fresh preparation and authorized merges.

## Behavior and compatibility

Provider `822c0e35dbe2549111912f539116b4225dfd3035` uses cached Git ancestry
instead of the GitHub comparison API. `--forward-only` prepares a separate lock,
resolves complete follows paths and validates changed reachable dependencies,
including transitives, before atomic installation. Equal/descendant supported
GitHub full-SHA sources pass. Regressions/divergence reject with status3;
unavailable or invalid evidence returns1. Both stop publication. The workflow's
final check validates exported HEAD:flake.lock against the original baseline,
then uses ordinary nonforce push. A moved target requires a fresh baseline.

Mirrors retain the existing exact-URL SHA256 cache layout. Per-mirror sibling
locks cover preparation and reads, including both changelog callers. Cold full
clones install atomically; warm objects avoid fetch; missing immutable commits
are fetched. Invalid/incomplete caches fail visibly. There is no silent API
fallback. All seven workflows cache ~/.cache/confctl and save after safe rejects.
Hosted Actions cache transport itself was not exercised locally.

Manual/set/unflagged behavior and deployment-tool pins stay unchanged. The
JSON listing supplies full alias-resolved revisions to status/IRC scripts;
normal table output stays abbreviated. No migrations, persisted-state format,
protocol or coordinated node changes occur. Sequential old/new cache reuse is
supported; simultaneous old/manual writers do not honor the new lock and are
outside the cooperating-writer guarantee. Ancestry does not detect a later
upstream revert or establish software compatibility.

## Verification

- [Independent final review](review-git-cache-report.md): retained reviewer0,
  Sol/xhigh/read_only, all four lanes and all eight full histories; no findings.
  Two provider commits, six one-commit consumers and status's three justified
  commits; no obsolete API/fixup/pin history or migrations. Remote R evidence ref
  was preserved before replacing the provider feature ref.
- [Actual package with 203 examples](verification/git-cache-exported-check.json): 98 seconds,
  zero failures/pending, actual caller/preload/Git-hook regressions included.
  Full source/input/NAR/derivation/runtime identities and owned output roots retained.
- [Seven selected paths](verification/git-cache-selected.json): six original
  successes plus same-source org-only successor. These are scoped updater
  checks, not seven complete new workflow reruns. Unchanged standalone dependency
  refresh/build and Terraform’s eight-example VM stages were omitted. Historical R complete
  workflows/VM remain component evidence at their exact old sources.
- HaveAPI took equality and exited before its existing inline flake check and
  commit arm. vpsFree actually updated llm-agents and verified its version.
  IRC and both old configuration caller probes passed with actual Ruby/BUNDLE
  state; update commits used repository hooks where the live branch made commits.
- Status created the single cold canonical nixpkgs mirror during its 2328.24-second
  selected update; IRC's later warm update took 12.58 seconds. These are whole
  command durations. Same directory device/inode and unchanged warm final
  snapshots prove reuse. Final shared cache uses 5,879,009,280 bytes.
- Original org fixture exited2 after 149 commands with status 0 because old tools-shell setup
  created untracked .bundle/config. [Reconciliation](package-c7-git-cache-selected-failure-reconciliation.json)
  found no provider defect or tracked mutation. Fresh org-only fixture excluded
  exactly that local generated file before baseline/setup and passed 195 commands with status 0;
  strict final status/HEAD/index/lock checks stayed intact. Original failure retained.
- [Real local race](verification/git-cache-race.json):59 commands passed in 10.149 seconds,
  expected stale push1 and stale-candidate guard3, equality0, manual target and
  lock/index/HEAD preserved. Deterministic candidate supplier; live Nix generation
  is covered by the selected paths.
- Final bounded observations: [provider](verification/git-cache-provider-final-observation/final.json)
  and [seven consumers](verification/c7-git-cache-final-observation-2/final.json).
  All observed exact-head CI runs completed successfully, including provider Tests
  and status Integration. OS and both configs had no matching exact-head runs.
  Fresh SSH features match reviewed heads; local series/full-index binary diffs
  are unchanged and clean. No CI wait, dispatch or rerun was used.

All runners and source operations ended. No guest, repository/machine claim or
uncertain mutation remains. Org's separate duplicate watcher log was omitted;
its complete launcher aggregate and every child stdout/stderr remain retained.
This did not require another run.

## Published branches and remaining integration

All use feature branch `2026-10-24-flake-update-downgrade-guard-replacement`.
Full bases/heads/trees are in the reviewed inventory and final observations.

| Repository | Published head | Target |
| --- | --- | --- |
| confctl | 822c0e35 | master |
| haveapi | c7bfc1aa | master |
| terraform-provider-vpsadmin | c3f20203 | master |
| vpsadminos | 889f14e5 | staging |
| vpsf-status | 018b700f | master |
| vpsfree-irc-bot | 0a160463 | master |
| vpsfree-cz-configuration | 5f0f4466 | master |
| vpsadminos-org-configuration | ca96c95a | master |

HaveAPI retains reviewed base 7ac977a2; its master is 1103a3a1 after an unrelated
library-lockfile/build-tooling change. The feature is not included there and is
not immediately fast-forwardable. After explicit HaveAPI/master integration
direction, inspect the then-current target, preserve upstream deletions and
prepare the adoption on that base, proving old/new patch/history equivalence
and applying affected review/checks as needed. Do not describe existing receipts
as runs on a future SHA. Other targets also require ordinary fresh merge checks.

Lead owns approval-bound coordination and acceptance. Implementer0 retains all
seven consumers/runtime diagnosis; implementer1 retains provider; architect0
owns design; reviewer0 retains independent review, all with saved settings.
No implementation/check blocker remains. Next action belongs to explicit
repository/target integration direction. Preserve feature refs, failed roots,
Nix roots and original recovery records. No cleanup/deployment/lifecycle action
is authorized.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)

Integration progress: six exact default heads verified; see verification/integration/*/result.json.
Focused refresh review f55e7a94 passed, target hook preparation89.206s passed; no duplicate runtime gates.

All eight integrations are now verified; every exact merge claim is released.
See [integration summary](verification/integration/summary.json). HaveAPI399 and
vpsFree252 are reviewed equivalent successors on their new bases. Original
source/runtime receipts remain preserved with their exact source identity.
No deployment, cleanup or lifecycle action occurred. Final CI status observation
is pending; no CI wait was requested.
