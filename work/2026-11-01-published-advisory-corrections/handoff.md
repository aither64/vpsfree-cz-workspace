# Advisory corrections — merge preparation

**Ready, awaiting merge approval.** Implementation, independent review, required
local acceptance, final source/input/cleanup proof and all five freshness checks
are complete. PR122 is ready; no further tests or source changes are selected. Nothing
has been merged into a default branch or deployed to production.

| Repository / target | Published feature head |
| --- | --- |
| vpsadmin / master | `942c6eaed41331f823d8e0f670ed239e2b308440` |
| security-advisories / 2026-07-13-security-advisory-automation | `0b771120bb2a878c012512b685208124c2b4263b` |
| vpsfree-kb-contracts / master | `f97785c2c265172a4c78893e0673034fde56e4dd` |
| vpsadmin-webui / main | `1c8478bceb3943645ec06ccde895ee4b0985873f` |
| vpsfree-cz-configuration / master | `c4107822060e9e34b24a83950d618c9f28a7722b` |

API preserves HaveAPI0.32.2 master5586 and has three logical commits: advisory
API, legacy advisory management, independent VPS return-navigation fix with
its owning regression. KB has one final API pin plus unchanged readiness helper;
configuration has one generated Services pin over0d71. Both select942c with
matching NAR. No migrations, obsolete implementation/fixup or repeated pin stream
remains. Old reviewed/deployed heads remain evidence refs, not literal ancestry.

[Independent affected review](admin-pagination-final-review.md) returned no
Blocking/Important/Advisory findings, including whole histories/no migrations,
assertion order, complete pin graphs and actual consumed-input reuse. It reuses
[prior navigation/HaveAPI conclusions](navigation-haveapi-final-review.md) at their
proven boundaries. The one-line admin test repair follows actual success and
canonical URL assertions, then reopens the filtered list for row observation;
it cannot hide wrong-Overview navigation. RuntimeC/auth/headers/timeouts unchanged.

Strict finalKBf977 passed509.55s. Admin-core on942c passed all3serial browsercases
(no failures/skips), nativeexpected_success; wrapper1299.84s/wholebatch2747.17s.
Only admin and strict ran in the final batch, under one verified restricted
Luna/low utility. Actual2823 services-up34, user-core4 and lifecycle3 passes are
retained under independently checked runtime/helper/selected-script/input reuse,
without claiming whole Playwright bundle or guest derivation equality. Hosted
API41544311588 all26topics+aggregate and actual0.32.2 environments likewise apply
through unchanged Ruby/API input proof. Earlier KVM stays at its stated sources.

Normal hooks/quick checks, KB zero drift and config graph/mapping/representative
evaluation passed. Ambient Overcommit0.71 prepush failure was recovered in declared
Nix0.74 without signing/bypass/recommit. Earlier runner-path setup failure was
resolved with short socket paths; original failures and utility provenance limits
remain retained. Original missing-count/password-lock causes remain UNKNOWN.

Final modern/client/config snapshot03:14:07Z confirms clean published heads and
unchanged ancestor defaults. Modern/client CI passed; config has no hosted runs,
with normal local hooks/evaluation recorded. PR122 is ready/MERGEABLE/CLEAN at
03:14:45.924716Z; only its approved terminal status sentence changed. Final API/KB SSH heads/defaults are exact/clean/ancestor, matching the reviewed
ranges. Final actual guest graph6656 binds2958matching runtime blobs and the
correct942c admin bundle; machine logs terminal/native PID gone, two retained
virtiofs pidfiles reference nonexistent processes. Preflight socket64bytes,
maximum observed path68bytes, below108limit.

Latest API942c CI41563874916 is queued; PHPUnit/i18n passed. KBf977 Check passed;
Managed41564405472 is in progress. Old2823 integration is completed/cancelled.
These pending current runs are not called green, and no broad wait/campaign is
selected. Any new actual failure needs disposition before integration.

DEV preview stays running: backendAPIa38c/modern1c, synthetic data intact;
host-mounted PHP reads unchanged runtimeC from942c without another activation.
Credentials remain in portal Cluster fields. Config's separate modern70bd source
is unchanged; the API channel does not select/deploy modern1c. No preview fixture
writes, restart, backend update or session lifecycle action is authorized.

Next: explicit integration direction for the repository/target set above. Each
approved merge still needs a fresh target/head/history check; material changes
require the appropriate refreshed verification and review. Future production
rollout needs compatible UI/API pairs, every active six-guard sync client and no
mixed API pool. Full hashes/bases/results and prepared recovery constraints are
in [state.md](state.md), [owner evidence](visibility-verification.md) and
[configuration receipt](config-channel-update.md). Keep the session open.

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

Session stays open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/
