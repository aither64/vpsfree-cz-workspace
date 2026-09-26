---
lifecycle: active
---

# 2026-09-23-storage-redesign

## Current status

2026-09-26 architecture checkpoint: the user-requested Astra assessment is
recorded in [plan.md](plan.md) and the current section of
[storage-integrity-design.md](storage-integrity-design.md). Milestone A is a
bounded, exclusive frozen maintenance workflow for provable existing-catalog
corrections and compatible service resumption. Continuously verified physical
identities and strict writer families are a separate milestone B. The review
identified four concrete G1a capture defects, a cold-offline CLI startup
effect, and the need for a held Node/osctld exclusion plus an active freeze
owner before executable repair. It proposed a separately tested current SIPB
dependency-projection policy; the default remains private physical-origin
evidence with no legacy parent edit. No repair approval/APPLY or production
window is authorized by the design update. A follow-up source check selected a
manual storage-only maintenance generation, stopped-daemon child proof,
one-shot signed 5290 runner and active API owner as G1b's working default;
the automatic Node/osctld hold protocol remains a later option. This is a
design decision, not an implemented exclusion gate. Implementer0 prepared two
separate G1a liveness fixes in an isolated worktree from published
`fe4f9b0f9`; fix 1 focused API specs passed 17/0, with its normal-hook
commit now at isolated `13368304d`. Fix 2 passed focused DbCapture specs
8/0 after correcting a missing STI type in the new fixture. Independent
four-lane review found one Important case: an old Node retry can overwrite a
previously started member with a skipped result. The amended second commit
`32f9875eb` rejects that as terminal proof; its mixed-member regression
passed 9/0, normal hooks passed, and the reviewer reran affected lanes with
no remaining Blocking or Important finding. The registered vpsAdmin tree
remains clean at `fe4f9b0f9`; broader tests and publication remain pending.
Retained reviewer0 assignment failed before submission because the portal's
queue-attempt ledger reached its hard-coded 1 MiB limit. The mandatory-review
standalone fallback used the installed default-team reviewer role with exact
gpt-6-sol/xhigh settings. Its review packet is at
`/tmp/storage-g1a-liveness-review-packet.txt`; no ledger file was altered.
Cold offline replay is committed separately at isolated `d533116` on
`32f9875eb`: a pure artifact loader replaces full API boot for
`compare|dry-run|plan`. A sealed artifact passed all three commands in a fresh
Ruby process without ActiveRecord; focused CLI specs 8/0, selector 18/77 and
normal hooks and independent four-lane review passed with no Blocking or
Important finding. GUID normalization was committed at isolated `b3f1bc260`
and cleanly replayed after the offline change, with an operator recapture
clarification amended into final `53a9768d8`. All 12 known
storage GUID DECIMAL fields use exact bounded uint64 digits; focused
DbCapture/ProofPlanner specs passed 37/0, targeted RuboCop and normal hooks
passed. Independent four-lane and final affected-lane reviews found no
Blocking or Important item; the documentation advisory was resolved. The
combined four-commit branch is clean at `53a9768d8`, with lifetime journal
capture volume still unresolved. Read-only design analysis found both the
scope-intent history fan-out and accumulated terminal `done=2` rollback rows;
exact rollback proof cannot be preserved by an indexed state filter alone.
The next G1a slice needs bounded current-graph/pending-SIP evidence closure
with explicit unknown lifetime-terminal coverage. Architect0 found that a
live unresolved registry cannot be trusted while old and direct-SQL writers
can change results without invalidating it; a full retained-history checkpoint
is deferred to a held maintenance window if an action needs that proof. A
one-file real-MariaDB red fixture at isolated `53a9768d8` ran 12 examples:
the two new settled-history/terminal-rollback-history cases failed exactly
with `DbCapture::Incomplete: DB capture row limit exceeded`; the other ten
passed. The first prerequisite is now isolated commit `543634b76` on
`53a9768d8`: offline readers validate source `(1,1)` and future `(2,2)`, adapt
legacy coverage to explicit unknown, and produce policy-2 reports and
policy-3 nonexecutable plans under collision-free names. The capture writer
still seals `(1,1)` because its present selector cannot claim complete
node-wide work. Focused four-spec API selection ran 57 examples with one
synthetic fixture run-ID error; the corrected affected artifacts spec passed
12/0, while the other 56 were green in the first run. Ruby syntax, targeted
RuboCop 8/0, diff --check and normal Nix pre-commit/commit-message hooks
passed. Reviewer0 independently cleared this HIGH-risk artifact-contract
commit in general, architecture,
scope and risk/compatibility lanes with no Blocking, Important or Advisory
finding. Reviewer0 retained saved gpt-6-sol/xhigh/read-only settings. That
prerequisite deliberately left the writer at `(1,1)` until the selector could
support a `(2,2)` coverage claim.

The dependent bounded-selector commit `e7f91a221` is clean in isolated
`/tmp/storage-g1a-bounded-capture-2026-09-23-vpsadmin`, based on
`543634b76`. It adds three nonunique query indexes, selects current catalog
and pending SIP evidence plus observable node work, bounds rows visited and
artifact bytes, and seals source `(2,2)` with historical terminal coverage
explicitly unknown. It includes exact current scope keys, same-node retained
locks, cross-intent malformed-reference closure and frontiers that avoid
repeated ID queries. Corrected focused DbCapture specs passed 23/0; unchanged
Artifacts 12/0 and migration 2/0 passed. Normal Nix pre-commit and
commit-message hooks passed. Independent reviewer0, using its saved
gpt-6-sol/xhigh/read-only settings, reviewed all four HIGH-risk lanes and
found no Blocking or Important issue. The reviewer confirmed that mandatory
selector failure cannot seal a complete artifact, while a complete diagnostic
capture still does not prove lifetime terminal history or permit APPLY. A
disposable 40k-object MariaDB capture passed on this head: 40,007 rows emitted,
40,009 returned rows visited, a 16,427,918-byte artifact and 13.33 seconds
for capture, with 20,000 unrelated settled intents omitted. Its private
database stopped and TCP port closed. The original EXPLAIN subprocess returned
zero without plans; a separate read-only retry produced six parsed JSON plans
and stopped the database again. SIP, target and waiting-transaction selectors
use their expected indexes. The retained-lock query plans an estimated
~19,910-row scan for its intent EXISTS arm on this fixture despite the chain
index. Its outer ResourceLock scan is global; the fixture has no retained-lock
cohort, so it does not measure repeated correlated probes from selected or
unrelated nodes. Architect0 recommends recording this as an advisory liveness
limit under the 10-second statement and 15-minute capture fail-incomplete
bounds, and measuring a populated cohort, including unrelated-node locks,
before live use or any index/query hint. Reviewer0 then inspected the complete
six-commit `fe4f9b0f9..e7f91a221` series, its sole additive migration, final
schema and offline artifact consumers. The independent final-series review
found no Blocking or Important interaction or history issue and retained the
lock-cohort performance and end-to-end/mixed-reader tests as advisory gates.
The clean registered vpsAdmin feature branch was fast-forwarded from
`fe4f9b0f9` to `e7f91a221`, preserving the former head under
`backup/2026-09-23-storage-redesign-before-g1a-bounded`. The new head was
pushed over SSH and verified at the exact remote feature ref. Push-triggered
API specs, migration specs, CI, libnodectld specs, i18n, storage group snapshot
contract and RuboCop runs were queued/running at this checkpoint; a fresh
verification watcher owns their exact run IDs. Cross-component integration
has not run on this head, and no configuration pin or running host was
changed. The queue-ledger capacity issue was handled in a separate session,
so managed team assignments work again.

