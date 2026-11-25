# I0 instruction documentation evidence

## R1 remediation and final publication

Current stable source is released to the lead. R1's narrow remedy was accepted
by the lead after exact assertion inspection and the focused passing test.
No pending semantic changes, commands, history operations or remote effects.
The original evidence below records the pre-review I0 delivery; this section
supersedes its revision, owned-file and remaining-work summaries.

- Reviewed original range: base `8fe5976e926e7df0c3edca920618ff872abcc526`,
  I0 `acd8262f07ae3781f36b10c13e1bb924cc62c75b`,
  I1/head `6d9e28a585c30a497d86c963cb9666b04cb317c6`.
- Narrow fix commit before consolidation:
  `ccd93a8b341a309ae4007d352c8da2c0e7df3432`, parent old I1/head.
  Only `test/agent_instructions_test.rb` changed (+5/-5), at lines 122–123 and
  142–144. Five existing assertions now match package-wide assigned execution,
  no takeover on access/session failure, owner continuity after delivery,
  fallback only for a missing purpose within saved authority, and resolving or
  parking unavailable members instead of taking their work. Test/assertion count
  and the remaining contract assertions are preserved. No new harness or
  obsolete wording restoration.
- The original quick-check selection omitted this existing required Ruby test;
  the reviewer identified that gap. Required check source is the flake's
  `checks.x86_64-linux.agent-instructions`, which runs
  `ruby <workspaceSource>/test/agent_instructions_test.rb` with `pkgs.ruby`.
- Focused command, before and after consolidation:
  `nix shell --inputs-from . nixpkgs#ruby -c ruby test/agent_instructions_test.rb`.
  Both passed: 10 runs, 220 assertions, 0 failures/errors/skips. Latest seed 30072,
  test time 0.079202 seconds. Nix emitted a dirty-tree warning; Git status after
  consolidation reported a clean feature worktree. No package build was started.
- `git diff --check -- test/agent_instructions_test.rb` and staged
  `git diff --cached --check` passed before the fixup commit; final
  `git diff --check 8fe5976e926e7df0c3edca920618ff872abcc526 HEAD` passed.
- Following final reviewer delivery and the lead's history-window release,
  `env GIT_SEQUENCE_EDITOR=true git rebase -i --autosquash 8fe5976e926e7df0c3edca920618ff872abcc526`
  folded R1 into I0 without conflicts. New series, same base:
  I0/docs+test `4837004b8c1491b03d124f2dd26820f7073bd958`,
  I1/final head `d43347c1fd4f9ff9dfdf5c19f6cccb9531bbd639`.
- `git range-diff 8fe5976e926e7df0c3edca920618ff872abcc526..6d9e28a585c30a497d86c963cb9666b04cb317c6 8fe5976e926e7df0c3edca920618ff872abcc526..HEAD`
  shows only the five requested assertion replacements added to I0; I1 is `=`.
  Stable I1 patch ID from `git show --pretty=format: <I1> | git patch-id --stable`
  is `fd9f64a6824aa3811e6e5d05d01bcfeca3796621` for both old and new I1.
  `git diff --exit-code ccd93a8b341a309ae4007d352c8da2c0e7df3432 HEAD`
  passed: the final tree exactly equals the unrewritten remediation tree.
- Fetched origin, then published over existing SSH origin
  `git@github.com:aither64/vpsfree-cz-workspace.git` with an explicit lease:
  `git push --force-with-lease=refs/heads/2026-11-25-team-lead-delegation:6d9e28a585c30a497d86c963cb9666b04cb317c6 origin HEAD:refs/heads/2026-11-25-team-lead-delegation`.
  Push completed and fresh `git ls-remote --heads origin refs/heads/2026-11-25-team-lead-delegation`
  confirmed exact remote head `d43347c1fd4f9ff9dfdf5c19f6cccb9531bbd639`.
- `dev-session worktree capture-comparison 2026-11-25-team-lead-delegation workspace --as-is --base 8fe5976e926e7df0c3edca920618ff872abcc526 --head d43347c1fd4f9ff9dfdf5c19f6cccb9531bbd639`
  succeeded for those exact revisions.
- Post-push `nix shell --inputs-from . nixpkgs#gh -c gh run list --repo aither64/vpsfree-cz-workspace --branch 2026-11-25-team-lead-delegation --limit 100 --json databaseId,headSha,status`
  returned `[]`; no superseded workflow runs required cancellation.

Final history retains two focused packages and no fixup commit, obsolete
approach, repeated update stream or migrations. I1's semantic patch is unchanged.
All original mode, approval, monitoring, retained-settings and documentation
preservation conclusions remain applicable. R1 adds no behavior, migration,
deployment or saved-prompt change. No merge, deployment, roster mutation or
session lifecycle action was performed. Lead owns further build/integration
steps; this evidence update does not hold source delivery.

## Original I0 delivery

Package I0, implementer0, ready for lead acceptance. No prior package; capacity
confirmed before execution. Accepted brief: [design.md](design.md), package D.
No design deviations or blockers. Lead retains state/portal updates and review
invocation; implementer2 owns repository packet assembly.

## Revision and owned scope

