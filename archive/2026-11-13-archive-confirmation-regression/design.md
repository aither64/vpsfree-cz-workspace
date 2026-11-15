# Archive confirmation and provider-switch investigation

Current outcome: Archive behavior is accepted and no Archive fix is pursued.
Package D identifies two provider-helper configuration omissions. The user has
now authorized implementation, aitherdev deployment through the configuration
repository, and integration after verification. G implementation belongs to
implementer0; H pin preparation belongs to implementer1 under the brief below.
Earlier checkpoints are retained as investigation history.

Package A, architect0, 2026-11-15. Findings and design only; no implementation,
commit, deployment or session lifecycle action was performed. The lead owns
plan/state and acceptance. This document is the exclusive architect-owned file.

## Conclusion and confidence

Fresh Archive still opens its confirmation dialog. The existing click handler
deliberately bypasses that dialog when it recognizes a pending archive or a
failed/paused archive receipt belonging to the current target. It immediately
sends the retry request instead. A failed pre-journal receipt can take this path
while the button still says **Archive session**. This is a concrete explanation
for an Archive click proceeding without a prompt, conditional on that state.

The bypass predates the November 11 archival-failures work. The relevant public
commit from that branch changes contention handling and progress presentation,
not the confirmation dispatch. There is no evidence that it removed confirmation.

Confidence is high in the code path and history conclusion. The particular user
incident remains unverified: no clicked-session receipt, browser state or request
trace was inspected. A failed operation-status read could also prevent the fresh
dialog from appearing, but that path reports an error and does not dispatch
archive. Installed-source equivalence is established below; the actual browser's
loaded asset and state at the incident are unknown.

## Scope and source evidence

Identity was verified before session-owned access: `dev-session current` and
`DEV_SESSION_SLUG` both returned `2026-11-13-archive-confirmation-regression`;
`DEV_SESSION_WORKSPACE` was `/home/aither/workspace/ai/vpsfree.cz`, matching the
thread binding. The live roster confirmed architect0 as design-purpose,
workspace_write. Investigation used canonical repository history and immutable
installed package sources, without accessing another session's records,
worktree, transcript or team.

Repository: `git@github.com:aither64/dev-workspace.git`, canonical bare clone
`repos/dev-workspace.git`. The inspected local `origin/master` was
`22351ed4207c47bf5ff3d975e7ab3d1f9fb73c92`; no fetch was performed. All current
source line numbers below refer to that exact commit.

| Evidence | Exact path and lines | Finding |
| --- | --- | --- |
| Fresh action and bypass | `portal/internal/web/static/app.js:4306–4370` | Lines 4340–4344 route pending archive or matching failed/paused receipt directly to `retryArchive`; otherwise open confirmation. Lines 4318–4323 fetch retry status and send receipt/journal to `client.retryOperation`. Fresh form submission at 4360–4361 calls `client.archive` after checking the confirmation target. |
| Dialog opening | `portal/internal/web/static/app.js:3567–3623` | `openLifecycleConfirmation` reads operation status, captures the current target and calls `showModal` at 3603. `confirmationForLifecycle` rejects a changed target. |
| Retry identity | `portal/internal/web/static/app.js:992–996,3462–3478` | A matching target plus receipt qualifies even without `journalExpected`; accepted journal recovery is another match path. Retry refreshes operation status and rejects changed/unrelated targets. |
| Labels | `portal/internal/web/templates/session.html:40`; `portal/internal/web/static/app.js:1554–1568,3510–3541,4310–4315` | Initial sidebar label uses pending lifecycle only. Status rendering does not synchronize that label for failed pre-journal receipts. `Retry archive` is set only by the retry reset callback; title/aria-label start as `Archive session`. |
| Existing dialog | `portal/internal/web/templates/session.html:315–320` | Contains destructive-effects explanation and Cancel/Archive controls. Reuse it. |
| Other retry entry | `portal/internal/web/static/app.js:4431–4435` | Status-panel Retry archive also directly retries unless options or changed-target confirmation are required. |
| HTTP payloads | `portal/internal/web/static/app.js:51–68` | New archive POST uses mode, targetId and optional receiptId; retry POST uses receiptId and journalId. |
| Server admission | `portal/internal/web/server.go:2968–3021,3482–3594` | New requests reject an unfinished journal and validate target/mode. Retry requires matching receipt/journal and failed/paused state, preserves original options, and checks pending journal identity. Both dispatch the authorized CLI path. |
| CLI confirmation | `libexec/dev-session:10676–10721,10763–10770` | Ordinary CLI asks yes/no. Portal-authorized invocation validates portal authorization instead of prompting again. No missing second CLI prompt needs repair. |
| Recovery contract | `docs/session-archive-recovery.md:374–383` | Exact worker/operation authorization is retained; failed/paused receipts require recovery. Completed historical evidence does not prevent fresh confirmation once no journal is pending. |
| Documented manual behavior | `docs/dev-sessions.md:1032–1048` | CLI confirmation, manual archival effects and retained committed content. Workspace lifecycle guidance explicitly says CLI and portal each ask once. |

History inspected:

- `0882cacc6ee1e0adfa8b203c0e805cf3ec5e4e07` (2026-09-09),
  `portal: make session status responsive and recoverable`, introduced direct
  retry for pending archive.
