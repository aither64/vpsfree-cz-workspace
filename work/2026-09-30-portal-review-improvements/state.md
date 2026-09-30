---
lifecycle: active
---

# 2026-09-30-portal-review-improvements

## Status

- Phase: reviewed Codex 0.159.2 candidate and aitherdev host generation
  verified; portal user-profile transition awaits an idle session turn.
- Clean feature heads are generic `41c648c`, extension `67bfbbd` and workspace
  `0e00eab5`. The workspace head retains the reviewed downstream pins and adds
  only the Nix-generated nested Codex dependency update. Its exact feature ref
  is published at `0e00eab5`.
- Mandatory four-lane review has no Blocking, Important or new Advisory
  findings. Generic/extension GitHub checks, the six-case Playwright suite,
  generic flake check and locked WebUI frontend/BFF builds pass at their exact
  unchanged heads. The workspace package build and all four flake checks pass
  at new `0e00eab5`.
- Retained reviewer0 rechecked all four lanes at workspace `0e00eab5` with its
  saved GPT-6 Sol/xhigh settings. It found no Blocking or Important issue. The
  existing aggregate deployment helper mismatch is an Advisory limitation:
  configuration `devWorkspace` still selects the older generic runtime, but the
  scoped aitherdev build/deploy takes system Codex from its separate root
  `llm-agents` input and does not invoke that equality helper. The earlier
  duplicated WebUI-pin Advisory remains accepted. Long candidate verification
  may proceed; no migrations or obsolete feature history were found.
- The portal user profile has not been switched and no session cluster state
  has been created. The candidate generation's cluster command correctly
  refuses use before activation.
- The installed portal profile still uses Codex 0.155.0; the running aitherdev
  system now resolves Codex 0.159.2 at the exact binary proved by the isolated
  same-account model probe. The corrected portal package and its protocol
  checks pass. Portal profile activation has not happened yet: a read-only
  `thread require-idle` check rejects this active conversation turn as
  `inProgress`, which is the package switch's required session preflight.

## Development record

- The portal performance and automatic-history changes are merged on
  `dev-workspace/master` through `7c133c5`.
- Retained delegated roster is ready: `architect0` (design, GPT-6 Astra/xhigh,
  workspace write), `implementer0` (implementation, GPT-6 Sol/xhigh, workspace
  write) and `reviewer0` (review, GPT-6 Sol/xhigh, read-only).
- Registered feature worktrees exist for `dev-workspace`,
  `vpsfree-dev-workspace` and `workspace`; `codex-web` is registered for
  read-only protocol comparison and currently needs no edits. A clean,
  read-only `vpsadmin` worktree was registered at `5c76e329` because the
  cluster runner requires this session's `worktrees/<slug>/vpsadmin` path.
- Accepted [design.md](design.md) from `architect0` as the implementation and
  verification brief. Deployment is still pending.
- The first `dev-workspace` unit is committed as `f00a0e5` (role defaults),
  `4f500a5` (live settings draft) and `ce282b6` (retained/Load-all diffs),
  with a clean worktree. The member's socket-free Go, Ruby,
  Node syntax and repository browser checks passed; Nix daemon and socket-based
  fixtures were blocked by the member sandbox; the lead ran the socket-based
  Go checks from its Nix environment. The commits include explicit Load-all
  and stale-settings browser fixtures.
- Lead Nix shell entry passed. Its default `GOFLAGS=-mod=vendor` needs a
  `-mod=mod` override for source-worktree quick checks without a vendor tree;
  `TestShippedBrowserClientMatchesSessionAPI` then passed with loopback sockets.
  The complete `internal/teamruntime`, `internal/web` and
  `cmd/workspace-portal` Go package suites passed from the lead environment
  (`GOFLAGS=-mod=mod`, 2026-09-30), including socket-based web fixtures.
- First-unit follow-up adds live browser fixtures for Load-all retention,
  bounded batching, failure retry and stale settings reads. Node syntax, Ruby
  creation tests (11 runs/73 assertions), repository navigation contracts and
  `git diff --check` pass. The later Playwright result is recorded below. The lead applied the required
  user-facing-writing pass to the new guide paragraph and settings error.
