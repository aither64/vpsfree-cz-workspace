# Codex 0.167.0 upgrade design

Design owner: architect0. Lead owns package allocation/acceptance, plan/state,
review, and authorization-bound integration/deployment. Implementers own the
application edits below. This is an investigation/design record, not deployment
or merge authorization.

## Scope and frozen selection

Upgrade codex-web compatibility, the dev-workspace packaged Codex, workspace
composition, and aitherdev's system Codex/host module through configuration.
Keep the vpsFree extension and unrelated inputs unchanged. Do not add feature
work, a packaging rewrite, a protocol redesign, or a configuration framework.

Official `openai/codex/releases/latest` selected `rust-v0.167.0`, published
2026-11-06T01:40:00Z. Its annotated tag peels to
`086ccc833bc9cf01024ad2dd6af7dbd421b6bf9a`.
Freeze llm-agents at `d960982d3b05c294f3cf98cab3e23798548a0ced`;
its `packages/codex/hashes.json` selects 0.167.0 with source hash
`sha256-9BVM0mUQ+F9QpqvnG+7x4ZXYaNTclcGLtF5DzEU5Zzg=` and cargo hash
`sha256-Dqo9nMfbkTcyT+S79U2JdXpnxwrN0fQjjMlG055jvJE=`.

The installed CLI reports 0.165.0. Workspace composition currently selects
runtime `c8edcb90dfccb720f7be6d0dd0876f254cf662cc`, codex-web
`dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`, and llm-agents
`91ff550fe42d4dd51dcf8b6bad87a0134fe7f314`.
Implementation bases can be newer than the deployed pins; retain the distinct
base, deployed and final identities in evidence.

Implementer1 realized the exact candidate from cache:

- Output: `/nix/store/22139ip2k5dfc272a1nv0br2ms0nymbv-codex-0.167.0`.
- Native: output plus `/libexec/codex/bin/codex`, SHA-256
  `13fc360e1eb73eeabeda7e2d9c6294aa56a0b062adc54a681b9d687a2e905b10`.
- Derivation: `/nix/store/9rxjqb3nzbf4b9s0bj3h4yl8igm105is-codex-0.167.0.drv`.
- Prepatch source: `/nix/store/j9bhifsiqjhxknbzmx46884jnr1lffrc-source/codex-rs`.
- Config schema SHA-256:
  `66ed795352d32f2464778acd2e332b7fafe644246d540cdceec4663c56cfbc16`.

The derivation applies daemon-nix-store.patch, a chatgpt recursion-limit
postPatch and Cargo optimization substitutions. Those do not edit config or
catalog. Implementer1's immutable reconstructed prepared-source receipt is
`/nix/store/a8rqnjz5jkqnr8fjab07a4bzrd0kid4f-codex-rs`; it incorporates the
derivation substitutions and is explicitly not the fetched source or a separate
built-source output. Config and catalog bytes match the fetched source. Official
exports alone are insufficient for our extended protocol corpus: generate
schemas from this exact native binary in private disposable state.

## Settled interfaces and invariants

The repository skill chain is workspace update-codex → configuration
update-aitherdev-codex → runtime update-dev-workspace-codex → codex-web
update-codex-web. Each implementer reads their repository instructions and skill
from their assigned checkout. Dependencies are passed as explicit roots and exact
published commits. No application source writes belong to architect0 or lead.

Preserve strict `RunEphemeralTurn` support at 0.163 with its two low-effort
profiles. Preserve prompted 0.164/0.165 support and extend it to 0.167 for
Luna low/high. Prompt instructions do not establish native tool isolation.
Preserve fixed restrictions, provider binding, immutable startup catalog and
sessionFlags-origin verification, private state, bounded output/deadline,
question rejection, retry proof and process teardown. No widening accepted
catalog content, generic version acceptance or new feature flags merely to pass
tests. Ordinary HTTP/browser authority and capabilities remain unchanged.