The staging-lineage vpsAdminOS provider port `107cef01f` passed focused
osctld specs 36/0, independent four-lane review with no Blocking/Important
finding, and its real `osctld/storage-activity` VM test 3/0. The separate
feature branch `2026-09-23-storage-redesign-staging-provider` is published
over SSH and its remote head verified exactly; push-triggered RuboCop and
RSpec passed. Its broad VM CI run `36236936656` had 78 expected successes and
three unexpected failures: `osctl/nfs-cancellation`, `kernel/vpsadminos` and
`kernel/livepatch-kernel-identity`; the port's `osctld/storage-activity`
result was `expected_success`. The NFS fixture expected a `hard` mount option
but the captured assertion saw `soft`. The kernel cases have a build/store
failure and a missing livepatch file respectively; their causes and rerun
disposition still need investigation. The provider patch does not touch the
NFS-specific test or kernel code.
The private test artifact is under
`/tmp/storage-os-port-ci-diagnosis/artifact`; no credential-bearing log was
copied into this record. This remains a publication/verification gate, not
evidence of a provider protocol failure. Neither the site OS pin nor a running
host was changed. vpsAdmin `fe4f9b0f9` push CI has seven successful workflows;
run 36234909917 was still in progress after 2h46m with no observed failure,
so the watcher returned an incomplete result without cancellation. The
session-owned disposable cluster
still runs the earlier reviewed `ebe4d8834` services and old-lineage
`dcad075a1` osctld, remains `read_write` at epoch 2, and can be used for
bounded freeze UI/admission testing; 5291 end-to-end trial has not run.

2026-09-26 latest checkpoint: vpsAdmin is clean and published at rewritten
feature head `ebe4d8834`, with unsigned production 5204 observer guards and a
bounded per-Dataset snapshot-name allocator folded into the owning commits.
The seven-commit history, one final additive migration and final tree passed
independent four-lane review with no Blocking or Important finding. Focused API
RSpec passed 35/0, then boundary 2/0 and separate-pool-copy 3/0; focused Node
observer/strict specs passed 88/0. The real backup-full-incremental VM passed
six examples, and dataset-migrate-retain-source passed its data-preservation
case at exact `ebe4d8834`. Push-triggered migration, RuboCop, WebUI PHPUnit,
i18n, group-snapshot contract and Node specs passed. API Specs `36230929375`
passed; selected broad CI `36230929362` remains under its watcher.
Production 5204 keeps its DB-staged guard, intent and started attempt without
a signature; 5290 and test-only strict paths still require signatures. No
production signer activation is planned.

The registered vpsAdmin feature ref fast-forwarded to the reviewed 5290/5291
commits and is clean and published at `fe4f9b0f9`. Commit `554850a49`
corrects the
existing 5290 Node catalog iteration and canonicalizes Pool GUIDs in
API capture; focused API 7/0 and Node 9/0 passed. Commit `ffcdb3774`
adds the signed 5291 API/Node probe and private advisory ActivityReport;
focused API 25/0 and Node 64/0 passed. Normal hooks passed for both commits.
Independent affected-lane review cleared the two-commit series with no
Blocking or Important finding, resolving the earlier history-split and GUID
issues. The reviewer noted advisory duplication in API GUID normalization
and the ActivityReport/Capture signer-prompt coupling. A separate,
normal-hooked `fe4f9b0f9` commit pins reviewed vpsAdminOS `dcad075a1`
provider; only its lock node rev/hash/timestamp changed. Independent
affected-lane final-head review found no Blocking or Important issue.
Push-triggered API, Node, i18n, WebUI, RuboCop, contract and selected CI
workflows are in progress. No 5291 long integration test has started.
Its report keeps `node_quiet`, `repair_ready` and executable repair false
because child lifetime is unproved.

The configuration feature branch is clean and published at `fc203cb0`:
an amended, independently reviewed guide commit and one confctl-generated
pin from the true `a65a4dfe` parent to exact reviewed vpsAdmin
`fe4f9b0f9`. The prior local `f5f107b0b` and published sibling
`e6932ddd` are retained in backup refs after an exact-lease feature push.
No shared host has been switched.
Staging/production OS pins remain unchanged. The guide accounts for
`int.vpsadmin1`, writer holds, schema-first order and rollback. It now
requires porting the osctld provider onto the current site staging OS
lineage before any staging OS pin: direct use of `dcad075a1` would discard
54 intervening staging commits. Current origin/staging is `af9543a54`,
one commit after the site OS pin. A one-commit provider port on that
lineage is prepared in an isolated worktree at `107cef01f`; focused
osctld specs passed 36/0 and normal hooks passed. Independent review and
its real VM test passed, as recorded above. Builds and dry activation of all affected
hosts remain outstanding.

The authorized disposable-cluster refresh is complete at vpsAdmin
`ebe4d8834` and vpsAdminOS `dcad075a1` on the services VM and all three
nodes. A private mode-0600 MariaDB pre-update dump remains at
`/tmp/storage-g0-preupdate-vpsadmin-20260926.sql.gz`, and old generations
were recorded. The services helper exited unsuccessfully after switching
because a payments timer hit a transient database connection interruption;
the task succeeded on retry and an explicit helper refresh restored the
cluster's ready marker. API/WebUI status and live browser login/review passed.
A new ordinary snapshot completed through the updated two-worker API without
signer unlock and exists on node1. The cluster remains `read_write`, epoch
2, with no active chains or unfinished transactions. An earlier mistaken
`update <slug> --help` was stopped during configuration build without a
switch. No shared host or production deployment occurred. See
[g0-dev-cluster-trial.md](g0-dev-cluster-trial.md).

Earlier 2026-09-26 checkpoint: the reviewed six-commit vpsAdmin feature branch
has one final additive migration. API fixture and endpoint-coverage corrections
were folded into their owning commits; reviewer0 cleared the rewritten series.
At `e29c82cfc`, the complete API topic run `36195794498` and selected broad
CI run `36195794538` passed, as did migration, i18n, RuboCop, WebUI, Node
specs and the API-to-Node group-snapshot contract. The later published
`2e4078166` adds the reviewed Node-local G1 activity observer; focused Node
tests passed 41/0, the full private-bundle Node suite passed 579/0, and its
push Node-spec and RuboCop runs passed. Its selected broad integration run
`36197858268` failed 35 storage tests. In 34 cases an ordinary snapshot got
HTTP 503: the branch made 5204 observer guards require a signature although
production has no active transaction signer. The test's single unlock reaches
only one of two Puma workers. One other test reported an unknown 5204 snapshot
preflight. This is a feature compatibility blocker, not a reason to enable
production signing. An uncommitted API/Node correction now permits unsigned
production 5204 observer receipts while retaining signed strict and operator
paths; focused verification and independent review remain pending. Old heads
`a15afb518` and `5b2814cac` remain in backup refs/recovery material.

The configuration feature branch is published at
`e6932ddd321a29d13d33de17b142d07fd02dff03`
with a confctl-generated `vpsadminServices` pin to the exact published
`e29c82cfc` head. Its parent really pins `a65a4dfe`, and the generated
changelog includes the foundation migration. The guide now accounts for
`int.vpsadmin1`, whose minimal NodeCtld also follows the service channel.
Reviewer0 cleared the rewritten two-commit guide/pin history without a
Blocking or Important finding. No shared host has been switched, and the
separate staging/production Node channels are unchanged.

