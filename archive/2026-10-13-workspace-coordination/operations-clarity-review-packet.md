# Final Operations clarity review packet

Initiative: 2026-10-13-workspace-coordination, workspace
/home/aither/workspace/ai/vpsfree.cz. Review all four mandatory lanes directly,
read-only, without nested agents. Read mandatory-change-review/SKILL.md and every
lane reference, root procedures, and affected local AGENTS before reviewing.

Reviewer: retained independent /root/coordination_confctl_review, GPT-6 Astra,
xhigh, read-only; same coherent coordination change. Installed policy at
/nix/store/6wr3fhkz63gdmks3xi20h3h940mlbcvd-dev-workspace-0.2.0/share/dev-workspace/agent-teams.json
selects lead_reviewed/reviewer as standalone fallback. No session roster exists.
The earlier native review and remediation are in operations-review-retained.md.
Confirm retained native identity/settings remain as recorded; report any mismatch.

Requested behavior: Operations above Automatic archival; readable reserved-machine
cards, Running and waiting table, Recent results table; active and completed jobs.
AITHERDEV RESERVED or distinct machine count badges with machine/status tooltip;
session Reservations between Clusters and Artifacts; incarnation-specific history.
Preserve focus and disclosure across refresh; stop hidden/tab-inactive reads;
retain last successful status with warning. Dates use local browser time and
Time unavailable when unknown. Machine hold continues throughout user review.

Complete four-repository series, base/head, final patches, range-diffs, previous
deployed heads and explicit no-migration provenance are in
operations-clarity-inventory.json. Inspect that complete inventory, not just the
last commit. Plan/state/design are alongside this packet. The approved revision
is at the end of design.md. Core coordination is unchanged by this follow-up.

Commit disposition: superseded flat portal rendering and all narrow UI fixes
are folded into the portal commit. Optional timing persistence/projection and its
packaging/tests/docs are independently reviewable in a third runtime commit.
Workspace direct nested runtime selection is one final input commit preserving
extension c697acc7 and sibling inputs. Configuration dev-workspace/devWorkspace
is one final generated confctl update, regenerated against its original input
so the complete generated changelog is preserved. No redundant intermediate pin
updates remain. Previous deployed exact refs and closure roots remain retained;
deployment alone does not justify retaining intermediate pin commits.

Risk: high because the full deliverable coordinates Git and live system/profile
activation, uses persistent authority, and spans mixed package generations. The
UI follow-up adds optional persisted timing metadata. All four review lanes apply.
Local operator is trusted per runtime AGENTS; remote clients remain untrusted.

Timing contract: ledger first, timing sidecar second under the existing mutex.
UUID/revision/state must match for dates to appear; absent/corrupt/stale/unwritable
metadata affects dates only. No authority schema/history, worker envelopes,
receipts, compatibility contract, scheduler, approval or ownership changes.
Old package ignores the sidecar; predecessor writes invalidate stale dates.
No backfill, rollback machinery, mutation controls or release-policy expansion.

Quick verification before review: Node browser 9/9 in
operations-clarity-browser-final.log; focused Ruby 8/76 in
operations-clarity-quick-final.log; Go focused OperationsNavigation,
ReservationCards and AutomaticArchival pass in operations-clarity-go-corrected.log
with the documented absent provider catalog. Initial test failures are retained;
Minitest mock dependency removed, projection assertion updated, stale autofocus
expectation fixed. git diff --check passes. Final consumer composition passes in
operations-clarity-composition.log. Configuration hooks pass without bypass.
Long integration/package/system tests have not started for this revision.

Owning component: generic dev-workspace owns authoritative coordination and portal
status/rendering. Consumers: vpsFree extension adapter c697acc7; workspace package
via direct nested runtime override; configuration selects matching host module.
No codex-web source change. Inspect imports, manifests, locks and current consumer
branches to validate this rather than relying solely on this description.

Docs: runtime docs/coordination.md explains dashboard, badge/tab, date semantics,
predecessor overlap and failure behavior; README links it. Existing runtime
coordination-operations.md, workspace docs/coordination.md and configuration
coordinated-deployment docs retain operational contracts. Individual rollout
revisions/evidence belong in rollout.md and operations-* artifacts.

Deployment authorized to aitherdev through feature configuration, then user
profile. Retained threadless synchronous bootstrap machine/profile pair reuses
reservation d114323d-806c-479f-b7a4-8c1a08afb45b. No reboot, integration, reservation
release or session closure. Merges remain paused after the user's wait.

Return ordered concrete findings by severity/lane with file and commit references.
Explicitly conclude whole-branch history/consolidation and migration lineage.
Record residual verification gaps; a final report may be written to
operations-clarity-review.md in this tracking directory (evidence only).

## Narrow CI fixture correction during review

CI run 38455974923 at 790544ae failed only because the existing session-sidebar
test expected Automatic archival autofocus. The index version was already
corrected; this equivalent session fixture now expects Operations autofocus.
No production code changed. Corrected focused session/sidebar/page/card/archival
Go checks pass in operations-clarity-go-corrected-final.log. Runtime is now
62a1b4cfd7ea3ca613b95a248b3968f846ab4519; the one-line test change is folded into
portal e1f70e97. Consumers are being repinned and consolidated; inventory follows.
