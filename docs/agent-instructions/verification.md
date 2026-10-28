# Development environment and verification

Required workspace procedure, selected by the routing table in `AGENTS.md`.
Its rules retain workspace scope and precedence. Paths and commands are relative
to the coordination workspace unless the text specifies another repository.

For queued merges/deployments, complete builds, tests and review before running
the integration or activation command. Feature development, checks, review and CI monitoring require no repository claim;
only approved shared-branch integration and machine deployment acquire ownership;
retained snapshot-based operations keep their original submission contract. Resource contention is a wait, not a failed check. Follow
[coordination](../coordination.md) for waiting-session notifications and retained-job stale-snapshot
refresh; repeat only the checks/review required by the changed patch or baseline.

Use separately exported Ruby checks and retained derivation/input receipts to
reuse exact successful verification. Tree equality alone does not justify reuse.
The aggregate Ruby check must prove complete unique shard coverage; preserve the
unsharded diagnostic mode. Run independent checks concurrently where safe.
An integration driver that also approves/submits/activates operations is launched
by the lead. A verification utility may observe its independent logs/status; it
must not launch or resume that mutation driver itself.

## Delivery and scope checkpoints

Before detailed implementation or review, compare the actual user request and
subsequent scope decisions with the diffstat, working time and delivered result.
An internal plan or lead-approved design does not expand user authorization.
Inspect large handwritten growth or new subsystems early; generated output and
locks need context rather than a universal line-count limit.

Assess evidence within the current phase. Design progress includes resolved
constraints, narrowed alternatives with reasons, clarified invariants and
dependencies, and fewer open decisions. Implementation and verification have
their corresponding deliverables and results. Time, zero code, an absent design
file, waiting implementers or no preview alone do not prove a stall; a phase
label or growing document alone does not prove progress.

When visibility is insufficient, ask at the next safe boundary for learning,
settled and open decisions, dependencies and the next observable milestone.
Existing notes or a working draft can supply this checkpoint; no per-check
document or commit is required. Preserve the adequate design brief before
substantive implementation. Release packages only when their relevant interfaces
and cross-cutting invariants are stable. Do not freeze provisional assumptions
or defer authentication, permissions or other dependencies to keep implementers
busy without demonstrating safe independence and preserved user scope.

For small documentation changes and bounded fixes, reassess after 30 working
minutes without a delivered milestone, excluding idle time and human waits.
Name the remaining deliverable, necessary checks and shortest valid completion
path. Stop optional expansion and simplify automatically; ask only for genuine
product decisions or required approvals. Necessary long checks may continue
with a concrete risk and stopping condition. Treat later user additions as
separate milestones instead of holding completed work behind them.

Complex work uses task-specific milestones; observation cadence is not a
delivery deadline. Identify the relevant clock, respect gaps in timing coverage
and never sum overlapping member clocks. Missed milestones, repeated
investigation without new evidence, unexplained churn and settled independent
work withheld for optional exploration remain actionable. An extension needs a
concrete reason and next observable result.

Use one implementer for narrow work unless independent execution packages justify
more. Give complete packages with acceptance criteria; avoid per-command releases
and repeated status documents. Keep the existing team and ownership rules.

Independent review starts with scope and proportionality before detailed
hardening, even when an internal design already approved the mechanism. Prefer
conventional tools and smaller solutions; optional hardening is follow-up work.
Do not excuse defects inside the supported contract. Resolve observer concerns
with observed learning, simplification, delivery or verified dependency
necessity. Inspected design evidence can refute a mistaken stall premise
without code delivery; acknowledgment and reassuring summaries alone are
insufficient. Reassess new evidence under the same unresolved key and name the
remaining gap before repeating a concern. Missing essential context means the
assessment is unavailable, not that progress is healthy or stalled.

## Keep verification proportional

Plan a related batch around the delivery risk it resolves, its expected duration
and a stopping condition. Prefer established commands and compact evidence:
tested revision, command, result and log location. Add custom launchers,
manifests or approval chains only when a concrete operation needs them.

Repeat checks when relevant inputs change, an earlier failure remains unresolved,
or a required check has not run. Preserve successful evidence for its actual
scope, including required derivation/input receipts when reusing Nix results.
Ordinary Git index metadata changes are not source changes when logical staged
entries and flags are unchanged; investigate raw bytes only when their format
matters to the correctness question. Continue to protect owned paths, actual
source/input identity, concurrent edits and uncertain mutations.

When a batch exceeds its expected effort, reassess the shortest valid delivery
path before adding more verification. Time alone proves neither success nor
failure and does not waive required checks. Distinguish a product defect from a
verification-environment problem; fix the latter once and continue affected work.
Do not turn an incidental environment problem into a new development project.

A progress observer may challenge waste caused by mandatory rules. Name the
conflicting requirement and propose a correction rather than silently bypassing
it. Routine observations, evidence and lead responses are operational analysis;
they do not trigger independent change review or add an approval gate.

## Workspace runtime availability

Runtime development must keep the selected workspace usable. Run lifecycle,
collection, creation and naming tests against disposable state and sockets;
do not repoint them at the live registered workspace or restart its conversation
service for a fixture. Keep the selected package unchanged until the candidate
passes review and applicable checks. Source builds alone do not select a package.

For changes to coordinator locking, collection, session creation or naming,
verify session creation during an active collection sweep, required preparation
and package-switch exclusion, and creation when the naming backend fails. After
an authorized deployment, verify portal health, naming and conversation continuity
before calling the runtime usable. A transient model failure must not block work.

## Development Environment

