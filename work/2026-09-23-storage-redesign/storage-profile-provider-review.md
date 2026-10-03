# Provider storage-profile review packet

## Status

Completed original mandatory review, 2026-10-02, followed by a verified direct
STI correction. The original reviewed range remains below. Host-migration
passed on that corrected head. The default-pin correction passed quick checks
and has been folded. Affected-lane review found one fixture-root lifetime issue;
its direct correction passed. The required host migration and retained-services
native fixture now pass; generated consumer composition remains next. See the
[disabled NixOS option lesson](../../notes/vpsfree-dev-workspace/2026-10-02-disabled-nixos-options.md).
No populated-cluster acceptance
or package activation is claimed.

Session: `2026-09-23-storage-redesign`. See [plan](plan.md), [state](state.md)
and the accepted [design and verification brief](design.md).

## Independent result and required correction

Reviewer0 completed this exact four-commit range in all four HIGH-risk lanes
with retained GPT-6.1 Sol/xhigh/read-only settings. Session identity, clean
head/tree and binary diff hash matched the packet. No Blocking findings and
one Important finding in general, architecture/repetition and risk/compatibility;
scope/proportionality has no findings.

**Important: fresh consumers cannot load persisted CatchUp chains.** Profile
commit `50e45ae5`, `dev-clusters/vpsadmin/lib/storage_profile.rb:420-439`, lazily
defines `DevClusters::VpsAdminStorageProfile::CatchUp` only when the provisioner
calls `catch_up_chain`. A nonempty chain persists that ActiveRecord STI name,
but ordinary enabled/retired config initialization does not define it in a
fresh API, supervisor or database-task process. Model-based chain readers then
raise `ActiveRecord::SubclassNotFound`, including for terminal history rows.
Same-process specs and provisioner waits already have the constant and conceal
the defect. Make one authoritative class available through normal active and
retired initialization and verify a real persisted nonempty chain in a fresh
reader, without calling the producer or adding an unknown-type fallback.

Implementer0 supplied this narrow direct correction and focused regression
before integration checks began. Mandatory-review step 9 permits direct focused
inspection/verification of the requested fix; a new contract would require
reconsidering the affected lanes. The original reviewed range remains the
review evidence; no later head is labelled independently rereviewed.

The held two-file correction moves the unchanged class body to
`load_catch_up_chain!`, calls it from normal `configure`, and delegates producer
lookup to that same definition. API bootstrap loads the models before ordinary
hooks/plans, so initialization can define the type without firing work. A fresh
Luna/low watcher ran one real-DB example: two ordinary active/retired
overlay readers query queued and terminal nonempty rows. Their test-only
READ UNCOMMITTED visibility is bound to the automatic disposable TestDb;
fixture state is not committed and runtime isolation is unchanged. This first
run failed 1 example/1 failure (exit 1, command 46.729833640 seconds;
RSpec 12.81 seconds): a reader subprocess failed but its suppressed diagnostics
did not identify the stage. Log `/tmp/storage-profile-watch.vEQpKkov/rspec.log`.
Both held hashes and heads/index were unchanged; no matching wrapper or owned
DB process remained. Public pinned ActiveRecord 8.1.4 source and a no-DB loader
probe identified the fixture error: `DatabaseConfigurations` was referenced
before `Base` loaded it. The child now uses
`ActiveRecord::Base.configurations.resolve` and finite numeric failure stages
without exporting messages, URLs or SQL. The fresh diagnostic watcher passed
1 example/0 failures, exit 0 in 40 seconds; log
`/tmp/storage-profile-watch.ShenILPS/full.log`. The runtime helper was unchanged
between attempts. Normal pinned Git folded only these two tested paths into
profile `23363e98`; the separate VM patch remains equivalent at `f36f15d7`.
This directly resolves the Important finding under mandatory-review step 9;
it is not a full independent rereview of the new head.

The reviewer explicitly inspected all four commits and 25 changed paths:
coherent independent purposes, no obsolete committed approach, no fixup-only
history or repeated input-update stream, and no provider migrations/schema
conversion. Outer schema 1/policy 3, private hold/config v1 and the consumed
Admin migrations remain as inventoried. Native fixture execution/results and
scoped clone cleanup conform at source level; no VM/payload result was claimed.

Residual gates: generated workspace pin and exact composed
package/host-tools contract; external idle activation; actual public copied boot,
Node refresh/release and original-VPS/accounting preservation; fixture payload,
automatic-cycle/rotation and repeated update/provision/retirement acceptance.
No reset, merge, production strict, quiet, repair or APPLY clearance is given.

## Requested outcome

Make the retained development cluster useful for storage testing: VPS backup
copies, member NAS roots, short automatic snapshot/backup scheduling, and
dedicated fixtures proving actual full and incremental payload preservation.
Preserve the user's existing VPS, files, snapshots, disks, source retention,
namespace/maps and personal resource assignments. No reset is authorized.

The provider owns the default-off storage profile and a small test-config
overlay. Production site hooks are behavioral references, not imported runtime
configuration. API scheduler/Plan support is a separately reviewed prerequisite.

## Review selection