The session-owned disposable storage-topology cluster is running on bridge
networking from the preceding runtime-equivalent `a15afb518` package. Its DB
has the final `20260924210000` schema and singleton control row. A bounded
authenticated API freeze trial passed: `read_write` epoch 0 became
`read_only` epoch 1 with one actor/session audit row, then returned to
`read_write` epoch 2 with a second row. A real snapshot chain remained queued
on node1's paused storage queue during the freeze; a new independent snapshot
was refused with HTTP 423 before chain/catalog/intent/ZFS effect. The queued
chain finished after queue resume. An empty cursor-bounded catch-up wrote one
requested/completed audit pair at epoch 1, while a stale request wrote none.
`db_drained` became true only after the chain finished; `repair_ready` stayed
false. Both queue and mode are restored; a new snapshot completed after
unfreeze. The fixture used two stopped VPS roots on a seeded hypervisor Pool,
not the checklist's primary-Pool fixture. Live WebUI login, status warning,
epoch-2 display and review form passed in a headless browser without a final
mode-change submission. The remaining support/delegated/scope negative cases
still need a cluster check, so record this as a partial G0 trial. The user can
inspect the control at `https://webui.aitherdev.int.vpsfree.cz/` with the
session dev-cluster credentials. No repair/APPLY or production strict mode is
enabled. Details are in [g0-dev-cluster-trial.md](g0-dev-cluster-trial.md).

The G1 provider slice is a separate vpsAdminOS read-only osctld per-zpool
GC/trash activity signal with a daemon-lifetime generation and fail-closed
unknown result. Its worktree is
registered at `worktrees/2026-09-23-storage-redesign/vpsadminos` on branch
`2026-09-23-storage-redesign`, based on
`8e44a5124439b1f3048ffc56b1717614a5360358`; the later upstream staging
rebase is still to be checked. This signal alone cannot make `repair_ready`
true or prove all node children quiet. The provider-side osctld slice is
published on that branch at `dcad075a171244cc17d67d625ab89c402d11781e`.
Its focused unit selection passed 26/0. The real UNIX-command VM case passed
all three examples after two test-fixture-only corrections, and normal
Nixfmt/RuboCop hooks passed on the amended commit. Reviewer0 cleared the
initial high-risk four-lane review and the affected-lane rerun without a
Blocking or Important finding. See
[g1-osctld-review-packet.md](g1-osctld-review-packet.md). The vpsAdminOS pin
and node rollout remain unchanged; this provider proves only GC/trash
activity, not all NodeCtld workers or child lifetime.
Push-triggered RSpec, RuboCop and the full VM workflow at `dcad075a1` are
green. The prior export fake failure was corrected in the same reviewed
provider commit. The vpsAdmin NodeCtld-local `node_activity_v1` observer is
reviewed, published as `2e4078166`, and still reports child coverage unknown;
it cannot set `node_quiet` or `repair_ready`. A separate isolated 5291
API-to-Node probe and private advisory report draft is uncommitted at
`/tmp/storage-g1-activity-probe-2026-09-23-vpsadmin`. Its first focused API
selection passed 22/0. Node ran 83 examples with one bounded UNIX parser EOF
failure; implementer0 corrected that failure and a narrow rerun is pending.
The report always marks quiet/readiness/apply false, even on complete
`gc_trash_v1` evidence, because child lifetime remains unproved.

The paragraphs below preserve earlier checkpoints and are superseded where
their refs or in-progress statements differ from this latest checkpoint.

2026-09-25 checkpoint: the unpublished vpsAdmin feature ref and registered
worktree now point to the reviewed six-commit head `a15afb518`, above
`origin/master` `7045c81b3`. The isolated replay branch remains at that head.
Its single final foundation migration is
`api/db/migrate/20260924210000_add_storage_integrity_foundation.rb`; four
transitional migrations, the host freeze launcher and unused reconciliation
decision/action schema are absent. The former 25-commit unpublished history
was replaced in an isolated replay; the replacement series preserves the
final 163-path feature patch except for two corrected v4 registry test fixtures.
The old head is preserved in a verified recovery bundle and local
`backup/2026-09-23-storage-redesign-pre-six-commit` ref. All six focused
commits passed normal Nix/Overcommit hooks, and both worktrees are clean.

Clean-head quick verification: focused ordinary API/model/resource specs
passed 76/0 and focused Node registry/receipt/settlement/inventory/Command
specs passed 122/0 using an isolated Bundler directory; the predecessor
migration passed 4/0 and fresh-schema bootstrap 2/0 on the clean head;
attempt provenance passed 3/0 on the identical source patch,
WebUI PHPUnit 5 tests/17 assertions, and CI selector 18 runs/77 assertions.
The initial shared Node gem directory could not load `i18n` before any test;
the isolated rerun is green. Retained reviewer0 (GPT-6 Sol/xhigh) completed
the independent high-risk four-lane review of `7045c81b3..175111ee7`.
It found one **Blocking general/architecture/scope history issue**: the
17,073-line functional commit combines independently reviewable foundation,
observer, advisory, freeze UI/API and test-only strict work. It found no other
Blocking or Important functional defect. Reviewer0 then reviewed the six-commit
replacement across all four lanes and found the history finding resolved,
with no remaining Blocking or Important finding. The final feature ref was
moved only after that review and exact final-tree comparison.

The isolated replay has six committed groups. It starts with
foundation/bootstrap commit `0ebec78ec`, paired
observer writer/settlement commit `a669bc76e`, advisory
inventory/reconciler commit `163bf3457`, authenticated API/WebUI freeze
commit `f07b23899`, test-only strict/contract commit `0aa5d334c`, and lasting
docs/AGENTS commit `a15afb518` at
`/tmp/storage-review-split-2026-09-23/vpsadmin`. All normal Nix/Overcommit
hooks passed; group-2 focused API and Node selections passed 72/0 and 82/0,
group-3 selections passed 65/0 and 54/0, and group-4 API/WebUI checks passed
36/0 and 5 tests/17 assertions. Group-5 focused API and Node selections
passed 11/0 and 107/0. The group-3 API watcher did not
retain its log despite reporting an exit-0 RSpec summary; the Node log is
retained. Final-headed migration and bootstrap checks passed 4/0 and 2/0 in
separate disposable DB processes. The real API-to-Node v4 contract passed
1 API and 3 Node examples (0 failures) on `a15afb518`; its private DB teardown
succeeded. The final 163-path
name/status manifest matches the old reviewed head exactly, as does every
binary patch outside the two authorized Transaction fixture lines. Retained
reviewer0 cleared all four lanes on the six-commit series and intermediate
dependencies; [final-vpsadmin-series-rerun-packet.md](final-vpsadmin-series-rerun-packet.md)
records the evidence.
Push-triggered CI then found two failures in the full libnodectld spec run
`36179658050` (569 examples, 2 failures, seed 58529): both DatasetExpander
examples call the new freeze-row DB check through `NodeCtld::Db.open`, while
their `FakeCfg` has no `db` key. The failed-attempt log was downloaded before
any rerun to private `ci-node-failed.log`. Implementer0 is investigating and
preparing a narrow correction in the isolated replay worktree so the running
dev-cluster build continues from the reviewed clean head. The CI run is not
accepted as green.
During group-2 staging, implementer0 found two Transaction/TransactionChain
test fixtures still construct an eight-field registry entry after v4 added
two strict-direction fields. The lead authorized the narrow two-spec fixture
correction in the owning observer commit, with a documented final-patch delta
and focused test run. No production runtime difference is planned.

The branch is **not ready for production repair or merge**. Production strict
dispatch, verified-scope publication and repair APPLY remain disabled;
`db_drained` is DB-only. The next integration gate is a disposable
storage-topology dev-cluster API/WebUI freeze trial after review, ending back
in `read_write`. Architect0 prepared a G0 checklist covering admin auth/CAS,
a paused preexisting chain, new admission refusal, DB-only status, audit and
queue/mode recovery. Node/child/GC quiet and repair remain outside G0. The
reviewed vpsAdmin feature branch was pushed at `a15afb518`; the session-owned
storage-topology cluster start is running on bridge after a fresh no-disk/no-VM
preflight. No shared host has been switched. See
[final-vpsadmin-review-packet.md](final-vpsadmin-review-packet.md) for the
full branch inventory, [g0-dev-cluster-trial.md](g0-dev-cluster-trial.md) for
the session trial checklist, and the separate configuration deployment guide
for prepared site ordering.

