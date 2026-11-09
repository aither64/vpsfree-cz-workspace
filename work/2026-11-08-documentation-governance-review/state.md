---
lifecycle: active
---

# Documentation governance

## Status

Ready, awaiting merge approval. All five feature branches are committed and
published. Independent final review found no findings; quick checks, both
pinned documentation builds and both exact-head package CI runs passed.

No integration, package activation, deployment or roster change is authorized.
The generic/site skill sources are prepared, not installed policy. Session stays
open/active. User authorization: 2026-11-09 "ok, implement it", following the
accepted proposal and requested concrete directory/file structure.

## Phase checklist

- [x] Investigation/design and user authorization.
- [x] Implementation complete; intended changes committed and published.
- [x] Quick checks and direct lead writing pass.
- [x] Independent final review, no remediation needed.
- [x] Pinned MkDocs builds and rendered-target inspection.
- [x] Exact-head package CI results collected.
- [x] Ready, awaiting explicit repository/target integration approval.
- Package activation/deployment: outside this implementation.

## Packages and transitions

| Package / owner | Delivered scope | Known transitions / result |
| --- | --- | --- |
| D1/D2 architect0, retained Astra/xhigh workspace_write | Findings, mappings and accepted release brief | D1 accepted 2026-11-08 ~22:42 UTC; D2 assigned ~09:32/accepted ~09:35 UTC 2026-11-09 |
| P1a implementer0, retained Sol/xhigh workspace_write | Generic authoring skill/human guide; workspace routing/editor convention | Assigned ~09:35, reviewable ~09:42, accepted ~09:47 UTC |
| P1b implementer1, retained Sol/xhigh workspace_write | Site packet inventory and seven review questions | Assigned ~09:35, committed/published ~09:42, accepted ~09:47 UTC |
| P2 implementer2, retained Sol/xhigh workspace_write | ZFS testing/flake operations docs and root/nav cleanup | Assigned ~09:36, draft ~09:39, published ~09:44, accepted ~09:47 UTC |
| P3 implementer3, retained Sol/xhigh workspace_write | Configuration reference/runbooks/transitions and navigation | Assigned ~09:36, draft ~09:42, published ~09:45, accepted ~09:47 UTC; renderer-command correction ~09:59 |

Owners confirmed capacity before execution and retain review-fix ownership.
Independent worktree/index/commit windows; lead owned serial registrations and
shared tracking. P3 mkdocs.yml nav added by explicit lead clarification. No other
scope deviations; no optional runtime/catalog expansion or new team member.
Times are observed approximate transitions, not summed role durations. No
material dispatch/acceptance delay; rework limited to narrow writing/link fixes
and verification environment correction. Exact native start times are unknown.

## Branches and reviewed heads

