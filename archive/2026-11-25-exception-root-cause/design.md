# Incident report IP-filter exception

## Release status and scope

Package A (investigation/design, architect0) is accepted; package B is executing
in the registered vpsadmin worktree. The verification sequence below incorporates
the measured full-file cost and the fixture failure reported by B through lead.
No application source has been edited by the architect. No production access
is needed.

The user's later direction supersedes the earlier blanket client-synchronization
requirement: package A3 below owns the policy correction. Package A2's Go/Rust
sync is parked; its retained brief/evidence is historical, not current execution
authority. Lead and implementer1 reconcile its effects separately.

Fix the reported `GET /v7.0/incident_reports` database exception in **vpsadmin**.
Keep this to the list query and its request regression. This is not a broader
incident-policy, pagination, HaveAPI, or database redesign.

## Evidence and root cause

- The supplied exception email is dated 2026-11-24. Relevant sanitized facts:
  `ActiveRecord::StatementInvalid`, caused by `Mysql2::Error: Column
  'detected_at' in ORDER BY is ambiguous`; action
  `VpsAdmin::API::Resources::IncidentReport::Index`.
- The request uses an `incident_report.ip_addr` filter, `limit=25`, and
  `_meta.includes=user,vps,ip_address_assignment`. Use documentation/test IPs
  when reproducing; the actual address and full request environment are unnecessary.
- The email's API package identifies vpsadmin revision
  `4062a8da3314aa7b48170b0d6f441446bad9b207`, ActiveRecord 8.1.4.1,
  mysql2 0.5.7, and HaveAPI 0.32.2. Its stack enters ActiveRecord's eager-load
  query path and HaveAPI action execution. No full SQL statement was extracted
  from the email; the SQL mechanism below is established from the source.
- Fresh `git fetch origin` on the canonical bare vpsadmin clone resolved
  `origin/master` to `81e930b25fa3252d7e849aff4819e663cec37b07`.
  `git diff 4062a8da3314aa7b48170b0d6f441446bad9b207 origin/master --
  api/lib/vpsadmin/api/resources/incident_report.rb api/models/incident_report.rb
  api/models/vps_incident_action.rb` was empty. The defect remains in current
  default source; production's present deployment was not queried.

`IncidentReport::Index#query` joins `:ip_address_assignment` for the IP filter.
`with_includes` applies the requested include for that same association.
ActiveRecord can therefore execute the includes as joined eager loading.
`Index#exec` also includes `notice_action: :incident_report`: the notice action
belongs to its triggering incident report, so this joins a second, aliased
copy of `incident_reports`. Both copies contain `detected_at`, while the final
order is the raw SQL string `detected_at DESC`. It no longer identifies which
report supplies the sort timestamp. The failure does not require an actual
notice row; SQL column resolution precedes result materialization.

Relevant source locations at the default revision:

- `api/lib/vpsadmin/api/resources/incident_report.rb`: `Index#query` and `#exec`.
- `api/models/incident_report.rb`: `has_one :notice_action`.
- `api/models/vps_incident_action.rb`: `belongs_to :incident_report`.
- HaveAPI tag `v0.32.2`, commit
  `1ef9b204ba45bb261d3334be5c555cc1856b713b`,
  `servers/ruby/lib/haveapi/model_adapters/active_record.rb`: `with_includes`
  applies parsed metadata associations; `with_desc_pagination` preserves the
  supplied order and applies the existing qualified primary-key cursor/limit.

Introducing interaction: vpsadmin
`d6d42b74aa3f38683a2b07d143e699e28eb20805` (`api: add reusable incident policies`,
2026-11-18) added `.includes(notice_action: :incident_report)` to `Index#exec`
while retaining the existing raw order. It is an ancestor of the email's
revision. This identifies the relevant source change without attributing the
exception to the ActiveRecord upgrade or requiring an historical bisect.

Confidence is high for current relevance and the failure mechanism. Implementer0
reproduced the exact ambiguous-column error before the production edit using
MariaDB 11.4.13 and ActiveRecord 8.1.4.1 (one example, one failure). The corrected
query proceeded to response serialization; successful end-to-end regression
evidence remains required after the fixture correction below. The architect
has not run or repeated B's tests.

## Package B: implementation and regression

