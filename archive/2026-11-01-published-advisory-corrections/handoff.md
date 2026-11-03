# Advisory corrections — merged; devcluster released

**All five reviewed branches are merged into their approved remote targets.**
PR122 auto-merged. Normal fast-forward merges, hooks, SSH pushes, exact remote
verification and all claim releases passed. The explicitly requested devcluster
Stop and full Release also passed; final status is foundfalse. No production
deployment or session archive/delete/stop occurred. Feature refs and records remain.

| Repository / target | Exact integrated head |
| --- | --- |
| vpsadmin / master | `942c6eaed41331f823d8e0f670ed239e2b308440` |
| security-advisories / 2026-07-13-security-advisory-automation | `0b771120bb2a878c012512b685208124c2b4263b` |
| vpsfree-kb-contracts / master | `f97785c2c265172a4c78893e0673034fde56e4dd` |
| vpsadmin-webui / main | `1c8478bceb3943645ec06ccde895ee4b0985873f` |
| vpsfree-cz-configuration / master | `c4107822060e9e34b24a83950d618c9f28a7722b` |

User approved “merge” for this set and “also stop & release the devcluster”.
The public provider implements full Release through reset after stop; both exited0,
with stopped/readyfalse then foundfalse. Preview disks/configuration were removed
as requested. Session/worktrees/refs and shared provider infrastructure remain.
The previous backendAPIa38c/modern1c/livePHP preview is historical, no longer running.

[Merge/release verification](merge-verification.md) retains exact claims/times,
remote head proof, hooks, package/observer policy and postmerge CI IDs.
[Independent final review](admin-pagination-final-review.md) found no Blocking,
Important or Advisory issue; histories/consolidation/NO MIGRATIONS verified.
No rebase or source change was needed at integration. StrictKBf977 passed509.55s;
admin-core942c all3browsercases passed, no failures/skips. Services34/user4/
lifecycle3/API26+aggregate passes are reused only with reviewed actual-input
proof; no whole Playwright bundle/guest equivalence is claimed.

API's three logical commits preserve the HaveAPI0.32.2 baseline. KB has one final
pin plus unchanged helper; config one generated Services pin, both select942c.
Other graph/OS/content/capture sources remain. Original missingcount/passwordlock
causes and duplicate-utility provenance limits remain explicit. Original KBManaged
UFW failed on Ubuntu mirror package setup before firewall assertions; user accepted
it as out of scope and the proposed follow-up never launched. It remains a failed
hosted attempt, not a retrospective green or flake claim.

One postmerge snapshot: clientRSpec/RuboCop SUCCESS; API RuboCop/PHPUnit/i18n
SUCCESS, broader CI running/API Specs queued; KBManaged running/Check queued;
modernCI/smoke/broad queued. Config has no hosted run. These new runs are not
assumed green; premerge review and accepted exact/scoped validation remain.
No new test campaign, retry or broad CI wait selected.

Merge/release request is complete. The session stays open; no integration claim
or uncertain owned command remains. Production deployment is a separate decision.
Config's modern70bd pin remains; merging API Services does not deploy modern1c.
Future writes require compatible UI/API pairs, every active six-guard sync
consumer and no mixed API pool. Interfaces and recovery constraints follow;
full source/input evidence is in [state.md](state.md) and linked owner receipts.

## API interface and validation

Existing authorized parent PUT edits name, localized summary/description/response
and publication time in draft, published or retracted state. Time may change or
clear without changing state; blank time remains blank and list ordering falls
back to creation time. Existing CVE create/update/delete and nested node-status
create/update/delete correct the same states; zero CVE links/missing node rows are
valid. Existing normalized CVE format, uniqueness, node scope and timestamp rules
remain. Published/retracted node create/update must be resolved, with both times
for mitigated. Existing retired rows can be removed.

Every correction requires expected_content_revision. Optional expected_state
(draft/published/retracted) is an intent precondition checked under the same parent
lock. Mismatch returns409 without changes. One successful mutation advances the
revision once. Original corrections preserve advisory identity/state/authorship
and existing update history; they never mail, republish, reset/create an advisory
or automatically append an announcement.

Published/retracted node membership or conclusion changes atomically rebuild
stored affected VPS/user projections and counts. The existing snapshot uses
current active/suspended VPSes and current ownership on mitigated nodes, not
reconstructed historical placement. Row/notes/projections/revision roll back
together on failure, including inside an outer transaction. Manual rebuild uses
the same parent lock. UI child saves remain separate requests: earlier successful
writes survive a later failed request, and both UIs stop rather than blindly retry.

Explicit new admin actions:

| Action | Interface | Semantics |
| --- | --- | --- |
| Retract | POST /security_advisories/:id/retract | Published only; silent; keeps report/history/projections; one retraction timestamp/revision |
| Delete | DELETE /security_advisories/:id | Any existing state; silent transactional owned cascade; repeated success then404 |

Both use the ordinary security_advisory JSON wrapper, expected revision and
optional expected state. New scopes security_advisory#retract and
security_advisory#delete are not automatically granted to existing tokens.
Deletion removes original/update translations, posts, CVE/node rows/notes,
projections and outage links. It preserves referenced users/nodes/VPSes/outages,
other infrastructure, transaction concerns and mail/log history. Recovery needs
an existing backup; software rollback cannot restore deleted content.

Publish is explicitly draft-only, preserving its unchanged-revision successful
publication/recovery contract. Separate security_advisory_updates retains its
explicit state/time changes and mail choice as the announcement mechanism.

## UIs and draft-sync safety

Legacy PHP and modern React use captured state/revision and sequential relation
writes. They support precise/null dates, empty CVE edits, explicit node add/remove,
localized notes and confirmed silent retract/delete. Missing partial fields do
not implicitly remove or recreate rows. Failed/uncertain forms retain input and
require explicit reload/review. Public/admin isolation and announcements remain.

The companion client remains draft-only. Before applying any write it checks
expected-state support on all SIX used action types, then sends draft on parent
Update, CVE Create/Delete and node Create/Update/Delete. Missing/malformed/denied
capability stops before writes; no fallback or removed guard. Existing source,
evaluation/digest/revision/checkpoint/publication recovery checks remain.
Read-only/dry-run commands stay available.

Actual HaveAPI metadata includes labeled choice maps; machine keys identify
states. Root OPTIONS is authenticated capability evidence, not record-specific
permission: endpoint preparation and write authorization/locking remain decisive.
No shared transport/framework/generated SDK change is introduced by the feature.
The refreshed API baseline selects HaveAPI 0.32.2 under the reviewed compatibility
and actual-input verification boundary.

## Compatibility and rollout requirements (not executed)

Pause sync during rollout. Upgrade all active sync clients, complete the API
rollout and use compatible UI/API versions before enabling writes; mixed API
pools are unsupported. Old unguarded UI/client versions are not safe admin-write
rollback partners. New affected writes fail closed on older APIs while reading
remains usable. No schema/data conversion, daemon protocol or OS coordination.
Software rollback leaves intentional corrections/retraction intact; deleted
content needs backup recovery.

Client source/spec patch was checked against public source-session feature
33f253a; docs need manual placement retaining its unrelated scope/history text.
No peer checkout/credentials were accessed and no feature history integrated.
Modern UI uses its required isolated dev/... branch and focused draft PR. Its
current-main rebase preserves intervening colleagues' release; exact source/input
and range evidence belongs in implementer1.md.

## Evidence and next operator action

- design.md: authoritative expanded A/B/C/E behavior and verification packages.
- package-a-expanded.md and metadata-labels.md: exact API/pin histories, savepoint
  and real-metadata CI diagnoses, hooks, equivalence and remote proofs.
- implementer1.md: client/legacy/modern source, checks, rebase and PR evidence.
- final-review.md and review-reconciliation.md: completed expanded independent
  review and accepted narrow fixes, with original and successor ranges retained.
- refresh-review.md and fixture-rebase.md: independently assessed HaveAPI0.32.1
  baseline, folded fixture correction and refreshed exact KB pin; no new findings.
- modern-verification.md: exact1c847 full unit/build/desktop/mobile/package checks
  passed; complete source/input/derivation receipts retained.
- api-acceptance.md: full88/core79 API and298 client examples passed, strict
  prior-pin KB passed, inventory correction and identical-input reuse evidence;
  final exact pin/browser acceptance and native cleanup are recorded.
- layout-final-review.md and readiness-final-review.md: independent affected
  reviews of observed legacy readiness and form-layout corrections, no findings.
- verification-brief.md: completed bounded acceptance command scope.
- react-screenshots/: synthetic implemented desktop/mobile cs/en captures; no
  production data or backend atomicity/mail/cascade claim from screenshots.

Any integration requires explicit direction naming repository and target. The
actual client default is 2026-07-13-security-advisory-automation; other defaults
are API/KB master and modern main. Deployment and production corrections remain
separate decisions. Historical KB Managed/process-fixture failures and their later source-scoped
outcomes remain in state.md and the linked owner receipts; they are not relabeled
as final HaveAPI 0.32.2 execution.

Session remains open; devcluster has been stopped and fully released:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/
