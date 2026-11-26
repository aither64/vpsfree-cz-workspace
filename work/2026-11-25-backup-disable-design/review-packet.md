# Final cross-project review packet

## Current focused review: valid scheduled-work regression proof

Status: reviewer0 completed actual all-four-lane focused review at140f0769/treea872,
no findings. Real DB/chain-construction positive proof accepted; see review.md.
No production change or live scheduler/node/ZFS certification inferred.

User explicitly requires scheduled_for? must not suppress actual valid backups to
solve the rare lookup-to-lock race. Current deliverable is tests only: three real-
fixture regressions,88lines in existing backup_spec.rb, group_snapshot_spec.rb and
dataset_backup_concurrency_spec.rb. No production predicate/source behavior or
public contract changed. Accepted brief: design.md positive scheduled-work section
and plan.md:76. Source trace found matching real action enums/IDs; review must
assess whether actual tests substantiate this without replacing guards, locks or
nested chain execution with mocks. Valid backup under ordinary query caching must
queue Send/Recv/RecvCheck before observable rotations on both source/destination;
real shared action must snapshot both current members; removing one from a stale
loaded two-member list must preserve work for its surviving member. Existing
direct/manual/stale/conflict assertions remain. No live node/storage certification.

All intended test changes are committed, clean, quick-checked and folded into the
owning API commit. Current base81e930b25fa3252d7e849aff4819e663cec37b07→head
140f0769e222dd2aa51e64d08f11cd5e8dae397b, tree
a872181147d22917e37f2a5023af7c30557fd7ea. Three logical commits:

- 8485ffe9f5f81d3b426814a467de1c52a594ca0a API/specs/reference.
- ed8f2e666d5be0c9bdb96a461266e782a339578a PHP including accepted R1.
- 140f0769e222dd2aa51e64d08f11cd5e8dae397b retained storage fixtures.

Complete feature31files,+2253/-80. Entire eb8→final delta is only the three named
nonfixture model specs,+88. Fixed3e4f66cc04f39d6e00d71d088aca242c0284b64a and final
full trees/binary deltas equal the tested a872 tree; immutable old/fixed refs and
complete pre/post series/range diff in [final identity](i1-positive-final-identity.json),
SHA253e4dcb9fa9f2265371b995c26aaa4970c58985bc2ea11a65894cddf6a3fa5c.
No migrations, obsolete/fixup approaches or repeated dependency/pin/generated
streams. Snapshot/Transfer remain original-base equal. Independently assess final
whole-history/migration conclusion while reusing original unchanged source review.

Actual focused coverage14unique passing IDs: initial full three-file14-example
run passed12, including the real scheduled backup/cache/transfer/rotation case.
Two new group fixtures failed BEFORE guard execution because required open backup
destinations were omitted. Only three fixture lines inside those two examples
were added; backup file and all12 passing bodies unchanged. Exact two previously
failed IDs then passed (0pending/outside errors) in44.907s. Lead independently
read native JSON and verified corrected IDs equal original failed IDs, disjoint
from initial12. All14 unique IDs have passed; no claim of one green full14 run.
Native/CLI/process effects joined; no blind rerun or hidden product failure.
Runtime packets: i1-positive-runtime-packet.json and i1-positive-followup-packet.json.
Native results/logs/exits `/tmp/backup-disable-positive-{runtime,followup}*`.
Three syntax/RuboCop checks and corrected two-file checks pass; all mandatory
precommit/message hooks pass, no bypass. Owning amend framework passes with no
staged delta, not claimed as repeated content checks.

29runtime/resource/model/config/db/profile/spec-support/plugin/exporter/tooling/
dependency/node/Nix/UI/fixture/doc objects are unchanged from actual eb8 schema
capture; entire new diff only nonfixture model tests. Preserve actual eb8/3ecd/
50aa receipts/cbe3/generator/client proof, mapping new test head honestly; no new
export/generation/client test churn solely for test-head SHA. I1 evidence top and
final identity supply this graph proof. No new project prose or docs placement
needed beyond session truth-table/acceptance rationale; lasting storage docs are
unchanged and reachable. Assess this no-doc-update rationale and preserved safety
contract under general review.