**Owner:** implementer0. **Technical clarification:** architect0 directly;
scope, consequential deviations, additional ownership and releases go to lead.

**Files owned:**

1. `api/lib/vpsadmin/api/resources/incident_report.rb`
2. `api/spec/api/resources/incident_report_spec.rb`

Replace only the raw order with ActiveRecord hash ordering:
`.order(detected_at: :desc)`. ActiveRecord then binds the timestamp to the
base model's table. Keep the nested notice include and all existing filters,
visibility restrictions, output and pagination. Do not change query loading
strategy merely to avoid the join.

Extend the existing Index request specs with the failing request shape:
an IP filter, explicit `user,vps,ip_address_assignment` includes, and limit 25.
Use the existing synthetic report/IP fixtures. Assert successful HTTP/API
response and exact report order by the base report's `detected_at`, with
distinct timestamps. Existing fixtures create older/newer reports in a way
that distinguishes time ordering from ID ordering. Cover the authorized
administrator request and retain member/other-owner filtering coverage,
including an empty match. Reuse/extend existing examples instead of building
a new test subsystem. An additional SQL assertion is unnecessary if the real
MariaDB-backed endpoint regression fails before and passes after the change.

**Invariants and acceptance:**

- The email-shaped IP-filtered request succeeds on the real API with MariaDB;
  the regression demonstrates the ambiguous-column failure before the fix.
- Results retain descending **base incident report** detection time ordering.
- Member ownership and current ownership-epoch restrictions stay intact;
  no new report, notice or associated-resource access is granted.
- Existing `limit`, `from_id`, includes, total-count and notice fields retain
  their contracts. The existing timestamp/ID cursor semantics are out of scope.
- No database migration, persisted-state mutation, schema/API declaration,
  dependency, frontend or node protocol change is introduced.

**Dependencies/resource boundaries:** lead owns initial tracking and worktree
registration. implementer0 alone owns this repository's application edits and
Git mutation window. architect0 owns this design file; lead owns plan/state and
portal records. No shared development cluster or machine reservation is needed.
The client evidence obligation below depends on the final committed API head
and does not block release of these two application files.

## Verification and evidence

Read vpsadmin `AGENTS.md`, `docs/agent-instructions/development.md`,
`docs/agent-instructions/testing.md`, and `docs/api-schema-export.md` before
implementation/checks. The existing incident-report spec belongs to
`platform-operations` in both full/core matrices; extending it needs no new
topic or CI selection rule.

Measured evidence changes the check order: B's all-plugin full-file run took
7m03 for 27 examples, with two failures in the changed explicit-include examples.
Both reached VPS serialization and failed with `undefined method pool for nil`
at `api/models/vps.rb:173`: the existing deliberately minimal VPS fixtures lacked
datasets. This is a fixture gap exposed after the SQL fix. B owns the narrow
fixture correction using existing helpers; preserve all requested includes and
response assertions. Do not weaken the request or change production VPS behavior
to make the regression pass. The failed full-file run did not execute component
lint because the batch stopped at RSpec failure.

Pre-review quick gate from the documented Nix shell (`nix develop .#api`, which
enters `api/`):

1. Reuse the recorded before-fix reproduction; do not repeat it without changed
   evidence. Run only the two corrected request examples, selected explicitly
   from `spec/api/resources/incident_report_spec.rb`, in both
   `VPSADMIN_PLUGINS=all` and `VPSADMIN_PLUGINS=none`. Require both examples to
   execute and pass in each mode, preserving the full email-shaped request,
   ordering, associated serialization and ownership assertions. Record the exact
   selectors/command and result. Use the automatic isolated MariaDB database.
2. Complete the component's required `bundle exec rubocop` and declared commit
   hooks. Changed-file lint alone does not establish that component lint passed.
3. Commit the complete correction and fixture/regression changes, then give the
   complete base/head series, diff, evidence and explicit no-migration conclusion
   to the lead for independent final review. Do not run another full-file batch
   before that review.

