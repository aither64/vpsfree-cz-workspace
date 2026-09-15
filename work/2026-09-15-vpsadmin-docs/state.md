---
lifecycle: active
---

# vpsAdmin documentation assessment

## Current status

Proposal prepared: ordinary Markdown with `docs/README.md` as the index;
defer MkDocs until rendering is needed. No project files changed, no feature
branch/worktree created, and nothing pushed or deployed.

## Next actions

If implementation is requested, create/register this slug's vpsAdmin worktree
from freshly fetched upstream master. Follow [plan.md](plan.md), verify
retained claims against current code, convert selected pages, update links,
apply writing conventions, and run mandatory review.

## Repositories and session

- Initiative: `2026-09-15-vpsadmin-docs`; `dev-session current` matched
  `DEV_SESSION_SLUG`. No project branches or owned worktrees.
- Reference: `/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin.git` at fetched
  `origin/master` revision `f8fb5b3af225f20b40ad16df49d4f4ceca68fcf7`.
  Bare local `master` is older; use `origin/master` for follow-up work.

## Documentation and findings

Read repository README/AGENTS, docs index/build instructions, architecture,
transactions, lifetimes, plugins, networking, VPS, storage, branching,
download, and v3.0 transition material. The proposal is in [plan.md](plan.md);
project edits are outside this recommendation turn.

- `.mdwn` files mix Markdown with ikiwiki links, formatting, and UML directives.
  Conversion alone would preserve outdated technical content.
- Overview/index describe OpenVZ and vpsAdmind; current components are
  nodectld/libnodectld on vpsAdminOS.
- Shaping docs describe per-IP HTB rules on `venet0`; current
  `libnodectld/lib/nodectld/shaper.rb` configures CAKE on host interfaces.
- VPS dataset docs describe `vzctl` paths. Console docs require a `vzctl`
  patch, while the current console wrapper invokes `osctl`.
- Lifetimes and plugin loading retain recognizable concepts. Storage,
  branching, and downloads contain substantial information to check and keep.
  `i18n-cs.md` was updated in September 2026; retain its current path.
- Release material ends at the v3.0 OpenVZ-to-vpsAdminOS transition and includes
  one-off migration scripts. Recommend removal after a final consumer check.
- Official MkDocs guidance confirms reuse of `.md` links and README indexes:
  <https://www.mkdocs.org/user-guide/writing-your-docs/>.

## Commands and verification

- Checked current session/environment, workspace status/index, and portal URL.
- Fetched vpsAdmin master into `refs/remotes/origin/master`; inspected source
  using `git ls-tree`, `git show`, `git grep`, and `git log`.
- Inspected current lifetime module, plugin loader, shaper, and console wrapper.
- Fetched workspace origin; master and origin/master matched and index was
  empty before tracking preparation. No hook framework is declared at root.
- No application tests: source inspection and proposal only. Mandatory change
  review applies when project changes are implemented.

## Remaining uncertainty

Full verification of retained technical claims belongs to implementation;
this inspection establishes the format recommendation and stale areas.

## Session and cleanup

Session remains open and active. No lifecycle action or cleanup scheduled.
Unrelated shared workspace changes were preserved.

Stable portal:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-15-vpsadmin-docs/>.
