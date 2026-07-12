# 2026-07-10-kb-czech-fixes

## Repositories

- Coordination workspace:
  `/home/aither/workspace/ai/vpsfree.cz`
  - Shared branch: `master`
  - Initiative: `2026-07-10-kb-czech-fixes`
- `vpsadmin`:
  `/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin.git`
  - Authority ref: `origin/master`
  - Authority commit:
    `7e0be5d215ce554009ff92381bdb54557e618776`
  - Feature branch: `2026-07-10-kb-czech-fixes`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-07-10-kb-czech-fixes/vpsadmin`
- `vpsfree-sms-gateway` (historical read-only input from the first cluster
  attempt; no longer used by the capture repository):
  `/home/aither/workspace/ai/vpsfree.cz/repos/vpsfree-sms-gateway.git`
  - Authority ref: `origin/2026-06-15-vpsadmin-events`
  - Authority commit:
    `af7b3faf`
  - Feature branch: `2026-07-10-kb-czech-fixes`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-07-10-kb-czech-fixes/vpsfree-sms-gateway`
- `vpsadmin-kb-captures`:
  `/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin-kb-captures.git`
  - Feature branch: `2026-07-10-kb-czech-fixes`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-07-10-kb-czech-fixes/vpsadmin-kb-captures`
  - Commits:
    - `838b3ef` (`captures: add standalone reproducible screenshot framework`)
    - `af5525e` (`captures: add Czech vpsAdmin screenshot inventory`)
    - `e0a3502` (`captures: put screenshot language first`)
    - `0cfad06` (`captures: share the root-password form`)
    - `e76a040` (`flake: update vpsAdmin 299147166 -> 7e0be5d21`)
    - `7157a51` (`captures: preserve complete content bounds`)
    - `3ff72c9` (`captures: provide deterministic terminal fonts`)
    - `ad41b29` (`fixtures: accept a pending NAS creation`)
    - `799b385` (`captures: refresh Czech screenshot set`)
  - SSH remote:
    `git@github.com:vpsfreecz/vpsadmin-kb-captures.git`
  - GitHub repository created by the user:
    `https://github.com/vpsfreecz/vpsadmin-kb-captures`
- `haveapi` (read-only background):
  `/home/aither/workspace/ai/vpsfree.cz/repos/haveapi.git`
  - Inspected current `origin/master`:
    `350547447ba42dfa765e09c762dd916ad0acce03`