Exact upstream 0.165 and 0.167 full catalogs are byte-identical: 539696 bytes,
SHA-256 `1384625c0b6b3e67d3c60da29becea2b017f2c283fc1e2d05b8edafb4698eb10`.
Their derived Luna catalog is byte-identical to the existing canonical resource:
62680 bytes, SHA-256
`049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1`.
Retain canonical resources, strict provenance and historical selectors; add
0.167 provenance/selection without copying or changing identical JSON.

Keep `mkCodexPackage`: selected upstream resources still include symlinks and
do not meet the materialized helper/copy contract. System and workspace can
assemble equal native bytes in different closures. Identify actual daemon
executables independently of public CLI version or assembled output.

No workspace schema, API, database or migration change is planned. Implementer0
found all 78 upstream SQL migrations unchanged, but rollout records, replay,
canonicalization and NFS migration code changed. This does not establish safe
downgrade. Test saved-thread continuity on disposable state and keep recovery
forward-only. No simultaneous writers from old and new Codex versions.

## Sufficient implementation packages

The briefs below settle relevant interfaces and ownership. Lead acceptance is
required to release them. Pending verification results block acceptance or
deployment, not safe independent source preparation. Members retain their own
worktrees and exclusive repository index/commit/rebase windows.

### W — codex-web compatibility; owner implementer0

**Sufficient for implementation now.** No unresolved design blocker. Base
`dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`; evidence
[codex-web-prep.md](codex-web-prep.md). Native/source handoff comes from R.

Files: `skills/update-codex-web/SKILL.md`, its `scripts/refresh-catalogs.py`, new
0.167 prompted provenance under `codex/testdata/`, existing native ephemeral,
state-upgrade and conditional-steer test files, and `docs/reference.md`.
Touch `codex/client.go`, protocol validators/fixtures or policy only for an
observed incompatible consumed field/config contract; report a consequential
contract change through lead before implementation. No binary flake dependency.

Add the bounded 0.167 helper/provenance path, prompted exact-native selector,
0.165→0.167 state-upgrade selector and relevant actual-binary selector. Preserve
old tests/resources. Do not implement optional newly advertised native features.
Official changes are mostly additive; there is no demonstrated core-client break.

Acceptance: supported old contracts remain explicit, generated selected-binary
schemas satisfy every actual request call site and consumed field, fixed config
keys/types remain valid, catalog provenance matches exact bytes, and final native
selectors enforce reviewed version/hash/source. Unknown behavior remains a gate,
not an assertion of compatibility.

Quick checks in repository Nix environment: focused Go/browser checks,
`test/codex_protocol_contract.py` against generated experimental schemas and
`test/codex_ephemeral_config_contract.py` against selected patched config schema;
run helper for 0.167 and prove historical canonical resources unchanged. Record
actual commands, base/head, diff, source/native/catalog identities and no new
migrations. Lead coordinates final review after commits and quick checks.

After review, a fresh watcher runs namespace ownership before prompted 0.167
native tests, supported Luna effort coverage, conditional-steer native acceptance
and 0.165→0.167 saved-thread/state fixture. Existing strict fixture evidence is
retained; rerun strict lanes if common changes affect them. Record actual tool
schemas, output, retries, questions, cancellation, teardown and separate old-reader
observations. Native fixture failure blocks release; fake/schema checks do not
prove native tool behavior or real-provider naming.

### R — runtime package and naming; owner implementer1

**Sufficient for independent source preparation.** Final pin/module/vendor commit
depends on W's published accepted source; final checks use that exact dependency.
Base `32a5e31bc32362b436ccc0cfc45b5d1b74f64cb6`.

Files: `flake.nix`, scoped `flake.lock`, `portal/go.mod`, `portal/go.sum`,
`nix/workspace-portal.nix`, `portal/cmd/workspace-portal/naming_runtime.go`, current
naming/native integration fixtures and relevant current actual-binary fixtures,
`nix/tests/session-creation.nix`, `docs/codex-package.md`,
`docs/session-preparations.md`, runtime update skill if needed. Preserve unrelated
retained-version fixtures; do not globally replace version text.

