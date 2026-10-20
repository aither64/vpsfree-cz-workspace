# 2026-10-19-vpsadmin-kernel-cves

## Goal

I'd like you to gather linux kernel CVEs in vpsadminos kernel since 6.12.95 to 6.12.113 (inclusive). start from the last CVE reported in vpsadmin security advisories at vpsadmin.vpsfree.cz. Make a list of eligible CVEs and after my approval, you will draft them in vpsadmin using the security-advisories repo.

Look at the existing advisories to see what CVEs we're interested in. There's too many in reality, so we choose those that can lead to privilege escalation, etc.  critical severity, I'd say. if  you're unsure about classification, you can ask.

## Affected repositories

- `security-advisories`: read existing assessment conventions and, only after
  approval, prepare unpublished vpsAdmin drafts.
- `vpsadminos` and `linux`: read-only kernel version, configuration, patch and
  stable-fix evidence. vpsAdmin production drafts may be created only for the
  approved60 through the guarded repository workflow.

## Approach

1. Architect defines the inclusive fixed-version interval, latest published
   advisory baseline, applicability rules and independent research packages.
2. Implementers gather existing-advisory/configuration evidence and enumerate
   upstream CVEs/fix versions, then reconcile reachability and impact.
3. Present a sourced shortlist, explicit exclusions and classification questions.
4. Selection approval received for exact60. Complete dossiers, one shared
   collection, per-CVE evaluation, final review and sequential guarded draft sync.

## Decisions

- User clarified during research: high-threat CVEs may be selected even where
  vpsAdminOS was not vulnerable, so members can see explicit non-applicability.
  Selection value and platform exposure are independent; unknown evidence must
  never become a not-affected claim.
- User requested reusable selection instructions in `security-advisories`.
  Add a repository-owned batch-selection procedure and routing from AGENTS/README,
  following existing layout. This authorizes documentation implementation,
  independent final review and feature-branch publication, not integration.

- Exact60 assessment and unpublished drafting are now approved. Publication,
  email, deployment and default integration remain unapproved.
- Assess tenant-to-host privilege escalation, container escape, arbitrary kernel
  execution and similarly serious impact; distinguish platform priority from
  formal CVSS severity. Do not infer exploitability solely from memory corruption.
- Use primary CVE and stable-fix evidence; record uncertainty and deduplicate
  against existing advisories rather than comparing CVE numbers chronologically.
- Existing advisory breadth includes conditional KVM, Ceph, BPF/perf and
  specialised networking. Preserve default and opt-in tenant exposure separately;
  true host-only prerequisites remain a reason for exclusion or explicit question.

## Compatibility and deployment

Research and reusable selection documentation do not change deployed systems.
The completed assessment phase additionally introduces bounded dossier schema2
for exact livepatch-introduced regressions, with CVE-2026-74753 as its consumer.
The loader supports schema1/2; old tooling rejects schema2. Rollback must withhold
schema2 dossiers rather than silently discard their rules. Evidence schema8,
evaluation schema4, submissions and API contracts remain unchanged. No kernel
or configuration deployment or coordinated machine update is requested.
Unpublished draft creation uses existing guarded API revision/readback/recovery
contracts. Publication, deployment and repository integration need separate scope.

## Documentation

Readers: user approving the selection and later advisory authors. Keep research
method in `design.md`, detailed evidence in session artifacts, and current phase,
ownership and unresolved classification decisions in `state.md`.

## Testing plan

Validate range endpoints, CVE identifiers, stable fix inclusion and applicability
against primary records, and confirm prior-report deduplication. No builds or
integration tests are needed for research alone. Routine findings are exempt
from automatic final change review; substantive later advisory changes are not.

## Revised selection and reusable procedure

The original41-CVE proposal is retained as a prior-policy artifact. The user
clarified that high-threat cases may warrant reporting even where the platform
was not vulnerable. Member relevance and exposure must be independent. Extend
selection with useful source-backed negative/conditional cases, retain exact
build/role/history scope and unknowns, and do not infer never-vulnerable fleet
history from current or archived source defaults.

