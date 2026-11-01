# Portal archive failure: unmanaged hook gem cache

Investigation date: 2026-10-25. Requested scope: investigate and suggest a durable
solution. No implementation, repair, retry or archival was performed.

## Confirmed cause

The failed worker ran the selected package
`/nix/store/48011krllhj3428878a8h55sb6x4wky0-dev-workspace-0.2.0`.
Its `ArchiveCleanup#walk_containers` in
`libexec/workspace-archive-cleanup.rb:610` walks everything beneath a session's
worktree group except verified canonical Git worktree roots. Outside those roots,
it accepts owned plain container directories but refuses every regular file or
symlink. The refusal at line 624 is deliberate. `clean: false`, used by explicit
archival, permits dirty checkouts but does not relax this structural rule.

The blocking path is
`worktrees/2026-10-22-haveapi-release/.haveapi-followups-hook-gems/bin/overcommit`.
The hidden cache is a sibling of the HaveAPI checkouts, not part of a registered
checkout. It contains 368 regular files in 53 subdirectories, 967,062 file bytes,
and no symlinks. Its five gem specifications identify Overcommit 0.73.0,
childprocess 5.1.0, iniparse 1.5.0, logger 1.7.0 and rexml 3.4.4. Files are mode
0444/0555 and directories 0555; they belong to the workspace user. The executable
is a generated RubyGems wrapper. These facts identify generated hook tooling;
the exact creation command and author were not established.

The installed cleanup source has SHA-256
`fd357da2e78890cd2a7f9046ee1f44dc4d192c8def4f44597e8499d4ea88568a`,
identical to local canonical dev-workspace master
`52dcd471186ef874c5c93f4133744195d4815454`. That establishes the source comparison,
not a fresh upstream check or the revision identity of every installed component.

## Failure ordering and impact

The actual systemd journal records the reported attempt from 15:42:38 through
15:43:04 CET on 2026-10-25, ending with status 1 and the same unmanaged-entry
error. The unit is
`workspace-archive-65ee298146b9072ffb04f24be709d295647ab36d951adce5fddbb15d1ebe85cc-1.service`.

In the installed executor, `quiesce_explicit_archive!` precedes
`cleanup.discover`. Discovery precedes publishing the cleanup sidecar and archive
journal and precedes checkout removal. At inspection there was only the creation
record for this slug under `worktrees/.locks/`; there was no archive journal or
cleanup sidecar. Tracking and worktrees remain present. This attempt therefore
failed before archive removal, although agent/goal/queue quiescing can already
have happened. No claim is made that all runtime state remained unchanged.

The portal's `startArchive` validates session/confirmation identity and starts a
supervised worker; it does not perform this filesystem discovery first.
The worker reports failures through a generic exit status plus recent logs.
Consequently a structural error appears as “Archive failed during starting”.
Retrying unchanged state reaches the same refusal. Adding a Git ignore rule or
changing file permissions does not change the discovery rule.

## Immediate recovery proposal

After checking that no active hook/build process depends on this copy, move the
cache inside its owning verified checkout, for example
`haveapi-followups/.gems-archive-cache`, or outside the worktree group to a
deliberately retained temporary location. Update any GEM_HOME/GEM_PATH or scripts
that still reference the old path if that tooling is to remain usable. Then use
the portal's ordinary archive retry. Inspect for further blockers; discovery
currently reports only its first one.

Moving is preferable to deleting an unreviewed tree. This is a proposed operator
repair, not an action taken during investigation. The read-only files also mean
ad hoc recursive deletion could encounter permission errors; permission changes
alone would not resolve the archive refusal.

## Durable solution proposal

The runtime should make explicit archival handle ordinary auxiliary session files
as part of its declared discard scope, rather than requiring cache-name-specific
exceptions or manual cleanup each time. Preserve canonical Git worktree discovery;
classify remaining owned regular files and directories as auxiliary data, include
them in the sealed cleanup inventory, and remove them through the same retryable
operation. Identify foreign or ambiguous Git repositories before treating a
directory as scratch. Keep path, wrong-repository and symlink-traversal refusals.
Do not replace the inventory with a blanket recursive deletion.

This proposal needs an intentional auxiliary-file retention contract matching
the selected explicit archive policy. The selected workspace currently documents
committed-head retention with uncommitted files discarded. Keep automatic and
`--require-merged` archival strict about undeclared leftovers unless that policy
is separately changed. Existing journals must resume their saved behavior;
extending the strict inventory schema requires explicit version/rollback handling.

Run read-only structural discovery before stopping agents or pausing goals, show
actionable blockers in the portal, and repeat validation under the lifecycle locks
before destructive work. A preview is advisory, not authority to reuse a stale
inventory. This addresses the present late failure even before auxiliary cleanup
support is implemented.

Prevent new misplaced caches by documenting and using checkout-local ignored
paths such as `haveapi-followups/.gems` for hook dependencies. Shared session
scratch should have an explicit lifecycle-owned location. The worktree group
should not be used casually as a general-purpose temporary directory.

Suggested implementation coverage: sibling hidden gem caches, read-only files
and directories, nested canonical checkouts, foreign/unregistered repositories,
symlink refusal, interruption during auxiliary removal, retry after partial
removal, strict automatic policy, old journals and supported package rollback,
and the packaged portal/systemd archive workflow. The prevention proposal has
not been implemented or integration-tested.

## Verification

[reproduce.rb](reproduce.rb) exercises the installed discovery class against a
disposable canonical Git repository. It creates no live session lifecycle
operation. It passed with exit 0: the sibling cache reproduced the exact error;
moving that fixture cache inside a verified checkout made discovery succeed;
a loose sibling symlink remained refused. Results are recorded in
[state.md](state.md). Temporary repositories are removed automatically. This
verifies discovery behavior only, not complete archive/revival or the proposed
future cleanup semantics.