The lasting storage explanation and schema reference are committed in
vpsAdmin `a15afb518` after normal hooks. The site rollout guide is committed
in configuration `57c6cb9c`; independent affected-lane review cleared its
host-specific writer hold after the guide added active API task timer and
service holds, and post-switch verification. The configuration feature branch
now has generated `confctl` channel-pin commit `3b492f0d` for exact
`a15afb518`; only the `vpsadminServices` lock entry changed. Reviewer0
cleared the full configuration feature series with no Blocking or Important
finding, and the feature branch was pushed. No shared host was switched.

Architect0 checked the canonical KB WebUI contract against this
superadmin-only Cluster control. Its member-page and capture routes do not
include this action, so no bilingual KB candidate or capture-contract change
is required for G0 or solely for this control's later release. Any later
member-visible denial or navigation change needs a fresh visibility check.

Lead/reviewer rules are committed in workspace `04b0e5c6` and canonical
extension `dcb2762`; workspace `3f539b0` pins the published extension SHA.
The composed Nix package and agent-policy checks passed, and reviewer0 found
no remaining source/package-level issue. A user-profile switch was attempted
with `workspace-host switch --source`, but its lifecycle guard refused this
in-progress thread and restored the old package. The installed skill and
shared-root AGENTS remain old. Existing retained members also keep their
saved role instructions, so the lead must send the final branch-review
packet explicitly. Package activation and default-branch integration remain
separate later steps; neither has been claimed complete.

Architect0 recorded the next node-inclusive quiet-observation design in
`storage-integrity-design.md`. It requires a read-only osctld activity signal
and cannot turn the current DB-only `db_drained` result into repair readiness.
No G1 probe, osctld interface, repair APPLY or strict production dispatch is
implemented by this checkpoint.

## Earlier verified observer work and completion decision

2026-09-25 completion work started after the user confirmed that the 22
vpsAdmin feature commits and five migrations have not been deployed and asked
for a clean branch, permanent lead/reviewer instruction fixes, clear system
documentation, a prepared configuration channel pin, an early dev-cluster
freeze trial, and the complete guarded repair path. The existing branch at
`52ae80dda` is observer-only: production strict dispatch is off,
`repair_ready` is false, and reconciliation cannot APPLY. It is not ready
for production repair or merge as the finished project.

The retained roster was checked. Architect0 owns a read-only final schema,
repair-gate and review-rule design audit. Implementer0 owns the bounded
vpsAdmin foundation migration cleanup, without committing or rewriting
history. The lead owns workspace/canonical instruction changes, branch
coordination, the configuration runbook and dev trial. Reviewer0 remains
independent and will review the complete cleaned branch and subsequent
changes. No production or shared-int deployment, merge, or APPLY is
authorized. The next gates are instruction changes, schema consolidation,
quick verification, branch-wide reviewer assessment, then the disposable
dev-cluster freeze trial.

The authenticated API and WebUI storage-freeze replacement is committed at
vpsAdmin `52ae80dda`; its worktree was clean before consolidation. Both freeze CLIs and the
root/sudo launcher are retired. The API records an active administrator and
direct session for mode changes, requires the current freeze epoch, and exposes
bounded DB-only status. The WebUI shows that status and reviews mode changes;
observer catch-up remains an explicit API action. The consolidated foundation
migration must precede the new API, and all API workers must upgrade before
operators rely on read-only admission. This interface passed its focused
verification, but the whole feature branch remains unfinished. The vpsAdmin feature branch was not pushed or deployed at that checkpoint.
Production strict dispatch and repair APPLY remain disabled.

Retained reviewer0 (GPT-6 Sol/xhigh) independently reviewed
`242c2a919..53ba33407` at high risk because this change affects authorization,
audit schema, the API/WebUI contract and mixed-version admission. The general,
architecture, scope and risk/compatibility lanes found no Blocking or Important
issue. Two Advisory findings concerned an older host-operator paragraph and
generated English API labels/descriptions. Both were corrected in the amended
`49bcbb25c` commit. This narrow documentation/metadata fix did not require a
review rerun. The fresh-schema migration spec passed 4 examples, the API
resource 13, adjacent
API/model/status specs 50, and WebUI PHPUnit 5 tests/16 assertions. API i18n
health, targeted RuboCop, syntax checks, CI selector, Nix evaluation and normal
commit hooks passed. The first services-VM browser run failed because its new
test searched for the safety caveat in `#content-in`; the template renders it
visibly in the adjacent `#perex`. The corrected locator, visibility check and
warning-body check are committed in `52ae80dda`. Retained reviewer0 rechecked
the general and architecture/test lanes at `3c437c723`, found no Blocking or
Important issue, and suggested the latter two narrow assertions. Normal hooks
passed after that direct review remediation. The disposable services-VM
`webui#admin-cluster` browser run passed on `52ae80dda` (exit 0, about 18
minutes), including the new freeze page and mode-change review flow.

The production KB inventory fetch found 114 Czech and 77 English pages; the
only Cluster references concern member resource views or API listings, with
no current freeze control/page/capture binding. No KB candidate or production
write was prepared. Project behavior and rollout limits are documented in
[integrity-foundation.md](../../worktrees/2026-09-23-storage-redesign/vpsadmin/docs/storage/integrity-foundation.md).

Implementation authorized on 2026-09-24. The approved first phase is the
existing storage catalog plus verified physical identities, vpsAdmin mutation
guards, one rerunnable reconciliation engine and a simple storage read-only
toggle. Bootstrap and later repair use the same engine. User snapshot deletion
and backup scheduling changes are deferred. No production reconciliation apply,
storage mutation, deployment or default-branch merge is authorized by this
implementation request. [plan.md](plan.md) holds the current contract;
[storage-integrity-design.md](storage-integrity-design.md) records the
architect's reconciled first-phase design.

The local storage-freeze operator launcher passed its isolated services VM
integration test on vpsAdmin `4a28d0e6a`; this verifies the test deployment's
sudo identity transfer, audited mode changes and catch-up path. It is not a
fleet freeze or repair-ready proof. The test-only NodeCtld strict pre-dispatch
refusal slice is committed as `df0a98b15`. Independent mandatory review found
no Blocking or Important issue. Production strict activation, verified scope
publication and APPLY remain disabled. The next strict 5204 provenance slice is
committed as `8c29cf196`; affected-lane independent review found no remaining
Blocking or Important issue. Its nullable
attempt markers distinguish strict execution from an observer receipt, and
final chain closure can prove one earlier strict snapshot alongside harmless
members. Migration and model specs passed 3 examples each; the focused Node
receipt and Command selection passed 86 examples after the target-shape fix.
Normal amend hooks passed. The migration must precede new NodeCtld binaries;
strict production dispatch is still off. Test-only paired strict 5215 group
snapshot handling is committed as `33fe64fdd`. It covers one sole-member
chain with 1–32 exact SIP/DIP targets and per-target execute/rollback
observations. Production 5215 retains its old observer input and opaque
targets. Final focused API specs passed 15 examples, Node specs passed 111,
and all normal commit hooks passed. Independent reviewer0 (Sol/xhigh) covered
general, architecture, scope and risk at high severity and found no Blocking
or Important issue. One Advisory dead handler fallback was deleted in the
amended commit; focused handler specs passed 9/0, and the normal hooks passed
again. The isolated API-to-Node 5215 contract is committed at `242c2a919`.
It passed against one disposable MariaDB instance: API producer 1/0, Node
consumer 3/0, with fake physical inventory and ZFS effects. Independent
reviewer0 (Sol/xhigh, high risk, all four lanes) found two Important test
harness issues: teardown could discard a failed DB stop, and the dedicated
workflow missed a receipt dependency. The amended runner retains a failed
stop and checks that its private TCP port is closed before deleting state;
the workflow now watches the direct dependencies. Fake teardown checks,
selector 18/77, normal hooks, and the committed full contract passed.
This verifies the signed API-to-DB-to-Node shape, not host ZFS or a fleet
cutover. No production activation has followed.

