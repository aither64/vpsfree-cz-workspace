# Corrected portable KB review packet (draft)

Do not assign this draft before the E exact-pin checks and normal consolidation
are complete. The final packet must replace the pending E head below.

The user authorized implementing portable KB tooling that also works outside
this workspace, plus an optional workspace adapter. All project branches remain
feature-only; activation, production KB writes and default integration are outside
this work. Read the accepted design, especially its artifact-lock clarification
at design.md:1998 and the original kb-runtime-review-result.md.

K base873758fd6aec0c03f50a94600e0ceab97946f255 ->
68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e is clean, published and canonically
checked. Complete binary diff/history/ref inventory is kb-runtime-remediated-k.*.
The series is unchanged pin a50f8c1a followed by the coupled runtime/capture
commit68aa33b. Its checked correction is exactly the original93-to-final diff,
with no leftover fixup. The old runtime93 is superseded, not an additional commit.
No database migrations or state/connection schema changes were added. Legacy
state remains recreate-only; no activation/release/production consumption is
established, and absence of external use is not inferred from local refs.

D basea2bbf2f1c588de7eec0d7d52580a89a9d4bef984 ->
51aba080b264c28f5584867b6cf006bf423ae2f3 is unchanged from the completed review.
Retain its transport/deadline review and exact fast CI evidence. E's original
base is0ff827df13e82dfab4b536ff29979280f264e8f5; final head is pending mechanical
K pin refresh and input-stream consolidation. Preserve its provider behavior,
D51 pin, complete graphs and existing follows. No DB migrations in D or E.

Original finding1 is corrected through a new physical handoff: the writing Node
process retains the same open file description flocked by its fixed Ruby helper,
with fd3 only to that helper and close-only last-close release after all capture
cleanup. Cancellation prevents work after known loss; physical retention covers
synchronous publication before an event loop observes loss. Validator writer
inheritance remains intact. This warrants skill step10 affected-lane review.

Original finding2 is corrected by refusing changed resolved SSH host/port before
candidate/journal/build/import/stop effects. Trust is not rebound. Root inspected
this scope reduction and verified three retained-state preservation cases plus
actual establish_ssh_trust with only keyscan mocked under skill step9. Include
its interaction with the final K tree without reopening unchanged lifecycle design.

Overall risk remains HIGH. Select the same independent reviewer0 at retained
Sol/xhigh/read_only, no model/effort override or nested reviewers. General,
architecture/repetition, scope/proportionality and risk/compatibility apply to
K's physical handoff and actual E pin composition. Do not rerun unaffected D/E
implementation lanes merely to repeat the completed review.

Evidence: focused quick2 has29 native Node cases and runtime24/159, zero failure,
error or skip. Actual-main synchronous PNG-rename blocking plus real helper death
keeps an independent capture excluded through browser cleanup/final close.
Other cases cover normal/abnormal helper exit, writer/wrapper death, no unrelated
FD inheritance, pending/window/known-loss cancellation and bilingual merge.
Canonical K68 bin/check0 includes closure12/51, pinned driver4/20, export4/18,
source/profile/rendered syntax and strict60concepts/120variants/120PNGs. The new
immutable runtime-source receipt and all54 extant changed blobs match Git.

E affected SDK/public exact-pair results, consolidated history, staged/expected
final-tree proof, final lock graph and clean-head derivation evaluation are
pending. Historical39/273 local evidence certifies K93 pairing only. No mocked
browser/guest fixture certifies real SSH, closure import, rendered images or
installation. Real standalone four-selector and two-image proof remains after
accepted review, bounded package outputs and fresh host capacity/nested KVM.

Owning explanatory docs are K cluster/runtime-contract.md (root doc2) plus its
README/cluster workflow and E README/dev-clusters/kb/README.md; E docs are unchanged.
No generic lock framework, new state schema, input overrides or workspace
requirement was added to K. Managed E/D retain their public mediated lease route.
Already-issued filesystem/remote operations are not rolled back on lease loss.
