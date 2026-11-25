# Final independent shared-redesign review

Reviewer-delivered report, preserved by lead on 2026-10-31. Reviewer remained
read-only and changed no files; no tests/builds/CI/browser/publication launched.

Reviewed by reviewer0, retained gpt-6.1-sol / xhigh / read_only; no overrides,
fallback or nested reviewers. Exact bound current confirmed again on 2026-10-31
from work/2026-10-30-oomd-abuse-policy; both environment markers absent, trusted
developer binding matches. Overall HIGH risk. All four mandatory lanes completed:
general, architecture/repetition, scope/proportionality, risk/compatibility.

## Findings

Blocking: none.

### Important R1 — reconciled timestamps do not reach the public VPS API

Commit ffbe4cc5234a294cd2ca9ffc49f492183c08ce8d, frozen head
e9a6530b0e18f2f58b013b3a470f3d6991d79876.
Paths: api/models/vps.rb:31-38, especially :32;
api/models/vps_incident_summary.rb:78-103; public attributes
api/lib/vpsadmin/api/resources/vps.rb:74-79.
Lanes: general correctness; risk/public contract.

VpsIncidentSummary.load derives the newly confirmed Stop completion and successful
Chown epoch before the scheduler persists them. However, Vps excludes
incident_last_stop_at and incident_accounting_since from its summary getters.
Actual API serialization therefore reads the old stored columns: a confirmed
stop may already return action_state=none and a new cooldown while last_stop_at
is nil/old; after successful Chown, counts/warning state can reflect the new epoch
while accounting_since remains nil/old. Both UIs consume those fields.
Summary-hash tests bypass this public boundary.

Smallest required outcome: use summary-aware API timestamp getters while
evaluator/reconciliation continue reading raw persisted timestamp attributes;
regress actual Index and Show after confirmed Stop and Chown, before scheduler
persistence.

Disposition: accepted by lead and assigned to owner0. Originally sent as S1,
subsequently tracked as R1. Lead reports original-source negative 2/2 and narrow
remediation positive 9/0 plus direct inspection. This report reviews the original
e9 source only: it retains R1 and does NOT certify current 3cde6709 or its WIP/final
successor. Lead may reconcile the requested narrow outcome under the skill's
direct-fix rule; no full unaffected review rerun is requested.

Advisory: no additional finding. No further Blocking/Important issue found in
the frozen ranges.

## Exact reviewed ranges and history

### vpsadmin

ac10a62f1cb0fc890378ae83cdf18dd0e29f049a..
e9a6530b0e18f2f58b013b3a470f3d6991d79876.
Complete series, exactly three commits:

- ffbe4cc5234a294cd2ca9ffc49f492183c08ce8d — shared backend/API/schema,
  supporting templates/tests/docs.
- 8a6309553d0de3ee2535ffce7af5e3960eb9caaf — legacy consumer.
- e9a6530b0e18f2f58b013b3a470f3d6991d79876 — isolated spec MariaDB
  semantics/diagnostics and documentation.

Final diff: 60 files, +3480/-153. Independently verified merge-base and tree
931bbd2c80c51c2c5db3e2eaa7bdc393e6005728; tree exactly equals retained
857b6147829261bf44f02f6efb51b684a7a687d3. The isolated testDB patch is
byte-equivalent to the earlier reviewed 52b794ef..4d72e3e patch. It changes no
production database setting.

### vpsadmin-webui

40653dffed4561dd6086716fd506a7223d3631d7..
55a813b44edb915c7ed5ce68366d6d797a551606.
Exactly one coherent application commit, 30 files, +1040/-23. Verified merge-base
and tree a9de950ca24ba002143a24744e6d8c1091e6a067, exactly equal to retained
preconsolidation 2fb91af6c21ec9fe84219fb957ca327178ad3e9d.

### vpsfree-notification-templates

2cfd218d9152888feea4109f064459078ea9f76e..
bf32762126f21fb7fc825fac25b5b45d075a2681.
Exactly one coherent template commit, 21 files, +362. Verified merge-base and tree
7fc30ef781a878c50a1e003600be2ab8131106f0. Independently compared all eight
memory-pressure subject/body blobs with the old accepted e8c2c3d OOM-specific
pair: all are byte-identical after their rename.

Whole-history conclusion: the final series introduces the selected shared design
directly. Superseded OOM-only implementation, old draft names, conversion/fixup
history, old feature aliases and obsolete screenshots are absent from these final
ranges. Retained original/preconsolidation refs preserve provenance outside the
final series. The three vpsadmin purposes are independently reviewable; the
supporting source/tests/docs within the backend behavior are coherent.
React/templates each implement one corresponding consumer/content contract.
No obsolete branch history remains in the reviewed series.

Repeated-stream conclusion: independently inventoried all changed paths and
complete commit lists. No dependency/channel/input/pin/lock update stream exists
in any of the three application ranges; no repeated generated-update stream or
redundant pin commits remain. Locale generated files support the one final UI
change. The old KB pin is outside this review and must be refreshed separately
against the final published application source.

## Migration lineage

