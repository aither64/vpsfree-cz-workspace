---
lifecycle: active
---

# 2026-09-23-storage-redesign

## Current status

Phase checklist:

- **Retained dev-cluster: stopped.** The user requested it for another initiative.
  Ordinary stop and status passed; configuration and all six disk identities
  were preserved. No automatic restart.
- **Earlier source prerequisites complete:** API reservation `425d399a`, OS
  disabled generation `80034c8c`, Admin OS dependency `bc9bb38e` and optional
  maintenance profile `6cd9f9a6` are feature published. Their completed reviews
  and bounded verification remain scoped to those revisions.
- **Current phase:** Contract2 acknowledgement and its requested-state review
  fix are committed at `32d7f0ac`. Fresh API/model127 and both three-file lint
  gates passed. All declared amend hooks passed. The complete primary
  c4d..543 review plus direct step9 remediation has no remaining Blocking or
  Important; the comparator CPU Advisory is accepted separately.
- **Source delivery complete:** feature `32d7f0ac` is published with exact
  readback and final comparison; master stays `c4d9b50f`. Source is ready,
  awaiting merge approval. No default integration or live delivery is authorized.
- **Held capabilities:** Contract2 invocation, termination/release, physical
  exclusion and G2 remain unavailable. Alias disposition, NAS history and
  destination availability remain unresolved; scheduler, objects and evidence
  are retained. Default integration, package delivery and live activation held.
- **Known verification limit:** broad flake validation remains blocked by the
  reproduced baseline overlay export. Focused results do not imply that gate
  passed.
- **Next action:** preserve the completed source checkpoint. Remaining
  termination/recovery and physical ownership contracts require a separate
  design and release; operational handoff is held. Retained cluster stays stopped.

### Current-read review resolved; feature publication complete, 2026-10-07

Normal owning amend PASS0/63.289s, child49.774s, driver56.370s/cleanup1/
children waited1/parity1. New32d7f0ac/tree3d9d65a7/parent6cd; actual precommit
and message hooks allOK/no hook warnings, nonfatal Nix dirty-tree warning only.
Parent verifies all3248 hashes, outside3243 byte/stat/cache parity, original
DB3289070 and commit child3289123 absent; signals0/prune0. Clean tracked/index.
Final27commits/222paths/27300+/461-, owner19paths/1543+/97-; exact four
migration/schema blobs preserved. Original543 backup and independent all-four
review remain; Important resolved through focused lead step9, no rerun claim.
See [disposition](storage-maintenance-handoff-current-actor-disposition.md)
and [final inventory](storage-maintenance-handoff-current-actor-final-inventory.json).
Fresh guarded feature publication PASS0/14.241s (push9.530s/waited1/parity1),
exact6cd->32d readback, masterc4d unchanged. Final comparison saved. Actual
child Bundler/push output and existing default-branch two-high Dependabot
advisory are distinct from hook success. Seven current CI runs were queued or
in progress at the metadata snapshot, unawaited. Superseded6cd CI37530868383
cancellation request0 only; completion not proved. No current/default run
cancelled. See [publication](storage-maintenance-handoff-current-actor-publication-result.json).
No default/live/physical or operational Contract2 release follows.

### Historical checkpoint: current-read checks passed; owning fold active, 2026-10-07

Fresh batch PASS0/513.868s/waited1/parity1; driver505.897s/cleanup1/
children waited1. API127/0/0pending/0outside passed (stage479.230s,
native465.596s, seed40690), including every10 older-view/current-request case.
Both component/root lint inspected3files with0offenses (5.936s/13.026s).
Parent read native JSON, actual lint output and cleanup result; all3248 bytes,
outside5 byte/stat/cache parity and original DB PID3283553 absence proved.
No signals/prune. Migration8/endpoint1/selector20/generated proofs remain exact
unchanged-byte carry, no extra execution.

Parent retained exact543 backup and staged only the reviewed5 paths, tree
3d9d65a703d20697be45088ce6f33449cf1b3429. Fresh Luna/low normal amend watcher
api_current_actor_amend_20261007 is active at /tmp/handoff-current-actor-amend-20261007.n6jzkkth/commit.py; frozen0ffe37d9/messageffde34d9, guards unchanged
except explicit expected parent6cd for the amend. Actual hooks and outcome
pending; no bypass. Important disposition/publication remain pending. All
physical/default/Contract2 invocation and stopped-cluster holds remain.

### Historical checkpoint: current-read remediation freeze, 2026-10-07

Implementer0's exact five-path freeze a47d4129 is accepted after parent full-delta
inspection. Canonical default SQL/order and existing caller lock order remain;
unknown requested state refuses. Authored25 new cases include15 real-row/query
cases and10 older ordinary-RR/concurrent-request refusals. Actor67/full API127
remain inventory until the fresh run finishes. Protected worker and original
spec bodies reconstruct exactly; only two exact-owned row bookkeeping additions.
Parent proves all3248 source hashes, exact five delta and other3243 parity,
owner19 with14 unchanged, schema/locales/four migrations/inputs and empty index.
Both owning guides received the main-agent prose pass.

Fresh Luna/low utility api_current_actor_checks_20261007 owns the once-launched
three-stage batch at /tmp/handoff-current-actor-checks-20261007.nuueaj4u/checks.py.
Frozen80d570b8, Ruby driver7bd984d8, guard911c91cb, wrapperaf1d488e. Complete
four owning API/model files then component/root lint for3 Ruby paths; all
results pending. No migration/endpoint/selector/regeneration/VM/CI wait.
Important remains open; normal unpublished fold, direct step9 disposition and
feature publication pending. Retained cluster stopped; all operational holds
remain.

### Original Important actor eligibility finding at543, 2026-10-07

Reviewer0 confirms an Important risk/general finding in retained actor helper
(origin a561366c, consumed by543a797). User/UserSession are current-locked, but
current_object_state is an ordinary SELECT. An established outer REPEATABLE READ
view may miss a separately committed requested suspension/soft-delete while
User.object_state stays active pending lifecycle confirmation. Existing tests
cover direct row-state changes and current Pool claims, not this requested-state
case. This is a source-backed authority gap, not a demonstrated remote exploit
or recovered incident.

Architect0's final five-path brief is accepted. Implementer0 task
01a11373-2e27-7490-b15d-652719bfee4c owns authoring and static verification only:
canonical Lifetimes opt-in locking read, storage admission, actor regressions,
object-lifetimes and integrity-model documentation. Parent owns the two-document
prose pass and guarded owning checks. All other source and the index stay held.
The original complete all-four-HIGH review is complete on exact543; Important
remains open until focused remediation checks and direct step9 disposition.
Publication remains held.
All prior pass scopes and stopped-cluster/operational/physical/G2/default holds
remain. No new physical trial is requested.

### Contract2 final lint gates and normal commit, 2026-10-07

Selected final batch PASS0/38.308s/waited1/parity1; driver31.553s/cleanup1/
children waited1. Component/root lint each10files/0offenses (5.182s/13.024s),
selector20runs/89assertions/0failure/error/skip (7.364s). Parent independently
read stage and cleanup results, proves original private DB PID absent and
all3248 source hashes/outside/cache parity; no signals/prune. Functional102+8+1
carry only through the equivalent actor conditional correction. All six
owning gates are now satisfied with their explicit source scopes.

Parent staged exactly17 including both new migration/spec paths. Staged tree
e8bbbadc65c6e8734c55723f2056ed2614d323c2; mandatory hooks installed/active,
normal new message word-identical72-column wrapping. Fresh utility
api_handoff_commit_20261007 owns /tmp/handoff-commit-prepared-20261007.ko2iw09s/
commit.py, frozen73913850, commit driver7a9cfae7/guard911c91cb/wrapper5df5cd2a.
Commit PASS0/62.410s/parity1, driver55.585s/cleanup1/children waited1. Actual
precommit and commit-message hooks all passed, no hook warnings; only nonfatal
Nix dirty-tree warning. New543a797/treee8bbbadc/parent6cd, clean tracked/index,
all source hashes and original private DB PID absence verified by parent.
Complete c4d..543 is27commits/220paths/27015+/457-, one17-path owner1255+/90-.
Final complete independent review is pending; no publication acceptance. All source/index held; retained cluster stopped.

### Contract2 style batch and final fixture lint correction, 2026-10-07

Fresh style wrapper failed1/476.438s/waited1/parity1; driver469.572s,
cleanup1/children waited1. API102/0/0pending/0outside passed
(stage420.270s/native408.580s), migration8/0 (stage7.038s), endpoint1/0
(stage30.624s). Component lint10files found one Lint/DuplicateBranch at actor532
and failed4.833s; root lint and selector did not run. Parent read actual results
and proved original private DB PID3193369 absent; no signal or prune.

Implementer0 turn01a1135b-c7d4-7993-b3d7-db74d81d786f merged only the identical
Integer/Time increment branches. Actor3f8f9d7c reverses exactly to b8e7844;
short-circuit order, result values, assertions and protected worker machinery
are unchanged. Final17 manifestf3831115 and complete patchb17fa2be accepted;
parent verifies all3248 source hashes, other16, head/tree and empty index.
Functional102+8+1 evidence carries narrowly for this equivalent fixture change.
Fresh utility api_handoff_final_lint_20261007 owns the selected APIlint/rootlint/
selector batch at /tmp/handoff-final-lint-20261007.u__t33by/checks.py,
frozen0cfedf01/selection driverd09606fd/guard911c91cb/wrapperaf1d488e.
All three results pending; no overall pass, commit or review acceptance inferred.
Prior failures and generated proofs remain. Retained cluster stays stopped;
operational handoff/default/live/physical/G2/alias holds remain.

### Contract2 third batch and style release, 2026-10-07

Remaining-five wrapper failed1/59.753s/parity1; driver53.041s/cleanup1/children
waited1. Migration8/0/0pending/0outside passed (stage7.331s/native5.895s), including
FK preservation and actual DELETE refusal. Endpoint1/0 passed (stage31.396s/
native19.011s). Component lint10files/38correctable offenses failed6.727s;
root lint and selector unrun. Parent confirms original private DB PID absent,
no signal/prune. Earlier API102 pass retains unchanged source scope.

Released exactly eight owned paths to implementer0 turn
01a1134d-5f53-7cb1-a2c4-3e4a94a6c538: new migration/spec, maintenance_run,
freeze_status and four existing API/model specs. Corrections are reported
alignment, redundant literal parentheses, numeric predicate spelling, terminal
guard clause, one nested ternary and single literal quote. No cop/config or
scope expansion; other9/index/schema/locales/docs/admission/resource/coverage
held. Compiled SQL bytes, invariants,102/8 examples and protected worker machinery
must remain exact. Fresh complete six-stage verification follows because runtime
branches change. Style freezefda692c4/fullpatch72b47fd0/correction7e9929a0 accepted. Parent inspects
complete eight-path delta and full3248/17/head/index parity; six compiled SQL and
column constants match exactly (digeste4575b28). Other9/schema/locales/worker
remain exact. Fresh utility api_handoff_style_checks_20261007 owns one full batch
at /tmp/handoff-style-checks-20261007.v6ug6tu2/checks.py, frozen3eb421c2, original
full driver939fdd16/guard911c91cb/wrapperaf1d488e. All six new outcomes pending;
prior passes retain old-byte scope. Member preparation-only Python warning/tool
JSON refusal is retained separately; final syntax/parity evidence owns bytes.
No aggregate pass or new gate.
Cluster remains stopped, operational handoff and all physical/default/live/G2
holds remain.

### Contract2 second batch and migration fixture, 2026-10-07

Second wrapper failed1/457.068s/waited1/parity1; driver450.149s/cleanup1.
API102/0/0pending/0outside passed (stage436.379s/native424.717s). Migration8/1
failed (stage7.126s/native5.752s) at spec91: fresh IndexDefinition objects compare
by identity. Pinned AR8.1.4 base/MySQL classes have no value-equality override;
all displayed index metadata matches. ForeignKeyDefinition is a Struct and its
unchanged equality remains valid. Parent verifies all3248 source hashes and
original DB PID absence, no signal/prune. Later endpoint/lints/selector unrun.

Only130000 migration spec is released to implementer0 turn
01a11347-dd2f-7571-a4b3-d36fc234f78b for a local explicit projection of all14 public
base index attributes plus MySQL enabled. Preserve every remaining assertion,
including FK equality and actual DELETE refusal. Other16/index/head/schema/locales
held. Corrected freeze5b14f456/manifest1631d6b1 accepted; parent complete3248/17/head/index
parity and exact reversal verified. Fresh utility api_handoff_index_checks_20261007
owns /tmp/handoff-index-checks-20261007.6h932zdg/checks.py, frozenb3913869,
selection-only driver18b30987/unchanged guard911c91cb/wrapperaf1d488e. All five
new outcomes pending: migration8/endpoint/lints/selector20;
API102 pass carries only with exact unchanged source. No runtime/migration or
contract defect/change is inferred. Retained cluster stays stopped.

### Contract2 first owning batch and fixture correction, 2026-10-07

First batch at exact6cd/final17 failed1/420.591s, waited1/parity1; driver
413.024s/cleanup1/children waited1. Native API102/1/0pending/0outside errors,
395.611s; stage407.794s. Later migration/endpoint/lint/selector stages did not
run. Parent rechecked all3248 source hashes and original private DB PID absence;
no signal/prune. The sole failure is API example421/expectation448: typed action
Datetime outputs are ISO strings while nested Custom status timestamps retain
ordinary UTC JSON strings. Full-summary diff differs only acquired_at and
handed_off_at. Installed HaveAPI0.29.8 Typed#format_output confirms this existing
boundary. No runtime defect or format change is indicated.

Only api/spec/api/resources/storage_freeze_spec.rb is released to implementer0
turn01a1133c-05b6-7132-9e8d-513478040b57. Project the two typed timestamps through
Time.iso8601(...).utc.to_s in the expected full summary; preserve every key,
subsequent effect/refusal assertions and102 examples. Other16/index/schema/locales
remain held. Corrected freeze accepted: spec279dcdf7 and manifest2350e959; complete reverse proof
restores prior474ac272 bytes. Parent verifies all3248 source hashes,17 owned files,
head/index and exact one-expression reversal. Fresh utility
api_handoff_timestamp_checks_20261007 owns the once-launched
/tmp/handoff-timefmt-checks-20261007.t1m1kmc7/checks.py, frozena6baeafb,
unchanged driver939fdd16/guard911c91cb/wrapperaf1d488e. All six outcomes pending;
no old failed-run pass carries.
Cluster remains stopped; no operational handoff or physical authority follows.

### Contract2 initial14 freeze and core generation, 2026-10-06

Member froze initial14 at unchanged6cd/tree0f11, empty index. Manifest
64088cae/source patch15c7ac74/owning message4f48c3ba are in the retained private
authoring packet. Lead inspected the complete fourteen-path change and found
no concrete deviation from the accepted record-only contract. The actual new
130000 migration matches the prepared five-column schema projection, including
exact binary tuple/profile checks and refusal before DDL for unsupported rows.
All3234 outside tracked sources and PHP cache file/directory bytes/stat match
the member baseline; schema/EN-CS, first three migrations and worker cleanup
remain unchanged. Source/index/head and scoped diff checks pass. Authored
102 API/model and8 migration examples are inventory only, not outcomes.

First utility api_handoff_schema_generation_20261006 ran one core-only
generation at /tmp/handoffgen-20261006.tecjll92. Frozen SHA
ced43cf43d7b771388d3ed828de0041fd355f0f87c9d6e968eb9dd513264c30f binds
all3248 current sources. Driver7cf38227/guard911c91cb/wrapperd5f3a1c1 retain
the accepted pre-effect and same-connection guard, sole pending130000,
180-table/five-column/one-constraint/version projection, exact predecessor
reversal and socket-bound cleanup without prune or fallback termination.
Parent preflight parity1/executed0 is separate from that child. The run failed
1/25.659s/waited1/parity1; generation17.073s/generated0/cleanup1/installable0,
GenerationRefusal at dump_core_schema/driver156. The output remains retained
and unaccepted. Parent read the exact schema diff: only version, five audits
and the owning constraint changed, but the changed constraint moved. Pinned
AR8.1.4 SchemaDumper sorts rendered CHECK statements, so the private validator's
fixed-position comparison refused it. Parent source guard passes and the
original private DB PID is absent; no signal or prune occurred.

The correction changes only the private comparison: remove the unique named
owning constraint from both table blocks before comparing every other byte
and order. Five-column checks and entire-schema predecessor reversal remain
exact; no SQL/helper/application-source or cleanup change. Offline comparison
of the retained failed output proves that is the sole mismatch. Fresh packet
/tmp/handoffgen-order-20261006.ltpvoe66 has frozena386fdef/driver60e79a33,
unchanged guard911c91cb/wrapperd5f3a1c1 and the same3248-source binding.
Syntax/preflight parity1/executed0 passed. Fresh utility
api_handoff_schema_order_generation_20261006 completed PASS0/23.284s,
waited1/parity1; generation16.683s/generated1/cleanup1/installable1. Core proof
is sole130000 on exact120000,180 unchanged tables,five audit columns,owning
constraint/version only, application boot0 and unrelated schema changes0.
Lead inspected the complete schema diff/proof, rechecked source guard and
artifact syntax, and proved the original private DB PID absent without signals
or prune. The emitted SHA2030ff5c9f12ff8b4ef10c405c6cc96cda7a89ab7824ea751c272fcac3a302a9
matches the retained first output, whose failed proof remains historical.

Only api/db/schema.rb installation was released to implementer0, turn
01a11321-0f44-72a3-b236-4b12e6b72439, byte-for-byte from the accepted second
artifact. Installation completed byte-for-byte (SHA2030ff5c,141134bytes,7+/2-),
with static syntax/diff0 and initial14/all3233 outside/cache/head/index parity.
Initial15/index and EN-CS remain held. No ordinary examples, live handoff, cluster restart or physical action
follows; locale generation/checks/review/publication remain separate.

### Contract2 full-plugin locale environment, 2026-10-06

Fresh utility api_handoff_locale_environment_20261006 owns the once-launched
/tmp/handoff-locale-env-20261006.qju819zi/checks.py. Frozen67ea05b7,
wrapper0c554c8b and environment264b7f83 bind all3248 source files, exact6cd,
empty index and installed schema2030ff5c. This declared full-plugin API shell
setup runs before snapshot capture so the effective generated Gemfile.lock is
bound correctly. Application/DB startup is absent from the prepared driver;
Environment setup completed0/7.212s/waited1/parity1, pinned Ruby3.4.9/AR8.1.4/
mysql2.5.7/full-plugin mode, app boot0/DB started0. Effective lock0ecd77cc and
all3248 source hashes match the parent readback. Dirty-tree warning is expected
for held source edits, not a check failure. Fresh raw locale packet
/tmp/handoffloc-raw-20261006.xwzu1pc1 freezes the complete private snapshot,
lock and unchanged locale3651d92a/guard911c91cb/wrapper0c554c8b, frozen8b0f9efc.
Fresh utility api_handoff_raw_locale_generation_20261006 owns one existing
vpsadmin:i18n:update run; all generation/cleanup/prose/health outcomes remain
pending. Application EN-CS/source/index and retained cluster remain held.

### Contract2 locale prose and health, 2026-10-06

Raw locale generation completed0/52.307s/waited1/parity1; generation45.96s,
generated1/cleanup1, full-plugin update child0, core schema unchanged/plugin
schema dump0. Parent verifies all source hashes and original private DB PID
absence without signals/prune. Raw proof remains unaccepted for installation
until prose/health. Each locale has2388->2399 leaves:13 additions and2 shared
descriptions moved to action-specific paths. Every other leaf is unchanged.
Lead applies owning vpsFree writing and EN/CS Humanizer guidance directly:
EN metadata needs no rewrite;13 CS TODO leaves are translated, preserving the
two previous abandonment descriptions and existing epoch wording. Exact key
and13-change comparison/YAML parse pass.

Fresh /tmp/handoffloc-health-20261006._t9mv6p0 freezes root sources separately
from normalized snapshot bytes. Frozen3367c91f/locale5675eb2e/guard911c91cb/
wrapper0c554c8b reuse the accepted health driver unchanged. Fresh utility
api_handoff_locale_health_20261006 completed0/97.036s/waited1/parity1.
Generation90.312s/generated1/cleanup1, update0 and health0, no normalization
byte change. Parent verifies root/snapshot/proof hashes and original private
DB absence without signals/prune. Final EN27cced81 and CSbbc77293 are accepted
for installation; only those two paths released to implementer0 turn
01a1132e-4970-76e3-9978-0319a0329863. Exact final17 freeze pending, no ordinary
API/model/migration example run. Prepared six-stage owning driver939fdd16,
guard911c91cb/wrapperaf1d488e remains unbound/unrun until final17 acceptance.

### Contract2 final17 freeze and owning checks, 2026-10-06

Implementer0 installed only accepted EN-CS bytes; final17 packet
/tmp/api-maintenance-handoff-final17-20261006.imr20pgw has manifestc83cb544,
complete patchb34fada4/locale patch8861649a/unchanged new-owner message4f48c3ba.
Initial15/head6cd/tree0f11/index and all3231 outside tracked byte/stat, first3
migrations, protected worker and foreign cache file/directory match baseline.
Parent independently verifies final17 hashes/stat, exact locale artifacts and
outside/cache parity. Member YAML2/static diff0 passes; initial no-index
status0 assumption failed because a clean difference correctly returns1,
then static checks were corrected without source rewrite. Parent's first
cache-directory projection assumed the file's five-field stat shape; it
refused before checks, then the actual saved four-field directory projection
passed. No source or operation changed for either private comparison correction.

Fresh utility api_handoff_owning_checks_20261006 owns the once-launched
/tmp/handoff-owning-prepared-20261006.05v4bdej/checks.py. Frozendc8f6872,
driver939fdd16/guard911c91cb/wrapperaf1d488e bind all3248 final sources and
empty index. Six stages: API/model102, core migration8, existing full-plugin
endpoint coverage, component/root lint10 and unchanged selector20. Counts
are authored inventory; every outcome is PENDING. Existing guarded DB/SQL/
cleanup ownership is retained; root Bundler isolation is private runner glue.
All source/index/runtime/default/alias/Contract2 invocation holds persist.

### Contract2 main prose, 2026-10-06

Implementer0 released only the three integrity guides while finishing the
other eleven static paths. Lead read the technical handoff and owning docs,
applied the vpsFree writing/Humanizer skills, and completed the prose pass.
The text states supported tuples, copied audit, first-transition locks,
original-CAS no-write replay and the absent termination/physical authority
directly. Existing unknown/malformed-reader refusal and multi-service reader
convergence wording are retained. No interface or policy decision changed.

Final SHA256: foundationf64f6688c2d850ce0f78b7eb5656a3e84ea3f063c049591b445eb440adffd6a3;
modelcd26f426bb69283d737a7e3d02756349df5b3ce7909a7734ac90b2b33b4275be;
reconciler4549abcf7d716d03efeadc04f46d804143868025f1d02fb8050b4b301f48a669.
Inline technical content, headings, links and fenced code match the technical
handoff; scoped three-doc diff check0, exact6cd and empty index. The final
bytes were returned to the active implementer turn for its initial14 manifest
and are held. No examples, generation or runtime action ran. Remaining
eleven-path authoring and generated schema/EN-CS holds remain unchanged.

### Contract2 generation preparation, 2026-10-06

During initial14 member authoring, lead prepared an unbound private schema
projection at /tmp/handoff-schema-driver-prepared-20261006.9pcbglpi.
Adapter911c91cb remains exact accepted bytes; driver7cf38227 keeps its
pre-effect identity/same-connection, core-only SchemaDumper and retained
cleanup rules. The projection requires predecessor120000, sole pending130000,
180 unchanged tables, only five nullable audit columns and the owning
constraint/version delta; reversal must reproduce the entire predecessor.
Column choices will be reconciled against the actual frozen migration before
release. Immutable Ruby syntax passes; no schema generation or DB started.
The accepted Python watcher wrapper d5f3a1c1 was copied byte-for-byte and
compiled in memory; it remains unbound and unrun. No frozen manifest, launch
shell or artifact directory exists. Updated prepared manifest SHA256 is
f0cc637faffc75501ea692bce0d3e0935ccc19eb75d6dfc901b58322b08564af. This is
prepared/unrun evidence, not source/migration/cleanup/install acceptance.
Initial14 source remains member-owned; schema/EN-CS and all runtime actions
stay held. Original generation packets and source evidence are unchanged.

### User-requested retained cluster stop, 2026-10-06

User continued source work and explicitly requested stopping the dev-cluster
for another initiative. Parent verified exact current/env identity and installed
public stop ownership. Fresh Luna/low utility
storage_retained_cluster_stop_20261006 ran one public status/stop/status batch
in private /tmp/storage-cluster-stop-20261006.oa7kj6ie, driverdf5fddcd.
Overall0/101.061s; stop child0/98.847s/waited1; final status0/stopped,
storage topology/bridge network/maintenance released. The public owner printed
`cluster 2026-09-23-storage-redesign stopped`, without timeout-kill fallback,
and removed its ordinary result-config GC link. Retained applied-selection and
provenance roots remain under the existing stop contract.

The private config SHA is unchanged and all six retained disk paths keep the
same device/inode/size. Admin head/index binding remains unchanged. These are
bounded preservation checks, not a new guest DB/file/history certificate or
universal process-reap proof. No reset, release, unregister, deletion,
configuration/mode/package change, scheduling restart, alias disposition or
other initiative operation occurred. The session stays active and this retained
cluster stays stopped until separately requested. See the
[public stop result](storage-retained-cluster-stop-result.json).

### Bounded Node endpoint fixture correction, 2026-10-06

Read-only preparation during the corrected VM copied the accepted guarded
TestDb adapter byte-for-byte (SHA911c91cb) into a private prepared packet.
No launch driver/frozen manifest exists and no DB, process or source operation
ran. The later handoff SchemaDumper must bind the actual current predecessor,
sole130000 migration and unchanged table set; it cannot reuse the reservation
new-table proof. Existing pre-effect identity/connection and retained cleanup
rules remain. This supplies no authoring or generation release.


The complete saved one-path design at design.md3903 is accepted. Authoring was
released to retained Implementer0, turn01a112c6-5335-7bb0-9aed-72eeea99c1b4,
for `tests/suite/admin/nodectl-refresh-and-runtime-state.nix` only. The live
transition uses installed Ruby for one nonblocking AF_UNIX probe: validated
parent and absent-path lstat, or exact ECONNREFUSED at a socket. Successful or
in-progress connections, other errors and cleanup failures refuse. The host
requires integer zero and one exact allowed label. OS unlink and fresh-boot
Node pathname predicates remain strict; all system/storage/RPC checks remain.
No guide update is needed: the checked maintenance guide makes no Node unlink
promise. Member freeze98904a58 and static Nix parse/format, full-script/probe Ruby syntax
and scoped diff checks passed. Lead inspected the entire one-file diff and
all3246 source/index/cache guards passed0.965s, executed0. Original first
example and all remaining predicates are preserved. Runtime/other source,
index, contract2 and publication remain held.

Fresh Luna/low utility admin_node_endpoint_fixture_eval_20261006 owns the one
actual scenario drvPath evaluation at /tmp/adminsocketcheck.7v04rosh. Frozen
9276d8b0/drivercaf14c8f/wrapperafa57da9/gate4fffa4dc bind the held source;
The single evaluation passed0/63.619s/parity1, stage60.722s/child_waited1;
main rechecked the full guard and original PGID2928668 had zero same-UID
members, no signals. It constructed the actual scenario JSON derivation and
executed no VM. Only the scenario file is staged. Original0d is retained under
a session backup ref. Fresh Luna/low admin_node_endpoint_fixture_amend_20261006
owns the normal unpublished amend at /tmp/adminsocketamend._l3bck61; frozen
1ded2d0f/driverda7801cf/wrapper5706e866/message810add8c bind staged tree0f11bc17
and unchanged parentbc9. The normal amend passed0/55.543s/parity1, producing
6cd9f9a6/tree0f11bc17 with source/cache parity and clean index. Parent verified
all hooks passed; child stderr retains a nonfatal TextWidth warning (maximum79
within the required80), correcting the utility's wrapper-only no-warning
observation. Original PGID2943088 had zero same-UID members, no signals.
The old-to-new source delta is exactly one scenario file; all three migration
and schema blobs remain identical. Complete range26commits/218paths/25850+/457-,
unit5paths530+/2-, completeSHAd775c3e7/unit905597f9/remediation9248fddb bind the
[final inventory](storage-admin-maintenance-profile-endpoint-inventory.json).
Lead accepted the focused direct-step9
[disposition](storage-admin-maintenance-profile-endpoint-disposition.md) under the
original complete review, without a new reviewer rerun or physical claim.

Fresh native Luna/low admin_maintenance_profile_corrected_vm_20261006 owns the
same existing two-example scenario at exact6cd. Packet /tmp/avmendpoint.zau3c8b3,
frozen25a16a7d/driver867b1a34/wrapper34fefde1/gatecba8c02a bind all3246 source
entries, index, refs and foreign state. Parent preflight passed0.938s/parity1,
executed0. The ordinary runner uses its fresh private state with
--no-destructive/--stop-on-failure. That run was cancelled at the user's pause:
waited driver1/401.630s, stage1/397.138s, parity1 and no completed examples.
Watcher verified exact PGID2953490 and sent TERM only; no KILL was needed.
Parent's bounded same-UID PGID scan returned zero. This is incomplete user
cancellation, not an assertion failure. Old packet and failed run remain
untouched. User continue authorizes fresh source verification; new prepared
packet /tmp/avmendpoint-resumed-20261006.juule2dt has unchanged driver867b1a34,
wrapperd56ef309, frozen1b4a0a05 and unchanged review gatecba8c02a. Its full
source/index/cache guard passed2.419s/parity1/executed0. After the separate
retained-cluster stop completed, fresh Luna/low utility
admin_maintenance_profile_resumed_vm_20261006 launched the same existing
scenario once in fresh private state. The batch passed0/869.343s/parity1,
stage0/865.272s/child_waited1. Native script606.47s: original Node-status and
read-only-RPC example1/2 PASS5.13s; ordered maintenance activation/fresh-boot/
restoration example2/2 PASS242.56s. Parent rechecked the complete frozen
source/index/cache guard0.947s/parity1; bounded same-UID stagePGID3056416 scan
returned zero, no signals. No local kernel compilation was observed. This
proves the installed generation/service/endpoint, current/booted systems and
boot-ID changes, Pool/Dataset GUID/property/known payload and config/key equality,
and ordinary restoration/RPC predicates in this disposable scenario. It does
not prove production bootloader persistence, complete descendant/delegated-GC
reap, physical exclusion, retained alias/NAS history or real payload recovery.
It did not use or restart the retained cluster. See the
[accepted corrected VM result](storage-admin-maintenance-profile-resumed-vm-result.json).

Parent fetched the canonical SSH remote after accepting the run. Default and
merge base remainc4d; feature425d is an ancestor of6cd, no rebase needed.
Fresh Luna/low admin_maintenance_profile_publication_20261006 now owns one
normal exact-lease feature push/readback at
/tmp/admin-maintenance-publication-20261006.lg7s1d8p, driverf8d6a1e8. Publication
passed0/15.430s, pushchild0/10.859s/waited1/sourceparity1. Actual SSH readback
is exact6cd feature and unchangedc4d default; final c4d..6cd comparison is saved.
Normal declared shell/hooks were used, with no bypass. Parent inspected actual
child output rather than treating wrapper silence as a no-warning certificate.
Current6cd workflows are in progress, unawaited. A cancellation request for
sole superseded425d CI37492572220 was submitted successfully; its completion
is unawaited. Defaults, package and retained-cluster selection stay unchanged.
See [feature publication result](storage-admin-maintenance-profile-publication-result.json).

After this accepted composition source-delivery checkpoint, initial fourteen
static Contract2 paths were released to implementer0 at published6cd, clean
tracked/index and preserved PHP cache. The accepted seventeen-path design is
unchanged; generated schema/locales stay held for guarded parent generation
and exact member installation. Main owns the three technical-document prose
passes after handoff. Authoring supplies no operational handoff, termination,
physical/G2/alias action or default/package/live authority. Source/index and Contract2/publication/live holds
remain. The failed first VM and its
unknown operand remain separate evidence. No socket deletion, timeout change,
retry or physical-exclusion claim follows from the source diagnosis.