After review, the required remaining long coverage is the complete incident-report
spec file in **both modes**, supplied by the ordinary GitHub API-spec
`platform-operations` full/core jobs at the exact final published API head.
These jobs already select this entire file, so successful CI replaces duplicate
local full-file reruns; both local and CI copies are not required. Retain the
exact run/attempt/head and manifests/results proving file inclusion and execution
of the two regressions in each mode, and require normal topic-coverage and other
selected CI checks to pass. A missing, filtered-out, failed, cancelled or
incomplete job does not establish coverage. If CI cannot supply a mode, B runs
the complete incident-report file for that missing mode locally **after review**
and records exact-head evidence; unrelated CI requirements remain in force.
Diagnose new failures before rerunning the smallest affected check. No optional
test expansion, additional VM campaign or production check is needed.

Use the monitor skill for uncertain-duration or greater-than-one-minute checks,
including focused checks if their duration is uncertain. Capture source revision,
effective dependency versions, command, result and compact evidence. The earlier
core run's outcome and any safe interruption/owned-database cleanup remain B's
existing reconciliation duty; this brief does not direct another process action.
Current gaps are the corrected focused passes in both modes, completed lint/hooks,
committed final review, and exact-final-head full/core CI coverage.

The earlier rule caused an export and three-client assessment for this behavior-only
query correction. Those completed receipts remain evidence, but the user explicitly
requested the narrower declaration-based gate in A3 below. The query correction
does not change the declared API contract. C found pre-existing missing Go/Rust
resources; that unrelated drift is separate scope and is not a prerequisite for
this fix. TypeScript's completed no-change proof needs no repeated check. No
further export/client comparison or update is required solely for this task's
declaration-neutral implementation or documentation changes.

Implementation delivery includes exact base/head, changed files, before/after
regression results, full/core and lint/hook results, known gaps, complete branch
history and no-migration provenance. This design is planning/evidence, not an
automatic independent-review deliverable of its own.

## Compatibility, deployment and recovery

This changes only read-query construction. All existing clients and deployed
nodes retain their request/response/protocol behavior; schema, settings, mail,
incident-policy evaluation and saved reports are unchanged. Old and corrected
API processes can coexist, although requests reaching an old process can still
fail. No coordinated node rollout or data conversion is required.

A future authorized deployment needs the corrected API package and ordinary
API worker restart/replacement. Rolling back to the preceding compatible
software restores the bug without requiring database rollback or state repair.
The failed GET does not require replaying incident creation, mail or node work.
No integration, deployment, machine mutation or session lifecycle action is
authorized by this brief.

Documentation readers are implementer0, reviewer and future maintainers of this
diagnosis. This session file is the appropriate home for the source lineage and
individual regression evidence. Existing `docs/incident-escalation.md` remains
accurate; no user-facing documentation or KB change is needed for a correction
that restores the existing list contract. The regression preserves the lasting
query invariant beside the owning resource tests. Raw email and environment
remain outside Git; do not copy them into source, logs or tracking records.

## Package A2 / C synchronization release brief

**Status:** parked by the user's later scope decision, superseded for this task
by A3. Retain the following as historical design/evidence only. It does not
authorize further synchronization. Lead and implementer1 own reconciliation of
any existing command effects; B's reviewed API correction is unchanged.

### Inputs and bounded output

The mandatory vpsAdmin synchronization procedure requires Go/Rust saved inputs
and generated output to match the final API source, even though this exception
fix changes no declaration. C's existing `client-artifacts/schema-drift.json`
shows exactly two added raw subtrees: `incident_policy_evaluation` and
`incident_policy_exposure`; nothing else changed. These are pre-existing API
read collections, not API work introduced by this session. C's completed
TypeScript comparison binds assessed head
`b619eb8324bfe80c7b225f698fb83efe97639c83` to the final API export: raw schema
byte-identical and all 691 owned generated files identical, including the
ownership manifest, with zero additions, changes or removals. See
[client-assessment.md](client-assessment.md). No TypeScript edits are required.

Use final API `da7724abdc080e59820cc4f0812ce1a41b3fc5df` and the unmodified
`/tmp/exception-root-cause-schema-1` export. [B-export-receipt.md](B-export-receipt.md)
binds its deterministic repeat, API 7.0/protocol 2.0, full-fixture profile, English
locale and six plugins. Raw schema SHA-256 is
`7e2a529787c06944f1ad0cdf3369edd8b4650d79826f3bbda9101af2dfb67628`;
source provenance and exporter lock hashes remain those in that receipt.

Client bases are Go `5934903568862a95b688479f0b13e11e4a36692f` (`master`) and
Rust `15db0ffd95ccd34247de9f839c906d860afb1b69` (`main`). C's complete comparison
maps bind reusable candidates under `client-artifacts/go-output/client` and
`client-artifacts/rust-output`:

- Go: 693 to 697 generated files; add
  `resource_incident_policy_evaluation.go`,
  `resource_incident_policy_evaluation_action_index.go`,
  `resource_incident_policy_exposure.go`, and
  `resource_incident_policy_exposure_action_index.go`; change only `client.go`
  among existing generated files. No removals.
- Rust: 698 to 702 generated files; add `mod.rs` and `index.rs` under each of
  `resources/incident_policy_evaluation/` and `resources/incident_policy_exposure/`;
  update only `.haveapi-generated.json`, `mod.rs` and `resources/mod.rs` among
  existing generated files. No removals; copied runtime bytes stay unchanged.

Reuse these actual generated candidates when their input/configuration/tool
identities and complete file hashes still match the C receipts. Do not repeat
the initial generation/comparison campaign or hand-edit generated code. If an
input changes or the candidate cannot be bound, report the discrepancy and
regenerate only the affected client under its documented command. Never infer
an omitted/deleted file from a partial diff.

### File ownership and pinned generation

Allowed Go changes are `schema/source-api-7.0.json`, `schema/provenance.json`,
`schema/tooling.Gemfile.lock`, derived `schema/api-7.0.json`,
`schema/generator.json`, and the five generated `client/` paths above. Align
only the embedded API source revision in README's existing development snapshot
paragraph; no new examples, prose expansion or release notes are needed.
Preserve handwritten tests, `go.mod`, projection helper, generator lock and tools.
Client provenance must update API source/exporter receipt digests, raw/effective
schema digests and generated file inventory, retaining the exact source hash
map, configuration and generator toolchain.

Allowed Rust changes are `schema/api-7.0.json`, `schema/source-provenance.json`,
`schema/tooling.Gemfile.lock`, `schema/provenance.json`, `schema/inventory.json`,
and the seven generated paths above under `src/generated/`. Bind the new raw
receipt/schema/coverage inventory honestly; preserve generator, runtime and
configuration identities. Preserve `src/lib.rs`, tests, examples, package files,
`Cargo.lock`, `generator.toml`, generator lock, tools and flake inputs. No Rust
prose change is needed: its existing development guide already describes the
authoritative saved-source and capability boundary.

Copy the raw schema, source provenance and exporter lock as a single input
receipt with unchanged bytes. Copying the new exporter lock records how B's
export was produced; it does not authorize changing client/runtime/generator
dependencies. Never substitute the exporter lock for a generator lock.

Both clients retain HaveAPI generator 0.32.2 at
`1ef9b204ba45bb261d3334be5c555cc1856b713b`. Complete pins remain in
`client-artifacts/generator-identities.json` and each client's provenance:

- Go: existing module/package/API options, Go/gofmt 1.26.10, Ruby 3.4.11,
  Bundler 4.0.23; generator lock SHA-256
  `f75dfbefc8ced373a643517b9a416ac8886695b9ac74e2cf8bd2eabd0be1afc5`.
  Retain all recorded generator/shared-source/runtime-template hashes.
  Use only existing `tools/prepare-schema`: its sole transformation is the
  fixture OAuth revocation URL to `https://auth.vpsfree.cz/_auth/oauth2/revoke`.
  Reuse C's twice-matching `go-effective.json` with recorded raw/derived hashes;
  no new transformation or weakening of origin trust is allowed.
- Rust: existing crate 0.2.0/options, edition 2024, MSRV 1.95, exact rustfmt
  1.9.0 and pinned Nix shell; Ruby 3.3.10/Bundler 4.0.23; generator lock SHA-256
  `061f5e4e0f3cb48d529a7914eb087cabda9889d4200a1af9d0d70af7908b5459`.
  Copied runtime SHA-256 stays
  `9c50b8167a8b82118ba42372633e3b004276ba49fbdfed75d4979a913feea739`;
  shared-schema identity stays
  `d704e6c155f9f2ec82bdf627857bdc23aa08a1d2133806df1f8ed5beb2d8c439`.

There is no handwritten API/client feature, generator/runtime modification,
dependency update, version bump, tag, publication or frontend change. Implementer1
owns the short Git mutation windows in these two session worktrees; no other
owner is assigned overlapping files. HaveAPI remains a pinned tool checkout,
and TypeScript remains unchanged under its completed no-change proof.

