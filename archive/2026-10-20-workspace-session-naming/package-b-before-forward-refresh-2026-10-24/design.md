# Session naming: approved implementation design

Status: approved for implementation, 2026-10-22, following the user's
"Implement the plan" direction. The final total naming budget is **30 seconds**;
earlier 10- and 15-second proposals are superseded. The architect owns this
brief; implementers own application edits. The lead owns plan/state, review and
deployment coordination. This brief grants no default-branch merge authority.

## Forward refresh before rollout — 2026-10-24

This section supersedes the implementation-baseline and exact-head rollout
assumptions below. The naming contract remains unchanged. The lead reports that
the unused machine claim was released at revision 3 on 2026-10-24; our initiative
has attempted no activation. Prepare the refresh outside machine ownership.
Do not select the previously built
`/nix/store/laryzlmk7lh9mg64ymfnb0iv7syms8l8-dev-workspace-0.2.0`.

### Established provenance and downgrade boundary

The selected package is
`/nix/store/l9sc1ksacdkm7iij99ggyg87bqsp9n15-dev-workspace-0.2.0`.
Read-only `nix derivation show` identifies its derivation as
`/nix/store/48n33d9ds4kssi4in9ijjaplr691bjaa-dev-workspace-0.2.0.drv`
and its `src` as
`/nix/store/igy5j2nx7n4andbi1ibfwd06jb93i5z6-source`.
The installed update skills also identify the composed workspace source
`/nix/store/ka50bkd0b175d61xynjyx7shnz9np15x-source` and client source
`/nix/store/549mbnzpbcs81ccvvv4wrh9xmjrxg86n-source`.
That workspace source's `flake.lock` and the runtime source's `flake.lock`
record runtime **b3a6eb2fc0b41cf0cb965bf4c39991815d9df734** and client
**11ec57d2203fc735696fe75a837d47da55a5c6af**. `nix hash path` independently
matched both immutable source directories to those locked NAR hashes:
`sha256-66oPdEj2gNM/Ty43eiF9xYqCfEWQnTCAFV3yMI9sRwQ=` and
`sha256-tWV8OX1uCr9fjcCvZBgwYYn+O9XvM1xpY+kPv4vgFSY=` respectively.
These are source/input proofs, not SHA guesses from output names. The composed
workspace's own Git SHA and the currently running system configuration's SHA
were not established by this bounded consultation.

Existing local `origin/master` refs equal those installed A/B revisions; no
fetch or remote freshness claim was made. Old local `master` refs are stale.
The naming branches diverge: A has 1 naming commit versus 8 baseline commits
since `ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5`; B has 4 naming/test commits
versus 18 baseline commits since
`bf6d4b0c49600c15e17fe71248807ef43424e932`. Neither installed A/B head includes
our naming patch. Later preparation must establish fresh target ancestry before
choosing its base; preserve at least these deployed heads.

Direct selection would discard deployed automatic failed-turn recovery and
session retry controls, shared-write cancellation isolation, bounded runtime
admission, accepted plan/fork recovery, conversation retirement during deletion,
failed-creation deletion recovery, and the native service descriptor limit.
The decisive state boundary is installed
`portal/internal/session/runtime-contract.json:9–10`: it adds
`turnRetryStateSchema: 1` and `turnRetrySessionPolicy: 1`; our old candidate
advertises neither. Installed `libexec/workspace-host:2904–2955` refuses a
candidate lacking support when retry records or policy sidecars exist.
`docs/turn-retry-recovery.md:226–249` requires forward recovery and preservation
even for canceled retries or malformed policy. This consultation did not inspect
other sessions' private state and does not claim whether those guards would
currently trigger. The behavior regression alone rules out the old candidate.
Do not delete state or weaken capability checks to enable a switch.

The native dependency remains exactly
`/nix/store/zgxck45jn2z9yf70rk6d794pdn6mq3ca-codex-package-0.163.0.drv`
in both application derivations. The naming catalog
`codex/ephemeral_luna_models.json` is byte-identical between installed and
candidate clients. Their installed team catalogs are byte-identical with the
same declared digest `840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa`.
The composed locks differ only in runtime/client nodes; extension
`767dfd587e346168e1443e65ccdb67ce748f3fe3`, native inputs and all sibling/follows
paths are unchanged. Coordination, claim, repository-claim and integration
contract files agree. The coordination catalog differs only in the generated
confctl adapter store path, not resource mappings or protocol. Preserve these
identities and the installed provider configuration; no native/model/provider
upgrade or new configuration policy is part of this refresh.

### Independent packages and dependent composition

- **A / implementer0:** refresh the reviewed `4300c40` naming change onto a
  verified baseline containing installed client `11ec57d`. Keep new continuation,
  prepared-send, turn-context, retry UI and shared-write cancellation behavior.
  The three-way changed-file overlap is `docs/reference.md` and
  `test/codex_protocol_contract.py`; merge their additions rather than replacing
  them. Preserve A's private retry metadata/accessor, exact settlement and
  cleanup proofs, early-event validation, native-progress handling and fixed
  deadline. Do not broaden classification or let naming cancellation disconnect
  another caller. Keep corrected native fixture advice/launch policy below.