- `vpsfree-cz-configuration`:
  `/home/aither/workspace/ai/vpsfree.cz/repos/vpsfree-cz-configuration.git`
  - Feature branch: `2026-07-10-kb-czech-fixes`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-07-10-kb-czech-fixes/vpsfree-cz-configuration`
  - Base: `origin/master` at
    `435f63d77be0aa20ab48cec334340e9fc94ac163`
  - Commits after rebasing onto current `origin/master`:
    - `594f4c55` (`cluster: add on-demand KB staging instances`)
    - `4392ef47` (`cluster: delegate KB staging container lifecycle`)

## Status

- Implementing the user-review follow-up on top of capture commit `e0a3502`.
  The declarative screenshot topology now uses `node1`, `node2`, and
  `backuper1` and seeds the supplied four environments, five locations, seven
  resources, complete package catalog, and per-environment defaults using
  local IDs and `example.test` domains.
- Fixture preparation now creates `vps` in Production/Praha,
  `playground-vps` in Playground/Playground, a `data` child dataset mounted at
  `/srv/data`, and a `nas` dataset on the primary pool. Export screenshots use
  NAS while restore screenshots continue to use the labeled snapshot.
- Added shared content-aware screenshot bounds, protected form input rows from
  status-value normalization, replaced the TOTP secret/QR before capture,
  replayed the live monitor's real ANSI transcript in xterm.js, expanded the
  WebUI console capture, and renamed the rescue checkpoint to
  `rescue-mode/vps-console-boot`.
- Added deterministic staging language-link warming and verification. A live
  quick check warmed English first and then Czech and verified both links for
  all 27 paired candidate pages; the three candidates without `<page>` remain
  intentionally unpaired.
- Quick checks pass: Ruby syntax and 13 staging/release tests (45 assertions),
  Nix parse, JSON parse, JavaScript syntax in the pinned shell, shellcheck, and
  inventory validation with the one intentionally not-yet-generated renamed
  rescue screenshot allowed missing. Nix evaluation reached the cluster
  derivation graph; an accidental build attempt was stopped and also exposed
  the expected absence of generated dev-cluster certificates before
  `bin/devcluster start`.
- Functional tooling changes are committed. The full screenshot topology and
  all 60 Czech assets remain behind the mandatory follow-up review gate.
- Mandatory review of workspace `2899390` and the original broad capture
  commit `6c8a830` found two blockers and two important issues. Before
  integration, the capture history was split into production-shaped fixtures,
  shared rendering mechanics, and scenario corrections; Playground creation
  and cloning now select Playground explicitly; object-resource `free_chain`
  uses the pinned model contract; and staging accepts an identical candidate
  page on retry after a transient language-render failure. A regression test
  covers that retry path. The reviewer also noted that the old orphan rescue
  PNG must be removed when the renamed artifact is generated.
- A fresh follow-up review found that README changes belonged in the first two
  capture commits, dataset discovery still accepted guessed or ambiguous
  matches, and the raw monitor stream retained changing numeric cells and the
  `script` termination epilogue. The rewritten capture series now documents
  topology/fixtures in its owning commit and crop mechanics in the next;
  dataset and mount discovery fail on missing or ambiguous fixture state; and
  the validated ANSI stream receives deterministic fixed-width cell overlays
  after its wrapper epilogue is removed. The target VPS row is derived from the
  captured cursor position instead of hard-coded.
- The final review found that the two timestamp overlays used the TUI's
  single-character refresh columns instead of the timestamp starts. They now
  begin at columns 26 and 51. `tools/check-terminal.cjs`, run by `bin/check`,
  decodes a representative ANSI screen and asserts the complete canonical
  header rather than merely looking for escape-sequence fragments.
- The final reviewer verified capture head `008acd3` and cleared the blocker.
  It confirmed the exact decoded header, epilogue removal, pinned-shell check,
  focused commit series, and coordination record, with no remaining findings.
  Long three-machine integration may proceed.
- The first bridge-mode start correctly refused because another active
  initiative (`2026-07-02-haveapi-i18n`) owns the shared service address
  `172.16.106.53`. Its runner and VMs are live, so they were not stopped or
  reused. Bridge networking is genuinely unavailable; this capture run uses
  the repository's isolated `--network local` mode as the documented fallback.
- The first local launch built the full topology and started all four VMs, but
  the three vpsAdminOS guests remained immediately after ROM because
  `/dev/shm` reached 100%. The unrelated integration test and long-lived bridge
  cluster already consumed 35 GiB of the 48 GiB tmpfs; our original 8/8/4 GiB
  node backends could not coexist. Only this partial cluster was stopped. VM
  runtime capacity is now services 4 GiB, node1 4 GiB, node2 4 GiB, and
  backuper1 2 GiB, driven directly by declarative config. These sizes still
  satisfy the two 4 GiB fixture VPSes and are independent of the public
  resource/package values displayed by the WebUI.
- The next local launch booted and seeded all four VMs, then exposed a runtime
  identity mismatch: the seed reassigned nodes to production-shaped fixture
  locations, while RabbitMQ and nodectld still used the original `.lab`
  domain. Capture commit `70285e0` now derives each node identity and nodectld
  location domain from the same safe `example.test` location fixture. A fresh
  mandatory standalone review returned no blocking, important, or advisory
  findings. The remaining integration check is to confirm the rendered node
  names, RabbitMQ accounts, and running nodectld daemons.
- That clean launch confirmed node1's corrected API/RabbitMQ/nodectld identity
  and a running nodectld, then exposed an osctld readiness race: the pool was
  visible before `/default` existed, so the first device grant failed with
  `group not found`. Capture commit `adf33bd` makes the existing readiness loop
  require both the pool and `/default`, and retains a fail-closed timeout. Its
  Nix-shell Bash, ShellCheck, diff, and Nix-parse checks pass. The mandatory
  standalone review returned no findings and confirmed the probe uses the
  pinned osctld pool-scoped group lookup; live refresh and repeated-refresh
  checks may proceed.
- Both live refreshes then passed, including repeated device grants. The first
  full capture attempt stopped before writing new images because the admin VPS
  wizard was entered without its required numeric target user; the final URL
  contained `user=` and the database remained free of VPS records. The first
  review caught that the members page needed `action=list` and that lookup had
  to match the designated login column. Amended capture commit `4f761e9`
  requests an exact login-filtered list, resolves one numeric user ID, and
  carries it through both fixture VPS wizards. Node syntax and allow-missing
  inventory checks pass; follow-up review returned no remaining findings.
- The next diagnostic capture reached `user=2` and preserved the rendered API
  error: no free node was available because Production requests a 120 GiB
  disk while each generated ZFS tank had only 20 GiB; the 250 GiB NAS package
  would fail the same check. Fixture commit `2597243` retains full rendered
  error text. Cluster commit `78f61f4` makes tank size configurable and gives
  node1, node2, and backuper1 sparse 320 GiB images, leaving public package
  values unchanged. Quick Nix-shell checks pass. Fresh review returned no
  findings and confirmed `truncate`-backed sparse allocation plus sufficient
  margin below vpsAdmin's projected pool-fill limit. The old 20 GiB runtime
  state must now be reset because existing tank images are not resized.
- The 320 GiB cluster then passed node capacity selection, and the preserved
  error advanced to `no ipv6 address available`: production-shaped defaults
  request one IPv6 object, while the standalone seed only had IPv4 networks.
  Capture commit `ac307a2` adds ten individual `/128` addresses in the RFC
  3849 `2001:db8:106::/64` documentation prefix through the existing generic
  network seeder. The first mandatory review found that the shared reverse-zone
  helper is IPv4-only; the amended commit disables reverse-zone creation only
  for this documentation IPv6 network and retains it for both IPv4 networks.
  JSON, diff, and inventory checks pass. Follow-up review cleared the finding
  with no remaining issues; reset/allocation integration remains to confirm
  that both fixture VPSes consume the seeded IPv6 addresses successfully.
- The final local-mode acceptance cluster now has two running fixture VPSes:
  `vps` in Production/Praha on node1 and `playground-vps` in
  Playground/Playground on node2. Both have documentation IPv4 and IPv6
  addresses. Dataset `1/data` is mounted at `/srv/data`; NAS dataset `nas` is
  provisioned with a 250 GiB quota on primary pool `backuper1`.
- Capture commits `484da75` through `e809e94` make dataset capacity, explicit
  mounts, NAS provisioning, and flake source filtering idempotent. The live
  database-setup rerun validated the existing NAS dataset, pool copy, quota,
  and resource accounting without recreating it.
- Capture commits `c17a731` through `c1d80b2` tighten action/form crops, add
  the documented interface address, retain exactly one additional fixture VPS
  allocation in Playground and Production, include the mount table with VPS
  datasets, prevent CPU status normalization from replacing requested cores,
  wait for NFS advanced options to reach full opacity, and anchor section
  crops at their headings. Fresh mandatory reviews cleared every functional
  change; the only history advisory was resolved by squashing the interface
  navigation correction into its owning commit.
- Determinism commits `b54a39c`, `5673aeb`, and `b82711e` remove the temporary
  TOTP device ID from route provenance, render a canonical rescue-console
  summary only after observing the real Alpine login, exclude volatile tips
  and transaction rows from the rescue sidebar, restore the start-menu timeout
  without a redundant restart, and allow the real traffic TUI up to 30 seconds
  to paint its first finite row. Back-to-back TOTP and rescue captures produced
  identical routes and PNG hashes. Fresh mandatory reviews returned no
  blocking or important findings.
- The definitive capture at `62126b5` completed all 60 Czech checkpoints in
  one process. `nix develop -c bin/check` passes with 60 assets, 63 page
  references, 60 PNGs, no duplicate hashes, JavaScript/Ruby/shell syntax, and
  ShellCheck. Contact sheets and direct image inspection confirmed all user
  feedback, including tight titled forms, populated mounts/NAS, opaque export
  options, production-shaped environments, corrected TUI, full TOTP content,
  and the full console/header/keyboard/rescue controls view.
- Force-with-lease was unnecessary when pushing the finalized capture branch:
  remote `e0a3502` fast-forwarded to `62126b5`. The repository has no GitHub
  Actions runs for this branch.
- Rebuilt the local 30-page/60-media release from capture commit `62126b5`.
  Reset staging to a fresh production mirror, then staged and API-verified the
  revised pages and media. Language-link warming verified all 27 paired Czech
  candidate pages. Production remains untouched.
- Rendered staging smoke checks returned HTTP 200 for the Czech home page, the
  rescue article, and the renamed rescue PNG with `image/png`. The dedicated
  capture cluster was stopped and its GC root removed; the global KB staging
  container remains running for review.

- The screenshot implementation and original production-draft bundle passed
  their earlier mandatory review. The staging infrastructure and release
  workflow have now passed their required fresh standalone review with no
  remaining findings.
- Detailed audit written to `kb-label-audit.md`.
- Added create-only DokuWiki media operations to `bin/kb-page` and committed
  them on the coordination workspace `master` as `5e2b40b`.
- Preparation tooling is committed separately on coordination workspace
  `master` as `2b6f7ea`; the reusable dev-cluster note is `b06f2f3`; the audit,
  exact source snapshots, complete previews, migration manifest, and
  synchronized screenshots are committed as `e3ae318`.
- A disposable draft media upload was written, downloaded byte-for-byte, and
  deleted. No smoke-check media remains on the wiki.
- The obsolete review set still contains 30 pages and 60 media assets under
  `drafts:2026-07-10-kb-czech-fixes` using create-only writes. The review entry
  page is
  `https://kb.vpsfree.cz/drafts:2026-07-10-kb-czech-fixes:domu`.
