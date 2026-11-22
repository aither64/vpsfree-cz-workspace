# P3 common retained-runtime ports prerequisite

Current P3 package milestone; native-routing effects remain parked and unfinished.
Committed checkpoint: `7e6229da4745db05484864107c03a9c72ab06dfc` on
`3318ca32392444167c4369ecd8cd17891bdaa4ce`. The exclusive index window is closed
and released; milestone acceptance is with the lead. No push or activation.

`WorkflowObservation.Settings` is captured with current policy/native proof and
sequence under the existing conversation lock. The optional same-Manager
`CheckedSubmissionSender.SendCheckedSubmission` validates the original handle,
full ref and input, enters the existing pre-lock invalidation ACK, then compares
the supplied digest with current settings under the same lock used by Configure.
It invokes unchanged `sendOwned` only after that comparison. It creates no prepared
row during preview and never replaces a supplied digest. The original ordinary
receipt encoding, digest, backend request and replay behavior are unchanged.

## Source and staging boundary

The final nine target paths and exact hashes are in
[tmp/p3i-common-ports-checkpoint.json](tmp/p3i-common-ports-checkpoint.json). Three new
guarded submission files, the new current-runtime reader/test, manager extraction,
workflow observation and the narrow runtime documentation are whole-file targets.
The earlier six-path checked-only packet remains a separate input receipt. `supervisor.go` is an index-only six-line `send_checked` case;
its tested clean target and patch are recorded in the packet. Its current native
inspection hunk must remain outside this checkpoint. No native prerequisite is
needed for this buildable overlay.

All seven parked native paths/hunks equal
[tmp/p3i-native-parked/manifest.json](tmp/p3i-native-parked/manifest.json). Removing
only the checked case from the current mixed supervisor reproduces the parked
supervisor hash. Do not stage that full mixed file. Peer central/UI/guard changes,
SDK leaf and native codec/writer work are excluded.

## Checks and their exact scopes

- On committed `6b64c744` plus only the guard overlay, pure checked cases passed
  **0.321s**. Actual Manager/Unix/pinned SDK normal ACK and socket-lost-ACK cases
  passed **4.739s**. Graph: [98 inputs](tmp/p3i-checked-inputs.json); log:
  [p3i-checked-check.log](tmp/p3i-checked-check.log). They verify post-Configure2
  current settings, stale-preview refusal before receipt/native input, exact
  original ref/input/witness, original Lookup after Configure3, exactly one native
  input, and Send ACK progress while an SH callback waits behind fixture EX.
- The added real question-domain fixture initially failed **2.196s** before the
  checked answer send. It omitted the private `0700` domain-store root setup used
  by the existing P6 fixture. The owning FileStore rejects a root with other
  permissions; Go testing creates each TempDir child with `0777` subject to umask.
  Added explicit `Chmod(0700)` and bounded test-only failure diagnostics. No
  production or timeout change. Failed evidence remains in
  [original domain log](tmp/p3i-checked-domain-check.log).
- That exact single corrected fixture passed **2.373s**, with compile-only
  **0.015s**, on committed `6b64c744` plus the guard overlay. Graph:
  [99 inputs](tmp/p3i-checked-domain-diagnostic-inputs.json); log:
  [domain result](tmp/p3i-checked-domain-diagnostic-check.log). It uses actual
  optional question/Plan callbacks and native-origin verification, real
  `piquestions.FileStore`/Service, response capture, Configure2, fresh atomic
  settings preparation, full-ref domain handoff persisted before checked Send,
  lost domain ACK, Configure3 and only original Lookup. Prepare and Send each run
  once; the transcript has bootstrap plus exactly one answer. Watcher command
  session46248 and parent CLI97400 completed0; no operation-owned survivors.
- Final committed `3318ca32` plus only owned guard overlays compiled and passed
  affected pure/real-control cancellation plus the newly committed retained-reader
  cases **0.831s**. Command:
  `nix develop /nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv --command go -C portal test -mod=readonly ./internal/piruntime -run '^(TestCheckedSubmission(Settings|Mismatch|Keeps|PreACK|RealControl)|TestInspectRetainedConversations)' -count=1`.
  [103-input graph](tmp/p3i-checked-final-inputs.json). Every nonowned input is from
  the committed parent; all five owned source overlays equal the passing native
  domain copy. No SDK rerun was needed for the committed guard-only parent change.
- Owned Go formatting and diff whitespace checks pass. The new operation covers
  pending/held/cold/policy-proof/scope/action/op/digest/message/context/generation
  mismatches, prepared/dispatching/Unknown/NotSubmitted/Accepted original receipts,
  pre-ACK context cancellation, actual ordinary-socket cancellation and watcher
  joining. Late ACK cannot revive a canceled send. No no-effect result is inferred
  after a native handoff.

