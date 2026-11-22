# P3 SDK worker and supervisor evidence

Owner: implementer1. This is source/fake-provider evidence, not installed launch,
provider entitlement, automation release or session lifecycle authorization.
P0 was accepted separately. Lead owns package acceptance and review allocation.

## Revision and input identity

- D source base: `6587c4c1cedabee95bcc52f4667e7d33e3a82859`.
- Tested committed core: parent `67e08f2f10faa288aefb7e97e2d3eb19d8819eb6`
  to `daa780d1781df025aa918970310f4fb0f5f66a83` (20 owned paths).
- Completed first-launch source: parent `fc02306ab8e66f85fdae06519b1c907dc1728120`
  to `a74ae62bfb57cdb1858381a8c66855e2ab9f2b5b` (31 actual owned delta paths).
  This follows the accepted core checkpoint; peer commits between them remain intact.
- Pi upstream `a22b888a58fe55b668cc45b80749ec88d4eb4ddc`, package
  `/nix/store/9hf2a7rz231w2pn50s4jlmrgs4007xc5-pi-1.5.2`.
- Node `/nix/store/gf597zf0ysgbngwb92baxgxjd02px6jh-nodejs-22.23.2/bin/node`.
- Go environment: repository Nix shell at immutable D
  `4f390101de7ca5047d9e41faa0b483088d591185`, Go 1.26.6. The mutable P7
  flake was deliberately excluded. No ambient compiler or CGO workaround.
- `portal/go.mod` selects C module
  `v0.0.0-20261112094020-f9b9b4831b23`; readonly module mode, no module edits.
- Full clean-copy input manifest: `tmp/p3-final-inputs.json`, SHA-256
  `a4758bbc2852bbbfb4bb40e68dd2e30a894eec0ee6bad3375379f7b32d14738e`.
  It captures 41 source/fixture/module inputs without central P2 code.
- A final streaming assertion changes only `pi-runtime/src/session.test.mjs`.
  Its independently passing input composition is
  `tmp/p3-final-inputs-stream-check.json`, SHA-256
  `457e7b06f37b99dd11c6c850837cf7e9090e85d5c362531cc78f7eaf35ae7b27`.
  Every production byte remains identical to the full clean-copy run. A later
  fixture listener cleanup ownership fix changes only supervisor_test.go and
  passes its focused actual-SDK case (4.245s). Final commit composition is
  tmp/p3-final-inputs-commit.json, SHA-256 be517cdae13b389ecd374f5298bca038992a215d0ebea16e514d9e5ebc606b85.

The production closure is `pi-runtime/src/{worker,protocol,session,accounts,package}.mjs`.
It uses public exports from the exact Pi root. Host-tool factories, P0 fixture
helpers, injected fake providers and ambient npm resolution are not production
runtime dependencies. Source fake fixtures may import the existing pinned public
package helper. No upstream patches or maintained fork are introduced.

## Checked capability boundary

| Path | Evidence and boundary |
| --- | --- |
| First launch/current replay | Manager reserves instance/generation before preparation, freezes launch/config/map bytes and records starting before H0. Interrupted preparation reuses exact originals; same-ID replay inspects and never starts again. Different request/successor is unavailable in this core. |
| H0 readiness | Exact v1 byte fixture/SHA, strict parsers, real private Unix channel, expected runtime-config hash and independent host/process verification code. Fake host observations are explicitly injected; installed systemd/cgroup/mount/group/sudo permissions remain unverified. |
| Create/load | Chosen stable native UUID, opaque HistoryRef golden encoding, private mapping/history/settings, exact canonical work/slug cwd. No synthetic prompt/header. Existing initialized worker can receive the first real input; missing expected persisted history and crashed loaded mappings hold. |
| Creation verification | Original creation tuple/current generation + authoritative mapping + exact original Accepted receipt + independent public native reopen/user-entry contents/lineage. Nil proof is initialized-only, cannot publish ready. Root initial and original team-assignment contexts both tested. Wrong ID/locator/entry/digest, stale generation and missing history refuse. |
| Input/ACK | Actual pinned SDK ordinary fresh/retained user event, exact new live entry, independent public reopen, then fsynced host receipt before Accepted. Repeated text, both original UUID/32hex spellings, changed duplicates, lost ACK and direct observational receipt lookup tested. |
| Crash gaps | Intent, dispatch, native result, witness and receipt fault boundaries never resend. Committed Accepted receipt survives lost ACK. Missing proof stays Unknown; held settings/descendants block further dispatch. Worker crash never creates another native ID or resumes a turn. |
| Text/paging/watch | Escaped text and bounded native branch pages; opaque scope/generation/content cursor refuses stale input. Snapshot invalidation tested through real socket with fake entries; actual SDK public message_update exposes a nonempty live assistant snapshot. No native replay-log claim. Oversized single native entry is unavailable; originals preserved. |
| Settings/provider switch | Both exact canonical pairs frozen before runtime, positive revision rules, idle/no unresolved work. Actual two-provider same-model-ID switch preserves native ID/history and original input count, avoids native global defaults, persists owned effective mapping and reloads it; other member unchanged. Account-only/provider-only/missing old/new map/skipped revisions refuse. Partial/lost native reply retains pending/Unknown with no second effect. |
| Account attribution | Required sorted bounded provider/account map, exact key pairing supplied by P4, immutable hash/replay checks. Actual worker production path rejects configured auth overrides and custom registered providers, then requires stored source. Fake status/config cases cover stored-plus-override, absent stored, runtime/environment and clean endpoints/models. No account identity, entitlement or real login/model proof. |
| Interrupt/unload | Public SDK abort tested during finite fake inference. Idle unload waits exact process exit; ambiguous session descendants retain a durable hold. Process-group emptiness alone is not treated as arbitrary tool containment. |
| Resources/metrics | Owned direct command launch, immutable operation/resource IDs, PID/start/group, duplicate/no-resend, exact stop and retained wait result tested with finite Node fixture. Unknown start/native observation held. Metrics code reads actual H0 cgroup and scratch views with explicit unavailable/external coverage; no quota or installed accounting claim. Existing registry integration remains gated. |
| Neutral slots | Verify, Read, Page, Send, Interrupt, Watch only. Direct trusted Configure/Lookup/CreationVerifier and resource Controller methods exist. Queue, uploads, dialogs, neutral Settings catalog, goals, Plan enforcement, utility identity, callback bridge and native fallback are not advertised by this core. |