- **B / implementer1:** refresh naming/manual recovery onto a verified baseline
  containing installed runtime `b3a6eb2f`. Naming implementation files do not
  overlap baseline changes; docs, dependency/package files and the attention
  test do. Preserve the new retry subsystem, runtime-contract capabilities,
  admission/creation/deletion recovery and service limits. Retain one original
  30-second deadline, two operation slots, at most two safe utility calls,
  200 ms cancelable backoff, and the 1-second inference plus 250-ms cleanup
  admission reserve. Resolve provider once; ultimate failure stays before slug
  reservation with saved inputs and manual controls.
- **B history reconciliation:** installed
  `portal/internal/web/attention_browser_test.cjs:1611–1623` already waits on
  the same explicit deferred stage as our `915b904` follow-up. It uses a
  2-second test bound and diagnostic instead of our 5-second bound and
  `Promise.race`. `git cherry` does **not** identify literal patch equivalence.
  Preserve the installed test and omit our redundant readiness follow-up after
  recording this semantic comparison; do not overwrite it or claim identical
  patches. Installed baseline does not change `test/archive_lifecycle_browser.cjs`;
  retain the reviewed `e515437` bounded/privacy-preserving diagnostic change.
- **Dependent pins:** B owns its exact refreshed A pin in `flake.nix`,
  `flake.lock`, `portal/go.mod`, `portal/go.sum` and package dependency hash.
  A and B can prepare independent source work concurrently; final B checks and
  publication depend on exact published A. Consolidate superseded pin updates
  into the final logical update while retaining original review/provenance.
- **C / implementer0 after B:** refresh the workspace feature and configuration
  feature from current verified default baselines, preserving newer deployed
  source/configuration behavior. Select exact final B in configuration's
  `dev-workspace` channel / `devWorkspace` role and workspace's existing nested
  runtime override. Retain extension/sibling/follows identities. Reconcile
  changed catalog adapter paths through composition, not manual store-path
  replacement. Lead owns current system provenance and activation records.

Application edits are released only when this saved brief is announced to the
lead and both owners. This is a forward refresh of the approved scope, not
default-branch integration approval. The lead serializes Git operations within
each repository. Route consequential conflict resolutions to the architect/lead;
do not redesign upstream behavior to make the naming patch apply.

### Compatibility and verification for refreshed heads

No new persisted schema or migration is needed by naming. Carry the installed
schema-1 retry/policy readers and writers and existing native submission receipts
unchanged. Pending retries, stopped chains, retained settings, roster/provider
identity and interrupted lifecycle recovery must survive the forward package.
Rollback to the old naming candidate is not supported. New package recovery
continues forward with the same state capabilities; no live state repair or
lifecycle action is authorized by this brief.

Preserve previous exact-head PASS/review/build receipts as historical evidence.
Use range-diff plus the complete final branch/history/migration inventory for
review; an omitted redundant test must have its explicit baseline disposition.
Baseline drift is substantive even where our naming patch applies cleanly.
Independent affected-lane review must cover preservation and conflict resolution
before long checks. Do not recertify new heads from tree similarity alone.
Reuse successful checks only when the exact derivation and complete input
receipts match; a matching derivation may remain satisfied in Nix without a
rerun. Changed derivations require verification on the refreshed inputs.

Quick selections in the owning Nix environment (commands are a plan, not runs):

```sh
# A: naming plus new shared-client/continuation behavior
nix develop --command go test -mod=readonly ./codex -run '^(TestEphemeral|TestCanceledWrite|TestAlreadyCanceledWrite|TestContinueFailedTurn|TestContinuation)' -count=1
nix develop --command python3 test/codex_protocol_contract.py --coverage-only codex/client.go
# B: manual recovery, generation fencing and accepted-fork contention
# Use an absent disposable DEV_WORKSPACES_CODEX_PROVIDERS path as before.
nix develop --command go -C portal test -mod=readonly ./internal/web -run '^(TestSessionNam|TestSessionPreparation|TestCreationAdmission|TestCreationRechecksGeneration|TestAcceptedForkSourceSharedLockRefusalAndReceiptRecovery)' -count=1
nix develop --command node --test portal/internal/web/attention_browser_test.cjs
nix develop --command node --check test/archive_lifecycle_browser.cjs
# C: exact final semantic input graph
bin/check-dev-workspace-deployment --workspace-root WORKSPACE_FEATURE --configuration-root CONFIGURATION_FEATURE
```

Keep terminal/permanent/uncertain-start/cancellation tests, late-error settlement
invalidation, native retry-progress success, safely settled fresh-call success,
persistent two-call exhaustion, provider freeze and preserved manual inputs.
Exercise retained retry-policy capability refusal using existing disposable
profile-transition tests; no live retry-record inspection or modification.

