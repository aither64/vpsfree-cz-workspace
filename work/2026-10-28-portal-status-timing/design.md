# Private portal Codex state and 0.165 upgrade

Lead-owned implementation brief; no retained team exists for this initiative.

## Boundary and interfaces

The workspace registry name determines a private native home under
<user-state>/codex-homes/<name>. Never select it from inherited CODEX_HOME. Portal
services, CLI dispatch, tmux clients, native lifecycle/recovery helpers, naming,
provider probes and team/observer services receive the same home. Explicit
CODEX_SQLITE_HOME and native sqlite_home/log_dir overrides prevent configuration
from directing native writes back to stock state. Keep public sockets, URLs and
thread IDs unchanged. Native home/storage settings participate in launch identity,
so changing them requires the existing idle native transition.

New workspaces initialize private directories. Retained sessions require populated
private state and fail closed before starting an empty backend. Settings, login,
provider secrets and skills are independently provisioned for the portal. Ordinary
stock shell environments remain unchanged. Do not create a permanent migration
API, shared-home mode, cross-daemon router or replacement process manager.

## State conversion and recovery

A dated, detached operation inventories registered active/archived roots, retained
team threads and native descendants/fork/recovery dependencies. CWD is not ownership
proof. Unknown/unowned threads remain in stock. Schema-check exact native SQLite
files; partition records and preserve transcript bytes. Rewrite only structured
absolute storage paths/indexes. Keep receipts, timing, registry, lifecycle and
coordination storage outside the native home in place. Copy no runtime ownership
files or stock remote-control enrollment into portal.

Prepare staged stock/portal homes and independent portal login before maintenance.
Wait for all source writers to become idle, hold normal lifecycle/transition and
maintenance exclusions, stop source writers, make a consistent final snapshot,
validate history and partitions, then journal each rename/publication. Original
.codex remains a retained same-filesystem backup. Persist status, exact artifacts,
checksums, resume command and failure recovery outside both native process trees.
Before publication recover original service availability; after publication resume
forward. Never downgrade or restore stale backups over new writes.

## Compatibility and deployment

Upgrade portal native 0.164 to frozen 0.165 from llm-agents
91ff550fe42d4dd51dcf8b6bad87a0134fe7f314. codex-web retains strict 0.163 semantics
while adding prompted 0.165 naming support after exact source/schema/catalog checks.
Keep mkCodexPackage and existing submission/lifecycle/cluster schemas. New home
selection is deliberately incompatible with unconverted shared state. Installation
must refuse missing retained native data; old packages cannot safely select the
new layout. Recovery is forward-only. No fleet-wide node update is involved.

Publish dependencies before consumer pins. Preserve extension
767dfd587e346168e1443e65ccdb67ce748f3fe3. Build/review exact host and application
compositions. Hold vpsfree:aitherdev for activation and deployed lineage; activate
system configuration before application profile. No reboot or default-branch merge.

## Acceptance and checks

Quick: Ruby/Go regression checks for home derivation/propagation, startup refusal
and native identity; exact schema/request/config/catalog validation; composition
pin check. Commit intended changes, then independent whole-branch/migration review.
Long: packaged/native startup and saved-thread resume/fork, naming/provider/tmux,
migration fixtures for low disk, active writers, absent history, interrupted
publication/activation and idempotent resume. Recheck actual storage budget before
copying (40 GiB allowance plus 20 GiB free reserve; latest free estimate 94 GiB).

Live: inventory conservation, every owned thread readable, stock/portal writer
isolation, reported status/timing restored, team and disposable lifecycle smoke.
Reconcile original confctl receipt 2a2656f4-3d35-4bee-9a71-14e20bc35669 and transcript
before retrying `yes go ahead` through portal with retry=true and the same ID.
Do not infer delivery from a successful HTTP connection alone.

## Cutover integration with ordinary package activation

The selected switch requires its old App Server to remain queryable during idle
admission. Therefore a detached runner must not stop both servers and then call
switch: that would remove the evidence needed by normal transition checks.

Use a temporary, instance-specific systemd user ExecStartPre drop-in as the
one-time publication boundary. The detached outer job drains the stock daemon
with a single native graceful shutdown signal (never a forced timeout), then
calls the ordinary claimed profile switch while the old portal server remains
available for its idle/submission checks. The normal switch stops the old portal
native server. Only then does ExecStartPre verify no source writers, take the
consistent final copy, partition/validate and publish both homes before the new
native process starts. The drop-in and scripts belong solely to this rollout;
remove the hook after accepted activation, retaining source and journal.

The detached runner keeps ordinary lifecycle, coordinator and transition gates.
It must not simulate proof or edit package journals. Before profile selection,
a refusal restores the old service availability. Profile selection itself is a
forward-recovery boundary even if home publication has not occurred yet: retry
the same reviewed switch and publication journal. This refines the earlier
before/after-publication recovery shorthand to match the existing runtime's
forward-only contract. No temporary shared-home runtime mode is needed.