Retained reviewer0 roster37 verified, saved gpt-6.1-sol/xhigh/read_only/thread
01a21203-fe72-75e0-a69c-cc33ce6663f1; no fallback/override. RiskHigh because tests
validate compatibility of destructive-operation/scheduler safeguards. Apply general,
architecture/repetition, scope/proportionality, risk/compatibility references to
the new tests and predicate evidence only; no repeated five-repository/full
unchanged-source review or reviewer test/build launches. Prior independent 3ecd
report and narrow eb8 source reduction remain explicit below. Return findings,
coverage/limits/history/migrations/docs conclusions for lead recording; I1 retains
any fixes. Real storage/PHP browser remain parked, published SDK before React
merge and separate integration/deployment authorization remain open.

## Preserved prior packet checkpoints

Latest source: clean eb8d111b6e0c318336b818aabeacc3d575ac3279/tree84a4 after
the user's narrow chain-scope reduction. Snapshot/Transfer now match original base
and are absent from the final feature diff; only Backup/GroupSnapshot plan guards
remain. Three-path deletion/restoration,+3/-13,36affected checks and all required
hooks pass. Lead step9 inspection/tree/history proof accepted; original3ecd
independent report below is preserved, not relabeled a new reviewer turn.
See [current final identity](i1-chain-scope-final-identity.json) and
[review.md](review.md). Actual final-eb8 schema/no-change comparison passed;
[proof](i3-chain-scope-schema-no-change.json) binds fresh cbe3/provenance8a5c.
No source scope expansion or automatic review rerun. Current-eb8 two-fixture
verification packet84pb/7ccb10a8 is released under fresh gates; no VM result claimed.

## Preserved affected review: locking simplification at 3ecd

Status: affected independent review complete at3ecd, no findings in any assigned
lane; see [review.md](review.md). I3's subsequent actual3ecd export and complete
canonical schema/provenance/client no-change assessment passed; see
[proof](i3-locking-schema-no-change.json). No integration readiness is claimed.

All intended correction files are committed and quick checks pass. Current clean
vpsAdmin head is `3ecd3ba69569b1a967784ce820712972189e1d94`, tree
`9904af35f776e64083c5019fbcc4c164adb283b9`. Review the changed locking behavior
under all four lanes: general, architecture/repetition, scope/proportionality and
risk/compatibility. Risk remains High because concurrency protects destructive
snapshot cleanup. Retained reviewer0 is independent, read_only, saved
gpt-6.1-sol/xhigh, thread `01a21203-fe72-75e0-a69c-cc33ce6663f1`; roster37 reverified.
No fallback or settings change. Original unaffected cross-project review remains
below and in review.md; do not repeat its five-repository content review.

The user asked why resource locks were insufficient, then explicitly directed
"ok, so please simplify it". Accepted brief: design.md:205 and plan.md:61. Remove
blanket SQL locking/current-read machinery; keep durable VPS/source/backup/source
snapshot locks, fresh post-acquisition scope/source/owner validation, all safety
and preservation predicates, Plan.Create/Delete resource exclusion, scheduled
action/member existence checks and shared-group action/task retention. Decouple
keep_shared_group from query locking. Supported isolation is configured production
READ-COMMITTED. Arbitrary preexisting REPEATABLE-READ transactions are outside this
bounded correction; no global database/test isolation change. No new framework,
API/schema/client/UI/node primitive, dependency, pin or storage-format change.

Complete vpsAdmin range:
`81e930b25fa3252d7e849aff4819e663cec37b07..3ecd3ba69569b1a967784ce820712972189e1d94`.
Final three logical commits,31files,+2178/-83:

- `cf231fee81f2bcee1bad4591dda281b8669ffa8b` API and its specs/reference.
- `842d8e9403360a9faaf3441a9d1a48dda0b488cc` PHP including accepted R1.
- `3ecd3ba69569b1a967784ce820712972189e1d94` retained storage fixtures.

Exact substantive delta from previously accepted e303 is7paths,+68/-45:
operation/dataset_plans/DatasetAction/DisableBackups chain, operation/concurrency
specs, storage guide. See current i1-evidence.md and
[exact final identity](i1-locking-final-identity.json) for complete files, pre/post
series/range-diff, input objects and immutable refs. Fixed correction
`3c5611bac2dd6394cf91b5fc5bfac4f84f7cfb62` and folded final head have identical
full trees and byte-identical narrow patches. Original e303 and reviewed50aa refs
remain preserved; they are not called literal ancestors after rewriting. The
correction is folded into its owning unpublished API commit. No obsolete D2/fixup
stream or repeated dependency/pin/generated stream remains. No migrations in the
entire range; none was merged/released/deployed/externally consumed. Independently
conclude whole-branch history, consolidation and migration soundness.

