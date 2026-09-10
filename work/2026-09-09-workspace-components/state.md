---
lifecycle: active
---

# 2026-09-09-workspace-components

## Repositories

- Coordination checkout: `/home/aither/workspace/ai/vpsfree.cz`, branch
  `master`.
- Workspace source baseline:
  `3580e60bb035c2d0ba5be6f0d2489bbbf30ded3d`.
- Configuration source baseline:
  `7481618dacab04bfd5b09bc730c373c2d2bf14d7` from remote `master`.
- Initial tracking commit:
  `58ccb4da27d6e1ef26c330662b2471d559d2c437`.
- `dev-workspace`: branch `2026-09-09-workspace-components`, worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/dev-workspace`,
  base `f39f8e62097b5e9da9de8a5eb678131b1e478e35`, remote
  `git@github.com:aither64/dev-workspace.git`, head
  `e4c75076573ed2e986298626a80309a93e07d93a`.
- `codex-web`: branch `2026-09-09-workspace-components`, worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/codex-web`,
  base `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8`, remote
  `git@github.com:aither64/codex-web.git`, head
  `e8655b7b2689da9b1aabe10df69858c32725dd61`.
- `vpsfree-cz-configuration`: branch
  `2026-09-09-workspace-components`, worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/vpsfree-cz-configuration`,
  base `7481618dacab04bfd5b09bc730c373c2d2bf14d7`, head
  `afc5a3f30aee330ddcceafbd8fe9a4b7236a4d3f`.
- `vpsfree-cz-workspace`: branch `2026-09-09-workspace-components`, worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/workspace`,
  review base `26606cfa0134ce3680cf592f9ab3c345683fbdc2`, head
  `42729432a8723648112cdd176497569d86bc23c2`.
- `vpsfreecz/dev-workspace`: branch `2026-09-09-workspace-components`,
  worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-workspace-components/vpsfree-dev-workspace`,
  neutral base `9b8d07e12c1115aef1c09cfafbc71ba10e167853`, filtered-history head
  `62ea5a17be81636e2e1e4c97742cc99800087a2c`, remote
  `git@github.com:vpsfreecz/dev-workspace.git`, and local project name
  `vpsfree-dev-workspace`.

## Status

- The user replaced the compatibility-output design with a strict four-layer
  split. Generic `codex-web` and `dev-workspace` must have zero current-tree
  references to vpsFree or aitherdev. Organization tools move to the new
  `vpsfreecz/dev-workspace`, while personal host/domain configuration remains
  in `vpsfree-cz-workspace` and the privileged configuration repository.
- The user selected a one-time namespace and path migration with no legacy
  runtime aliases. Published history remains intact. The new organization
  repository will preserve filtered source history and must itself contain no
  aitherdev references.
- Both generic repositories already contain GitHub Actions workflows running
  the complete flake check. The new organization repository needs the same
  coverage.
- Constructed the new organization repository locally with a neutral default
  branch and 134 relevant commits filtered from `dev-workspace`, then replayed
  that history on the dated feature branch. No remote refs have been written
  yet.
- The user accepted the three-component split and requested implementation.
- Seeded both public repositories from path-filtered workspace history. Their
  default branch is `master`; both use the MIT license and have passing Nix
  bootstrap checks.
- `dev-workspace` now ships the core tooling and a separate vpsFree
  compatibility output containing KB commands and packaged workspace skills.
- `codex-web` now provides the public Go App Server client, secured conversation
  handler, framework-free ES module and a loopback example. It does not run as
  a separate service.
- The NixOS host module provides generated basic authentication, local-CA TLS,
  nginx and a closed firewall unless source ranges are configured.
- The workspace feature is a thin consumer that retains coordination records
  and policy while re-exporting the pinned `dev-workspace-vpsfree` package.
- The aitherdev feature configuration consumes the reusable host module and
  preserves the existing identities, state paths, socket, hosts and source
  network rule.
- This standalone Codex CLI owns implementation. It is intentionally not a
  managed development session and does not use the retained portal thread.
- Created canonical bare clones and all four dated feature worktrees. The four
  exact heads above are committed, pushed and clean. The reusable NixOS
  substrate and user-profile generation 16 are deployed on aitherdev; the
  final idempotency remediation is committed and pending review and deployment.

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

## Compatibility decisions

- Intentionally replace the old environment, tmux and state-path namespaces
  in one coordinated cutover. No mixed-version alias remains after migration.
- Preserve manifest meaning, journals, operation receipts, submission ledgers,
  registry entries, thread IDs, working directories and tmux identities while
  rewriting their machine-consumed runtime paths and metadata names.
- Pin Numtide `llm-agents.nix` revision
  `c2a308c84bbfa9f30827344219b7284f8104bdd8` and Codex 0.153.4 for the first
  cutover. Do not override Numtide's package or nixpkgs.
- Keep aitherdev's existing credentials, local CA and TLS material during the
  NixOS module migration.
- Keep shared bridge, DHCP and NAT configuration in
  `vpsfree-cz-configuration`; the reusable module accepts existing bridges.
- Default-branch integration, releases, archival, deletion and session stop
  are not authorized. aitherdev deployment is authorized.

## Review and testing

- Risk classification: high, because the change affects authentication,
  persisted runtime state, public interfaces, destructive lifecycle helpers,
  host deployment, rollback and mixed package generations.
- Mandatory review v11 used General, Architecture, Scope and Risk lanes with
  `gpt-5.6-sol` at `xhigh`; all four lanes completed cleanly. Live rollback
  testing then found the target-generation restoration defect. All findings
  through v24 are remediated; affected lanes will review packet v25 before
  corrected live deployment.
- Current review packet:
  `work/2026-09-09-workspace-components/review-packet-v25.md`.
- Final idempotency deployment, restored-leaf verification and current-head CI
  remain pending.

## Open work

1. Create the filtered `vpsfree-dev-workspace` history, bare clone and feature
   worktree, then register it in `portal.yml` and this state file.
2. Implement generic namespace and extension contracts, move organization
   tooling/configuration, extract the inline Nix tests and update exact pins.
3. Run quick checks, mandatory review and all affected review reruns.
4. Run full component and migration integration tests, then perform the
   journaled aitherdev namespace/state cutover and final service checks.
5. Monitor exact-head GitHub Actions and investigate every failure.

## Cleanup

- Session remains active. No lifecycle action or delayed cleanup is authorized.
- Stable portal URL:
  https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-09-workspace-components/
