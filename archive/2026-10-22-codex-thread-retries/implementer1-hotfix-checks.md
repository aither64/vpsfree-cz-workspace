# B emergency retention hotfix — owner verification

Final published source: `ed2a75b98a75f9b37b7a359e9091a94e9846644e`,
tree `63eba6140c340d28f38c39b010d0a5b2874b7680`. Independent full review covered570;
lead requested narrow H1 and test-only fixture corrections, recorded below.
Deployed supported predecessor: `d819ad044ef7fcc7bb4a111dc7676fe251383249`.
Original base: `bf6d4b0c49600c15e17fe71248807ef43424e932`.
The original four commits remain exact ancestors; one emergency successor was
appended. A remains pinned to `c1f415ad5602c23e6443cced73cb59267a796f05`.
No schema migration, capability, native protocol, API, UI, Nix or dependency
change is included. The original bundle, history, diff and candidate receipt
are retained alongside this record.

All commands below ran from the B worktree through
`nix develop --command bash -c`, with `cd portal` and `TMPDIR=/tmp`.
Go tests use `-mod=readonly`. No native, packaged, deployment or CI wait was run.

| Scope | Exact Go command | Result and artifact |
| --- | --- | --- |
| New focused cases | `go test -mod=readonly ./internal/turnretry ./internal/workspacecodex -run 'Test(Retention.*|RetryRetention.*)$' -count=1 -v` | PASS core0.241s, wrapper43.774s; `implementer1-hotfix-focused-4.log` |
| Full core races | `go test -mod=readonly -race ./internal/turnretry -count=1` | PASS7.637s; `implementer1-hotfix-race-core.log` |
| Admission races | `go test -mod=readonly -race ./internal/turnretry ./internal/workspacecodex -run 'Test(Retention.*|RetryRetention(Managed.*|Protected.*|Crash.*))$' -count=1 -v` | Core2.787s PASS; protected FIFO19.28s and four crash/save cases62.05s PASS. Replay fixture failed from expired context; preserved `implementer1-hotfix-race-admission.log`. |
| Controller and managed fences | `go test -mod=readonly -race ./internal/workspacecodex ./internal/web -run 'Test(RetryRetention(Cached.*|Aggregate.*|Unknown.*)|Retry(Loaded.*|Managed.*|Queue.*|Proof.*|Steer.*|Settings.*|Warm.*)|TurnRetry.*)$' -count=1 -v` | PASS wrapper88.445s/web7.346s; `implementer1-hotfix-race-controller-corrected.log` |
| Corrected original-identity replay | `go test -mod=readonly -race ./internal/workspacecodex -run '^TestRetryRetentionManagedSteersBeyond64AndExactReplay$' -count=1 -v` | PASS37.185s; `implementer1-hotfix-race-replay-corrected.log` |
| Proof/result encoded byte budgets | `go test -mod=readonly -race ./internal/turnretry -run '^TestRetentionProofAndAcceptedReceiptByteBudget$' -count=1 -v` | PASS1.503s; `implementer1-hotfix-race-byte-budget.log` |

The admission race failure was diagnosed before rerun: the replay timeout began
before 69 durable sends, whose setup takes roughly17s under races. It now starts
at the replay phase. Changed tuple assertions also require the actual generic
identity-reuse error, so deadline errors cannot count as identity rejection.
Earlier focused fixture errors were explicit empty-vs-null item data, repeated
synthetic item IDs, and an idle owner path incorrectly treated as an implicit
settings resume. The fixtures now model the supported wire shape and admit the
independent queue while the warm source turn remains active. A malformed Go
selector using negative lookahead failed before testing and was replaced by
explicit supported selectors. All original failure logs remain preserved.

Root and retained-member production wrappers each deliver69 distinct steers
from the deployed64-bound shape. Exact original accepted replay, restart and
browser acknowledgment/history recovery leave native send count69 and retained
snapshot count64. Changed text/action/options are rejected. The production
unknown-automatic fixture retains64 protected entries and settles its exact
receipt across active and failed restarts with native count2: one manual source,
one automatic continuation, zero repeats. Unit cases also prove no reanchor or
rearming when space later becomes available, conflicting receipt rejection,
positive-unsubmitted preflight refusal, byte pressure and persistence failure.

