# Native review fixes: N1/N2 committed, ready for acceptance

One executing priority package in isolated `dev-workspace-native-fix`, branch
`2026-11-11-pi-codex-migration-native-fix`, exact base
`d3b0057f6b032d19a4b2cc86b81a3493e5220981` and committed fix head
`234dfd530d8412a559e6e0b09b9eaa671037d48a`. The primary d3 source stays frozen.
R4 is parked under [its exact source manifest](tmp/p3i-r4-parked-source.json)
and [handoff](p3i-review-instructions-evidence.md); its three untested Go hashes
and empty index were independently rechecked unchanged. No concurrent R4 work.

## N1 result

Successful ownedNativeSettled sets released and cancels its original lifetime.
The retained arm therefore has ctx.Err even after positive settlement. The old
inspection predicate treated that as unresolved, falsely holding observations
and the Manager Load discovery path, including after explicit physical reset.
The only production change is `!nativeRun.released` on that unresolved-arm arm;
callback, unreleased/expired/held, mapping pending and runtime proofs stay intact.
One nearby comment explains why successful cancellation is expected.

The new seven-case regression composes the existing nativeTransactionFixture,
nativeDispatchFixtureWorker and positive canRelease proof seam. Its fake
certificates are explicit. It reproduces the exact released+canceled memory
state of positive settlement; it does not claim another actual SDK settlement.
Positive Inspect verifies without a write; owning loaded Load and physical reset/
Inspect/Load succeed, original tuple/pointer/canceled deadline remain unchanged,
and dispatch count stays zero. The six negatives preserve canceled/held/expiring
unreleased arms and independent routing-pending/callback-unknown/mapping holds.
Only the explicit physical-reset routing apply is allowed; no input/charge path
is invoked. No new original, retry arm, receipt or history repair is introduced.

The final unchanged test bytes ran RED against the original production predicate
**Go0.185s**, exit1, failing only `released` as held/unresolved_state:
[red inputs](tmp/p3i-native-n1-red-inputs.json), [red log](tmp/p3i-native-n1-red.log).
With N1, the seven subcases plus five related existing inspection/reset/lifetime/
positive-effect groups pass **Go0.359s**, command5.517s, exit0:
[command](tmp/p3i-native-n1-green-command.json), [green log](tmp/p3i-native-n1-green.log).
Both were quick inline checks; no SDK component rerun or watcher was needed.

An earlier first-green attempt reached the new Load assertion and found that the
existing transaction fixture omitted snapshot.HistoryFile. Only the test setup
was corrected to its exact owned history pathname; no product check was weakened.
The final test then ran RED again before GREEN, with identical final test bytes.
Initial red4638/exit1, fixture-diagnostic64204/exit1, final red39674/exit1 and
final green52002/exit0 all joined. No command/process effect remains running.

The [121-input graph](tmp/p3i-native-fix-inputs.json) SHA256 is
`9b787ea5ee267115c83c1370c1334b319a72f70c49af30b929d27b009f53554c`,
exact d3 plus only native_routing.go/test.go. All other native component source
inputs match their original scoped graph. The [owned patch](tmp/p3i-native-fix.patch)
SHA256 is `58131993f3a5fa9cf228389c79721f093f9f93229dc7e1a17d60d8b6d8c7aba4`:
92 additions/one deletion over two files. Diff-check and gofmt checks pass.
That was the pre-N2 source checkpoint; the final consolidated commit is below.
Existing technical docs already describe positive
settlement; the bug fix needs no new semantic prose. Original SDK4.711/7.267 and
other native scopes remain exact old-source evidence, not a full fixed-head run.

## N2 design dependency (resolved before implementation)

Reviewer0/lead also require independent Manager schema3 package guards on
Configure and ApplyToolPolicy. Before implementation, architect0/1 identified
a decisive race in a pre-m.call two-read helper: Manager A sees legacy2 and skips
its nil/error native guard, then waits in m.call Inspect; Manager B converts the
same mapping to3. A reaches an accepting supervisor under the same Runtime/Start/
generation/settings/policy and can write schema3 with only the supervisor guard.
Existing supervisor capture/checkRecord fences its own schema, not A's capture.
There is no cross-Manager/process lock spanning all converters and A mutation.

Per the lead's consequential-interface boundary, N2 implementation stopped until the architect/lead settled the exact schema-
classification refusal seam. The subsequent accepted canonical amendment and
lead-expanded source window explicitly released that private frame repair.
No permission boolean, lock, parser or legacy guard was invented. The factual
private field below is exactly the later architect/lead-approved amendment.
Sequential nil/error cases alone cannot prove the transition race. Lead report
7362bccf and direct architect0/1 source facts record this blocker. Current package
remains one native fix; reviewer0 retains independent source review ownership.

No source revision was pushed, rebased, integrated or activated. No schema/native3
producer, real model/auth, B1, Instructions or ActiveHostInput change. Production
native/B1/recovery limitations of the original finite checkpoint remain.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/