## Verification receipts

The reproducible source-only copy driver is `tmp/p3-core-check.py`. It copies only
owned P3 sources plus explicit module/identity/fixture inputs into a Python-owned
temporary directory, and invokes the immutable repository Nix environment:

```sh
env PI_PROBE_PACKAGE=/nix/store/9hf2a7rz231w2pn50s4jlmrgs4007xc5-pi-1.5.2 \
  nix develop 'git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-pi-codex-migration/dev-workspace?rev=4f390101de7ca5047d9e41faa0b483088d591185' \
  --command python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-11-11-pi-codex-migration/tmp/p3-core-check.py
```

- Full copied `go test -mod=readonly ./internal/piruntime -count=1`: **pass,
  12.893s**. Node five account/protocol/native-session/provider-switch/partial
  mutation cases: **5/5 pass, 2.042s**. Complete inner batch 16.736s.
  Unified session `70807` terminal exit 0, no remaining process.
- CLI `go -C portal test -mod=readonly ./cmd/workspace-portal
  -run '^TestPiSupervisorCommandRefusesOtherArguments$' -count=1`: **pass,
  0.055s**. Unified session `69149` terminal exit 0. Real handler is owned by P3;
  main registration remains P2's separate source/commit.
- Fixture cleanup ownership: fakeHost disables automatic unlink through a closed
  /proc/self/fd bind pathname; TempDir owns its exact socket. Production retains
  its directory FD through listener close. Focused native supervisor test passes
  **4.245s**, terminal exit 0, no remaining command.
- Added streaming assertion: pinned Node `--test pi-runtime/src/session.test.mjs`:
  **3/3 pass, 1.815s**. It changes no production or Go input.
- Earlier focused runtime gate: real Unix manager/supervisor/two SDK workers,
  creation witnesses, private state, stale/hold cases **pass 4.380s**.
  Native provider switch/reload/other-member case **pass 6.139s**.
- Formatting and owned diff whitespace checks pass. No builds, installed units,
  live services, credentials, real account/model calls, profile activation or
  deployment were run for these P3 tests. Finite fixture processes are joined;
  source tests contain only explicit owned fixture termination.

A fixture cleanup assertion initially assumed every fake worker was an OS
worker. It failed promptly; the checked assertion now distinguishes the in-memory
fixture. No production failure was inferred. No expensive duplicate build ran.

## Persistence, compatibility and limits

New schema-1 P3 mapping/runtime/resource/submission records are source-only,
unreleased, undeployed and have no consumed migration lineage. Original UUID
submission digest/schema encoding is preserved; 32hex support widens only exact
syntax and never aliases spellings. Native IDs and stable refs exclude execution
generation from submission deduplication. Runtime-config gains required
account_bindings before any live release; earlier incomplete fixture shapes
refuse, with no inferred bindings or silent migration.

Host records are atomically published, fsynced and retained outside scratch.
The pinned native SessionManager._persist uses synchronous file writes/appends
and close (packaged session-manager.js:807-822), without native fsync. Independent
reopen proves observed native-file/process-crash acceptance, not native JSONL
survival of a host power failure. A missing entry/history on later verification
remains held. Neither this receipt nor native abort establishes exactly-once
external effects or permits automatic redispatch.