After committed final heads, quick checks and review, the lead assigns a fresh
watcher to the same acceptance lanes in
`verification-packages-e5154378-result.json`: A flake, B package, session-creation,
session-archive-lifecycle and full flake, plus the disposable real-collector/portal
probe. Use `nix flake check --no-write-lock-file --print-build-logs`; B builds use
`nix build --no-link --no-write-lock-file --print-build-logs --max-jobs 1`
with `.#checks.x86_64-linux.package`, `.#checks.x86_64-linux.session-creation`
and `.#checks.x86_64-linux.session-archive-lifecycle`. Confirm complete Ruby shard coverage, including
the retained retry-policy and failed-creation recovery tests supplied by B's
new baseline. Reuse individual unchanged shard derivations with receipts.

Rebind `verify-native.sh` to the new exact A head and catalog source, verify the
unchanged native binary digest, then run its existing namespace-ownership and
ephemeral-protocol selectors with `-tags=codex_integration`. Its current
`4300c40` guard must not be bypassed. Rebind the existing collection probe to
the exact clean final B head only after checking its fixture seams. Preserve
its actual-collector plus portal admission/handoff and preparation/activation
exclusion claims; it does not prove a usable native conversation during a sweep.
No new broad fixture framework is required.

Finally rebuild exact C system/application outputs and capture fresh complete
input/derivation receipts. Copy before reacquiring the machine. Lead rechecks
the then-selected package/system baseline and ordinary transition guards before
system dry-activate/switch then application profile activation, with no reboot.
Fresh deployment acceptance includes portal health, naming within 30 seconds,
manual failure recovery, conversation continuity and retained retry capability.
No activation, native test, build, fetch, rebase or application edit was performed
as part of this architectural consultation.

## Scope and required behavior

Automatic naming must produce a useful name from the request. Transient provider
errors receive native retry and, where safe, an automatic fresh utility attempt
within one thirty-second
total budget. Successful naming returns immediately; there is no minimum wait.
If naming ultimately fails,
stop before reserving a session identity and offer the existing **Retry naming**
and **Use name and continue** controls. Preserve the accepted request, files,
provider and team/model settings. Successful automatic naming needs no user
confirmation. Do not use a generic or heuristic fallback.

For the example goal, a suitable proposed name is
`2026-10-21-php-upload-progress-mitigation`. This is a human recommendation,
not output observed from the failed model call.

Affected projects are `codex-web` (ephemeral error-notification handling),
`dev-workspace` (fallback policy and consuming the corrected client), the
coordination workspace (composed runtime selection), and
`vpsfree-cz-configuration` (matching aitherdev host contract pin). No PHP
configuration changes or changes to the example session are in scope.

## Evidence and confidence

Identity was verified with `dev-session current` and both environment values:
`2026-10-20-workspace-session-naming`, workspace
`/home/aither/workspace/ai/vpsfree.cz`. The retained roster identifies
`architect0` as the design owner, Astra/xhigh, with workspace-write access.

The selected runtime resolves to
`/nix/store/1pbxq09x01amjaczfxq3lzyh8s6mq6kp-dev-workspace-0.2.0`.
Its derivation identifies source
`/nix/store/vwknkmiinqdz775qb0y7arpjpv2qk8mz-source`; the naming files and
README/preparation guide are byte-identical to locally available dev-workspace
master `52dcd471186ef874c5c93f4133744195d4815454`. Its
`portal/go.mod:7` pins codex-web `57972192e30f`. These are installed-source
observations, not an assumption that current master is deployed.

Proven facts:

- The retained creation receipt for `2026-10-21-development-session` contains
  the original request to mitigate PHP vulnerabilities using
  `session.upload_progress.enabled = Off` throughout
  `vpsfree-cz-configuration`, and to report machines and a confctl command.
  Its selected provider is `codex-lb`.
- The private preparation mapping
  `session-preparation-mappings/bcbf95aa-1c45-4f3d-8b56-f597c51c68ee.json:1`
  records `namingOutcome: utility_error` and the generic slug.
  The mapping is under
  `/home/aither/.local/state/dev-workspaces/portal/vpsfree.cz-8a2a555cb2f65b33/`.
- The portal service journal at **2026-10-21 07:36:47 UTC** records
  `session naming duration_ms=1451 outcome=utility_error category=server`.
  At 07:40:01 it records a separate successful model naming call after 2613 ms.
  Thus naming is wired up and can succeed; this example is a failed utility
  call, not a model choosing the words `development-session`.
- Read-only inspection of `/home/aither/.codex/logs_2.sqlite`, table `logs`,
  row **810054713**, identifies naming thread
  `01a15d64-2511-7c03-bc62-c17e46c8d7bd` and turn
  `01a15d64-260d-75a0-b44b-870fc39bcb6e`, model `gpt-6-luna`, effort `low`.
  The native client reports: `stream disconnected before completion: Preferred
  account is not available`, and schedules retry **1/5 after 192 ms**.
- Rows **810054715–810054719** immediately show an App Server `error` event,
  a `turn/interrupt` request, and abortion of that same turn. Process identity
  is `pid:225653:714aee84-19bf-4221-aa88-48b47dffcba3`.
