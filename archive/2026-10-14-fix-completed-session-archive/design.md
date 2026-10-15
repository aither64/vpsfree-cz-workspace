# Completed-session explicit archive correction

The lead owns this bounded design and application edits. There is no retained
team roster; independent final review uses installed catalog fallback.

## Behavior and invariants

In DevSession::Runner#tracking_lifecycle_content, parse the anchored lifecycle
with the existing validator. Return the original object for a matching target.
For a different value accept current active or target archived; otherwise retain
the existing error. Within the matched anchored header substitute the actual
validated current value with target. This avoids changing lifecycle-looking body
text and retains LF/CRLF. All callers continue selecting their existing policies.

Explicit archival therefore accepts active, complete, abandoned and archived.
Strict completion and abandoned modes keep the active-to-terminal and matching
terminal transitions; other terminal-to-terminal conversions still refuse.
No new option, public interface, schema, migration or fallback path is introduced.

## Verification

Add conversion matrix coverage, valid-header LF/CRLF preservation and malformed
header rejection. Extend explicit archive/revive fixture coverage to completed
and abandoned sources, preserving staged/unstaged/untracked/ignored/binary local
contents and retained refs. Add completed-source interrupted explicit archive
retry evidence, retaining operation identity. Keep strict-policy tests intact.
Quick checks precede committed independent review. The review covers general,
architecture/repetition, scope/proportionality and risk/compatibility because
this is a destructive lifecycle/deployment path. The complete three-branch
series includes generated pins, no migrations and no superseded update streams.
Run full package and deployment checks only after review. No changed Go/browser
behavior requires a new protocol or interface test.

## Composition and rollout

Use the exact published runtime head in configuration's dev-workspace channel
devWorkspace role and workspace's direct nested vpsfree-dev-workspace/dev-workspace
override. Preserve extension, Codex, codex-web and unrelated dependencies.
Prepare system and composed application package outside execution claims.
Use one vpsfree:aitherdev reservation and ordered machine_activate then
profile_activate jobs. Verify both identities and service/conversation continuity.
Recover an interrupted activation through its original attempt; application
selection is forward-only. Existing lifecycle journals must finish before a
conflicting package switch. The format contract is unchanged by this fix.

## Acceptance

The installed helper converts the actual original complete state to archived
without changing its body. Ordinary explicit archive of the original slug then
finishes: committed archive tracking, archived lifecycle, worktrees removed,
refs and private recovery retained, conversations preserved, runtime retired,
and no unfinished archive journal. The real session stays archived; revival
is proven only with fixtures. Default-branch integration needs separate user
direction and the fix initiative/reservation remain open until then.
