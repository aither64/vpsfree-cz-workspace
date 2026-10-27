# Independent final review — original committed head

Reviewer report preserved by lead (retained reviewer is read-only).
Reviewer0: `gpt-6.1-sol`/`xhigh`, independent, verified ready, no overrides or
fallback, no nested reviewer. General, architecture/repetition,
scope/proportionality and risk/compatibility lanes covered. Decision: original
head NOT READY: one Blocking and two Important findings.

Exact repository:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-workspace-session-ui/dev-workspace`.
Base `b3a6eb2fc0b41cf0cb965bf4c39991815d9df734`;
head `5293cf5b3d6752e804223833a1bb9d484e55b759`.
Reviewer checked trusted binding/current slug; environment markers were absent,
consistent with portal thread binding. Initial worktree/index clean. Reviewer
used local origin/master and did not assert fresh fetch proof. In-flight fixes
are outside this original-head report.

## Findings

### R1 — Blocking — risk/compatibility and general

Recovered UNKNOWN attempts become discardable after draft detachment failure.
`app.js:313–316`, `5821–5845`, composer commit
`74a55c8ba75c784683ee8d6fa386f6a9e3f52960`.

A retained outside-buffer unresolved send/queue record is recovered with
`retry:true` when an identical draft is submitted. If `uploads.clear()` fails,
`hold(id)` unconditionally persists `state:'failed'`. Editing/Discard unsent can
then delete the original durable attempt despite possible delivery on an
older page. Zero new HTTP on the current page does not prove it was never sent.
This destroys the recovery identity and lets later work pass uncertainty.

Exact-head immutable-object/shipped-fixture reproduction: seed unresolved prior
send with attachment IDs, make clear throw, submit same draft =>
`{retry:true,state:'failed'}`; Discard unsent removes original durable/ordered/
pending ID. Correction: preserve uncertainty for recovered IDs. Only provably
fresh never-dispatched captures may become editable/discardable. Cover recovered
send/queue detach/storage failures and reload.

### R2 — Important — architecture/repetition, risk/compatibility and general

Failed-message edits orphan recovery records on partial storage failure.
`app.js:5777–5786`, same composer commit.

The revised attempt ID is stored before ordered replacement. A thrown ordered
write leaves the new never-dispatched record outside the buffer, blocking all
retries after reload. Also, ignored `removeFailedAttempt(attempt)` false after
successful replacement leaves the old original outside the buffer.

Exact-head reproduction: fresh validation-refused input, edit, allow revised
record write but throw ordered replacement => after reload two pending IDs/one
ordered entry, Retry issues zero HTTP. Reconcile ordered replacement and both
attempt records at each write/removal boundary; retire only provably safe IDs.
Use a bounded fix, no general transaction framework.

### R3 — Important — general and risk/compatibility

Fresh attachment validation refusals permanently fence later submissions.
`app.js:286–295`, same composer commit. Only literal
`message and browser attempt ID are invalid` is recognized as unsent after HTTP.

A ready attachment deleted/unavailable before dispatch produces 400
`An attachment is unavailable, incomplete or repeated` from unchanged
`portal/internal/uploads/store.go:978`; pinned codex-web
`conversation/handler.go:590–595` returns `prepareAttachments` error before
`Client.Send`. Similar fresh prompt-reference-size refusals occur before native
submission. Dispatcher leaves these unknown: immutable invalid attachment set
fails forever, no edit/discard, later entries held. Exact-head fixture: that
400/error => unknown head, discard false, second never dispatches, one HTTP.

Do not blanket-classify 4xx or prior uncertain retries as unsent. Provide a
reliable bounded fresh pre-send refusal recovery path; current pinned endpoints
expose upload refusal through ordinary status/error text. If proof cannot be
established, explicit Important disposition or minimal architect-owned contract
change is required, with affected-lane review for new contract/design. Native
behavior need not be re-proven by mocks. Existing tests omitted this case.

No additional Advisory finding. No separate concrete settings, quiet queue or
unread correctness finding: switches preserve native behavior/saves, deferred
save-handler redesign respected; queue renderer retains shared timing/rows/
Retry without new timer; unread reuses renderer/disclosure/filter state and
separates history. Real-browser checks remain pending.

## Whole-branch history, migrations and compatibility

Reviewed complete series and final diff:

- `439e33a596ab334c539271cb7ebac9e508acb564` settings.
- `4b3817f4f39e73e6012a5b3a57f7c61769a48b03` unread/cache refs.
- `74a55c8ba75c784683ee8d6fa386f6a9e3f52960` composer.
- `dedf61d843796ddb1b6d7f3bf690ddf295bab12f` quiet queue/test.
- `5293cf5b3d6752e804223833a1bb9d484e55b759` guide.

Each has coherent purpose/support/tests. No obsolete unmerged approaches,
fixup/tidy commits, transitional compatibility paths or needed consolidation in
the original series. Corrections must be folded/reassessed normally. No repeated
dependency/channel/input/generated streams or pin/lockfile changes. One shared
app.js cache advance is not a repeated dependency stream.

No migrations. No DB/server/native schema lineage changes or migrations needing
merge/release/deployed/external-use proof. Authors report no deployed feature
revision; reviewer did not invent deployment evidence. Browser schema-1 ordered
metadata is separate from legacy attempts. New browser recovers older attempts
subject to R1, pauses on reload rather than replaying. Old browsers ignore the
new key and cannot preserve new local FIFO semantics. Compatible forward
recovery matters: retain pending state and use matching new assets. Old-client/
rollback execution unvalidated. Existing server/native endpoints and pinned
codex-web `11ec57d2203fc735696fe75a837d47da55a5c6af` unchanged. Browser FIFO is
this tab's dispatch promise, not combined native execution ordering.

Architecture/scope: bounded tab/conversation dispatcher justified by click-order
and uncertain-delivery requirements, native queue/delivery/refresh ownership
stays shared. No speculative abstraction or new local-operator security boundary.
R2 is a concrete cross-record consistency gap. Remote clients remain untrusted;
no new server authentication/authorization/secret-handling surface. Guide is
discoverable from README with feature/recovery docs correctly owned there;
R1/R3 contradict its original recovery promises.

## Verification and limits

Reviewer read all relevant guidance, packet/design/state/diff/history; range
whitespace check passed. Only short Nix Node diagnostic reproductions on shipped
fixture/immutable original Git objects were run. Packet quick checks inspected,
not claimed rerun. No Chromium/package/native/CI/deployment checks by reviewer.

Remaining: authored browser tests; native multiple-steer/active-to-idle, queue
FIFO, two tabs/automatic-retry interaction as planned without broader execution
ordering guarantee; storage/attachment refusal/reload corrections directly.
Mandatory-review step 9 permits lead inspection/checks for narrow direct repairs
without blanket rerun; new design/contracts need affected-lane review.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/>.