Pin frozen llm-agents, then exact published W revision in both Nix and Go.
Run go mod tidy and refresh vendorHash from a genuinely fresh dependency
derivation. Update exact host/child version prerequisites and actual native
hash/source fixtures together; immutable catalog hash/size remain unchanged.
Preserve unavailable-on-version-mismatch naming, local-only child launch,
ordinary-daemon continuity, deadline, cancellation and supported forward recovery.

Quick acceptance: focused Go/Ruby/browser and naming tests, local workspace
protocol corpus against candidate schemas, pin consistency, package contract,
fresh vendor proof and source/native identity. Documentation records supported
0.167 behavior without erasing retained support. After combined review, run
packaged checks and managed naming lifecycle/failure/forced-exit/continuity tests
plus required native runtime lanes selected from actual candidate fixtures.
Positive real-provider naming uses explicit existing authorization and unchanged
serving transport; it is distinct from synthetic checks.

### C — aitherdev configuration; owner implementer2

**Sufficient; final channel edits depend on R's published final revision.**
Base `1072f89f932ad570fb6d14007387d230549ccd14`; evidence
[configuration-evidence.md](configuration-evidence.md).

Only channel-managed inputs expected: `llm-agents/llm-agents` to the frozen
revision, then `dev-workspace/devWorkspace` to final R using
`confctl inputs channel set --commit` (llm-agents uses `--no-changelog`). Keep
generated messages and consolidate superseded updates. Preserve other channel
identities and build actual semantic source graphs, not alias-assuming metadata.

Validate the entire managed DeepSeek config against selected config schema.
System Codex and codex-ds both use the existing assembled package. Preserve
provider env_key and credentials; no forced shared OpenAI login setting.
No profile edits are currently justified. Schema-discovered changes affecting
provider behavior return through lead. No application added to system profile.

Quick checks: evaluated versions, exact inputs, schema validation, hooks and
diff. After review: exact committed aitherdev system build, generation/build-plan
receipt and copy preparation. Activation belongs to lead under machine ownership;
no implicit reboot. Verify system/profile/native identities and the actual Home
Manager codex-ds wrapper; use one authorized ephemeral strict-config provider
request, not `--help`, for startup validation.

### S — workspace composition; owner implementer3

**Sufficient; final edit depends on R's published final revision, final joint
check also depends on C's final locks.** Initial base
`527362b66eb903819ccb13ebb1e62495887195ca`.

Files: feature checkout `flake.nix` and generated `flake.lock` only. Select R via
`inputs.vpsfree-dev-workspace.inputs.dev-workspace.url`; run scoped
`nix flake update vpsfree-dev-workspace/dev-workspace`. Preserve extension
`f8da821e3c76e26e73aa9d89a712eab0e0faa319` and
`sha256-U5y/TEny6nsyXWNlCMktmxTZhpVO0QY4kOo/qgwsapM=`, sibling input graphs and
follows paths. No incidental lock deduplication or new top-level runtime input.

Quick acceptance: semantic before/after graph and
`bin/check-dev-workspace-deployment --workspace-root WORKSPACE_ROOT --configuration-root CONFIGURATION_ROOT`.
That check proves matching runtime and site contracts, not Codex/native or Go
identity; retain R/C's separate evidence. After review: final composed output
build and applicable composition checks. Lead owns selected profile activation.

## Review, rollout and recovery dependencies

Dependency order: W published commit → R published commit → C and S independent
consumer updates → combined final review → required long/native/system/application
checks → authorized system activation → dependent application profile activation.
Build/copy and readiness evidence are prepared before acquiring machine ownership.
Read installed `workspace-host coordination guide` and authoritative policy before
activation/integration; retained operations keep their original recovery contracts.

