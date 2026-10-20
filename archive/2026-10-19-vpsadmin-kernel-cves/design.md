# Linux CVE research design

## Scope and approval boundary

Research Linux CVEs corrected by vpsAdminOS kernels spanning Linux 6.12.95
through 6.12.113 inclusive. Produce a sourced selection for user approval.
The initial investigation-only phase is complete. User steering now authorizes
a broader member-relevance proposal and reusable selection instructions in
security-advisories, including high-threat CVEs with evidence that the platform
was not affected. The phase-two brief below supersedes exposure-dependent
selection and the original prohibition on project documentation edits.
No advisory dossiers, drafts, sync, publication, deployment, exploit execution
or vpsAdmin/service writes are authorized. The lead owns tracking, worktree/Git
coordination and user-facing selection. Architect0 owns this brief and
classification reconciliation. Implementers own disjoint assigned files.
Research findings alone do not trigger final review; the completed, committed
repository instruction deliverable does.

## Inclusive range and prior-report baseline

The primary universe is CVEs with a corrective Linux 6.12 stable commit first
included in 6.12.95 through 6.12.113. The graph interval is therefore
`v6.12.94..v6.12.113`, including fixes shipped in 6.12.95. Use exact release
commit identities when tags are absent; record the source and endpoint proof.
Do not select by CVE number, CVE publication date or the current kernel alone.
Inspect current Linux CNA records as well as stable commits; stable backports,
subsequent corrections and later CVE assignments can defeat a changelog-only
or CVE-version-string-only search.

Also reconcile downstream corrections and the canonical 6.12.95 livepatch
coverage document. Keep upstream first-fix version, first downstream correction,
and first mitigating livepatch distinct. An ineffective earlier upstream fix
needs a documented exception, not silent date or version rewriting. A defect
already fixed before 6.12.95 belongs outside the primary range unless a relevant
later correction is independently established. Unassigned security fixes belong
in a separate appendix until a current primary record assigns a CVE.

The newest public publication is advisory **56**, NFS file lock list
use-after-free, **CVE-2026-72472**, published **2026-08-23T07:47:57Z**.
Its public response names upstream **6.12.97** and first livepatch
**6.12.95.2**. The date is a reporting checkpoint, not a version cutoff.
Deduplicate against the complete public association set, not only that CVE.
Package A reports 56 published advisories / 57 CVEs; all 51 repository dossiers
are published. Public reads cannot rule out private drafts; state that limit
and defer authenticated duplicate resolution until authorized draft work.

## Sources and read-only interfaces

- Public API: `GET https://api.vpsfree.cz/v7.0/security_advisories` and
  `GET .../security_advisory_cves`, optionally filtered with
  `security_advisory_cve[security_advisory]=56`. Verify counts and pagination;
  a test `limit=1` returned the full advisory list. Public UI at
  `https://vpsadmin.vpsfree.cz` establishes the user's reporting context.
- Linux CNA vulnerability records and upstream stable commit/release data are
  primary range/fix evidence. Preserve URLs, snapshot revision and access date.
- Read security-advisories AGENTS.md, README, docs/api-permissions.md and
  relevant existing analyses from the canonical bare repository. Its local
  HEAD targets absent master; inspected reference is `refs/remotes/origin/HEAD`
  at `ea6247687fd02417f87e1e5593fecd8b9055925d`. Do not repair refs for research.
- vpsAdminOS `docs/os/livepatches/6.12.95.md` is canonical historical coverage,
  not deployment proof. Inspected OS reference is
  `87fc13aac3fc8ce3d6c71c7ef3a8e72a5993a088`. V6 is quarantined; do not turn
  historical coverage into a deployment recommendation or activation claim.
- Pin exact vpsAdmin, vpsAdminOS, Linux, configuration and LXC revisions used
  for capability, namespace, device, syscall, module and configuration claims.
  Read each repository's AGENTS.md before work there. Source defaults and
  optional features are distinct from measured runtime state.

## Selection and classification invariants

Treat the user's tentative “critical” primarily as serious platform impact,
while preserving formal CVSS authority, version, vector and score separately.
The lead owns the pending user preference. Never invent a score or equate every
kernel memory-corruption defect with demonstrated host escape.

For each candidate classify VPS-root escalation, host-root/kernel execution,
cross-VPS confidentiality/integrity, and host availability separately. State
whether each outcome is demonstrated by a cited report, plausible from a
specific primitive and reachable interface, or unresolved. A crash report alone
proves neither arbitrary code execution nor privilege escalation. An absence
claim names its reviewed source/test scope; it is never a claim that production
was not exploited.

Use three reachability groups:

1. Default tenant-reachable operation, including ordinary user or VPS-root
   access through delegated namespaces/devices.
2. Optional tenant feature or configuration: keep explicit prerequisites and
   match the historical advisory breadth (KVM, Ceph, perf/BPF and specialised
   networking). Disabled-by-default is not itself grounds for exclusion.
3. Host-only, unrelated hardware/architecture or otherwise unavailable paths:
   exclude with concrete evidence. Initial-user-namespace privilege must not
   be confused with capabilities in a tenant user namespace.

Prioritise privilege gain, tenant-to-host/guest-to-host escape, arbitrary shared
kernel execution, and serious cross-tenant read/write. Flag speculative
information disclosure or serious pure host DoS as separate borderline cases
when the prior advisory precedent supports them; do not silently expand the
main shortlist. Distinguish prerequisites, trigger prevention, exploit
hardening, detection and actual fixes. Missing runtime evidence remains a
qualification on applicability, not a safe/mitigated conclusion.

## Evidence record and acceptance

Every proposed CVE needs its ID/title/subsystem; primary CVE URL and current
status; introduction and 6.12 fix boundaries; stable corrective SHA/release;
other required corrective commits; primitive and attacker prerequisites;
source-backed tenant reachability; separate impact and exploit-evidence claims;
formal CVSS if provided; dedup result; and confidence/open questions. Record
first downstream mitigation separately where relevant. Preserve a machine-
readable inventory and per-version counts, including versions with zero hits.

Accept the shortlist only after joining all range candidates to the complete
published set, resolving inconsistent fix boundaries, checking candidate-specific
configuration/capability gates, and providing reasons for screened exclusions.
Completeness means every enumerated record has a disposition or explicit
unresolved status; it does not imply every CVE is equally relevant. Keep a
manageable main selection and a conditional/borderline appendix. The user
approves selected CVEs before any vpsAdmin draft is prepared.

## Independent execution packages

| Owner | Files | Work and acceptance | Dependencies/checks |
| --- | --- | --- | --- |
| implementer0 | `research/platform-baseline.md`, `research/platform-evidence/` | Public advisory chronology and full CVE dedup; historical selection breadth; exact source/kernel configuration and tenant privilege matrix; candidate-specific applicability | Starts independently; verify API coverage, frozen source identities and limits; consume B shortlist for focused gate checks |
| implementer1 | `research/cve-candidates.md`, `research/cve-evidence/` | Complete primary-record/stable-fix join for inclusive range; per-version coverage; plausible serious candidates and explicit exclusions; scores separate from impact | Starts independently; prove release endpoints, primary snapshot, fix inclusion and rejected/withdrawn handling; consume A dedup |
| implementer2 | `research/supplemental-critical.md`, `research/supplemental-critical-evidence/` | Bounded supplemental screen of CNA Critical records outside B's 109 manually screened entries for missed serious tenant-reachable candidates | Added by user; saved Sol/xhigh settings retained. Consume existing range/dedup artifacts; send candidate evidence to architect without duplicating completed screening |
| implementer3 | `research/selection-checks.md`, `research/selection-check-evidence/` | Mechanical acceptance ledger: IDs, fix versions, scores, status, dedup and exact final proposed IDs | Added by user; saved Sol/low settings retained for this mechanical unit. No substantive design or impact reclassification; use architect final selection and primary records |
| architect0 | `design.md`, `research/classification.md`, `research/selection.json` | Resolve scope, correction and severity disputes; reconcile package evidence and propose final tiers and exact machine-readable ID set | No duplicate enumeration; communicate material scope changes through lead |
| lead | `plan.md`, `state.md`, portal and final user shortlist | Own decisions, acceptance, artifact registration and user approval boundary | No drafting before user approval |

No overlapping file edits or shared Git mutations. Send early candidate IDs
across the team through lead or same-session peer messaging. Raise missing
source access or source contradictions immediately; do not substitute guesses.

## Verification, compatibility and recovery

Quick research checks: exact endpoint releases and ancestry; CVE identifier and
status validation; stable SHA membership; zero duplicate IDs; published-set
join; reproducible counts and known-CVE control cases; primary links; explicit
source/configuration identities and uncertainty. No kernel builds, VM tests,
CI or exploit execution are justified for this research phase. Longer manual
verification is a candidate-specific source review, not a fleet scan. Any later
build/CI requirement follows the workspace verification and watcher procedure.

No persisted platform state, schema, API, protocol, generated configuration or
mixed-version deployment changes occur here. No coordinated node updates or
rollback operation are required. Recover interrupted research from pinned source
snapshots and artifact provenance. Correct findings in owned session files;
retain superseded evidence when necessary to explain a changed conclusion.
Future advisory preparation is a separately approved phase using the repository's
current schema/evidence and guarded sync workflow; research alone is not a
publishable per-node mitigation assessment. Leave this session open.

## Phase two: member relevance and reusable selection procedure

### User decision and preserved baseline

The user now wants serious kernel threats to be considered for member-facing
assessment even where vpsAdminOS was not vulnerable. Selection-worthiness and
platform exposure are independent decisions. A clear, sourced explanation of
why the service was not affected can itself be useful. Preserve the original
41 recommended / 11 conditional / 9 borderline / 8 deferred selection and its
reasons as the earlier policy checkpoint; do not silently rewrite those findings
into claims of past exposure. New recommendations live in a separate artifact
and reference the earlier decision when it changes.

Use member relevance to choose a manageable set: plausible serious privilege
gain, isolation bypass, broad kernel/host compromise or substantial shared-host
data exposure with an understandable relation to tenant-facing Linux interfaces,
common workloads or prominent kernel threats. Disabled MPTCP, blocked syscalls,
privileged program types, or unavailable devices can justify useful negative
assessments. Do not include unrelated hardware/architectures solely because
their CVSS score is high. Keep formal CVSS authority/version/vector/date
separate from source-backed impact and this editorial relevance decision.