Exactly one new backend migration:
api/db/migrate/20261030180000_add_incident_escalation.rb, AddIncidentEscalation.
It directly adds the final shared VPS fields, provenance/notification
acknowledgment fields, per-type policy table and typed durable-action table.
Core schema matches those additions; no plugin tables or intermediate OOM schema
are introduced. It uses the immediate deployed predecessor, with no
schema-existence guards or transitional draft migrations. Existing incidents
remain unqualified through nullable provenance; settings inherit defaults.

Reviewed owner/lead provenance states this version and superseded drafts were
never merged, released, deployed or externally persisted; only disposable
local/hosted spec databases used them, with no runtime guests booted. On that
evidenced boundary, rewriting the single additive migration in place is correct.
No supported predecessor requires retaining an abandoned draft step. Migration
down removes feature state and is documented as unsuitable for recovery with
active upgraded services/actions; software rollback retains additive schema/audit
and requires observe/reconciliation first.

React: no migrations. Site templates: no migrations. Migration lineage is sound
for the reviewed unreleased boundary. This is not evidence of an executed
production migration.

## Scope, architecture and consumers

Compared the delivered growth with the original thresholds and the later
explicit “ok, agreed, reworkit” shared-type decision. The static registered-rule
boundary and per-VPS/type policy storage serve that accepted request. Only oomd
is registered in production; there is no arbitrary rule builder, second production
rule/action, new endpoint/transport, daemon protocol change, or coordinated
all-node upgrade. Existing OomReport/OomPrevention/process-kill codenames remain
distinct. I found no unsupported subsystem requiring removal.

The backend owns qualification/counting/dispatch. The same registered
qualification drives evaluator, summary/filter SQL, scheduler discovery and
qualified-history privacy. Deliberate ingest plus the synthetic manually
qualified second rule demonstrates actual shared arrival/evaluation without a
node key; it is not production registration or automatic codename enrollment.
Trusted oomd provenance is backend-only and historical source-node qualification
survives migration. Per-type warning/overrides are distinct from shared physical
cooldown, stop exclusion, exemption and ownership accounting.

Inspected API/direct-chain validation, selected-type batched Index/Show/filter
behavior, admin-only overrides/writes, audit path, owner history/privacy,
ordinary mail acknowledgment/savepoints and intentional-empty New/Create,
durable stop/mail retry and transfer reconciliation. The old mixed-update,
nil-transfer and ordinary-mail failure boundaries remain present. R1 is the
remaining identified API-output defect.

Actual companion consumers inspected: legacy PHP list/detail/filter/settings/
history and React adapter/list/detail/settings/filter helpers, tests and docs,
plus core and site template registration/selection/rendering. Both UIs omit new
initial selectors for old APIs and hide unavailable capability rather than invent
zero counts; writes are explicit selected-type isolated settings. UI code does
not locally enforce or count incidents. Documentation has an owning backend
explanation linked from docs/README.md, React contract/workflow/REQ-051 updates,
and template interface documentation.

Specific-template absence alone selects generic fallback. Suppression, missing
translations, renderer errors and delivery failure do not become permission to
send another template. Type labels follow the actual selected translation
language; recipient timezone and historical decision counts/current consequence
settings have meaningful coverage. Generic bodies avoid memory/site-membership
assumptions; specific site copy preserves the approved remedies, impact and links.

Compatibility: schema before backend/supervisor; observe by default;
corresponding templates/backend before expecting new UI capability. Old daemon
messages and ordinary clients remain supported without a node update. Frontend
rollback leaves backend policy/audit intact. Software rollback does not undo
physical stops. No compatibility with abandoned unreleased oom_* feature aliases
is needed.

## Evidence and limits

Inspected native quick evidence and relevant prepared test source, including 48
affected app examples/0 failures, 2 separate migration examples/0, corrected
six-path adjacent 49/0, and 9 actual-site/backend-registry renders/0. Also inspected
topic/runtime selection evidence (13 topics, 421 files exactly once in full/core;
incident scenarios selected), minimal fixture cleanup and the recorded
negative/positive diagnostics. Consumer packets retain focused PHP/React/site
rendering and lint/type/locale/hook results for their exact inputs. Tree/history
equivalence is established; these scoped outcomes are not a broad final
hosted-foundation acceptance claim.

The invalid trailing-dot adjacent run (native 143/empty JSON) is not a valid
application result and was not counted as a pass. Earlier contaminated CI
failures and corrections remain separate evidence. The reviewed testDB commit
does not qualify future production database defaults.

The prepared real-node scenario includes physical stop/autostart, independent
mail retry without another stop, manual start/cooldown, successful Chown
epoch/privacy and known file contents before/after start and transfer. Source
inspection of those assertions is not execution proof. Long physical integration,
legacy/React browser execution and updated media, exact-final-head hosted
full/core CI, and final KB pin/capture/strict contract checks remain required after
corrected-source clearance. Old screenshots, cached images and KB1119 do not
certify the shared redesign or React runtime.

## Verdict

Original all-four-lane final review is complete. No Blocking finding; one accepted
Important finding R1 remains in frozen e9. No additional required source fixes
identified. The original range cannot receive unconditional source clearance until
R1 is reconciled; lead owns direct narrow-fix verification and final-head/history
recording. Unaffected reviewed content need not be repeated. This report grants
no runtime, KB capture, merge, deployment, production readiness or lifecycle
authority. Session remains open.

Session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/