All final production blobs were exercised by the race matrix. Later changes
only strengthened fixture synchronization, replay timeout placement/assertions,
and added the byte regression, each checked by its focused selector. No
production edit followed the matrix. Focused race runtime exceeded the initial
nonrace estimate; the parent retained its already-owned tool handles through
completion instead of relaunching or abandoning them.

Review is in progress at exact570. Lead requested a narrow follow-up retaining
the known-unsubmitted Pending tuple on blocked preflight refusal. Source remains
frozen until the reviewer completes this disposition. That correction will be
folded only into the unmerged successor; deployed d819 stays unchanged.

SSH publication was verified at570 and the source is clean. CI snapshot:
`39974175490`, attempt1, current570 `in_progress`; all superseded runs in the
bounded branch query were completed. Current CI was neither waited on nor
cancelled. See `implementer1-hotfix-ci-snapshot.json`.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/

## Final H1 remediation

Final published B `5a5583ae7559bb038e6c8c684a6484d425d11e64`, tree
`453e12d9a216c9fb98a3b385e33721d12dfd4f6d`. The exact570 review found only
H1. Lead released the narrow correction: retain the known-unsubmitted Pending
tuple when receipt preflight is blocked. The final diff against570 changes only
that assignment and strengthens the existing unit check to compare the complete
pending tuple, reload, and call a fresh controller twice with the same failure.
The tuple keeps its empty ResultTurn and ChargedAtMS; native sends and quota
remain unchanged. No new eligibility or admission path was introduced.

Focused command `go test -mod=readonly ./internal/turnretry -run
'^TestRetentionFreshAutomaticPreflightAndReceiptSaveFailure$' -count=1 -v`
PASS0.185s; the same selector with `-race` PASS1.981s. Full log:
`implementer1-hotfix-h1-quick-race.log`. Original570 bundle, receipt, metadata,
patch and old/new range-diff are retained. Only the unmerged successor was
amended; deployed d819 and the original four commits are unchanged.

Published source metadata: `/nix/store/nmvdiviyyzg7y0gknp0wki5gw7s01xd8-source`,
NAR `sha256-qwSe/j1j7uQSX/OcDER3pov8xZ8Tp67PKmbmzKBso/Q=`,
lastModified1792768211, revCount564. See `implementer1-hotfix-source-metadata.json`.
Source clean, SSH remote exact. Final CI39975956680 attempt1 was in progress
on the one-shot snapshot. Superseded570 CI39974175490 completed failure;
bounded failed-job evidence diagnosis is in progress without rerun or source
mutation. No superseded active run required cancellation.

## Final fixture correction and publication

The superseded570 CI failure was diagnosed from all three full failed-job logs.
The notification fake omitted supported thread/items/list, which exact generic
reconciliation now calls. Lead released the two-line empty-page fixture response;
all delivery/settings/count/owner assertions remain unchanged. Exact selector
normal0.184s and race1.485s PASS both active=false and active=true. Complete log:
implementer1-hotfix-coordination-fixture-quick-race.log. See the separate compact
CI diagnosis and complete preserved original logs.

Final source ed2a75b, tree63eba614, remains one hotfix successor after deployed
d819. Full five-commit inventory and final nine-file delta are captured in
implementer1-hotfix-final.json and implementer1-hotfix-final-history.txt. Original
four deployed commits, reviewed570 and intermediate5a receipts/bundles/ranges
remain preserved. Exact source NAR is
sha256-sC3xe3YlpNRPhskCyfdwj1BBA1J9boKdfwGELZtHnYs=, lastModified1792768595,
revCount564, /nix/store/all1xk9s94zdhbjks4wmwjz8ax4lwhc9-source. Remote SSH receipt
matches, source clean/frozen, A and Nix/module pins unchanged.

Current ed2 CI39976880008 attempt1 in progress on the bounded snapshot.
Cancellation of superseded5a39975956680 was rejected HTTP403; no credential
workaround or current-head cancellation. No CI wait/native/build/deployment.
Lead retains final step9 inspection and subsequent verification/deployment gates.