HIGH risk: retained guest disks, boot-time writer holds, package compatibility,
seed preservation, physical provisioning, nested-chain rollback and scheduling.
All four lanes apply: general; architecture/repetition; scope/proportionality;
risk/compatibility. Use retained reviewer0, review purpose, read-only,
GPT-6.1 Sol/xhigh, without model or effort overrides. Reverify the same-session
roster and independence when assigning the completed packet.

## Source and history

Worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/vpsfree-dev-workspace-storage-profile`.

Branch: `2026-09-23-storage-redesign-storage-profile`.
Fetched base: `c56f981a950ab763b71dc91c59e8b5256d478851`.
Original reviewed head: `59f1d0999ec61546383668cbef219d24127634cb`.
Original reviewed tree: `ccd8f1351f756938ce4b9fa57f9d23bf8d48557e`.
Tracked tree/index and untracked status are clean. Fresh SSH master fetch
confirmed the assigned base unchanged.

Complete committed inventory:

1. `da058353ac4a43f08313d02b485c1578f3547378` — one generated canonical
   runtime-input update to reviewed/published generic `2b67af62`; flake source
   and lock only, four changed dependency leaves.
2. `8613c8da74677ff3110f1775ca1ebd530d77ad5e` — typed retained-services
   maintenance boot/copy/restart with exact evidence, writer masks, durable hold,
   receipt, disk preservation, adoption checks, focused tests and owning README.
3. `50e45ae5bf787aed661345aab2dd0151747acaff` — enabled preserving seed,
   profile/hooks/provisioning and fixed payload fixture: 16-path functional commit.
4. `59f1d0999ec61546383668cbef219d24127634cb` — native retained-services
   maintenance fixture and explicit app: 3-path commit. `flake.nix` is the sole path shared by these two inventories.

The complete final diff has 25 paths, 4991 additions and 64 deletions relative
to `c56f981a`. Complete binary patch SHA256:
`60694b6e655dc55b70a3b5cb8b4a8e1b150d1d11e671a9fc8c5611fed24ce4da`.
The last two commits divide 18 distinct files without changing the tested
source bytes; `flake.nix` is shared by their inventories. The source profile and its fixed payload
wrapper share normal-chain provisioning and must ship together; the explicit
retained-boot test is independently reviewable and remains a separate commit.
The old instruction-extension tree is retained and excluded from this branch.
No provider migrations or database schema conversion are present in either
the complete committed range or final tree. The feature uses existing
models/chains and adds a version-1 private hold and generated profile contract
while retaining outer cluster schema 1 under canonical transition policy 3. Obtain an explicit final whole-history/no-migrations
conclusion, including any superseded or unused approach found during review.

## Companion interfaces and compatibility

- API support: published `46b3bf6f9549eaf579053bc296ebf19c417bb848`, base
  `878a0d10c86060ed2ce62027223832371ca5e49e`. Whole 21-commit review plus
  direct numeric-schedule remediation is recorded in the
  [Admin review](storage-profile-admin-review.md). Its two consumed migrations
  and core schema are unchanged; the new scheduler/Plan support has no migration.
- Generic runtime: published `2b67af62b40149e7554bab0c31b139cd52c963c1`, base
  `4bec20165387d567b761e43b11fdeabb096618d7`. Schema 1/policy 3, with no
  host algorithm change; [runtime review](storage-profile-runtime-review.md).
  Ordinary package selection of policy 2 is refused with any registered cluster
  state. Old candidate/store recovery is outside the supported procedure.
- Default provider API input stays `5c76e329`. Enabled smoke/runtime uses the
  explicit same-session API source override; disabled checks keep the old pin.
- Provider's default OS input is `15802517e`; its API input follows that OS.
  The selected retained-cluster OS is separately `8d05dc3ae`, whose OSVM already
  accepts per-start kernel parameters. Inspect the actual default and selected
  graphs; a path source label does not change a Nix input by itself. No OSVM or
  Node wire change is required. Selected React remains unchanged at `aa2f60b8`.

Require actual preserving-seed selection and matching marker, not Git labels or
an enable flag alone. Host and tools must consume the same canonical contract.
The input export was compared byte-for-byte; assembled-package proof is pending.
Normal old services boot is unsuitable because the old seed rewrites retained
assignments. The reviewed maintenance path is the prerequisite for actual boot.

Retirement keeps the enabled preserving overlay with boolean
`storageProfile.enrollment:false`. Verify that its static seed removes only the
owned future default link, never re-creates it or rewrites existing allocations,
and that direct add/verify and provision refuse while unregister still works.
The CLI must compare desired and actual loaded enrollment after services
replacement; a new inspection process alone does not establish worker restart.
No disabled legacy-seed restart or persisted retirement engine is supported.

## Quick evidence so far

Maintenance held bytes passed four independent Ruby processes in the pinned
provider shell: 97 tests, 1021 assertions, zero failures/errors/skips, 392 seconds.
Breakdown: maintenance 13/112, runner 10/27, commands 23/295, status 51/587.
Log: `/tmp/storage-maintenance-parser-check.TlJqs6sb/tests.log`.
Syntax, shell parsing, scoped whitespace and pinned Nix formatting passed.
Normal pinned Git commit preserved tested hashes; no hook framework is declared.

Earlier loader failure ran zero examples; pinned bundled-gem isolation fixed
the environment. The first actual maintenance run exposed a parser/update
boundary error, corrected before the passing batch. These attempts are retained
in state, not counted as passing verification.

The first enabled helper/seed slice passed provider 3 tests/23 assertions.
Its real-AR file reached 16 examples: 15 passed before the configuration-savepoint
correction, then both affected default/frozen examples passed 2/0 on corrected
bytes. This covers the current 16 cases; it is not a fresh single 16/0 run.
Actual static-seed preservation, nested confirmation ownership and staging
failure cases are included. Held manifest:
`/tmp/storage-profile-helper-atomic-defaults.sha256`; focused log:
`/tmp/storage-profile-atomic-check.0WnkJgKi/run.log`.
Retain the earlier loader/query/atomic failures in state.

Provision/CLI integration and both fixture sources are complete. The active/retired Nix smoke passed; real guest and payload results and final
independent review remain pending. The README has been reconciled with exact retention targets, preservation,
retirement, fixed fixture commands and failure handling under the writing skill. Reconcile any later helper drift with the tested
hashes. No guest or populated-cluster result follows from these AR/host fixtures.

Current 13-path semantic checkpoint includes durable retirement and command
orchestration: provider 4 tests/32 assertions, six selected CLI cases/71
assertions, and a fresh complete 22-example AR run/0 failures. Manifest
`/tmp/storage-profile-retirement.sha256`, SHA256
`546007a47efd041cf4c276902dab5c97cc841e3fc8b751a1f641f018f86f8117`;
AR log `/tmp/storage-profile-retirement-api.odsx_28j/run.log`.
Held hashes matched and disposable DB stopped. Earlier omitted runtime-contract
environment and extra `.` invocation failures are recorded in state; they do
not certify broader API tests or demonstrate a profile fix. Enabled Nix smoke,
final fixtures and complete-series review remain pending.

A later retirement guard rejects any remaining shared template outside the
exact configured source/NAS pools. The focused atomic-refusal example passed
1/0 in 46 seconds after correcting its setup to persisted task column names.
Log: `/tmp/storage-profile-api-spec.J0TZ8R/run.log`; helper SHA256
`6c039b21f89bb186b16d0974ad65de1f0231d571a092e94074946e7f3a0a5356`,
spec `8cf172dba8826e80613607639bfd51e81ad669df62d9ac6d924779b8a2d11077`.
This is focused coverage after the 22-example checkpoint, not a fresh 23/0 run.

The final 18-path snapshot reached its first no-VM Nix smoke, which failed
before configuration evaluation with a duplicate dynamic app system attribute.
The app grouping was corrected and the subsequent fresh smoke passed; no VM was launched.
Log: `/tmp/storage-profile-smoke-20261002/command1.log`.


## Original reviewed source and quick verification

The verified final committed tree after app grouping is
`ccd8f1351f756938ce4b9fa57f9d23bf8d48557e`. Complete source manifest:
`/tmp/storage-profile-complete-staged.sha256`, digest
`44accac189fb16ae10b85cb1d4af6a356f54252cb129cd2831c77d1eb7d15931`.
The profile commit tree is `804d755ba4c537927cd94788a42e6e31e83baeb1`;
the second three-path commit adds the retained-services test and app. All inputs
and the lock are unchanged by these functional slices.

Syntax passed for 11 Ruby files, two shell files and four Nix files. Targeted
new Ruby Layout/Style/Lint checked nine files with zero offenses. Existing
command/smoke files have unrelated baseline lint offenses; those lines are
unchanged. These checks do not establish guest masks, transport, payload or
retained-boot preservation.

The payload fixture uses normal User/VPS/Dataset/Snapshot/Transfer/Backup and
UseClone chains, writes only newly validated fixture objects, and cleans only
its own returned clone through FreeClone/RemoveClone confirmations. Review its
scoped PurgeClones subclass and actual persisted STI boundary; no global sweep
is intended. No live payload fixture has been executed.

The retained fixture uses the real pinned TestRunner framework through its
constructor-only sealed-config adapter, one defined example and one mutable
services registry. Review authoritative example/result checks and cleanup,
actual generator evidence, exact copied descriptors on both attempts, and the
honest `starting_copied` endpoint. No Node refresh or release is simulated.
Its app is explicit and excluded from ordinary quick checks.

The immediate workspace package consumer is the registered `workspace` tree,
now clean at actual pin-change base `508064ed951e5efc78131dd09d006586280d9285`.
Its old unmerged instruction/pin head `3f539b0` is backed up; none of that
superseded payload was replayed. Current provider input remains `c56f981a`.
A single generated reviewed-provider pin and exact composed host/tools contract
proof follow publication; no default integration or package activation is
claimed by this preparation.

## Original final no-VM result and normal commits

The fresh grouped-app batch passed all three commands: enabled-profile smoke,
explicit maintenance program-path evaluation and pinned `nixfmt --check` on
all four Nix paths. Smoke evaluated bridge/local defaults and overrides,
React enable/refusal behavior, actual enabled and retired storage services
closures/markers, invalid enrollment and missing-storage-topology refusals;
both provider runners built and loaded. Log:
`/tmp/storage-profile-watch.CnNXmd/1-nix-run.log`.
App evaluation resolved
`/nix/store/mb0npawpipqvv4zzc8c4rnpyxkpn8qa3-devcluster-maintenance-check/bin/devcluster-maintenance-check`.
It was not executed. All 18 manifest hashes and the staged tree were unchanged;
no operation remains. The watcher could not recover exact elapsed times from
the yielded handles, so none is inferred.

Normal pinned Nix/Git commits created `50e45ae5` and `59f1d099`. The prepared
index split preserved the verified trees exactly; no source changes or hook
bypass were used. Provider has no declared hook framework, no `core.hooksPath`
and only sample default hooks. Commit messages describe behavior and rationale;
checks remain in these records. Final whitespace and clean-tree checks passed.

The lead found no superseded committed approach or transitional migration in
the inventory; source draft corrections were folded into these functional
commits. Require the reviewer's independent complete-history/no-migrations
conclusion rather than treating this inventory as clearance. The four provider
commits remain unmerged, unreleased and undeployed. The corrected feature head
was published over SSH; default master remains `c56f981a`. Host/AR fixtures
have consumed source behavior; no live provider profile/hold or migration
transition has been deployed by this slice.

## Per-commit path inventories

### `da058353ac4a43f08313d02b485c1578f3547378`

```text
flake.lock
flake.nix
```

### `8613c8da74677ff3110f1775ca1ebd530d77ad5e`

```text
dev-clusters/lib/devcluster_runner.rb
dev-clusters/vpsadmin/README.md
dev-clusters/vpsadmin/bin/devcluster
dev-clusters/vpsadmin/lib/devcluster-runner.rb
dev-clusters/vpsadmin/lib/maintenance.rb
flake.nix
test/devcluster_commands_test.rb
test/devcluster_maintenance_test.rb
test/devcluster_runner_test.rb
test/devcluster_status_test.rb
```

### `50e45ae5bf787aed661345aab2dd0151747acaff`

```text
dev-clusters/vpsadmin/README.md
dev-clusters/vpsadmin/bin/devcluster
dev-clusters/vpsadmin/lib/storage_profile.rb
dev-clusters/vpsadmin/nix/storage-profile-provision.rb
dev-clusters/vpsadmin/nix/storage-profile.nix
dev-clusters/vpsadmin/nix/storage-profile/config.rb
dev-clusters/vpsadmin/nix/storage-profile/dataset_plans.rb
dev-clusters/vpsadmin/nix/storage-profile/hooks.rb
dev-clusters/vpsadmin/nix/test.nix
dev-clusters/vpsadmin/tests/run-storage-profile-api-specs.sh
dev-clusters/vpsadmin/tests/storage-profile-acceptance.rb
flake.nix
test/devcluster_commands_test.rb
test/devcluster_nix_smoke.rb
test/devcluster_storage_profile_test.rb
test/vpsadmin_storage_profile_spec.rb
```

### `59f1d0999ec61546383668cbef219d24127634cb`

```text
flake.nix
nix/tests/retained-services-maintenance.nix
test/retained-services-maintenance/devcluster-runner.rb
```

## Required next gates

After final quick verification, normal commits and this independent review:

1. Existing `nix build --no-link --print-build-logs .#host-migration-test`, required
   by provider AGENTS for the changed upstream host-state compatibility contract.