A source-only first-launch/manual/provider-switch result does not establish
Pilot-ready, Automation-ready or Launch-ready deployment. P2 admitted creation,
installed H0/tool access, package/catalog composition, callback authority/tools,
explicit successor recovery and relevant automation operation proofs remain
separate owned gates. No rootless fallback, session cleanup, automatic native
retry or Durable substrate is introduced.

Technical docs are in `docs/pi-runtime.md`; host contract remains
`docs/pi-runtime-host.md`. Lead owns the final writing pass, branch-level review
and package acceptance. No partial push, merge or lifecycle operation follows
from this evidence.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/

## Completion and ownership handoff

The full first-launch package is committed at `a74ae62bfb57cdb1858381a8c66855e2ab9f2b5b`.
All frozen source hashes were compared before staging; only owned actual deltas
were staged, including the lead-transferred complete operator documentation.
No dependency files, P2 main/central code, P7 package files or nested host-tool
factories were included. Normal commit hooks were not bypassed; no hook framework
is declared. Index verified empty immediately after commit. No partial push,
review invocation, merge, installed test, deployment or lifecycle action occurred.

The feature has no database migrations or externally consumed P3 state. The two
P3 functional checkpoints have no obsolete alternate implementation: the first
introduced the SDK/witness core, the second completes its first-launch controller.
Final whole-branch consolidation/migration review remains the lead/reviewer's
responsibility; this is not a branch-ready or integration claim.

The accepted boundary refuses successor requests and automatic crashed-turn
resumption. Those are separate required runtime-readiness work, alongside actual
P2/P7 composition and installed H0 permissions. Native power-loss durability and
arbitrary tool exactly-once semantics are not claimed. Independent review and
long installed verification remain with the lead's ordinary final ordering.

Committed delta inventory:

- `docs/pi-runtime.md`
- `pi-runtime/src/accounts.mjs`
- `pi-runtime/src/accounts.test.mjs`
- `pi-runtime/src/protocol.mjs`
- `pi-runtime/src/session.mjs`
- `pi-runtime/src/session.test.mjs`
- `pi-runtime/test/fake-worker.mjs`
- `portal/cmd/workspace-portal/pi_runtime.go`
- `portal/cmd/workspace-portal/pi_runtime_test.go`
- `portal/internal/piruntime/accounts.go`
- `portal/internal/piruntime/accounts_test.go`
- `portal/internal/piruntime/accounts_validation_test.go`
- `portal/internal/piruntime/adapter.go`
- `portal/internal/piruntime/adapter_test.go`
- `portal/internal/piruntime/controller.go`
- `portal/internal/piruntime/conversation.go`
- `portal/internal/piruntime/identity.go`
- `portal/internal/piruntime/manager.go`
- `portal/internal/piruntime/manifest.go`
- `portal/internal/piruntime/manifest_test.go`
- `portal/internal/piruntime/processes.go`
- `portal/internal/piruntime/protocol.go`
- `portal/internal/piruntime/receipts.go`
- `portal/internal/piruntime/resources.go`
- `portal/internal/piruntime/resources_test.go`
- `portal/internal/piruntime/settings_test.go`
- `portal/internal/piruntime/supervisor.go`
- `portal/internal/piruntime/supervisor_test.go`
- `portal/internal/piruntime/transport.go`
- `portal/internal/piruntime/worker.go`
- `portal/internal/piruntime/worker_test.go`

## Current runtime integration checkpoint: B1, native sync and tagged codecs

The next source checkpoint is buildable on
`563f6be3ae0498c4b4e9d5fffe0c8844f4555e75`. Its exact 31 owned paths and
SHA-256 values are in `tmp/p3i-b1-checkpoint-inputs.json` (manifest SHA-256
`fdc4803c3e0f2cee38b539e1f1dc60a5b75e7ce5c28cbe81fe636f84066ab4b0`).
The 64-input source copy excludes the separate, uncommitted B2 policy files;
all owned production/test bytes match that copy. Documentation is technical
source awaiting lead's writing pass. No index window or push is implied.

This checkpoint implements bounded retained callbacks over existing worker pipes
and control.sock, optional supported-tool projection, original durable Accepted
input admission, exact native tool origin and linear selection, cancellation and
persistent Unknown holds. Historical InspectNativeOrigin uses public current and
reopened history without an active-input guess, Load or effects. It adds the actual
read-only ValidatePackage/ReadStart and literal UUID-or64lowerhex CreationID seams.
Shared tagged receipt/mapping codecs and UtilityController/Authority/ReadAuthority,
refs/grants/digest/identity exports are real source dependencies; no Manager utility
method implementation or active utility capability is claimed by this checkpoint.