- Repository/worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-team-lead-delegation/workspace`.
- Branch: `2026-11-25-team-lead-delegation`.
- Clean initial rebase: `09ea6f43a9ddd17317c0ae96481c46b0c1c24695`
  advanced to current shared master `8fe5976e926e7df0c3edca920618ff872abcc526`;
  no feature patch existed before the rebase. Relevant guidance was unchanged.
- I0 base: `8fe5976e926e7df0c3edca920618ff872abcc526`.
- I0 head: `acd8262f07ae3781f36b10c13e1bb924cc62c75b`.
- One commit: `Clarify delegated execution and lead acceptance boundaries`.
- Owned paths: `AGENTS.md` (+13/-9), `docs/agent-teams.md` (+63/-14),
  `docs/agent-instructions/verification.md` (+6/-1): 82 insertions, 24 deletions.
- Only these three paths were staged. I1's `config/agent-teams.nix` remained
  unstaged and preserved. Initial rebase and I0 commit windows are released;
  no further Git mutations by I0 while I1 executes its window.

## Checks and preservation

All checks below passed before commit; the staged check passed on the committed
content. No declared hook framework, configured `core.hooksPath` or active hook
was found; the ordinary hooks directory contains sample hooks only. Hooks were
not bypassed. No runtime/integration check is warranted by this documentation-only
package under D; no new test harness was added.

| Command or inspection | Result and scope |
| --- | --- |
| `git diff --check -- AGENTS.md docs/agent-teams.md docs/agent-instructions/verification.md` | Pass; I0 whitespace/errors. |
| `git diff --cached --check` | Pass; staged I0 commit content only. |
| `python3 - <<'PY'` local link/anchor inspection | Pass: all 28 local Markdown links/anchors across the three owned files resolve, and all prior heading anchors remain. Script reads Markdown links, skips external/mail links, checks relative destination files and Markdown heading slugs, and compares heading sets with `git show HEAD:<path>` before commit. |
| `git diff -- AGENTS.md docs/agent-teams.md docs/agent-instructions/verification.md` | Factual diff inspected against D: safety/approval, compatibility, mode, monitoring, final review and lifecycle requirements preserved. No sections moved or removed; headings preserved. |
| `git diff --stat -- AGENTS.md docs/agent-teams.md docs/agent-instructions/verification.md` | Three owned files, 82 insertions/24 deletions. |
| `git diff --cached --name-only` | Exactly the three owned files before commit. |
| `git status --short --branch` after commit | Only I1 config remained dirty; I0 content committed. |
| I1 config diff semantic read | No D mismatch identified. I1 evaluation checks were not repeated; their results remain I1-owned. |

## Semantic scenarios

Manual reading against the committed text establishes these instruction outcomes;
these are semantic checks, not claims of runtime enforcement.

| D scenario | Result / governing text |
| --- | --- |
| Full-team unclear diagnosis | Delegate bounded investigation once question/deliverable/owner/acceptance are known; role guide initial-triage paragraph. |
| Completed package missing evidence | Return specific gap to package owner; package workflow diagnosis/evidence paragraph. |
| Unchanged passing checks | No lead rerun for confidence; further assigned work needs contradictory evidence, changed inputs or a required unrun check; acceptance paragraph. |
| Busy/unready/blocked/inaccessible member | Resolve or explicitly park dependency; no absence/takeover exception. |
| Small edit with direct lead brief | Separate design document may be omitted; execution ownership remains mode-specific in AGENTS and guide. |
| Solo / Lead and reviewer | Lead still investigates, designs and implements; mode table and opening mode paragraphs preserved. |
| Lead-designed | Lead still owns substantive design; acceptance limits explicitly preserve mode-assigned lead design/implementation duties. |
| Safety and required writing | Lead retains approval interpretation, ownership/freshness checks, approval/submission/activation drivers and context-dependent writing; delegation grants no approval authority. |
| Retained prompts | Model/effort/access/instructions retained; actual conflicts escalated. Existing stock-observer refresh and custom-instruction exception preserved. |
| Observer duplication/capacity | Must cite concrete work, ownership and missing reason from existing evidence, allowing legitimate lead duties/blockers. Clocks, idle members and roster ready alone prove neither duplication nor capacity. |

## History, documentation and limits

I0 adds one focused instruction commit, with no obsolete intermediate approach,
repeated dependency/pin stream, migrations, generated changes or state format
changes. No migration has been merged, released, deployed or externally consumed
because none exists. Whole-branch history conclusion after I1 remains with the
packet owner and independent reviewer.

Documentation routing: team operating contract → agents/maintainers, procedural
reference → `docs/agent-teams.md`; concise mandatory entry point → `AGENTS.md`;
verification ownership cross-reference → `docs/agent-instructions/verification.md`.
The existing package-workflow link remains the authoritative route; no duplicate
guide, new process or navigation entry was added. Link checks and factual review
above cover these homes; there is no unresolved applicability.

No deployment, merge, roster mutation or session lifecycle action was performed.
Source changes do not update saved member prompts. Shared guidance applies when
read after integration; catalog selection/rollout remains a separate authorized
deployment. Remaining work: lead acceptance, combined packet, independent final
review, feature publication and explicit integration approval. I0 can handle
current-package findings; a new package requires acceptance/parking and capacity
confirmation under the existing workflow.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-team-lead-delegation/>.
