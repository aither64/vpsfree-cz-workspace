# Final review disposition

Review: [verbatim retained reviewer report](combined-final-review.md), delivered
by reviewer0 in the conversation because its retained read-only role forbids
writing the report. The lead preserved it without substituting a self-review.
Actual verified reviewer: thread01a16f9d-3224-70f3-b688-e9fe41ba53f1,
gpt-6.1-sol/xhigh/read_only, purpose review; no fallback or override. All four
lanes and complete four-repository histories were assessed at the report's
exact ranges. Risk classification remains high.

One Important finding, no Blocking or Advisory findings. The reviewer found no
other correctness, architecture, scope, compatibility, history, repeated pin or
migration defect. Those conclusions remain scoped to the reviewed ranges and
do not establish native or deployment acceptance.

| Finding | Decision and owner | Acceptance |
| --- | --- | --- |
| R1: contradictory late turn/item evidence can retain fresh-attempt proof | Fixed in d0fe57bed9022db526fbe90836a8576dc4e92950, owning unit c1253607. | Full nonnative/tagged compile/focused race PASS; parent and reviewer independently reconstructed all137 committed files. Affected final review finds no remaining issue. |

The lead accepts the prepared design at design.md section “Review follow-up:
late evidence must revoke ephemeral retry proof”. Validation/revocation precedes
both prior-error shortcuts and remains monotonic. Equivalent validated duplicate
failure evidence stays idempotent; changed transient error evidence is not
equivalent. Cleanup-processed evidence must affect the final issued proof through
the existing teardown/lock boundary. No new scheduler, policy option, native
patch, tool-isolation contract or persisted format is authorized.

All other reviewed sources remain frozen. Corrected dependency publication is
held for focused parent inspection; downstream pins follow only that published
revision. Retain original reviewed heads, manifests, source imports and receipts.
Consolidate the narrow fix into its logical owning client unit and refresh one
final dependency stream per downstream consumer. No obsolete interim pin should
remain in a final branch.

Apply mandatory-change-review steps9–10: inspect and verify a direct requested
narrow correction without automatically repeating independent review. If the
repair introduces new transport machinery, expands the accepted boundary or
changes a public/cross-project contract, stop for design disposition and rerun
only affected lanes with the same independent reviewer. No such expanded repair
has been accepted. Pure final generated pin changes still require exact identity,
whole-history consolidation and migration-transfer proof.

Teardown disposition accepted (e1401bec/dc9484ef): the implementation needs a
small internal reader-launch/detach change in client.go as well as the sink fix.
Add a generation-bound reader-done signal; after cleanup RPC, atomically detach
only the exact private generation under connectionMu with a narrow expected-close
branch. Skip only its synthetic transport failure. An unexpected disconnect that
wins before the cutoff retains ordinary failure behavior. CloseNow runs outside
locks, already-read frames finish validation, and the helper joins the reader
only within the existing cleanup deadline before sampling final proof under the
sink mutex. No matching reader, timeout or cleanup failure means no retry.
Public Close, reconnect policy and shared-client behavior remain unchanged.

The complete architect subsection “R1 teardown disposition — released bounded
implementation” is now durable and read by lead. Implementation is released
after owner0 reads it (7ea5ecdf). Focused deterministic race verification is
required; uncertain instrumented compilation is assigned to a fresh watcher. This adds an internal lifetime/locking
implementation beyond the original reviewed sink-only path. Therefore step10
applies: after complete intended repair is committed and quick checks pass,
assign the same independent reviewer affected general, architecture/repetition
and risk/compatibility lanes, including ordinary Close/disconnect regression.
The prior scope/product-contract conclusion remains applicable; no public
contract, scheduler, tool policy or native patch is added. No early/advisory review
is requested, and no publication precedes this affected final review.

Original preservation evidence that client.go matched8b605 remains historical
and accurate for reviewed975. The repair must explicitly document its narrow new
client.go delta and prove unrelated SQLite/writers/readers unchanged. Consumer
and runtime sources remain frozen until corrected dependency publication.

Native/state/provider acceptance, exact system/profile builds and copies, idle
cutover and live verification remain unreleased. No default integration or
session lifecycle action is authorized.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/)

## Accepted affected final review

Same retained reviewer0 completed the required affected general, architecture
and risk review at exactd0fe57bed9022db526fbe90836a8576dc4e92950, tree
5e232c202077efd4c75d602abca28da12ac167d1. R1 is resolved; no Blocking, Important
or Advisory finding. Lead preserved the message verbatim in
[r1-affected-final-review.md](r1-affected-final-review.md). Actual identity/thread,
model/effort/access were reverified, no fallback/overrides or nested reviewers.
The internal reader lifetime/locking, ordinary Close factoring, test barriers
and complete final history/preservation were explicitly assessed.

Client publication is released df60765b with fresh exactdefault/old975 lease
checks. Runtime mechanical pin/module/vendor refresh is conditionally released
95e8d58f only after exactclientpublication and actual Go sums. No source policy,
API, native or catalog change is authorized by the refresh. Retain old/new reviewed
ranges and consolidate each final stream; prove generated/mechanical transfer
and unchanged source before final verification. No blanket product rereview is
needed for proven mechanical pin transfer. Any substantive departure returns to
design and affected review.

Native/provider/state-runtime/browser/creation and final assembly/build/copy/idle
activation gates remain pending; this review closure supplies no merge, machine
claim, deployment or lifecycle action.