- Read every draft page and media asset back through the API. All 30 page
  sources match the local previews byte-for-byte and all 60 media SHA-256
  hashes match the manifest.
- No staging or production deployment has been attempted. The user/operator
  deploys aitherdev and internal DNS from a build machine. Production
  publication remains subject to explicit user approval.
- All 60 Czech screenshot assets are generated and tracked in the standalone
  repository. The inventory maps 63 page references to exact scenario
  checkpoints and stable semantic draft/permanent media IDs.
- The user chose stable semantic screenshot names without order or revision
  suffixes. Git and DokuWiki will retain revisions of canonical media IDs.
- The user also required the capture repository to own its complete dev-cluster
  lifecycle and fixture setup with no runtime coordination-repository
  dependency. The repository now vendors and adapts the cluster definition,
  pins upstream inputs in `flake.lock`, and has passed a fresh acceptance run.
- The capture feature branch is pushed through language-first commit
  `e0a3502`.

## Staging implementation update

- Added the stopped-by-default declarative `kb-staging` NixOS container to
  aitherdev, with Czech and English DokuWiki sites, shared media, the production
  template/syntax plugins, local staging-only authentication, and an explicit
  full-state reset helper.
- Added internal DNS CNAMEs and aitherdev nginx reverse proxies for
  `kb-cs.aitherdev.int.vpsfree.cz` and
  `kb-en.aitherdev.int.vpsfree.cz`.