The installed full-access execution policy applies to members and utilities.
Launch standalone CLI watchers with `--sandbox danger-full-access
--ask-for-approval never` explicitly. Do not add the root-owned Nix daemon socket
directory as a sandbox writable root. Resolve member failures to use Nix,
network or direct peer messaging instead of treating lead-only checks as normal.

Use the generic `dev-session-monitor` skill for authorized tests, CI checks and
builds expected to exceed one minute, and delegate uncertain-duration integration
tests and builds before launching them. Resolve the fresh verification watcher
from the installed catalog's separate utility policy. It is not a team member
and must not edit source, diagnose, retry, approve, or deploy.
Keep known quick checks inline. Resolve planning, implementation and diagnosis
settings from the retained team roster. Mandatory review uses an eligible
retained review-purpose member's saved model and effort; without one, use a
review-purpose role from the installed catalog's default development team in a
fresh standalone thread, including for solo sessions. Do not invent a team or
change the roster. Run final review only after the substantive deliverable is
complete, all intended changes are committed, and quick checks pass, before
long integration tests. Completed substantive documentation and configuration
deliverables remain in scope. Routine planning, investigation, findings,
session tracking and evidence alone never trigger automatic review. Earlier
review requires an explicit user request, is advisory, and does not replace
final review. A reviewer in a preset receives no automatic assignment. Pass
project escalation rules, including
unexpected local kernel builds, in the watcher's brief. The parent continues
automatically on completion or escalation. If the skill or delegation is
unavailable, report
that once and use minimal-output parent monitoring. A user's instruction not to
wait for CI takes precedence.

Development is generally Nix-based. Prefer each repository's `nix develop`,
`nix-shell`, flake outputs, or documented development shell before running
language-specific tools. Deployment is usually to NixOS or vpsAdminOS systems,
often through `confctl` and the configuration repositories.

Treat an unexpected local Linux kernel build in vpsAdminOS development or test
workflows as a bug unless the current work intentionally changes kernel sources
or configuration. vpsAdminOS kernels should normally be substituted from the
vpsAdminOS binary cache after GitHub Actions or its runners build them. When a
command starts building a kernel, stop it and investigate why the derivation
missed the cache. A local rebuild is acceptable only when the kernel or its
configuration is intentionally changed, or when the responsible runner has not
yet built and published the expected derivation; record the justification in
the initiative `state.md`.
If the work needs an additional kernel output, update the vpsAdminOS CI builder
to build and publish that output as part of the same initiative instead of
relying on recurring local builds.

When running `vpsadmin-devcluster`, use the bridge network by
default. Do not choose `--network local` unless the user explicitly asks for it
or the bridge network is genuinely unavailable; if local networking is used,
record the reason in the initiative state.

Use GitHub Actions as a feedback loop after pushing branches. If `gh` is not
available in the current shell, run it through Nix, for example
`nix shell nixpkgs#gh -c gh run list ...`. Inspect failed logs, monitor reruns,
and resolve failures instead of leaving CI for the user to chase.
Successful checks, review, and CI are verification evidence, not permission to
merge or push feature content to a default branch; follow the Git approval gate.
Before calling an unmerged feature branch ready, give the independent reviewer
its complete cleaned base-to-head commit series, final diff, and migration
provenance under the mandatory-change-review workflow. Require explicit
conclusions on obsolete history and migration lineage, including "no migrations"
when applicable.
Record findings and remaining deployment limits in the initiative state.

After a force-push or a follow-up fix push, cancel superseded queued or
in-progress GitHub Actions workflow runs for the same branch. Only cancel runs
whose `headSha` no longer matches the current branch head; do not cancel
workflows for other branches or workflows already running on the current head.

When creating or editing GitHub workflows, verify the latest upstream version of
each imported action from its official repository before choosing the `uses:`
ref. Do not rely on remembered version numbers; use the newest compatible
version unless the workflow records a specific reason to pin an older one.

Rerunning a failed GitHub Actions job is not a substitute for investigation.
Before accepting a rerun as validation, download or open the failed attempt's
logs and artifacts, identify the root cause as far as the available evidence
allows, and record the finding in the initiative `state.md`. If the artifacts
are insufficient, improve the test or runner diagnostics rather than treating a
green rerun as proof that the failure did not matter. Prefer fixing the
underlying problem; when the failure is unrelated to the current change, record
the evidence for that conclusion.

When a repository is missing a tool in the ambient shell, enter the repository's
Nix shell or use an appropriate `nix shell` command. Do not work around missing
tooling by recording local environment limitations in commit messages.

When adding new integration tests that use the vpsAdminOS test-runner, write
test scripts in the current RSpec-style structure with examples and
expectations, such as `describe`, `it`, and `expect`. Do not refactor existing
tests solely to convert their style unless the user explicitly asks for that
refactor.

## Disposable test data

Record temporary test and benchmark directories in the owning initiative. Stop
owned runners and guests through their native tools, then remove disposable
data when verification ends. Keep only compact evidence needed for review or
recovery. A dated pathname alone does not prove that another initiative has
retired its data.

Aitherdev's configuration-managed cleanup retains recognized completed
`/tmp/**/os-test-*` runs for seven inactive days. Active run locks, process
references and `.keep` markers preserve them. Ad hoc campaigns and benchmark
directories need explicit owner cleanup. New resource claims create no source/target snapshots. Its legacy
collector uses 24-hour preparation retention and preserves live recovery dependencies; use `workspace-host coordination gc --dry-run --json` to inspect its
reference decisions. See the configuration repository's
`docs/operations/aitherdev-disk-retention.md` for host policy and recovery.