2. The planned retained-services regression: old seed/writers masked from boot,
   deliberately altered allocations preserved, copy/interruption handling and
   exact new preserving boot. It has a different purpose from host migration.
3. Exact composed package/source/contract checks and supported activation.
4. Retained cluster provisioning/catch-up and real fixture A/S1/full then
   B/S2/incremental destination payload checks, automatic cycle, fixture-only
   retention and repeated services-update preservation.

No default merge, production/shared deployment, dataset cleanup, strict mode,
identity publication, physical quiet, repair readiness or APPLY is authorized.

## Corrected published head and required VM evidence

Current head `f36f15d79f92b50fd37ead32481d7fd7bd628286`, tree
`444248213740404522864493afca3408b130fb9e`: four coherent commits, 25 final
paths, 5176 additions/64 deletions. Full binary diff SHA256
`37a86f215074cf27ea866b05e1881e49b03a8c8048b80d715bb75831619f7189`.
The first two commits and retained-services fixture are patch-equivalent; only
the owning profile commit contains the requested two-file correction. Backup
`backup/2026-09-23-storage-redesign-provider-before-sti-fix` retains `59f1d099`.

The required host-migration target passed exit 0 on this exact clean head/tree
in 5m34s, 19:53:16–19:58:50 UTC. Private logs:
`/tmp/storage-profile-host-migration.r4JiK7/command.log` and `output.log`.
The test script and QEMU cleanup completed; no local Linux kernel build or
owned process remained. This covers the existing host-state compatibility VM;
it does not prove retained services masking, seed preservation or payloads.

