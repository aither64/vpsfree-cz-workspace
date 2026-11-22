# REVIEW-R4-P3: dependent creation-proof successor committed

Current correction is isolated over accepted owning source
`8c16a2865e8ef73aeed6789b72ec99150783c093`, not a new package. Lead released
only CreationProof.InstructionsDigest production changes in types.go and the
existing fresh verifyCreation block, plus existing tests and a short doc note.
Eight-c source remains preserved and unadvertised; owner3 already adopted it,
while this committed dependent proof field awaits lead acceptance and later handover.

[Exact five-path checkpoint](tmp/p3i-r4-proof-checkpoint.json) SHA256
`98f2530dd62d0abfda40aa86d634516899ebccca8dc2cfd1d56a805db58adf00`,
[patch](tmp/p3i-r4-proof-checkpoint.patch) SHA256
`610a527d629f52d0225f71778edaa91ef71256143a0f6482dd6e40906722a141`:
67 additions/two deletions. Two production lines expose the same-worker snapshot
value only after the existing immutable nonempty mapping digest match; no config
hash echo, signature/request/op/persisted schema/Goal/receipt/H0/utility change.
Legacy-empty omission keeps old proof JSON bytes and historical observational
semantics. No missing/cold worker proof can cause Load/Create/retrofit/resend.

Focused producer fake checks pass **Go0.070s**, [receipt](tmp/p3i-r4-proof-pure-receipt.json):
verified exact lowercase64, legacy golden/omission, fresh missing/mismatch/replaced/
cold refusal without caching earlier evidence, mapping and receipt bytes unchanged.
Existing actual R4 case alone was changed to assert the new PUBLIC proof before
Goal, after fresh worker/new Manager/Configure and on original Bootstrap Verify;
actual prior-R JS missing-ack hold/reap and empty legacy support stay in that case.
Fresh installed Luna/low ran it on [718-input graph](tmp/p3i-r4-proof-inputs.json),
SHA256 `1cf88e64bb3d58d8b497fdd904b518a3f1d641d9ce751255ed1c97865ba849c2`,
8c+four Go overlays, same independently verified prior-R27 JS inputs:
**Go7.569s**, command11.880s, exit0. [Log](tmp/p3i-r4-proof.log);
[watcher](tmp/p3i-r4-proof-watcher-result.md). Pure69109 and watcher4194 joined0,
all test-owned processes reaped/joined. No interface/native/broad SDK rerun.
All current runtime/test hashes match this frozen graph; diff-check/gofmt pass.

