# Expanded FINAL committed-deliverable review packet

All intended A/B/C/D/E changes are committed, worktrees clean, quick checks pass.
This is a NEW final review before longer manual acceptance/build suites. Earlier
paused review/interim report does not certify these ranges. Full exact inventory
below; no further source change pending.

## User scope and acceptance

Original request: authorized corrections to published original advisory text and
node conclusions, no email/republish/reset/new advisory/automatic update; preserve
scopes, optimistic revision, update history and coherent stored user/VPS counts.
Explicit later direction: include CVE corrections and adding/removing node rows,
editable publication time, retract/delete, and vpsadmin-webui changes as needed.
No production data/credentials/deployment/default integration/session cleanup.

Current accepted behavior (full design at top of design.md):

- Existing parent/CVE/node CRUD correct draft, published and retracted reports.
  Publication time may change/clear; zero CVEs or missing node rows are valid.
  Node create/update keeps existing resolved-state/time/scope rules outside draft;
  removal supports retired rows. Omitted fields/languages preserved.
- Every correction requires expected_content_revision and accepts expected_state
  under the parent lock, increments once; published/retracted node CRUD atomically
  refreshes current affected VPS/users/counts. Manual rebuild shares that lock.
- Explicit admin POST /:id/retract: published only, silent, once timestamp/revision,
  preserves report/history/projections. Explicit parent DELETE: any state,
  guarded transactional owned cascade; repeated success then404; referenced
  nodes/VPS/users/outages/environments/locations/mail/logs survive. Backup needed
  to recover deleted content. No production deletion is authorized.
- Publish draft-only under lock, unchanged-revision successful publication/recovery
  retained; cannot republish/refill cleared time. Separate advisory-update resource
  retains explicit announcement state/time/mail behavior. No automatic update/mail.
- Draft-sync prewrite authenticated root capability check covers all SIX used
  mutation types; send expected_state=draft+revision on parent update, CVE
  create/delete and node create/update/delete. Fail closed before any write on
  missing/malformed/denied metadata. Preserve read-only/dry-run, existing draft,
  digest/source/evaluation/checkpoint/recovery safeguards; no new client command.
- Both UIs use captured state/revision, sequential child changes and per-request
  atomicity, preserve unsaved values and stop on conflict/uncertainty. Explicit
  lifecycle confirmations, exact/null dates and localized notes. Public/admin
  boundaries, existing announcement flow and unrelated transport remain intact.

## Repository ranges and full series

All worktrees under /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-published-advisory-corrections/.
Session branches use the slug except modern UI dev/published-advisory-corrections.

vpsadmin target master:
base610a96f8ce523afbcd3e4374a70047dbe3264b0d;
head 218e3180896debd3006b9a0583e557286702761d. Complete series:
1. 866bccf1a8e1d7f758012cb4d6490c0f3af2cb34 api: support guarded advisory corrections and lifecycle actions
2. 218e3180896debd3006b9a0583e557286702761d webui: manage advisory corrections, retraction and deletion
Whole diff22files+1930/-146: about 1300 focused API/model/concurrency/plugin/browser
regression lines, conventional existing runtime owners, behavior docs and locales.
No schema/migration/seed/daemon/config/dependency changes. API and legacy UI are
separate logical commits with their supporting tests/docs. Fresh target unchanged,
clean head/remote proof, mandatory hooks and exact final-tree proof passed.
Earlier892b68b/d80ac520 preserved in backup ref/receipts, superseded restrictions
folded into final A/B rather than retained fixup history. See package-a.md.

security-advisories target actual default2026-07-13-security-advisory-automation:
base7b6c71807e3c5a41f585fd1d9563e151ada71244. Final committed/pushed/remote-proven head
0b771120bb2a878c012512b685208124c2b4263b; complete series one commit:
Require draft state preconditions for every sync mutation.
Final one-line docs fold complete, no application change since37focused passes.
One coherent six-action guarded-sync commit; four files+397/-13, no scopes/schema,
assessment/dossier/evidence changes. Earlier9140/85a3917 are superseded evidence,
not retained update commits. Source/spec patch compatible with public33f253a;
its docs need manual placement preserving unrelated scope/history text, no peer
checkout accessed or feature history imported. See implementer1.md.

vpsfree-kb-contracts target master:
basece2c8cd9358c3636e5d39343e595df813a0b197f;
head21c5213256c28f4a65fd582485e07234a02f5f55, complete series one commit:
Pin KB contracts to published advisory corrections.
Five coherent pin files only, single consolidated mechanical commit. Preserve
explicit vpsadminos6bdf458fd9105379860234ff33d352e55844f08f and all unrelated lock
nodes/root follows/capture provenance/assets/pages. Prior0a12d7d9 old pin retained
as receipt, not repeated final stream. No advisory binding or modern-app input
exists, so no fabricated pages/captures. Strict full pinned bin/check pending.