Changed native invocation requires idle sessions. Do not interrupt other sessions,
reconcile them implicitly or bypass package-transition refusals. Preserve current
and old system/profile paths, roots, conversations and journals; repeat an uncertain
original transition instead of starting a conflicting mutation. Application
recovery selects a corrected forward generation through the supported operation.
System rollback requires independent proof that its old Codex can read new state;
an old-reader probe alone does not authorize old writes.

Lead's rollout receipt must bind complete source/input graphs, native/assembled
outputs, system/profile paths, repo targets, machine aliases, deployed/final heads
and fresh remote ancestry. Verify portal/terminal/browser health, providers,
naming and saved-thread resume/fork. Release the exact owned machine claim promptly
only after verified effects and complete deployed lineage integration into approved
remote defaults, then verify resulting claim state. Missing approval/integration
evidence keeps a deployed hold. Release never authorizes session cleanup.

Integration requires separate explicit user direction. Review gets complete
base-to-head series, final diffs, pin consolidation and explicit migration
conclusions. Approved merge claims cover only fresh target check, required-hook
FF merge, push and remote proof; release before records/tests. Workspace shared
master integration additionally takes the tracking lock without waiting. No
archive/delete/stop/cleanup action is part of these packages.

## Remaining gates

No unresolved product/design decision blocks W or independent R preparation.
Selected-binary schemas/config checks, patched-source receipt, native behavior,
state continuity, final published dependency heads, final review, long checks and
authorization-bound rollout remain acceptance gates owned above. Any unexpected
incompatible request/config, persistent-state behavior or package transition
returns to architect and lead with the concrete failure and smallest correction.

## W1 — concurrent first-open correction

Owner: implementer0, as a narrow addition to W. **Sufficient brief; pending lead
acceptance before source edits.** R's final dependency pin waits for the corrected
published W head. This correction changes startup ordering, not the storage
format, native protocol or supported recovery boundary.

### Evidence and cause

CI run `42532327561`, attempt 1, W head
`7e3143bd508153d8c1860b2a916029ee9b8c455b`, failed
`TestConditionalSteerConcurrentClientsShareOneClaim/database=true` with
`SQLITE_BUSY`. Implementer0 reproduced 2/20 failures on that head and 3/30 on
exact baseline `dd90fb4308ba85617ee2a4267cc835aa9a4f11ce` with the unchanged
cold-client test. One diagnostic error-label overlay identified
`initial user_version/connection bootstrap`; a subsequent passing diagnostic
batch is not corrective validation. Evidence: `codex-web-ci-42532327561.log`
and `/tmp/cw-w-diag/{baseline,current-overlay,current-stage}.log`.

`openSubmissionDatabaseLocked` creates a lazy `sql.DB` with busy timeout, WAL
and FULL pragmas. `initializeSubmissionDatabase` first queries user_version,
opening the connection and applying those pragmas, then creates schema and
reads migration phase. Only afterward does it acquire the predecessor locks.
The driver already applies busy timeout first. Concurrent fresh clients can
therefore race during connection/WAL bootstrap before existing serialization.
This is an observed supported-startup defect also present on baseline; warming
the test database or retrying CI would conceal it.

### Smallest correction and ownership

Files: `codex/submission_migration.go`, focused
`codex/submission_database_test.go` coverage, and a short clarification in
`docs/submission-storage.md`. Keep the existing conditional-steer concurrency
test's cold setup and assertions unchanged. No driver update, generic retry
layer, new lock file, process-global mutex or database refactor.

After the existing database/predecessor equality rejection, construct the same
primary/legacy path list and acquire `lockSubmissionPredecessors` before the
first SQLite operation. Its sorted, context-aware file locks already serialize
all cooperating clients and are released on every exit. Hold them through
bootstrap, phase inspection, import and fence publication/verification. Call
`verifySubmissionFencesLocked` directly in the ready branch. Remove the now
redundant later lock acquisition/phase recheck and the unused locking wrapper;
do not recursively acquire the same flocks. Creating the private empty database
file before lock acquisition may remain unchanged; connection initialization
and schema writes must wait.

