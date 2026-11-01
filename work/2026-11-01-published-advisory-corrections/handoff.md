# Advisory corrections — prepared implementation

Reviewed implementation and local acceptance are complete. Ready, awaiting merge
approval; session remains active. No production correction, retraction, deletion,
mail, credential change, deployment or default integration occurred.

Final pushed heads: API49f5a29e5a7d85559d06d31496acb5c08895bcda,
client0b771120bb2a878c012512b685208124c2b4263b,
KB5276b64b9cab0d29bc14968730eccf88c230059d and
modern1c8478bceb3943645ec06ccde895ee4b0985873f.
Modern [draft PR122](https://github.com/vpsfreecz/vpsadmin-webui/pull/122).
state.md records exact bases, final CI snapshot and any remaining hosted checks.

Full/core advisory API88/79 and client298 examples passed; modern1976 tests,
production build,10desktop/2mobile cases and all5Nix outputs passed. Final strict
KB passed453.13s and all18 real legacy Playwright cases passed (command1387.69s).
Native guests exited/destroyed with no owned runner process left. Original API
runtime-test SHA and proven identical source/derivation/bundle inputs are retained
honestly; final legacy/strict KB were executed on the exact heads above.
Independent full and affected reviews are complete with findings fixed and
consolidated whole-history/NO MIGRATIONS conclusions.

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
No shared transport/framework/generated SDK or dependency migration is introduced.

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
separate decisions. Hosted KB Managed retry status is in state.md; its first
failed unchanged process-fixture precheck remains preserved, not relabeled.

Session stays open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/