The worker now opens the already verified native history read-only, syncs file
then directory and closes both before its witness. Existing host receipt sync
still precedes Accepted ACK. Owned-fake traces prove this ordering, injected
open/sync/close refusal and unchanged bytes. An actual native sync failure holds
Unknown, requests abort and admits no second input. This is conventional sync
completion for the witnessed input prefix, not physical power-cut proof, later
output durability or a retroactive upgrade of old receipts.

Focused evidence, with distinct input scopes preserved:

- Original frozen64-input B1/tagged copy: callback cancel/disconnect Unknown and
  durable hold/no new input/unload refusal, overflow/availability, tagged owner
  and utility receipt crash boundaries, linear fixture **pass 4.220s**.
  Base `11888bcb6e37eaffe1cc0f3c99b92b4ccdf34e11`, manifest SHA-256
  `5bc7129f19fe37d72abb6a57b8ac619caec2765495792fc240d2a55df1417eb6`.
  Fresh Luna/low watcher/command terminal0; output in `tmp/p3i-b1-watcher.log`.
- Later frozen64-input copy: withheld-ACK setup cancel/deadline and socket drain,
  ReadStart missing/empty/ordinary-lock/artifact holds without native calls,
  literal64hex Create and no-file VerifyCreation, fixed package manifest checks,
  retained schema1 exact bytes/digest and receipt fault cases, same shared utility
  receipt engine/owner confusion and real SDK pipe sync/witness/lost ACK all passed
  within a **6.400s** batch whose one historical-origin case failed. Original
  manifest SHA-256 `d9ddfea4cc1391cd543cf7082224d1d9b9d56d9996ac347721458426f7b80f00`;
  full output `tmp/p3i-b1-final-check.log`. This is not a passing whole-batch claim.
- The historical failure was public SDK in-memory optional undefined fields versus
  identical serialized native entries. A focused diagnostic proved exact full
  JSON.stringify equality; the accepted correction uses that persisted
  representation without replacer, sorting or pruning. The final real SDK
  callback/origin case then **passed 2.147s**, including independent original
  Lookup-visible Accepted input, two native calls/same assistant anchor/distinct
  tool IDs, historical read after active input settles, exact copied argument
  content, unchanged history bytes, stale generation/wrong anchor refusal,
  verified unload and cold inspector refusal without Load.
  Final tool session `43528` terminal0. The earlier diagnostic sessions `83686`,
  `28764`, `90307` are terminal1; the last was a fixture's overstrict raw JSON
  escaping comparison despite successful returned native content. The fixture now
  compares decoded content as the accepted historical contract requires.
- Final Node native-sync failure case **1/1 pass 1.975s**; framing, lineage,
  persisted-origin content/duplicate/oversize/Unicode/missing-file, sync helper
  ordering/faults and production pre-init version smoke **6/6 pass 0.369s**.
  Tool session `71697` terminal0. No actual SDK session/auth/model setup occurs
  in the production version smoke.
- Actual runtime compile **pass 0.015s**, no tests, using the cached repository
  shell and `go test -mod=readonly ./internal/piruntime -run '^$'`.
  Owned diff whitespace checks pass. New historical Node3/3 also passed0.228s.

Commands use the already-proved D shell
`/nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv`, public pinned SDK
`/nix/store/9hf2a7rz231w2pn50s4jlmrgs4007xc5-pi-1.5.2`, fake provider/auth and
owned disposable histories. First watcher launcher failures (nonexistent env
path, then missing GCC) ran no Go tests; both ended before source checks. The
cached-shell watcher corrected that environment once. All watchers/commands are
terminal and finite fixture processes are joined; no live runtime was launched.
No native retry writer, policy activation, successor launch, migration, installed
runtime, credentials or real model access was introduced or exercised.

Retained schema1 receipt and mapping bytes/digests stay unchanged. Schema2 utility
records are owner-tagged codecs only at this checkpoint, in disjoint expected
roots. No automatic conversion, repair or cleanup is added. Full utility engine,
B2 integration after its committed API, explicit positively drained successor and
combined P2/utility cross-seam post-review verification remain current-package
work. Separate component tests are not one end-to-end proof. Final package and
whole-branch independent review remain lead-owned.

The API/B1/fsync/tagged checkpoint is committed at
`2dd2af9499fa64602bfce94c20a17b6e41139eca`, parent
`563f6be3ae0498c4b4e9d5fffe0c8844f4555e75`: exact31 files,2636 insertions/230
removals. Lead's prose-only pass changed only the documentation SHA-256 to
`698c2108685b2954e2e4faab305b5dba8bc3acf3842ebdb5d86156de1f59007d`.
Every tested owned Go/Node byte matched before staging; every unowned input in
that source-copy graph matched the committed parent. Normal commit-F/hook behavior
was preserved. Full committed/current hashes and exact inventory are recorded in
`tmp/p3i-b1-commit-receipt.json`. Index verified empty and all31 checkpoint paths
clean immediately after commit. No peer/policy files, utility method bodies,
source dependencies or successor writer were included. No partial push occurred.
The first lead report contained an incorrect full-head suffix; the corrected
report `3de2fa11680b4f7aa42fabefb92986f3` and this receipt are authoritative.
P2/P5/P6 received the actual full head directly. The index window is closed;
full P3-I remains executing, with no readiness or package acceptance inferred.

