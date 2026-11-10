# Rebase and deployment-doc refresh, 2026-11-02

Scope: rebase the registered configuration feature onto the actual remote default,
complete bounded deployment guidance in the existing operations pages, check/review,
then update the published feature with an exact lease. No master integration,
provisioning, credentials, deployment, live operations or lifecycle changes.

## Saved pre-rebase identities

- Worktree: `worktrees/2026-10-21-aitherdev-observability-access/vpsfree-cz-configuration`.
- Feature: `2026-10-21-aitherdev-observability-access`.
- Old base: `38e7c837893695999e588a73f5d2a0088b8257b1`.
- Old head: `d07b4251172020472b21e8830e92b023849d543f`.
- Old tree: `b19544c8db2097a2f98a20e5781d7f1f5c6ce6dd`.
- Remote feature/force-with-lease expected SHA:
  `d07b4251172020472b21e8830e92b023849d543f`.
- Actual remote default discovered by `git ls-remote --symref`: `refs/heads/master`.
- Fetched target: `c040c14cdbacc07998700b524996a89306188d7f`.
- Target includes 59 commits above the old base. Neither old feature commit is
  an ancestor of that target; the old base remains an ancestor. No merged history
  will be rewritten. Worktree/index were clean, branch/ref matched registration,
  remote used canonical SSH, and Overcommit hooks were active before mutation.
- Upstream changes among environment/configuration files include `flake.lock` and
  `Gemfile.lock`; this package does not select or edit input revisions.

Old complete feature series:

1. `bd54b28c63770b782a4af435ad8dfb9619b6032c` — logger access.
2. `d07b4251172020472b21e8830e92b023849d543f` — Prometheus query access.

Architect0 owns the bounded deployment-doc gap brief. Application behavior and
the existing accepted authorization/permission contracts remain the scope boundary.
No migrations are introduced or rewritten.

## Publication receipt, 2026-11-02

Published the reviewed and verified feature without further source changes.
Before publication, `dev-session current` matched the bound session, both optional
environment markers were absent, and the retained implementer access was
`workspace_write`. The canonical worktree and index were clean at
`9ad4f869699fee02e2bc4c8f3cceccdea95d8a29`, tree
`f96f6b549d94f4fb070ea72b068921e641f69bee`.

A fresh scoped `git fetch --no-tags origin` and
`git ls-remote --symref origin HEAD refs/heads/master refs/heads/2026-10-21-aitherdev-observability-access`
confirmed default `master` at `c040c14cdbacc07998700b524996a89306188d7f` and
the feature at the expected lease `d07b4251172020472b21e8830e92b023849d543f`.
The canonical remote remained
`git@github.com:vpsfreecz/vpsfree-cz-configuration.git`.

Executed from the canonical project worktree, with the active Overcommit
pre-push hook and no bypass:

```bash
nix develop --no-write-lock-file --command git push --set-upstream \
  --force-with-lease=refs/heads/2026-10-21-aitherdev-observability-access:d07b4251172020472b21e8830e92b023849d543f \
  origin \
  refs/heads/2026-10-21-aitherdev-observability-access:refs/heads/2026-10-21-aitherdev-observability-access
```

Post-push `ls-remote --symref` proved the feature at
`9ad4f869699fee02e2bc4c8f3cceccdea95d8a29` and default/master unchanged at
`c040c14cdbacc07998700b524996a89306188d7f`. Local upstream is
`origin/2026-10-21-aitherdev-observability-access`; `git rev-list --left-right --count HEAD...@{upstream}`
returned `0 0`, and worktree/index remained clean. No push process remains.

The only workflow, `daily-update.yml`, has scheduled/manual triggers and no
push trigger. `gh run list` for this exact feature branch returned `[]`;
there were no superseded runs to cancel and no workflow was dispatched.

Lead's final verification receipt confirms the unchanged logger VM passed at
this exact head (exit 0, 110 seconds), the exact proxy integration derivation
was valid, and both affected host builds passed. Earlier incomplete verification
and diagnosis remain historical evidence; no fixture or production fix was
needed after the controlled rerun.

Git ownership is released to the lead. The feature remains unmerged, ready and
awaiting merge approval. No deployment or live operation was performed in this
package; any earlier user rollout remains unknown and user-owned.

## Operator-guide simplification, awaiting review

On the lead's revised history instruction, amended only the owning docs commit:
published `9ad4f869699fee02e2bc4c8f3cceccdea95d8a29` becomes local
`98384b6b12fbc61c4df7c545d070cea446cc89bd` (tree
`51c606cbfec041e25b5b267216da6262e18708e5`). The first two implementation
commits remain exactly `5e15c92cb8a4cf42a6e97f9d2a447fef1734febf` and
`46bddfcdb0b5e1bfcc95edc98f1f8aa1f4c5cd21`, above base
`c040c14cdbacc07998700b524996a89306188d7f`. No migrations or implementation
changes. The entire delta from published head is the two operation pages:
logger +99/-81 lines, proxy +135/-221 lines, including moved sections.

The architect's simplification brief and lead's main prose pass are applied.
Setup comes first; interactive htpasswd and a private editor-written curl config
replace inline Python. Logger inventory review now uses `less` in the same root
terminal; its presence was checked in the exact previously built logger closure.

Quick checks passed: 16 shell snippets, local links, six bounded mocked restart
cases, interactive bcrypt creation/rotation and password verification, native
revocation, private directory/file modes, synthetic curl-config parsing with
Basic/HTTPS/5s/45s defaults, and diff whitespace. An initial probe-only unsupported
curl option was corrected; the documented commands never contained it.
Pinned `nix develop` amendment ran active Overcommit hooks: Nixfmt and commit-msg
checks passed, with advisory TextWidth warnings for two lines over 72 characters
(within the repository's 80-character limit). No VM or host build was repeated.

Worktree/index are clean. Source is frozen for independent follow-up review;
Git ownership returns to the lead. No push yet: the exact expected future lease
remains published `9ad4f869699fee02e2bc4c8f3cceccdea95d8a29`. No live credential
or provisioning command was run.

## Simplified guides published, 2026-11-02

Lead confirmed final review PASS at exact
`98384b6b12fbc61c4df7c545d070cea446cc89bd`, with no findings; see
[operator-simplicity-review.md](operator-simplicity-review.md). No further source
edits or tests followed. Binding, canonical SSH remote, frozen head and clean
worktree/index were verified. Fresh scoped fetch and `ls-remote --symref`
confirmed default/master `c040c14cdbacc07998700b524996a89306188d7f` and expected
feature lease `9ad4f869699fee02e2bc4c8f3cceccdea95d8a29`.

Executed with the pinned environment and active hooks, without bypass:

```sh
nix develop --no-write-lock-file --command git push --set-upstream \
  --force-with-lease=refs/heads/2026-10-21-aitherdev-observability-access:9ad4f869699fee02e2bc4c8f3cceccdea95d8a29 \
  origin \
  refs/heads/2026-10-21-aitherdev-observability-access:refs/heads/2026-10-21-aitherdev-observability-access
```

Push exited 0. Post-push remote proof shows the feature at
`98384b6b12fbc61c4df7c545d070cea446cc89bd` and actual default/master unchanged
at `c040c14cdbacc07998700b524996a89306188d7f`. Local tree/index remain clean;
upstream is the same origin feature, with ahead/behind `0 0`. Exact-branch
`gh run list` returned `[]`; nothing was canceled or dispatched. The known sole
workflow remains scheduled/manual only. Git ownership is released to the lead;
the session remains open and the feature awaits merge approval.