vpsadmin-webui target main:
base63d484fc070dbee633d32624de545e834d483701;
headb02c922a2c11ff9f3296cf01b48df07387b7fa6e. Complete series one commit:
Guard advisory corrections and lifecycle actions. Branch dev/published-advisory-corrections;
DRAFT PR https://github.com/vpsfreecz/vpsadmin-webui/pull/122.
48files+1681/-605: advisory-specific adapters/hooks/forms, focused tests and four
browser specs/type adoption, cs/en catalogs, required docs/inventory, six synthetic
PNG review captures in existing layout. Removed one resolved structural exception,
no gate relaxation. Shared transport/BFF/dependencies/package locks unchanged.
Source/table/dialog extraction preserves current boundaries; no generic framework.

Prior basef2765d3/head73c05d60 preserved; clean rebase retained both adjacent OAuth/
advisory docs sections. Tested rebased49c4e1626227c9da6a8c68876f157921e7d4ad97
over new base, tree088911bf (full in receipt); finalb02c tree5779c38ff97ab39765c4beebd46917920d6e63de.
Application/catalog/browser/scripts byte-equivalent between tested candidate and
final amendment; only factual worklog provenance and three refreshed desktop PNGs
changed, mobile PNGs byte-equal. Final remote exact and main63d484fc proof, clean.
Old/new full ranges/range-diff/source equality retained in implementer1.md.
No peer checkout or unrelated release content imported into the feature diff.

## Risk, lanes and reviewer

High risk: authorization/state boundary, persisted derived data/cascade,
transaction rollback/concurrency, public preconditions and actual consumers,
UI partial/uncertain outcomes and compatibility. All four lanes: general,
architecture/repetition, scope/proportionality, risk/compatibility.
Selected retained independent reviewer0, gpt-6.1-sol/xhigh, read_only, codex-lb;
live purpose/settings/native identity verified before NEW assignment. No override/fallback.
Read mandatory-change-review SKILL.md and all four references in full; perform
review directly without nested agents. Source fixes belong to implementers.

Independently inventory complete base-to-head series/final diff and migration
provenance in all FOUR repos; conclude no obsolete/transitional approaches,
repeated dependency/pin stream disposition and explicit NO MIGRATIONS when empty.
No new migration exists to be merged/released/deployed/externally consumed.
No deployment or production correction performed. Confirm actual file inventory.

## Evidence-driven corrections to inspect

Original exactd80 CI41331585935 failed two rollback specs: with_lock joined an
existing transaction without savepoint, so a caught exception left writes visible.
Final public edit/rebuild/delete/announcement helpers use conventional
requires_new savepoints plus original parent locks/fresh reads. Named regressions
cover text/node/notes/projections/manual rebuild/announcement mail failure/child
translation/dependent delete rollback. Full actual MariaDB behavior still needs
post-review runs; do not accept source reassurance alone.

Actual OPTIONS emits labeled choice maps with machine states in keys; original
array-only fake expectations were wrong. C/E validators now accept real labeled
string maps plus intentionally supported all-string arrays, reject malformed
keys/labels/missing state with zero writes, and retain machine/human distinction.
E wire fixture uses exact auth/meta/resources root envelope through existing
HaveAPI projection, not a resources-only fake. Shared transport unchanged.

No FKs protect advisory children; narrow parent-lock/reload changes to update
create/translation/delete and outage-link Create prevent orphan races with
parent deletion. Preserve separate announcement mail/state/time behavior.

## Quick verification and documentation

A/B: runtime/spec syntax and all11touched Ruby lint pass, prescribed locale
regeneration/health passed. Main-agent direct English/Czech writing pass applied.
A/B amended mandatory root hooks pass including RuboCop, both locale health,
MigrationSpecs and relevant PHP/Nix format. Root/API test-layout disagreement
resolved by local relation variable, no semantic/rule bypass. Final tree proof
27b1d1327541f2137a347c9b240d965263c66f88 matches intended captured tree.

C: real-metadata37focused cases pass seed51862 in1.31s; full/affected lint/hooks
pass. Includes all six capability failures, all publication races, recovery/
checkpoint/lost-create/legacy cases. Final docs-only amendment uses required hooks.