## Utility engine and retention export continuation

The shared utility engine's first72-input source copy, base
`fa43219096e3e8b9e5002cb28efccadf73a1a2ce`, passed5.990s: actual
Manager/Unix/pinnedSDK initialized/no-file creation, tagged worker identity,
original-grant revalidation per effect, changed-input/revoked-after-Bind refusal,
separate current original-ref read authority, schema2 Accepted witness, exact
same-input replay with one native user entry, unload/old-generation/cold-read
refusal. Retained callback/history and native sync/lost-ACK regressions and
schema1 exact receipt bytes passed in that same related batch. Snapshot manifest
`tmp/p3i-utility-inputs.json` SHA-256
`c554ada60cc6aa94b15a1553b70c002b5615f7c87f700c11d1ab08cb3f727c44`.
Fresh Luna/low watcher/command were terminal0, no survivors; log
`tmp/p3i-utility-check.log`. This uses fake injected authority, not the final
central P2/P5 cross-seam or installed readiness proof.

The utility callback pair initially failed40.160s because the owned fake report
omitted required elapsedMillis and the shipped factory refused it before the
bridge. A report-only3.917s diagnostic captured that exact native toolResult.
Only the fake response gained elapsedMillis:0; no production validation changed.
The report/lost-reply pair then passed3.812s, proving reconstructed utility caller,
HostCall.Runtime, original Lookup-visible Accepted input before handler admission,
monitor-only tool projection and persistent Unknown/unload refusal after lost
report reply, while the original input remains Accepted. Diagnostic output now
contains only bounded fake tool results instead of whole native prompts/history.
Tool81080 terminal0; failed watcher65817 and command87021 terminal1, no survivors.
Golden Go utility digest/identity and retained-worker-envelope fixture passed.016s;
Node exact cross-language utility fixture/lineage suite passed4/4,.224s.
These are distinct source/fixture scopes; no passing whole-final-suite claim.

The disjoint new retention.go/retention_test.go export is ready as a narrow API
checkpoint. Exact committed-parent `1eeecfb575220d7f8d152bc42b6b9e91c77c995b`
plus only those two files passes.371s (cached D shell, -mod=readonly); initial
working-source check.378s. It inventories all utility namespaces and original
receipts with actual strict codecs, preserves pending/terminal outcomes, refuses
orphan/scope/owner/ref/generation/digest/filename/artifact mismatch and returns no
partial result. Owned temporary-state snapshots prove no writes or runtime/lock
creation; native history stays opaque. No Manager/auth/host/native invocation is
used. Exact hashes/base are in `tmp/p3i-retention-api-inputs.json`; formatting and
whitespace pass, index untouched. API comments hold the local consumer contract;
P2 owns CLI/operator documentation and identity-only stdout projection. This
source API alone grants no runtime or writer capability.

The utility method body and B2 integration remain uncommitted current-package
work. ToolPolicy fields preserve retained schema1 bytes and reject utility policy;
impl4 alone appends isolated supervisor methods in its new file after the supplied
field window. Main runtime dispatch/config/create/load/session remain P3-owned.
No native retry writer declaration, successor or implicit repair was added.

The retention export is committed at
`e4b9f861f14c5f6fa803c320e4e66e71cca866f4`, parent
`1eeecfb575220d7f8d152bc42b6b9e91c77c995b`, exactly2 new files/365 additions.
Both frozen hashes match staged, committed and current bytes; the index is empty
and both owned paths are clean. Normal commit-F/hook behavior preserved, no push.
Full actual-head receipt is `tmp/p3i-retention-commit-receipt.json`; lead and P2
received that checked head directly. No utility/policy/core/peer delta was staged.

## Coherent utility and retained policy source checkpoint

The combined utility/B2 source is ready on current parent
`0a647bdfcdfbf900b614cec7935f147dba79997d`. Its18-path inventory and SHA-256
values are in `tmp/p3i-utility-policy-checkpoint.json`, manifest SHA-256
`012338470e4d593e259fdab70bfb2cb0ccb4323cb55b1d257a08a4c9a6de5d76`.
The16 P3-owned paths depend on implementer4's two owned tool_policy.go/test method
hunks; any combined logical commit needs lead's explicit ownership transfer/window.
No staging has occurred. All75 production/test/dependency input hashes match the
actual frozen passing source; every nonowned input matches the committed parent.

Fresh Luna/low observed one related check batch from the immutable source copy,
base `74c5646455e1e40f03732347c5eb567dd90d8fbc`, manifest SHA-256
`ee2f058da28c1f9d2e4439312770755ed85804bd70ed20c479eb4b889199109e`:

