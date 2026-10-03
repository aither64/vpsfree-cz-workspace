# Rebased workspace composition review

## Request and boundaries

The user requested rebasing onto advanced dev-workspace master and asked whether
the workspace pin could merge after successful activation while the redesign
continues. This packet requests independent review of the rebased composition,
not merge, activation or storage acceptance. Session: 2026-09-23-storage-redesign;
workspace: /home/aither/workspace/ai/vpsfree.cz. Read [plan](plan.md),
[state](state.md), [design](design.md), and the current rebase/early-merge brief.

Overall risk is HIGH: persistent cluster state, package transitions, rollback
and cross-project browser/runtime composition. Retained reviewer0 is ready,
review-purpose, read_only, gpt-6.1-sol/xhigh. Saved settings govern the assignment;
no override or fallback. Cover general, architecture, scope and risk concerns
of the changed composition and complete final inventories. Prior provider
functional lanes remain recorded evidence; do not claim their independent
rerun merely from pin inspection. Read mandatory-change-review and all four
references. Review directly without nested agents, edits, tests, builds,
network fetch or private artifact access.

## Source and complete histories

The generic policy patch compares equal after rebase. Provider maintenance,
profile and fixture patches compare equal; all non-flake final blobs match
45d7ce88. Repeated development fixes are folded into the four owning commits.
The generated provider pin is based on upstream's new graph, not an old lock
replay. The consumer remains one generated pin commit. No migrations or schema
conversion exist in any of these three branches. No superseded input-update
stream, fixup or abandoned implementation is intentionally retained.

### Generic

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/dev-workspace-maintenance-policy`.
Base: `924c0ec28c41dd8b56aaf17f2212b302ca614899`.
Head: `4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4`.
Tree: `2c4c4b7ecfd74a12dda2241fe05033e44151e4a9`.
Final binary diff SHA256: `e661821280fe51d09ba7056e56c5c7e7959d161f4ecf78da4fcb471c97675c62`.
4 files changed, 175 insertions(+), 3 deletions(-).

Complete commits:

- `4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4 runtime: require maintenance-aware cluster transition policy`

Complete paths:

- `docs/workspace-portal.md`
- `libexec/workspace-host`
- `portal/internal/session/runtime-contract.json`
- `test/workspace_host/profile_transition_test.rb`

### Provider

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/vpsfree-dev-workspace-storage-profile`.
Base: `8f8d8ecf5031c40d3e4a4ee2e9425721fc035800`.
Head: `399c33023a568a8d7a21e4e4df52829628720a28`.
Tree: `557303f2b98bb9f136962c6f9f35af43122ba28e`.
Final binary diff SHA256: `5cdf235611468e0ae67399318765f72fe7edd986d819a32b0ff3e0ba220f313f`.
25 files changed, 5288 insertions(+), 67 deletions(-).

Complete commits:

- `5b2e9a4bb95bcf4070d62da33b219ed3c5a33f12 flake: require the maintenance-aware runtime transition policy`
- `101d31264fb54cc39b2d0d9519a202d0705a7078 vpsadmin: preserve stopped clusters through maintenance copy`
- `f50c92bf146c3f3d93a5293e0c005f5fdb3a26e2 vpsadmin: preserve assignments in the development storage profile`
- `399c33023a568a8d7a21e4e4df52829628720a28 vpsadmin: test retained services through interrupted maintenance`

Complete paths:

- `dev-clusters/lib/devcluster_runner.rb`
- `dev-clusters/vpsadmin/README.md`
- `dev-clusters/vpsadmin/bin/devcluster`
- `dev-clusters/vpsadmin/lib/devcluster-runner.rb`
- `dev-clusters/vpsadmin/lib/maintenance.rb`
- `dev-clusters/vpsadmin/lib/storage_profile.rb`
- `dev-clusters/vpsadmin/nix/storage-profile-provision.rb`
- `dev-clusters/vpsadmin/nix/storage-profile.nix`
- `dev-clusters/vpsadmin/nix/storage-profile/config.rb`
- `dev-clusters/vpsadmin/nix/storage-profile/dataset_plans.rb`
- `dev-clusters/vpsadmin/nix/storage-profile/hooks.rb`
- `dev-clusters/vpsadmin/nix/test.nix`
- `dev-clusters/vpsadmin/tests/run-storage-profile-api-specs.sh`
- `dev-clusters/vpsadmin/tests/storage-profile-acceptance.rb`
- `flake.lock`
- `flake.nix`
- `nix/tests/retained-services-maintenance.nix`
- `test/devcluster_commands_test.rb`
- `test/devcluster_maintenance_test.rb`
- `test/devcluster_nix_smoke.rb`
- `test/devcluster_runner_test.rb`
- `test/devcluster_status_test.rb`
- `test/devcluster_storage_profile_test.rb`
- `test/retained-services-maintenance/devcluster-runner.rb`
- `test/vpsadmin_storage_profile_spec.rb`

