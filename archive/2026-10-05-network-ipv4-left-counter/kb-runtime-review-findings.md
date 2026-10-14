# Portable tooling review findings

Original committed review is complete on K93a16d6, D51aba080 and Ed2079f6,
with two Important K findings and no additional D/E findings. Both corrections
now pass focused and canonical checks and are published at K68aa33b. The new
descriptor handoff awaits affected-lane committed review after E's pin refresh.
The original review remains tied to its original snapshots.

## Important: output lock loss does not cancel capture

Reviewer0 GENERAL and risk/compatibility lanes identified K runner/capture.cjs
30-31,59-76,81: the artifactLease signal/assertLive is ignored after acquisition.
The cluster lease alone gates remote actions/publication. Loss of the artifact
controller releases flock while the old capture can still publish its retained
result snapshot and overwrite a competing writer. Root inspected the source
and accepted the finding. No runtime reproduction is claimed by the reviewer.

Assigned implementer0 the narrow combined-liveness/cancellation and publication
fix, with an actual controller-loss/competing-writer capture regression in the
declared Nix environment. Checked physical serialization also retains the
writer's copy of the same flocked open file description through final cleanup.
Focused evidence and final K commit equality are in kb-runtime-review-fix-result.md.
No long package/VM checks may begin before the affected review gate.

## Important: changed SSH endpoint fails only after shutdown

Reviewer0 GENERAL and risk/compatibility lanes identified original K
cluster/lib/kb_runtime.rb199-209 and510-522. Compatibility admits changed SSH
host/port, while retained known_hosts must match scanned lines byte for byte.
Even unchanged guest keys acquire a different host/port prefix, so readiness
fails after predecessor stop. Existing runtime tests override trust entirely.
Root confirmed and selected the bounded rejection path: compare resolved
per-machine SSH host/port during preflight, before journaling/import/stop effects.
Do not rewrite retained trust or introduce endpoint-update support.

Host/port rejection and real trust-boundary coverage pass: three changed-endpoint
preflights preserve the predecessor, and the real trust method accepts the same
endpoint/key while refusing changed prefixes or keys. Same-endpoint compatible
source updates remain supported. Root verified this narrow fix under skill step 9.

Root reconciled the owning update contract directly: updates retain resolved
SSH hosts/ports because existing host-key trust is not rebound. The final doc
bytes are frozen in the authoritative kb-runtime-review-fix-doc2.sha256 and
committed with the checked behavior. Earlier doc/packet receipts remain historical.

## Accepted lock-lifetime clarification

Architect0 inspected committed K93 and confirmed that async cancellation alone
leaves an unobservable interval during synchronous publication. Root accepted
the design.md:1998 retained-descriptor boundary: Node safely opens the persistent
lock and shares that same open file description only with the fixed helper.
Both copies close without LOCK_UN; the writer closes last after cleanup.
Known-loss cancellation remains required. This introduces no schema or D/E
protocol changes, but its new physical ownership plumbing needs affected-lane
committed review under skill step 10.

The provisional quick1 is honestly unlaunched and preparation-only. A new packet
proved physical exclusion when helper death occurs while the writer event
loop cannot process cancellation, plus endpoint preflight and real trust tests.
Root's updated contract prose is frozen in kb-runtime-review-fix-doc2.sha256.