Lead main prose is closed ONLY on the new three-line CreationProof note in
docs/pi-runtime.md, approved SHA256
`93e11f66178422c203f84a553206ab5f4c0afe019315b9afbda8b1a0987c4fb6`. It clarifies comparison to SHA-256 of the frozen original role.
Removing it exactly reproduces closed8c prose; runtime4 remain unchanged.
Original pre-main packet/patch are preserved under tmp/*.pre-main.*. The exact5
ordinary cached-Nix commit completed without hook bypass. [Committed receipt](tmp/p3i-r4-proof-commit-receipt.json)
SHA256 `c26877c95eb4c6681d0b8a3b06c74c53e89c2cc2e376cba687794ff245c5588b` binds head
`602d75063a0ad4877441992751b1757175740ac4`, parent `8c16a2865e8ef73aeed6789b72ec99150783c093`,
tree `1099ee30405222042ad7affcf72f00c393b299be`. All5 committed/current/index blobs
equal approved source, all718 tested source inputs match current, whole worktree
clean/index empty; commit command and earlier watcher effects joined. Primaryd3
and native234 remain exact and clean. Source/index window is complete, ready for
lead acceptance and explicit dependent handover. Producer source does not implement or allocate
P2's three frozen-original comparisons, owner3 guard/projector handover, or last
publication; production remains held for those separate full proofs. Native234,
primaryd3, reviewedR/C stay frozen; no push/rebase/activation/lifecycle.

## Accepted initial owning checkpoint and its original evidence


One executing isolated package, branch
`2026-11-11-pi-codex-migration-review-instructions`, worktree
`dev-workspace-review-instructions`, exact reviewed base
`cd5fd5cbc9670311d411466de8ec63ff670d53b0` (R), committed head
`8c16a2865e8ef73aeed6789b72ec99150783c093`. No native d3/234, special native
codec/schema3 or leaf source is imported. Native fix234 is separately accepted
and frozen with no new review findings. The earlier three-Go-hunk park for N1/N2
is preserved in [its receipt](tmp/p3i-r4-parked-source.json); lead explicitly
resumed this package after capacity confirmation. Those old hunks were untested
then; the current source/results below supersede that status.

## Result and source boundary

[Exact nine-path packet](tmp/p3i-r4-checkpoint.json), SHA256
`6f9e08b90f9ebc57ff64480e3e2b431ea3d6c2dcebb4285062958272f62140b3`,
freezes eight tested runtime/test overlays plus only new role paragraphs in
`docs/pi-runtime.md`. The [owned patch](tmp/p3i-r4-checkpoint.patch) SHA256 is
`32b6cde34e6bb55f0b23b03e79929d8ec26ffffad0b87fbb05b9e6d0b99a1a28`;
595 additions/35 deletions, no new source file. All runtime/test hashes match
the actual component graph. Index empty after the exact ordinary stage/commit; no push has run. Technical
doc SHA256 `4358596b7a51e766807fd6aabc2080a0190bb6e4dc2275420ac4c0d29461780b`
is closed by lead main prose ONLY after CreationID and before HistoryRef.
Existing common/workflow/tool-policy/host sections remain byte-unchanged.

Canonical disk Instructions is omitted for legacy empty or present nonempty
valid UTF8/NUL-free<=4096 bytes in retained2 only. Empty/null/case/type/oversize,
retained1 or utility presence refuses in the owning single conversation codec.
Go empty request omits the field; persisted immutable bytes are saved before init,
replay compares exact original, every load uses the saved field, Configure does
not select a role. A legacy-empty worker cannot be retrofitted by Create replay.
Owner3's HasInstructions/whole inventory/scanner/target gate and original-fence
proof remain later dependencies, not implemented by this package.

Actual loader append override captures a detached immutable complete base and
returns base+[original literal], preserving normal default/custom/AGENTS and the
owned ToolPolicy suffix. A private closure rechecks actual whole loader array,
public observed construction options/customPrompt/contextFiles/effective prompt,
same session/loader/runner at init/snapshot/pre-send before pending/active/prompt,
and pre-Configure. Failure holds, not NotSubmitted. The lowerhex SHA256 ACK hashes
only the observed final literal's UTF8 bytes, never config/full-prompt/JSON/trim.
Go correlates the actual init/process/NativeID/generation and exact expected saved
digest before publishing the worker; later snapshots and VerifyCreation recheck.
Missing/wrong/malformed proof cannot grant ready/Goal or recovery authority.

## Public SDK source-fit correction and checks

A precise type preflight caught our earlier attribution error BEFORE any SDK
fixture: ordinary session_start ExtensionContext has getSystemPrompt only;
getSystemPromptOptions belongs to ExtensionCommandContext. Its factory is inert:
actual runner.createCommandContext creates lazy closures and calls no command,
wait, reload or mutation. Completed bind installs the same actual session's option
accessor before session_start. Architect0/1 and lead corrected canonical design.
Current code captures that bound runner, checks identity, creates a fresh public
context and calls ONLY getSystemPromptOptions, detaching all observations. Missing/
stale/unbound cwd-only fallback cannot satisfy the complete nonempty addendum.
The ordinary event context still supplies independent getSystemPrompt. No command
registration/dispatch, new API/op/version, parallel builder/parser, substring-only
proof or SDK patch was added.

Pure owning codec/replay/ACK plus unchanged initial-tool-policy and utility golden
checks passed Go0.056s; the initial failure was only a test searching arbitrary
Instructions substring inside its own temporary pathname. It now checks the exact
JSON key. NUL/Unicode/newline/byte bounds are explicit: the generic identifier
validString was correctly replaced for role text because it forbids all controls.
Pure Node failed-proof-before-pending/config plus original version smoke pass2/2,
0.352s; syntax passes. Final pure Go0.058s/command1.763s passed; its complete receipt is in
[tmp/p3i-r4-final-pure.log](tmp/p3i-r4-final-pure.log), exact command alongside it.
All owned files pass diff-check and Go files are gofmt-clean.

Fresh installed Luna/low ran ONLY the actual public pinned1.5.2 interface case:
[34-source graph](tmp/p3i-r4-interface-inputs.json), SHA256
`27dff68b3c6f5efd2f3c243fc1dbdf1bbc28d62b77720390bc3a08ff6795614b`,
R+seven then-current overlays. It passed1/0, test207.598ms, command2.821s.
[Log](tmp/p3i-r4-interface.log), [watcher](tmp/p3i-r4-interface-watcher-result.md).
Default and genuine custom prompt, preexisting append, AGENTS, existing-file path
kept literal, multibyte/newline exact observed role/digest and one copy were proved;
injected resource/session replacement and changed observed append refused. Faux
model registry only; no prompt/provider request or credentials in this scope.

Fresh installed Luna/low then ran ONE changed existing Manager/Unix/pinnedSDK
component on [718-input graph](tmp/p3i-r4-component-inputs.json), SHA256
`93382e63abcdc8ddd8a7f703989258ef6ab25aa9fad064d20a0b3b8dc6a42b8a`,
R+eight runtime/test overlays and an independently archived actual prior-R tree
with27 verified JS inputs. PASS **Go7.819s**, command12.415s.
[Log](tmp/p3i-r4-component.log), [watcher](tmp/p3i-r4-component-watcher-result.md).
One original Goal/user/Accepted receipt/witness remains unchanged; actual SDK system
history preserves default/base/AGENTS/literal role. Fresh unload/Load via a new
Manager uses a different worker and the original saved role, no new runtime/Goal;
Configure leaves role/digest unchanged and original creation/Lookup remain exact.
Actual prior-R session/protocol/fake-worker hashes are asserted, imported unchanged
through a PID-only wrapper. Missing ACK refuses before any Goal, the original child
is reaped (Wait4 ECHILD), loaded intent/IDs stay held and replay/Load cannot replace;
no native history/submission file appears. Prior empty legacy worker still starts
without an invented digest and cannot be retrofitted. No second harness or framing
parser, real model/auth, historical repair or host Send retry was used.

All process/tool effects joined: Go33704, compile19841, pure Node73897, public
interface CLI74692 and actual component CLI63028 terminal0; original pure test
failure70886 terminal1. The final pure command75606 is joined before handoff.
No SDK fixture failure/retry/broad unchanged batch occurred. Each watcher was a
fresh installed gpt-6-luna/low/full_access utility with saved package/catalog/source
receipt, explicit danger-full-access/approval never. Native SDK scopes remain
separate and are not rerun or relabeled.

## Compatibility, review and remaining delivery

Persisted optional retained2 Instructions is deliberately unknown to old strict
readers; canonical omitted legacy stays byte-compatible. No database migration,
Goal/receipt/digest/H0/public op/utility/native3 change. Same-worker ACK prevents an
old JS worker silently ignoring the new init field. Original load intent holds
on failure; no downgrade strip/repair or already accepted Goal resend is permitted.
Production writer/capability publication still waits complete owning inventory/
predecessor guards, P2 original saved-intent transport and last metadata publication.
No ready production or owner3 codec handover follows before lead acceptance and
its explicit dependent source release.

Remaining current-package work: lead acceptance/review of the completed exact
committed receipt, then explicitly sequenced owning codec handover. No native
review wait is a dependency; requested new native fixes would retain lead priority.
No deployment, activation, ref cutover/rebase/push or session lifecycle action.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/

## Completed exact-nine commit

Actual head `8c16a2865e8ef73aeed6789b72ec99150783c093` has parent exact R
`cd5fd5cbc9670311d411466de8ec63ff670d53b0` and tree
`124c769892d91a5f40f45a37d7adb784237be7a3`. The ordinary cached-Nix
`git commit -F` temporary-message path exited0; no declared framework or active
hook exists and none was bypassed/changed. Exactly nine existing files changed,
595 additions/35 deletions. All approved/staged/index/committed/current target
hashes match, all eight runtime/test overlays equal the actual tested component
input graph, the worktree is clean and the post-index is empty. Main prose was
closed only on the new role span; removing that span reproduces original R doc
prefix/suffix bytes. Primary d3 and isolated native234 stayed exact and clean.

The post-prose [packet](tmp/p3i-r4-checkpoint.json) SHA256 is
`6f9e08b90f9ebc57ff64480e3e2b431ea3d6c2dcebb4285062958272f62140b3`;
prepared and committed [patch](tmp/p3i-r4-checkpoint.patch) SHA256 is
`32b6cde34e6bb55f0b23b03e79929d8ec26ffffad0b87fbb05b9e6d0b99a1a28`.
Original pre-prose packet/patch remain under p3i-r4-pre-prose-checkpoint.*.
[Completed receipt](tmp/p3i-r4-commit-receipt.json) SHA256 is
`b06c8a1932f05636ffb5fcae0e04b89957c9e031d8ae2edadaf9556ef857997f`.
It contains every path/hash, complete diffstat, parent/tree, format/compatibility
and effects provenance. Source/index window released in report0b28049e. No
prose-triggered SDK rerun, ref cutover, rebase, push, merge, activation or lifecycle.

Ready for lead owning-source checkpoint acceptance and independent review. The
committed owning codec is a concrete prerequisite for owner3's later validated
HasInstructions projection; it does not grant that source release or claim the
scanner/target/predecessor/P2/publication work already exists. Current capacity
and priority fix ownership remain retained until lead sequences acceptance.