### Compatibility and recovery invariants

The bindings add optional GET Index calls for the administrator-only incident
policy evaluation history and exposure overview. Generated membership does not
establish deployed resource availability, caller permissions or data visibility.
Existing server authorization, ownership rules, filters, response types and
pagination metadata remain authoritative. Consumers must check deployed server
capabilities before enabling new calls; do not add fallback requests or enable
these calls automatically. Old clients can keep their existing calls against
the compatible API, and new clients can use existing calls against older API
installations. New methods require backend support and authorization.

Preserve every existing generated action/input/output and runtime behavior.
Go's public Client gains resource fields, so retain its existing constructor and
accessor usage; do not promise compatibility for arbitrary unkeyed composite
literals of expanded exported structs. Go scalar/null limitations, Rust optional
values, authentication, retries and transport behavior remain unchanged.
No database, on-disk application state, node protocol or migration changes.

No deployment ordering is needed merely to store these bindings. Enabling the
new calls would require compatible backend deployment/capability checks, outside
this package. Recovery restores saved schema/provenance, generated output and
its input receipt together to a known consistent client commit; consumers may
pin the preceding client revision. Preserve published versions and tags. Neither
this brief nor client checks authorize integration or deployment.

### Acceptance, checks and review disposition

Before committing, verify the complete candidate/installed generated file sets
against C's existing hashes, the exact added/changed/removed inventory above,
raw receipts and retained pins. Any additional difference returns to lead;
do not resolve it by silently expanding scope. Record final base/head per
repository and update [client-assessment.md](client-assessment.md) with actual
results, not the obsolete initial no-change expectation.

Quick checks use the clients' own environments and existing contributor commands:

- Go `nix-shell`: schema preparation Python unit tests, formatting of the
  generated output, `go test ./...`, and declared commit hooks. Reuse the
  proved projection/candidate generation; compare installed bytes after copying.
- Rust `nix develop`: `cargo fmt --all -- --check`,
  `bash -n tools/regenerate`, `tools/check-provenance`,
  `python3 -B tools/test-provenance.py`, and final saved-input consistency with
  the documented generation/check contract. The existing complete candidate
  proof may be reused only with matching saved schema, generator lock/config,
  formatter, runtime and all output hashes; otherwise run the ordinary
  `tools/regenerate --check` once. Keep existing refusal checks; no new test
  framework or live fixture is needed for this mechanical refresh.

Commit one coherent schema/provenance/generated update per client, preserving
the generated/handwritten ownership boundary. Supply both complete branch
histories, final diffs, the single input-update stream per repository and an
explicit no-migrations/no-release/no-deployment inventory to the independent
reviewer. The mandatory-review skill permits genuinely mechanical generated or
metadata updates with no substantive changes to skip standalone content review;
this is a candidate for that exemption, not an architect waiver. The independent
reviewer determines the actual disposition and always concludes whole-branch
history/consolidation. Any substantive difference receives applicable content
review after commits and quick checks, before long verification.

After that review disposition, use normal exact-final-head CI for Rust
default/blocking tests, Rust 1.95 default/blocking MSRV, documentation, packaging,
and regeneration/refusal checks. The current `ci.yml` supplies these gates;
successful exact-head CI replaces duplicate local long runs. A missing gate
requires only its documented local command, not another complete campaign.
Go's offline tests and normal selected CI remain required. Use the monitor skill
for checks over one minute or of uncertain duration. No production requests,
new real-server acceptance campaign or fixture deployment is justified when
runtime and existing calls are unchanged.

Completion evidence must bind the final API export and exact client heads,
generation inputs, comparison maps, checks, review disposition and TypeScript's
separate no-change result. Implementation completion is distinct from integration;
all branches remain unmerged until explicit repository/target approval.

## Package A3: gate client synchronization on declared contract changes

**Release status:** sufficient settled brief, ready for lead acceptance and
allocation to implementer2. architect0 owns routine design clarification;
implementer2 owns the documentation patch, quick checks, commit and review
follow-up. Lead owns the short same-repository index/commit window and acceptance.
No source/export/generation investigation is needed for this package.

**Exact file boundary (vpsadmin):**