Exact-head Check run `37057284522` failed at Nix evaluation before its smoke
step: disabled `mkIf false` still declares unknown
`vpsadmin.api.scheduler.taskRefreshInterval` against the unchanged default API
`5c76e329`. Failed evidence is retained at
`/tmp/storage-profile-provider-ci.b0U1wyHf/failed.log`. Implementer0 owns a
bounded definition fix; architect0 is checking the explicit app's default-pin
contract. No blind rerun, default-pin update or runtime-failure claim is made.

The clean registered workspace feature was normally rebased from `508064ed`
to committed master `58df04cf76d1bf424dd4cb2a21585708fa38e7d4`. Its two
additional commits are unrelated tracking/notes only; applicable source and
procedures are unchanged. Original `3f539b0` backup and registration remain.
The generated final provider pin is still pending.

The first wiring watcher stopped at session lookup before inspecting source or
running checks: `current` returned no session with both environment markers
absent. The lead immediately reverified the exact slug in the tracking cwd
with `login:false`. A fresh utility uses that verified command-only identity
explicitly; no source or session state changed and no Nix result is inferred
from the failed preflight. The five-path snapshot remains held.

The first bound quick batch failed command 1 (default smoke), exit 1 after
about 6m15s. Default/explicit-disabled bridge and local configs and the enabled
bridge WebUI evaluated, then the invalid WebUI revision case did not contain
its expected error text. The harness discarded captured stderr, so that refusal
is not accepted as the expected validation. Log
`/tmp/storage-profile-ci-wiring.1FDsWkU9/command-1.log`; all five held hashes,
head and index were unchanged, no kernel/QEMU or owned process remained.
Commands 2 and 3 were not run. Implementer0 owns narrow diagnostic correction
and source inspection before a fresh focused check; no guard is relaxed.