The checks are separate component scopes, not central web, installed-package,
whole final suite or native-routing authority proof. No real model, live runtime,
activation, push, session lifecycle action or production fixture export occurred.
The finite SDK uses the existing test worker and test-only supervisor harness.

## Current runtime reader amendment

Lead released the accepted reader into this same priority checkpoint. The optional
same-Manager `CurrentRuntimeReader.ReadCurrentRuntime(ctx,SessionRef)` returns
literal `record.Runtime`; `ReadStart` returns literal `record.Start` from the
same private `readSavedRuntimeRecord`. That helper retains the existing strict
`m.record` current pointer/connected immutable history and original missing versus
ambiguous-artifact classifier, including error classifications. It introduces no
second parser, native call, state directory, runtime lock or repair. The new reader
checks cancellation before disk work and after a successful read. ReadStart keeps
its existing pre-read cancellation behavior. Returned identity, including a
preparing request, is not liveness, readiness or effect authority.

New pure reader tests passed **0.255s**. They use the actual `NewManager`, owning
reservation helper and strict codec; no supervisor/worker/SDK or transport harness
is added. A new Manager over retained schema1 or current successor schema2 returns
the exact full ref without Ensure, while an existing runtime.lock is held EX.
Retained bytes/mtime and directory entries remain unchanged. Damaged, wrong-scope,
config-mismatched, disconnected, missing-current, duplicate-generation and unknown
records refuse; both read ports share missing/empty/emptylock-versus-artifact
classification. Native Host Start/Inspect and Dial are explicit failure tripwires.
A canceled read creates no state. Ordinary non-directory path errors preserve the
same ReadStart refusal rather than being reclassified as absent.

Final common overlay passed **0.948s**, including compilation and existing
ReadStart initial/absence, strict schema2 malformed-history and explicit successor
read regressions, plus checked pure/real-control cases. Command:
[tmp/p3i-common-ports-focused-command.sh](tmp/p3i-common-ports-focused-command.sh),
[log](tmp/p3i-common-ports-focused.log),
[105-input graph](tmp/p3i-common-ports-final-inputs.json). Every nonowned input is
committed `3318ca32`; all eight owned source inputs equal current targets, with
only the guard case in the supervisor target. Pinned package env permits existing
fake-supervisor setup, but these cases start no SDK worker. All five prior checked
source overlays still equal their passing native domain scope. No unchanged SDK
rerun occurred. Command session50155 completed0, no operation-owned survivors.

P2 still rechecks exact Session/current authority Generation and the full current
Runtime after attachment waits, including same-generation replacement. Existing
AttachHost handshake, initial ACK and live workflow/domain proof remain mandatory.
The real new Server retained-attachment composition fixture stays with owner2; this
reader proof does not claim central attachment or installed readiness.

## Documentation and compatibility

The owning behavior and recovery explanation is the new common-port text in
`docs/pi-runtime.md` under Workflow observations and invalidation; lead main prose
pass is closed. Final doc SHA256:
`5933001c00eb5fe8aef070bc046ea0aea498804a18faba110ce855aedd1ad490`. It describes current settings, unchanged digest/receipt bytes,
pre-lock barrier, through-ACK admission, original-ref Lookup-only recovery and
missing-port refusal. It belongs in runtime reference documentation, with check
history retained here. No migration or retained format change is introduced by
this prerequisite. Older clients keep ordinary Send behavior; optional new
consumers require implemented Settings/sender support and cannot silently fall
back. Native schema3 and guards remain a separate unfinished source slice.

## Committed checkpoint and remaining work

The accepted final packet is
[tmp/p3i-common-ports-checkpoint.json](tmp/p3i-common-ports-checkpoint.json), SHA256
`5c06fac8cf4c7de4cd75f2d10dbedf174d94aaf226a3cad9ac2f88fe7aad2a3c`.
[Completed receipt](tmp/p3i-common-ports-commit-receipt.json) records the actual
full head/parent, exact nine-path inventory, precommit staged/committed/current
hashes and the expected mixed-supervisor exception. The ordinary Nix-shell
`git commit -F` used the verified staged index without `--only` or hook bypass.
All nine committed targets equal the tested packet; all eight whole-file current
targets are clean. The supervisor retains only its original native inspection
hunk at the original mixed source hash. All seven parked native paths/hunks are
unchanged. The post-commit index is empty and the window was released before
this evidence update. No peer paths entered the commit.

Next: lead milestone acceptance, then resume the already released native package
under its remaining guards and authority gates. Full central composition,
installed proof and final independent whole-branch review remain lead-owned gaps.
This checkpoint does not claim native-core or production composition readiness.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