### Decision/evidence contract

The selection record is a research record, not a new API or advisory schema.
Each considered candidate records:

- CVE, primary snapshot/URL/status, exact stable fix SHA and first release,
  introduction and correction exceptions, plus known downstream correction;
- impact primitive, attacker prerequisites and claimed outcome with evidence
  strength; formal CVSS with source/version/vector if supplied;
- selection decision (`propose`, `conditional_review`, `defer`, `exclude`) and
  member-relevance reason independent of exposure;
- exposure conclusion (`affected`, `not_affected`, `conditional`, `unknown`,
  or `unassessed`), its exact build/configuration/source/runtime evidence,
  node roles/workload, applicable dates/versions and remaining limits;
- separate current status, historical interval and mitigation state; a fixed
  current kernel does not establish that earlier kernels were never affected;
- dedup state for all public associations, repository dossiers and accessible
  private drafts, with explicit unavailable/private-read limits;
- previous selection/claim and reason for revision, approval state and next
  evidence needed before an accurate dossier can be prepared.

`not_affected` requires positive evidence that a necessary trigger prerequisite
was absent throughout the stated scope (for example an exact archived build
has CONFIG_MPTCP=n, or the relevant tenant profile necessarily blocks the
only trigger). A source default alone establishes only that default/profile;
it does not prove every deployed node or historical interval. A missing module
sample, an uninspected override, undocumented device delegation, absent logs or
unobserved exploitation are not proofs of non-exposure. Namespace capability
checks must distinguish initial-user-namespace authority from delegated userns
authority; module compilation, preload, autoload and intrinsic built-in paths
must be distinguished. Host-service/storage roles need their own workload
assessment. Unknown history remains unknown, not retroactively safe.

The procedure must accommodate both negative and positive assessment outcomes
without weakening the existing repository's per-node evidence/evaluator rules.
Research `conditional` is not a replacement for any existing evaluator enum.
Full runtime/historical assessment remains required at the approved dossier
phase, with exact mitigation claims and partial-coverage limits preserved.

### Repository interfaces and implementation boundaries

Use the repository's existing instruction/documentation layout. No local skill
is needed: there is no established skills directory, and a mandatory AGENTS
route plus a discoverable README pointer makes the procedure reusable without
introducing a skill framework or duplicated authority.

| Owner | Exact files / result | Dependencies | Acceptance and checks |
| --- | --- | --- | --- |
| implementer0 | In lead-prepared security-advisories worktree: `docs/cve-selection.md` (canonical procedure), `AGENTS.md` (mandatory route before selecting/gathering CVE batches), `README.md` (entry-point link) | This brief; lead resolves worktree registration and required Nix/hooks before commits. Read repository AGENTS and linked relevant evidence docs in full. | Procedure covers independent relevance/exposure, all range/dedup/evidence rules below, staged approval gates and negative conclusions. Links resolve, diff clean, terminology consistent with current evaluator; repo quick checks/hooks pass. No application code, dossiers or fixture/schema changes. Implementer owns normal documentation commit; lead serializes Git/publication. |
| implementer1 | `research/member-relevance.md` and `research/member-relevance-evidence/` including machine-readable revised proposal | Existing corpus, primary records, A source gates, original selection; no new broad enumeration | Propose bounded high-threat negative/conditional additions with exact IDs/fixes and clear member benefit; one independent relevance and scoped exposure result per row. Check primary membership, duplicate IDs/prior reports, source paths and exclusion strength; preserve prior 41 unchanged. Unknown runtime/history remains explicit. |
| architect0 | Update `design.md`; revised exact set in `research/member-selection.json` and rationale in `research/member-classification.md`; report to lead | Both package reports | Resolve consequential negative-evidence/classification questions; check candidate relevance and evidence scopes without duplicating corpus research. Prior `selection.json` remains the earlier policy checkpoint. |
| lead | Tracking, exact worktree/branch, member-facing proposal, approval questions and final review coordination | Accepted artifacts and committed repository docs | Repository documentation receives mandatory independent final review after quick checks and commit. Research-only expansion does not trigger a separate automatic review. Draft approval remains outstanding. |

### Required reusable method

The canonical procedure must describe: establish user intent/threat breadth and
previous advisory examples; freeze exact source snapshots; use the complete
inclusive stable graph range (start predecessor excluded, end included); join
primary CVE fixes rather than CVE numbers/publication dates; handle later
assignments, corrective commits, rejected/withdrawn records and semver omissions;
deduplicate complete public/private/dossier association sets; separate mechanical
enumeration from focused manual review and expose the unresolved remainder;
evaluate member relevance independently of deployment exposure; trace exact
source/runtime prerequisites and negative evidence; preserve current/history,
role, build and partial-coverage boundaries; record citations and checks; present
exact proposed IDs with conditional/borderline/not-affected reasons; obtain user
selection approval before preparing advisory dossiers or vpsAdmin drafts when
research-only was requested; follow existing evaluation/review/sync guards for
the approved phase; require separate explicit exact-revision publication approval
and separate email authorization. Local token availability never supplies those
approvals. Existing dossier/revision claims must not be silently overwritten.

The procedure may use a compact evidence table/template, but adds no required
machine format or runtime behavior. Avoid embedding this session's transient
snapshot IDs, CVE count or fleet state as timeless policy. Examples must remain
clearly examples, not assertions about every current deployment.

### Compatibility, verification and recovery

Only internal instructions and linked documentation change in the project.
No database, persisted advisory schema, API/client contract, node protocol,
configuration, kernel or service rollout changes. No coordinated node update,
migration, deployment or runtime rollback is required. The new instructions
must preserve the current guarded draft/publication workflow and evidence
contract; a procedure must not claim permission to execute later operations.

Quick checks: verify links and mandatory route; inspect complete final diff;
check examples/schema names against existing docs and code; ensure no credentials
or raw private-node evidence; run repository-required quick checks and hooks in
Nix under the verification procedure. This documentation-only change does not
justify new tests that mirror prose, kernel builds or long integration tests.
Any unexpectedly long check follows the monitor skill. After intended docs are
committed and quick checks pass, lead runs mandatory independent final review
including whole-branch history and documentation consistency. No merge is
authorized by this instruction update.

Recovery is a normal owned-document correction on the feature branch, preserving
published history and unrelated workspace changes. Research corrections retain
their previous decision provenance. Leave all session lifecycle state open.

## Phase three: approved 60 assessments and unpublished drafts

This section supersedes the research-only phase boundary for the exact 60 IDs
in `approved-cves.json`, bound to `research/member-selection.json` SHA-256
`8e9906fb11133cb7fafafbcb68cc7ec0900ee7f6e2e7ac50b1ca1af5b2b4b72a`. The user approved: “let’s go ahead
with the 60 cves you selected”. This authorizes complete dossiers, typed evidence,
evaluations and unpublished vpsAdmin drafts. Publication, email, integration,
deployment, unrelated CVEs and lifecycle actions remain outside this phase.

### Execution packages and file boundaries

The exact disjoint partition is [assessment/packages.json](assessment/packages.json):
three groups of 20, covering the approved set exactly once. Same owned worktree
and feature branch extend reviewed documentation head `69027fd`; no new worktree.

- **implementer0**: CVE-2026-98858, CVE-2026-98260, CVE-2026-97594, CVE-2026-80521, CVE-2026-53388, CVE-2026-63824, CVE-2026-74753, CVE-2026-93817, CVE-2026-74517, CVE-2026-89929, CVE-2026-89930, CVE-2026-89932, CVE-2026-98720, CVE-2026-63830, CVE-2026-74616, CVE-2026-98039, CVE-2026-53260, CVE-2026-72069, CVE-2026-98222, CVE-2026-99999.

- **implementer1**: CVE-2026-74668, CVE-2026-80841, CVE-2026-74586, CVE-2026-74587, CVE-2026-74588, CVE-2026-74688, CVE-2026-89478, CVE-2026-89479, CVE-2026-98586, CVE-2026-74724, CVE-2026-74669, CVE-2026-80714, CVE-2026-74656, CVE-2026-74630, CVE-2026-74581, CVE-2026-74615, CVE-2026-74662, CVE-2026-80725, CVE-2026-74746, CVE-2026-74597.

- **implementer2**: CVE-2026-74730, CVE-2026-90151, CVE-2026-68159, CVE-2026-89653, CVE-2026-89656, CVE-2026-64383, CVE-2026-64384, CVE-2026-64385, CVE-2026-64386, CVE-2026-64387, CVE-2026-64597, CVE-2026-89633, CVE-2026-80585, CVE-2026-80586, CVE-2026-80587, CVE-2026-72463, CVE-2026-98229, CVE-2026-98368, CVE-2026-98370, CVE-2026-89783.


Owners 0/1/2 each own only `advisories/<their-CVE>/**` and session
`assessment/<owner>/**`. They own complete primary/source diagnosis, full
mainline and stable introduction/fix rules, configuration/capability/role and
history reasoning, mitigation correctness, `analysis.md`, bilingual factual
`advisory.yml` candidates, justified optional `historical-attestations.yml`,
evaluation and quick validation, plus review fixes. Start primary/source dossier
preparation immediately; production evidence is a later shared dependency.
Do not copy another dossier's livepatch tuples, historical override or exposure
claim without exact supporting evidence. Preserve the research qualifications.

Implementer3 retains saved Sol/low settings: bounded authenticated dedup and
mechanical ledger/union checks, no substantive classification. Existing
`draft-preflight/` is its disjoint path; additional collection receipts and
mechanical ledgers use `assessment/implementer3/`. The corrected authenticated
CVE association projection uses `cve_id`; the earlier projection is superseded.
Lead reports final readback: 56 advisories/57 CVEs, terminal pagination proven,
zero approved CVE, external-ID or local-dossier matches. Confirm that result
before writes and stop for reconciliation if later state differs.

Architect owns this brief, `assessment/packages.json`, cross-owner design
questions and the shared collection contract. Lead owns tracking, editorial
writing, Git scheduling, mandatory review, exact remote-write scheduling and
user-facing status. No owner edits another owner's dossiers or shared code,
schema/tooling/instructions without a separately scoped blocker resolution.

### Dependencies and batching

1. Each substantive owner reads current repository AGENTS, selection procedure,
   README, evidence/API contract, schema, loader/evaluator and representative
   dossiers. Inspect full primary records and current pinned downstream sources
   per CVE. Write complete factual dossier candidates and derive a per-owner
   requirements ledger with required CONFIG names, reviewed sysctl values,
   boot/module/LSM/device/program prerequisites, Node roles and history start.
   Send that ledger early; no need to finish all analysis prose first.