Both architect and implementer inspected the caller chain: only initialization
calls the locking verification wrapper; the per-client queue mutex precedes
initialization, and no predecessor flock is already held there. Cooperating
clients already must share database and predecessor identities. Ordinary
transactions after initialization retain SQLite concurrency and existing claims;
the predecessor locks are not held for network requests or the client's lifetime.

### Invariants and acceptance

Preserve WAL/FULL, busy_timeout(5000), max-one connection, existing bounded
startup context, atomic version-0 schema creation with BEGIN IMMEDIATE, and
version-1 fail-closed handling of missing/corrupt receipt tables. Preserve exact
source identities, checksummed backups, imported/ready journal recovery,
predecessor fences and all uncertain/submitting/accepted receipt semantics.
Propagate lock cancellation and real SQLite/import errors; do not reclassify
them as successful startup or automatically repeat mutation attempts.

No new migration or stored format is introduced. Existing databases and
interrupted imports remain readable under the same supported contract. Old
client binaries retain their startup race; the fix does not claim to coordinate
their pre-lock work. Application migration still excludes predecessor writers,
and recovery stays forward-only.

### Checks and evidence

1. Add a deterministic first-open lock regression: hold the actual predecessor
   flock, attempt initialization with a short bounded context, require its
   cancellation error and nil `c.submission`, and prove no SQLite header/schema
   or WAL was initialized. An empty private database file is permitted. Release
   the lock and prove the same client can initialize successfully.
2. Cover simultaneous cold clients preserving distinct attempts without a seed
   operation; retain the existing warm concurrency coverage. Keep the original
   conditional-steer test proving one native claim/steer and the shared receipt.
3. Run the cold conditional-steer lane for one bounded 100-iteration batch, plus
   focused submission database/import/fence/cancellation tests in the declared
   Nix environment. Stop on the first remaining mechanism failure, diagnose that
   observed stage, and report it rather than adding retries or more batches.
4. Pass ordinary quick checks, commit the correction with its reason, and include
   this production change and complete branch history in final independent review.
   Refresh consumers to that final published head. Long/native checks retain
   their existing post-review ordering and watcher requirements.

Acceptance evidence names exact old/new heads, commands/results and preserves
the original CI failure/root cause. State explicitly that no new schema migration
was added and no existing migration history was rewritten. Lead accepts the brief
and package result; implementer0 owns implementation and any review fixes.

## R2 — selected-native provider incompatibility

**Deployment/acceptance blocker; no implementation released.** Preserve concurrent
explicit session providers and retained provider switching unless the user changes
that product requirement. This conclusion is bounded to the exact 0.167 guard,
config schema, App Server CLI/request surface, existing provider documentation,
and implementer1's creation CI evidence. The authorized minimal private native
start/resume control is owned by implementer1; no broad VM rerun is needed to
choose the next design.

CI `42534510998`, creation job `128895731073`, log line 5063 rejects the first
explicit alternate-provider session's resume with RPC -32600: saved alternate,
current primary. The accepted browser selection and runtime request are alternate,
gpt-5.5/high. This is consistent with the exact selected prepared source at
`/nix/store/a8rqnjz5jkqnr8fjab07a4bzrd0kid4f-codex-rs`:

- `app-server/src/config_manager.rs:247`: `load_latest_config` supplies no request
  overrides and default typed overrides; it reloads the server/cwd selection.
- `config_manager.rs:434`: `check_thread_model_provider_for_input` retains the
  managed-policy check, then unconditionally requires the thread provider to equal
  that current selection. There is no feature/config/capability conditional around
  this comparison.
- `config_manager.rs:539`: `load_for_resume` computes current selection before
  applying resume overrides, checks configured providers and managed requirements,
  then requires **both** saved and requested providers to equal current selection.