The repository deliverable is `docs/cve-selection.md`, routed from `AGENTS.md`
and linked from the README. It describes reproducible range enumeration,
full dedup, relevance and exposure criteria, evidence/confidence, revision of
prior claims and explicit selection/draft/publication/email boundaries. No new
skill framework, runtime code or schema changes are needed for the reusable
procedure; later approved dossier work is a separate deliverable. It preserves
the existing evaluator contract in `docs/evidence.md`, including conservative
historical affected classification where applicable evidence is missing.

Owners: architect updates design/reconciles revised selection; implementer0 owns
repository docs, Nix hooks, quick checks, commit and review fixes; implementer1
owns disjoint member-relevance research; lead owns final prose, tracking and
approval/review coordination. Mandatory independent final review applies to the
committed reusable procedure. No merge or deployment is authorized.


## Approved assessment and draft phase

The user explicitly approved the exact60-CVE member-selection proposal for
assessment and unpublished vpsAdmin drafts. `approved-cves.json` binds the IDs,
policy and source hash. This supersedes research-only restrictions for those
IDs only; publication, email, deployment and default-branch integration remain
unapproved. Use repository dossiers, supported typed Node history/evidence,
per-CVE source/primitive/role/config/runtime analysis, evaluation and guarded
sync. Preserve meaningful exact-build negatives independently from member
relevance. Reuse a coherent shared evidence collection once prerequisites are
known, with no broad capacity collection or per-CVE redundant fleet scans.

Architect owns phase3 design/dependencies and disjoint execution packages.
Implementers own assigned dossier paths, diagnosis, quick checks, commits and
review fixes; lead applies context-owned bilingual prose review and coordinates
serialized Git/remote writes. Final substantive dossier changes must be committed
and independently reviewed before long tests and before remote sync. Every remote
write requires exact dry-run/evaluation acceptance, post-write readback and a
committed submission baseline before the next write. No publishing or email.


## Final assessment verification and execution

All60 dossiers and exact frozen 13-node evaluations are committed. Independent
four-lane whole-branch review is complete. Its primary-provider citation and
primitive-specific KVM protection fixes were inspected directly under the narrow
fix policy; conclusions, public texts, code/schema/specs stayed unchanged.
Final source head is d23040cd3f3e8e33677dafdeb8e59cc83466e17b after the
independently accepted cross-cohort dossier-spec correction. Full verification
passed:212 RSpec examples/0failures and29lintfiles/nooffenses. Implementer1 owns sequential
exact60 unpublished draft writes with frozen evidence, exact readback and one
normal-hook submission commit before each next write. Keep genuine consumed
source/recovery lineage. Four dossiers retain truthful publication blockers;
no additional investigation or invented safe states is required for drafting.

Project evidence.md documents schema2 compatibility and runtime introduction;
session design and receipts retain source-specific decisions. The prepared
operator procedure is assessment/implementer1/draft-sync/README.md. Final branch
publication/CI and history inventory follow draft completion; default integration,
publication, email and session closure are outside authorization.


## User-directed blocker reassessment

After completing all60 drafts, user clarified that storage runs no user workloads
and VPSes do not receive CIFS mounts that could expose64387. They ask whether the
known livepatch-introduced74753 interval followed by6.12.113 correction suffices.
Architect owns bounded applicability/evaluator diagnosis before changes; preserve
host-workload distinctions, exact stablefix corrections and supported history
semantics. Implementers own disjoint technical changes/quickchecks/commits and
followupfixes. Lead owns bilingual editing and guarded remoteupdate release.
This authorizes accurate affected draft updates, not publication/email/merge.

Accepted bounded follow-up: a retained boot into an upstream-corrected kernel,
followed by an entirely safe suffix, can resolve the final perf interval despite
uncertain earlier introduction. Preserve all global evidence guards, historical
uncertainty and actual transition bounds; no schema/collector/API extension.
Old evaluator behavior remains conservative on unchanged input formats. RT uses
existing localized node notes for the current positive non-RT observation;
its absent storage history is not replaced with an invented safe past. CIFS and
empty-role schema changes remain deferred pending period-wide operator scope.

The two focused source commits were reviewed, checked locally and verified by
full exact-source feature CI before three existing-draft updates. Each update
has exact returned readback and its own normal-hook baseline commit before the
next write. Preserve the72-commit consumed series; final feature-only SSH push,
exact-head CI and bounded whole-history provenance review complete this batch.
No further source changes or evidence collection are planned. User answers to
whole-period CIFS/non-RT scope can open a later bounded correction; current
facts alone do not authorize retrospective exclusions. All publication, email,
default integration, deployment and session lifecycle gates remain separate.