2. Architect reconciles the three ledgers into one required-option/sysctl union.
   Collection uses the existing repository collector, which discovers option
   names/history scope from dossier files. All intended 60 dossier declarations
   must exist, validate and match the union before the single collection. Older
   repository dossiers remain present; do not remove them to narrow collection.
   The typed reporter's available sysctls are not a global inventory: missing
   relevant values remain unknown. No capacity/VPS/user/process collection.
3. Lead releases one global `bin/security-advisory collect` via the repository
   Nix environment; implementer3 may execute the exact bounded read-only brief.
   Store raw evidence only in ignored `.state/evidence.json`, mode restricted;
   record a redacted digest/timestamp/option-coverage receipt. Do not print raw
   collection output. If duration is uncertain, lead uses the required fresh
   verification watcher where applicable. No per-CVE collection. Existing
   coherent evidence can substitute only after exact scope/catalog/history
   coverage and collection-time freshness are checked under docs/evidence.md.
4. Freeze that shared snapshot for owners. Each evaluates its dossiers against
   it, resolves source/evidence questions and records honest residual gaps.
   Evaluate uses `.state/evidence.json`; guarded sync explicitly supplies it.
   Do not overwrite the shared snapshot during parallel evaluations. Recollect
   only for a changed deployment, Node/security scope or justified missing
   evidence requirement, with lead coordination and reevaluation of affected
   dossiers. Configuration absence on historical affected releases is handled
   conservatively; inventing history or attestations is forbidden.
5. Owners hand off technically complete batches incrementally for lead's
   context-owned bilingual writing pass. Lead serializes all Git staging and
   commits; no concurrent index use. All intended dossier/evaluation edits must
   be committed and quick checks pass before mandatory independent final
   review of the complete resulting branch. Early checks may be incremental;
   they do not replace final committed review. Review fixes stay with owners.
6. After final review, a single lead-designated sync owner processes the exact
   approved set sequentially. Review dry-run, use `sync --apply --evidence
   .state/evidence.json <CVE>`, verify exact remote readback/revision and commit
   its `submission.yml` recovery baseline before the next remote write. No
   drafts are created before this gate; no publication or mail command is run.

### Assessment and evidence invariants

Preserve formal CVSS separately from platform outcomes. Root inside VPS,
host root/kernel execution, cross-VPS access and availability each need their
own evidence strength. Five archived-build negative findings do not become
fleet/history claims. Module/default seccomp/program authority and actual
runtime state remain distinct. Tenant optional capabilities are not initial
user-namespace privileges. Real host/storage workloads require separate role
assessment; older kernels alone do not make a storage role applicable.

Use complete mainline and stable ranges including backport introductions and
explicit open-ended EOL branches, source-linked exact fixes and correction
exceptions. Source fix inclusion is separate from livepatch content correctness,
activation and history. Respect boot transitions, cumulative patch semantics
and exact tuples; quarantine/deployment risk does not erase independently
observed historical mitigation. No exploit execution or exploit instructions.

The schema and evaluator remain unchanged. Research labels are not new
per-Node enum values. Typed evidence is classified through existing version,
option, sysctl, accepted-build and mitigation rules. Evidence for prerequisites
not representable by the current schema stays explicit in analysis and honest
unknown/conservative conclusions; escalate a real modeling blocker rather than
invent unsupported YAML fields or weaken evaluation. No fabricated absence,
mitigation timestamp, history override or attestations.

Unpublished drafts may legitimately contain `unknown` states supported by a
truthful evaluation. Unknown is not a reason to fabricate resolution or block
all other draft work. The final report states the unresolved facts and affected
drafts. `ready`/publication requires resolved permitted states and complete
mitigation times, so an accurate draft need not be publication-ready. User
approval of this phase supplies neither publication nor email permission.

### Acceptance, verification, compatibility and recovery

Quick acceptance per batch: exact assigned IDs; full branch ranges and primary
links; validated schema; necessary option/sysctl declarations; actual role and
prerequisite reasoning; current/history separation; EN/CS meaning match after
lead editorial pass; evaluation against the same coherent snapshot; explicit
unknowns with no invented safe state. Run repository `validate` and required
RSpec/RuboCop in Nix, preserving hooks. Lead coordinates long checks/CI with
the watcher policy; no kernel builds or exploit testing. Independent review
covers all 60 dossiers, source and mitigation correctness, negative scopes,
public text, evaluation/history, complete branch history and no migrations.

Remote acceptance for each synchronized CVE: the committed dossier/evaluation
matches selected evidence, unique intended draft, exact CVE association/texts/
per-Node results, revision readback and committed submission baseline. Final
ledger covers all 60 as verified draft or explicit blocker, with any unknown
or vulnerable conclusions and publication-readiness limits. No claim that all
60 are mitigated merely because drafts exist.

No schema, API/client, protocol, kernel/configuration or service deployment
change is planned. Existing compatible dossier/evaluation/submission formats
are used. Old/new tools remain compatible; no coordinated node updates or
migration. Review and restore local owned content normally; retain reviewed
history. On uncertain sync outcome, stop that batch and use existing external-ID
and submission recovery/readback guards; never blindly recreate or adopt a
differing remote draft. Preserve successfully committed baselines and resume
from the first unverified CVE. No automatic delete/retract/rollback of remote
objects. Leave session open.

### Collector/evaluator interface clarification after source inspection

Per-owner early requirements artifact is `assessment/<owner>/requirements.json`:
use a `rows` array with exactly the owned CVEs and fields `cve`,
`required_options` (map), `required_sysctls` (name to reviewed effective string
values), `history_required_since`, `affected_node_roles`, `source_prerequisites`
and `unmodeled_prerequisites`. Source and unmodeled fields include citations and
what evidence would resolve them. These ledgers are research interfaces, not new
dossier schema. Owners may refine them before the shared collection freeze;
report changes after that point to architect/lead.

The collector loads **every** existing dossier from the worktree and unions
`platform.required_options` names plus the earliest history start. It does not
read Git blobs or only the approved list. Thus no global collection while any
partially written dossier is invalid. It fetches the existing typed reporter
sysctl resource; declaring a key does not add that key to the Node reporter.
Missing/unreviewed required values result in unknown. Do not add invented
requirements solely to force an unknown outcome.

`required_options` describes necessary **vulnerable-interface** conditions,
not desired safe settings: e.g. an MPTCP flaw requires `CONFIG_MPTCP: enabled`;
an observed n then proves unreachable. Requiring n would reverse the intended
meaning. `enabled` accepts y/m; module compilation alone does not establish
module availability. A y-vs-m mismatch is unknown, not an exclusion.

`required_sysctls` is a list of reviewed effective values, not a declarative
predicate whose mismatch means safe. `SysctlEvidence` returns unknown for
missing/unavailable/unreviewed values; accepted values permit the remaining
version/configuration/mitigation evaluation. A source-default restrictive
value must not be encoded as an automatic mitigation through this field.
Review namespace scope: host sysctl values do not prove tenant-controlled
per-netns values. Preserve source-gate analysis rather than silently treating
a host value as the tenant state.

The evaluator has no generic module/device/program/CPU/boot-parameter policy
predicate and no per-CVE manual-status override. Its loaded-module/parameter
inventory is evidence for the analyst, not an automatic negative decision.
Existing accepted-build rules describe exact affected/fixed source builds and
must not be abused to assert a missing runtime prerequisite is a source fix.
If an unmodeled unresolved prerequisite would make the generated conclusion
materially misleading, report the exact CVE/result/needed fact to architect and
lead. Do not edit evaluation JSON by hand or add arbitrary ignored YAML keys.
A genuine unsupported truthful outcome may be a bounded tool/schema blocker;
prefer the existing honest conservative/unknown result when it is supported.

Source identity: `Config.load` reads the existing external token file and
`APIClient` supports typed GET/OPTIONS without exposing credentials. The completed
authenticated preflight already established that path; no second inventory or
Node pre-collection is needed. CLI `collect` prints its raw snapshot, so direct
stdout to an ignored restricted file or use the library with redacted output.
CLI `evaluate` consumes the shared default snapshot and writes only its dossier
result. `sync --evidence` re-evaluates without collection; dry-run alone does not
prove fresh-evaluation equality, but apply enforces it before mutation.

`ensure_source_committed!` checks the **whole worktree**, including untracked
files outside `.state/`. All substantive owner edits must therefore be finished
and committed before sync, even if only an early group is being written remotely.
Keep transient scripts/receipts in session records or ignored `.state/`, never
untracked project root files. Incremental local handoffs remain useful, while
remote writes wait for complete-source commit and final review. Sync writes
`submission.yml` after each operation/checkpoint; commit the final baseline
before the next CVE. This preserves the repository's fail-closed recovery path.

### Shared historical livepatch reconciliation (after the one collection)

This bounded dependency prevents valid old livepatch protection from being lost
when later CVE assignments receive dossiers. It does not authorize another API
collection, module operation or deployment. Start from the frozen shared
snapshot and [historical seeds](assessment/livepatch-seeds.json), which join
approved IDs to already-discovered upstream/downstream commits. Seeds are leads,
not accepted module tuples or proven activation. The known intersection is
12 CVEs: owner1 has 11 networking cases and owner2 has NFS FREE_STATEID 74730.
Owner0 has no seeded CVE but owns shared observed-source identity binding.

**Disjoint work and dependencies:**

- Implementer3, after collection release only: mechanically extract current and
  retained event livepatch observations, preserving boot IDs, event kinds,
  enable/transition state, kernel releases and source/software identities.
  Keep full Node/event linkage and raw components restricted under ignored
  project `.state/livepatch-observations.json`. Write a sanitized unique-tuple
  index plus snapshot hash and extraction completeness counts to
  `assessment/implementer3/livepatch-observed-tuples.json`. Do not infer coverage,
  fill missing identities, accept tuples, classify intervals or obtain more
  API evidence. Include inactive/transitioning observations and both halves of
  possible atomic replacement; extraction must not discard them as irrelevant.