All branches: `2026-11-08-documentation-governance-review`. Worktrees beneath
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-08-documentation-governance-review/`.
All use canonical SSH remotes and are registered in portal.yml.

| Repository / target | Reviewed base | Published final head |
| --- | --- | --- |
| dev-workspace / master | d2cb9975a88079d79f361c5b4c65836ba0835821 | 6587c4c1cedabee95bcc52f4667e7d33e3a82859 |
| workspace / master | 992ce14f295c16bcf395f25107b1fd60f0923ad8 | 1a3a10d9c9e5ef7ef7da05dc42459cf6871b6d4d |
| vpsfree-dev-workspace / master | f8da821e3c76e26e73aa9d89a712eab0e0faa319 | 0c7168f352f6d4f11c46368e702b9356d81012c6 |
| vpsadminos / staging | 4bfed8ba8ddfec49e5a3909df5ede733ea762c99 | 6154dbcd5eaea4a505168f2a7f4fdc25aed4c96d |
| vpsfree-cz-configuration / master | 9e25b996034f8e05f4858dc5ec1f1246a516b109 | f3149765d2db49c5556983df2954cd368a7b0800 |

One focused owned commit per repository, no migrations, obsolete approaches or
repeated dependency/input update streams. Workspace inherits two unrelated
shared-master archive commits after remote master 1134fb3c; metadata/ancestry
accounted for in review without accessing peer records. Preserve that history.
Shared root remains master. No source edits after independent review.

Fresh SSH checks ~10:00–10:04 UTC verified all published heads, clean worktrees
and unchanged remote targets (workspace remote master 1134fb3c; local shared
master 992ce14f). Portal comparisons captured after review at these final heads.
Integration still requires fresh target/premerge checks and explicit approval.

## Verification and review

- Generic: canonical skill/human guide link/fence check under repository Nix
  environment; 25 local/source-mapped targets across four policy/guide files.
- Workspace: pinned Ruby `test/agent_instructions_test.rb`, 10 tests/217
  assertions, no failures/errors/skips.
- Site: pinned Ruby `test/skill_policy_test.rb`, 5 tests/72 assertions, pass.
- OS/config: command/paragraph/provider/queue/recovery preservation, relative
  links/fragments/legacy anchors and nav checks passed. All 12 original config
  command fences and ZFS fence unchanged; OAuth byte-identical. Required active
  hooks passed; generic/workspace/site declare no framework/custom hooks.
- Direct lead site-writing/English-humanizer pass completed before prose commits;
  no factual drift. All owned ranges pass whitespace checks.
- [Final independent review](final-review.md): reviewer0, native thread
  01a1bd4c-16ae-77b3-bf2e-57506d30138c, retained Sol/xhigh/read_only. General,
  scope and risk/compatibility lanes; high risk for relocated recovery guidance.
  No findings at any severity. Explicit placement/preservation, whole-history,
  no-migrations/no-repeated-stream conclusions accepted. No fallback/rerun.
- OS MkDocs exit 0, 0.82s render. Existing unlisted os/faulted-write-ci-handoff.md
  notice only. Configuration corrected MkDocs exit 0, 0.47s render; existing
  out-of-docs link warning in unchanged codex-deepseek-aitherdev.md. Both warnings
  confirmed outside owned changes; no unrelated cleanup. Rendered pages/section
  IDs for ZFS/updater/index/abuse recovery/both transitions checked directly.
- Existing CI: generic run 42595732388 attempt 1 at exact generic head; site run
  42595237520 attempt 1 at exact site head. Both completed success, without reruns. Other
  three branches have no push CI. No redundant local runtime/VM/kernel/ZFS suite.

Detailed commands, pinned source/input graphs, setup issues and native watcher
receipts are in [verification.md](verification.md); logs/raw build artifacts
remain disposable under artifacts/, sites under /tmp. No production operations
were executed or certified. Supported legacy transition retirement remains
unknown; instructions explicitly retained for old/restored state and recovery.

## Monitoring and setup reconciliation

- Full OS shell client PID 2878944/session 53177 canceled/joined; no unfinished
  effects. Narrow pinned Overcommit/Nixfmt/Ruby setup passed active hooks.
- Workspace full shell hit unrelated Savannah config.sub 404; completed command,
  pinned Ruby-only check passed. No source environment workaround.
- Watcher 0030 ran no command, returned incomplete and exact native turn completed;
  resolved via 0031 evidence. Fresh 0032 actually ran docs batch (session 88571)
  and ended; OS passed, P3 pure-evaluation import error before rendering.
- P3 owner corrected command only with --impure, same pinned nixpkgs source.
- Fresh managed operation a182a705-007d-4c1b-bf1b-202611090041 runs corrected P3
  render + watches exact CI. Script SHA256
  5bb6bb541b6942c790b09c0b1e3ca8ddf7ef0ce55d907648bbd10a6826a840dd;
  native thread 01a1bfbf-bf64-7d51-bab7-56f6b3c976cd, turn
  01a1bfbf-c596-7b21-9370-8ca65f25c7e7. Frozen installed package
  /nix/store/8p7fs26ja6flmlgc886ddfgpprdkhfjy-dev-workspace-0.2.0,
  catalog f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d,
  Luna/low/full_access. Exact tool session 79396 still observed; no duplicate
  command. Escalation confirms P3 exit 0. Report's elapsedMillis=0/claimed
  10-minute threshold is not trustworthy timing; receipt was ~10:00 UTC.

## Documentation and next action

- [Design and mappings](design.md), [complete review packet](review-packet.md),
  [review result](final-review.md), [detailed check evidence](verification.md).
- Reusable environment lesson:
  `notes/vpsadminos/2026-11-09-documentation-hook-environment.md`.
- Collect final CI evidence, reconcile any failure, then present branches as
  ready awaiting explicit integration approval. Preserve session open/active.
- No repository/machine/cluster/service claims, deployment or lifecycle action.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-08-documentation-governance-review/

## Final CI and monitor reconciliation, 2026-11-09

- Generic run [42595732388](https://github.com/aither64/dev-workspace/actions/runs/42595732388),
  attempt 1, exact head 6587c4c1cedabee95bcc52f4667e7d33e3a82859, completed
  success at 10:29:50 UTC. Creation/fast/archive succeeded, host skipped under
  normal workflow condition. Site run
  [42595237520](https://github.com/vpsfreecz/dev-workspace/actions/runs/42595237520),
  attempt 1, exact head 0c7168f352f6d4f11c46368e702b9356d81012c6, completed
  success at 10:00:34 UTC. Fresh API evidence at 10:30:31 confirms both.
- Runtime watcher 0041 had ended terminal-incomplete at 10:20 while its original
  shell/gh watch remained alive. Tool session 79396 could not transfer, so lead
  observed exact original shell PID3009781/child3011678 and CI status; no source
  command/CI was repeated. Both processes gone by 10:30:31; original log advanced
  through successful site watch. The aggregate shell exit handle is unavailable;
  component render/CI results independently establish verification.
- Runtime resolution a182a705-007d-4c1b-bf1b-202611090052 accepted at 10:31:50 UTC
  with exact native termination, process quiescence, log and CI evidence. The
  incomplete historical report stays intact; no known operation effects remain.
- Attempted CI observer 0051 had no confirmed launch/receipt. Source validation
  requires WorkflowID and rejects the submitted missing value before operation
  creation/launch; status did not find an operation. No corrected start was
  issued because original run completed. Public CLI status lacked native caller
  binding; no impersonation/bypass or private helper used. No duplicate check.
- Original P1a owner inspected overrun once (~3 min): snapshot showed successful
  progress through 10:19, inherited VM timeout at ~10:52, no terminal failure.
  Source changes were unnecessary. CI completed before that timeout.

Necessary source work/draft delivery took ~10 minutes after release; independent
review and renderers completed before the long CI wait. Do not sum overlapping
member durations or count the overnight interval as working time. No source
rework, rerun or optional expansion was added to fill the wait.

## Handoff

All intended source changes remain at independently reviewed exact heads above;
no migrations, deployment or integration. Keep source branches and session open.
After explicit integration direction, refresh targets and workspace branch as
needed (shared tracking may advance master), preserve reviewed patch equivalence,
then use ordinary short claims/hooks/push/proof/release. Installed skill rollout
remains separate. No repository/machine/cluster/service resources are held.

One consolidated 2026-11-09 tracking checkpoint preserves this outcome, including
original plan/design/review/evidence. It does not integrate feature content.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-08-documentation-governance-review/
