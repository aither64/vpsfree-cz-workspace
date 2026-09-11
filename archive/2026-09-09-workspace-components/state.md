---
lifecycle: complete
---

# 2026-09-09-workspace-components

## Current deployment checkpoint (2026-09-11)

- The aitherdev cutover is accepted. The live NixOS generation is
  `/nix/store/r43gb0agv9zhh0rxrlk8s5nw13mq890i-nixos-system-aitherdev-26.05.20260903.a5cc6f2`
  and the selected user package is
  `/nix/store/41mxyvi54bb6w1y5x959j184b6qlhlfi-dev-workspace-0.2.0`.
- The deployed dependency chain is `workspace@d00f8ee ->
  organization@3e3f0ff -> generic@4b3d426 -> codex-web@7a05da0`;
  configuration `6956ff4` pins the same generic and Codex heads. Workspace
  cleanup commit `b5aae3d` removed the completed one-time aitherdev cutover
  script, runbook and contract test and is fast-forwarded to local and remote
  `master`.
- All old user, runtime, router and root-owned credential paths are absent.
  Router, portal, Codex App Server and tmux services are active under the new
  namespace, certificate renewal is active, and authenticated HTTPS access to
  the stable portal succeeds with the expected TLS identity.
- The three audited development clusters were reset. Nine intended active
  session authorities were recreated: eight Codex sessions and one shell-only
  session. All 18 portal manifests and every recorded thread materialization
  validate; the archived authority was not recreated.
- Forward-only deployment recovery handled two concrete activation races in
  place: migrated absolute systemd instance links were re-enabled from the new
  package, and router admission waited for the socket after systemd reported
  the service started. Credential contents, modes and ownership matched the
  migration journal, and the post-activation tar inventory remained stable.
- `codex-web`, generic `dev-workspace`, organization `dev-workspace`, and the
  configuration worktrees are clean at their pushed heads. Every exact feature
  head is now merged into and equals its remote `master`; retained feature
  branches were not deleted. The post-merge `codex-web` Actions run is green.
  Duplicate master-branch runs for the already-green exact generic and
  organization heads were still in progress when the user explicitly directed
  cleanup to proceed without waiting. No configuration workflow run appeared
  for the exact head when checked.
- GitHub still advertises `2026-09-09-workspace-components` as the default
  branch of `vpsfreecz/dev-workspace`, although both that branch and `master`
  point at `3e3f0ff`. Changing the repository default to `master` was attempted
  and returned HTTP 403 for the available token. No further review cycle will
  be run, per the user's instruction.

## Superseded review v42 checkpoint

- All v41 Blocking and Important findings are remediated, committed and pushed
  at the exact heads prepared for `review-packet-v42.md`.
- The final dependency chain is `workspace@7be93a1 -> organization@0d3fbb1 ->
  generic@2e43821 -> codex-web@7a05da0`; configuration `c75b9e9f` pins the same
  generic and Codex heads. Compatibility source `57ffc0b` is immutable and not
  exported by the final workspace flake.
- Both generic repositories retain enforced case-insensitive source scans for
  `vpsfree` and `aitherdev`. The organization tree retains its `aitherdev`
  exclusion. Workspace presentation and provider selection now have one
  authority: `.dev-workspace.json` in the registered workspace root.
- The concrete deployment is now one strict workspace-owned operator script.
  It checks the exact live inventory before any mutation, stops every managed
  session and old tmux/App Server process, drives concrete forward and reverse
  migrations and system/profile activation, and recreates every session before
  reopening either router. Interrupted final recreation stops only actual
  authorities proven to be a subset of the reviewed inventory.
- Generic `dev-session start --replace-missing-thread` resumes the recorded
  thread when present and creates a fresh one only when absent. The
  compatibility restart runs before migration preflight, so any replacement
  manifest is journaled and exactly reversible. The complete restart command
  now tests both portal URL fields and the required-runtime flag.
- Certificate renewal remains runtime-masked through forward acceptance or
  completed rollback. The recovery TSV uses `-` for an empty link target, so
  exact-range whitespace validation passes. The workspace deployment checker
  now rejects a non-object registration with a concise contract error.
- General's GitHub-default finding remains an explicitly accepted
  repository-metadata deviation after the administrative update returned HTTP
  403; neutral `master` exists and exact consumer pins are unaffected.
- Generic host tests pass with 73 runs / 453 assertions. Organization migration
  tests pass with 43 runs / 831 assertions. Generic dev-session tests pass with
  286 runs / 2887 assertions and all portal Go packages pass. Workspace
  deployment tests pass with 3 runs / 14 assertions; its cutover contract passes
  with 5 runs / 29 assertions, and the changed flakes pass no-build evaluation.
- The committed 37-line recovery manifest exactly matches all 11 live target
  recovery roots and aggregate hash
  `837e40a5f9754a9f9ae6442dfebc356288d9f32d0d3c8e58123c9d5eb1cbe917`.
- Exact `codex-web` Actions run `34555724208` is green. Exact-head generic run
  `34572091420` and organization run `34572849148` are in progress. Generic run
  `34568265248` failed only because a new test repeated the forbidden legacy
  prefix; its logs were inspected, the redundant literal was removed and the
  exact source scan passes. Cancellation was submitted for superseded
  organization runs `34569805854`, `34569273665`, `34568494154` and
  `34564709694`; superseded generic run `34569227294` could not be cancelled
  because the token returned HTTP 403.
- Review v41 found three General Blocking issues, one Risk Blocking issue and
  three Important issues: late inventory admission, non-gating shell snippets,
  missing concrete activation/reverse commands, missing ready-thread
  replacement, partial session-recreation rollback and stale tracking. The
  workspace-owned script and generic restart support remediate all of them;
  v42 reruns all four lanes from fresh context. Long NixOS VM/integration builds,
  host activation, user-profile migration and default-branch integration have
  not started.

## Repositories

- Coordination checkout: `/home/aither/workspace/ai/vpsfree.cz`, branch
  `master`.
- Workspace review base:
  `a3a3804a2acfd114796a63995b8f16ca3537f4a4` on shared `master`.
- Configuration review base:
  `e5458562a2a8cb12fe002be20b2d82e6a741f7ee` from remote `master`.
- Initial tracking commit:
  `58ccb4da27d6e1ef26c330662b2471d559d2c437`.
- `dev-workspace`: branch `2026-09-09-workspace-components`, worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/dev-workspace`,
  base `f39f8e62097b5e9da9de8a5eb678131b1e478e35`, remote
  `git@github.com:aither64/dev-workspace.git`, head
  `4b3d426d0484a62bac5bcfc7d5c7b6ff2140b045`.
- `codex-web`: branch `2026-09-09-workspace-components`, worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/codex-web`,
  base `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8`, remote
  `git@github.com:aither64/codex-web.git`, head
  `7a05da0cd79b19f3c9a0a8fa23b7043a1f984d4e`.
- `vpsfree-cz-configuration`: branch
  `2026-09-09-workspace-components`, worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/vpsfree-cz-configuration`,
  base `e5458562a2a8cb12fe002be20b2d82e6a741f7ee`, head
  `6956ff4197d36e731084b3167b0d5e76b5003583`.
- `vpsfree-cz-workspace`: branch `2026-09-09-workspace-components`, worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/workspace`,
  review base `a3a3804a2acfd114796a63995b8f16ca3537f4a4`, deployed head
  `d00f8ee6bf187850159ffee42d2b8f617d6d2243`, cleanup/current head
  `b5aae3d9fd412bea5bd04653c223cc9161952cc9` (fast-forwarded to `master`).