- Implementer0 (xhigh): for each distinct observed identity that could cover a
  selected CVE, bind exact booted/current clean vpsAdminOS revisions to their
  kernel/livepatch recipes, Linux source, module ID/variant and patch version.
  Write `assessment/implementer0/livepatch-source-identities.json` with immutable
  source URLs, SHAs/hashes and accepted/rejected/unresolved identity reasoning.
  Resolve this once per unique source tuple, not separately in 60 dossiers.
  This proves package identity only; it does not certify CVE correction content
  or actual protection. No broad audit of unobserved successor versions.
- Implementer1 (xhigh): review the 11 owned networking seeds against those exact
  candidate module/backport sources and any actually observed cumulative
  successor needed to interpret history. Write
  `assessment/implementer1/livepatch-coverage.json`, one source-backed decision
  per relevant CVE/identity. Verify the correction and prerequisites actually
  appear in the module function replacement/state, not merely that a Git commit
  exists somewhere in a cumulative repository. Cite first correcting version
  and any later correction exception. Edit only own dossier acceptance tuples.
- Implementer2 (xhigh): independently review FREE_STATEID 74730 correction
  content and the NFS cancellation boot variant, writing
  `assessment/implementer2/livepatch-coverage.json`. The cancellation kernel may
  contain this correction intrinsically while its variant module omits those
  replacements. Distinguish a proved exact fixed boot build from a livepatch;
  use supported accepted-build evidence only when complete identities/digests
  support it. Coordinate identity facts with owner0, without repeating recipe
  binding or editing owner0 records. Edit only own dossiers.
- Architect reconciles the three technical receipts and the mechanical index
  into `assessment/livepatch-reconciliation.json`; lead accepts the gate and
  schedules any resulting dossier/evaluation edits and final review. No source
  correctness decision is delegated to implementer3's low-effort package.

**Receipt contract:** keep an opaque observed-tuple key tied to the immutable
snapshot hash. Record candidate module `id`, `patch_version`, module-reported
`kernel_version`, booted release, reported Linux source if present, relevant
booted/current OS revision and cleanliness, exact recipe/module-source identity,
variant and immutable source links. Per-CVE content rows reference that key and
record upstream correction, downstream backport/replacement evidence, intrinsic
boot-fix versus livepatch-fix, first correcting patch version, technical decision
and unresolved reasons. Never infer a source from the display release alone.
Missing reported Linux source may use the evaluator's existing exact clean OS
identity contract; do not invent the missing field or relax the other checks.

An accepted source-content row is eligible for the dossier's
`accepted_livepatches`; it is not proof every matching observation mitigated the
CVE. The existing evaluator alone reconciles activation/timeline against the
reviewed tuples. A reboot ends protection unless a new observation establishes
it; no patch identity survives by assumption. A transitioning patch cannot
start mitigation. Preserve same-boot protection across atomic replacement only
with both exact accepted tuples and the required outgoing/counterpart stable
states. Keep sparse internal observation handling distinct from public lifecycle
and boot events. `mitigated_since` comes from the first non-affected transition
after the last genuinely affected interval, not the newest cumulative version.

Quarantined v6 remains unsuitable as a deployment recommendation. That operational
risk does not erase source-correct, observed loaded/enabled/nontransitioning
historical protection. Equally, a coverage page or package pin does not establish
activation. The original boot `a2384967...` uses `livepatch_6`; the NFS cancellation
boot `563bbb35...` uses `livepatch_6_nfs_cancel`, both reporting coverage version6.
Do not interchange their modules or copy tuples/Node history overrides from old
dossiers. An empty accepted list is honest before review; it must not be left
as the final basis for a later mitigation date if the collected history provides
a verifiable earlier protection. Unresolvable source/identity/activation gaps
remain explicit with the evaluator's supported conservative/unknown result.

**Source access:** use `GIT_NO_LAZY_FETCH=1` for local Linux object inspection.
Do not trigger broad partial-clone lazy tree fetches or local builds. Missing
objects may be replaced by exact public upstream/downstream HTTP commit, tag,
Makefile or source snapshots with URL, revision, retrieval date and hash. Preserve
primary Git/semantic-version evidence and honest missing-metadata limits. This
substitution changes source access, not the required confidence or fix boundary.

Acceptance: every observed candidate tuple has identity disposition and every
seeded CVE has a source-content disposition or explicit unresolved reason;
no blanket acceptance of a cumulative version. Dossier accepted tuples match
receipts, evaluator results use the same snapshot, quarantine language remains
separate, and first mitigation dates preserve valid historical protection. No
additional kernel build, exploit reproduction or API call is part of this unit.

### Bounded prerelease caveat: CVE-2026-74753

Owner0's exact mainline introduction is `7.2.0-rc1`, with correction before
`7.2.0` final. Preserve those precise global bounds and explicit older stable
regression intervals; do not invent an affected final mainline release. Current
`Advisory` validation orders the RC before final correctly, but `Evaluator`
strips the RC suffix and would classify a running `7.2.0-rc1` as fixed.
The bounded Nix/Ruby check is recorded in
[assessment/prerelease-boundary.json](assessment/prerelease-boundary.json).

At the shared snapshot gate, implementer3 mechanically flags current and retained
event/boot/reported 7.2 prerelease identities and ambiguous relevant custom builds.
If none require this distinction, retain exact dossier metadata and existing
correct stable-final classifications without changing tooling. If an actual
snapshot needs RC ordering, stop that CVE's unsafe evaluation/sync and refer a
narrow evaluator fix to lead/architect. No hand-edited evaluation, false safe
state or artificial mainline boundary is permitted. This does not block the
other dossiers or authorize a general version-parser rewrite.

### Source correction exception: CVE-2026-64387

The primary claim of a 6.12.96 fix conflicts with the reviewed stable patch:
`1665f25...` resets `send_set_info`, while the described
`SMB2_query_directory` replay cleanup remains uncorrected in exact downstream
6.12.113 source `1dfea587...`. Lead accepted an open 6.12 affected boundary
(`fixed_in: null`) pending an effective correction, preserving the official
release/SHA as disputed provenance. Do not claim 6.12.96 fixes this defect in
public response or evaluation. The finding is scoped to reviewed sources,
not a claim that no later correction can exist.

[The correction receipt](assessment/CVE-2026-64387-correction.json) binds evidence.
Owner2 retains exact mainline patch retrieval and final branch/source assessment;
the failed empty mainline patch file supplies no evidence. No unverified global
7.2 safe assertion or artificial boundary is authorized. This changes the
approved CVE assessment, not the selected IDs. Other 59 dossiers continue, and
truthful vulnerable/unknown draft conclusions remain allowed. No tool/schema
change follows automatically from the source discrepancy.

CVE-2026-64387 follow-up: exact mainline `9647492...` diff was retrieved from
the kernel source mirror and hash-verified; it resets the correct
`SMB2_query_directory` function, so the source-backed global 7.2 final fix is
accepted. The 7.1.4 hunk is also correct. The 6.6.145 hunk instead modifies
`SMB311_posix_qfs_info`, so that official stable boundary also cannot establish
correction. Owner2 retains the bounded 6.18.39 patch retrieval and final stable
branch rules. The correction receipt records each branch separately; no safe
boundary is inferred from another branch's successful fix.

CVE-2026-64387 final reconciliation: the exact 6.18.39 patch also targets
`send_set_info`, verified by its retained commit-patch hash. Accept effective
fixes only at mainline 7.2 and stable 7.1.4; keep 6.6, 6.12 and 6.18 rules open
with the disputed official fix commits explained in analysis. There is no
remaining source retrieval blocker. Owner2 applies and validates these supported
schema rules. Open boundaries are conservative pending verified correction;
only 6.12 was additionally checked through downstream 6.12.113. Do not extend
that latest-source inspection claim to an uninspected later 6.6/6.18 release.

### Requirements refinement before collection

The reconciled approved-60 union now contains **43 CONFIG names and four sysctl
names**. CVE-2026-98039 additionally requires `CONFIG_DEBUG_INFO_BTF` and
`CONFIG_BPF_JIT` for kfunc admission; both were enabled in the exact archived
build. These necessary interface gates do not prove privileged program/token
authority. CVE-2026-98368 now declares reviewed `kernel.io_uring_disabled` values
`0`, `1`, and `2`; no new sysctl name is needed. Accepted restrictive values
remain reviewed observations, not automatic mitigation or historical safety.

[The requirements union](assessment/requirements-union.json) binds the latest
three owner ledgers. The exact 60 IDs, role scopes and January history baseline
are unchanged. Actual YAML-to-ledger equality, repository-wide collector union,
validation and lead release remain prerequisites for the single collection.

Collection catalog acceptance is recorded in
[assessment/collection-catalog-acceptance.json](assessment/collection-catalog-acceptance.json).
All 60 approved declarations match the latest owner ledgers and reconciled union;
the full 111-dossier repository catalog requests 67 CONFIG names and seven
sysctls, with earliest history start 2026-01-01. The two dossier edits after the
mechanical receipt preserved their collection fields and passed validation.
The catalog gate is satisfied; the lead owns release of the one restricted
collection. This acceptance does not certify runtime evidence or evaluations.

### Shared snapshot released for assessment

The lead reported the single collection completed with exit status 0 and froze
the restricted repository `.state` snapshot with SHA256
`61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274`:
schema 8, 13 nodes, 12,544,228 bytes, collected at
`2026-10-19T21:48:39Z`, mode `0600`. The watcher elapsed-time field was a
placeholder; precise duration is unknown. Do not overwrite this snapshot or
repeat the API collection for individual dossiers.

Owners 0/1/2 evaluate their assigned 20 dossiers each with the normal tool and
this exact snapshot. Owner3 supplies the mechanical receipt, prerelease check
and observed livepatch index; owner0 binds observed source identities, and
owners1/2 verify correction content within their previously assigned boundaries.
Architect reconciliation uses those receipts and addresses concrete gaps only.
Current fixed state does not establish historical non-exposure. Residual unknown
states may remain in accurate unpublished drafts and still prevent publication
readiness. Editorial completion does not replace evaluation, committed checks,
independent review or guarded sequential sync.

### Snapshot reuse and unresolved history

[assessment/snapshot-reusability.json](assessment/snapshot-reusability.json)
records a bounded offline call of the existing evidence-digest and reuse guards
against the frozen snapshot. Both pass; no network client or raw-data change was
used. All present timestamps satisfy the collection-time guard. Missing current
timestamps remain evaluator unknowns, and one late history/reconstruction start
leaves an unknown result across the approved set. A later production-entry date
may justify an override only with independently reviewed lifecycle evidence;
the first retained observation alone cannot supply it. These facts do not
require automatic recollection and do not prevent accurate unpublished drafts.