The corrected smoke retains the fixed bad-input Nix stderr on an assertion
mismatch. A fresh wrapper-only, one-evaluation diagnostic passed exit 0 in
14.009 seconds on unchanged five-path bytes at `f36f15d7`. The lead inspected
the actual final error: the intended lowercase-source refusal at `test.nix:69`.
Private artifacts: `/tmp/storage-profile-revision-launch-w2__mmmt/run.34_u8swz`.
The original discarded error remains unavailable and its cause is unknown.
The fresh default/API46-profile/default-no-build batch is running; this focused
result alone is not full smoke or retained-services evidence.

The five-path correction will be folded into the two existing owning commits:
profile option omission/disabled smoke, and invocation-time fixture evaluation
with captured selected input sources. Default API/OS pins and the lock stay
unchanged. The new lazy app contract requires affected general,
architecture/repetition and risk/compatibility review after quick verification
and normal folds. The original whole-series review and scope conclusion remain
recorded separately; do not claim a full rereview of the pending head.

## Committed evaluation correction: affected-lane packet

Review `f36f15d79f92b50fd37ead32481d7fd7bd628286` to
`4f75d0642129bf078d6852601ed602f9b4520ac8` in general,
architecture/repetition and risk/compatibility. HIGH risk remains appropriate
because the explicit fixture carries selected host/guest inputs into a later
boot. The previously reviewed scope lane is unchanged. Use the same eligible
retained reviewer0, GPT-6.1 Sol/xhigh/read-only; no overrides or nested review.

The correction has exactly five paths: provider `nix/test.nix`, the existing
smoke, root flake, retained-services fixture Nix and provider README. Disabled
profiles omit the unsupported scheduler leaf; enabled profiles retain refresh
60. The existing smoke covers explicit disabled selection and preserves Nix
stderr for its fixed invalid inputs. The explicit maintenance app now exposes
only lazy fixed fixture configs through `lib.retainedServicesFixtureConfigs`;
on invocation it carries selected source trees, revision metadata and existing
follows into fixed config builds, then passes only built store JSON to the
unchanged native runner. No caller config, fallback, new feature input, pin or
lock change is introduced. Review those actual captured input paths and the
default/compatible consumer graphs, not only the exported app type.

The fresh three-command no-VM batch passed on the exact five hashes now
committed:

- Default `nix run --no-write-lock-file .#devcluster-check`: exit 0, 6m56s.
- Actual API46 override with `.#devcluster-check -- --storage-profile`:
  exit 0, 10m40s.
- Default `nix flake check --no-build --no-write-lock-file --show-trace`:
  exit 0, 11s.

Private logs `/tmp/storage-profile-default-compatible-eval.eueu9z`; no kernel,
QEMU or owned handle remained. The earlier discarded-error failure is retained
above with unknown cause. Current successes are not retroactive diagnosis.

Normal pinned Git folds preserved all five tested hashes and the two STI-fix
hashes. The complete branch remains four commits on `c56f981a`:

1. `da058353ac4a43f08313d02b485c1578f3547378`, unchanged generated input.
2. `8613c8da74677ff3110f1775ca1ebd530d77ad5e`, unchanged maintenance runtime.
3. `530c9b979e7e14d923ebb11e40e5fe48aa38cec3`, profile, still 16 paths.
4. `4f75d0642129bf078d6852601ed602f9b4520ac8`, fixture, now four paths because
   its invocation guidance lives in the existing README.

Final clean tree `6a34e39ce0023948bc399f6bff12f0bb48abdaec`, 25 total paths,
5259 additions/67 deletions, complete binary diff SHA256
`a0248b0423c99825adfd2b4cf0676a85ba3285e39138ab09a9c28700fa38149e`.
Range-diff preserves the first two commits; only the declared two profile and
three fixture paths differ from `f36`. Backup
`backup/2026-09-23-storage-redesign-provider-before-ci-wiring` retains `f36`.
There are no provider migrations or obsolete follow-up commits. Preserve the
original independent whole-history/migration conclusion; explicitly assess any
new history or compatibility issue in this bounded committed delta.

