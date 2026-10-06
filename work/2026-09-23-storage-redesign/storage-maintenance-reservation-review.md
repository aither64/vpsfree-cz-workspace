# Final Admin branch review: API maintenance reservation

Status: final committed review packet; review acceptance pending.

Base `c4d9b50f4e74417ed37b5fe410cca3ec1addc24e`, head `edc26498f4875340de6a2484b230fb6e8865d492`, tree `a09dd851695e7139aeb431b2bd2dfef15579d7e3`.
24 commits; 214 final-diff paths. Complete binary/full-index SHA256
`e7b4b84f2c45c99b2ddc925acd910a6e25a33695cca1068015f3bdc936887b4e`; new19-path unit SHA256
`c76c37509d166031adad0e152695eb45616c763c58c4a193e787b630ec975166`.

Artifacts: [inventory](storage-maintenance-reservation-inventory.json),
[complete diff](storage-maintenance-reservation-complete.diff),
[new unit](storage-maintenance-reservation-unit.diff),
[rebase union](storage-admin-c4d-rebase-inventory.json),
[range diff](storage-admin-c4d-rebase-range-diff.txt).

## Assignment

Independent mandatory final review, all four HIGH-risk lanes: general,
architecture/repetition, scope/proportionality, risk/compatibility. HIGH applies
to authenticated authority, schema/persisted state, concurrency, API/Node
contracts and mixed-version deployment. Retained reviewer0 is independent,
ready/review/read_only/gpt-6.1-sol/xhigh; preserve saved settings, no override,
fallback or nested reviewer. Read the mandatory-change-review skill and all
four references, applicable workspace procedures and Admin AGENTS/procedures.

Review COMPLETE c4d..edc26498f4875340de6a2484b230fb6e8865d492, including all 24 commits and the entire final
diff. Earlier incremental reviews do not discharge this assignment. Inventory,
complete diff and new-unit diff are adjacent artifacts. The prior 23 commits
were published and consumed in the retained Admin290f composition. A normal
rebase onto c4d preserves all seven upstream commits, all 23 source units,
consumed migration/schema blobs and selected OS input. It has 21 equivalent
range-diff entries plus two recorded context unions; do not rewrite consumed
lineage to make a superficially short history. Independently conclude whether
obsolete approaches, fixups, transitional migrations or redundant inputs remain.

Session: 2026-09-23-storage-redesign. Repository vpsfreecz/vpsadmin, feature
branch2026-09-23-storage-redesign at the registered Admin worktree. Owning
plan/state/design are in this tracking directory. Source owner: Admin. Current
new unit is one API-only reservation behavior with its inseparable model,
resource, migration/schema, metadata translations, selector tests and three
reference pages. Code, tests and generated companions belong together. The
unpublished owning commit was normally amended for four lint-comment relocations
and message wrapping; no fixup remains and no consumed predecessor was amended.

## Requested result and acceptance boundary

Existing authenticated StorageFreeze gains maintenance_reserve/show/abandon.
StorageMutationAdmission owns service/auth/current-lock semantics; one retained
StorageMaintenanceRun and restrictive singleton owner pointer declare contract1,
reserved revision1 -> abandoned revision2, manual_storage_only_v1. Requested
Pool/Node scope is an immutable catalog snapshot, never dependency or physical
proof. Reserve uses exact UUID/epoch/direct administrator and current Pool/Node
locks. Exact replay resolves uncertain COMMIT; another owner refuses. Abandon
requires exact UUID/epoch/revision/scope digest/known predecessor and fresh
current direct administrator, preserves acquisition and abandonment identities,
and leaves read_only/epoch unchanged. Session death never clears ownership.
Unknown future handoff contracts refuse. Read_write and contradictory
read_write+owner admission refuse.

Pool selector is required Custom pool_ids: JSON Array1..256 of unique positive
Integers, without coercion/dedup/fallback. The installed HaveAPI Resource type
is scalar; the list shares UUID/epoch fields and is revalidated with exact set
agreement under owner/catalog locks. Existing required-empty pre-action behavior
is HTTP200 logical status:false/response:null with parameter error. Nonempty
malformed cases422, missing catalog/stale owner409 and authorization403 remain
as tested; no empty scope is admitted.

Explicit non-goals: no acquisition-ready claim, Node dispatch, capture approval,
physical exclusion, repair/action journal, G2 execution, TTL expiry, automatic
abandon, alias adoption/rename/delete, provider repair interface or new engine.
Status remains repair_ready:false. A future physical handoff must change the
recognized record contract before taking responsibility so an old API-only
abandoner cannot release it.