Quick verification:6Ruby syntax checks and6RuboCop checks pass. Existing three
complete focused files pass47examples/0failures/0pending/0outside errors,
RSpec133.044s/command158.902s. Two new behavior cases reject source/subtree changes
completed before acquisition; stale-action/member assertions remain with local
RC transaction isolation. Exact command/environment/patch bindings are in
[runtime2 packet](i1-locking-runtime2-packet.json); native results and authoritative
exit are `/tmp/backup-disable-lock-runtime2{.json,-exit.json,.log}`. Tested staged
tree9904 equals committed/folded final tree; no unchanged repeat. All required
precommit and commit-message hooks pass; no bypass. Invocation-only failures
before tests/hooks were corrected and retained, with no product assertion failure
or dependency install. No operation-owned runtime/DB/VM effects remain.

Documentation inventory: supported concurrency → developer reference → final
implementation context in docs/storage/disable-backups.md → exact lead-written
two-sentence RC/fresh-read/resource-lock paragraph plus47focused examples. Existing
member receipt, preservation/failure/retention/reenable/deployment text and links
remain unchanged. Execution/cache/history records remain in session evidence.
Assess placement, fidelity and preservation under the general lane.

I3's single actual final-source schema export/full canonical and provenance/input
comparison is pending the I4 utility handoff; source inspection proves unchanged
resource declarations/profile/fixture/exporter/tooling, not a completed current
schema comparison. Existing clients and React heads below are unchanged. Preserve
immutable50aa acquisitions; do not relabel them current runtime evidence.

Remaining limits: actual ZFS assertions and PHP browser remain unrun; React full
379files/2586tests, build and34browser cases passed, with four persisted cleanup
captures being completed separately. Published SDK selection remains required
before React merge. API/scheduler coordinated update/drain and irreversible
rollback limits remain unchanged. No push/merge/release/deploy/lifecycle authority
or integration-ready claim. Reviewer stays read-only, runs no tests/builds, and
returns report for lead recording. I1 retains any source/review-fix ownership.

## Preserved original review packet

Status: original final independent review complete; see [review.md](review.md).
The user's later locking-simplification request is in implementation; this
original packet does not certify that correction. The affected review will bind
its committed final range, quick checks and current input evidence separately.
Two Important narrow fixes and final history/tree proofs verified; see report
for original e303/c723 bindings and post-review verification limits. Original
source is committed and its known quick checks pass. Rust compilation/package/MSRV matrix passed after dispatch without source
changes; no live integration has started. Final
assignment must bind this packet and current owner evidence, not historical D2.

## Requested result and scope

Implement administrator-only backup disabling with default-on `backup_first` and
optional recursive scope. Remove all selected primary/hypervisor snapshots,
including manual snapshots, retain live filesystem/VPS state and backup history
under ordinary retention. Support planless datasets. Both plan forms explain that
ordinary plan removal leaves snapshots.

The user rejected `preservation_chain`, two-call orchestration, special repair of
unexpected older unbacked snapshots and broad dataset-plan policy changes, and
explicitly required one chain. D3 is authoritative: one normal request with only
recursive/backup_first, ordinary empty dataset namespace plus action-state receipt.
Use ordinary Transfer; uncovered older/middle gaps reject construction. All
required transfer/copy checks precede every source deletion. Metadata/destruction
suffix is not_reversible, including helpers. Preserve ordinary plan semantics;
only necessary locks/stale-work fences and scoped shared-group unregister remain.
No first-plan reset, notifier/Nix repair, manifest, force-full mode, rotations,
new live-state snapshot, public phases/continuation or browser-exit cancellation.
Accepted work continues after client exit; unknown outcomes never auto-replay.

Review the actual user boundary before hardening; do not extend edge-case support
or invent another orchestration mechanism. Do not waive correctness inside the
supported destructive-operation boundary.

## Source ranges and complete series

Workspace `/home/aither/workspace/ai/vpsfree.cz`; worktrees under
`worktrees/2026-11-25-backup-disable-design/`. Branches and source evidence are in
[state.md](state.md). Unchanged `haveapi-i3` is tooling only at
`1ef9b204ba45bb261d3334be5c555cc1856b713b`, not an authored feature. Dedicated
`vpsadmin-export-i3` is the same final source graph, not another implementation.