- In pinned codex-web, `codex/ephemeral.go:741–743` treats every `error`
  notification as `ErrEphemeralServer`, without inspecting its parameters or
  distinguishing a retry notification. Lines **126–128** interrupt an owned
  turn on failure. This is the source defect to correct.
- Installed dev-workspace `portal/internal/web/session_namer.go:48–49`
  wraps utility errors with `errSessionNamingFallback`;
  `session_name.go:112–116` converts that error into successful naming with
  `development-session`. Queue timeout does the same at **96–101**.
  `preparation.go:532–546` then saves the base and reserves the slug.
- Git history locates the regression at **fdb13f8381946347da6301218cdf591e98ca4693**,
  `portal: continue session creation when automatic naming fails`, dated
  **2026-10-20 19:48:59 +02:00**. It introduced that fallback and changed queue
  timeout from a naming error to successful generic naming. The earlier
  **0a9bd5f63916ab0393dcb8934bfbe63e833b1d96** change on October 14 introduced
  stopping before reservation and manual selection on the saved request.
- The manual flow still exists: `preparation.go:765–769` enables name choice
  only while stopped and without a slug/handoff; `templates/creation.html:23–27`
  contains the form; `static/creation.js:147–151` exposes **Retry naming** and
  that form. The regression bypasses it by converting failure into success.

The causal connection from the retryable native warning to the unconditional
error handler and interrupt is strongly supported by the adjacent logs and
source. The retained outgoing-event log records the method, not the full
notification payload, so the incident's exact `willRetry` value was not directly
observed. No wire replay or live API call was made. The provider's reason for
the preferred account being unavailable, and whether its next attempt would
have succeeded, remain unknown. Do not claim a particular account, quota or
load-balancer fault. No evidence justifies changing the naming prompt or model
to repair this incident.

## Original implementation baseline (superseded for rollout)

The selected package is now
`/nix/store/4cn1hh88xdpql5jp9pyrnf5fvnqsc829-dev-workspace-0.2.0`, with source
`/nix/store/7lwlcd2vxv9490pgrlbj0vlpq95x60lc-source`. Its two naming adapter
files and naming-runtime launcher are unchanged from the investigated revision;
its codex-web dependency has advanced to `ea64ef57fdd2`. That revision's
`codex/ephemeral.go` and unit test are unchanged from `57972192e30f`.
Implementer A starts from freshly fetched codex-web
`ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5`; B starts from dev-workspace
`bf6d4b0c49600c15e17fe71248807ef43424e932`. Preserve intervening unrelated
changes and refresh dependencies from those baselines, not the older local
master refs. No new root-cause investigation is required.

## Interfaces, files and invariants

1. **Preserve retryable native errors in codex-web.** Correct
   `codex/ephemeral.go` to distinguish a validated error notification with
   `willRetry: true` from terminal failure. Validate its owned thread/turn and
   connection generation. Keep waiting for the exact successful completion
   within the existing hard deadline; do not treat the warning as output or
   reset the deadline. Fatal errors and malformed/foreign notifications remain
   failures. Preserve exact-turn interruption, cleanup reserve, output
   validation and the private tool-free runtime. Add
   `CanRetryEphemeralTurn(err error) bool`, backed by private typed error
   metadata and discoverable through `errors.As` across wrapping. Keep the
   `RunEphemeralTurn` signature and existing `errors.Is` categories. Expose no
   retry-error constructor and no raw remote diagnostics. The accessor returns
   true only for an allowed transient failure AND proved stopped execution
   plus successful applicable cleanup. Generic `ErrEphemeralServer` is false.
2. **Restore failure recovery in dev-workspace.** Remove
   `errSessionNamingFallback` and all automatic `development-session` success
   paths from `portal/internal/web/session_name.go` and `session_namer.go`.
   Automatically retry a clearly transient terminal failure when the previous
   utility attempt is settled and enough of the original deadline remains.
   On unavailable runtime, unrecoverable utility error, exhausted retry budget,
   invalid output or queue timeout, return the existing naming error with no
   base. Reuse the existing failed preparation, retry and custom-name APIs;
   a successful automatic name proceeds immediately. Do not derive words
   heuristically or create an interim generic session.
3. **Retain clear progress and diagnostics.** Existing naming progress and
   stopped/manual controls express the two paths without a routine approval
   step. Keep safe outcome/category logging; include the preparation request ID
   for correlation if useful. Do not log raw provider errors, prompts or model
   outputs. Remove the contradictory fallback description in
   `docs/session-preparations.md:145–154`; preserve and reconcile the manual
   recovery explanation already present later in that file and in
   `docs/workspace-portal.md:1202–1209`.

The pinned **Codex 0.163.0** native source is
`/nix/store/9is267xl3palxb615kk86qlli9nggkf9-source`. Read its
`codex-rs/app-server-protocol/schema/json/v2/ErrorNotification.json` and
companion TypeScript `ErrorNotification.ts`, `TurnError.ts`, and
`CodexErrorInfo.ts` under `schema/typescript/v2`. No code generation or Codex
upgrade is needed. ErrorNotification requires `error`, `threadId`, `turnId`
and boolean `willRetry`. The JSON TurnError requires only `message`; its
`codexErrorInfo`, `additionalDetails` and `misalignment` may be absent or null.
CodexErrorInfo is an open string/object union. Unknown variants are valid
protocol inputs but not newly retryable. Transport variants carry optional
nullable uint16 `httpStatusCode`; validate present values and do not infer a
status from text.