### Admin maintenance profile committed and reviewed, 2026-10-06

The five-path source unit was frozen at Adminbc9bb38. Lead inspected the profile,
actual-module check, flake exports, extended Node scenario and owning guide.
The original API/RPC example and documentation prefix remain unchanged.
Main applied the required prose pass directly; the guide's final SHA929b4a92
retains the import example, identifiers, refusal and compatibility boundaries.
All five full hashes match the member manifestf7c4f573; source patch60c96c98
and normal owning message3d000f9f were used for the completed commit below.

Member static checks passed: four Nix parses/formats, extracted Ruby syntax and
scoped whitespace. The 30 module projections, nine refusals and two VM examples
are authored inventory, not results. Lead verified all3241 outside tracked
files and the declared PHP cache against the pre-authoring byte/stat baseline.
Only the two new Nix files were staged for Git-backed flake access; all five
source bytes and the index are held. Inputs and the accepted OS800 lock remain
unchanged. The complete current-source patch binds SHAeaec2703.

Fresh Luna/low watcher admin_storage_maintenance_profile_checks_20261006 owns
one batch at /tmp/adminprofile.hz4jzg1p. Frozen4f2c551e, drivere2867c67,
wrapperf5653310 and source-gatede4070d4 bind all3246 source entries, exact index,
heads and declared foreign state. The batch passed0/201.805s/parity1: focused
build60.370s, all six actual check drvPaths72.707s, exact registered Node scenario
JSON drvPath63.678s. Main read the built output: all30 projections are typed
true. The installed halt policy checks ran in the focused derivation. Main
rechecked source/index/foreign guards and proved all three original stage PGIDs
empty, no signals; no kernel build was observed. See the
[accepted check result](storage-admin-maintenance-profile-check-result.json).
The evaluations construct derivations; they do not execute other check bodies
or the two VM examples. Broad flake
validation stays blocked by the reproduced predecessor overlays.list shape;
no repeated baseline run or overlay fix is selected.

One parent-only inspector could not start through unified exec; the same pinned
bash executable and /bin/sh were positively verified, with no test re-execution.
A parent-only metadata projection initially assumed full store paths; pinned
Nix2.34.8 metadata version4 uses store-relative names. The exact version4
projection then read the already-built output without rerunning a build.
See the [metadata note](../../notes/cross-project/2026-10-06-nix-derivation-v4-store-relative-paths.md).

Fresh SSH fetch retains master/basec4d and remote feature425d, so no rebase is
needed. All five owned paths are now staged at treeef6b3371. Fresh Luna/low
admin_storage_maintenance_profile_commit_20261006 owns the normal commit/hooks
at /tmp/adminprofilecommit.qy48_31e: frozenfa12820c, driverda7801cf and
wrapperd5a571fb. The normal commit passed0/59.850s/parity1, all required hooks.
TextWidth warned on14 body lines above72; maximum79 satisfies the mandatory80
column limit. No hooks were bypassed. Final0d5c855c2493dec51ec400a99ea3f61dc8e31469
has treeef6b3371e2158a5b1c0de5273234057f2e101e63 and parentbc9. Lead independently
matched all3246 source entries and foreign byte/stat state, clean tracked/index,
original PGID2627173 empty and no signals.

Complete final history has26 commits/218 paths/25793+/457-, with five-path
unit473+/2-. [Inventory](storage-admin-maintenance-profile-inventory.json),
[complete diff](storage-admin-maintenance-profile-complete.diff) and
[unit diff](storage-admin-maintenance-profile-unit.diff) bind exact final source
and three migration versions/provenance; completeSHAf0466c6d/unitSHAeaec2703.
Retained independent reviewer0 is assigned all four HIGH lanes on the COMPLETE
c4d..0d range, turn01a1128f-182f-7ca2-a2ab-36a50613d1d5, saved Sol/xhigh/read_only.
The [review packet](storage-admin-maintenance-profile-review.md) distinguishes
source checks carried through unchanged bytes from final runtime proof. All
final review completed all four HIGH lanes with no Blocking/Important.
[Consolidated result](storage-admin-maintenance-profile-review-result.md) records
the accepted comparator Advisory, complete history/no-obsolete conclusion and
three preserved migration versions. No source remediation or review rerun is
required. Supplied checks remain parent/watcher evidence; the owning VM is unrun.

The first exact-head VM packet /tmp/avm.jf7ha2ma completed: frozen64a7ab89,
driver867b1a34 and wrapper8b3baf45 bind final0d, all3246 source entries, clean
index and preserved PHP cache. Lead accepts the completed review disposition
and releases only this prepared exact-head verification operation.
The sole command runs the existing admin/nodectl-refresh-and-runtime-state
scenario with a short private state path, no-destructive and stop-on-failure.
Final review disposition and prefix preflight0.947s/parity1 preceded fresh
Luna/low admin_storage_maintenance_profile_vm_20261006. Review gate8ab9799f
records exact0d review acceptance. The waited run failed1/1714.637s/parity1;
stage1710.327s, native first RPC example passed and second failed908.8s at
`test ! -S /run/nodectl/nodectld.sock && test ! -S /run/osctl/osctld.sock`.
The successful switch and both runit down acknowledgements precede the combined
wait. That result does not identify which path or a live listener/daemon.
Normal stop/fresh maintenance boot/restoration were not reached. See
[first VM evidence](storage-admin-maintenance-profile-vm-result.json).
Parent final source/index/cache guard passed. Original PGID2716429 is empty;
readable same-UID prefix command/FD counts are zero, with four FD observations
unreadable. No unqualified global FD absence is claimed; no signals/kernel
build were observed. Native runner disks/logs/state remain retained.
Implementer0 read-only source diagnosis turn01a112b9-7b38-7a21-a8fd-4c657ee9bcef
is active. No runtime cause, correction, rerun, publication or new source gate
is inferred. Earlier source checks/review keep their scope.

The next contract2/handoff_pending API design is accepted as a separate
record-only source slice, still unreleased. Its operational invocation needs
separately reviewed responsibility recovery/termination and physical contracts.
This adds no gate to the current composition. Architect's public-source
containment/reap assessment is complete in design.md under
"G1b service containment and reap: public-source assessment, 2026-10-06".
Runit is the appropriate service owner, but existing immediate-group TERM and
process-only controls provide no complete incarnation-bound descendant wait
or delegated-GC coverage. Empty membership/socket or kernel kill is not a reap
receipt. The proposed entry-failure hardening remains only a candidate
precursor; no authoring release or complete stop/reap manifest is accepted.
Interrupted physical-work settlement remains separately unresolved.
Implementer0 completed read-only next-slice preparation, turn
01a1129d-4852-7ab2-b594-26ea7cc6ca98, on exact0d/treeef6b/clean index. The
seventeen-path manifest is sufficient (fourteen static plus schema/EN-CS
companions); proposed130000 migration/spec paths are absent. No authoring,
checks or runtime operations occurred. Existing unsupported-record fixtures
persist contract2/reserved; the new explicit SQL tuple constraint must refuse
that malformed setup, so those owning tests need separate constraint and
reader-refusal coverage. Do not weaken the constraint. HaveAPI normalizes its
integer parameters; strict Integer CAS tests belong at the model boundary,
without a new raw-JSON interface. Existing concurrency/reap/status/metadata
owners suffice. No wider scope or material design conflict was found; source
release remains held until the current composition completes.
Live Admin290f, the stopped scheduler, aliased DIPs and all retained
objects/evidence remain unchanged.
No default integration, deployment, capture or physical action is authorized
by these source checks.

### First owning VM failed; bounded fixture correction, 2026-10-06

The following records the first run and its correction. Current source and
the second run are recorded in the next checkpoint.

Exact8e0 source run /tmp/osvm.zov_e_u4 was waited: exit1/416.137s/parity1,
stage413.253s, first seven examples passed, eighth failed7.09s. The initial
disabled switch itself passed0/5.05s and stopped osctld without osctl activate.
The disabled_services compound check failed1/.22s with no output, before the
owning stop/fresh-boot/return assertions. All original checks/evidence retained;
this is no full transition or preservation acceptance. Main proved original
PGID1345014, exact packet-prefix cmdlines and FD holders zero, no signals.
Ordinary cleanup poweroff returned0/.28s; this does not replace owning assertions.
No Linux compilation was reported or found in the supplied build lines.

Main reproduced a process-check hazard using the actual guest procps4.0.6
binary. Each probe was restricted to one newly spawned/waited host-only child:
the exact failed compound argv matched the daemon regex, neutral argv did not,
and daemon argv did. Private proof /tmp/ospgrep.d1ohn7ow/result.json binds
commandSHA676ea9fd. No guest/live/source mutation occurred. The original
unlabelled compound does not identify its first failing predicate, so this
proves the self-match hazard without claiming every other predicate passed.
See the [reusable process-assertion note](../../notes/vpsadminos/2026-10-06-process-assertion-self-match.md).
Pool-tank's check also reported running while later logs reached completion;
its prior marker semantics remain a source nuance, not an assigned cause/fix.

Lead released only tests/suite/system/switch-to-configuration.nix to the same
implementer turn01a11253-f29b-7ee2-b49f-90f93cdd4818: isolate the same daemon
absence predicate from literal service-path arguments, add fixed failure labels,
preserve all eight examples/first-seven bodies, normal stop/boot and every
system/GUID/property/payload check. No runtime/framework/timeout/scenario or
Pool-wait change is released. The exact static-only member freeze was accepted
and folded as recorded below. Publication, Admin pin/composition and all
alias/G1b/G2/physical/default/live actions stay pending/held.

### Process assertion corrected; second owning VM passed, 2026-10-06

Lead inspected the complete one-path18+/18- correction and exact reverse
lambda parity. Final scenario SHAaa75c103 binds the same eight examples;
all first-seven bodies, helpers, runtime sources and normal stop/boot/system/
GUID/property/payload assertions remain unchanged. Each original compound
predicate now has a fixed failure label. The same daemon regex runs separately
without service-path literals in its argv, and requires pgrep status1 exactly.
This fixes the reproduced self-match hazard without attributing the first run's
unlabelled failure or changing Pool waiting semantics.

Normal owning amendment passed0/13.022s/parity1 with every mandatory hook;
final80034c8cc6489db6287b43f439a9617511f14908,
tree497afa5c0863b2dd824664408a0e06cba4c0305d, parent7f85 and message unchanged.
Original8e0 is retained in an explicit backup. Main proved commit PGID1389319
empty, no signals; source/index clean, all other10 owning paths and64 foreign
files/17 directories preserved. Complete history remains two coherent commits,
26 paths1709+/82-, unit11 paths826+/59-, no OS SQL/schema migrations.
[Current inventory](storage-os-disabled-process-final-inventory.json) records
completeSHAde0d26fc, unit89f8a457 and the exact one-path fix2a051047.

Fresh Luna/low watcher osctld_disabled_process_corrected_vm_20261006 launched
the existing system/switch-to-configuration scenario once at /tmp/osvm.acec89l4.
Frozend695bb19/driver015a159c/wrapperd04b583b/review-clearancef9a216d7 bind
exact800 source/empty index/foreign inventory. The waited result passed
0/623.055s/parity1; runner620.272s, all8 examples successful, final216.37s.
The expected-success result and actual scenario assertions prove normal-to-
disabled activation, normal installed poweroff, fresh disabled boot on retained
disks and ordinary return with exact systems/new boot ID, pool/dataset GUID,
active property and known payload equality. Main independently rechecked
source/foreign parity and proved PGID1398701, exact packet-prefix cmdlines
and FD holders zero, no signals. No Linux compilation was observed. This is
disposable transition proof, not production bootloader persistence or physical
exclusion.
Original all-four review plus shutdown direct-step9 disposition is preserved;
this bounded fixture-only correction adds no runtime/interface/authority change.
Broad flake validation remains baseline-blocked. Fresh SSH fetch keeps
stagingcbfc and remote feature8d05; no rebase was required. Normal exact-lease
SSH publication passed, readback confirms feature800/stagingcbfc unchanged and
the final comparison is captured. CI37509517986/RSpec37509517958/RuboCop37509517981
are in progress at800, unawaited; no superseded active same-branch run was found.
No default/package/live/physical/G2/alias action is inferred.

Fresh Admin SSH fetch retains masterc4d/feature425d/basec4d, no rebase.
Fresh Luna/low admin_os800_dependency_update_20261006 launched once at
/tmp/adminosdep.pye1en2t from the clean425d source/index. Frozena0896b0e,
driver99c9333d, wrapper78f10b69 and releaseaf894b15 bind all3244 sources,
existing cache and accepted published800. The existing update_vpsadminos_flake.sh
owns generated lock-only normal commit/hooks; its exact dependency graph is
planned graph checks and ordinary no-build. The actual outcomes follow below.
The owning updater itself passed0/65.597s with all hooks, committing
bc9bb38ee6f87dcd092097e512c5c84d74fc2417/treec5afa522af6894a04249e04c0a761d5ef47b37fe
at parent425d: only flake.lock9+/9-. The first private batch then refused
1/67.574s on its incorrect `OS original refused` expectation; its reported
old head/sourceparity0 are not acceptance evidence. No-build was unrun.
Main inspected the actual final graph: exact OS800, only vpsadminos/nixpkgs_2/
nixpkgsUnstable locked values change; original staging reference, all edges,
flake.nix and every other source/cache/index are unchanged. LockSHAe7b83936.
This is the required mechanical generated update, review-exempt. Main proved
owned PGID1539645 zero, no signals. See the [guard lesson](../../notes/vpsadmin/2026-10-06-generated-lock-original-reference.md).

No updater retry or source change followed. Fresh Luna/low watcher
admin_os800_pin_no_build_20261006 owns ONLY existing no-build at bc9,
/tmp/adminpincheck.ycyd54db, frozen46dfa9f7/driver397bc0e0/wrapper651bab40/
gate118ce767. The waited no-build failed1/3.634s/parity1, child0.696s, at existing
`overlays.list`: overlay is a list rather than a function. An immutable complete
425d source snapshot (all3244 bytes verified) reproduces the same error1/.408s.
The initial bare-path baseline attempt failed before evaluation at Git discovery
1/.125s; explicit path: selects the intended snapshot. Both histories remain.
No broad flake pass or overlay-source change is claimed. The mechanical pin
prerequisite is accepted; bc9 remains feature-only/unpublished.

Lead released the accepted exact five-path profile implementation to
implementer0 from clean bc9. Existing exported/default integration and retained
settings/packages/roots remain; the profile is opt-in, final contradictions
refuse. Focused actual-module/build/evaluation, full-range review and existing
Admin VM are pending. No new API/SQL/Node/protocol/ownership/containment unit or
live authority is released.

### Corrected OS source accepted; owning VM earlier launch, 2026-10-06

Final8e0b2d9fa1876ad2e28ce34e23724f841cacec01,
tree39155267633908eadee772caac39cd8c5b74c630, parent7f85 unchanged.
Normal owning amendment passed0/13.411s/parity1; Nixfmt/RuboCop and all
message hooks passed, no bypass. The expected Nix dirty-tree warning came
from the staged amendment, not a hook failure. Index/tracked source clean;
64 foreign files/17 directories unchanged. Main proved owned commit PGID1340289
empty, no signals. Fresh staging fetch/readback remains cbfc, no rebase.

Original all-four-HIGH cbfc..097 review is preserved. Lead inspected and
verified the exact seven-path installed-halt/stage3 remediation under mandatory
step9, with no new public/authority/containment boundary. The sole Important
is resolved in the [consolidated result](storage-os-disabled-review-result.md).
Complete final history is two coherent commits26 paths1709+/82-; new unit11
paths826+/59-. No OS SQL/schema migrations or obsolete/fixup history added.
[Final inventory](storage-os-disabled-final-inventory.json) records complete
SHA316b6188, unit0ab5b344 and exact remediationf067a4e1.

Fresh Luna/low watcher osctld_disabled_corrected_owning_vm_20261006 owns the
single existing system/switch-to-configuration scenario at /tmp/osvm.zov_e_u4.
Frozene4420be8/unchanged driver015a159c/wrapper1acca815/clearance1526955e
bind final head/all2238 sources/empty index/foreign64+17. Ordinary runner uses
short state path, --no-destructive and --stop-on-failure; existing eight examples,
normal machine.stop and framework deadlines are unchanged. This earlier launch
subsequently failed as recorded above; it does not certify final800.
The old /tmp/osvm.07em5svg remains unrun and cannot prove this changed head.
No live cluster, physical exclusion, G2/alias disposition, package/default
integration or publication is implied. Admin composition stays accepted but
unreleased, after tested/reviewed/published OS and generated dependency delivery.

### Earlier OS review and shutdown correction, 2026-10-06

Reviewer0 confirmed an Important finding in original09786fbc, general and
risk/compatibility lanes. After the new scenario proves osctld/socket absent,
Machine.stop invokes poweroff -f. The installed Halt wrapper still invokes
osctl shutdown --force; its missing-socket path waits for a marker producer
that is intentionally absent. Normal disabled-generation poweroff/reboot
has the same defect. Lead source inspection confirms it; non-force confirmation
also invokes osctl ct ls unconditionally.

The owning VM stays unrun. Increasing its timeout or replacing normal shutdown
with a test-only forced stop would not resolve the consumer. Architect0 saved
the final seven-path correction brief; lead accepted it and released static-only
authoring to implementer0, turn01a11228-da69-7c52-ae1b-1f0525d0765a.
The preliminary six-path release is superseded by explicit seventh-path
steering; no contrary source decision remains. The consolidated independent
report confirms this as its sole finding: no Blocking or additional
Important/Advisory. All four lanes and complete history/migrations were reviewed.
See the [review result](storage-os-disabled-review-result.md).
The final brief also covers config/runit.nix stage3's second unconditional
shutdown request, confirmed by lead source inspection. The same final
osctld.enable predicate gates only that command, preserving both clock writes
and all other stage3 behavior. The generated Halt predicate preserves enabled
shutdown; disabled skips only daemon-dependent blocks. Actual generated-class
and recording-stub stage3 checks accompany the normal owning stop/boot scenario.
Seven correction paths overlap three original paths: expected final unit11,
subject to actual inventory. The final seven-path correction is frozen on097;
lead completed diff/source inspection with no concrete deviation. All seven
hashes match manifest418a32c9 and correctione7310de6. Main guard confirms2238
tracked files/2231 outside the seven, empty index and unchanged64 foreign files
in17 directories. These are source/static facts, not finding resolution.
Both technical docs were handed back and the main-agent prose pass is complete:
runlevels SHAe2360e7e5bf8487f3fffba82370591f1b10d5c9f0f63aac591823068d00a95e1;
installed halt manual SHA4087adbeff43b29268c0ad26658a81db43c79028ab6f50c828f682e04f273a0a.
Protected commands/options/code samples and surrounding sections remain equal
to the technical handoff; scoped diff check passed. These two bytes are held
for inclusion in the final seven-path freeze. Runtime tests remain unrun.
Parent's raw-template Ruby syntax check failed at the bare Nix boolean marker
in halt.rb. Lead relayed a bounded representation correction: quote the rendered
true/false token and compare it with the string `true`, keeping the constant Boolean
and the final Nix option as its sole input. No runtime discovery or hook/exclusion
change is allowed. Raw and both rendered syntax checks passed before freeze;
this is static template evidence, not an observed shutdown/runtime failure.
The fresh Luna/low watcher osctld_shutdown_corrected_checks_20261006 owns the
three-command quick batch at /tmp/oshalt.f01o2t52: focused actual check build,
all five check derivations and the exact owning scenario JSON derivation.
FrozenSHA0d8e254f, unchanged driver2fbe7bcb and wrapper12deac92 bind all source,
index and foreign files. The waited batch passed0/217.826s/parity1: focused0/35.527s printed
module19/activation6/halt19/stage3four; five derivations0/131.134s;
scenario JSON0/46.441s, exact r529qzgk derivation. Main inspected all results
and proved stage PGIDs1329162/1330766/1334923 empty, no signals. The ordinary
broad flake gate remains baseline-blocked; other check bodies and VM unrun.
Fresh SSH fetch/readback keeps stagingcbfc and feature remote8d05; no rebase
is needed. Lead staged only the seven correction paths, saved reviewed097
backup and tree39155267. A fresh owning-fold watcher at /tmp/osfold.1xk1um5o
is active; amendment/hooks results are pending. Message words are preserved
with72-column wrapping, and hooks remain mandatory.
Prior checks remain scoped to their unchanged original bytes. The prepared
VM clearance remains absent and its original-head guard will refuse a changed
head. All live, alias, package/default and physical/G2 holds remain.

### OS committed; complete branch review finished with a finding, 2026-10-06

Final OS HEAD09786fbc20a2d8e134e2e3001d53ef287646e74b,
tree523c25edbb0bb2675c88b3c5d083aab907d6703a,
parent7f85b137835907b3a786dec225a49e9ff694537a. All seven intended paths
are committed; tracked source/index are clean and all64 foreign files remain
unchanged. Inputs/lock remain exact stagingcbfc. No new source was published.

The accepted bounded evaluations passed0/183.911s/parity1: all five actual
check drvPaths0/131.341s and the registered switch-test JSON drvPath0/48.851s.
They construct those derivations; they execute neither the other four check
bodies nor the eight VM examples. Focused19/6 runtime evidence carries on
unchanged source. Ordinary full flake validation remains baseline-blocked.
See the [reusable baseline note](../../notes/vpsadminos/2026-10-06-flake-overlay-list-validation.md).

Normal owning commit passed0/14.453s. Two message-width warnings were resolved
with a normal unpublished message-only amend0/13.420s; source/tree/parent
unchanged, all hooks passed without warnings. Final index is empty. No hooks
were bypassed, and no source rerun is implied by the message-only amendment.

The complete cbfc..097 range contains two coherent commits,22 paths,
1265 additions/49 deletions. Complete binary/full-index SHA256
27831036572eaed0648b5449c8fbf66367666d30013dea3dc2048b19ce84389e.
No OS SQL/schema migrations are present. Retained reviewer0 (Sol/xhigh,
read_only) owns all four HIGH lanes, turn01a11218-1ee1-7120-b079-a2d3dc36e4ea;
review is complete with the shutdown Important open. See the
[complete review packet](storage-os-disabled-review.md),
[inventory](storage-os-disabled-inventory.json),
[complete diff](storage-os-disabled-complete.diff) and
[new unit](storage-os-disabled-unit.diff).

The existing owning switch VM is unrun and follows review disposition.
Its prepared private packet is /tmp/osvm.07em5svg: frozen15e3276e,
driver015a159c, wrappera1f84ff1. It uses the ordinary runner's short state path,
--no-destructive and --stop-on-failure, exact2238 source/index guards and
unchanged64 foreign files/17 directories. The review-disposition file is absent;
the packet was syntax-checked but not executed. No new test runner or retry
mechanism was added. Parent also proved the message-amend PGID1228061 empty.
Admin composition is accepted but unreleased; its clean-source generated OS
dependency update follows reviewed/tested/published OS source. No physical
exclusion, API handoff, alias recovery, package activation or default merge
is supplied by this checkpoint.

### Earlier OS freeze and baseline flake failure, 2026-10-06

The seven-path source is frozen at unchanged OS7f85b137 on stagingcbfc.
Lead inspected the complete runtime/test/doc delta and found no concrete
design deviation. All seven hashes match the member manifest3698e6c3 and
patch32202b97; all other tracked source, lock and64 foreign files/17
directories are unchanged. Lead completed the runlevels prose pass at
SHA4e1c2e57; original code sample, links and technical limits are preserved.
Only the new tests/osctld-disabled-eval.nix is staged for Git-flake inclusion,
blob14d6caad. The remaining six paths are unstaged and all seven/index held.

Member static evidence: Ruby syntax for runtime/two extracted scripts,
five Nix parses, five nixfmt checks and scoped whitespace checks passed.
Authored19 module predicates/6 activation cases and8 owning scenario examples
(7 unchanged plus1) are not results.
Fresh focused selection is Nix build osctld-disabled-eval, then flake check
without builds, under /tmp/osdisabled.iq19cihf/. FrozenSHA2a754a9e,
driverSHA2fbe7bcb guards2238 source entries, staged index and complete foreign
inventory. The first watcher stopped on its own non-mutating help/preflight
error before the driver; zero checks ran. A fresh watcher owns the same
unstarted selection through a simpler bound preflight.
The bound batch finished exit1/59.540s/parity1: focused build passed0/55.664s
and printed module_checks=19/activation_checks=6. Standard no-build failed1
in0.195s before reaching checks because flake.nix exports overlays.all as a
list, while Nix2.34.8 expects a function. The immutable7f85 baseline reproduces
that failure; its flake/lock are exact stagingcbfc bytes. This is not a new
runtime regression or a broad green result. Parent verified2238 source/index
parity and both owned stage PGIDs1204648/1207032 empty; no signals.
Lead requested the design owner's bounded alternative: evaluate all five
declared check derivations and the registered owning switch-test JSON
derivation without builds. The prepared /tmp/oseval.8v81f2qd subsequently
passed both evaluations as recorded above. No overlay/public-interface source
edit was released.
No VM, physical exclusion, package delivery/default integration or alias/G2
operation is implied.

### API reservation reviewed and feature-published; OS authoring active, 2026-10-06

Final source is Admin425d399afb3876bde4f3f4023f3810a45bee6f3f,
treec0babd3297b9c0bbab2eb35b322ca902ca675bdd, parent5dd06eeb.
All20 intended paths are committed; tracked/index clean, declared PHP cache
preserved. API73/0, migration6/0, final API+root lint12/0 each, selector20/89/0
pass with the scoped receiver/comment equivalence described below. Normal
amend passed0/66.273s with all hooks passed without warnings, source/tree parity1
and private cleanup1; original spawned DB absent/owned PGID0/no signals/prune.

