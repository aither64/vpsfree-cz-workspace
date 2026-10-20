# Design and verification brief

Owner: main agent, substantive design/implementation at xhigh. Threadless external
initiative has no retained team; application edits stay with the lead.

## Boundaries and interface

A separate schema-1 commands.json file in the existing coordination store records
simple command execution and explicit reservations. The existing ledger remains
unchanged. Both paths use the existing ledger mutex for resource admission. New
commands resolve repository common directories/canonical remotes and machine IDs
through the existing catalog. No new hook adapters or trust stores are introduced.

CLI: coordination run SESSION --as-is --request FILE [--background], command-status,
command-log, command-cancel, command-resolve, machine-reserve and machine-release.
Requests are schema 1 with caller UUID requestId. Run requests name argv, cwd,
repositories, machines and label. Exact UUID retries never execute again. Machine
reservations use the same canonical physical ID as old reservations. Normal
nonzero exit logs failure and releases execution resources. Signal or missing
completion is interrupted and retains exclusion until explicit owner resolution.
Resolution records the owner's note and never changes interruption into success.

All commands execute as independent systemd user workers. Attached invocation
waits for the same operation and returns its command exit status; interruption of
the caller does not stop the worker. Commands supply their own environment setup
(e.g. nix develop --command ...); no environment dumps or automatic dependency
setup. The CLI transports its PATH to the worker without persisting environment
values. Cancellation before execution is settled; cancellation after start is an
interruption until inspection. Private command logs reuse bounded initial/tail
capture and drain both streams.

A live command context permits workspace-host's ordinary profile switch while
holding the canonical profile machine resource and an explicit reservation.
Package preparation/activation and forward recovery stay host-owned. Activation
must retain its exact candidate in the host's activation journal; generic command
results never certify deployment effects.

## Compatibility and invariants

New command state is additive, bounded and advertises a separate package
capability. Old job/snapshot/attempt/integration formats are unchanged. New and
legacy resource admission inspect both stores under one mutex. Legacy workers
already admitted retain their old claims. No new legacy workflow may start;
existing run/job continuations and exact receipts remain supported. No operations
are recovered or rewritten by this initiative.

Lifecycle fencing cancels waiting commands, refuses running/interrupted commands,
and releases new reservations only on successful archive completion. Deletion
must retain held reservations under its existing policy. Package checks require
the command capability whenever command state exists; active package roots remain
retained. Suspension and unregister see both stores. Explicit reservation release
requires its owner and no live command on the machine; no merge proofs are added.

The trusted local operator owns arbitrary command execution. Remote portal APIs
remain read-only for these commands. Existing remote authentication/authorization
is unchanged. Session incarnation, package generation, directory identity,
idempotency and concurrent access are validated as ordinary correctness boundaries.

## Storage, docs and delivery

No generated feature/target worktrees or prepared hook roots on the new path.
Only bounded records/logs and necessary worker runtime roots are retained.
Extend existing read-only Operations status to show new commands/reservations.
Generic coordination guides own the contract; workspace procedures adopt wrappers
while preserving explicit merge/deployment approval and independent review rules.
The existing integration guide is installed for legacy recovery.

## Checks

Quick: Ruby syntax and focused command tests (execution/result, retries, failures,
locks, reservations, interrupts, lifecycle and compatibility), affected existing
suites, Go/browser checks when UI types change, whitespace check. Commit all
intended content, inventory full branches and no-migration provenance, then run
mandatory independent review. Longer: packaged Ruby shards, systemd focused
integration, disposable signed Overcommit fixtures and command disk/latency
checks. Utility watcher owns long/uncertain checks. Runtime selection follows the
separately authorized rollout below; master integration remains outside scope.
Recovery preserves original state and selects a compatible forward
package rather than deleting records or rolling back.

## Authorized aitherdev rollout

The user subsequently authorized deploying aitherdev through
vpsfree-cz-configuration and verifying operation. Prepare matching exact published
runtime pins in the workspace's nested input and configuration's existing
dev-workspace/devWorkspace channel. Preserve extension and sibling inputs. The
installed profile and system currently use baseline 74ff349, an ancestor of the
candidate, so the rollout preserves deployed source behavior. Source and pins
remain on feature branches; no master integration was authorized.

Use the selected predecessor's supported coordination for the first system switch
and composed user-profile activation. Keep the original reservation and jobs for
recovery; no direct activation or fabricated owner is permitted. The existing
threadless initiative may need its normal retained-tracking conversation creation
path to obtain an ordinary owned admission identity, without selecting a team or
adding members. Validate that path before mutation. Initial bootstrap is not a
general transition route for an existing ledger.

After quick checks and applicable independent review, build/copy aitherdev and the
composed application outside claims. Dry activation and no-reboot switch precede
profile activation under the same canonical machine reservation. Preserve active
Codex/tmux consumers and forward recovery. Verify system/profile identities,
service and portal/router health, command capability, and an owned disposable
command's log/status/failure behavior. Keep rollout receipts and exact revisions
in the initiative; preserve machine ownership during user review.