B: PHP syntax/format, JS syntax, fixture Nixfmt, locale generation/health and diff
checks pass; explicit add/remove/partial omission/retired rows and lifecycle
browser cases authored, not full acceptance executed.
E: root npm ci and complete ci:quick pass (audits/lint/format/catalog/structural/
frontend/tooling/strict E2E/BFF types),31focused cases10files pass, four same
synthetic desktop/mobile cs/en capture-only cases pass on current-base49c4.
Locked terminologya65a4dfeb92a59df4a80a737a20bcbf8558793ff unchanged/rechecked.
Earlier extracted delete-state declaration/type issue and published readiness
alert were narrowly fixed; final same capture cases assert no readiness element
on published. Editor and delete confirmation captures inspected by lead.
No production backend/transaction/cascade/mail claim from fixtures.
Logs /tmp/2026-11-01-advisory-react-rebased-{quick,unit,capture}.log (exact names
and tested source digest in implementer1.md); old first-failure logs retained.
D: final five-pin parse/diff/full lock-graph/follows/provenance checks pass,
only vpsadmin node changed; clean single amended commit/pushed, no hooks declared.

Owning docs: vpsadmin docs/security-advisories.md/index; client README/API-permissions;
modern REQ055 with REQ054 isolation, WORKFLOWS/API/ACTION contracts, evidence matrix,
required generated inventory and dated work-log/WORK_LOG pointer. Lead directly
applied writing skills using locked terminology. Session handoff records prepared
rollout only. No KB content/capture publication or broad docs backfill.

## Compatibility and non-goals

Pause sync during rollout; upgrade all sync consumers before resuming against
complete upgraded API, no mixed pools. New UI writes fail closed against old API,
reading retained. Old unguarded UI/client is not a safe admin-write rollback
partner. No new persisted format/schema/daemon/OS coordination. Intentional
null dates/zero relations/retraction are readable by older software; reverting
software does not reverse corrections, and deletion needs backup restoration.

No republish/reset/automatic announcement substitute, global lifecycle framework,
soft-delete/tombstone schema, batch transaction API, generated SDK/dependency/BFF
migration, generic capability/error framework or unrelated transport changes.
Per-row form saves are separate transactions with prior successes retained.
New lifecycle scopes are explicit and not automatically granted to scoped tokens.
No actual token issuance/production data/default integration/deployment/cleanup.

## Later verification (after final review/finding disposition)

Full/core advisory API/model/concurrency plus outage plugin where enabled,
legacy advisory browser scenario, full client suite, strict exact-source KB check,
modern full unit/build/focused desktop/mobile browsers and declared package checks.
Use fresh retained Luna/low verification utilities for related bounded batches,
exact commands/revisions/logs/time and actual failure evidence; no blind reruns.
All final heads/PR/screenshots/quick evidence included. Write/return final-review.md
findings by severity, exact ranges,
history/migration conclusions and residual test gaps. No operational authority.

## Last metadata-only equivalence refresh

The expanded218e API range differs from priorfb53 solely in explicit human labels
for expected_content_revision (root/node/CVE and standalone Publish) plus one
English locale label. Three paths5+/1-, no runtime/description/enum/test change;
Czech bytes unchanged, B patch byte-identical. Normalization/health/lint/syntax and
mandatory amendment hooks passed. Old/new full ranges/tree proofs retained in
label-equivalence receipt; final whole-range review still required. D amended
single pin accordingly, only selected vpsadmin lock node changes. No repeated
pin or superseded metadata commit remains in final series.

## Current exact-head CI identities (listed, acceptance pending)

API218e: API Specs41337574258,CI41337574315,i18n41337574263,
RuboCop41337574264,WebUI PHPUnit41337574308.
KB21c5: Managed page runtime41337657793,Check41337657622.
Client0b771120: RSpec41336065180/RuboCop41336065173 completed SUCCESS.
Superseded fb53 API/CI and9389 KB runtime confirmed canceled; no current head
run canceled. See metadata-labels.md for full equivalence/proof/log links.

Modern finalb02c exact-head CI41338075403(CI),41338075464(Playwright smoke) queued
at inspection; retained, no superseded active own-head run to cancel. Client C
final exact-head RSpec/RuboCop green. Modern DRAFT is no merge/deploy permission.

## Final reviewer deliverable

Compare explicit user scope with actual whole series/diff/time/milestones first.
Read current repo AGENTS/procedures and skill/all four lane references in full.
Independently inspect source, tests, scopes, DELETE serialization, real metadata,
savepoints/locking/cascade/reference retention, partial/uncertain UI behavior,
actual consumers and supported rollback. Include ALL four repos, whole histories,
single pin stream and explicit NO MIGRATIONS conclusions. Earlier original-scope
review is context only; this must be a new complete final assessment.
Stay read-only and perform review directly without nested reviewers. Return report
text to lead if read-only prevents writing tracking file. No suites/mutations,
production/default integration/deployment/lifecycle action. Necessary fixes remain
with original implementer owners; narrow-fix policy governs later reconciliation.
