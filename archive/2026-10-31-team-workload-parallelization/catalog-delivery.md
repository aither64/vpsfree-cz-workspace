# Catalog package A delivery

Implementer0 delivered the catalog portion of the accepted 2026-11-03 design.
This records package evidence for lead acceptance and whole-branch review;
it does not declare the combined branch reviewed, published or deployed.

## Revision and scope

- Workspace worktree: `worktrees/2026-10-31-team-workload-parallelization/workspace`.
- Branch: `2026-10-31-team-workload-parallelization`.
- Base: `6383e8848c92c06a9d817f8109853b5b61305c89`.
- A head: `f69a21f462ea5ee6b5514536745f69855eec0236`.
- One commit: `teams: clarify execution packages and member coordination`.
- Changed only `config/agent-teams.nix`: 16 added, 9 removed lines.
  `flake.nix` needed no assertion adjustment. Package B's three documentation
  edits remained unstaged and were preserved at the A commit boundary.

Shared delegated-lead wording now defines complete package ownership, direct
routine clarification, one executing package per implementer, explicit prior
package disposition/capacity, initialized-versus-available semantics, steering,
safe repository mutation windows and package evidence ownership. Architect and
implementer prompts describe their corresponding responsibilities. Shared lead
requirements permit independently settled implementation briefs while preserving
bounded small edits with direct briefs. The team guide owns the detailed workflow.

## Quick verification

All checks below passed on the exact catalog committed in A. Commands used the
repository's `nix develop --no-update-lock-file` environment where applicable.

| Check | Evidence/result |
| --- | --- |
| Raw catalog evaluation | `nix eval --json --file config/agent-teams.nix` passed. |
| Effective prompt byte bounds | jq checked every `.teams[].roles[].instructions` for nonempty UTF-8 length at most 4,096. All passed; no limit change. |
| Unchanged non-instruction policy | Evaluated base catalog from `git show BASE:config/agent-teams.nix`; jq removed only each role's `instructions` from both catalogs and compared entire remaining objects. Exact equality. |
| Unchanged review/observer policy | Full reviewer and observer role objects, including instructions, compared equal to base in every preset. |
| Existing policy assertions | Extracted unchanged catalog jq predicate from `flake.nix:126-258` and ran it against the evaluated raw catalog with repository jq. Result `true`; no new prose assertions. |
| Package schema/dev environment | `nix develop --no-update-lock-file --command true` passed after consolidation; subsequent checks ran inside the same default environment successfully. |
| Diff and commit scope | Scoped `git diff --check -- config/agent-teams.nix flake.nix` and staged diff check passed. Only `config/agent-teams.nix` was staged/committed; B paths were untouched. |
| Hooks | Repository declares no hook framework; `core.hooksPath` unset and no executable non-sample hooks present. Ordinary `git commit -F /tmp/team-workload-package-a-commit.txt` succeeded without bypass. |

Effective instruction byte lengths:

| Role/preset | Bytes |
| --- | ---: |
| Full-team lead, all five variants | 4,018 |
| Lead-designed lead | 4,006 |
| Lead and reviewer lead | 3,024 |
| Solo lead | 2,802 |
| Architect | 1,076 |
| Implementer | 1,371 |
| Reviewer, unchanged | 1,190 |
| Observer, unchanged | 1,799 |

The initial draft exceeded the existing limit and default environment validation
correctly refused it. Raw evaluation allowed measuring and consolidating the
draft; the final catalog restored validation without changing schema or bounds.
Known Nix warning: `system` renamed to `stdenv.hostPlatform.system`; checks passed.
No broad tests or new tests mirroring prose were added.

## History, compatibility and remaining work

The A range is one focused commit with no superseded intermediate commits,
migrations, dependency/channel/input updates, generated updates, schema/API/
protocol changes or runtime changes. All non-instruction catalog settings,
counts, models, efforts, access, lifecycle and utility records are unchanged.
Solo/Lead-and-reviewer application ownership, delegated modes, explicit roster
change authority, independent final review and approval boundaries remain intact.

Catalog prompts affect future selections only after separately authorized
package deployment. Retained sessions and forks keep saved prompts/settings.
This package performs no roster change, package switch, deployment, merge or
publication. Prompt changes do not alter persistent-state or rollback formats.

Lead still owns combined acceptance and mandatory independent final review of
both packages and their complete history/migration inventory. Focused packaged
`agent-instructions`/`agent-team-policy` checks follow that review under the
monitoring skill. Raw-catalog assertions above do not establish packaged
metadata/native-role rendering or deployed behavior. No speedup is claimed.

## Pilot timeline and ownership transfer

- Actual start observed: `2026-11-03T22:27:20+01:00` (`21:27:20Z`).
- Reviewable with all quick checks: `2026-11-03T22:35:43+01:00` (`21:35:43Z`).
- Committed: `2026-11-03T22:36:08+01:00` (`21:36:08Z`).
- Commit completion reported to implementer1 and lead using IDs
  `8b52409b-7dea-4acb-bcb3-7800e0e52d93` and
  `0e791aaa-9726-49a6-8be3-1d240fdbd13c`. Both received native steered receipts.
- A explicitly ended its Git/index mutation window and transferred the next
  window to B. No further A Git/index mutation is authorized without a new
  lead-assigned follow-up window. Lead acceptance time remains unknown.

Raw temporary evaluation inputs/results and the extracted existing predicate
are `/tmp/team-workload-package-a-{base.nix,base.json,current.json,existing-policy.jq}`;
they are disposable supporting artifacts. This Markdown preserves the evidence
needed for review without depending on their retention.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-31-team-workload-parallelization/>.