1. `docs/api-schema-export.md`: replace the opening blanket requirement under
   `Generated client synchronization` with the assessment/stop rule below; make
   the existing numbered export-and-sync workflow explicitly conditional on a
   declared-contract change. Align the short introductory pointer if needed.
   Retain the heading/anchor, exporter instructions and all downstream safeguards.
2. `AGENTS.md`: keep API work routed to the same authoritative section, but label
   the link `API contract assessment and client synchronization` (or equally
   clear wording). All API work, including behavior-only work, must read the
   assessment rule; that routing does not itself require exporting/regenerating.
   Do not copy the policy into the routing table or change unrelated rows.

The workspace verification procedure already links to the authoritative vpsadmin
section. No workspace feature edit, SDK edit, generator/tooling change, new test,
workflow, helper, dependency or release work is needed. This is a small prose
correction in the established contributor guide, not a new policy subsystem.

**Required policy semantics:**

- First inspect the complete task/branch base-to-head diff for declared API
  contract changes: resources, actions, input/output parameters, types, choices,
  nullability, defaults, routes, API/protocol versions and metadata that affects
  the exported contract. Follow relevant plugin, concern and dynamic declaration
  sources, including indirectly derived declarations; file location alone does
  not establish an unchanged contract.
- When that assessment establishes no declared-contract change, record one
  concise source-diff-based conclusion tied to exact base/head and relevant
  files/reason in existing task/review records, then stop client synchronization.
  Do not export schemas, create client worktrees, regenerate, compare or refresh
  clients solely because the implementation behavior changed. This conclusion
  is scoped to the task diff; it does not certify global client freshness.
- Existing unrelated baseline/client drift is separate scope and never a
  prerequisite to completing a declaration-neutral task. Do not turn a prior
  stale saved snapshot into a mandatory cleanup campaign.
- Runtime, authorization and behavior compatibility still need relevant
  assessment/tests. They do not trigger mechanical generation by themselves
  when the declared contract is unchanged. A behavior-dependent declaration
  must be assessed as a declaration, not hidden under that exception.
- If the diff leaves a concrete uncertainty, inspect the specific declaration
  path or use the smallest focused check that resolves it. Do not automatically
  export/regenerate every client as the uncertainty response. Record the reason
  if that narrow resolution establishes an actual contract change.
- For declared-contract changes retain the existing final clean-source export,
  raw provenance/lock/profile, all-client impact/synchronization and applicable
  checks, generated ownership, transformations, compatibility, recovery,
  integration approvals and separate publication/release rules. Scope any
  completion wording about all changed/unchanged clients to this conditional
  synchronization path. Do not weaken these protections.

**Acceptance and quick checks:** inspect the final prose against both outcomes:
a query-ordering-only change stops after the base/head source assessment; a
changed action/parameter or plugin/dynamic declaration enters the existing full
workflow. Confirm that prior unrelated Go/Rust drift does not obstruct this fix,
and that runtime compatibility duties remain. Review the complete two-file diff,
run `git diff --check`, verify existing Markdown link targets and retained
`generated-client-synchronization` anchor, and run declared commit hooks. No
new automated tests, schema exports, generator runs, DB setup or expensive checks.
These are manual policy/link checks, not an invented test framework.

**Existing evidence and review:** B owns API CI at
`da7724abdc080e59820cc4f0812ce1a41b3fc5df`. Record the docs follow-up's exact
parent/head and changed paths to prove API/runtime/spec/dependency/CI inputs are
unchanged, and reuse completed passing checks within their proven scope.
Do not represent tests at the parent as executed at the new head, and do not
automatically repeat the API/client matrices for this documentation-only patch.
The docs comparison is new evidence; mandatory independent final review of the
substantive policy change follows its commit and quick checks. Include the
whole final branch history/diff and no-migrations conclusion; lead chooses the
applicable review lanes. Any genuinely required unrun check remains explicit.

**Compatibility/recovery:** no API behavior, schema, persisted data, generated
client, protocol or deployment changes. This adjusts contributor effort and
completion scope while preserving contract-changing work's safeguards. Recovery
is an ordinary documentation revert; it has no data or process effects. No
integration, deployment, SDK update or session lifecycle operation is authorized.
The policy's authoritative home remains the existing vpsadmin guide for
contributors/reviewers; session-specific receipts and rationale stay here.