Implementer0 owns vpsAdmin source edits in the session feature worktree.
Architect0 owns design validation and the session design document. The lead
owns coordination, tracking and review. The vpsAdmin worktree was created at
`486350466e8fb6f966add1cde3fa2bc12b4d6b62` after fetching `origin/master`;
its registration is complete in `portal.yml`. The initial helper invocation
created the worktree but stopped on an Overcommit configuration-signature
check. After reading `.overcommit.yml`, the lead ran
`nix develop .#vpsadmin -c bundle exec overcommit --sign` and retried the
helper successfully. The first source commit passed its pre-commit hooks in
the lead's Nix shell after the implementer prepared and staged the changes.

Inventory branch ready, awaiting merge approval for
`vpsfree-maintenance-tasks` `master`.

The read-only backup inventory has been run against a production DB capture
and `backuper2.prg` ZFS capture supplied by the operator. The corrected offline
comparison contains 660 diagnostic findings. See
[investigation.md](investigation.md#read-only-production-inventory-2026-09-24)
for the evidence and interpretation. The private version 2 report is at
`tmp/storage-inventory-report-v2.jsonl` outside the initiative tracking tree;
raw captures and report must not be committed or exposed through the portal.
The [task guide](../../worktrees/2026-09-23-storage-redesign/vpsfree-maintenance-tasks/2026-09-24-storage-inventory/README.md)
documents capture and report semantics.
The DB collector now uses vpsAdmin API models for application rows, following
the repository's maintenance-task pattern. Its few direct SQL statements set
the read-only snapshot and capture DB connection/time metadata.
This session has not connected to production or changed live state. It read the
operator-supplied captures locally. The DB and ZFS observations were separate;
their comparison is diagnostic, not proof of one consistent instant or
permission to delete a snapshot. The follow-up comparator corrections are
pushed to the feature branch and await merge approval.

The current first-phase design retains existing SnapshotInPool and
SnapshotInPoolInBranch meanings and adds physical identity and clone-origin
evidence on catalog-owned rows. The design document is reconciled to this
scope. Snapshot deletion and backup dispatch remain later, separate work.
The requested integrity boundary covers vpsAdmin-initiated commands,
including its osctl wrappers; independent osctld and root ZFS mutations are
outside this guarantee. Backup dispatch remains separate later work.

## Repositories and ownership

- `vpsfree-maintenance-tasks`: worktree
  `worktrees/2026-09-23-storage-redesign/vpsfree-maintenance-tasks`, branch
  `2026-09-23-storage-redesign`, base `2fdc9f2`, current head
  `a457cfc3aa4431565d65d6bbe9f4e63f8d8d327e`, pushed to `origin`.
  The worktree is clean. No merge or deployment occurred.
- `vpsadmin`: session worktree
  `worktrees/2026-09-23-storage-redesign/vpsadmin`, branch
  `2026-09-23-storage-redesign`, base `486350466e8fb6f966add1cde3fa2bc12b4d6b62`,
  current head `52ae80dda` (additive
  foundation, observer writer, advisory reconciler, offline proof planner,
  versioned effect registry, DB drain and audited operator controls);
  registered in `portal.yml`. No push, merge or deployment occurred.
- `vpsadminos` canonical bare HEAD `2166e5934fe1`: reference review only.
- `architect0` supplied physical graph and migration design, scheduler
  feasibility came from `implementer0`, and a fresh writable agent wrote the
  first inventory commit. After the environment update, retained
  `implementer0` wrote the model-based revision and reviewer fixes;
  `architect0` assessed its transaction and runner assumptions. The lead
  handled coordination, review integration, and tracking.

This conversation is bound to `2026-09-23-storage-redesign`, as checked with
`dev-session current` and the environment identity. The older session named
in the request was not accessed. The environment update allowed the retained
architect and implementer to verify this session with `dev-session current`
before accessing its worktree.

## Verification and review

- Earlier model-based collector revision: 24 tests and 104 assertions passed;
  Ruby syntax, `git diff --check`, and the README shell-block syntax check
  passed. The final comparator revision is verified below.
- Fetched `origin/master`; it remained at base `2fdc9f2`. Captured the
  repository comparison at base `2fdc9f2` and head `f5440b4`.
- The repository has no GitHub Actions workflows. `gh run list` returned no
  branch runs after push.
- Mandatory review classified the change **high risk** because it reads a
  production database and storage host and emits sensitive topology. A fresh
  independent standalone reviewer from the installed default development
  team's review role, GPT-6 Sol/xhigh, covered general, architecture, scope,
  and risk lanes. Retained read-only peers had reported `dev-session current`
  EROFS failures, so the retained reviewer was treated as unverified.
- Initial review found a blocking missing DB-to-ZFS branch-origin comparison
  and important host-scope, metadata-integrity, and ZFS-type checks. The
  implementation agent fixed them and broadened scoped lock capture. A review
  rerun confirmed those fixes, then found short hostnames could collide and
  asked for one cohesive unpublished commit. The final focused fix requires
  a qualified hostname and rejects short aliases; collision and failure tests
  pass. The two unmerged commits were folded into the single final commit.
  Review covered original `69dac3e` and remediation `86a7612`; their final
  equivalent plus the narrow host-scope reduction is `4ff9b48`. The narrow
  final fix did not require another review rerun.
- The user's model-based correction is committed as `883b846`, followed by
  focused review fixes in `f5440b4`. These are separate commits because
  `4ff9b48` had already been published. Retained reviewer0 (GPT-6 Sol/xhigh)
  independently reviewed `883b846` in the general, architecture, scope, and
  risk lanes at **high risk**. The reviewer found a blocking relative output
  path that fails under the API runner's service user/package CWD and an
  important missing Snapshot resource-lock scope. The implementer added an
  absolute-path CLI check, a private service-user-owned output recipe, and
  Snapshot lock capture with focused tests in `f5440b4`. These are direct,
  narrow fixes; no review rerun was needed. Reviewer0 could not run tests in
  its read-only shell, so the lead reran the passing suite in the writable
  environment.
- Operator captures passed checksums, scope and identity checks. The initial
  private comparison yielded 821 findings. The first follow-up commit
  `12cb437` fixed head-tree, unresolved parent and reference-count scope
  classifications; independent reviewer0 (GPT-6 Sol/xhigh) reviewed the
  general, architecture, scope and risk lanes at high risk, finding two
  Important issues: unresolved pointers also produced unrepresented physical
  edge findings, and pending references could produce a false firm undercount.
  The narrow remediation `a457cfc` fixes both and documents the distinction.
  Its 42-test/165-assertion offline suite passed in the lead's environment,
  along with diff checks. A review rerun was not needed for the direct,
  focused fixes. The corrected comparison yields 660 findings; its version 2
  JSONL report was verified by the Reader and has mode 0600. No integration
  or production commands were run by the team.
- Fetched `origin/master` at `2fdc9f2`, pushed feature head `a457cfc`, and
  captured its comparison at base `2fdc9f2`. `gh run list` returned no
  workflow runs for the branch; this repository has no GitHub Actions
  workflows. The worktree is clean.
- Follow-up design review by architect0 separated logical history from physical
  identity and ZFS clone edges, specified scoped validation, journaled guarded
  mutations and repair classes for the observed anomalies. Implementer0 mapped
  topology-changing handles, including receive `-F`, clone/promote and its
  rollback, export clone lifecycle and osctl-backed VPS operations. The user's
  latest scope correction excludes independent osctld/root operations;
  vpsAdmin-invoked osctl work remains covered. Architect0 and implementer0
  confirmed that SIP is one logical snapshot per DIP while a backup SIP may
  have several SIPB branch occurrences. A minimum additive schema can enrich
  SIP/SIPB with observed identity rather than duplicate every known snapshot.
  No source code, production state or private capture changed in this design
  step.
- Foundation migration and models committed as `cdeb6d616`. In isolated local
  MariaDB, core-only schema load and migration passed; separate migration and
  model specs passed 3 and 10 examples respectively. `api/db/schema.rb` was
  generated by the migration. All pre-commit hooks passed after RuboCop fixes;
  the commit-message hook reported text-width warnings only. Linked physical
  identity remains unpublished during mixed old-writer operation. This code
  does not yet guard writers or reconcile storage.
- Observer writer slice committed as `aab70d711`. It classifies vpsAdmin
  storage transactions, rejects new classified writes through a durable global
  read-only admission row, records observer intents, and gives nonbackup
  CreateSnapshot (5204) an identity-bound node receipt. It does not publish
  physical catalog identities or mark scopes verified. Ordinary proved
  compensation and unprovable attempts are distinguished; hard kills and
  receipt-start failures leave fatal chains and needs-reconcile evidence.
  Focused NodeCtld specs passed 63 examples and API admission/detach specs
  passed 11 examples after the final receipt fix. The normal Nix Overcommit
  pre-commit hooks all passed. The first commit attempt exposed locale ordering;
  the implementer normalized the two new messages before the successful hook
  run. Retained reviewer0 (GPT-6 Sol/xhigh) independently reviewed foundation
  `cdeb6d616` and original writer head `58eb29a8f` at high risk across general,
  architecture, scope and risk lanes. The review found no Blocking or Important
  issue and one Advisory documentation contradiction about when read-only
  admission is enforced. The implementer corrected only that description and
  the lead amended the unpublished writer commit to `aab70d711`; all hooks
  passed again. That narrow correction did not alter runtime behavior and did
  not require a review rerun. Residual limits are mixed-version unverified
  scopes, opaque handles, and no strict legacy-handle refusal, reconciler or
  production freeze/drain CLI. No long integration test has started.
- Architect0 specified the next observer reconciler slice as signed two-pass
  whole-zpool capture, consistent API-model DB capture, private complete-only
  artifacts, compare and dry-run. The CLI will run as the existing Supervisor
  service user, prompt for the signer passphrase on its TTY, and use that
  service's broker config. It uses one private persistent HMAC key for opaque
  disk-only finding IDs; loss blocks replay and requires a new capture. The
  stream uses broker confirms and fsynced consumer checkpoints before manual
  ACK, without a reverse node ACK route. Implementer0 committed this advisory
  slice as `daefd242e`. It has no repair/apply path, physical catalog import or
  verified-scope assertion. The signed 5290 command persists the old `storage`
  queue name, allowing old nodes to fail with Unsupported command; upgraded
  nodes route it to their dedicated inventory queue. Quick Nix checks passed
  32 API and 50 NodeCtld examples; CI selection passed 17 tests/76 assertions,
  and normal hooks passed. The additional queue compatibility spec omitted from
  the initial API selection failed because it inspects validation errors on a
  different Transaction instance from the one validated. Implementer0's
  narrow test correction checks a persisted inventory transaction and the
  same invalid instance; the lead's Nix rerun passed 2 examples. Retained
  reviewer0 (GPT-6 Sol/xhigh) completed the required high-risk general,
  architecture, scope and risk lanes on `daefd242e`. The reviewer found no
  Blocking issue and three Important advisory-report defects: normal
  Pool::Create structural filesystems appear disk-only; a fatal pending 5204
  snapshot can appear as separate DB-missing and disk-only findings; and an
  interrupted or repeated offline report publication cannot be rerun against
  its complete capture. Implementer0 committed focused remediation as
  `10819d32c`: exact structural paths are excluded while unknown children
  remain visible; pending-name candidates remain unresolved; and matching
  offline outputs can be reused or completed after interruption. The lead's
  focused Nix API run passed 19 examples, all normal commit hooks passed, and
  the worktree is clean. Reviewer0 reran affected general, architecture and
  risk lanes directly and confirmed all three findings resolved, with no new
  Blocking or Important issue. The reviewer found no apply/approve,
  disk-only DB import, verified-scope or deletion behavior. Representative
  Rabbit, ZFS, Supervisor and failure-window checks remain future
  verification. No production capture or apply is being run.
- Architect0 defined the plan-only proof layer in
  `storage-integrity-design.md`: private deterministic candidate actions from
  the same sealed capture, all seven observed finding classes, no guessed
  logical parent or disk-only import, and no executable or DB action.
  Implementer0 committed it initially as `35f579856`. Focused Nix API specs
  passed 43 examples and all normal pre-commit hooks passed after style
  corrections.
  Retained reviewer0 (GPT-6 Sol/xhigh) independently reviewed the commit at
  high risk across general, architecture, scope and risk lanes. The reviewer
  found no Blocking issue and two Important issues: existing-origin proposals
  lack a full-node uniqueness blocker and negative claim check, and repeated
  full-table scans can make planning quadratic at the supported inventory
  size. Implementer0 corrected both and the lead amended the unpublished
  commit to `662e906b8`: every origin candidate carries a full-node claim
  blocker and locked negative owner/path/digest preconditions; one-time indexes
  replace repeated occurrence and identity scans while retaining duplicate
  detection. Focused Nix API specs passed 49 examples, targeted RuboCop found
  no offenses, and all normal hooks passed. Reviewer0 reran the affected
  general, architecture and risk lanes and confirmed both Important findings
  resolved with no new Blocking or Important issue. Every candidate remains
  non-executable; this commit does not approve or apply a repair.
  Architect0 also specified the registry/admission and
  read-only/status/drain CLI slice now being implemented.
- Effect-registry/admission commit `9ef414361` adds versioned execute and
  rollback classifications across API and NodeCtld, covers previously missed
  VPS runtime/network and export routes, and separates read-only admission
  from physical/dependency/catalog verification impact. Opaque node effects
  now record every existing Pool scope in one atomic staging transaction;
  data/config-only writes can be refused during read-only mode without
  invalidating the ZFS graph. Focused Nix API specs passed 44 examples and
  NodeCtld specs 38 examples; CI selector and normal hooks passed. Strict
  dispatch remains off. `130a622f9` adds generic settled-unverified intent
  lifecycle, fair explicit catch-up, read-only DB drain reporting, and frozen
  admin-chain gates. Its additive migration must precede upgraded NodeCtld.
  `40d583c31` adds a root-owned fixed Nix launcher, narrow optional sudo
  operators, host-UID audit events and an epoch-CAS toggle. The transition
  history is application-append-only. Focused migration and API specs passed
  4 and 40 examples; the Nix launcher check, CI selector and normal hooks
  passed. Strict dispatch, production deployment and repair readiness remain
  disabled. Architect0's design keeps DB-drained separate from node/physical
  repair readiness.
- Reviewer0 independently reviewed `9ef414361` through `40d583c31` at high
  risk across general, architecture, scope and risk lanes. The review found one
  Blocking issue: opaque backup snapshot 5204 intents could not reach generic
  terminal settlement, so routine completed work could prevent DB drain. It
  also found one Important issue: API-only unsupported handle 5225 could be
  staged in read-write mode. Implementer0 fixed both in `75504f32b`. An opaque
  5204 now needs positive backup-Pool, guardless input, complete observer
  target/scope and no-attempt evidence plus terminal chain proof; guarded or
  ambiguous work remains prepared. Handle 5225 refuses before parameters or
  staging. Focused Nix API checks passed 51 and 14 examples; NodeCtld passed
  10 examples with an isolated gem path. All normal commit hooks passed.
  Reviewer0 reran all four affected lanes on `75504f32b` and confirmed the
  original findings resolved, then found one Important reporting defect:
  malformed prepared backup 5204 was absent from the catch-up page, so the
  privileged command could report success while DB drain remained blocked.
  Implementer0 fixed bounded page reporting in `14124a297`: every prepared
  chain is scanned and an ineligible 5204 is reported blocked, while the CAS
  settlement update remains limited to proved generic intents. Focused Nix
  API and NodeCtld checks passed 25 and 12 examples, including malformed-only,
  cursor, CLI exit and two-Pool cases; all normal hooks passed. Architect0
  aligned the session design. This direct, requested reporting fix did not
  change settlement authority, so no further reviewer rerun is needed under
  the mandatory review procedure. The isolated launcher VM test is next.
- The single-services-VM launcher fixture is committed in `51559d887`.
  It tests the installed fixed sudo launcher, numeric OS actor preservation
  across `systemd-run --uid`, literal reason bytes, freeze and catch-up audit,
  root-console unfreeze, and unauthorized routes. The test runner selected
  only `admin/storage-freeze-launcher` under its exact filter; Nix evaluation,
  syntax, CI selector and normal commit hooks passed. Retained reviewer0
  (GPT-6 Sol/xhigh) reviewed the original `19041d0b3` at high risk across
  general, architecture, scope and risk lanes. The reviewer found no Blocking
  issue and one Important gap: a NOPASSWD regression would pass the positive
  sudo test. The amended fixture now first attempts the valid launcher with
  `sudo -k -n` in a fresh operator PTY, requires a password refusal, and
  checks that mode and audit rows did not change. Quick checks and normal
  hooks passed again. This direct negative test follows the reviewed path
  and adds no application or launcher behavior, so no review rerun was
  needed. The reviewer also noted that the exact selector rule is redundant
  with the existing broad admin rule; this conservative broad selection is
  accepted. The first isolated VM integration run on `51559d887` failed
  before reaching sudo: the fresh services DB had a
  `storage_freeze_controls` table but no singleton row. The Nix setup loads
  the current `schema.rb` and then runs migrations; the foundation
  migration's row INSERT is skipped when the schema version is already
  current. This also affects fresh installs using that path. Architect0
  specified the bootstrap boundary, and implementer0 prepared it in
  `1db225c47`: an idempotent API Rake task now inserts row 1 only in the
  fresh-schema Nix branch, after schema load and before the setup marker.
  Repeated invocation preserves a frozen mode, epoch and audit; established
  databases still fail closed if their row is missing. The focused Nix spec
  passed 2 examples, targeted RuboCop found no offenses, and normal hooks
  passed. Retained reviewer0 (GPT-6 Sol/xhigh) reviewed `1db225c47` at high
  risk across general, architecture, scope and risk lanes, finding no
  Blocking or Important issue. The reviewer confirmed the fresh-only Nix
  branch, pre-marker failure handling and unchanged established row. The
  source-order spec is not runtime fault injection, so the isolated VM rerun
  remains necessary. The Rake task is manually callable by a DB writer;
  it is intended only for fresh-schema bootstrap and must not be used to
  reset an established database with a missing control row. The failed VM
  was disposable; no production system was involved.
- The second isolated services VM run on `1db225c47` confirmed fresh setup
  created the singleton (`id=1`, read-write, epoch 0). It then timed out in
  the fixture's passwordless negative test: util-linux `script` inherited
  an open test-harness stdin and did not exit within 240 seconds. This is a
  PTY harness failure before the intended sudo refusal assertion, not
  evidence that the launcher granted access. Implementer0 added explicit
  stdin EOF while retaining the real PTY and valid command. The
  narrow fixture correction is committed as `1aa45864f`; it gives the
  passwordless `script` invocation `</dev/null` and bounds expected refusal
  to 30 seconds. Nix parse, embedded Ruby syntax, CI selector and normal
  hooks passed. This direct harness correction follows the reviewed
  negative-test path and does not change application authority, so no
  reviewer rerun is needed before another isolated VM attempt.
- The third isolated VM run on `1aa45864f` reached sudo. The `sudo -k -n`
  check refused within 0.31 seconds with a password-required message and
  left the DB unchanged. The following authenticated `sudo -l` failed:
  piping the test password into util-linux `script` sent it before sudo
  opened its prompt, so sudo saw no password. The positive helper now uses
  Expect to wait for the prompt, send the disposable password on a PTY,
  redact captured output and propagate the child exit status. A local
  dummy-prompt check proved success exit 0 and wrong-password exit 9. The
  fixture change is committed as `9d73d4e17`; normal hooks passed. Retained
  reviewer0 (GPT-6 Sol/xhigh) found one Important fixture gap across the
  general/risk lanes: a quiet command could exhaust Expect's 30-second
  prompt timeout after authentication, and negative tests accepted any
  nonzero result, including helper timeouts. The narrow fix is committed as
  `4013f10fa`: Expect now uses a separate 180-second completion deadline,
  distinct internal failure codes, and negative checks require the expected
  sudo or launcher denial text. Local Expect smoke covered a quiet child,
  wrong password and both timeout paths; Nix parse, CI selector and normal
  hooks passed. Focused direct inspection confirmed the requested correction
  without an application or authority change, so the review workflow did not
  require another independent rerun. The next isolated VM run on `4013f10fa`
  again reached the sudo checks. It failed in the generic-runner negative:
  `sudo -l /run/current-system/sw/bin/vpsadmin-api-ruby` exited 1 but emitted
  only the password prompt, while the preceding full sudo listing showed just
  the fixed launcher with PASSWD. The fixture expected denial prose and
  therefore rejected a real sudo refusal. The narrow `e7c1f929c` fix now
  requires exact status 1 for that `sudo -l` check while retaining distinct
  helper-timeout rejection. Local prompt-only refusal smoke, Nix parse,
  selector and normal hooks passed. The next isolated VM run on `e7c1f929c`
  passed the authenticated sudo read-only transition, the empty catch-up
  audit and the remaining sudo negatives. It then hung on the fixture's
  direct-root stale-epoch call, which invokes `systemd-run --pty` without a
  controlling PTY, until the harness's 240-second command timeout. The
  disposable runner also stalled during cleanup; after the test had recorded
  `unexpected_failure`, the lead authorized termination of only that failed
  runner and its disposable VM processes. All identified processes exited;
  logs remain under `/tmp/storage-freeze-vm-silent-sudo-denial.log` and
  `/tmp/os-test-runner/os-test-admin__storage-freeze-launcher-5a6b1ad7/`.
  The narrow `4a28d0e6a` fixture fix now gives both direct-root calls a
  closed-stdin PTY through util-linux `script -e` while preserving command
  status, root UID and the stale-epoch assertion. Nix parse, embedded Ruby
  syntax, selector and normal hooks passed. The isolated services VM test
  passed on `4a28d0e6a` (`./test-runner.sh test admin/storage-freeze-launcher`,
  exit 0, one example in 53.01 seconds; full runner 585 seconds). It exercised
  the authenticated nonwheel sudo transition, exact literal reason bytes,
  requested/completed catch-up audit, direct-root stale refusal and unfreeze,
  and the negative authority routes. Full log is
  `/tmp/storage-freeze-vm-root-pty.log`. No production action occurred.
  The lead invoked three narrow fixture commits (`4013f10fa`, `e7c1f929c`,
  `4a28d0e6a`) with `git commit -m` instead of the repository-required
  temporary message file plus `-F`. Their normal hooks and commit-message
  checks passed; no hook was bypassed. Future commits must use `-F`.
- The test-only strict NodeCtld pre-dispatch slice is committed as
  `df0a98b15`. Paired API/Node registry version 3 support states and a signed
  5204 guard version precede exact target, owner and receipt checks. A bounded
  same-transaction chain-closure gate prevents a no-op rollback or read-only
  tail from releasing locks after an earlier unproved effect. Strict fatal
  chains retain signatures and locks and skip confirmations. Architect0's
  pre-commit check distinguished deterministic binding refusals from
  uncertain DB reads or prior started attempts; the former close fatal
  without phase 5, and the latter quarantine a validated intent if the DB
  save succeeds. The final focused Nix API registry/admission suite passed
  24 examples and the Node receipt/Command suite passed 64 examples. Ruby
  syntax, CI selector (17 tests/76 assertions), diff checks and all normal
  commit hooks passed. The first hook run reported RuboCop offenses; the
  implementer corrected only style before the successful `git commit -F`.
  Independent reviewer0 (Sol/xhigh, general, architecture, scope and risk
  lanes) reviewed `4a28d0e6a..df0a98b15` at high risk and found no Blocking
  or Important issue. The reviewer confirmed strict dispatch is reachable
  only through test constructor injection, unknown/unsupported directions
  refuse before a handler is built, and fatal closure retains locks and
  signatures without confirmations. A later member after a completed strict
  5204 is conservatively refused because current chain proof accepts only
  the active guarded member; this is a documented narrow limit. No long
  strict integration test, production strict switch, scope verification or
  apply was added.
- The next test-only strict 5204 receipt slice is committed as `8c29cf196`.
  Nullable attempt columns hold registry version 3 and the exact signed input
  digest only for a strict started attempt; old and observer attempts remain
  null. An ActiveRecord validation prevents later marker updates. Final chain
  proof accepts one strict 5204 anywhere among harmless members after checking
  the retained signature, exact two-target API manifest, owner identity,
  marked attempts and terminal physical observations. The additive migration
  must precede new NodeCtld. Quick checks: migration 3/0, API model 3/0,
  API admission 17/0, Node receipt/Command 86/0, CI selector 17/76,
  Ruby syntax and normal Nix hooks green. Initial mandatory review by retained
  reviewer0 (Sol/xhigh; high risk; general, architecture, scope and risk)
  found a Blocking API/Node mismatch: the original Node fixture had one
  target, but API stages a Pool observer target plus a DIP snapshot target.
  The amended commit preserves that producer contract, validates both targets
  and scope links before the effect and at closure, and adds matching API/Node
  fixtures. Reviewer0's affected general/architecture/risk rerun found the
  blocker resolved and no new Blocking or Important findings. No real
  API-staged strict command has run against host ZFS; production strict,
  verified scopes and APPLY remain disabled.
- The test-only 5215 group snapshot slice is committed as `33fe64fdd`.
  Paired registry version 4 signs an exact 1–32-member manifest only through
  an internal default-false API test hook. Production observer 5215 retains
  its original payload and opaque targets. Node strict dispatch requires one
  persisted chain member, exact owner/target evidence and a durable started
  attempt before ZFS. It records each member's physical result, rechecks each
  identity before rollback destroy and defers logical snapshot naming until
  terminal proof passes before confirmations. Final focused API specs passed
  15/0 and Node specs 111/0; selector 17/76, targeted RuboCop, Ruby syntax,
  whitespace and all normal hooks passed. Independent reviewer0 (Sol/xhigh,
  high risk; general, architecture, scope and risk) found no Blocking or
  Important findings on `8c29cf196..f2fb787fc`. Its sole Advisory noted an
  unreachable guarded-observer handler fallback. The lead removed only that
  branch in the amended `33fe64fdd`; focused handler specs passed 9/0 and
  hooks passed. This deletion does not expand the reviewed behavior, so the
  mandatory-review procedure needs no affected-lane rerun. Real ZFS partial
  results, mixed-version routing and a physical
  quiet/drain gate remain untested. Production strict, verified scopes and
  APPLY remain disabled.
- The API-to-Node strict 5215 contract is committed as `242c2a919`. A real
  API `GroupSnapshot.fire` stages signed chains in one disposable MariaDB;
  NodeCtld consumes those rows through real Command, receipt and confirmation
  paths. Inventory and handler ZFS calls use bounded in-memory effects. The
  success, partial compensation and extra Pool target refusal scenarios passed
  API 1/0 and Node 3/0 on the committed head. Independent reviewer0 (Sol/xhigh,
  high risk, all four lanes) found two Important harness issues in the first
  commit: teardown could hide a failed database stop, and CI missed a direct
  receipt dependency. The amended runner fails closed on stop or port-probe
  failure, retaining private diagnostics; the workflow now watches that
  dependency. A fake-tool teardown test, selector 18/77, all normal hooks and
  the final contract passed. This does not prove host ZFS behavior, delayed
  child quiescence or mixed-version production cutover.
- The guarded-writer audit found additional vpsAdmin-initiated osctl paths:
  impermanent VPS start/stop/restart and boot can create or move temporary ZFS
  datasets, sometimes through later garbage collection; network-interface
  rename and chown can stop a VPS. These remain strict-cutover gates. The
  architect's handle matrix and `zfs recv -F` identity/victim-set requirements
  are in `storage-integrity-design.md`. The current read-only admission is not
  a complete topology freeze.

The operator's DB capture lasted about seven seconds, and the two ZFS passes
took about 22 minutes for 48,288 objects. These timings are observations from
the supplied artifacts, not a throughput guarantee. Two ZFS scans can miss a
change that reverts between them. Version 1 draft captures are incompatible
with the final version 2 format and must be recaptured.

## Next actions

1. Finish and verify the unsigned production 5204 observer correction. Rerun
   representative snapshot integration on two Puma workers without a signing
   unlock, then obtain independent review and update the configuration feature
   pin to the accepted vpsAdmin head. Keep strict 5204 signed and test-only.
2. Correct the 5291 bounded UNIX EOF case, rerun focused API/Node tests,
   commit and review the signed advisory probe/report. Coordinate the reviewed
   osctld provider revision with vpsAdmin's vpsAdminOS pin only after its
   staging-base compatibility check. Old/mixed components must report unknown.
3. Complete G1 child-process and all-queue coverage before any node-quiet or
   physical repair-ready claim. Complete strict execute/rollback receipts for
   remaining topology and dependency directions, including osctl and
   `zfs recv -F`, before verified identities or scopes can be published.
   The current 5215 contract uses fake ZFS and does not prove host behavior.
4. Keep the reconciler advisory until one-engine frozen approval, bounded
   DB-only apply, crash resume and final verification are implemented and
   reviewed. Do not use the time-separated inventory as an apply gate.
5. Before any shared-host switch, build all channel consumers and dry-activate
   selected hosts, hold all writers, migrate the database first, then update
   NodeCtld and both API workers before relying on the freeze. The completed
   disposable G0 trial is partial and does not authorize production deployment.
   Keep configuration on its feature branch and seek explicit integration
   direction before merging affected feature branches to default branches.

The task guide owns repeatable operator instructions. The source investigation
and proposed future compatibility/deployment sequence remain in this session;
they are not executed rollout records.
