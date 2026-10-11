# Cluster controls: design and verification brief

The primary agent owns this design and all application edits. No retained team
exists for the externally created shell session. Read the plan for user choices.

## Portal and provider interface

Status schema 2 optionally carries `actions: ["start", "stop", "release"]`,
with the subset appropriate to the current state. The portal opts in via
DEVCLUSTER_PORTAL_CONTROLS=1 in the status helper environment. Old callers do not
receive the field; old helpers ignore the environment and omit it. Missing
actions mean legacy Release-only support. Explicit empty actions mean none.
Validate known unique actions, schema/found requirements and maintenance/state
consistency. Cached observations must not retain enabled actions when status is
busy or unavailable. Lifecycle and generation locks remain authoritative.

Providers advertise Start only when stopped and a retained configuration,
topology and network exist; running/stale state advertises Stop. Release remains
available unless a pending maintenance hold forbids ordinary reset. Pending
maintenance never advertises Start/Release. Missing selection requires CLI setup.

`start <slug> --existing` accepts no other options. Inside the existing helper
lock it refuses missing retained state/config/selection, then uses the recorded
topology and network with the ordinary Start implementation. No force, reset or
maintenance bypass is introduced. Normal CLI calls retain their prior defaults.

POST start-cluster/stop-cluster accept only kind and share the release-cluster
admission path. The configured provider owns the executable; the client cannot
choose commands, options or paths. A per-session/provider in-memory reservation
rejects overlapping browser requests instead of queuing them. Fresh status must
allow Start/Stop and opt-in Release. Provider CLI locking closes native races.
Start has a 30-minute operation deadline, Stop/Release 180 seconds. The server's
operation context ends work on shutdown, while a browser disconnect leaves the
admitted helper running. Process-group timeout cleanup follows existing code.
Failures invalidate stale cache and return conflict; the browser refreshes real
state and never automatically repeats a mutation.

## Browser layout and refresh

The top toolbar contains state and Ready plus visible icon/text Start/Stop and
Release buttons. Topology/network stay below. Credentials use fixed reveal and
copy columns with a flexible input; readable fields reserve the eye column.
The shared copy handler detects icon markup and restores its original accessible
label/title without changing the SVG. Feedback names the field, never its value.
Reveal updates title, aria-label and aria-pressed and swaps eye/eye-off SVGs.

Keep per-kind pending/progress/error state in browser memory. Allow normal
details refreshes, preserving selected service tabs and reapplying local pending
state after card replacement. Completion refreshes details, without page reload.
Unknown responses show errors and actual status; busy observations disable all
actions. Archived/noninteractive cards have no mutation controls. Phone layouts
wrap toolbar controls but retain horizontal credential actions.

## Compatibility, rollout and recovery

No persistent format, database, CLI default, catalog or runtime transition policy
changes. No migrations. Old/new provider-reader combinations are tested. Helpers
are deployed as one composed workspace application, with the matching host
runtime pin in configuration. Preserve exact rollback sources and generation IDs.
Provider source and maintenance compatibility still govern ordinary starts.
Stop/Start preserve disks; Release intentionally removes them after confirmation.

## Checks and acceptance

Quick: Go cluster/web behavior tests, JavaScript syntax/browser contracts, Ruby
provider status/start-selected cases, bash syntax and git diff --check. Fixtures
prove reserved copy alignment, repeated toggles, hidden copying, clipboard errors,
tab preservation, pending/error controls, concurrency, lifecycle admission,
deadline cleanup, missing selection, maintenance and old/new helper contracts.

After committed-deliverable review: Nix package checks and real Chromium/Firefox
portal fixtures with desktop/phone widths. Verify configured build/deploy contract,
host dry activation and user-profile switch, then use an owned disposable cluster
for Stop/Start/disk-retention/Release if its selected sources and binary cache
allow the build. Stop unexpected kernel builds and investigate under the
verification procedure. Do not operate on foreign live clusters.
