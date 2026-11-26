# Disable VPS backups: implementation plan

## Scope and ownership

The user authorized implementation and then explicitly corrected the design to
**one ordinary chain**. D3 in [design.md](design.md) supersedes the D2 two-call
contract; lead accepted the correction. Architect0 owns design and this plan.
Lead exclusively owns [state.md](state.md), package status/timeline, coordination,
acceptance and final English/Czech prose. Application source stays with its
assigned implementers. Integration, publication and deployment require their
separate approvals.

The user subsequently requested a persistent session development cluster for
human UI review. That development-only startup/provisioning is authorized;
production rollout, integration and teardown remain outside this request.
The sufficient packet is [Persistent UI-review cluster](design.md#persistent-ui-review-cluster).

## Accepted inline cleanup correction

Lead accepted the [inline cleanup brief](design.md#inline-cleanup-form-and-concise-copy-correction)
and released I2/PHP and I4/React. Design is settled and parked; those owners retain
source, focused tests, technical docs, commits, review fixes and evidence. Lead
owns acceptance and activation. The independently reviewed Incidents/menu commit
`cc922af3` remains a separate logical change. Infrastructure prevention remains
I1's independent package; no further design investigation is planned.

Both cleanup forms use only this consolidated explanation:

> This removes the selected datasets from all backup plans and deletes their local snapshots. Backups are preserved. Re-enabling backups will require a full transfer.

> Tato akce odebere vybrané datasety ze všech zálohovacích plánů a odstraní jejich lokální snapshoty. Zálohy zůstanou zachované. Opětovné zapnutí zálohování bude vyžadovat úplný přenos.

Confirmation labels are exactly **Confirm** / **Potvrdit**, required and
unchecked initially. Remove the dataset identity sentence, descendant preview
and its presentation-only read, separate primary/manual/backup-retention prose,
long backup-first/no-new-snapshot/opt-out help and recursive help. Do not relocate
the removed text into warnings, tooltips or hidden previews. The separate
Backup plans explanation about plan removal remains.

PHP retains its actual form below Backup plans and uses one paragraph in the
existing `colspan=2` row followed by valid two-cell controls. No global CSS/helper
change. React removes the cleanup opener/pop-up and renders the actual form
immediately below the plan list or empty state. Its independent recursive checkbox
starts false unless the existing `recursive=true` shortcut selects it; changing
the checkbox does not change page filters or the URL. Backup-first remains
independent and checked by default. Reset confirmation on dataset/recursive scope
changes and accepted submission, preserving button and handler/POST enforcement.

Keep admin/capability gating, dataset-bound single-use PHP CSRF, server scope
validation, preflight, pending/double-submit guards, one ordinary mutation and
existing receipt/task/unknown-outcome handling. No API, SDK/dependency or BFF
change. Focused behavior checks and EN/CS desktop/narrow visual proof precede
acceptance; live verification never submits cleanup or mutates the review fixture.
No guest, runtime or fixture action is part of design reconciliation.

## Accepted React review baseline and prevention follow-up

The prior real React review milestone is complete and accepted at
`ff2cf8ae4b44781f90941611294a94fd6953763a`, tree
`2c1c9ff8928011b29d23ab96ab22ea2a14edfead`. The default-unchecked confirmation,
local SDK package, matching Nix frontend/BFF, guest daemon import/roots, trusted
TLS and real admin/member OAuth/UI checks passed. The active review URL is
`https://newadmin.aitherdev.int.vpsfree.cz:8443/admin/datasets/1/plans?recursive=true`.
Keep registered BFF/edge, all five guests and VPS1/plan/three source snapshots/one
backup intact. [state.md](state.md) and [I1 evidence](i1-evidence.md) own current
receipts; the original PHP-first decision below is historical. The new inline
correction above is a subsequent source package, not yet covered by that proof.

The user's prevention request has a sufficient independent I1 brief:
[Future-session React preparation and SSH prevention](design.md#future-session-react-preparation-and-ssh-prevention-brief).
Document ordinary React-enabled preparation **before first boot** in the provider
README; separately route generic `dev-workspace` SSH through the existing
interactive helper and extend its dispatch/lock tests. The custom credential bug
was ours; fixtures were healthy. No default flip, generalized launcher, live share
migration, selected-package switch or current runtime mutation. I1 uses separate
infrastructure worktrees/indexes after lead release, disjoint from I2's vpsAdmin
PHP form package. Quick checks, committed independent review and affected package
checks precede any separately authorized deployment. Lead owns allocation/status
and acceptance.

## React development dependency package (retained implementation rationale)

The user now requests actual React review with the unreleased local SDK. The
[sufficient dependency brief](design.md#sufficient-local-sdk-packaging-brief)
releases I4's independent source/dependency package: retain immutable671b54 SDK
archive in regular source, npm-generated relative file dependency/lock, select
the standard frontend dependency-import inputs and update existing provenance/
packaging docs. The initial prefetch failed on file:; the settled correction uses
`importNpmLock` with its matching config hook and one exact SDK source override,
per-module lock integrity instead of a frontend aggregate `npmDepsHash` (see
design). No retry of the incompatible fetcher. Preserve
all unrelated dependencies and matching frontend/BFF source. No SDK publication,
regeneration, backend/client adapter or BFF behavior changes. Quick identity/type/
action/source checks, commit and independent review precede long Nix package and
runtime proof. I4 owns source/index/commit, checks and evidence; lead acceptance
and activation remain separate.

The earlier React milestone added the required default-unchecked confirmation
with submit gating and reset. The accepted inline correction above now supersedes
its dialog placement and long copy; confirmation enforcement remains. Earlier
`18597` outputs preceded the completed checkbox correction and were not activated
as final. Subsequent UI source changes require their own matching package proof.

The existing React-disabled cluster lacks the required credential virtiofs
share. Installed provider update and retained-start compatibility both reject
adding it; a services or whole-cluster restart is not a workaround. No destructive
reset or manual applied-record edit is permitted. The registered-service route
below preserved the cluster and completed actual React deployment. The provider
layout restriction still applies. Keep PHP and all fixture data live.

Lead selected the existing ordinary registered-service alternative:
[Selected runtime route](design.md#selected-runtime-route). Accepted I1 facts
select `https://newadmin.aitherdev.int.vpsfree.cz:8443` on services VM
`172.16.106.53`, BFF `127.0.0.1:3001`, existing matching certificate/CA and a narrow
new guest TCP/8443 allowance (not reachable before activation). I1 owns exact
operational commands, separate nginx configuration and small foreground SSH
ownership wrapper; I4 supplies matching reviewed/built frontend+BFF paths and
application proof. Lead owns normal nondefault OAuth client/exact callback,
private credentials/session provisioning, firewall and activation drivers.
Existing API preflight permits token-header requests from the origin; no CORS
policy rewrite. Keep provider flag/layout unchanged, no Vite/synthetic API/provider
feature. Bind registered local lifetime to only the new remote processes; unknown
connection/exit requires reconciliation. Runtime prep is independent of the SDK
source package. Preserve every current guest and fixture object, with no timed
cleanup or guest/main-service stop.

For guest package residency, use
[App closure import](design.md#app-closure-import-into-the-running-guest): I1
prepares a complete public Nix export under the existing ignored backend mount,
root imports from that guest-visible file using `NIX_REMOTE=daemon` and registers
per-output persistent roots. I1's one root-authorized daemon query passed and
proved its actual store mount writable. Final app import, persistent roots and
runtime proof subsequently passed; no import or activation remains here.
This avoids closed caller stdin and does not remount the
client's read-only store. Successful final-path/closure/root proof gates activation;
no raw copy, alternate store, build or speculative recovery. Root retains mutation
authority, and OAuth provisioning remains independent.

## Human review cluster execution boundary

The running cluster is now the user's persistent review fixture. The subsequent
PHP layout correction is specified in
[PHP layout correction and live review](design.md#php-layout-correction-and-live-review).
I2 owns the bounded existing PHP renderer/form/translation/spec/docs changes:
explanation inside Backup plans, no perex cleanup link, actual cleanup form
immediately below with independent recursive/default-on backup-first controls.
Include a required confirmation checkbox unchecked by default, with explicit
plan-disable/local-snapshot-removal consequences and the fact that re-enabling
backups will require a full transfer, using lead-approved English/Czech wording.
The latest inline correction above removes the static optional-descendant preview
and its presentation-only read while preserving dataset-bound single-use CSRF
and server scope/authorization checks. It also simplifies React's presentation;
API/client contracts remain unchanged.

Existing files are served live from the selected worktree. There is no build,
provider refresh or separate activation command for this correction. After I2's
commit, quick checks and independent review, lead releases its nondestructive
rendered-form proof with exact changed host/guest file binding. I1 is needed only
if actual staleness requires diagnosis; no speculative reload work. Preserve
VPS1/plan1/three source snapshots/one backup and all guests. These follow-up
checks supersede repeating the original C1–C3 creation/provisioning steps below.

This is separate from the completed feature design and parked storage/PHP VM
verification. Lead retains status and dispatch; the following defines ownership,
not a second status table.

- **C1 / I1 preparation:** exact backend `140f0769`/tree `a8721811`, installed
  fjr83 provider and effective OS `cf53d670`; preserve private original config
  then change only `newWebui.enable=false`, as explicitly released by lead.
  Deliver source/gem/input identity, stopped owned namespace, bridge/address
  availability, current resources and normal-provider cache/kernel admission.
  No application edits or global route takeover. Independent of fixture setup.
- **C2 / lead startup, I1 technical support:** after C1 admission, public
  `vpsadmin-devcluster start 2026-11-25-backup-disable-design --topology dual --network bridge`.
  Private mode-0600 raw log; fresh observer watches existing driver only.
  Accept full applied boot, ready status and API/node/pool health. Preserve
  uncertain effects; no force/reset or unapproved fallback.
- **C3 / I1 fixture:** after C2 health, ordinary Pool/Vps/Dataset/Plan/Snapshot/
  Backup operations from the linked recipe. One VPS, real daily plan, three
  confirmed source snapshots and at least one readable confirmed backup copy.
  Record IDs and receipts; verify marker content and PHP action/plan explanation.
  Retain the fixture and cluster for the user; do not perform disable cleanup.
- **React / I4, original creation boundary:** c723's registry SDK lacked this
  action, so initial startup was PHP-first. The later user-requested local SDK
  and registered React deployment superseded that temporary limitation and are
  complete as recorded above; no registry publication was needed.

Owners put only safe evidence in existing session records; credentials and raw
config/start output remain private. Lead supplies the UI URL, fixture IDs and
protected access path in its final handoff. No additional broad tests or review
framework is introduced for this operational fixture brief.

The user subsequently approved the bounded locking simplification in
[design.md](design.md#accepted-locking-simplification). It supersedes blanket SQL
locking and arbitrary enclosing RR support, preserving all settled behavior.

Settled scope:

- Administrator-only `Dataset.DisableBackups`; all primary/hypervisor snapshots
  removed, including manual/untransferred snapshots; planless datasets supported.
- `recursive=false`, `backup_first=true`. Preserve existing snapshots only on all
  existing open backup targets; do not create a new live-state snapshot.
- One ordinary chain/receipt: all transfers/checks, then plan removal/head detach,
  then explicit source destruction. No rotations. An old gap ordinary Transfer
  cannot preserve rejects construction; no new force-full mode.
- Ordinary HaveAPI response wrapping remains: `response.dataset` is `{}` and
  `response._meta.action_state_id` is the chain receipt. There are no declared
  action-specific output fields; clients may already unwrap `response`.
- No continuation input, public phases, manifest, browser-exit cancellation or
  orchestration subsystem. Plans/head edits use ordinary confirmations; the
  complete metadata/destruction suffix is not_reversible, never keep_going.
- Ordinary Plan.Create/Delete meanings and permissions remain unchanged. No
  zero-to-one head reset, restore policy, notifier repair or Nix socket change.
  Keep only source-lock and post-lock scheduled membership safety fences.
- Both dataset-plan forms explain that plan deletion leaves snapshots in place.
  Normal disable→reenable gets a new tree/full first transfer from detached heads.

## Packages and correction boundaries

These remain the existing owners; this document does not dispatch work. Lead owns
release and mutation windows. Each owner retains prior exact-head/check evidence,
removes superseded unpublished mechanisms from its own files, and reports the
complete corrected source/check inventory. No compatibility shims for D2.

| Package / owner | Exclusive deliverable/files | Dependencies, acceptance and evidence |
| --- | --- | --- |
| Configuration channel / implementer0 | Only the `vpsadmin` channel update in `vpsfree-cz-configuration`; no deployment. | Normal recovery/preparation complete; awaits root's actual merged API SHA. Implementer2 retains client/source-mapping ownership; root owns integration drivers. |
| I1 / implementer0 | One API action/chain, complete coverage validation using ordinary Transfer/Send and existing RecvCheck, scoped unregister option, narrow plan-lock/scheduled guards, specs and storage/usage docs. `api/lib/vpsadmin/api/resources/dataset.rb`, `api/lib/vpsadmin/api/dataset_plans.rb`, `api/models/dataset_action.rb`, relevant `api/models/transaction_chains/dataset*` and focused corresponding specs; `tests/suite/storage/backup-multiple-destinations-remote.nix`, `backup-remote-interrupted-send.nix`, bounded `remote-common.nix` helpers and selection metadata only as needed; `docs/storage/`, transaction/usage docs as relevant. Own removal of D2-only helpers/NoOp payload and API-service Nix stanza from prior work. | Accepted D3. Preserve all-source/all-target data or reject construction; all preservation precedes all destruction; irreversible suffix retains successful backups on partial failure. Prove planless/empty/recursive/reference/race behavior and unchanged ordinary plan semantics. Actual ordinary wire receipt check. Exact base/head, changed files, focused quick results, fixture source and no-migration/history conclusion. |
| I2 / implementer1 | PHP one-submit/default-on checkbox/task handling and plan-removal explanation in `webui/forms/dataset.forms.php`, `webui/forms/backup.forms.php`, `webui/pages/page_dataset.php`, related locales/browser tests. Remove continuation forms/options/session orchestration from prior work; retain ordinary CSRF and duplicate-submit handling. | Corrected I1 action with only two booleans and ordinary receipt; admin/capability/zero-plan gating. Status requests only observe; browser exit does not cancel accepted work. Correct pending/failed/unknown/completed messages, both plan-removal facts and scope display. Lead supplies final prose/KB assessment. |
| I3 / implementer2 | Final clean committed API export and Go/Rust/TypeScript client synchronization in owned client repositories. Replace unpublished D2 schema/output with corrected action, without compatibility members. | Final committed I1 and quick checks. Record API/schema/profile/generator identities, complete generated diffs/checks and any exact no-change evidence. No new output payload or client continuation. Publication remains a separate action; published TS dependency is required before I4 merge. |
| I4 / implementer3 | React ordinary action adapter in `src/lib/api/datasets.ts`, shared DatasetPlansPage, VPS storage link, locales/unit/browser tests and relevant requirement/inventory/work-log docs. Remove phase/continuation adapter and controls. | Corrected I1 contract and I3 SDK. Existing action-state task workflow; admin/capability/no-plan/default-on behavior, correct actual routes, both plan-removal explanations, unknown receipt reconciliation, Czech/English and desktop/mobile checks. Candidate SDK is permitted for development; final manifest/lock uses published SDK before merge. |

The narrower safety changes in I1 are justified in design.md: prevent Plan.Create
from adding schedule membership while disable holds its source; prevent an action
or group list loaded before removal from running after locks release; avoid
asynchronous deletion of a shared group that another dataset joins. Use a scoped
keep-shared-group unregister option for this action, leaving old callers unchanged.
Do not repair unused DatasetPlans.confirm or add scheduler control/configuration.

## Order and shared boundaries

### Current I1 simplification brief

I1 owns the exclusive backend source/index/commit window; this remains its
existing package. Architect supplies the brief and lead owns release/acceptance.

Accepted narrow guard correction: retain only the post-resource-lock checks in
Backup/GroupSnapshot, the two configured plan paths. In
`api/models/transaction_chains/dataset/{snapshot,transfer}.rb`, remove this
feature's standalone guard/allow_empty changes and revert Transfer's incidental
Time.new → Time.now line. Remove only the corresponding standalone dispatch
arguments from `api/models/dataset_action.rb`. Preserve Backup/GroupSnapshot
behavior and existing concurrency assertions. The real lookup-to-lock race,
fail-fast/no-retry semantics and reason not to move ownership handling into the
scheduler are recorded in design.md. No framework, API or scope expansion.

Current positive-path clarification adds only focused I1 regression coverage in
`api/spec/models/transaction_chains/dataset/backup_spec.rb`,
`api/spec/models/transaction_chains/dataset/group_snapshot_spec.rb` and
`api/spec/models/dataset_backup_concurrency_spec.rb`, using existing fixtures.
The brief is [Positive scheduled-work acceptance](design.md#positive-scheduled-work-acceptance):
real plan-created DatasetAction.execute must queue conventional backup
transfer/rotation and snapshots for every current shared-group member; a removed
stale member must not suppress surviving members. Include ordinary query caching
in one positive path and retain manual/stale/conflict checks. No predicate/lock/
whole-chain stubs, production change predetermined, schema/client work, VM/disk
work or broader supported isolation. I1 owns tests, quick checks, commits and
evidence; a concrete behavior failure returns to lead with the smallest fix.

- Files: `api/lib/vpsadmin/api/operations/dataset/disable_backups.rb`,
  `api/lib/vpsadmin/api/dataset_plans.rb`, `api/models/dataset_action.rb`, the
  plan-enumeration query in `api/models/transaction_chains/dataset/disable_backups.rb`,
  focused existing operation/API/concurrency specs and affected storage usage docs.
- Remove broad SQL locking reads from the operation, source-helper reads and
  scheduler existence checks. Keep durable VPS/source/backup/source-SIP locks,
  ordinary fresh post-lock reads, source/subtree/owner revalidation, Plan API
  resource fences, scheduled action/member checks and all safety predicates.
  Decouple keep_shared_group from query locking; keep its retention behavior.
- Supported isolation is configured production READ-COMMITTED. No global
  database/test-isolation edits. Local connection isolation in the specific
  concurrency examples is acceptable, restored afterward. Replace the unsupported
  old-RR guarantee, not the stale-action/member behavior assertions.
- Focus checks on `api/spec/models/dataset_backup_concurrency_spec.rb`,
  `api/spec/models/operations/dataset/disable_backups_spec.rb` and
  `api/spec/api/resources/dataset_disable_backups_spec.rb`: preserve exclusion,
  fresh scope/ownership checks, reference rejection, shared-group retention,
  all-target preservation and ordinary one-chain behavior. Use existing package
  quick-check/hook procedures; no new harness or architect-run tests.
- No API/schema/generated-client, UI, node primitive or public contract change.
  Report precise final diff/head, checks and any remaining input/provenance
  reconciliation to lead. Preserve previous evidence for its actual source;
  review and downstream verification freshness remain lead-coordinated.

1. Lead releases correction work against the sufficient D3 brief. I1 owns shared
   API/storage/scheduler logic as one package. I2 and I4 may simplify their disjoint
   UI work against its settled ordinary receipt shape. Do not edit during an active
   source freeze; keep current verified heads/evidence until the owner resumes.
2. Sequence I1/I2 index/commit/rebase windows in their shared vpsAdmin checkout.
   Application fixes stay with the original owner. Architect resolves routine
   questions; material scope/contract/ownership changes go to lead.
3. I1 commits complete intended source including storage fixture extensions and
   passes relevant quick checks. I3 then exports/regenerates final clients. No
   SDK publication is implied. I4 finishes against that actual contract.
4. Owners consolidate superseded unpublished approach history before final review,
   retaining exact prior/new ranges and evidence. Supply complete base-to-head
   series, final diff, migrations/no-migration conclusion and changed-file/check
   inventory. Lead invokes independent review under the required procedure;
   owners fix findings. Long integration and applicable browser/KB checks follow.
5. Prepare delivery/rollout evidence. Integration and deployment remain separate
   approvals. Do not equate implementation, review, VM results or branch publication
   with integration/deployment readiness or session completion.

## Focused checks and acceptance

Use design.md's matrix; avoid repeating unchanged passing checks except where D3
changes their inputs/meaning.

- API: admin-only, both defaults/false, planless/empty/recursive scope, all open
  targets, closed history, strict existing or this-chain planned coverage, pending
  and protected snapshots, no rotations. Old/middle gap outside ordinary Transfer
  selection raises before a chain is queued; existing normal initial-full/history
  paths still work without a new force-full option.
- Ordering/failure: every required transfer/check across all datasets/targets
  precedes first Destroy. Existing per-snapshot checks cover newly copied selected
  intermediates. Preservation failure executes no source deletion. All metadata
  and cleanup helper transactions are not_reversible; later failure cannot roll
  back preserved backups. Forward confirmations retain actual successful metadata
  and deletions, leaving failed/future source copies. Fatal/unknown outcomes are
  reconciled through ordinary chain tooling.
- Concurrency: plan mutation lock, stale loaded scheduled action/group list,
  unrelated shared-group join and subtree creation. Ordinary plan semantics and
  restore behavior unchanged; no first-registration detach. No socket/notifier
  compatibility or NoOp-manifest tests remain necessary.
- UI/CLI: exactly one mutation plus normal receipt waits/status reads; no second
  call or phase protocol. Default-on checkbox, opt-out loss fact, admin/capability
  gating, no-plan entry, scope display, plan-removal explanations and correct
  pending/unknown/failed/completed outcomes. Closing client does not cancel.
- Storage source before review: extend existing two-destination and interrupted
  sender fixtures named above. Use known per-snapshot/live contents, ordinary
  lagging-target preservation, source removal, readable retained backup history,
  old-gap rejection, failure with zero source deletion, then normal reenable new
  tree/full followed by incremental. Preserve existing cases and helpers; no new
  harness. Metadata registration/selection changes only if actual paths require.
- Post-review VM execution proves actual file contents/checksums at source and
  retained branch locations, not just counts. Raise retention to protect fixture
  evidence. No new live-state snapshot. Quick syntax/Nix/spec/selection checks use
  repository instructions; long checks use the monitor workflow.

Each package reports exact tested head, commands/results, remaining unrun checks
and source/history evidence. D3 itself runs no application or VM tests and does
not trigger independent implementation review.

## Documentation and compatibility

Primary readers are API/CLI administrators, PHP/React users, storage maintainers
and reviewers. Lasting behavior/failure semantics and one-call examples belong in
vpsAdmin storage/usage docs; React updates its existing requirements and workflow
records. Session design keeps the evidence/rationale; lead state keeps progress.
Both UIs assess KB form/navigation/screenshot impact. Lead applies the required
writing skill to final prose; production KB writes retain exact-change approval.

No migration, new command/wire field or storage format. Existing nodes execute
existing primitives. API and scheduler processes must both have the necessary
lock/membership fences before exposing the action; no Nix socket deployment is
part of this feature. Complete/reconcile pending chains before software rollback;
rolling back cannot recover destroyed snapshots or removed schedules. Existing
backup retention and deliberate restore/manual-transfer semantics remain intact.

The ordinary action is additive to the prefeature API. Generated clients follow
final committed input; old API capability gating remains. No forced compatibility
with the unpublished D2 protocol. Published TS dependency before React merge,
backend readiness, repository integration and package publication are distinct.