- The GitHub-only repository origin boundary preserves manifest and API
  compatibility.
  It is committed at `91cd9fbb3971f6b1c5227204b02df32ceb1d6c64` with
  a clean worktree. Repository, manifest, web/template and browser-navigation
  quick checks pass. The lead applied the user-facing-writing pass before
  commit. Its live Playwright result is recorded below.
- The immutable staged/unstaged snapshot unit is committed at `41c648c` with
  a clean `dev-workspace` feature worktree. It includes
  non-ignored untracked files, ephemeral comparison IDs and frozen previews.
  The full repository and web Go packages, focused worktree tests, Node syntax,
  browser navigation contract, formatting and diff checks pass. Early capture
  admission and in-progress reservations guard the 64/256 MiB quotas. Live
  Playwright coverage is summarized below. The lead applied
  the user-facing-writing pass to snapshot errors, notices and guide text.
- The side-by-side React WebUI cluster unit is committed at `1d76d60`; exact
  generic runtime pin `67bfbbd` completes the clean, published
  `vpsfree-dev-workspace` feature branch. Focused runner, status and
  seed Ruby fixtures, Nix parsing, shell syntax and the package derivation
  evaluation passed. The lead updated the root flake lock to the selected vpsAdmin API
  `5c76e329` and reviewed WebUI `534caa83`; its package derivation evaluates.
  The generated nested flake lock was removed because it would freeze unrelated
  previously floating `vpsadminos`, `vpsfStatus` and transitive inputs. The
  subflake instead pins the two selected source URLs in `flake.nix`, preserving
  its existing lock behavior. The lead applied the user-facing-writing pass to
  the extension README and checked visible errors/labels; no product WebUI
  source or KB navigation contract changed. No live cluster boot has run;
  package evidence at the final head is pending.
- The workspace branch is committed, rebased on current shared master and
  published at `99e38751`. Separate commits select exact `gpt-6.1-sol` policy,
  enable the distinct `newadmin` bridge site and pin the complete extension,
  generic runtime, API and WebUI dependency graph. Focused Ruby tests, direct
  catalog checks, lock inspection and package derivation evaluation pass.
  Existing roster state and all unrelated site settings are unchanged.
- The [final review packet](review-packet.md) inventories every base-to-head
  commit and final diff. Overall risk is high. Retained read-only `reviewer0`
  completed all four mandatory lanes at the prior heads with its saved GPT-6
  Sol/xhigh settings. The final test-only fixture amendment and exact pin
  refresh are queued for an affected-lane recheck. The inventory has no new
  migrations or obsolete history.
- The automatically triggered extension Check run `36739199046` failed in the
  packaged enabled cluster evaluation: the selected NixOS module has no
  `systemd.services.<name>.requiresMountsFor` option. The failed log was
  inspected. The supported `unitConfig.RequiresMountsFor` correction was first
  committed as `ce596df6`. Reviewer0 classified the stale downstream pin as
  Blocking and requested clean-history consolidation. The correction is now
  folded into owning cluster commit `1d76d60`; the exact extension and workspace
  feature refs were force-updated with leases to `0965e73` and `feda1f39`.
  Workspace evaluation passes against the corrected pin. A fresh Luna/low
  watcher observed replacement Check run `36742275523` to success at exact
  superseded extension head `9e7ebeb`; its packaged devcluster smoke passed. Full output
  is retained at `/tmp/portal-review-ci-36742275523.log`.
- Reviewer0 completed the high-risk four-lane review of the earlier complete
  series. It found no Blocking issue and one Important extension finding:
  post-build `webui-source.json` publication could leave stale provenance after
  `result-config` advanced. Architect0 recorded the immutable-result correction
  in [design.md](design.md); implementer0 implemented it. The correction and
  README entry-point link are folded into `1d76d60`; the then-current workspace
  pin selected `0965e73`. Focused lead checks passed: status 3/45, runner 6/94, Bash/Nix
  parsing, Ruby syntax and diff checks. The earlier snapshot TTL concern was
  withdrawn because the accepted contract is process-local LRU/quota retention.
  Reviewer0's affected-lane recheck at those heads found no Blocking or
  Important issue. It confirmed the corrected source/result contract, clean
  branch histories and sound selected-API migration lineage. Its Advisory is
  that a future WebUI input-pin update could drift from the runner's hard-coded
  pinned revision; they agree at this exact head. This is accepted for the
  current review and should be checked on the next WebUI pin update. A fresh
  Luna/low watcher observed extension Check run
  `36749437628` to success at the exact `0965e73` head, including the packaged
  `devcluster-check`; full output is at
  `/tmp/portal-review-ci-36749437628.log`.