Retryability and settlement are distinct:

- Allow terminal `serverOverloaded` and `internalServerError`. Allow typed
  `httpConnectionFailed`, `responseStreamConnectionFailed` and
  `responseStreamDisconnected` with status 408, 500, 502, 503 or 504, or an
  absent/null status where the typed connection/disconnection variant itself
  establishes transport failure. Allow `responseTooManyFailedAttempts` only
  with one of those explicit transient status codes. A temporary pre-turn
  dial/connect failure can qualify when no turn was issued and applicable
  thread cleanup is proved. Other/unknown failures, permanent authorization,
  configuration, quota/rate-limit, validation, isolation and policy errors do
  not qualify. Never inspect arbitrary error message text for retryability.
- An owned, valid `willRetry: true` notification is native progress. It does
  not end the call, cancel inference, reset its deadline or start another call,
  regardless of whether its category would allow a fresh terminal retry.
- `willRetry: false` records failure. For a potentially retryable terminal
  failure, continue observing within the same deadline until the exact owned
  `turn/completed` proves failed/interrupted termination. A later successful
  completion cannot turn that failed attempt into success. A fresh retry is
  possible only after successful applicable cleanup. The error notification,
  interrupt acknowledgement, unsubscribe or connection close alone does not
  prove that a turn stopped. If no turn/start was issued, prove that fact and
  complete any known thread cleanup instead. Uncertain thread/start ownership
  or an unacknowledged/lost turn/start reply remains nonretryable.
- Validate connection generation, thread and turn identity. Buffer early
  notifications within existing event/byte limits until the start response
  binds identity; do not adopt an error's IDs as success or new-start authority.
  Mismatched identity or malformed fields fail closed. Preserve existing scoped
  cleanup evidence rules and never interrupt foreign execution. Cleanup failure
  or deadline/cancellation makes the accessor false.

Retry has one owner and one **30-second total wall-clock naming deadline**,
created before queue admission. Queue wait, all native retries, any automatic
fresh attempt, backoff and every cleanup share that deadline. Never give each
attempt a new thirty-second timeout. Retain the limit of two concurrent naming
operations per workspace, holding each slot across that operation's retries.

- Let the native retry sequence run on the same owned turn when it reports
  retryable progress. The incident reports a five-retry native maximum. A retry
  notification must not trigger an additional application attempt.
- Permit at most **one automatic fresh utility attempt** after a clearly
  retryable terminal failure (two utility calls total). Use a **200 ms**
  cancellation-aware backoff within the remaining budget. Start it only after
  the previous attempt's ownership and cleanup are settled, and only if time
  remains after backoff for at least **1 second of inference plus 250 ms of
  cleanup**. Check remaining time and cancellation again after backoff. Each helper still
  receives the original absolute deadline. A native sequence that consumes the
  budget goes directly to manual recovery.
- Retryability must come from validated protocol/transport classification,
  with affirmative evidence that no previous turn remains running. Do not infer
  it from arbitrary provider message text or the generic server-error category.
  A lost turn/start reply, unresolved ownership or unconfirmed cleanup blocks
  a fresh start. Do not change provider or restart the naming runtime.
- Do not automatically retry invalid naming output, malformed notifications,
  isolation/settings errors, permanent authorization/configuration errors or
  explicit cancellation. Unknown failures stop safely. Persistent transient
  failures stop when the attempt cap or shared deadline is reached.

After that bounded automatic recovery, retain the saved request without a base
or slug and expose the existing manual choice and explicit **Retry naming**.
An explicit user retry may begin a new preparation attempt under the existing
receipt/attempt contract. No automatic loop repeats whole preparation attempts.
A larger total budget requires a separately recorded design decision.

`namePreparation` owns the single deadline and semaphore slot. Put the bounded
production retry loop inside `normalSessionName`, after it resolves the accepted
explicit provider or current inherited default **once**. Freeze that resolved
provider across both calls; a workspace-default change between attempts must
not reroute this request. Both calls retain identical bounded input,
instructions, output schema and model/effort. Each owns fresh private scratch
state through normal `modelSessionName` cleanup. Test the loop through a small
private helper accepting an injected call and retry predicate; production must
pass `codex.CanRetryEphemeralTurn` directly. This seam is approved for B's
focused tests; A's tests establish real positive metadata and the native
integration test establishes the cross-package path. Keep production adapter
negative tests too. Do not expose constructors merely for B's tests.

Attachment-only requests have no textual subject. In the automatic-name path,
offer manual selection before reservation rather than inventing a fallback;
custom-name attachment requests continue normally. The existing `session`
special case in `session_name.go:85–86` and `canSetPreparationName` must be
covered explicitly so this requirement is not silently bypassed.