- Added `bin/kb-stage` and `lib/kb_stage.rb` for ownership, generated
  credentials, start/stop/status, full production mirror reset, and safe
  release of the global staging instance.
- Added `bin/kb-release` and `lib/kb_release.rb` for checksummed staging,
  verification, drift-safe production promotion, and pending-manifest binding.
- Changed `bin/kb-page` so staging writes require current ownership and every
  production write requires `--approved-production`. Staging uses generated
  Basic credentials; production continues to use bearer tokens.
- Migrated the local review bundle from draft IDs to exact production page IDs
  and final Czech media IDs. `kb-release.yml` now contains 30 page candidates
  and 60 create-only media objects. Page translation tags and relative links
  remain intact for staging review.
- Changed both capture-repository and initiative artifact paths to
  `screenshots/cs/<topic>/<view>.png`; DokuWiki IDs are
  `cs:screenshots:vpsadmin:<topic>:<view>.png`.
- The old production draft set will be removed only after staging has been
  deployed and verified, with separate explicit production approval.
- After the first operator deployment, both internal names resolved to
  `172.16.106.40` and all 30 production source pages still matched the release
  manifest. Runtime start then exposed that aitherdev's general sudo policy
  requires an interactive password, which Codex cannot provide.
- Replaced direct privileged `nixos-container` calls with a Nix-store-backed
  helper that validates one action and always targets only `kb-staging`.
  Passwordless sudo is limited to the helper's exact `start`, `stop`, and
  `clear` command lines. Unprivileged status continues to call
  `nixos-container status` directly.
- Built aitherdev generation `2026-07-11--09-49-03`, inspected the generated
  sudoers and helper outputs, and validated the sudoers with `visudo -cf`.
  Unknown actions and extra helper arguments exit with status 2.
- A fresh mandatory security review found that the live
  `nixos-container status` output is lowercase `up`/`down`, while the first
  reset guard expected uppercase `UP`. Amended coordination commit `9553f71`
  centralizes lowercase status parsing and adds coverage for `up`, `down`,
  uppercase output, and command failure. The reviewer returned no remaining
  findings. Post-redeployment validation must exercise the sudo allow/deny
  matrix and the complete lifecycle.
- Force-with-lease pushed the rebased configuration feature branch through
  `4392ef47`; the previous remote head was the pre-rebase staging commit. No
  GitHub Actions runs exist for the branch, so there were no superseded runs to
  cancel.
- The first permission redeployment still prompted for a password. Runtime
  inspection showed that the later generic `%wheel ALL` rule overrode the
  earlier aither `NOPASSWD` tag. The corrected configuration uses `lib.mkAfter`
  so the three exact rules are last. Both sudoers and the coordination tooling
  use the root-controlled `/run/current-system/sw/bin/kb-staging-containerctl`
  path with one exact action argument.
- The mandatory follow-up review found that a direct Nix-store path in sudoers
  would not match the system-profile path used by the tooling under the
  deployed sudo version. Corrected both sides to use the same profile path.
- Built corrected aitherdev generation `2026-07-11--10-22-44`; its generated
  sudoers puts the exact profile-path allowlist after `%wheel ALL` and passes
  `visudo -cf`. The amended configuration commit is `324afe7`.
- The mandatory permission follow-up review returned no findings. It confirmed
  that the paths now match, rule ordering is effective, and privilege remains
  limited to exact start, stop, and clear actions for `kb-staging`.
- Force-with-lease pushed configuration commit `324afe7` and pushed matching
  coordination commit `2438ef9`. The configuration repository's push hook must
  run inside `nix develop`; the ambient-shell attempt was rejected because its
  bundled hook gems were unavailable, and the Nix-shell push passed.
- After redeployment, the live sudo boundary passed: exact start and stop work;
  unknown actions, extra arguments, direct `nixos-container`, direct
  `systemctl`, and shell execution are all rejected by `sudo -n`. Unprivileged
  status reports lowercase `up` and `down` as expected.
- The first live reset reached the permitted clear action, then failed because
  `systemd-tmpfiles --create` tried to change permissions on the intentionally
  read-only credential bind mount. Stopped the partially cleared container.
- Configuration commit `9e6f2d58` excludes only `/private/kb-staging` from the
  reset-time tmpfiles pass. Repository hooks and a full aitherdev build passed;
  generation `2026-07-11--10-35-32` contains the corrected clear script.
- The standalone reset-fix review returned no findings and confirmed that all
  writable wiki and shared-media tmpfiles rules still run. After redeployment,
  reset validation must also compare credential hashes and modes before and
  after the clear/mirror operation.
- Pushed reset-fix commit `9e6f2d58` to the configuration feature branch;
  awaiting redeployment for the live reset retry.