| Repository | Base | Head | Scope |
| --- | --- | --- | --- |
| vpsadmin | 81e930b25fa3252d7e849aff4819e663cec37b07 | 50aa37aede8926965598f4f8fb0782dce377afb6 | API/PHP/storage fixtures;31files+2138/-85 |
| vpsadmin-go-client | 5934903568862a95b688479f0b13e11e4a36692f | 70a29effc9832c5c4d055b53501671ad34608a5c | Generated/input refresh plus handwritten wire tests;14files+4361/-25 |
| vpsadmin-rust-client | 15db0ffd95ccd34247de9f839c906d860afb1b69 | f03bab11b7dd6d88281e334790d6b3897ed33e46 | Generated/input refresh plus handwritten smoke;15files+3157/-32 |
| vpsadmin-typescript-client | b619eb8324bfe80c7b225f698fb83efe97639c83 | 6d4941bbf617a0d1e1c131a2bf14ca6476389809 | Generated/input refresh plus handwritten real-runtime tests;13files+341/-39 |
| vpsadmin-webui | e311b1c0af0f50fa4c6f6ce83c514c1a866eb042 | 9e6ed96a49de2f6b65bb3e730047c428b77185f4 | Generated adapter/shared control/route/locales/tests/docs;19files+815/-10 |

vpsAdmin:

- cbb8def6056301558ed17c8b4818a9653ae5d35e api: preserve snapshots before disabling scheduled backups
- bd36c4f241ed34da4ce726b702988e3e151d2549 webui: add admin backup cleanup confirmation
- 50aa37aede8926965598f4f8fb0782dce377afb6 tests: cover single-task backup disablement on remote storage

Go:

- b98943d103f9fea010594589cee201212bb10362 Regenerate client for the backup-disable API contract
- 70a29effc9832c5c4d055b53501671ad34608a5c Verify backup-disable options and the ordinary receipt

Rust:

- 63027b689b444f92c7c493fc6cb0b0e8661cde87 Regenerate client for the backup-disable API contract
- f03bab11b7dd6d88281e334790d6b3897ed33e46 Verify backup-disable options and the ordinary receipt

TypeScript:

- 5c4fcfdc97de0f420419bb260e330054f16f59e2 Regenerate SDK for the backup-disable API action
- 6d4941bbf617a0d1e1c131a2bf14ca6476389809 Verify backup-disable options and the ordinary receipt

React:

- 9e6ed96a49de2f6b65bb3e730047c428b77185f4 storage: add administrator backup cleanup

Review complete base-to-head diffs and series in each repository, including
handwritten client tests and generated streams. Complete owner path/diff inventories:
[I1](i1-evidence.md), [I2](i2-evidence.md), [I3](i3-evidence.md),
[I4](i4-evidence.md). React exact diff/series and installed-input receipts are in
`i4-logs/final.diff`, `final-series.txt`, `final-receipt.json`, `final-sdk-graph.json`
and `final-installed-package-lock.json`.

## History, migration and input lineage

All superseded D2/correction/fixup streams were unpublished, unmerged, unreleased,
undeployed and externally unconsumed. Owners retain historical refs/evidence only;
final histories introduce D3 directly. vpsAdmin old five-commit range ended68fb149;
initial consolidation tree equaled it. Final tree differs only one obsolete NoOp
selector deletion. Lead verified that delta and identical API/node/exporter source
from tested5526c99 to final50aa. React has one amended final commit. Clients each
have one generated stream and one handwritten verification commit; stale local Go
staged-output commits were removed from final history and all698committed output
files matched fresh generation. No compatibility path for D2 is supported.

There are **no database migrations**, database-schema/storage-format changes,
node-wire changes, dependency-toolchain upgrades or deployment/release boundaries requiring intermediate
commits. Independently conclude whole-branch history/migration and repeated-stream
soundness; owner claims and an earlier tree check do not replace that review.

Actual final API export50aa schema SHA256
`cbe3a7ca90d7f1c94e2b769058b1c32a570e36fd92f55cf48a4302d4e50dc05d`,
raw provenance `31545e703ae6142f5d4ffce87b581a30685cecbb89662eff3ad25fedb00441c0`,
lock `dd5db5ca44bb69ca2ae0244515103146f17b7621f12ca34c3dec6950f4455aaf`.
Full six-plugin English fixture, API7.0/protocol2.0, generator1ef9b204 unchanged;
client-specific generator/runtime/toolchain bindings are in I3 evidence.

React development SDK6d4941b archive SHA256
`671b54f52da297cd465c1b7516841a859c84099ab30d776e5086802559d19a10`.
Its local version0.6.0 is not the registry0.6.0 archive. Manifest/lock retain the
registry baseline without the new action. Exact installed graph has409nonSDK
entries matching lock and1392SDK files matching this archive. Previous candidate
runtime/types/schema equal final; only2provenance files changed. Do not treat
source review or local candidate tests as registry/Nix-release certification.

