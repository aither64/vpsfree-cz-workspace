# Risk and compatibility review

Lane: risk and compatibility
Model/effort: `gpt-5.6-sol`, `xhigh`

Reviewed the packet, plan, state, local repository guidance, commit history and
exact committed ranges:

- dev-workspace
  `8f75ece30462b184065f21867508af5e14365c4a..6735370851447ec62f6fbce25175c21db97c4686`
- vpsfree-dev-workspace
  `213a3db57dea9298f61309eb157c0853f2310e9b..67c217eb65f554b1d234a2e4ec69cdb8ab0fa9c2`
- workspace
  `ec3f99b42a7f6b850c3eb14219ae796ccacba98a..7a2e9caad9bd91bc4fd64f7c9f3830d8a9feeef8`
- vpsfree-cz-configuration
  `8ef765d339ac792ef4f01a5c7a160e48600adcaf..192e163ed71bcbeefcbc296691c03da6a2692087`

## Blocking

None.

## Important

None.

## Advisory

1. **A source page can load incompatible static modules if it straddles a
   rollback.** At dev-workspace commit `6735370`,
   `portal/internal/web/static/source-file.js:52-64` dynamically imports the
   unversioned `/static/review-editor.js` and unconditionally calls the newly
   added `clearLine()` method. If the new server returns the file API response,
   the profile is rolled back, and the dynamic import then reaches the retained
   old server, that server supplies the previous editor bundle without
   `clearLine()`. The page has already received the source bytes but ends in the
   outer error path with a JavaScript type error instead of rendering the cited
   line. This is a narrow availability issue during the deployment transition;
   it does not expose data or corrupt state. Make the call tolerant of the old
   editor interface, version the coupled assets, or explicitly accept that an
   in-flight source page must be reloaded after rollback. A browser test with a
   pre-change editor bundle would make the mixed-generation contract explicit.

## Security and data-safety assessment

No authorization bypass, path traversal, symlink escape, Git metadata exposure,
or secret-handling regression was found in the committed range. The host nginx
configuration applies Basic authentication to the whole virtual host, including
the new page and API routes. The server treats the repository ID and relative
path as selectors rather than authority: it resolves the ID against the current
session, revalidates the exact worktree root, canonical repository, checked-out
feature branch and locally available commit, then requires literal Git-index
membership. `openat2` confines the final read below the workspace without
following final or intermediate symlinks and rejects non-regular files. Output,
Git process concurrency and execution time are bounded. Errors returned to the
browser do not include Git diagnostics or host paths.

Archived reads use the manifest's immutable `final_head_sha`, verify an exact
regular blob with a literal `ls-tree` lookup, and never fall back to a moving
branch or missing live worktree. Artifact reads retain the existing manifest
catalog plus built-in `plan.md` and `state.md` authorization and use the same
confined regular-file opener. Binary, invalid UTF-8, oversized and excessive-line
content is classified without returning source text. Current-worktree reads can
naturally observe a mutable file while it is being edited; that is consistent
with the accepted live-link semantics and does not broaden the remote authority.

## Contracts, deployment and rollback

The `/files/<slug>` page and `GET /api/sessions/<slug>/file` response are additive.
They do not change manifests, lifecycle journals, persisted conversations, Codex
protocol messages, CLI behavior, Nix options or host state. Existing browsers and
old portal generations ignore the new API because no stored record requires it;
rolling back restores the previous 404/rendering behavior. Archived final heads
remain reachable under the workspace rule that retained feature branches are not
deleted during cleanup.

The reviewed dependency chain is internally consistent: both generic runtime
nodes in the workspace lock resolve to dev-workspace `6735370`, the organization
package resolves to `67c217e`, the workspace package resolves to `7a2e9ca`, and
the generated aitherdev host input resolves to the same generic `6735370`. The
host module and nginx route/authentication shape are unchanged. The recorded
user-profile package switch followed by configuration activation is compatible
with the existing generation model, and the previous user and system generations
remain sufficient for rollback because this change creates no new persistent
state. No vpsAdminOS node rollout or coordinated machine update is involved.

## Residual test gaps

- Full packaged and aitherdev configuration builds, dry activation, live browser
  checks and the authorized deployment were intentionally deferred until review
  findings are resolved.
- The focused tests cover invalid paths, tracked and staged files, symlinks,
  FIFOs, preview limits, missing active worktrees, moved archive branches and
  archived artifacts. The planned live checks still need to confirm proxy
  authentication, rendered HTML escaping, reload/back/new-tab behavior and line
  selection against the deployed package.