- After redeployment, reset mirrored 146 Czech pages, 70 English pages, and 166
  shared media objects. Credential contents and modes were identical before
  and after reset. Staged and API-verified all 30 candidate pages and 60
  create-only media objects at their production IDs.
- HTTP checks rendered all 30 pages and fetched all 60 distinct referenced
  screenshots as valid PNG files. A Playwright check then found six broken
  template images: the template derivation's versioned name installed it under
  `lib/tpl/dokuwiki-vpsfree-2023-12-09`, while DokuWiki generated URLs under
  `lib/tpl/dokuwiki-vpsfree`.
- Configuration commit `d19575b1` restores the exact configured template name.
  Hooks and full aitherdev build passed; generation
  `2026-07-11--10-52-15` contains `lib/tpl/dokuwiki-vpsfree/images/logo.png`.
- The standalone template follow-up review returned no findings. It confirmed
  that both language packages retain all 64 template files with identical
  bytes and modes and change only the directory name. Deployment-only browser
  validation remains.
- Pushed template-path correction `d19575b1`; awaiting aitherdev redeployment
  and a staging-container restart. The staged release remains pending in the
  persistent container state.
- After deployment, stopped and restarted the container onto the corrected
  generation. The pending release survived and `kb-release verify` still
  matched all 30 pages and 60 media objects.
- Final Playwright validation covered all 30 page URLs, 304 rendered image
  instances, all 60 distinct KB screenshots, and the six previously missing
  template assets. No same-host document, stylesheet, script, image, or font
  requests failed. The first pass's `networkidle` timeout on the SSH article
  was caused by its external embed; the final check waits for DOM completion
  and validates all same-host resources explicitly.
- Visually inspected full-page renders of `informace:novacci`,
  `navody:vps:datasety`, and `navody:vps:konzole`; the template, screenshot
  cropping, scaling, and article layout render correctly. Czech staging is
  ready for user review at `http://kb-cs.aitherdev.int.vpsfree.cz/`.
- Final coordination commits are `e29896d`, `e89a91c`, `a14b15e`, and
  `693f8da`, followed by state-only completion commits.

## Commands run

- `bin/dev-session current` and environment verification.
- `bin/kb-page whoami --wiki cz`.
- Read-only DokuWiki JSON-RPC through the `bin/kb-page` client:
  - `core.listPages` with namespace `""` and depth `10`;
  - `core.getPage` for every returned page;
  - `core.listMedia` with depth `10`;
  - selected `core.getMediaInfo` checks.
- `git -C repos/vpsadmin.git fetch --prune origin`.
- Created the initiative vpsAdmin worktree from the user's updated
  `origin/master` at `299147166ecb8459c712ed8a5c4dd14f673663fc`.
- `git -C repos/haveapi.git fetch --prune origin`.
- Read vpsAdmin `AGENTS.md`, `doc/i18n-cs.md`, WebUI PO/POT catalogs,
  API English/Czech YAML catalogs, and relevant WebUI source at the authority
  commit.
- Compared KB text to flattened WebUI and API English/Czech label pairs, then
  manually reviewed navigation-shaped and emphasized text.
- `ruby -c bin/kb-page`.
- `ruby test/kb_page_test.rb`: 25 runs, 104 assertions, 0 failures, 0 errors.
- Draft media smoke check using `media-save --create`, `media-info`,
  `media-get`, SHA-256 comparison, and `media-delete`.
- Started the standalone repository's single-node dev cluster with local
  networking. Local networking was used because another initiative owns the
  one VPN-visible bridge-cluster slot.
- Created a local canonical bare `vpsadmin-kb-captures` repository and feature
  worktree, then connected the user-created GitHub repository over SSH.
- Pinned the Nix development shell and Playwright browser in `flake.lock`.
- Ran the complete capture command against vpsAdmin commit
  `299147166ecb8459c712ed8a5c4dd14f673663fc`.
- Ran `bin/validate --update`, strict `bin/validate`, JavaScript syntax checks,
  Ruby syntax checks, and `bin/check`.
- Ran the mandatory standalone change review. It found four blocking areas:
  console readiness accepted a service banner, CLI traffic output had no
  finite row, fixtures reused arbitrary cluster objects/dynamic dates, and one
  coordination commit mixed tooling with the generated review bundle. It also
  requested stronger result/immutability validation and resolution of six
  exact duplicate-image groups.
- Regenerated the standalone flake lock with vpsAdmin pinned at
  `299147166ecb8459c712ed8a5c4dd14f673663fc` and successfully evaluated the
  repository-owned cluster outputs with `nix flake show --impure`.
- Ran `bin/devcluster refresh kb-captures` against the repository-owned cluster
  after adding its osctld socket and pool readiness checks.
- Ran `bin/capture --cluster kb-captures --language cs`; all 60 checkpoints
  completed in one process.
- Ran `bin/validate --update`, `nix develop -c bin/check`, and
  `git diff 4f6a144..HEAD --check`; all passed.
- Generated and visually inspected contact sheets for all eight scenarios.
- Pushed the two capture commits to
  `origin/2026-07-10-kb-czech-fixes`.
