# Original Pi request recovery — source and quick-check handoff

Ready for lead acceptance and retained reviewer0 review; no publication, consumer
qualification or live retry is claimed. The assigned correction is committed at
`8ff582caf5b4c7b6ac867d0f180212b1b4b0ce80`, tree
`9ae186e214adb0621b5ba31bb81cd5396f507aee`, with exact consumed parent
`dc64356b852ab497a0250d07e3296a69152a1963`. Worktree:
`worktrees/2026-11-11-pi-codex-migration/dev-workspace-pi-roster-preflight-fix`.
The nine committed/current/index files equal the final checkpoint; worktree and
index are clean. [Commit receipt](tmp/pi-start-recovery/commit-receipt.json)
SHA256 `33625762f81afa3a60bf14de5850995f6795b7c63e0580b9a2352f25fcca05e4`
contains exact inventory, hashes, scopes and process effects.

The sufficient architect brief is design.md:13054–13222, accepted file SHA256
`a2b2f15b93e3b371cb01a4feaa2c9c3e653e6d22bf70a22d1a6f07afad7b6a44`.
Scope is the existing original-request Retry creation path. No new command,
control, schema, registry, helper, worker, SDK, endpoint or Nix setting is added.
Production changes are manager.go, pi_providers.go and pi_creation_flow.go.
Existing tests plus one start_recovery_test.go verify the boundary. Maintained
docs are pi-runtime-host.md and session-preparations.md; no unrelated prose changed.

## Delivered behavior and boundary

The existing strict helper decoder classifies only exact uncancelled exit1
schema1 rejected/unknown_request with matching instance/request as
ErrHostIntentAbsent, which remains errors.Is-compatible with ErrUnavailable.
Malformed, foreign, oversized, sudo/empty, signal, cancellation, other exit and
non-inspect cases never classify as absence. Redacted diagnostics remain bounded.

ResumeInitialStart requires the saved current schema1 initial starting record,
exact Start, existing private runtime.lock and frozen launch/config/root inputs.
It reads and verifies bytes and owning identities, checks the original package
with the existing validator, and performs no reservation, record rewrite, phase
repair or ID allocation. It holds runtime ownership, never launch.lock during
helper entry. It inspects first and calls same-ID Host.Start only on exact typed
absence; existing observations follow normal validation. Ordinary Ensure/Inspect
retain their prior observational behavior.

The creation owner derives permission after its existing lock/profile/receipt/
lifecycle checks, from a retained ReadStart observed before Ensure, unchanged
pre-native creating journal/binding and absent runtime authority. Fresh Ensure
failures cannot resume in that attempt. Optional runtimes without the method
refuse. After resume, readiness only inspects the original ref. Existing native
intent/result retains Unknown or original Lookup/Verify behavior with no resend.

Current selected portal B and original launch A are admitted independently.
The five runtime-contract/pi-runtime/pi-worker/pi-models/pi-providers files must
be present, bounded and byte-identical; actual owning package, model, provider,
team and instruction validators remain enabled. Current B profile must match;
saved A path/profile token and explicit accepted model/effort overrides remain
unchanged. Original A continues to supply models/supervisor/worker. No portal
executable equality is imposed.

## Checks and exact attribution

Declared shell: `/nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv`.
Go commands use explicit `-mod=readonly`. No hook framework or active non-sample
hook is declared; both ordinary commit/amend used the Nix shell and tempfile -F,
without bypass. Diff-check and gofmt pass. Both main-agent prose spans are closed:
pi-runtime-host.md `b009331f6c766030498ee308d786c94e0cc7e48d6e8e6a69882c332c79c5b4ec`;
session-preparations.md `df0d222a8ce87d5887409b033f4780d334444925e43c4cfc41b926069b4097d0`.

- Focused owning Manager/decoder tests initially passed Go0.672s; final changed
  Manager/decoder/refusal scope passed Go0.839s (tool40821), including missing lock,
  symlinked lock/config parent, changed bytes, invalid package, successor/history,
  scope and uncertainty. Frozen bytes and helper-lock availability are checked.
