# Storage redesign implementation briefs

## Current workspace correction rebase and integration brief, 2026-10-04

**Scope and authority:** the user explicitly requested “rebase, let's activate
it and merge the fix again”, with the rest of the storage work aside and **no
CI wait**. This authorizes the root workspace correction's activation and
workspace/master integration after verification. It authorizes no new default
integration in generic/provider/Admin/OS, no retained-cluster operation, no
scheduler resume or storage trial. Preserve the existing VPS, disks, files,
namespaces, allocations and stopped-scheduler state. The prior checkpoints
below retain their original dates and evidence; this section governs the
current package-only sequence. [State](state.md) and rollout records remain
lead-owned.

### Current execution checkpoint

**Lead-reported phase: activation verified and workspace/master integration complete.** Normal
provider rebase dropped the upstream-equivalent native commit and retained
exactly the four corrected `0b0ba9d8` blobs in one residual fix:
`cd81e83f91a552eb0138e58cb76312784a2988df` on `e1bb5cf3`, tree
`e038dc276462c0cbc3bacc744390bb63536fb36b`, 540 additions / 4 deletions.
Full-index patch SHA `ae52282070254f1ac108e295360af3ca7a043ee915d3eca911ebfd0a663456b3`
equals `399c3302..0b0ba9d8`. Upstream flakes, generic6a and Codex32775 are
unchanged. Three pinned-Ruby syntax checks and the whitespace check passed.
Prior 47/0 and independent reviews carry through exact corrected-source,
helper, harness and Admin290f parity; no re-review or VM rerun is claimed.
Exact-lease SSH publication/readback completed at cd81, provider master e1bb
is unchanged, and the old0b durable remote backup is retained.

The root URL and generated lock became one normal commit
`1acb207784d31e8891fbc6db95125d2470df6d8d` on `c3124834`, tree
`8effecec401f1a0adb092f01a138e74e695badce`: two flakes, 5 additions / 5 deletions,
full-index patch SHA `429bf72deda410f468bfad2a4b12d05589c0f9a10ce728cb4d23540351f33a70`.
Exactly four provider metadata leaves changed; all other upstream inputs,
defaults and follows remain. Final no-build passed. Feature/old19 backup
readbacks and public comparison capture at base c312/head1acb completed;
root master c312 and historical registration metadata remain unchanged.
The mechanical pin exemption applies, with no new substantive difference.

Two verification launches ran zero checks: the first used the wrong CWD;
the next driver referenced the superseded cfrf command. The stable public
command from the tracking directory passed identity resolution. The fresh
Luna/low watcher using `/home/aither/bin/dev-session` passed exit 0 in
252.856s/parity 1: four existing root checks in 245.712s, default-package build
in 6.836s, and packaged proof exit 0. The parent read all eight equality flags
as 1, schema 1/policy 3/providers 2/profile_loader 1, with generic6a/Codex32775
owner bytes and model catalog matching. Canonical contract SHA remains
`33acdc50fa6b7ed94f84d1f7f1db0af8d76d7d57d2e721cbb6a204a96b27c0d1`.
Built package:
`/nix/store/s7y4bgq7iw0idkv5japb538kfwphk4nf-dev-workspace-0.2.0`;
tools: `/nix/store/q49yi3hizfraywb6d0fwi3drzzlylqjq-vpsfree-dev-workspace-tools-0.1.0`.
No unexpected kernel build or owned handle remains. Package Ruby test logs
retain Git-identity-unknown stderr; all command and suite statuses are zero.
This establishes no cause for the earlier broker failure. Private evidence
`/tmp/storage-workspace-rebase-20261004.6uinnel5/package` remains unread by the
architect. The package was unselected at that preparation checkpoint.

The lead published the normal three-record tracking commit
`fd7d07a41ea7e71c374d19efd06bbfab476a128c`, then replayed the pin onto it as
`86fe8f201ad041bbbb7bfabb6783cc09debde46c`, tree
`3f59ae7c95253b6b2b412aad0f6e557319156fed`. Range-diff is `=`; the exact
`429bf72d` patch, message and both flake hashes (`d2e55a04` / `1562ac96`)
remain unchanged. Root/index are clean and foreign work was untouched.
Final evaluation exited 0 and resolves the **same tested s7y4 package**;
final no-build also exited 0. No extra realization, VM or review is claimed.
Exact-lease feature publication/readback at86fe and public comparison capture
basefd7/head86fe completed, preserving historical registration metadata;
remote master was still fd7 at that checkpoint. Provider cd81 remains the unmerged fix on e1bb,
whose original feature support is already upstream. Private references
`/tmp/storage-workspace-rebase-20261004.6uinnel5/consumer-replay.json` and
`handoff.json` remain unread by the architect.

After the user reported activation and said to proceed, the lead verified
public host status selecting the exact **s7y4 package / q49 tools** above.
Selected-byte proof passed all eight equality flags, schema 1/policy 3/providers
2/profile_loader 1, with active/profile Codex realpaths equal. Four owned core
services are active/running with ExecStart through the selected profile.
Public session identity and retained roster settings passed. Own provider
status exited 0 and reported stale/ready true/bridge, maintenance phase released
and pending false; no refresh, update, storage operation or second switch ran.
This supersedes the earlier nl29/xx5v selection with old provision scripts.

Fetched/shared master fd7 was unchanged, so no rebase or new build was needed.
The lead refreshed public comparison basefd7/head86fe, preserving historical
initial metadata, then normally fast-forwarded shared master to
`86fe8f201ad041bbbb7bfabb6783cc09debde46c`: only two flakes changed, no paths
were staged. Index entries outside those two paths and the complete before/
after dirty status were identical. Normal SSH master publication completed;
exact remote readback confirms **master and feature both at86fe**. Refs and
backups remain. A later tracking-only descendant does not change this source
integration evidence.

The user's workspace/master scope is fulfilled without waiting for CI or
integrating provider/Admin/OS defaults. Selected host proof does not deliver
corrected scripts into the retained services guest. Guest delivery, provision,
payload, scheduler and API trials remain held; the session stays active.
Private evidence `/tmp/storage-workspace-rebase-20261004.6uinnel5/activation`
is referenced only and unread by the architect. These are lead-reported
results, with no architect runtime operation or additional acceptance claim.

### Source decision and smallest commit shape

Public Git inspection confirms the fetched graph:

| Component | Fetched default | Selected source shape |
| --- | --- | --- |
| Generic runtime | `6a972b9ab01077611b2c60e0fc726c185e050315` | None: reviewed `4ef298b3` is already an ancestor; canonical schema 1/policy 3, host switch and transition-spec bytes are retained. |
| Provider | `e1bb5cf3ad37c5ef31445a68ab85f53db2858777` | One admission-fix commit containing exactly the residual `399c3302..0b0ba9d8` four-path patch. |
| Root consumer | `c31248344e4b0a26d94d7fa319406501cc4fc28f` at the supplied shared-master snapshot | One generated provider-pin commit on the actual current shared master, preserving upstream source and coordination work. |

Provider `399c3302` is already an ancestor of `e1bb5cf3`: maintenance,
profile and native-fixture support have entered upstream. Its four residual
fix paths are `dev-clusters/vpsadmin/README.md`,
`dev-clusters/vpsadmin/nix/storage-profile-provision.rb`,
`dev-clusters/vpsadmin/tests/storage-profile-acceptance.rb`, and
`test/vpsadmin_storage_profile_spec.rb` (540 additions / 4 deletions).
The lead confirms each predecessor blob at `e1bb5cf3` equals `399c3302`;
the independently inspected upstream six-path delta touches only root README,
flakes and review-policy skill/test files. There is no overlapping application
edit to resolve. Preserve the old published heads/backups, construct the one
residual fix on `e1bb5cf3`, and retain the already merged history. Do not replay
the old four-commit series or its obsolete generic pin.

The minimum sequence is **provider residual fix, then root generated pin**.
A generic feature replay is unnecessary. Pinning old `0b0ba9d8` directly from
current root would regress the generic runtime and Codex client. Keep generic
`6a972b9a` and current `codex-web`
`32775fa7fdd9bc9b41aef74b7f195e5c3bc0f8d5`; the prior `4c170393` is historical.
Keep current generic `codexModelCatalog` packaging and its matching Go/browser
client, root team-mode checks/catalog/procedures, all follows, ordinary cluster
defaults and Admin/OS/React pins. Root `flake.nix` resolution changes only the
provider URL; the lead generates the lock from the current graph. Expected
lock change is the provider's four metadata leaves, with no transitive input
change because the corrected provider keeps `e1bb5cf3`'s flakes unchanged.
No parallel runtime input or manual old-lock restoration is needed.

The lead owns backups, short Git steps, generated locks, publication,
comparison capture and integration. The implementer owns any necessary
four-path application conflict or URL authoring; an unexpected substantive
conflict returns to the lead rather than broadening this brief. Architect0
owns only this design record. Retained review purpose/model/access are unchanged.

### Verification carried forward and final composition proof

Carry the prior **47/0** real-API correction tests, projection **4/32**, provider
`8f8..0b0b` independent review and consumer `ad..bcb` review as their original
evidence. First compare all four corrected final blobs with `0b0ba9d8` and
confirm unchanged Admin290f/helper/harness dependencies. Record the new complete
one-commit provider history and one-commit root history, with no migrations;
old folded feature history is now upstream, not a new unreviewed replay.
The runtime guard semantics remain the two short SQL admission transactions
and fresh payload identity check documented below, with no physical wait under
the staging transaction.

For this byte-preserving rebase, repeating the 47-example DB run, default and
enabled-profile smoke, Node restore VM, retained-services VM or host-migration
VM is unnecessary. The inspected generic host helper/contract/transition tests
and provider maintenance/runner/native/OSVM inputs are unchanged; upstream
portal naming and team-policy work does not change the host-state migration
interface. Prior VM results retain their limited scope. If a conflict changes
one of those bytes or inputs, rerun only the affected existing check and
reassess its review lane. Do not create a new runtime scenario.

The lead verifies the exact residual patch and generated lock, syntax/whitespace
and no-build evaluation, then records review carry-forward. The already
reviewed identical correction needs no full functional re-review; a genuinely
mechanical root pin is exempt under mandatory-change-review step 1. If the
final comparison reveals a substantive difference, review the affected lanes
on the committed final diff before proceeding. No generic feature review is
needed for consuming its current default.

Use one fresh watcher for the existing four root checks
(`deployment-contract`, `agent-instructions`, `agent-team-policy`,
`cluster-provider-composition`), default-package build and actual packaged
proof. Prove installed provision/acceptance scripts equal the corrected
provider, provider launchers/maintenance/default JSON equal their intended
owners, host/tools canonical contracts equal at schema 1/policy 3, both
providers and profile loader present, and runtime/Codex sources match the
new selected graph. The old `vyf5` build proves the old composition only.
Current root policy checks must remain intact. No CI result or wait is a gate
for this user-directed slice.

### Public activation and workspace-only fast-forward

The initial lead-reported selected package was `cfrf8m`/tools `k5vvj`; the
current checkpoint above supersedes that selection with
`/nix/store/nl29dilg1awgqxmim73d04pizsp5px3j-dev-workspace-0.2.0` and tools
`xx5v`, still carrying the old bare admission check. Earlier public inspection
found the host script equal between nl29 and
`/nix/store/cfrf8mjcww7lks1ylqzgfay5920ab029-dev-workspace-0.2.0/libexec/.workspace-host-wrapped`
and confirmed the existing boundary: `switch` calls `quiesce_sessions` at line 622;
lines 1877–1911 invoke the predecessor's public session quiesce for ready
managed sessions before selecting the candidate. Generic `dev-session`
`quiesce_and_require_idle!` checks both lead-thread and team idleness. The
resolved `~/bin` wrapper is not itself evidence of the selected profile; the
lead must use the current public selected-generation/status result.

After final publication/comparison and package proof, leave the team idle for
the operator's ordinary public `workspace-host switch --source` of the exact
reviewed root worktree. An active lead cannot perform its own idle handoff.
Do not use `--from-candidate`, force, private helpers, delayed switching,
session stop/archive or an unselected provider runner. A refusal leaves the
selection unproved; recover through the supported forward switch, retaining
maintenance-aware provider and policy at least 3. No downgrade or cluster
reset is a recovery step.

After the operator reports activation, the lead verifies public host/package
selection, same-session current/team commands, own stable service bindings and
installed corrected script/contract/default bytes. A public provider status
read may confirm ownership/current reported state; it must not start, update,
release or provision the cluster. Preserve any unrelated selected-generation
change rather than assuming yesterday's package remains active.

Then capture the exact final workspace comparison and fast-forward shared
master with ordinary hooks/SSH, preserving foreign work/index and all feature
refs. Today's explicit approval covers this workspace/master fix. If master
advances only through coordination, rebase the single pin, prove patch/config
equivalence and compare the final default output with the activated output.
An equal output carries the built/activation proof; a different output needs
the existing package/byte-equivalence proof before integration, with no new
storage VM or automatic reactivation. Any substantive source/default change
returns to the lead. Publish/read back the exact root master and retain a
reachable published provider dependency; generic is already on its default.
Do not integrate the provider correction or any other default in this task.

**Current status:** provider correction and root pin are published; final
package proof is pending as reported above. The architect only reconciled
this design record from supplied evidence. Package activation and workspace
integration remain pending; retained-cluster delivery/provision and API CI
diagnosis remain separate, held work.

## Current storage-profile contract, 2026-10-02

The user has said **Implement the plan**, selected five-minute snapshots and
ten-minute backups, and approved normal later snapshot rotation for the
existing VPS under its unchanged retention settings. This section is the
accepted implementation and verification contract. It supersedes the earlier
daily/every-minute/comma-list proposals and the reset authority in the
historical rebase brief below. **Preserve the current cluster, user-created
VPS, files, disks, namespaces and existing resource allocations. No reset.**

This slice adds a reusable, explicitly enabled development storage profile.
It does not enable production strict dispatch, node quiet, repair readiness,
identity publication or reconciliation APPLY. The scheduler change supplies
interval syntax and refresh configuration; it does not redesign backup
scheduling or retention safety. Existing unsigned observer 5204 and ordinary
5215 wire behavior remain supported. No new Node protocol or database
migration is required. Preserve consumed migrations `20260924210000` and
`20260926100000`, including their contents and bootstrap behavior.

Read this section for implementation decisions; [plan](plan.md) and
[state](state.md) remain lead-owned sequence/results. The broader storage
architecture remains in [storage-integrity-design.md](storage-integrity-design.md).
The historical brief records the preceding successful rebase/React trial,
including failures and limits; it is not an instruction to repeat that trial.
Current source baseline: vpsAdmin `e65a5a6b`, OS `8d05dc3ae`, configuration
`5eff558c4`, React `aa2f60b8`. These are source references, not claims that the
new profile is implemented, reviewed or deployed.

Latest lead-reported preflight: the cluster is stopped with stale status and
services SSH has no route. Retain its disks. The new provider worktree
`vpsfree-dev-workspace-storage-profile` starts clean at current default
`c56f981a950ab763b71dc91c59e8b5256d478851`, matching the installed provider
source. The earlier `074` default was stale; the old `dcb` branch is retained
untouched and is not the implementation base. These are lead-reported facts;
the architect performed no host/cluster check.

### Current execution checkpoint, 2026-10-03

