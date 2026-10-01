---
lifecycle: active
---

# 2026-09-30-portal-review-improvements

## Status

- Phase: approved default-branch integration complete. All seven registered
  final feature heads are ancestors of their freshly fetched remote defaults.
  Generic869 and extension074 fast-forwarded unchanged; configuration9824 and
  workspacec3b are independently reviewed, patch-equivalent rebases. The other
  three dependency heads were already contained. SSH pushes and final comparisons
  are complete; source feature worktrees are clean and refs retained.
- CI is report-only by explicit user direction. Initial observations show
  [generic Check](https://github.com/aither64/dev-workspace/actions/runs/36904460292)
  and [extension Check](https://github.com/vpsfreecz/dev-workspace/actions/runs/36904534674)
  in progress. Do not wait for or infer their final conclusions.
- Deployed z20 remains selected from runtime1227/extension074/workspacecd287.
  Its switch succeeded0/70s; portal, Codex and router are healthy, with the exact
  visible gpt-6.1-sol high/xhigh catalog. The v4 live probe passed0/10s: six frozen
  summaries, layout/spacing, empty staged/unstaged views, history retention,
  reload/assets and no page errors. Populated counters/run-link focus and nonempty
  previews were not exercised by this live sample; predeployment fixtures passed.
- Configuration source is merged; shared DNS publication remains held. Re-render
  and build approved DNS targets against9824 before any later authorized deployment.
  No profile switch retry, system/cluster/DNS activation or lifecycle action occurred.
  Session remains active/open. Shared master and59 unrelated modified tracked files
  plus the preexisting empty staged diff were preserved during its fast-forward.
- See [integration.md](integration.md) for approval scope, exact heads, rebase/review
  evidence, final comparisons, remote ancestry proofs and CI observations, and
  [handoff.md](handoff.md) for the concise continuation record.

### Earlier checkpoints

The entries below retain earlier evidence and identities; the current selected
profile and pending work are stated above.

- The original card UI unit has 19 paths and preserves existing API/schema/provider
  contracts. The extension changes only its generic input. The workspace final
  graph changes only extension and transitive generic nodes from `aca3b39d` and
  preserves the approved Codex 0.159.2 closure at
  `af40d966`/`07a5bfc8`/`f45c6f04`. A temporary unpublished workspace commit
  captured an old nested closure during concurrent lock generation; the exact
  override restored it and the bad tree was amended out before review or push.
  Workspace `4a6d44a2` evaluates to
  `/nix/store/9gdvn344zpng5vxwa7x4cvibp5kprhf1-dev-workspace-0.2.0.drv` with
  lock writes disabled. Extension package-check evaluation resolves
  `/nix/store/sgzrn8rmwrix63wwiaaff3czmln0k0jp-dev-workspace-0.2.0.drv`.
- Spacing clarification: `1rem` means vertical separation above the repository
  review action row (`margin-top`); the existing `.5rem` button gap and desktop
  one-row fit remain. Workflow totals describe returned/displayed exact-revision
  runs, at most 100. Initial nil runs must not appear as an observed zero.
  Successful empty results show exactly `Workflows · 0 total`, without an empty
  disclosure or five-counter row. Unavailable results are compact; nonempty
  results retain the native disclosure during refresh and show all five
  counters. Reinserted disclosures after a compact state start closed.
  Presentation-only counters and retained native workflow disclosure are the
  accepted design boundary, recorded in design.md:1926. Counts, loading/error
  states and native disclosure retention use existing data; no API/schema field
  or provider query is added. At that earlier checkpoint `bpz` was active.
- The previous user profile was exact package `bpzvfhdn…`, built from workspace
  `aca3b39d` with generic runtime `e64a9fda`, extension `362ebd4` and Codex
  0.159.2. The guarded switch completed with exit status 0 in 88 seconds. The
  portal restarted successfully as PID 2031444.
- Live acceptance on `2026-09-23-storage-redesign` confirms staged and unstaged
  empty comparisons encode `files` as arrays and render without a page error.
  Six repositories stack one per row; all four desktop actions share one row;
  narrow layout does not overflow; Local commits starts closed, stays open during
  refresh and closes again after reload; Origin and Load all diffs are visible.
- Shared DNS candidate d24b and its four built consumers are prepared. The latest
  user direction explicitly keeps DNS/configuration unpublished, superseding the
  earlier approval question. Configuration d24b remains clean; no DNS activation
  or publication is included in portal acceptance.
- Independent reviewer0, saved gpt-6-sol/xhigh/read-only, completed the affected
  general/architecture and exact pin compatibility review at e64a9fda/362ebd4/
  aca3b39d/d24b2515. No Blocking or Important finding. It explicitly confirms
  coherent complete 12/6/7/1 histories, preserved consumed ancestry, no obsolete
  unapplied approach or transitional migration, and no new database/persisted
  migration. Prior scope/security and upstream nine-migration provenance remain
  unchanged. The stale-head documentation Advisory is reconciled below.
- Reviewed repository-review follow-up: generic
  `8019b9b7` restores empty comparison arrays, accepts legacy null in the
  browser, uses one full-width repository card and closes Local commits by
  default. Extension `361be9c7` and workspace `9818b805` select it exactly while
  retaining Codex 0.159.2. Focused Go, mounted-browser, Node syntax, whitespace
  and pin checks pass; all feature refs are published and worktrees are clean.
  The retained independent reviewer completed all four lanes with no Blocking
  or Important finding. Long checks now own the remaining evidence before the
  user-profile deployment. Shared DNS publication remains separately unapproved.
- Verification correction: `repository-followup-long-checks-final.status` is
  zero, but its log contains failed browser/Go stages at `8019b9b7` and a failed
  `packages.x86_64-linux.package` lookup. Its `ALL_STAGES_PASSED` footer does not
  establish success of those stages. The desktop action-row failure motivated
  `e64a9fda`; the separate 84.274s browser run verifies that correction. Generic
  and workspace flake stages in the earlier log passed at their recorded old
  heads; exact new-candidate build/protocol/catalog gates remain pending.
  A fresh watcher assigned for a duplicate focused check used the workspace
  root instead of the specified tracking directory and failed identity before
  starting any test. Parent identity was rechecked successfully from the exact
  tracking directory; no duplicate operation or source mutation occurred.
- The preceding exact-head final verification used fresh Luna/low
  `final_candidate_e64_proper`. Its predecessor omitted the assigned Nix wrapper:
  `/tmp/portal-review-e64-final/01-go-tests.log` records exit 1 because browser
  subprocesses could not find Node. The parent verified that the actual Nix
  shell supplies Node 24.19.0 and Go 1.26.6, then prepared a syntax-checked
  literal batch at `/tmp/portal-review-e64-final-proper.sh`. That watcher ran
  the exact script once; separate command statuses/logs/elapsed records are in
  `/tmp/portal-review-e64-final-proper/`, with failure propagation and immutable
  clean-head gates. No application fix was inferred from the missing wrapper.
- The properly wrapped full Go/browser stage exited 1 after 175s at `e64a9fda`.
  The failure is Firefox `presentation_browser_test.cjs:218`: intentional
  Keep open POST failure restores the checkbox before Playwright `uncheck`
  checks its final unchecked state. Chromium and repository layout assertions
  passed. Evidence is `/tmp/portal-review-e64-final-proper/01-go-browser.log`
  with status 1; later stages did not run. Implementer0 owns the bounded
  fixture-only action/503-response correction; architect0 owns the verification
  and retained-runtime-pin disposition. No production change is assumed and
  no failed-stage result is counted as a pass.
- Architect0 recorded the bounded fixture-only disposition in `design.md:1755`.
  The reviewed runtime graph remains e64a9fda/362ebd4/aca3b39d, with prospective
  package `bpzvfhdn…`; the optional CJS correction will have a separate generic
  verification head. Unfiltered source changes derivation identity if repinned,
  so no package identity equivalence is claimed. Fresh Luna/low utility
  `hold_fixture_focus` owns the literal focused normal-host script
  `/tmp/portal-review-e64-hold-fixture-focused.sh`; logs, true status and elapsed
  use the matching prefix. Implementer0 holds its one-file commit until that
  check passes. No consumer pins, production assets or lifecycle state changed.
- Reviewer0 used its retained `gpt-6-sol`/xhigh settings and read-only access to
  inspect the complete 9/5/6/1 commit histories at generic `8019b9b7`, extension
  `361be9c7`, workspace `9818b805` and configuration `d24b2515`. General,
  architecture and repetition, scope and proportionality, and risk and
  compatibility lanes found no new security or compatibility issue, obsolete
  unmerged approach, transitional migration or incoherent commit split. No
  branch adds a database or persisted-format migration. Its documentation-only
  Advisory identified stale published-head references in this file; the
  repository inventory below now uses the reviewed heads. Existing accepted
  pin-duplication and deployment-checker Advisories remain unchanged.
- The preceding release is deployed and ready for use. Implementation, independent review, final
  verification, profile activation and the bridge-cluster services update
  passed, including the corrected browser fixture at generic `50586880`. The
  final Origin label and container autostart refinements are active. Shared DNS
  publication waits for approval of the four exact targets.
  The accepted architect assessment retains runtime pins at generic
  `50af66d` / extension `8e04f262` / workspace `45cce0a8`.
- At that earlier checkpoint, clean published generic verification head was
  `618df553`.
  Published consumer heads remain
  extension `362ebd4` and workspace `aca3b39d`. The consumers retain runtime input
  `e64a9fda`; the local configuration candidate remains
  unchanged at `d24b2515`. During the earlier recovery, a conflicting brief
  temporarily published a consolidated extension chain and its consumer.
  Recovery restored the original deployed ancestry locally and remotely with
  checked ref updates, then amended only the then-unselected consumer `45cce0a8`,
  whose parent remains deployed `0e00eab5`. Later appended pins preserve that
  ancestry and the Codex 0.159.2 closure.
  The final packet is synchronized to these preserved histories. No selected
  package or running cluster changed during recovery.
- Mandatory final four-lane review at exact generic `50af66d`, extension
  `8e04f262`, workspace `45cce0a8` and configuration `d24b2515` has no
  Blocking or Important findings. The retained reviewer accepted the two
  existing Advisories: the duplicated exact WebUI revision and the aggregate
  deployment checker that rejects the documented scoped host/profile pin
  mismatch. The complete histories contain no obsolete unapplied approach or
  transitional migration. Exact generic `50af66d` and extension `8e04f262`
  GitHub checks pass. The earlier six-case Playwright pass was at `41c648c`;
  the full run at `50af66d` passed five cases and failed the wake-counter
  fixture. Locked WebUI frontend/BFF builds and generic/workspace flake checks
  pass. The final workspace package built
  at `45cce0a8` as `/nix/store/51i6gp92srgvqcmmwfv8qsg9xq9xfdqf-dev-workspace-0.2.0`.
- The bounded general/architecture review at generic `50586880` found no
  Blocking or Important issue and confirms the retained runtime pins. Its
  Advisory notes that a late focus activity response could increment the same
  counter; accept this bounded fixture-isolation limit unless focused/full
  checks expose another failure. The complete seven-commit generic series has
  no obsolete unapplied history and adds no migrations. Exact-head CI run
  `36780221159` passed.
- A fresh Luna/low watcher verified generic `50586880`: declared-environment
  Node syntax, three focused lifecycle runs, all six browser cases and the
  packaged flake check passed. Logs/statuses:
  `/tmp/portal-review-browser-505-{syntax,focused,full}.log` and
  `/tmp/portal-review-generic-505-check.log`. The full Go suite took 81.702s and
  the flake check about 6m40s. This completes the remaining final verification
  gates for the retained runtime package.
- The user ran the final guarded transition while this conversation was idle.
  The selected profile is now exact built package `51i6gp92…` from workspace
  `45cce0a8`; no pending transition remains. Live portal checks show seven
  `Origin` repository links, no generic `GitHub` repository labels, Load all
  diffs, the atomic settings client and exact `gpt-6.1-sol` with all supported
  efforts.
- Retained reviewer0 completed the final all-lane review with its saved GPT-6
  Sol/xhigh settings. The existing aggregate deployment helper mismatch is an
  Advisory limitation:
  configuration `devWorkspace` still selects the older generic runtime, but the
  scoped aitherdev build/deploy takes system Codex from its separate root
  `llm-agents` input and does not invoke that equality helper. The earlier
  duplicated WebUI-pin Advisory remains accepted. Long candidate verification
  may proceed; no migrations or obsolete feature history were found.
- Normal `workspace-host status` now selects the realized `51i6gp92…` package
  from workspace `45cce0a8`. The running host uses the reviewed Codex 0.159.2
  binary. Live portal `/api/models` exposes exact `gpt-6.1-sol` with high and
  xhigh; this authorized lead turn reads back that model with xhigh effort.
- Filtered normal cluster status proves this exact session is running and ready
  on single/bridge networking. PHP and React service links coexist; selected
  build provenance is clean pinned WebUI `534caa83`. The first React request
  exposed a real lifecycle defect: the enabled `newadmin` container had no
  autostart target. A manual diagnostic start restored it and the assigned
  correction sets `containers.newadmin.autoStart = true` with enabled and
  disabled evaluation assertions.
- Live React acceptance now passes for TLS trust/SANs, static assets, public
  config, health, CORS, loopback-only private listeners, nginx configuration,
  BFF service hardening, legacy PHP coexistence and exact clean build metadata.
  Real OAuth authorization, callback exchange, one-use state rejection,
  authenticated API access, forced access-token refresh, stable session
  identity across BFF restart, repeated seed execution, logout and access-token
  revocation all passed without recording credentials or tokens.
- A fresh real OAuth login produced an authenticated BFF session before final
  activation. The supported services update completed through a fresh Luna/low
  watcher in about 7m25s. The services VM activated exact selected toplevel
  `vv7b9mh…`; cluster status is running and ready on single/bridge networking.
  `container@newadmin` is active, enabled, wanted by `machines.target` and
  ordered after the successful seed. The clean worktree source record is exact
  WebUI `534caa83`; the pre-update session retained its session key, health,
  legacy PHP, authenticated API and CORS checks return 200, and ports 18082 and
  3001 remain loopback-only. All temporary authentication material was removed.
- Ordinary host and VPN-client resolution for
  `newadmin.aitherdev.int.vpsfree.cz` is absent from both internal authoritative
  DNS copies even though the running cluster's guest DNS has the record. A
  bounded configuration candidate adds one CNAME to the existing aitherdev
  frontend and advances the zone serial. It is committed, independently
  reviewed and zone-checked. Build-only evaluation passed for all four exact
  consumers. Publication to
  `prg/int.ns1`, `brq/int.ns1`, `prg/int.mon1`
  and `prg/int.mon2` requires separate exact-target approval because the user
  authorized deployment of aitherdev, not those four shared DNS consumers.

## Development record

- Follow-up quick verification passed in the declared generic Nix shell on the
  in-progress patch: raw empty committed/staged/unstaged responses, submodule-only
  array shape, active/archived disclosure/actions, existing Origin template and
  repository navigation contracts. Focused Go time was 1.665s. App/review/live
  and presentation JavaScript syntax and the repository browser contract passed.
  Shell entry rebuilt prerequisites and completed normally; these are focused
  quick checks, not committed-head review or long browser/build evidence.
- The main-agent user-facing writing pass is complete for the follow-up README,
  portal guide and visible labels/errors. Implementer0 is authorized to commit
  two focused appended units: empty-response compatibility, then card
  presentation/disclosure/cache coordination. The scoped grid rule preserves
  the actual development-cluster card consumer in templates/clusters.html.
  The necessary test/repository_browser.cjs fixture update is included in the
  19 owned paths. No deployed ancestor will be folded or rewritten.

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
- The live bridge start completed successfully through a fresh Luna/low
  watcher. Its initial public React probe returned 502 because
  `container@newadmin.service` was linked but had no `WantedBy` target and was
  inactive. Manual diagnostic start proved the application stack itself;
  final acceptance requires the corrected unit to be enabled for
  `machines.target` after the supported services update.
- The deployed portal accepted one atomic settings write from GPT-6 Sol/high to
  exact `gpt-6.1-sol`/xhigh and retained both values on readback. Staged and
  unstaged endpoints returned immutable snapshots for disposable test changes,
  which were removed afterward. The deployed repository viewer includes
  retained loaded diffs and `Load all diffs`.
- A clean session-owned `vpsadmin-webui` worktree is now registered at exact
  reviewed head `534caa83a5f97d2b40b4a126886649b14dc9e8d3`. The final cluster services
  update will exercise the documented local-source override and must report
  that exact clean revision.

## Phase checklist

Repository-card design follow-up:

- [x] Verify the same-session roster and resolve action-row spacing.
- [x] Complete and accept architect0's design and verification brief.
- [x] Assign application edits to implementer0 under the accepted brief.
- [x] Receive the scoped patch and apply the main writing pass.
- [x] Finish compact-state/focus refinements and final quick checks, then commit
  the coherent presentation unit without rewriting consumed history.
- [x] Independently review the committed card unit, resolve the workflow-link
  focus finding, publish the exact focus/cache consumer graph and complete its
  affected-lane review.
- [x] Commit and independently review the optional archive fixture correction
  `869b8d47`, retaining runtime `1227`/extension `074`/workspace `cd2875`.
- [x] Pass the corrected full Go/browser suite and generic flake at verification
  head `869b8d47` (170s/324s).
- [x] Pass new-head generic CI, retained consumer flakes, exact z20 build/protocol,
  real-editor harness and extension smoke (all nine stages status 0).
- [x] Complete candidate catalog/protocol acceptance with the same exact packaged
  binary/client/account and current visible model catalog.
- [x] Execute the separately authorized guarded profile transition and verify
  selected z20 package/service identity (status0/70s).
- [x] Complete the requested unchanged v4 live probe with true exit0/10s;
  summaries, layout/spacing, empty diffs, history retention and reload passed.
- [ ] Observe populated workflow counters/run-link focus and nonempty previews
  live if required; this sample contained unavailable workflows and empty diffs.
  Their both-engine/real-editor fixture evidence is already complete.

Repository-review follow-up:

- [x] Reconfirm the retained roster, clean feature worktrees and affected pin
  chain.
- [x] Complete and accept the design correction.
- [x] Implement and commit the generic API/browser/layout/docs changes with
  quick checks.
- [x] Complete mandatory whole-branch review and reconcile findings.
- [x] Update and commit the extension and workspace pins.
- [x] Correct desktop action-row alignment with real browser verification and
  publish the exact consumer pins while preserving the Codex closure.
- [x] Complete the affected-lane review of e64a9fda/362ebd4/aca3b39d and refresh
  the whole-history conclusion.
- [x] Commit and independently review the optional Keep open fixture correction
  at `4a1da3c3`, retaining runtime pins and the candidate package identity.
- [x] Verify exact extension CI at `362ebd4`, including packaged cluster smoke,
  and confirm account support for new defaults and retained member pairs.
- [x] Commit and independently review the standalone real-editor retention
  fixture at `618df553`, preserving the runtime consumer graph.
- [x] Pass full Go/browser and generic/workspace flakes, exact candidate
  build/protocol and extension CI/cluster smoke at their recorded revisions.
- [x] Finish the exact `618df553` real-editor harness and generic CI.
- [x] Activate the new workspace user profile and verify the reported session.

Preceding release evidence:

Runtime candidate verification is scoped to generic `50af66d`, extension
`8e04f262`, workspace `45cce0a8` and configuration `d24b2515`. The complete
series and changed paths are in [final-diff-inventory.md](final-diff-inventory.md).
Reviewer0 completed all four lanes at those clean published heads with no
Blocking or Important finding. Exact generic CI run `36771070080` and extension
CI run `36774580291` passed;
superseded consolidated-chain run `36776380225` was cancelled. The evaluated
workspace candidate is
`/nix/store/51i6gp92srgvqcmmwfv8qsg9xq9xfdqf-dev-workspace-0.2.0`, derivation
`/nix/store/zjpfzn5k6y6mw7lbyzn7pg2g29p3y6rr-dev-workspace-0.2.0.drv`.
The package build and final flake check passed. Generic `50af66d` flake checks
passed. The corrected optional browser fixture and generic checks passed at
final branch head `50586880`; unchanged runtime behavior lets the corrected
browser evidence apply to the retained candidate without a pin cascade.
The local extension smoke was interrupted by host garbage collection: the
`nix-store-gc-on-pressure.service` journal records deletion of both the running
check app and its tools output at 23:34:08 CEST. The fixture passed bridge
defaults and override evaluations before the missing-package read. Its log is
`/tmp/portal-review-final-cluster-8e04f262.log`. A fresh Luna/low watcher then
retained the full app closure with a normal out-link and ran the same check
successfully: exit 0 after about 5m40s. Evidence:
`/tmp/portal-review-rooted-cluster-8e04.log` and `.status`; root
`/tmp/portal-review-devcluster-check-8e04-gc-root` is retained. Enabled bridge,
disabled bridge/local, enabled-local refusal and runner build/load checks pass.
No application or GC-policy change is indicated. The conditional
DNS build in that batch did not run. Separate completed build logs were then
verified: `/tmp/portal-review-extension-flake-check-8e04f26.log` ends with all
checks passed, and `/tmp/portal-review-internal-dns-four-builds-d24b251.log`
records all four DNS generations. Their realized BIND configurations each
reference a zone with serial `2026093000` and one exact newadmin CNAME;
`named-checkzone` from each built BIND package returned OK. Generation IDs and
toplevels are recorded in [rollout.md](rollout.md). The user has been asked to
approve dry activation/publication to those four exact shared hosts; approval
remains pending.

- [x] Verify there is no current initiative and create an isolated session.
- [x] Verify the retained roster and saved access.
- [x] Record the approved plan and compatibility/deployment constraints.
- [x] Complete and accept the architecture/verification brief.
- [x] Create/register project worktrees from current remote defaults.
- [x] Implement and commit all intended changes with quick checks.
- [x] Complete mandatory independent review and reconcile findings.
- [x] Finish long integration/build verification through Luna watchers.
- [x] Verify the active deployment is ready for use and activate the final
  label refinement.
- [x] Prepare the whole-branch history and migration inventory for handoff.

## Next actions

- The user-directed integrations are complete. Commit/push this consolidated
  durable handoff; no additional source integration or CI wait remains authorized.
- Preserve selected z20 and the active session. Do not retry the package switch,
  reconcile/activate services or perform a session lifecycle action.
- Keep shared DNS publication held. Later deployment requires its own authority
  and checks against rebased configuration9824, even though the source is merged.
- Preserve the live sampling limit and the initial-only CI states; no final CI or
  populated-workflow/preview live result is inferred.

## Documentation

- [Design and verification brief](design.md)
- [Final committed-change review packet](review-packet.md)
- [Aitherdev rollout record](rollout.md)
- [Team sandbox verification note](../../notes/dev-workspace/2026-09-30-team-sandbox-verification.md)
- [Git clean-filter fixture lesson](../../notes/dev-workspace/2026-09-30-git-clean-filter-control.md)
- [Confctl input metadata alias lesson](../../notes/cross-project/2026-09-30-confctl-input-info-lock-alias.md)
- [Checkbox rollback fixture lesson](../../notes/dev-workspace/2026-10-01-playwright-checkbox-rollback.md)
- [Watcher identity directory lesson](../../notes/dev-workspace/2026-10-01-watcher-session-working-directory.md)
- [Detached deployment launcher lesson](../../notes/dev-workspace/2026-10-01-detached-deployment-launcher.md)
- [Retaining separate browser build assets](../../notes/dev-workspace/2026-09-12-browser-acceptance-gc-roots.md)
- [Publication before amendment](../../notes/cross-project/2026-10-01-publication-before-amend.md)
- [Paired browser refresh observations](../../notes/dev-workspace/2026-10-01-paired-browser-refresh-observations.md)

## Repositories

- `dev-workspace`: branch `2026-09-30-portal-review-improvements`, worktree
  `worktrees/2026-09-30-portal-review-improvements/dev-workspace`, initial base
  `7c133c562ac51076c1f45af46e180f8bfbabe836`, published head
  `869b8d4728394127ba949dc76724dce56eae136b`; retained candidate runtime input
  `1227f5c21f4f9a38bbde37c141c2f35f50008554` (active runtime remains e64).
- `vpsfree-dev-workspace`: same branch name, worktree
  `worktrees/2026-09-30-portal-review-improvements/vpsfree-dev-workspace`,
  initial base `bd961682cecb0b3b2bf729a53d2e08bda3d48eb2`; current upstream
  `6a0a2eb873e7cb376092c74bdf82fc2c51c349da` is incorporated, with published
  head `074926d33f7306288f7cfad87c6a85e8a430e750` (active extension remains362).
- `workspace`: same branch name, worktree
  `worktrees/2026-09-30-portal-review-improvements/workspace`, initial base
  `d66bda525c823fe0ce52ea9a1c35550f147b569c`; final review base after the
  required shared-master rebase is `034eb08e`, with published head
  `cd2875f3d4fb2199dd1992b07a3e664eb901e50f` (active workspace remainsaca).
- `codex-web`: same branch name and worktree under that initiative group,
  initial base `d210d3f7cc93981d0ab163b1fcf0718f9587f47e`. It is currently
  a read-only comparison with no changes planned.
- `vpsadmin-webui`: same branch name and clean session worktree at reviewed head
  `534caa83a5f97d2b40b4a126886649b14dc9e8d3`; read-only dependency with no
  feature diff.
- `vpsadmin`: same branch name and clean worktree under that initiative group,
  base/current head `5c76e3290481b297dcd0baa76d246133f0353d8f`;
  read-only source required by the cluster runner.
- `vpsfree-cz-configuration`: same branch name and clean worktree under the
  initiative group from upstream base
  `ee99382c8c448a15347052a6964030f838cb0381`, with published feature head
  `d24b251531a9a482b8f1b5dd81540da85981189f`. Its bounded diff adds the
  newadmin internal-DNS CNAME and advances the zone serial; it has not been
  deployed. Exact aitherdev generation
  `2026-09-30--21-42-52` was built, dry-activated and switched without
  integrating configuration history.

## Commands run

- `dev-session current`
- `dev-session start portal-review-improvements --team delegated ...`
- `dev-session team list 2026-09-30-portal-review-improvements --as-is`
- `dev-session worktree add ...` for the five registered repositories above.

## Results

- Stable portal URL:
  `https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-30-portal-review-improvements/`

## Open questions

- Shared DNS publication to the four reviewed/built hosts awaits approval.
  The exact-target question has been sent; no approval is inferred from time
  elapsed or the preselected answer.
- Final profile activation requires an idle session. The supported candidate
  command is above; live card-summary/focus acceptance follows selection.
  No cluster/system update is needed for this UI correction. No default-branch
  integration is authorized.

## Cleanup

## Keep open fixture commit (2026-10-01)

Implementer0 appended `4a1da3c3d1d099a6b0d309b194bd1e343d8d38c1` directly to
`e64a9fda`, changing only presentation_browser_test.cjs (10+/2-). Normal
`git commit -F`, no declared active hook framework, Node syntax and whitespace
passed; worktree/index clean. Fresh Luna/low focused watcher passed the identical
patch in both engines, true status0 and elapsed36s. Runtime pins e64/362/aca and
prospective bpz package remain unchanged. Complete inventory now has11/6/7/1
commits; bounded independent review and exact-head final checks remain next.

Reviewer0 completed the general/architecture affected-lane recheck at clean
4a1da3c3/362ebd4/aca3b39d/d24b2515 with its saved Sol/xhigh/read-only settings.
No Blocking, Important or new Advisory finding. Its explicit full11/6/7/1
history conclusion confirms no obsolete unapplied approach or transitional
migration, preserved consumed ancestry and no new migrations. It accepts the
distinct verification head and retained runtime graph; source identity differs
if repinned. The reviewed gate clears the remaining long checks, not deployment
or default-branch/shared-DNS approval.

Exact extension CI `36850019822` at `362ebd4` is now verified successful:
both `nix flake check --print-build-logs` and `nix run .#devcluster-check` passed
on 2026-10-01. This closes extension checks and packaged enabled/disabled smoke
for the retained consumer; no duplicate local rerun is required. The prepared
new generic-head batch keeps consumer guards and completes full browser-enabled
Go, generic flake, workspace flake, candidate build/protocol and packaged editor
browser checks, stopping on the first actual nonzero stage. Its separate status
files preserve evidence and do not reuse the invalid older aggregate footer.

The first new batch watcher used the workspace root for its separate identity
probe despite the assigned tracking directory and stopped before launch. Parent
identity still matches from the exact session directory. No check ran or
operation remains; replacement uses a fresh watcher with the first shell
identity command and its working directory explicitly specified.

The generic fixture commit was published normally over SSH at4a1da3c3; exact
CI run36854636430 is included in the replacement batch. No superseded active
generic CI run needed cancellation. Main read-only live catalog verification
on Codex4mxlhqv9…/0.159.2 confirms exact gpt-6.1-sol with high/xhigh and all
four retained lead/member model-effort pairs remain supported. Profile51i6gp92…
and portal PID1250667 still match, and the bound session activity is working.
The supported profile transition's idle gate must be respected; no force,
private lifecycle invocation or delayed activation is authorized.

## Final literal batch results and packaged fixture correction

Fresh Luna/low `final_4a_literal_batch` ran the exact guarded script once:
full Go/browser0 (172s), generic flake0 (329s), workspace flake0 (259s), candidate
build0 (7s), check-codex0 (3s). Candidate is rooted at
`/tmp/portal-review-candidate-e64-gc-root` and resolves to exact bpzvfhdn… package.
Batch exited1 at packaged-editor browser (41s), so the batch is not all-green.
Settled log `/tmp/portal-review-final-4a1da3c3/07-packaged-browser.log` is3275bytes
and identifies `test/repository_browser.cjs:274`: the old <=8 editor mount
assertion sees30 retained editors. The watcher's initial empty-log report is
superseded by this direct settled evidence. This old assertion contradicts the
accepted retained-editor behavior; no production defect is demonstrated.

Implementer0 owns a one-file correction with real editor retention/content
proof; architect0 owns its bounded verification/pin disposition. Hold commit
until the focused real-editor proof. Preserve all successful exact-head results,
the built e64/362/aca candidate and current51i profile. Generic CI36854636430
at4a1da3c3 is successful; its stage was not reached in the stopped batch but
was independently verified afterward. No retry, activation or cleanup occurred.

Focused real-editor correction run21s exited1 after passing the new30-editor
retention assertions. The next stale assertion expected zero editor nodes after
collapse, while setCollapsed hides its body and retains the loaded node/content.
Evidence: `/tmp/portal-review-real-editor-retention-focused.log`, line309 of
current fixture. Architect's earlier assertion-validity assessment is corrected;
implementer owns hidden/retained-node/reopen/no-refetch proof in the same file.
No product issue or broader edit is inferred. A fresh watcher will verify the
corrected complete harness; no failure was accepted as a pass or blindly retried.

The second focused run exited 1 after 69s before the new assertions, waiting
for the initial editor at fixture line 132. Its explicit editor-assets store
directory `3g3bvqg…` is absent. The fixture returns 404 for missing static files;
Playwright and Codex-web inputs still exist. The rooted candidate's derivation
names that exact asset output and its still-present derivation `vwkvpcfc…`.
System/user GC journal inspection did not establish the deletion's cause or
timing. Restore and retain the exact asset output under an explicit GC root,
check its editor/worker files, then verify the unchanged one-file patch in a
fresh watcher operation. No product/input defect or new pin is inferred.

Rooted focused proof passed: fresh Luna/low `real_editor_retention_v3` ran the
guarded script once, status 0, elapsed 29s, with 84 fixture requests. The log
`/tmp/portal-review-real-editor-retention-v3.log` includes retained real editors,
syntax/lazy assets and the complete harness checks. The exact candidate asset
output is retained by `/tmp/portal-review-real-editor-assets-gc-root`; restoration
log is `/tmp/portal-review-real-editor-assets-restore.log`. Implementer0 is
authorized to commit only the 40+/7− CJS fixture patch, preserving runtime pins.
Independent affected-lane review and exact generic CI follow that commit.

Retained reviewer0 completed independent general/architecture review at exact
`618df553` / `362ebd4` / `aca3b39d` / `d24b2515`, saved Sol/xhigh/read-only. No
Blocking or Important finding. It explicitly confirms the complete 12/6/7/1
histories, final 38/13/8/1 file inventory, preserved consumed ancestry, no obsolete
unapplied approach or transitional migration, and no new database/persisted
format migrations. Prior upstream nine-migration provenance is unchanged.

Accepted Advisory: the immediate request-count assertion after same-layout
reopen could miss a later asynchronous request. This is a narrow regression-test
limit: inspected production retains the editor/content and returns without a
fetch on that path. No observed product failure or additional implementation
is required for this rollout. A future change to reopen/fetch scheduling should
strengthen that negative assertion with quiescence or a late-request trap.
Existing WebUI-pin duplication, aggregate deployment-checker and wake-counter
Advisories remain recorded. Fresh exact-head Node/CI checks follow review.

Implementer0 committed `618df5530ba378f8b98f9557cdca700367016c11`, parent4a1da3c3,
with only `test/repository_browser.cjs` (40 additions, 7 deletions). Normal
`git commit -F`, hook inventory, Node syntax, staged/range whitespace and clean
worktree checks passed. Complete inventories now contain12/6/7/1 commits and
38/13/8/1 changed files; generic final diff is3858+/402−. Runtime e64/362/aca,
Codex closure and rooted bpz candidate remain unchanged. Retained reviewer0
receives the bounded general/architecture follow-up plus explicit complete
history/migration conclusion before final exact generic checks.

Normal SSH feature push advanced generic4a1da3c3 to618df553. Upstream master
remains base7c133c5 and is an ancestor; no rebase or default integration occurred.
Exact CI36860394508 is in progress on618df553. No superseded queued/in-progress
run needed cancellation. Fresh Luna/low `final_618df553_checks` owns the guarded
script `/tmp/portal-review-final-618df553.sh 36860394508`, with separate true
Node/CI stage statuses under `/tmp/portal-review-final-618df553/`. No duplicate
full local Go/flake/consumer build was launched. Fresh read-only activity still
reports working, and the active portal unit PID1250667/selected profile51i remain
unchanged; the supported package transition requires idle sessions.

## Final verification result and activation handoff

Fresh Luna/low `final_618df553_checks` completed its owned operation with status0,
elapsed303s. Committed-head Chromium real-editor harness passed (status0,49s);
exact generic CI36860394508 at618df553 concluded success (watch stage249s).
Separate stage status/log/elapsed and CI JSON are retained under
`/tmp/portal-review-final-618df553/`; no operation remains running. Reusable exact
evidence remains full Go/browser and generic flake at4a, workspace flake ataca,
bpz build/protocol, and extension362 CI/cluster smoke. The final optional fixture
changes no runtime input, so no consumer cascade or duplicate build is needed.

Main confirmed selected profile51i and active portal PID1250667 remain unchanged;
normal API activity reports working. Latest candidate activation and live new
UI acceptance are not claimed. The user can execute the guarded switch above
after this turn is idle. All feature branches and the session remain open;
shared DNS publication and default integration remain separately unapproved.

## Guarded profile activation and live acceptance

The normal candidate switch was launched only after the bound portal thread
reported idle. A first `nohup` launcher was removed by the command runner before
its script opened a log or changed the profile. Authoritative profile, portal PID
and process checks proved that no transition had started. The replacement used a
named transient user service and a fresh Luna/low observer. It ran the exact
reviewed command once, exited 0 after 88 seconds and left no running operation.
The unit reported `Result=success` and `ExecMainStatus=0`; full output is in
`/tmp/portal-review-switch-bpz-systemd/switch.log`.

The selected profile now resolves to
`/nix/store/bpzvfhdnrj3clw9zfd1qhrhw7fjksyvb-dev-workspace-0.2.0`.
`workspace-host status` reports that package, its bundled Codex reports 0.159.2,
and `workspace-portal@vpsfree-cz.service` is active with PID 2031444 and a new
14:27:17 CEST start time.

Direct live POSTs against the reported `2026-09-23-storage-redesign` vpsadmin
repository returned HTTP 200 for staged and unstaged captures. Both responses
contain `files: []`, zero-file statistics and immutable ephemeral snapshot IDs.
A Chromium run through the live router socket then passed with no page errors:
six full-width repository cards, a single desktop action row, no narrow-screen
overflow, empty staged and unstaged rendering, visible Origin and Load all diffs,
collapsed history on first load and full reload, and retained open history during
status refresh. The final run exited 0 in 8.8 seconds; its JSON summary is
`/tmp/portal-review-live-acceptance-final.json`.

This completes the authorized portal deployment and acceptance. The development
cluster remains on its already verified React and legacy UI rollout. The
unselected four-host DNS candidate and all default-branch integrations still
require separate approval.


## Repository-card final review result

Retained reviewer0 used saved gpt-6-sol/xhigh/read-only settings and reviewed the
complete 13/7/8/1 series across all four mandatory lanes. It found one Important
issue in `repository-review.js`: same-card refresh retains the workflow details
and summary but replaces the run links, dropping keyboard focus from a focused
run. `presentation_browser_test.cjs` covered summary focus only. Long checks and
rollout remain blocked until the narrow fix is committed and directly verified.

No other Blocking, Important or Advisory finding was reported. The reviewer
confirmed coherent commit splits, no obsolete unmerged approach, no unused
compatibility path and no transitional migration. None of the four ranges adds
a database or persisted-format migration. The selected API's nine upstream
migrations remain historical lineage with unknown production deployment and
rollback provenance. Workspace's final lock changes only generic and extension
nodes and preserves the approved Codex closure. Real browser/full Go/flake/CI,
new candidate build/protocol/catalog and live rollout remain pending.

## Workflow-focus correction and clean consumer graph

Published generic `6245fe9b` owns the three-file focus fix. Cache child
`1227f5c2` advances review v9/app v19 in five references, with CSS v3 retained.
The finite rejected non-force push discovered concurrent publication of `6245`;
only its unpublished amendment was rebased onto that published parent. The final
source tree equals the checked interim amendment. See the reusable
[publication lesson](../../notes/cross-project/2026-10-01-publication-before-amend.md).
No published history was rewritten or force-pushed.

The supported targeted extension lock update yielded `074926d3`; only its
`dev-workspace` node changes. Targeted workspace update followed by exact nested
`--override-input` restoration yielded `cd2875f3`, direct parent `4a6d44a2`.
Its only node changes are generic/extension; all other nodes, input maps and
`af40d966`/`07a5bfc8`/`f45c6f04` closure remain identical. The lead performed the
normal owned two-file workspace commit after member graph/quick checks because
member shared-index writes are restricted; no application edit was taken over,
alternate index or hook bypass used. All three refs were pushed over SSH by
fast-forward. Full inventory is now 15/8/9/1 commits and 40/13/8/1 paths.

Node syntax and mounted checks pass. Lead Nix workflow/template Go passed
0.115s after supplying the established GOFLAGS=-mod=mod; the omitted flag first
failed on inconsistent local vendoring before tests. Final clean workspace drv
is `/nix/store/ad34hy4q21lj2kppdddj7256glpm6djr-dev-workspace-0.2.0.drv`, not yet
built. Generic exact-1227 CI Check36877192519 and extension exact-0749
Check36877758314 are successful (finite exact-head metadata confirmed). Earlier-head
passes do not establish the new real-browser/candidate gates. The active bpz
runtime, configuration/DNS candidate and running cluster are unchanged.

## Workflow-focus affected-lane review result

Reviewer0 completed general, architecture/repetition and affected compatibility
recheck at exact `1227f5c2`/`074926d3`/`cd2875f3`/`d24b2515`, using saved
`gpt-6-sol`/xhigh/read-only settings. No Blocking, Important or new Advisory;
prior Important is resolved. It inspected unchanged run-node retention, exact
href restoration and native-summary fallback after reattachment, with no focus
theft or closed-disclosure opening, and all three mounted/real-browser cases.
It ran no tests. It explicitly confirmed coherent complete 15/8/9/1 histories,
preserved published `6245` and consumed ancestry, no obsolete supported approach
or unused compatibility path, and no authored database/persisted-format migration.
The nine upstream API versions and unknown production/rollback provenance remain
as inventoried. Unaffected scope/security conclusions stand. Accepted prior
WebUI duplicate-pin/helper mismatch and optional fixture proof limits remain.
Real browser/full candidate checks and guarded profile/live acceptance remain
separate gates; no operational readiness or new deployment authority is claimed.

## Exact workflow-focus verification operation

Fresh utility `/root/workflow_focus_final_1227` uses pinned policy digest
`d540572c…`, gpt-6-luna/low, matching native watcher config `dw_c1d02bb3…`.
It owns the single literal `/tmp/portal-workflow-focus-final-1227.sh` operation:
one browser-enabled full Go suite (including both focus engines), generic/
extension/workspace flakes, full candidate build/protocol, real-editor harness,
rooted extension packaged smoke, exact CI identities. Separate true stage logs,
statuses and elapsed values are under `/tmp/portal-workflow-focus-final-1227/`;
stop on first failure, no retries or source/deployment edits. Heads remain clean
and fixed at `1227`/`0749`/`cd2875`/`d24b`. The candidate will be explicitly rooted
at `/tmp/portal-workflow-focus-candidate-gc-root`; expected output is
`/nix/store/z20g487rcankkgaprsrdya5na079i1rl-dev-workspace-0.2.0`.
The candidate's evaluated editor input is the already rooted exact `3g3bvqgs…`
output; this does not claim whole-package equivalence with active bpz. Existing
roots and evidence remain. No check result is claimed until its status returns.

## Full Go/browser batch failure at 1227

The fresh watcher completed stage `01-go-browser` with exit 1 after 152 seconds;
the batch stopped with exit 1 after 153 seconds. Logs and separate statuses are
under `/tmp/portal-workflow-focus-final-1227/`. Stages 02–09 did not run. Firefox
`TestArchiveFailurePage` failed at `archive_failure_browser_test.cjs:82`, expecting
Running while the page showed Paused with an old fixture timestamp. Chromium
passed that fixture. All six `TestQuestionBrowser` children passed in 90.50s;
the presentation child passed Chromium and Firefox, including the new focus
regressions. These passes do not make the aggregate Go stage successful.

Source inspection suggests the preceding visible-wake refresh can still be in
flight when the fixture changes its operation response and dispatches another
wake. The banner assertion observes one branch of a Promise.all; the next wake
can be suppressed by the existing in-flight guard. This is a hypothesis pending
implementer confirmation, not a product diagnosis. Implementer0 is assigned only
the existing archive browser fixture, preserving throttling, hidden-page,
held-request, running/completion and read-only assertions. No retry, application
edit, consumer cascade, deployment or lifecycle operation is authorized by that
assignment. The clean published production graph and active bpz remain unchanged.

## Archive fixture correction committed

Implementer0 appended `869b8d4728394127ba949dc76724dce56eae136b`, parent
`1227f5c2`, changing only `portal/internal/web/archive_failure_browser_test.cjs`
(25+/1−). The fixture observes paused operation response bodies, changes the
still-old timestamps to identify refreshed Paused rendering, then awaits both
resumed response bodies and banner/detail rendering before the Running wake.
It requires the Running response body and UI while preserving all earlier
throttle, held-response, hidden-page, identity, warning, completion and read-only
assertions. The race diagnosis is supported by source; the failed log does not
record the private guard state. No production change or new visible prose.

Member Nix-provided Node and lead declared `nix develop` Node syntax pass;
staged/committed whitespace checks pass. Normal `git commit -F`, no framework or
custom hooks declared, sample-only hook directory; no bypass. Worktree/index
clean. Architect design.md:2257 confirms the optional fixture is not embedded
or installed as runtime code, so retain the ad34/z20 candidate and exact consumer
graph. Unfiltered source identity means no store-byte equivalence is claimed.
Complete inventory is now 16/8/9/1 commits and 41/13/8/1 paths. New bounded review,
exact-head CI and one corrected full Go/browser run remain pending; all later
candidate gates from the failed batch remain unexecuted.

## Archive fixture review and corrected verification operation

Reviewer0, saved gpt-6-sol/xhigh/read-only, reviewed exact clean verification
head `869b8d47` and retained `074926d3`/`cd2875f3`/`d24b2515` in general and
architecture lanes. No Blocking, Important or Advisory. It confirms both paused
response bodies/rendering precede Running, no relaxed assertion/private hook,
and the one-file optional fixture packaging. Complete 16/8/9/1 history is
coherent, preserves published ancestry and adds no database or persisted-format
migration. Earlier scope/risk conclusions and upstream nine-migration limits
remain; no production defect is established from the prior log.

After canonical SSH fetch, master remains recorded base `7c133c56`. Normal SSH
push advanced the feature from published `1227` to `869`; no rewrite or force.
Finite workflow metadata found no superseded active runs to cancel. New-head CI
is still required; old generic/current extension passes are not relabelled.

Fresh utility `/root/archive_fixture_final_869b8d47` uses the pinned d540 policy,
gpt-6-luna/low and matching native verification watcher configuration. It owns
one literal `/tmp/portal-archive-fixture-final-869b8d47.sh` run, with separate
stage/status/elapsed artifacts under `/tmp/portal-archive-fixture-final-869b8d47/`.
The nine-stage sequence updates only the generic verification-head guard while
retaining runtime/candidate/consumer identities and explicit GC roots. It stops
at the first failure; no retry, cleanup, source mutation, deployment or lifecycle
action. Head guards run before/after each stage. No new stage result is claimed
until the watcher reports it.

## Fresh account catalog evidence during the corrected batch

The lead ran the existing isolated App Server probe from generic869's declared
Nix environment with CGO_ENABLED=0/GOFLAGS=-mod=mod and exact Codex
`/nix/store/4mxlhqv9angcqgjw4c067nfpjlxv3d4h-codex-0.159.2/bin/codex`.
Resolved client module is version `v0.0.0-20260929193321-d210d3f7cc93`, no replace.
Client ListModels uses limit100/includeHidden=false with its normal cursor loop.
The read returned nine models and exactly one visible `gpt-6.1-sol`, default true,
default effort low and supported low/medium/high/xhigh/max/ultra. Raw nonsecret
catalog and module identity are `/tmp/portal-869-codex-catalog.json` and
`/tmp/portal-869-catalog-client-module.json`. No account credential or real session
thread was printed/created; the probe owns its isolated process/socket cleanup.

This is current exact binary/client/account catalog evidence, not a multi-page
test or a deployed successful turn. Reuse it only after the candidate protocol
stage confirms the packaged Codex is the same exact path; the pinned client and
approved af40 closure are unchanged. Candidate build/protocol and live new-UI
readback remain pending. No saved roster model/effort was changed.

## Corrected verification batch: first completed gates

Watcher `/root/archive_fixture_final_869b8d47` reports stage01 full Go/browser
exit0 in170s and stage02 generic flake exit0 in324s at clean exact869. The full
suite includes corrected archive diagnostics in Chromium/Firefox and all six
question-browser cases, including workflow focus. No extra focused browser run
was needed. Stage03 retained extension flake has started; stages04-09 remain
pending. The watcher owns exec handle1922, script PID/process group2582686.
No unexpected kernel build observed and no cancellation taken. Complete
per-stage artifacts remain `/tmp/portal-archive-fixture-final-869b8d47/`.
These results clear the corrected Go gate without converting the prior failed
1227 batch into a pass. The unbuilt z20 candidate and active bpz remain distinct.

## Final verification gate completed; guarded profile rollout authorized

Fresh watcher `/root/archive_fixture_final_869b8d47` completed its owned
`/tmp/portal-archive-fixture-final-869b8d47.sh` operation successfully. Parent
verified separate batch/stage artifacts. Stages 01-09 all status 0:

| Stage | Scope | Seconds |
| --- | --- | ---: |
| 01 | Full browser-enabled Go, including both engines | 170 |
| 02 | Generic flake at verification869 | 324 |
| 03 | Retained extension074 flake | 514 |
| 04 | Workspacecd287 flake | 254 |
| 05 | Exact candidate z20 build | 7 |
| 06 | Candidate/current protocol | 4 |
| 07 | Real-editor harness | 47 |
| 08 | Packaged extension smoke | 447 |
| 09 | Exact current CI | 5 |

Batch status0, elapsed1776s. Logs/status/elapsed are retained beneath
`/tmp/portal-archive-fixture-final-869b8d47/`. Generic869 CI36884355447 and
extension074 CI36877758314 conclude success. Both candidate/current Codex resolve
`/nix/store/4mxlhqv9angcqgjw4c067nfpjlxv3d4h-codex-0.159.2/bin/codex`, with
compatible schema/App Server. Candidate root is
`/tmp/portal-workflow-focus-candidate-gc-root`; exact target is z20. These results
are attributed to their actual heads; no consumer repin to optional869 is made.

The latest explicit user request authorizes one normal guarded user-profile
switch and live portal acceptance on `2026-09-23-storage-redesign`. It directs
shared DNS/configuration to remain prepared but unpublished and excludes default
integration. Prior DNS approval question is superseded by this explicit hold.

### Deployment launcher environment correction

The first named transient unit `portal-card-summary-switch-cd2875.service`
failed at the initial identity command (`dev-session: command not found`), before
source/profile prechecks or the switch. Status1/elapsed0; selected profile still
bpz, no switch occurred. The user-service environment lacks the interactive
user's command PATH. The corrected literal launcher supplies that known PATH,
retains all identity/source/profile/graph guards and will use a fresh unit,
watcher and v2 artifact directory. Original failure evidence is retained under
`/tmp/portal-card-summary-deploy-cd2875/`. No guard bypass or private helper.

### Guarded switch refused before profile selection

The explicit-PATH v2 launcher reached the normal source/package/schema checks,
then the installed predecessor's quiesce command refused this bound root thread:
its latest turn was `inProgress`. The exact switch artifact is status1/elapsed59s,
and the named unit's completed result is exit-code/ExecMainStatus1. Both selected
profile records remain bpz. The watcher's early report sampled transient unit
state and looked for shortened artifact names; parent checked the finalized
`switch.status`/`switch.elapsed` and authoritative unit result after completion.
The log is `/tmp/portal-card-summary-deploy-cd2875-v2/switch.log`.

No selection or deployment occurred; normal refusal/restoration and pending
compatible Codex reconciliation remain intact. No force/private activation or
state clearing is permitted. A bounded read-only architect assessment is checking
one normal idle-gated continuation before ending this lead turn. Live acceptance
harness preparation continues independently; no acceptance of the old UI is
claimed for the new candidate.

### One-shot idle-gated deployment and live acceptance continuation

Architect0's read-only source assessment confirms the installed public
`workspace-portal thread require-idle` is a suitable read gate: exact thread/cwd,
terminal turn state, pending requests, queued messages and unresolved submissions
are checked without interrupting/resuming/archiving/submitting. Ordinary ledger
lock creation is possible, but the ledger is not rewritten. It is advisory, not
an idle reservation; the actual switch repeats full root/team/session and
journal/cluster/runtime/profile/registration gates.

The parent prepared `/tmp/portal-card-summary-idle-deploy-accept-cd2875.sh` for
one named user unit. It waits at most600s only for the exact bound lead's expected
inProgress refusal; any other read-gate error or source/profile identity change
stops. Once idle, it runs the already authorized clean-source candidate switch
once, never retries it, verifies actual z20 selection/service executable/model
catalog, then executes the prepared live acceptance harness. The parent will
finish its turn so the normal idle boundary can pass. A fresh Luna/low observer
owns monitoring of that exact named unit and independent status artifacts.
No deferred cleanup, session lifecycle or extra deployment is scheduled.

Implementer0 delivered syntax-checked ephemeral
`/tmp/portal-card-summary-live-cd2875.cjs` (SHA256
16b52b1c468f1d4b75072195d3c0ba08a575dc8f8b465aa549dafa366fd74b9f).
The normal live page/API/socket proxy is limited to the explicitly authorized
storage-redesign page, its GET resources and staged/unstaged capture POSTs.
It checks six cards, frozen history summaries, run-derived counters/compact
states, closed defaults, spacing and desktop/mobile layout, observed details
refresh/focus/node retention, frozen POST+GET snapshots and reload/cache reset.
It emits aggregate metadata only. Fixed live data may not exercise changed/
removed run-link transitions, already proven by the complete both-engine suite;
first-repository empty snapshots may not provide a nonempty file preview.
Node and browser store outputs are explicitly rooted for the operation.

Parent logs/status are under
`/tmp/portal-card-summary-idle-deploy-accept-cd2875/`: batch.log/status/elapsed,
01-switch and02-live-card-acceptance logs/status/elapsed, selected-before/after,
service-state/portal-executable/live-models. No stage is accepted before status
and actual selected identity are checked. If selection precedes a failure,
retain z20 and use ordinary selected-helper forward recovery rather than retrying
--from-candidate. Pending Codex record is retained; installed reconciliation
cannot select an unselected package and is not a substitute for the switch.

## Guarded z20 deployment completed; acceptance harness diagnosis only

The independent observer of invocation38d8db52d6f94936b263ea94952d5f0d reports
stage01-switch status0/70s. Parent rechecked finalized artifacts under
`/tmp/portal-card-summary-idle-deploy-accept-cd2875/`, actual selected profile,
portal executable and service state. Beforebpz, afterz20; portal PID3043113
executes z20/bin/workspace-portal. Portal, Codex and router remain active/running
with successful service results. Live-models.json confirms nine models, exactly
one visible gpt-6.1-sol with high/xhigh. No switch retry is authorized or needed.

Stage02 acceptance status1/32s, combined batchstatus1/149s. The original probe
SHA25616b52b1c468f1d4b75072195d3c0ba08a575dc8f8b465aa549dafa366fd74b9f
is preserved. Its log contains an unhandled page.waitForResponse timeout30000ms
at line173, the history-response observer registered after navigation. A missed
eager response is a hypothesis pending implementer0's source-based diagnosis;
there is no claim yet that the live UI failed its requested behavior. Latest
user authorizes bounded ephemeral correction and live-only rerun, and directs
z20 preservation and DNS/configuration/default holds. Saved implementation
purpose/workspace-write was confirmed before the scoped assignment.

### Bounded live-harness correction and live-only rerun

Implementer0 preserved the original probe and delivered separatev2, SHA256
ad295658755ef529b2894a7c96af50da9ed582eb27974c24ac8fcb82a1c0f7a7.
Source/log establish an unhandled observer rejection; the log does not prove
whether a history request was sent or an eager response was missed. The prior
ok-only predicate also excluded non-2xx responses. V2 observes history requests
and responses before navigation, resolves any status, bounds the wait after
activation, and emits sanitized counts/statuses/load-state diagnostics. It
immediately catches snapshot/details wait rejection. All requested summary,
workflow, layout, focus, frozen snapshot/preview, reload and page-error checks
remain. Parent inspected the exact ephemeral diff; Node syntax passed. No
repository/branch/product/cache/protocol change or new committed-review gate.

A fresh pinned Luna/low utility will own one literal live-only operation
`/tmp/portal-card-summary-live-only-cd2875-v2.sh`, logging beneath the matching
`/tmp/portal-card-summary-live-only-cd2875-v2/` directory. It guards selectedz20
and exact clean workspacecd287 plus the probeSHA, then runs only the normal live
storage-redesign probe. No deployment/activation/reconciliation, code/pin change,
DNS/default action or retry is included. The failed original run remains failed;
new acceptance is pending until true status/result evidence arrives.

### Live-only v2 diagnostics: initialization remains unproved

Fresh Luna/low watcher ran the live-only v2 command once, status1/33s. Log
`/tmp/portal-card-summary-live-only-cd2875-v2/log` reports load-repositories
TimeoutError with zero history requests/responses, zero review-module requests
and one page exception. This is not evidence of a missed history response; the
review module never requested in this observation. Original unhandled timeout
is now bounded, with more useful diagnostics. The current failure may precede
repository mounting. Main assigned further bounded initialization/transport/DOM
contract investigation to implementer0; no speculative product defect is claimed.
A message initially understated pageErrors, immediately corrected from the log.
No switch or other deployment was retried; selected z20 is retained. No acceptance
claim is made from v2 and no blind rerun is authorized without better evidence.

### Concrete probe bootstrap mismatch found in source

Parent read-only source inspection found app.js:969 awaits
`/codex/assets/conversation.js?v=11` before installing repository activation
listeners at2294-2314. The ephemeral proxy allowlist permitted /static/ but
rejected /codex/assets/ with403. This is a concrete probe/server interface
mismatch consistent with one startup exception and no review/history request.
Implementer0 is correcting only the bootstrap GET allowlist and adding numeric
conversation-module diagnostics. Live success must still establish actual module
loading; the earlier log did not identify the exception text. /api/models is a
normal read-only bootstrap request whose failure is caught separately, and is
not assumed to be the startup exception. All acceptance assertions and the two
capture-only POST restriction remain. No product/deployment scope changes.

### Source-proven proxy correction accepted for one live-only v3 run

Implementer0 confirms both session stylesheet references and app's awaited
conversation import use /codex/assets/. The v2 proxy deterministically returns
403 for those GETs, so an executing app cannot register repository activation
handlers after that await. V2's exact exception stack was not retained, so another
exception is not excluded. V3 permits the necessary /codex/assets/ GET resources
and exact read-only models/limits bootstrap endpoints; captures remain the only
permitted POSTs. It observes required conversation module2xx/version11 before
interaction and native tab/panel activation before history observation, with
sanitized numeric/module/frame diagnostics. All original behavior assertions
remain. Parent reviewed v2-to-v3 diff and Node syntax; no application code changed.
ProbeSHA09ab0478ef60fd9658dcc47a25b30532d14c33a18e52574a96381295b872f376.

A separate fresh pinned Luna/low watcher owns one live-only v3 literal wrapper.
Artifacts retain under `/tmp/portal-card-summary-live-only-cd2875-v3/`; failed
original/v2 evidence remains separate. Selected z20 and exact clean workspacecd287
are guarded before/after. No profile switch, activation, reconciliation or other
operation is included. Acceptance remains pending actual status/result.

### V3 assertions completed; owned probe terminated after teardown hang

The user supplied the bounded 1069-byte v3 excerpt: complete JSON `ok:true`,
six repositories and six frozen history summaries, desktop/mobile one-column
layout, desktop action row, 1rem margin/.5rem gap, retained history/card through
an observed details GET, zero-file staged/unstaged arrays, reload reset, assets
app19/review9/css3 and no page exceptions. Its workflow baseline contained six
unavailable states, so it did not prove nonempty workflow counters or run-link
focus; the observed focus target was the history summary. Keep this limit explicit.

The command remained alive after printing its result. Implementer0 traced the
proxy's unowned outbound ClientRequests, including the normal EventSource GET;
closing browser/server-side connections does not destroy those upstream clients.
The user accepted this diagnosis and authorized only the existing watcher's
termination of the stuck probe. The watcher preserved argv/PPID evidence for
bash3064937 and its Node child3065035, sent SIGTERM only to that verified Node,
and accounted for exec37040. Final status143/751s and the success JSON are retained
under `/tmp/portal-card-summary-live-only-cd2875-v3/`; neither process remains.
This is incomplete verification, not status0 and not a portal failure.

Implementer0 was assigned separate v4 with explicit ClientRequest ownership and
awaited server teardown on success/failure. All acceptance assertions/observations
remain unchanged; no process.exit, timer, app hook or product edit is authorized.
Parent will inspect the exact diff/Node syntax, then delegate one fresh live-only
run. z20 remains selected; no switch, reconciliation, publication, merge or
session lifecycle action is included.

### Teardown-only v4 inspected and assigned once

Implementer0 delivered `/tmp/portal-card-summary-live-cd2875-v4.cjs`, SHA256
1a2b68f48f0bacc47bf2c0ced79998ce7f1e9f94455291af035b6159d2712131.
Parent inspected the full v3-to-v4 diff and reran exact Node syntax: only proxy
request ownership/error cleanup and the final awaited close changed. The Set
removes requests on close, destroys the corresponding upstream on early
browser-response close, and drains remaining requests after initiating proxy
close. Nested finally retains proxy teardown if browser.close rejects. All
assertions, waits, observations and output remain unchanged; no process.exit
was introduced. Original/v2/v3 hashes remain unchanged.

The selected profile is still z20 and workspacecd2875 remains clean. Fresh
pinned Luna/low utility `portal_live_only_cd2875_v4` owns one execution of
`bash /tmp/portal-card-summary-live-only-cd2875-v4.sh`, guarded by those identities
and the exact probe hash. Artifacts are under its matching /tmp directory;
acceptance requires true exit0 plus the JSON. No second operation or cancellation
is delegated. User-authorized v3 termination is complete; no owned v3 process
remains. No deployment or lifecycle action is included in v4.

### Live-only v4 passed with normal teardown

Fresh Luna/low `portal_live_only_cd2875_v4` executed the literal wrapper once,
true exit0 matching status0, elapsed10s. Parent read the completed JSON/status and
rechecked selected z20 plus actual portal executable and active portal/Codex/router
units. There is no running probe handle or cancellation for v4. This establishes
normal completion after the teardown-only correction; it does not retroactively
make the terminated v3 command pass.

Observed normal storage-redesign UI/API proof: six repositories and six frozen
history summaries; 1rem top margin/.5rem action gap; desktop one-column/action row
and mobile one-column/no overflow; observed details GET with retained history
node/open state and history-summary focus; empty staged/unstaged POST+GET arrays
and no-changes rendering; closed disclosures after reload; app19/review9/css3;
zero page errors. All six sampled workflow states were unavailable, so
workflowCountersVerified0 and runLinkOutcome not-applicable are limits, not
positive nonempty counter/link proofs. Both captures used the first repository
and were empty, so no nonempty preview was exercised. Original v4 observations
and assertions were preserved exactly as requested.

Artifacts: `/tmp/portal-card-summary-live-only-cd2875-v4/{log,status,elapsed}`.
Runtime/candidate remains1227/074/cd287/z20; optional verification head869 and
configurationd24 are unchanged. No source/branch/cache/pin, switch, reconciliation,
cluster/system/DNS or lifecycle operation occurred. DNS/configuration remains
prepared and unpublished; defaults remain unmerged and lifecycle remains active.

## Explicit default-branch integration approval (2026-10-01)

The latest user directly approves every registered repository and its configured
remote default branch. Exact scope and approval wording are recorded in
[integration.md](integration.md). Phase is now default-branch integration:
fetch, patch-equivalent rebase if needed, review/check, comparison capture,
fast-forward-only SSH push and exact remote ancestry proof. No approval is
requested again for that scope. Shared DNS deployment remains held; z20 stays
selected with no switch retry. Session/feature refs remain open and retained;
no archive/delete/stop/retirement action is authorized.

### Post-push CI is report-only

The user explicitly supersedes the prior CI wait: complete pre-integration
review/checks and all pushes/proofs, then report applicable CI URLs/initial states
without waiting for completion. No CI-wait watcher is authorized for this phase.
All deployment, DNS publication and lifecycle holds remain.

## Default integration completed and durable handoff requested

All seven final-head remote ancestry checks passed after fresh SSH fetches;
exact results are in integration-remote-proofs.json. The user then explicitly
requested a durable tracking/handoff commit and push without waiting for CI.
This is the authorized consolidated integration handoff checkpoint. It includes
only this initiative's coordination records and owned reusable notes; preserve
all unrelated shared-checkout/index changes. No lifecycle transition is made.