The current workspace consumer is clean at `58df04cf`; its provider pin remains
`c56f981a`. Generated pin/package proof and activation are pending. The required
host-migration pass at `f36` remains evidence for the unchanged host-transition
behavior. Retained-services runtime, full public cluster release and payload
acceptance remain unproved and must not be cleared by this source review.

### Independent affected-lane result

Reviewer0 completed exact `f36..4f75` with saved GPT-6.1 Sol/xhigh/read-only
settings and verified session/head/tree/full diff. No Blocking findings, one
Important across general, architecture and risk: `--no-link` runtime builds
leave the resident/candidate JSON and referenced closures unrooted after each
Nix subprocess. Ordinary concurrent GC can remove the resident during the
candidate build or remove either before native reopen/copy; the later
next-config root does not cover that interval. Root both outputs from their
builds through the native scenario's last use, without putting entries in its
initially empty artifact directory. This is a reliability defect, not an unsafe
hold-release result.

The reviewer found no other Important issue: default option omission, explicit
disabled smoke, input source/metadata/follows handling, fixed JSON/native
boundary and README conform. The complete four-commit order is coherent, the
first two unchanged, no new obsolete approach or migration concern, no provider
migrations. Original scope and whole-series conclusions remain unchanged.

Implementer0 is preparing the direct standard `--out-link` correction in the
owning fixture, with a private root directory outside the empty artifacts.
Focused source/quick verification and a normal owning amend must precede native
app invocation. No full unaffected rereview is required if this meets step 9.
The actual lazy app/selected graph and retained guest have still not run.

The direct root correction uses only normal `--out-link` for the two fixed
builds in a fresh private root directory outside native artifacts. The resident
root exists before candidate construction; neither root is removed by exec,
runner cleanup or failure inspection. No new configuration argument, phase,
cleanup engine or fallback was added. Focused default/compatible app-path and
default no-build checks passed 0/0/0 in 6s/9s/9s; evidence
`/tmp/storage-profile-root-lifetime-eval.S7rXko`. The sole tested fixture Nix
hash is `690f2f63c62a2147bddfb9fa97d4144d393296127c30ac4cd9886ae3e5c6057b`.
The lead inspected the requested lifetime fix directly under step 9.

Normal owning amend and exact-lease SSH publication created
`eee1998c640441061ff5f6d76e379bc706ba81f6`, clean tree
`35fba2731f7e0da92d6cdac29196f2d9dfe8baa5`, still four commits/25 paths,
5264 additions/67 deletions, full binary diff SHA256
`2cab5ba43547a6188ea1f262046bdb4e96695b733e0bf5fb149182e0020685d9`.
Only the tested Nix fixture differs from `4f75`; parent profile/first two
commits and the native runner are unchanged. The prior head is preserved at
`backup/2026-09-23-storage-redesign-provider-before-fixture-roots`. This is a
verified direct remediation, not an independent rereview of `eee1998`.
The explicit native app subsequently exited 1 after 7m30s, before native
execution or guest startup. Its resident output built under the standard
fixture root; the enabled candidate's config-overlay builder failed replacing
copied read-only `hooks.rb`. Evidence:
`/tmp/storage-profile-retained-services-watch.P9e3XA`. Implementer0 owns a
bounded copy-mode correction in the profile builder, followed by actual overlay
realization. This does not change the reviewed overlay or root lifetime
contract. No native preservation result or populated-cluster/package clearance
is inferred.

The copy-mode correction changes only the two profile replacements to
`cp --remove-destination`; ordinary copied fixtures and all selected policy,
marker, inputs and native semantics remain unchanged. Lead source inspection
and actual-overlay realization/file comparisons passed in 52s, evidence
`/tmp/storage-profile-overlay-build.8cDI5F8c`, source SHA256
`88dc4138df4359bc70b6d914bee41ba8940c9e8d7dc70f044fb16a94b379123f`.
Normal owning fold created profile `3a09ebc38425a62e9dadae292a8a83adce6e7234`
and fixture `75fb840bfe6d9f12f26e953ce63c40ff06a828ce`; first two commits and
the fixture patch are identical by range-diff. Clean tree
`b8689b5f2233f63f7da9a7579d1e4f8a528387a6`, still four commits/25 paths,
5264 additions/67 deletions, full binary diff SHA256
`ff81be472d637fe9f51fe48783fd6176c9047f38a9eadbff06b65cd485d3212d`.
Backup `backup/2026-09-23-storage-redesign-provider-before-overlay-copy`
preserves the previous exact head. This is a focused builder defect correction
within the existing reviewed contract, not a new design or full independent
review of the rewritten head. The native retry and all package/populated-cluster
acceptance gates remain pending.

The exact `75fb840` native retry exited 1 after 455s, with both real configs
successfully built/rooted but no guest startup. The fixture entrypoint creates
`test-runner.log` before the constructor repeats the originally-empty artifact
directory check. Implementer0 owns a bounded initialization-order fix; existing
guard, native examples/results, execution and cleanup remain the contract.
Evidence `/tmp/storage-profile-retained-services-retry`. No preserved-data or
public-release result is implied by reaching native execution.