The initial 60 evaluations use matching snapshot and dossier digests. Their
aggregate states and reasons are a provisional receipt, before historical
livepatch reconciliation. CVE-2026-64387 remains conservatively vulnerable by
version on eleven applicable nodes; actual host-prepared CIFS workload is an
unmodeled prerequisite, so this does not establish demonstrated exposure.

Owner0 reported a concrete additional CVE-2026-74753 concern: the earlier
perf correction for CVE-2026-64556 may backport its introducing change into
6.12.95 through a livepatch. Hold acceptance of that CVE's current pre-introduction
classification until owner0 verifies actual function coverage and correction
content. Absence of prerelease strings resolves only the previously identified
RC parser issue, not custom backported introductions. No manual evaluation
change or speculative schema extension is authorized by this concern.

### Node126 lifecycle scope accepted

[assessment/node126-lifecycle.json](assessment/node126-lifecycle.json) records an
independent read of configuration commit `e27882a9bc8f6900903e6ae84841b9935190548c`
and its parent, plus the frozen snapshot's first retained boot. The commit first
adds Node126 as a production hypervisor; its reconstructed history begins that
same day. Owners may use the existing supported Node126-only history override
`2026-03-31T20:11:46Z`, citing that commit and explaining the reviewed lifecycle
scope. This is the first retained baseline, not an asserted exact deployment
instant. Global January scope is unchanged. No evidence supports an override
for storage161; its two applicable RT assessments remain unknown.

### Bounded livepatch-introduced regression support

**Problem and scope.** Owner0 verified that observed cumulative 6.12.95 v2–v6
patches contain the introduction of CVE-2026-74753 and lack its correction. The
upstream 6.12.96 introduction remains true; changing that canonical branch bound
would misclassify unpatched 6.12.95. Add only source-bound livepatch introduction
rules, using the existing evidence snapshot. No kernel deployment, API change,
new collector request, arbitrary state override or general predicate framework.

**Interface and compatibility.** Add optional `platform.affected_livepatches`,
an array of exact tuples with the same five identity fields and validation as
`accepted_livepatches`: module `id`, `patch_version`, boot `kernel_version`,
`kernel_source_revision`, and clean `vpsadminos_revision`. Every tuple represents
a reviewed introduction, not protection. Require dossier `schema_version: 2`
whenever this field is present; schema1 must reject the field. New tooling reads
both versions, with existing schema1 behavior unchanged. Existing tooling already
rejects any dossier version other than1, so the schema2 dossier fails closed on
old tools rather than silently losing this rule. Update the JSON schema and Ruby
loader consistently. Only 74753 needs schema2; no bulk migration, evidence or
evaluation schema bump. Reverting tooling requires withholding schema2 dossiers,
never changing their version to1 to bypass the guard.

**Evaluation contract.** Assess this runtime introduction before returning a
safe upstream-version or accepted-build result. A loaded, enabled, nontransitioning
exact matching tuple on the matching boot introduces an affected base state;
normal necessary CONFIG/sysctl evidence still applies. A present explicitly
inactive, nontransitioning tuple does not introduce it. A transitioning candidate,
missing activation fields, or candidate with missing/untrusted/mismatched source
identity yields unknown when the base version would otherwise look safe; never
infer safety from failed identity matching. A candidate is scoped by declared
module ID and matching boot/patch release family; ambiguous partial identities
within that scope remain unknown. A distinct, complete fixed-kernel boot with
no matching candidate follows the ordinary fixed rule. Exact empty inventory on
an otherwise sufficient pre-introduction snapshot preserves the ordinary
unaffected result. Release-only history on a declared affected boot release (or
its numeric livepatch suffix) lacks activation evidence and is unknown, not
proof that a patch was absent.

Do not carry an introduced state across a boot. Reuse existing sparse internal
event normalization; do not build a second atomic-transition inference engine.
Conservative unknown is acceptable when exact historical identity is unavailable.
If introduction and protection are simultaneously reported effective, require
unambiguous supported ordering or return unknown; do not assume that protection
wins over a regression-producing replacement. A source-matched stable active
introduction overrides a nominally fixed custom base as well, because replacement
code can reintroduce a bug. Existing protection rules and their boot/transition
tests must retain their current behavior for dossiers without introduction rules.

**Independent implementation package.** Implementer2 owns only this bounded
tooling change in `lib/security_advisories/{advisory,evaluator}.rb`,
`schema/advisory.schema.json`, focused tests in `spec/{advisory,evaluator}_spec.rb`
and `docs/evidence.md` (README pointer only if needed). Existing20 dossier
ownership remains unchanged. Implementer0 owns the 74753 schema2 rule tuples,
source analysis and reevaluation after the interface lands. Architect resolves
interface questions; lead handles wording, Git serialization and final committed
independent review. Do not edit another owner's dossiers or add source tuples
from filenames alone.

**Checks and acceptance.** Focused tests must exercise genuine before/after
outcomes: unpatched pre-introduction kernel; active exact introduction; inactive
tuple; partial/dirty/mismatched identity; forward/reverse transition uncertainty;
release-only ambiguity; same-boot sparse observation; boot reset and subsequent
fixed kernel; conflicting effective protection; schema1 rejection of the new
field and schema2 rejection by the retained old loader. Existing schema1 fixtures
must still validate and keep their results. Run the targeted RSpec files and
lint in Nix, then normal repository checks once the deliverable is complete.
Verify 74753 against the same frozen snapshot and source receipts; any residual
unknown remains truthful and blocks publication. Hold its sync until committed
checks and mandatory independent review cover this change. No new collection
or altered historical attestation is required.

The historical twelve-CVE source/content join is finalized in
[assessment/livepatch-reconciliation.json](assessment/livepatch-reconciliation.json).
Eleven corrections accept the three exact original-boot v6 source tuples;
CVE-2026-74630 remains withheld for incomplete inline-header fanout proof.
All input hashes and the frozen snapshot match. Nine sparse identities remain
unresolved, and no unobserved NFS-cancel build is added. Actual activation and
dates remain evaluator results. The separate 74753 introduction rule is still
an implementation/review dependency and is not resolved by correction coverage.

Implementation clarification: candidate matching may use declared module ID
with either the declared boot/reported release family or the module's reported
kernel family. This deliberately preserves unknown for an apparently old active
module on an incompatible new boot. Complete inactive evidence can exclude
execution without source matching, but all activation fields must be booleans
before that decision; missing fields and contradictory activation flags remain
unknown. An uninterpretable inventory entry on an in-scope boot cannot be treated
as proof of an empty inventory. A distinct fixed boot with a valid empty inventory
still follows normal release rules. No additional transition cache is needed.

The initial normal-tool 74753 schema2 evaluation now binds all eleven reviewed
introduction tuples and the unchanged frozen snapshot. It reports twelve
applicable-node unknowns and one storage role exclusion: historical release-only
rows lack introduction inventory/boot identity, with additional source/activation
ambiguity on one node. Current 6.12.113 does not erase those history gaps.
Canonical upstream bounds remain unchanged. Owner0's final analysis edits need
fresh digest-consistent evaluation before committed checks/review; the initial
receipt establishes corrected conservative behavior, not final sync readiness.

Tooling handoff: commit `3ab9740a964f053d20a2de1e5e89e1f71cc3c650`
contains the six assigned code/schema/spec/documentation files. Their committed
and current hashes match the owner receipt; 113 focused examples and focused
lint pass. The retained old loader explicitly rejects schema2 while both loaders
accept schema1. [The acceptance receipt](assessment/runtime-introduction-acceptance.json)
records this bounded handoff. Final complete-deliverable review and the refreshed
74753 dossier/evaluation remain required; no sync/publication readiness is implied.

### Bounded dossier-spec cohort correction

**Diagnosis.** Full verification at `ef4b060` completed with 205 RSpec examples,
three failures and 29-file RuboCop success. The failures in
`spec/dossiers_spec.rb` are obsolete cohort assumptions, not grounds to change
source assessments: all-directory iteration expects only the original 51,
assigns their two exact fixed-build overrides to every non-legacy-livepatch CVE,
and indexes their `EXPECTED_STATES` with new CVEs. The same three loops also
contain latent legacy-only assertions: fixed summary/description phrases,
legacy monitoring membership, `node`-only applicability, overrides for both
126 and 401, universal resolved evaluations, and universal storage exclusion.
The explicitly enumerated old livepatch/version-range loops are already scoped
correctly and retain their exact assertions.

**Implementation boundary.** Implementer2 owns only `spec/dossiers_spec.rb`.
No application, schema, dossier, evaluation, raw evidence, API, dependency or
test-runner change. Keep existing legacy constants and exact guarantees. Make
the original cohort explicit from the existing 51 `EXPECTED_STATES` keys and
iterate its exact paths for the three legacy regression examples. Verify the
legacy membership/count explicitly, so missing legacy dossiers cannot silently
drop from the tested set. Add one compact ID-only constant for the approved new
60, sourced during authoring from `approved-cves.json`; tests must not depend on
session files, Git history or ignored production evidence. Assert disjointness,
unique membership, counts 51/60 and exact total directory membership. This
membership list is not an expected-state/source table; do not copy 60 per-CVE
outcomes or tuple sets into a second manually maintained oracle.

**New-cohort contracts.** Check all new dossiers through the real loader and
their committed evaluations: schema/CVE/dossier digest binding; nonempty valid
provenance digests and timestamps; the same exact 13 unique Node IDs; one coherent
collection identity across the new cohort; allowed per-Node states and nonempty
reasons. Independently recompute state counts, unresolved Node IDs and
`resolution_complete` from committed Node rows and compare the completeness
summary. Do not require unknown/vulnerable rows to become resolved. Validate
structural English/Czech public fields through the existing loader; do not apply
legacy summary strings, stock root phrases or legacy monitoring lists to the
new cohort. Check the reviewed batch invariant of no invented accepted-build or
historical-attestation entries, and only the independently reviewed Node126
history override (exact source and scope time), not the old Node401 override.

Add a few explicit regression examples for consequential new evidence, rather
than a mirrored expected-60 table:

- CVE-2026-64387 preserves open 6.6/6.12/6.18 correction boundaries, verified
  global/7.1 fixes and applicable-node vulnerable results in this committed
  snapshot; no published false 6.12.96-safe assumption.