- Existing HTTP retry/lost-memory tests initially passed Go4.585s. The final
  meaningful join uses actual Manager Ensure/ReadStart/Resume and actual frozen
  files, with fake Host and existing fake post-host readiness/Create/Send. It
  passes Go3.020s (tool27521): first refusal gives zero host intent/Create/Send;
  original retry produces one native-start fixture count, one Create/first Send;
  ready retries add no effects and preserve IDs and frozen bytes. The first join
  setup failed Go2.099s because generic slug `example` is invalid for real runtime;
  only the fixture changed to its existing dated-slug constructor.
- Strict immutable A/B source admission passes Go2.989s. Inputs come through
  PI_START_RECOVERY_PACKAGES; reusable source contains no site package paths.
  The retained A is unchanged; disposable B copies only static metadata and links
  to A's executable for validation, never execution. Five-file drift, missing and
  symlinked input, instructions/catalog/current profile/request/token/session/
  replacement/revision negatives refuse. Captured overrides and A models path
  remain exact. [Input receipt](tmp/pi-start-recovery/package-inputs.json) binds
  copied bytes and task-owned indirect retention roots.
- The one original affected-package batch on [929-input graph](tmp/pi-start-recovery/check-inputs.json)
  `010d0a2d72e45933d62ac5b80d65e413dc6203bd1ac09071c43ed5174481b623`
  exited1 after332.775s: piruntime passed5.897s; web failed329.672s. Exactly two
  selectors failed: unrooted disposable B had disappeared before A/B admission,
  and the unchanged browser helper's require(playwright) lacked NODE_PATH.
  Ruby did not run. [Original output](tmp/pi-start-recovery/check.log) and
  [outcome](tmp/pi-start-recovery/check-results.json) remain unchanged.
- After identical fixture reimport with retention roots and cached NODE_PATH,
  a fresh Luna/low watcher ran only those two failed web selectors, then the
  previously unrun Ruby host test. They passed29.988s and1.779s respectively;
  Ruby reports21 tests/120 assertions/0 failures/errors/skips. This is changed
  input verification, not a repeated full package pass. All remaining original
  web tests completed without reported failure in the original batch.
  [Targeted output](tmp/pi-start-recovery/final-check.log),
  [results](tmp/pi-start-recovery/final-check-results.json) and
  [watcher](tmp/pi-start-recovery/final-watcher-result.md) retain that scope.

The original watcher's source332.775s operation and final watcher command/CLI
operation are terminal and joined. The final watcher launch first refused a CLI
flag position before any source command; moving global --ask-for-approval before
exec launched the sole corrected batch. Final Manager and real-Manager HTTP tests
ran after the frozen original batch; exact final deltas are in the receipt. No
unchanged full SDK, Nix build, VM, CI or integration batch ran.

## Whole-series review and compatibility

Overall risk HIGH; lead invokes retained reviewer0 across general, architecture,
scope and risk/compatibility lanes. This packet supplies evidence without
self-review or invoking another reviewer. The full range is
`9241a342a6ef4ca69148594e98cce7ddcfb459a6..8ff582caf5b4c7b6ac867d0f180212b1b4b0ce80`,
51 commits: literal consumed prior50 plus this one coherent correction. See
[full history](tmp/pi-start-recovery/full-history.txt),
[full final diff](tmp/pi-start-recovery/full-final.patch),
[full diffstat](tmp/pi-start-recovery/full-diffstat.txt) and
[proper-parent correction](tmp/pi-start-recovery/correction.patch).
Consumed dc643/full50 review d909ed10 and existing review-packet.md:4604 onward
remain at their actual scope. Full-series diff hash is
`3f29fa971225579fcfde2036517fa01a0103aa30166911e31ea9ae72a93651cd`.

This correction adds no database or persisted-state migration, capability value,
new operation or dependency/pin update stream. The complete series is NOT
migration-free: inherited runtime1→2, communication1→2, creation4, preparation and
retained-reader/forward-recovery obligations remain. Existing consumed deployed/
selected boundaries, original failed live request, diagnostics, direct/built refs
and migration evidence stay unchanged. See prior consumed-boundary receipts under
tmp/pi-roster-preflight-fix/monitor-correction and the existing full review packet.
Do not call an equivalent historical successor literal ancestry or discard old
consumers. No repeated new dependency stream or obsolete implementation remains
in this delta. Unpublished local fc39 was amended only for the required joined
test; its receipt/checkpoint/patch are preserved as fc39-* artifacts.