## N2 implementation and final assurance

Only Configure and ApplyToolPolicy classify with the existing full owning mapping
reader. Stable3 requires the initiating Manager's own package guard, then fresh
full Runtime/Start and schema checks. The private ExpectedRecordSchema scalar is
omitted for legacy1/2 and present exactly integer3 for schema3. Owning strict
decoding rejects present null/0/1/2/other/fraction/string/case/duplicates. It is a
schema precondition, never permission. Other retained reads/interrupt/unload and
utility bodies do not gain this field/gate. Supervisor independently guards, then
compares schema under c.mu before pending/save/worker effects. Mismatch conflicts;
no implicit readmission/retry/repair or original receipt change occurs.

The existing fakeHost/Manager/Unix and nativeTransactionFixture are composed
without SDK or a second parser/harness. Stable3 tests prove Manager nil/error with
accepting supervisor, opposite per-side refusal, both-good, exact immutable root
forwarding/outside-lock invocation, schema-change/context refusal and unchanged
schema1 Configure/schema2 Configure+Apply. The actual two-Manager test pauses A's
legacy call in Host.Inspect after final classification; B converts via its public
ConfigureNativeRouting while Runtime/Start/settings/policy remain exact. A's public
Configure and Apply both conflict. File bytes/inode/modtime, pending fields and
worker-call inventory show zero additional writes/effects. Both Manager calls and
their explicit goroutine joins finish. All guards/worker/process identities are
fixture fakes; this proves control/serialization, not production native readiness.

Final source is exact d3 plus six owned Go overlays in
[121-input manifest](tmp/p3i-native-fix-final-inputs.json), SHA256
`9ae55c57bda2d834f188769ba0a032f32458539548c2b9a736105b5426972e26`.
On this graph, final asymmetric/late-conversion/unchanged utility-golden groups
pass **Go1.591s** (command6.607s), [command](tmp/p3i-native-n2-final-command.json),
[log](tmp/p3i-native-n2-final.log). Final strict private-field/legacy/utility
mapping/native-B2/physical-settings groups pass **Go0.126s** (command1.835s),
[command](tmp/p3i-native-n2-codec-command.json), [log](tmp/p3i-native-n2-codec.log).
Earlier N2 source passed1.863s before extra inode/modtime assertions; that older
receipt is separate. Initial unused-variable compile errors were corrected before
any fixture ran; the small strict interface and one both-good case passed before
the batch. N1's earlier unchanged six-group .359 scope is preserved, not rerun or
relabeled. No JS/SDK/real model/auth check or long watcher was launched.

Final six-source diff-check/gofmt pass. Existing docs already promise both guards
and positive release; private code comments preserve the specific rationale, so
no semantic main prose change is necessary. The final packet links exact paths,
hashes and changed scope. No persisted schema/receipt/utility/H0 format or database
migration is introduced. The new private schema3 precondition is intentionally
refused by incompatible strict predecessors; absent legacy frames stay identical.
R4's parked hashes/index and primary d3 were preserved. All N2 command sessions
45636/83484/96414/93728/75217/10810/14711 are terminal; no process effect remains.

## Completed isolated commit

Normal temporary-message-file Nix-shell git commit exited0 at
`234dfd530d8412a559e6e0b09b9eaa671037d48a`, parent exact d3 above, tree
`52e10df22e75a9254e82aed4ba353d7b363aa6e1`. Its six owned Go files are 491
additions/10 deletions; no new source file or peer path. The
[final packet](tmp/p3i-native-fix-final-packet.json) SHA256 is
`4d21830885549c6a391ace7466f207dea650b3d41b8514d9df98e302c299be3c`;
[exact committed diff](tmp/p3i-native-fix-final.patch) SHA256 is
`dc6ac9febb86ea7041e89d2cd76b403e45f785ff76440425d9950f7ab40b4a6c`.

[Complete commit receipt](tmp/p3i-native-fix-commit-receipt.json) SHA256
`6de5a922532fb9656c86c2e6894705f7c0bd011179b03cdd7c404dd57ea05203`
proves exact inventory, staged/index=committed=current target hashes, clean owned
and full isolated worktree, empty index, unchanged clean primary d3 and exact
parked R4 hashes/index. There was no declared hook framework or active hook;
ordinary hooks were not bypassed or changed. All source/check/commit effects are
joined. This isolated window is released, report929d680d.

Ready for lead acceptance and reviewer0 affected-lane review of the new private
N2 classification design/frame/consumer checks; prior N1 review conclusions and
unchanged successful scopes remain separate. No branch or ref was cut over,
rebased or pushed, and no primary/reviewed R source or installed selection changed.
No database or persisted migration occurred. Current fix ownership is retained;
R4 stays parked until explicit lead sequencing, not concurrently executing.