### Consumer

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/workspace`.
Base: `93389c3373647fb3dc2d7ee15efa9acb93a8c62f`.
Head: `6d1b9c4d63d900dbe8fe5b8790c8f92b28ab0b25`.
Tree: `17967cd9a75c452cb3fcecf7b23f2011de5e7487`.
Final binary diff SHA256: `18d2131e8abf5f7ab427837f34c09374af91328f5851f07a96c6059177c7a333`.
2 files changed, 9 insertions(+), 9 deletions(-).

Complete commits:

- `6d1b9c4d63d900dbe8fe5b8790c8f92b28ab0b25 flake: select the preserving storage-profile provider`

Complete paths:

- `flake.lock`
- `flake.nix`

## Dependency resolution and upstream context

Generic upstream 4bec..924 adds session creation/recovery progress and Codex Web
4c170393a96ed0a6ac2e43488d073f6fcab36132. The old host helper, canonical contract,
transition spec, host module and host paths retain exact bytes at the rebased
feature. Shared portal documentation preserves both upstream progress and
policy-3 sections. Upstream changes Go module/sums/vendorHash and browser/client
sources together; inspect pairing and existing packaged Go/JS/Ruby coverage.

Provider upstream c56..8f8 changes only its generated generic pin. New pin5b2e9a4
selects published generic4ef; exactly four generic lock metadata leaves differ
from8f8. Codex Web4c and every other node/follow remain upstream. Default API5c76,
OS158025, WebUI534c/status and all guest/runner selections remain unchanged.
Enabled fixtures still explicitly select same-session API46b3bf6f.

Consumer upstream8990..933 already pins provider8f8/generic924/Codex4c, alongside
coordination changes. Its rebased pin6d1 selects published provider399; exactly
eight leaves (locked.rev/narHash/lastModified and original.rev for provider and
generic) change from933. All other nodes/follows and root defaults remain equal.
The root has no enabled storageProfile selection. Inputs/locks were generated
with owning Nix commands; no hand splice. Exact backups retain old2b/45d/492.

Canonical runtime contract remains schema1/policy3, owned by generic and consumed
by both host and organization-tools from the same input. Provider wrappers,
optional runner policy, maintenance_adopt before common early return and ordinary
hold guards stay unchanged. Unknown/malformed hold/state still fails closed.
A later generic policy-3 pin paired with a legacy provider lacking hold guards
is insufficient: early root integration must retain the complete reviewed
composition and durable published refs, or coordinate generic policy with at
least provider maintenance integration. No new enforcement mechanism is added.

## Existing review and verification evidence

Original generic4bec..8b review had no Blocking/Important; its preservation
wording advisory was fixed directly before2b publication. Whole provider
c56..59f1 all four lanes had one Important lazy CatchUp STI loader, corrected by
eager normal active/retired initialization and real fresh-reader queued/terminal
regression1/0. Affected f36..4f75 general/architecture/risk found the lazy config
GC-root lifetime; direct standard out-link correction passed. Direct fixture
runtime corrections and their bounded proofs are recorded in
[provider review](storage-profile-provider-review.md) and [rollout](storage-profile-rollout.md).
The prior root8990..492 four-lane review had no findings. These original ranges
remain the independent evidence; this packet does not rewrite them as new-head
full rereviews.

Lead-reported host-migration PASS at f36 and real native services PASS at45d/API46
remain scoped evidence. Native sole example611.85s (command802.973s),
scenario_completed1/starting_copied1/released0. It proves ordered masks,
old-writer exclusion, interrupted copy/receipt, protected SQL/sentinel/disk and
forced copied seed retry/two starts. It does not prove public full-cluster Node
refresh/release or actual VPS/NAS full/incremental/history acceptance. Reuse
requires final host/contract/helper/runner/profile/fixture and relevant guest
input/interface equivalence; independent review should assess this rationale.

The fresh frozen-source quick batch passed all six stages in1175.12s, parity1:

- Generic policy/transition fixture40runs/250assertions, all0 (2.704s).
- Provider maintenance13/121, runner10/27, selected CLI8/105, all0 (60.651s).
- Existing default smoke (428.045s).
- Explicit API46 profile smoke (654.618s).
- Provider no-build (23.366s).
- Root no-build (5.625s).

No guest, maintenance app, selected-package or registered-cluster operation ran;
no local kernel compilation was reported. The first utility ran current from
the wrong CWD and performed zero checks; its replacement used the exact tracking
binding. Private evidence is `/tmp/storage-profile-rebase-quick.cgbjlt0h`; the
reviewer need not read it. Generic4ef CI37113228573 also passed. Provider399 Check
37114037083 was in_progress at last metadata query. Existing four root checks,
default package and actual packaged contract/helper/client byte proof follow
this review. Their earlier492 results do not prove the new composition.

Separate companion API broad CI37030949481 failed117/118; sole remote restore
example3 rollback timeout900s, dependentexample4 423Locked. Read-only [diagnosis](api-remote-restore-ci.md) identified an upstream-existing
Node RPC cleanup timeout/daemon exit and restart losing the fixture zero-delay
patch. The broker trigger remains unknown; no blind rerun/manual unlock or
workspace rebase cause is assumed.
Topic API46 CI27/27 succeeded. API branch/migrations are unchanged by this packet:
its two previously consumed migrations remain foundation then bounded indexes,
and additive schema remains unchanged. The API failure limits storage readiness;
root default remains API5c76 and profile disabled.

## Documentation, trust and integration

Owning generic docs/workspace-portal.md and provider README explain supported
policy/hold/preserving profile/recovery. Individual operation/status evidence
belongs in linked session records. The new rebase has no behavioral doc rewrite;
its exact graph, review and proof belong here/state/design. The trusted local
operator assumption remains from repository AGENTS; it does not weaken remote
client or guest boundaries. No extra hostile-operator filesystem tests are asked.

User has authorized rebases, not master integration. Successful external public
activation is still pending, after checks/review/package proof and idle managed
sessions. Do not invoke switch as an active-turn idleness probe or use private
candidate helpers. The narrow workspace pin may merge independently after
activation and explicit workspace/master approval; retain feature refs/session
and complete maintenance-aware dependencies. No other project integration,
production strict/quiet/repair/APPLY or reset is cleared.

Please report ordered findings/severity/source lanes, compatibility and dependency
pairing, explicit complete-history/no-obsolete and no-migrations conclusions,
plus remaining gates. No private logs need to be read or tests rerun.

## Independent result

Reviewer0 completed the exact three-range composition review with saved
Sol/xhigh/read_only settings and no override/fallback. No Blocking, Important
or Advisory findings in any of the four lanes. Exact heads/trees and all three
full-index binary hashes matched. Complete1/4/1 commit histories are coherent;
no obsolete/fixup/repeated pin stream and no migrations/schema conversion remain.
The provider's three functional patches and all non-flake final bytes match45d.

The review confirmed canonical ownership, exact four/eight leaf deltas and
unchanged defaults/follows; upstream creation/recovery progress and Codex4c
are paired with module/sums/vendorHash. Reusing hostf36/native45d observations
is justified by unchanged relevant source/guest inputs, within their original
scopes. This does not prove the new package output or activation.

Remaining gates: exact root package/four checks/installed runtime-client-helper
proof (fresh watcher now assigned), durable exact dependency reachability,
external idle public activation, explicit workspace/master merge direction and
the separate full-cluster Node refresh/release/payload/restore follow-up.
The review ran no tests/builds/fetches/private reads/ref/index or lifecycle
actions. Prior unchanged functional reviews are retained rather than relabeled
as new-head reruns.

## Post-review package and publication evidence

The fresh package launcher completed all three stages at exact clean `6d1b9c4d`:
exit 0 in 245.623s, source parity 1. It realized the four existing root checks,
built the default package and proved installed runtime/helper/Codex source bytes
plus canonical host/tools contract equality, schema 1/policy 3, two executable
providers and the eager profile loader. Evidence:
`/tmp/storage-profile-rebased-package.xnradz5x`. Package:
`/nix/store/zmwh78dk1vjh2b91qnibjl682rb8hmwc-dev-workspace-0.2.0`; tools:
`/nix/store/vah0176g8h75vasl0nlg0farmaacybid-vpsfree-dev-workspace-tools-0.1.0`.
A redundant verifier invocation supplied its hash as a package argument and
performed no checks; the launcher's correctly parameterized proof had passed.

Generic CI37113228573 and provider CI37114037083 succeeded. Normal exact-lease
SSH publication advanced root feature `492fdf8e` to `6d1b9c4d`, leaving remote
master `93389c33` unchanged. Public comparison capture records exact933..6d1.
Readback confirmed durable ordinary remote anchors at exact dependency heads:
generic `backup/2026-09-23-storage-redesign-workspace-runtime-4ef298b3` and
provider `backup/2026-09-23-storage-redesign-workspace-provider-399c3302`.

Those package/publication gates are now complete. Package selection remains
pending external idle activation; workspace/master integration still requires
explicit user direction. Public full-cluster refresh/release, payload/history
acceptance and the separate Node/remote-restore follow-up remain outstanding.