- Selected Go native/core tests **pass17.952s**: actual Manager/Unix/SDK policy
  creation with pending-before-setup and positive apply, exact Revision1 replay,
  nil/changed initial target refusal, real Plan write refusal, Default permitted
  write, return-Plan overwrite refusal, fixed ceiling/CAS, later-revision Create
  unavailable, unload/cold Inspect/no Load, retained policy reapply on authorized
  Load, and interrupted initial setup with no second Create/native setup.
- The same related batch passes the original-grant utility worker/input/read/
  unload cases and native monitor callback/lost-reply Unknown/drain cases after
  shared-loader changes. Actual retained callback/history and native cross-provider
  configuration regressions, retained mapping shape and exact schema1 receipt
  bytes also pass under the combined source.
- Node WorkerSession **4/4 pass2.130s** after public bindExtensions({}) activation:
  ordinary fresh/retained witness, same-history provider switch, partial settings
  Unknown hold and sync failure/no second input.

The command/watcher are terminal0 (command38903, parent17878), no owned survivors;
log `tmp/p3i-policy-check.log`. This is a focused affected-source batch, not an
unchanged broad suite or final complete-package/cross-seam proof. Earlier failed
callback fixture diagnostics and narrower passing inputs retain their original
scopes; the elapsedMillis-only fake fix did not weaken production validation.

Applied policy is source-only optional behavior, with no central registration or
runtime capability advertisement. Schema1 mapping/receipt/digest bytes remain
unchanged; new retained schema2 and utility schema2 are discriminated and utility
policy is unavailable. Pending policy and failed completion hold, never repair or
reinitialize. Interrupt remains unavailable for utilities. No database migration,
installed record, model/account probe, deployment, cleanup or native retry writer
is introduced. Source docs explain the exact authority, tool ceiling and recovery
boundaries; lead's final writing pass remains before commit.

Explicit successor source and the final reviewed central authority/domain receipt
through Manager/host/SDK publication/report/drain flows remain required current
package work. Component fixtures do not claim those combined end-to-end outcomes.

The combined utility/B2 checkpoint is committed at
`4c0bd9a0f97c15de76d45e8c5fe54a31ef7afce2`, parent
`0a647bdfcdfbf900b614cec7935f147dba79997d`, exact18 files/1720 insertions/93
removals, including lead-transferred implementer4 method/test hunks. All75 tested
inputs and every nonowned committed dependency matched before staging. The final
prose-only documentation hash is
`9271492f92b3e6fb8b28580b011f79dd45f144d6b5c04cd8ba6f4768babf092e`.
Normal commit-F/hooks preserved; committed/current inventory and hashes checked,
owned18 clean and index empty immediately after commit. Full actual receipt:
`tmp/p3i-utility-policy-commit-receipt.json`. No push or capability activation.
Lead/impl4/architects received the exact landed mapping/B2 base; full source
package remains executing. The subsequently supplied P6 fake response branch is
a new test-only delta and is not part of that committed/passing75-input claim.

## Explicit successor source checkpoint

The continuation implements an explicit new StartRequest.ReplacesRequestID on the
same instance with one newly reserved generation and retained request history in
schema2 of the existing runtime.json. Schema1 initial bytes remain unchanged.
Historical Ensure/Inspect use original host receipts without contacting the
successor socket. Exact per-request launch/config/package roots remain retained;
legacy roots are preserved. Preparation failure/uncertainty retains the new
current pointer and generation; no rollback or replacement identity escapes it.

Only a stopped terminal H0 receipt with complete exited/stopped drain evidence,
matching current boot and fresh positive owned cgroup-empty/absent proof admits
preparation. Existing loaded/pending/Unknown member, utility and resource records
refuse. H0 Inspect precedes launch.lock; the lock covers pure captured-tuple/local
proof/descriptor revalidation and publication, and releases before H0 Start's
fresh unit/job/invocation gate. No new helper verb, private receipt reader,
implicit draining or crash resume is introduced.

Verified successor startup alone may replace the fixed stale control.sock after
one same-UID ordinary-socket check, no-payload bounded connect yielding definite
ECONNREFUSED, and exact dev/inode/type/UID recheck. Initial launch, live listener,
changed path, wrong owner/type or ambiguous probe refuses. Tests operate only in
owned disposable directories; no installed runtime/socket/session was changed.

Verification retains distinct source scopes:

- Earlier frozen89-input successor/SDK cases pass4.842s, graph
  edff213078114cdc014fa4a3111dbcdf37beaa836c163e0facff0fceef6e4336,
  base3872155b55688742355b8dc16b88584f4cb5a303. They prove positive unloaded
  history reopen across generation, original Accepted receipt/generation and
  one user input after duplicate replay; historical socket exclusion, exact
  roots/config, failed Start/preparation holds, current drain and socket checks.