## Verification and limits

- API:56examples covered by53unaffected passes plus3test-only repairs passing;
  node46pass. Exact ordinary response.dataset=={}+meta assertions passed. Source
  equality after consolidation proven. Required hooks, lint/catalogs, selector16/55,
  full/core13topics432eligible files exactly once pass. See I1 for commands/hashes.
- PHP: full176tests/1438assertions, final affected15/70; syntax/format/gettext and
  browser-source syntax pass. Consolidated owned paths match tested source. Baseline
  warning/deprecation documented by I2, not introduced failures.
- Go: schema helpers4 and all-package wire checks pass; exact698output-file proof,
  unchanged handwritten boundaries and final-source input binding. See I3.
- TS: real-runtime/strict types/consumer/build and19tests pass; deterministic
  generation and exact retained final archive checker pass. Metadata-only refresh
  reused semantic evidence after complete file equality proof.
- Rust: format/provenance7/deterministic generation and refusal10 pass. Compiler,
  docs/package and MSRV1.95 matrix passed: native47356 exit0/status0,696s,
  both compiler default/blocking lanes; opt-in real API ignored.
- React: canonical409entry dependency graph,64focused tests and completeci:quick
  pass. Final metadata-refreshed archive installed exactly, final30consumer/wire
  tests and docs audit pass. Earlier drifted dependency graph is historical only.

Unrun long integration remains deliberate: two existing remote storage VM suites
with real per-snapshot payload/live-data assertions, relevant PHP browser script,
React full suite/build/browser EN/CS desktop/mobile captures and applicable release
packaging. No deployed behavior, live OAuth or actual ZFS contents are certified.
No session preview or deployed machine has been started; unit fixtures use isolated
loopback servers where required. No production mutation is authorized.

Published SDK release containing new action is required before React merge; final
manifest/lock/provenance and affected release checks must then select that artifact.
API/scheduler guards must deploy together before exposing capability; older workers
must drain/restart. Backend deployment, SDK publication and default-branch integration
need separate authorization. Review does not authorize any of them.

## Documentation routing and fidelity

| Topic/readers | Class/authoritative location | Evidence or remaining limit |
| --- | --- | --- |
| API/storage behavior, CLI, failure, reenabling | Reference/how-to, vpsadmin docs/storage/disable-backups.md via storage README/index | I1source/specs, main-agent prose pass; actual VM execution pending |
| PHP confirmation/tasks | Developer reference, vpsadmin docs/webui-backup-cleanup.md via docs index | I2client regressions, main-agent copy/guide pass; browser pending |
| Generated contract/acquisition/regeneration | Each client README/development docs and schema/provenance inputs; vpsadmin docs/api-schema-export.md owns export contract | I3finalsource hashes and semantic/archive/compiler/package checks |
| React action/SDK constraints | Reference, docs/design/{ACTION_CONTRACTS,WORKFLOWS,HAVEAPI_CLIENT,REQUIREMENTS,EVIDENCE_MATRIX}.md | I4source/tests/audits and main-agent copy/instructions pass |
| React individual implementation/check boundaries | Individual execution, docs/work-log/2026-11-25-disable-backups.md | Candidate and dependency environment receipts; no deployment claim |
| Current status/ranges/recovery | Session design/plan/state and owner evidence | Historical D2 explicitly superseded; no product reference depends on private session |
| Member KB/captures | Existing PHP-bound KB contracts, owner assessments in I2/I4 evidence | Exact published-pin checks/captures pending; no KB writes authorized |

Assess navigation, placement, preserved recovery/partial-failure warnings and factual
fidelity independently. Main-agent writing passes and link audits are not technical
review. Existing project transaction docs remain authoritative for rollback mechanics.

## Reviewer assignment

Overall risk **High**: destructive storage cleanup, irreversible partial failure,
authorization, cross-node ordering, shared schedules and cross-project API/SDK.
Eligible retained reviewer0 uses saved `gpt-6.1-sol`/`xhigh`, read-only instructions.
Fresh roster37 at dispatch verified purpose review, ready state, read_only and
the unchanged saved model/effort. No nested reviewers or source edits.

Assign all four lanes from mandatory-change-review: general, architecture/repetition,
scope/proportionality and risk/compatibility. Read each lane reference from the
skill. Report findings ordered Blocking/Important/Advisory with actual paths/lines,
explicit whole-history/no-migration/repeated-stream and documentation placement
conclusions, residual risks and unrun verification. Original implementers own fixes.