- `5d2f8993f3ce9e5d88b03639b5766bab4d5a5831` (2026-10-05),
  `portal: preserve lifecycle targets and recover confirmations in place`,
  expanded the handler to matching failed/paused receipts and retained fresh
  confirmation for changed targets. This is the relevant earlier behavior change.
- `e1c67dbee3188df9dc7c37fa1d1e724515530fea` (authored 2026-11-11),
  `session: wait through archive preparation contention`, changes
  `lifecyclePresentation` around `app.js:902–935`; its server diff updates displayed
  preparation errors. It does not change the click handler, dialog or HTTP
  confirmation contract. Keeping an already accepted preparation waiting is not
  removal of an initial user confirmation.
- The locally available published branch
  `origin/2026-11-11-session-archival-failures` points to
  `734a85fea42c8f8276e6b037196c24cf8903cd12`. In its recent range after
  `f124fd4e4fa34b20aef5063247a3ae8cb57a6d48`, the only change to the Archive
  JavaScript/template is `e1c67dbe` above. This is ordinary repository history,
  not evidence read from that session's private records.

The stable `dev-session` command resolves to selected package
`/nix/store/q85i6cmv3qkmif3k23nn3qvzsh779f7b-dev-workspace-0.2.0`.
Its derivation is
`/nix/store/53025bpwn15dnfvm3mgh50zy3ykszqvv-dev-workspace-0.2.0.drv`, whose
`src` is `/nix/store/q0dlf4srzzd1vm4bv35197cji10d3x4x-source`.
Git blob hashes of the four relevant installed source files match current
`origin/master` exactly:

| File | Matching Git blob |
| --- | --- |
| `portal/internal/web/static/app.js` | `bb570e56a8bc216123f88e4bb9fcff7d75790c9d` |
| `portal/internal/web/templates/session.html` | `63f0f429bae9565c5fcf3b7d81855e3d488f3027` |
| `portal/internal/web/server.go` | `6eb7cb4a49bd6cac01dd2ff4b86afc2a08558714` |
| `libexec/dev-session` | `d512ec1fdf05e3b6e729ed11d47f9dc5fadd8c40` |

This proves selected package source equivalence, not the historical incident's
deployed version or browser cache. No live session was clicked or mutated.

## Smallest proposed behavior

Use the existing archive dialog for every user-triggered Archive or Retry archive
click, including both sidebar and status-panel controls. Cancel or Escape sends
no mutation. Submit dispatches exactly once using the appropriate existing path:

1. A fresh archive retains the current target confirmation and archive POST.
2. A failed pre-journal receipt remains an explicit retry of that receipt after
   dialog confirmation; it does not become a new operation merely to show a prompt.
3. A pending/failed/paused journal resumes the original operation through the
   retry endpoint after dialog confirmation, preserving mode, receipt and journal.

The dialog needs only small in-memory intent state distinguishing fresh archive
from retry. Bind retry confirmation to its receipt/journal and revalidate them
before dispatch; if they changed while the dialog was open, do not silently retry
the replacement operation. Keep existing changed-target reconfirmation and
completed-archive reconciliation. Cancel clears this dialog intent only; it does
not cancel an already accepted background operation.

Do not route accepted journal retries through the fresh archive form path:
`startArchive` rejects pending journals, and `openLifecycleConfirmation` rejects
fresh archive of an already archived target. An unfinished journal can legitimately
need recovery after tracking has moved into `archive/`. Its dialog should describe
resuming that operation, then use the existing receipt/journal checks. Reuse the
dialog presentation without removing the fresh-action guard for archived targets.

Keep visible labels, title and aria-label aligned with the chosen action:
**Archive session** for a new action, **Retry archive** for an existing retry.
Show retry intent in the confirmation button as well. Reuse established dialog
styles and destructive-effects explanation; no new confirmation framework.

The added prompt governs a new human click. It does not revoke accepted
authorization or require background recovery, worker restart, automatic archival
or the portal-authorized CLI to ask again. This is a small intentional change to
retry interaction, while preserving recovery semantics. There is no demonstrated
need for a server token, schema migration or backend hardening.

## Invariants, compatibility and recovery

- No user-triggered archive mutation before dialog submission; no mutation on
  cancel, Escape, status-read failure or a stale confirmation.
- Accepted operations retain exact receipt/journal, target checks, saved policy,
  original recovery path and existing duplicate-attempt protection.
- No API, CLI, on-disk, journal, database, native protocol, cluster or Nix option
  change. Old/new browser-server combinations retain the existing request shapes.
- Update the existing `app.js` URL version consistently in its three templates
  so a newly loaded page selects the fix. Already open tabs need a reload; this
  limitation must be stated during any later deployment.
- No coordinated node update is needed. A later authorized user-profile package
  deployment follows normal review/build/deployment guidance. Do not deploy now.
- Recovery uses the original supported retry command/receipt. Never edit journals
  or clear receipts as a workaround. Installed packages are forward-only; recover
  a faulty UI release with a corrected package under the normal package workflow.
  The proposed change creates no new state that older readers must interpret.

## One possible future implementation package

**B — Confirm Archive clicks, owner: implementer0 if subsequently assigned by
the lead. Status: technically settled; not released or authorized to implement.**

Dependencies: user direction to implement; lead acceptance/allocation and capacity
check; an owned dev-workspace feature worktree with fresh repository instructions.
No other application package is required. Architect0 retains design ownership;
lead retains scope, user-facing wording, plan/state and review/integration authority.