- Later strict runtime-schema2/old-reader/malformed history cases pass.162s.
- Full affected piruntime regression passes39.635s using exact committed
  aec5bea24c6a1bf18dd5c7941617286c869e4c7d dependencies plus only10 successor
  Go overlays. Graph490da29e884ffc90b87156de1c0bd1c31638133694be654b5e5cc5581f28c19f
  has90 inputs; compile-only .015s first. Log tmp/p3i-successor-final2-check.log;
  command26420 and parent65644 exited0, no owned survivors. Watcher's elapsed
  estimate is approximate; Go's39.635s is the check duration evidence.
- The first attempted90-input copy failed compilation before any test in1.2s:
  it captured a peer's in-progress admission.go without its new companion read.go.
  Reconstructing all nonowned inputs from the exact committed parent resolved
  that snapshot fault; no peer source change or failing runtime assertion was
  involved. Failed graph045af100458d645782e9f1ca2a347ed89c90526624f33564b14a213d517dd9c3
  and tmp/p3i-successor-final-check.log remain failed evidence.
- Final technical inspection tightened missing cgroup.events handling: only a
  definitely absent group qualifies; an existing group without events holds.
  This changes only successor_proof.go and its focused successor_test.go case.
  Final helper check uses graph
  f1d839ec6205398b26800a51082a3044b81ec07367e227ba58fa96e38ca86a29;
  its result is recorded below. Prior native/full-suite scopes are not relabeled
  as exact final-source whole-suite proof.

The proposed source inventory is10 owned runtime Go files plus docs/pi-runtime.md.
It excludes peer P2/P6 changes and the unallocated observation/native-routing
writer. No database migration, push, package activation or live lifecycle action.
Schema2 requires the separately owned old-target/read guard and current central
admission before functionality. Final independent review, combined P2 authority /
Manager-H0-SDK witness-current publication and utility original-ref/report/drain
flows, and installed verification remain named gaps. Component tests do not
establish central or installed end-to-end readiness. Lead owns state/prose pass,
index sequencing and final review; current source remains unstaged pending window.

Final affected drain helper check **passes0.015s**, command68212 terminal0;
no owned process remains. Exact11-path checkpoint packet:
`tmp/p3i-successor-checkpoint.json`. All10 Go hashes equal the final tested
graph; all nonowned test dependencies equal committed aec5 source. Index was
empty at packet preparation; peer dirty source is excluded.

Explicit successor checkpoint is committed at `cf3997b35fd1e40208e66437888d4b7d6a71916d`,
parent `aec5bea24c6a1bf18dd5c7941617286c869e4c7d`, exact11 paths,
1487 insertions/58 deletions. Every staged/committed/current hash matches the
accepted checkpoint; owned11 clean and shared index empty. Normal commit-F and
hook behavior preserved, no push. Full receipt:
`tmp/p3i-successor-commit-receipt.json`. Sole index window released immediately
before this evidence update; source reported for lead acceptance, capacity
available only after acceptance/next explicit release. Central/installed proof
and final independent review remain open; session stays open.

## Workflow observation and pre-effect barrier source

The lead-released optional port adds WorkflowObserver.ObserveWorkflow and
HostInvalidationHandler on the existing authenticated control/AttachHost stream.
Observation combines independent retained/live policy with synchronous worker
pending/streaming/bridge/policy-run/active-tool counts, callback/receipt uncertainty,
exact captured host tools, child and resource evidence. It never loads, repairs,
applies policy or submits input. Missing flags/counts/proof do not default to idle.
The public proof is ephemeral display state and never authorizes an effect.

Negotiated workflowObservations:1 initializes the host map and exact ACK before
attachment readiness. One runtime-scoped monotonic sequence and mutation-pending
interval prevent publication across mutation/attachment handoff. Queue and ACK
waiter bounds are128; overflow closes the attachment. Sequence never wraps. A
runtime that negotiated once cannot downgrade to B1 while disconnected. Earlier
B1-only attachments retain their protocol/behavior. Completion/native events
notify without ACK. Only a pre-effect invalidation waits (at most5s, subject to
operation cancellation), before conversation/receipt/native state locks; guards
recheck current permit after lock waits and at effect boundaries. Host invalidation
is pure map invalidation and must never enter runtime/domain/native locks.

Retained/utility/resource control and callback-forwarding paths share the barrier.
Resource natural Wait invalidates before publishing terminal state, without
blocking reaping/persistence on host ACK. The lead separately released utility.go,
resources.go and ordinary transport.go hooks for these existing contracts.
Ordinary callRaw closes only its owned socket on caller cancellation; the supervisor
uses one operation-local same-scanner EOF/extra-frame monitor after exact identity
validation. Closing the connection joins that monitor. The context is not a native
run lifetime: an Accepted run continues after its request ACK/socket closes.
AttachHost keeps its separate duplex path and cancellation contract.

