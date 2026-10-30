# Workspace storage retention

Archive deletes uncommitted checkout files and keeps committed Git heads. Its
tracking projection retains Markdown and portal.yml; commit project work and
write useful summaries before archiving. Historical Git objects and branches
remain available, but revival does not restore uncommitted changes from new
archives. Predecessor archives retain their recorded policy until compacted.

Additional workspace checkouts exclude work/ and archive/ through Git sparse
checkout. The registered shared checkout still contains session tracking. Nix
package and check inputs filter out those directories. Git archive exports use
.gitattributes; Nix Git fetches can also select `exportIgnore=1` to avoid copying
tracking into the initial flake source.

## Explicit maintenance

After deploying a runtime with archiveRecoveryPolicy 3, preview local cleanup:

```sh
bin/compact-session-storage \
  --workspace /home/aither/workspace/ai/vpsfree.cz \
  --runtime /home/aither/.local/state/dev-workspaces/profile \
  --authority /run/user/1000/dev-workspaces/vpsfree-cz/authority
```

Add --apply to perform the same selection. Use --recovery-only or --tracking-only
to limit the operation. The default state root is the user's XDG state directory
under dev-workspaces; --state selects disposable state for tests.

The script skips active tracking, busy sessions, unfinished lifecycle journals
and pending tracking sync. It takes the package transition and session locks.
Completed session-creation records (`SLUG.creation.json` with the matching slug
and `state: ready`) remain as historical metadata and do not block cleanup.
Incomplete, malformed or mismatched creation records still block that session;
a completed creation record never overrides an unfinished lifecycle operation.
Completed recovery inventories become committed-head metadata before their old
file/index payloads are removed. Git branches and committed objects remain.
Cleanup is irreversible for uncommitted files; there is no backup or artifact
store. Rerunning finishes leftover payload removal.

Historical tracked-file removals belong in an ordinary reviewed workspace
commit. They do not rewrite history. Do not run tracking cleanup on shared master
until that change has integration approval; recovery-only cleanup is independent.
Revival requires tracking edits to be committed before it accepts the cleaned
archive. Pending tracking transitions must finish before cleanup. Use the authority
directory of the registered workspace; a different path does not exclude its
lifecycle commands. Markdown links to removed raw artifacts remain historical
links.

Inspect coordinator storage using the selected runtime:

```sh
workspace-host coordination gc --dry-run --json --sizes
workspace-host coordination gc --dry-run --json --expire-unused
workspace-host coordination gc --apply --json --expire-unused
```

Unused preparations and orphan grace last 24 hours. Explicit expiration can
retire old unused leases sooner. Live jobs, reservations, recovery journals and
explicit holds retain their dependencies. Run ordinary Nix GC after root
collection to reclaim store data, and compare df before/after. Never delete
store paths directly. The runtime coordination guide owns the detailed policy.