Exclusive application file boundary:

- `portal/internal/web/static/app.js` for intent, event routing and accurate labels.
- `portal/internal/web/templates/session.html` for minimal dialog selectors/copy
  if needed; `templates/{session,index,automatic-archival}.html` for the shared
  asset version.
- Existing `archive_failure_browser_test.cjs` and
  `presentation_browser_test.cjs`, plus their existing Go harness only if needed;
  `browser_contract_test.cjs` for focused intent/request assertions if useful.
- `docs/dev-sessions.md` for one short clarification of confirmation on explicit
  Archive/Retry clicks. Preserve the recovery guide's authorization contract.

No server/CLI/journal edits are planned. Any demonstrated need to cross that
boundary returns to the lead before implementation.

Acceptance and evidence:

- Fresh action, matching failed pre-journal receipt, paused journal and failed
  journal each show a dialog from both applicable controls before any POST.
- Cancel/Escape produce zero lifecycle POSTs. Confirm produces one request with
  the existing fresh target or exact retry receipt/journal, without duplicate CLI
  confirmation. Repeated clicks cannot dispatch duplicate submissions.
- Retry still works after tracking has moved; stale receipt/journal/target or
  completed archive cannot cause a new unintended archive.
- Labels identify Archive versus Retry consistently. Existing changed-target
  confirmation and retry race/cancellation checks still pass.
- Deliver exact base/head, changed files, check results/gaps and an explicit
  no-migrations conclusion for the lead's final review packet.

Quick checks, in the repository Nix environment: JavaScript syntax check; focused
shipped-client/asset/server tests; focused browser confirmation/cancel cases using
the existing harness and disposable fixtures. Relevant existing tests include
`TestShippedBrowserClientMatchesSessionAPI`,
`TestBrowserAssetVersionsForRetryAndQuestionUI`, `TestArchiveFailurePage`,
`archive_failure_browser_test.cjs:208–290` (retry races) and
`presentation_browser_test.cjs:401–428` (changed-target reconfirmation). Existing
CLI confirmation coverage is `test/dev_session/lifecycle_commands_test.rb:1046–1091`.
Update tests expecting immediate retry to submit the confirmation first while
preserving their original race/identity assertions.

Longer checks, only after committed-deliverable independent review: the affected
browser suite in Chromium and Firefox and repository-required package checks.
The repository also requires `session-archive-lifecycle` before deployment; use
its disposable sessions and established monitoring workflow. Any live acceptance
archive/revive needs separate explicit authorization for the exact disposable
session. No real-session lifecycle operation is part of this investigation.

No tests or builds were run for this findings-only package. Source/history reads,
selected-source blob comparisons and document inspection are its evidence.
No feature branch exists and no merge readiness is claimed.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-archive-confirmation-regression/

## Package C — provider preparation failure investigation

2026-11-15, architect0. Package A was accepted. The user accepts the existing
Archive behavior; package B above remains a historical proposal and is not being
pursued. The current assignment is findings only for a provider switch reported
against the affected session, targeting the selected load-balancer provider:
Waiting for session access, 0 of 1, 1 second, preparation failed before any thread
was closed, `native locking-sessions failed`.

The current session identity and both environment markers were reverified before
this work. No affected-session files, roster, transcripts, worktrees or native
socket were accessed; no provider operation was retried. The only new edit is
this section. Applicable procedures and repository guidance were retained from
package A; `docs/codex-providers.md` and codex-web's AGENTS.md were also read.

### Finding and limits

There is no native command called `locking-sessions`. It is a progress stage,
translated to **Waiting for session access**. The stage remains in force after
locking while retry cancellation, retained-session inventory, native metadata and
settings checks run. Unclassified failure anywhere in that interval becomes
`native_locking-sessions_failed`; the UI replaces underscores with spaces.
The displayed 0 of 1 initially counts session slugs, before the retained thread
inventory exists (`codex_provider_scoped.go:143`). It does not identify the exact
thread/check that failed.

The concrete defect established here is loss of useful failure classification,
not a proven cause of this provider switch failure. No deterministic argument or
selected dependency mismatch was found. The original helper error is captured
and then deliberately omitted from durable diagnostics. Existing records cannot
recover it. A generic failure after one second does not establish lock contention
or a problem with the target provider credentials.

### Exact call and error path

Current references use dev-workspace commit
`22351ed4207c47bf5ff3d975e7ab3d1f9fb73c92` unless stated otherwise.