The initializer correction preserves both guards and constructs the fixture
before creating its owned log. Actual main-bootstrap verification passed in
about 14s using the native Ruby/dependencies and sealed fixture JSONs, stopping
before the inherited run body (zero guests, scenario_passed=0). Source SHA256
`eb7046fbf931e6d4ec0529ba7094b395653dc618affcfd6532428c3cc368f509`, evidence
`/tmp/storage-profile-native-bootstrap-launch.mhVJCD24/run.9rnfmbco`.
Normal owning amend/publication created
`78ffa6f028b89af6276efa9678cdbe52f250dda9`, clean tree
`31066a6d271df533eb1db73c353116ff990cd0fd`, four commits/25 paths,
5265 additions/67 deletions, full binary diff SHA256
`bf6e7e3fc5fc6d95379d2b28b55d16292b6351bc6b5f6231da3d165493505da2`.
The first three commits are unchanged; the sole final delta is the verified
initializer order/comment. The prior head remains at
`backup/2026-09-23-storage-redesign-provider-before-fixture-init`.
No new artifact acceptance, framework behavior or cleanup contract is added;
no full independent rereview or physical result is claimed. The native retry
remains pending on this exact source.

The exact `78ffa6f` native retry exited 1 after 680s, with its first disposable
guest booted. The one example failed after 216.23s in stage 1. Parent private
shell-log inspection found MariaDB ERROR 1064 at the namespace mutation's
unquoted `offset` column, in both its assignment and `MIN(offset)` expression.
Implementer0 owns the bounded SQL quoting correction and a focused actual
disposable database check, preserving transaction and native framework semantics.
Evidence `/tmp/storage-profile-retained-services-78.W0DG89VX`; no process remains
and the registered cluster is untouched. No new design or physical acceptance
is inferred from this failure.

The lead directly inspected the one-line quoting fix. Actual API46 automatic
disposable schema PREPARE passed 0/38s with no UPDATE or guest, cleanup complete;
logs `/tmp/storage-profile-prepare-watch.vvTykFkl`. Tested SHA256
`2c63e8c775a3f50cef56f87544ef1e85fe695ac92397e40966b3ed869637915c`.
Normal fixture-owning amend and exact-lease publication created
`3175df09a8e3080947730e25d06c3fb577816a2f`, clean tree
`f710925bb6c9a4d4810022c572ca3b0fef3f3ca3`, four commits/25 paths,
5265 additions/67 deletions, full binary diff SHA256
`9ac69fd487cfb636a7420de54fc8f0b95ae233a42e2ca30794dd563c300f1802`.
First three commits are identical; the sole fixture delta quotes the two
identifier occurrences. Backup before-fixture-sql retains `78ffa6f`. This is
direct focused correction within the reviewed fixture contract, with no new
schema, framework or physical acceptance. The subsequent native retry reached
the refusal recorded below.

The exact `3175df0` native retry exited 1 after 421s, sole example 218.63s at
stage 2. After initial old boot/mutation/projection/stop, the existing inventory
guard refused before masked boot: the actual fixture closure contains
`vpsadmin-rabbitmq-setup.service`, absent from MASKS. Its real API46 module
declares a `multi-user.target` oneshot; this is a fixed-set completeness issue,
not permission to bypass unknown writer/trigger refusal. Architect0 owns the
bounded decision and compatibility record. Hold remained `held`, no candidate
or runner bound. Parent verified no owned QEMU/virtiofs process; artifacts remain.
Original independent review conclusions and physical acceptance limits persist.

Architect0 selected the exact setup-unit mask addition with version/mask policy
1 and runtime policy 3 unchanged. No selected new package or deployed profile
hold requires migration; unknown writer/alias/trigger/activation and copy-only
hold checks stay intact. Focused regression passed 2 runs/21 assertions, then
the current helper validated both exact sealed closures (no guest), exit 0 in
2.119s; logs `/tmp/storage-profile-mq-launch.9vb6wq2l/run.glff8eol`. The prior
utility preflight failure ran zero checks; it is not validation evidence.
Lead directly inspected the two-file original-contract completeness correction.
Normal maintenance-owning fold and exact-lease publication created clean
`1743940f608bf3d450555f5de7f5f7188190d846`, tree
`aab4f03f3e14d9dbb463b88f378d2ad6ef192688`, four commits/25 paths,
5268 additions/67 deletions, full binary diff SHA256
`4d240b67a8564dda20cf92716f1fc492090e0fc9505cd9f3dc6cbed25e199182`.
Generated first commit is unchanged; only maintenance's two tested paths differ,
profile/fixture patches are identical. Backup before-rabbitmq-mask retains
`3175df0`. No new record/phase/interface/framework or full unaffected review is
claimed. Native preservation result remains pending on the exact new head.

The exact `1743940f` native run failed at stage 4 in 544.801s, one example
331.88s, with hold release 0 and source parity 1. Its first post-reboot refusal
assertion submits the old boot token before rebind, so it still matches the
helper's persisted identity. The production caller reads current runner/guest
identity; this fixture assertion must supply the newly observed identity before
rebind and prove old-token rejection after rebind. Implementer0 owns that bounded
correction and an existing identity regression; architect0 is checking its
rationale. Prior mask/generator/status checks and partial-copy refusal completed,
but copied boot and complete preservation remain unproved. No runtime validation
change or expanded contract is proposed. Evidence remains at
`/tmp/storage-profile-native-1743.i0ldpjza`; no path-bound VM process remains.