The complete branch has24 commits/214 paths/25320+/455-. All three migrations
have explicit provenance: foundation/index consumed unchanged, reservation only
disposable generation/spec use. Complete binary SHAab5ea0b9b10dc698520e7af29a07bc7434b6e662a13c5f7ed51a5078b1740114.
Retained reviewer0 (Sol/xhigh/read_only) owns all four HIGH-risk lanes,
turn01a111d3-499a-7ae3-a36c-977d8002dc6e; complete report accepted. See
[final packet](storage-maintenance-reservation-review.md) and
[original reviewed inventory](storage-maintenance-reservation-inventory.json),
[final amended inventory](storage-maintenance-reservation-final-inventory.json)
and [independent result](storage-maintenance-reservation-review-result.md).
Reviewer0 reports one source-backed Important omission: the three advertised
maintenance actions are absent from covered/pending endpoint manifests, so the
existing endpoint coverage gate would fail. Only
api/spec/api/covered_endpoints.yml is released as the20th companion path,
turn01a111d8-ad0d-7273-8228-3dede274f158; addexact three covered scope entries,
other19/runtime/index held. Existing full-plugin endpoint_coverage_spec is the
focused regression gate. The exact three-entry correction is frozen at
SHA256 ec79801a5962be80a21063c4ab32ad08a4d44347cbe098472d941a3f2b233ceb.
The existing full-plugin endpoint gate passed: 1 example, zero failures,
pending or outside errors; wrapper exit0/54.508s/parity1 and private cleanup1.
Parent proved the original database PID absent and owned PGID empty; no
signals or prune. Evidence: /tmp/rescoverage.780l9mav/.
Normal unpublished amend at /tmp/rescoverageamend.q_bhrt6t/ passed exit0
in72.166s/parity1 with all hooks passed, private cleanup1 and no bypass.
Parent proved exact staged/final tree, all3244 source bindings, unchanged
other19/message/PHP cache, empty index, absent original database PID and owned
PGID0. The committed edc..425d delta is only those three manifest rows.
Lead has directly verified the requested remediation under step9; the
consolidated independent report confirms its resolution and inspects the
endpoint-only committed delta. Primary review remains edc plus directstep9.
This is direct mandatory-review step9, with no new public behavior,
policy/version or automatic full review/test rerun. Reviewer completed the exact
COMPLETE c4d..edc committed source/history assessment is complete in all four
HIGH lanes. No Blocking/Important remains; one comparator repeated-scan
Advisory is accepted for a separate measured cohort/indexing follow-up. It
introduces no reservation or physical-trial gate. The reviewer confirms coherent
history/no obsolete approach and all three migration lineages; consumed
predecessors are preserved and the new additive migration was disposable-only
at review.
Fresh SSH master/base remains c4d. Normal force-with-lease feature publication
and exact SSH readback at425d are complete; master is unchanged. Final comparison
is captured with basec4d/head425d and original registration base retained.
The new migration is now feature-published, without live/external DB use.
One bounded CI metadata read found four current-head active runs and no
superseded active run; nothing to cancel, no CI wait. No default/live delivery.
Architect0 completed the next seven-path OS prerequisite brief at
[design.md](design.md#next-common-g1b-slice-an-osctld-disabled-generation-prerequisite-2026-10-06).
Lead accepts its bounded option/pool/activation design. Normal OS replay onto
fresh SSH staging cbfc283d completed exit0/7.953s. New head7f85b137835907b3a786dec225a49e9ff694537a
preserves the exact one-commit activity patch (range-diff=), all five upstream
commits/lock/OSVM and all62 retained temporary files. Consumed8d05 has an exact
backup; pins/remote feature remain unchanged. See
[OS replay inventory](storage-os-cbfc-rebase-inventory.json).
The first attempt stopped on Overcommit's stale configuration signature before
rebase. Parent reviewed the configuration/custom hook and registered its normal
signature; no hooks were bypassed. Two watcher context preflights executed
zero commands; the cached short signing/replay ran inline with existing guards.
Implementer0 owns exactly the seven-path authoring/static unit under
turn01a111ed-59cc-78d2-a577-f00b63841fcc. Checks, commit, review and owning VM
remain pending. Docs return to lead for prose; no other source/runtime release.
The OS generation prerequisite supplies no physical exclusion or G2 authority.

The generation and check history below retains its original byte scope.
At the initial freeze, source was at Admin5dd06eeb, index empty.
The final 11 receiver substitutions in three model specs reconstruct the prior
bytes exactly when reversed; installed RSpec3.13.6 binds the same real classes
through all string contexts. API73/0 and migration6/0 from the full style batch
therefore carry for unchanged runtime and equivalent receiver spelling. Fresh
lint passed all 12 inspected files with zero offenses.

The lint/selector batch at /tmp/rescheck.wz3_n6re/ failed1/32.155s,
waited/parity1/cleanup1. Selector failed before examples with minitest/autorun
LoadError (stage11.572s). Parent proved the original private DB process absent.
Source diagnosis: RubyGems explicitly loads BUNDLER_SETUP, which the nested API
Bundler environment retained after clearing RUBYOPT and common selectors.
Bundler's own with_unbundled_env clears that variable. The private driver now
uses this standard helper around root-shell spawn; product source, command,
database guard and coverage remain exact. No application dependency edit.
Fresh626 Luna/low reservation_unbundled_selector_20261006 owns selector-only
/tmp/resselect.a5vtamy1/; frozen813ee390/driverfe94d8a9/guard911c91cb/
wrapperaf1d488e. Selector passed0/21.586s, waited/parity1/cleanup1,
stage7.643s:20 runs/89 assertions, zero failures/errors/skips. Parent verified
all3244 source bindings, original private DB absent and owned PGID count0;
no signals or prune. This is scoped selector evidence, not an all-suite rerun.

Normal hooks are installed/active and bypass selectors are absent. Fresh SSH
master/base remains c4d. A cache-path preflight refused before staging because
the retained PHP cache is a file beneath its directory; the corrected guard
binds that exact preexisting file. Parent staged only the 19 owned paths,
matching all tested source hashes, tree675ed9ea6b33cba4625864159441a305ee0aad76.
Fresh626 Luna/low reservation_owning_commit_20261006 owns the normal hook commit
at /tmp/rescommit.491dbf3p/ (frozen682f1976/driver7a9cfae7/wrapper5df5cd2a).
Normal commit passed0/66.315s, waited/parity1/cleanup1. New unpublished
head06434a329a96525d7add643ae564210f256ebdc1 has exact tested
staged tree675ed9ea and parent5dd06eeb. Parent verified all3244 source hashes,
empty tracked/index changes, unchanged retained PHP cache, original private DB
absent and owned PGID0; no signals/prune. The wrapper's head field intentionally
names its input base; actual Git and final tree prove the new commit.
Normal hooks passed with warnings: root RuboCop1.85 rejects four disable-next
comments supported by the API checker; commit-message width also warned.

Only the actor spec is released for relocating those four comments to standard
inline disable directives, preserving every rescue/body/test. Implementer turn
01a111c9-1850-79d1-a238-8b8b77461a7b; other18/index held. Lead will verify both
lint owners, narrow comment parity, then normally amend the unpublished owning
commit with a wrapped message and enabled hooks. API73/migration6/selector20
carry only because comments cannot alter executed behavior. No independent
review is assigned until the final commit; complete c4d..final inventory will
replace the current064 preparatory inventory. Feature publication remains
pending.

Historical generation and verification checkpoints follow.

Provider placement is reviewed and feature-published at e33. Admin replay onto
c4d completed at5dd06eeb5111af52fe49bf76e39f163f83aa8478,
treec79214a735d7a7962313c59b0fdcaa6db6cae407. All23 feature and seven upstream
commits remain; source/locale/CI union parity, consumed migration/schema/input
parity and complete topic coverage passed. Range-diff has21 equivalent commits
and two expected context differences. See
[inventory](storage-admin-c4d-rebase-inventory.json) and
[range-diff](storage-admin-c4d-rebase-range-diff.txt). Fresh selector check passed
18 runs/77 assertions in9.225s, waited/parity1. Original290f backup and remote
remain; historical290f runtime evidence does not certify the new composition.

Initial16 reservation paths were frozen and completely inspected: no concrete
design deviation, empty index, outside-source parity1. Member syntax12/diff0
were static checks. Authored API/model73 (32 new), migration6 and selector20
(two new) were unrun at that initial freeze. Lead prose is complete in the three owning reference
pages. Full19 includes generated core schema and English/Czech metadata.

First private core generation failed1/12.952s, source parity1/cleanup proved1,
no schema. Its ArgumentError has no saved exact frame. Public pinned AR source
shows the adapter changes Mysql2 result defaults to arrays; the private probe
needed an explicit hash result. Fresh corrected generation passed0/23.153s,
child waited1/source parity1, generation16.075s. Core-only proof: sole pending
20261006120000,179→180 tables, unrelated schema changes0, application boot0,
schema installable1 and cleanup proved1. Lead inspected the full schema diff
and proved the original spawned DB process absent; no signal or prune.
Evidence remains in /tmp/resgen.z26aq47e/; failed packet is retained separately.

Implementer installed ONLY path17, api/db/schema.rb, exact generated SHA256
cbce0d81ad37d8a4d621684af58a2a1dd0ec1d7d32eb526bfd9426fda9c0574b.
Diff31+/1-, Ruby syntax/diff0. Initial16, EN/CS predecessor, other source,
head/index and PHP cache remain unchanged. Schema plus initial16 are held.

Private full-plugin locale generation passed0/54.606s, waited/parity1,
generation46.994s/cleanup proved1/application source unchanged1/core schema
unchanged1/plugin schema dump0. The generated diff contains the reservation
metadata only; raw Czech TODOs are prepared output, not final translations.
Evidence and private state remain in /tmp/locgen.wb2i6406/.

Lead applied the owning English/Czech prose workflow. The implementer made
four same-resource metadata changes: distinct reserve/abandon reason text,
`1 to 256`, and an explicit UUID output label. Input names/types/required and
epoch bounds remain exact. Final resource SHA270fbed8bc286d11382773fbe63185a195c033eb0a50995da27d44d0a94b6eb1;
reverse-only-four-change parity restores the original resource. Transcribed
intermediate member hashes are superseded; parent measured the actual bytes.
All other16 source paths/index/cache remain held unchanged. These changes are
metadata prose, not a new authority or interface.

Lead translated30 new Czech metadata placeholders in a separate private
snapshot. Normalization and full-plugin i18n health passed0/98.425s, waited1,
source parity1/cleanup proved1. Both ordinary tasks exited0; generated core
schema/application source stayed exact and no plugin schema was dumped. Lead
accepted the complete locale diff: all2359 old leaves per language unchanged,
29 reservation metadata leaves added per language, no TODOs. Original DB PID
is absent; no signal or prune. Evidence remains in /tmp/lochealth.dplxbw3r/.

Implementer installed ONLY EN/CS exact accepted bytes and refroze complete19
at unchanged5dd06eeb, empty/unchanged index and outside-source/cache parity1.
English SHA9d880d77a5e06bc3a64d10f164987236dd19a2a0cb054684f60eb9f75f56eeea;
Czech SHA2592098d5c2831a2df865422eab4e3afc387660f5b5991d2dfb3e18fc96e5c56.
Both parse/diff checks pass. Final packet
/tmp/storage-maintenance-reservation-final19-20261006.rdmqa4ly/ binds manifest
9aaf7859 and complete patch79aad3d2, including three new unstaged owned paths.
Authored73 API/model,6 migration and20 selector remain inventory, not results.

Fresh managed626 Luna/low watcher reservation_owning_checks_20261006 owns the
four-stage disposable batch: complete focused API/model files, sole new core
migration spec, component RuboCop, and existing root selector. It reuses the
accepted pre-effect guarded Instance/private Unix socket; no app/helper source
or SQL policy change, no shared/live DB, no automatic prune. Packet
/tmp/rescheck.l4zn04rc/ binds all3244 source files; frozen SHA
c6b3fc9f87fcf5f866f75f88dbeab8679ac2900674b2adfa1bdf7c703e9f679d,
driver56522e9d/guard911c91cb/wrapperaf1d488e. Driver Ruby and wrapper Python
syntax passed. First batch failed1/277.995s, waited/source parity1/cleanup proved1. API stage
265.312s, native RSpec73/2/0 pending/0 outside errors, duration253.454s/seed45718.
Later three stages are unrun. Parent confirmed both native JSON and the actual
stage-1 result; early watcher artifact/parity wording was inaccurate. Original
DB/stage PID and prefix process scan are absent; no signals or prune.

The two failed fixtures assume an application422 response for the inherited
HaveAPI empty-required-value validation, and pass a corrupted run epoch into
the supposedly current CAS before owner-consistency validation. Only the two
spec files were released for exact boundary assertions. Corrected source is
refrozen: API spec8e512b9d, actor specedbede33; every other17 path/index/head/
cache is unchanged. Parent inspected the entire narrow diff and verified all
3244 source hashes. Packet /tmp/storage-maintenance-reservation-fixture-fix-20261006.u06447pf/
binds manifest58b4dc05/complete patche9c042cc/correction83caac83. The original
73/2 failure remains prior-byte evidence; no runtime guard defect inferred.

Fresh626 Luna/low watcher reservation_fixture_checks_20261006 now owns the
complete four-stage batch at /tmp/rescheck.eweq0et_/. Frozen SHA
dfe84772e95dfbb924fd7237865da9c4c22dfa15c82b3c98b82e4265fe091844,
driver030e2542/guard911c91cb/wrapperaf1d488e. The root selector starts with
inherited API Bundler selectors removed so its declared root shell selects
its own environment. This is private driver environment precision only;
existing commands/coverage/database guard are unchanged. Second batch failed
1/301.954s, waited/source parity1/cleanup proved1. API73/0/0 pending/0 outside
passed, stage283.436s/RSpec270.776s. Migration6/1 failed stage5.246s/RSpec3.666s;
lint/selector unrun. Original DB and owned PGID are absent; no signals/prune.

The migration fixture correction removed only the metadata-symbol expectation:
pinned AR8.1.4 MySQL maps default RESTRICT to nil. The migration still declares
RESTRICT; actual DELETE/missing-pointer InvalidForeignKey assertions, FK
column/table and audit/down checks remain. Corrected migration spec SHA256
c463ea99ad0efb0d56ce158febdc11872eb2573c71a9460d0fb68947ae179bdc.
Packet /tmp/storage-maintenance-reservation-migration-fix-20261006.xqm162k4/
binds manifest a3aa3e47 and complete patch f0ae8904; the other 18 paths stayed
exact. Both earlier failures remain separately recorded.

Third disposable batch failed exit1 in 28.013s, waited/source parity1,
children waited1/cleanup proved1. Corrected migration: six examples, zero
failures/pending/outside errors, RSpec3.704s/stage5.062s. RuboCop failed in
9.081s: 12 files inspected, 65 offenses, 28 autocorrectable. Selector is unrun.
Evidence: /tmp/rescheck.y8wjozbc/, frozen c8c8782e, driver7b739790,
unchanged guard911c91cb/wrapperaf1d488e. This is a style gate failure, with no
new reservation or migration behavior failure established. Parent confirmed
the original DB PID absent and owned PGID process count zero; no signals/prune.

Lead read the complete lint report. Implementer0 has the exact nine affected
owned files for style cleanup, turn01a111a1-9d2b-7a42-a677-670ddcab854e;
the other ten paths and index stay held. No cop configuration change, test
removal, weaker negative dispatch proof or concurrency/cleanup relaxation is
authorized. All 73 API/model, six migration and 20 selector cases must remain.
After the member freeze, lead will inspect the complete correction and rerun
all four owning stages because runtime/spec source will change. The prior
API73 and migration6 passes remain evidence for their tested bytes. No current
full-batch pass or selector result is inferred.

Style cleanup is complete and all 19 paths/index are held. Parent inspected
all nine source deltas with indentation separated from substantive edits,
verified prior snapshots/current hashes/other-ten parity, and found no concrete
design deviation. Runtime changes are whitespace and equivalent has_key?
spelling. Class contexts keep inherited hooks in their original sibling scope;
scoped spies refuse signing/dispatch immediately; fault injection uses the
actual current locked singleton; example-owned worker state preserves binding,
reap and error rules. Case descriptions and metadata retain API73/migration6/
selector20. Member Ruby9 syntax/diff0 remains static evidence.

Style packet /tmp/storage-maintenance-reservation-style-20261006._niw1ya7/
binds manifest2ecc9790, correctionaf4dcfc5 and complete patchde5381f6.
Fresh626 Luna/low utility reservation_style_checks_20261006 now owns the same
complete four-stage batch at /tmp/rescheck.pfhr38ik/. Frozen SHA256
f499ee8e17102190476ea9f911a30ddf4ef45f0c35f0b980706d794668214a73;
driver030e2542/guard911c91cb/wrapperaf1d488e unchanged. All 3,244 source files
were guarded. The full batch completed exit1/302.155s, waited/parity1 and
children waited/cleanup proved1. API passed 73 examples with zero failures,
pending or outside errors (stage276.787s/RSpec264.204s). Migration passed all
six with zero failures/pending/outside errors (stage5.349s/RSpec3.853s).
RuboCop failed with 11 autocorrectable DescribedClass offenses in three model
specs (12 inspected/stage7.1s); selector remains unrun. Parent read the complete
lint report and confirmed original DB absent/owned PGID count zero, no signals
or prune. These results are separate from the earlier 65-offense failure.

Only the 11 reported receiver spellings in the actor/admission/status specs
are released, turn01a111b2-4586-7311-aaa5-38ac67668dc7; other16/index held.
Each file has one real class describe, and installed RSpec3.13.6 inherits that
class through string contexts. Replace only those constants with described_class;
no runtime, assertion, class scope or worker changes. After exact reverse-byte
and receiver-binding inspection, run remaining lint/selector. The 73+6 pass
carries for equivalent test receiver spelling and unchanged runtime; no single
all-four-stage passing run or fresh current-byte API rerun is claimed.

Fresh SSH fetch confirms master/base c4d unchanged, so no further rebase is
currently needed. Normal Overcommit pre-commit is installed and core.hooksPath
unset. No hooks were bypassed.

- [x] Placement implementation, owning checks, whole-branch review and feature publication.
- [x] Admin rebase/source/history/schema parity and topic/selector verification.
- [x] Reservation authoring, complete inspection and static freeze.
- [x] Guarded core schema generation, accepted diff and exact installation.
- [x] Full-plugin locale generation, lead translation/health and final19 freeze.
- [x] Real API/migration/authorization/concurrency checks and clean component lint.
- [x] Existing root selector in its own unbundled environment:20/89, zero failures/errors/skips.
- [x] Normal owning commit with all hooks passed and tested-byte tree parity.
- [ ] Independent all-four-lane COMPLETE c4d..edc branch/history/migration review.
- [ ] Physical exclusion, G2 approval/action proof and separately authorized recovery.
- [ ] Real payload/history/automatic/repeat/retirement after proved recovery/delivery.

Actual alias, stopped scheduler and admitted objects/evidence remain held.
No live reservation, package delivery, activation, default integration or repair
is claimed. Session stays active/open, with no CI wait.

### Placement reviewed and published; Admin preparation, 2026-10-06

Independent reviewer0 completed all four HIGH-risk lanes for COMPLETE
0ff827df..e33b8d0, tree e71ffb04e6f657be6d2c55676dd9ad7317a8ff3b,
with no findings. Saved Sol/xhigh/read_only settings were retained without
override or fallback. The reviewer confirmed both coherent commits, all ten
paths, complete diff SHA21f496e1, supported v1/legacy compatibility, no obsolete
history and no provider SQL migrations. Intentional NAS naming, profile2 and
inspection2 remain distinct from unchanged maintenance2/applied1/schema1-policy3.
See [final report](storage-profile-backup-placement-review-result.md).

Fresh SSH master/base stayed0ff. Normal feature push and exact readback are
complete at e33b8d0075fb37c49c91a4fcc68251a1e1815545; default remains0ff.
The public comparison is captured at exact base0ff/head e33. Current CI run
37464626649 is in progress; no superseded queued/running run needed cancellation
and no CI wait is imposed. Local checks retain their scoped lineage above/below;
source review and publication do not deliver this feature into the retained guest.

The architect's API-only reservation brief and typed Pool-selector precision
are complete. Fresh Admin fetch is c4d9b50f4e74417ed37b5fe410cca3ec1addc24e;
held feature290f has seven upstream commits to carry forward. Parent prepares
the normal rebase; implementer0 owns actual source conflicts and exact-once
topic/testing-table carry. Keep both consumed migration blobs and the core
schema exact. Reservation source release follows final rebase inspection.

Backup ref2026-09-23-storage-redesign-admin-290f-before-c4d-20261006 preserves
exact290f, which also remains the remote feature. Initial pre-rebase refusal
performed no replay: a stale Overcommit configuration signature. Current
config/custom hooks were read and shown unchanged in both source ranges, then
ordinary --sign succeeded with hooks enabled. Rebase is now at step2/23,
HEAD dda3b1126e717e42cf3d76d36b066c527c9c224b, REBASE_HEAD9d215ffcd;
only EN/CS locale conflicts are released to implementer0, turn
01a1113c-efd2-7d00-aa6d-dab71a58ab74. Parent owns index/continue. A wrong-CWD
read-only REBASE_HEAD query failed against shared root; the corrected registered
Admin read supplied this binding, with no mutation from the failed query.
Architect0 is refining the generated core-schema workflow and locale-health
path requirements, design-only turn01a1113d-0cef-7540-ba05-93b9eb180680.

- [x] Placement implementation, owning checks and complete independent review.
- [x] Feature publication/readback/comparison; defaults and feature refs preserved.
- [x] API reservation design and interface precision.
- [ ] Rebase Admin, preserving upstream CI/locales/instructions and consumed schema.
- [ ] Implement and review the API reservation foundation.
- [ ] Complete physical exclusion, action proof and separately approved recovery.
- [ ] Prove real payload/history/repeat/retirement after authorized delivery/recovery.

Retained alias, stopped scheduler and admitted objects/evidence remain held.
No pin, package, activation, default merge, live reservation or recovery action
is authorized by this checkpoint. Session stays active/open.

### Placement committed; complete branch review pending, 2026-10-06

Fresh resumed selected-Admin290f no-VM smoke PASS0/1203.510s, followed by
provider no-build PASS0/11.881s; total0/1216.065s/parity1. The lead read both
waited statuses, actual v1/v2 active/retired producer/marker and runner
milestones, and all ten unchanged source hashes. Earlier API89/0, pure7/69,
host8/132 and full-flake0 carry only on exact nine-file equality; this is not
a new four-stage rerun. Original failed and user-cancelled runs remain below.

Fresh SSH default/merge-base still0ff; normal new placement commit
e33b8d0075fb37c49c91a4fcc68251a1e1815545, tree
e71ffb04e6f657be6d2c55676dd9ad7317a8ff3b, exact ten-path806+/67-, clean and
tested-byte parity. No hook framework/custom executable hook is declared or
active; no bypass. Complete0ff..e33 contains bd5 namespace prevention plus
e33 placement: two commits/ten final paths/1150+/72-, full-index binary SHA
21f496e15576d841272fa5af6928e696a09fa6c5706ce9148aa5f03d30cd0c94.
No provider SQL migrations; intentional NAS naming/profile2/inspection2 and
unchanged maintenance2/applied1/schema1-policy3 remain explicit. Actual
consumed Admin foundation/captureindex/schema blobs match their inventory.

Mandatory independent all-four-HIGH COMPLETE branch review is assigned to
retained ready reviewer0, review/read_only/gpt-6.1-sol/xhigh, no override or
fallback, turn01a11128-415f-7661-9da6-19ca5e70899f. Findings and whole-history/
migration conclusion are PENDING. See
[packet](storage-profile-backup-placement-review.md),
[inventory](storage-profile-backup-placement-inventory.json) and
[complete diff](storage-profile-backup-placement-complete.diff).

- [x] Complete owning source and scoped verification; commit exact tested bytes.
- [ ] Resolve complete-branch independent review and publish the feature.
- [ ] Finalize design-only common API maintenance-owner/CAS brief.
- [ ] Implement/review the future recovery foundation and action proof.
- [ ] Obtain separately approved retained recovery and payload acceptance.

No new feature publication, pin/package delivery, activation/default merge or
cluster operation is claimed. Actual alias/scheduler/objects/evidence remain
held. Architect0's next-source design remains separate and unreleased; session
stays active/open, with no CI wait.

### Placement verification resumed, 2026-10-06

The user explicitly said “continue”, lifting the work pause. Exact session/env
and roster23 binding match; all ten frozen sources, bd5/Admin290f heads and
empty provider index match yesterday. Fresh SSH master fetch/merge-base remain
0ff827df, so no provider rebase is needed. Cancelled smoke evidence reached
actual omitted-v1 and active/retired-v2 producer projections before TERM; its
Open3 stream-close diagnostics followed cancellation and are not a test-failure
conclusion. Complete smoke/no-build remains unproved.

Fresh Luna/low utility `/root/profile_placement_resume_smoke_20261006` owns
the exact unchanged driver at
`/tmp/storage-profile-placement-resume-checks-20261006.8iin6afb/checks.py`,
SHA20ad14ce75aaa44ca374c308c4ac121a4cfe3415b035951bd9e3d83deaf9c360,
frozen SHAb297247dc7f045bfa1b21c7f1c8ae869760d4e000f61a799faef41279c8ab797.
Selected-Admin smoke then provider no-build are active/pending; no duplicate
API/fullflake/VM/CI run. Earlier source-specific passes and failed/cancelled
evidence remain distinct. All source/index held until result; commit, complete
branch review and feature publication follow a pass. Alias/scheduler/G1bG2/
physical/delivery/default/operation holds remain; session stays active/open.

While verification runs, retained architect0 owns a design-only refinement of
the common G1b/G2 recovery foundation into an exact next source brief, turn
01a1111a-1a09-7961-b4b7-5bdc79da5f07. This is not a placement gate or application
release. The API maintenance interlock must remain distinct from actual held
Node/child/GC exclusion and authenticated action approval; no live evidence or
repair operation is authorized. Current public consumer master5561663 selects
provider0ff with generic4c3ea2/Codex3d07; earlier67505/i95b proof is historical.
Architect0's initial direction is an independently testable API-only retained
reservation/CAS boundary, with direct-admin reserve/show/abandon and ordinary
unfreeze refusal. The lead requested strict predecessor-state/version refusal,
no expiry release and explicit old-mode-writer exclusion. The exact source brief
is still being authored; neither application implementation nor physical hold,
capture authority or G2 execution is released.

### User-requested pause, 2026-10-05

The user explicitly requested “pause”. Development is paused; the session
lifecycle remains active/open. The fresh corrected-smoke watcher cancelled
only its owned stage1 PGID2986195 with TERM: stage exit-15/waited1/770.019s,
driver exit1/770.755s/source-parity1. The watcher reports zero members in that
PGID; provider no-build stage2 never started. This is an incomplete user-
cancelled run, not a failing test conclusion. No retry or further work starts
until the user resumes. All ten source bytes/index remain frozen on bd5; no
placement commit, final review, publication, package/cluster or default action
was performed. Evidence remains at
`/tmp/storage-profile-placement-envelope-checks-20261005.1ckw2r_c/`.

On resume: inspect the cancelled smoke evidence, choose a fresh watcher for
the remaining owning check, then commit and review the complete branch if it
passes. Earlier API89/0, pure7/69, host8/132 and full-flake source-specific
evidence remains scoped to unchanged bytes. Retained alias recovery, stopped
scheduler, G1b/G2 and physical/operation approvals remain unresolved and held.

Namespace prevention atbd5 is checked, independently reviewed and published
feature-only. The lead accepted architect0's complete separate placement brief
and released its ten provider paths to implementer0. The optional VPS backup
root keeps omitted v1 behavior, selects a distinct destination for empty
hypervisor sources under v2, and preserves valid sole existing copies. Source
authoring/static checks are complete and all ten paths are frozen; owning
verification is assigned to a fresh watcher and committed review remains
pending. Provider/default0ff, consuming default67505 and selectedi95b/npjj
are unchanged.

- [x] Complete and publish reviewed namespace prevention atbd5.
- [x] Accept the separate placement design and release bounded source authoring.
- [ ] Check and independently review the complete placement deliverable.
- [ ] Implement guarded recovery and obtain exact retained-action proof/approval.
- [ ] Resume the payload/history/repeat/retirement acceptance after safe recovery.

The retained NAS/VPS alias and stopped scheduler remain held. Placement does
not withdraw DIP12 or establish historical NAS integrity or destination
availability; common G1b/G2 exclusion, approval/action persistence and exact
dependency/lifetime/physical proof remain missing. No new package activation,
default integration or live trial is authorized by this source release.

Parent verification selection is frozen at
`/tmp/storage-profile-placement-checks-20261005.crxlbuxo`, driver SHA
8adb59aa9015c9c3b6d79b2bed1f4ff944f0b590b6251f413ead073e77526683;
frozen manifest SHAee69d69d9ea4b88a9580f1926aa89a5d95a0704f004cb77d9db9b09ae00f61ba.
The parent read the full ten-path diff and verified HEADbd5, every source hash,
empty index, exact modified inventory and unchanged flakes/wrapper/Admin290f.
The selected batch is the complete disposable-API harness, focused
profile/host Ruby checks, full existing flake checks and selected-Admin290f Nix
smoke. Fresh operation-only Luna/low watcher
`/root/profile_placement_quick_checks_20261005` owns execution. Its one bounded
numeric-metadata progress report records stage1 exit0/122.857s, stage2
exit0/137.658s and stage3 exit0/1122.582s. Actual counts, aggregate status and
source parity are not yet extracted. Stage4 selected-Admin290f no-VM smoke is
active at PID/PGID2947569; result pending. Parent has not polled live logs.
No new runtime gate or scenario was added.

The first batch completed with driver exit1/1879.380s/parity1 (watcher/tool
1879.511s). API89/0 and pure7/69 + selected host8/132 passed; full flake passed.
The smoke failed exit1/495.620s at the new projection helper: KeyError env.
Actual selected Nix2.34.8 emits envelope version Integer4 with a derivations
map; the helper iterated the envelope itself. Parent registered metadata read
and package input prove that shape without realizing VM closures. Owned stage4
PGID2947569 has zero remaining processes; no signals. Only the smoke test file
is released to implementer0 for the explicit selected-envelope correction;
other nine files/index stay held. Corrected freeze and fresh selected-Admin
smoke -> no-build are pending. Unchanged nine-source API/pure/host/full-flake
evidence carries only by exact byte parity. No current v1/v2 producer smoke
pass, aggregate success, runtime repair or new contract is claimed.

The helper-only correction is frozen at f0263f14748e8cf6e83e8c34628e79421b73d99abd57baadaa068deb2030a1b9. Parent inspected exact typed Nix version4 envelope/map handling; the remaining projection/scenario is unchanged. Other nine hashes/head/index/flakes/Admin match. Corrected author packet
`/tmp/storage-profile-placement-metadata-v4-20261006.uk276ou2` has
manifest a213ffae and ten-path full-index patch bb39b67e. A fresh Luna/low
utility `/root/profile_placement_envelope_smoke_20261005` owns driver
`/tmp/storage-profile-placement-envelope-checks-20261005.1ckw2r_c/checks.py`,
SHA20ad14ce75aaa44ca374c308c4ac121a4cfe3415b035951bd9e3d83deaf9c360;
frozen SHAb297247dc7f045bfa1b21c7f1c8ae869760d4e000f61a799faef41279c8ab797.
Only actual selected-Admin smoke then provider no-build are running/pending.
All ten source bytes/index remain held. Prior fullflake includes command45/545
zero failures/errors/skips; upstream suite summaries/skips are not aggregated.
No new interface, format or runtime acceptance follows from this test-only fix.
The reusable metadata lesson is in
[notes/vpsfree-dev-workspace/2026-10-05-nix-derivation-metadata-envelope.md](../../notes/vpsfree-dev-workspace/2026-10-05-nix-derivation-metadata-envelope.md).

Fresh explicit SSH master fetch still resolves to0ff827df, also the current
merge base, so no provider rebase is needed. Declared hook-framework inventory,
core.hooksPath and executable custom hooks are empty; no hook is bypassed.
Actual Admin290f foundation/capture-index/schema blobs match the established
consumed lineage; no provider SQL migration is introduced. Full branch review
preparation covers bd5 prevention plus the prospective placement owner, with
all results and the final placement head still pending.

Author packet `/tmp/storage-profile-backup-placement-freeze-20261005.uu8hyhi6`
has manifestdb1aa0c5 and complete patch07b62c4c. The actual delta is ten paths,
798 additions/67 deletions; full-index binary patch SHAd33172c6cd6420b13539af7a80aac45df95bec8729c026e8545f05d503b11576.
Authored inventory is89 API examples,7 pure methods,45 total command methods
(8 selected), with active/retired v2/omitted v1 and7 invalid-root Nix projections;
these counts are not results. Member-reported current-byte Ruby/Bash syntax,
Nix formatting and scoped whitespace checks passed. All source/index remain
held; no new commit, review, publication or runtime acceptance is inferred.

Implementer0 released only the technical README for the lead's owning prose
pass while finishing the other nine paths. That pass is complete at SHA
1712eb66f0a6dc09a83697451c60dee2525bb51f48517dd12524b23fc65459ee;
scoped whitespace check passed. Configuration example and prior prevention
prose are preserved; placement/reuse/refusal, inspection, writer transition,
rollback and delivery limits are unchanged. Final source freeze includes these
bytes; owning checks and new review remain pending. A nonlogin shell could not resolve the bare
`dev-session` name and performed no owned action; the absolute public command
then verified exact binding/env/roster before owned reads and edits. The
unexecuted driver now uses that verified absolute command.

### Payload correction activation and integration complete, 2026-10-05

The user reported activation and explicitly directed: “activated. verify it and
once again, merge the workspace fix into the default branch.” In the current
correction context this covers provider vpsfreecz/dev-workspace master (reviewed
0ff827df fixture/test correction) and consuming aither64/vpsfree-cz-workspace
master (67505d97 mechanical pin), preserving all other storage feature branches.
Approval is recorded before integration. No guest update, fixture retry or
other default integration is inferred from this turn.

Read-only activation proof PASS: selectedi95b/toolsnpjj, all nine actual-source/
contract/default/Codex comparisons and loader/schema1policy3/providers2 pass,
active Codex resolves to this package, and all four router/portal/Codex/tmux
units are active/running with stable ExecStart links resolving to selectedi95b.
An initial literal store-prefix assertion did not resolve the stable profile
link and failed; resolving the actual links proves the intended binding. This
was a proof assumption, not an activation or service failure. Public cluster
status reports running/readytrue/bridge and v2released/pendingfalse. The guest
acceptance script remains the oldc7a1 until ordinary services delivery.

Fresh SSH fetch confirms provider master77dd/feature0ff and root master35c/
feature67505 unchanged. Saved review48/0/package261.457s/equivalent-output proof
carry on exact source/input parity. Both FF-only integrations and normal SSH
readbacks are complete: provider master=feature0ff827df; root master=feature
67505d97. Shared index stayed empty and all seven held storage/other feature
heads remained exact. Public comparisons retain exact pre-integration bases.
Only the clean temporary provider target worktree was removed; feature refs,
registered worktrees and the session remain. No CI was awaited. Private proof references:
`/tmp/storage-profile-memory-activation-20261005.nqkppk5z`. The session stays
active/open; faileduser5/chain48 and the scheduler state remain preserved.

Current phase after completed integration: the one ordinary installed public
services update passed exit0/399.864s/parity1 to exact l2n9 services toplevel.
The fresh read-only post-delivery packet passed exit0/25.419s: actual immutable
acceptance77f2 and provisionef775 SEED_FILEs, services system, original ordinary
file/four quota properties and all three actual Node source/socket/running/
zero-delay proofs match. Protected DB changes0 across27groups/1253rows. Relative
to the original baseline there are100 added rows; relative to the exact accepted
post-user5 capture there are no protected additions, changes or missing rows,
only four Pool-space and five snapshot-count observations differ. Faileduser5/
chain48 remain intact. The supported services switch restarted scheduling.

Private evidence remains at
`/tmp/storage-profile-memory-delivery-20261005.ukggg26d`. Fresh bounded preconditions PASS: loaded enrollmenttrue/all four Pools, active
scheduler/test-admin, enabled compatible template1, read-write mode0/epoch4,
and prior chain48 done with no unfinished transaction, confirmation or lock;
user5 has no VPS. The one corrected fixture then failed exit1/202.570s at first full-transfer
stage2, after VPS/member preparation. Chain71 is failed/state4, with five
transactions, pending confirmations0 and locks0. Tx186/handle5213/node201
CreateTree failed because its dataset already exists; rollback failed because
the filesystem has children. The remaining four members were dependency-skipped;
no send/receive completed. This is not a quoting or history-assertion failure.

A bounded read-only catalog snapshot confirms the cause boundary: NAS Dataset3/
user3/backupDIP5 and new VPS Dataset6/user6/VPS3/backupDIP12 have the same full_name
in exactly the same backupPool5/node201. The NAS copy already has confirmed
headTree2/index0, Branch2 and three snapshot copies. This establishes a canonical
path alias between distinct logical owners. Exact-target physical metadata was
read separately without mount/write/adoption/deletion. Historical GUID/ownership
and safe disposition of the new aliased copy are not inferred from metadata.

Post-failure original preservation PASS0/26.639s: original ordinary file/four
quota properties and protected DB rows remain equal; all three actual Node
proofs pass. There are180 added rows relative to the original baseline, versus
100 before the new fixture. An offline join of the two existing captures binds
all56 newly added protected rows to fixture user6/VPS3 or its NAS, namespace,
package and resource records. The other24 additions are observations:6 accounting,
6 DIP-space,6 snapshot-count,3 Plan links and3 tasks. Task/action ownership is
not established by this collector, nor is physical alias disposition. The
private comparison hash is996b91faefcd794c92120ac843310036663edeb05690afe7b8ebce3ddd42e65a.
No new guest/DB read was run for this comparison. Host childPID/PGID2156563 is reaped; owned-group/prefix/FD-holder
observations are zero, no signals. Scheduler remains stopped, all old/new
admitted objects and evidence are retained. The first wrong-CWD watcher launched
zero operations; the bound-CWD watcher launched once.

Current phase: reviewed prevention feature published; source-only recovery
proposal recorded, retained trial held. The lead accepted the architect's three-path brief; the
original335+/9- freeze and its two fixture corrections are preserved below.
The final three-path commit has348+/9- and passed the complete64-example
API290f suite plus provider no-build with exact tested-byte parity. New NAS roots
use `nas-<user-id>`, valid legacy roots retain their
identity, and an admission-serialized current read refuses distinct catalog
owners of the same backup path before staging can commit. Existing pending and
confirmed copies, including duplicate Pool aliases, are covered. This is
catalog/profile-writer prevention, not a physical ownership or old-writer fence.

The retained alias remains a separate recovery blocker. No inspected public
interface safely separates the two DIPs with their history intact. Prevention
cannot make this trial resumable; scheduler stays stopped and all admitted
objects/evidence remain. No retry, cleanup, unlock, mode change, recovery or
retirement is performed. Private evidence:
`/tmp/storage-profile-corrected-payload-20261005.b23vqo76`. Workspace/provider
integrations remain complete, no further workspace defect is established;
other storage branches and the active session are preserved.

- [x] Workspace fixes activated, verified and integrated at0ff/67505.
- [x] Guest delivery and original-preservation proofs accepted.
- [x] First-transfer failure diagnosed as a confirmed NAS/VPS path alias.
- [x] Three-path prevention authored and frozen; static syntax/diff passed.
- [x] Full-file disposable-DB suite/provider no-build checks accepted.
- [x] New prevention committed atbd5bf53 with tested-byte parity.
- [x] New prevention commit independently reviewed on the feature branch.
- [ ] Existing-alias ownership/disposition and supported recovery decided.
- [ ] Owning payload/history/automatic/repeat and retirement acceptance completed.

The lead inspected the full frozen patch and actual unchanged fixture consumer
without finding a concrete deviation. The fresh Luna/low batch failed exit1/
83.177s/parity1: the full Admin290f harness reached64 examples with8 failures in
82.569s; provider no-build did not run. All eight failures are new competing-owner
fixture inserts missing required Dataset boolean fields, before their collision
assertions. Only the spec was released for that setup correction; helper/README,
index and HEAD0ff stay held. No corrected pass or runtime defect is inferred.
Fresh provider SSH fetch returned master0ff unchanged.
Evidence: `/tmp/storage-profile-namespace-checks-20261005.g15pfu3z`.

The boolean-fixture correction preserved the helper/README and all64 examples.
The second fresh batch failed exit1/88.575s/parity1: stage1 took87.947s with
64 examples/3 failures; no-build remained unrun. All three failures are two new
expectation lines comparing string states to the held Confirmable symbol getter,
after the collision/refusal and rollback checks. Only these two spec expectations
were released for exact symbol comparison; runtime/docs/index remain held. The
owned stagePGID2270288 has zero processes; no signals were sent. Evidence:
`/tmp/storage-profile-namespace-checks-final-20261005.ff3_8b3k`.

The exact two-expression symbol correction is frozen at spec42dd4823; reversing
only those expressions recreates prior219436f9 byte-for-byte. Helperbe9/READMEece8
remain unchanged, all64 examples and reader/cleanup controls are preserved, and
index/HEAD0ff remain held. The fresh symbol-corrected batch is active under
`/root/profile_namespace_symbol_quick_checks_20261005`; frozen manifestb65fc57f
and driverba430f1b are bound in
`/tmp/storage-profile-namespace-checks-symbols-20261005.2letm09k`. No outcome is
inferred from the freeze or launch.

Final batch PASS0/104.756s/parity1:64 examples/0 failures in88.605s and
provider no-build0/15.518s. Parent checked actual results, exact three hashes,
complete patch, empty index and no unrelated source. Normal new owning commit
`bd5bf53c9ba24ab6f37272ed928baa6a0b49e6ca` is complete atop consumed0ff;
treece5f7ba58990cfd1280fd96aa33a05a6dde90391,348+/9-, clean source/index.
Complete one-commit/three-path inventory and diff have SHA
d50e7c56b06a3d417d70d675c85d38d13c5f052b5972995023a09f3c59f39013.
No SQL migration/input/wire/schema/CLI/module or inherited state-version change;
new NAS naming/legacy compatibility and rollback constraints are intentional.

Mandatory final review is COMPLETE from verified retainedreviewer0, review/
read_only,gpt-6.1-sol/xhigh (no override/fallback), HIGH risk/all four lanes.
No Blocking, Important or Advisory findings. Reviewer independently verified
exact0ff..bd5/tree/diff/threehashes and one coherent complete commit with no
obsolete history or migrations. Consumed predecessors/Admin migration lineage
are preserved; prevention/old-writer/physical/recovery limits are retained. See
[final prevention review packet](storage-profile-namespace-prevention-review.md),
[inventory](storage-profile-namespace-prevention-inventory.json) and
[complete diff](storage-profile-namespace-prevention.diff).

Normal SSH feature publication succeeded atbd5bf53 after fresh master0ff
readiness/no-rebase proof; public comparison captures exact0ff..bd5. Default
master stays0ff, consumer/default67505 and selectedi95b/npjj remain unchanged;
no new selection/delivery/default merge. CI metadata reports current-head Check
run37321075184 in_progress; no CI was awaited and no superseded branch run was
queued/in_progress, so none was cancelled. Both final local stage process groups
are empty; no signals were sent.

The lead read architect0's separate
[G2 empty-alias withdrawal proposal](design.md#proposed-recovery-g2-catalog-only-withdrawal-of-an-empty-backup-alias-2026-10-05).
The candidate withdraws only an exactly proved empty backup claim and its
source-specific scheduling metadata inside the existing reconciler, with zero
Node/ZFS effects. It is not executable: common G1b held exclusion/maintenance
ownership and G2 authenticated approval/action persistence/execution do not
exist. Current capture also lacks complete Plan/task/property/resource closure
and whole DIP lifetime/deleted-confirmation proof. Historical NAS GUIDs cannot
be reconstructed; retrospective NAS integrity stays unresolved. No operation
or application release follows from this source assessment.

Even a future approved withdrawal would not restore VPS3 backup eligibility in
Pool5: its logical name still conflicts with the retained legacy NAS. A separate
namespace/destination policy is necessary; another fixture ID or physical
rename/deletion is not a supported workaround.

Current source phase: backup-placement authoring is released to ready
implementer0 at providerbd5, after the lead read architect0's complete
[placement brief](design.md#proposed-backup-placement-preserve-existing-copies-choose-a-distinct-vps-destination-2026-10-05).
The optional `storageProfile.vpsBackupFilesystem` preserves omitted v1 behavior
and introduces explicit v2 selection, reusing valid sole legacy copies. The
ten-path release covers the shared placement owner, generated configuration,
provision/guest/host consumers, existing tests and owning README. Only static
syntax/format/diff checks are assigned to the author; runtime outcomes are
pending. Existing-alias recovery, destination availability and operation
approval are not supplied by this source policy. Common G1b/G2 implementation
and exact held action evidence remain separate prerequisites. Existing-alias recovery/disposition and remaining trial
acceptance stay held. Prevention is locally checked, independently reviewed and published
on its feature branch, awaiting any later integration/delivery direction. The
already-fulfilled0ff/67505 approval does not cover this new substantive correction.
New default integration and recovery operations are not authorized by the
already-fulfilled0ff/67505 approval.

### Retained-cluster recovery resumed, 2026-10-05

The user directed continuation after the workspace-default integrations.
Fresh public status confirmed stopped/bridge/readyfalse with the original
version-1 starting_copied hold. The three immutable source configs and their
hashes, genuine prior released/full-boot ledger, actual three Node-update
selections and completed services copy matched. All six retained disks remain
present at their original sizes; fresh metadata scans found no owned runner or
disk FD holder. Historical inode/device is not inferred from current stat.

The installed public maintenance-recover-config completed exit0 in25.543s.
Readback proved version2/starting_copied, exact archived predecessor bytes,
unchanged services/candidate/copy and all three Node descriptors, with only the
two DNS descriptors restored from the prior successful full boot. Current disk
bindings remain equal. At that metadata checkpoint, applied selection remained
pending copied_boot, before guest boot or release. Recovery evidence is private under
`/tmp/storage-retained-resume-20261005`.

The exact public start --copied-config passed exit0 in666.808s under its fresh
Luna/low watcher. All six guests proved recorded systems/rooted closures, actual
seed/API/Supervisor and normal Node refresh completed, applied selection was
published complete, then the version2 hold released. Disk identities/sizes
remain equal. The exact command launched once; PID/PGID1579638 ended and no
unexpected kernel build was reported. The earlier wrong workspace-root CWD
identity check launched zero operations; corrected tracking-CWD identity
matched before execution. Parent readback accepted released/pendingfalse and
complete six-machine applied selection.

Post-recovery read-only proof passed exit0 in29s: both actual immutable guest
SEED_FILE hashes match the corrected scripts, original ordinary-file and four
quota properties remain equal, protected DB changes0 across27groups/1168rows,
and all three actual Node code/socket/running/zero-delay proofs passed. Seven
package/item additions are identical to the prior verified owned seed metadata;
only two observed Pool-space rows changed. Original assignments, ceilings,
namespace/map and retention rows are unchanged. The file proof is forward from
the established first post-copy observation, not a fresh preboot measurement.

Public profile provisioning passed exit0 in78.601s: version1/members2/sources3/
provisionedtrue, stderr0. Post-provision preservation reads passed: original
file/four quotas and all protected rows remain equal. Of52 added rows, seven
are the prior seed metadata and45 are the expected backup/NAS catalog,
quota/retention, memberships/tasks and NAS-use rows. All four loaded Pools are
present; enabled compatible template and read-write mode were freshly checked.

The one existing VPS/NAS payload fixture attempt failed exit1 in27.444s at
preparation stage1, before payload writes. Its normal user chain48/user5 was
admitted. The API rejected VPS staging with ClusterResourceAllocationError:
the fixture requests512 MiB but the actual seeded memory minimum is1024 MiB.
The fixed API minimum remains unchanged. The owned foreground/PGID1671507
ended; no fixture retry, deletion, unlock, cancellation or freeze change occurred.
Scheduling remains stopped as recorded by the fixture.

Current phase is the reviewed fixture correction's immutable package delivery.
The complete owning profile spec file passed48examples/0 in65.106s and provider
no-build evaluation passed0/13.224s; the fresh batch passed0/78.929s/parity1.
Normal new commit0ff827df (parent77dd/tree867d2378) contains exactly two paths,
51+/1-, with the1024-MiB request and selected-seed regression. Independent
reviewer0 inspected the complete committed77dd..0ff range in all four lanes:
no Blocking, Important or Advisory findings; one coherent commit, no obsolete
history or migrations. The consumed77dd predecessor is preserved.

The provider feature was published/read back at0ff827df; default77dd remains.
Fresh root masterc754 is unchanged. Implementer0 authored its one provider-URL
edit; normal Nix generation changed exactly the four provider metadata leaves,
preserving generic3ed/Codex3d07 and all other inputs/follows. Root no-build
passed and normal new commit7d5507f5/tree2e750552 contains exactly two flakes,
5+/5-, with clean index/tree. It is a mechanical pin exempt from additional
independent review. Fresh Luna/low watcher payload_memory_package_20261005 completed the existing
four checks, default build and actual proof PASS0/261.457s/parity1 (254.616s,
6.604s, proof0). All nine source/contract/default/Codex equality flags, loader1,
schema1/policy3 and two providers passed. Input revisions are exact0ff/provider,
3ed/generic and3d07/Codex; actual installed acceptance hash77f2 matches. The
built package is `/nix/store/i95b471mnd2xw88knbs9c7wcyj31lma1-dev-workspace-0.2.0`,
with tools `/nix/store/npjjcfz1m4zaxcy3zg8s6q853rn8q0m5-vpsfree-dev-workspace-tools-0.1.0`.
Evidence packet is `/tmp/storage-profile-memory-package-20261005.g6uxu1uw`.
The watcher ended; no retries/cancellations or CI wait occurred. Public host
status still selects3fzi/wg7/oldc7a1; the proved package is UNSELECTED.

Current phase is EXTERNAL IDLE ACTIVATION HANDOFF. Normal tracking commit35c5ab1e
is published, preserving the two other coordination commits4df/af907 and all
foreign work. Tested root7d was retained in its backup ref, then replayed onto
35c as clean67505d97/tree24b13218. Full patch/message/flake bytes are identical
and range-diff is '='; final eval0/7.771s resolves to SAME testedi95b output and
final no-build passed0/3.746s. Normal SSH feature publication/readback and public
comparison base35c/head67505 are complete; provider77dd..0ff comparison is also
saved. Master35c contains tracking only; no new pin/default integration.
Obsolete-workflow metadata was handled without a CI wait.

Run the public switch from an idle terminal:
`workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/workspace`.
workspace-host requires session quiescence before selecting a package; the
active lead cannot bypass that public boundary. After selection, lead verifies
actual sources/contracts/services, performs the ordinary services update, and
proves the actual new77f2 guest script and original preservation before one
new owning payload fixture/key. New readonly proof packet
`/tmp/storage-profile-post-delivery-proof-20261005.0gz33zhd` is prepared/unrun;
it changes only provider/new acceptance guards, retaining original baselines,
Node probes and forward-only file proof. Source correction is ready, awaiting
new merge approval; no new provider/workspace default integration is inferred.
Shared index remains empty. A concurrent extra foreign status entry appeared;
only the six owned tracking paths were committed, and no foreign cleanup or
record/index change was performed.

After the failed preparation, original protected-DB changes remain0 across
27groups/1253rows. The admitted user chain48 is done with no unfinished
transaction, pending confirmation or retained lock; user5's fixture VPS count
is0. Failed objects/evidence remain preserved and scheduler remains stopped.
Payload/history/rotation/automatic/repeat and retirement are unproved;
separate API diagnostics remain held. The session stays active and open.

### Current activation and integration approval, 2026-10-05

The user reported activation and explicitly directed: “please verify that we're
finally done with workspace fixes. if so, you can merge the workspace changes
into default branches, keep the rest of the storage work in feature branches.”
This authorizes provider vpsfreecz/dev-workspace master at77dd (cd81 admission
and retained-selection/roots correction) and consuming
aither64/vpsfree-cz-workspace master atc754. Generic policy4ef is already an
ancestor of generic master3ed; no duplicate integration is needed. Admin290f,
OS/config/WebUI/maintenance-tasks and other storage branches are excluded.

Public installed status and actual-byte proof PASS: exact3fzi/wg7, all9equal1,
loader1/schema1policy3/providers2, active Codex path equals selected package.
Router, portal, Codex and tmux are active/running; all four ExecStart paths
resolve to the selected3fzi package. Same-session public status0 reports
stopped/bridge/readyfalse and intact version1 starting_copied/pendingtrue hold.
No switch, restart or cluster mutation was performed by the lead.

Fresh SSH master88a/e1bb and published c754/77dd are unchanged. Prior full
review/direct-step9/native/package evidence retains its original scope;
architect0 confirms no concrete remaining workspace source gate. Normal public
captures and FF-only provider→consumer integration/readback are now authorized;
source/index/foreign work and all feature refs remain protected. Actual retained
recovery/fullboot/preservation/profile payload gates remain unproved. The
historical dcb skill-only branch is superseded by upstream e1bb’s rewritten
final-history/migration guidance; no additional runtime correction remains
there, and its reference is retained.


Earlier workspace-only checkpoint, 2026-10-05: activation and default integration COMPLETE;
retained storage recovery/acceptance remains pending. Public selected status,
actual sources/contracts/Codex and all four service bindings verify exact3fzi/wg7.
Provider master and feature are77dd0d04; consuming workspace master and feature
arec754120b after authorized FF-only integration and normal SSH readback.
Generic policy4ef was already integrated into generic master3ed. No remaining
known workspace source gate was found. The seven held feature heads, foreign
shared work/index and session refs remain preserved. CI was not awaited.
Prior3df/zwdv/jq982 handoffs are historical. The overall session stays active.
Independent review and direct host-root remediation are complete. The native
passed with bounded diagnostics and the source-proved readiness prerequisite;
the earlier counter-or-disk failure remains unattributed. The user said
“ok, continue” after the ordered next steps were described. The earlier86fe activation/integration and the currentc754 recovery-pin
activation/integration are complete. This continuation uses the selected corrected
package for a supported second maintenance copy/boot, actual guest-script proof,
one justified provision retry and the existing VPS/NAS acceptance and retirement/reactivation
sequence. The present approval covers only workspace/provider defaults; storage project
defaults remain excluded.
Separate API diagnostics remain held; CI is not awaited.

### Historical pre-recovery status

Public workspace-host status selects3fzi with toolswg7, and the actual
corrected maintenance helper SHA8f205b0c matches reviewed provider77dd.
All nine actual-source comparisons, loader, schema1/policy3 and two-provider
catalog passed; active Codex resolves to the selected wrapper. Earlier
s7y4/q49 and jq982/psjf selections are historical. Same-session Admin290f is
unchanged. Initial stale/ready status was disproved by the absent runner
and failed SSH. A second public maintenance cycle has now booted the proved
resident generation, captured a fresh masked DB backup/baseline and copied the
corrected closure. Supported stop completed, but copied start failed at DNS
boot readiness. The hold remains `starting_copied`; the runner performed its
own shutdown. The currently installed provider includes the reviewed recovery interface;
its selected source is
`77dd0d0447f48c8d8e667257cef2276738d053a0` (original review at bcc retained;
rooting checks at b748 retained within unchanged runtime/input scope).
Provision and
the prepared read-only delivery batch remain unexecuted.
Original disks, cold recovery copies and prior DB/file/quota evidence are retained.
Architect0 owns the saved recovery brief and fixture decision; implementer0
completed the eight-path host-root remediation, now committed and held. The lead owns coordination, proof
selection and acceptance. The lead inspected and folded the final one-path fixture amendment; the fresh
watcher completed its native pass. Activation and selected-byte verification are now complete. Actual metadata
recovery/copied boot and storage acceptance remain pending; no cluster
mutation was performed during this verification/integration.

### Current phase checklist

- [x] Resolve the host-payload rooting finding and check the final provider
  retained-selection/v2 recovery correction.
- [x] Complete committed provider review and direct rooting remediation disposition.
- [x] Run the existing native scenario with its added retained DNS-root regression.
- [x] Publish the provider and check the generated consumer/default package.
- [x] Rebase onto fresh master, pass the new composition/package proof, and
  finish exact consumer publication/readback and comparison.
- [x] Verify external activation and integrate provider/workspace defaults,
  preserving all storage feature branches.
- [x] Review and publish feature-only namespace prevention atbd5;64/0 and no-build passed.
- [x] Accept the separate compatible backup-placement source/verification brief.
- [ ] Author and check the ten-path placement change, then review the complete committed range.
- [ ] Implement guarded G1b/G2 recovery and prove/approve the exact retained alias action.
- [x] Prepare exact stopped evidence and run supported metadata recovery/copied
  boot before the retained storage trial.
- [x] Capture a fresh masked protected DB baseline and logical backup; retain
  prior ordinary-file/quota evidence without inventing a fresh preboot read.
- [x] Deliver services through the public provider and prove both actual guest
  wrappers' immutable scripts match the selected correction.
- [x] Recheck preservation, then complete public provision and Pool/catch-up proof.
- [x] Correct the payload request against the actual guest minimum, pass48 specs
  and complete independent final review of the new two-file provider commit.
- [x] Build/prove the consuming package with its actual corrected fixture bytes.
- [x] Complete external activation and ordinary services delivery, then prove the
  new actual guest script and original preservation.
- [ ] Complete the existing VPS/NAS payload/history, rotation, automatic cycle and
  repeat seed/provision fixture, with separate original-object comparisons.
- [ ] Complete retirement/repeat/nonreactivation and re-enrollment, retaining data.

## Completed external activation and integration, 2026-10-05

The user completed the public external switch. Lead read-only verification
proved selected package3fzi/toolswg7, exact runtime/provider/default/Codex
sources, canonical contract, loader/catalog and active Codex path. Router,
portal, Codex and tmux are active/running; every ExecStart resolves to3fzi.
Same-session public status reports stopped/bridge/readyfalse, existing version1
starting_copied/pendingtrue hold. No service or cluster operation was launched.

The user's conditional workspace-default approval was recorded above before
integration. After captures atproviderbasee1bb/head77dd androotbase88a/headc754,
provider master FF/push/readback completed at77dd through a fresh target worktree.
The consumer FF in shared master staged nothing; push/readback completed atc754.
Shared status metadata matched before/after, index was empty and foreign work
was preserved. Generic4ef is already in generic master3ed. Seven held feature
head snapshots remain exact, including Admin290f, OS8d05, config5eff and WebUIaa2.
No second switch or additional source/package fix is currently required.

Evidence reference: `/tmp/storage-profile-workspace-activation-20261005`.
The existing private recovery template is still invalid until real hold/disk/
provenance placeholders are validated. Next work is supported retained-cluster
recovery and actual fullboot/preservation/provision/payload/retirement acceptance.
Keep storage feature branches, original disks/evidence, unchanged retention and
session state. No reset/private helper/early release/quiet/repair/APPLY follows.

## Historical fresh-master rebase and handoff, 2026-10-05

The requested freshness check fetched exact SSH master88a75655 and feature3df.
Shared master matches the remote; its foreign work/index remains preserved.
The sole master advance changes only flakes: an explicit nested generic3ed
selection and Codex3d07 metadata. All fifteen inspected root instruction,
configuration and check-source blobs match09da. Provider mastere1bb has no
advance and feature77dd matches its remote. Exact3df is retained in the
before-upload-runtime-rebase backup.

Implementer0 resolved the one flake.nix conflict from full88a bytes with only
providerURLcd81→77dd, as architect0’s saved brief requires. Normal generated
lock and rebase completion produced clean c754120b/treeaedb64dd: two flakes,
5+/5-, exact four provider metadata leaves. Every other lock node/follow equals
88a, including new generic3ed/Codex3d07. Commit message is unchanged; range-diff
shows only the URL hunk adapting to upstream’s attrset. New flake hashes are
4af9f4b3/218f080e and binary diff8a682dba. First un-waited launch returned0
without checks/results or a live driver; it remains incomplete zero-check
evidence. Fresh Luna/low watcher workspace_rebase_package_waited_20261005
completed the waited launch PASS0/254.433s/parity1: four existing root checks
247.982s, default build6.210s, actual proof0. Driver0b565810/verifier0239b631/
selectionca550d2d bind exact c754/77dd/290f. All nine equality flags and profile
loader passed; schema1/policy3/providers2. New output is
`/nix/store/3fzif0563caiknl53a8s64axaxyf0ph8-dev-workspace-0.2.0`, tools
`/nix/store/wg7hnssgk49kqg4wkyj2dminlcji9h2b-vpsfree-dev-workspace-tools-0.1.0`.
Parent inspected exact immutable generic3ed/Codex3d07 input revisions and proof
artifacts. Test skips, a deliberate-test Git identity message and a Nix rename
warning preserve the actual successful statuses; no kernel build was reported.

A second fresh SSH fetch found master88a/e1bb unchanged. Normal exact-lease
root publication and remote readback completed atc754/master88a; public
comparison captured exactbase88a/headc754, preserving initial metadata. GitHub
branch-run metadata returned an empty list: no superseded workflow to cancel
and no CI wait. Shared index stayed empty; foreign work and all refs remain.
An optional final YAML assertion expected captured base/head inside portal.yml
and failed; source shows public capture delegates to portal user-state metadata.
Its successful exact result and owned inventory are the evidence. Corrected
final source/hash/shared-index guards passed; package proof is unaffected.
The new output is unselected. External idle activation of the registered root
worktree is the next operator action, then selected proof before the already
planned actual recovery/trial. No default integration or cluster mutation ran. No CI wait, new
provider/native work, activation, cluster mutation or default integration is
implied. Evidence is retained privately in
`/tmp/storage-profile-workspace-rebase-20261005`.

## Native preservation evidence amendment, 2026-10-05

Implementer0 froze only the native Ruby fixture at SHA256 `5f72cdc3…d27f5`.
Lead inspection and Ruby3.4.9 syntax/diff passed; all nine other guarded source
hashes and the lock remained exact. Normal owning amend produced provider
`77dd0d04`, tree `31986d97`, preserving `b7488807` in an exact backup.
The complete branch still has two coherent commits; admission `cd81` is
unchanged. No runtime, public interface, state format or migration changed.

The fixture now checks initial API, Supervisor and scheduler independently:
`systemctl is-active` with multiple arguments succeeds if any is active.
The existing final API/Supervisor wait uses the same all-of meaning, without a
new scheduler gate. The existing auth timer is stopped before its service;
both synchronous stops and inactive states are checked. Original equality,
data reads, masked boots, copy interruption and release guards remain intact.
Private baselines and bounded pre-assertion comparisons now distinguish
projection/payload/counter/disk failures. No raw SQL/config/credential output
was added. These are source-proved prerequisites, not a diagnosis of the prior
unresolved counter-or-disk failure.

Fresh one-operation Luna/low watcher `retained_dns_baseline_native_20261005`
owns `/tmp/ndns.27h2r2lc` at exact `77dd0d04`/Admin290f. Driver
`bfedae90…12509`, ten-source manifest `0959b517…4072e`, review-clearance
`0f7d2f74…d3bf5` bind this run. Only the two inspected module-trim/initrd-pack
noncompiling derivations remain monitor exceptions. The batch completed PASS0/1018.533s/parity1, one example, stage6,
scenario_completed1 and hold_released0. All six saved preservation comparisons
were equal. Parent process metadata found zero prefix/PGID825613/FD holders.
This proves the owning services+one-DNS scenario, not actual full-cluster
release, host GC survival or the prior failure cause. Provider SSH publication
and exact readback completed at77dd; default e1bb is unchanged. Consumer URL
authoring is assigned; lock/package/activation/public recovery remain pending.
Provider CI37249592515 is in progress at77dd; metadata listed no superseded
queued/in-progress run, so none was canceled. CI is not awaited.

## Consumer and package preparation, 2026-10-05

Implementer0 authored only the provider URL on clean root `e5ba1912`.
Normal lead generation changed exactly the four provider metadata leaves to
`77dd0d04`; generic6a, Codex32775, defaults and every other node/follow stayed
exact. Root no-build and diff checks passed. The normal one-commit pin is
`de915cd11b97ea8438eb1d8ddbeac139a379db68`, tree
`46efba7693c56b18020f5c38fdd204be20b59697`: two flakes,5+/5-, binary diff
`48eed400…337f2`. [Consumer inventory](storage-profile-retained-selection-consumer-inventory.json)
and [diff](storage-profile-retained-selection-consumer.diff) retain its complete
range. This mechanical URL/generated-lock update is exempt from a new independent
review; complete provider review and direct-remediation proof remain scoped
under their original provenance.

Fresh Luna/low watcher `retained_selection_package_20261005` owns the existing
four root checks, default build and actual provider/helper/runtime/contract/
Codex/default byte proof in `/tmp/storage-profile-retained-selection-package-20261005.u4_knzyn`.
Exact root/provider/Admin bindings are de915/77dd/290f. Driver7348596a,
verifier0239b631 and selection35822c94 are frozen. The batch passed0/260.657s/parity1: existing four checks252.368s,
default build8.038s, actual proof0. All nine equality flags and profile loader
passed with schema1/policy3/providers2. Package is
`/nix/store/zwdv3dc17zbbfkdm24qrm4rz1l0xg5nz-dev-workspace-0.2.0`, tools
`/nix/store/n2ki0wm9lr7qjs49j1v155gp42g2j3a2-vpsfree-dev-workspace-tools-0.1.0`.
The successful check contains Git identity-warning stderr; its exit status is0.
No package selection is inferred. The consolidated owned tracking checkpoint09da was normally published.
A one-pin replay from de915 onto09da produced3dfda5c6/tree61859531: range-diff
`=`, exact patch/message/flake hashes. Final evaluation0/7.492s selected the exact
tested zwdv output; final no-build0/4.083s passed. SSH feature publication/readback
is3dfda5c6, remote master09da unchanged. Public comparison captured exact
base09da/head3dfda5c6, preserving initial_base metadata. Shared index is empty;
foreign working/untracked records and feature refs were preserved. Root CI
metadata returned no runs; CI was not awaited. No default feature integration
was performed. The new root pin is ready, awaiting merge approval after activation. Public `workspace-host status` still selects s7y4/q49;
its actual maintenance SHA20761bf1 is the old helper. Public recovery and the
retained trial remain held until the new package is built and externally
activated while managed sessions are idle. No new default integration authority
is inferred from the earlier completed86fe activation/integration.

## Provider correction checkpoints, 2026-10-05

The following checkpoints retain the original failures, intermediate holds and
later disposition in execution order. Current phase is summarized above.

The final authoring manifest is `ca7ff1dd…9056f`; the normal commit preserved
all eight hashes. Before host-root remediation, provider `bcc0532` had a
clean worktree/index and unchanged inputs. Bash/Ruby/Nix syntax, Nix formatting and diff checks passed. A fresh
Luna/low watcher completed all four quick stages against Admin `290f1ef0`:
exit0/1259.483s/parity1, no remaining operation or reported kernel build.
Focused stage 1 passed in
465.321s: maintenance 28 runs/222 assertions, commands 37/426, runner 13/35,
all zero failures/errors/skips. Existing flake checks passed in687.491s;
candidate/resident evaluations passed in54.039s/52.037s. Existing skips and
repeated upstream summaries in the flake log are not a deduplicated test count.
Reviewer0 completed all four HIGH-risk lanes with saved Sol/xhigh/read_only
settings against the complete `e1bb5cf..bcc0532` two-commit/11-path range.
[Review packet and inventory](storage-profile-retained-selection-review.md).
Review completed with one Important host-payload rooting finding and one
Advisory retention-cost finding. The added DNS native regression remains held.

Reviewer0 report `ef116da3-cd14-4ca3-a7b4-9a612d229cc0` completed all four
HIGH-risk lanes at `e1bb5cf..bcc0532`: no Blocking finding, one Important and
one Advisory. The complete two-commit history is coherent, with no obsolete
approach or SQL migration; maintenance1→2 and applied1 are intentional private
format changes. The Important finding confirms that raw imported JSON roots do
not retain embedded host boot closures. The parent's read-only query of the
actual prior maintenance-next JSON returned exit0 with empty references.
Architect0 saved the explicit per-store-item rooting supplement and real-Nix
reachability regression contract. Lead released exactly eight remediation paths
to implementer0 at `bcc0532`, including one new focused test and its existing
flake-check invocation/dependency. Inputs and unrelated source/index remain held.
No host GC, native or public operation has run.

Adjacent lead inspection found that content-named JSON roots can collide for
byte-identical configs stored under distinct names while provenance requires
both exact paths. Architect0 saved the bounded clarification and lead released
it within the same manifest: permanent `maintenance-source-*` roots hash the
containing store-item path, retaining old roots and record content digests.
One real-Nix private-store case must prove both registrations remain after the
second source and first-source retry. README's owning prose pass is complete;
the final eight-path freeze is complete. Manifest `235edcd5…3965a` matches
all source bytes. The lead staged only the new store-root test for Git-flake
inclusion; seven tracked modifications remain held. Fresh watcher
`host_roots_quick_20261005` runs four focused Ruby files, existing flake checks,
and actual Admin290f candidate/resident evaluation, stopping at the first failure.
Driver `74c43fc6…eb580` and ten-file guard manifest `3cf8d582…58c44` bind the
exact bcc head, source bytes and staged new test. The first batch stopped at stage1: exit1/713.502s, overall714.202s/parity1,
no unexpected kernel build or remaining process. Maintenance31/236 passed;
commands42/458 had four assertion failures (seed34147); runner/store-root and
stages2–4 were not run. The new assertions expected internal error text, whereas
the actual CLI uses a generic diagnostic and the fixture suppresses warnings.
Lead released only commands_test to replace those invalid text expectations with
per-attempt causal mock-Nix refusal events, retaining every no-effect/pending/
predecessor/root check. Runtime and the other seven paths remain frozen, and the
new test remains parent-staged. The corrected command fixture is frozen at SHA256 `0b426280…b9c57`, with
manifest `c44061db…affe7`. Only that test file changed: refusal assertions now
use exact events emitted during each attempt; the selected missing-registration
case keeps its file present to reach the Nix validity check, while actual absent
items remain covered by the real-Nix test. All other seven source hashes and the
parent-staged new test are unchanged. Fresh watcher
`host_roots_corrected_quick_20261005` owns driver `a89d9d70…001a4` / ten-file
manifest `107f31ad…a42dd`. It checks the four corrected methods and six real-Nix
methods, then the existing full flake check (all92 methods) and both actual
Admin290f evaluations. This avoids repeating the slow complete command file
outside and inside the full check. The corrected batch stopped at stage1: exit1/70.051s, overall70.708s/parity1,
no kernel or remaining process. Four corrected command cases4/40 passed
(seed2463). Actual-Nix6/89 had six EACCES errors (seed27258) from implicit
Dir.mktmpdir cleanup of read-only imported store directories; those cleanup
errors can mask earlier errors, so rooting acceptance remains unproved. Only
the new store-root test is now released for standard-library cleanup of its own
private store plus explicit primary-error preservation. Host store/runtime and
the seven other paths are held. The parent will restage this one file after its
new freeze. Later fullflake/evals/native remain unrun.

The cleanup correction and valid unregistered-store basename were frozen at
manifest `85c04dbb…ed1108`; new test SHA `70ff71c8…ae76e` was restaged by the
parent. Fresh watcher `host_roots_final_quick_20261005` ran actual-Nix6 against
these exact bytes. It stopped at stage1: exit1/9.01s, overall9.632s/parity1,
no kernel or remaining process. Six runs/89 assertions had zero assertion
failures and three errors, seed11095: root registration was unproved. Cleanup
now exposed the primary failures. The lead's bounded synthetic local-store
probe showed actual `nix-store --query --roots` output is `ROOT -> ITEM`; helper,
mock and real-Nix assertions incorrectly required a bare root path. Lead
released only maintenance.rb, commands_test and store_roots_test for the exact
formatted root/item proof and matching fixtures. Other five paths/index remain
held. No persisted-state/public contract or rooting design change is proposed.
The exact query-format correction is frozen at manifest `e2a00a58…e414d`:
helper `8f205b0c…b6ef4`, commands `2573c280…f9ad8`, store test `f8ed0db1…0beda`;
the other five paths and inputs/lock are unchanged. Parent restaged only the
new test. Fresh Luna/low watcher `host_roots_formatted_quick_20261005` owns
private batch `/tmp/storage-profile-host-roots-formatted-check-20261005.un6qcor0`,
driver `2bdc2381…42eac` / ten-hash manifest `4e8569d5…4a191`.
Actual-Nix stage1 passed exit0/27.022s, all six required cases, no kernel;
assertion count remains pending the complete watcher report. Fullflake stage2
is active under the same owned driver; exactAdmin stages3/4 remain unreported.
The real-store proof establishes root registration without a GC run.
The full flake gate covers all four complete affected files/all92 methods;
no additional CI wait or VM matrix is introduced. The complete formatted batch passed exit0/1092.449s/parity1; all four stages
passed and no handle or kernel build remains. Actual-Nix6/141 passed; fullflake
passed in956.702s with maintenance31/236, commands42/478, runner13/35 and
store6/141. Candidate/resident evals passed54.039s/54.038s. Broader upstream
skips/repeated summaries are retained without an aggregate count. Git identity
diagnostics preceded the final all-checks-passed status.

Normal owning amendment produced `b7488807e95ad3d79febccf021d47a6afaee2b4d`,
tree `73fb0a2344976bbf50657b0780ac178ed6385e3d`, preserving all eight tested
hashes and unchanged lock. Backup
`backup/2026-09-23-storage-redesign-provider-before-host-roots` retains bcc;
cd81 admission stays unchanged. Fresh SSH fetch confirmed default e1bb and
remote feature cd81, so no new upstream replay is needed. Complete e1bb..b748
is two commits/13 paths/2776 additions/84 deletions, full diff SHA
`591f878c8198429cd7dfa6050fe8fc6b53ffa4038838e3f180805e77b6a70072`.
Original bcc inventory/diff and ef116da3 report remain linked separately.

The lead resolved Important1 under direct step9 inspection and checks: one
registrar retains exact source items and selected payloads, Nix proves roots,
and root failures precede effects/publication. No new public/state boundary,
SQL migration, obsolete branch history or step10 rerun is introduced. Cumulative
retention Advisory is documented and accepted. This does not claim observed GC
survival or native/public boot success.

Fresh watcher `retained_dns_native_20261005` owns private batch
`/tmp/storage-profile-retained-dns-final-native-20261005.of35dldp`, driver
`2bb09bd5…e1adb`, manifest `8691720e…153ae`, direct-review clearance
`65c6bbbd…a340b`. Exact b748/Admin290f guard passed. It runs the one existing
services+oneDNS ordered native fixture. That first attempt is incomplete:
driver exit1 / underlying -2 / 125.235s / parity1, zero examples and no VM
artifacts. Its broad Linux-build matcher canceled the exact modules-shrunk
derivation; the parent confirmed the owned PGID had no remaining processes.
Source inspection proved that derivation only copies/trims registered modules,
firmware and runs depmod, with no kernel compilation. The exact inspected
derivation is now allowed while all other Linux-build cancellation remains.
Fresh Luna/low watcher `retained_dns_trim_aware_native_20261005` owns
`/tmp/storage-profile-retained-dns-trim-aware-native-20261005.nkekuy3y`, driver
`c73ab983…06f88`, the same manifest/review clearance and source guards. Its
The trim-aware retry also stopped before examples: driver1/underlying-2,
68.647s/parity1, zero native artifacts. Its broad matcher flagged the initrd.
The parent inspected its derivation: make-initrd-ng/cpio/compression only,
empty buildInputs and all42 referenced store items registered. A fresh watcher
retained_dns_payload_aware_native_20261005 now owns
/tmp/storage-profile-retained-dns-payload-aware-native-20261005.qqla295w,
driver 64b9ff5f…6e3c53, with the same source manifest and review clearance.
Only the two exact inspected module-trimming/initrd-packing derivations are
allowed; every other Linux-build cancellation remains. That run completed
exit1/430.174s/parity1, no unexpected kernel build. One native example failed
in17.67s at stage1: the artifact prefix made its Unix socket122 bytes, above
the108-byte limit. Parent source/path inspection confirms this launch-path
constraint and an exact owned-path process scan found zero processes.
Fresh watcher retained_dns_short_native_20261005 now runs the unchanged driver
and guarded source in /tmp/ndns.e87t01sh. The observed socket would be68 bytes
with this prefix; this is a launch-path correction, not a source fix. That
run completed exit1/385.891s/parity1 with no unexpected kernel build. One
example failed325.69s at stage2, passed0/hold_released0, expected true got false.
Bounded shell evidence narrows failure to old-writer counters or the following
unlogged host disk-stat tuple comparison before mask/start probes. The initial
counter/disk baselines were not saved, so the specific difference/cause remains
unproved; the parent corrected its premature counter-only attribution.
Implementer0 completed bounded diagnosis: all eight protected SQL projections
are byte-identical to before.json and payload equality passed. Failed predicate
remains counters or the following host tuple; both original baselines are absent.
Raw-disk and one-clone source checks support no qcow2/reset cause. Late initial
scheduler start is only a timing candidate; no readiness fix is inferred.
A fresh parent metadata scan found zero exact-prefix cmdline processes,
PGID790647 members and artifact FD holders. Lead released only the native runner
to implementer0 for private bounded baseline/comparison diagnostics, preserving
all reads, assertions and lifecycle semantics. No runtime correction or guessed
stabilization is authorized. Ruby syntax/diff and lead inspection precede normal
owning fold and a fresh short-path native run. Other source/index and
publication/package/actual cluster operations remain held. Earlier failures stay.

Root preparation advanced the clean feature from integrated86fe to actual
shared master `e5ba1912b74e0bad6d47a61b629100931aa53e52` by fast-forward only.
The three intervening commits change coordination records only; relevant
instructions, source/config/tests and both flakes are byte-identical. Foreign
record contents and shared work/index were untouched. The consumer still pins
cd81; new pin authoring waits for native proof and exact provider publication.

Implementer0 prepared only an invalid recovery evidence template in private
/tmp/storage-profile-recovery-template-20261005.o1za129y:
template SHA669ce203…00d2 / README51961ae7…fa51. The exact version1 schema
has31 NULL placeholders for the current hold digest, proof references and
current disk bindings; it supplies no measured facts or runnable evidence.
Historical device/inode remains unmeasured. Lead must validate the immutable
sources, copy receipt, stopped ownership and disk identities after package
activation before completing any final evidence. No operation was run.


The Advisory concerns cumulative digest-named config roots. The lead accepts
and documents this retention cost for the current provenance/history
contract. This remediation does not authorize pruning roots or changing cluster
lifecycle behavior. Required pending and historical evidence stays rooted.
Direct requested rooting remediation will use focused inspection and checks
under mandatory review step9; substantive boundary changes would require the
affected step10 lanes. Review findings are recorded in the linked packet.

## Earlier retained-trial execution evidence (2026-10-04)

Private execution evidence:
`/tmp/storage-profile-resume-20261004.7t052v6y`.

Fresh baseline attempt failed exit1/17.932s before SQL: public services SSH
reported no route to host, with zero rows captured. The recorded runner PID
does not exist. Read-only host metadata found six retained disks, no process
references to the owned VM paths, no disk FD holders, no recorded Unix socket
listener, and no response from the services address on the existing bridge.
No mutation or retry occurred. Supported ordinary storage/bridge start is being
checked; this is a liveness issue, not a DB comparison failure. Prior original
baseline and cold copies remain available. New measurements after boot cannot
be described as an unperformed fresh pre-boot file/DB capture.

Source inspection showed ordinary start points at the new toplevel without
copying it into the preserved root; that proposal was not executed. Architect0
saved the supported second public maintenance cycle. The latest immutable full
configuration's services selection matches the prior validated copy and copied
boot/release. All three nonservices descriptors match the actual successful Node
update selections; all six disk sizes/mtimes and the prior released ledger were
preserved before any action. New private `prior_copy` evidence references that
ledger, not just a host store root. A fresh watcher now owns public
maintenance-start against the proven resident configuration. Fresh masked DB
backup/baseline, public copy-only, stop and copied start/refresh/release will
deliver the correction; successful actual delivery makes an additional ordinary
services update unnecessary. No new mode or VM test is introduced.

The first maintenance watcher used the default CWD and executed zero operations.
Parent identity/guards passed from the literal tracking CWD. A fresh watcher ran
the public maintenance command: exit0/70.755s/parity1, running services under
maintenance_ready/readyfalse. The next backup/baseline launcher stopped before
SQL at its public JSON-status preflight (exit1/1.312s, no detailed stderr).
Read-only parent status observation then proved the live runner/held phase via
the text command, followed by a successful JSON status with the same ownership.
That unexplained status observation failure is retained. No DB comparison or
backup had run; a fresh guarded read-only capture is now the next operation.

The fresh masked capture passed exit0/10.058s/parity1. Logical backup is
1,324,514 bytes. The consistent baseline covers 27 groups/1,168 rows with zero
protected changes against the original pre-copy baseline. Its seven additions
are exactly package6 and items31–36 already observed after the previous seed;
only two dynamic Pool-space rows changed. A fresh watcher now owns the public
services copy-only command; no unmasked boot or provision retry is running.

Copy-only passed exit0/260.432s/parity1 and reached copied with the running
generation still held. All five nonservices descriptors, including the three
updated Nodes, remain byte-equal in the rooted next configuration. The watcher
reported no unexpected local kernel build. Supported stop has completed;
copied-config start/real refresh/release was run by its fresh watcher.
The fixed delivered-script/original-file/quota packet is prepared and guarded
against the exact copied toplevel, but unexecuted. Provision remains unstarted.

Copied-start failed exit1/985.14s/parity0 at recorded runner readiness. Services
obtained its boot shell, but the runner stalled at DNS-primary and then shut
down its machines. DNS-primary failed initrd NixOS activation; DNS-secondary
failed finding its NixOS closure. The PID and ready files are now absent; the
hold remains starting_copied. No seed/refresh/release success is inferred.

Immutable comparison with the prior successful full boot confirms that both
DNS descriptors changed only toplevel/rootDisk in the latest full result-config
from Node updates. Those updates never copied or activated DNS. The lead's
resident proof established the three updated Nodes but missed DNS residency;
five-descriptor equality against that build configuration did not fill the gap.
Architect0 assesses supported recovery; implementer0 inspects update/result-config
bookkeeping read-only. No pending-hold edit, disk import, reset, force or retry
has been performed. All source/index/package and separate API holds remain.

Both source assessments found no current public recovery seam for this pending
selection. The lead authorized a bounded provider correction: distinguish the
full build candidate from successfully applied per-machine selections, and
derive recovery from genuine earlier DNS boot provenance while retaining the
current Nodes, copied services and six disks. Architect0 is saving the concrete
brief before application authoring. A provider-local maintenance record v2 is
accepted in principle for explicit predecessor/provenance, with legacy v1 read
without inference. Canonical schema1/policy3, mask policy1 and preserving-seed
contract1 stay unchanged; no new phase or relaxed release guard is planned.
The finalized brief releases eight provider source/test/documentation paths to
implementer0, including the existing native fixture's retained DNS-root check.
No generic/OSVM/Admin or input change is included. Application source is now in
authoring; package transition and all cluster operations remain held. The new
public metadata-only recovery will preserve the predecessor hold, retain copied
services and actual Nodes, and derive only the two DNS descriptors from prior
successful boot provenance. Earlier services-only native proof cannot cover
that case; new review and the owning DNS regression precede package delivery.

Historical device/inode were not measured. The accepted trusted-operator
continuity account uses original paths/sizes/cold evidence, exact successful
per-machine source references and the intervening operation ledger, with no
known reset/replacement/restore/truncation. Current stopped-disk stat is a fresh
execution binding, not historical inode or unchanged-content proof. Any known
contradiction remains a blocker. Actual executable-bound host inspection after
runner cleanup found zero owned runner/QEMU/virtiofs processes and zero disk FD
holders, with all six images present. No release/provision/payload is claimed.

### Completed rebase preparation before activation

Initial fresh fetches selected generic master6a972b9a, provider mastere1bb5cf3
and workspace masterc3124834. Generic maintenance policy4ef is already upstream; provider also
contains the earlier maintenance/profile/native series, but not the four-path
admission correction. Architect0 owns the bounded rebase/composition brief,
implementer0 owns any source conflict/URL edits, and the lead owns normal
rebase/generated locks, local proof, publication and final integration.

Provider residual rebase is complete and published at
`cd81e83f91a552eb0138e58cb76312784a2988df` on current `e1bb5cf3`.
It contains one commit and exactly the reviewed four-file correction,
540 additions / 4 deletions, full-index patch SHA256
`ae52282070254f1ac108e295360af3ca7a043ee915d3eca911ebfd0a663456b3`.
All corrected blobs equal `0b0ba9d8`; upstream flakes, generic6a/Codex32775
and merged feature history are preserved. Three Ruby syntax checks and diff
checks passed. Prior47/0 and independent review carry forward as their original
source-equivalent evidence; no new DB/VM or full review run is claimed.
Remote provider master remains `e1bb5cf3`; the old exact0b0b head has a
published backup ref. Root rebase is complete at
`1acb207784d31e8891fbc6db95125d2470df6d8d` on actual `c3124834`, one commit,
exactly two flakes (5 additions / 5 deletions). The generated lock changes only
four provider metadata leaves; generic6a/Codex32775 and all other nodes/follows
remain current upstream. Final no-build evaluation passed. Both feature heads
and backups had exact SSH readbacks; root master was c312 at that checkpoint. Public comparison
captured basec312/head1acb, preserving initial registration metadata.

The old-CWD watcher preflight ran zero commands; the next launch refused a
superseded hardcoded public generation before checks. Neither supplies check
evidence. The private driver now invokes the stable public command from the
literal tracking CWD, and a fresh Luna/low package watcher completed the four existing
root checks/default build/output proof; final results are recorded below.
Before activation, public status selected package `nl29dilg` with old provision
hash `1c067262...`; the correction was not selected at that checkpoint. CI metadata was read once only to
ensure no superseded provider run remained; current-head CI is not awaited.
Activation and workspace/master integration were pending at that checkpoint.
Storage remains held.
Private execution evidence: `/tmp/storage-workspace-rebase-20261004.6uinnel5`.

The earlier selected packagecfrf8m had schema1/policy3 and old bare admission
checks. Workspace selection is now fixed; retained services delivery remains
separate. The retained cluster trial, scheduling and separate API diagnostics
remain held; this continuation performed no storage trial. Session remains active.

### Activation and integration result, 2026-10-04

The user reported the public switch complete and said “done, proceed”. Public
host status selects the exact tested `s7y4` package and `q49` tools; active/profile
Codex resolve to the same executable. All eight selected-byte equality checks
passed at schema1/policy3/providers2/profile_loader1. The four core owned
workspace services are active/running with their ExecStart bound through the
selected profile. Public same-session current and retained roster commands pass.
Own provider status exited0 and reports stale/readytrue/bridge, released with
pendingfalse; no refresh or cluster mutation was performed. Selected package
proof does not update or certify the retained services guest scripts.

The actual shared/remote master remained fd7, so no further rebase or build was
needed. Public comparison was refreshed at basefd7/head86fe. Shared master
fast-forwarded normally to `86fe8f201ad041bbbb7bfabb6783cc09debde46c`, changing
only the two flakes. No paths were staged for integration; foreign working-tree
and index entries were preserved. Normal SSH publication completed; exact final
remote readback confirmed both master and feature at exact86fe. This implements the user's explicit
workspace/master direction without awaiting CI. No other repository default or
storage operation was integrated/performed, and all feature/backup refs remain.
Evidence: `/tmp/storage-workspace-rebase-20261004.6uinnel5/activation`.

### Completed package proof and activation handoff

Fresh Luna/low verification passed0/252.856s/parity1, stages1/2/3 all0:
four existing root checks, default package and actual packaged source proof.
All eight equality fields passed; schema1/policy3/providers2/profile_loader1.
Selected generic6a/Codex32775 sources and model catalog match the package;
corrected provision/acceptance scripts, launchers, maintenance, ordinary defaults
and canonical host/tools contract match their owners. No kernel build or
remaining watcher handle was reported. The build logs retain Git identity
chatter from test fixtures; the reported command/suite results remain all0.
Evidence: `/tmp/storage-workspace-rebase-20261004.6uinnel5/package`.
Package `/nix/store/s7y4bgq7iw0idkv5japb538kfwphk4nf-dev-workspace-0.2.0`;
tools `/nix/store/q49yi3hizfraywb6d0fwi3drzzlylqjq-vpsfree-dev-workspace-tools-0.1.0`.
At the package-proof checkpoint the package was built and unselected. After
that tracking checkpoint, any final
coordination-only replay must preserve both flake hashes and resolve this same
output; a changed output needs the existing package-equivalence proof.

- [x] Preserve current upstream history and the exact reviewed residual fix.
- [x] Publish provider and generated workspace pin with durable backups.
- [x] Pass local no-build, four root checks, package and byte proof.
- [x] Finish final comparison/publication after the tracking checkpoint.
- [x] Operator activates through the public switch with managed sessions idle.
- [x] Verify the selected generation, then fast-forward/publish workspace master.

Final tracking checkpoint `fd7d07a41ea7e71c374d19efd06bbfab476a128c`
committed only the three owned coordination records with normal hooks and SSH.
The pin was replayed to final `86fe8f201ad041bbbb7bfabb6783cc09debde46c`,
range-diff `=`, identical full patch/message/two flake hashes and clean index.
Final package evaluation is the exact tested `s7y4` output; final no-build passed.
Root feature SSH readback and comparison are complete at actual basefd7/head86fe;
At that pre-activation checkpoint remote master was fd7. Package/source proof
carry by equality,
not by claiming another four-check realization on the replay. Historical
registration/initial-base metadata remains unchanged; foreign work/index is
preserved. Evidence: the private `consumer-replay.json` and `handoff.json`.

The completed operator handoff used the ordinary public command from an
external terminal with the lead and managed sessions idle:

```sh
workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/workspace
```

Expected output package: `/nix/store/s7y4bgq7iw0idkv5japb538kfwphk4nf-dev-workspace-0.2.0`.
Activation verification and the authorized workspace/master fast-forward are
now complete. No second switch or CI wait was performed. Other repository
default integration and retained services delivery remain separate.

Storage operations, scheduler resume and API diagnostics remain held. The
session stays active and feature refs are retained.

### Prior correction handoff, 2026-10-03

2026-10-03 current phase: external idle activation handoff for the corrected
provider. Final consumer feature `19cb25ee8d5333a4ea4c1816806c130c41652f1f` is
published, independently reviewed through its identical original pin patch,
and locally verified. Provider `0b0ba9d8` review and exact CI passed. The
four-stage provider batch passed 47 real API examples and the default/compatible
checks. Both source histories are coherent, with no obsolete approaches or
provider/root migrations.

The fresh package batch passed exit0/248.639s/parity1: all four existing root
checks, default package build and actual output proof. Corrected admission
scripts, unchanged provider launchers/defaults/helpers, host/tools canonical
contract and Codex sources match their selected owners. Package:
`/nix/store/vyf5bpadsnplrzfvrhx182wcsfnw5602-dev-workspace-0.2.0`.
Tools: `/nix/store/4w4mbc7x9kgj798bf16kpfq7mdi11w6b-vpsfree-dev-workspace-tools-0.1.0`.
Schema1/policy3/providers2; contract SHA256 is
`33acdc50fa6b7ed94f84d1f7f1db0af8d76d7d57d2e721cbb6a204a96b27c0d1`.
This package is built and **unselected**. Installed399 remains unchanged;
no live retry, scheduler resume or package selection occurred.

Platform API CI diagnosis remains separate. All three ordinary
Node updates and process-bound corrected-source proofs passed. Public copied
boot completed real regular Node refresh and released the maintenance hold.
Node review/direct corrections, declared lint,
full Node634/0 and the one remote-restore integration4/4 passed. The selected
workspace package is unchanged. The registered bridge cluster is running and
ready with its maintenance hold released. Scheduling remains stopped after the
provision failure; no retry or resume has been performed.

The retained config now explicitly selects storageProfile enable:true and
enrollment:true; every other JSON field is equal to the prior config. Private
recovery and preparation evidence is at
`/tmp/storage-profile-retained-20261003.nemcjis2`. The earlier public maintenance
command passed0/88.027s/parity1, followed by copy-only with phase copied. The private
logical DB dump and 27-group baseline (one original VPS) completed before copy.
The full cluster is now running and ready; original VPS/data and all six cold
recovery disk copies are retained. Profile provision, physical payload/history
and retirement remain pending.

The user selected "Fix Node recovery first" and then directed "Implement the
plan." Architect0 owns the saved design brief; implementer0 owns Node cleanup,
telemetry recovery and the existing remote-restore fixture; reviewer0 owns the
independent committed HIGH-risk review. The lead owns tracking, normal commits
and fresh Luna/low verification watchers. No additional default-branch merge or package switch is authorized. The completed
Node slice now permits the separately recorded retained-profile public trial.

- [x] Save precise Node recovery and fixture design before source edits.
- [x] Implement cleanup error precedence, safe channel retirement and bounded
  storage-status failure handling; author persistent restart/payload fixture.
- [x] Pass declared runtime lint and the full Node suite.
- [x] Finish selector/static checks and two normal owning commits/hooks.
- [x] Finish final-head scoped fixture evaluation after upstream rebase.
- [x] Complete independent committed review of all four HIGH-risk lanes.
- [x] Resolve both Important findings with focused verification and owning fold.
- [x] Pass the corrected remote-restore scenario with actual payload proof.
- [x] Complete masked resident boot, fresh DB/catalog baseline and public copy-only.
- [x] Complete public copied boot, real regular-node refresh and automatic release.
- [x] Update all three Nodes and prove their running final runtime.
- [x] Inspect exact290f platform API failures and assess provision impact.
- [ ] Capture the hidden request exceptions with test-only diagnostics.
- [x] Fix the provider's two top-level admission observations and prove real
  autocommit staging/visibility, freeze refusals and reader cleanup.
- [x] Finish independent provider review and exact feature publication.
- [x] Finish generated consumer pin and independent composition/history review.
- [x] Finish checked package and final feature publication/comparison.
- [ ] Complete supported external activation and verify the selected generation.
- [ ] Update services and prove its actual corrected guest scripts before retry.
- [ ] Complete the recorded retained-profile update and full-cluster acceptance.

The four-path provider remediation is committed at
`0b0ba9d869c04a4362f6051f5cc281ddf1b5a642` on8f8, with tree
`2dfb8aeba684b17a829af5123adba5641d9c3cce` and a clean worktree/index. Its47
passing examples include actual autocommit staging/second-connection visibility,
bounded reader cleanup and fresh payload-routing refusals. The
initial run is retained at `/tmp/storage-profile-admission-quick.7syutiak`
(exit1/66.717s/parity1). ActiveRecord uses a next-transaction isolation override;
the failed assertion inspected the session default instead. The narrow reader
session setup correction retained all assertions. The passing batch is at
`/tmp/storage-profile-admission-quick-fixed.i40tueb9`: API61.964s, existing
projection4runs/32assertions0/0.803s, default no-build12.193s, compatible profile
smoke658.645s. See the [committed review packet](storage-profile-admission-review.md).
The four-commit/25-path series contains no provider migrations; correction
folded into its owner, backup399 retained, no hooks bypassed. Installed provider399 still contains
the old immutable scripts, so source checks do not repair public provision.
Provider Check37154598713 completed SUCCESS at exact0b0b; prior399
Check37114037083 also completed success. All older branch checks in the short metadata query are
completed, so there is no superseded live run to cancel. CI is not awaited.

Provider review used retained reviewer0 gpt-6.1-sol/xhigh/read_only in all four
HIGH-risk lanes, justified by storage admission, file writes and deployment
ordering. Its sole Advisory concerned stale rollout wording, now explicitly
historical; no source amendment or review rerun was needed. The replacement
consumer review also completed with no findings; package realization remains
pending. These reviews authorize no deployment, merge or physical readiness claim.

Consumer reviewer0 retained gpt-6.1-sol/xhigh/read_only and independently inspected
the complete ad539..bcb one-commit/two-path range, exact tree bf8038 and binary
diff 4e193905, all four HIGH-risk lanes. No obsolete history, root/provider
migrations or additional pin/default/follow change was found. Root no-build
passed0 before commit; this is evaluation only. The fresh one-operation package
driver is `/tmp/storage-profile-admission-package.p5dtjka1/launch.py`, with all
root/provider/Admin/generic source and index held. Its prelaunch local variable
name collision was corrected before execution; this was private launch plumbing,
not application source or failed verification. Source proof and installed-script
delivery still precede a public retry. See the
[consumer review packet](storage-profile-admission-consumer-review.md).

### Activation clarification, 2026-10-04

The user questioned the requested additional workspace activation. The earlier
activation/integration is complete. The later provision failure exposed a
provider-script defect; the corrected provider requires a new package selection
and services update because these guest scripts are embedded immutable inputs.
Read-only public workspace-host status now selects
`/nix/store/cfrf8mjcww7lks1ylqzgfay5920ab029-dev-workspace-0.2.0`, tools
`/nix/store/k5vvjzpr72xbmaycgail274bgqxh6dk7-vpsfree-dev-workspace-tools-0.1.0`.
Its contract remains schema1/policy3. Both provision/acceptance scripts are
byte-identical to the previous vah tools and still use the top-level bare
admission check. Thus the reviewed correction is not selected. The status/code
checks performed no switch or cluster operation; no claim is made about who
selected this generation or why. The remaining external package update and
supported services delivery are unchanged.

### Final consumer source and operator handoff

A normal one-commit replay onto actual shared master `990a5929` produced final
`19cb25ee8d5333a4ea4c1816806c130c41652f1f`, tree
`3087dbed87bc9066707c656a87d63ec1e7c75e2e`. The 30 upstream paths are coordination
records only; relevant source/config/procedure blobs are unchanged. Range-diff
is `=`, both flake hashes, complete two-path 5+/5- binary diff and commit message
are identical to the reviewed `ad539340..bcb25d08` patch. Shared HEAD/index and
foreign working files were preserved. Backup
`backup/2026-09-23-storage-redesign-before-admission-publication` retains bcb.

Final package evaluation passed0/7.218s and resolved the exact already-built
vyf5 output. Final no-build check passed0/3.838s. These checks preserve the
original independent review and package observations within identical source;
no new review or VM run is claimed. SSH feature readback is exact19cb25; remote
master remained1fa9 at feature publication. Public comparison capture records actual base990a5929 and
head19cb25, retaining historical initial registration metadata.

The consolidated operator handoff was committed and published as tracking-only
`a51fa51e2e2503ce658003f75b77a5be1ff6c042`, with eleven owned record/note paths.
Remote master now includes that checkpoint; the new pin remains only on feature
19cb25, not merged. Foreign index entries were preserved, shared index empty.
This is the genuine external activation ownership handoff under the tracking
cadence, not another application or default integration.

Private package evidence: `/tmp/storage-profile-admission-package.p5dtjka1`.
Stage1 took241.182s, stage2 took7.191s, stage3 proof exit0. No watcher handle or
reported kernel compilation remains. Source/index holds remain in place.

From an external terminal, after this lead and every managed session/member is
idle with no pending request or submission, run:

```sh
workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/workspace
```

The public switch's idle requirement prevents activation from an active lead
turn. No delayed/background activation is arranged. Report the result so the
lead can verify the actual selected generation, perform the normal services
update and prove its immutable provision/acceptance scripts before retrying
provision. The retained cluster stays running/ready/released, scheduler stopped.
No new workspace/default integration is authorized; the earlier approval covered
already-merged1fa9. Profile payload/history/scheduling/repeat update and retirement
acceptance remain pending, as do the separate held API CI diagnostics.

The [Node recovery brief](design.md#node-rpc-cleanup-and-remote-restore-recovery-slice-2026-10-03)
specifies original-error precedence, per-channel retirement completion,
verified transport closure and consumer-thread exit, the late-recovery request
race, bounded recovery waits and cooperative updater stop. Known transport
failures are classified narrowly; programming errors remain visible. Lasting
behavior is documented in Admin `docs/node-rpc.md` and linked from its index.
The lead's direct writing pass accepts that prose unchanged. Two commits will
separate the runtime/spec/docs behavior from the existing scenario's persistent
restart and A/B/C payload/history acceptance.

Fresh Luna/low `node_rpc_full_declared_46` passed at the complete frozen nine-path
source plus six dependency/flake hashes: root RuboCop 1.85 exit0/14.904s;
full libnodectld 618 examples/0 failures exit0/38.756s; total54.107s,
source parity1 and empty index before/after. Evidence:
`/tmp/node-rpc-full-z7bkokjv` (directory0700/files0600); no owned command or
automatic disposable TestDb process remains. Tests use the owning Nix shells,
an isolated bundle and automatic disposable DB; inherited/configured DB is
refused. These checks do not establish real broker/VM/payload recovery.

Earlier focused verification is retained in the
[review packet](node-rpc-recovery-review.md): incomplete33/3 exit1/761.69s
controlled-fixture stall, corrected39/1 exit1 missing transport timeout accessor,
then focused39/0 followed by declared root lint10 offenses. Test fixtures were
corrected without weakening assertions. Portable scoped directives and removal
of redundant Struct keyword initialization resolved the declared lint issue;
this last delta changed no runtime control flow. The first interrupted run's
exact RSpec process and automatic TestDb were reaped under explicit lead
cancellation; no source acceptance is inferred from that incomplete run.
All original logs remain private. A parent log-creation permission defect in the
third verifier was corrected to0600; the new driver sets umask077 before opening
logs. Runtime source was unaffected.

Architect0 is source-checking the fixture's ordinary startup/restart/input/output
interfaces against the saved brief. This is design conformance, not independent
review or execution evidence. The command-first `nodectl get --parsable` scalar
interface is retained; no CLI change or transient repatch is required.

### Completed workspace activation and integration
The user reported activation and explicitly approved workspace/master integration
conditional on successful verification: "activated. you can verify it, if it is
ok, you can merge the workspace." This approval covers only the workspace;
generic/provider defaults and storage deployment remain outside that scope.

Activation verification passed through the installed public commands. Host
status selects the exact reviewed `zmwh78dk` package; current/team commands
work through that generation. Router, portal, Codex and tmux units are active,
and all four stable ExecStart paths resolve to that selected package. The
public same-session provider status succeeds with stopped/bridge state and
the exact reviewed tools. Installed contracts match schema 1/policy 3.
The portal responds with its expected unauthenticated HTTP 401 using the
configured public CA, TLS verification 0. No credential was read or sent.
An initial literal unit-path check missed the stable profile indirection;
the default curl CA bundle also lacked the internal CA. Corrected checks use
resolved paths and the existing CA, without changing units or trust settings.
Evidence: `/tmp/storage-profile-activated.zsuzp_g4`.

Normal one-commit replay onto tracking-only local master `3fd3ff77` produced
clean `1fa9c982b866a305bd1451f2c32f6d387d2dc1a3`. Range-diff is `=`; both
tested flake hashes, the complete two-path 9+/9- patch and its full-index
SHA256 remain unchanged. Final Nix evaluation resolves the same actual selected
package path, so the built package proof and original independent composition
review carry forward without a new activation or full review rerun. The exact
integration comparison was captured as `3fd3ff77..1fa9c982`; backup
`backup/2026-09-23-storage-redesign-workspace-before-integration` retains the
activated source `6d1b9c4d`.

The fresh final-head no-build flake check passed. Normal shared-root
`git merge --ff-only` advanced local master `3fd3ff77` to exact pin `1fa9c982`,
changing only the two flake files. Normal SSH push advanced remote master from
`93389c33` to `1fa9c982`; the feature ref is retained at that same head.
The already-published handoff tracking commit is included as an ancestor.
A concurrent session then advanced shared local master with three tracking
files; its commit was preserved. The pin remains an ancestor, both tested
flake hashes match, and all other index entries outside those concurrent paths
remain equal to the pre-merge snapshot. No generic/provider default was merged,
no additional package switch or cluster lifecycle action occurred.

The requested rebase is complete. The generated locks preserve upstream's
Codex Web `4c170393` selection and every unaffected input/follow.

| Repository | Current base | Feature head | Publication |
| --- | --- | --- | --- |
| Generic runtime | `924c0ec2` | `4ef298b3` | Published |
| Provider | `8f8d8ecf` | `399c3302` | Published |
| Workspace consumer | `3fd3ff77` | `1fa9c982` | Merged and published to master |

The generic policy commit has an unchanged range-diff. The provider's three
functional commits also compare equal; only its two pin files differ from
`45d7ce88`. The consumer remains one commit changing two flake files, with
exactly eight generated provider/runtime metadata leaves relative to `93389c33`.
Backups retain published `2b67af62`, `45d7ce88` and `492fdf8e`. The shared master,
unrelated files/index, registration and historical initial base remain intact.
The member authored the root conflict files; its read-only shared `.git` blocked
staging, so the lead verified hashes and staged/generated/continued normally.
[Shared index access](../../notes/cross-project/2026-10-03-shared-worktree-index.md)
records that boundary without a permission or hook bypass.
[Git pathspec CWD](../../notes/cross-project/2026-10-03-git-pathspec-cwd.md)
records why an empty nested-directory diff check supplies no evidence; the
corrected root-directory check passed for the owned tracking files.

Fresh watcher `storage_profile_rebase_quick_bound` passed all six stages in
1175.12s with source parity1: generic40/250, maintenance13/121, runner10/27 and
selectedCLI8/105, all zero failures/errors/skips; default and explicitAPI46
smoke passed, followed by provider/root no-build. The first utility's wrong-CWD
current-session refusal started zero checks. Evidence:
`/tmp/storage-profile-rebase-quick.cgbjlt0h`. Generic4ef CI37113228573 passed.

Reviewer0 completed the committed [composition review](storage-profile-rebase-review.md)
with saved Sol/xhigh/read_only settings and all four HIGH-risk lanes: no findings
at any severity. All exact heads/trees/full-index diff hashes match; coherent
1/4/1 complete histories, no obsolete iterations or migrations. The review
supports carrying forward the scoped host/native observations because relevant
source/input interfaces are unchanged. Prior functional lanes are not claimed
as rerun.

Fresh watcher `storage_profile_rebased_package` passed all three stages in
245.623s with source parity 1: four existing root checks (238.146s), default
package build (7.296s), then installed runtime/contract/helper/Codex byte proof.
The host and provider contract bytes match schema 1/policy 3 and SHA256
`33acdc50fa6b7ed94f84d1f7f1db0af8d76d7d57d2e721cbb6a204a96b27c0d1`.
Installed host/session helpers and selected Codex `4c170393` source bytes match;
provider catalog has two executable providers and the eager profile loader is
present. Package: `/nix/store/zmwh78dk1vjh2b91qnibjl682rb8hmwc-dev-workspace-0.2.0`;
tools: `/nix/store/vah0176g8h75vasl0nlg0farmaacybid-vpsfree-dev-workspace-tools-0.1.0`.
Root test groups passed 4/19 and 7/95; package groups passed 350/3731 (12 skips),
8/33 (0 skips), 115/796 (3 skips), with zero failures/errors. No local kernel
compilation or owned process remains. Evidence:
`/tmp/storage-profile-rebased-package.xnradz5x`. A redundant post-launch verifier
received a hash where its package path was required and performed zero checks;
the launcher's correctly parameterized installed proof had already passed.

At the pre-activation checkpoint, normal exact-lease SSH publication advanced
the workspace feature to `6d1b9c4d`; remote master was still `93389c33`.
Public comparison capture recorded that exact
base/head. Ordinary remote backup refs preserve both exact pinned dependencies:
`backup/2026-09-23-storage-redesign-workspace-runtime-4ef298b3` in generic and
`backup/2026-09-23-storage-redesign-workspace-provider-399c3302` in provider.
Readback confirmed both heads; no default integration occurred. Generic CI
37113228573 and provider CI37114037083 passed. The later activation and merge
are recorded above.

API support stays at `46b3bf6f`. Its broad CI run `37030949481` completed with
117/118 tests passing. The sole failed test is
`storage/restore-after-reinstall-remote`: remote rollback timed out after 900s,
then its dependent snapshot creation returned 423 Locked. [Diagnosis](api-remote-restore-ci.md) identifies an upstream-existing Node
RPC-cleanup timeout/daemon exit and restart losing the fixture zero-delay patch.
The broker timeout trigger remains unknown. Node reliability and persistent
fixture timing are separate follow-up work; no blind rerun/manual unlock occurs.

The user-approved workspace/master merge is complete without waiting for the
storage redesign. Keep durable exact published dependency refs and preserve both
maintenance-aware provider code and policy >=3 in later repins; a policy-3
number paired with a legacy provider is insufficient. The profile stays off
by default. The reviewed package is selected; no storage-cluster operation
occurred during activation verification or integration.

The user reported activation after the handoff for this installed public command:

```sh
workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/workspace
```

The lead verified the public selected generation and did not invoke or schedule
a second switch. Future package switches still require an external idle operator.
User-created VPS/disks/files remain preserved.
Full-cluster public refresh/release and payload acceptance remain pending.

### Previous package checkpoint before the latest rebase

Current provider: clean published `45d7ce88`; API support: `46b3bf6f`. Required
host migration and the real retained-services native fixture passed. The native
result proves its ordered services-only assertions and ends at `starting_copied`,
with no hold release. The generated consumer pin is committed at `492fdf8e`;
reviewer0 completed all four HIGH-risk composition lanes with no findings.
The four root checks, composed package build and packaged contract/source-byte
proof passed. The external operator owns the next public package switch while
all managed sessions are idle. Full-cluster public refresh/release and populated-cluster
payload acceptance remain pending. API broad CI was still running at this
checkpoint; its completed failure is recorded above.

Consumer branch preparation: normal pinned-Git rebase advanced the clean
registered workspace feature from `58df04cf` to committed shared master
`8990ecca0cea7a3b59dd88e31138b177500bc43a`. Its package inputs, procedures,
registration and original `3f539b0` backup remain unchanged; shared head/index
parity was verified. The normal pin commit changes only two flake files and
eight provider/generic lock metadata leaves; all other nodes and follows are
unchanged. The fresh consumer no-build check passed in 16.151s with source
parity 1. [Consumer review packet](storage-profile-consumer-review.md) records
the complete one-commit series, actual review base, contracts and remaining
package/activation gates. The fresh package watcher passed all three stages in
250.02s with source parity 1: four existing root checks, default package build,
and packaged contract/helper-byte proof. Consumer `492fdf8e` is published over
SSH. Package activation remains pending.

Built package: `/nix/store/g1jwv2598a5ig64f8yk1xg62mminkzpi-dev-workspace-0.2.0`;
provider tools: `/nix/store/k62d9v4jjgqv4y2wgxz019k67liv75jp-vpsfree-dev-workspace-tools-0.1.0`.
Host and tools canonical contract bytes match SHA256
`33acdc50fa6b7ed94f84d1f7f1db0af8d76d7d57d2e721cbb6a204a96b27c0d1`,
schema 1/policy 3. Selected profile helper, maintenance helper and provider Nix
source bytes also match. Evidence: `/tmp/storage-profile-composed-package._oa5spvo`.
Root deployment/instruction tests report 4/19 and 7/95 with zero failures;
package test groups report 344/3633 (12 skips), 8/33 (0 skips), 115/796 (3 skips),
all zero failures/errors. No kernel compilation or owned process remains.

Reusable fixture lessons: [forced VM replacement observations](../../notes/vpsfree-dev-workspace/2026-10-03-forced-vm-fixture-observations.md).

### Storage-profile verification history

The exact published `78ffa6f` retained-services invocation exited 1 after 680s.
Its one native example failed after 216.23s in stage 1, after the initial
disposable services guest booted. Parent inspection of the private guest shell
log located MariaDB ERROR 1064 at the fixture namespace mutation: the `offset`
column is unquoted in both the assignment and `MIN(offset)` expression.
Implementer0 owns a one-file identifier-quoting correction and a focused
disposable database check before another native run. Evidence:
`/tmp/storage-profile-retained-services-78.W0DG89VX`. Cleanup completed; no owned
process remains and the registered retained cluster is untouched. This attempt
does not prove maintenance masks, preserved allocations, copy or new boot.

The one-line correction quotes both `offset` identifiers. A fresh Luna/low
check passed against the actual API46 automatic disposable database/schema in
38s: PREPARE succeeded, no UPDATE or guest executed, database cleanup completed.
Logs `/tmp/storage-profile-prepare-watch.vvTykFkl`. The tested source SHA256 is
`2c63e8c775a3f50cef56f87544ef1e85fe695ac92397e40966b3ed869637915c`.
Normal fixture-owning amend and exact-lease SSH publication created clean
`3175df09a8e3080947730e25d06c3fb577816a2f`, tree
`f710925bb6c9a4d4810022c572ca3b0fef3f3ca3`; first three commits remain identical,
and the last differs only at that SQL line. Four commits/25 paths, 5265 additions/
67 deletions, full binary diff SHA256
`9ac69fd487cfb636a7420de54fc8f0b95ae233a42e2ca30794dd563c300f1802`.
Backup `backup/2026-09-23-storage-redesign-provider-before-fixture-sql` retains
`78ffa6f`; freshly fetched master remains `c56f981a`. No new contract or full
unaffected rereview is implied. Fresh watcher `storage_profile_retained_services_3175`
owned the actual compatible native retry, logs
`/tmp/storage-profile-retained-services-3175.6ka7ukno`; source/index were held.
Exact-head provider Check `37075156498` passed; prior `78ffa6f` Check
`37072305045` passed. All earlier same-branch runs are completed, so no superseded
live run requires cancellation. API46 broad `37030949481` remains in progress;
the topic selection's 27/27 success is unchanged.

The exact `3175df0` native retry exited 1 after 421s; its one example failed
after 218.63s in stage 2. The initial old guest, corrected namespace/resource
mutation, projections and clean stop completed. `validate_system!` then refused
before the masked guest boot: “resident has an unsupported application writer”.
Parent inspection of the actual public fixture closure identifies exactly
`vpsadmin-rabbitmq-setup.service`, absent from the fixed mask set. Its owning
API46 module declares a boot oneshot under `multi-user.target`; architect0 owns
the bounded mask-completeness decision before implementation. The hold stayed
`held`, with no bound runner/candidate. Logs
`/tmp/storage-profile-retained-services-3175.6ka7ukno`, fixture roots
`/tmp/retained-services-roots.ayRSqk1q`. Artifact directories and stale pid files
are retained evidence, not live resources: parent confirmed all three recorded
virtiofs PIDs are dead and no QEMU/virtiofs process binds to this fixture path.
The registered cluster remains untouched; maintenance/preservation proof is pending.

Architect0 selected the bounded completeness fix: mask only
`vpsadmin-rabbitmq-setup.service`; keep maintenance record/version and mask policy
1, runtime policy 3, and existing unknown writer/trigger/activation refusals.
No deployed profile hold or selected maintenance package needs migration, and
the failed disposable hold never reached masked boot. Both actual closure unit
inventories have 365 entries with this sole unsupported unit; the augmented
command line is 967 bytes under the existing 2047-byte bound. Implementer0 owns
the two-file helper/regression correction. Focused literal-mask/inventory tests,
current-helper validation of both sealed closures and native rerun remain pending.

The two existing focused mask/inventory cases passed: 2 runs/21 assertions,
zero failures/errors/skips. The current helper then validated both exact
`3175df0` resident/candidate closures, with zero guests. Fixed launcher exit 0
in 2.119s, source/index parity retained; logs
`/tmp/storage-profile-mq-launch.9vb6wq2l/run.glff8eol`. An earlier utility stopped
before execution on failed current/cwd preflight and supplies no test evidence;
the parent reverified the binding/hashes and the fixed launcher uses matching
literal session markers with conflict refusal.
Normal maintenance-owning fold and exact-lease SSH publication created clean
`1743940f608bf3d450555f5de7f5f7188190d846`, tree
`aab4f03f3e14d9dbb463b88f378d2ad6ef192688`. Runtime commit `b108c414` contains
only the two tested deltas; profile `f6b12398` and fixture patches are identical
by range-diff, generated `da058353` unchanged. Four commits/25 paths, 5268
additions/67 deletions, binary diff SHA256
`4d240b67a8564dda20cf92716f1fc492090e0fc9505cd9f3dc6cbed25e199182`.
Backup before-rabbitmq-mask retains `3175df0`; freshly fetched master remains
`c56f981a`. Record/version/mask policy 1 and runtime policy 3 remain unchanged.
The direct completeness fix adds no new mechanism or full unaffected rereview.
Fresh Luna/low `storage_profile_native_1743` owns the actual compatible native
retry at `/tmp/storage-profile-native-1743.i0ldpjza`; source/index are held.
The watcher reports that fixed launcher preflight passed and the isolated
services guest has started; the single run remains active with no kernel-build
indicator. This is a startup milestone, not mask/copy/preservation acceptance.
Exact-head provider Check `37077660749` and API46 broad `37030949481` are
still in progress at the latest bounded metadata check.

The exact `1743940f` invocation exited 1 in 544.801s (23:29:49.249–23:38:54.051
UTC on October 2); one example failed after 331.88s in stage 4 because an
expected `Maintenance::Invalid` was not raised. Parent source/log inspection
identifies the first stage 4 assertion: it submits the original boot identity
before rebinding, which still matches the persisted old identity. The helper
checks supplied tokens; the production CLI obtains current runner/guest identity
before that call. Implementer0 owns the bounded fixture correction: submit the
newly observed identity before rebind, then prove the old identity refuses after
rebind. Architect0 is checking the existing-contract rationale. No runtime,
record/version or validation relaxation is proposed. The initial old mutation,
first masked boot with exact mask/generator/status checks, unchanged old writer
counters, partial-copy refusal and second masked boot preceded this failure;
full copied-boot/preservation acceptance remains unproved. Hold release was 0,
post-run source parity was 1, and no QEMU/virtiofs process binds to the fixture
path. Private evidence remains at `/tmp/storage-profile-native-1743.i0ldpjza`.

Architect0 confirms the supplied-token boundary; no production discrepancy was
found. The corrected existing identity test passed 1 run/19 assertions, no
failures/errors/skips, exit 0 in 1.537s with exact source/index parity; logs
`/tmp/storage-profile-identity-check.ruz8g68p`. The fixture now submits the new
identity before rebind and rejects the old one afterward. Normal maintenance
test/fixture folds and exact-lease SSH publication created clean
`5ee8281b07628de03454068e204c66367a8980dd`, tree
`8922be76e13bccc8603e21ccf020ea266bb42acd`. Four commits/25 paths, 5281 additions/
67 deletions, full binary diff SHA256
`6791baae87a35abff15bc15a65ec7d0a6fb083bddf870ad1cb0ec9ba1e2e5b0b`.
Generated `da058353` is unchanged; maintenance `683b84eb` changes only its test,
profile `455d89f5` is patch-identical, and fixture changes only the two assertions.
Backup before-fixture-identity retains `1743940f`; freshly fetched master is
still `c56f981a`. Provider Check `37077660749` succeeded at the prior head; new
exact-head `37079212058` is in progress, with no superseded live run to cancel.
This is direct correction within the reviewed contract, not a full rereview.
Fresh Luna/low `storage_profile_native_5ee` owns the actual compatible retry,
logs `/tmp/storage-profile-native-5ee.uvtsral8`; source/index are held.

The exact `5ee8281b` run exited 1 in 644.558s (23:48:43.266–23:59:27.824 UTC
on October 2), one example 437.03s, stage 6, `starting_copied`, release 0,
source parity 1. Parent inspected the actual terminal logs: QEMU could not
connect to the vpsadmin virtiofs socket, and that daemon reported its pid-file
lock unavailable. QEMU exited 1; the reported stream error is secondary. The
first copied boot reached its new-seed barrier before the forced interruption;
completed preserving seed and final projections remain unproved. No process
binds to the private fixture path after cleanup. Roots remain at
`/tmp/retained-services-roots.tUP47BfH`.
Pinned OSVM `Machine#start` enforces a five-second settle when restarting the
same instance; the fixture constructs a new instance after each stop, losing
that gap. The observed lock failure is consistent with this source-backed
timing issue, not proof of every underlying daemon detail. Architect0 accepted
the fixture-local monotonic timestamp after successful teardown and only the
remaining five-second gap before replacement start, with no initial delay.
Implementer0 owns that one-file correction and focused no-guest timing check.
Startup failures must still fail; no pid-file deletion, OSVM change or cleanup
engine is authorized. The existing native gate remains the acceptance check.
Exact `5ee8281b` provider Check `37079212058` completed successfully; this does
not replace the failed native result.

The real-main no-guest timing probe passed, exit 0 in 23.127s: five checks,
zero guests/scenario runs, startup error propagation 1 and source parity 1.
Logs `/tmp/storage-profile-settle-watch.qg93r99v`, child artifacts
`/tmp/storage-profile-settle-probe.40xjirfX/run.a6sht9rj`. The common successful
stop/kill tail is source-inspected; this probe does not prove physical reaping.
Normal fixture-only amend and exact-lease SSH publication created clean
`563c5255a5f08797640be8d9375705011bd15eb2`, tree
`011f51a9b1a403369cba6ea29c08384a0af05773`; first three commits unchanged,
four commits/25 paths, 5288 additions/67 deletions, binary diff SHA256
`ad0c274110a74229e84e1d13d441bd74935339060f8a910b5e4b88b3f20e450e`.
Only the seven-line fixture monotonic timestamp/remaining-five-second delta
changed, tested SHA256
`d1a2c7fb1f4d5c0dc46614c343d1dc48108f71365be68c9b2ed8e55ca85377f2`.
Backup before-fixture-settle retains `5ee8281b`; fetched master is unchanged
`c56f981a`. No OSVM/helper/record/public-contract change or full unaffected
rereview is claimed. Fresh native watcher runs the exact API46 app through
`/tmp/storage-profile-native-563.zugxbi_7/launch.py`; physical outcome is pending.
Exact-head provider Check `37081959992` subsequently succeeded; prior `37079212058`
succeeded and all older runs are completed. No superseded live run needs cancellation.

The exact `563c5255` native invocation exited 1 after 774.795s
(00:25:32.442–00:38:27.239 UTC), sole example 562.61s, stage 6, release 0,
source parity 1. Parent inspected terminal command order and numeric counters:
final seed Result=success, exact copied generation, complete protected SQL
projections, payload checksum, old-writer counters and retained disk identity
passed; the following two-start assertion failed with `new-seed=1`.
The first copied boot observed its seed barrier, removed the marker and
immediately forced power loss. Its counter append/removal have no explicit
flush, so loss of buffered fixture instrumentation is plausible, not established
as the sole cause. Architect0 is selecting a bounded durability correction;
no assertion weakening, runtime helper/OSVM/record change or automatic retry.
The full example remains failed, with no release/public payload acceptance.
Architect0 approved the native-only `rm .../new-seed-entered && sync -f
/var/lib/storage-profile-fixture` before the existing forced kill, keeping
`block-new-seed` present. Both append and marker deletion must be flushed;
`guest!` must propagate failure before kill and the >=2 assertion remains.
The focused real-main disposable-filesystem probe checks command/reopen/failure
behavior only; actual forced-reboot durability remains the native gate.
Logs `/tmp/storage-profile-native-563.zugxbi_7`; the guest powered off and the
watcher confirmed no path-bound QEMU/virtiofs process remains. Cached Linux
6.12.109 was used, with no local kernel compilation observed.

The guarded real-main command probe passed, exit 0 in 23.405s: three checks,
zero guests/scenario runs, two failure cases prevented kill, source parity 1.
Logs `/tmp/storage-profile-durability-watch.yjibafux`, child artifacts
`/tmp/storage-profile-durability-probe.gz1m1aVU/run._dv8m8y0`. The earlier utility
used the wrong current-session CWD and ran zero checks. Parent reverified exact
binding and all frozen hashes; its reported child-hash mismatch was not actual
drift. The fresh guarded launcher supplied matching literal markers and checked
current in the tracking directory before accessing source. No power-cut
acceptance follows from command/reopen checks alone.
Normal fixture-only amend and exact-lease SSH publication created clean
`45d7ce88fcb3a3d528f59b240c081667666526e3`, tree
`09647aa2044c0da695654038091a45d59a2236a0`; first three owners unchanged,
four commits/25 paths, 5288 additions/67 deletions, binary diff SHA256
`c6c5e3f789b93f4bef6749b82822cd04e0d8a30098476448f371759d2f7c46b7`.
Only the tested native guest-command line changed; source SHA256
`0d7ba5548a5449981978f8215769f1195147b06dc9bc7e51d4766eee2167c8d0`.
Backup before-fixture-durability retains `563c5255`; fetched master remains
`c56f981a`. Fresh native watcher uses the exact API46 app through
`/tmp/storage-profile-native-45d.g5bgua19/launch.py`; outcome remains pending.
Exact-head provider Check `37083986313` is in progress; previous `37081959992`
succeeded, all older runs completed. No superseded live workflow needs cancellation.

The exact `45d7ce88` native fixture PASSED: exit 0/802.973s
(00:55:09.744–01:08:32.717 UTC), sole example 611.85s. Summary: passed 1,
scenario_completed 1, phase_starting_copied 1, hold_released 0, examples 1,
stage 6, source parity 1. It proved the ordered real services-only masks,
zero old-writer starts, changed namespace/package preservation, interrupted
copy/receipt recovery, exact copied boots, forced seed interruption/retry,
two seed starts and unchanged protected projections/payload/disk identity.
Logs `/tmp/storage-profile-native-45d.g5bgua19`; cached Linux 6.12.109 used,
no local kernel compilation observed. Guest powered off; parent independently
found no QEMU/virtiofs process tied to this exact native artifact path.
The policy intentionally remains `starting_copied`; it cannot prove full
cluster Node refresh/public release or VPS/NAS backup payload acceptance.
Exact-head provider Check `37083986313` also succeeded. Full consumer pin,
composition review/package contract proof and external idle selection are next.

- [x] Approved profile policy: snapshots every five minutes, backups every ten
  minutes offset by two; existing VPS uses normal later rotation under unchanged
  retention, and catch-up performs no rotation.
- [x] Exact session and saved roster reverified; architect0 owns design,
  implementer0 owns application changes, reviewer0 remains independent.
- [x] Clean provider worktree registered as `vpsfree-dev-workspace-storage-profile`
  on branch `2026-09-23-storage-redesign-storage-profile`, fetched base
  `c56f981a950ab763b71dc91c59e8b5256d478851`. Superseded instruction branch retained.
  HEAD-only bare fetch initially left origin/master stale at `074926d`; explicit
  master fetch verified the actual default and the clean new branch advanced
  fast-forward before feature edits.
- [x] Final architect brief recorded; missing seeded-user namespace allocation
  is deferred to the normal post-readiness chain, and existing rows are preserved.
- [x] Scheduler support committed as `1848d41e11481eaa0fa52e64c8d7303b5d170412`:
  focused RSpec 22/0, Ruby lint 6 files/0 and Nix formatting; all normal signed
  hooks passed. Exactly nine paths. No schema/protocol change.
- [x] Common Plan support committed, normal hooks and focused checks passed.
- [x] Final Admin support whole-branch review; the Important numeric-schedule
  compatibility finding was directly corrected, checked and published.
- [x] Focused numeric-schedule verification: 8 examples/0 failures.
- [x] Normal owning-commit amend: Admin `46b3bf6f` with all hooks passing.
- [x] Provider profile, preserving seed and both acceptance fixtures implemented;
  deployment and fixture runtime results remain pending.
- [x] Canonical transition-policy prerequisite reviewed, directly remediated and
  published as `2b67af62b40149e7554bab0c31b139cd52c963c1`.
- [x] Provider maintenance boot/copy quick checks: 97 tests/1021 assertions.
- [x] Normal maintenance commit: provider `8613c8da`, clean tested tree.
- [x] Actual preserving profile seed, storage policy/helper and acceptance fixture
  source completed; runtime preservation and payload results are unproved.
- [x] First helper/seed semantic slice: provider 3/23 and all 16 real-AR cases
  covered after focused corrections; full profile integration is still pending.
- [x] Durable retirement contract: keep `enable:true`, select
  `enrollment:false`, preserve assignments and block future enrollment.
- [x] Retired selection runtime/CLI checks and full 22-example AR selection.
- [x] Actual enabled/retired Nix closure and preserving-marker evaluation.
- [ ] Real retained-boot preservation with no recreated future defaults.
- [x] Final no-VM smoke, runner build/load, app wiring and formatting.
- [x] Normal functional commits: profile `50e45ae5`, retained fixture `59f1d099`;
  exact tested trees preserved, provider clean, no declared hooks bypassed.
- [x] Independent complete-series provider review in all four HIGH-risk lanes.
- [x] Important CatchUp STI loading correction, fresh-reader regression and
  normal owning-commit fold; direct mandatory-review step 9 complete.
- [x] Required host-migration VM check on corrected provider `f36f15d7`.
- [x] Default-pin option omission/lazy-app correction, default/compatible smoke
  and flake evaluation; normal folds preserve verified bytes.
- [x] Affected general/architecture/risk review: one Important fixture root
  lifetime finding; no other Important or Blocking finding.
- [x] Direct fixture root correction, focused evaluation and normal amend.
- [x] Retained-services VM preservation/interruption proof at exact `45d7ce88`;
  one native example passed, services-only hold intentionally unreleased.
- [x] Final generated workspace pin, full consumer review and checked composed
  package with matching canonical host/tools contracts.
- [x] Rebased runtime/provider/consumer composition: focused checks, affected
  review and new composed package/contract-byte proof.
- [x] User-reported external activation; selected generation/public status verified.
- [x] Explicitly approved workspace/master fast-forward integration and publication.
- [ ] In-place update, repeat-safe catch-up, real full/incremental fixture payload
  proof, automatic cycle and retained VPS verification.

The first final no-VM Nix smoke exited 1 in seven seconds before
configuration evaluation: the two app declarations repeated the dynamic
`apps.${system}` attribute. Only the app grouping was corrected; no VM,
cluster or lock change occurred. All 18 staged hashes remained unchanged.
The wiring and formatter commands were not run after that failure. The fresh
grouped-app batch subsequently passed all three commands on unchanged runtime
bytes; log `/tmp/storage-profile-watch.CnNXmd/1-nix-run.log`. Exact elapsed times
were unavailable from the yielded watcher handles and are not inferred. Log:
`/tmp/storage-profile-smoke-20261002/command1.log`.

No profile deployment has completed. The last two provider commits contain 18 distinct final
source paths: the planned 16-path profile and 3-path retained-services inventories
share only `flake.nix`. The no-VM enabled/retired smoke, runner builds/load, app evaluation and pinned
formatting passed. Normal commits created `50e45ae5` and `59f1d099` without
changing verified bytes. At the direct-correction checkpoint, provider HEAD was
`f36f15d79f92b50fd37ead32481d7fd7bd628286`,
clean with four coherent commits on `c56f981a`. Reviewer0 completed the exact
`c56f981a..59f1d099` series in all four HIGH-risk lanes with saved GPT-6.1
Sol/xhigh/read-only settings. No Blocking findings; one Important class-loading
finding: nonempty catch-up chains persist the named CatchUp STI type, but the
class is defined only when the provisioner calls `catch_up_chain`. Fresh normal
API/supervisor/database-task readers cannot load these rows, including terminal
ones. See the [persisted STI loader lesson](../../notes/vpsfree-dev-workspace/2026-10-02-persisted-chain-sti-loading.md).
Implementer0 supplied normal enabled/retired initialization and a real
fresh-reader regression. Focused verification and the normal owning-commit
fold completed under mandatory-review step 9. Reviewer
independently confirmed coherent four-commit history, no obsolete committed
approach and no provider migrations/schema conversion. Actual VM/cluster
acceptance remains pending. The fresh Luna/low host-migration watcher passed exit 0 on exact `f36f15d7`
in 5m34s; test script and QEMU cleanup completed, no local kernel build or
owned process remained. Logs `/tmp/storage-profile-host-migration.r4JiK7`.
The retained-services VM remains pending after the default-pin CI correction. Default API/OS inputs and the provider lock
are unchanged. A fresh SSH fetch confirmed provider master remains `c56f981a`.
The first fresh-reader regression reached 1 example but failed in a child
process; generic suppressed diagnostics did not locate the failing step.
Command exit 1 in 46.729833640 seconds, RSpec 12.81 seconds; log
`/tmp/storage-profile-watch.vEQpKkov/rspec.log`. The eager-loader helper and
spec hashes remained unchanged, index empty, and no owned DB/wrapper remained.
Implementer0 added safe numeric stage/cause evidence and checked public
bootstrap behavior before the later passing focused run. This failed attempt is not
accepted as class-loading or VM proof.
Public pinned ActiveRecord 8.1.4 source and a no-DB loader probe then located
the fixture error: the child referenced `DatabaseConfigurations` before `Base`
loaded it. The resolver now uses `Base.configurations.resolve`; numeric failure
stages preserve diagnostic privacy. The fresh focused run passed 1 example/0
failures in 40 seconds, log `/tmp/storage-profile-watch.ShenILPS/full.log`.
It proves queued and terminal nonempty rows in fresh ordinary active/retired
readers, without producer calls or Node effects. Both tested hashes remained
unchanged, index empty, and no owned DB/reader process remained.
Normal pinned Git fixup/autosquash folded those exact two paths into profile
`23363e98e8db067f66bb7a2cf2bc4f740af3ebb8`; the separate VM commit is
`f36f15d79f92b50fd37ead32481d7fd7bd628286`. The first two commits and the VM
patch are identical by range-diff; only the profile patch contains the direct
fix/regression. Final clean tree `444248213740404522864493afca3408b130fb9e`,
four commits/25 paths, 5176 additions/64 deletions, binary diff SHA256
`37a86f215074cf27ea866b05e1881e49b03a8c8048b80d715bb75831619f7189`.
Backup `backup/2026-09-23-storage-redesign-provider-before-sti-fix` retains the
original reviewed `59f1d099`. No schema, public contract, chain admission or
confirmation change was introduced; no unaffected review lane was repeated.
The registered `workspace` checkout was cleanly consolidated onto current
committed master `508064ed951e5efc78131dd09d006586280d9285` through an empty
normal Nix/Git replay. Its superseded instruction/pin payload was not replayed.
Original head `3f539b0f6f034a77dd31efacb7044751237809df` is preserved at
`backup/2026-09-23-storage-redesign-workspace-instructions-before-storage-profile`.
Branch, path, registration and historical initial-base metadata are retained.
The checkout is clean; shared master/index/unrelated working changes are
untouched. Normal SSH feature publication now selects exact `f36f15d7`;
provider master remains `c56f981a`. Exact-head Check `37057284522` failed at
Nix evaluation: a disabled `mkIf false` declares the unsupported scheduler
option against default API `5c76e329`. Evidence:
`/tmp/storage-profile-provider-ci.b0U1wyHf/failed.log`. Implementer0 owns the
bounded definition correction; architect0 checks app/default compatibility.
The generated pin remains pending. The default/API46/no-build wiring batch is
owned by a fresh bound watcher after an earlier lookup-only preflight failure;
that first attempt launched no checks and is not verification evidence.
The bound default smoke later exited 1 after about 6m15s at an invalid WebUI
revision error assertion, after real disabled/default evaluation passed.
Captured stderr was discarded; diagnostic/source work precedes retry.
Commands 2/3 were unrun; source/index stayed unchanged, no kernel/VM/process
remained. Log `/tmp/storage-profile-ci-wiring.1FDsWkU9/command-1.log`.
The smoke now retains Nix stderr on a fixed invalid-input assertion mismatch.
A fresh Luna/low diagnostic built only the current wrapper and ran one
bad-revision evaluation: exit 0 in 14.009 seconds, with the actual final Nix
error matching the intended lowercase-source refusal at provider `test.nix:69`.
Evidence `/tmp/storage-profile-revision-launch-w2__mmmt/run.34_u8swz` and
`/tmp/storage-profile-revision-watch.z0PUYU`. This does not recover the earlier
discarded error or establish its cause. The five held source hashes and empty
index stayed unchanged. The full default/API46/no-build batch is now assigned
to a fresh watcher on those same bytes; no retained-services app or guest is
authorized in that batch.
The batch subsequently passed all three commands on unchanged hashes: default
smoke exit 0/6m56s, API46 profile smoke exit 0/10m40s, default flake evaluation
exit 0/11s. Logs `/tmp/storage-profile-default-compatible-eval.eueu9z`;
no kernel, QEMU or owned handle remained. Normal pinned Git folds created
profile `530c9b979e7e14d923ebb11e40e5fe48aa38cec3` and retained fixture
`4f75d0642129bf078d6852601ed602f9b4520ac8`. The first two commits are unchanged;
the final branch is clean with four commits/25 paths, tree
`6a34e39ce0023948bc399f6bff12f0bb48abdaec`, 5259 additions/67 deletions and
full binary diff SHA256
`a0248b0423c99825adfd2b4cf0676a85ba3285e39138ab09a9c28700fa38149e`.
Exactly the verified five paths differ from `f36`; all five hashes and both
STI correction hashes match. Backup
`backup/2026-09-23-storage-redesign-provider-before-ci-wiring` retains `f36`.
Reviewer0 now owns the committed affected general, architecture/repetition and
risk/compatibility review under unchanged saved Sol/xhigh/read-only settings.
The new lazy fixture contract requires this step-10 review; the original
whole-series review, scope conclusion and direct STI correction remain separate
evidence. No retained-services guest or package activation has run.
The affected review completed on exact `f36..4f75`, with no Blocking findings
and one Important issue: runtime `--no-link` builds protect neither fixed JSON
output nor its referenced closure after the Nix subprocess exits. Ordinary GC
can remove a config during the second build or native fixture. Reviewer0
confirmed option omission, captured input/follows handling and clean four-commit
history, with no new migration concern. Implementer0 owns the narrow standard
Nix-root correction: both fixed builds use private fixture-owned roots outside
the native runner's initially empty artifact directory, retained through last
use and failure diagnostics. Focused verification and normal fixture amend are
pending under mandatory-review step 9; no new runtime contract is planned.
That direct correction subsequently passed default/compatible app-path and
default no-build flake evaluation, all exit 0 in 6s/9s/9s on the sole changed
fixture file; logs `/tmp/storage-profile-root-lifetime-eval.S7rXko`. Lead source
inspection confirms standard roots are established by each fixed build and
retained outside the empty native artifact directory through execution and
diagnostics. Normal pinned amend created published provider
`eee1998c640441061ff5f6d76e379bc706ba81f6`, tree
`35fba2731f7e0da92d6cdac29196f2d9dfe8baa5`, four commits/25 paths,
5264 additions/67 deletions, binary diff SHA256
`2cab5ba43547a6188ea1f262046bdb4e96695b733e0bf5fb149182e0020685d9`.
Only that tested file differs from reviewed `4f75`; the parent profile and first
two commits remain unchanged. Backup
`backup/2026-09-23-storage-redesign-provider-before-fixture-roots` retains `4f75`.
The Important is resolved under direct step 9, with no full affected/unaffected
rerun claim. SSH publication used an exact lease against remote `f36`;
fresh master fetch remains `c56`. Exact-head Check `37067408291` completed
successfully; the old failed run is completed, so no cancellation was needed.
A fresh Luna/low watcher ran the explicit API46 retained-services app on
this clean head. It exited 1 after 7m30s, before the native scenario or any
guest boot. Logs: `/tmp/storage-profile-retained-services-watch.P9e3XA`.
The app created private Nix roots at `/tmp/retained-services-roots.3tKF8UTH`
and built the resident configuration. The enabled candidate failed while
building `vpsadmin-storage-profile-config`: `cp` could not replace `hooks.rb`.
The owning builder first copies read-only Nix-store fixture files, then tries
to overwrite the copied hooks/plans. Implementer0 owns the bounded copy-mode
correction and a focused actual-overlay realization before the next VM run.
No process remains. This is a configuration-builder defect, not seed,
preservation, registered-cluster or package-activation evidence. The correction
changes only the two overlay replacements to `cp --remove-destination`; initial
fixture copy, overlay contents, marker/selection and input pins stay unchanged.
The sole changed source hash is
`88dc4138df4359bc70b6d914bee41ba8940c9e8d7dc70f044fb16a94b379123f`.
Nix parse/format/diff checks passed. A fresh Luna/low watcher owns actual
candidate-dependency selection and realization of only the config overlay,
with file-content comparisons; no full guest build or boot in that batch. See the
[Nix overlay copy-mode lesson](../../notes/vpsfree-dev-workspace/2026-10-02-nix-config-overlay-copy-modes.md).
The focused overlay batch passed all four steps, exit 0 in 52s, logs
`/tmp/storage-profile-overlay-build.8cDI5F8c`. The actual overlay contains the
six expected files, with preserved ordinary fixture content and exact selected
profile hook/plan/helper bytes. The source SHA256 above is unchanged; the
watcher's reported `fc505ca` is the Git blob, not the SHA256.
Normal pinned Git fold created profile `3a09ebc38425a62e9dadae292a8a83adce6e7234`
and fixture `75fb840bfe6d9f12f26e953ce63c40ff06a828ce`. First two commits and
fixture patch remain identical by range-diff; only the tested two copy lines
changed. The clean four-commit tree is `b8689b5f2233f63f7da9a7579d1e4f8a528387a6`,
25 paths/5264 additions/67 deletions, binary diff SHA256
`ff81be472d637fe9f51fe48783fd6176c9047f38a9eadbff06b65cd485d3212d`.
Backup `backup/2026-09-23-storage-redesign-provider-before-overlay-copy` retains
`eee1998`. Fresh SSH master remains `c56`; exact-lease feature publication
created `75fb840`, with new Check `37069787350` subsequently successful. The previous
exact-head Check succeeded and is completed, so no cancellation was needed.
This bounded builder correction preserves the reviewed overlay contract;
no additional schema, policy, review clearance or physical outcome is claimed.
A fresh Luna/low watcher now owns the native API46 fixture retry on exact clean
`75fb840`, with a new private artifact directory and the source/index held.
That retry exited 1 after 455s (21:59:05–22:06:40 UTC), logs
`/tmp/storage-profile-retained-services-retry`. Both real configs built under
`/tmp/retained-services-roots.2UtogfhJ`; the corrected overlay build is no
longer failing. Native execution began, but no guest started: the entrypoint
created `test-runner.log` before the constructor repeated its private/empty
artifact-directory guard. Implementer0 owns the bounded initialization-order
correction in the native fixture; the guard and native framework stay intact.
Source parity passed and no process remains. This attempt gives no seed,
payload or retained-boot result. A focused no-guest bootstrap check and normal
fixture-owner fold precede another native retry.
The one-file fix constructs the fixture before opening its owned log; both
private/empty guards remain unchanged. Source SHA256
`eb7046fbf931e6d4ec0529ba7094b395653dc618affcfd6532428c3cc368f509` passed
syntax/lint and actual main-bootstrap verification in about 14s. Evidence:
`/tmp/storage-profile-native-bootstrap-launch.mhVJCD24/run.9rnfmbco` and
`/tmp/storage-profile-native-bootstrap-watch.X2CMxWSm`. The probe stopped
before the inherited run body, with zero guests and scenario_passed=0.
See the [artifact initialization lesson](../../notes/vpsfree-dev-workspace/2026-10-03-private-empty-fixture-artifacts.md).
Normal fixture-owner amend/publish created
`78ffa6f028b89af6276efa9678cdbe52f250dda9`, tree
`31066a6d271df533eb1db73c353116ff990cd0fd`, four commits/25 paths,
5265 additions/67 deletions, binary diff SHA256
`bf6e7e3fc5fc6d95379d2b28b55d16292b6351bc6b5f6231da3d165493505da2`.
First three commits are unchanged; only the tested initializer order/comment
differs from `75fb840`, retained at
`backup/2026-09-23-storage-redesign-provider-before-fixture-init`.
Fresh SSH master remains `c56`; publication used the exact old-head lease.
Exact-head provider Check `37072305045` at `78ffa6f` completed successfully.
A later utility preflight compared the native script's hash to `flake.nix`;
it ran zero checks/guests and left no handle. The lead rechecked all three
actual paths/hashes and assigned a fresh watcher with literal paths/argv/log
directory. The real retry now uses exact clean `78ffa6f`, evidence root
`/tmp/storage-profile-retained-services-78.W0DG89VX`; no runtime result yet.
The clean workspace feature subsequently
rebased normally to committed master `58df04cf`; its extra two commits are
unrelated tracking/notes only and source/procedures are unchanged. This is the
current prospective pin-change base; historical registration remains unchanged.
Package activation uses the normal installed `workspace-host switch --source`
from an external terminal after the source, review, VM and composed-package
checks are complete. The switch rebinds managed terminals before checking
idleness and visits ready sessions across registered workspaces; it cannot be
used as an active-turn idle probe. No switch, manual quiescence, delayed action
or direct provider-store bypass is executed or scheduled. After the operator
reports activation, verify the public selected package before cluster work.
The [retained rollout record](storage-profile-rollout.md) separates prepared
operator steps from future actual boot/provision/payload evidence.
Historical scheduler hook/commit
watcher returned exit 0 after 53 seconds, log
`/tmp/storage-profile-scheduler-hooks.Xn2wjtmM/output.log`. TextWidth gave a
72-column advisory; the reviewed message meets the workspace's 80-column rule.
Scheduler verification logs: `/tmp/storage-profile-scheduler-check.XAVcqHHF`.
Fresh Luna/low watcher ran the held snapshot, then reported disposable DB cleanup
and no remaining process. No kernel build occurred. Scheduler documentation was
checked against the source and plain writing rules; no prose correction needed.
Saved member settings remain unchanged; the fresh verification utility uses current installed
catalog `4676433c` GPT-6 Luna/low and one-operation lifetime.
Common Plan support was verified as a seven-path draft on `1848d41e`; legacy plans
retain their first-open backup destination behavior, while the keep-empty
profile requires an exact sole destination. Previous attempts ran zero examples: one watcher used
incorrect relative preflight locations; the next test database hit the known
107-byte socket limit beneath a Nix-nested temporary path. Required guidance
exists and identity was reverified. The corrected command sets a short private
`TMPDIR` inside `nix ... -c`; no surviving prior MariaDB process was found.
See [the reusable socket lesson](../../notes/vpsadmin/2026-07-31-test-db-socket-path-length.md).
The corrected batch reached the Plan examples: 57 examples, 47 failures from
an unqualified Scheduler constant in the owning Plan namespace. Implementer
changed that one reference to `::VpsAdmin::Scheduler::CronTask`. The fresh
three-file rerun reached 57 examples with 56 passing and one fixture failure:
the spec attempted a duplicate GroupSnapshot that the real unique index rejects
before its expectation. Only that fixture was corrected to check the constraint
and the schema-possible ambiguous environment case; runtime bytes are unchanged.
The fresh narrow example at line 245 passed 1/0 in 46 seconds, completing
verification of the 57-example selection; seven held hashes remained unchanged,
the index stayed empty and the disposable DB stopped. Normal Plan hooks passed
and created `96ab16726b516ee601b3f366439f1079a1030d19`, exactly seven paths;
all committed blobs match tested bytes. No loader, schema or larger runtime
change was added for the fixture. Logs:
`/tmp/storage-profile-prereq-check.SCWrBf71/admin.log` and
`/tmp/storage-plan-namespace-check.ckLoxIBo/rspec.log` and
`/tmp/storage-plan-fixture-check.wsS3tA3K/rspec.log`.
Normal Plan hook evidence: `/tmp/storage-plan-normal-commit.G24Zov6t/output.log`.
Nixfmt, MigrationSpecs, both i18n hooks and RuboCop passed. Two existing lint
disable comments moved around unchanged statements; no extra runtime edit.
The permitted 80-column message passed hooks with advisory 60/72-column warnings.
Its nonempty private hook temporary directory was retained, with no MariaDB left.
Before review, SSH default fetch found only two new PHP dependency files at
`878a0d10c86060ed2ce62027223832371ca5e49e`. Normal signed replay of all 21
commits created `2323829cc79d2d64661825d2f8f9e170ceb98170`. All 21 range-diff
entries, complete messages, 202 feature blobs, both migrations/schema and
base-to-head binary patch remain identical. Backup `96ab1672` is retained.
Focused PHP after dependency replay passed 5 tests/17 assertions; index/tracked
tree clean, PHPUnit cache preserved. Evidence:
`/tmp/storage-admin-default-refresh.Dqw9aj2I`.
The complete Admin series and consumed migrations are inventoried for the
independent HIGH-risk four-lane [support review](storage-profile-admin-review.md).
Reviewer0 completed all four lanes on `878a0d10..2323829c`, with no Blocking
findings and one Important compatibility finding: validated integer schedule
arguments were compared against persisted strings, blocking valid numeric DSL
reuse/removal. The implementer supplied a one-expression string normalization
and four real-DB numeric group/backup regressions for legacy and retained plans.
The three-file remediation passed its eight focused real-DB examples in 45
seconds, with held hashes unchanged. Log:
`/tmp/storage-numeric-plan-bound-check.d8GL3Zsh/rspec.log`. The watcher verified
no MariaDB remained and removed its empty short temporary directory. The status
helper printed that the DB was stopped, then raised a standalone NameError;
the actual RSpec exit was 0. A prior watcher used the parent tracking directory
by mistake and ran no examples; the bound retry used the exact session path.
Normal Nix sign/amend completed as `46b3bf6f9549eaf579053bc296ebf19c417bb848`;
all pre-commit hooks passed, with only permitted message-width advisories.
The parent and first twenty commits are unchanged; the old reviewed head to
new head diff contains exactly the tested three paths. The owning Plan commit
still has seven paths, the series still has 21 commits, and migrations/schema
remain unchanged. Log: `/tmp/storage-numeric-plan-amend.GFNTMieF/amend.log`.
The nonempty private hook temporary directory was retained; the DB reported
stopped. Backup of reviewed `2323829c` is retained. Direct step-9 remediation
is complete; no new contract or unaffected review rerun was introduced.
The exact final Admin `46b3bf6f` was SSH-published with an explicit lease on the
previous remote feature `e65a5a6b`; `ls-remote` confirms it. Default `878a0d10`
remains unchanged. This is feature publication, not integration or deployment.
Nine exact-head workflows have started or queued, led by API topics
`37030949457` and broad CI `37030949481`. The previous e65 workflows are now
all successful, including broad CI `36925295149`; these are historical results,
not exact-head acceptance. No superseded queued/running job remained to cancel.
Latest watcher observation: seven successful workflows, API topics still running
and broad CI queued. Monitoring was released for the local profile checks;
GitHub runs continue, with no cancellations or local monitor left running.
A later bounded metadata read confirmed exact-head API topics
`37030949457` completed successfully: all 27 jobs, including full-platform and
topic coverage, passed. A later bounded metadata read reports broad CI
`37030949481` in progress, updated `2026-10-02T19:10:57Z`, still at exact
`46b3bf6f`. Its conclusion is pending; there is no active local CI watcher.
The complete 21-commit history and two
consumed migrations were independently checked and have no history/schema
finding. Direct remediation follows mandatory-review step 9; unchanged lanes
do not need another review merely to confirm normalization.
No source-test result is inferred from the earlier startup failures.
The generic prerequisite passed 40 runs/244 assertions with its required
suspension-test fixture loader. Normal Nix commit created
`8b2439938cbcbe527f2c703d88ed3c9f72f44b7e`, exactly three paths and no migrations;
the tree is clean. No hook framework or active non-sample hook is declared.
Reviewer0 (saved GPT-6.1 Sol/xhigh/read-only) completed the full branch review
in all four HIGH-risk lanes under [the exact packet](storage-profile-runtime-review.md).
No Blocking or Important findings; one general/risk Advisory identifies the
preexisting refusal message that suggests resetting retained clusters. Lead
assigned and directly verified a narrow wording correction to preserve state
and select a reviewed compatible package. Its focused real transition test passed
1 run/26 assertions. Enforcement stays unchanged; no unaffected review lane was
repeated. The
review explicitly concludes one coherent commit, no obsolete history and no
migrations. Normal amend created final `2b67af62b40149e7554bab0c31b139cd52c963c1`:
one commit/four paths, with only the message and two assertions added to reviewed
`8b243993`. SSH fetch confirms default `4bec2016` is unchanged; the exact final
feature SHA was published and confirmed with `ls-remote`. The generated provider
runtime input update is released, separate from its maintenance implementation.
No package activation or default-branch integration occurred.
The provider's generated runtime pin is committed as
`da058353ac4a43f08313d02b485c1578f3547378`, exactly `flake.nix`/`flake.lock`.
Only four dev-workspace revision/hash/time/original-revision leaves changed;
all other lock nodes are identical. `nix develop` was refused because this
provider exports no development shell/default package. The normal commit then
used its pinned `nix shell --inputs-from . nixpkgs#git` environment without a
hook bypass. Maintenance drafts remain separate; flake source is released for
their test registration. No provider publication or activation has occurred.
The provider's evaluated canonical runtime export is schema 1/policy 3 and
matches the published generic source byte-for-byte (SHA256
`33acdc50fa6b7ed94f84d1f7f1db0af8d76d7d57d2e721cbb6a204a96b27c0d1`).
This verifies the input export, not the assembled host/tools package or activation.
Before its commit, the maintenance prerequisite was a held ten-file draft on `da058353`:
typed boot/copy/restart, private immutable evidence/hold/receipt, fixed masks,
per-machine retained-disk checks and adoption validation. A fresh Luna/low
watcher ran the four separate Ruby suites plus pinned Nix formatting.
Its first attempt ran zero examples because a user-installed Minitest 6.0.6
shadowed pinned Ruby's bundled 5.25.4 and lacked `minitest/mock`; formatting
passed. The source-backed loader correction selects `Gem.default_dir` for both
GEM_HOME/GEM_PATH and unsets RUBYOPT. A new watcher using that isolated
environment on identical held hashes reached 13 tests/105 assertions with one
error: the JSON duplicate-key parser subclass rejected a legitimate phase
assignment in copied startup. The remaining three suites did not run. The
implementer corrected that parser/update boundary and documented bundled gem
isolation; exact shape/digest/phase checks remain. The fresh four-process run
passed in 392 seconds: maintenance 13/112, runner 10/27, commands 23/295 and
status 51/587, with no failures/errors/skips. The command suite accounted for
319 seconds; no timeout or retry was used. All ten corrected hashes matched
before/after. Log: `/tmp/storage-maintenance-parser-check.TlJqs6sb/tests.log`.
Normal pinned-shell Git commit created
`8613c8da74677ff3110f1775ca1ebd530d77ad5e`, exactly ten tested paths, with a
clean tree/index and matching hashes. No hook framework is declared or bypassed.
Implementer0 is released for actual enabled profile implementation from this
head. Fresh SSH fetch confirms provider default c56 and Admin default 878
are unchanged; the remote Admin feature was still e65 at this checkpoint.
Final whole-provider review includes all intended source before the VM gate;
there is no extra review delay between these two implementation slices. See the
[provider shell lesson](../../notes/vpsfree-dev-workspace/2026-10-02-checks-without-development-shell.md).
The [provider review preparation](storage-profile-provider-review.md) records
the two committed prerequisites and remaining profile checks. It is not yet a
review assignment; final source inventory and quick results remain pending.
No preserving marker is emitted yet: actual enabled seed preservation and the
storage policy remain the next implementation slice. Unit fixtures alone do
not establish guest masking, preservation or populated-cluster readiness.
Approved profile ownership includes the Nix selection/overlay, shared API helper,
hooks/plans, post-ready provision/retire entrypoint, actual-seed preservation
tests and dedicated full/incremental payload fixture. Pre-API setup never waits
for Node work; Pool-dependent templates are established after real Pool::Create
and before enrollment. Implementer0 owns these application paths; architect0
keeps design conformance, and the lead owns subsequent checks and operations.
The first nine-file helper/overlay/seed snapshot is held for a fresh Luna/low
provider test and real-AR API check. Manifest:
`/tmp/storage-profile-helper-first.sha256`, SHA256
`9dc728fcded46ce52535856c8e435f1b8bed36a9b8f237957d72cbdd1e94b7d7`.
Local syntax, shell/Nix parsing, scoped whitespace and targeted Ruby lint passed.
Provider quick checks passed 3 tests/23 assertions. The API command ran zero
examples: API `.rspec` preloaded spec_helper, whose automatic disposable DB
set DATABASE_URL before the provider spec's second inherited-DB guard. That
guard rejected the newly created test database. Log:
`/tmp/storage-profile-helper-check.8HIFQUFi/check2.log`; DB teardown completed.
The [provider API harness lesson](../../notes/vpsfree-dev-workspace/2026-10-02-api-harness-rspec-preload.md)
records the custom-options correction and retained database preflight.
The lead released the hold for a narrow loader-order correction that retains
pre-schema refusal of inherited/configured databases. The 15-example semantic
selection remains unverified. Remaining provision/CLI/smoke and acceptance-fixture
source is still in development. The loader-order fix changed only the runner;
the next check reached all 15 examples (9 pass, 6 fail). Source inspection
identified a real NAS selector error (`parent_id` SQL on the ancestry model)
and spec queries treating transactions as STI instead of using their `handle`.
Log: `/tmp/storage-profile-helper-rerun.6omq4vXB/run.log`. All nine hashes
matched and the disposable DB stopped. Implementer0 is correcting those queries
without a schema change. The static future-default bootstrap must also work
under retained read_only: its metadata-only admission check is being removed,
with a regression for unchanged freeze/assignments/physical enrollment. All
physical/template/Plan/provision admission remains required.
The corrected nine-path slice is held under
`/tmp/storage-profile-helper-roots-freeze.sha256`, SHA256
`76e46e50bb4e731611fdd7ca0071ba78b19b23035e93a91f8ac023f86f682a9e`.
Only helper/spec differ from the preceding held snapshot; syntax and targeted
lint passed. The fresh 16-example run completed with 15 passing and one failure
in the frozen-bootstrap conflicting-policy refusal. Its Environment changes
survived a caught exception because the configuration transaction joined the
RSpec outer transaction. Log:
`/tmp/storage-profile-roots-freeze-check.NdhrO0mq/api-specs.log`; held hashes
matched, API stayed clean and the run/DB stopped. Implementer0 is adding the
owned savepoint for atomic refusal; protected-row assertions stay intact.
Only the affected default/bootstrap examples need focused verification next.
That focused check passed both examples (2/0, 30 seconds), with all nine held
hashes matching. Manifest:
`/tmp/storage-profile-helper-atomic-defaults.sha256`, SHA256
`cf3122da7ce422a672084b3d161698d3453eb04ede4e2dc977b8b91a29fdd56b`.
Log: `/tmp/storage-profile-atomic-check.0WnkJgKi/run.log`. The command tree
ended and the API tree stayed clean; the log has no separate teardown line.
The previous 15 passing cases plus these two affected cases cover the current
16-example slice; this is not a claim of one fresh 16/0 run. The hold is released
for implementer0 to finish provision/CLI/smoke and both acceptance fixtures.
Parent read-only hygiene check found no MariaDB process tied to any
`/tmp/vp-profile.*` directory and four empty short temp directories; no cleanup
or private database inspection was needed.
Architect0 recorded the enduring retirement contract in design.md; implementer0
is implementing it within the approved profile slice. `storageProfile.enrollment`
is a boolean, default true. The retired selection keeps `enable:true` and sets
`enrollment:false`, retaining the preserving seed, marker and Plan definition.
The false static branch removes only the exact owned future default-package
link under the Environment savepoint/lock; it creates no package/default and
rewrites no Environment permissions or existing assignments. Hooks skip new
enrollment, explicit provision/catch-up/templates and direct Plan add/verify
refuse, while normal unregister remains available. Retirement requires false
in the CLI and loaded helper, including desired/effective boolean agreement
after normal services-generation replacement. Existing owned rows mean pending
retirement; atomic removal under ordinary admission/Plan locks establishes the
retired state. Failure keeps scheduling stopped and the remaining rows intact
for retry. Future false boots must not recreate defaults or enrollments.
No persisted retirement engine or disabled legacy-seed boot is introduced;
the new behavior and focused regressions remain unverified implementation work.
Implementer0 handed over a held 13-path retirement/provisioning snapshot at
provider `8613c8da`; its manifest is `/tmp/storage-profile-retirement.sha256`,
SHA256 `546007a47efd041cf4c276902dab5c97cc841e3fc8b751a1f641f018f86f8117`.
The first watcher passed the pure configuration tests (4/32), then its six
selected CLI cases failed before profile execution because the lead brief
omitted `DEVCLUSTER_RUNTIME_CONTRACT`. API examples were not run in that attempt.
Log: `/tmp/storage-profile-retirement-check.1xpUmCZ4/check1.log`.
The held source stayed unchanged. A fresh Luna/low watcher is running the same
checks with the canonical published generic contract and fixture defaults,
followed by the 22-example disposable API database selection. This is an
environment correction, not an application fix. CI monitor-only utility was
released again; broad run `37030949481` remains unchanged, with no local monitor.
The corrected environment passed provider 4/32 and six CLI cases/71 assertions
in 47 seconds. Its API invocation mistakenly included an extra `.` argument,
selecting the whole API directory rather than 22 provider examples. After
the watcher reported that expanded scope, the lead explicitly stopped only
the owned RSpec run. Wrapper exit 143 at 451 seconds; its disposable MariaDB
and wrapper exited, hashes remained unchanged, and unrelated processes were
untouched. Log: `/tmp/storage-profile-retirement-env.9hcO4D3l/command2.log`.
The expanded suite's failures are not accepted profile verification. This was
an invocation error from ambiguous command punctuation in the lead brief,
not a demonstrated harness/source defect. A fresh watcher now uses an exact
six-element argument vector with no trailing `.` to run only the provider
file. Provider pure/CLI passes stand; no repeat of those checks is needed.
The exact bounded argument-vector retry passed 22 examples/0 failures in
61.948 seconds on API `46b3bf6f`. Log:
`/tmp/storage-profile-retirement-api.odsx_28j/run.log`. All 13 held hashes
matched; the API tree remained clean apart from its existing PHPUnit cache,
and the owned run/disposable DB ended. Together with provider 4/32 and CLI
6/71, this verifies the current semantic retirement/provisioning slice.
The lead released semantic/flake holds for final fixture, documentation and
Nix-smoke preparation. Actual enabled/retired Nix evaluation, final provider
review and guest/payload trials remain pending; these AR cases do not prove
real boot-time preservation or worker replacement.
Implementer0 then added a narrow retirement ownership guard: remaining shared
templates must belong to the exact configured source/NAS pools. The focused
regression reached one example but failed during fixture setup because it used
`day` instead of the persisted `day_of_month` task column (31 seconds, exit 1).
Log: `/tmp/storage-profile-api-watch.rRFb3q/run.log`. Both held hashes and
repository heads/indexes stayed unchanged, and the disposable DB ended.
The guard remains unverified until the corrected fixture reaches its atomic
refusal assertion; the earlier 22-example result remains separate evidence.
After changing only the fixture's task columns, the exact affected example
passed 1/0 in 46 seconds. Log: `/tmp/storage-profile-api-spec.J0TZ8R/run.log`.
Helper `6c039b21…` and corrected spec `8cf172db…` matched before/after;
the index stayed empty and the disposable DB ended. The runtime ownership
guard and atomic refusal are now verified alongside the earlier 22 passing
cases. A prior retry ran no tests because the watcher could not locate a bare
`dev-session` command; the bound retry used `/home/aither/bin/dev-session`.
The hold is released for fixture/README/Nix-smoke completion.
Fresh stable-helper preflight reports the owned cluster stopped, with stale
readiness; services SSH returns No route to host. Retained disks/config and
result-config remain. A supported retained-disk start is needed after source
review; do not infer the prior running state or reset the populated cluster.
Architect source inspection found the old seed/closure gap: a normal old boot
can rewrite allocations, while a new host closure is not automatically copied
into the retained guest store. Lead selected a bounded reviewed maintenance
boot/copy-only prerequisite before any populated-cluster boot. It holds writers
from initial boot, permits DB inspection/backup and copies the new closure;
normal startup follows with the preserving seed. No such operation has run.
The stopped cluster's private cold recovery copy completed at
`/tmp/storage-profile-cold-recovery-20261002.9b7dxg0i`: six disk sizes match,
source inode/size/mtime/ctime stayed unchanged, copy exit 0, no visible disk
writers. Read-only `debugfs` on the copy extracted the recorded old services
`init` and its exact systemd 260.4 debug generator; both byte hashes match the
host store files. The selected generator directory exists and is empty, so
no override was found there. This corroborates the prior activated-generation
record; it is not a recursive closure check or permission to boot. The raw
ext4 image reports journal recovery needed. No mount, repair, journal replay
or write to the retained source disks occurred. Reviewed maintenance support
and its disposable regression remain required before the actual boot.
Lead prepared the required version-1 residency evidence at
`/tmp/storage-profile-cold-recovery-20261002.9b7dxg0i/residency-evidence.json`:
669 bytes, mode 0600, exact config-byte digest and selected services toplevel,
with a reference to the prior activation record and cold-copy proof. Source
disk metadata was rechecked unchanged. This trusted operator reference does not
replace the later full-closure and masked-boot checks.
The compatibility check found that policy-2 providers ignore a new hold record
on an ordinary package switch. The lead selected canonical policy 3 with schema
1 unchanged, in new clean `dev-workspace-maintenance-policy` worktree/branch
`2026-09-23-storage-redesign-maintenance-policy`, fetched default
`4bec20165387d567b761e43b11fdeabb096618d7`. The architect brief is ready and
the policy-only commit passed focused checks and independent review. This intentionally
refuses ordinary package downgrade while
cluster state exists. Ordinary rollback is already disabled; old candidate
recovery entry points are outside the supported procedure, not universally
blocked by code they do not contain. Existing integrated instructions remain
untouched.
The shared storage1 disk is about 20 GiB: logical backup copies do not provide
independent fault protection. New source retention 2/3 and backup 2/5 are rotation
targets, not hard usage limits. Existing migrations/protocols and advisory
strict/quiet/repair/APPLY boundaries remain unchanged. Full brief is in
[design.md](design.md). The initial initiative plan/state are already committed;
working updates follow the daily checkpoint cadence.

## Completed rebase and React deployment

Historical 2026-10-02 checkpoint: requested rebase and dev-cluster redeploy verified. The user
requested rebasing the storage work onto current default branches and adding
the separate React vpsadmin-webui component to the retained dev cluster.

- [x] Session binding and ready roster verified; architect0 owns the design
  and verification brief, implementer0 owns application edits.
- [x] Defaults fetched: vpsAdmin `90184b374`, vpsAdminOS staging `26f28c691`,
  site configuration `029c616e`, React WebUI main `aa2f60b8`.
- [x] Architect brief accepted in [design.md](design.md); the installed provider
  already owns the React/BFF integration. Old source refs and private cluster
  configuration/provenance are backed up.
- [x] Rebase source branches; preserve deployed migration versions and complete
  provider checks, whole-branch review and feature publication.
- [x] Verify/review final vpsAdmin pin and complete whole-branch history/schema review.
- [x] Publish final vpsAdmin and regenerate/review the configuration pin.
- [x] Rebuild/redeploy the fresh bridge/storage cluster and verify React/BFF,
  API, legacy PHP storage controls and Node services.
- [x] Complete the compact browser acceptance: 242 checks, both PHP mode
  changes, epoch 2 to 4, exactly two new audits, no fallback recovery.
- [ ] Resolve broader CI and separately approved future maintenance/repair
  work. No merge or production operation is authorized.

At that checkpoint the cluster was running and available for development. Real React login, API
access and logout passed under trusted TLS. PHP freeze/unfreeze, administrator
authority, stale/same-mode CAS and frozen write rejection passed. Independent
guest SQL confirms `read_write` epoch 4, four total audits, singleton row 1 and
both migrations. The earlier PHP unfreeze attempt remains unexplained; its
failed evidence is retained, and no application fix is claimed. The final
diagnostic run passed without changing form timing or assertions. Broad CI and
the unrelated upstream React nightly failures remain recorded limitations.

The consolidated tracking checkpoint is `52fa4313060929567557a0f236ff69153f21b2b2`.
Reviewer0 (saved GPT-6.1 Sol/xhigh, read-only) completed its documentation-only
GENERAL review with no findings. This covers the ten committed tracking/note
paths and their consistency, authority limits and provenance; it does not
replace the completed source reviews or independently rerun private runtime
checks. This clearance is recorded in the working state under the normal
daily cadence, without another same-day tracking commit.

The user explicitly authorized resetting this cluster, noting no personal
changes. The supported reset/config helpers completed for this exact cluster;
its fresh private configuration enables React and a dedicated disposable admin.
The selected rollout is a clean rebuild after rebase and review;
existing test records and branch backups are retained. The legacy PHP UI remains owned by vpsAdmin;
React is an additional component, not a path extraction. No React storage
freeze feature is in this request. Superseded instruction-only branches stay
retained and are excluded. Default-branch integration, shared-host deployment,
production strict, repair readiness and APPLY are not authorized.

The saved implementer and reviewer settings now resolve to GPT-6.1 Sol/xhigh;
architect0 remains GPT-6 Astra/xhigh. Earlier settings below are historical.

Initial rebases are clean: vpsAdmin `eade85a5` retained all nineteen patch entries
and all 189 feature-path blobs exactly; the two consumed migration blobs and
generated schema match `fa7cec3`. OS `8d05dc3a` is one provider commit on current
staging, fourteen unchanged provider blobs plus the additive test registration.
Configuration guide-only `603da36e` is on current master, with the obsolete
service pin removed pending regeneration. React is clean at default `aa2f60b`.
The provider focused specs passed 36/0 and normal Nix hooks passed. The rebased
API focused checks passed 62/0, Node 42/0, PHP 5 tests/17 assertions, and selector
18 runs/77 assertions. Reviewer0 (saved GPT-6.1 Sol/xhigh, read-only) cleared all
four HIGH-risk lanes for the complete OS range `26f28c691..8d05dc3ae`, with no
findings and an explicit one-commit/no-migrations conclusion. Publication and
the single generated replacement Admin/config pins precede final review and
deployment. These first Admin checks still used the old internal OS pin;
final-pin checks remain required. The old provider pin was dropped at `0bdd6caaa`
with all eighteen retained patches/messages equivalent. Normal generated updater
committed final vpsAdmin `e65a5a6b0` with one current-provider pin. Architect
conformance found no blocker: its two transitive nixpkgs lock changes exactly
match OS `8d05`; migration/bootstrap/signing/advisory behavior is unchanged.
Final-pin checks passed: migration processes 4+2+2/0, API 74/0, Node 42/0,
and all normal Admin hooks. Reviewer0 cleared the complete nineteen-commit
range `90184b374..e65a5a6b0` in all four HIGH-risk lanes, with no Blocking or
Important findings and explicit migration/history conclusions. One documentation
advisory is accepted for this redeploy: integrity-foundation.md incorrectly
describes copied identity owner IDs. Identity ownership actually uses RESTRICT
FKs; copied metadata belongs to scopes/targets. Runtime behavior is correct and
identity publication remains off; no schema or runtime change is warranted.
Exact-head broad CI and fresh runtime acceptance remain pending.

Admin `e65a5a6b0` is now published and SSH-fetchable. Required confctl generation
created configuration `5eff558c4`: guide `603da36e` plus one generated service
pin. Only the service locked triple changes; site OS/React/production/follows
remain unchanged. Normal full configuration hooks and thirteen-channel
evaluation passed. Reviewer0 cleared the complete two-commit branch in all
four HIGH-risk lanes, with no findings and an explicit no-migrations/history
conclusion. Its separate site provider/follows and full consumer inventory
limits remain; no shared host is deployed by this pin.
Configuration `5eff558c4` is also published and independently SSH-verified.
The exact owned bridge/storage build booted all guests but start returned 1
because ordinary seeding did not complete. Guest database setup successfully
loaded schema/bootstrap/migrations, then the lead-added disposable admin seed
failed with a missing required namespace allocation. The lead corrected only
that private cluster configuration, after verifying unused blocks. The normal
services recovery update passed, including node refresh (about 7.5 minutes).
This is a
configuration omission, not a demonstrated migration/source defect. No reset,
manual DB seed or bypass of React startup dependencies is used. Runtime
acceptance remains pending. A disposable admin password exposed during a
member's generated-seed inspection has been replaced privately; its normal
services application also passed. No credential value belongs in these records.
All services and seeds are healthy; all three selected Node generations match
and the actual osctld v1 `gc_trash_v1` provider responds correctly. Activated
nginx/BFF paths and strict-TLS served build-info match the selected pair, with
their supported unknown embedded revision reported honestly. A private DB
backup preceded the trial. React real login/API read/logout/anonymous 401 passed;
the first attempt stopped before PHP or any freeze because the private helper
incorrectly version-prefixed the token-auth URL. Actual OPTIONS advertised the
versionless path and a short direct probe returned 200. The corrected retry
passed PHP login/status/freeze, stale and same-mode CAS 409, anonymous 401,
member 403 and valid Pool Create refusal 423 with unchanged data rows. It failed
at the PHP unfreeze path without enough step evidence; its normal owner-bound
API recovery restored read_write epoch 2 with two audits. This recovery is not
accepted as PHP-unfreeze verification. Implementer0 added numeric UI-step
diagnostics, preserving the failed evidence before any edit. The resulting
fresh Luna/low trial passed all 242 checks, including actual PHP unfreeze
(change POST 302), epoch 2 to 4 and audit delta 2, without recovery. The prior
failure was not reproduced or explained; no deployed application change was
made. Detailed executed evidence is in the rollout record.
Admin exact-head migrations, Node, PHP, lint, clients, i18n and the 5215 contract
CI passed; the exact-head API topic workflow also finished successfully, with
all 27 jobs green. Broad Admin/OS CI remains queued. No superseded
same-branch live runs remained. Browser dependency setup is ready: NSS uses the
multi-output `-tools` GC root, and host Chromium subprocess/version checks pass.

The existing path-input integration may record unknown/dirty/unavailable inside
both React package build-info files. That is a supported, honest development
form, separate from the clean selected Git SHA. Acceptance verifies matching
package metadata, selected source/tree and output paths rather than relabeling
unknown metadata as a clean release. No provenance feature is added.

The shared frontend address was occupied by the dev cluster from
`2026-09-30-portal-review-improvements`. The user explicitly requested releasing
that session's addresses. The authorized action is stopping that exact dev
cluster through the supported helper, monitored by a fresh Luna/low utility;
it does not authorize archiving or changing that session's records/team.
The bound utility completed the stable stop with exit 0 (about 20 seconds);
the shared frontend address is rechecked before our cluster starts.

2026-09-27 coordination-policy reconciliation: workspace `master`
`74f830c7` and vpsfree-dev-workspace `master` `bd961682` already provide the
updated architect design brief, lead progress and whole-branch review rules,
and current team defaults. The installed mandatory-review skill is byte-for-byte
the extension's current master version; the workspace package pins that master
revision. This session's older instruction-only feature heads, workspace
`3f539b0` and extension `dcb2762`, are superseded release candidates. Their
clean worktrees and branch refs are retained for provenance; do not merge or
repin them. No branch was deleted or rewritten.

The verified session roster retains its saved settings and prompts:
`architect0` is Astra/xhigh with workspace write access, `implementer0` is
Sol/xhigh with workspace write access, and `reviewer0` is Sol/xhigh and
read-only. The new defaults did not migrate those members. Future assignments
must give the architect the design and verification brief explicitly and keep
application edits with the implementer. This instruction reconciliation made
no vpsAdmin, cluster or production change. The active storage phase remains
G1a advisory diagnosis; maintenance exclusion and executable repair remain
future work.

2026-09-26 G1a checkpoint: the registered vpsAdmin feature branch is clean
and published at reviewed `fa7cec3a89e433e91516a369f10b1b17b6eddfef`.
Nine focused commits since `fe4f9b0f9` now bound current diagnosis capture,
keep lifetime terminal history explicitly unknown, restore pooled MariaDB
isolation, and use the existing transient RabbitMQ node exchange for signed
5290 inventory. The independently reviewed final nine-commit series has no
Blocking or Important finding. Focused API/Node specs and normal hooks passed;
exact-head API Specs and broad CI are still in progress under a dedicated
watcher. The site configuration feature remains pinned to older `fe4f9b0f9`;
no shared or production host was switched.

The disposable bridge/storage cluster was updated to `fa7cec3` under
`read_only` epoch 3. A real signed 5291 activity report completed two signed
5290 captures and returned the expected `sampled_incomplete` result because
child lifetime is unproved. Both source `(2,2)` manifests sealed complete
diagnostic captures; fresh offline compare, dry-run and plan produced six
nonexecutable candidates, each blocked by unknown historical terminal
coverage. Services and nodes were healthy, and authenticated CAS restored
`read_write` epoch 4 with one audited transition. The detailed executed trial,
failure/recovery sequence and private evidence locations are in
[g1a-dev-cluster-trial.md](g1a-dev-cluster-trial.md). This did not enable
node quiet, repair readiness, strict production dispatch or APPLY.

The 40k-object scale result covers a graph without retained locks. A global
retained-lock fan-out case, including unrelated nodes, remains unmeasured and
could make diagnosis fail incomplete under the statement timeout. The G1b
manual maintenance exclusion and API owner interlock remain unimplemented.
The queue-ledger capacity issue was resolved in its separate session; it no
longer blocks retained team review. The older chronology below is preserved
as history, including checkpoints that were pending when written.

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

Current 2026-10-05 sequence; the remote-restore integration and Admin feature
publication are already complete. Workspace/provider activation and approved
default integrations are also complete. No further workspace switch is planned.

1. Validate fresh stopped hold/disk/provenance evidence, then use the installed
   public metadata recovery command and copied boot. Prove every guest's actual
   selected closure, seed/API/Supervisor and Node refresh before hold release.
2. Prove delivered guest scripts and compare original DB, file and quota
   evidence. Complete public profile provision through ordinary Pool/CatchUp
   chains while preserving existing allocations and retention.
3. Run the existing VPS/NAS full/incremental payload/history, rotation,
   automatic scheduling and repeat update/provision acceptance; then prove
   retirement, repeat/nonreactivation and re-enrollment with data preserved.
4. Diagnose the two API request-500 test failures in the separately saved,
   held test-only scope. Their underlying exceptions remain unknown; neither
   an unchanged CI rerun nor a runtime patch is justified by current evidence.

### Overall redesign remaining work

The storage application foundation, bounded advisory capture/offline analysis
and Node RPC correction are implemented and reviewed. Their recorded local,
disposable integration and browser checks retain their exact scope. The live
G0 freeze trial remains partial; the G1a trial passed diagnostic collection,
not executable repair. After the retained profile acceptance above:

- Finish remaining live freeze/authorization/race cases and populated retained-
  lock capture performance plus pooled-session failure/restoration coverage.
- Implement G1b's held physical writer exclusion and API maintenance owner.
  The development-cluster maintenance hold is not that storage repair gate.
- Implement G2's exact approval, bounded DB-only action journal, crash recovery
  and final same-engine verification; rehearse repair/resumption under G3.
- Complete Milestone B's writer-family coverage, authoritative physical
  identities/origins and strict continuous verification as a separate stage.
- Refresh branch readiness/review and compatibility/rollout evidence before
  requesting storage-project default integration. Production deployment and a
  repair maintenance window remain separately approved operations.

The current cluster is stopped with its hold intact. Original disks/cold copies
and baselines are retained, but post-recovery equality is still unproved.
Production strict dispatch, physical quiet/repair-ready claims and APPLY remain
unavailable. Session lifecycle remains active.

### Earlier redesign sequence, retained as history

1. Keep the rebuilt cluster running for development. The requested rebase and
   compact runtime acceptance are complete at Admin `e65a5a6b0`, OS `8d05dc3ae`
   and React `aa2f60b8`; final configuration `5eff558c4` is published. Exact-head
   API topic CI passed all 27 jobs. Broader Admin/OS CI remains queued; inspect
   any later failures against the exact heads before accepting them.
2. Benchmark a populated global retained-lock cohort, including unrelated
   nodes, before live diagnostic use. Keep query timeout failures incomplete;
   do not infer performance from the lock-free 40k-object case. Add focused
   pooled-session failure/restore tests before wider rollout.
3. Implement and review G1b's active freeze owner, manual storage-only
   maintenance generation and isolated signed inventory runner. Prove stopped
   daemon and child/delegated-work exclusion in a disposable VM before any
   `node_quiet` or repair-ready claim.
4. Keep the reconciler advisory until one-engine approval, bounded DB-only
   apply, crash resume and final verification are implemented and reviewed.
   Do not use two inventory passes or 5291 observation as an apply gate.
5. The current-staging provider port and final service pin are reviewed and
   published. A later shared rollout still needs actual consumer builds and a
   separately reviewed site OS provider pin. Keep production pins and hosts
   unchanged. Default-branch integration needs explicit direction; the session
   remains active and all feature refs are retained.

The task guide owns repeatable operator instructions. The source investigation
and proposed future compatibility/deployment sequence remain in this session;
they are not executed rollout records.

### Node slice final-head preparation

Normal runtime/spec/docs8-path commit and fixture1-path commit passed all hooks;
preferred commit-width warnings remain nonfatal and every line meets80 columns.
The first private bundle-exec commit launch failed the nested API localization
hook; direct normal owning-shell Git passed with all hooks enabled. No source
or hook configuration was changed to accept it. Evidence:
`/tmp/node-rpc-commits-26bn4c5f`.

Fetched origin/master148ef adds only API packaged parallel2.3 and WebUI dependency
updates on four non-overlapping paths. Normal complete23-commit replay keeps
every patch/message (`range-diff` all`=`), the binary feature patch, all nine
source hashes and both consumed migration/schema blobs. Final clean head
`7da85b7a16851ebf08e655ee12fd918762cff991`, tree4ae8a7a5; backup retains the
pre-rebase fdc9be376. No published master rewrite or source/dependency rollback.

The added generic whole-flake no-build command failed on baseline overlays.list
not being a function, unchanged in old46 and fetched master. It supplies no
verification. The correctly-bound final fixture evaluation passed exit0/57.757s/parity1; a first
utility preflight started zero checks outside the literal tracking cwd. Parent
current check in the exact tracking path passed; guard now checks it directly.
No source failure or ownership loss follows from that zero-check launch.

Reviewer0 is assigned the actual148ef..7da complete23-commit inventory and210-path
final diff, with saved independent Sol/xhigh/read_only settings and all four
HIGH-risk lanes. No clearance is claimed while the review runs. The baseline
whole-flake failure remains in the packet. Final scoped configuration evaluation
resolved fixture JSON derivation `ih1g6r614gsskcqxkyb51437jax71qzz` with no guest
closure realization or scenario run; private evidence0700/0600. All19 guarded
source/dependency hashes and tracked/index state match. Real broker/VM/payload
acceptance remains after findings resolution.


### Node recovery mandatory-review findings, 2026-10-03

Retained reviewer0 (gpt-6.1-sol/xhigh/read_only; no override or nested reviewer)
completed actual148ef..7da across general, architecture/repetition,
scope/proportionality and risk/compatibility. No Blocking findings; two Important:

1. The shared30-second publisher wait can escape existing required publisher
   threads and terminate nodectld through abort_on_exception. Restore ordinary
   required-publisher waits and keep an explicit bounded RPC opt-in.
2. Ambient `$!` can describe an already-handled enclosing error and suppress a
   cleanup-only failure. Track constructor/body errors locally in RpcClient.run.

Architect0 owns the saved narrow correction brief; implementer0 will own the
released runtime/spec/docs paths. The existing restore integration is held
until both direct fixes are verified and folded. Complete23-commit history is
coherent; no obsolete follow-ups and no new Node-slice migrations. The two
externally consumed additive migrations retain their exact versions/blobs.
See [review findings](node-rpc-recovery-review.md#independent-review-outcome).

Saved correction brief: [narrow Node review remediation](design.md#narrow-node-review-remediation-brief-2026-10-03).
Exactly five runtime/spec/docs paths are released to implementer0. The internal
`recovery_timeout: nil` preserves ordinary required-publisher gate waits; RPC
explicitly passes RECOVERY_WAIT even without a stop predicate. The existing
StorageStatus save_properties consumer supplies the representative regression.
RpcClient.run will record its own constructor/body exception locally. These
are direct step9 remediations; no fixture/schema/wire/pin or recovery-owner
change is accepted. Fresh focused/lint/full verification and owning fold are
pending. The conditional retained-profile sequence is saved separately and
remains unexecuted until actual Node restore acceptance.


Direct correction source frozen at7da85b7a: exactly five unstaged paths, empty
index, no other source/dependency changes. Final manifest SHA256
88c6fa0e2eaf20e835f9dcf91b6e16e40eef54f07414bfdede3aca606ad593fd.
The lead inspected the runtime and regressions against the saved brief and
applied the owning writing skill directly, accepting docs/node-rpc.md unchanged
(hashc965c997…24ec5). Four syntax checks and scoped whitespace checks pass;
55 focused examples are authored, not yet passed. Fresh Luna/low
node_rpc_direct_review_fixes owns the sequential focus/root1.85lint/fullNode
batch at /tmp/node-rpc-review-fixes-xp7ieeh5, with19 protected source/dependency
hashes, empty-index/head/binding guards and isolated automatic DB. Result
pending; no integration launch. Direct step9 boundary remains unchanged.


First direct-remediation focused batch at7da85b7a stopped on55examples/1failure,
exit1/18.630s (total20.081s/parity1). Evidence remains at
/tmp/node-rpc-review-fixes-xp7ieeh5. Declared lint and full suite were unrun.
The lead read the failure and owning source: the new explicit-RPC-opt-in spec
called protected response= outside RpcClient's lexical context; the actual
reply callback uses it within the owning class. Released only that existing
spec for explicit test access to the unchanged protected setter. Runtime/docs
and all other files/index remain held. No operation remains; original failure
is preserved, and passing prior cases do not clear the failed example.


Corrected focused verification PASS55examples/0failures,19.636s. Declared
RuboCop1.85 then failed with exactly2 autocorrectable test argument/key
alignment offenses,13.399s; total35.129s/parity1. Full Node stage unrun.
Private evidence /tmp/node-rpc-review-fixes-final-c_1ufkiq; parent corrected
expected.json mode0644 to0600 (directory already0700). Released only those
existing NodeBunny spec alignment lines; runtime/docs/otherfiles/index held.
Next fresh watcher selects declared lint then full Node, which includes all55
focused cases; no separate focus repeat for a whitespace-only correction.


The next declared lint gate stopped at1 remaining ClosingParenthesisIndentation
offense in the same nested test expectation,13.436s/total14.834/parity1.
Full Node unrun; private /tmp/node-rpc-review-lint-full-l60o9740. Parent read
the actual cop's column11 requirement and released only that closing whitespace.
No logic/runtime change; earlier55/0 remains the corresponding focused proof.
Source/index hold and mandatory-review step9 remain in force.


Final direct-remediation source gate PASS: fresh Luna/low
node_rpc_declared_final_suite ran declared rootRuboCop1.85 (4files/0offenses,
13.275s) then full Node634examples/0failures (35.803s), total51.225s/parity1.
Private evidence /tmp/node-rpc-review-verified-ck0mwrka,0700/0600. No owned
operation remains. The full suite includes all55 focused cases at final
whitespace-corrected bytes; earlier55/0 and each diagnosed failure are retained
separately. Controlled Bunny fixture-close IOError diagnostics are expected
failure-path output, not an additional daemon/real-broker observation.

Lead focused inspection confirms exact requested narrower publisher contract
and local primary-error ownership. Both Important findings are resolved under
mandatory-review step9; no new mechanism or affected-lane rereview is needed.
The normal owning runtime fold and unchanged separate fixture replay are
executing with hooks. Actual remote-restore integration is still unrun.


Normal owning fold complete: runtime d82a6cc1cf25e6e23671ae095880a4478a9d4e18,
separate fixture290f1ef07972e53c2b5154dbfa8b088802bde619,
treea2de421a02cc0add7a256273133b5dab9a2b2f32. All pre-commit and commit-message hooks passed in owning
Nix environment. First21/e882 parent unchanged; separate fixture's full binary
patch is identical and range-diff equals. Final19 protected hashes match tested
bytes; tracked/index clean and preexisting PHP cache preserved. Backup
backup/2026-09-23-storage-redesign-before-node-review-remediation retains7da.

Final complete inventory:23 commits/210paths/210 files changed, 23740 insertions(+), 454 deletions(-); full-index binary
SHA256f2abad5545f2e5b0daefcec7c0aca6a7e013be077b49ba200cb28bc4ba74565e. Exactly the tested five-path372+/26-
correction differs from the reviewed7da. Both consumed migration versions and
core schema blobs are unchanged; no new Node-slice migrations. Original full
independent review plus direct step9 verification remain evidence; no fresh
unaffected full-review claim.

Fresh Luna/low node_rpc_remote_restore_290f owns ONE existing disposable
storage/restore-after-reinstall-remote via /tmp/nrvm.0qykahy0/run.py atclean290f,
emptyindex/19hash/binding guards. It uses newprivate state plus no-destructive
evidence retention; native runner owns disposable cleanup. Outcome pending,
source/index held. No registered retained-cluster or release operation is run.

### Node integration and publication, 2026-10-03

Fresh Luna/low watcher `node_rpc_remote_restore_290f` passed the single existing
`storage/restore-after-reinstall-remote` at exact290f1ef0/treea2de421a: exit0,
1610.195s, parity1, four of four examples172.32/265.1/172.97/51.58s, native
script1109.64s. Actual A/B backup snapshot content, reinstall absence, remote
restore of B with normal lock release and subsequent C/incremental history,
transaction/GUID/payload assertions passed. Parent confirmed numeric result,
zero exact-state QEMU/virtiofs processes and clean tracked/index state with the
preexisting PHPUnit cache preserved. Evidence `/tmp/nrvm.0qykahy0` stays private.
This does not establish the original broker acknowledgement-timeout trigger or
arbitrary live-transfer crash recovery.

Fresh SSHfetch retained default148ef and old feature46. The first ambient push
was refused by Overcommit's changed configuration signature before publication.
After verifying the declared configuration, normal owning .#vpsadmin
`overcommit --sign` and the same exact-lease push completed at290f. Remote
readback confirms feature290f/master148ef; no hook was bypassed and source bytes
are unchanged. CI37144608422 and libnodectld37144608395 started at exact290f;
other owning checks also started. No older queued/in-progress same-branch run
was found among100 returned runs; no cancellation or broad-CI wait is needed.

Preboot checks confirmed selectedzmwh package, own stale-ready storage/bridge
status, no live recorded PID and six nonresponding configured addresses. The
private mode0600 residency evidence still matches its exact session/config SHA
and services toplevel, both store selections available. Desired profile was
absent; lead set only enable:true/enrollment:true with other JSON fields equal.
Pre-copy masked baselines are DB/catalog/entitlement/retention only. Live VPS
file manifest begins after public copied boot, before Node updates/provision,
and is compared with prior file evidence where available; no unperformed
preseed live-file comparison is claimed. Cold disk copies are recovery evidence.

### Registered masked boot and original baseline

Public maintenance-start against the recorded resident config/toplevel and
mode0600 residency evidence passed0/88.027s/parity1. The public command validated
resident inventory/disks and real masks/boot identity; public status reports
maintenance_ready/pendingtrue, storage/bridge, ordinaryreadyfalse. The watcher
observed result/identity only; a mismatched byteoffset field meant it did not
inspect runner logs. No kernel observation is inferred from that omission.
Driver and foreground command exited while the supported masked runner remains
active. Evidence `/tmp/storage-profile-retained-20261003.nemcjis2`.

Private logical vpsadmin dump passed0/4.028s,1,141,715bytes/SHA256
e516a8727fe0bec811888ba883bcb0b5f1e13725988c9d88cec05187ddb8c664.
The implementation-owned private collector was inspected before execution; its
current-command CWD was corrected to literal tracking before any guest query.
The final8b223cd3 packet captured27groups/1161rows/60932bytes/oneVPS, SHA256
5d0077d9f2ceee72d5f1dfe56e7b6ae0508d4e6dec951d8db4623a18bbdb635a.
Rows, SQL and stderr remain private under baseline-before-copy. Both are
read-only pre-copy DB evidence; no original preseed file checksum is invented.

Public update services --copy-only passed0/349.549s/parity1, phase copied; the
old generation remained held. The supported stop then completed, and public
start --copied-config is running through the guarded parent driver and fresh
Luna/low observer retained_public_copied_boot_290f. New seed/services, actual
regular-node refresh and automatic hold release remain pending. Selected source
heads/config/package are frozen; cold recovery disk copies remain untouched.

### Public copied boot and Node updates

Public stop/start --copied-config passed0/621.783s/parity1. Fresh observer
retained_public_copied_boot_290f and parent public status confirm running/ready,
maintenance phase released/pendingfalse/active true. The actual new seed/API/
Supervisor and regular-node refresh completed through the supported command;
no private release helper was used. Foreground command/driver exited; the
registered runner continues. No local source-kernel compilation was observed.

Post-copied consistent DB capture passed:27groups/1168rows/61218bytes, zero
missing/changed original protected rows. Seven additions are one shared package
and its six items; no added existing-user assignments or entitlement ceilings.
Two dynamic Pool-space observations changed. Original VPS1 on verified node1 is
running. Its four physical quota properties and known ordinary-file checksum
were captured privately before Node updates. No earlier checksum or user-data
file was supplied; this is a post-boot ordinary-file baseline, not proof across
the first seed or of unspecified user payload. Evidence remains under the
private retained-trial root.

The lead-owned guarded driver now runs ordinary public updates node1, node2,
storage1, stop-first-failure, with each current-system/running/socket check.
Fresh Luna/low retained_public_node_updates_290f observes the one related batch.
Outcome and actual packaged runtime/source proof remain pending; no provisioning
or fixture write has started.

The three ordinary Node updates passed0/341.213s/parity1, updated3/running3.
Parent closed the foreground handle; no source-kernel compilation was observed.
The inspected private implementation-owned packet then passed0/15.627s on all
three actual daemon processes: stable PID/start identity, socket peer ownership,
running control path, selected current system, exact final node_bunny/rpc_client/
storage_status file hashes, and keyed send/recv delays0. This binds the running
corrected files; it is not Ruby heap introspection or completed transfer proof.

Exact290f CI feedback: Node specs, RuboCop, migrations, PHPUnit, client, i18n and
group-snapshot contract passed. General integration CI37144608422 remains queued,
not awaited. API topics37144608379 completed failure in only core/full platform
jobs111265858355/111265858600. Failed-step logs were downloaded privately to
/tmp/node290f-api-platform-ci-szd1r95_; implementer0 owns a read-only diagnosis,
without a rerun or source edit. Provisioning has not started; original post-Node
file/quota and DB comparisons completed separately: physical quota and the
captured ordinary file are byte-equal; post-Node DB capture still has zero
protected changes, the same seven shared-package additions and two dynamic
Pool-space differences. Evidence node-runtime-proof, original-after-nodes and
baseline-after-nodes remains private under the retained-trial root.

Implementer read-only CI diagnosis: core968/1 seed25925 ObjectHistory admin Index
and full968/1 seed21301 ActionState authenticated Cancel returned HTTP500 rather
than200. Their generic statusfalse/responsenull/errorsnull shape supports the
outer HaveAPI request_exception path; no underlying exception was captured.
Affected endpoint/spec/auth bytes equal upstream148ef and pre-Node e882, and
the Node slice changes no api files. This does not prove nondeterminism or
exclude earlier feature/global spec-state interactions. Direct profile provision
uses db:seed:file/normal Pool and CatchUp chains rather than these HTTP routes;
these failures do not demonstrate a provision blocker. No runtime fix or
unchanged rerun is justified. Architect0 owns a bounded test-only diagnostic
brief; application authoring remains held during the retained trial.

Public storage-profile provision ran in the guarded parent driver with
fresh Luna/low retained_profile_provision_literal_290f observation. Final Node
source, original baseline and released public hold prerequisites passed; template1
is enabled/supported/compatible. Provision failed1/21.055s/parity1 before reaching
Pool/CatchUp staging; physical Pool/catch-up readiness and payload acceptance
remain pending. Scheduling stays stopped. No manual unlock/reset/private release
or retry.

Lead read the bounded private guest rake diagnostic through supported SSH:
the public error is "storage mutation admission requires a staging transaction"
at storage-profile-provision.rb82. Admin's owning check requires an open SQL
transaction before its freeze-row lock. Observed freeze was read_write/mode0/
epoch4; the refusal is missing staging, not proof of a read-only switch. The
payload fixture's top-level validation contains the same misuse. Architect0
owns a saved narrow correction/verification brief, including an autocommit
test context that the existing outer RSpec transaction concealed. No whole
physical-operation transaction, admission weakening or live data correction.

The first provision observer used the wrong shared-root CWD and performed zero
observation. Parent reconfirmed the exact tracking binding; a fresh literal-CWD
observer inspected the existing result without relaunching provision. Both
foreground PIDs exited, and private failure evidence is retained. The owning
script is packaged in the immutable selected provider399, so a worktree edit
alone cannot reach the public command: corrected provider publication, generated
consumer pin and checked package precede external idle activation and a justified
supported retry. Source/index remain held pending the precise brief.

The consolidated tracking whitespace gate rejected the immutable .diff files'
blank context lines (a required single-space patch prefix). Exact patch digests
were preserved and verified; prose/JSON/YAML whitespace checks passed with those
three patch artifacts excluded. No source or hook was bypassed or changed.
