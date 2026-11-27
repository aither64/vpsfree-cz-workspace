# Observer verification guidance: review packet

Requested acceptance: the assigned source-only package is complete and published,
ready for lead acceptance and independent final review. Assess the complete
branch for scope, preserved observer protections, instruction size, documentation
fidelity and history/migration lineage. Independent review has not been run.

## Exact source and history

- Repository/remote: workspace,
  `git@github.com:aither64/vpsfree-cz-workspace.git`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-26-observer-verification-guidance/workspace`.
- Branch: `2026-11-26-observer-verification-guidance`.
- Final review base: `bbfaf615b7c1406fc028a486330efda9fb35cb04` (current shared
  workspace `master` at final preparation).
- Final head: `844ac4dbf768ebced1d27d208f4d5ebaf8b82deb`.
- Complete feature series: one commit, `844ac4dbf`,
  `observer: reassess costly verification before another full run`.
- Original registered base: `94d89fc5b36b0be8a65f36019049f68da76986b1`.
  Fetched origin and rebased the previously unmodified feature onto shared
  `master` before edits. Fetched again before commit; shared `master` remained
  the final base above. There were no feature commits or patches to migrate
  during that rebase.
- No migrations, superseded implementation history, repeated dependency/pin
  updates, generated updates or externally consumed intermediate feature heads.
  No deployment or runtime prompt replacement. Please explicitly conclude on
  whole-branch history and the absence of migrations in independent review.
- Feature push completed over SSH. Fresh `git ls-remote --heads origin
  2026-11-26-observer-verification-guidance` verified exact head equality with
  `844ac4dbf768ebced1d27d208f4d5ebaf8b82deb`. No default-branch integration or PR
  was performed.

Run from the feature worktree:

```sh
git log --reverse --format='%H %s' bbfaf615b7c1406fc028a486330efda9fb35cb04..844ac4dbf768ebced1d27d208f4d5ebaf8b82deb
git diff bbfaf615b7c1406fc028a486330efda9fb35cb04..844ac4dbf768ebced1d27d208f4d5ebaf8b82deb -- config/agent-teams.nix docs/agent-teams.md
```

## Scope and acceptance evidence

Only `config/agent-teams.nix` and `docs/agent-teams.md` changed (36 insertions,
17 deletions). No changes to the brief, AGENTS.md, tests, runtime, catalog
settings, other roles or scheduling. No design deviations.

The observer prompt now challenges serial discovery of basic defects and
verification infrastructure disproportionate to delivery risk. It asks for
implementation/design and verification-strategy reassessment, distinguishes
product/design defects from environment trouble, identifies the next uncertainty,
and recommends bounded shared-cause diagnosis and related fixes before another
costly run. Independent fixes may proceed. It prefers faithful existing checks
against the real interface/dependency, states their cost/evidence/limits, reuses
valid evidence and preserves required review and acceptance checks.

Prose inspection confirms retained protections: phase-aware milestones,
30-working-minute reassessment, timing gaps and overlapping work, design brief,
safe dependencies, delegated ownership, stable concerns resolved by evidence,
necessary long checks, read-only advisory authority, cross-session read policy,
scheduled JSON response and no report_to_lead from the observer. Condensation
keeps the prompt inside the unchanged catalog limit.

| Documentation topic | Reader/class | Authoritative home and routing | Fidelity evidence |
| --- | --- | --- | --- |
| Verification advice | Workspace leads/observers; technical role reference | Existing Independent progress observation section in docs/agent-teams.md; already routed from AGENTS.md and linked to verification procedure | Matches the revised observer instructions; no new workflow, gate or timing collector |
| Catalog versus retained prompt refresh | Workspace operators; compatibility reference | Existing Review and retained instructions section in docs/agent-teams.md | Matches accepted design.md runtime findings: recognized historical migrations differ from latest site-catalog selection; custom prompts and idle/pending safeguards remain |
| Exact revisions, checks and publication | Lead/reviewer; temporary evidence | This packet and ignored checks/ logs; lead owns state.md/portal.yml | Kept out of maintained feature documentation |

No links or anchors were removed or added. Existing documentation routes and
related acceptance assertions pass within the focused test below.

## Quick checks and known baseline failure

Pure catalog checks passed. Evaluated base and candidate using
`nix eval --json --file <catalog-source>` and recursively compared values:

- Only the seven `teams.<preset>.roles.observer.instructions` values differ.
- All seven complete observer roles remain identical to one another.
- All non-observer values, role settings, models, effort, access and inheritance
  remain unchanged.
- Every role instruction is nonempty and at most 4,096 UTF-8 bytes. Observer:
  **4,021 → 4,087 bytes**, cap unchanged.
- Logs/snapshots: `checks/catalog-comparison.log`, `checks/catalog-command.log`,
  `checks/base-catalog.json`, `checks/candidate-catalog.json`. These are ignored
  disposable files beneath this session, not source additions or a harness.

`git diff --check` and `git diff --cached --check` passed. The tested source was
committed unchanged; the feature worktree is clean. Hook inspection found no
declared hook framework, no core.hooksPath override and only sample Git hooks.
No hooks were disabled or bypassed.

The declared instruction check uses pkgs.ruby. Pure evaluation of
`.#checks.x86_64-linux.agent-instructions.nativeBuildInputs` selected
`/nix/store/5shv7ihqxa98r1psfz995q3j2cwk22sa-ruby-3.4.9`; ran:

```sh
/nix/store/5shv7ihqxa98r1psfz995q3j2cwk22sa-ruby-3.4.9/bin/ruby test/agent_instructions_test.rb
```

Result: **10 runs, 220 assertions, 1 failure, 0 errors, 0 skips**. Nine tests
passed. The sole failure is
`test_core_leaves_headroom_below_codex_discovery_limit`: AGENTS.md is 16,550
bytes, exceeding the existing 16,384-byte assertion. Full suite is not green.
Candidate output: `checks/candidate-instructions.log`.

One bounded baseline reproduction copied the final base's AGENTS.md, docs and
unchanged test into a disposable /tmp directory and ran the same command. It
reported the same 10 runs/220 assertions/one failure with identical 16,550 versus
16,384 values (exit 1); see `checks/baseline-instructions.log`. Baseline and
candidate/final AGENTS.md are byte-identical, SHA256
`2e9628a5dd6574b2531206e712ac3a2a8da2fd490af68a62f6a8570c6f31b32d`.
Lead explicitly directed preserving the two-file boundary, recording this
existing failure, and completing commit/publication for independent review.
No assertions were relaxed, tests skipped or broader suites launched.

## Limits and next dependency

No builds, new tests, infrastructure, live team changes, services, deployment or
integration. There are no GitHub workflow definitions in this repository.
The source-only change needs separate package deployment to affect newly
selected observers. Existing observers, including this session's observer,
retain their prompt unless a supported recognized historical refresh or explicit
reconfiguration applies. Rollback of source/package does not rewrite retained
prompts. These limitations are documented; no live behavior is claimed tested.

Lead owns package acceptance, tracking updates, packet completeness and review
invocation. Implementer0 remains available for findings/fixes. Integration and
deployment need separate authorization; the session stays open.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-26-observer-verification-guidance/>