## Confirmed operator-period exclusions

The user has confirmed both historical facts for2026-01-01 through2026-10-19:
backuper2 was non-RT throughout, and the hosts did not use CIFS at all. Preserve
this positive operator attestation distinctly from frozen collected evidence.
Architect0 owns a bounded node-specific RT applicability representation and
prepared CIFS empty-role schema alignment before implementation. Owner0 owns
RT/evaluator unit; owner2 owns CIFS/schema unit with serialized shared edits.
Lead applies EN/CS prose directly. Preserve flawed LTS bounds, no fabricated
kernel identity or mitigation timestamp, and all consumedcfef162 lineage.
Independent committed review and full exact-sourceCI precede sequential guarded
updates to only64387/53260/72069 with a normal checkpoint before the next write.
No publication, email, default integration, deployment or lifecycle action.

Confirmed-period batch completed: two focused source commits, independent4lane
review and fullsourceCI, three guarded draftupdates/normalhookcheckpoints, final
SSHfeaturepublication+fullCI+bounded77historyacceptance. All60nodeassessments
resolved; no publication/email/defaultmerge/deployment orsessionclosure.
Futureevidence/workloadchangesrequireordinaryscopedreassessment.

## Direct public wording correction

User clarifies RT has never been enabled anywhere and rejects archived-build-only
public qualification, redundant backuper notes and undefined "reviewed period"
in CIFS prose. This is a bounded editorial unit under the direct-lead-brief
exception: no new architecture, runtime rule, evidence contract or assessment
state/date change. Lead owns EN/CS rewrite of3YAMLs; owner0 owns concise source
provenance reconciliation, removal of obsolete note assertions, normal3CLI
digest regeneration, focused quick check/lint and one normal-hook source commit.
Retained independent review covers general/public-security fidelity and complete
history; feature CI follows, then3 ordinary guarded existingdraft updates with
normal checkpoints. Preserve3fab77consumedprefix/all66boundaries. No publishing,
mail, default integration, deployment or lifecycle authority.

Directpublicwordingcorrectioncomplete: sourceaa15boundedreview+CI, threeexisting
draftsupdated17/17/27 withRTnotesremoved/exactreadback+normalcheckpoints, final
e6cebfeaturepublished/finalCI+81historyaccepted. Alltechnicalstates/reasons/dates
remainunchanged. Sessionopen; no publication/mail/defaultmerge/lifecycle.

## PREEMPT_RT repository history verification

User requests read-only vpsAdminOS repository search to verify the historical
never-enabled RT statement. Architect0 owns investigation/method/coverage notes,
using canonical Git refs and retained source caches only. Search current tracked
configuration and full available relevant history, including historical RT alias
and Nix generation/patch selection. Separate actual CONFIG enablement from
conditional code/comment/support references. Record exact tips/branches/tags,
shallow/partial/remote freshness limits and immutable source links. No changes
to application, configs, drafts or production; findings/evidence do not trigger
new implementation review/tests/CI. User-facing conclusion must stay within the
searched source/history scope and distinguish deployed/custom overrides.

## Authorized publication and integration

User now explicitly directs publication of the reviewed drafts and merging the
changes. Scope: exact60 latest accepted snapshots at e6ceb642, send_mail:false,
plus security-advisories feature integration into configured default
2026-07-13-security-advisory-automation. Architect0 owns the bounded operations
brief, implementer1 the guarded publication batch, implementer0 coordinator merge
preparation/execution. Existing content/revisions must pass read-only preflight;
no recollection/evaluation/sync refresh is authorized. Preserve consumed history
and immutable receipts; do not rewrite external recovery boundaries. Source and
final-history independent review/CI remain applicable to unchanged e6ceb642.
Merge-only coordination requires no machine reservation. Session remains open.

Publication/integration outcome: all60 exact reviewed advisories published with
no email; normal coordinator fast-forward integrated e6ceb642 into the configured
default. Post-merge exact-head RSpec/RuboCop both passed. All81 consumed commits,
69 recovery boundaries and111 baselines preserved. No requested work remains;
session stays open. Final evidence is linked from state.md and handoff.md.