- Rechecked all 30 live source pages immediately before draft creation; their
  revisions and byte-exact content still matched the recorded snapshots.
- Verified identity, create ACL, and nonexistence for the exact 30 page and 60
  media draft targets.
- Uploaded all 60 draft media objects with `bin/kb-page media-save --create`,
  followed by all 30 pages with `bin/kb-page save --create`.
- Read all 30 pages back and compared their bytes, then read all 60 media
  objects back and compared their SHA-256 hashes.
- Fetched all 30 public draft renders, confirmed all 63 expected embeds and no
  legacy screenshot references, and fetched all 60 unique rendered PNG URLs.
  The first URL check retained HTML-encoded `&amp;` query separators and received
  HTTP 412 for resized images; decoding the extracted HTML URL fixed the test.
  The reusable lesson is recorded in
  `notes/cross-project/2026-07-10-dokuwiki-rendered-media-url.md`.
- Stopped the standalone `kb-captures` dev cluster after verification.
- Re-ran the three coordination generators and confirmed the complete review
  bundle remained unchanged.
- Re-ran `ruby test/kb_page_test.rb`: 25 runs, 104 assertions, no failures.
- Re-ran `nix develop -c bin/check` in `vpsadmin-kb-captures`: 60 assets, 63
  references, and 60 PNGs; syntax and inventory checks passed.
- Updated the capture inventory to schema 3 and ran
  `nix develop -c bin/check`: 60 assets, 63 references, 60 PNGs, and all
  language-first paths passed.
- Ran `ruby test/kb_page_test.rb`: 30 runs, 120 assertions, no failures.
- Ran `ruby test/kb_stage_test.rb`: 9 runs, 34 assertions, no failures.
- Regenerated `screenshot-manifest.yml` from capture commit `e0a3502` and
  regenerated `kb-release.yml`: 30 pages and 60 media objects.
- Ran Ruby syntax checks for `kb-page`, `kb-stage`, `kb-release`, and their
  libraries; all passed.
- Ran `nixfmt` on the aitherdev configuration and built
  `cz.vpsfree/machines/aitherdev` with `confctl build -y`; generation
  `2026-07-10--22-59-41` completed successfully. This was a build only; no
  deployment or DNS update was performed.
- A standalone `nixpkgs#rubocop` invocation could not activate because its
  packaged `rubocop-ast` requires `prism ~> 1.7`, which was absent from the
  generated Ruby load path. The configuration repository's RuboCop could not
  be reused as-is because its project config targets Ruby 2.7 while this
  workspace already uses Ruby 3 keyword shorthand. Ruby 3.4 syntax checks,
  unit tests, line-length inspection, and `git diff --check` are the recorded
  fallback checks; the coordination repository declares no Ruby hook framework.
- Ran the mandatory fresh-context review across coordination commit range
  `b7afb3f..693f8da`, capture commit `e0a3502`, and configuration commit
  `bbe8a5db`. The review initially found unsafe removal of a live media bind
  mount, stale pending-release markers, staging mutation races, non-retryable
  partial publication, an unguarded future media-update policy, an overly wide
  correction commit, and a long production drift-check window.
- Corrected every finding: reset preserves bind-mount roots; all staging
  lifecycle and publication operations share the ownership lock; staging bytes
  are reverified before promotion; partial page saves are retryable; update
  media requires the recorded source hash; source pages are rechecked directly
  before each save; and the coordination history was rebuilt as four focused
  commits. The reviewer returned **no remaining findings**. The documented
  residual is DokuWiki's lack of compare-and-swap saves, so publication needs
  an announced editing window.
- Pushed capture branch `2026-07-10-kb-czech-fixes` through `e0a3502` and
  configuration branch `2026-07-10-kb-czech-fixes` through `bbe8a5db`.
  Pushed coordination `master` through the review-resolution state commit.
- The configuration repository's ambient pre-push hook initially could not
  load its bundled gems. Re-running the push from `nix develop` loaded the
  declared hook environment and succeeded without bypassing the hook.
- Queried GitHub Actions for both feature branches after push; neither
  repository has a workflow run for this branch.
- Fast-forwarded the vpsAdmin worktree to current `origin/master` commit
  `7e0be5d215ce554009ff92381bdb54557e618776`.
- Captured all 59 Czech checkpoints in one process and ran
  `nix develop -c bin/check`; schema-4 inventory, 63 references, 59 distinct
  PNGs, crop/font regression checks, syntax checks, and ShellCheck passed.
- Pushed `vpsadmin-kb-captures` feature head
  `799b385635d051a87a90bff2e14787f635904bb8` over SSH. The repository has no
  GitHub Actions workflows or branch runs.
- Ran `bin/kb-stage reset --yes`, `bin/kb-release stage --yes`, and
  `bin/kb-release verify`; the final release contains 30 pages and 59 media
  objects and remains pending on Czech staging.
- Ran a Playwright staging acceptance pass over every candidate page. All 30
  documents and same-origin resources loaded, and all 59 distinct canonical
  screenshots returned successful `image/png` responses.
