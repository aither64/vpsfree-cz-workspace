# Guidance package delivery

Owner: implementer1. Feature checkout:
`worktrees/2026-10-31-team-workload-parallelization/workspace`, branch
`2026-10-31-team-workload-parallelization`. Initial base:
`6383e8848c92c06a9d817f8109853b5b61305c89`.

## Package B

Canonical workflow: `docs/agent-teams.md#package-workflow`. Minimal routed
pointers: `docs/agent-instructions/sessions.md` and
`docs/agent-instructions/verification.md`. No changes to `AGENTS.md` or
`test/agent_instructions_test.rb` were necessary. Core size remains 16,356 bytes.

The workflow covers complete execution and evidence ownership; direct routine
same-session clarification; sufficient per-package release; one executing
package, initialized versus available state, and busy-target steering; narrow
same-repository mutation sequencing; compact status and meaningful timeline
transitions; and effects on retained prompts. Lead scope/acceptance, saved role
authority, independent review and approval gates remain intact.

The guide owns the detailed behavior; session and verification procedures link
to it. This avoids expanding the nearly full core instructions or introducing
another scheduler, ledger, telemetry system or status document per command.
The explanatory package table is a manual convention in existing plan/state.

### Timeline and current disposition

- Brief/release: recorded by the lead as available by 2026-11-03T21:27:27Z;
  exact assignment event timestamps belong to runtime receipts.
- First recorded execution timestamp: 2026-11-03T21:28:14Z. Setup was already
  underway; an earlier exact start was not recorded.
- Reviewable draft and quick checks: available by 2026-11-03T21:31:09Z.
- A explicitly completed its Git/index window and confirmed no further mutations.
- B commit completed by 2026-11-03T21:37:01Z:
  `dcd5e837d5e1ee9fab2c0b48097be7c980674585`, subsequently rebased as below.
- Acceptance: pending lead inspection; final independent review has not started.

### Quick verification

- `nix develop .#checks.x86_64-linux.agent-instructions --command ruby
  test/agent_instructions_test.rb`: **pass**, 10 runs, 206 assertions,
  zero failures/errors/skips. Focused check environment derivation:
  `/nix/store/rr2d8k1rqz0nlgli2yc3vd0sf9hfkj2r-workspace-agent-instructions-tests-env.drv`.
- Repeated for the final committed sources and then the refreshed baseline with
  `--no-update-lock-file`: **pass**, again 10 runs / 206 assertions, no failures,
  errors or skips. Final run completed by 2026-11-03T21:38:41Z in environment
  `/nix/store/zs4q5f0hfpynnfm26yb2jxzk7brkijcg-workspace-agent-instructions-tests-env.drv`.
- `git diff --check -- docs/agent-teams.md
  docs/agent-instructions/sessions.md docs/agent-instructions/verification.md`:
  **pass**. Local Markdown link targets and the new workflow anchor checked.
- Peer CLI example checked with `bash -n`; it was not executed/submitted.
  It preserves the existing sender/recipient, stdin, exact-retry and stable-ID
  arguments used by the supported same-session transport.
- Existing instruction assertions were sufficient; no new prose-mirroring tests.
- Root hook-framework declarations are absent; `core.hooksPath` is unset and
  `.git/hooks` has no active hook files. No hooks were bypassed or modified.

The first `nix develop --command ruby test/agent_instructions_test.rb` attempt
failed during default package evaluation, before tests, because package A's
in-progress role text exceeded the unchanged 4,096-byte limit. Implementer0
confirmed that cause and owns its correction. The focused instructions-check
environment avoids evaluating the team package and supplies the repository's
pinned Ruby dependencies. This failed draft evaluation is not accepted as
successful verification. Implementer0 subsequently restored default package
validation without changing
the limit; see [catalog-delivery.md](catalog-delivery.md). B's ordinary commit
also succeeded through `nix develop --no-update-lock-file --command git commit
-F /tmp/team-workload-implementer1-commit.txt`.

## Whole-branch preparation

After A's handoff, `git fetch origin master` succeeded. The remote default
remained `6383e8848c92c06a9d817f8109853b5b61305c89`; shared local master had
advanced to `aa94433b2c41a17d54f8128b119e33f3289e93ba`. An ancestry check proved
remote master is an ancestor of shared master. The baseline difference contains
tracking/archive records and durable notes only, with no application/policy/check
source changes. Only path categories were inspected; no peer record contents.
An initial preparation assertion allowing only work/archive correctly failed on
the durable notes; it made no mutation. The corrected scope check includes notes.

`git rebase master` completed without conflicts, preserving two commits:

| Package | Before refresh | Final head |
| --- | --- | --- |
| A | `f69a21f462ea5ee6b5514536745f69855eec0236` | `2d00c953509fc8ab297b0a8c39d4dc7a4e41567d` |
| B | `dcd5e837d5e1ee9fab2c0b48097be7c980674585` | `b1e8441dd74a4313da72b434eb991d8c35c6b626` |

Original range: `6383e8848c92c06a9d817f8109853b5b61305c89..dcd5e837d5e1ee9fab2c0b48097be7c980674585`.
Final range: `aa94433b2c41a17d54f8128b119e33f3289e93ba..b1e8441dd74a4313da72b434eb991d8c35c6b626`.
`git range-diff` marks both commits `=`. The complete `git diff --binary`
payloads for these ranges are byte-identical, SHA-256
`d433a99bdc4491d009b996abb80856662f8f06d8f35abfe42b057000e6b6bd0c`.
This preserves A's exact catalog/check evidence as source evidence; it is not a
substitute for the required independent review or packaged checks.

Final whole-range `git diff --check`, local link/anchor checks and CLI syntax
inspection pass. Git porcelain is empty and shared master is still the final
base. The final series/diffstat and combined evidence are in
[final-review-packet.md](final-review-packet.md). No branch push or integration
has occurred; lead owns review invocation, long packaged checks and publication.

## Compatibility and remaining limits

No runtime/schema/API/protocol/pin or roster-setting changes. Catalog changes
affect future selections only after a separately authorized package deployment;
retained sessions and forks keep their saved prompts/settings. Workspace guidance
applies as read and does not silently update retained developer instructions.
The recognized stock-observer refresh exception is preserved. No deployment,
integration, session lifecycle action or persistent-state migration is authorized
or performed by this package. Any corrective work remains an ordinary scoped
feature edit under the existing review and approval rules.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-31-team-workload-parallelization/>.