- A fresh Luna/low watcher built the complete workspace package at `feda1f39`
  to `candidate-workspace-package` (`/nix/store/n00scmqfidkwn0fw8i54c3dg8lz42f0d-dev-workspace-0.2.0`);
  its package checks passed. This build is superseded by the corrected generic
  test fixture and downstream pin refresh, so it must be repeated.
- The post-review generic `nix flake check --print-build-logs` failed at
  `TestWorktreeCaptureSkipsUnchangedLargeFilesAndFilters`: the test's own
  `git diff-files --name-only` positive control did not always invoke the
  hostile clean filter. The same focused test failed 2/10 repeated host runs.
  The fixture writes same-length tracked and working README content, making
  its control depend on Git's stat/racy handling. The corrected test uses
  `hash-object --path` for deterministic filter liveness and a test-local PATH
  guard that rejects unsafe Git commands on both captures. Twenty repeated
  focused runs passed. This test-only correction was folded into the snapshot
  commit and the exact downstream pins were refreshed with lease-protected
  feature pushes. No application capture behavior failed in the original log.
  Full check output is `/tmp/portal-review-generic-flake-check-13383c0.log`.
- Generic `41c648c`, extension `67bfbbd` and workspace `99e38751` are the
  current clean published feature heads. The Load all browser correction is
  folded into its owning generic commit; later commits were replayed and the
  final tree matches the locally tested fix exactly. Extension and workspace
  locks select these exact sources. Earlier CI/build results were superseded;
  final-head results are recorded below.
- Retained independent `reviewer0` completed the final exact-head affected-lane
  recheck using saved GPT-6 Sol/xhigh settings. It found no Blocking,
  Important or new Advisory issue. It confirmed the generic test-only change,
  exact downstream pins, clean complete histories, and sound selected-API
  migration lineage. The earlier hard-coded WebUI-pin drift Advisory remains
  accepted for these matching exact revisions.
- GitHub Check run `36755854565` completed successfully at former generic
  `9ef5858` (fast job; host job skipped by branch policy). Extension Check run
  `36756041388` completed successfully at former `87f6133`, including its
  packaged cluster check. Both heads were later superseded. The workspace
  repository has no branch Check run.
- A fresh GPT-6 Luna/low watcher ran generic `nix flake check
  --print-build-logs` at exact `9ef5858`: exit 0 after 334 seconds, all checks
  passed. Its VM test used a prebuilt kernel; no unexpected kernel build began.
  Full output: `/tmp/portal-review-generic-flake-check-9ef5858.log`.
- The post-review Playwright `TestQuestionBrowser` run at `9ef5858` failed in
  `repository_review_live_browser_test.cjs`: the fixture expected one failed
  preview with 11/12 loaded, but observed 12/12 loaded. The other five browser
  subtests passed. The cause and correction are recorded in the next item.
  Full output:
  `/tmp/portal-review-playwright-9ef5858.log`.
- The browser failure came from an IntersectionObserver read silently retrying
  a failed preview. Generic `41c648c` leaves failed records alone during
  automatic reads while retaining explicit Retry and priority file actions.
  The live fixture now verifies the injected failure and uses a precise
  submodule-notice selector. The focused Playwright repository scenario passes
  at the final generic head; Node syntax, repository browser contracts and
  diff checks pass. The full rerun result is recorded below.