Passing checks retain exact distinct scopes:

- First Go compile-only .012s; fake barrier/observation .492s; pure Node atomic
  policy/count cases2/2 pass216ms. A first pending-policy test used invalid same
  revision in its fixture; correcting it to existing next-revision shape changed
  no production validator.
- Frozen committed cf3997b35fd1e40208e66437888d4b7d6a71916d plus13 owned workflow
  overlays/94 inputs passes actual Manager/Unix/pinnedSDK component and affected
  B1 native callback regression6.085s, Node protocol smoke1/1 .353s. Graph:
  90c47adccb8159010dfb37739494fca25e96632a561423e52e840f2193b3c11d.
  Source log tmp/p3i-workflow-check.log. Command98924 and parent82192 terminal0,
  no owned survivors. Initial watcher50519 declined before command launch, so
  its result is incomplete; explicit parent-resolved-policy handoff then launched
  a fresh watcher. No failed SDK run or unchanged job retry is hidden.
- This native component proves initial complete idle observation; creation EX
  through persisted-input Send ACK and original Lookup/VerifyCreation while native
  callbacks independently wait SH; lock-free map invalidation still progresses;
  policy/configuration changes invalidate; pending callbacks refuse idle; cold
  observation does not load; attachment loss refuses effects; reconnect and
  authorized Load keep native IDs/history and exactly one original user input.
- The later narrow ordinary transport cancellation cases pass.243s: real Unix
  callRaw cancellation/EOF/second buffered frame while pre-ACK withheld produces
  zero retained-policy/utility/resource effects, normal ACK/close preserves an
  Accepted fake-native run and receipt, and all connection monitors join.
- Final clean committed-parent+14owned overlays/94-input graph
  8b1a880a6c1f79f28d0ab3bb0d9703f13d80f8846399f0d259ed1f16dfebc5a2
  passes changed pure/ordinary-socket/late-ACK/initial-readiness/resource-proof and
  B1 attach setup cancellation slice .741s. Compile-only .014s first. This graph
  adds only approved transport cancellation and bounded readiness/ACK-map/resource
  proof corrections after the native component; no whole-final-SDK claim.
  Log tmp/p3i-workflow-final-focused.log, command89085 terminal0.
- One intermediate test-only late-ACK variable-scope edit failed compilation;
  it ran no tests and was fixed before the final source-copy check. A tentative
  timing in an interim report was explicitly withdrawn, not pass evidence.

All nonowned graph inputs come from the committed parent rather than concurrent
P2/P6 source. No central route/frontend/metadata/native-routing change, new service,
poller/TTL/ledger, package activation, push or live lifecycle/socket action is
included. Exact P2 authority/observation-map/domain refresh composition, final
independent review and installed verification remain open integration gates.

The accepted historical-resource compatibility arm retains only Supervise's exact
verified directory privately. Successful successor startup/reclaimControl and
validateSuccessorStartup plus the existing strict Manager.records reader establish
current exact Runtime and the full connected original chain. Historical rows join
full Runtime/RequestID/schema/file/resource/operation/digest, stopped and ExitCode.
No old numeric PID/cgroup re-probe, historical rejected acceptance, second decoder,
format/registry or public/config field is introduced; resource effects stay current.
Focused17-case source check passes0.925s, then exact committed
bd329bb9775db45351db639044328546c7dae72e +ONLY14 owned overlays copy passes0.956s
with compilation against the landed P6/P2 dependencies. Graph96 inputs:
46757ba82f8c182f342894a9935c97e31a17a750064d3eb49ffeadfa977029af.
Log tmp/p3i-workflow-history-check.log, command52382 terminal0. This is the
smallest historical compatibility follow-up, not a repeated SDK/native suite.

Final15-path packet: tmp/p3i-workflow-checkpoint.json. All14 source/test hashes
match this clean parent-copy graph; every nonowned input is committed bd329.
Lead's doc prose pass is closed, SHA256
e1e7a1d93096c40579e6f72b5c5566107072123c6ccfa520cfeb9466fa39425d.
Source remains unstaged; final index window and package acceptance are lead-owned.

Workflow checkpoint is committed at `6b64c7447674340db63b96c1c07cbc2b13878748`,
parent `bd329bb9775db45351db639044328546c7dae72e`, exact15 paths/1696 insertions45
deletions. All staged/committed/current hashes match the accepted packet0847bb1d;
owned15 clean, shared index empty and short window released immediately before
this evidence. Normal commit-F/default declared hook behavior preserved, no push.
Full receipt: `tmp/p3i-workflow-commit-receipt.json`. Package reported for lead
acceptance; source capacity available after acceptance and next explicit release.
Public port consumers receive this exact committed parent, without stubs or
uncommitted dependencies. Central/combined review and installed gates remain open.
