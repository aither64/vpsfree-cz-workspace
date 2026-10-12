# Explicit archive policy and verification brief

Lead-owned design, substantive work at xhigh. The local operator is trusted;
retain protection against wrong session selection, concurrent writers, data loss
and interrupted operations, not hypothetical hostile-local-operator boundaries.

## Lifecycle and interfaces

Normal CLI and portal archival select the explicit policy. Automatic worker
always selects completion proof; existing pending operations resume their saved
policy. Add neutral archived lifecycle. Preserve old complete/abandoned formats
and discard semantics. New explicit archive journals and recovery sidecars are
versioned. Ordinary ready manifests for explicit archives use a new supported
version so missing unavailable final heads are honest and old readers fail closed.

Reuse the existing archive phase, tracking digest, commit and runtime retirement
owners rather than introducing an independent lifecycle transaction. Explicit
preflight cancels owned running turns and holds queued submissions, retaining
records. It snapshots after quiescence and removes dirty checkouts forcefully.

## Local recovery

Private workspace-scoped recovery stores a complete checkout filesystem copy
excluding Git administration plus index/operation state. Pin checkout HEAD and
index objects locally, without fetching/publishing. Staged, unstaged, untracked,
ignored and binary contents remain recoverable. Snapshot integrity is checked
before deletion; clean/merge/ref status never gates explicit closure. Missing
registered refs without a checkout omit a final head. Exact canonical checkout
ownership still governs destructive removal.

Revival recreates checkout paths from retained commits, restores index and
working files, then restarts the retained conversation. Snapshot and restore are
journaled and idempotent; partial removals/recreates retain positive evidence.
No worktree remains after successful explicit archival. Existing Git branches
and private recovery remain retained.

## Automatic policy

Each registration proves its exact local/remote head against its own recorded
default_branch, which is an integration target rather than repository-wide
origin/HEAD. Auxiliary checkouts select a qualifying registered target, preferring
origin/HEAD when included and otherwise sorting names. No registered target uses
origin/HEAD as fallback. Retry always reproves the selected sealed target.

## Compatibility, rollout and recovery

Keep existing journals unchanged and finish pending operations before package
switches. Read old and new manifests/journals. No database or node migration;
only aitherdev host/application update. Configuration uses its dev-workspace
channel; workspace uses its direct nested runtime override. Verify their composed
contract. Dry-activate/switch host, switch application user profile, verify live
assets and lifecycle operation. Application recovery is forward-only. Default
integration remains unauthorized. The original session's explicit archive is
authorized by the accepted plan; this implementation initiative stays open.

## Acceptance and checks

Quick syntax and focused aggregate Ruby/Go/browser contract checks precede
committed independent review. Then packaged tests, browser lifecycle exercises,
host build and rollout use fresh utility watchers. Cover mixed integration
targets, missing publication/ref obligations, dirty/index/untracked/ignored
files, detached/index blob retention, cancellation/queue preservation, retries
at capture/removal/move/commit/retirement/restore, legacy journal recovery and
automatic refusals. Verify real requested archival removes all ten checkouts.


A session created without Codex may have an exactly owned tmux terminal. Explicit
archive validates normalized threadless tracking and rejects contradictory Codex
identity while retaining that terminal through capture and tracking commit. It obtains
full conversation absence proof; it never adopts a conversation from the terminal or shared working path.

Final retirement ignores SIGHUP only for the exact caller terminal while completing
the archive journal, then restores its prior signal handler. A closed terminal's
final status write may be dropped after successful completion. All filesystem,
Git and lifecycle errors retain their ordinary refusal/recovery behavior.


Fresh explicit capture is journaled before full conversation absence observation,
which runs before every destructive checkout phase. Unknown conversation proof
leaves captures/journal retryable with the original worktrees intact. Both Ruby
and Go validate a positively owned threadless terminal; automatic observation
still requires terminal/authority absence. Closed caller-terminal phase output
cannot abort final journal cleanup, while storage/Git failures still propagate.

## Artifact metadata prevention (user-requested scope extension)

The network-ipv4-left-counter thread prepended three uncommitted artifact entries
with name captions instead of label. The existing strict Go and Ruby readers
reject this presentation-field mismatch and disable normal session access. There
is currently no typed artifact writer; agents edit the YAML directly. The user
explicitly requested correcting this record and preventing recurrence.

Add matching name-as-label reads in Go/Ruby, retaining label as the canonical
written field and preserving path confinement, explicit scope and all identity
validation. Add dev-session artifact add SLUG PATH --label TEXT --as-is as a
locked, generation-checked, fully validated atomic manifest update. It updates
normalized existing paths without duplication, refuses pending lifecycle/creation
operations and never starts a session or changes repositories/conversations.
Document the command in the session guide/documentation skill and site procedure.
Repair only the three specified caption keys in the selected record. No automatic
repair of arbitrary identity metadata; no schema bump or new persisted format.
Old executors read every newly written canonical manifest. Aliases supplied by
hand remain a forward-readable input extension; canonical writers remove them.
Quick checks cover shared Go/Ruby alias fixtures, unsafe paths and caption
precedence, update/insert without scope loss, failed update leaving bytes unchanged,
operation exclusion and CLI parsing. New public mutation/interface requires
affected independent review before final long checks and deployment.