- Stopped dev cluster `2026-07-10-kb-czech-fixes`, removed its GC root, and
  verified `stopped no-gcroot`. The staging KB container remains `up`.

## Results

- Accessible page inventory: 116 pages.
  - 6 root pages
  - 1 draft page
  - 32 `informace` pages
  - 63 `navody` pages
  - 3 `private` pages
  - 5 `uzivatele` pages
  - 6 `wiki` pages
- Pages requiring draft copies for text and/or screenshot work: 30.
- Pages with no direct text or screenshot work in this initiative: 86.
- Screenshot work: 63 affected references to 60 unique media files across
  18 pages. Their revisions range from 2014-10-29 through 2025-03-16.
- The exact mapping, page locations, screenshot list, intentional exceptions,
  and no-change page coverage are recorded in `kb-label-audit.md`.
- Screenshot feasibility check:
  - the initiative single-node dev cluster ran with the expected WebUI/API
    hostnames;
  - the host has about 395 GiB of free disk and 72 GiB of available memory,
    which is sufficient for the services VM, one node, and headless Chromium;
  - vpsAdmin's Playwright suite provided patterns for login, Czech language
    switching, and page helpers; the standalone repository now supplies the
    dedicated deterministic KB scenarios and viewport/crop conventions;
  - another initiative's bridge dev cluster
    (`2026-07-02-haveapi-i18n`) is currently running. The dev-cluster tooling
    allows only one VPN-visible bridge cluster at a time. This initiative uses
    local networking to avoid changing or stopping the other session's
    cluster; this is the recorded reason for departing from the bridge default.
- The first coordination-workspace cluster evaluation failed because its
  dev-cluster flake references
  the private `vpsfree-sms-gateway` repository with a `github:` input, which
  returned an unauthenticated 404. An isolated worktree temporarily supplied
  that input as a local path. The standalone capture repository eliminated
  this runtime dependency. The original workaround is recorded in
  `notes/cross-project/2026-07-10-devcluster-private-github-input.md`.
- Reproducible screenshot repository result:
  - 60 manifest assets and 63 source-page references;
  - eight scenarios: getting started, networking, storage, console,
    VPS management, Playground, environments, and account;
  - 54 WebUI assets, five live-console assets, and one real CLI asset;
  - deterministic fixtures for two VPSes, a snapshot, public key, traffic,
    NixOS generation metadata, and an unconfirmed TOTP device;
  - 60 PNGs with dimensions, SHA-256, sanitized route provenance, and the
    current vpsAdmin commit;
  - the acceptance run completed all 60 checkpoints in one process and strict
    validation passed.
- Mandatory-review resolutions:
  - console checkpoints wait for guest-specific Alpine/OpenRC/login output,
    rather than accepting a remote-console service banner;
  - the CLI checkpoint validates a real finite traffic row for the fixture VPS
    and its actual network interface before rendering stable documentation
    output;
  - fixtures identify and recreate only their own labeled objects, reject
    duplicates, and normalize dates and volatile counters;
  - validation binds every result to its exact scenario, checkpoint, driver,
    output path, and SHA-256, while protecting accepted assets from mutation;
  - the six duplicate-image groups were replaced with distinct checkpoint
    captures, and strict validation rejects any duplicate PNG hashes;
  - the coordination history is split into tooling, durable note, generated
    review bundle, and state commits.
- Draft result:
  - 30 complete Czech review pages;
  - 60 new semantic Czech media IDs and 63 embedded image references;
  - no production page or legacy media write;
  - byte-for-byte page verification, SHA-256 media verification, and rendered
    page/media checks passed.

## 2026-07-11 screenshot review follow-up

- Fetched vpsAdmin and fast-forwarded the clean initiative worktree from
  `299147166` to `7e0be5d21`, the current `origin/master`. The capture flake and
  every inventory entry now pin that exact revision.
- Traced `informace:details2.png` to the incorrect
  `getting-started/vps-action-menu` asset. No other page uses that capture.
  Capture schema 4 removes it and records `informace:details2.png` as a legacy
  alias of `vps-management/set-root-password`, which is now shared by
  `informace:novacci` and `navody:vps:sprava`. The expected result is 59 unique
  assets and 63 page references.
- The crop helper now includes complete table/fieldset boxes, preserves heading
  line heights, and applies symmetric eight-pixel padding. The Web Console
  selects its complete H1 element. Synthetic and WebUI terminals use a pinned
  Liberation Mono font through the Nix-shell Fontconfig configuration.
- Browser-level crop and font checks pass in `nix develop`, as do the terminal,
  console, provenance, dataset-link, Ruby syntax, inventory allow-missing, and
  ShellCheck quick checks.
- A direct pure `nix eval` of the cluster derivation still hits the pinned
  vpsAdminOS source's existing unlocked `builtins.getFlake` path. The capture
  shell evaluates and builds through the repository's normal dev-cluster
  lifecycle; this failed diagnostic did not change tracked files.
- Release synchronization and generation now accept legacy aliases, remove
  stale generated PNGs, require 59 media objects, and fail if
  `informace:novacci` does not use the canonical root-password form.