Architect0 confirms the existing supplied-token boundary. The focused identity
case passed 1 run/19 assertions, zero failures/errors/skips, 0/1.537s with parity,
logs `/tmp/storage-profile-identity-check.ruz8g68p`. Lead inspected the exact
two-path test/fixture correction and normal folds: clean published
`5ee8281b07628de03454068e204c66367a8980dd`, tree
`8922be76e13bccc8603e21ccf020ea266bb42acd`, four commits/25 paths, 5281 additions/
67 deletions, binary diff SHA256
`6791baae87a35abff15bc15a65ec7d0a6fb083bddf870ad1cb0ec9ba1e2e5b0b`.
The first generated commit is unchanged; the profile patch is identical;
maintenance changes only its identity regression and the fixture only its
observed-token assertions. Backup before-fixture-identity retains `1743940f`.
No helper, record, interface or acceptance relaxation is introduced and no full
unaffected rereview is claimed. The exact-head native retry remains pending.

That native retry failed at stage 6, 1/644.558s, one example 437.03s, after
copy completion and first copied boot/seed barrier. The terminal public-command
logs show QEMU unable to connect to the vpsadmin virtiofs socket and a matching
daemon pid-lock error; the top stream error is secondary. The pinned OSVM
restart path has a five-second settle guard, which fresh fixture instances
lose. Architect0 selected a fixture-local monotonic stop timestamp after
successful teardown and only the remaining five-second gap before replacement
start. Focused no-guest timing verification and the existing native gate remain.
No OSVM/record/public contract change or cleanup engine is proposed. The hold
remains `starting_copied`, release 0, and full preservation
acceptance remains pending. Evidence `/tmp/storage-profile-native-5ee.uvtsral8`.

The direct fixture lifecycle correction passed a real-main no-guest timing
probe: exit 0/23.127s, five checks, zero guests/scenario runs, startup failure
propagation 1, parity 1. Lead inspected the successful common stop/kill tail
and seven-line monotonic timestamp/remaining-five-second change. Normal owning
amend/publication produced `563c5255a5f08797640be8d9375705011bd15eb2`, tree
`011f51a9b1a403369cba6ea29c08384a0af05773`, first three owners unchanged;
four commits/25 paths, 5288 additions/67 deletions, binary diff SHA256
`ad0c274110a74229e84e1d13d441bd74935339060f8a910b5e4b88b3f20e450e`.
Backup before-fixture-settle preserves `5ee8281b`. This restores the pinned
lifecycle constraint without changing OSVM, masks, persisted state or public
contracts. Original independent review and direct-remediation lineage remain;
no full unaffected rereview or physical acceptance is inferred. The exact-head
native retry remains pending at `/tmp/storage-profile-native-563.zugxbi_7`.

The exact `563c5255` native run failed its final two-start fixture-counter
assertion: 1/774.795s, one example 562.61s, stage 6/release 0/parity 1.
Terminal command order shows successful preserving seed, API/Supervisor, copied
generation and protected projections/payload/old-counter/disk checks before
`new-seed=1` failed the required >=2 assertion. First-barrier instrumentation
is not flushed before the intentional forced power cut. A bounded fixture
observation-durability decision is assigned to architect0 before implementation;
no weakened assertion or production contract change is proposed. Full native
acceptance remains pending; logs `/tmp/storage-profile-native-563.zugxbi_7`.

The approved one-line native `rm && sync -f` correction passed the focused
real-main probe: 0/23.405s, three cases, zero guests/scenarios, both nonzero
command cases prevented kill. No power-loss durability is inferred. Parent
inspected the exact line and normal fixture-only amend/publication:
`45d7ce88fcb3a3d528f59b240c081667666526e3`, tree
`09647aa2044c0da695654038091a45d59a2236a0`, first three owners unchanged,
four commits/25 paths, 5288 additions/67 deletions, full binary diff SHA256
`c6c5e3f789b93f4bef6749b82822cd04e0d8a30098476448f371759d2f7c46b7`.
Backup before-fixture-durability preserves `563c5255`. Original review/direct
fix lineage remains; no OSVM/helper/record/interface or assertion relaxation,
no full unaffected rereview. Actual native result remains pending at
`/tmp/storage-profile-native-45d.g5bgua19`.

The final exact `45d7ce88` native fixture passed: 0/802.973s, sole native
example 611.85s, completed scenario, phase `starting_copied`, hold release 0,
source parity 1. It exercised the original ordered assertions including masks,
old-writer exclusion, real interrupted closure copy, receipt recovery, copied
boot/forced seed retry, >=2 starts and protected rows/payload/disk preservation.
Guest shutdown and parent path-bound process check completed; no QEMU/virtiofs
remains. Evidence `/tmp/storage-profile-native-45d.g5bgua19`. This is native
services-only acceptance; real public Node refresh/release and full/incremental
VPS/NAS fixture payload proof remain separate pending gates. Generated consumer
composition and package proof remain next; no selected package/cluster mutation
or full independent rereview of the direct-fix head is claimed.