- CVE-2026-74753 keeps canonical upstream introduction/fix bounds, schema2 and
  its 11 reviewed affected-livepatch entries; applicable-node history remains
  unknown and publication incomplete rather than falsely pre-introduction safe.
  Existing unit specs own the general introduction-state-machine behavior.
- The two RT dossiers include storage and preserve its missing-evidence unknown;
  other new dossiers exclude storage by reviewed role and show that exclusion.
- CVE-2026-74630 has no accepted whole-v6 protection; the eleven reviewed
  correction CVEs use the same three exact original-boot v6 tuples. A small
  group and shared tuple expectation may bind this source exception, without
  duplicating all per-CVE release histories or evaluation rows.

**Acceptance and verification.** Every existing legacy assertion remains active
for its original 51 IDs, including exact builds/livepatches, first mitigation
dates, summaries, open ranges and resolved state counts. All 111 dossiers still
load and have digest-bound evaluations; the new 60 receive the contracts above.
No skipped/pending examples, weakened inclusion-only inventory check, catch-all
fallback state, fabricated fixed build, production API, or raw-evidence runtime
dependency. Inspect every all-directory loop in this spec for cohort assumptions;
do not change unrelated already-enumerated regression loops.

Quick owner checks: Nix RSpec for `spec/dossiers_spec.rb` only and targeted lint
for that file, with the original seed 42615 available for reproducing failures.
This file reads local artifacts and does not run the 14-minute full suite; if its
runtime becomes uncertain or exceeds the watcher threshold, use the prescribed
watcher rather than launching a long inline check. Owner supplies exact changed
assertion boundaries and results; lead serializes the spec-only commit. Mandatory
independent affected-lane review must accept the committed test correction before
the lead schedules any full rerun through a fresh watcher. Architect does not
rerun tests or edit the spec. Source/evidence stay frozen and draft sync remains
unreleased. This test-only change has no deployment/API/state migration or
rollback effect; reverting it restores the obsolete test assumptions only.

### User-directed follow-up: RT storage, perf history and CIFS workload

**Scope and invariants.** Follow up only CVE-2026-53260, CVE-2026-72069,
CVE-2026-74753 and CVE-2026-64387 from published feature head `8d1413ef`.
User-authorized draft corrections do not authorize publication, email, default
branch integration or rewriting the already consumed branch/submission lineage.
Keep the frozen `61904e...` snapshot and all remote submission baselines. No API
or collection in source investigation. Lead owns final bilingual writing and
serial Git/sync after committed affected-lane independent review.

**Immediate factual boundaries.** No VPS/user processes on storage does not
alone remove a TCP listener-close/timer race (53260) or generic substituted RT
spin/rw-lock RCU lifetime race (72069). Their necessary `CONFIG_PREEMPT_RT`
condition, affected branch and actual host backup/NFS/TCP/locking paths must be
checked. Do not classify storage as safe by extrapolating tenant isolation.
For74753, the present algorithm returns unknown upon any unresolved historical
point before considering a later fixed boot. Earlier exposure uncertainty can
remain true while a subsequent retained corrected boot proves the risk ended.
For64387, source already blocks tenant-created CIFS mounts; the operator's
no-exploitable-delegated-mount statement closes the other tenant path within its
actual time/workload scope. The ineffective LTS patches remain defective.

**Owner0 package: perf timeline and RT diagnosis.** Own
`advisories/CVE-2026-{53260,72069,74753}/` and
`assessment/implementer0/followup-*` artifacts. Use pinned primary/fix/source and
frozen relevant evidence only. For RT, establish whether a necessary path is
absent from actual storage or its exact historical kernel/configuration is
positively non-RT/pre-introduction/fixed. No API call, archived-config inference
for an unrelated build, role removal without path proof, or copied attestation.
If the user's no-workloads statement is insufficient, return the precise missing
condition and keep unknown; this is a valid bounded outcome.

For perf, preserve every reviewed introduction tuple and canonical upstream
range. Inventory all actual historical unknown categories and each node's
subsequent retained fixed-kernel boot. Implement the smallest terminal-interval
correction in `lib/security_advisories/evaluator.rb` and
`spec/evaluator_spec.rb`: earlier point-level uncertainty must not hide a later
proved corrective kernel boot with a fully classifiable safe suffix through the
current observation. Continue requiring current freshness, history coverage,
baseline and attestation integrity. Do not resolve a current unknown, later
unknown/reintroduced affected point, or an apparently fixed current observation
without a retained corrective transition. Missing source identity, partial
introduction inventory and transitions remain unknown at those historical points.

A qualifying retained fixed boot after the last affected **or unknown** point
may produce `mitigated`, with the reason explicitly retaining uncertain earlier
exposure. Use the actual transition's exact effective time only where supported;
otherwise retain its observation bounds. Do not backdate to the first presumed
patch application or call this the globally earliest possible mitigation. The
existing result fields need no manual rewrite or new API/evaluation schema.
Choose a conservative supported fixed boot rather than broadening this unit to
arbitrary workload/configuration transitions. Existing all-known timelines and
runtime introduction/protection state rules remain unchanged. If the available
boot evidence cannot supply a defensible interval, keep unknown with the reason.

**Owner2 package: CIFS prerequisite scope.** Own
`advisories/CVE-2026-64387/`, `assessment/implementer2/followup-*`,
`schema/advisory.schema.json` and focused compatibility checks in
`spec/advisory_spec.rb`. Existing Ruby loading and evaluator role dispatch already
support `affected_node_roles: []`; JSON schema alone currently rejects it. If the
operator confirms no vulnerable tenant mounts throughout the reviewed period,
use that empty role set as the smallest supported dossier exclusion, with the
operator statement, its date, workload and time scope recorded in analysis.
Allow empty arrays in JSON schema; verify old and current Ruby load/evaluate
them identically. No schema-version bump is needed when runtime semantics are
unchanged. Do not invent CONFIG absence, fixed-build acceptance, timestamps,
special role names or unsupported per-node status fields. All open erroneous-LTS
fix bounds and verified mainline/7.1 corrections remain unchanged.

The quoted generic operator policy has no explicit January start. Lead is asking
whether it applies throughout the reviewed January-to-snapshot period, including
host-prepared/delegated mounts, or only currently. Prepare independent source,
compatibility and factual text work while waiting; do not apply whole-history
empty-role exclusion before that scope is established. If only current scope is
confirmed, report that precise limitation and retain historical uncertainty;
do not expand this package into a general dated-attestation framework. Host-only
CIFS use outside the tenant assessment is explicitly outside this conclusion.
No automatic update of the other CIFS advisories is part of this package.

**Shared-file serialization.** Owner0 has the first exclusive slot for
`docs/evidence.md` and `spec/dossiers_spec.rb` to describe/test the terminal fixed
boot rule and adjust only the relevant reviewed results. Owner2 prepares its
empty-role explanation and minimal dossier-test delta in its follow-up artifact,
then applies those shared-file changes only after owner0 and lead release that
slot. Owner2's empty-role evaluator behavior tests can similarly be handed to
owner0 during its evaluator-spec slot, or applied after explicit handoff. Neither
owner edits the other's dossiers or submission files. Lead integrates editorial
changes before final evaluation digests and serial commits.

**Acceptance/checks.** Owner0 tests uncertain history followed by a real fixed
boot; affected then unknown then fixed; no unknown after that boot; unknown after
fix; current-only fixed observation; missing overall coverage/baseline; valid
observation-bounded timing; unchanged all-known/atomic-replacement behavior.
Verify the actual12 perf node histories against the frozen snapshot without
publishing their raw linkage. Owner2 tests empty role acceptance/old-runtime
compatibility and all-role exclusion without inventing freshness evidence, while
nonempty role semantics remain unchanged. Dossier tests retain false-LTS-fix
regression assertions and adapt only the now-evidence-supported impact/history
expectations. RT negative checks require positive necessary-path or exact-build
evidence, not merely the requested desired label.

Run targeted Nix specs/lint and four normal CLI validations/evaluations with the
frozen snapshot after factual/editorial changes. Keep meaningful assertions;
never relax snapshot guards or manually edit evaluation JSON. Lead obtains
committed affected-lane independent review before watcher-run long checks and
guarded sequential draft updates. Expected compatibility is unchanged API and
evidence formats; timeline logic changes assessment conclusions only. Old tools
are conservative for the perf change and already support empty-role exclusions.
No kernel deployment, data migration or branch rewrite is required; rollback
retains prior committed dossiers/submission baselines and never overwrites remote
draft revisions without ordinary conflict guards.

#### Storage operator configuration observation: current exclusion

The operator supplied `zgrep -i preempt_rt /proc/config.gz` from
`backuper2.prg.vpsfree.cz`, returning `# CONFIG_PREEMPT_RT is not set`. This
positively excludes the necessary real-time kernel mode for both 53260 and
72069 on the observed running storage kernel. The exclusion no longer rests
on absence of VPS workloads. It does not require another configuration check.
The conversation establishes receipt of this observation on 2026-10-20; it
does not supply an exact execution time, boot identity, build digest or
January-to-snapshot history.

There is no reviewed evidence here of any earlier RT deployment on this
storage node. Archived and current vpsAdminOS non-RT configurations corroborate
the operator observation, but source defaults do not identify every historical
storage boot. Its missing frozen evidence is a coverage limitation, not evidence
that an RT kernel was used. Do not describe the historical possibility as an
observed or likely exposure.

**Smallest supported representation.** Owner0 records this exact observation,
source and scope in both RT analyses, retaining `storage` in affected roles and
the unchanged frozen evidence. Lead may add a short, storage-specific bilingual
`node_notes` entry distinguishing the operator-confirmed current non-RT kernel
from unresolved earlier coverage. This existing dossier mechanism makes the
current exclusion visible in the draft without inventing typed runtime data.
Regenerate evaluation normally after final prose so the dossier digest and
notes remain coherent. No new schema, evaluator branch, API call, accepted
kernel build, history override or historical attestation is authorized by this
observation. Owner0's source/configuration investigation is complete unless a
new exact record appears; do not request the same current proof again.

The current single `state` represents the assessment period and drives
publication completeness. For this frozen storage row it remains `unknown`;
that does not retract the affirmative current exclusion. Changing it to
`not_affected` would incorrectly resolve the whole period. A separate
machine-readable current state with unresolved historical coverage would be a
new result/input and publication-compatibility contract, not an existing
configuration option. Do not introduce that extension within this follow-up
without a separately accepted bounded brief from the lead.