All name choice and retries retain the original request ID, receipt ownership,
accepted goal, date, provider, settings and attachments. Failed naming leaves
base/slug/handoff empty and creates no session tracking, branch, worktree or
root conversation. Preserve custom-name syntax/48-character limit, automatic
collision suffixes, custom collision recovery and exact choice replay. After
successful reservation a slug remains immutable across retries.

## Implementation boundaries and dependencies

| Package / owner | Owned files and result | Dependency and acceptance |
| --- | --- | --- |
| A / implementer0 | codex-web `codex/ephemeral.go`, focused/unit/native integration tests, `docs/reference.md` | Implement the pinned error schema and CanRetryEphemeralTurn; retry progress reaches completion; terminal retry metadata requires settlement and cleanup. |
| B / implementer1 | dev-workspace naming files, preparation/manual-selection tests, relevant creation browser tests, preparation/portal docs | Fallback removal/manual recovery proceed independently; 30-second orchestration uses A's accessor. Freeze resolved provider across both calls. Exhaustion stops before reservation with original inputs intact. |
| C / assigned implementer after A+B | dev-workspace codex-web pin (`portal/go.mod`, `go.sum`, `flake.lock` as required), package/native creation fixture | Consume exact corrected client; test real naming path with recoverable and persistent provider failure. Serialize Git operations and overlapping integration edits. |

Implementation is authorized and A/B may proceed once this saved brief is
announced. The lead assigns dependent integration and configuration packages and
serializes overlapping edits/Git operations. The architect owns consequential
design revisions. This brief does not assign a reviewer or authorize merging
any repository into its default branch.

## Compatibility, deployment and recovery

No intended manifest, preparation, receipt, roster, journal, database, public
CLI or provider format change is necessary. Reuse `model`, `utility_error`,
`timeout`, `invalid_output` and `custom` outcomes. Current manual selection is
already identity-bound and persists through retries. The Go utility signature
and supported model remain unchanged; error notification handling changes and
safe retry/cleanup information is additive error metadata. Existing callers
retain their error-category checks; the revised runtime alone opts into the
bounded fresh attempt.

Existing selected bases and reserved slugs are historical identities. Do not
rename `2026-10-21-development-session` or move its tracking/worktrees/branches,
URLs, Codex roots or receipts. The fix applies before allocation to new
requests, or to already failed requests with no chosen base. Older readers can
read the same fields; older writers still have the faulty fallback policy.

Deployment targets **aitherdev**, system contract first and application user
profile second, without reboot. After A/B and dependent pin integration pass
review and verification, select the exact published runtime revision through
configuration's existing `dev-workspace` channel / `devWorkspace` role using
`confctl inputs channel set --commit dev-workspace devWorkspace REV`. Preserve
generated channel history and verify only intended/transitive lock changes.

The workspace composition must select the same revision at
`inputs.vpsfree-dev-workspace.inputs.dev-workspace.url`, retaining the extension
revision/content hash, sibling inputs and follows paths. Regenerate its lock
with `nix flake update vpsfree-dev-workspace/dev-workspace`; do not rewrite the
extension's lock or add a competing top-level runtime. Run
`bin/check-dev-workspace-deployment --workspace-root PATH --configuration-root PATH`
on the final locks. This is a host contract pin plus separate user-profile
application deployment, not application installation through NixOS.

The lead owns the exact rollout record and selected-package coordination guide.
Use the same aitherdev machine claim through confctl dry-activate/switch and
the ordinary `workspace-host` profile switch with exact session identity and
claim. Preserve current native/model/catalog compatibility and other deployed
runtime features; no unrelated upgrade is authorized. Follow the selected
runtime's retention/release contract (including integration of the deployed
lineage) instead of assuming release after a successful switch. Implementation
and deployment approval do not authorize configuration or application master
integration. This architect task performs no deployment or claim mutation.

No PHP service, API client, database or fleet-wide rollout is implicated.
Refresh browser assets together if changed. Package switches are forward-only;
recovery retains the current compatible runtime or deploys a newer corrected
package. Pending requests must remain recoverable. A source revert in a newer
package must preserve the no-generic-fallback requirement and current readers.
The approved implementation plan includes deployment, with the required claims
and verification; no deployment has yet been performed by this design task.

## Acceptance and verification plan

Quick checks in each repository's Nix environment, after implementation:

Existing defaults to change: `session_name.go:89` is `10*time.Second`;
`session_namer.go:75` and the preparation guide describe ten seconds.
`TestSessionNameAdapterFailureAndWorkspaceConcurrency` bounds the adapter
deadline to ten seconds, and `TestSessionNameTimeoutIncludesSemaphoreQueue`
expects generic success within 9–12 seconds. Replace those with the 30-second
contract and failed/unreserved outcome. Replace the production-fallback
expectations in `TestSessionPreparationProductionNamingFailureStillCreatesWithOriginalRequest`,
`TestSessionNamingUtilityUnavailableOwnedSocketUsesNeutralName` and
`TestSessionNamingUnavailableRuntimeNeverUsesConversationSocket`. Preserve
existing manual-choice/replay/upload coverage and legacy `attachment_only`
record readability. Use an injectable private timing seam for short deadline
tests, while separately asserting the production 30-second default.