Documentation routing: host recovery and immutable launch contract → operator/
reference → docs/pi-runtime-host.md; request retry and no-resend semantics → caller/
reference → docs/session-preparations.md. Individual execution and source hashes
stay in this session record. Existing old paragraphs/commands are preserved.

The repository's trusted-local-operator boundary is unchanged. Wrong scope,
ordinary filesystem mistakes, concurrent owners, stale profile and uncertain
native work refuse; no hostile administrator containment framework is added.
Actual helpers, systemd, SDK/provider dispatch and private auth/history are outside
these fixtures. Real corrected B output qualification, independent source review,
publication/CI, W/H build/activation and one original live retry remain lead-owned.
No live records, credentials, native history, provider/API/helper/service/claim,
browser, merge or lifecycle action occurred. The session remains open.

[Stable session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/)

## Coherent transition and original retry: committed successor

The source correction is committed at
`2e7b2489e56193dd3a5c31316da9d4e838f8c0e1`, tree
`0a951f0ce91c0b88b686d76105f0eed5872458e2`, directly over consumed
`8ff582caf5b4c7b6ac867d0f180212b1b4b0ce80`. The literal full51 history remains
unchanged; the complete series from `9241a342` now contains 52 commits. This
checkpoint has no publication, consumer-pin, application-build or live authority.

The strict Ruby backend reader returns a stopped pre-native disposition only
after validating the receipt, journal, immutable companion and original creating
binding together. One host admission accounts for both unfinished labels. It
rereads current state during preparation, before maintenance dispatch, under
exclusive transition validation and in the selected `_activate` process. The
direct switch and reconstructed `activate-prepared` share that decision. There
is no saved eligibility, new prepared field, schema or dispatch interface.
Preservation requires unchanged native registration and maintenance; selected
activation also requires the exact ordinary pending target. Every other
unfinished fence and the original retry's Start/Create/Send authority remain.

Production changes are confined to `libexec/workspace-host`,
`libexec/workspace-session-backends.rb`, and the one pre-maintenance routing site
in `libexec/workspace-coordination-host.rb`. Tests extend the existing profile
transition suite, actual-scanner driver and Go original-retry fixture. The two
documentation spans are in `docs/workspace-updates.md` and
`docs/session-preparations.md`; lead's final prose hashes remain `a38c15c9` and
`5e473f73`. The exact eight committed/current files match final check inputs;
the worktree and index are clean. The ordinary Nix environment and `git commit
-F` were used; no hook framework or active Git hooks were declared or bypassed.

The main joined regression passed in all four modes: direct candidate switch,
serialized preparation in another process, selected pending forward recovery,
and a harmless advanced but stopped attempt. Each uses the same disposable
original records and profile through actual Ruby host preparation, EX validation
and a separate selected `_activate`, then the original HTTP retry. The actual Go
scanner and real Manager own validation of the saved reservation, launch and
configuration. Nix/systemd, physical claim, post-host readiness and native
Create/Send remain fake boundaries. Switching has zero Pi Start/Create/Send;
the original retry produces one successful Start, Create and first Send, with
no extra effects from ready retries. Frozen A, its profile token, IDs and launch
bytes remain original. The four-mode result is 49.360 seconds wall time
(Go reports 33.004 seconds).

Focused negatives cover running/missing/mismatching bundles, native intent and
explicit null, successor binding, unrelated unfinished work, actual retained
native-domain claims, changed startup arguments before maintenance, fresh EX
refusal, and selected/pending mismatch. The original affected Ruby run finished
with 79 tests, 1500 assertions and seven failures. One caught an eager lookup of
an optional preparation field before the existing service-cleanup refusal;
the final source restores its nil default. One expected an obsolete refusal
label after the owning backend check moved earlier. Five unchanged tmux cases
hit Nix's long temporary pathname. Those seven cases and the four new negatives
passed with the corrected source/assertion and `TMPDIR=/tmp`: 11 tests,
381 assertions, zero failures/errors/skips in 12.531 seconds. The other 72
successful cases retain only their original input scope. The backend reader
passed 12 tests/320 assertions in 1.167 seconds; the existing actual-scanner/Ruby
retired-fence case passed in 8.881 seconds. Ruby syntax, gofmt and diff checks pass.