- Retained independent `reviewer0` completed all four affected lanes at exact
  `41c648c` / `67bfbbd` / `99e38751` using saved GPT-6 Sol/xhigh settings.
  There are no Blocking, Important or new Advisory findings. It confirmed the
  explicit retry guard, asset versions, exact pins, five/two/three coherent
  feature commits and no new migration. The earlier matching WebUI pin
  duplication Advisory remains accepted. Selected API lineage supports the
  fresh disposable cluster; older-API database rollback is not proved.
- A fresh GPT-6 Luna/low watcher ran the full Playwright
  `TestQuestionBrowser` suite at exact generic `41c648c`: all six browser
  subtests passed (Go test 83.390 seconds). Full output:
  `/tmp/portal-review-playwright-41c648c.log`.
- A fresh GPT-6 Luna/low watcher reran generic `nix flake check
  --print-build-logs` at exact `41c648c`: exit 0 after about 3m13s, all checks
  passed. Full output: `/tmp/portal-review-generic-flake-check-41c648c.log`.
- Generic GitHub Check run `36759668293` succeeded at exact `41c648c` (fast
  job; host job skipped by branch policy). Extension Check run `36759784918`
  also succeeded at exact `67bfbbd`, including its packaged cluster check.
- A fresh GPT-6 Luna/low watcher built the complete workspace package at exact
  `99e38751`: exit 0 after 241 seconds. The candidate link resolves to
  `/nix/store/j0d65mfyh3wi208iqzqk4cwnshyl473w-dev-workspace-0.2.0`.
  Packaged Ruby, Go and asset checks passed; full output is at
  `/tmp/portal-review-workspace-build-99e38751.log`. A separate final-head
  `nix flake check --print-build-logs` also passed (four checks); its output is
  `/tmp/portal-review-workspace-flake-check-99e38751.log`.
- The extension's exact locked WebUI frontend and BFF both evaluate to build
  metadata for revision `534caa83a5f97d2b40b4a126886649b14dc9e8d3`.
  A fresh GPT-6 Luna/low watcher built both exact locked packages at extension
  head `67bfbbd` (exit 0, 48 seconds): frontend
  `/nix/store/k9cd0z3iad2wysqps4xjzvfx7vcz9irq-vpsadmin-webui-frontend-1.0.0`
  and BFF `/nix/store/5aifx8zh3s3da64qa0b6r282nwygy204-vpsadmin-webui-bff-0.1.0`.
  Full output: `/tmp/portal-review-webui-package-build-67bfbbd.log`. Live
  bridge-cluster proof remains pending. The candidate `vpsadmin-devcluster`
  command correctly refuses before activation because it belongs to a newer
  package generation.
- Active portal `/api/models` (read over its local Unix socket on 2026-09-30)
  lists eight models and does not include the requested `gpt-6.1-sol`. The
  workspace policy retains that exact requested name. The separate 0.159.2
  candidate probe below establishes account access for that binary; deployment
  still requires packaged and active portal checks without substituting a
  different model.
- An isolated same-account App Server probe established the upgrade boundary:
  installed 0.155.0 and system 0.158.0 omit exact `gpt-6.1-sol`, while the
  `af40d966` package's Codex 0.159.2 returns that exact model. Architect0 added
  the separate system/profile rollout and forward-recovery design. Implementer0
  inspected the Nix-generated workspace lock update; because its sandbox could
  not reach the Nix daemon or shared Git index, the lead executed the exact
  requested generation and commit steps. Workspace commit `0e00eab5` changes
  only `llm-agents` `ddc89534` to `af40d966` and its nested `bun2nix`/`nixpkgs`
  closure. JSON, whitespace, flake metadata and package drv/out-path evaluation
  pass. The existing top-level Ruby candidate-switch harness passed four
  focused cases and 26 assertions; invoking its individual file alone failed
  because the test's shared `TransitionHost` helper is loaded by the harness.
  The mandatory related-revision review has since completed; candidate build,
  packaged protocol check and active portal catalog were the next gates.
- A fresh Luna/low watcher built the complete workspace package at exact
  `0e00eab5` (exit 0, 237 seconds); the candidate link now resolves to
  `/nix/store/aidlqw1p8dxijyd35jn7fxr6avzkqvc9-dev-workspace-0.2.0`.
  Its packaged Codex resolves to the identical 0.159.2 store binary used by
  the successful isolated catalog probe. Full build output is at
  `/tmp/portal-review-workspace-build-0e00eab5.log`.
