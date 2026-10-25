# Library lockfile instruction review packet

Requested result: record the user's library/application distinction in HaveAPI's
root instructions. Exact rule at AGENTS.md:34:

> Do not track dependency lockfiles for library components in Git. Application
> lockfiles may be tracked.

Repository `haveapi`, worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-library-lockfile-policy`, branch
`2026-10-24-haveapi-library-lockfile-policy`.
Complete review range: `67fcd34ba506264a5c7ee2e8e18a88d221c6f469..7ac977a26080d45d44b6608aafad2cadd2ec7f81`; tree `d92f9ecef3854b11d4f4d26106d524ff2d72758d`.
There is exactly one commit, `AGENTS: document library lockfile policy`, adding
only that paragraph (three inserted lines including separator) before Coding Style
inside Project Structure. Full series and binary/full-index diff are adjacent.
No obsolete unmerged history, repeated update streams, superseded approaches or
migrations. No application, protocol, state, package or dependency behavior changes.

The rule is independent of the architect's larger lock-removal design. Existing
library lockfiles are untouched by this bounded commit. No workflow, dependency,
test, generation-ban or bot policy change is included. Old91 supported integration
remains HOLD, and its clean detached b64 target and accepted artifacts are untouched.

Checks: ordinary diff/whitespace and added-line/message wrapping passed. Normal
checkout hooks and normal pre-commit/commit-msg hooks ran through the unchanged
qualified tool/Python/native-Ruff adapter and post-adapter own temporary directory.
Actual stdout/stderr/trace and environment paths are retained here. No hook bypass,
config/signature change, setup/native copy or functional test campaign occurred.
The final owned worktree/index/nonignored status is clean.

Risk LOW: localized instructions only; no runtime or persisted-state effect.
Mandatory final review is general lane only. Retained reviewer0 is verified ready,
review-purpose, gpt-6.1-sol/xhigh/read_only; preserve its saved settings. Lead is the
coordinating agent and assigns the review after this source/Git yield. Reviewer
must read ~/.codex/skills/mandatory-change-review/SKILL.md and its general reference,
inspect the complete committed range and exact user wording independently, and
report findings with explicit history/consolidation/no-migrations conclusions.
No default/backport/claim action follows until lead accepts review and routes it.

Workspace guidance read in this context: Git/worktrees, commits/hooks,
documentation, verification and sessions; HaveAPI AGENTS/development/releases.
Instructions are kept in the owning repository, where future edits discover them.
Shared state remains lead-owned. Source/Git and utility are yielded, session open.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/)