Current phase: workspace activation is verified and workspace/master
integration is complete under the user's conditional approval. Continue the
original storage work separately. The completed rebase of the generic runtime,
provider and consumer is covered by the bounded
[rebase and early-merge brief](#current-rebase-and-early-merge-brief-2026-10-03)
below. Previous `492fdf8e` review/build evidence
is retained for that composition; it does not prove the replacement package.
The lead reports generic/provider publication at `4ef298b3` / `399c3302` and
the completed clean root rebase/pin `6d1b9c4d` on `93389c3`. The six-stage
quick batch passed all six stages. Retained `reviewer0` cleared the actual
three-repository composition/history in all four HIGH lanes without findings.
The final root checks, package realization and source-contract/Codex-client
proof passed at exact `6d1b9c4d`. The lead confirms root feature publication
and public capture-comparison are complete at base `93389c3` / head
`6d1b9c4d`, with remote master unchanged at that checkpoint. The user now
reports activation and conditionally authorizes workspace/master integration
after the lead verifies it. The lead reports successful installed public
activation checks and final pin replay `1fa9c982b866a305bd1451f2c32f6d387d2dc1a3`
on tracking-only master `3fd3ff77`. Final package evaluation equals the exact
active output; no rebuild or reactivation was needed. Final comparison,
feature publication, shared-root fast-forward and remote master push completed.
The pin remains an ancestor of concurrent tracking-only local master
`4123553c1ae1fc47767e9b30445ff4f7f79266e9`; foreign work was preserved.
Prior zero-check attempts remain distinct, and
unchanged host/native evidence is retained without calling it a rerun.
The separate API46 failure is diagnosed as an existing Node daemon/restart
fixture reliability issue; its broker-timeout trigger remains unknown. It
limits broader storage acceptance, not this default-disabled package rebase.
The lead now reports successful public maintenance-start, a private logical DB
backup and read-only catalog/entitlement baseline, and services copy-only.
Public copied stop/start completed with real seed/services/regular-node refresh
and hold release. All three ordinary Node updates and bounded process/source
binding checks passed. Protected DB projections were preserved, and a known
ordinary file plus four quota properties matched across Node updates; this is
not pre-seed or user-payload equality. Normal public profile provision failed
before Pool/CatchUp staging: its initial admission check lacked a SQL staging
transaction. The scheduler remains intentionally stopped; no retry, unlock or
reset follows. The bounded
[provider admission remediation](#provider-provision-admission-remediation-2026-10-03)
below takes priority and includes the installed-package correction boundary.
Payload acceptance and retirement remain pending. The lead accepted the bounded
provider brief and released its four owned implementation paths; no operation
or runtime acceptance follows from that release.
Exact-head API core/full-platform CI diagnosis identified two unexpected 500s
without the underlying exception. The bounded
[test-only diagnostic brief](#api-platform-request-exception-diagnostic-brief-2026-10-03)
below preserves the source hold: application authoring awaits the lead's release.
No cause or runtime correction for the API 500s is established. Exact
Admin `290f1ef0`, installed provider `399c3302` and selected `zmwh` remain the
runtime baseline; Admin source and the separate CI observer remain held;
the Node review/direct remediation and integration pass are recorded below. The
conditional approval covers only workspace/master, with the bounded checks
and integration sequence below. Generic/provider default integration,
production storage deployment and quiet/repair/APPLY remain excluded.
Detailed lead-reported results and prior evidence follow; operation records
remain in [state](state.md).

- vpsAdmin whole-branch review `878a0d10..2323829c` covered four HIGH lanes,
  21 commits and both consumed migrations. Its one Important finding was
  comparing a validated numeric DSL schedule with its persisted string. The
  bounded `.to_s` correction and four legacy/keep-empty group/backup DB
  regressions passed the eight-example check with zero failures in 45 seconds;
  the lead reports all three held file hashes matched. Normal hooks and the
  owning Plan amend produced `46b3bf6f9549eaf579053bc296ebf19c417bb848`,
  SSH-published with the exact `e65` lease; default `878a0d10` is unchanged.
  This is the direct step-9 correction; no full review rerun is required.
  The lead observed exact API46 CI run `37030949457` complete successfully
  with 27/27 jobs; latest broad-run `37030949481` metadata is `in_progress`,
  updated `2026-10-02T19:10:57Z`, replacing the earlier queued status. These
  are bounded lead-observed GitHub metadata, not an architect rerun or
  completed broad CI. The lead's latest short query still reports broad CI
  in progress with no failed-job metadata; the 27/27 topic result is unchanged.
- Generic policy-3 prerequisite `2b67af62` is published. Provider commit
  `da058353ac4a43f08313d02b485c1578f3547378` pins that input; unrelated lock
  nodes are unchanged. The tested ten-path maintenance implementation is now
  normally committed as `8613c8da74677ff3110f1775ca1ebd530d77ad5e`; the lead
  reports a clean tree at that commit before releasing the profile slice.
- Its first test invocation ran zero examples because inherited Minitest 6
  shadowed bundled 5.25. After isolating gems through `Gem.default_dir`, the
  actual maintenance suite ran 13 tests / 105 assertions with one phase-update
  error: duplicate-key parsing left `UniqueHash` in mutable state. The bounded
  conversion after parsing and README isolation instructions were then checked
  in four separate processes: maintenance 13/112, runner 10/27, commands
  23/295 and status 51/587 (tests/assertions), totaling 97 tests / 1021
  assertions in 392 seconds, with zero failures, errors or skips. The held
  `b054…` manifest was unchanged. Commands took 319 seconds and status 72;
  both completed normally without timeout or retry.
- The enabled profile, preserving seed and helper were developed on
  `8613c8da`. Their approved source scope includes
  `nix/storage-profile.nix`, `lib/storage_profile.rb`, profile config/hooks/
  plans/provisioning, provider fixtures, a real API/ActiveRecord harness and
  payload acceptance fixture, plus the existing provider Nix/CLI/README/
  flake/smoke/command integration paths. All application ownership remains
  with the implementer. Pre-API preservation and default-package setup must
  not wait for Node chains. Templates requiring NAS/source Pool IDs follow
  post-readiness `Pool::Create`, before enrollment; no fake DIP or readiness
  is permitted. Run the final independent whole-provider review after all
  intended commits and before both the existing host-migration test and the
  retained-services VM trial; no extra intermediate review gate is added.
- Lead-reported profile checks now pass: pure 4 tests / 32 assertions,
  CLI 6 tests / 71 assertions, and the exact AR selection 22 examples /
  0 failures. Earlier AR evidence remains distinct: the initial 15-example
  run had 9 passes / 6 failures (NAS ancestry lookup and spec handle-query
  corrections); another invocation accidentally selected thousands of API
  resource examples and was stopped/diagnosed, not accepted. The new
  foreign-Pool retirement refusal is being checked separately and is not
  included in this acceptance evidence. These focused results do not complete
  the final independent whole-provider review or VM gates.
- The initial staged implementer manifest reconciled to 18 unique paths: the
  16-path profile and 3-path native retained-fixture inventories overlap only in
  `flake.nix`, with no missing or extra path. The original normal pinned-Git
  commits were `50e45ae5bf787aed661345aab2dd0151747acaff` (16 profile paths) and
  `59f1d0999ec61546383668cbef219d24127634cb` (3 retained-fixture paths).
  The source was clean at the latter commit; the direct correction below now
  supersedes those two heads. Default input pins and the lock are unchanged
  by these commits and the correction.
- The first no-VM smoke command exited 1 after seven seconds,
  before configuration evaluation: duplicate dynamic `apps.${system}`
  declarations at `flake.nix:234,238`. All 18 held hashes and tree `f692…`
  were unchanged. Command 2 (wiring) and command 3 (formatters) did not run.
  The implementer was released only to group both apps under one dynamic
  attribute set and update the split artifacts, then repeat the same batch.
  Evidence is in the lead-owned `/tmp/storage-profile-smoke-20261002/command1.log`.
  This was a source-wiring failure, not seed/runtime failure or acceptance;
  no VM, kernel or cluster action occurred.
- After grouping both apps, the lead observed all three commands in the
  repeated no-VM batch exit 0: actual enabled/retired configuration closures
  and preserving markers, invalid selections/refusals, both provider runners
  built and loaded, maintenance app-path evaluation, and four Nixfmt checks.
  The app evaluated to
  `/nix/store/mb0npawpipqvv4zzc8c4rnpyxkpn8qa3-devcluster-maintenance-check/bin/devcluster-maintenance-check`
  but was **not executed**. All 18 hashes matched final manifest `44accac…`
  and tree `ccd8f135…` remained unchanged. Lead-owned evidence is
  `/tmp/storage-profile-watch.CnNXmd/1-nix-run.log`; exact elapsed time is
  unavailable. These are lead-reported source/evaluation results, not an
  architect rerun or VM/physical-payload proof.
- The lead reports reviewer0 completed the whole-provider review of
  `c56f981a..59f1d099` with saved Sol/xhigh/read-only settings across all four
  HIGH lanes. The reviewer inspected all four commits and 25 paths; the full
  diff hash matched the packet. History was coherent, with no obsolete
  committed iteration or migrations. There were no Blocking findings, one
  Important finding and no additional Important findings; the scope lane
  found none. In profile commit `50e45ae5`, the normal AR STI `CatchUp` class
  was defined lazily only by the provisioner's `catch_up_chain`, preventing
  fresh API, Supervisor and database-task readers from instantiating persisted
  nonempty or terminal chains.
- The lead reports the direct eager-loader correction's fresh-reader real-DB
  diagnostic passed 1 example / 0 failures, exit 0 in 40 seconds at API46;
  evidence is `/tmp/storage-profile-watch.ShenILPS/full.log`. The original
  child run (1 example / 1 failure) remains distinct: its fixture touched
  AR 8.1.4 `DatabaseConfigurations` before `Base` initialization. The fixture
  was corrected to `Base.configurations.resolve` with finite safe diagnostic
  stages; the runtime eager loader was unchanged between runs.
  Normal pinned-Git fixup/autosquash folded the exact two tested files into
  profile commit `23363e98e8db067f66bb7a2cf2bc4f740af3ebb8`; the separate VM
  commit became `f36f15d79f92b50fd37ead32481d7fd7bd628286`. The first two
  commits `da058353` and `8613c8da` are unchanged. Range-diff marks those and
  the VM commit `=`, and only the profile commit `!`, matching the requested
  two-path correction. That clean four-commit tree was
  `444248213740404522864493afca3408b130fb9e`; full binary-diff digest is
  `37a86f215074cf27ea866b05e1881e49b03a8c8048b80d715bb75831619f7189`,
  with 25 paths, 5176 additions and 64 deletions.
  `backup/2026-09-23-storage-redesign-provider-before-sti-fix` retains the
  original reviewed `59f1d099`. Direct mandatory-review step 9 is complete,
  with no new contract, schema or fallback and no unaffected-lane rerun.
  The original `c56f981a..59f1d099` range remains the independent review
  evidence; this does not claim full independent rereview of `f36f15d7`.
- The lead reports the required host-migration check passed at exact
  `f36f15d7` / tree `44424821`: exit 0 in 5 minutes 34 seconds,
  `19:53:16–19:58:50 UTC`, under fresh Luna/low watcher
  `storage_profile_host_migration`. Its private artifact root
  `/tmp/storage-profile-host-migration.r4JiK7` was not inspected by the architect.
  The provider feature was SSH-published at exact `f36f15d7`; default
  `c56f981a` is unchanged. This does not complete the separate retained-services
  VM or prove guest seed/payload behavior.
- Provider Check `37057284522` failed the default flake check: API input
  `5c76e329` lacks `api.scheduler.taskRefreshInterval`, and `mkIf false` still
  leaves an unknown option definition. The correction omits that definition
  from the disabled path. Source inspection at `f36f15d7` also found the retained
  app eagerly interpolates `(make true).json` into its wrapper, forcing the
  unsupported enabled configuration during default app evaluation even after
  the disabled-path fix (`nix/tests/retained-services-maintenance.nix:136–168`).
  Recommended bounded correction: keep the same app and native sealed-config
  runner, defer its fixed fixture configurations until explicit invocation,
  and carry the selected existing input overrides through that build. Default
  pins stay unchanged; the enabled fixture still requires compatible API46
  and actual preserving seed/marker, with no alternate input or fallback.
  The lead reports the folded lazy-app implementation uses fixed `lib` fixture
  outputs and invocation-time builds of the selected root sources/follows,
  preserving the native runner/store-JSON interface. Its completed quick batch
  and pending affected-lane review are recorded below. This source/evaluation
  wiring correction is not seed or physical failure evidence and adds no gate.
- A prior default smoke failed after 6 minutes 15 seconds but discarded its
  stderr. Its exact cause cannot be recovered; the later diagnostic does not
  explain that historical failure. The lead reports fresh one-operation
  Luna/low watcher `storage_profile_revision_diagnostic` ran
  `python3 /tmp/storage-profile-revision-launch-w2__mmmt/launch.py` at provider
  HEAD `f36f15d7`: probe exit 0 in 14.009 seconds, all five held hashes
  unchanged and index empty. The parent directly read the final error in
  `/tmp/storage-profile-revision-launch-w2__mmmt/run.34_u8swz`: the actual
  throw at provider `test.nix:69` was `Enabled React WebUI requires a
  40-character lowercase source revision`. This is confirmed final diagnostic
  output, not an inference from a trace snippet. Probe success is not a
  successful configuration evaluation: no full smoke, VM or runner ran, and
  no diagnostic handle remains.
  The lead-reported smoke revision `bdf265…492` retains stderr on the fixed
  invalid-input assertion mismatch.
- The lead reports the fresh three-command batch passed: default smoke in
  6 minutes 56 seconds, actual API46 `--storage-profile` smoke in 10 minutes
  40 seconds, and default `flake check --no-build` in 11 seconds, all exit 0.
  Evidence is under `/tmp/storage-profile-default-compatible-eval.eueu9z`,
  unread by the architect. All five held hashes and the index matched; no
  kernel or QEMU ran and no owned handle remains. Pins are unchanged.
  Normal pinned-Git owning folds produced profile commit
  `530c9b979e7e14d923ebb11e40e5fe48aa38cec3`, followed by fixture commit
  `4f75d0642129bf078d6852601ed602f9b4520ac8`; the first two commits are unchanged.
  The clean four-commit tree is `6a34e39ce0023948bc399f6bff12f0bb48abdaec`,
  with full binary-diff digest
  `a0248b0423c99825adfd2b4cf0676a85ba3285e39138ab09a9c28700fa38149e`.
  Total scope remains 25 paths, now 5259 additions and 67 deletions. The exact
  five tested paths differ from `f36f15d7`; both STI correction hashes remain.
  The fixture commit now owns four paths because its lazy-invocation README
  guidance belongs there; this does not expand the full branch's path scope.
  `backup/2026-09-23-storage-redesign-provider-before-ci-wiring` retains `f36f15d7`.
- The lead reports reviewer0 completed the committed `f36f15d7..4f75d064`
  review in general, architecture and risk lanes using saved Sol/xhigh/read-only
  settings: no Blocking and one Important finding. Invocation-time fixture
  configs built with `--no-link` lack GC roots for their required lifetime.
  The default-option omission, source-input follows and README otherwise
  conform. The affected history remains four coherent commits, with no
  obsolete iteration or migrations; original whole-history/scope evidence is
  unchanged. This changed lazy-app contract received mandatory-review step 10,
  not a full rerun of unaffected lanes. Its direct step-9 correction uses
  standard `--out-link` for both fixed configurations in
  one private mode-0700 root directory outside the initially empty native
  artifact directory; root the resident before building the candidate and
  retain both through the runner's last use and failure evidence. This adds no
  phase, configuration arguments, cleanup engine or lifecycle action.
- The lead directly inspected that correction and reports its one held Nix
  file (`690f…057b`) passed default app-program evaluation in 6 seconds,
  compatible app-program evaluation in 9 seconds and default no-build flake
  check in 9 seconds, all exit 0. Evidence is
  `/tmp/storage-profile-root-lifetime-eval.S7rXko`, unread by the architect.
  Normal pinned-Git fixture-owning amend and exact-lease SSH publication
  produced `eee1998c640441061ff5f6d76e379bc706ba81f6`; parent profile
  `530c9b97` and the first two commits are unchanged. The clean four-commit
  tree is `35fba2731f7e0da92d6cdac29196f2d9dfe8baa5`, with full binary-diff
  digest `2cab5ba43547a6188ea1f262046bdb4e96695b733e0bf5fb149182e0020685d9`;
  scope remains 25 paths, 5264 additions and 67 deletions. The lead's
  `backup/2026-09-23-storage-redesign-provider-before-fixture-roots` retains
  `4f75d064`. Default `c56f981a` is unchanged. The lead directly confirmed
  exact-head Check `37067408291` at `eee1998c` completed successfully;
  API46 broad `37030949481` remains in progress. This CI success proves
  neither enabled-overlay realization nor a native fixture result; the later
  overlay correction has separate evidence below. The
  older failed check is complete, with no cancellation needed. Original
  four-lane review of `59f1d099` plus STI step 9, affected
  `f36f15d7..4f75d064` review plus this root-lifetime step 9, and host-migration
  evidence at `f36f15d7` remain distinct; none claims a full rereview of `eee1998c`.
- The lead reports the actual retained-services app with explicit API46
  override at clean published `eee1998c640441061ff5f6d76e379bc706ba81f6`
  failed: exit 1 after 7 minutes 30 seconds, before the native scenario or
  guest started. The parent directly read stderr under
  `/tmp/storage-profile-retained-services-watch.P9e3XA`; the architect did not
  inspect those artifacts. The app printed fixture Nix roots at
  `/tmp/retained-services-roots.3tKF8UTH`, correcting the watcher's initial
  omission of that evidence. The resident configuration built; candidate
  `vpsadmin-storage-profile-config` realization failed with `cp hooks.rb:
  Permission denied`. The lead's source diagnosis at provider
  `test.nix:365–373` is that read-only store fixture files are copied before
  overwriting hooks/plans. The bounded one-file correction changes only the
  two copies to use `--remove-destination`, without changing store permissions.
- The lead reports four focused actual-overlay steps passed, all exit 0 in
  52 seconds: metadata, only the overlay build, and six-file/source comparisons.
  Evidence is `/tmp/storage-profile-overlay-build.8cDI5F8c`, unread by the
  architect; the held source fingerprint `88dc4138…9123f` was unchanged.
  Normal pinned-Git fold produced profile commit
  `3a09ebc38425a62e9dadae292a8a83adce6e7234` and native-fixture commit
  `75fb840bfe6d9f12f26e953ce63c40ff06a828ce`. The first two commits are unchanged
  and the VM patch is range-diff `=`. The clean four-commit tree is
  `b8689b5f2233f63f7da9a7579d1e4f8a528387a6`, with full binary-diff digest
  `ff81be472d637fe9f51fe48783fd6176c9047f38a9eadbff06b65cd485d3212d`;
  scope stays 25 paths, 5264 additions and 67 deletions. Backup
  `backup/2026-09-23-storage-redesign-provider-before-overlay-copy` retains
  `eee1998c`. Exact-lease SSH publication reached `75fb840b`; freshly fetched
  default `c56f981a` is unchanged. The lead now confirms exact-head Check
  `37069787350` at `75fb840b` completed successfully; old Check `37067408291`
  also completed successfully. This is a direct
  bounded copy-mode correction within the reviewed overlay contract, not a
  new policy or full independent rereview claim.
- The lead reports the fresh-watcher native retry at exact `75fb840b` / API46
  exited 1 after 455 seconds, `2026-10-02 21:59:05Z–22:06:40Z`. Evidence is
  under `/tmp/storage-profile-retained-services-retry`, unread by the architect.
  Both actual resident and candidate configurations built with the corrected
  overlay under `/tmp/retained-services-roots.2UtogfhJ`. The runner started,
  but no guest did: the private-empty-artifact guard at `constructor.rb:35`
  failed. The lead's public-source diagnosis is that the entrypoint validates
  the private empty directory, then creates its own `test-runner.log` through
  `stderr.reopen`, before the constructor repeats the empty check.
  The bounded one-file initialization-order correction preserves the original
  guard and native framework, results and cleanup without expanding accepted
  preexisting artifacts. Its subsequent no-guest check and fold are below.
  The operation exited with clean `75fb840b` / API46 post-run parity, the
  untracked cache preserved and no process remaining, according to the lead.
  The original `eee1998c` copy failure, 52-second overlay pass, previous
  reviews/direct corrections and host-migration evidence remain distinct.
- The lead reports actual no-guest main bootstrap passed, exit 0 in about
  14 seconds, using exact native Ruby/dependencies and sealed configs. Held
  script hash was `eb7046fbf931e6d4ec0529ba7094b395653dc618affcfd6532428c3cc368f509`.
  Execution stopped before the inherited run body: zero guests and
  `scenario_passed=0`. Evidence root
  `/tmp/storage-profile-native-bootstrap-launch.mhVJCD24/run.9rnfmbco` is unread
  by the architect. Normal fixture-owner amend and exact-lease SSH publication
  produced `78ffa6f028b89af6276efa9678cdbe52f250dda9`; the first three commits
  are unchanged, with only the tested initializer order/comment corrected.
  The four-commit tree is `31066a6d271df533eb1db73c353116ff990cd0fd`, 25 paths,
  5265 additions / 67 deletions, binary diff
  `bf6e7e3fc5fc6d95379d2b28b55d16292b6351bc6b5f6231da3d165493505da2`.
  Backup before-fixture-init retains `75fb840b`; freshly fetched default
  `c56f981a` is unchanged. This is no expanded guard/contract or full rereview.
  The lead's metadata query confirms exact `78ffa6f` Check `37072305045`
  completed successfully; prior `75fb840b` / `eee1998c` checks also completed
  successfully, with no superseded live run to cancel. API46 broad
  `37030949481` remains in progress.
  A later utility preflight mistakenly applied the native hash to `flake.nix`,
  ran zero checks/guests and left no handle. The parent rechecked three literal
  paths and assigned a fresh watcher to retry at exact clean `78ffa6f` under
  source hold; log root is `/tmp/storage-profile-retained-services-78.W0DG89VX`.
  The fresh watcher's actual three-path preflight passed before the retry.
- The lead reports that exact `78ffa6f` / API46 retry finished with exit 1
  after 680 seconds. Its sole native example failed after 216.23 seconds at
  stage 1, after the first disposable services guest booted. The parent
  directly located MariaDB `ERROR 1064` in private `services-shell.log:1407`
  under `/tmp/storage-profile-retained-services-78.W0DG89VX`, unread by the
  architect. The fixture's `mutate_retained_fixture!` updates `user_namespaces`
  with unquoted `offset=(SELECT MIN(offset)...)`, which MariaDB rejected as
  invalid syntax. The direct correction quotes two identifiers on that one
  owning Ruby line; no runtime mechanism or broader design is added.
  Lead-reported cleanup completed with
  no owned process remaining and the live session cluster unchanged.
- The lead reports actual API46/schema MariaDB `PREPARE` passed, exit 0 in
  38 seconds: `prepared=1`, `executed=0`, `guest_count=0`, stage 6. Evidence is
  `/tmp/storage-profile-prepare-watch.vvTykFkl`, unread by the architect.
  Held Ruby hash was `2c63e8c775a3f50cef56f87544ef1e85fe695ac92397e40966b3ed869637915c`.
  Normal fixture-owner amend and exact-lease SSH publication produced
  `3175df09a8e3080947730e25d06c3fb577816a2f`, tree
  `f710925bb6c9a4d4810022c572ca3b0fef3f3ca3`. The first three commits are
  unchanged; range-diff contains only the tested SQL-line correction. The
  clean four-commit scope remains 25 paths, 5265 additions / 67 deletions,
  with binary diff `9ac69fd487cfb636a7420de54fc8f0b95ae233a42e2ca30794dd563c300f1802`.
  Backup before-fixture-sql retains `78ffa6f`; freshly fetched default
  `c56f981a` is unchanged. This preparation check does not prove execution of
  the fixture mutation or native acceptance, and no full rereview is claimed.
  Fresh Luna/low watcher `storage_profile_retained_services_3175` ran the
  API46 native app with literal three-path preflight and source/index hold;
  artifact root `/tmp/storage-profile-retained-services-3175.6ka7ukno` remains
  unread by the architect. The lead reports exit 1 after 421 seconds; its
  sole example failed after 218.63 seconds at stage 2. Initial old boot,
  actual SQL mutation/projections and stop passed. `masked_boot!` then
  reached `validate_runner!` / `validate_system!`, which refused with
  `resident has an unsupported application writer` before starting a masked
  guest. Public inventories of both sealed closures contain 365 entries;
  the sole unsupported unit is `vpsadmin-rabbitmq-setup.service`. The complete
  command line with its additional exact mask is lead-reported as 967 bytes,
  below the unchanged 2047-byte bound. The selected source correction is
  limited to the helper's fixed mask and existing maintenance unit tests;
  no changed record version or relaxed unknown-writer refusal is required.
  The failed hold remains `held`, with null runner PID and candidate. The
  parent checked the three owned virtiofs PID files and QEMU/virtiofs
  bindings: no process remains and the live cluster is unchanged. At that
  checkpoint exact `3175df09` CI was reported in progress; prior `78ffa6f`
  succeeded.
- The lead reports focused fixed-mask and inventory tests passed: 2 runs,
  21 assertions, zero errors/failures/skips. The current helper validated
  both exact `3175df09` sealed closures, `validated=1`, `guest_count=0`.
  The fixed launcher exited 0 in 2.119 seconds with `parity=1`; artifacts
  `/tmp/storage-profile-mq-launch.9vb6wq2l/run.glff8eol` remain unread by the
  architect. An earlier fresh utility used the wrong working directory and
  could not establish `current`; it did no work and supplies no verification
  evidence. The parent reverified binding and both held hashes. The fixed
  launcher uses matching literal environment identity with conflict refusal.
  Normal maintenance-owner fold and exact SSH publication produced clean
  `1743940f608bf3d450555f5de7f5f7188190d846`, tree
  `aab4f03f3e14d9dbb463b88f378d2ad6ef192688`. Generated pin `da058353` is
  unchanged; maintenance is `b108c414`, profile `f6b12398` and fixture
  `1743940f`. Profile/fixture patches are identical in range-diff; only the
  two tested maintenance paths changed. The four-commit scope is 25 paths,
  5268 additions / 67 deletions, binary diff
  `4d240b67a8564dda20cf92716f1fc492090e0fc9505cd9f3dc6cbed25e199182`.
  Backup before-rabbitmq-mask retains `3175df09`; freshly fetched default
  `c56f981a` is unchanged. `VERSION=1`, mask policy 1 and runtime policy 3
  remain intact. This directly completes the original bounded hold contract;
  no new persisted mechanism or full rereview is claimed. Fresh Luna/low
  `storage_profile_native_1743` ran the actual API46 app through the
  fixed launcher under source hold; evidence root is
  `/tmp/storage-profile-native-1743.i0ldpjza`, unread by the architect.
  The lead relayed successful launcher preflight and an isolated services
  guest running, with no reported kernel-build indicator. At that startup
  checkpoint the parent's short CI query reported exact-provider run
  `37077660749` and API46 broad `37030949481` both in progress; the architect
  did not poll CI.
- The lead reports the single exact `1743940f` / API46 native run exited 1
  after 544.801 seconds, from 2026-10-02 23:29:49.249 to 23:38:54.051 UTC.
  Its sole example failed after 331.88 seconds at stage 4, `hold_released=0`.
  The parent read `test-runner.log` under the same private artifact root:
  an expected `Maintenance::Invalid` was not raised. Initial old SQL/
  projections, first masked boot with every mask's generator/LoadState/
  inactive checks, old-writer counters and container refusals, partial-copy/
  incomplete refusal/stop, and second masked boot completed before failure.
  These are lead-reported partial results, not full scenario acceptance.
  Public source shows the first stage-4 refusal assertion supplied
  `original_identity` before `bind_boot!(second_identity)`, while the old
  identity still matched the persisted record. The helper checks the supplied
  tuple; the CLI owns fresh runner/guest observation. Correct only the
  fixture to refuse observed `second_identity` before binding, then bind it
  and refuse `original_identity` afterward, before the valid new-identity
  copy. The existing unit regression must retain phase/evidence on refusal.
  No helper, record, version or production behavior changes are needed.
  The failed hold is `copying` with the earlier recorded boot ID; the last
  actual guest boot differs. The lead reports no positively path-bound
  QEMU/virtiofs process remains and the live cluster is unchanged.
- The lead directly read the focused identity unit result: 1 run,
  19 assertions, zero failures/errors/skips. Its launcher exited 0 in
  1.537 seconds with `parity=1`; private evidence
  `/tmp/storage-profile-identity-check.ruz8g68p` is unread by the architect.
  Normal maintenance-test and fixture-owner folds, followed by exact-lease
  SSH publication, produced clean `5ee8281b07628de03454068e204c66367a8980dd`,
  tree `8922be76e13bccc8603e21ccf020ea266bb42acd`. Generated pin `da058353`
  is unchanged; maintenance `683b84eb` contains only the unit-test delta,
  profile `455d89f5` has an identical patch in range-diff, and the native
  fixture changes only the two identity assertions. The four-commit scope
  remains 25 paths, 5281 additions / 67 deletions, binary diff
  `6791baae87a35abff15bc15a65ec7d0a6fb083bddf870ad1cb0ec9ba1e2e5b0b`.
  Backup before-fixture-identity retains `1743940f`; freshly fetched default
  `c56f981a` is unchanged. The lead used normal Git/Nix execution with no
  declared hook framework and no bypass; private fold evidence remains
  unread by the architect. No new contract or full rereview is claimed.
  The lead reports `1743940f` Check `37077660749` succeeded and later confirmed
  exact `5ee8281b` Check `37079212058` completed successfully; all older
  provider runs completed. This is CI evidence, not native acceptance.
  Fresh Luna/low `storage_profile_native_5ee` ran the exact API46
  public app with the fixed identity/parity launcher under source/index hold;
  private root `/tmp/storage-profile-native-5ee.uvtsral8` is unread by the
  architect.
- The lead reports that exact clean `5ee8281b` / API46 run exited 1 after
  644.558 seconds, from 2026-10-02 23:48:43.266 to 23:59:27.824 UTC. Its sole
  example failed after 437.03 seconds at stage 6, with phase `starting_copied`,
  `hold_released=0` and `postparity=1`. The parent read the actual private
  console/virtiofs logs: QEMU immediately exited 1 because its vpsadmin
  virtiofs socket was missing; that virtiofs process reported a PID-file lock
  error (`Resource temporarily unavailable`). The earlier masks, copy and
  receipt, and first copied new boot/seed barrier had been reached. Full
  recovery/preservation and public release were not proved. The parent
  reports no path-bound QEMU/virtiofs process remains after cleanup.
  Both the private evidence root above and configuration roots
  `/tmp/retained-services-roots.tUP47BfH` remain retained and unread by the
  architect. Public pinned OSVM `osvm/lib/osvm/machine.rb:100-108` preserves
  a five-second stop/start gap in the same instance; the fixture replaces
  that instance on each boot and loses its timestamp. The log symptoms are
  consistent with this missing gap, not proof that it is the exclusive cause.
  The selected correction is a fixture-local monotonic stop-completion
  timestamp and only the remaining five-second delay before replacement
  start. Existing stop/reap/kernel checks, native cleanup/results and startup
  error diagnostics remain authoritative. No OSVM patch, helper/record change,
  PID-file deletion, retry engine or new scenario is authorized.
- The lead reports the focused real main/bootstrap timing watcher passed,
  exit 0 in 23.127 seconds: 5 timing checks, `guest_count=0`,
  `scenario_passed=0`, `startup_failure_propagated=1`, `parity=1`.
  Actual stdout first reports `passed=0` / stage 0, then the five timing
  successes with zero guests/scenario successes and propagated failure.
  The shared successful stop/kill tail was source-inspected; this no-guest
  probe did not dynamically prove either teardown path. Private artifacts
  `/tmp/storage-profile-settle-watch.qg93r99v` and
  `/tmp/storage-profile-settle-probe.40xjirfX/run.a6sht9rj` remain unread by
  the architect. Normal pinned-Git fixture-only amend produced
  `563c5255a5f08797640be8d9375705011bd15eb2`, tree
  `011f51a9b1a403369cba6ea29c08384a0af05773`. The first three commits are
  unchanged; the only delta is seven native-fixture lines for the monotonic
  timestamp and remaining five-second wait, held SHA
  `d1a2c7fb1f4d5c0dc46614c343d1dc48108f71365be68c9b2ed8e55ca85377f2`.
  The four-commit scope remains 25 paths, 5288 additions / 67 deletions,
  binary diff `ad0c274110a74229e84e1d13d441bd74935339060f8a910b5e4b88b3f20e450e`.
  Backup `backup/2026-09-23-storage-redesign-provider-before-fixture-settle`
  retains `5ee8281b`; freshly fetched SSH default `c56f981a` is unchanged.
  Exact-lease SSH publication from `5ee8281b` to `563c5255` succeeded.
  New CI metadata was pending. Fresh Luna/low `storage_profile_native_563`
  was assigned the actual API46 app through the fixed launcher at
  `/tmp/storage-profile-native-563.zugxbi_7/launch.py`, with exact head/tree/
  five-hash preflight and source hold. Neither the no-guest checks nor
  publication prove native acceptance.
  Existing reviewer lineage is unaffected and no full rereview is claimed.
- The lead reports the exact `563c5255` native run exited 1 after
  774.795 seconds, from 2026-10-03 00:25:32.442621 to 00:38:27.239366 UTC.
  Its sole example failed after 562.61 seconds (`expected true, got false`)
  at stage 6, with `hold_released=0` and `parity=1`. The parent read terminal
  evidence in `/tmp/storage-profile-native-563.zugxbi_7`, unread by the
  architect. Final seed `Result=success`, exact new toplevel, protected SQL
  projections, payload SHA, old-writer counter equality and retained disk
  identity passed before a second counter read and the failing assertion.
  The reported `new-api`, `new-seed`, `new-supervisor`, `old-api`, `old-seed`
  and `old-supervisor` counters were each 1; `new-seed >= 2` therefore failed.
  Guest poweroff was clean and no path-bound process remains. This is useful
  partial runtime evidence, not complete scenario acceptance.
  Public source appends the seed counter and touches its entry marker before
  waiting in `ExecStartPre`; stage 5 removes that marker then immediately
  force-kills the guest. At that revision neither operation flushed the filesystem.
  Loss of the first buffered counter/removal is plausible, not an exclusive
  causal proof. Correct only the native stage-5 command to remove the entry
  marker and successfully `sync -f /var/lib/storage-profile-fixture` before
  the same forced kill, with `block-new-seed` still present. Retain the
  `>= 2` assertion and the real interruption. No runtime helper, OSVM,
  policy/version or scenario change is needed.
- The lead reports the fresh guarded Luna/low actual-main command probe
  passed, exit 0 in 23.405 seconds: 3 checks, `guest_count=0`,
  `scenario_passed=0`, `failurepreventedkill=2`, `parity=1`. The parent read
  its fixed numeric stdout. Private evidence
  `/tmp/storage-profile-durability-watch.yjibafux` and
  `/tmp/storage-profile-durability-probe.gz1m1aVU/run._dv8m8y0` remains unread
  by the architect. An earlier utility used the default working directory
  for `current` and ran zero checks; its reported child-hash mismatch was
  erroneous. The parent reverified exact binding and all three unchanged
  frozen hashes before the fresh guarded run. There was no actual source
  hash drift. This proves command/temporary-filesystem behavior, not survival
  across power loss.
  Normal fixture-owner amend produced `45d7ce88fcb3a3d528f59b240c081667666526e3`,
  tree `09647aa2044c0da695654038091a45d59a2236a0`. The first three commits
  are identical; the sole delta is the tested `rm && sync` line, SHA
  `0d7ba5548a5449981978f8215769f1195147b06dc9bc7e51d4766eee2167c8d0`.
  The four-commit scope remains 25 paths, 5288 additions / 67 deletions,
  binary diff `c6c5e3f789b93f4bef6749b82822cd04e0d8a30098476448f371759d2f7c46b7`.
  Backup before-fixture-durability retains `563c5255`; freshly fetched SSH
  default `c56f981a` is unchanged. Exact-lease SSH publication from `563c5255`
  to `45d7ce88` succeeded. The lead reports exact `563c5255` Check
  `37081959992` succeeded; new `45d7ce88` CI metadata was pending. API broad
  `37030949481` remained in progress with no failure in that short metadata
  query. Fresh Luna/low `storage_profile_native_45d` was assigned
  the exact head/tree/API46 app through
  `/tmp/storage-profile-native-45d.g5bgua19/launch.py` under source hold;
  the runtime outcome was then pending.
- The lead reports the exact `45d7ce88` / API46 native app passed, exit 0
  after 802.973 seconds, from 2026-10-03 00:55:09.744613 to 01:08:32.717996 UTC.
  Its sole example succeeded in 611.85 seconds, with `passed=1`,
  `scenario_completed=1`, `phase_starting_copied=1`, `hold_released=0`,
  `examples=1`, stage 6 and `parity=1`. The parent read summary/terminal logs
  under `/tmp/storage-profile-native-45d.g5bgua19`, unread by the architect,
  and independently found no exact-path QEMU/virtiofs processes in `/proc`.
  The watcher reported guest poweroff and a cached kernel, with no local
  kernel build. This proves the ordered services fixture: masks, old-writer
  exclusion, interrupted copy and receipt, forced new-seed retry with two
  starts, and protected SQL/sentinel preservation. It does not prove
  full-cluster Node refresh, public-command hold release or public payload
  acceptance. Exact-head Check `37083986313` succeeded; API broad
  `37030949481` remains in progress according to the lead.
  Provider `45d7ce88` remains clean/published with four coherent commits and
  the original independent-review plus direct-fix lineage; no full rereview
  or exclusive explanation of prior failures is claimed. The implementer was
  assigned only the root flake URL edit on clean registered `8990ecca`, with
  lead-generated locking next. Root inputs were unchanged at that checkpoint;
  prepared base, `c5d8bed5` ancestry, exact `3f539b0f` backup and registration
  remain preserved. Review and composed-package checks precede any external
  idle-operator activation handoff.
- The lead reports the consumer URL and generated lock are now committed
  clean at `492fdf8e57639c83befed3e938fdd4b670e1bdbe`, on actual review base
  `8990ecca0cea7a3b59dd88e31138b177500bc43a`, tree
  `ec731f150cc5c0b2d8d4df44ffcd335a640f3b48`. The complete delta is one commit,
  exactly `flake.nix` and `flake.lock`, 9 additions / 9 deletions, binary diff
  `f93b029e69041b6030603b97adc7ef3c1d393691d451a648b2dd62d217ec91dd`.
  Exactly eight metadata leaves change: provider `c56f981a` to `45d7ce88`
  and canonical generic runtime `40838` to `2b67af62`; all other nodes and
  follows are equal. Tested `flake.nix` SHA is
  `a1c8d5d5771301968c2032c01f5929c183b9d6897be4e7e744841bac4710e916`;
  generated-lock SHA is
  `68c6711177ea2c6a46abe6c777aa30441a99ee372030ba4e9a9fab6422b16189`.
  Fresh Luna/low consumer no-build verification exited 0 in 16.151 seconds,
  `parity=1`; private evidence `/tmp/storage-profile-consumer-eval.1iswc69k`
  is unread by the architect. The lead verified normal hooks/no declared
  framework and no bypass. Retained `reviewer0`, saved Sol/xhigh/read-only,
  completed actual `8990ecca..492fdf8e` consumer composition review in all
  four HIGH lanes, with no findings at any severity. The review confirmed
  exact clean head/tree/diff, eight metadata leaves, defaults and canonical
  ownership, and explicitly concluded one coherent commit with no migrations.
  Original provider lanes were not rerun. Fresh Luna/low
  `storage_profile_composed_package` executed the four existing root
  checks, default-package build and packaged canonical-contract/helper-byte
  proof under exact `492fdf8e` source hold.
- The lead reports that exact composed-package batch passed, exit 0 in
  250.02 seconds, `parity=1`, with all three stages exiting 0. All four
  existing root checks were realized and the default package built. Actual
  packaged proof reported `contracts_equal=1`, schema 1, policy 3,
  `providers=2`, `profile_loader=1`; helper, maintenance and owning test-Nix
  hashes passed. Package:
  `/nix/store/g1jwv2598a5ig64f8yk1xg62mminkzpi-dev-workspace-0.2.0`;
  tools: `/nix/store/k62d9v4jjgqv4y2wgxz019k67liv75jp-vpsfree-dev-workspace-tools-0.1.0`.
  Canonical contract SHA:
  `33acdc50fa6b7ed94f84d1f7f1db0af8d76d7d57d2e721cbb6a204a96b27c0d1`.
  Private evidence `/tmp/storage-profile-composed-package._oa5spvo` is unread
  by the architect. The lead reports no local kernel compilation or remaining
  operation handle. Normal SSH publication of root feature `492fdf8e` is
  complete; the feature did not change default master. API broad CI remains
  in progress in the latest lead metadata; no new CI wait is required here.
  The built package is unselected. Only the external idle-operator public
  `workspace-host switch --source` boundary is prepared; no switch, cluster
  start, public refresh/release or payload acceptance has occurred.
  The original 680-second stage-1 failure, prior reviews and host-migration
  evidence remain intact, including the `5ee8281b` stage-6 lifecycle failure
  and its timing explanation as an inference. The services scenario is now
  accepted; public payload/release acceptance remains on hold. This is the
  existing ordered retained-services gate, not a new scenario. Package
  activation and public-cluster payload acceptance remain pending;
  copy-only still requires the actual preserving marker at execution.
  The services-only fixture can prove through `starting_copied`; the existing
  full-cluster acceptance must prove actual Node refresh and public-command
  release. Neither a no-VM smoke nor that fixture substitutes for release.
  The retained session cluster remains stopped; no maintenance boot of that
  cluster or package activation has occurred.
  Existing private recovery evidence, residency checks and policy/VM gates
  remain prerequisites; current disks and user data remain preserved.

### Current rebase and early-merge brief, 2026-10-03

**Original rebase scope:** rebase and regenerate the existing dependency chain.
No new storage feature, schema, selected package, cluster operation or session
lifecycle change is included. The lead owns ref backups, short Git steps,
generated locks and records; the implementer owns conflict resolution and
input URLs, watchers own long verification, and the retained reviewer owns
independent review. This is a design assessment, not another code review.
The later user-reported activation and conditional workspace/master approval
are recorded in the activation-verification subsection below.

| Component | Preserve as prior evidence | New default base |
| --- | --- | --- |
| Generic `dev-workspace` | Policy commit `2b67af62b40149e7554bab0c31b139cd52c963c1` from `4bec2016` | `924c0ec28c41dd8b56aaf17f2212b302ca614899` |
| `vpsfree-dev-workspace` provider | Four commits ending `45d7ce88fcb3a3d528f59b240c081667666526e3` from `c56f981a` | `8f8d8ecf5031c40d3e4a4ee2e9425721fc035800` |
| Root workspace consumer | Pin `492fdf8e57639c83befed3e938fdd4b670e1bdbe` from `8990ecca` | Current shared/origin master `93389c3373647fb3dc2d7ee15efa9acb93a8c62f` |

The source inspection found three generic upstream commits touching 27 paths:
session creation/recovery progress and the `codex-web` input update to
`4c170393a96ed0a6ac2e43488d073f6fcab36132`. The canonical contract at
`924c0ec:portal/internal/session/runtime-contract.json` still declares schema
1 / policy 2. Upstream does not change `libexec/workspace-host`, the session
runtime-contract implementation, transition tests, host module or host paths.
Its additions to `docs/workspace-portal.md` concern creation progress; preserve
them alongside the policy-3 explanation. The provider default change is only
its generic `924c0ec` URL/generated lock. Root default already carries the
new provider/runtime/Codex graph and coordination records. Do not discard
those updates by replaying an old lockfile wholesale.

Lead-reported execution checkpoint: the generic clean normal rebase onto
`924c0ec` is published as `4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4`.
Its owning range-diff is `=`; host helper, canonical contract and transition
spec blobs are unchanged from `2b67af62`. Syntax, whitespace and schema-1/
policy-3 checks passed. Exact-head CI `37113228573` succeeded; the old
`2b67af62` CI completed successfully with no superseded live run. Backup
runtime-before-master-rebase retains `2b67af62`. This reports source/check
evidence, not a new independent-review clearance. The normal provider rebase
onto `8f8d8ecf` initially stopped at dependency commit `da058353`,
conflicting only in `flake.nix` / `flake.lock`; exact `45d7ce88` is backed up.
The implementer was released for the bounded URL change to `4ef298b3` and
upstream generated-lock baseline, with generated locking owned by the lead.
The lead now reports normal rebase complete at
`399c33023a568a8d7a21e4e4df52829628720a28` on `8f8d8ecf`, with source/index
clean. Generated first pin `5b2e9a4` changes exactly four generic metadata
leaves and preserves upstream `codex-web` `4c170393`. Maintenance `101d312`,
profile `f50c92b` and fixture `399c330` all have `=` range-diffs; the entire
old `45d7ce88` to new `399c3302` tree differs only in `flake.nix` / `flake.lock`.
Normal SSH exact-lease publication from `45d7ce88` to `399c3302` completed.
The root normal rebase/generated pin is clean at
`6d1b9c4d63d900dbe8fe5b8790c8f92b28ab0b25` on `93389c3`. Its two owned
flake files change 9 lines each way: exactly eight expected metadata leaves
select provider `399c3302` / generic `4ef298b3`, preserving Codex `4c170393`.
Shared-master/index contents were unchanged. This is source-equivalence
evidence, not new independent-review
clearance or a VM-rerun decision. No selected package or cluster state changed.

The initial utility for the related six-stage quick batch called
`dev-session current` from the workspace root instead of the specified
tracking directory and returned no session. It ran zero checks and left no
process; this was a launch-CWD error, not a source/test failure or evidence
of a missing trusted binding. The parent immediately reconfirmed the exact
slug from the tracking directory with both environment identity variables
absent. The lead now reports the fresh correct-CWD batch passed all six
stages, exit 0 in 1175.12 seconds with `parity=1`, no remaining handle and
no reported local-kernel build. The supplied final results are:

| Stage | Result | Elapsed seconds |
| --- | --- | --- |
| 1: generic policy/transition | 40 runs / 250 assertions, all failure/error/skip counts zero | 2.704 |
| 2: provider maintenance / runner / selected CLI | 13/121, 10/27, 8/105 runs/assertions respectively, all failure/error/skip counts zero | 60.651 |
| 3: default smoke | Exit 0 | 428.045 |
| 4: explicit API46 smoke | Exit 0 | 654.618 |
| 5: provider default no-build | Exit 0 | 23.366 |
| 6: root no-build | Exit 0 | 5.625 |

These are lead-supplied results, not architect reruns or inferred counts.

The lead captured the complete inventories for the prepared
[rebase review packet](storage-profile-rebase-review.md), including all
histories and no migrations:

| Review range | Commits / paths | Diff | Tree |
| --- | --- | --- | --- |
| Generic `924c0ec..4ef298b3` | 1 / 4 | 175 additions / 3 deletions | `2c4c4b7e` |
| Provider `8f8d8ecf..399c3302` | 4 / 25 | 5288 additions / 67 deletions | `557303f2` |
| Consumer `93389c3..6d1b9c4d` | 1 / 2 | 9 additions / 9 deletions | `17967cd9` |

Retained `reviewer0` completed those actual committed ranges in all four
HIGH composition/history lanes with no findings. Saved Sol/xhigh/read-only
settings were unchanged, without override. Report
`cd4a54af-c26f-4d36-95e7-8a8fb72f2440` confirms exact clean heads/trees/diff
hashes and coherent 1/4/1 histories, no obsolete iterations and no migrations.
Original unchanged functional reviews and scoped host/native evidence are
retained; they are not relabeled reruns.

The lead reports the fresh rebased-package launcher passed, exit 0 in
245.623 seconds with `parity=1`: four existing root checks passed in
238.146 seconds, default package built in 7.296 seconds, and the actual
package-content proof exited 0. The parent directly read results/contracts:
`runtime_sources_equal=1`, `codex_sources_equal=1`, `contract_equal=1`, schema
1, policy 3, `providers=2`, `profile_loader=1`. Package:
`/nix/store/zmwh78dk1vjh2b91qnibjl682rb8hmwc-dev-workspace-0.2.0`;
tools: `/nix/store/vah0176g8h75vasl0nlg0farmaacybid-vpsfree-dev-workspace-tools-0.1.0`.
Selected Codex source revision is `4c170393a96ed0a6ac2e43488d073f6fcab36132`;
canonical contract SHA is
`33acdc50fa6b7ed94f84d1f7f1db0af8d76d7d57d2e721cbb6a204a96b27c0d1`.
Private evidence `/tmp/storage-profile-rebased-package.xnradz5x` is unread
by the architect; no process remains according to the lead. A redundant
post-launch verifier received its SHA instead of the package argument and
exited before verification. It supplies no evidence and does not invalidate
the correctly parameterized stage-3 proof; no rerun was requested.

Latest lead CI metadata confirms generic `37113228573` and provider
`37114037083` both succeeded. Source holds are unchanged. Ordinary SSH
empty-lease remote anchors now retain the exact pinned dependencies:

- Generic `backup/2026-09-23-storage-redesign-workspace-runtime-4ef298b3`
  points to `4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4`.
- Provider `backup/2026-09-23-storage-redesign-workspace-provider-399c3302`
  points to `399c33023a568a8d7a21e4e4df52829628720a28`.

These preserve published reachability without default integration; the lead
confirms both remote anchor readbacks match their exact heads. Normal SSH
exact-lease root feature publication is complete. Remote readback confirms
`6d1b9c4d63d900dbe8fe5b8790c8f92b28ab0b25`, with remote master unchanged at
`93389c3373647fb3dc2d7ee15efa9acb93a8c62f`. Public capture-comparison is also
complete at that exact base/head, with base label `Merge base` against locally
available `origin/master`; historical registration `initial_base_sha` is
preserved. This completed the pre-activation handoff. The subsequent user
report and conditional integration approval are recorded below; public Node
refresh/release, VPS/NAS payload acceptance, node-quiet, repair and APPLY
remain outside that approval.

The lead also reports API46 broad CI completed with 117 of 118 jobs passing;
the sole failed job is `storage/restore-after-reinstall-remote`. The supplied
read-only implementer diagnosis identifies a Bunny `queue_delete`
continuation timeout in the node2 StorageStatus updater's `RpcClient.close`
ensure path; `abort_on_exception` exits the daemon. Transaction 40 / handle
5221 send ran without persisted completion, leaving chain 9 locked. Restart
loses the fixture-only zero `start_delay` and reloads the production 90-minute
delay, beyond example 3's 900-second wait at action 9. Dependent example 4
then returns HTTP 423. The compared Node RPC, StorageStatus, Bunny, send,
CLI and fixture files are reported byte-identical to upstream `878a0d10`;
the diagnosis is not attributed to this feature or rebase. The initiating
broker-ack timeout remains unexplained; do not infer startup authentication
errors or claim safe chain recovery from this evidence.
This is a separate Node reliability/restart-fixture follow-up, with no fix,
manual unlock or blind rerun authorized here. The workspace composition
retains default API `5c76e329` and a disabled storage profile: the failure
limits broader storage acceptance, not rebase-only package activation.
The architect has not inspected private logs, run a test or polled CI.

#### Ordered source and verification work

1. **Generic first.** Preserve published `2b67af62` and rebase its single
   policy commit onto `924c0ec`. Keep exactly the schema-1/policy-3 change,
   transition regressions, preservation wording and owning documentation;
   no duplicate contract or new migration. Run the focused policy/transition
   cases through `test/workspace_host_test.rb` in the declared Nix toolchain,
   including policy-2 forward adoption, policy-3 downgrade refusal, malformed
   contracts and provider adoption. Give the retained reviewer the complete
   new one-commit series plus range-diff and upstream overlap. Publish the
   resulting exact reviewed head over SSH before downstream generation.
2. **Provider second.** Rebase the existing four coherent commits onto
   `8f8d8ecf`. In the owning dependency commit, select that published generic
   head in `flake.nix`; the lead regenerates `flake.lock` with Nix. Preserve
   upstream `codex-web`, all unaffected nodes/follows, default Admin/OS/React
   pins and default-disabled profile behavior. Keep maintenance, profile and
   native-fixture commits separate and patch-equivalent outside the intended
   dependency resolution. Focused maintenance/runner/command tests and the
   existing default/explicit-API46 Nix evaluation cover this composition.
   Review the changed dependency/compatibility surface and final four-commit
   inventory, then publish the exact provider head.
3. **Consumer last.** Rebase the one pin commit onto current `93389c3`
   (or a newly recorded current master if it advances). Select the new exact
   published provider through the existing root URL; generate the lock rather
   than adding a parallel generic input. Verify that only intended dependency
   metadata changes, with upstream Codex changes preserved and all follows
   intact. Capture the actual final base/head/tree and complete one-commit,
   two-path diff; historical registration `initial_base_sha` is not that base.
   Run the no-build evaluation, affected composition review, then the existing
   four root checks (`deployment-contract`, `agent-instructions`,
   `agent-team-policy`, `cluster-provider-composition`), default-package build
   and actual packaged contract/helper-byte proof. Publish with normal hooks
   and exact leases. Preserve old evidence/refs; do not alter shared-master
   contents or unrelated index changes during these feature operations.

The new generic package must keep its Ruby helper, portal, `codex-web` source,
Go module/vendor hash and browser protocol artifacts together. The existing
`nix/workspace-portal.nix` package check runs Go/JS and the Ruby session/host
suites; use that packaged verification, including new creation/recovery tests,
instead of inventing a live session-creation scenario. Independent review
should cover the affected general/composition/compatibility concerns and the
final history/no-migration conclusion. Preserve prior provider review and
direct-fix evidence; do not label unrelated provider lanes rerun.

**VM evidence reuse:** the observed upstream delta does not justify repeating
either existing VM solely because the package derivation changes. Carry the
`45d7ce88` native PASS and earlier host-migration PASS forward only after the
final comparison confirms unchanged maintenance/profile/fixture/runner bytes,
OSVM/API46 and other relevant guest inputs, and unchanged schema/policy-3,
host-path/module/migration semantics. The host test
`nix/tests/host-migration.nix` exercises host substrate forward/reverse paths;
it does not exercise the changed portal creation flow. Provider `AGENTS.md`
requires that VM when migration behavior or its upstream host-state contract
changes; neither is changed by the inspected upstream delta. A material
conflict or changed interface invalidates the affected proof and requires
rerunning that existing test after review, not adding a new scenario. New
package/source/contract proof is required regardless of VM reuse.

#### Activation, rollback and early root integration

After those gates, the external operator can activate the exact new reviewed
source through the existing public `workspace-host switch --source`, once
the lead/team and other managed sessions are idle. The active lead cannot
invoke it as an idle probe. Verify actual selected generation, matched
helper/portal/provider contracts, existing-session/portal availability and
read-only retained-cluster status before declaring activation successful.
Do not run old unselected helpers or relax transition/adoption refusals.
There is no cluster reset, boot, hold release or storage repair implied here.

Keep the complete maintenance-aware provider/runtime composition together.
Policy 3 intentionally refuses a policy-2 target while any registered cluster
state exists, even with the profile disabled or no pending hold. Recover
forward with the same or a newer reviewed compatible composition; retained
backups are evidence, not authority to use a pre-policy-3 recovery binary.
The profile remains off by default and retains the old API default pin;
enabled use still requires API scheduler/Plan support and the existing
preserving-seed/mixed-version gates. Activation affects the workspace runtime
for managed sessions; it does not deploy storage changes to shared or
production nodes. Strict, node-quiet, repair and APPLY remain off.

**Recommendation on the user's original merge question:** yes, integrating the narrow
root package pin after successful activation and its own review/checks is a
reasonable independent milestone. It need not wait for the vpsAdmin storage
redesign or full-cluster payload work. The user has since supplied conditional
approval for workspace/master, as recorded below. Capture the final comparison,
refresh current-master ancestry and integrate fast-forward only after the
activation checks pass. Keep the feature ref and this session active for its
remaining work.

Exact published generic/provider feature commits can remain intentional root
dependencies; upstream integration is not technically required for an exact
Nix pin. For that choice, retain published reachability for those exact
commits, record them as dependencies, and prevent later routine repins from
silently dropping maintenance support. A lock/NAR hash alone is not a promise
that a force-rewritten, unreachable upstream commit stays retrievable.
The lead has created the ordinary exact Git remote anchors listed in the
checkpoint after review; retain them with the pinned commits. This uses no
new enforcement mechanism and authorizes no further ref operation here.

There is a concrete composition hazard in integrating only the generic policy
first: `8f8d8ecf:dev-clusters/vpsadmin/bin/devcluster` still routes
`transition-adopt` directly to `devcluster_adopt_package_transition`, whereas
the feature uses `maintenance_adopt` and guards ordinary commands during a
hold. A legacy provider updated to generic policy 3 could advertise an equal
policy while lacking those guards. Do not accept that as a safe downstream
update. If upstream integration is preferred, coordinate generic policy 3
with at least the provider maintenance prerequisite, or the complete provider
feature once its own release gates and approval are satisfied. The small
host-policy/hold prerequisite can be integrated independently of future
storage redesign; full enabled-profile readiness remains a separate claim.
This strategy does not authorize a new split, default merge or updater change
within the present rebase task. Until coordinated integration is approved,
the exact reviewed complete feature pins are the bounded alternative.

#### Verified activation and completed workspace integration

The lead relays the user's exact direction: “activated. you can verify it, if
it is ok, you can merge the workspace.” This authorizes verification and,
conditional on success, integration into **workspace/master only**. It does
not authorize another package activation, generic/provider default merges,
storage deployment, cluster actions or session lifecycle changes. The lead
owns the checks and Git operations. The following completed activation and
integration results are lead-reported; the architect ran no operation.

**Activation verification PASS:** installed `workspace-host status` selects
the exact reviewed `zmwh78dk…-dev-workspace-0.2.0` package and lists the owned
`vpsfree-cz` workspace. The selected wrapper matches that package; current/team
commands work through the new generation. Public same-session
`vpsadmin-devcluster status` exited 0 with stopped/bridge state. Installed
tools match `vah0176g…-vpsfree-dev-workspace-tools-0.1.0`, with equal canonical
schema-1/policy-3 contract. All four owned router/portal/Codex/tmux units are
active, with each stable-profile ExecStart resolving to the expected selected
package. An unauthenticated request to the owned portal using the existing
public CA returned HTTP 401 with TLS verification result 0, without credentials.
Initial literal-path/default-CA checks reflected harness assumptions and were
corrected without runtime or trust changes. Private artifacts remain unread
by the architect.

The completed verification used the following bounded public-check contract:

1. Run installed `workspace-host status` and confirm the selected package is
   `/nix/store/zmwh78dk1vjh2b91qnibjl682rb8hmwc-dev-workspace-0.2.0`, the package
   whose actual contents passed the recorded proof. Check the reported active
   Codex matches that composition and that the existing workspace/session
   portal remains available. A responding old portal alone is insufficient:
   match its service executable to the selected package using public service
   metadata, without reading private logs or credentials.
2. From that selected package, check public
   `share/workspace-portal/runtime-contract.json` against recorded SHA
   `33acdc50fa6b7ed94f84d1f7f1db0af8d76d7d57d2e721cbb6a204a96b27c0d1`
   (schema 1 / policy 3), and
   `share/dev-workspace/extensions.json` for the two expected providers and
   their reviewed tools package
   `/nix/store/vah0176g8h75vasl0nlg0farmaacybid-vpsfree-dev-workspace-tools-0.1.0`.
   The prior exact-package proof already covers helper, profile-loader and
   Codex source bytes; selection of that same immutable package carries it
   forward without a new build or repeated full content test.
3. Run the installed public
   `vpsadmin-devcluster status 2026-09-23-storage-redesign` from the verified
   workspace. Require normal generation/provider dispatch and an intelligible
   retained-state result. The last expected runtime state is stopped; stale
   readiness does not authorize refresh/start. Record only nonsecret status.
   An identity/adoption error needs resolution before merge; do not bypass it
   with an unselected helper or alter the retained cluster to make status pass.

These use existing interfaces (`libexec/workspace-host` methods `status` and
`dispatch_cluster`, its `ExtensionCatalog`, and the provider's `status` command).
They verify the selected composition and continuing access, not Node quiet,
maintenance hold release or VPS/NAS payload behavior.

**Completed integration result:** normal pin replay onto actual shared local
master `3fd3ff77398c1557ba57e9da3e4dadb5f6748b7e` produced
`1fa9c982b866a305bd1451f2c32f6d387d2dc1a3`. The single pin is `=` in range-diff;
both tested flake hashes match, with the same two-path 9-addition/9-deletion
change and binary diff SHA
`18d2131e8abf5f7ab427837f34c09374af91328f5851f07a96c6059177c7a333`.
Nix evaluation of the final default outPath equals the exact active
`/nix/store/zmwh78dk1vjh2b91qnibjl682rb8hmwc-dev-workspace-0.2.0`.
Final-head flake check without builds exited 0. Original independent review
and actual package proof therefore carry forward; no new build, activation,
full review or VM rerun is claimed.

Explicit capture-comparison completed at `3fd3ff77..1fa9c982`; the
before-integration backup retains `6d1b9c4d`. Normal exact-lease feature
publication completed, then shared-root `git merge --ff-only` advanced
`3fd3ff77` to `1fa9c982`, changing only the flakes. Normal SSH master push
`93389c3..1fa9c982` completed. The lead's final remote readback confirmed both
master and the retained feature at exact `1fa9c982`. A concurrent other-session tracking-only commit then
advanced local master to `4123553c1ae1fc47767e9b30445ff4f7f79266e9`, changing
three foreign tracking paths and no source/procedure/config content. The pin
is an ancestor, both flake hashes remain exact, and other index entries were
preserved, with the index empty afterward. An exact-HEAD postmerge check first
noticed this concurrency; Git metadata established the cause without reading
foreign records, rewriting master or performing any foreign lifecycle action.

Workspace integration is complete. Generic/provider defaults are not merged;
the published dependency anchors and maintenance-aware provider/policy-3
composition remain required. This performs no physical cluster operation.
Native `45d7ce88` evidence still ends at `starting_copied`, `released=0`;
public Node refresh, full VPS/NAS payload/history acceptance and the separate
API broad-CI RPC reliability follow-up remain pending. The session stays active
and open, with refs retained. Lead-owned state/rollout/review records track the
operation and final readback.

**Retained reconciliation and FF contract:** the lead reported local master
advanced from `93389c3` to
`3fd3ff77398c1557ba57e9da3e4dadb5f6748b7e` through seven owned tracking files;
remote master was last `93389c3`. Preserve published `6d1b9c4d` and its review
evidence, then replay the single pin commit onto the actual current master in
the registered feature worktree if it still requires that replay. Verify the
intervening delta is coordination-only, the pin range-diff is equivalent, and
final `flake.nix`, `flake.lock`, `config/`, package/test inputs and relevant
procedures match the reviewed composition. The root package expression uses
the pinned provider plus `siteConfig`/`teamConfig`. Tracking records and the
root commit ID are not semantic runtime settings, but `clusterDefaults`
references `./config/*.json`: a changed root source NAR/path context can yield
a different package path even with identical config bytes. Do not infer an
identical package output from equal flakes/config alone.

**Bounded final package gate:** after the replay onto current master, the lead
evaluates the exact final default-package output and compares it with the
activated `/nix/store/zmwh78dk1vjh2b91qnibjl682rb8hmwc-dev-workspace-0.2.0`.

- If the output path is equal, reuse its actual built-content and activation
  proof. No duplicate package build, activation or VM is required.
- If the path differs, a fresh watcher runs the same four existing root
  checks and default-package build, then proves the final built runtime,
  canonical contract, provider/helpers/profile-loader and Codex match the
  active build, together with byte equality of the ordinary default JSON
  inputs and unchanged effective configuration. Record both package paths.
  Differences attributable only to source/store path context are acceptable
  when every changed reference resolves to the same effective content. No
  runtime/default logic, dependency leaf, helper, OSVM or configuration-content
  change is permitted under this equivalence claim. No second activation or
  new VM scenario is needed; a substantive mismatch instead blocks this
  carry-forward claim for assessment.

This gate is sufficient for a source-equivalent final merge after successful
activation. If outputs differ, state precisely that the earlier package was
activated and the final package was built and proved equivalent; do not say
the final distinct store path was selected.

Under that exact equivalence, retain the four-HIGH no-findings review, six-stage
quick results, package proof and scoped VM evidence without claiming reruns.
The user's conditional approval survives the clean equivalent rebase; it does
not require a new activation or VM scenario. If actual runtime/package inputs
change, assess that concrete delta and the affected proof before integration.
Record the new head and actual review base, publish the feature normally over
SSH with the exact lease, and repeat
`dev-session worktree capture-comparison 2026-09-23-storage-redesign workspace --as-is`
after the final head change. Preserve historical registration initial-base
metadata; the old `933..6d1` capture is not the new comparison.

Once activation verification and equivalence pass, confirm the feature
descends from the still-current shared master, preserve foreign work/index,
stage nothing for the merge, and use shared-root
`git merge --ff-only <registered-feature-branch>`. Publish master normally over
SSH and read back the final heads. If master advances again, repeat only the
necessary ancestry/equivalence/comparison steps; never reset or stash shared
changes. Keep feature and dependency anchor refs and the session open. These
gates were satisfied for the completed integration recorded above; this
retained contract is not a request to repeat the operation.

### Ownership and configuration boundary

| Owner | Deliverable |
| --- | --- |
| Implementer: vpsAdmin | Small generic scheduler grammar/refresh support and plan-level `keep_empty_group_snapshots`; common registration/removal guards, focused tests and owning docs. |
| Implementer: vpsFree dev-workspace provider | Explicit storage-profile configuration, API config overlay, shared provisioning/hook helper, safe seed integration, fixtures and provider tests/docs. |
| Lead / assigned operator | Same-session source selection and package transition, private config and DB backup, supported in-place services update/provisioning, acceptance evidence and recovery. |
| Architect0 | This technical brief and bounded source/design conformance. No application or cluster edits. |
| Independent reviewer | Committed changes and complete relevant branch delta after quick verification, before long integration. |

The affected provider owns `dev-clusters/vpsadmin/{nix/test.nix,README.md}`
and its command/provisioning support in `vpsfree-dev-workspace`. Introduce
generic profile behavior there; consuming workspace/cluster configuration
selects its concrete node, pool roots and defaults. Do not revive superseded
instruction-only branches or change generic dev-workspace behavior to carry
this policy. Production `configs/vpsadmin/api/{hooks.rb,dataset_plans.rb}`
are read-only behavioral references, not imported site policy or deployment
targets. OS, React, PHP freeze UI and production/shared hosts need no feature
change for this slice.

The profile is off when absent/disabled. Its enabled overlay replaces the
fixture hooks/plans exactly once and preserves unrelated fixture config.
Within the enabled profile, boolean `storageProfile.enrollment` defaults to
`true`. The enduring retired selection is `enable=true, enrollment=false`:
preserving seed and its marker stay enabled, while new enrollment is disabled.
Require a boolean in Nix and the generated version-1 helper configuration;
emit the normalized value explicitly. Disabled legacy behavior is unchanged
and is not a supported way to retire a previously enabled retained cluster.
Use the same config directory for API, DB setup, supervisor and scheduler;
do not load both fixture and profile backup hooks, or append hooks on every
provisioning invocation. Keep existing default single/dual behavior unchanged.
The storage profile requires the configured storage topology and exact pools.

### Pool layout, schedule and retention

| Setting | Accepted value |
| --- | --- |
| VPS source pools | Existing regular-node hypervisor pools; preserve existing roots and data. |
| Backup pool | Configured `storage1`, `tank/backup`, role `backup`, initial `max_datasets=32`. |
| Member NAS pool | Configured `storage1`, `tank/nas`, role `primary`, initial `max_datasets=32`. |
| NAS root quota | 1024 MiB per member root; fixture child shares that quota. |
| Snapshot minute field | `*/5`; other fields `*`. |
| Backup minute field | `2-59/10`; other fields `*`. |
| Task reload | 60 seconds for the enabled dev profile; 10800 seconds remains the production/default value. |
| Newly profile-created source retention | Minimum 2, maximum 3, maximum age 1800 seconds. |
| Newly created backup retention | Minimum 2, maximum 5, maximum age 3600 seconds. |
| Existing source retention | Preserve its current minimum, maximum and age; normal later Backup may prune under those settings. |

These roots share storage1's physical `tank`: they test logical separation
and real transfers, not independent failure domains. Validate real free space;
the provider's synthetic capacity figures do not prove room on its roughly
20 GiB disk. Existing quotas/retention are not lowered to make provisioning
fit. A capacity or entitlement shortfall is an explicit refusal.

Use one `dev_short_backup` plan with group snapshots and normal Backup at
the times above, including newly provisioned NAS DIPs. NAS backup uses the
same-node transfer path; VPS backups to storage1 exercise the cross-node path.
GroupSnapshot alone never rotates; assigning retention columns alone cannot
bound NAS history. Normal Backup transfers and then rotates both copies.
The 3/5 limits are targets after successful rotation. Dependencies, locked or
failed backups can retain more history; the profile must not promise a hard
physical snapshot or disk-space ceiling.

Extend `CronTask.parse_field` with the bounded grammar `*`, integer,
`*/positive_step`, and `start-end/positive_step`. Preserve valid wildcard and
integer behavior. A stepped range is inclusive, starts at `start`, does not
wrap, stays within the field bounds, and has a positive step no larger than
the field's cardinality. Reject zero/negative steps, reversed/out-of-range
ranges and partial/garbage parsing. Required minute expansions are
`[0,5,...,55]` and `[2,12,...,52]`. Do not add comma lists, a general cron
dependency, multiple task rows per action, or another timer/engine.

Validate profile schedules before persistence and report invalid schedule
rows explicitly. Keep task replacement atomic for valid loaded tasks; a
malformed row must not silently become minute zero. The existing local
`schedulerctl update` requests immediate reload; `get-tasks` confirms the
loaded schedules. The two-minute offset reduces contention but does not
prove the snapshot chain finished. Resource locks and terminal chain results
remain authoritative. Frozen/locked task skips retain existing behavior.

### Shared group lifetime and common registration guards

Add the **plan-level** option `keep_empty_group_snapshots: false` to the
existing Registrator/Plan/BlockEnv/Executor path. Enable it only for
`dev_short_backup`; preserve false/default behavior for other plans.

For this option, bootstrap one shared group `DatasetAction` and one
`RepeatableTask` per exact `(DatasetPlan, source Pool)` before enabling
enrollment. They are profile configuration, created in a separately committed
provisioning transaction. The group may have zero members: existing execution
already skips an empty group. Never use a dummy DIP to create the template.

- `add_group_snapshot` requires exactly that compatible action/task and adds
  only this DIP's `GroupSnapshot` membership. Missing/ambiguous templates are
  a provisioning error; user/VPS chains never lazily create them.
- `del_group_snapshot` removes the DIP membership and retains the shared
  action/task even when it was last. They never receive source-chain
  creation or deletion confirmations.
- Bootstrap/recovery, true-plan register/unregister and retirement use a
  common SQL transaction and lock order: `StorageMutationAdmission.check!`,
  then `DatasetPlan SELECT FOR UPDATE`, then relevant action/task rows.
  The Plan-row lock serializes the absent-template insertion case too.
  It lasts through staging commit, not through Node execution. No whole-Pool
  lifetime resource lock is needed because source chains cannot delete the
  template later.
- Keep normal Dataset/DIP ResourceLocks for source-specific operations.
  Common direct plan API paths must refuse a source locked by another chain
  or a pending conflicting membership confirmation. Same-outer-chain reuse
  is allowed. Put these checks in common plan behavior, not only hooks:
  the direct Dataset Plan API calls `dip.add_plan/del_plan` without firing
  a storage chain.

Require one environment-plan per actual eligible environment, one membership
per source DIP, one group member per DIP, one backup action per membership,
and exactly one task per action. A repeated services update/provisioning run
is a no-op when these rows match. Refuse duplicates, conflicting destinations,
pending destructive confirmations and incompatible partial state; do not
delete unexplained rows to force idempotency.

Set `EnvironmentDatasetPlan.user_add=true`: current clone/migrate paths skip
plan copying when it is false. Every registration route must still validate
the exact configured source pool/environment and backup destination. The
existing backup DSL selects the first open backup DIP; before invoking it,
require exactly one eligible open backup DIP for this logical Dataset and
prove it is the configured copy. Check the resulting action destination too.
Missing/closed/offline/wrong-role or multiple/foreign pools never cause an
automatic fallback. Preserve `vps_replace`'s `preserve_existing_backups` rule.

### One helper and exact rollback ownership

The provider owns a shared helper, conceptually
`ensure_backup_and_plan!(chain:, source_dip:, configured_backup_pool:, ...)`.
Call it from DatasetInPool create/migrated hooks and a bounded normal
catch-up chain for existing objects. The helper runs inside the caller's
staging SQL transaction and uses that outer chain's confirmations. It must
not independently `.fire` a child chain or wait for Node execution there.
The catch-up wrapper explicitly checks storage admission before provisional
writes; its new class name is not automatically covered by the registry.

Persisted named chain classes must load during normal profile initialization
in both active and retired selections. A fresh API, Supervisor or database-task
process must read nonempty and terminal `CatchUp` chains without first calling
the provisioner. Loading the class does not enroll objects or fire work.

1. Reuse a compatible confirmed backup DIP, or create only the missing DIP
   with `confirm_create` and the new-copy retention. Append existing 5201
   with `create(new_backup_dip)` only, and lock the new DIP.
2. Attach newly added plan membership, group membership, per-source backup
   action/task to the same outer chain's NoOp using `just_create`.
   Shared templates and preexisting rows receive no creation confirmation.
3. Never pass the existing logical source Dataset through `Dataset::Create`
   just to add a backup copy: it unconditionally confirms `create(part)` and
   Node rollback can delete that reused Dataset. Fresh NAS/VPS logical
   Datasets may use it normally; their original creation remains owned by
   their original outer chain.
4. A staging exception rolls back provisional SQL. A later ordinary failure
   or rollback compensates only newly owned objects through the same
   `dst_chain/use_chain` and normal confirmations. A no-change catch-up may
   use `allow_empty`; it need not manufacture a physical operation.

Existing-VPS catch-up creates missing backup/schedule metadata without
Rotate or payload writes. If its first preservation copy needs a snapshot,
use normal Snapshot followed by Transfer and await completion. Only later
scheduled Backup invokes normal rotation under the unchanged source policy,
as the user explicitly selected. Never reset/reinstall that VPS or treat it
as the writable acceptance fixture.

### Future members and safe repeatable seeding

Create one provider-owned reusable shared `ClusterResourcePackage` before
User::Create, with both `user_id` and `environment_id` null; attach it to the
configured dev environment via `DefaultUserClusterResourcePackage`.
The accepted configurable defaults are CPU 4, memory 4096 MiB, swap 2048 MiB,
diskspace 8192 MiB, IPv4 4, private IPv4 16. Set that environment's
future-user create/destroy permissions true and `max_vps_count=2`.
User::Create already assigns defaults and calculates resources before its
NAS hook. Do not assign the package again in the hook. Max-VPS count is a
ceiling: 8 GiB covers 1 GiB NAS plus one 4 GiB VPS, not two such VPSes;
another VPS must fit remaining entitlement or an explicitly larger package.

Default packages are additive: detect conflicting/duplicate defaults. Treat
the shared package's policy as versioned once assigned, so routine updates
cannot change existing subscribers' entitlement. Never rewrite personal
packages. Existing-user NAS catch-up uses available entitlement and reports
a shortfall; it does not silently grant more. Create a namespace/default map
only when absent, using the normal allocator; retain existing allocations.

**Pre-API freeze boundary:** `bootstrap_defaults!` may run while the retained
storage mode is `read_only`. With enrollment enabled it validates/creates the future shared
package and its items/default link, and sets the Environment's future-user
permission/count metadata. Remove `StorageMutationAdmission.check!` from
this static-only method; retain its SQL transaction, Environment row lock,
duplicate/assignment checks and immutable package-policy validation. It must
not change the freeze mode, epoch or audit history, existing user assignments,
namespaces, Plan enrollment or physical/catalog storage state. This permits
the preserving seed to boot without temporarily unfreezing storage.
Physical provisioning, Plan/template changes and catch-up retain admission;
this exception does not apply to the whole seed or provisioning helper.
With enrollment disabled, the same static transaction/Environment lock only
validates and removes the exact owned future default-package link, if present.
It creates no package/default, changes no Environment permissions/count and
preserves all packages, items and user assignments. Ambiguous ownership
refuses; unrelated defaults are never removed. Preservation of namespaces
and existing resource assignments remains enabled in both selections.

**Required seed integration:** the installed provider's repeatable seed
currently rewrites existing namespace blocks/maps and personal resource
packages on every update (`nix/test.nix:748-830,888-891`). An overlay/helper
alone does not preserve them. For the enabled profile, make the seed path
preserve existing assignments and validate/report incompatible state;
the pre-API seed validates and preserves existing namespaces/maps, and
defers truly missing namespace allocation to post-readiness provisioning
through the normal `UserNamespace::Allocate` chain and its NoOp confirmations.
It must not wait for a chain or perform physical work before API/Supervisor
readiness. Use the supported accounting path for missing resource state.
Leave disabled-profile behavior compatible.
Test changed existing namespace/package values surviving a services update.
Keep credential management on its existing private path.

Seeded users bypass User::Create and need the same explicit catch-up helper.
Future API-created members get NAS through the new User hook; future VPSes
and NAS child DIPs get their backup and plan through the common DIP hook.
For future User::Create, namespace allocation uses the same allocator within
the existing outer chain (`use_chain`), never independently fired work.
Do not replay User::Create for an existing user. Separate pre-API static
configuration/default-package seed from post-node-ready physical provisioning;
waiting for a Node chain inside the pre-API seed would block its own services.

### Implementation sequence and acceptance

Implementer owns a small reviewable series: (1) generic scheduler/plan support
and focused API tests, (2) provider overlay/helper/provision/seed integration
and tests/docs, (3) real payload acceptance fixture. The architect edits no
application path. Keep normal hooks and CI selectors/topic coverage current.
No plan/state/portal changes belong to this brief's owner.

Quick checks, in the owning Nix environments:

- API CronTask and Daemon specs: exact 5/10-offset matching, invalid grammar,
  wildcard/integer compatibility, default/dev refresh and discovery of new
  tasks without restarting the scheduler.
- Dataset-plan/helper specs: default-false cleanup unchanged; keep-empty
  retains the same action/task IDs after last-member removal; concurrent
  different-DIP unregister/enroll; direct API admission/lock/pending-state
  refusal; same-source concurrency; missing templates/pools and foreign
  destinations; repeated provision/update without duplicate rows.
- Confirmations: failure during nested User/VPS creation or catch-up deletes
  only its new objects; reused logical Dataset/source DIP/shared templates
  survive. Cover same-chain multiple DIPs, source reuse, clone/migration and
  preserve-existing-backups replacement behavior.
- Provider focused Ruby/config tests: disabled compatibility, overlay loaded
  once by all services, retained existing namespace/package data, future
  default entitlement, retirement and supported partial-run recovery.
  A real-DB frozen-bootstrap regression must prove static defaults succeed
  repeatably under `read_only`, without mode/epoch/audit or existing assignment
  changes, new chains, storage rows or Plan/template enrollment. Keep the
  conflicting-policy refusal and atomic SQL rollback checks.
  Use existing `test/devcluster_*_test.rb` conventions and Nix smoke checks.
- Scoped whitespace checks, declared lint/hooks, API exact-once topic
  coverage and affected CI selectors. Component `.#api` shells already
  enter `api`; do not add a second `cd api`.

**Verification source selection:** the provider's default `devcluster-vpsadmin`
input remains `5c76e329`; enabled-profile verification requires the selected
API `46b3bf6f` with scheduler/Plan support. Keep disabled/default checks on
their existing pin. The provider-owned real-AR harness runs from that API
worktree through `nix develop .#api -c bundle exec ruby <absolute-harness>`;
use the shell's `VPSADMIN_REPO_ROOT` to load its actual `api/spec/spec_helper.rb`
and provider helper. Allocate a disposable database with that API's
`tools/test_db.rb` before loading the schema, rather than inheriting a database
URL or configured database. Record the API revision and loaded source paths.

For the planned explicitly requested enabled smoke case, reuse the root
flake's existing `devcluster-vpsadmin` override, e.g.
`nix run --no-write-lock-file --override-input devcluster-vpsadmin path:<api-worktree> .#devcluster-check -- --storage-profile`
from the provider root. The trailing smoke flag is a proposed test interface,
not an existing operation. Existing `flake.nix:147-165` passes that input to
the smoke script, which overrides the installed nested `vpsadmin` input
(`test/devcluster_nix_smoke.rb:47-54`). Set storage topology only for the
enabled fixture and retain the script's disposable config/environment
isolation. A source-path environment variable alone does not select the Nix
modules. No default-pin change, parallel feature input or capability registry
is needed. Forcing the enabled configuration's derivation evaluates the real
scheduler option/overlay; AR checks separately prove DSL semantics.

After committed quick verification and independent review, the lead runs
the in-place cluster gate through the normal verification watcher:

1. Complete the reviewed maintenance-start/copy-only prerequisite below.
   Ordinary startup of the old services closure is blocked by the preservation
   requirement: its seed can overwrite existing allocations/namespaces.
   Preserve cold-disk/config/generation recovery evidence, then boot only
   services with the fixed writer hold. Once reachable under that hold,
   privately capture a fresh logical DB backup and existing VPS/resource/
   namespace baseline. Keep DB/schema/OAuth credential pairing; publish no
   credentials or member paths. Never reset or replace retained disks.
2. Copy the reviewed preserving services closure without activation, then
   stop and restart through the recorded-copy path below. Keep storage/bridge
   topology. Deploy scheduler/DSL support before introducing its new syntax
   or keep-empty configuration. Subsequent normal in-place updates use
   `vpsadmin-devcluster update 2026-09-23-storage-redesign services` only after
   the maintenance hold has been successfully released into the new closure.
3. Provision exact Pool roots through normal Pool::Create after Node services
   are available; await confirmations/Node pool preparation. Regular-node
   refresh alone is insufficient because current provider refresh skips the
   storage role. Bootstrap templates separately, then run repeat-safe user
   and DIP catch-up. Refuse unexpected preexisting ZFS objects rather than
   importing them into catalog rows.
4. Use a dedicated ordinary-member fixture VPS and NAS child for payload
   writes. Reuse only positively identified profile fixtures; a partial or
   unrelated object is inspected/refused, never overwritten. Keep the existing
   scheduler held during controlled initial fixture creation/proof, then
   resume it explicitly; no second scheduler is introduced. Record/recover
   its service state even when the exercise fails.
5. In the fixture VPS write known small payload A, snapshot S1 and complete
   the initial full backup to its empty storage1 backup copy. Read actual
   destination S1 bytes/checksum. Change/add/delete fixture files to payload
   B, snapshot S2 and complete an incremental backup. Verify both historical
   versions, common S1, same backup tree/head branch, second send inputs
   S1+S2, and terminal SIP/SIPB confirmations. A queued task reply or matching
   row counts is not payload proof. NAS gets an analogous small same-node
   backup check; it does not replace cross-node VPS evidence.
6. Receive only into dedicated backup branches. Existing `recv -F` can alter
   destination live content, so never use the member NAS working dataset or
   user VPS as a receive target. Use supported read-only snapshot access for
   checks and avoid exporting private paths in reports.
7. Reload/inspect the one task/action schedules, resume the scheduler and
   observe an automatic snapshot/backup cycle. Exercise retention above 3/5
   only on fixtures, retaining the latest incremental base and validating
   payloads. Re-run provisioning and one supported services update; prove
   unchanged schedule counts and preserved existing VPS/files/namespaces/
   resource settings. Validate future API-created user/VPS behavior too.
8. Leave the cluster usable, with automatic short scheduling active and PHP,
   React and API access intact. Retain existing freeze/auth/CAS behavior;
   return any trial freeze through the authenticated API with a fresh epoch.
   Report actual chain/payload results and failures separately. DB-only drain
   still does not establish node quiet or repair authority.

### Retained-disk maintenance bootstrap prerequisite

**Selected design; implementation draft, not reviewed or operated.** The lead selected this
bounded provider prerequisite because services are stopped and the preserving
closure is not yet in their retained Nix store. It holds old application
writers from initial boot, permits backup and closure copying, and uses a
second boot to start the new preserving seed. This is not the broader storage
G1 exclusion protocol and grants no quiet/repair/APPLY authority. Main API
scheduler/plan/profile implementation can proceed independently.

#### Boot and source contract

At provider `c56f981a`, `bin/devcluster:start_cluster` rebuilds the selected
configuration before boot; it does not choose the retained disk's default
system generation. OSVM `8d05dc3a` passes the selected kernel/initrd and
`init=<config.toplevel>/init` directly, and preserves existing disk images
without copying the new closure into them. The services guest does not mount
the host Nix store. Thus a new host build alone is insufficient; booting an
old resident closure normally reruns its baked old seed. Neither failure may
fall back silently to a normal old boot.

Implement this only in the vpsAdmin provider, with a narrowly typed runner
mode calling OSVM's existing `start(kernel_params: ..., wait_for_boot: false)`.
No OSVM, Node/DB protocol, generic recovery framework or arbitrary kernel
parameter option is needed. The public command proposal is:

```text
vpsadmin-devcluster maintenance-start <slug> --resident-config <recorded-store-config> --expect-services-toplevel <recorded-store-toplevel> --residency-evidence <private-evidence.json>
vpsadmin-devcluster update <slug> services --copy-only
vpsadmin-devcluster stop <slug>
vpsadmin-devcluster start <slug> --copied-config
```

These are proposed new supported forms, not commands available at `c56`.
The first command uses an exact, previously recorded configuration whose
services toplevel was positively observed in the retained guest. The explicit
expected toplevel is a CAS check against that configuration, not proof of
residency by itself. Lead-owned prior successful activation/copy evidence is
the bootstrap prerequisite; a selected `result-config`, source SHA, stale
ready file or guest profile generation number alone is insufficient. Record
that evidence's reference with the operation. Refuse if the lead cannot
establish the pairing; do not discover it by booting an unmasked candidate.
Do not build or replace the resident selection during maintenance-start.

`--residency-evidence PATH` is required, including first bootstrap and retry.
It names an operator-owned regular, nonsymlink mode-0600 UTF-8 JSON file,
maximum 8 KiB, with exactly these fields:

```json
{
  "version": 1,
  "workspace": "/absolute/registered/workspace",
  "slug": "bound-session-slug",
  "resident_config": "/nix/store/recorded-config",
  "resident_config_sha256": "64-lowercase-hex-digits",
  "services_toplevel": "/nix/store/recorded-services-toplevel",
  "evidence_kind": "cold_residency",
  "evidence_reference": "private operator evidence reference"
}
```

The hash is SHA-256 of the exact resident config file bytes. Require matching
workspace/slug, config argument/digest and expected services toplevel; reject
unknown versions, extra/missing/duplicate keys, invalid types and control
characters. Bound each string to 2048 bytes and the slug to 128 bytes.
`evidence_kind` is one of `prior_activation`, `prior_copy`, `cold_residency`;
`evidence_reference` is a nonempty bounded reference, not executable input.
Do not open its referenced artifact or require a recursive closure/hash graph.
This is trusted operator evidence, not authentication or independent proof.
For this first bootstrap the lead prepares it from prior activated provenance
and the read-only cold-copy init/generator evidence; stale selected metadata
alone remains insufficient.

Before spawning, atomically capture the validated fields and evidence-file
byte digest in the existing private maintenance operation record. Never print
its private reference in normal status. Retry requires the same captured
content/digest and resident selection; a relocated identical evidence file is
acceptable. A changed file or attempted retarget of a pending record refuses.
Interrupted initial recording cannot authorize boot; an already recorded hold
survives later errors. No separate proof registry or implicit evidence upgrade
is introduced. Focused fixtures cover absent/malformed evidence, wrong scope/
config/toplevel/hash, same-evidence retry and changed-evidence refusal.

Use normal workspace/session/socket ownership, package-generation recheck
under lifecycle and cluster locks, occupancy refusal and runner identity.
Reject force/local fallback, a live or ambiguous runner, unsupported boot
mode, topology/network/disk mismatch, or a missing expected disk. Require
`preserve=true` for every managed disk; this path must not exploit OSVM's
create-if-missing behavior. Start the services VM only. Keep node1, node2,
storage1 and any DNS VM stopped and preserve their exact configurations and
all disks. Preserve existing mounts and credentials; do not rotate bundles.
The normal seed wait, Node refresh and credential-printing URL output do not
run. A successful result means maintenance services reachable with the hold
proved, not a usable whole cluster.

#### Fixed initial writer hold

Pass repeated literal `systemd.mask=<unit>` parameters before the services
VM starts. No post-SSH masking race, unit-file modification, wildcard kernel
mask or caller-supplied list is permitted. The fixed set for the inspected
old provider/API composition is:

- `vpsadmin-database-setup.service`, `vpsadmin-rabbitmq-setup.service`,
  `vpsadmin-devcluster-seed.service`,
  `vpsadmin-devcluster-webui-seed.service`,
  `vpsadmin-devcluster-webui-credentials.service`,
  `vpsadmin-notification-templates.service`;
- `vpsadmin-api.service`, `vpsadmin-supervisor.service`,
  `vpsadmin-scheduler.service`, `vpsadmin-password-recovery.service`,
  `vpsadmin-console-router.service`, `vpsadmin-api-wait-online.service`;
- `container@webui.service`, `container@newadmin.service`,
  `container@mailer.service`, plus `nginx.service`, `haproxy.service`,
  `adminer.service` and optional `phpfpm-vpsfree.service` for application
  ingress; the mailer container contains a DB-writing minimal NodeCtld;
- `timers.target`, to suppress the inherited timer graph for this maintenance
  boot, including periodic Rake writers and Nix garbage collection.

The RabbitMQ setup unit is part of the original writer hold. API46
`nixos/modules/vpsadmin/rabbitmq.nix:131` defines a boot oneshot that runs the
initialization script and records completion; the services fixture's mailer
also requires it (`tests/configs/nixos/vpsadmin-services.nix:287-291`). Mask
this exact unit rather than exempting it from inventory validation. Unknown
writers, aliases, automatic Rake callers and activation triggers still refuse.

For this pre-deployment completeness fix, retain `VERSION=1`, `mask_policy=1`
and runtime transition policy 3: the record fields/phases, residency evidence
and preserving-seed marker are unchanged. No selected maintenance package or
deployed profile hold exists; the failed disposable hold never reached masked
boot. An older boot is not evidence that the added mask was present. Retry
must revalidate the resident and inject the full current list; copy-only must
still check the actual hold before and after copying. No live adoption of an
unproved earlier mask set is authorized.

Extend the existing fixed-mask/unit-inventory regression to require this
literal unit exactly once, retaining all refusal tests and the 2047-byte
complete command-line bound. The parameter adds 45 bytes including its
separator. Validate the current helper against both actual sealed closures
before the existing native rerun. Its `check_masks!` already derives command
line, generator symlink, masked load state and inactive state checks from
`MASKS`; it must prove the added unit too. This adds no test mode, list registry
or separate VM scenario. Application/test edits remain implementer-owned.

Absent optional units may be masked harmlessly. SSH, network/test-shell,
MariaDB and the Nix daemon remain available. This is an application-writer
hold, not a byte-for-byte immutable guest: MariaDB crash recovery and ordinary
OS bookkeeping can write. No regular/storage guest is running to write the
DB. Do not expose this mode as normal application availability.

The aggregate timer mask is deliberate: `api/rake-tasks.nix` gives Rake
services only `After=vpsadmin-api.service`, not a requirement on the API.
Masking the API therefore does not disable them. Each enabled task below is
`vpsadmin-api-<name>.service`, with the same `.timer` when configured:

```text
migrate-db migrate-plugins
 auth-tokens user-sessions report-failed-logins migration-plans mail-process
 monitoring-check monitoring-close monitoring-prune incident-reports
 oom-reports-run oom-reports-prune purge-clones vps-status-logs-prune
 dataset-property-logs-prune dns-transfer-logs-prune daily-report
 mail-user-expiration-regular mail-user-expiration-forced
 mail-vps-expiration-regular mail-vps-expiration-forced
 users-suspend users-soft-delete users-hard-delete vpses-expire others-expire
 prometheus-export-base prometheus-export-dns-records dataset-expansion-run
 payments-process payments-report requests-ipqs outage-reports-auto-resolve
```

Also account for `vpsadmin-api-prometheus-export-deploy.service`, pulled only
by the two export tasks. Core/plugin migrations and users-hard-delete have
no default timer. Enabled plugin tasks depend on the actual old plugin set.
Derive the applicable exact service/timer inventory from the recorded
closure's unit tree, including aliases, wants/requires and activation
triggers. For this known composition, timer tasks have no independent boot,
socket, path or other automatic caller once `timers.target` is masked; the
untimed migration/manual tasks are not independently started. Assert that
condition rather than assuming every `vpsadmin-api-*` service is disabled.
If an additional writer or trigger exists, refuse until its bounded policy
and exact mask are reviewed. Do not invent a generic dependency analyzer or
silently ignore a new task. No application runner is invoked manually during
maintenance, including apparently read-only API runtime loading.

Keeping the timer graph disabled avoids a long list of repeated timer and
service parameters. Check the complete generated kernel command line,
including OSVM/config parameters, against the selected kernel's supported
length; never tolerate truncation. Reject conflicting `init=`, generator
path overrides, `systemd.wants=`, debug-shell or equivalent overrides in the
recorded configuration. PHP and React BFF stay inside masked containers, so
their normal requirements cannot start either seed or API. After boot check
all required masks and absence of active Rake tasks/timers/containers; missing
or unexpected evidence fails maintenance readiness and permits only a safe
stop/retry. It never authorizes unmasking to obtain readiness.

**Generator gate:** `systemd-debug-generator` implements boot-lifetime
`systemd.mask=` ([upstream contract](https://raw.githubusercontent.com/systemd/systemd/main/man/systemd-debug-generator.xml)).
The pinned NixOS systemd module supports its generator paths and overrides
([OS lock's Nixpkgs source](https://raw.githubusercontent.com/NixOS/nixpkgs/e4bae1bd10c9c57b2cf517953ab70060a828ee6f/nixos/modules/system/boot/systemd.nix)).
Before any real boot, resolve the exact old toplevel's systemd package,
verify its executable `lib/systemd/system-generators/systemd-debug-generator`
and that the selected `/etc/systemd/system-generators` does not override it
with `/dev/null` or another program. The source contract is available; this
design investigation did not inspect the private selected guest generation
and therefore does **not** claim that concrete binary check has passed.
A generic host systemd version is not evidence. The disposable fixture must
prove generator masking before any old seed executes, not merely inspect
inactive units after boot. Any NixOS activation script outside systemd that
loads the API/seed invalidates this supported profile and must be refused.

#### Copy, second boot and interruption semantics

Use one small provider-owned operation record under the existing cluster
state/lock, not a new catalog: version, mode/phase, resident config path and
digest, expected services toplevel and residency-evidence reference, held-unit
policy version, and nullable candidate/next-boot config paths/digests plus
verified copied services toplevel. Reuse the existing cluster/socket/package
identity. Record the hold before spawning; retain it through stop/failure.
After boot bind readiness/copy evidence to that runner and guest boot ID.
Expose bounded mode/phase and selected/copied/active distinctions in status;
never report the new selection as activated merely because it built.

The helper's boot check compares its caller-supplied tuple with the persisted
tuple; the public CLI must obtain the current runner/start identity and guest
boot ID. It cannot infer a new boot from an old tuple supplied twice. After
reboot, the observed new tuple must refuse copy against the old record; after
readiness binds the new tuple, the old tuple must refuse. Refusals preserve
the record. Rebinding clears prior candidate/copy proof before a new copy.
The native fixture and existing identity unit regression must test this
ordering, without changing the helper or adding a discovery mechanism.

`update ... services --copy-only` is allowed only under the proved maintenance
hold. Build the reviewed enabled-profile closure, validate its preserving
seed and compatible schema/scheduler/DSL inputs, and use existing authenticated
`nix copy --to ssh://...` transport. After copying, verify the guest store
contains the complete target closure and exact `init`; retain it through the
controlled restart using a provider-owned Nix GC root. This operation does
not call `switch-to-configuration`, set the system profile, restart/unmask
units, refresh Nodes or load the API. Recheck hold and boot/runner identity
before recording copy success. Failed or interrupted copy leaves no success
receipt and no release authority; repeating the copy is safe.

Before copy transport, require one provider-generated preserving-seed contract
in the evaluated candidate's labels. Preserve the existing string-valued label
convention: `labels.vpsadminPreservingSeed` is a JSON-encoded string containing
exactly `{"version":1,"existingAssignments":"preserve"}`. Parse it strictly;
missing/unsupported version, malformed shape or another policy refuses copy
and release. This policy covers existing namespace/map associations, personal
resource-package assignments and allocations: validate/preserve existing rows;
defer missing namespace allocation to the accepted post-readiness chain.
It does not assert scheduler/DSL compatibility or whole-cluster readiness.

Emit this marker only from the **same enabled-profile seed preservation
selection** that chooses the actual preserving implementation. A Git revision,
profile flag without that implementation, or independent caller-supplied label
is insufficient. Disabled/old seed selection emits no marker. Bind the checked
label to the candidate config digest and copied services toplevel, carry it
into the recorded next-boot config and recheck it before `start --copied-config`.
Keep the existing scheduler/DSL deployment gate. Provider tests must prove
marker/seed-selection agreement, preserved nondefault existing assignments,
disabled absence and all refusal cases; a label-only fixture does not prove
seed preservation. No broader capability registry is added.

Create the next-boot configuration through the provider: replace only the
services machine entry with the copied candidate, preserving every other
machine entry, topology/network and disk mapping from the recorded resident
configuration. Reject changed disk ownership/device paths, accidental fresh
disk replacement or incompatible credential/mount layouts. Within disk
descriptors, permit exactly one producer-driven difference:
`machines.services.rootDisk.image`, the source image of the rebuilt closure.
Keep its device, resolved retained path, type, create/preserve flags, size and
layout identical; require `type=file`, `create=true`, `preserve=true`, and the
existing positive-size retained file. Every other disk descriptor remains
identical. The changed image is not copied onto the retained disk: OSVM
`prepare_disks` skips it when preserve=true and the destination exists
(`osvm/lib/osvm/machine.rb:800-817`). Missing/empty/replaced or mismatched
retained disks refuse; no missing-disk creation or fallback is authorized.
Recheck all expected disks immediately before runner construction and recheck
each started machine's disks immediately before its OSVM `start` call, under
the existing operation ownership. This covers a disk disappearing between
validation and construction/start without changing OSVM or adding a physical
file graph. Networks, mounts and all nonservices machine entries remain exact.

`tests/make-test.nix:273-286` also emits `qemu` as a **package directory**, not
an executable path. Validate the executable appended by the selected OSVM
runtime: at pinned `8d05dc3a`, NixosMachine uses `bin/qemu-kvm`
(`osvm/lib/osvm/nixos_machine.rb:14-25`), possibly a package-provided alias;
do not assume that the JSON value itself or an invented binary name is the
command. Regression fixtures must allow a rebuilt services image source with
a preserved sentinel, reject every other disk/layout change, and reject a
missing disk after construction but before start without copying an image.
A new complete cluster build alone does not prove that other retained guests
contain its closures.
Root both immutable config artifacts while the operation is pending; current
`stop` removes `result-config`, so that link cannot be the only reference.
No operator edits generated JSON, guest disks, units or runner arguments.

After successful copy and private DB backup, normal supported `stop` ends
the masked boot. `start --copied-config` requires the completed matching copy
record, all old owned processes stopped and the exact retained disks. It
boots that recorded next configuration, with no maintenance masks, so the
**new** preserving seed runs. It does not rebuild from potentially changed
worktrees/config on the way in. The new seed's preservation checks must
complete before normal API/Supervisor availability; only then run normal
Node refresh/readiness and mark the operation released. A changed or missing
candidate, incomplete copy, failed seed, or unknown activation remains a
recovery state. Retry the same masked resident boot/copy or diagnose while
stopped; never fall back to the old seed, reset or delete disks. If the new
boot may already have changed schema/state, re-evaluate software compatibility
before choosing any old resident generation for masked recovery.

While a hold is pending, plain `start`, normal `update`, `restart` and
`refresh` must refuse, including after the helper/runner crashes. Supported
status, stop, maintenance retry and copy-only remain available. Package
switch/rollback must preserve and understand this pending mode or refuse;
do not downgrade to a helper which ignores it. Keep normal lifecycle lock
and package-generation checks, and cover this with the provider's existing
package-transition contract. This prerequisite does not authorize lifecycle
changes, operator SQL correction or restoring an old DB over newer user work.

#### Assembled workspace package source choice

The lead selected reuse of the clean, registered `workspace` worktree and
`2026-09-23-storage-redesign` branch for the final generated provider pin.
The lead reports the old head `3f539b0f6f034a77dd31efacb7044751237809df`
is retained under
`backup/2026-09-23-storage-redesign-workspace-instructions-before-storage-profile`.
The existing path, portal name, branch registration and `initial_base_sha`
are unchanged; that base remains historical registration metadata, not the
base of the new pin review.

The lead completed the normal pinned-Nix/Git empty rebase onto committed local
`master`, `508064ed951e5efc78131dd09d006586280d9285`, using the exact old head
as upstream. The registered branch then pointed to `508064ed` with a clean
worktree. No old instruction or pin payload was replayed; shared `master`, its
index and unrelated working changes were untouched. This ordinary
unmerged-history consolidation avoided helper alias changes and retained the
superseded history through the backup ref. These are lead-reported operation
results, not an architect rerun.

The fetched predecessor `origin/master` remains recorded as
`c5d8bed5fcd3bc01ce18831ea680aac7edfd68ee`; local `508064ed` adds six committed
coordination-record commits, with identical relevant runtime, AGENTS, flake,
configuration and procedure bytes according to the lead's comparison. One
generated provider pin, evaluation and package activation were pending the
final provider. Subsequently, the lead reports shared `master` advanced from
`508064ed` through `537a9b60` to `58df04cf`, solely for unrelated committed
session tracking and notes; source/procedure bytes are unaffected. The lead
completed the normal pinned-Git rebase: the registered package feature
was clean at `58df04cf76d1bf424dd4cb2a21585708fa38e7d4`, with fetched
`origin/master` `c5d8bed5` still an ancestor, the exact old `3f539b0f` backup
preserved and shared `master`/index untouched.

An earlier lead-reported normal pinned-Git rebase moved that clean consumer
feature from `58df04cf` to prepared base
`8990ecca0cea7a3b59dd88e31138b177500bc43a`, a shared-master coordination commit.
SSH-fetched `c5d8bed5` remains an ancestor; relevant flake/input/procedure/
configuration bytes have no difference. Shared-master HEAD and index digest
were unchanged before/after the operation, the feature is clean, and the
exact `3f539b0f` backup, path/name/branch registration and historical initial
base remained intact. That completed consumer pin was `492fdf8e` and its
actual inventoried review base is `8990ecca`, with one commit and two paths
as recorded in the current checkpoint. This uses the final pin inventory,
not registration `initial_base_sha`. Re-establish the actual base if another
rebase follows. Retain `508064ed` and `58df04cf` as earlier source checkpoints.
The URL/generated lock changed only the recorded provider/runtime metadata;
no package activation occurred. Native `45d7ce88` services fixture acceptance
and consumer no-build verification are complete. Consumer review cleared
all four HIGH lanes without findings. Package realization and contract-byte
proof passed at exact `492fdf8e`, and normal SSH feature publication is
complete. The package remains unselected; full-cluster release is separate.
This source checkpoint adds no schema, helper, interface or
verification scenario and does not change the recorded review lineage.

The subsequent user-authorized rebase replaces that candidate with exact
consumer `6d1b9c4d63d900dbe8fe5b8790c8f92b28ab0b25`, actual review base
`93389c3373647fb3dc2d7ee15efa9acb93a8c62f`. The complete composition review
and new package proof passed as recorded above. The lead confirms root feature
publication, exact remote dependency-anchor readbacks and public
capture-comparison at that base/head are complete; remote master is unchanged.
That was the completed pre-activation checkpoint. The user subsequently
reported activation and approved workspace/master integration conditional on
verification. Verification and the equivalent final replay/merge at `1fa9c982`
are now complete as recorded above. Historical registration metadata and
backups remain evidence, not the final review base.

#### Activation handoff boundary retained as historical procedure

The lead-reported review and verification prerequisites above are complete
for exact consumer `6d1b9c4d`; root publication and comparison are also
complete. The following describes the handoff before the user's activation
report; it is not an instruction to switch again. The lead completed the
public verification and authorized integration described above.

Finish the existing source checks, complete independent review and resolve its
findings, run the required host-migration/retained-services VM checks, and
prepare the final generated pin and checked composed package before the final
activation handoff. No package switch is executed or scheduled by this note.
Normal activation uses the installed public `workspace-host switch --source`
with the exact reviewed `worktrees/2026-09-23-storage-redesign/workspace`
source. The user/operator runs it from an external terminal after this lead
turn and ready team members have become idle. The switch also visits ready
sessions in other registered workspaces: their leads/members must be idle and
the operator must account for the normal terminal/service rebind. Do not stop
sessions, manually quiesce them, force a refusal, or arrange a delayed switch.

This boundary follows generic `2b67af62`: `workspace-host:622,1877-1903`
performs session quiescence; `dev-session:7763-7804` can replace a managed
terminal client before checking lead/team idleness and restores it on refusal.
The active agent turn therefore cannot safely use switch as an idle probe.
The selected public provider wrapper takes a shared transition lock and checks
the originating package against the selected profile before dispatch
(`workspace-host:1153-1180,2639-2694`; `nix/workspace-portal.nix:345-353`).
The new provider's operational commands require selection of the complete new
package; invoking its unselected store helper/runner is not a supported bypass.
The host's own candidate `transition-adopt` preflight is part of normal switch,
not a separate operator entry. On refusal, preserve state and diagnose through
the public command; after profile selection, recover forward with the same or
a newer reviewed compatible package. Resume session work after the external
operator reports the result and the public selected-generation checks pass.

#### Canonical runtime policy prerequisite and verification

The lead selected the existing monotonic transition-policy mechanism. Verified
canonical `dev-workspace` default `4bec20165387d567b761e43b11fdeabb096618d7`
declared schema **1** / policy **2** at the initial inspection; policy 3 was
not reserved there. The same-session `dev-workspace-maintenance-policy` branch
now has one published feature commit,
`2b67af62b40149e7554bab0c31b139cd52c963c1`, declaring policy **3** with outer
schema **1**, tracking limits and other policy fields unchanged. The default
remains `4bec2016`; no default integration or old instruction branch revival
is included.

Lead-reported verification: independent review cleared the original range
`4bec20165387d567b761e43b11fdeabb096618d7..8b2439938cbcbe527f2c703d88ed3c9f72f44b7e`
in all four HIGH-risk lanes, with no Blocking/Important findings or migrations.
The direct remediation then replaced unsafe reset advice with preserving
retained state and selecting a reviewed compatible package. Its focused check
passed 1 run / 26 assertions; normal amend and SSH publication produced the
final commit above. The source manifest and one-commit shape were also checked
read-only by the architect. Final paths are exactly:

- `portal/internal/session/runtime-contract.json`: canonical policy 2 to 3.
- `test/workspace_host/profile_transition_test.rb`: focused compatibility tests.
- `docs/workspace-portal.md`: policy and retained-state recovery contract.
- `libexec/workspace-host`: refusal-message string only; enforcement algorithm
  unchanged, no migration.

The final head includes that direct remediation after the original reviewed
head; this note does not claim a second independent review of unchanged lanes.
The generated provider input update is committed as
`da058353ac4a43f08313d02b485c1578f3547378` (`flake.nix` and `flake.lock` only).
Lead reports only the four `dev-workspace` revision/hash/time/original-revision
leaves changed, with other lock nodes preserved. Provider implementation
remains a draft; no package deployment or cluster boot has occurred for this
prerequisite.

The existing generic host compares schema/tracking fields exactly and requires
target policy at least its own (`libexec/workspace-host:2310-2355`), then
invokes the candidate provider's `transition-adopt`. Forward switch checks at
line 609 precede activation; activation repeats the check at line 870. The
old provider only validates socket/runner ownership and would ignore a new
maintenance record. Policy 3 therefore pairs the host's existing gate with
maintenance-aware provider adoption/refusal; publishing the number alone
does not make an old provider understand the hold.

The deliberate consequence is **package-wide old-policy switch refusal while
any registered development-cluster state exists**, even if this maintenance
hold has completed or the remaining state belongs to another provider.
It is not merely a pending-hold check. Existing schema-1 state can be adopted
forward by the reviewed policy-3 package without disk conversion/reset.
Do not reset retained clusters to evade a downgrade refusal. With no cluster
state, this particular guard does not apply; other package constraints remain.
Ordinary `workspace-host rollback` already refuses unconditionally
(`libexec/workspace-host:901-905`). Recovery uses the same or a newer reviewed,
maintenance-aware package. Old `--from-candidate` recovery/store helpers are
outside this supported recovery procedure: their own old checks cannot prove
the new hold. No universal downgrade guarantee or new current-side mechanism
is claimed.

Canonical ownership/export paths are `portal/internal/session/runtime-contract.json`,
`flake.nix:51-62` (`lib.runtimeContract`) and
`nix/workspace-portal.nix:282-283` (installed host contract). With the generic
source gate complete as reported above, the provider's generated input update
now selects published `2b67af62` in `da058353`; unrelated inputs are preserved.
Provider `flake.nix:62-69` and `nix/organization-tools.nix:101-102` must consume
the same canonical contract as the packaged generic host; do not hand-edit
only the copied provider JSON. Activate only the complete reviewed composition
of policy-3 runtime and maintenance-aware provider. Lead owns registration,
publication and package activation; no default-branch integration is included.

Focused generic tests are in `test/workspace_host/profile_transition_test.rb`;
`test/support/workspace_host_test_case.rb` and README were not changed.
The owning explanation is in `docs/workspace-portal.md`. The implementation
retains the following acceptance contract; assembled provider package checks
and maintenance acceptance remain pending after the committed input update:

- Retain the forward compatible/higher-policy case and establish the
  policy-2 predecessor accepts schema-1/policy-3 candidate contract.
- From policy 3, a target declaring policy 2 refuses **before** profile
  selection, consumer quiescing or candidate adoption while cluster state
  exists. Cover ordinary state with no hold as well as a hold-bearing fixture;
  proving refusal must not require reading or changing provider-private data.
- Equal/newer supported policy still invokes candidate adoption; its refusal
  aborts activation. Schema mismatch and malformed/missing contract remain
  rejected. No-cluster-state behavior and unrelated metadata stay unchanged.
- Run focused tests in the repository Nix environment, e.g.
  `nix develop -c ruby test/workspace_host/profile_transition_test.rb`, then
  its normal hooks. Inspect the final packaged host/provider JSON pair for
  schema 1/policy 3 after the generated input update. Provider tests separately
  prove hold preservation and unknown/malformed-hold refusal.

This is a small prerequisite plus generated provider pin, not a new cluster
state registry. Provider `AGENTS.md:33-38` requires the existing
`nix build --no-link --print-build-logs .#host-migration-test` after review
when the upstream host-state compatibility contract changes. Policy 2 to 3
triggers that gate even though its file arrived through an input update.
Run it once on the final reviewed provider composition under the normal
verification watcher. This existing host-namespace/package integration test
(`flake.nix:231-235`, `nix/tests/host-migration.nix`) is distinct from the new
retained-services maintenance VM fixture below: neither substitutes for the
other, and the host test does not prove guest seed preservation or hold
recovery. No additional VM scenario is requested.

#### Ownership, commit boundary and acceptance

Implementer owns one cohesive provider prerequisite, independent of Admin
scheduler commits: typed CLI forms, bounded runner mode, copy receipt/status,
normal-operation refusals, tests and provider README. Source insertion points:

- `dev-clusters/vpsadmin/bin/devcluster:1051-1174,1176-1211,1396-1446,1545-1556`:
  start/build/refresh, stop GC-root lifetime, update copy/activation split and
  locked dispatch; `lib/runtime.sh` existing ownership helpers remain authoritative.
- `dev-clusters/vpsadmin/lib/devcluster-runner.rb` and shared
  `dev-clusters/lib/devcluster_runner.rb:151-202`: filter services before
  construction/start and pass only the typed fixed kernel parameters. Preserve
  normal vpsAdminOS-provider behavior and cleanup's per-disk preservation.
- Provider `nix/test.nix:423-891,1457-1562,1565-1750`: baked seed writers and
  container dependencies; vpsAdmin `tests/configs/nixos/vpsadmin-services.nix:283-429,520`
  plus `nixos/modules/vpsadmin/api/{default,rake-tasks,scheduler}.nix` and
  `database-setup.nix`: inherited writers, timers and migration/bootstrap.
- OS reference only: `osvm/lib/osvm/machine.rb:87-138,526-543,800-817`,
  `tests/make-test.nix:144-153,278-299` and `tests/configs/nixos/test-vm.nix`.
  No OSVM patch is part of this prerequisite.

Quick provider tests extend `test/devcluster_{commands,runner,status}_test.rb`
and Nix smoke contracts: exact-only argument parsing, stale generation/foreign
ownership/refusal, unknown resident/copy evidence, missing disks, services-only
start, fixed masks before start, no ordinary refresh/URL dump, interrupted
record writes/copy, unchanged source selection on replay, pending-mode
refusals and normal behavior outside maintenance. Verify declared package
transition/schema compatibility and the full command-line bound. Use the
existing Ruby harness and normal hooks; no private runner invocation by the
operator is a supported escape hatch.

After quick checks and mandatory review, a disposable provider fixture must:

1. Populate a retained services disk, change a user's namespace/map and
   personal resource allocation away from the OLD baked seed inputs, and
   preserve a disk payload sentinel. Capture the exact resident configuration.
2. Boot that old closure through maintenance-start. Prove generator masks
   from initial boot, SSH/DB access, no old seed/API/task/mail NodeCtld start,
   no task execution through an accelerated representative Rake timer, and
   unchanged allocation/namespace rows. Exercise dependency attempts to pull
   seeds through the BFF/PHP path and verify refusal.
3. Fail a copy midway; stop/retry maintenance and prove masks/preservation
   persist. Missing target `init`, incomplete closure, mismatched config and
   missing recorded disk each refuse normal release. Kill the helper between
   copy and receipt publication; retry verifies the copy rather than guessing.
4. Complete copy-only, prove no activation and unchanged running generation;
   stop/restart the exact new resident closure normally. Verify preserved
   allocations/namespaces/payload, successful new seed and application readiness.
   Repeat the maintenance/copy sequence and interrupt the normal restart;
   recover without executing the old seed or replacing any disk.

Fixture execution proposal: one provider-owned
`nix/tests/retained-services-maintenance.nix` and
`test/retained-services-maintenance/devcluster-runner.rb`, exposed as the
explicit post-review `devcluster-maintenance-check` app. Reuse the pinned
OSVM dependencies through `dev-clusters/lib/runner.nix`; boot one services
guest repeatedly on the same retained root. Derive old-disabled and
new-enabled closures from the actual provider module and selected API46,
with test-only start counters and an accelerated existing Rake timer. Do not
replace the seeds with a toy SQL writer. The fixture uses real maintenance
policy, systemd, MariaDB, closure transport and OSVM; it is not an operator
escape hatch or a second provider protocol. A test-only loopback network
does not change the public maintenance command's bridge requirement.

The lazy app must build both fixed store-JSON configurations with standard
`--out-link` roots in one private mode-0700 directory outside the native
runner's initially empty artifact directory. Establish the resident root
before starting the candidate build, and retain both roots through the
runner's last use and failure-evidence retention. Printed store paths from
`--no-link` alone do not establish that lifetime. Keep the existing runner
arguments and phase contract; no cleanup engine or lifecycle action is added.

At pinned OSVM/test-runner `8d05`, `TestEvaluator#initialize` always invokes
`TestConfig.build`, which rebuilds through `NixCli`; no prebuilt loader exists.
Use a fixture-owned **constructor-only** subclass initialized from the two
validated store JSON descriptors, fixed packaged script and shared guest
registry. Initialize the upstream evaluator's instance fields/mutexes; a
checked Hash supplies its `[]`/`dig` config interface. Construct a real
`TestRunner::Test` and its one `default` script with one worker/attempt,
`expect_failure=false` and defined example order. Force destructive and
recreate-disks options false. The constructor must not rebuild, boot, create
another guest registry or modify sealed inputs. Keep inherited execution,
assertions, results, hooks and cleanup; no global patch or alternate engine.

The evaluator clones its script context. Share the same mutable registry
with at most one `services` guest; resolve that guest dynamically, not through
a stale cloned instance variable. Reap/check kernel failure/finalize the old
guest before replacing it, and register the replacement before starting it,
so inherited kernel checks and cleanup cover it. The entrypoint must require
the expected nonzero executed examples, no pending/skips, and exactly one
successful default-script result. Returning from `run` is insufficient:
script exceptions become failed result objects, and empty groups can return
success. One ordered end-to-end example can stop dependent stages at the
first failed assertion. This adapter is tied to the inspected pinned runner
interface and remains inside the existing fixture paths.

Preserve OSVM's existing stop/start settle requirement when replacing its
machine instance. Pinned `osvm/lib/osvm/machine.rb:100-108` waits five seconds
from its instance's stop timestamp; the reaper stops/reaps virtiofs and sets
that timestamp after cleanup (`:648-665`). The fixture must keep its own
monotonic stop-completion timestamp after successful existing stop/kill,
kernel check, finalize and cleanup. Before the next fresh instance starts,
wait only the positive remainder of five seconds. Initial boot or an elapsed
gap of at least five seconds needs no delay. Apply this to graceful and
forced replacement alike, retaining the shared registry and registration
before start. The delay supplements reaping; it cannot prove termination or
justify swallowing/retrying a startup failure. Do not alter OSVM, delete PID
files or add cleanup behavior. A focused no-guest check should cover initial,
immediate, partial and fully elapsed gaps, both stop paths, and propagation
of startup failure; the existing native scenario remains the runtime proof.

Record a sorted before/after projection of namespace, block ownership, maps,
map entries, personal package/items, assignment links and effective resource
rows, plus a payload digest and retained-file identity. Count **zero additional
old-seed starts** across every held/copy/new-boot phase, not merely unchanged
final SQL values. Copy completion must leave the old boot ID/current-system
unchanged; the copied boot must select the recorded new toplevel and prove
successful preserving seed plus real API/Supervisor readiness. An interrupted
copied boot retries that same new closure. Keep fault checkpoints in the
fixture, without adding production failure switches.

Make the fixture's interrupted-start observation durable before its stage-5
forced cut. After observing `new-seed-entered`, use one successful guest
command: `rm /var/lib/storage-profile-fixture/new-seed-entered && sync -f
/var/lib/storage-profile-fixture` (one shell line). Keep `block-new-seed`
present so the seed remains in its `ExecStartPre` barrier. The counter append
precedes the observed marker; flushing this filesystem after deletion covers
both that append and removal of the old marker. Flushing only in the counter
script before touching the marker would not persist its later deletion.
The guest command must fail before forced kill if removal or sync fails.
Keep `new-seed >= 2`, changed-boot checks and the genuine forced interruption;
the count proves entries into the seed start barrier, not two completed seeds.
Use the existing real-main/bootstrap probe with a disposable real filesystem
to append instrumentation, run the command and reopen/assert counter retained,
entry marker absent and block marker present, plus failure propagation before
kill. That no-guest check cannot establish power-loss durability; the existing
native reboot scenario must supply it. No alternate test framework, helper,
OSVM, policy or version change is introduced.

This minimal VM fixture does not boot VPS nodes and cannot prove normal Node
refresh. Keep the single-services policy observation at `starting_copied`;
never simulate refresh to claim `released`. Existing command tests cover CLI
sequencing; the already-planned in-place cluster acceptance must additionally
prove the real public command's complete refresh/release path. The separate
existing host-migration target remains required as described above. These
are explicit proof boundaries of the existing gates, not additional scenarios.

The lead owns cold backup, positive resident-generation proof, the actual
binary/generator check, package activation and all cluster operations after
review. These are release gates, not observations made by the architect.
Main storage fixtures then follow the in-place acceptance sequence above.

### Retirement, compatibility and recovery

Retirement uses the enduring enabled-preserving selection
`storageProfile = { enable = true; enrollment = false; }`. No DB retirement
marker or new engine is needed. Existing owned rows mean retirement is still
pending; their proved removal means it is complete. Repeated post-boot
operator cleanup is not the durability mechanism. Keep the same profile
identity, package version and Pool selections through retirement.

1. Select enrollment false and complete the supported services update/restart
   with the preserving overlay. Every API/Supervisor/scheduler process using
   this profile must load the new selection before retirement proceeds;
   changing the host config file alone is insufficient. Extend the existing
   bounded profile `inspect` response with the actual loaded boolean and
   compare it with the desired selection. This is not a new capability
   protocol. Do not overlap retirement with an old active-config writer.
2. Pre-API static bootstrap removes only the exact owned future default link
   under the Environment lock, as above, before new User::Create requests.
   Keep all assigned/shared/personal packages and allocations. Install the
   preserving seed and its unchanged marker and retain the Plan definition
   and its `DatasetPlan` row. Hooks skip new automatic NAS/backup/plan
   enrollment; normal unrelated user/VPS operations retain their behavior.
3. Explicit provision, catch-up, `ensure_*` enrollment and template bootstrap
   refuse enrollment false before creating any rows or chains. The Plan DSL
   also refuses direct registration/verification (`BlockEnv.direction` is
   `:add` or `:verify`), so the direct Plan API cannot bypass hook suppression.
   Its `:del` direction remains available and executes normal removal.
   `retire!` requires false; provision requires true. Check in both the
   public CLI and loaded helper; avoid jq `// true`, which converts false
   into the default.
4. The existing retirement CLI stops scheduler dispatch; let admitted work
   settle. Under admission, Plan and action/task locks, unregister memberships
   normally, require no pending confirmations/locks or remaining template
   users, then remove only owned tasks/actions and `EnvironmentDatasetPlan`
   rows. Reuse idempotent owned-default-link cleanup. Static pre-API removal
   may already have committed; a later retirement failure leaves enrollment
   disabled and remaining scheduling rows intact for diagnosis/retry. The
   bounded retirement SQL transaction remains atomic; unexpected pending,
   fatal or ambiguous state refuses cleanup. No datasets, DIPs, snapshots,
   VPSes, backup roots, packages, assignments or payloads are destroyed.
5. Reload/start the scheduler only after successful retirement validation;
   unrelated tasks may resume and this profile has none to rediscover. A later
   services update or retained boot with enrollment false preserves data and
   does not reinstall the default link, templates or memberships. Failure
   keeps the current stopped-scheduler recovery behavior. Do not switch to
   disabled legacy seed as a recovery or retirement step.

Explicit re-enrollment requires selecting true in a compatible services
generation, then the existing provision path, including Pool readiness and
separate template bootstrap before enrollment. A missing empty template may
be recovered only in that active path after ownership/shape and pending-chain
checks; never recreate it inside source rollback or retired bootstrap.

Required focused regressions: omitted enrollment retains active behavior;
invalid booleans refuse; false retains the preserving marker/config; boot
false twice (including under read_only) removes only the owned future default
and never recreates it or rewrites existing assignments; hooks skip while
direct Plan add/verify and explicit provision refuse; Plan unregister still
works; pending work makes retirement atomic/refusable; retire twice and repeat
static seed/templates/provision attempts without reactivation. Verify all
retained catalog objects/package links/payload fixture records survive and
old active-config/desired-retired mismatch refuses before retirement. These
are regressions within the existing AR/provider/maintenance acceptance gates.

An old scheduler silently misreads the new grammar, and old plan code removes
the last shared template. Before rolling either back, retire the profile's
schedules/memberships using the new code and select compatible config.
An ordinary supported API/Node rolling update retains legacy command wire
and unsigned observer semantics; all scheduler/plan-writing API processes
must support this option before enrollment begins. No fleet-wide Node/OS
upgrade is needed. Keep existing additive schemas on software rollback;
never run migration down or reset the freeze singleton.

On provisioning/transfer failure retain ordinary locks, confirmations and
evidence, identify the failed phase and resume through supported commands.
Do not blind-retry failed Pool::Create against an unknown existing root, or
delete it to make a rerun pass. A matching guest-generation rollback is not a
DB rollback and must not erase new user work. Report the actual scheduler and
enrollment state if recovery cannot restore them safely.

### Evidence anchors and documentation handoff

Source anchors inspected at vpsAdmin `e65a5a6b`:

- `api/lib/vpsadmin/scheduler/{cron_task,daemon,server}.rb`: original integer/
  wildcard parser, three-hour reload and queued-only `run-task` reply.
- `api/lib/vpsadmin/api/dataset_plans.rb:21-140,198-231`: shared group/task
  creation/removal, one task/action, destination selection and confirmations.
- `api/lib/vpsadmin/api/resources/dataset.rb:792-835`: direct plan API paths;
  `api/models/transaction_chains/dataset/migrate.rb:468-503` and
  `vps/clone/base.rb:70-109`: user-add gate and copied memberships.
- `api/models/transaction_chain.rb:82-113,140-168`,
  `transaction_chains/dataset/create.rb:99-105` and
  `libnodectld/lib/nodectld/confirmations.rb:101-109`: staging/nesting and the
  reused-Dataset creation-confirmation hazard.
- `api/models/transaction_chains/dataset/{backup,rotate,send}.rb` and
  `api/models/dataset_action.rb`: rotation, common-base preservation, full/
  incremental paths and empty-group execution.
- `api/models/transaction_chains/user/create.rb:13-79` and
  `api/models/cluster_resource_package.rb`: default resource assignment and
  shared-package recalculation.
- Provider `dev-clusters/vpsadmin/nix/test.nix:617-655,748-891,1457-1488`
  and `bin/devcluster` refresh/update paths: regular-only Pool seeding,
  repeated user mutations and startup ordering. The installed source is
  evidence; the implementer changes its owned repository, never the store.
- Production config `configs/vpsadmin/api/{hooks.rb,dataset_plans.rb}` and
  API fixture `tests/configs/vpsadmin/api/{hooks.rb,dataset_plans.rb}`:
  production behavior versus the smaller existing fixture adapter.

Lasting generic syntax/plan semantics belong in vpsAdmin docs; reusable profile
configuration, provisioning, recovery and limitations belong in the provider
README. Exact revisions, private acceptance artifacts and rollout results
belong in the lead's session records. This brief adds no implementation or
verification result and leaves production/shared/default integration off.

## Historical current-default rebase and React cluster brief

Everything below records the preceding rebase/rebuild scope and its evidence.
The completed reset authorization does not apply to the current populated
cluster or storage-profile implementation. Preserve this history; use the
current contract above for new work.

## Scope and authority, 2026-10-01

This is the architect's implementation and verification brief for the user's
authorized rebase of active storage feature branches and redeployment of this
session's disposable cluster with the new React WebUI component. The lead's
subsequent instruction selects **reset and clean rebuild**: the user explicitly
permitted resetting this cluster and said they had not changed its data. This
replaces the earlier retained-disk upgrade proposal. It does not authorize a
session lifecycle change, integration into default branches, or a shared-host
deployment.

Keep the storage feature at its present advisory boundary. Production strict
dispatch, node quiet, repair readiness, executable reconciliation and APPLY
remain off. Keep PHP storage-freeze controls and direct-admin API access. Do
not implement storage-freeze controls in React for this task.

Readers: implementer, lead, independent reviewer and disposable-cluster operator.
The [plan](plan.md) and [state](state.md) own sequence and executed results;
[storage-integrity-design.md](storage-integrity-design.md) owns the storage
architecture and future maintenance/repair gates. The [previous G1a trial](g1a-dev-cluster-trial.md)
remains historical evidence and must survive the reset. This document contains
the acceptance contract and explicitly attributed execution checkpoints;
the lead owns detailed state, rollout and provenance records.

### Execution checkpoint reported by the lead, 2026-10-02

Whole-branch reviews and SSH feature publication are complete for vpsAdmin
`e65a5a6b`, OS `8d05dc3ae` and configuration `5eff`. The exact vpsAdmin API CI
workflow `36925295017` passed all 27 jobs; broader CI is queued.

The first owned clean start built and booted, then failed at the generated
dev-user seed because the added level 99 lacked a namespace. Both consumed
migrations and the freeze singleton were already valid. After checking the
available namespace range, the lead completed the private configuration and
ran the supported services update successfully (exit 0, including refresh).
No source/migration correction, further reset or manual DB seed was used.
A disposable credential was replaced privately and its supported services
update also passed. All services/seeds, the three selected Node generations,
actual osctld `gc_trash_v1` responses and activated nginx/BFF package paths
were proved as recorded in [state](state.md). Served frontend/BFF metadata
matched, with the supported unknown embedded revision reported honestly.

The diagnostic browser trial passed at these exact sources:

- vpsAdmin `e65a5a6b0f227f78cdcd40afa6a8de1f5b497b36`;
- vpsAdminOS `8d05dc3ae1fb71c1385609990acdf093af49ceec`;
- React `aa2f60b89df65d2f987be48784ed42bab7010833`.

The lead reports exit 0, 242 checks and about 46 seconds in the private
`browser-acceptance-php-diagnostics.log`: real React login/API/logout and
anonymous 401; PHP login/status/freeze/unfreeze; stale and same-mode CAS 409;
anonymous 401/nonadmin 403; and valid Pool Create refusal 423 with unchanged
rows. The trial advanced epoch 2 to 4 with exactly two new audit events and
`recovery_attempted=0`. Independent guest SQL, also reported by the lead,
confirmed `read_write`, epoch 4, four total audits, exactly one singleton and
both consumed migrations applied. The compact runtime gates are complete.

Preserve the earlier attempts separately: the token-route helper error was
corrected, but the earlier PHP unfreeze failure remains unexplained. Its API
recovery was not PHP verification, and the later diagnostic pass does not
establish a root cause or an application fix. Broad CI is still queued and
the upstream React nightly remains residual evidence to assess separately.
The architect has not rerun tests or inspected generated seed configuration,
credentials, private browser logs or the running cluster. Production strict,
node quiet, repair readiness and APPLY remain off.

## Source selection and ownership

The following defaults were fetched and reported by the lead on 2026-10-01;
the architect inspected their local Git objects. Save exact old/new refs and
range comparisons before any rebase. Recheck the default if it advances before
the final candidate is selected.

| Component | Existing session head | Fetched default / action |
| --- | --- | --- |
| vpsAdmin | `fa7cec3a89e433e91516a369f10b1b17b6eddfef` | Rebase onto `origin/master` `90184b374ce0a139319b66326a29373b92d8ee93`. |
| vpsAdminOS | Registered `dcad075a171244cc17d67d625ab89c402d11781e`; reviewed staging port `107cef01f` | Use current `origin/staging` `26f28c69149b5312305aceb7f5614bd1d3fe3bbc` plus one copy of the reviewed provider patch. Prefer replaying the staging port; do not put the old `dcad` lineage over current staging. |
| Site configuration | `fc203cb0ff260d741f14a6c446b3d543e9eb06d2` | Rebase onto `origin/master` `029c616ed906de80b8813cc20391e294c3e9f4c2`; preserve current channels and the separate React host. No host switch. |
| Maintenance tasks | `a457cfc3aa4431565d65d6bbe9f4e63f8d8d327e` | Default `2fdc9f2889ac419136cd0cde0e0955c015ae7107` is unchanged: already based on current default; no artificial rewrite or script execution. |
| React WebUI | No storage feature needed | Select published default `main`, `aa2f60b89df65d2f987be48784ed42bab7010833`, through the existing provider's same-session source override. |
| Workspace / extension | Superseded session instruction branches | Retain their refs for provenance. Do not revive, merge or repin them. Use the installed current provider. |

The vpsAdmin default delta since the original base `486350466` consists of
fourteen Ruby/PHP dependency lock/packaging files. It does not extract PHP into
the React repository. `vpsadmin-webui/AGENTS.md` and `README.md` explicitly keep
the API and legacy PHP UI in vpsAdmin. The PHP freeze forms, page, cs/en catalogs,
PHPUnit test and Playwright admin-cluster test therefore stay in vpsAdmin.

The inspected OS default delta `af9543a54..26f28c691` changes only `flake.lock`.
The reviewed staging provider port is based on `af9543a54`; reapply its source
patch while retaining current staging inputs. The original provider branch is
based much earlier and must not discard the staging lineage. Preserve the
unrelated untracked `libosctl/tmp/` in the registered OS worktree. The lead owns
ref backups and branch selection; implementations must not duplicate provider
commits or reset shared/unrelated work.

## Existing React integration: no new application feature

The installed vpsFree development-cluster extension already contains the
integration in `dev-clusters/vpsadmin/{flake.nix,nix/test.nix,README.md}`.
It is separate from vpsAdmin's own `tests/configs/nixos/vpsadmin-services.nix`.

- Enable `newWebui.enable=true` and a distinct `domains.newadmin` in this
  cluster's private config. Keep `storage` topology and `bridge` networking.
- The provider's built-in pin is older WebUI
  `534caa83a5f97d2b40b4a126886649b14dc9e8d3`. The lead selects published current
  default `aa2f60b89df65d2f987be48784ed42bab7010833` for this rebuild. Use the
  registered clean same-session `vpsadmin-webui` source override and check both
  immutable packages. This needs no new WebUI behavior patch. The lead owns
  worktree/ref setup; do not silently rewrite the installed provider pin or
  borrow another session's worktree.
- Provider input `vpsadminWebui.inputs.vpsadmin.follows="vpsadmin"` binds the
  frontend/BFF reference to this cluster's selected API. Its `nix_overrides`
  binds both `vpsadminos` and `vpsadmin/vpsadminos` to the selected OS source.
  Frontend and BFF must come from the same input and have matching build-info;
  the accepted path-source provenance boundary below applies.
- The provider owns the new `newadmin` container, TLS frontend routing, private
  nginx port 18082, loopback BFF port 3001, cluster CA trust and API version 7.0.
  Use these existing interfaces, without a parallel hand-written proxy/seed.
- A separate nondefault OAuth client preserves the PHP default client. The
  provider owns the private credential bundle and seeds the exact callback
  from the selected newadmin origin. Do not print credentials, cookie values,
  OAuth codes or tokens in build/test reports.

The site configuration has an independent `vpsadmin-webui` channel mapping to
`vpsadminWebui`, with `inputs.vpsadmin.follows="vpsadminServices"`. Preserve this
new upstream graph and host while rebasing the storage service pin. It does not
select this disposable cluster's React package. Likewise, its
`vpsadminServices` input follows separately pinned `vpsadminosStaging`; a service
pin alone never upgrades osctld. No site OS or React channel update is required
to start this disposable component. A later exact feature pin, if needed, uses
`confctl inputs channel set --commit`, not hand-edited `flake.lock`.

### Accepted path-source provenance boundary

The supported same-session override passes `path:<worktree>`. A clean selected
Git checkout does not guarantee that Nix supplies `self.rev`: WebUI
`aa2f60b:nix/provenance.nix` then emits `commit="unknown"`, `dirty=true`,
`source="unavailable"`. Its package checker explicitly accepts this form and
requires frontend/BFF metadata equality
(`scripts/check-package-contents.mjs:28-43,112-115`). This is acceptable for this
disposable functional trial; it is not evidence of a known clean release build.
Do not rewrite build-info or present the provider's Git selection label as
package metadata. No new packaging feature is required.

Record separately at build/activation time:

- Selected full Git SHA and tree ID, with clean status before and after the
  build; keep that source unchanged while the build runs.
- Evaluated frontend/BFF derivation and output paths, and the filtered source
  store path plus NAR hash consumed by each derivation. Record any BFF source
  subdirectory explicitly. An output hash alone does not prove a Git revision.
- Activated nginx root and BFF executable/package paths; served frontend
  `build-info.json` and installed BFF `share/vpsadmin-webui-bff/build-info.json`
  must agree. Record their actual fields, including unknown/dirty/unavailable
  when present, alongside the separate source-selection evidence.

This evidence binds the selected `aa2f60b` source and the deployed pair without
claiming that embedded metadata contains a revision it does not contain.

### Minimal history and pin order

Proceed with independent clean rebases while pins are coordinated. Rebase the
reviewed OS provider first, verify/review its complete delta on current staging
and publish the selected provider feature head. Rebase the vpsAdmin feature
series concurrently as appropriate; keep its runtime and both migration blobs.
Replace the old provider pin with **one logical generated pin commit** selecting
that new published OS head, using `tools/update_vpsadminos_flake.sh`. Do not keep
an obsolete old-provider pin followed by a corrective new-provider pin in the
final rewritten series. Review the complete final vpsAdmin base-to-head series
and publish its exact candidate.

Checkpoint reported by the lead: the whole OS branch
`26f28c691..8d05dc3ae1fb71c1385609990acdf093af49ceec` passed its four-lane
independent review as one commit with no migrations; the normal signed SSH
lease push succeeded and the remote exact head was confirmed. The vpsAdmin
old-pin removal/replay reached `0bdd6caaa4aadfc16b5f124f16b7b5bb102bc0ed`,
with all 18 retained entries patch-equivalent and no non-lock delta reported.
The architect's read-only comparison also found no `api/db` delta from
`fa7cec3` at that intermediate head. The updater produced final candidate
`e65a5a6b0f227f78cdcd40afa6a8de1f5b497b36`; its source conformance is recorded
below. The lead subsequently reported whole-branch review and feature
publication complete; the later runtime result is recorded in the execution
checkpoint above.

Rebase the site rollout guide onto current config master, then regenerate one
service-channel pin to that published vpsAdmin candidate with
`confctl inputs channel set --commit vpsadmin vpsadmin REVISION`. Replace the
obsolete `fe4` feature pin rather than retaining two successive service-pin
commits. Preserve the new React follows/channel graph and unrelated lock nodes;
inspect required transitive changes individually. Do not update site OS channels
or deploy shared hosts. The lead's inventory reports no application-source
overlap in the vpsAdmin dependency-only upstream delta; the OS test-registration
overlap in `tests/all-tests.nix` must retain both upstream tests and the provider
test. Pin coordination must not hold those otherwise independent clean rebases.

### Final pin and migration conformance, e65a5a6b

The architect's read-only Git/source assessment found no conformance blocker:

- There are 19 commits above `90184b374`. The final generated commit changes
  only `flake.lock`, replacing the original `8e44a5124` pin directly with
  published `8d05dc3ae1fb71c1385609990acdf093af49ceec`. Its recorded NAR hash is
  `sha256-J0GUpTd2OCkPCN0qCl4hQSwZy5HcPl4EljEBKpDEsVY=`. The only other
  changes are the locked revision/hash/time fields of existing
  `nixpkgsUnstable` and `nixpkgs_2`; both match the selected OS's own lock.
  Input mappings, original input specifications and unrelated nodes are
  unchanged. This source check does not independently recompute the NAR hash.
- Relative to `fa7cec3`, the final tree differs only in `flake.lock` and the
  fourteen upstream dependency files. All fourteen equal current default
  `90184b374` exactly. Application source, docs and tests are preserved.
- The branch adds exactly the two consumed migrations relative to the default.
  Both migration blobs and `api/db/schema.rb` equal `fa7cec3`. The bootstrap
  task at `api/lib/vpsadmin/api/tasks/db.rake:2-12` is also unchanged: insert
  singleton row 1 or leave it intact. The fresh setup calls it after schema
  load and before its initialization marker, then runs migrations
  (`nixos/modules/vpsadmin/database-setup.nix:167-182`). Existing setup skips
  bootstrap. Migration `20260924210000:128-135` still supplies the upgrade
  insert. Retain the additive schema on software rollback; do not run `down`.
- Advisory limits remain explicit: `api/models/transaction.rb:204-210` allows
  unsigned observer 5204, while 5290/5291 require signatures. API strict mode
  and the 5215 opt-in still return false; Node `Command` defaults strict
  dispatch to false. Planner output remains non-executable, historical
  coverage unknown, and activity/status output cannot claim repair readiness
  or child quiet. No identity publication or APPLY was added by this rebase.

This assessment ran no tests, evaluated no configuration and touched no
cluster. It does not replace independent review or runtime acceptance; later
lead-reported review/publication and CI results are recorded above.

## Rebase and compatibility invariants

1. Preserve the two consumed migrations **with their existing filenames,
   versions and contents**: `20260924210000_add_storage_integrity_foundation.rb`
   and `20260926100000_add_bounded_storage_capture_indexes.rb`. Compare their
   blobs against `fa7cec3`. Resetting the dev cluster does not make their prior
   consumption disappear. Any later schema change needs a forward migration.
2. Preserve generated final `schema.rb`, fresh-schema singleton bootstrap and
   existing-upgrade behavior. A missing singleton in an established DB fails;
   startup must not reset a frozen epoch or recreate read_write implicitly.
3. Preserve API admin/action-scope/session checks, both-direction epoch CAS,
   append-only transition/catch-up audit, atomic admission and bounded DB-only
   status. Keep `settle_observer` API-only and proof-gated.
4. Preserve unsigned production observer 5204 compatibility, exact Pool/member
   manifests, test-only strict 5204/5215 gates and whole-chain confirmation
   semantics. Rebase must not require a production transaction-signing rollout.
5. Preserve signed 5290/5291, paired registry behavior, inventory framing,
   transient Node exchange compatibility, `(1,1)`/`(2,2)` readers, policy-2
   reports, policy-3 nonexecutable plans and unknown historical coverage.
   Equal samples still do not prove exclusion or child lifetime.
6. Preserve the generic osctld `gc_trash_v1` schema, boot/instance/generation
   semantics and unknown-on-unsupported behavior. A new Node against an old
   provider reports unknown. No provider upgrade turns readiness on.
7. Resolve generated dependency conflicts using current dependency selections
   and project regeneration tools, retaining storage-specific source/gem
   metadata. Do not restore old composer/gem/OS locks wholesale merely because
   they were present in the feature branch.
8. Compare complete old/new patch series and final base-to-head diffs, including
   schema, locale artifacts, CI topic coverage and selector rules. Record any
   semantic resolution; it needs focused verification and independent review.
   Existing migration versions cannot be squashed away. Keep branch backups.

Software rollback returns to saved feature revisions and matching guest system
generations while retaining the additive schema and data. Do not run migration
`down` or select an old API that bypasses admission and then call the system
frozen. React frontend/BFF roll back as a matched pair. Keep the new OAuth
client separate; disabling the new container leaves legacy PHP available.

## Verification brief

The implementer/lead runs these checks; the architect ran none. Use project Nix
environments. Long or uncertain-duration checks belong to a fresh verification
watcher. Complete quick checks and commit before mandatory review; the dedicated
reviewer must assess each complete rewritten branch, migration provenance,
cross-project pins and any conflict resolutions before longer integration.

### Quick source and focused checks

- All affected trees: scoped `git diff --check`, declared hooks, exact old/new
  heads, `git range-diff`, and no accidental unrelated paths. Verify both
  consumed migration blobs and schema version. Keep default refs untouched.
- The vpsAdmin `.#api`, `.#libnodectld` and `.#webui` shells already enter
  their component directory; do not run a second `cd` into that component.
- vpsAdmin API (`nix develop .#api`): `bundle exec rspec
  spec/migrations/20260924210000_add_storage_integrity_foundation_spec.rb
  spec/migrations/20260926100000_add_bounded_storage_capture_indexes_spec.rb
  spec/migrations/storage_freeze_bootstrap_spec.rb`; then focused
  `spec/api/resources/storage_freeze_spec.rb`,
  `spec/models/storage_mutation_admission_spec.rb`,
  `spec/models/storage_observer_settlement_spec.rb`,
  `spec/models/storage_freeze_status_spec.rb`,
  `spec/models/storage_reconciler*_spec.rb` and
  `spec/models/storage_activity_report_spec.rb`.
- Node (`nix develop .#libnodectld`): existing registry,
  receipt, strict-dispatch, command, node-activity, inventory and 5291 specs;
  broaden to the full component suite only for a concrete remaining runtime
  risk. Keep fixture-only strict mode separate from deployed configuration.
- Legacy PHP: `nix develop .#webui`, `composer install`, then
  `composer test -- --filter StorageFreezeUiTest`; check
  changed locale source/generated pairs and normal PHP hooks.
- vpsAdminOS (`nix develop`, `cd osctld`): `bundle exec rspec
  spec/osctld/storage_activity_spec.rb spec/osctld/garbage_collector_spec.rb
  spec/osctld/trash_bin_spec.rb spec/osctld/commands/simple_delegators_spec.rb
  spec/osctld/commands/heavy_system_spec.rb` and declared hooks.
- CI plumbing: `ruby tests/ci-selection-test.rb` in vpsAdmin; preserve exact-once
  API spec topics and the separate 5215 contract workflow. Evaluate config/pin
  changes with their owning tools. No `confctl deploy` to shared hosts.

No React source change means no new React implementation suite is required.
The selected published `aa2f60b` needs the accepted provenance evidence above
and the real cluster acceptance below. If a packaging/runtime compatibility change becomes
necessary, use its `nix develop` toolchain and affected declared checks, including
`npm run ci:quick`, `npm run ci:tests`, `npm run build` or module/package checks
as appropriate to the change. Record upstream evidence separately from local
results; synthetic browser fixtures do not certify this real dev API login.

### Required post-review cluster gate

- Build/evaluate the exact selected development-cluster configuration, including
  the React pair and provider-preserving OS source. Stop an unexpected local
  kernel build and investigate cache availability under workspace procedure.
- Reset and start this disposable cluster as below. Require real React login
  and API reads, legacy PHP freeze/auth/CAS checks, fresh bootstrap/OAuth ordering,
  Node provider checks and coexistence. Upstream fixture/VM proof does not
  substitute for this trial.

The lead reports the rebased focused checks passing: OS 36/0 with normal Nix
hooks successful, API 62/0, Node 42/0, PHP 5 tests/17 assertions, and selector
18/77. These are lead-reported results, not architect-executed verification.
Whole-branch review/publication is complete for OS, vpsAdmin and configuration,
as is the architect's final vpsAdmin source conformance assessment. The lead
reports the exact-head API CI workflow passed and compact runtime acceptance
is complete: fresh schema/bootstrap/OAuth setup, honest activated package
evidence, real React login/API/logout, PHP/API freeze/auth/CAS/admission and
return to read_write, and Node/provider health. Broad CI remains queued and
the upstream React nightly is a separate residual. The earlier unexplained PHP
unfreeze failure is retained above; no application fix is claimed. This trial
does not add separate VM prerequisites or establish repair authority.

### Residual checks with a concrete trigger

Unchanged source patches plus an OS dependency rebase do not by themselves
require separate backup, migration, provider, PHP or 5215 integration runs
before this disposable trial. Keep their prior results as historical evidence.
Run an affected test if a conflict resolution, focused failure or actual runtime
change exposes a remaining risk:

- `tests/contracts/storage_group_snapshot_v4/run.sh` for changed API/Node
  staging, signatures, receipts or confirmation behavior.
- OS `./test-runner.sh test osctld/storage-activity` for changed provider logic
  or a node-provider failure in the fresh cluster.
- vpsAdmin `./test-runner.sh test 'webui#admin-cluster'` for changed PHP controls
  or a browser failure that requires its isolated fixture.
- `storage/backup-full-incremental` and `storage/dataset-migrate-retain-source`
  for demonstrated transfer/rollback/data-preservation risk; retain their
  file-content assertions. These tests do not clear older unrelated CI failures
  unless those failures are reproduced and investigated explicitly.

## Selected clean rebuild and acceptance sequence

Only the lead/assigned operator executes this sequence. The stopped/stale
preflight state below is historical: the owned clean start has since built and
booted, followed by the supported seed recovery and successful second services
update recorded above. Browser/provider acceptance is complete by the lead's
reported evidence, with the remaining limitations preserved above. The numbered
sequence records the trial's acceptance contract, not a request to repeat it.
Do not repeat reset or run cluster actions as an architect-side verification step.

**Pre-start occupancy history:** the lead's 2026-10-01 preflight found the default
bridge address `172.16.106.53` occupied by another session's active cluster;
this session was stopped then. The user subsequently explicitly requested
releasing those addresses, saying they considered that session done. The lead
assigned a fresh verification utility only the stable command
`vpsadmin-devcluster stop 2026-09-30-portal-review-improvements`. This is narrow
authorization for that cluster stop, not permission to archive/delete a session,
reset its disks, edit its records or change its team. The architect takes no
foreign-session action. The lead reports that the authorized stop completed
with exit 0 and the frontend no longer responded to ping. This records the
reported release outcome, not a permanent reservation or an architect-run
probe. Any later start still requires a fresh address-availability check. Do not use
`--force` or switch to local networking to bypass an occupancy refusal.

1. Before reset, verify exact workspace/slug and retained process/socket/disk
   ownership through the supported lifecycle tooling. Privately preserve the
   current cluster config, selected result-config/provenance, source heads,
   prior generation references and earlier DB backup/trial records. Reconcile
   stale runtime state through supported refusals; do not remove ownership
   metadata manually. Retain Git backups and historical session evidence.
2. The user waived preservation of old VM data. A new old-DB dump or complicated
   frozen in-place upgrade is therefore not a prerequisite. Perform the
   explicitly authorized reset of **this cluster only** with
   `vpsadmin-devcluster reset 2026-09-23-storage-redesign`. Do not reuse an old
   runner to prepare disks, reset another cluster or change session lifecycle.
3. Recreate/configure this cluster with storage topology, bridge networking,
   `newWebui.enable=true` and distinct configured `domains.newadmin`. Preserve
   other reviewed seed/config choices rather than assuming defaults are
   identical. Credentials belong to the provider; after a clean reset it may
   generate a new complete private bundle. Do not combine old DB OAuth rows
   with a different credential bundle. Keep diagnostics private.
4. Start the reviewed sources with
   `vpsadmin-devcluster start 2026-09-23-storage-redesign --topology storage --network bridge`.
   Do not use `--force` to bypass an occupied bridge address. Prove selected OS
   supports rootDisk/per-disk preservation before runtime construction; current
   provider rejects an older incompatible runner. Record selected revisions,
   clean/dirty provenance and actual activated systems separately.
5. Check fresh initialization: schema load, singleton bootstrap, core/plugin
   migrations, ordinary dev seed, runtime WebUI credentials, React OAuth seed,
   then `container@newadmin`. Require successful unit results and both migration
   versions recorded as applied, singleton row 1 exactly once, expected initial
   mode/epoch, and no synthetic bootstrap reset of an existing control.
6. The ordering is source-backed: vpsAdmin
   `nixos/modules/vpsadmin/database-setup.nix:173-182` bootstraps immediately
   after fresh schema load and before migrations; provider
   `nix/test.nix:1513-1552` makes the React seed depend on database setup,
   ordinary seed and credentials, and makes its container depend on that seed.
   A failed prerequisite must prevent the new container starting. Do not
   force-start BFF around these gates or seed clients manually to conceal a
   setup failure.
7. Verify services API/Supervisor/MariaDB/RabbitMQ/nginx and all three nodes.
   Check provider `pool_storage_activity`/`gc_trash_v1` where osctld manages the
   selected pool, preserving unknown child coverage. An absent/inapplicable
   provider remains explicit unknown, never invented quiet proof. Verify actual package/process revisions
   and `/run/current-system`, not just the built result link. Take a fresh
   private logical DB backup and record guest generations after successful
   fresh initialization and before further stateful trial work.
8. New React endpoint: verify trusted TLS and the accepted path-source evidence
   above, including actual frontend/BFF metadata equality; unknown embedded
   revision is reported truthfully. Check `/config.json`, anonymous
   `/session.json`, OAuth login
   with a seeded disposable member and successful actual API data retrieval.
   Verify logout; check that API errors are surfaced and no standalone fallback
   masks BFF failure. Check direct SPA navigation, PHP UI availability and its
   separate default OAuth client. Do not put cookies or authentication URLs
   containing codes into public/session evidence.
9. Legacy PHP/direct-admin API: show the full bounded DB-only status; CAS to
   read_only using the observed epoch and a reason, reject a stale CAS without
   an extra transition, verify a nonadmin is denied, and confirm new
   storage-mutating chains are refused. Use an existing disposable fixture for an
   admission test; do not interpret a missing-resource error as freeze proof.
   Preexisting work settles normally. Return to read_write using the fresh
   epoch and verify one audit event per successful transition. React is usable
   without new storage-admin controls; those remain in PHP/API.
10. Report cluster running/usable, React and legacy URLs, exact component
    revisions, mode/epoch, migrations, observed unit results and limitations.
    `db_drained` remains DB-only; `node_quiet=false`, `repair_ready=false`,
    executable plans/APPLY off and production strict off. No private raw
    topology or credentials belong in this report.

## Failure and recovery decisions

- A build/evaluation failure leaves deployment incomplete. Diagnose source/input
  compatibility; do not select an older OS lineage, alter consumed migrations,
  bypass hook failures or repair the cluster state by hand.
- Fresh DB/bootstrap/OAuth-seed failure blocks acceptance. Preserve bounded
  private logs, identify the failing unit and retry the supported setup path
  after a reviewed correction. Do not reset blindly to hide a migration defect.
- After successful fresh setup, a services regression may use a saved compatible
  system generation and matching frontend/BFF pair. Preserve the additive DB
  and credential pairing. Any DB restore must match the recorded backup's
  schema and client-secret bundle; a guest-generation rollback alone is not a
  DB rollback.
- API release from read_only requires a fresh authenticated epoch CAS. Do not
  reset the singleton or delete intents/locks to make a trial appear drained.
  If normal release cannot be proved, report the actual frozen state and blocker.
- This task does not claim G1b child/orphan exclusion, historical terminal proof,
  production repair approval, or resolution of the retained-lock scale caveat.

## Remaining evidence and implementation boundary

No substantive new application feature is expected. The implementer owns rebase
resolutions, generated dependency consistency and any demonstrated packaging
compatibility fix. The lead owns fetches/ref backups, current plan/state,
review coordination and the exact authorized disposable reset/start. The
architect owns this brief only. Material source deviations return to the lead.

The selected React `aa2f60b` revision, activated package/source evidence and
actual private cluster settings are recorded by the lead; the selected default
and provider's built-in pin differ. Broad CI and the upstream React nightly
remain separate residual checks. Preserve the unexplained earlier PHP unfreeze
failure without claiming that the passing diagnostic trial fixed it.
Upstream WebUI documentation retains some older verification-status text, so
use exact revision evidence and this trial's observations, not broad readiness
claims. Existing provider support, rather than a revived workspace instruction
branch, is the implementation boundary.

## Node RPC cleanup and remote-restore recovery slice, 2026-10-03

**Current authorized scope:** implement the Node reliability correction before
the retained-cluster trial. This bounded slice supersedes the earlier statement
that no new application feature was expected. The implementer owns application
and test changes in vpsAdmin at the current API46 base; the architect owns this
brief. The lead owns verification, review and publication. No default merge,
provider/generic change, new Node wire field, DB schema or production
configuration input is authorized. Preserve the declared PHP test cache.
The separate workspace activation/integration is complete. This brief is a
proposal for implementation, not evidence that the Node correction passed.

### Current implementation checkpoint

**Current lead-reported result:** the independent `148ef..7da` review completed
all four HIGH-risk lanes with no Blocking and two Important findings: the global
publisher wait budget and ambient `$!` exception ownership. Both are resolved by
the saved five-path direct step-9 remediation. This is not a full review rerun.
Normal Nix/Git amendment passed every hook and commit-message check. The runtime
owner is now `d82a6cc1cf25e6e23671ae095880a4478a9d4e18`; the separate unchanged
fixture patch is `290f1ef07972e53c2b5154dbfa8b088802bde619`, tree
`a2de421a02cc0add7a256273133b5dab9a2b2f32`. The first 21 commits and `e882` parent
remain unchanged; the tested five-path correction is 372 additions/26 deletions,
and fixture range-diff is `=`. The before-node-review-remediation backup retains
`7da`. Tracked source/index are clean; the preexisting PHPUnit cache is preserved.

Remediation verification retains the 55/1 protected-setter fixture failure,
its spec-only `send` correction, subsequent 55/0 pass in 19.636s, and the two
then one remaining lint offenses. Final root RuboCop 1.85 passed four files in
13.275s; the full Node suite passed 634/0 in 35.803s, total 51.225s/parity 1
against the final five-file manifest `88cd3edb…a82e`. The owning documentation
writing pass accepted the tested text unchanged. These results are supplied by
the lead; the architect has not read private artifacts or rerun verification.
The **one existing remote-restore integration scenario passed** at exact clean
`290f1ef07972e53c2b5154dbfa8b088802bde619`, tree `a2de421a`.
Lead reports watcher `/root/node_rpc_remote_restore_290f` exit 0 in 1610.195s,
parity 1, four of four examples passing in 172.32s, 265.1s, 172.97s and 51.58s;
the script took 1109.64s. Private evidence is referenced at `/tmp/nrvm.0qykahy0`
and was not read by the architect. The parent independently confirmed the
numeric result, zero QEMU/virtiofs processes bound to that exact test state,
clean tracked/index state and preserved PHPUnit cache.

This is disposable integration evidence for the recorded restart, transfer,
restore and subsequent incremental payload assertions. The original broker
timeout trigger remains unknown; arbitrary live-send crash replay is not proved.
Lead reports final feature publication and remote readback at exact
`290f1ef07972e53c2b5154dbfa8b088802bde619`; remote master `148ef` is unchanged.
The initial ambient push was refused by the Overcommit signature check before
ref mutation. After verifying the existing hook configuration, normal
`.#vpsadmin` signing and the same exact-lease push succeeded, without bypass or
source changes. Exact-head CI `37144608422` and libnodectld `37144608395` started;
the lead found no older queued/in-progress branch run in the 100-run read.
These workflows are not awaited here. The retained/public-cluster maintenance
has since completed public copied-start/refresh/release and all three Node
updates, as recorded in the conditional sequence below. VPS/NAS profile payload
acceptance and retirement remain pending and separate from these results.

Earlier verification and review provenance follows:

Lead evidence: the earlier incomplete focused runs (33/3 and39/1) and declared
lint failure remain recorded in the [review packet](node-rpc-recovery-review.md).
Portable paired directives and removal of redundant Struct keyword initialization
changed no runtime control flow. Fresh Luna/low verification passed root-declared
RuboCop1.85 and the full Node suite618/0, total54.107s/parity1. The frozen nine
source paths then passed CI selector18/77, actual fixture derivation evaluation
and owning Nixfmt, total82.342s/parity1. These are quick source/static results,
not real broker/VM/payload acceptance.

Two normal commits passed all pre-commit and commit-msg hooks (preferred-width
warnings only), then the complete23 patches replayed identically on fetched
master148ef. The original reviewed head was `7da85b7a`, tree `4ae8a7a5`, with
clean tracked/index state and all
nine tested source hashes unchanged; preexisting PHPUnit cache preserved.
Upstream changed only four non-overlapping dependency files (packaged API
parallel2.3 and WebUI dependencies). All23 range-diff entries are`=` and the
full binary feature patch is identical. Scoped final-head fixture evaluation
subsequently passed before the independent all-four-HIGH review. An additional
whole-flake
probe failed on the unchanged baseline `overlays.list` non-function output;
that failure is retained, with no expanded source correction or passing claim.

The bounded source conformance check found no fixture mismatch requiring a
change: scenario-local persisted queue settings, `manageCluster = false` and
the custom startup preserve normal startup while replacing transient queue
patching with a graceful daemon-child restart and keyed JSON scalar checks.
Transfer projections use the actual `input.input.snapshots` envelope and
`output.execute.status`, together with successful done/status fields, the
restored branch/path, receive history, GUID agreement and read-only A/B/C
snapshot contents. These are transaction/payload assertions, not a claim of
retained cryptographic signature evidence: normal chain close clears signatures.
The architect inspected public source only and ran no application checks or
operations; the integration result above is lead-reported evidence. The subsequent independent
review findings and remediation boundary below supersede the earlier pending
review status, without converting the prior checks into remediation evidence.

### Narrow Node review remediation brief, 2026-10-03

**Direct remediation and the existing integration pass completed.** The following
saved brief governed the two Important findings from the completed `148ef..7da`
review. Both were source-confirmed and resolved under mandatory-review step 9;
no broader recovery mechanism was added. Implementer owned exactly five
application paths: `libnodectld/lib/nodectld/{node_bunny,rpc_client}.rb`, their
two existing `libnodectld/spec/nodectld/*_spec.rb` files, and `docs/node-rpc.md`.
Keep StorageStatus/MountReporter runtime, fixture, pins, schemas, wire, production
defaults and docs index unchanged. This brief authorizes no test or operation
by the architect; lead-reported remediation evidence is in the checkpoint above.

**Required publishers at reviewed `7da`:** `NodeBunny#acquire_publisher` created a
30-second deadline for every caller (`node_bunny.rb:219-227`). Ordinary
`publish_wait` must again wait without an imposed recovery/owner-gate deadline.
`StorageStatus#save_properties` (`storage_status.rb:263-279`) and
`MountReporter#report_thread` (`mount_reporter.rb:56-85`) are required publishers,
not bounded RPC calls; do not rescue their failure broadly or drop their message.
Keep optional `publish_drop` behavior unchanged.

Add one explicit internal keyword, `recovery_timeout: nil`, to `publish_wait`
and its publisher-acquisition path. Nil means unbounded gate waiting; RPC
explicitly passes `NodeBunny::RECOVERY_WAIT` even when `stopped` is nil.
Convert that opt-in duration to a monotonic deadline once per gate-acquisition
wait. Do not infer boundedness from the cancellation predicate. Consume the
keyword at NodeBunny's Ruby boundary; neither it nor `stopped` may enter
`exchange.publish` options. Existing message properties must pass unchanged.
An unbounded wait still releases the monitor and observes any supplied stop
predicate; a bounded RPC wait retains the existing one-second stop polling and
typed timeout. Timeout/stop cannot acquire/release another publisher's gate or
acknowledge a retirement. Keep existing transport retries, channel lifecycle,
exact retirement tokens, late-arrival handling and consumer cleanup unchanged.
This bounds individual RPC gate waits, not the whole publish/RPC call, existing
15-second transport retry or synchronous Bunny operation.

In `node_bunny_spec.rb`, exercise actual `StorageStatus#save_properties` through
the real NodeBunny gate (allocate the status with its exchange/message counter;
do not start its updater). Hold recovery beyond the RPC budget using controlled
time/wakeup, then complete it: the submitter remains waiting, publishes exactly
once, clears its batch and advances its counter only after publication. Cover
the competing-publisher gate as well. Separately prove opted-in RPC waiting
expires with `stopped:nil`, cancellation still interrupts it, and no private
keyword reaches the exchange. Retain the real Bunny continuation/retirement
regressions. No 30-second sleep or alternate recovery implementation is needed.

**Exception ownership at reviewed `7da`:** `RpcClient.run:20-35` mistook an
enclosing rescue's
ambient `$!` for this call's failure. Initialize a local pending exception before
an explicit begin/rescue/ensure around construction and the yielded body.
`rescue Exception => error` records that local error and immediately uses bare
`raise`; ensure closes the constructed client. If close fails, suppress/log the
secondary failure only when that local pending error exists. Otherwise re-raise
cleanup's typed, programming or signal exception unchanged. Do not use `$!`,
entry/exit exception-object comparison, or a return from ensure. Partial
constructor retirement remains owned by existing setup logic; no initialized
client means no additional `run` close.

This preserves the same raised object/backtrace, including a body explicitly
re-raising the very exception already handled by its caller. Successful cleanup
preserves ordinary values and nonlocal return/break. With no locally raised
body error, cleanup failure interrupts return/break by normal Ruby ensure rules.
Add regressions inside an enclosing rescue for successful body plus cleanup-only
timeout (`CleanupError` with cause), unexpected error and Interrupt/SystemExit;
also successful cleanup/value/return/break. Cover local body errors/signals plus
secondary cleanup, and re-raising the same enclosing exception object. No
cleanup or diagnostic failure may replace the locally recorded primary error.

Update `docs/node-rpc.md` error ownership and timeout wording: caller rescue
state is irrelevant; ordinary required-publisher gate waits are unbounded;
RPC explicitly opts in. Use portable paired RuboCop directives where needed.
Focused verification remains the existing three RPC/NodeBunny/StorageStatus
spec files through `.#libnodectld`, then the full Node suite. Run four changed
Ruby paths through root `.#vpsadmin` RuboCop 1.85, not the component's undeclared
lint bundle. Preserve every existing fixture/source proof; no fixture change
or new integration scenario is needed. The lead inspects the direct fixes and
focused results, then folds them into the owning runtime commit with normal
hooks. If implementation instead changes recovery ownership, public/wire
behavior or other consumers, route that deviation back and rerun only affected
review lanes under step 10. Both Important findings are now resolved and the one
existing remote-restore integration run passed as recorded above.

### Conditional retained-profile sequence after Node proof

Execution checkpoint supplied by the lead: independent review completed, its two Important findings
are resolved by direct step 9, and **one existing
`storage/restore-after-reinstall-remote` integration run passed**. Final feature
publication and exact remote readback completed. The authorized retained trial
has begun through the existing public sequence. Select the
actual final Admin worktree head (currently `290f1ef0`, retaining the original
review plus direct remediation evidence), not the earlier API46 revision in
the historical rollout table.
No command in this outline has been executed by the architect.

Completed public maintenance-start passed exit 0 in 88.027s/parity 1, with
masked services at `maintenance_ready`, `pending:true`, `ready:false`.
The private logical DB dump passed exit 0 in 4.028s (1,141,715 bytes). The
original read-only consistent baseline captured 27 groups, 1,161 rows and
60,932 bytes covering one VPS; this supplies no original live-file proof.
Public services copy-only passed exit 0 in 349.549s/parity 1, phase `copied`,
with the old generation still held. The supported stop then completed.
Public copied stop/start passed exit 0 in 621.783s/parity 1. Public own status
reported running, `ready:true`, `phase:released`, `pending:false`, `active:true`.
Actual new seed/services and regular-node refresh completed through the public
path; no private release was used. All three ordinary public Node updates
(`node1`, `node2`, `storage1`) passed exit 0 in 341.213s/parity 1, with
`updated:3`, `running:3`. The observer completed and the foreground process
ended; no kernel compilation was observed.

The lead inspected and ran the fixed implementation-owned process-binding
packet: exit 0 in 15.627s, `nodes_proved:3`. For each Node it checked actual
stable wrapper/child PID-start identity and socket peer, running control,
current system, the three corrected source-file hashes and both keyed transfer
delays equal to zero. This is bounded process/source evidence, not heap or
full-tree certification or evidence of a completed transfer.

Before the updates the original VPS was running; four physical quota properties
and one known nonsecret ordinary file were captured. Afterward `quota_equal:1`
and `file_equal:1`. No earlier checksum or identified user-data file was
available, so neither pre-seed nor user-payload equality is claimed. Pre-copy
versus post-copied and post-Node DB comparisons covered 27 groups and 1,168
post-capture rows: zero protected changes, exactly seven additions (the shared
profile package and six items), no new existing-user assignment/ceiling, and
two dynamic Pool-space changes.

Lead-reported exact-290f CI successes cover Node, RuboCop, migrations, PHPUnit,
client, i18n and group snapshot. General CI is queued and not awaited here.
API topics run `37144608379` failed only core/full-platform jobs
`111265858355` and `111265858600`; failed-step logs were downloaded privately,
and implementer0's read-only diagnosis found core 968/1 at seed 25925
(ObjectHistory admin Index) and full 968/1 at seed 21301 (ActionState
authenticated Cancel). Both expected 200 but received the generic outer
HaveAPI 500 response; the underlying exception was not captured. Relevant
endpoint/spec/auth bytes are unchanged, but earlier feature/shared spec-state
interactions remain possible. No runtime patch or unchanged rerun follows.
The separate test-only observer brief below is held for lead release.

Evidence reference: `/tmp/storage-profile-retained-20261003.nemcjis2`, unread
by the architect. Normal public provision subsequently failed exit 1 in
21.055s/parity 1. The fresh literal-CWD observer confirmed the foreground ended;
the first watcher's wrong-CWD attempt observed nothing. The public error was
`storage mutation admission requires a staging transaction`, at provider
`storage-profile-provision.rb:82`, before Pool/Create or CatchUp staging.
The scheduler is intentionally stopped. No retry, resume, reset or unlock was
performed. Physical Pool/catch-up readiness and VPS/NAS payload/retirement
acceptance remain pending. Provision uses ordinary `db:seed:file`,
Pool and CatchUp chains rather than the two failing HTTP endpoints; the CI
evidence does not demonstrate an immediate provisioning blocker. Original
review/direct-step-9, host/native and Node integration
evidence retains its separate scope; these checkpoints do not imply storage
quiet, repair readiness or APPLY.
Keep the exact Admin290f/provider399/selected-zmwh source hold.

The installed public provider already selects
`worktrees/2026-09-23-storage-redesign/vpsadmin`: `bin/devcluster:680-685,787-795`
passes it as `--override-input vpsadmin path:...`, and `:733-756` records the
source revision. Its flake imports the API modules from that input. Thus normal
public build/update uses the final API and Node sources without another workspace
pin or package switch. Keep the reviewed OS/React selections, retained disks,
existing credentials and preserving `enable:true,enrollment:true` profile.
Public installed maintenance/profile/fixture sources match provider399; the
installed launcher differs only by its packaged Bash shebang.

1. Immediately before boot, repeat `workspace-host status`, `dev-session current`
   and `vpsadmin-devcluster status 2026-09-23-storage-redesign --json`. Require
   the selected reviewed package/contract, exact ownership and stopped/bridge
   state. Recheck the recorded bridge addresses and owned runner/socket absence;
   an occupied address or unknown owner stops the sequence. Preserve cold recovery
   and residency evidence; do not reset, force-start or stop another cluster.
2. Use `maintenance-start <slug> --resident-config <recorded-store-config>
   --expect-services-toplevel <proved-resident-toplevel>
   --residency-evidence <private-evidence-file>`. Under the proved fixed masks,
   take the fresh private logical DB backup and original VPS/catalog, namespace/map,
   package/accounting/quota and retention baselines. Maintenance starts only
   services (`dev-clusters/lib/devcluster_runner.rb:164-174`); stopped Node disks
   and the original VPS files are not reachable through public Node SSH here.
   Keep the recorded cold recovery copies of all six managed disks and any
   already-known original-file path/digest evidence. No old unmasked seed fallback.
3. Run public `update <slug> services --copy-only`, then the supported
   `stop <slug>` and `start <slug> --copied-config`. The latter checks successful
   new seed/API/Supervisor, performs actual regular-node refresh, then releases
   the hold itself (`bin/devcluster:1727-1751`). No private release call or
   services-only fixture result substitutes for this full-cluster outcome.
   On refusal, retain the pending hold and diagnose before supported recovery.
   After successful copied boot, take the first supported live read-only original
   file manifest through public Node SSH/VPS access, before Node updates,
   provisioning or fixture writes. Compare stable original files with prior
   evidence where available. If no earlier file digest exists, this establishes
   the baseline for subsequent operations; it does not retroactively prove
   byte equality across seed/first boot. Cold disk copies preserve recovery
   evidence, not an unperformed per-file comparison. There is no supported
   pre-seed file reader in this services-only path; do not invent a held-node
   boot, host ZFS import or private disk-reading step.
4. **Install the Node correction before provision/payload work.** The recorded
   copied configuration replaces only services (`maintenance.rb:442-448`);
   refresh restarts existing regular-node daemons and skips storage-role nodes
   (`bin/devcluster:951-1034`). After public release, use ordinary public
   `update <slug> node1`, `update <slug> node2`, `update <slug> storage1` and
   verify the actually running selected Node package/source and keyed transfer
   delays. A selected result or successful refresh alone is not that proof.
   Recheck the original stable-file manifest after these updates and preserve
   it through provision, repeat update, payload acceptance and retirement;
   writes remain confined to the dedicated new fixtures.
   If the old regular-node daemon cannot complete the bootstrap refresh, the
   hold remains pending and ordinary updates refuse; report that exact failure
   to the lead rather than bypassing release or inventing a held Node update.
5. Use `storage-profile <slug> provision`. Existing source Pools must already
   exist; the helper checks physical/catalog root agreement, refuses unknown
   roots, creates only missing backup/NAS Pools through normal chains, waits for
   confirmations/locks and fresh capacity, then creates templates and catch-up.
   Storage1 readiness is separate from regular-node refresh. Keep source
   retention unchanged; catch-up does not Rotate or write original VPS files.
6. Run the existing provider-owned `tests/storage-profile-acceptance.rb` with
   `--slug <slug> --artifact-dir <new-private-directory> --os-template-id
   <enabled-compatible-template>`, using the installed/provider399 source.
   It owns new member/VPS/NAS payloads, full/incremental A/B history, read-only
   clone checks, fixture rotation, automatic cycle, repeat provision and services
   update. It does not replace the separate original-VPS file/retention baseline
   or prove retirement. Retain failure evidence and admitted work; no blind retry.
7. For the already planned retirement check, keep `enable:true`, select
   `enrollment:false`, complete ordinary services update, then public
   `storage-profile <slug> retire`; repeat and verify no reactivation after a
   preserving seed. Keep all payload/catalog/package/assignment objects. Restore
   enrollment true through services update and provision to leave the requested
   useful profile active. Check original files, namespace/accounting/quota and
   retention settings again; ordinary later pruning under unchanged retention
   remains allowed. Confirm scheduler, PHP, React and API usability.

These steps add no scenario or source change. The public payload runner handles
its existing scheduler stop/resume contract; a failed provision/retirement may
leave scheduling stopped for diagnosis. No storage quiet, strict production
mode, repair/APPLY or additional default-branch integration follows.

### Evidence and owning files

[The CI diagnosis](api-remote-restore-ci.md) records the one failed remote
restore scenario and its limits. The acknowledgement-timeout trigger is still
unknown. Do not infer that cleanup was the first RPC error or that a manual
unlock is safe. Public source establishes the following:

- `libnodectld/lib/nodectld/rpc_client.rb:13-31`: ensure cleanup can replace
  the body error; close is not idempotent. Setup at lines 129-174 can abandon
  partially declared channels. Keep the existing request/retry protocol.
- `libnodectld/lib/nodectld/node_bunny.rb:69-96,159-215`: existing creation
  mutex, recovery monitor/condition/generation and timed-out-channel registry
  provide the recovery mechanism to extend. A generation increment alone
  does not prove a particular late channel was retired.
- `libnodectld/lib/nodectld/storage_status.rb:75-86,96-158`: build a local
  complete pool view before publishing it under the mutex. The updater
  currently has no RPC exception boundary. `nodectld/lib/nodectld/cli.rb:177`
  sets global `Thread.abort_on_exception`, so this escape can kill the daemon.
- Pinned Bunny **2.24.0**, as selected by `libnodectld/Gemfile.lock` and the
  owning gemsets: `lib/bunny/queue.rb:322` deregisters before deletion;
  `channel.rb:1168` hardcodes synchronous queue.delete. There is no nowait
  deletion shortcut. `channel.rb:252` can cancel consumers before close when
  enabled (the default flag is false), then `session.rb:586` waits on the
  **connection-wide** continuation shared with channel.open. A late delete-ok
  or close-ok must never satisfy a later operation's continuation.
- Bunny `session.rb:780-805` invokes the before-recovery hook before transport
  initialization and registered-channel recovery; `:1052` unregisters and
  releases a channel ID but does not stop its consumer pool.
  `channel.rb:1696` recovers consumers; `consumer_work_pool.rb:62,95` separates
  shutdown/running state from actual thread lifetime. Unregister alone leaks
  resources; `running? == false` alone does not prove workers exited.

Owned runtime edits: the three libnodectld files above and their existing
`spec/nodectld/{rpc_client,node_bunny,storage_status}_spec.rb`. Add a small
owning `docs/node-rpc.md`, linked from `docs/README.md`, covering supported
error precedence, recovery and stale telemetry behavior. Keep CI incident
revisions and individual operation evidence in the linked session diagnosis.
Test edits belong in `tests/suite/storage/restore-after-reinstall-remote.nix`
and a small test-only module imported there; change `remote-common.nix` only
for a genuinely shared bounded helper. No production Nix-module/default edits.

### Error precedence, close and refresh behavior

Use `RpcClient::CleanupError < RpcClient::Error` for known RPC cleanup failures,
and `RpcClient::TransportError < RpcClient::Error` if normalization is useful.
Retain existing `RpcClient::Timeout`. Known transient transport failures are
`::Timeout::Error` (including Bunny ClientTimeout/ConnectionTimeout),
`Bunny::ConnectionClosedError`, `Bunny::ConnectionAlreadyClosed`,
`Bunny::ChannelAlreadyClosed`, `Bunny::NetworkFailure`,
`Bunny::NetworkErrorWrapper`, `Bunny::TCPConnectionFailed` (including its
all-hosts subtype), and broker-forced connection closure
(`Bunny::ConnectionForced`, `Bunny::ForcedConnectionCloseError`). Normalize
raw `IOError`, `EOFError`, `SocketError`, and connection errno failures
`EPIPE`, `ECONNRESET`, `ECONNABORTED`, `ECONNREFUSED`, `ETIMEDOUT`,
`EHOSTUNREACH`, `ENETUNREACH` only around actual Bunny transport calls, never
around catalog parsing or the whole updater. Classify the underlying cause of
NetworkErrorWrapper/NetworkFailure; their wrappers must not hide a programming
or protocol error. An exposed permanent broker error behind a closed-channel
exception likewise remains visible. Do not rescue all `Bunny::Exception`,
`ConnectionLevelException`, `StandardError` or `SystemCallError` as transient:
authentication/authorization, protocol, malformed data and programming defects
remain visible. Do not change Ruby signal/Interrupt/SystemExit behavior.

| RPC body | Cleanup | Result |
| --- | --- | --- |
| success | success | Original return value |
| exception | success | Same exception object/backtrace |
| exception | known cleanup failure | Same original exception; bounded secondary cleanup diagnostic |
| success | known cleanup failure | CleanupError with original cleanup cause |
| any | unexpected programming/signal failure | Never convert to success or a refresh retry; preserve a pending original exception during ensure and report secondary diagnostics |

Record this constructor/body's exception in a local rescue and re-raise it;
use that local pending state in ensure, never ambient `$!`. Return/break and
non-StandardError unwinding retain normal Ruby semantics. A no-primary unexpected cleanup
error propagates as itself. `close` has a synchronized one-shot lifecycle:
only the first caller attempts protocol cleanup or registers retirement;
later calls do no broker I/O or duplicate retirement. A failed first close
marks the client unusable; retain its diagnostic rather than retrying an
ambiguous queue operation. Reject further requests on a closing/retired client.
Initialization failures must also retire their allocated channel before
discarding references; failed construction never reaches `run`'s close.

The StorageStatus updater rescues only `RpcClient::Error` and the explicit
known transport set from **fetch/its RPC cleanup**, logs one bounded warning,
and continues at the normal update interval. On failure, retain the exact
previous complete `@pools` view; do not publish a prefix, clear it or enqueue
a success-triggered read. Periodic reading/submission of the previous view
may continue; this is stale membership, not a successful fresh catalog.
Even a completed body with failed cleanup does not publish the replacement.
A later successful fetch atomically replaces the view. Keep `read`, `save`,
catalog parsing and programming errors outside this rescue.

### Retire poisoned channels through existing NodeBunny recovery

Extend the existing mechanism; do not create a second connection manager,
replace Bunny, disable automatic recovery or add one thread per failed RPC.
Use one retirement entry per exact channel object with a request/generation
token and pending/completed state. Never key proof only by reusable channel
number. The implementation must satisfy this order:

1. Healthy RPC cleanup performs queue.delete and channel.close at most once.
   Serialize application channel open/close continuations through the same
   lifecycle mutex, including setup. Admission to those operations must wait
   for full recovery, not merely `connection.open?`. Keep the existing publisher
   gate; once retirement is requested, close that gate immediately, before
   triggering recovery. Optional publishes drop; required publishes wait.
2. On an ambiguous timeout at any setup/cleanup step, register retirement and
   stop issuing methods on that channel. In particular, do not call
   channel.close after queue.delete timed out. Do not unregister/release its
   number while the old transport can still deliver frames. A close timeout
   poisons the connection continuation too and requires the same recovery.
3. Close the old transport using the existing NodeBunny/Bunny path. Verify
   actual closure: `Session#close_transport` logs and swallows close errors,
   so its return alone is insufficient. The before-recovery hook must ensure
   closure before retiring its pending batch; callback entry alone is not
   proof. The old reader must also be at a recovery stop boundary with no
   subsequent old-frame dispatch; account for reader-thread versus synchronous
   publisher-thread recovery without joining the current thread or waiting
   on a reader that needs a held recovery monitor. Do not clear continuation
   queues manually on a live transport.
4. Before Bunny recovers registered channels, remove each exact retiring object
   from the recovery registry and stop/reap its local consumer-work-pool threads.
   Use the pinned work-pool interface, including actual thread joins even when
   `running?` is false; do not kill unrelated channels or join the current
   thread. Drop the client's local consumer/queue/exchange references once safe.
   Exclusive reply queues disappear with the old connection; never recover
   the discarded reply consumer or let it mutate a replacement client's response.
5. Mark a retirement entry complete only after old-transport closure, exact
   registry exclusion and worker cleanup. A waiter tests **its entry**, not
   `generation != old_generation`. Keep creation/required publication gated
   until surviving channels are recovered and all required retirements are
   handled. No user handler or transaction confirmation runs from these hooks.
6. A request arriving after the before-recovery batch was taken remains pending.
   It must be consumed at a safe boundary before that channel is recovered,
   or force the next existing recovery cycle while gates stay shut. Never let
   the first unrelated after-recovery increment acknowledge it. If it was
   already recovered, close that transport before removing it. Repeated and
   concurrent retirement requests coalesce; a late request is not dropped.

Lock order is lifecycle mutex, then short recovery-state monitor sections.
Do not hold the recovery monitor across a broker continuation, transport close,
worker join or wait for callback progress. Recovery callbacks do not acquire
the lifecycle mutex held by a caller awaiting recovery. Condition waits release
the monitor. Preserve publish's existing reentrant recovery behavior: a write
failure can initiate recovery on the publishing thread. Test both that path
and reader-thread recovery. Do not release the publisher gate merely because
the TCP socket reopened; Bunny still has to recover survivor channels.

Close must not wait indefinitely for the broker to return. Register retirement
and establish transport closure, then let existing recovery finish it; either
return after proved retirement or report CleanupError with retirement pending.
Pending is never successful cleanup and continues to own its resources/gate.
Use bounded condition waits (a 30-second monotonic recovery-wait budget is
sufficient here), leaving the pending entry for recovery after timeout; no
unsafe force-unregister fallback. Setup cannot proceed onto a new channel until
that pending retirement is accounted for.

**Stop behavior:** preserve normal daemon/supervisor signal handling and global
abort-on-programming-error policy. The updater checks stop before another
refresh, after fetch and after the known-error rescue; it does not publish a
replacement or schedule retries after stop. Where it waits for NodeBunny/RPC
recovery, supply a cooperative cancellation predicate from StorageStatus;
condition/retry waits recheck it at most once per second and raise a dedicated
`RpcClient::Stopped < Error`. Existing callers without the predicate retain
their contract. Stop still registers safe retirement and never waits for
broker reconnection, clears a gate or starts another recovery worker itself.
An in-flight synchronous Bunny call remains subject to its existing I/O and
continuation bounds; do not promise a hard whole-daemon shutdown deadline or
asynchronously interrupt Ruby while it owns Bunny locks. No persisted state
or untracked background cleanup is added.

### Persistent fixture and payload acceptance

Use the existing `extraModules.nodes.node1/node2` import seam in
`tests/machines/cluster/2-node.nix` / `mk-cluster.nix`. A small module selected
**only by this remote-restore scenario** sets
`vpsadmin.nodectld.settings.vpsadmin.queues.{zfs_send,zfs_recv}.start_delay = 0`.
The existing module `nixos/modules/vpsadmin/nodectld/options.nix` writes those
settings to `/etc/vpsadmin/nodectld.yml`; the vpsAdminOS runit module and CLI
reload them on service restart. Production `config.rb` defaults remain
90 minutes. Do not move this default to all development/production nodes.

Before starting fixture transaction chains, use existing graceful
`nodectl restart` (without `--force`) on the affected fixture nodes. It
schedules restart; command success alone is not restart completion. Wait for
changed daemon start identity/PID and initialized/running state, then assert
JSON scalar `0` from exactly these existing commands before any subsequent
`prepare_node_queues` patch:

```sh
nodectl get --parsable config vpsadmin.queues.zfs_send.start_delay
nodectl get --parsable config vpsadmin.queues.zfs_recv.start_delay
```

`nodectl/lib/nodectl/commands/get.rb` already selects the requested key for
parsable output; `commands/restart.rb` defaults to a graceful scheduled
restart. No new runtime interface is needed. Never run an unkeyed config
dump or print the generated YAML to prove these two values. Keep the existing
bounded queue/status projections for readiness; a file-only check does not
prove the restarted process loaded the settings. This verifies configuration
survives a real restart, without killing a live transfer or claiming general
transaction crash replay.

Keep the existing ordered RSpec-style remote-restore scenario and its API/ZFS
history assertions. Add these checks within it:

1. Write small deterministic payload **A**, sync and read it through the VPS;
   take/transfer snapshot 1. Change the same path to distinct **B**, sync/read,
   take/transfer snapshot 2. Prove the corresponding backup snapshots contain
   A/B through a read-only snapshot view and actual contents/hash, not only
   row counts or names. Use existing proof helpers where sound; do not mount
   a writable clone merely to compare data.
2. Reinstall via the normal API, wait for its chain and prove the sentinel is
   absent on the new primary while backup history persists. The scenario runs
   on the restarted daemons with the persisted zero-delay settings proved
   above; do not reapply a transient config patch to conceal a failed load.
3. Restore snapshot 2 over the existing remote send/recv path; prove normal
   chain completion, VPS running, payload B restored (not A/reinstall state),
   and locks released normally. Preserve head/history/handle assertions.
4. Change payload to **C**, take the next backup and verify actual C on the
   destination snapshot while prior A/B remain correct. Prove the intended
   incremental base/stream through the existing transaction inputs/output and
   ZFS history, not merely presence of the generic send handle. No manual
   unlock, row repair or bypass of normal chains is allowed.

Failure diagnostics are bounded and scenario-local: relevant chain/transaction
IDs, status/done/timings and queue workers/reservations/start delays, current
daemon identities, recent Node/broker error classes and bounded owning-log tails,
plus send/receive child/mbuffer state for those transactions. Use existing
private test artifacts; omit credentials, environment/API/generated-config
dumps, complete RPC payloads and unrelated member paths. Diagnostic failure must not replace the
test failure. Keep the existing 900-second chain limit rather than increasing
it to mask the production 90-minute delay.

### Verification, compatibility and commit boundary

Quick regressions must exercise real pinned Bunny continuation/registry and
consumer-work-pool objects with a controlled transport, following existing
`node_bunny_spec.rb`; mocks that bypass these mechanisms are insufficient.
Cover error precedence/identity/backtrace, successful return, cleanup-only
error, double/concurrent close, partial setup and final exhausted setup,
late delete-ok/close-ok, no ID reuse before transport closure, concurrent
channel creation/publishing, synchronous publisher recovery, the retirement
request arriving after the callback's pending-batch snapshot, survivor recovery,
no recovered retired consumer, and actual worker termination with running=false.
Cover failed transport closure and recovery-wait timeout without false success.
StorageStatus specs cover previous-view preservation after a later pool fails,
cleanup-only failure, later success, programming errors propagating, stop during
backoff/recovery, and no refresh publication after stop.

Exact quick argv from the vpsAdmin root (component shells already change CWD):

```sh
nix develop .#libnodectld -c bundle exec rspec spec/nodectld/rpc_client_spec.rb spec/nodectld/node_bunny_spec.rb spec/nodectld/storage_status_spec.rb
nix develop .#vpsadmin -c bundle exec rubocop libnodectld/lib/nodectld/rpc_client.rb libnodectld/lib/nodectld/node_bunny.rb libnodectld/lib/nodectld/storage_status.rb libnodectld/spec/nodectld/rpc_client_spec.rb libnodectld/spec/nodectld/node_bunny_spec.rb libnodectld/spec/nodectld/storage_status_spec.rb
nix develop .#vpsadmin -c ruby tests/ci-selection-test.rb
```

Run the existing full libnodectld suite when the focused cases pass, under the
watcher for uncertain duration. Keep unknown common runtime paths on the
selector's broad fallback rather than narrowing them to storage only; if a
test module/path is added, ensure this remote scenario remains selected.
One coherent Node runtime/spec/docs commit and one persistent-fixture/payload
commit are appropriate. No migration or generated dependency pin is needed.
Give the independent reviewer the full final branch delta and these changes
before the existing long acceptance command:

```sh
./test-runner.sh test storage/restore-after-reinstall-remote
```

A fresh watcher owns that disposable test, stops an unexpected local kernel
build and reports actual stage/failure; it does not diagnose or retry. A green
rerun without the focused cleanup/recovery regressions and restart/payload
assertions does not establish the fix. Keep failure provenance and the unknown
initial broker trigger. Small lasting Node-RPC documentation must ship with
runtime changes; this session brief is not its sole contract.

This changes in-process error/recovery handling only: old API/new Node and new
API/old Node keep the same RPC wire; old Nodes retain the bug. Deploying the
new Node package follows ordinary service restart when authorized. Reverting
code requires no DB conversion, but restores the defect and cannot repair a
previously interrupted chain. No additional rollout, production strict,
node-quiet, verified topology, repair/APPLY or default integration is claimed.
Material deviation from the lock/lifecycle/error contract returns to the lead.

## API platform request-exception diagnostic brief, 2026-10-03

**Design saved; application authoring remains held.** The lead releases this
test-only change after the current retained-cluster operation. Keep exact
Admin `290f1ef0` clean while it is a live build input. This brief adds no runtime
rescue, API behavior, schema, dependency pin, Node change or deployment action.
The architect read public source and lead-supplied diagnosis only; no failed
private logs, credentials, checks or reproduction were accessed or run.

### Evidence and smallest owning change

Core platform ran 968 examples with one failure at seed **25925**:
`api/spec/api/resources/object_history_spec.rb:228` expected HTTP 200 for admin
Index and received 500. Full platform likewise ran 968/1 at seed **21301**:
`action_state_spec.rb:403`, authenticated Cancel, expected 200 and received 500.
Both envelopes have `status:false`, `response:null`, `errors:null`. This supports
HaveAPI's outer `report_exception` path, but supplies no original exception or
root cause. The lead/implementer report the affected specs, resources, auth
helper, UserSession and Gemfile equal at `148ef` / `e882` / `290f`, and no API
delta in the Node slice. Earlier feature/bootstrap/global spec interactions
are not exonerated. No flake or production-runtime attribution is justified.

Own exactly four existing API spec paths:

- `spec/support/app_helper.rb`: attach the observer and provide the bounded
  unexpected-status diagnostic formatter.
- `spec/api/resources/{object_history,action_state}_spec.rb`: use that formatter
  in their existing `expect_status` helpers only for unexpected HTTP 500.
- `spec/smoke/api_boot_spec.rb`: focused observer/privacy/response regressions
  against the actual memoized app.

No new spec file, workflow selector, dependency or diagnostic engine is needed.
The existing smoke glob covers the focused tests; platform's file/example
selection remains unchanged. Keep a short owning helper comment explaining
return-value preservation and the output privacy boundary.

### Callback, output and isolation contract

`api/lib/vpsadmin/api.rb:31-42,340-347` creates and mounts a new server on each
`VpsAdmin::API.default` call. `spec/support/app_helper.rb:12-13` memoizes its Rack
app. In that existing initialization block, attach one instance callback to
**the returned app's `settings.api_server`**, then retain that same app. Do not
call `default` again for instrumentation, register a global class hook, remount
routes or change initialization order. HaveAPI 0.29.8's own
`spec/server/integration_spec.rb:159-177` uses this instance hook after mount.

The pinned gem's `lib/haveapi/server.rb:203-230` calls `request_exception` before
formatting the response; `lib/haveapi/hooks.rb:167-189` merges listener returns
and supports early stop. The observer must return the **same incoming `ret`
object unchanged**, with no status/message keys or `Hooks.stop`. It must not
re-raise the observed exception, modify context/authentication/locale, read the
request payload, or change framework handling of signals and programming errors.

Keep only a sanitized candidate in a namespaced key of this request's Rack
environment (`context.request.env`); do not retain the exception, context,
request or raw backtrace in a module/global/example buffer. No logging occurs
inside the callback. Missing context/env/backtrace produces a fixed unavailable
marker. A small rescue of **observer-internal StandardError only** may replace
failed formatting with that marker and return `ret`; it must not invoke
HaveAPI's hook-failure warning, which prints the diagnostic error's message.
Do not rescue the application request or catch signals in the observer.

The candidate contains only a bounded exception class name and up to **six**
`{frame_id, line}` pairs, inspecting at most the first **64** backtrace locations.
Map frames to known public Ruby source files under this checkout's
`api/{lib,models,spec}` and the selected HaveAPI gem's `lib`, using public relative
IDs such as `api/models/user_session.rb` or `haveapi/lib/haveapi/server.rb`.
Accept only enumerated source files, bounded IDs and positive integer lines;
omit unknown/eval/private/config/seed paths and method labels. Do not emit
absolute paths, exception messages/causes/inspection, SQL, URLs, headers,
request/response bodies, user data or credentials. Cap the rendered diagnostic
at **1024 bytes**; nil/anonymous/malformed class names use a fixed marker.

The existing two status helpers emit the sanitized diagnostic only when
`last_response.status == 500 && expected_status != 500`. Use the current
`last_request.env` candidate; when absent, emit a fixed unavailable marker.
For that branch, **replace**, rather than append to, their current path/body
failure text. Keep every status expectation and other response assertion
unchanged. Expected 500, HTTP 200 domain failures, successful requests and
unrelated examples produce no exception diagnostic. Per-request storage avoids
stale exceptions leaking into a later request or randomized example; do not
add an after-example global dump or a new reset/bootstrap hook.

### Verification and review boundary

After lead release, focused tests must prove one registration on repeated
`app_instance` access and execution through its real server hook. Inject a
temporary request-level failure on an existing action with RSpec's scoped
stub; do not add a permanent route or construct a substitute API server.
Assert the original HTTP status/envelope and hook-return object/keys remain
unchanged, including an existing non-500 return override. Test unexpected 500
with and without an observed exception, expected 500 and ordinary successful
responses, then a second request with no inherited diagnostic. Include fake
secret messages, SQL/URL/header/body sentinels, private/eval frames, nil and
oversized traces, and an observer-formatting failure. None may reach emitted
diagnostics or alter the assertion's expected/actual status.

Proposed quick argv from the Admin root (the component shell enters `api`):

```sh
nix develop .#api -c env VPSADMIN_PLUGINS=none bundle exec rspec spec/smoke/api_boot_spec.rb
nix develop .#api -c env VPSADMIN_PLUGINS=all bundle exec rspec spec/smoke/api_boot_spec.rb
nix develop .#vpsadmin -c bundle exec rubocop api/spec/support/app_helper.rb api/spec/smoke/api_boot_spec.rb api/spec/api/resources/object_history_spec.rb api/spec/api/resources/action_state_spec.rb
```

Use the owning disposable automatic DB, never retained-cluster DB/config.
The lead assigns uncertain-duration checks and subsequent reproduction to fresh
Luna/low watchers. This is a new API test-harness/privacy change, **not step 9
of the completed Node review**. After quick verification and a normal owning
commit, reuse the independent reviewer for the affected test-harness lanes
under step 10 (general, architecture, scope and privacy/risk), without repeating
unchanged Node runtime, fixture, migration or whole-history review. Narrow
requested fixes from that review then use step 9 normally.

For reproduction, generate the **complete sorted platform file list** using
the existing `.github/workflows/api-specs.yml:116-142,159-184` selection, retain
it as the run manifest, and run each matrix mode in a separate fresh process
and disposable DB. Within the API shell, the intended argv is:

```sh
env VPSADMIN_PLUGINS=none xargs -a "$platform_spec_list" bundle exec rspec --seed 25925
env VPSADMIN_PLUGINS=all xargs -a "$platform_spec_list" bundle exec rspec --seed 21301
```

Require one RSpec invocation per matrix mode with the original platform list
and expected 968 examples; no `--example`, fail-fast, retry or bisect initially.
The seeds order Ruby examples; differing Ruby/DB/platform versions may still
affect reproduction, so record versions without environment/config dumps.
Preserve original failures even if neither recurs. A recurrence with sanitized
class/frame evidence returns to lead/implementer for diagnosis before any
runtime fix or additional reproduction. A green run alone does not establish
root cause or repair. No production/shared/default integration, retained-cluster
mutation, new scenario, strict, quiet, repair readiness or APPLY follows.

## Provider provision admission remediation, 2026-10-03

**Priority bounded correction; the lead accepted this brief and released exactly
the four owned provider paths below.** No operation or verification result is
authorized or implied by that implementation release. The actual
public provision failed at clean Admin `290f1ef0`, provider `399c3302`, selected
`zmwh` package, as recorded above. The lead's pre-operation control observation
was singleton 1, read-write mode 0, epoch 4. That is an observation, not a
continuing admission token. Preserve the original VPS/files/retention,
namespaces/accounting, six retained disks, successful maintenance/release/Node
proof and all failure evidence. No whole-cluster quiet or absence of unrelated
work is established. The CI-500 observer remains a separate held diagnostic.

### Current remediation checkpoint

**Current phase: external idle activation handoff.** Provider and consumer
review, package proof, equivalent final replay and feature publication are
complete. The reviewed replacement package remains **unselected**; installed
provider399 and the stopped scheduler are unchanged.
The lead reports the four-stage batch passed exit 0 in 733.663s/parity 1:
AR **47/0** in 61.964s; projection **4 runs / 32 assertions / 0 failures** in
0.803s; default no-build in 12.193s; compatible-profile check in 658.645s.
Evidence reference `/tmp/storage-profile-admission-quick-fixed.i40tueb9` is
unread by the architect. These are scoped checks, not a new VM or physical
provision/payload pass.

Normal owning fold produced profile
`a308868022d9f582a8266c65a5e657f810851b5a` and native-fixture head
`0b0ba9d869c04a4362f6051f5cc281ddf1b5a642`, tree
`2dfb8aeba684b17a829af5123adba5641d9c3cce`. The first two commits are unchanged;
the fixture patch is `=`, and only the four tested paths differ from provider399,
with hash parity. The clean series has four commits / 25 paths / 5824 additions
and 67 deletions; full binary diff SHA is
`b2c217dfa3b2245dfaa55b2a43a88902cca24897aefe9aca0bb0fb6f2a86b8fa`.
The before-admission-fix backup retains `399c3302`. Retained reviewer0, saved
Sol/xhigh/read-only, completed actual `8f8..0b0b` across all four HIGH lanes:
no Blocking, Important or source Advisory findings; coherent four-commit
history, no obsolete iterations or provider migrations, and both consumed Admin
migrations unchanged. One coordination Advisory concerned stale rollout
"Current preparation" wording at lines 200–209; the lead relabeled it historical
with past verbs. No source amendment or review rerun was needed.
Normal exact-lease SSH feature publication completed at `0b0ba9d8`; default
`8f8d8ecf` and the old399 anchor remain preserved. The parent captured exact
remote readback separately, confirming exact feature0b0b/default8f8/old399 anchor.
Lead-reported Check `37154598713` at exact provider0b0b completed successfully;
older branch checks, including old399 `37114037083`, are complete, with no
superseded live run. No architect CI polling was performed.

Earlier lead/implementer-reported authored state: provider base `399c3302`, Admin
`290f1ef0`, empty index, and four frozen hash prefixes: README `9225`, provision
`ef775`, acceptance `c7a1`, spec `bd8e`. Expected selection is **47 examples**:
24 existing, seven autocommit, seven reader and nine host examples. Static
syntax/diff checks passed; lint still exits 1 with 45 unchanged baseline
offenses and zero introduced offenses. This is not a passing lint run.

The ordinary reader's `Thread.kill`, checked three-second join, own connection
disconnect, primary-error preservation and outer whole-restoration refusal
were initially authored without runtime proof; the corrected checks above now
cover their focused regressions. The first Luna launch could not find
a command before starting its driver and ran zero checks; this is not evidence
of a session-binding failure. The parent positively resolved the installed
`dev-session` and profile tools. The first actual four-stage batch stopped at
stage 1: **47 examples / 13 failures**, exit 1 in 66.717s/parity 1. The lead
inspected all 13 failure blocks: each expected session `@@tx_isolation` to be
`READ-COMMITTED`, but it remained `REPEATABLE-READ`. AR 8.1.4's
`abstract_mysql_adapter.rb:256-274` uses next-transaction `SET TRANSACTION`;
that does not change the session variable. The lead corroborated this with
the official MariaDB SET TRANSACTION documentation.

Only the spec was then released to set session READ COMMITTED after proving
the distinct owned connection and before its transaction, preserving explicit
AR isolation, all assertions and disconnect/cleanup behavior. The other three
runtime/docs paths stayed held. Original failure evidence reference
`/tmp/storage-profile-admission-quick.7syutiak` remains unread by the architect.
Stages 2–4 were unrun in that failed attempt; all four completed in the corrected
batch above. These are supplied reports, not architect-run checks.

Installed provider399 still supplies immutable scripts to the selected package.
The scheduler remains stopped; provision retry and replacement package
selection have not occurred. The consumer URL and lead-generated lock are now
committed at `bcb25d08` on actual `ad539340`; retained reviewer0 completed all
four HIGH lanes without findings, confirming exact head/tree/diff/four leaves,
one coherent commit and no migrations. The exact-bcb package batch passed
exit 0 in 248.639s/parity 1: the four existing root checks took 241.182s,
default package 7.191s, and installed proof exited 0. The parent read all seven
proof flags equal to 1: provider launchers, admission scripts, ordinary defaults,
runtime sources, Codex sources, canonical contract and profile loader.
Schema 1/policy 3/providers 2 and canonical SHA prefix `33acdc50` are unchanged.
The watcher completed without a remaining handle or reported kernel compilation.
Private evidence `/tmp/storage-profile-admission-package.p5dtjka1` remains
unread by the architect. Final equivalent consumer head `19cb25ee` resolves
to that same built package, as detailed below; source holds remain unchanged.
API CI diagnostics remain separate and held. The lead owns the external idle
handoff, followed by public services update, actual corrected guest-script
proof and the justified provision/payload retry. Prior Node/maintenance/native/public-release evidence
keeps its original scope; no new runtime acceptance is claimed.

### Cause, exact ownership and transaction contract

`api/models/storage_mutation_admission.rb:118-127` deliberately requires an
open transaction before locking singleton 1. Provider
`dev-clusters/vpsadmin/nix/storage-profile-provision.rb:82` violates that
contract at the top of `provision!`; the same defect occurs in
`dev-clusters/vpsadmin/tests/storage-profile-acceptance.rb:84`,
`Guest.validate!`. Both run through the normal production database task in
autocommit context. Ordinary API specs' outer rollback transaction concealed
this entry condition. Do not weaken the API admission implementation.

Implementer owns those **two existing provider Ruby files**, regressions in
`test/vpsadmin_storage_profile_spec.rb`, and the short owning
`dev-clusters/vpsadmin/README.md` clarification. No Admin, generic runtime,
schema, auth, freeze-mode/epoch, policy version, provider interface or Nix
option change is needed. Source release does not authorize deployment.

Replace each top-level admission call with the same short observation:

```ruby
StorageFreezeControl.transaction(requires_new: true) do
  StorageMutationAdmission.check!
end
```

The block completes before Pool lookup/staging, remote work or a wait. It
acquires/releases the normal admission lock and propagates the existing typed
`StorageReadOnly` refusal, including a missing/malformed singleton failure.
It writes no mode, epoch or audit row. Do not duplicate the mode predicate or
cache/return this observation as authority for later work. Do not wrap
`provision!`, `Guest.execute`, or their physical waits in one transaction:
that would hide staged rows from Nodes and retain the freeze lock.

Retain admission at every actual write boundary:

- `TransactionChain.fire2` (`api/models/transaction_chain.rb:82-116`) owns the
  transaction, registry admission and complete chain staging before returning.
  `Pool::Create` saves the new Pool inside it. Its return precedes the wait.
- Provider `lib/storage_profile.rb:229-262` calls
  `Plan.with_configuration_lock` for templates. That API method
  (`api/lib/vpsadmin/api/dataset_plans.rb:344-354`) opens its own transaction,
  checks admission, then locks the Plan. Template configuration commits before
  enrollment. Retirement keeps this same existing transaction boundary.
- The named CatchUp `link_chain` (`storage_profile.rb:423-442`) explicitly
  checks admission inside `fire`; `ensure_backup_and_plan!` and `ensure_nas!`
  retain their checks and same-outer-chain confirmation semantics. No source
  Dataset create confirmation, Rotate, or existing retention rewrite is added.
- Payload User/VPS/Dataset/Snapshot/Transfer/Backup/UseClone/FreeClone and the
  fixture's restricted RemoveClone continue through their existing API chains.
  Do not remove a staged check because `Guest.validate!` already ran.

A freeze between the initial observation and a later chain/template transaction
must refuse that later work. Previously committed chains retain normal outcome
and evidence; a later refusal does not roll the entire provisioning run back.
Keep inspect read-only and enrollment/actor/owner validation unchanged.

### Payload direct-write precondition

The host's `write_payload!` (`storage-profile-acceptance.rb:526-537`) writes only
the newly created fixture VPS/NAS through public SSH. These file writes are not
API-staged topology commands. Immediately before each A/B write, use the
**existing** guest `info` request, whose fixed `Guest.validate!` performs the
short read-write check; revalidate the same member/source/node/filesystem
identity and settled evidence before constructing the write. Any refusal or
changed identity aborts before SSH. No new guest operation or wire field is
needed. Do not use an earlier cached info response as that precondition.

Keep `info`'s existing string-keyed response shape. Compare the stable projection
`source_id`, `destination_id`, `source_node`, `destination_node`, `source_fs`
with the already bound source/destination, require `source_id` to match the
current fixture request and `settled == true`, and use that validated response
for the write. Guest `source!` already rechecks the member/VPS/NAS ownership;
do not add member fields to the response. Do **not** compare whole `info`
hashes: `tree_id`, `branch_id` and `snapshots` legitimately change between
initial A and post-full-transfer B. The unchanged retention assertions remain
separate. These fields prove catalog routing and confirmation state, not ZFS
GUID identity, absence of all locks/children or physical quiet. Retain the
existing NAS mounted-path checks and VPS `osctl ct exec` route.

This is a fail-fast observation, not atomic freeze exclusion across DB and SSH.
The owning fixture therefore requires a read-write trial with no concurrent
operator freeze change during its direct payload writes. It must not toggle
freeze itself or claim that two observations enforce an interlock. Supporting
concurrent freeze with those out-of-band writes would need a different runtime
contract and is outside this correction. Original user files remain read-only
comparison targets, never payload destinations.

### Focused proof and existing acceptance

Extend the existing guarded API/AR harness with fresh **autocommit** examples
(`:no_transaction`, with owned fixture restoration) rather than another outer
RSpec transaction. Assert `transaction_open? == false` at orchestration entry
and at every intercepted chain/readiness wait. Use a second ordinary-isolation
connection to the same harness-owned disposable DB to prove staged rows are
visible and the singleton lock is obtainable after return, before the waiter
continues. Do not use the existing fresh-reader test's READ UNCOMMITTED trick:
that would conceal the exact commit-visibility defect being tested. Never
commit or roll back a surrounding harness transaction to manufacture this proof.

Minimum regressions: read-write provision reaches real Pool/CatchUp staging
without the staging-transaction error; read-only initial calls refuse without
new Pool/chain/template/member rows; mode changes after the short observation
are caught by real staged admission; templates commit separately; waits hold
no SQL transaction; Guest validation works/refuses in fresh autocommit context;
and a fresh-info refusal or changed identity prevents the host payload write.
Use controlled wait boundaries after actual DB staging, not fake admission.
These DB checks do not simulate successful physical Node execution.

**Bounded ordinary-reader cleanup supplement:** choose the standard Ruby
`Thread#kill` / checked `join` path, without SQL `KILL` or another cancellation
mechanism. The current draft's `Timeout.timeout(5) { reader.value }` followed
by an unchecked `reader.join(3)` can return while its reader remains alive;
the outer autocommit ensure would then delete fixtures and restore the singleton
concurrently. That is not acceptable proof or cleanup.

Keep the same positively bound automatic TestDb, distinct reader connection,
READ COMMITTED transaction and two-second InnoDB lock wait. Verify the reader
connection differs from the main connection before using it. Give this short
reader an unconditional owning ensure that disconnects its adapter after
transaction unwind, before `with_connection` returns it to the pool. Replace
the current ensure's `SET SESSION ...` reset with this close; do not issue a
retrying reset query or reconnect the canceled connection. A disconnected
adapter may return through the ordinary pool API and reconnect on a later
checkout; the old transport must already be closed. This disposes of the changed
session timeout on success as well as cancellation, with no connection-ID race.

Capture the actual `reader.value` exception locally and re-raise it unchanged;
do not use ambient `$!`. On timeout or abnormal parent exit, kill only this
recorded thread if alive, then join for at most the existing three seconds.
A join exception must not replace an already pending timeout/reader assertion
or signal. Accept reap only when the thread is dead and its connection-close
ensure completed (or it never acquired a connection). ActiveRecord 8.1.4
`abstract/transaction.rb:643-675` rolls back an aborting thread and discards an
incomplete transaction; `connection_pool.rb:452-469` runs lease release in
ensure, and `mysql2_adapter.rb:122-128` closes the raw connection. These paths
support orderly unwinding, not a guarantee that arbitrary native I/O stops
within three seconds.

If reap/close remains unproved, preserve the original failure, mark this spec
process for no further examples, and skip **all** autocommit fixture deletion
and DB restoration, including the surrounding ensure's control/key updates.
Retain the failure for the owning disposable harness/watcher to terminate;
do not detach the thread, proceed to another example, or report cancellation
success. Keep the guard on the outer restoration path as well as the reader
helper. A cleanup-only close/join failure must itself fail the test.

Focused acceptance covers normal return, reader assertion failure, parent
timeout with successful reap, connection-close/lease cleanup, and an unproved
reap refusing fixture restoration and subsequent examples. Use controlled
barriers and short timing in existing spec infrastructure; no production DB,
new fixture scenario, real five-second sleep or global thread patch is needed.
SQL `KILL` is not selected: a recorded ID alone does not prove its connection
is still exclusively owned when the command arrives, and it would not replace
the required thread/ensure proof.

Run through the existing selected-Admin API harness, with initial CWD set to
the registered Admin repository root
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/vpsadmin`.
The shell then enters `api`; do not add another `cd api`. The absolute flake
selector does not set initial CWD: Admin's `enterRepoHook`
(`flake.nix:365-386`) locates the nearest flake from PWD, so launching from the
provider root would select the wrong `VPSADMIN_REPO_ROOT`.

```sh
nix develop /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/vpsadmin#api -c /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/vpsfree-dev-workspace-storage-profile/dev-clusters/vpsadmin/tests/run-storage-profile-api-specs.sh
```

Keep its inherited/configured-DB refusal and automatic disposable ownership
proof. Lead/watchers own focused checks, the provider's declared checks and
compatible enabled-profile smoke. Commit normally and have the retained
reviewer cover affected general/architecture/scope/risk lanes before the public
retry. This newly exposed orchestration bug is not either of the completed
Node review's step-9 fixes. Narrow fixes from its own review use step 9; any
broader admission/package mechanism requires step-10 affected review. Carry
forward unchanged Node integration, maintenance VM and host-policy evidence;
no additional VM scenario or host-migration rerun is justified by these files.

### Installed package, deployment and recovery boundary

**Prepared consumer checkpoint (lead-reported):** the earlier provider SSH
fetch confirmed default `8f8d8ecf` and feature `399c3302` unchanged; reviewed
feature `0b0ba9d8` is now published as recorded above. Consumer
`origin/master` remains `1fa9c982`; the clean registered workspace feature was
normally fast-forwarded from that head to current shared local master
`b9c2ef2b51b66c898ee073a958581d3ac36c4bc7`. Its 24 additional paths are
coordination records under `work/` and `notes/`; the lead confirms unchanged
source/procedure/config/input bytes, including AGENTS/flakes/configs/team
blobs. Shared master/index were unchanged by the operation. The backup
`backup/2026-09-23-storage-redesign-workspace-before-admission-pin` retains
`1fa9c982`. A subsequent normal feature fast-forward moved `b9c2ef2b` to
`ad539340b25786bf5cac11fa9c968144c417d1bd`: seven more coordination-only
paths, with relevant AGENTS/flake/config/`.dev-workspace` bytes equal and the
feature clean. Explicit SSH fetch still found origin/master at `1fa9c982`;
shared HEAD/index were unchanged by the operation. The initial read used
nonexistent config filenames and stopped before mutation; correcting those
to the canonical `config/vpsadmin-devcluster.json` and vpsadminos config paths
resolved the read assumption, with no source failure.
The generated pin was normally committed at
`bcb25d08b5aba776bff16c0415023e405435c97d` on actual base `ad539340`, tree
`bf8038c2504deaff69b45e2640a9a03e1ec40c3a`: one commit, two flakes, 5 additions
and 5 deletions, full binary diff SHA
`4e193905614362220e288ec20f8db5a2f665a2993ce4e81281243e256f6e40b3`.
Exactly four provider metadata leaves change 399 to 0b0b; generic4ef, Codex4c,
all other nodes/follows and defaults are equal. The lock was generated, not
manually edited. Root no-build passed on the final precommit flake bytes
(`flake.nix` hash prefix `97f69c73`, lock `1a0b5e22`); no timing or realization
is inferred. Retained reviewer0 completed actual `ad539340..bcb25d08` across
all four HIGH lanes without findings, confirming the exact composition and
one coherent commit/no migrations. The package batch above built
`/nix/store/vyf5bpadsnplrzfvrhx182wcsfnw5602-dev-workspace-0.2.0` and tools
`/nix/store/4w4mbc7x9kgj798bf16kpfq7mdi11w6b-vpsfree-dev-workspace-tools-0.1.0`.
The canonical contract SHA is
`33acdc50fa6b7ed94f84d1f7f1db0af8d76d7d57d2e721cbb6a204a96b27c0d1`.

The lead then normally replayed the single pin onto actual shared master
`990a5929bf7c54489c1d75a4c292492239502adc`, producing clean
`19cb25ee8d5333a4ea4c1816806c130c41652f1f`, tree
`3087dbed87bc9066707c656a87d63ec1e7c75e2e`. The 30 intervening paths were
coordination-only, with relevant source/config/procedure blobs equal; no foreign
contents were inspected. Range-diff is `=`, full binary diff/file hashes/message
are unchanged, and shared HEAD/index were preserved. The
before-admission-publication backup retains bcb. Final package evaluation passed
in 7.218s and resolved to the **exact same vyf5 output**; final no-build passed
in 3.838s. The original independent `ad..bcb` review and built proof carry
forward for the identical patch; no review or VM rerun is claimed.

Normal exact-lease feature publication and readback completed at `19cb25ee`;
remote master remains `1fa9c982`. The lead confirms the final public
capture-comparison completed with base
`990a5929bf7c54489c1d75a4c292492239502adc`, head
`19cb25ee8d5333a4ea4c1816806c130c41652f1f` and base label `Captured comparison`,
preserving initial registration metadata; the portal URL was also confirmed.
This is lead-reported evidence, not an architect operation. This is an
**unselected** package ready for the
external idle activation handoff, not a new merge/default-integration approval.
Generic/provider/Admin defaults remain unmerged. No switch, public services
update, corrected guest-script proof or provision/payload retry has occurred
for this replacement. CI-observer edits and cluster operations remain held.
The architect performed no private-artifact inspection or operation.

Provider `nix/test.nix:1166-1167,1207-1208` embeds each Ruby script into the
services wrapper through an immutable store path. The selected public provider
also supplies the Nix module. Editing its worktree or retaining Admin290f does
**not** change the currently installed command or current guest wrapper.

The supported sequence is: reviewed provider correction/publication; generated
consumer input pin to that exact published provider, preserving generic policy
3 and unrelated inputs; consumer composition review/checks and package/source
byte proof; external idle operator activation through the public workspace
switch; public selected-generation/provider/status verification; ordinary
`vpsadmin-devcluster update 2026-09-23-storage-redesign services`; verify its
installed fixed provision and guest-acceptance scripts, preserved profile
selection and original DB/file baselines; then one justified public provision
retry and the already approved payload/repeat-update/retirement sequence.
Use the same-session Admin290f input unchanged. No direct extension store
helper, unselected runner, guest script replacement or private lifecycle path
is an alternative. Do not infer a new workspace/default merge approval.

Until that sequence is ready, retain the intentional scheduler stop and report
the actual state; do not resume/retry/unlock from this brief. A services update
may restart scheduling, so the lead retains control of its accepted paused
provisioning window and subsequent normal resume. A failed retry retains
committed chain IDs/evidence and rechecks ownership/readiness before any next
action. Never reset retained disks, disable the preserving profile, alter the
singleton, cancel/delete locks, or restore old allocations to hide the error.
An old package rollback reintroduces this bug; it is not a recovery fix.
No new quiet/repair/APPLY, production operation or default integration follows.