- `vpsfreecz/dev-workspace`: branch `2026-09-09-workspace-components`,
  worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/vpsfree-dev-workspace`,
  neutral base `9b8d07e12c1115aef1c09cfafbc71ba10e167853`, filtered-history head
  `3e3f0ff7c2d23f08f19887822efa12f969bbb56f`, remote
  `git@github.com:vpsfreecz/dev-workspace.git`, and local project name
  `vpsfree-dev-workspace`.

## Status

- The requested four-layer ownership split is implemented. Generic components
  contain no organization or host naming; concrete domains live in the
  workspace consumer and privileged NixOS values live in configuration.
- Both generic repositories and the organization repository have GitHub
  workflows running their full flake checks with the verified current official
  checkout and Nix-install actions.
- The final runtime has no legacy environment, tmux or path aliases. The
  compatibility generation is retained only as historical package state and
  is no longer selected.
- The workspace feature is integrated into `master` and the one-time cutover
  implementation is removed. All four remaining exact feature heads are also
  fast-forwarded into their remote `master` branches. Feature branches remain
  retained.

## Commands run

- Read `AGENTS.md`, the prior plan, state, assessment and independent handoff.
- Verified `/proc/self/cgroup` is
  `/user.slice/user-1000.slice/session-614.scope`, outside
  `workspace-codex@vpsfree-cz.service` and
  `workspace-tmux@vpsfree-cz.service`.
- Verified this shell has no inherited `VPSFREE_*` variables and
  `dev-session current` reports no current managed session.
- Read official OpenAI App Server documentation and the OpenAI Docs,
  vpsFree user-facing writing, mandatory change review and session handoff
  skills.
- Inspected the current portal, Codex adapter, lifecycle helpers, package,
  cluster flakes, aitherdev configuration, runtime contract and project map.
- Fetched workspace `origin`; local `master` remains one scoped tracking commit
  ahead of `origin/master`.
- Verified both new GitHub repositories are public, reachable over SSH, empty
  and have no default branch.
- Ambient Python lacked PyYAML for the tracking check. Ruby's standard YAML
  library validated the portal manifest instead; the scoped staged diff also
  passed `git diff --check`.
- Pushed `dev-workspace` bootstrap commit
  `f39f8e62097b5e9da9de8a5eb678131b1e478e35` to public `master`.
- Pushed `codex-web` bootstrap commit
  `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8` to public `master`.
- `nix flake check --print-build-logs` passed in both bootstrap repositories.
- Created canonical bare clones and dated worktrees for all affected
  repositories. The configuration worktree hook reported missing ambient Ruby
  gems after successfully creating the worktree; subsequent commands will run
  through its Nix development environment.
- `codex-web`: `CGO_ENABLED=0 go test ./...` passed at the final head. The
  initial feature also passed Node syntax and browser contract tests and
  `nix flake check --print-build-logs`.
- `dev-workspace`: `CGO_ENABLED=0 go test ./...` passed after the final
  `codex-web` pin. Full core and vpsFree package builds passed before the final
  dependency-only follow-up, including Go, lifecycle, cluster and host suites.
- `vpsfree-cz-workspace`: `nix flake check --print-build-logs` passed with the
  final dependency tree. The feature branch is based on current shared
  `master` at `91b85b48b35cef51fd8920cd3445ca23a0023648`.
- `vpsfree-cz-configuration`: `confctl` produced the final exact feature pin,
  Nixfmt and all pre-commit hooks passed, and a dry `confctl build` recognized
  `cz.vpsfree/machines/aitherdev` before stopping at the confirmation prompt.
  Repeated intermediate input updates were consolidated before review.
- Pushed every dated feature branch. Configuration Git operations must run
  through `nix develop` because its Overcommit hooks require repository-pinned
  Ruby gems; the existing durable note documents this requirement.
- Investigated current-head `dev-workspace` CI run `34393548789`: its only
  failure was the expected Nix `vendorHash` mismatch after the final Go module
  pin (`sha256-KrT...` specified, `sha256-NtG...` computed). Updated that hash,
  folded it into the dependency commit and pushed the rewritten dependency
  chain. GitHub refused cancellation of two superseded in-progress runs with
  HTTP 403 because the available token lacks Actions write permission.
- Focused host-module building exposed two pre-review defects: a literal patch
  marker in the generated multi-name certificate check and a restored
  ShellCheck SC2016 diagnostic. Corrected both, added a multi-name example
  regression check, built `checks.x86_64-linux.host-module` successfully and
  folded the fixes into the owning implementation commit.
- Mandatory review v4 ran all four required lanes with `gpt-5.6-sol` at
  `xhigh`. It found three blocking and four important issues plus advisories:
  rejected intermediate commit states and redundant pin-only follow-ups;
  repeated hand-written ledger lock transactions; durable retry keys that did
  not include a custom conversation target; a browser contract that used a
  duplicate fake client; stale coordination state; and browser targets where a
  backslash could normalize into a cross-origin URL.
- Rewrote only the unmerged feature histories to remove rejected intermediate
  states and keep the final dependency pin in the owning commit. Added one
  locked transaction helper and release-on-error coverage, same-origin URL
  normalization, endpoint-bound durable namespaces with an explicit alias
  override, real shipped-client browser coverage, an embedded shared
  conversation client, and documented removal criteria for compatibility
  aliases and command/skill tombstones.
- Re-ran final-head quick verification after those fixes. `codex-web` passed
  its browser contract and complete race-enabled Go suite. `dev-workspace`
  passed every portal package with the race detector. The workspace flake
  check and configuration no-build flake check passed at the exact final pins.
- Force-pushed the cleaned feature histories with lease protection. The exact
  dependency chain is now `vpsfree-cz-workspace@b7f23e0 ->
  dev-workspace@7022856 -> codex-web@2c2d2e1`; the configuration feature also
  pins `dev-workspace@7022856`.
- Mandatory review v5 found a blocking retained commit boundary, a blocking
  browser client/storage identity gap, two important reusable-boundary and path
  issues, and two advisories. The Scope lane was clean. Reconciled every
  finding: application-owned ledger paths retain the old compatibility default;
  browser clients carry immutable endpoint identity into durable senders;
  arbitrary clients require an explicit target; root paths join canonically;
  dot-segment, encoded and backslash paths are rejected; and the standalone
  example enforces loopback endpoints plus anti-framing headers.
- Folded legacy route aliases, browser paths, shared storage and their tests
  into the original `dev-workspace` dependency-integration commit. The exact
  resulting boundary `9ce1cec` passes every Go package independently; no
  retained commit temporarily breaks the old `/api/sessions/` conversation
  contract. Removed six unused `codex-web` module dependencies.
- Investigated exact-head `codex-web` CI run `34433947701`. The failure was a
  deterministic Nix fixed-output hash mismatch after dependency cleanup, not a
  flaky test. Updated the owning flake hash to the reported value and ran
  `nix flake check --print-build-logs` successfully at the rewritten final
  head. Propagated that final source revision through all downstream exact pins.
- Mandatory review v6 found three independent manifestations of two security
  boundaries in `codex-web`: reflectively mutable client target metadata, and
  noncanonical or twice-decoded opaque URL segments. General reported two
  Important findings, Architecture one Blocking finding and Risk two Blocking
  plus one Important finding; Scope remained clean.
- Replaced discoverable Symbol metadata with a module-private `WeakMap` and a
  frozen target record. Browser clients and durable senders can no longer have
  their endpoint and persistence identity redirected independently.
- Parse `URL.EscapedPath()` on the server, decode each opaque conversation and
  queue segment exactly once, require an encoding identical to JavaScript
  `encodeURIComponent`, and reject dot segments, repeated separators, trailing
  aliases and noncanonical escapes before resolution or mutation. Browser and
  Go regressions cover literal `%`, `%41`, `%2F`, `%2e%2e`, Unicode, dot IDs,
  malformed path aliases and queue deletion.
- The remediated `codex-web` head passed its Node browser contract, the complete
  race-enabled Go suite and `nix flake check --print-build-logs`. Ambient Node
  and C compilation were absent, so these checks used Nix-provided Node, Go and
  GCC as required by the repository.
- Folded the remediation into the original conversation commit and propagated
  exact pins and vendor hashes through all downstream owning commits. The
  remediated dependency chain is `vpsfree-cz-workspace@db2c24a ->
  dev-workspace@d880db6 -> codex-web@94977e9`; configuration head `2e6f55eb`
  also pins `dev-workspace@d880db6` and nested `codex-web@94977e9`.
- At the final downstream heads, the dev-workspace portal passed every Go
  package with the race detector, and dev-workspace, workspace and
  configuration each passed a no-build flake evaluation. The configuration
  input was changed only through `confctl inputs channel set --commit`; its
  Nixfmt and commit hooks passed. Configuration rebase and push hooks required
  `nix develop`, and their generated `.bin` and `.bundle` helpers were removed.
- Mandatory review v7 found one Blocking and five distinct Important issues:
  falsy custom-client targets bypassed explicit identity, the browser and Go
  identifier domains differed on length and UTF-8, Go accepted base paths that
  could never route through `EscapedPath`, the legacy portal adapter erased
  escaped spelling before conversation and lifecycle dispatch, and the retained
  dependency commit temporarily dropped the existing nonblocking prompt policy.
- Remediated all v7 findings. Supplied path options now default only when absent
  and reject empty, null and non-string values before storage. Browser and Go
  enforce valid Unicode and a 256-byte UTF-8 ceiling; Go base paths use an
  explicit browser-compatible ASCII path alphabet. The legacy adapter validates
  the untouched escaped path before ServeMux normalization and preserves the
  raw queue segment through delegation. The 60-second hidden plus 60-second
  visible prompt policy and its behavioral test now live in the original
  `dev-workspace` dependency commit.
- The exact rewritten dependency commit `dbb617a` independently passed every
  Go package with `-mod=mod -race`. The final `dev-workspace` head passed the
  same complete race suite and a no-build flake evaluation. `codex-web` passed
  its complete flake check after the v7 remediation.
- Propagated and pushed the final exact dependency chain:
  `vpsfree-cz-workspace@50de231 -> dev-workspace@9f934d2 ->
  codex-web@dc52d0d`; configuration `f8619943` pins the same nested revisions.
  The configuration pin was again generated only through `confctl`, and all
  generated shell helpers were removed after its clean evaluation and push.
- Exact-head GitHub Actions run `34437088347` for the preceding codex-web head
  passed. The newest provider pushes started replacement runs. Attempts to
  cancel superseded dev-workspace runs `34434884079` and `34434307304` still
  fail with HTTP 403 because the token lacks Actions write permission; see the
  durable cross-project note.
- Mandatory review v8 found two General Important issues and one Risk Important
  issue; Architecture had one commit-message Advisory and Scope was clean.
  Queue start now uses the same Unicode/byte/dot/slash/NUL identity validator as
  deletion without trimming whitespace. Browser and Go base paths share one
  explicit printable-ASCII alphabet with exhaustive parity tests. Both direct
  and legacy routes reject raw-path hints Go would otherwise silently
  canonicalize before exact spelling validation.
- Folded the v8 fixes into the original conversation and dependency commits,
  and corrected the retained policy provenance in the dependency and
  presentation commit messages. The exact pushed dependency chain is now
  `vpsfree-cz-workspace@3fb1eab -> dev-workspace@014092d ->
  codex-web@a46ccd2`; configuration `0c6447a` pins the same revisions.
- The final codex-web tree passed every race-enabled Go package and its Node
  browser contract. The exact rewritten dev-workspace dependency commit
  `6a1fd10` and final tree independently passed every race-enabled Go package.
  All four final flakes passed no-build evaluation; configuration input changes
  were again made only by `confctl`, and its hooks passed.
- Mandatory review v9 found the valid queue ID `start` could not be deleted, a
  shared cross-language parity oracle was missing, and decoded control
  characters could alter log structure. The route is now method-disambiguated,
  both test suites consume `conversation/testdata/path_contract.json`, and logs
  quote decoded request paths.
- An uncached rerun of the exact dependency commit exposed that the new shared
  browser's collaboration-mode request was not in the bounded legacy GET alias
  list. Added `models` and `collaboration-modes` to that adapter and reran the
  exact commit successfully with `-count=1 -mod=mod -race` and Node available.
  Final codex-web tests also ran uncached. The exact pushed dependency chain is
  now `vpsfree-cz-workspace@e374791 -> dev-workspace@d09221b ->
  codex-web@e8655b7`; configuration `d6331b2` pins the same revisions.
- Mandatory review v10 had clean General, Architecture and Risk lanes. Scope
  found the per-session `models` and `collaboration-modes` aliases supported
  only an intermediate design. Restored the original global mode lookup in the
  dependency commit and removed both unused aliases and test rows. The exact
  dependency commit `fa5f7d4` and final dev-workspace tree independently pass
  uncached with the race detector and Node present. The exact pushed chain is
  now `vpsfree-cz-workspace@4b4cf06 -> dev-workspace@7763a02 ->
  codex-web@e8655b7`; configuration `c6d3fb1` pins the same revisions.
- Mandatory review v11 is clean in all four required lanes (General,
  Architecture/Repetition, Scope/Proportionality and Risk/Compatibility), with
  no Blocking, Important or Advisory findings. Reviewers confirmed that the
  final compatibility adapter contains only real pre-split conversation
  consumers, destructive workspace routes remain excluded, the shared Go/Node
  path oracle prevents identifier-contract drift, the retained dependency
  commit already contains the final global mode lookup, and all four exact
  dependency pins agree.
- Long validation built the generic and vpsFree provider packages, the complete
  provider flake, the workspace wrapper and the aitherdev NixOS closure. The
  host dry activation and live switch passed; systemd and firewall health checks
  both succeeded without a kernel build.
- User-profile switch to generation 15 succeeded. The router, Codex, portal and
  tmux services were active; both runtime sockets existed; the portal health,
  model catalog, collaboration-mode catalog, index and retained thread APIs
  responded; authenticated TLS health at the stable hostname succeeded.
- Live rollback selected retained generation 14 and kept every service healthy,
  but failed while restoring the first quiesced terminal client: the outgoing
  helper correctly failed its package-generation check after the profile link
  changed. Folded target-generation restoration and its regression into the
  original host-ownership commit, corrected the installed-update documentation,
  and regenerated the exact workspace and configuration pins. Mandatory review
  packet v12 covers this live-test remediation.
- Mandatory review v12 found that restoration still stopped after the first
  failing session, its test did not exercise the real helper paths, and the
  deployment example needed a clearer bootstrap boundary. Restoration now
  attempts all clients and aggregates failures without masking the transition
  error. Focused tests cover two sessions, every target-owned path and profile
  token, successful rollback with a sync failure, and compensation through the
  original generation. The exact-head host suite passes 57 tests and 366
  assertions; packet v13 covers the remediated boundary and final pins.
- Tmux pane process start times identify the exact eight sessions quiesced by
  the failed live rollback: `2026-06-15-vpsadmin-events`,
  `2026-08-12-dns-secondary-zone-transfer-failure`,
  `2026-08-18-vpsadmin-password-reset`, `2026-08-22-osctld-boot-failures`,
  `2026-09-01-vpsadmin-rbac`, `2026-09-09-ip-accounting-review`,
  `2026-09-09-ip-release-mechanism` and
  `2026-09-09-workspace-components`. Only these exact sessions will be synced
  after corrected activation; older intentionally idle shell panes are not in
  scope.
- Mandatory review v13 Architecture and Risk were clean. General found that
  unregister, suspend and partial-quiesce rescue paths could still replace a
  primary error when aggregate client restoration also failed. All three now
  use one primary-first restoration boundary, with an exact combined-error
  regression. The final host suite passes 58 tests and 368 assertions; packet
  v14 covers the closure and regenerated pins.
- Mandatory review v14 General, Architecture and Scope were clean. Risk found
  that an early unregister compensation failure could still abort later safe
  recovery. Unregister now attempts each eligible registry, runtime, service,
  router and terminal recovery stage independently and reports the primary
  error before labeled recovery failures. Its path regression injects primary,
  service-recovery and terminal-recovery failures; the exact-head host suite
  passes 58 tests and 375 assertions. Packet v15 covers this closure.
- Mandatory review v15 found two related Important gaps in the unregister
  transaction boundary. A registry replacement could persist before its method
  returned, leaving the cached success flag stale, and dependent recovery could
  run after registry or runtime restoration failed. Irreversible runtime
  disposal and success output were also still inside the compensation rescue.
- Unregister now reconciles registration from a fresh on-disk registry,
  restores registry and runtime independently, and enables services or restores
  clients only when both prerequisites are ready. Router recovery follows an
  actual registration restoration. The reversible block ends before retired
  runtime disposal and success output. Regressions model stale cached registry
  state after replacement, failed late recovery prerequisites, and broken
  stdout after commit. The exact-head host suite passes 61 tests and 400
  assertions; packet v16 covers this closure.
- Pushed the remediated exact dependency chain:
  `vpsfree-cz-workspace@ad19e8a -> dev-workspace@0f9d96b ->
  codex-web@e8655b7`. Configuration `a804fda7` pins
  `dev-workspace@0f9d96b` with NAR
  `sha256-rFEYhvJIVvAbNGJW677/SIlzNfHAgXS1v2wXQaUOyH8=`. The configuration
  input was changed only through `confctl`; its Nixfmt and commit hooks passed.
- Rebased the workspace feature onto current shared `master` at `ecbfb9a` and
  republished it with lease protection before v16 review. The three workspace
  feature commits are now `a573dff`, `59b9948` and `c4db2ca`; their trees are
  unchanged from the pre-rebase commits.
- Mandatory review v16 General, Architecture and Scope were clean. Risk found
  one Important isolation gap: a foreign entry that acquired the same workspace
  name correctly blocked service and client recovery, but old retired runtime
  could still move back under that name. Registration recovery now returns an
  explicit `original`, `restored`, `absent`, `foreign` or `unknown` state.
  Runtime restoration remains independent only for states proven safe; foreign
  and unreadable ownership retain the old runtime in quarantine. A regression
  installs a replacement between unregister and compensation, preserves that
  exact entry and proves the original authority remains retired. The exact-head
  host suite passes 62 tests and 409 assertions.
- Folded the v16 remediation into the owning host commit and republished the
  exact dependency chain with lease protection:
  `vpsfree-cz-workspace@c4db2ca -> dev-workspace@0694767 ->
  codex-web@e8655b7`. Configuration `46f7dd90` pins
  `dev-workspace@0694767` with NAR
  `sha256-4OkE53/5mKdnZP4Q+cFrbaoyeWXoHiR2P5amIM7lulo=`. The superseded
  configuration input commit was removed before `confctl` generated the exact
  final replacement; its hooks passed.
- Mandatory review v17 General and Risk found that a failed recovery register
  was still classified as absent without rereading after its own atomic
  replacement. Risk and Architecture also found that a genuinely absent
  registration must not reclaim the public name-scoped runtime because a later
  replacement could adopt it. The other reviewed boundaries were clean.
- After a failed recovery write, registration is now reopened again and
  classified as absent, foreign, unverified exact content or unreadable.
  Only a pre-existing exact entry or a fully returned registration write can
  reclaim runtime. Absent, foreign, unverified and unknown states retain the
  retired directory. Regressions prove both a true absent failure and a
  post-replacement recovery failure leave the authority quarantined. The
  true-absent path then registers a replacement and proves that the hidden old
  runtime is not adopted. The exact-head host suite passes 63 tests and 423
  assertions.
- Folded the v17 remediation into the owning host commit and republished:
  `vpsfree-cz-workspace@9ddf62f -> dev-workspace@b3040c5 ->
  codex-web@e8655b7`. Configuration `5f0415b2` pins
  `dev-workspace@b3040c5` with NAR
  `sha256-LRk4Ui9i5/U7dw9QHjxaVTLXVkM1vjst+RAeZ2QJIEQ=`. The workspace pin
  was amended, while the prior generated configuration pin was removed before
  `confctl` created the single exact final replacement; all hooks passed.
- Mandatory review v18 is clean in all four required lanes, with no Blocking,
  Important or Advisory findings. Long provider validation then passed both
  package variants, including 285 lifecycle tests and 2,721 assertions, the
  45-test cluster suite and the packaged 63-test host suite. The workspace
  wrapper flake and package also built successfully.
- Built aitherdev generation `2026-09-10--11-26-21`, dry-activated it and
  switched it live. Systemd and firewall health checks passed and no kernel was
  built. Switched the user profile to generation 16, restored the exact eight
  previously quiesced clients, and verified all services, sockets, local APIs,
  retained thread identity and authenticated TLS.
- The corrected live rollback from generation 16 to retained generation 15
  succeeded and restored all eight clients with their target generation. The
  portal remained healthy with the exact retained thread. A second forward
  switch to generation 16 succeeded. A temporary empty workspace used generic
  labels, exposed no provider arguments, passed service/API checks and
  unregistered cleanly; its empty temporary root was removed.
- Final host-state comparison found that the password and CA remained exact,
  but substrate reconciliation changed the derived bcrypt entry and renewed
  the TLS leaf on each activation. The old configuration already regenerated
  bcrypt unconditionally, but retaining a valid entry is more stable. The leaf
  renewal was a new locale-order bug: shell `sort` placed the wildcard SAN
  after letters while the Nix expected set used byte order. Directly rerunning
  reconciliation reproduced another unnecessary leaf generation.
- Added idempotent bcrypt verification with password on standard input and
  byte-stable `LC_ALL=C` SAN sorting. The focused host-module build and
  ShellCheck pass. The original TLS pair is still retained on disk and will be
  restored after deploying the fix, then checked through repeated
  reconciliation. The original bcrypt bytes are not recoverable, but the
  persistent password is unchanged and authenticated TLS proves the credential
  meaning is preserved.
- Pushed the post-deployment exact dependency chain:
  `vpsfree-cz-workspace@8865955 -> dev-workspace@a005e31 ->
  codex-web@e8655b7`. Configuration `2f59e38e` pins
  `dev-workspace@a005e31` with NAR
  `sha256-Cr1Io+M1kesHNCYhNNsi5NaWAQXeaUy86XpzGRFpjAs=`. Its input was
  generated only by `confctl`; all hooks passed.
- Mandatory review v19 General found that the double-quoted bcrypt ERE lost
  its literal-dollar escaping, so a valid entry would still be regenerated.
  Architecture and Risk also required an executable provider-owned regression
  for the persistent reconciliation contract. Scope had not started before the
  remediation superseded packet v19. Replaced the ERE with one single-quoted
  variable and added a NixOS VM
  test covering stable password, bcrypt, CA, leaf and symlink state under a
  non-C locale plus malformed, mispermissioned, misowned and nonmatching auth
  recovery. The fast host-module build and full no-build flake evaluation pass.
- Folded the v19 remediation into the owning host commit and republished the
  exact chain: `vpsfree-cz-workspace@255b43d -> dev-workspace@4cb5f58 ->
  codex-web@e8655b7`. Configuration `770ff95f` pins
  `dev-workspace@4cb5f58` with NAR
  `sha256-jSES0Giv4MfbGHmREJZebdkqpELYkp+tGNktdeMK/LA=`. The configuration
  pin was generated only by `confctl`, and its hooks passed. The workspace
  feature was rebased onto current shared `master@26606cf` before review.
- GitHub Actions run `34463804815` for the packet-v20 dev-workspace head failed
  during NixOS VM activation. Its logs showed that the reconcile service ran
  during boot before `/run/lock` existed, so opening the configured lock file
  failed and the dependent nginx service never started. The failure was
  deterministic and directly exercised the new boot-level coverage; packet
  v20 was superseded before reviewer conclusions.
- The host module now creates the configured lock-file parent directory with
  root ownership and mode 0755 before acquiring the lock. A subsequent VM run
  exposed the remaining bcrypt churn: Apache `htpasswd -niBC 12` writes one
  credential line followed by an empty output terminator, while the validator
  required exactly one newline. The validator now accepts one credential plus
  at most that one empty terminator while rejecting a second entry, extra blank
  lines, an unexpected user, malformed bcrypt or a password mismatch.
- The focused NixOS VM test passed in 62.49 seconds. It booted the real module
  under `en_US.UTF-8`, proved two reconciliations preserve all tracked state,
  and proved malformed, mispermissioned, misowned and password-mismatching
  authentication files are replaced once and then remain stable. The test used
  cached NixOS VM kernel and initrd outputs; no kernel was built locally.
- At final `dev-workspace@efff4d2`, Nixfmt, `git diff --check`,
  `nix flake check --no-build --show-trace`, the generated-script host check
  and the focused NixOS VM test all pass. The final exact pushed dependency
  chain is `vpsfree-cz-workspace@6acc69d -> dev-workspace@efff4d2 ->
  codex-web@e8655b7`. Configuration `ab29e61a` pins
  `dev-workspace@efff4d2` with NAR
  `sha256-QGt0G8MrU8ZnNt/+mfNVF02pG8W8yDi5fcWmGUv2WVc=`. The configuration
  pin was generated only by `confctl`, all hooks passed, and every worktree is
  clean and equal to its pushed feature ref.
- Mandatory review v21 ran General, Architecture, Scope and Risk lanes with
  `gpt-5.6-sol` at `xhigh`. General found two Blocking history issues: the
  final reconciler remained in a fixup commit, and both consumers retained
  repeated updates of one input. It also found an Important binary-validation
  gap and an Advisory commit-message width issue. Architecture found two
  Important issues: generated htpasswd output bypassed the full validator, and
  unrestricted managed paths could alias destructively. Risk independently
  reported the lock-path boundary as Advisory. Scope found one Advisory
  Apache-only self-test that duplicated the real VM coverage.
- One `auth_file_valid` function now validates existing and newly generated
  files before publication. It rejects NUL bytes, requires the complete file
  to equal exactly one credential plus one or two terminating newlines, checks
  the configured username, bcrypt cost and alphabet, ownership, permissions
  and the persistent password. VM cases cover trailing and embedded NULs, a
  second credential and excess terminators in addition to the earlier recovery
  cases. The duplicate Apache-only test and its repeated regex were removed.
- One pure Nix path validator now owns the reusable module's managed-path
  contract. All paths must be normalized and absolute, their owning
  directories must be distinct and non-nested, and the lock must be directly
  below root-controlled `/run/lock`. Reconciliation atomically creates a
  root-owned mode-0600 regular lock, rejects unsafe pre-existing state, opens
  it without truncation and verifies the opened inode before flocking. Focused
  evaluation covers relative, colliding, nested and out-of-root lock paths.
- The first remediated generated script failed ShellCheck SC2094 for a
  read-only same-path comparison pipeline, so the binary comparison now uses a
  protected temporary file. The first remediated VM then failed during boot
  because Nixpkgs provides `cmp` in `diffutils`, not `coreutils`; adding the
  owning runtime input fixed the actual activation path. Both non-obvious
  failures have dedicated durable notes.
- The final remediated NixOS VM passed in 99.08 seconds. It booted the real
  module under `en_US.UTF-8`, verified the protected lock, all textual and
  binary auth recovery cases, and preserved password, bcrypt, CA, public CA,
  TLS leaf and `current` target across reconciliation. The cached VM kernel and
  initrd were used; no kernel was built locally.
- Rewrote only unmerged feature history. The final host implementation and VM
  now live directly in `dev-workspace` commit `964dbdd`; the separate fixup is
  gone. Workspace and configuration each contain only one input update, and
  all non-generated commit-message lines are at most 80 columns. The final
  exact pushed chain is `vpsfree-cz-workspace@9a10a22 ->
  dev-workspace@6890ab6 -> codex-web@e8655b7`. Configuration `a564d1cf` pins
  `dev-workspace@6890ab6` with NAR
  `sha256-gY4J+J75UxCf0VkpTs+Pgyym9sXQAYKN5jBpHUH+1Ko=`. The configuration
  revision was generated only through `confctl` before being consolidated into
  its original input commit. Every worktree is clean and equals its pushed
  feature ref.
- At the rewritten exact heads, dev-workspace Nixfmt, `git diff --check`, the
  focused host check, full no-build flake evaluation and cached VM result pass.
  Workspace and configuration no-build flake evaluations pass. Exact-head
  dev-workspace GitHub Actions run `34469910621` is in progress.
- Mandatory review v22 found three related state-boundary gaps. General and
  Risk found that a retained TLS pair was trusted without enforcing its file
  types, ownership and modes. Architecture and Scope found that lexically
  disjoint configurable directories could still resolve through symlinks or
  bind mounts to the same storage. Architecture also found that the password
  check accepted extra bytes around an otherwise valid 64-hex first line.
  General and Scope requested focused lock and malformed-state coverage; Scope
  also classified the unrestricted persistent-path contract as Blocking
  because the implementation could not safely validate arbitrary roots.
- The reusable public path contract now requires persistent state below
  root-controlled `/var/lib`, the router below `/run` and the lock directly
  below `/run/lock`. Reconciliation rejects a symlink in any managed directory
  component, non-root ownership, group/world writable directory components,
  physical directory aliases and unsafe final metadata. The README documents
  this boundary.
- Password validation now reconstructs and byte-compares exactly one lowercase
  64-hex value plus one newline, and dangling password or authority symlinks
  fail closed. TLS retention accepts only a direct `pairs/<name>` target and
  validates the pair directory, certificate and key types, exact ownership and
  modes, expiry, CA signature, exact SAN set and matching public key. Generated
  pairs pass the same validator before atomic publication.
- Expanded provider-owned VM coverage rejects unsafe lock type, ownership and
  mode without truncating it; symlinked and physically aliased state
  directories; leading, excess, embedded-NUL and unterminated password forms;
  and malformed, missing, mismatched, misowned, mispermissioned or symlinked
  TLS state. Every invalid TLS case renews once and the next reconciliation is
  stable; generated leaves prove the exact SAN set and key match.
- The first remediated fast host check found a ShellCheck expansion of an
  undefined generated-script variable; using the candidate's own directory
  fixed it. The exact final host check passes. The exact final focused VM then
  passed in 285.65 seconds under `en_US.UTF-8`; its NixOS kernel and initrd were
  fetched from cache and no kernel was built locally.
- Folded the complete remediation into the original host-module and
  documentation commits, then regenerated both downstream pins. The exact
  pushed chain is now `vpsfree-cz-workspace@010e3dd ->
  dev-workspace@f9ef74b -> codex-web@e8655b7`. Configuration `141daeb8` pins
  `dev-workspace@f9ef74b` with NAR
  `sha256-MBOQ8iqu+ldp5DLsjqaayccRZxDTTm3cER1pYcpNXCY=`. The configuration
  update was generated only through `confctl`; all repository hooks passed.
- A direct configuration push failed because its pre-push hooks could not find
  repository-pinned Ruby dependencies in the ambient shell. Repeating the
  exact lease-protected push through `nix develop` passed; the dedicated
  durable note records the requirement. The shell-generated `.bin` and
  `.bundle` helpers were removed afterward.
- At all four exact pushed heads, `git diff --check` passes and every worktree
  is clean. Dev-workspace, workspace and configuration no-build flake checks
  pass. Exact-head dev-workspace Actions run `34474248837` is in progress.
  Superseded run `34469910621` is also still running because the available
  token lacks Actions write permission and GitHub returned HTTP 403 when its
  cancellation was attempted.
- Mandatory review v23 found two blocking host-state boundaries and related
  important/advisory gaps. The physical-alias check did not cover the complete
  directory inventory or aliases hidden behind absent final paths, and command
  substitution made the selected-pair link parser lossy. Reviewers also
  required canonical single-certificate CA publication, strict server-leaf
  purpose/extensions and explicit distinct/non-nested public wording.
- One managed-directory inventory now covers the router, lock, all persistent
  outputs, internal authority and pair directories, and the selected TLS pair.
  Reconciliation records every existing ancestor identity with its planned
  suffix, rejects unexpected physical relationships even when final paths are
  absent, rejects internal and selected-pair mounts, and repeats the complete
  layout check at every state-transition boundary.
- The `current` target is captured losslessly, must match the exact direct-pair
  grammar and is reread with an inode check after validation. CA and leaf PEMs
  must each be one canonical certificate. Retained leaves additionally require
  exact critical constraints/key usage, server-auth purpose, SANs, signature
  and matching key.
- The first alias implementation launched filesystem commands in nested loops
  and made emulated VM boot reconciliation take about 2 minutes 17 seconds.
  Precomputing ancestor identities and comparing them in shell arrays reduced
  that activation phase to about 9.25 seconds. The durable dev-workspace note
  records the symptom, cause and correction.
- A first complete VM run reached its final legacy test before exposing a stale
  expectation that a symlinked selected-pair directory would be replaced. The
  stricter contract correctly failed closed; the test now checks rejection,
  unchanged state, explicit restoration and subsequent stability.
- The corrected focused VM passed in 1,055.02 seconds under `en_US.UTF-8`.
  Nixfmt, `git diff --check`, the generated-script host check and full no-build
  evaluation also pass. The tested pre-rewrite tree and rewritten final commit
  have identical tree `6a57521a83135662435b93b55e88b4c039fcccf3`.
- Folded all remediation into the original host and documentation commits and
  regenerated the two downstream exact pins. The pushed chain is now
  `vpsfree-cz-workspace@4fba092 -> dev-workspace@0571f1e ->
  codex-web@e8655b7`. Configuration `c144b41f` pins
  `dev-workspace@0571f1e` with NAR
  `sha256-7XJmatzfRf/mzynHPnEUWrHVjtxy1tJCkQYT1lyipcI=`. The configuration
  update used only `confctl`, all hooks and no-build evaluation passed, and
  generated shell helpers were removed.
- Dev-workspace Actions run `34474248837` for the preceding head completed
  successfully. Current exact-head run `34483741579` is in progress.
- Mandatory review v24 Scope was clean. Architecture and Risk independently
  found a Blocking self-ancestor bind escape because same-inventory ancestor
  identities were not compared. Risk also found an Important pre-validation
  metadata mutation on hard-linked or file-bind-mounted CA files. General
  found a Blocking ordering gap because the selected TLS pair joined the
  managed inventory after auth and CA mutation, plus an Important ambient
  OpenSSL trust-store escape for retained leaves.
- Reconciliation now rejects a repeated device/inode identity within one
  managed path, discovers and inventories a validly named selected pair under
  the protected lock before any credential or CA mutation, and retains the
  later target reread and inode comparison. Existing CA key and certificate
  files must be unmounted single-link regular files with exact numeric
  ownership and modes before validation; reconciliation no longer normalizes
  unsafe existing CA files. Explicit `-no-CApath -no-CAstore` verification
  isolates CA self-checks and retained leaves from ambient trust directories.
- VM regressions bind a parent onto its child with the final output absent,
  exercise both hard-linked and file-bind-mounted CA certificates, combine an
  unsafe selected pair with malformed auth metadata, and offer a conforming
  foreign-signed leaf through a hashed `SSL_CERT_DIR`. Every unsafe path fails
  without changing the recorded unrelated bytes or metadata, while the
  foreign leaf rotates once to the configured local CA.
- The first v24-remediation VM run reached the new foreign trust fixture after
  all other new cases passed, then failed because `openssl rehash` was given a
  directory containing the private key as well as the certificate. Moving the
  key to a sibling path fixed the fixture. The clean full rerun passed in
  1,099.01 seconds; the cached NixOS kernel and initrd were used and no kernel
  was built locally. Dedicated notes record the rehash and formatter setup.
- Folded the remediation into the original host and documentation commits,
  regenerated both downstream pins, and pushed the exact chain
  `vpsfree-cz-workspace@4272943 -> dev-workspace@e4c7507 ->
  codex-web@e8655b7`. Configuration `afc5a3f3` pins
  `dev-workspace@e4c7507` with NAR
  `sha256-iN4P2rZQzoCukmLMTvwigLo74iEZacWyJb9TkLWsCG0=`. Its update used only
  `confctl`; hooks and no-build evaluation passed, and generated helpers were
  removed. All four worktrees are clean and equal their pushed refs.
- Exact-head dev-workspace Actions run `34491981369` is in progress.
  Superseded run `34483741579` remains in progress because its cancellation
  returned HTTP 403; a durable cross-project note records the missing Actions
  write permission.
- Review v28 found one final compatibility export, unsafe migration preflight
  ordering, missing generic/runtime and organization/site contract checks,
  bundled histories and missing nontrivial commit rationale. The final
  workspace now exports only its default and organization package. Generic
  validation reserves `workspace-portal`; site configuration has exact nested
  keys and immutable JSON-object inputs; migration journals and validates all
  rewrites before any keeper or namespace mutation.
- The new migration regressions pass with 13 runs and 123 assertions. Generic
  host tests pass with 71 runs and 446 assertions. Both exact no-build flake
  evaluations pass, as do the final workspace and exact bridge evaluations.
- Rebuilt the generic contract hardening into focused commits and the workspace
  delegation into separate policy, configuration, dependency, source-removal,
  bridge and final commits, all with required rationale. Updated both downstream
  pins and pushed the exact v29 chain
  `workspace@2276ccd -> organization@4dd1e54 -> generic@ddba3ca ->
  codex-web@c3200c4`; configuration `b85582e` pins `ddba3ca` via `confctl`.
- Current exact-head Actions runs are generic `34527817922` and organization
  `34528090696`, both in progress. Organization superseded run `34525161667`
  accepted cancellation; generic superseded run `34524824514` again returned
  HTTP 403.
- Review v29 found an accidental `~/bin/workspace-portal` link, repeated input
  updates, an omitted occupied registry path, and migration rollback/preflight,
  locking, retry and metadata gaps. All Blocking and Important findings are
  remediated in the exact v30 heads.
- Generic activation now separates public home commands from reserved private
  executables. Organization migration tests cover complete move and reverse
  rewrite preflight, required transition-lock ordering, bridge-current and
  compensated rollback, interrupted tmux convergence, invalid registry types,
  supplementary groups and read-only user/host preflights. They pass with 23
  runs and 264 assertions.
- Repeated organization and configuration input updates were consolidated into
  their original dependency commits. The pushed exact chain is
  `workspace@7bd8f5c -> organization@e399c86 -> generic@ee4e282 ->
  codex-web@c3200c4`; configuration `031104a` pins `ee4e282`.
- Exact no-build flake checks pass for generic, organization, workspace and
  configuration, all worktrees are clean, and forbidden-name scans are empty.
  Codex-web Actions `34512598834` is green. Current generic Actions
  `34529633403` and organization Actions `34531031684` are in progress.
  Superseded organization runs accepted cancellation; generic cancellation
  still returns HTTP 403 under the available token.
- Review v30 found stale legacy-link cleanup, stale tmux socket identity,
  incomplete window metadata migration and reverse preflight, mutable rollback
  inventories, duplicated host-path/domain contracts, inaccurate constructor
  documentation and one misleading dependency commit message. The v31 heads
  remediate every Blocking and Important finding.
- Generic `dev-workspace` tests now pass with 73 runs / 454 assertions for the
  host and 285 runs / 2,852 assertions for dev-session. Organization migration
  tests pass with 27 runs / 313 assertions, and its packaged Nix check passes
  all tool suites. The workspace deployment checker passes 2 runs / 9
  assertions and the live cross-worktree contract check. Exact no-build flake
  evaluation passes for all four Nix consumers.
- The pushed v31 chain is
  `workspace@83d14b7 -> organization@5243d50 -> generic@868826d ->
  codex-web@c3200c4`; configuration `55b87fa` pins `868826d` via `confctl`.
  Codex-web Actions `34512598834` is green. Exact-head generic Actions
  `34534735689` and organization Actions `34535187363` are still running.
- Review v31 found missing absence records for managed tmux metadata, one
  bundled generic remediation commit, an incorrect compatibility-bridge SHA,
  incomplete user-state-root propagation, duplicated router defaults, unsafe
  migration socket handling and an oversized-journal write/load mismatch.
  It also identified the organization repository's feature-branch default as
  an administrative follow-up and two history/documentation advisories.
- Generic portal lifecycle receipts, removal records and dev-session recovery
  now share one explicit namespace state root. Package router metadata derives
  from the exported host path contract. Stale-socket cleanup probes the exact
  UNIX endpoint and rechecks its identity, including a live-server regression.
  The remediation was folded or split into the commits owned by each affected
  subsystem instead of remaining as one catch-all follow-up.
- Organization migration schema 4 journals tmux option/environment absences,
  the exact server-socket identity and all serialized journal bytes before any
  write. Forward and reverse preflights reject late metadata, symlinked or
  replaced sockets and aggregate journals above 16 MiB. The exact migration
  suite passes with 31 runs / 358 assertions.
- The final generated configuration pin was consolidated without editing its
  `confctl` message. All exact heads were force-pushed with leases. The pushed
  v32 chain is `workspace@7c1ea44 -> organization@bc33735 -> generic@a6713ba
  -> codex-web@c3200c4`; configuration `ebc3de33` pins `a6713ba`.
- Exact-head quick verification passes: generic workspace-host 74 runs / 457
  assertions, dev-session 285 runs / 2,852 assertions, focused Go packages,
  organization migration and no-build checks, workspace deployment contract
  2 runs / 9 assertions, and workspace/configuration no-build evaluations.
  The live checker confirms domain identity and the exact `a6713ba` pin.
- Exact-head Actions runs are codex-web `34512598834` (green), generic
  `34539084838` (running) and organization `34539152574` (running).
  Superseded organization run `34535187363` accepted cancellation; generic run
  `34534735689` could not be cancelled because the token returned HTTP 403.
- Review v32 found two Blocking history issues: the first organization
  migration commit introduced schema 3 and was followed by repair commits, and
  organization/configuration dependency updates were repeated. The current
  initiative tail is rewritten so its first migration commit contains the
  complete schema-4 design, the organization history has one generic input
  update, and configuration has one unchanged-message `confctl` dependency
  commit. Generic documentation commits were also rewrapped without tree
  changes.
- Review v32 found an Important command-boundary issue. The destructive
  migration helper now exists only at
  `libexec/vpsfree-dev-workspace-migrate`; an explicit eight-command allowlist
  controls public KB extension commands. Package checks prove the helper is
  executable at the private path and absent from `bin`, the catalog and home
  links.
- Review v32 found a Blocking journal-capacity gap. Migration now projects the
  largest reachable forward/reverse/retry journal state and checks both current
  and projected serialization before any write or preflight mutation. The
  migration suite passes 33 runs / 370 assertions, including an exact boundary
  case and a six-file near-limit forward/reverse/retry scenario.
- Scope review noted that the 135 retained predecessor commits contain selected
  path histories that were later deleted. This is accepted intentionally: they
  preserve original source provenance and ancestry before the initiative, have
  no final-tree or runtime effect, and re-filtering them would destroy useful
  commit identity. The current initiative tail, where ownership and deployment
  behavior are introduced, was rewritten into clean functional commits.
- The pushed v33 chain is `workspace@1d8b322 -> organization@f7c300c ->
  generic@086e3d8 -> codex-web@c3200c4`; configuration `f26ea40a` pins
  `086e3d8`. The immutable bridge is workspace commit `a05abc1`.
- Post-remediation quick checks pass: organization migration 33 runs / 370
  assertions, organization package metadata, organization/workspace/configuration
  no-build flake evaluation, workspace deployment contract 2 runs / 9
  assertions and the cross-worktree checker at exact generic revision
  `086e3d8`.
- Current exact-head Actions runs are generic `34542903217` and organization
  `34543301253`, both in progress when last checked. Superseded organization
  run `34539152574` accepted cancellation; superseded generic run `34539084838`
  could not be cancelled because the token returned HTTP 403.
- Review v33 found two invalid generated/history boundaries, one duplicated
  migration-state declaration, an unnecessary public constructor, missing
  two-parent rename durability, incomplete authority validation, unsafe host
  ancestors, incorrect quiescence ordering and stale deployment wording. All
  Blocking and Important findings are remediated in the v34 heads.
- The complete private migration package now exists in its owning migration
  commit. The configuration history declares its channel separately and then
  contains the exact untouched lock-only commit produced by
  `confctl inputs channel set --commit`.
- Migration validation and worst-case journal projection share one exhaustive
  `PERSISTED_STATE_FIELDS` declaration. Forward, reverse and recovery renames
  durably synchronize both parents before journal advance. Authority preflight
  enforces the actual schema, identities, modes and size limit, and the
  organization package asserts generic authority policy version 1.
- The flake exports only `mkPackage`, unsafe host-root ancestors are rejected
  before any mutation, and the runbook quiesces the old runtime before the
  compatibility switch and stops compatibility services again before
  preflight. The focused migration suite passes with 38 runs / 485 assertions.
- Scope's direct-lock traversal advisory is accepted intentionally. Both
  deployment consumers are required to publish direct immutable GitHub refs;
  a `follows` or indirect topology must fail closed until the deployment proof
  is deliberately updated.
- The pushed v34 chain is `workspace@761d940 -> organization@57a491f ->
  generic@086e3d8 -> codex-web@c3200c4`; configuration `580edfc` pins
  `086e3d8`. The immutable bridge is workspace commit `7f4cf74`.
- All five remote feature refs match their clean local heads. Codex-web Actions
  `34512598834` is green; generic `34542903217` and organization `34547074046`
  are running. Superseded organization run `34543301253` accepted
  cancellation.
- Review v34 found a Blocking authority-policy gap and one tracking Important:
  JSON coercions differed from the destination runtime, ready authorities were
  not correlated with their live tmux identity, the allowed path spelling was
  narrower than the generic slug contract, and the durable plan retained the
  old unsafe bridge order. Scope also advised consolidating three overlapping
  internal site validators.
- Migration now consumes the generic shared authority corpus, requires exact
  JSON types and the complete supported slug domain, and binds every authority
  to one frozen live tmux session before journaling or keeper handoff. The live
  test uses consistent session/Codex metadata; mismatch regressions cover the
  socket, stable ID, name, workspace, tmux identity and Codex triple. The suite
  passes with 41 runs / 678 assertions.
- Site validation now has one authoritative public boundary, while the private
  tools derivation retains only the independent authority-policy assertion.
  The plan and runbook now specify the same build, quiesce, compatibility
  switch, second service stop, preflight, migration, host activation and final
  profile ordering.
- The pushed v35 chain is `workspace@204d78a -> organization@c93ae3f ->
  generic@086e3d8 -> codex-web@c3200c4`; configuration remains `580edfc` at
  generic `086e3d8`. The immutable bridge is workspace commit `4c7a5ab`.
- Organization and workspace no-build flake evaluations, the 2-run/9-assertion
  deployment checker and the live cross-worktree contract pass at the v35
  heads. New organization Actions run `34549692881` is active; superseded run
  `34547074046` accepted cancellation.

## Compatibility decisions

- Intentionally replace the old environment, tmux and state-path namespaces
  in one coordinated cutover. No mixed-version alias remains after migration.
- Preserve manifest meaning, journals, operation receipts, submission ledgers,
  registry entries and working directories while rewriting machine-consumed
  runtime paths and metadata names. Stop and replace all tmux processes.
  Preserve a thread ID when it remains available; explicitly replace only a
  missing ID before the migration inventory is journaled.
- Pin Numtide `llm-agents.nix` revision
  `c2a308c84bbfa9f30827344219b7284f8104bdd8` and Codex 0.153.4 for the first
  cutover. Do not override Numtide's package or nixpkgs.
- Keep aitherdev's existing credentials, local CA and TLS material during the
  NixOS module migration.
- Keep shared bridge, DHCP and NAT configuration in
  `vpsfree-cz-configuration`; the reusable module accepts existing bridges.
- Default-branch integration and aitherdev deployment were authorized and are
  complete. Releases, archival and deletion remain unauthorized.

## Review and testing

- Risk classification: high, because the change affects authentication,
  persisted runtime state, public interfaces, destructive lifecycle helpers,
  host deployment, rollback and mixed package generations.
- Reviews v4 through v26 cover the preceding implementation. Review v27 found
  final-package activation alias leakage, catalog/default immutability gaps,
  remaining inline host-test logic, superseded unmerged history, archived
  revive incompatibility and the registered-root policy deployment gate. The
  code/history findings are remediated in the exact heads above. Review v28
  then found a final-head bridge export, a missing core-command collision,
  incomplete site-configuration validation, unsafe migration preflight order,
  bundled commit boundaries and missing commit rationale. All are remediated
  in the v29 heads and focused tests.
- Review v36 found unsafe global string substitution in structured state,
  lossy tmux value handling, missing exact tuple arity, overbroad/retry-unsafe
  parent cleanup, duplicated tmux metadata ownership, incomplete inverse-corpus
  and filename coverage, repair history and stale tracking. All findings are
  remediated in the v37 heads and packet.
- Review v37 found a known-unbuildable generic pin hidden in a later
  organization commit, stale schema wording, retained inline/extracted test
  churn, an incorrect tmux window-path classification, one unisolated deletion
  test and a runtime error-path `NoMethodError`. Every finding is folded into
  its owning commit in the v38 heads. The previously created test-recovery tree
  was inventoried and will be preserved under a separate backup name during
  deployment rather than deleted.
- Review v38 found one bundled generic history commit, two stale history/test
  artifacts, a wrong bridge SHA, incomplete preservation and registered-root
  deployment instructions, and non-exact authority-format validation. All
  findings are remediated in the v39 heads. The Risk lane did not start before
  remediation because only three reviewer slots were available, so v39 runs
  all four required lanes from fresh context.
- Review v39 found an unsafe sibling-prefix path rewrite, a duplicated
  workspace-configuration authority, stale commit wording, incomplete
  occupied-target evidence and operator commands, open user/root writer races,
  and a missing whole-host migration/reconciliation fixture. The v40 heads fix
  all code, history, documentation and test findings. The repository default
  remains the dated organization branch only because the administrative GitHub
  update returned HTTP 403; accepting that external metadata temporarily is an
  explicit decision and an administrator follow-up.
- Review v41 found executable-cutover, fail-closed admission, reverse
  activation, missing-thread and interrupted-recreation findings. The user then
  simplified the deployment contract: processes and tmux state may be discarded,
  the currently materialized active conversations use the normal restart path,
  and the archived authority remains stopped. The v43 heads and packet reflect
  that final scope.
- Final review packet retained for history:
  `work/2026-09-09-workspace-components/review-packet-v44.md`. The user ended
  further review cycles before deployment.
- The user authorized Codex-session restarts, cluster resets and fast-forward
  workspace integration. The journaled forward cutover and live acceptance are
  complete.

## External follow-up

- An organization owner may change the GitHub default-branch setting of
  `vpsfreecz/dev-workspace` from the dated feature branch to `master`; both
  names already resolve to the same integrated commit. The available token
  returned HTTP 403, and this repository-metadata preference does not affect
  the merged code or deployed runtime.

## Cleanup

- The completed one-time aitherdev cutover script, runbook and contract test
  were removed from workspace `master` in `b5aae3d` after live acceptance.
- The clean detached compatibility worktree, generated configuration caches,
  preserved test-recovery tree, and accepted user/host migration journals were
  removed after successful deployment. All feature branches are retained.
- The user explicitly requested cleanup and then directed archival to proceed
  without waiting for duplicate exact-head master workflows.
- Stable portal URL:
  https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-09-workspace-components/