`tmp/pi-start-recovery/transition/verification-attribution.json` reconstructs the
original tested hashes from final bytes: only the missing-key nil fallback and
that refusal-label assertion changed after the four-mode success. Present-key
joined paths remain identical; the missing-key path was rerun successfully.
The original failed Ruby result is retained rather than relabeled successful.
Earlier joined setup failures are also retained: a fixture helper typo at
compile time, an initial preset/receipt override mismatch, a missing disposable
`repos/`, and generic registration arguments incompatible with A's reporting
contract. Small Ruby reproductions then identified the Pi-only B fixture's
missing `workspace-host` and the physical-claim boundary. The final fixture uses
already qualified A/jcb and B/vq metadata, the existing reporting-aware external
seams and current compiled scanner. It does not loosen production validation.
One initial setup reproduction reached the ordinary offline Codex contract
check in disposable directories before claim refusal; the final fixture mocks
that external native seam. No live provider or native session was used.

The compact receipt is
`tmp/pi-start-recovery/transition/commit-receipt.json`, 13262 bytes, SHA-256
`258faf58769d238685d6b38371f8ce98ea007c422393172b3731bbc64674f050`.
It binds all eight file hashes, 27 artifacts, correction and full52 patches,
history, selected immutable inputs, results and verification reuse. Native
delegation was unavailable in the current tool surface, so checks used the
monitor skill's visible parent-observation fallback. All original handles are
terminal/joined: compile 25529/33604, joined checks 73259/18234/35701/43649,
Ruby reproductions 83329/55709/64475/15388/15421, focused Ruby 98375/11723,
syntax 8042, and affected batches 56985/7172. No current operation is running.

This delta adds no migration or persisted format. The full R series is not
migration-free: inherited schema and consumed rollout obligations above still
apply, including accepted full51 review `5540a0a2`. No history was amended or
rebased, and no consumed ref or root was removed. The trusted local operator
boundary remains unchanged. No live original record, credential, provider,
browser, helper, service, profile, machine claim or session lifecycle action
occurred. Lead owns acceptance and retained reviewer0's affected final review,
then any separately released publication, matching consumers and live recovery.

## CI assertion correction

R2e7's original CI run `43973662710`, attempt1, failed in all three active jobs
on the same stale malformed-journal assertion. The earlier owning reader now
reports `session backend compatibility: cannot read backend evidence`; malformed
state still refuses before profile selection. Saved original job metadata,
failure excerpts and ZIP remain under `tmp/pi-start-recovery/ci-2e7/`. No CI job
was rerun.

The exact selector reproduced red in 1.508 seconds. Changing only its expected
label passed the selector in 1.396 seconds, retaining all four assertions. One
full owning `workspace_host` Ruby suite with the declared environment and short
`TMPDIR=/tmp` passed in 108.408 seconds: 331 tests, 5196 assertions, zero
failures/errors/skips. Neighboring error-label expectations were inspected once;
no production or documentation change was needed.

The lead confirmed that neither W nor H had begun a 2e7 realization or external
deployment and authorized folding this direct test correction. Exact published
`2e7b2489` remains at `2026-11-11-pi-codex-migration-r-2e7-published`. Corrected
head `a43c82f1741fd6f713acd3014c57932759cf323b`, tree
`2b2a49155d14e754129509b95cd134f13ac08af8`, is an amended sibling over literal
`8ff582ca`; 2e7 is retained, not an ancestor. Full52 still preserves literal
consumed full51. Its only difference from 2e7 is that one assertion string;
production, closed prose and the other seven files are byte-identical.

The clean committed/current checkpoint is bound by
`tmp/pi-start-recovery/transition/ci-label-fix/commit-receipt.json`, 8423 bytes,
SHA-256 `0516ebb22075452955422b2b0bd0cfdc5c13ccb5b248bcd11f51d9193355014b`.
It includes the narrow difference, corrected full52/history, original CI evidence
and exact red/green/full-suite results. Tools 83696 and 69893 and their children
are terminal/joined. W175c and He8e7 remain frozen, unbuilt candidates; their
metadata and sole shared checker retain only R2e7 input scope. No republication,
repin, build, live probe, activation, claim or lifecycle action followed this
correction. Lead owns exact-fix acceptance and continuation.