- The same watcher ran `nix flake check --print-build-logs` at exact
  `0e00eab5`; all four checks passed. Candidate `workspace-host check-codex`
  accepts both the installed 0.155.0 transition source and candidate 0.159.2.
  A same-account probe through pinned codex-web `d210d3f` returns one visible
  exact `gpt-6.1-sol` with high/xhigh support. Logs are
  `/tmp/portal-review-workspace-flake-check-0e00eab5.log` and
  `/tmp/portal-model-probe-candidate-0e00eab5.log`.
- Fresh Luna/low watchers built only `cz.vpsfree/machines/aitherdev` from clean
  configuration head `ee99382`, dry-activated generation
  `2026-09-30--21-42-52`, then switched that exact generation. All three
  commands passed. The running system is
  `/nix/store/cb7sziy9ijyf2sxw1ajdbjwrzj2ac591-nixos-system-aitherdev-26.05.20260928.7fc6f2c`,
  reports Codex 0.159.2, remains `running`, has an active firewall and no
  failed system/user units, and keeps the router/portal/Codex user services
  active. Complete logs are `/tmp/portal-review-aitherdev-build-ee99382c.log`,
  `/tmp/portal-review-aitherdev-dry-activate-2026-09-30--21-42-52.log` and
  `/tmp/portal-review-aitherdev-switch-2026-09-30--21-42-52.log`.
- Confctl's generation summary labels the `llm-agents` revision as nested node
  `ddc89534` because its metadata lookup uses the colliding lock-node name. The
  generation's actual `llm-agents.input` symlink equals the root input's
  `af40d966` source; the built and activated system executables both proved
  Codex 0.159.2. Treat the label as evidence-quality metadata, not package
  selection evidence.
- The candidate-initiated profile switch performed its preselection checks and
  correctly refused because this bound thread's current turn is `inProgress`.
  It restored the terminal client and left the old profile selected. Exact
  retry after this conversation becomes idle:
  `/nix/store/aidlqw1p8dxijyd35jn7fxr6avzkqvc9-dev-workspace-0.2.0/bin/`
  `workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/`
  `worktrees/2026-09-30-portal-review-improvements/workspace --from-candidate`.
  The refusal log is `/tmp/portal-review-profile-switch-0e00eab5.log`. Do not
  bypass the idle gate or invoke the ordinary old-helper switch.
- An early capture review found a full tracked-file scan in the draft reader.
  The member proved Git's `ls-files -m`, `diff-files --name-only` and porcelain
  status can invoke hostile clean filters. The accepted [design clarification](design.md)
  uses stage/debug index stats and no-follow lstat to select candidates before
  bounded reads. Oversized candidates will be metadata-only with an explicit
  “content not compared” warning and unknown line totals. Tests must prove
  hostile filters do not run and unchanged large files are not opened.
- The accepted gitlink clarification keeps unstaged review of unrelated files
  available. Frozen `unverifiedSubmodules` metadata sits outside changed-file
  and line totals, with a “working state not inspected” notice. It does not
  claim a submodule is changed, clean or dirty; staged/committed gitlink diffs
  retain their existing behavior.
- The `vpsadmin` worktree-add command returned nonzero from an inherited
  Overcommit post-checkout signature check, after creating and registering the
  worktree. Branch, portal registration, exact HEAD and clean status were
  verified; no vpsAdmin files were edited. No vpsAdmin commit is planned.
- `architect0` completed the [design correction](design.md) for the WebUI
  cluster unit. The extension's packaged vpsAdmin smoke input predates the
  required OAuth client fields; enabled smoke must pin selected compatible API
  `5c76e329` or a proved descendant. A separate runtime seed must follow
  database/general seeding and credential preparation. Existing HaveAPI CORS
  already supports the token header without cross-origin cookies. Bridge is
  the acceptance path; enabled local mode must refuse until both browser and
  BFF can reach one exact provider origin. Recovery keeps the selected
  compatible API/schema while disabling React if needed.