Mixed-version limit: old mode setters ignore this new pointer. Exclude every old
unfreeze writer before relying on the reservation; no universal old-writer fence
or API-only VM proof is claimed. Audit persists on software downgrade; rollback
with active owner is unsupported. Migration down refuses used run/owner before
DDL. Compatible API/Supervisor/task/admin readers must converge.

## Complete lineage and consumers

Three migration versions in the full range:
- 20260924210000 foundation: feature-published and externally consumed at290f;
  exact blob7d929052f314d5a821b2ce65345680c0740b1b0c preserved.
- 20260926100000 capture indexes: feature-published and externally consumed;
  exact blobd60868e615024c70fb4b87b736a2466ceb8349db preserved.
- 20261006120000 reservation: additive exact predecessor; only private disposable
  generation/spec use, not master/released/live-deployed/externally consumed.
  Exact blob and generated schema hashes are in the final inventory.

Core schema was generated using existing TestDb::Instance and pinned AR core-only
predecessor load + sole migration, without app/plugin boot, unrelated changes
or plugin dump. 179->180 tables; generated schema accepted/installed byte-for-byte.
Locale update/health uses ordinary full-plugin tasks in separate guarded private
snapshot; all2359 predecessor leaves per locale unchanged,29 additions each,
no TODO. No historical migration replay or schema-existence fallback was added.

Actual consumers include API/HaveAPI clients/WebUI, staging models/Plan/task and
Node commands in the full branch. Inspect imports, routes, current inputs and
companion branches rather than assuming a closed consumer list. Admin selected
OS input8d05dc3ae1fb71c1385609990acdf093af49ceec is unchanged by reservation.
Provider placemente33 was reviewed/published separately, not delivered; current
root provider0ff and retained guest Admin290f do not load this new owner. No pin,
package, default integration or live reservation follows this source review.
Inherited canonical schema1/policy3 and provider maintenance2/applied1 are outside
this Admin unit and unchanged. The retained alias remains a separate blocker.

Reference docs changed: docs/storage/integrity-foundation.md,
integrity-model.md, integrity-reconciler.md. These describe owning behavior and
limits; individual trial/provenance is in tracking design/state. Inspect docs
placement, unknown-state refusal, mixed-version/readiness limits and upgrade
ordering. Rebase/source inventory and historical tests remain linked separately.

## Verification and limits

Full selected files at final runtime/style bytes: API73 examples,0 failures/
pending/outside errors; sole migration6/0. Afterwards11 exact receiver spellings
changed from explicit class to described_class with actual RSpec3.13.6
same-class inheritance/no override and reverse-byte proof, followed by four
comment relocations only. Runtime, assertions, worker binding/isolation/reap,
primary-error/no-restore semantics remain identical. These are scoped functional
carry, not a claimed single final all-four-suite rerun.

Final API and root RuboCop both inspect12 files/0 offenses; generated schema is
excluded by repository policy. Root selector20 runs/89 assertions/0 failures/
errors/skips. Standard Bundler.with_unbundled_env in a PRIVATE nested driver
removes API BUNDLER_SETUP before root shell; no product dependency/env/SQL change.
Normal commit hooks run with existing installed Overcommit and private bound DB
for ordinary i18n health, no bypass. Final normal hooks passed without warnings; source/tree/foreign
cache parity and disposable shutdown were proved. Recorded in inventory. Checks are lead/watcher evidence;
reviewer must not run checks or read private log/DB/credential artifacts.

Historical failures retained: required-empty/expected-epoch test assumptions;
AR RESTRICT reflection metadata; fixture lint/nesting and receiver spellings;
nested BUNDLER_SETUP pre-example LoadError; old root lint-comment grammar.
Corrections are folded into the one unpublished owner. No runtime/alias repair
is inferred from a corrected test pass. Private database shutdown and child
waiting are proved; files retained, no automatic prune/live DB operation.

No new VM/CI wait, live Node/storage operation, physical exclusion or G2 trial.
Actual NAS historical integrity, aliased DIP5/DIP12 disposition, fresh preferred
Pool availability, full/incremental payload/history/automatic/repeat/retirement
remain unproved. Keep scheduler stopped, admitted objects and evidence intact.
Source review supplies no default merge, deployment, activation, repair/retry,
cleanup/cancel/unlock/retirement/APPLY or acquisition authority.

## Report

Start with findings by severity, exact file/line/commit and lane. If none, say so
and state residuals. Give distinct lane conclusions plus explicit COMPLETE
history/obsolete/migration provenance conclusion and intentional format/API
changes; do not call this no-format-change. Verify final exact head/tree/diff
hash/path/source inventory and independence/settings at start/end. Review all
committed public source directly, read-only, no nested reviewers. Lead will
record findings and handle steps8-10 of the mandatory skill. Do not rubber-stamp
parent's source assessments or treat earlier reports as final clearance.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-23-storage-redesign/