- The mandatory standalone review found no correctness, security,
  compatibility, or deployment issues. It blocked the original broad capture
  commit only because the pin, alias migration, crop behavior, and font setup
  could be reviewed independently.
- Rewrote the unmerged capture change into four focused commits with an
  identical final tree: `0cfad06` (password-form alias/removal), `e76a040`
  (vpsAdmin pin), `7157a51` (crop and console heading), and `3ff72c9`
  (terminal fonts). Repeated every quick check after the rewrite; all pass.
  The generated schema-4 provenance and refreshed PNG hashes remain
  intentionally pending until the full cluster capture.
- Bridge networking remains occupied by the running
  `2026-07-02-haveapi-i18n` initiative. This run will reuse the already
  isolated `local` capture-cluster configuration. `/dev/shm` has 33 GiB free,
  sufficient for this topology's 14 GiB VM allocation without disturbing the
  other cluster.
- A completely reset cluster exposed the two-stage seed lifecycle: database
  setup creates the transaction-backed NAS records, then the idempotence seed
  can run before nodectld confirms them. Commit `ad41b29` accepts only the
  coherent four-record `confirm_create` state in addition to the fully
  confirmed state; missing, mixed, and unsupported states remain drift. A
  fresh mandatory review returned no blocking or important findings, and its
  unsupported-state test advisory was incorporated before the live update.
- The live services update reran the seed successfully, refreshed both nodes,
  and preserved the dedicated cluster. Representative VPS-management, Web
  Console, and CLI-monitor captures passed visual inspection.
- Capture commit `799b385` regenerates all 59 Czech assets in one process.
  Strict `nix develop -c bin/check` passes with schema-4 provenance, 63 page
  references, 59 distinct PNG hashes, crop/font regression checks, Ruby/Node
  syntax, and ShellCheck. Refreshed contact sheets confirm complete right
  borders with symmetric margins, the complete console title and keyboard,
  natural terminal spacing, contextual Czech buttons, populated storage
  fixtures, and the shared root-password form. The branch is pushed and has no
  GitHub Actions runs.
- Reset the internal staging instance from production after generating the
  final release. The mirror contains 146 Czech pages, 70 English pages, 58
  language pairs, and 166 shared media objects. Staged and API-verified the
  final 30-page/59-media release. Its pending-manifest SHA-256 is
  `5c27cab9a2569d8e8ff69066b1ed600dff315308b316cf4c81dd410ebee8289c`.
- The final Playwright pass rendered all 30 candidate pages, checked all
  same-origin resources, and fetched all 59 distinct screenshot paths as
  PNGs. The root-password image appears twice at different display widths, as
  expected, but resolves to one canonical media object.
- The dedicated local-network capture cluster is stopped and its GC root has
  been removed. The global KB staging container remains up and owned by this
  initiative for user review. Production remains untouched.

## Open questions

- Before publication, decide whether to modernize the old Slovak article
  `navody:vps:obnova_webu_zo_zalohy` beyond its UI labels. The current plan
  deliberately limits that page to localization/navigation corrections and
  screenshot recapture.
- The current WebUI catalog translates the mount toggle button `Enable` as
  `Zapnuto`. The plan avoids turning that odd button text into prose by
  describing the operation naturally while retaining the exact UI labels only
  where necessary.
- No publication naming decision remains: draft and permanent screenshot IDs
  use functional-topic, language, and semantic-view components. English
  variants will reuse the same topic/view structure in the `en` namespace.
- The standalone capture and configuration feature branches are pushed and
  ready for operator review/merge.

## 2026-07-12 node identity and console follow-up

- User review requested production-shaped short node domain names and a final
  correction to the Web Console framing.
- Exact exposed identities are `node1.prg`, `node1.pgnd`, and
  `backuper1.prg`. The Playground VM retains internal machine key `node2`;
  duplicate bare `node1` values must not be used as peer or seed identifiers.
- Exact location domains are Praha `prg`, Brno `brq`, Playground `pgnd`, Praha
  Storage `prg`, and Staging `stg`. Environment domains remain documentation
  fixtures.
- The console follow-up will crop the H1 with the complete outer iframe so
  nested-frame scrolling cannot clip its top or right edge. Other screenshot
  crop behavior remains unchanged.
- Implementation will use a fresh local-network cluster, recapture all 59
  assets, rebuild and verify the 30-page/59-media staging release, and leave
  production untouched.

## Cleanup

- The standalone initiative dev cluster has been stopped and its GC root
  removed.
- The four initiative worktrees (`vpsadmin`, `vpsfree-sms-gateway`,
  `vpsadmin-kb-captures`, and `vpsfree-cz-configuration`) remain available for
  review and post-deployment acceptance.
- Temporary capture credentials, console tokens, raw terminal streams, fixture
  state, and contact sheets are under the ignored `tmp/` directory in the
  capture worktree and are not committed.
- The 30 review pages and 60 review media assets remain in the draft namespace
  for user review.
- The current 30-page/59-media release remains on the internal staging KB at
  `http://kb-cs.aitherdev.int.vpsfree.cz/`; production has not been changed.