## Phase checklist

- [x] Verify there is no current initiative and create an isolated session.
- [x] Verify the retained roster and saved access.
- [x] Record the approved plan and compatibility/deployment constraints.
- [x] Complete and accept the architecture/verification brief.
- [x] Create/register project worktrees from current remote defaults.
- [x] Implement and commit all intended changes with quick checks.
- [x] Complete mandatory independent review and reconcile findings.
- [ ] Finish long integration/build verification through Luna watchers (final
  generic/browser/workspace, extension CI and WebUI package checks passed; live
  bridge checks remain).
- [ ] Deploy the reviewed portal package and verify it is ready for use.
- [x] Prepare the whole-branch history and migration inventory for handoff.

## Next actions

- In an idle window for this session, run the documented candidate entry from
  the clean workspace feature source using the exact realized candidate command
  recorded above.
  The account model and packaged protocol gates now pass; retain the ordinary
  journal, registration and generation preflights. If the candidate is selected
  before an error, continue only through the newly selected installed helper,
  never an older profile rollback. Then verify active portal models/settings,
  boot only this session's bridge cluster and complete React OAuth/BFF/PHP
  coexistence checks. Leave all feature heads unmerged pending explicit
  default-branch integration approval.

## Documentation

- [Design and verification brief](design.md)
- [Final committed-change review packet](review-packet.md)
- [Team sandbox verification note](../../notes/dev-workspace/2026-09-30-team-sandbox-verification.md)
- [Git clean-filter fixture lesson](../../notes/dev-workspace/2026-09-30-git-clean-filter-control.md)
- [Confctl input metadata alias lesson](../../notes/cross-project/2026-09-30-confctl-input-info-lock-alias.md)

## Repositories

- `dev-workspace`: branch `2026-09-30-portal-review-improvements`, worktree
  `worktrees/2026-09-30-portal-review-improvements/dev-workspace`, initial base
  `7c133c562ac51076c1f45af46e180f8bfbabe836`, published head
  `41c648cd92cb324037778be165e45e17c46bbc75`.
- `vpsfree-dev-workspace`: same branch name, worktree
  `worktrees/2026-09-30-portal-review-improvements/vpsfree-dev-workspace`,
  initial base `bd961682cecb0b3b2bf729a53d2e08bda3d48eb2`; current upstream
  `6a0a2eb873e7cb376092c74bdf82fc2c51c349da` is incorporated, with published
  head `67bfbbd653694e13e8d5aee53ef0f8e283694bf5`.
- `workspace`: same branch name, worktree
  `worktrees/2026-09-30-portal-review-improvements/workspace`, initial base
  `d66bda525c823fe0ce52ea9a1c35550f147b569c`; final review base after the
  required shared-master rebase is `034eb08e`, with published head
  `0e00eab555f9a41136f13cad0f82662f5c2f717b`.
- `codex-web`: same branch name and worktree under that initiative group,
  initial base `d210d3f7cc93981d0ab163b1fcf0718f9587f47e`. It is currently
  a read-only comparison with no changes planned.
- Read-only dependency: `vpsadmin-webui` at reviewed head `534caa83`.
- `vpsadmin`: same branch name and clean worktree under that initiative group,
  base/current head `5c76e3290481b297dcd0baa76d246133f0353d8f`;
  read-only source required by the cluster runner.
- `vpsfree-cz-configuration`: same branch name and clean worktree under the
  initiative group at existing upstream head
  `ee99382c8c448a15347052a6964030f838cb0381`; it has no feature diff. Exact
  aitherdev generation `2026-09-30--21-42-52` was built, dry-activated and
  switched without integrating configuration history.

## Commands run

- `dev-session current`
- `dev-session start portal-review-improvements --team delegated ...`
- `dev-session team list 2026-09-30-portal-review-improvements --as-is`
- `dev-session worktree add ...` for the five registered repositories above.

## Results

- Stable portal URL:
  `https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-30-portal-review-improvements/`

## Open questions

- None. Native browser find and side-by-side WebUI placement were selected
  during planning.

## Cleanup