| Source | Evidence |
| --- | --- |
| `libexec/workspace-provider-sessions.rb:331–340,417–429` | Ruby invokes the selected package's `bin/workspace-portal codex-provider scoped-prepare`, passing `--workspace`, `--state-root`, `--socket`, `--host-profile`, `--authority`, `--snapshot`, `--target`, `--operation`, `--roots` and `--sessions`. Success is bounded JSON on stdout. Target-provider model/auth preflight follows successful preparation. |
| `portal/cmd/workspace-portal/codex_provider.go:50–109` | Those flags and action are accepted by the Go CLI. It creates an App Server client and a three-minute context, then calls `scopedProviderCommand`; it does not invoke a Codex `locking-sessions` subprocess. |
| `portal/cmd/workspace-portal/codex_provider_scoped.go:120–190` | The deferred failure writer uses a typed `scopedProviderFailure` reason when available, otherwise `native_` + current stage + `_failed`. It sets `locking-sessions` at 143 and retains it through cancellation at 183 and inventory at 187. The next stage is `capturing-settings` at 195. |
| `portal/internal/session/authority.go:77–155`; `codex_provider_scoped.go:146–179` | Authority/lock open, ownership/mode and filesystem errors can fail immediately. EAGAIN/EWOULDBLOCK waits at 100 ms intervals with `session_runtime_busy`. Pending lifecycle and changed root/socket set their own reasons. |
| `portal/cmd/workspace-portal/codex_provider.go:334–495` | Inventory can fail reading retained state, loading the installed team catalog, proving thread ownership/materialization, reading settings, or collecting monitor/member evidence. All still appear under the locking stage. Native reads include `thread/read` and `thread/loaded/list`. |
| `portal/cmd/workspace-portal/main.go:185–192` | The helper writes the underlying error to stderr and exits 75 for a transport error, otherwise 1. |
| `libexec/workspace-host:3931–3941` | `capture!` captures both streams, chooses stderr (or stdout if stderr is empty), and puts it in a Ruby exception on nonzero exit. This error text is not automatically journaled. |
| `libexec/workspace-provider-sessions.rb:461–495` | Rescue emits a sanitized diagnostic, writes the generic preparation-failed message, and attempts terminal restoration. It does not rethrow or persist the helper text. |
| `libexec/workspace-codex-providers.rb:547–575` | Logger explicitly excludes exception messages, helper arguments/output, native transcripts and settings. Its stage allowlist omits `preparing`, and its frame allowlist omits `workspace-provider-sessions.rb`. The scoped caller initializes the timing origin in rescue at `workspace-provider-sessions.rb:480`, explaining `elapsedMs: 0` rather than attempt duration. |
| `portal/internal/web/static/codex-providers.js:78–98,101–116` | Maps stage to Waiting for session access and falls back to replacing underscores in an unknown reason. UI elapsed time is calculated separately from operation timestamps. |

Preparation has possible effects even though no thread has been closed: terminal
quiescing precedes the helper (`workspace-provider-sessions.rb:404–415`), and
`CancelSession` can cancel retry work/write retry evidence
(`portal/internal/turnretry/store.go:319–369`). Failed preparation attempts to
restore terminals. Routing changes and native archive occur later. This report
does not assert that the target experienced no effects or that restoration was
verified.

### Selected-package and history evidence

The selected package, derivation and immutable source path are the same as in
package A. The installed source and inspected current master have matching blobs:

| Source | Matching Git blob |
| --- | --- |
| `portal/cmd/workspace-portal/codex_provider.go` | `be473a94f8d1f284dda204bf5487df107328291e` |
| `portal/cmd/workspace-portal/codex_provider_scoped.go` | `d25e4d60b1626b9610c61cbb2f79d179b0cea075` |
| `libexec/workspace-provider-sessions.rb` | `a22410935323b18930323c38bf2fdfdf6a0b71c3` |
| `portal/go.mod` | `0afb4ceeb48fdada55a30108591c4e267e4f5a43` |

The current module and flake lock agree on codex-web
`91a17d00a737d59a91b5e7bb420aa89e7ec52d93`. At that commit,
`codex/client.go:3876–3895` reads native metadata via `thread/read`;
`4120–4142` requires the exact thread, current model and rollout path for settings.
Failures there are compatible with the reported stage. The November 14 change
at `91a17d00` only allows `project/read` for ObserverOnly clients; this provider
helper does not construct an ObserverOnly client. That change is not evidence
of this failure's cause. The running native daemon version and the incident's
exact package generation were not independently sampled.

Relevant dev-workspace history:

- `d99f468edcb2ff91137b3473c9b52c5669465751` (2026-10-18): scoped provider
  switching with stock Codex.
- `9621c7b94b734c7104eef6d52b50516956538c2a` (2026-10-18): cancel preparation
  before the native-close boundary.
- `aafaf4195d695c4641ce4f9342d56a1786f237c3` (2026-10-22): adds
  `RetryStore().CancelSession` before inventory, without advancing the stage.
- `0b87a178a2ecf17432bae9e8e6d0bee9327a6b9c` (2026-11-04): latest inspected
  change to `codex_provider.go`, involving monitor delivery. History alone does
  not distinguish this incident's failing inventory check.

### Retained diagnostics and ranked unresolved causes

A bounded generic application-journal read was performed, without session files:

```sh
journalctl --user --unit=workspace-codex-provider@vpsfree-cz.service \
  --since='2026-11-15 08:20:00 UTC' --grep='^PROVIDER_FAILURE ' \
  --lines=3 --no-pager --output=cat
```

It returned three sanitized failures, each with `DevWorkspaceHost::Error`,
`stage: unavailable`, `step: scoped-transition`, `elapsedMs: 0`, and a frame at
`workspace-host:3940`. This confirms the diagnostic limitation on the selected
installation. These records were not attributed to the reported target: its
operation UUID/timestamp was not provided. They contain no retained Go error,
exit code or failing native method. The same bounded command, narrowed to the
incident time and exact operation UUID, can confirm correlation but cannot
recover text this code discarded. No raw provider catalog/token content was read.

