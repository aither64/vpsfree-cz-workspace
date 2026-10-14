# Integration performance design and verification brief

The lead owns this brief and application edits; no retained team is configured.
The trusted local operator boundary applies. Remote portal clients remain
untrusted; the new integration interface is CLI-only.

## Interfaces and execution

Add coordination integrate, integration-status, integration-resume and submit-batch.
Run requests carry schema 1, request UUID, mode, ordered repository operations,
dependency IDs, review/check references and actual user approval sources. Optional
deployment/finish sections provide their independent approval and acceptance.
Installed integrationConfig recipes name immutable protocol-1 executables; the
generic package defaults to an empty integration catalog. The extension supplies
confctl and nested-Nix-input refresh recipes, configured by the workspace.

Driver journals live privately under coordination/integrations, have an exclusive
per-run lock, and persist each request identity before calling existing engine
operations. Resume inspects retained receipts/jobs; never blind-replays effects.
Status includes phase, outcome, jobs, exact final heads, phase durations, queue
duration and evidence references. All related merge snapshots are admitted in
one ledger transaction; normal worker resources, dependency rules and FIFO remain.
Refresh only clean owned feature worktrees and certified mechanical changes.
Preserve original refs and use exact publication leases. Stop for review or
approval changes. Completion updates only owned tracking paths using real hooks.

## Admission and notifications

Ordinary coordinator admission and worker admission use a shared session lock;
lifecycle mutations retain exclusive locks. Logical writes stay under the ledger
mutex with expected revision/idempotency. Admission timeout defaults to 30s,
zero is nonblocking, and monotonic polling is cancelable before the callback.
Diagnostics are optional, never ownership proof. Notifications run in a separate
per-owner worker, retaining shared generation/session protection through native
RPC, immutable options/message identity and original ambiguity reconciliation.
Scheduling and ordinary coordinator commands do not wait on notification RPC.

## Certification and compatibility

certified_equivalent binds owner, repository/target, original independent review,
old/new base/head, reconstruction/tree proof, migration conclusion and checks.
Only identical trees, non-substantive patch-preserving rebases, fully absorbed
patches and recipe-validated generated pins qualify. Stable patch IDs alone do
not prove equivalence. Reconstruct the candidate against the new base; refuse
reverted effects, merge transformations, conflict edits and migration changes.
Check reuse requires matching complete derivation/input identities, not SHAs.
Review and check reuse are separate. Exact final self.rev machine preparation
remains required when its derivation changes. Existing reviewed_change remains.
No ledger, snapshot or attempt migrations. Pending driver runs require package
integration capability; ordinary predecessor jobs remain recoverable. Profile
failure recovery remains forward-only. No DB, vpsAdminOS or service wire changes.

## Verification packaging

Ruby checks become independent cached derivations whose explicit inputs include
commands, helpers, fixtures, contracts and tools. Package verification still gates
on all checks. Export checks via flake/passthru. Session suite: four processes;
coordination suite: two; whole-suite loading preserves helper definitions.
Partition by deterministic test identity and assert discovered/executed manifest
equality. Each process gets isolated HOME/temp/state. Add per-test timing and an
unsharded diagnostic mode; replace unrelated fixed sleeps with readiness signals.
Portal-only edits preserve Ruby check derivations; Ruby inputs invalidate them.

## Acceptance, rollout and recovery

Quick checks: syntax, focused admission/batch/driver/certificate/shard tests and
Nix evaluation/source-filter contract tests. Final review covers complete branch
history, no migrations, concurrency, ordering and cross-package compatibility.
Long checks: full cached/sharded package suite, browser regression, extension and
workspace contracts, aitherdev build, existing host/package transition tests,
disposable integration scenarios, three comparable performance runs. Watchers
follow installed Luna/low policy and preserve command status/owned log handles.
Deploy via existing system-then-profile jobs after review; use the installed new
driver only after its package is selected. Integration remains separately gated.
Retain prior sources/artifacts, original reservation and uncertain claims. No
archive/delete, forced release, direct bypass or backward profile recovery.