Planned commands (from the owning repository's Nix shell; not yet run):

```sh
# codex-web
go test -mod=readonly ./codex -run '^TestEphemeral' -count=1
python3 test/codex_protocol_contract.py --coverage-only codex/client.go

# dev-workspace; use an absent fixture DEV_WORKSPACES_CODEX_PROVIDERS path
# on this configured host, as required by its README.
go -C portal test -mod=readonly ./internal/web -run '^(TestSessionNam|TestSessionPreparation)' -count=1
```

The focused web selection must include the shipped-browser HTTP test and manual
name-selection browser contracts; an injected retry predicate alone cannot
prove production wiring. Implementers own required repository hooks and any
focused selectors adapted to their current source baseline.

- Unit/protocol sequence: owned `error(willRetry=true)` followed by one valid
  final answer and successful completion returns the name, without an early
  interrupt. Repeat retry notifications do not reset the deadline.
- A classified transient terminal failure with confirmed cleanup triggers one
  automatic fresh call, whose success continues without user action. Assert
  identical accepted input/provider/settings, no overlapping turns and no
  extra preparation attempt or identity allocation between calls.
- Queue delay, native retries, backoff, fresh call and cleanup fit within the
  same thirty-second deadline. Test both attempt-cap exhaustion and deadline
  exhaustion, including too little time to start the second call. Neither
  nested retry sequences nor zero-delay failures create an unbounded loop.
- Validation/permanent failures receive no fresh automatic call. A lost
  turn/start reply or uncertain cleanup also prevents it, even if the error
  otherwise looks transient. Cancellation during backoff starts no new turn.
- Change the workspace default between calls and prove that the resolved
  provider, model, effort, instructions and input remain identical. Verify the
  200 ms backoff and the 1 second plus 250 ms post-backoff admission threshold.
- Terminal error, eventual retry exhaustion, cancellation, malformed retry
  flag, wrong thread/turn and lost turn/start reply cannot become success or
  interrupt a foreign turn. Test the permitted early-notification ordering.
- Real production adapter wiring: missing runtime, server failure, invalid
  JSON/schema and queue/deadline exhaustion all leave base/slug/handoff empty.
  A fake injected namer alone is insufficient: the regression specifically
  wrapped errors in the production adapter.
- Failure renders Retry naming and the custom-name form. Selecting
  `php-upload-progress-mitigation` continues once with the exact original PHP
  request and settings. Lost responses, reload, stale attempt, concurrent
  choice and custom collision preserve existing replay/ownership contracts.
- Success with the supplied PHP request creates a subject-relevant name
  without user confirmation. Assert meaningful subject/action and syntax, not
  one brittle exact stochastic phrase. Include conversational openings,
  technical identifiers, a later main subject and UTF-8 truncation cases.
- Attachment-only automatic requests offer manual choice; explicit custom
  names and already reserved historical slugs retain their normal behavior.

After committed changes, quick checks and mandatory independent final review,
run longer checks with the required verification watcher: codex-web's pinned
native ephemeral integration, then dev-workspace's packaged session-creation
VM/browser path. Inject an actual retryable provider error followed by success,
a safely settled transient terminal failure followed by automatic fresh-call
success, and a persistent failure that exposes manual choice before session
creation within the shared budget.
Require a controlled live check with the selected provider before declaring
automatic naming repaired; synthetic success alone does not establish actual
provider availability. Use dedicated test sessions only under the later
verification authorization, never the user's example session.

For deterministic native failure fixtures, use HTTP 200 SSE `response.failed`
with `response.error.code = "server_is_overloaded"`; pinned
`codex-api/src/sse/responses_error.rs` explicitly maps this to
`ApiError::ServerOverloaded`. **Correction after provisional B268 CI:** overload
without server retry advice is terminal in the pinned native implementation,
regardless of a positive `stream_max_retries` ceiling. The native-progress
scenario must include the nested JSON string header
`response.error.headers = {"retry-after": "1"}` on each injected overload.
This means one second of native delay per response; fractional seconds are not
supported. An HTTP response header alone is not the streamed error field read
by this path. The complete SSE event data is:

```json
{"type":"response.failed","response":{"id":"fixture-overload","status":"failed","error":{"code":"server_is_overloaded","message":"fixture overload","headers":{"retry-after":"1"}}}}
```

Send two advised overloads before success: the native release build can hide
its first WebSocket retry notice. A's built-in OpenAI fixture must retain the
native provider unchanged, including the default stream retry ceiling of five.
Do not inject `model_providers.openai.*` at thread or daemon startup: the pinned
native configuration forbids overriding that reserved provider. B's explicitly
custom fixture providers may retain their test-only `stream_max_retries = 2`
native-progress and `= 0` terminal settings. Keep retry advice **absent** in
terminal/fresh-utility and persistent-failure scenarios. Advice-free overload
is terminal even under A's default retry ceiling; allow success on the fresh
utility call only after the first turn's exact failed completion and cleanup.
Assert observed owned retry/completion events, not guessed total POST counts
across transport fallback. HTTP-level retries may be disabled in the fixture;
an HTTP 200 SSE error avoids that additional retry layer. This explicit overload
also avoids the separate unbounded ConnectionFailed recovery branch that can
complicate EOF/dial-failure fixtures. Keep production provider configuration,
model/catalog and isolation policy unchanged. These recipes are source-backed
test plans, not executed verification; A/B own their fixtures and the review
packet must identify any custom-provider test-only overrides.

The pinned source root is
`/nix/store/9is267xl3palxb615kk86qlli9nggkf9-source/codex-rs`.
`codex-api/src/sse/responses_error.rs:26–31` reads the nested headers and
`:87–89` retains retry advice for overload;
`codex-api/src/sse/responses_error_tests.rs:118–139` proves this exact JSON
header representation produces a native retry delay (using seven seconds in
the upstream test). `http-client/src/retry_after.rs:24–38` accepts integer
seconds, so the disposable fixtures use `"1"`.
`protocol/src/error.rs:438–440` requires server advice for overload;
`core/src/responses_retry.rs:88–90` returns the error when no delay exists,
before considering the retry ceiling. This corrects the earlier fixture
recommendation; it does not change the approved production retry policy.

Failure evidence: `package-b-provisional-ci-failed.log:4551` begins the native
positive case and `:4566` records stopped/manual naming instead of success;
`:4563` records `duration_ms=512 outcome=utility_error category=server`.
B owner confirmed its failed `test/creation_model.py:87–90` overload payload
had no nested retry headers, and A owner confirmed the same omission in
`codex/ephemeral_integration_test.go:1862–1868` at `ee119a01`.
Thus both native-progress fixtures need this correction. Two terminal overloads
consuming both allowed utility calls is the source-backed explanation consistent
with the short failure; exact POST counts and native RPC frames were not retained
in the CI artifacts, so that execution sequence remains inferred. There is no
demonstrated production parser/identity defect from this failure. The corrected
native-progress cases must prove owned `willRetry=true`, success within the same
turn, no premature interrupt, and no fresh utility call; the advice-free cases
must still prove settled fresh-call recovery and ultimate manual choice.

The first A native run at `f722adab914fa34da9d7c66bca63f9515e1ebf6f`
found a second fixture error. `verification-native.log:16` and `:19` record
`thread/start` rejection with JSON-RPC `-32600`, no owned thread/turn and zero
provider POSTs/upgrades in both new cases. Thus neither overload payload nor
retry/settlement handling was reached. Those cases alone added
`model_providers.openai.request_max_retries` and `stream_max_retries` in
`codex/ephemeral_integration_test.go:2690–2702`.
Pinned `config/src/config_toml.rs:67–73,929–957` explicitly rejects reserved
built-in provider overrides before provider-name validation.
`app-server/src/request_processors/thread_processor.rs:1355–1358` and
`request_processors/config_errors.rs:32` map that configuration failure to
invalid request. The exact diagnostic text was reduced to `other-native-error`
in the saved trace; the reserved-provider explanation is source-derived, while
the pre-inference failure is directly observed.
The minimal A fixture correction is to remove that override block entirely,
preserving built-in capabilities and the existing request payload. Adding a name
or moving the same override to startup would not fix the reserved-ID violation.
`model-provider-info/src/lib.rs:67` sets the default stream ceiling to five,
enough for two advised overloads; HTTP 200 SSE avoids the HTTP retry layer.
No production retry policy, allowlist or API change is warranted by this failure.
The corrected native run remains required through the lead's review/watcher gate.

Long commands after review, through the required fresh verification watcher:

```sh
# codex-web, with documented pinned binary/hash/source, namespace tools and
# Luna model/catalog fixture environment from docs/reference.md
go test -mod=readonly -tags=codex_integration ./codex -run '^TestEphemeralNamespaceOwnershipIntegration$' -count=1 -timeout=180s
go test -mod=readonly -tags=codex_integration ./codex -run '^TestEphemeralProtocolIntegration$' -count=1 -timeout=180s

# dev-workspace
nix build --no-link --print-build-logs .#checks.x86_64-linux.session-creation
```

Run applicable package/flake checks as well. Naming changes also require the
workspace verification procedure's creation-during-collection, preparation and
package-switch exclusion, and failed-backend coverage in disposable fixtures.
The existing component inventory does not establish the combined collector and
portal case. [collection-probe-plan.md](collection-probe-plan.md) specifies a
session-only post-review composition of the actual collector/host guards and
real HTTP admission/handoff, with inert activation boundaries. It is prepared,
not executed, and explicitly does not prove a usable native conversation during
the same sweep; a requirement for that stronger result needs the bounded existing
creation-VM scenario described there, through the lead.
After deployment verify portal health, actual-provider naming and conversation
continuity. Synthetic fixture success alone is not deployed readiness evidence.

No checks in this section have been executed by this design task. Investigation used read-only
installed source, local Git objects, exact preparation metadata, the portal
journal and bounded native SQLite log queries. Only this design is written.