Diagnostic priorities, not proven incident causes:

1. **Early inventory/metadata/settings or retained-state proof failure.** Several
   immediate-return sites retain the misleading locking stage. Exact helper error
   or a classified substep is missing; no target state was inspected.
2. **Runtime authority/lock filesystem error other than contention.** Directory
   absence/mode/ownership or file/open errors produce the same generic reason.
   Exact error category/errno is missing. Ordinary busy locks instead report
   `session_runtime_busy` and wait, making a one-second generic failure a poor
   match for ordinary contention.
3. **Other early preparation error**, including retry-evidence cancellation or
   progress persistence. These require the same exact substep/error evidence.

Unfinished lifecycle, changed session identity and target model/authentication
failure have different explicit paths/reasons. Target preflight follows successful
prepare; the supplied evidence does not support blaming Snajpa authentication.
Confidence is high in this control-flow conclusion and logging defect, limited
in ranking the incident's actual cause.

### Minimal remedy and bounded follow-up

Do not retry the live switch merely to reproduce the generic message. The smallest
useful proposed code change is to apply the existing `scopedProviderFailure`
classification to early preparation failures, and set a distinct substage before
retry cancellation and inventory/settings reads. Reuse existing reasons such as
`native_metadata_unavailable` and `thread_identity_unproved` where accurate;
classify lock filesystem errors separately from legitimate contention. Keep
private text and credentials out of public progress and logs. Preserve every
ownership/refusal and provider-transition boundary.

Correct the existing Ruby diagnostic projection to recognize scoped stages and
the scoped source file; measure from before the attempt, not from rescue. This
needs no new diagnostics service, state schema or provider-switch mechanism.
It is a proposed diagnostic correction, not a demonstrated provider-switch fix.

If implementation is subsequently requested, use one lead-assigned implementer
for these existing files and focused tests. Verify preparation-only fixtures with
injected lock-open, metadata, settings and inventory failures. Assert exact safe
reason/substage, preserved failure identity, unchanged routing, and zero
`thread/archive`, `thread/unarchive`, `thread/resume` or `turn/start` requests for
the early-failure fixtures. Check that synthetic credential-like error text never
reaches status/logs. Preserve possible retry-cancellation effects in assertions.

Any native follow-up must use isolated fixture directories, private synthetic
histories/provider configuration and a separate socket. The existing
`TestNativeScopedProviderSwitch` (`provider_scoped_integration_test.go:29–41,
315–332`) provides a disposable selected-native harness but goes on to perform a
full switch; it must not be invoked as a supposedly read-only diagnostic. A
preparation-only variant should stop after `scoped-prepare`, retain synthetic
failure evidence, and never use the affected session or real provider credentials.
The lead should approve the concrete fixture command/effects and assign it before
execution. No reproduction, test, build, instrumentation or implementation was
performed in package C.

No persisted format/API change is needed for the proposed diagnostic work;
existing operation/recovery receipts remain authoritative. Actual repair depends
on the classified cause, and any later deployment follows ordinary reviewed,
compatible package procedures. Leave the failed live operation and session intact.

## Package D — active-thread root-cause investigation

2026-11-15, architect0; package E reproduction belongs to implementer0. The user
explicitly requires provider switching while session threads are working. Package
C's diagnostics finding is secondary and does not resolve this request.

### Settled active-session contract and discriminating test

- Preserve working threads during preparation; active execution is supported,
  not grounds to reject or wait for completion. Native close/reopen after accepted
  preparation restores interrupted work with the existing identities and receipts.
- `libexec/dev-session:1802–1818` recognizes an authorized scoped provider pause
  and calls terminal-only `quiesce_native_client!`; it bypasses ordinary
  `quiesce_and_require_idle!`. Preparation is intentionally allowed to see a
  working native thread. No terminal was detached in this investigation.
- `buildProviderInventoryScope`, `codex_provider.go:390–401`, applies its idle
  and active-goal gates only for `scope == nil`. The scoped switch passes a
  nonnil map. Its `add` closure instead checks metadata identity/source/path
  and reads current model/effort (`383–408`).
- Pinned codex-web `91a17d00` metadata/settings methods issue plain `thread/read`
  calls. `Request` has no active-turn gate (`client.go:1117–1140`);
  `ReadThreadSettings` requires nonempty `thread.model` and `thread.path`
  (`4108–4142`). The exact incomplete-model error is
  `thread/read returned incomplete current settings`.
- Selected native package is
  `/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0`.
  The lead independently verified that the shared active native service's
  executable resolves to that package's `libexec/codex/bin/codex`; this proves
  the current executable, not a historical incident version.
- Static schema generation with that exact executable, using
  `app-server generate-json-schema --experimental --out
  /tmp/archive-confirmation-regression-provider-source/schema`, completed in
  about 0.12 seconds. It did not start a server or access a session/socket.
  `v2/ThreadReadResponse.json#/definitions/Thread/properties/model` exists and
  allows null when unavailable; its description says loaded threads expose the
  current configured model. The field was not simply removed from the protocol.
  `ThreadReadParams` uses `includeTurns`, whereas these readers send
  `excludeTurns: true`; that spelling is valid on `ThreadResumeParams`. Whether
  the read ignores the unknown field must be tested before attributing failure.