- `request_processors/thread_processor.rs:4759` applies the same input check to
  a loaded resume. Turn/steer, queue and goal paths also call the input guard.
- `config_manager_provider_tests.rs:269` explicitly tests effective selection:
  a retained gateway thread is accepted under matching selection and refused
  under default OpenAI selection. The mismatch is intentional native behavior.

The inspected `core/config.schema.json` exposes `model_provider` and provider
definitions but no provider-mismatch admission policy. `cli/src/main.rs`'s
`AppServerCommand` and `app-server/src/startup_config.rs` expose no exception flag.
`app-server-protocol/src/protocol/v2/thread.rs:354` exposes resume `modelProvider`
and `config`, but the guard above runs against the pre-override selection. These
public fields do not supply a supported escape from the check.

**No supported minimal invocation preserves the present contract.** A global
`-c model_provider=...` can select one provider for that server, not concurrent
different explicit providers. Per-cwd selection alone cannot preserve an existing
P→Q switch: the saved P and requested Q would both have to equal one current
selection. Shared config rewrites would also invalidate other active sessions.
Removing the explicit request does not remove the saved-provider check. Disabling
strict config or changing the test's expected failure cannot repair behavior.

The runtime's `docs/codex-providers.md` promises per-session explicit/inherited
selection and provider changes on the same daemon without a native patch. That
contract is now incompatible with the unmodified selected 0.167 native output.
The previous general upgrade acceptance assumptions are therefore conditional
on resolving this blocker; no rollout should proceed on the earlier schema-only
compatibility conclusion.

### Product options for the lead/user

1. Preserve behavior and ship 0.167 with a narrowly scoped downstream native
   compatibility change. The candidate design would preserve configured-provider,
   authentication and managed-policy requirements while restoring explicit
   retained/request provider routing; simply deleting all provider validation is
   unacceptable. This is the smallest code surface identified, but changes the
   source/binary/package identities, requires a Rust rebuild and new exact-native,
   provider-switch and package verification. It needs explicit scope/design
   acceptance before an implementation brief or patch. No claim of proven patch
   correctness is made here.
2. Retain the installed 0.165 runtime while awaiting a compatible upstream
   release or deciding the correction above. This preserves existing behavior
   and avoids an unsafe deployment, but does not complete the latest-0.167 task.
3. Adopt 0.167's one-selected-provider behavior only after an explicit user
   decision to change the product contract, with a migration/support design for
   existing explicit sessions. This is a regression and not an acceptable routine
   upgrade correction. Separate provider daemons/routing would be a substantially
   larger architecture project and is not proposed for this bounded update.

No global live provider change, thread-history rewrite, credential copy, native
patch or routing subsystem is authorized by this finding. Keep the exact failure
and CI's successful primary cases distinct from any later corrected-binary evidence.

### Bounded native probe outcome

Implementer1's one authorized no-inference probe is **incomplete for resume
compatibility**, not a successful reproduction or a compatibility pass. The exact
0.167 binary (SHA-256 `13fc360e1eb73eeabeda7e2d9c6294aa56a0b062adc54a681b9d687a2e905b10`)
initialized and accepted primary and alternate `thread/start`, echoing the expected
provider/model/high effort. All four resume variants, including the primary
control and alternate explicit-provider/config-only/both cases, failed earlier
with RPC -32600 `no rollout found for thread id ...`. Untouched no-inference
threads had not materialized a rollout, so none reached the provider comparison.

There were zero synthetic HTTP requests/POSTs and no model calls or credentials.
Implementer1 reports process 3129318 exited 0, reader/server joined and process
group empty after 1.574 seconds. Evidence is in
`runtime-provider-probe/{result.json,frames.json,stderr.log}`; disposable script
and log are `/tmp/codex-r-0167-provider-probe.py` and
`/tmp/codex-r-0167-provider-probe.log`. No rerun, history seeding or rewriting was
attempted or released. The product blocker remains established by the creation
CI and exact source above; this probe adds no independent resume confirmation.
