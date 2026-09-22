# Phase 2B.2 host registration design

## Scope and commit boundary

Phase 2B.2 is one generic commit, `host: register pinned agent teams with
Codex`. It wires the Phase 2B.1 registration helper into App Server launch,
records the exact semantic plan, and makes forward package switching reconcile
that plan. Managed creation, UI, ordinary managed sends, team transitions,
member observation, lifecycle release, migration execution and downstream pins
remain out of scope.

Affected generic files are limited to `libexec/workspace-host`, the runtime
contract/projection, workspace-host and focused command tests, and Nix package
wiring. The existing systemd unit continues delegating to `run-codex`; no
configuration argv is embedded in systemd or global Codex configuration.

## Shared contract

Runtime contract adds exact `agentTeamRegistration`:

```json
{
  "helperSchema": 1,
  "policy": 1,
  "markerSchema": 1,
  "pendingSchema": 1,
  "maxOutputBytes": 4194304,
  "migrationJournalSuffix": ".agent-teams-migration.json"
}
```

Go projects and validates this object and asserts helper/policy parity with the
agent-team package constants. Ruby validates the same exact object when loading
the runtime contract. The migration suffix is only reserved and detected in
this slice; Phase 2D owns its schema and execution.

## Registration helper boundary

For a registry entry, Ruby invokes the selected package directly, without a
shell:

```text
PACKAGE/bin/workspace-portal agent-teams registration
  --package-root REAL_PACKAGE
  --state-root STATE_ROOT
  --workspace WORKSPACE_ROOT
```

Stdin is exactly `{"schema":1}\n`. Stdout is capped at 4 MiB and must contain
only exact keys `argv`, `digest`, `policy`,
`required_native_child_threads`, `schema`, and `states`.

Ruby validates schema/policy, lowercase 64-hex digest, string argv with no NUL,
the 256 KiB argv+NUL aggregate bound, capacity 0..64 and at most 512 sorted,
unique state inventory entries for the requested canonical workspace. State
entries retain the exact Phase 2B.1 response shape and bounded identity/revision
fields. The Go helper remains the only authority for state discovery, strict
state/catalog validation and exact retained-root verification; Ruby does not
infer pins from manifests.

## Runtime marker

Each workspace's existing private runtime directory owns `registration.json`,
written as an atomic, mode-0600, no-symlink file with parent fsync. Runtime
quarantine/removal therefore owns this operational evidence; it never appears
as content in the source workspace. Exact schema:

```text
schema: 1
workspace: { name, root }
launch: {
  codex_path, package_root, policy, digest, argv,
  required_native_child_threads
}
validated_inventory: { package_root, states }
```

`launch` describes the actual exec. `validated_inventory` records the latest
helper-verified current durable inventory. An inventory-only change with the
same semantic digest refreshes that field atomically without restarting App
Server. Inventory is audit/validation evidence, not restart identity. A missing
or malformed marker requires restart; an unsafe marker path is a hard error.

`run_codex` obtains the current plan, writes marker intent, then executes:

```text
active_codex PLAN_ARGV... app-server --listen SOCKET
```

Root `-c` options precede the App Server subcommand. Helper or marker failure
prevents service startup. Later managed creation may trust the marker only when
the expected socket/service is also live.

## Pending reconciliation record

The old plaintext pending file is replaced by atomic mode-0600 strict JSON:

```text
schema: 1
package_root
codex_path
workspaces: [ { name, root, registration_digest } ... ]
```

Workspaces are sorted by name. The record is only a retry target; reconciliation
always recomputes current plans and roots rather than trusting stored argv or
inventory. Unknown/legacy pending bytes are a forward-migration precondition
error. Deployment drains the old pending record while sessions are idle.

## Reconciliation and restart matrix

Compute the desired plan for every registered workspace before deciding:

- same binary and every semantic digest equal: no restart, refresh inventories;
- same binary and any digest differs: quiesce and restart all Codex/portal
  consumers once;
- different binary and equal digests: restart once;
- binary and digests differ: restart once;
- missing or malformed marker: restart.

State revision or full inventory equality never controls restart. Before a
restart, run the existing Codex contract check and one no-inference App Server
launch probe for each unique desired semantic digest with its exact argv.

Busy quiesce writes the versioned pending target and preserves existing defer
semantics. Successful restart waits for sockets, rereads every marker and
requires exact Codex path plus desired semantic digest before clearing pending
and restoring terminals. Partial failure stays on the selected forward package
with quiesced/pending evidence.

## Forward package switching

Under the existing generation/transition lock:

1. refuse any open creation, lifecycle or migration journal;
2. build the candidate;
3. run the candidate registration helper for every workspace against current
   durable state/roots;
4. probe unique candidate argvs;
5. unconditionally quiesce sessions before profile mutation, even if semantic
   digests match;
6. select/install/activate the candidate;
7. reconcile/restart according to the matrix; and
8. restore clients only after exact marker/socket verification.

Every `state=creating` creation journal is open, including records without a
tmux identity. Existing lifecycle/fork/start operations remain blockers. Any
file with the reserved migration suffix is a blocker. Unknown or malformed
current creation JSON fails closed; completed ready journals remain allowed.

No old-target check is added. Explicit `workspace-host rollback` refuses with a
forward-only diagnostic. After profile mutation, failures never compensate into
an older package; they keep the selected candidate and forward-recovery evidence
for rerunning the same or newer switch/reconcile.

The first aitherdev transition into the Phase 2B.2 package is necessarily driven
by the pre-2B.2 host. Its old switch path still contains rollback compensation,
so deployment uses an explicit one-time operator bootstrap: verify every session
idle, quiesce portal/App Server services, select and activate the new profile
forward, then let the new registration reconciliation restart and verify the
private markers. Do not claim that the new forward-only switch governs its own
initial installation.

## Nix packaging and tests

No new runtime dependency is needed: the host calls the selected package's
installed helper, Ruby `Digest` is standard library, and Nix is already present.
Post-fixup smoke asserts `bin/workspace-portal` is executable, invokes the
installed registration helper against an empty private state/workspace, and
checks exact schema/policy/digest/inventory output.

Focused tests cover:

- exact helper flags/stdin, output bounds/shape and option ordering;
- marker permissions, atomic/no-follow behavior and inventory-only refresh;
- malformed/oversize output and invalid/unsorted/duplicate inventory;
- restart matrix and strict pending-record recomputation;
- partial restart marker verification and fail-closed startup;
- creation/lifecycle/migration journal blockers;
- candidate validation before profile mutation and unconditional quiesce;
- refusal of rollback and absence of post-mutation compensation to old code;
- runtime-contract field/parity and unchanged registration response.

Quick checks use focused workspace-host Ruby tests plus Go agent-team/portal
command tests. Every test wait is delegated to a fresh Luna/low watcher.
Mandatory review follows the complete Phase 2B commit series; long packaged and
deployment verification remains behind that review.