**Acceptance adjustment.** Owner0's expected RT result remains 12 mitigated and
one history-unknown storage node; its analysis and optional localized node note
must clearly identify the current prerequisite as absent. Never move the
observation backward into the frozen 2026-10-19 collection or infer an earliest
mitigation date. Preserve all existing role/configuration checks and raw
snapshot hash. Tests should assert the supported note/digest contract only if
needed for these factual dossier changes, rather than introduce a synthetic
config/history fixture pretending to represent production.

This bounded decision does not hold the independently completed perf terminal
boot correction. CIFS whole-period exclusion still depends on the already
pending operator scope answer; no answer is inferred from the RT observation.

#### Narrowed follow-up verification through feature CI

The active implementation/review/sync batch is now the perf correction and
the two RT dossiers' current-observation notes only. CIFS period scope and any
stronger RT historical assertion remain pending; no empty-role schema/dossier
change is included in this batch. Earlier four-dossier and owner2 acceptance
steps apply only if that separate work is subsequently released.

After the two focused owner0 commits and mandatory affected-lane review,
successful **full feature-branch CI at that exact reviewed source head** may
serve as the longer verification. A duplicate local full-suite run is not
required by this design. The inspected repository workflows run unfiltered
`bundle exec rspec` and
`bundle exec rubocop --parallel --force-exclusion` on Ruby 3.4.0; the Nix
development shell uses Ruby 3.4. The RSpec configuration applies random order
without CI-specific omissions or evidence-dependent exclusions. The workflows,
Gemfile lock and local test configuration have no pending changes in this
package. No workflow modification is needed.

Local targeted Nix verification remains a prerequisite: the reported 128
targeted examples, three-file lint, three normal dossier evaluations and
unchanged-other-conclusion comparison against all60 supply the focused and
real-evidence checks that CI's fixtures do not replace. Preserve their receipts
and the frozen snapshot hash. Independent committed review must precede the
feature push that starts the full CI runs. A fresh verification watcher may
observe those runs under the existing monitor procedure; no local full run
should be launched solely to duplicate them.

Before any draft sync, retain each workflow's run identity, exact head SHA,
terminal success and full-suite/lint summary. Require both workflows to pass
on the reviewed head, without cancellation, skipped coverage or a substitute
run from an older head. A failure requires diagnosis before any retry. A
substantive follow-up change invalidates the affected review/check receipts
and must follow the ordinary correction workflow.

The three guarded sequential draft updates remain lead-owned and follow full
CI success. Commit each submission checkpoint before the next write, retaining
the consumed lineage. Afterwards inspect the exact three checkpoint diffs for
submission-only scope, preserve the reviewed source/evaluation content, and
record final feature-head CI and the whole-branch history conclusion. This
mechanical tail does not justify rewriting consumed commits or silently
accepting source changes. Feature CI/push is development verification, not
default-branch integration, publication or production deployment.

### Confirmed operator-period exclusions: RT storage and CIFS

**Accepted evidence and supersession.** The operator has now confirmed both
pending facts: backuper2 ran without `CONFIG_PREEMPT_RT` throughout
2026-01-01 through 2026-10-19, and the assessed hypervisors did not use CIFS on
their hosts at all throughout that period. These are accepted operator
attestations, not inferred source defaults. They supersede the current-only RT
limitation and pending CIFS question above. No further logs, repeated question
or production collection are required. Preserve the command/output previously
supplied for current RT configuration as corroboration, without manufacturing
historical boot identities, configuration digests or event timestamps.

The new bounded batch changes only CVE-2026-53260, CVE-2026-72069 and
CVE-2026-64387 plus the small supporting applicability contract below. Start
from published/consumed `cfef162049f632016c9e67bca0e400c58c8618d2`
(72 retained commits). Preserve the perf assessment and every other CVE,
the frozen `61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274`
snapshot and all submission baselines. Existing draft baselines are RT
112/v14 and 113/v14, CIFS106/v13; perf85/v25 is unchanged. These identifiers
are expected preconditions, never permission to ignore remote revision drift.
No rewrite of consumed history, publication, email, merge, deployment or
session lifecycle operation is authorized.

**RT representation: one necessary-option exclusion for one node and period.**
The existing role list cannot express the specific backuper2 fact: removing
`storage` would silently exempt other storage nodes. Exact-build and historical
event attestations require identities that this operator statement does not
provide. Add one optional dossier map,
`platform.operator_node_exclusions`, keyed by positive decimal Node ID strings.
Use only the following explicit record shape in this bounded implementation:

```yaml
operator_node_exclusions:
  "161":
    type: required_kernel_option_disabled
    node_name: backuper2.prg
    node_role: storage
    valid_from: "2026-01-01T00:00:00Z"
    valid_through: "2026-10-19T21:48:39Z"
    option: CONFIG_PREEMPT_RT
    value: "n"
    source: "analysis.md#operator-confirmed-non-rt-period"
    reason: "Operator confirms this node ran without PREEMPT_RT throughout the assessed period."
```

The name must match the existing frozen API Node identity, with the FQDN from
the operator linked explicitly in analysis. The final reason/source text may
be refined without changing this contract. `valid_through` is inclusive and
chosen to cover exactly the frozen collection within the operator-confirmed
October19 day. It is a claim boundary, not a fabricated observation time or
mitigation transition. Keep both RT dossiers' affected roles as
`[node, storage]`, required options and all upstream ranges unchanged.

The loader and JSON schema require a map with valid Node-ID keys and all
listed fields. Reject unknown record fields, unsupported type, non-string or
blank identity/source/reason, invalid or reversed timestamps, non-CONFIG option,
or any value except `n`. Require the named option to be declared `enabled`
in this dossier's `required_options`: a disabled unrelated option cannot
grant an exemption. An absent or empty map preserves prior behavior. Do not
accept arbitrary result states, role-wide selectors, fabricated kernel
versions, or free-form predicates.

Evaluation may return `not_affected` from this reviewed operator claim before
requiring otherwise unavailable per-node kernel history, only when Node ID,
name and role match and its validity interval fully contains
`[history_required_since(node), evidence_time]`. Use the snapshot collection
time, not the later evaluation/editorial clock. On identity mismatch or
outside that interval, do not apply the exemption; use ordinary evaluation.
A future collection beyond the bound cannot inherit this operator conclusion.
Invalid declarations fail loading. A known exact retained configuration that
contradicts the claimed disabled option must yield `unknown` with a conflict
reason rather than silently lose to the operator claim. Inspect only the
node's current and retained in-scope event configuration evidence using the
existing catalog/attestation readers; missing option data is not a conflict,
and another node's catalog entry is not evidence about this node. No new
timeline reconstruction, collector or runtime-state model is needed.

The generated result reason must identify operator attestation, the disabled
necessary option, node and assessed interval. It must not say the typed raw
configuration proved the fact or that the kernel source contains the fix.
Use existing `not_affected` result fields without invented mitigation dates,
release, boot or configuration digest. Analysis records the exact operator
statement, its receipt date, identity link, period and source-based necessity
of PREEMPT_RT. Keep `historical-attestations.yml` and raw evidence unchanged.
This is a source-reviewed negative applicability fact, not a replacement
historical kernel snapshot or a new current-versus-history result framework.

**CIFS representation.** Apply the prepared minimal JSON-schema alignment
allowing `affected_node_roles: []` and set that existing field only in64387.
The runtime already excludes all roles with an empty list. The operator's
confirmed absence of all host CIFS on the assessed hypervisors closes both
host-created/delegated and tenant-selected mounting paths for the assessed
period. Preserve the previous storage workload exclusion. Record operator
source, receipt date, named assessed role/node scope and period in analysis;
do not convert it into a global assertion about all future machines.
Keep 6.6, 6.12 and6.18 `fixed_in: null` and all disputed-versus-effective fix
provenance, plus the verified mainline/7.1 corrections. Absence of use does
not repair those backports. No other CIFS dossiers change in this batch.
New collection or changed host workload requires ordinary applicability
review before reusing the static role conclusion.

**Compatibility and recovery.** Keep dossier schema1 for these three files.
The additive RT map only grants a reviewed negative exemption. The exact
`cfef1620` loader accepts that additional key and its old evaluator ignores
it, producing the existing conservative storage unknown rather than false
safety; verify this behavior with isolated parent-runtime tests. Normal sync
must reject that old recalculation against the new committed resolved result
before writes. Do not weaken digest/conclusion comparison to make rollback
work. Using old tooling to reproduce the new RT result is unsupported: retain
the matching tool/dossier commit or withhold those updates until compatible
tooling is restored. Empty-role CIFS behavior is identical in old/current Ruby
loaders/evaluators; the old JSON schema may reject the newly explicit empty
array, which is a safe authoring refusal. No API, evidence, evaluation-format,
database, kernel deployment or coordinated node upgrade is involved.

**Disjoint execution packages and shared-file order.**

1. Implementer0 owns the RT contract and dossiers:
   `lib/security_advisories/advisory.rb`,
   `lib/security_advisories/evaluator.rb`,
   `advisories/CVE-2026-{53260,72069}/{advisory.yml,analysis.md,evaluation.json}`,
   and `assessment/implementer0/operator-period-*`. It has the first exclusive
   slot for `schema/advisory.schema.json`, `spec/advisory_spec.rb`,
   `spec/evaluator_spec.rb`, `spec/reconciler_spec.rb` if a focused rollback
   guard test is needed, `spec/dossiers_spec.rb`, and `docs/evidence.md`.
   Add only the RT map/validation/assessment and meaningful tests/docs in this
   slot; do not implement owner2's empty-role alignment concurrently.
2. Implementer2 owns the CIFS dossier
   `advisories/CVE-2026-64387/{advisory.yml,analysis.md,evaluation.json}` and
   `assessment/implementer2/operator-period-*`. It may prepare these facts in
   parallel. After owner0 freezes and lead explicitly releases the shared
   slot, it applies the prepared minimal empty-role schema alignment and
   focused tests/docs to the current files, preserving owner0's RT changes.
   It owns that second slot for the same shared schema/advisory/evaluator/
   dossier specs and `docs/evidence.md`. Revalidate parent-runtime proof
   against exact `cfef1620`; do not replay stale patches blindly.

Neither owner changes submission files, perf, other dossiers, dependency locks
or workflows. Lead owns final English/Czech prose after the facts settle,
including replacing the now-obsolete RT history-unknown note. Then owners
regenerate the final digest-bound evaluations. Git commits and draft writes
remain serialized by lead; the written brief must be accepted before execution.