- Settings capture later calls `thread/resume` with the current provider
  (`codex_provider_scoped.go:449–487`), before native close. A failure there has
  already advanced to `capturing-settings`, unlike the reported stage.

The selected helper constructs its wrapper without retry-store root/workspace
fields. The separate RetryStore wiring concern is parked by lead direction;
do not expand it into an implementation or claim it caused this incident.

Package E's isolated native 0.165.0 fixture passed both idle and working
preparation with the installed helper. The working turn remained active.
Metadata/model/effort/path and settings reads passed; the native reader accepted
the existing `excludeTurns` request shape. The fixture had no retained monitor
utility, so it did not exercise the failing provenance path below. See
[provider-reproduction.md](provider-reproduction.md). No duplicate fixture or
full-switch run was performed by architect0.

### Root cause: incomplete provider-helper client configuration

The provider helper bypasses the ordinary workspace client constructor to avoid
implicit resume, watches and provider routing during a reserved operation. That
special composition omits two inputs required by the validators it still calls:

1. Its raw SDK options omit `ThreadSourceKinds`. The SDK preserves the empty
   list, and its headless identity validator rejects every source outside that
   list, including the workspace's expected `vscode` source. The earlier monitor
   metadata check can therefore pass while bootstrap validation returns
   `headless Codex thread has the wrong identity`.
2. The scoped Ruby subprocess does not supply `codex_environment(entry)`.
   Its Go wrapper obtains `CodexHome` from `DEV_WORKSPACE_CODEX_HOME`; an ordinary
   provider worker does not have that session-specific environment. Once source
   validation succeeds, monitor archive-state proof can fail with
   `archive proof requires a retained thread, canonical directory and Codex home`.

These are configuration omissions at the provider-helper boundary. They do not
justify an idle requirement or weaker thread identity, history, bootstrap or
archive proofs. The history-mode and `includeTurns` hypotheses are not the
source explanation: `VerifyHeadlessBootstrap` first calls the headless identity
validator, then checks the exact synthetic marker in the native rollout; it
does not search full `thread/read` response turns for that marker.

All dev-workspace lines below refer to `22351ed4207c47bf5ff3d975e7ab3d1f9fb73c92`
and its installed source identified above. Codex-web lines refer to pinned
`91a17d00a737d59a91b5e7bb420aa89e7ec52d93`, installed at
`/nix/store/jlqqwc73iw5bllbdyziyrq90m99qfb5r-source`.

| Evidence | Exact source | Consequence |
| --- | --- | --- |
| Raw provider client | `portal/cmd/workspace-portal/codex_provider.go:89–100` | Omits source policy, preserves explicit no-implicit-resume behavior, reads home from environment. |
| Correct workspace source policy | `portal/internal/workspacecodex/client.go:23,57–77` | Sets `ThreadSourceKinds` to `vscode`; also installs behavior unsuitable for a blind constructor replacement. |
| SDK option semantics | `codex/client.go:945–959,5936–5938` | No default source list; `threadSource` requires membership in the configured list. |
| Failing identity condition | `codex/headless.go:27–38,106–124` | Headless materialization checks source policy before bootstrap rollout scanning. Preserve its CWD/origin/ephemeral/paginated-history checks. |
| Monitor gate order | `portal/internal/monitoroperation/lifecycle.go:51–89` | Project, metadata, bootstrap, then archive-state proof. |
| Provider inventory caller | `portal/cmd/workspace-portal/codex_provider.go:438–457` | Invokes monitor lifecycle proof before settings capture; failure still reports `locking-sessions`. |
| Missing scoped environment | `libexec/workspace-provider-sessions.rb:331–340` | Calls `capture!`, inheriting the worker environment. |
| Existing correct environment | `libexec/workspace-codex-providers.rb:272–282`; `libexec/workspace-host:3797–3810,3931–3943` | Existing provider helper uses `capture_env!(codex_environment(entry), ...)`; the environment derives canonical storage from registered workspace identity. |
| Home precondition | `portal/internal/workspacecodex/archive_proof.go:78–85` | Rejects an empty/noncanonical home before archive proof. |
| Launch-test gap | `test/workspace_host/provider_sessions_test.rb:25–30` | Existing scoped fixture replaces the entire subprocess helper, so it cannot detect the omitted launch environment. |

Narrow blame identifies the raw constructor in
`5421e563478418f54506c3bad6573e1ce6a3b82c` (2026-10-12,
`providers: preview limits and switch workspace Codex routing`) and the scoped
subprocess call in `d99f468edcb2ff91137b3473c9b52c5669465751` (2026-10-18,
`providers: switch retained session threads with stock Codex`). These dates
identify the omissions, not when a particular session first encountered them.

The selected package's installed team catalog also passed the read-only
`workspace-portal team-preset --package-root <selected-package> --team delegated`
check. The shared provider worker's whitelisted environment lacks
`DEV_WORKSPACE_CODEX_HOME`; its process began before the correlated failed
operation. No provider configuration or credentials were printed.

Package F supplied the exact-target causal comparison to the lead; the incident
evidence is retained in same-session reports, including architect report
`9575badb-792a-4aad-8a5b-e86e55f4793c`. Target-derived records, identities and
comparison output remain private under the workspace sensitive-data policy.
This document records the independently inspectable source defect
and fix contract. No real switch was retried, and no claim is made that every
later switch stage has been verified. Preparation may already have quiesced
terminal clients or canceled retries; “no thread closed” does not mean no effects.