**Focused acceptance.** RT tests must cover correct identity and complete
period yielding an operator-labeled exclusion despite absent raw history;
other node/name/role, too-short period and collection after the upper bound
falling back; inclusion at the exact upper bound; later editorial time with
the same collection; malformed/unsupported declarations; irrelevant-option
rejection; exact conflicting configuration; and absence of this field leaving
ordinary states unchanged. Parent-loader/evaluator proof must show conservative
RT unknown and ordinary pre-write drift rejection, with no manual JSON.
CIFS tests preserve nonempty-role behavior, prove empty-role old/current
equivalence, retain ineffective-LTS-bound assertions and establish the new
operator-scoped result. Keep legacy51 and new60 membership/digest guarantees.
Do not copy a giant expected-state table or weaken unrelated assertions.

After lead editorial work, run three normal validations/evaluations against
the untouched frozen evidence. Expect each RT dossier to have12 mitigated
hypervisors and one not-affected storage node; expect64387 to have13
not-affected nodes. The perf result and the other56 selected dossiers'
conclusion fields must equal parent `cfef1620`; all111 dossier inventory and
unmodified submission baselines remain intact. Check source ranges/options/
accepted tuples are unchanged outside the new explicit applicability fields.
Targeted Nix specs and touched-file lint precede commits; retain concise
receipts and frozen/source hashes.

**Review, full verification and updates.** Lead arranges mandatory committed
affected-lane review of code/schema/tests/docs and these three security
conclusions before the exact reviewed source head is pushed to start full
RSpec/RuboCop feature CI. That CI is the full-check gate; do not duplicate
the long local suite. Wait for both exact-head workflows to succeed before
any draft write. Then use ordinary guarded dry-run/apply/readback, in order
53260,72069,64387, committing each submission checkpoint before the next
write. Reject remote revision/content drift rather than overriding it. Record
the three resulting drafts/revisions, final feature-head CI and complete
history/consumption conclusion. Preserve all72 prior commits and source/
submission boundaries. No publication, email or merge follows from success.

### Read-only vpsAdminOS PREEMPT_RT repository-history check

The user's request is to verify whether the vpsAdminOS repository ever enabled
real-time preemption. This is a bounded source/history investigation, not a
change to the accepted dossiers or operator statements. Architect0 owns the
scan and `assessment/preempt-rt-repository-audit.{md,json}` evidence. Use only
the canonical `repos/vpsadminos.git` and this session's retained artifacts;
never inspect another session's worktree.

First inventory every locally available branch/tag/ref, exact tips, shallow and
partial-clone status, history count/roots and missing objects. Read repository
instructions from the exact existing default ref. Run all Git object/history
reads with `GIT_NO_LAZY_FETCH=1` and no external diff/text conversion. Search
current ref trees and all reachable local history for `PREEMPT_RT` and
`PREEMPT_RT_FULL`; inspect relevant config/generator/patch changes, including
enabling assignments and removal of explicit disabling. Separate RT support/
conditionals from real configuration selection and from PREEMPT_DYNAMIC.
Retain exact commit/path/line references for conclusions and a reproducible
coverage record, including missing refs/objects and upstream-input limits.

Initial metadata inspection shows this vpsAdminOS clone is not shallow and has
no promisor/partial-clone setting. Its local origin default is `staging` at
`a26791178a929adb96d978c093f6a3c5be4b0f9d` (2026-10-20), while origin/master is
an older historical branch. Confirm actual object/ref coverage before treating
this as complete local history. No network fetch is initially needed; if a
material gap appears, report its scope and estimated fetch cost before any
authorized bounded SSH fetch. Do not trigger missing-blob fanout.

No source/index/ref/API/advisory/evaluation edits, tests, builds, Nix operations,
new agents or lifecycle actions. Findings do not trigger mandatory change
review or CI. Report any real RT enablement promptly. An absence result must
be scoped to inspected reachable repository history, not an unsupported claim
about deleted refs, arbitrary downstream configurations or all deployed builds.

Completed repository audit: 3,524 unchanged local refs, 11,645 reachable commits,
103,215 objects and 35,637 unique blobs; zero missing objects, no fetch.
`7c9ca632` added an optional `6.1.46-rt13` package with RT enabled on
2023-08-23 while keeping ordinary `6.1.46` as default; `972c8d49` removed that
package on 2023-09-08 while advancing the non-RT default to `6.1.52`.
Two historical release tags retain the option. The current default tree retains
only false-by-default RT helper code, with non-RT catalog defaults. No tracked
RT default or machine-use selector was found. Repository support/package
availability is not deployment proof and does not contradict the separate
operator statement that RT never ran in the fleet. Full scope, immutable links
and reproducible evidence are in
`assessment/preempt-rt-repository-audit.md` and its companion JSON.

### Authorized publication and default-branch integration

**Scope and authorization.** The user's instructions, “good, let's publish the
drafts” and “and merge the changes”, authorize publication of the reviewed60
and integration of security-advisories into its configured default branch.
`assessment/publication-and-merge-user-authorization.json` records that
direction; it supersedes the earlier drafts-only phase restriction. There is
no further approval question for these unchanged drafts and this merge.
Architect0 supplies this brief only. Lead accepts preparation and releases
execution; implementer1 owns publication, implementer0 owns integration.

The exact local binding is `assessment/publication-integration-design.json`,
SHA256 `75a2a8614778ba0e65ec4f3194b625902c86f27a88795adb68dc42a0924c5c8f`.
Its60 unique rows preserve the original approved membership and bind each
CVE to its advisory ID, content revision, dossier/remote digest, source parent,
and committed submission/evaluation hashes. This is a local design manifest,
not a remote-preflight receipt. In particular,53260 is112v17,72069 is113v17,
64387 is106v27, and74753 remains85v25. All60 committed evaluations are resolved
and agree with their submission dossier digests.

**Immutable inputs and compatibility.** The source head is
`e6ceb642878dd97546174217676d9861afc38d4e`; the target is
`refs/heads/2026-07-13-security-advisory-automation`, previously
`ea6247687fd02417f87e1e5593fecd8b9055925d`, at
`git@github.com:vpsfreecz/security-advisories.git`. Preserve all81 consumed
commits and69 source-parent recovery boundaries, with no squash, rebase,
history rewrite or feature-ref deletion. There are no migrations. Preserve
all111 submission baselines and the frozen evidence
`61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274`.
This phase changes neither code/schema nor dossier/evaluation content.
No collection, persisted reevaluation, draft sync or content refresh is
authorized. Consume implementer1's already-running read-only readiness receipt
against the frozen evidence; do not initiate another readiness/collection loop.
Publication itself does not evaluate or collect evidence.

**Publication package and gates.** Implementer1 prepares the repository's
normal `publish` dry-run for precisely the manifest60, from the repository Nix
environment. Before any write, every row must pass committed-source/evaluation
checks, full remote identity/content/CVE/node comparison, submission digest and
revision checks, draft state with no publication time, and effective publish
action permission through the existing permission checker. Stored token scope
alone is insufficient. Bind the successful plan to this manifest and source
head; fail on drift without adopting or rewriting remote content.

After lead release, use the same batch with `--approved-publication`; this is
the existing user's approval attestation. The publisher repeats whole-batch
preflight before its first write, then publishes sequentially with each exact
`expected_content_revision` and `send_mail: false`. Require exact readback of
identity, unchanged revision/content/nodes, published state and a valid
publication time for every advisory. Keep sanitized plan, outcome and readback
receipts under session assessment records. Never expose the token.

The publisher does not persist a submission baseline after publication.
Therefore no publication checkpoint commits are needed: retain all111
baseline bytes, committed evaluations and the e6ceb source head. Do not run
sync or adopt a published advisory to manufacture a new baseline.

**Integration package and gates.** Implementer0 prepares the exact merge using
the selected installed workspace-host coordinator and its catalog entry.
The documented individual prepare/approve/submit route is accepted because
this installed package lacks the linked integration-driver guide. Preserve
normal Nix hooks and SSH transport. Merge-only work has no machine reservation
(`reservationId: null`); it still requires the coordinator queue and an
approval record carrying the user's actual instruction, repository, full target
ref and reviewed source snapshot. Do not bypass contention with direct Git.

Before submission, require fresh remote target/feature identities, fast-forward
ancestry, clean source/index, captured comparison and the complete reviewed
81-commit series/final diff. The lead's
`assessment/merge-lead-current-history-check.json` binds all10 whole-series
and bounded-final-check artifacts to accepted review. Existing exact-e6ceb
RSpec/RuboCop CI and whole-history review are accepted; current preparation
reports no target/feature drift. Reconfirm those bindings at release. No new
full suite or independent review is needed for unchanged inputs. A changed
source, target incompatibility or substantive resolution returns to lead;
never rewrite the consumed lineage to force a fast-forward.

**Order and acceptance.** Preparation may run in parallel. Lead first accepts
the all60 publication preflight and exact-head integration preparation.
Publish and read back all60, verify source/baseline/evidence immutability,
then submit the prepared merge of the same e6ceb head. If preparation expires,
refresh it against unchanged source and the current target. Confirm coordinator
success and the remote target contains the exact approved head, with the
feature ref retained and all consumed boundaries preserved. Lead records
publication and integration outcomes separately; these operations are not
cross-system atomic. No deployment, email or session lifecycle action follows.

**Failure and recovery.** A whole-batch preflight failure must cause zero
publication writes. A later failure can leave a published prefix; retain its
verified IDs and the exact failing target. The existing recovery readback can
confirm an exact matching published row, but a still-draft response after a
transport error is an uncertain outcome, not immediate retry permission.
Reconcile that target read-only and settle the original effect before continuing
only the confirmed-unpublished remainder. Never blindly rerun all60 or bypass
revision checks. Changed content/permissions return to lead; the unchanged
remaining subset retains the existing authorization.

If publication succeeds and integration fails, retain the publication success
and recover the merge independently. Retry an uncertain coordinator request
with its original request identity/input or inspect its original attempt;
do not start a competing job after an ambiguous push. Resource waits remain
interruptible. A source rollback cannot unpublish remote advisories, and older
tooling must not overwrite them; retain exact source/baselines for diagnosis.
Retraction, unpublication, notification and destructive recovery are outside
this authorization. The session remains open.