### Smallest supported fix and one future implementation package

**Package G: provider-helper configuration parity — sufficient brief, unassigned.**
Owner: one lead-assigned implementation-purpose member (implementer0 is the
existing technical contact). Dependencies: accepted D/F evidence and a subsequent
implementation assignment. Application implementation is not requested by this
investigation; no code, commit or deployment is part of D.

- In `portal/cmd/workspace-portal/codex_provider.go`, explicitly supply the same
  `vscode` source list as the ordinary workspace constructor. Keep the raw
  construction, disabled implicit resume, submission paths and no-watch/no-routing
  composition. A direct switch to `workspacecodex.NewWithOptions` also installs
  lifecycle routing and changes implicit-resume policy, so it is not equivalent.
- In `libexec/workspace-provider-sessions.rb`, launch the scoped helper with the
  existing `codex_environment(entry)` using the established environment-aware
  subprocess mechanism. Derive the home from the registered workspace, never from
  browser input, another session or the invoking shell's incidental Codex home.
- Add focused regression coverage in the existing provider Go tests and
  `test/workspace_host/provider_sessions_test.rb`. Exercise the production client
  composition and the actual Ruby helper boundary; do not merely assert duplicated
  test option values or keep the whole-helper override as the only coverage.

Acceptance: a disposable retained monitor with valid source, project, CWD,
non-ephemeral paginated history and exact bootstrap marker passes inventory with
the production helper setup. Wrong source/origin/CWD/history/bootstrap still
fails. The subprocess receives the workspace's canonical home even when the
parent has no Codex variables or conflicting incidental ones. Working lead/member
threads remain eligible; unrelated sessions and utilities are not mutated by the
checks. No extra provider request, lifecycle action, broad client refactor,
RetryStore change or diagnostic subsystem belongs in this package.

Quick checks: focused Go provider/provenance tests using disposable fixtures and
Ruby scoped-provider tests in the repository's Nix environment; Go uses
`-mod=readonly`. Include a negative empty-source case and a missing-home case so
each omission is independently caught. Preserve safe error projection.
After implementation and ordinary review, the longer check is E's existing
isolated native 0.165.0 idle/working preparation harness extended with one valid
retained monitor and the real Ruby launch environment. Use a registered temporary
service and the monitor workflow if required. Stop at preparation; a full switch
or a retry on the affected session requires its own assigned execution scope.

Compatibility and recovery: no persisted schema, protocol, provider selection,
thread identity or recovery-journal change is needed. The two inputs restore
already-required validation contracts under the current native/package pair.
Keep all accepted operation/recovery semantics. A software rollback can read the
same state but reintroduces these refusals. Deploy only through ordinary reviewed
package procedures if later requested; leave the existing failed operation and
session intact. Package C's safe diagnostic improvements remain secondary and
are not a prerequisite to this functional repair. Archive behavior remains
accepted and its possible fix is not pursued.

## Package H — runtime selection and deployment preparation

2026-11-15, architect0. This supersedes G's earlier unassigned status: the lead
assigned G implementation to implementer0 and H pin preparation to implementer1.
The lead accepts H release once the final published G head is supplied. Host
activation depends on the exact generation comparison; it does not block pin
preparation. Architect0 owns this brief only; lead owns claims, activation,
integration and rollout records.

### Scope, ownership and dependencies

| Component | Owned files / interface | Required selection |
| --- | --- | --- |
| G, implementer0 | `dev-workspace` runtime fixes/tests | Published final reviewed feature head; no Codex or codex-web upgrade. |
| H, implementer1 | Workspace feature worktree `flake.nix`, `flake.lock` | Direct `inputs.vpsfree-dev-workspace.inputs.dev-workspace.url` points to G head. |
| H, implementer1 | Configuration feature worktree, generated input lock | Channel `dev-workspace`, role `devWorkspace`, selects that same G head. |
| Unchanged extension | `vpsfree-dev-workspace` | Preserve revision, content hash, sibling inputs and follows edges. No extension commit. |
| Lead deployment | Composed workspace default package and exact aitherdev generation | User-profile application is required; system-only deployment does not deliver G. |

Fresh preparation baselines reported by implementer1: workspace
`aa9333916fdc1062755a88e1b8298b845ec2ccc4`, configuration
`11ef63c5e173019b5312d672570158a0b0fb6dad`. Both effective runtime paths select
`458c7857b942fb592607c83af7b5287a6c93ea96` before H; extension is
`d76bd681c6db981907a52c187a3298549af87ab0`. Current selected user package at H
inspection is `/nix/store/qvszj2a3yj34jsra0hrh2lrcr18bi21x-dev-workspace-0.2.0`;
the earlier investigation's q85 package is not the deployment baseline.

Clean worktree registration, hook/environment preparation, baseline input graph
capture and parity checking are independent of G. Pin edits wait for the lead's
published final G head; do not pin an intermediate commit. Implementer1 retains
both H worktrees and their short commit windows; no shared-master edits or
repository claim is needed for this feature work.

### Pin commands and quick acceptance

In the workspace feature worktree, edit only the existing nested URL to
`github:aither64/dev-workspace/G_HEAD`, then run:

```sh
nix flake update vpsfree-dev-workspace/dev-workspace
```

In the configuration feature worktree's declared Nix environment:

```sh
confctl inputs channel set --commit dev-workspace devWorkspace G_HEAD
```

Keep confctl's generated commit/history. Do not manually edit its lockfile,
change its channel mapping, add a top-level workspace runtime input or rewrite
the extension's lock. Compare semantic locked identities and follows paths,
not node labels alone: only the runtime revision/hash and necessary transitive
changes are allowed. G makes no dependency change, so codex-web, llm-agents,
nixpkgs, extension, KB/devcluster siblings and unrelated configuration inputs
should remain identical.

Run the existing parity check against both prepared worktrees:

```sh
bin/check-dev-workspace-deployment --workspace-root WORKSPACE_TREE --configuration-root CONFIGURATION_TREE
```

This evaluates only aitherdev's site identity file and compares the two exact
runtime lock paths. Configuration quick acceptance also includes
`confctl inputs channel ls dev-workspace` and `confctl ls cz.vpsfree/machines/aitherdev`
in its Nix environment, verifying role/selector resolution without a build or
activation. Preserve declared hooks. Report final commits, exact old/new runtime
identities, unchanged siblings and check results. Lead applies the required
review before longer builds; no broad flake suite or host build belongs in H's
pre-review quick-check phase.

### Host versus application and deployment ordering

Configuration `flake.nix` maps channel `dev-workspace` / role `devWorkspace`
to input `devWorkspace`. Aitherdev `module.nix` consumes that channel;
`config.nix` imports `devWorkspace.nixosModules.host` and calls
`devWorkspace.lib.mkCodexPackage`. At runtime baseline 458c7857, the host module
imports `nix/host-paths.nix` and renders host reconciliation/nginx/TLS; native
packaging uses `nix/codex-package.nix` and the unchanged native input. Neither
depends on G's Go provider client or Ruby scoped subprocess implementation.
These fixes require application selection, not a functional NixOS change.

The configuration's `docs/operations/codex-providers-aitherdev.md` explicitly
permits application-only deployment and requires system-first ordering when
both change. Its older provider-activity description is not authority for G;
retain the current active-switch contract above. Respect the user's requested
configuration path by preparing its exact pin and checking the built host
generation. Do not introduce unrelated system changes just because defaults moved.

After review, prepare the composed package outside machine ownership with
`nix build --no-link --print-out-paths WORKSPACE_TREE`. For the authorized
aitherdev configuration, use its environment and only the exact selector:

```sh
confctl build cz.vpsfree/machines/aitherdev
confctl deploy --generation GENERATION --copy-only cz.vpsfree/machines/aitherdev switch
```

Retain the exact generation and compare its system output with both
`/run/current-system` and `/nix/var/nix/profiles/system`. Identical outputs need
no system change; pinned confctl `ff5e017780a35fb97b549db2a51b570193867c3b`
skips an already deployed generation. If a reviewed host change is required,
lead activates only that prepared generation under the held machine claim:

```sh
confctl deploy --generation GENERATION cz.vpsfree/machines/aitherdev dry-activate
confctl deploy --generation GENERATION cz.vpsfree/machines/aitherdev switch
```

Use no reboot, preserve configured auto-rollback and health checks, and verify
both live-system and system-profile identities. Unexpected unrelated activation
effects require reconciliation before proceeding. Then select the composed
application through the stable selected command:

```sh
DEV_WORKSPACE_CLAIM_ID=CLAIM_ID \
DEV_SESSION_SLUG=2026-11-13-archive-confirmation-regression \
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
workspace-host switch --source WORKSPACE_TREE
```

Lead's schema-2 machine request uses registered repository
`vpsfree-cz-configuration`, selector `cz.vpsfree/machines/aitherdev`, adapter
`confctl`; verify that exact held mapping before the activation batch. Build/copy
first, acquire near activation. Package-switch admission and forward recovery
remain owned by the selected runtime; no private helper, forced restart,
session interruption or lifecycle action is authorized by this brief.

### Verification, compatibility and recovery

G's focused tests and independent review precede long checks. Longer verification
uses the existing isolated native preparation fixture with one retained monitor,
then composed-package and exact configuration builds as needed. Use the monitor
workflow for uncertain/long checks and registered temporary services. Verify
selected profile package, unchanged native executable, portal health and continued
session access after activation. A live provider switch is not silently added to
deployment verification; retain private incident evidence outside tracked records.

No persistent format, host option, native protocol or extension API changes are
required. Preserve current coordination, provider/lifecycle journals, sensitive
session support and machine-identity compatibility. Retain predecessor package
and system identities for diagnosis. Workspace recovery is forward-only: resume
the original switch or select a corrected compatible package; do not use
`workspace-host rollback`. Preserve confctl auto-rollback for a failed system
activation and reconcile both system/profile outputs and any unfinished command.

Lead records exact runtime/workspace/configuration heads, complete effective input
graph and extension identity, built/selected profile and system paths, configured
machine binding, checks and fresh remote ancestry. Integrate the approved runtime
and both downstream feature lineages after verification, using separate short
repository claims; shared-workspace integration also takes the nonblocking
tracking lock. If deployed history changes, preserve reviewed equivalence or
redeploy a substantive successor. Release aitherdev promptly once deployment
effects and all deployed lineage are verified integrated, then verify release.
No session archive, stop or cleanup follows from release or handoff.
