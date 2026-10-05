---
lifecycle: active
---
# 2026-08-14-kb-updates

## Repositories

- Repository: `vpsfree-kb-contracts`
- Branch: `2026-08-14-kb-updates`
- Worktree: `worktrees/2026-08-14-kb-updates/vpsfree-kb-contracts`
- Base: `origin/master` at `5bf06be`
- Validation-only worktree: `worktrees/2026-08-14-kb-updates/vpsadminos`
  detached at `67fcc17372d175b036706a1459a8b471bfc225e0`

## Status

The first implementation, review, verification, integration, and staging pass
completed at `d85cadc`. User review requested a follow-up revision; its
implementation is in progress on the same feature branch. Staging remains
claimed by this initiative and production has not been changed.

## Commits

- `7737225` — Manage and test the Guix KB article
- `d85cadc` — Refresh navigation coverage for the KB updates

## Commands run

- `bin/dev-session current`
- Workspace and bare-repository status/ref inspections
- `git --git-dir=repos/vpsfree-kb-contracts.git fetch origin --prune`
- `git --git-dir=repos/vpsfree-kb-contracts.git worktree add -b ...`
- Repository-local `AGENTS.md`, flake, and hook-framework inspection
- Fresh production fetch with `bin/kb-contract-fetch`: 119 Czech and 76
  English pages
- Schema-4 candidate construction with `bin/kb-contract-build`: 23 changed
  pages, including 9 new pages, 12 guarded replacements, and 2 managed Guix
  pages
- Candidate-aware `tools/check-kb-annotations.rb`
- `nix develop --command bin/check --allow-missing`
- `./test-runner.sh test --fresh 'kb/guix#reconfigure'`
- Mandatory standalone change review using
  `skills/mandatory-change-review/SKILL.md`
- Review follow-up: split Guix from navigation/capture changes, added semantic
  SSH detail and public-key paths, delegated console UI steps to its dedicated
  guide, added literal IPv6 endpoint syntax, asserted the reconfigured hostname
  after the Guix restart, and stopped marking untested recovery claims as
  runtime-covered
- External-link requests for all 33 distinct URLs in changed pages
- Final candidate construction and localized manifest generation: 12 Czech
  page writes and 11 English page writes
- Feature-branch push and GitHub Actions monitoring for exact head `d85cadc`
- `bin/kb-stage start` and `bin/kb-stage reset --yes`
- Staging `whoami` checks and exact-page ACL checks for all 23 manifest targets
- Fresh target-worktree fast-forward, full static check, master push, and
  removal of the temporary integration worktree
- `bin/kb-release stage` and `bin/kb-release verify` for both localized
  manifests
- Authenticated ACL checks and direct staging deletes for the five retirement
  targets, followed by explicit absent-page checks
- HTTP render/title checks for all 23 staged pages and managed-source toolbar
  checks for both Guix pages

## Results

- Active session and `VPSFREE_DEV_SESSION_SLUG` both resolve to
  `2026-08-14-kb-updates`.
- Contract work starts from current `origin/master` (`5bf06be`).
- The repository declares no separate Git hook framework; repository checks run
  through its Nix shell and `bin/check`/`bin/validate` tooling.
- Reciprocal Czech and English candidates are prepared for SSH, firewall,
  Docker, Snap, WireGuard, Guix, and NixOS Mailserver. The old Docker, Snap,
  and Mailserver IDs are localized move stubs.
- SSH and firewall both explain recovery through the vpsAdmin remote console.
  The SSH page keeps root access as the template convenience default and does
  not recommend IP allowlists. The firewall page treats a local firewall as an
  optional protection layer and documents UFW, firewalld, and NixOS.
- The current candidates contain no links from changed pages to the five IDs
  selected for retirement. The retirement set is the generic Nginx page, the
  old NixOS Nginx and getting-started pages, OpenShift on CentOS, and the OpenWrt
  WireGuard page. Deletion is a separate staging operation because release
  manifests represent page writes, not removals.
- Guix is now a managed bilingual article with a pinned vpsAdminOS runtime test
  that imports the current image, changes the documented system configuration,
  reconfigures it using the exact article fixture, restarts it, and verifies
  networking and SSH.
- The first runtime-test design built an unpinned current Guix image and used a
  24 GiB VM. The coordinating process was killed by the OOM killer; the exact
  orphaned test VM was stopped without touching unrelated QEMU processes. The
  VM was reduced to 12 GiB and the test was changed to import published image
  version `20260613` instead of testing moving image-source code.
- A plain `guix system reconfigure` on that image then correctly refused a
  channel ancestry mismatch between the image's packaged Guix revision and the
  revision recorded by its active system generation. The managed command now
  uses `guix time-machine -C /run/current-system/channels.scm`, loads the active
  generation profile, and keeps Guix's ancestry check intact. The fixture also
  configures a working container DNS resolver for substitutes.
- The final focused runtime test passed all three examples and the complete
  `kb/guix` test in 2533.58 seconds. It verified the shipped platform module,
  created and activated a new generation with the exact article fixture,
  restarted the container, and confirmed the new hostname, network, and SSH.
- The mandatory review reported two Blocking findings, two Important findings,
  and one Advisory. Both Blocking and both Important findings were resolved.
  The Advisory requires explicit absence checks for the five direct staging
  deletes and a separate representation decision before any future production
  retirement; those checks remain in the staging procedure.
- Navigation inventory validation passes with 82 bindings and 9 documented
  exceptions. Full repository validation passes: 40 controls, 32 paths, 33
  capture concepts, 2 managed articles, 6 article tests, 118 screenshot
  variants, 64 Czech references, and 59 English references. Ruby suites pass
  with 8/50, 9/20, and 15/43 runs/assertions and no failures.
- After review the contract contains 32 paths, including the two new SSH paths.
- All changed-page external links returned HTTP 200 except the Alpine Docker
  wiki, which rejected the automated request with HTTP 403; it remains the
  current browser-facing distribution wiki URL.
- Candidate source revision is production base `5bf06be` and managed contract
  head `d85cadc`. Candidate files are in
  `work/2026-08-14-kb-updates/kb-candidates`.
- The release manifest's reciprocal-language guard caught the legacy Czech Snap
  move notice claiming the canonical English Snap page. The move-only page now
  has no counterpart marker, while the canonical pair remains reciprocal. The
  old English trash navigation page was also translated and paired with its
  Czech counterpart instead of retaining Czech text.
- Candidate-aware annotation validation found the translated link index as a
  new lexical navigation match. It is now recorded explicitly as a KB link
  index, not a vpsAdmin WebUI path; the final full and candidate-aware checks
  pass at `d85cadc`.
- Feature-branch GitHub Actions passed on exact head `d85cadc`: Check run
  `31824695204` in 5m50s and managed runtime run `31824695207`, with Guix in
  28m57s and KVM in 39m54s.
- A fresh target worktree fast-forwarded local master from `5bf06be` through
  both feature commits. The complete static suite passed there before master
  was pushed, and the temporary integration worktree was removed. Master
  Check run `31828654721` passed in 5m50s; managed runtime run `31828654719`
  passed Guix in 33m45s and KVM in 31m01s. No workflow was rerun and no failed
  artifact required investigation.
- The staging mirror was refreshed at `2026-08-14T17:44:56Z`. Both staging API
  identities are authenticated as the staging admin and all manifest targets
  returned ACL 255.
- The Czech manifest staged and verified 12 pages; the English manifest staged
  and verified 11 pages. Both language checks warmed and verified all 11
  reciprocal page pairs. All 23 HTTP-rendered pages returned their expected
  localized titles, and the managed Guix pages expose the intended GitHub
  source toolbar link without rendering the marker itself.
- The generic Nginx, old NixOS Nginx and getting-started, OpenShift on CentOS,
  and OpenWrt WireGuard pages were deleted from Czech staging after a fresh
  identity and ACL check for each write. `kb-page get` reports every ID as not
  existing. Direct deletions intentionally invalidate the single-manifest
  pending-release marker; production retirement needs an explicit
  representation/restaging decision before promotion.
- Workspace note commit `4254261` records the reproducible Guix time-machine,
  channel-lineage, DNS, and VM-memory lesson on workspace master.

## Open questions

None. The user confirmed that `ssh-copy-id` stays as the normal default-password
path, the Guix alternative must preserve its original `guix deploy` purpose,
and GRE should become a modern managed bilingual article with runtime tests.
The Debian GRE section will retain `/etc/network/interfaces`: vpsFree Debian
templates install ifupdown, while the old article's inner and outer endpoint
fields need correction.

## Cleanup

- Leave staging claimed after verification so the user can review it.
- The temporary master integration worktree and merged feature worktree were
  removed after green CI and integration.
- Keep the feature branch locally and remotely after merge.

## Follow-up worktree

- Recreated `worktrees/2026-08-14-kb-updates/vpsfree-kb-contracts` on
  `2026-08-14-kb-updates` at `d85cadc` after fetching the SSH origin.

## Review follow-up progress

- Fetched a fresh production source set with 119 Czech and 77 English pages;
  the additional expected-new page is `manuals:server:gre`.
- Updated the SSH drafts to use the normal root-password `ssh-copy-id` path,
  removed the custom-port noise, added the address and host-key screenshots,
  and made remote-console recovery explicitly reassuring.
- Updated Snap with the upstream 2018 change that made `/lib/modules`
  optional; current vpsFree templates still prepare the directory.
- Simplified NixOS Mailserver to an introduction, upstream release/setup
  guidance, release notes, and MXToolbox checks. Updated the English index with
  GRE and a descriptive Postfix link.
- Restored a full bilingual `guix deploy` configuration and added a second-VPS
  deployment/restart test. Added a bilingual managed GRE article and a
  two-container transient/ifupdown/restart test.
- `nix develop --command bin/check --allow-missing` passes with 3 managed
  articles, 6 pages, 7 runtime scripts, 11 executable samples, 60 capture
  concepts, and only the two intentionally missing new PNGs.
- The shared bridge address was occupied by the active
  `2026-08-12-dns-secondary-zone-transfer-failure` cluster, so the screenshot
  cluster uses local networking. The first `single` topology attempt reached
  a running VPS but correctly failed because it lacks the preseeded NAS fixture
  required by shared capture preparation. It was stopped and restarted with
  the repository-documented `screenshots` topology; no output from the failed
  run was accepted.
- Capture preparation exposed two reproducibility issues: a rejected Start
  action was never retried while VPS creation settled, and the public key was
  split at spaces when passed to the remote shell. The fixture now retries a
  stopped VPS every 15 seconds and transports the public key as base64.
- The localized SSH host-key captures were generated from a deterministic,
  public-only Ed25519 fixture and visually reviewed. The Czech image is
  672x138 with SHA-256 `6f1c113198ab92f97c9d9f32622212267f605a80ed32c4bf91c263c47d45a652`;
  the English image is 724x138 with SHA-256
  `62bcf15f65d05450c9b55c5f38f1b49379fe1a4761aa0fc681f2f613a293db7c`.
  Both show the complete expected fingerprint without clipping. The local
  capture cluster was stopped and its garbage-collection root removed.
- Follow-up contract commits are `c930203` (managed Guix deployment and GRE
  workflows) and `e5ba775` (SSH host-key captures and fixture hardening).
- Strict `nix develop --command bin/check` passes at `e5ba775`: 40 controls,
  32 paths, 33 capture concepts, 3 semantic selectors, 82 annotation bindings,
  9 exceptions, 3 managed articles, 6 pages, 7 runtime tests, 11 executable
  samples, 60 screenshot concepts, 120 variants, and all Ruby suites with no
  failures. The worktree is clean.
- Candidate preparation found that schema-4 builds rejected a registered page
  when its guarded production source was missing, even when managed
  reconciliation verified a bootstrap. Workspace commit `d815bcf` permits only
  that verified bootstrap case, emits a create policy, and adds regression
  coverage for the release manifest. The workspace tool suite passes with 30
  runs and 150 assertions.
- The full navigation inventory now includes the new English GRE page and
  refreshed SSH/Guix discoveries in contract commit `700a372`. Candidate-aware
  annotation validation passes with 82 bindings and 9 exceptions, and the
  strict repository check remains green at that head.
- Review of the rendered staging index showed that the Czech bare Postfix link
  uses the useful article title while the English link rendered only
  `Postfix`. The final English draft now labels it `Several domains on one
  email server` explicitly.
- Follow-up candidates in `kb-candidates-followup` contain 25 changed pages,
  4 managed pages, 2 new media objects, and 12 guarded full-page replacements.
  Guix and GRE reconcile as verified bilingual bootstraps; the new English GRE
  page is a managed create. The Czech and English follow-up manifests contain
  13/12 pages and one localized media object each, with managed contract head
  `700a372be5464f0d50545a403e0db9ff88ca5fb7`.
- The standalone mandatory review found no content, security, compatibility,
  staging-safety, or missing navigation-binding defect. It reported one
  Blocking history finding because Guix and GRE were combined, plus an
  Advisory to validate per-sample DokuWiki language identifiers.
- The unmerged feature history was rewritten as focused commits `d6a05e6`
  (Guix deployment and validated Scheme samples) and `2d7766e` (managed GRE),
  followed by replayed SSH capture commit `be8288e` and navigation inventory
  commit `5b5dfce`. The language validator has regression coverage. Strict
  `nix develop --command bin/check` passes at full head
  `5b5dfceefd2d42d25df663baedffa103a882582a`, including 16 runs and 46
  assertions in the article-contract Ruby suite. Both review findings are
  resolved before long runtime testing.
- The first `kb/gre#tunnel` run passed the transient and persistent/interface
  cycling examples, then failed only its restart representation assertion.
  Preserved logs in `/tmp/os-test-runner/os-test-kb__gre-cd082134` show the
  working restarted tunnel as `10.0.0.1 peer 10.0.0.2/32` rather than the
  transient command's `10.0.0.1/30`; endpoints and MTU were correct. This is
  Debian ifupdown's equivalent kernel representation of `dstaddr`, not an
  article failure. Commit `327c93f` now asserts the local/peer pair both after
  `ifup` and after restart while retaining `/30` checks for the transient
  commands. Nix formatting, diff checks, and the full static suite pass before
  the focused rerun.
- The focused GRE rerun passed all three examples and the suite in 451.31
  seconds at `327c93f`.
- The first follow-up Guix run preserved its artifact at
  `/tmp/os-test-runner/os-test-kb__guix-ca1988c9`. Its reconfigure command
  failed after 55.4 seconds while updating the pinned channel checkout with
  `Git error: SSL error: syscall failure: Resource temporarily unavailable`.
  The following boot check failed only because no new generation was created.
  The second-VPS deploy then remained inside its two-hour network-dependent
  operation for 3765 seconds; after the upstream transport cause was known,
  the already-failed run was interrupted rather than consuming the remaining
  timeout. The VM process exited and no orphan remained.
- Commit `cd32a28` adds three bounded attempts around the exact documented
  time-machine reconfigure and deploy operations. It does not change either
  article command and keeps the existing two-hour timeout per attempt. Nix
  formatting and the full static suite pass before the fresh Guix rerun.
- The fresh Guix rerun completed all five examples in 5535.61 seconds and
  preserved the same artifact path. The platform contract passed in 7.54
  seconds, the exact pinned-channel reconfiguration created and activated a
  new generation in 4912.3 seconds, and the reboot/network/SSH check passed in
  38.21 seconds. The deploy example failed deterministically after three
  attempts, and the dependent boot assertion then failed because the target
  remained on its original generation.
- The complete deploy logs identify a pinned-Guix container compatibility bug,
  not a network or article-syntax failure. Guix's safety probe tries to inspect
  initrd modules for the vpsAdminOS integration's intentionally dummy
  `/dev/null` root filesystem. The probe returns Scheme `#f`, after which Guix
  crashes while formatting it as a module list. The target was reachable by
  the pinned SSH host key and needed no store transfer before this check.
- Commit `70628d2` sets `safety-checks? #f` only for the container-specific
  bare-metal filesystem/initrd checks, documents why in both languages, and
  retains `allow-downgrades? #f`. It also limits the retry helper to the exact
  transient Git/SSL class seen in the first run, so deterministic command
  failures are no longer retried. Strict `nix develop --command bin/check`
  passes with 8/50, 9/20, and 16/46 Ruby runs/assertions and all 120 screenshot
  variants present.
- A focused non-fresh runtime probe temporarily skipped only the three examples
  already proven green by the 5535-second run. The corrected exact `guix deploy`
  command successfully built the target, sent 31 store items (496 MiB), switched
  it to system generation 2, activated hostname `guix-target`, retained the
  coordinator signing key, and reported `successfully deployed guix-target`.
  The target then restarted into the new system hash and accepted key-only SSH;
  that second example passed in 40.05 seconds.
- The deployment example's only remaining failure was a test-only invocation of
  `sshd -T` without Guix's generated `-f /gnu/store/...-sshd_config`, which made
  OpenSSH look for nonexistent Debian path `/etc/ssh/sshd_config`. Commit
  `ccd7942` instead verifies the exact managed fixture contains both
  `password-authentication? #f` and `permit-root-login 'prohibit-password`, while
  retaining the real post-reboot key-login test. The temporary skip markers were
  removed, the worktree is clean, and the strict static suite passes again.
- Snap validation used a clean detached vpsAdminOS worktree at the contract's
  exact pin `67fcc17372d175b036706a1459a8b471bfc225e0`. The first bare
  `snap/ubuntu` selector matched zero scripts and was explicitly rejected as a
  no-op. The corrected fresh selector `snap/ubuntu#*` ran both current Ubuntu
  scripts: LXD passed in 530.5 seconds, `hello-world` passed in 142.74 seconds,
  and the complete suite passed in 737.48 seconds. Neither path manually
  created `/lib/modules`, confirming the article can limit that workaround to
  older VPS templates.
- Final follow-up candidates were regenerated from clean contract head
  `ccd79422e3bfc269009aa1f237c621db1b4278f6`: 25 changed pages, 4 verified
  managed bootstraps, 9 new pages, 12 guarded full-page replacements, and 2
  localized SSH media objects. The Czech/English manifests contain 13/12 page
  writes plus one media object each and record that exact contract head.
  Candidate-aware annotation validation passes with 82 bindings and 9
  exceptions; reciprocal Guix/GRE mappings, the explicit English Postfix label,
  screenshot references, and the container-specific Guix safety setting were
  checked in the generated files.
- Feature branch `2026-08-14-kb-updates` was pushed over SSH from `d85cadc` to
  `ccd7942`. Workspace master commit `d815bcf` was fetched, confirmed linear
  over `origin/master`, and pushed without staging any unrelated shared-tree
  changes. Exact-head GitHub Check run `31860267246` and managed runtime run
  `31860267245` are being monitored.
- Exact-head GitHub Check run `31860267246` passed. In managed runtime run
  `31860267245`, article discovery and the GRE job passed; KVM and Guix remain
  in progress with no failure.
- The exact-head KVM job later failed only its final delegated-IPv6 source
  assertion. Full uploaded artifact `kb-kvm-test-logs-31860267245` shows the
  endpoint returned HTTP 200, the guest/domain/routes/firewalls were healthy,
  and the source remained inside the delegated `/64`, but source selection used
  SLAAC EUI-64 `2001:db8:200:0:5054:ff:fe12:3010` instead of configured
  `2001:db8:200::10`. Every other KVM example passed. `git diff --quiet`
  confirms no KVM page, fixture, or test changed between `d85cadc` and
  `ccd7942`; the same suite passed locally and on the prior head. This is a
  diagnosed pre-existing address-selection race, not a current-change failure.
  Rerun only the failed KVM job after the still-running Guix job completes.
- Exact-head managed CI completed the Guix job successfully in 58m22s. This
  independently covered the full managed article path after the final SSH
  policy assertion fix; no Guix failure artifact was produced. The already
  green GRE job completed in 4m16s. Only the diagnosed KVM job was rerun with
  `gh run rerun 31860267245 --job 94952329296`; the expensive Guix and GRE jobs
  were not repeated.
- A fresh detached integration worktree at
  `worktrees/2026-08-14-kb-updates/vpsfree-kb-contracts-integration` was created
  from unchanged `origin/master` (`d85cadc`) and fast-forwarded locally to
  reviewed head `ccd7942`. Its strict `nix develop --command bin/check` passes:
  all documentation/article/annotation validators, Ruby suites with 8/50,
  9/20, and 16/46 runs/assertions, and the complete 120-image inventory are
  green. Master has not yet been pushed while the targeted KVM rerun is active.
- Immediately before staging preparation, all five retirement candidates were
  fetched read-only from production and still matched the captured source
  hashes exactly: `navody:server:nginx` (`e1812d2`),
  `navody:distribuce:nixos:nginx` (`ec21be9`),
  `navody:distribuce:nixos:zaciname` (`2ae7acf`),
  `navody:server:openshift_centos` (`b9e83ba`), and
  `navody:server:wireguard:openwrt` (`b9ad1c2`). Their only remaining obsolete
  link references are inside pages in this same retirement set; the updated
  navigation no longer links them.
- Targeted KVM rerun job `94959109909` passed in 23m08s at the same exact head,
  confirming the earlier delegated-IPv6 source mismatch was transient. The
  integration worktree was fetched again, `origin/master` was still `d85cadc`,
  and `master` was fast-forwarded over SSH to full head
  `ccd79422e3bfc269009aa1f237c621db1b4278f6` without a merge commit.
- Staging was reset from production after the contract push: 116 Czech pages,
  70 English pages, 224 shared media objects, and 58 language pairs were
  mirrored. Authenticated `aither` identities and exact-target ACLs were
  checked for all 25 page writes, 2 media uploads, and 5 deletes; every ACL was
  255 and the retirement hashes still matched after the reset.
- The Czech schema-3 manifest staged and verified 13 pages plus one media
  object; the English manifest staged and verified 12 pages plus one media
  object. Both manifests were verified again after both languages existed.
  The five obsolete Czech pages were then deleted from staging with descriptive
  localized summaries and explicitly verified absent. Both release manifests
  still verify after those removals.
- All 25 changed staging pages returned rendered DokuWiki content. The two new
  SSH images were fetched from the rendered media paths and matched hashes
  `6f1c1131...a652` (Czech) and `62bcf15f...db7c` (English). Both SSH pages
  render the existing address image and the new host-key image. Guix and GRE in
  both languages render reciprocal translations and the managed-source toolbar
  pointing to the exact file on contract `master`; all five old Docker, Snap,
  and NixOS Mailserver handles contain the intended canonical link. The English
  home renders the descriptive Postfix label, and neither home source retains
  any of the five retired IDs.
- Staging remains claimed and running for this initiative with no pending
  promotion marker. Production has not been written. Duplicate exact-head
  GitHub runs created by the `master` fast-forward are being monitored:
  Check `31863911564` and managed runtime `31863911628`.
- Exact-head master Check run `31863911564` passed. Master managed runtime run
  `31863911628` also passed completely: discovery, GRE, KVM, and Guix are all
  green; the duplicate Guix job completed in 46m30s. Both `master` and the
  retained local/remote feature branch point to
  `ccd79422e3bfc269009aa1f237c621db1b4278f6`.
- The clean detached integration worktree and clean feature worktree were
  removed after master CI passed. The temporary pre-review history backup ref
  `tmp/kb-followup-pre-review-split` was deleted; the feature branch itself was
  intentionally retained locally and remotely. Staging remains claimed for
  user review, and production remains untouched.

## Second review follow-up progress

- User review requested smaller SSH wording fixes, removal of historical
  workaround prose, `/32` playground examples for GRE and WireGuard, clearer
  trusted-network scope for GRE, a Guix wording/link correction, and a managed
  firewall article with simple iptables and nftables examples.
- The user selected runtime coverage for every documented firewall path:
  iptables, native nftables, UFW, firewalld, and NixOS.
- The verified session remains `2026-08-14-kb-updates`. The contract feature
  worktree was recreated at `ccd79422e3bfc269009aa1f237c621db1b4278f6`,
  exactly matching both retained feature-branch and `origin/master` heads.
- Guix deployment coverage was rechecked before editing: the existing runtime
  test creates a second Guix VPS, renders its real host key into the exact
  fixture, deploys it, restarts it, and verifies generation, hostname, signing
  authorization, and key-only SSH.
- Production remains untouched and staging stays claimed by this initiative.
- Workspace commit `c23a4f8` adds the current-state KB authoring rule while
  preserving the unrelated pre-existing `AGENTS.md` session-ownership edit in
  the shared working tree; it was pushed linearly to workspace `master`.
- Contract commits `bfc5a07`, `cd898ab`, and `142aad2` respectively add the
  same repository-local policy, refine Guix wording without changing its
  fixture, and scope GRE to the vpsFree internal network with deterministic
  test-address substitution. The GRE and Guix changes remain independently
  reviewable.
- Contract commit `521e4ef` manages the bilingual firewall article and adds
  five independent runtime scripts for Debian iptables, Debian nftables,
  Ubuntu UFW, Fedora firewalld, and NixOS. All paths use exact registered
  samples and check dual-stack allowed/blocked ports, IPv4 and IPv6 established
  traffic, outbound traffic, and restart persistence. UFW verifies IPv6 before
  activation, and the NixOS test activation is kept separate from the later
  persistent switch.
- Contract commit `d74ee70` separately inventories reciprocal SSH and firewall
  console/start-menu recovery references which are not direct vpsAdmin WebUI
  actions. The SSH and firewall prose distinguishes live-system recovery from
  the start-menu Run shell, where systemd is not running.
- `nix develop --command bin/check` passes at
  `d74ee707f6e71c2229aae8b91adf84307b162103`: 4 managed articles, 8 pages,
  12 tests, 19 executable samples, all Ruby suites, and all 120 screenshot
  variants are valid. The candidate-aware navigation check also passes.
- Final second-feedback candidates were built from production snapshot
  `kb-sources-followup`, managed reconciliation base
  `5bf06beccdd29c333f04bb044a7610cee5ccda3d`, and exact contract head
  `d74ee707f6e71c2229aae8b91adf84307b162103`. Directory
  `kb-candidates-second-feedback-reviewed` contains 25 changed pages and 2
  media objects; `kb-release-second-feedback-reviewed-cs.yml` contains 13
  Czech pages and one media object, while the reciprocal English manifest
  contains 12 pages and one media object. Production remains untouched.
- The mandatory fresh-context review completed at exact head `d74ee70` with no
  Blocking, Important, or Advisory findings. The reviewer independently passed
  the full contract check, candidate-aware navigation validation, manifest
  SHA-256 validation, exact 25-page/2-media union, clean-worktree check, and
  `git diff --check`. The only residual gaps are the long firewall/GRE VM tests
  and staging verification, which are intentionally performed after review.
- Long firewall runs exposed only test-scaffolding defects, not article-rule
  defects: detached clients were reaped, pre-firewall connections had no
  conntrack state, coreutils timeout status 124 was classified as a runner
  timeout, the NixOS listener used `/bin/cat`, and its flake-only template
  required the live hostname and flake-aware evaluation. Commit `205e429`
  corrects these conditions while retaining the exact registered article
  samples. The four non-NixOS paths then passed in one fresh serial run:
  iptables 164.25 seconds, nftables 141.05 seconds, UFW 142.03 seconds, and
  firewalld 152.66 seconds. A final fresh NixOS-only run passed in 450.15
  seconds, including exact `nixos-rebuild test` and `switch`, held IPv4/IPv6
  flows, fresh blocked/allowed connections, outbound traffic, and restart.
- The changed `kb/gre#tunnel` runtime passed fresh in 430.78 seconds: all three
  transient, persistent ifupdown, and both-container restart examples passed.
  The full quick contract suite also passes after the runtime corrections.
- Final artifacts were rebuilt again at exact head
  `205e429f3e9c34403979d03e0633493cd440e6e2` under
  `kb-candidates-second-feedback-runtime-reviewed`, with reciprocal manifests
  `kb-release-second-feedback-runtime-reviewed-{cs,en}.yml`. Candidate-aware
  navigation validation passes; the manifests still contain 13 Czech and 12
  English pages plus one media object per language.
- The exact-head follow-up review found that UFW's no-flush activation could
  leave the test's temporary established-connection rules in place. Amended
  runtime-test commit `800af9c802171d730ad22c791e65651b4e70a012`
  explicitly deletes both temporary rules before applying the exact UFW
  fixture and fails if either IPv4 or IPv6 rule remains. A fresh isolated
  `kb/firewall#ufw` run passed: its example took 182.53 seconds, the script
  445.91 seconds, and the complete test 466.04 seconds.
- The full quick contract suite passes at `800af9c`: 4 managed articles, 8
  pages, 12 tests, 19 executable samples, all Ruby suites, and all 120
  screenshot variants. Final exact-head artifacts are in
  `kb-candidates-second-feedback-final-800af9c`, with manifests
  `kb-release-second-feedback-final-800af9c-{cs,en}.yml`; they contain 25
  changed pages and 2 media objects, split into 13 Czech pages plus one media
  object and 12 English pages plus one media object. Candidate-aware
  annotation validation passes with 82 bindings and 9 explicit exceptions.
- The fresh-context mandatory review is complete at exact head `800af9c` with
  no Blocking, Important, or Advisory findings. The reviewer independently
  passed the focused diff review, full quick suite, candidate-aware annotation
  validation, manifest hashes, base/head pins, and the exact 25-page/2-media
  union. The change is clear to push, integrate, and stage; pushed-head CI and
  staging verification remain pending.
- Feature head `800af9c` was pushed to
  `origin/2026-08-14-kb-updates`. Exact-head GitHub Actions passed: `Check`
  run `31881236898` completed in 5m49s and managed runtime run `31881236886`
  completed successfully. Its jobs passed GRE in 3m4s, firewall in 15m49s,
  KVM in 22m46s, and Guix in 30m45s. No reruns or superseded runs were needed.
- A fresh detached integration worktree was created from fetched
  `origin/master` at `ccd7942`, fast-forwarded to `800af9c`, and passed the full
  quick suite. `origin/master` was fetched and confirmed unchanged immediately
  before the SSH push; master then fast-forwarded to `800af9c` without a merge
  commit. The temporary integration worktree was removed and the feature branch
  was retained locally and remotely.
- Staging was reset from current production after integration: 116 Czech pages,
  70 English pages, 224 shared media objects, and 58 language pairs were
  mirrored. Both staging identities authenticate as `aither`; all 25 manifest
  page targets and five retirement targets have ACL 255, both new media targets
  were absent, and the retirement contents matched their recorded source
  hashes before writing.
- The final Czech manifest staged and verified 13 pages plus one media object;
  the English manifest staged and verified 12 pages plus one media object. The
  five obsolete Czech pages were deleted with target-specific Czech summaries
  and verified absent. Both manifests still verify after deletion.
- All 25 staged pages render over HTTP, both new SSH screenshots match their
  expected SHA-256 hashes, and the reciprocal Guix, GRE, and firewall pages
  show managed-source links to their exact contract files. SSH renders both
  vpsAdmin screenshots and the live-system/Run-shell recovery split. Staging
  source checks confirm the raw iptables/nftables sections, `čistý Debian`,
  playground `/32` addresses, trusted-network GRE scope, one-line WireGuard
  key command, corrected Guix wording/NixOS link, descriptive English Postfix
  label, and absence of obsolete notices and Docker/Snap workaround prose.
  Production remains untouched and staging remains claimed for user review.
- Duplicate workflows triggered by the master fast-forward were monitored.
  Master Check run `31882742782` is green. Managed runtime run `31882742774`
  passed GRE in 3m1s, firewall in 9m11s, and Guix in 34m43s, but its unchanged
  KVM job failed after 40m5s in the final delegated-IPv6 example. The uploaded
  diagnostics show the HTTP request succeeded, but Linux selected the guest's
  concurrently learned EUI-64 address
  `2001:db8:200:0:5054:ff:fe12:3010` instead of the expected static source
  `2001:db8:200::10`; the same exact KVM test and SHA passed on the feature
  branch in 22m46s. This is an unrelated, nondeterministic IPv6 source-address
  selection issue in the pre-existing KVM test, not a failure in the changed
  KB articles. After this log and artifact investigation, only the failed KVM
  job was rerun; it passed in 24m23s and returned the complete master managed
  workflow to green. No CI runs remain pending.

## Third review follow-up progress

- User feedback requests annotated low-level firewall examples, explicit
  resulting-policy descriptions, removal of test-only apt environment settings
  from reader commands, refined GRE and Snap wording, and a bilingual redesign
  of the new-members landing page.
- The verified session is still `2026-08-14-kb-updates`. The contract worktree
  starts clean at integrated and pushed head
  `800af9c802171d730ad22c791e65651b4e70a012`.
- Production remains untouched. The staging container is still owned by this
  initiative and contains the now-superseded second-feedback release; it will
  be reset from production before staging the rebuilt complete release.
- The change remains documentation- and test-only. It has no API, protocol,
  database, persisted-state, or mixed-version deployment implications and can
  be rolled back by declining promotion or restoring the prior page revisions.
- Planned focused runtime coverage is Debian iptables, Debian nftables, Ubuntu
  UFW, and the KVM libvirt path affected by test-only environment injection.
  The mandatory fresh-context review will run after quick checks and commits,
  before those long tests.
- A fresh read-only production snapshot in `kb-sources-third-feedback` matches
  the previous snapshot byte-for-byte: 119 Czech and 77 English inventory
  entries, including the same ten expected-new canonical page IDs.
- Contract commits appended after `800af9c` are `8db995b` (firewall comments,
  policy descriptions, fixtures, and test-only apt environment), `95ba34b`
  (KVM reader/test environment separation), `6d36465` (managed-source policy
  checker), `3259856` (GRE wording), and `5498867` (new-member navigation
  allowlists, counts, and independent candidate inventory).
- The full quick suite passes cleanly at exact head
  `5498867e37bfbf571b765d090ef0e8fe241b9bb4`: 4 managed articles, 8 pages,
  12 runtime scripts, 19 exact samples, 4 managed-source policy tests with 10
  assertions, and all 120 screenshot variants. Candidate-aware annotation
  validation passes with 86 bindings and 9 explicit exceptions.
- The manual WebUI action audit found 14 annotated action blocks per language
  across the changed new-member, SSH, KVM, and Snap pages. They bind only to
  `vps.details.open`, `member.public-keys.add`, `member.public-keys.open`,
  `vps.features.open`, dataset create/edit/mount, and routable-address paths.
  Untagged discoveries in the new-member pages are read-only detail/address/
  traffic screenshot context or recovery delegated to the console guide;
  firewall exceptions likewise describe console/start-menu recovery rather
  than direct vpsAdmin WebUI actions. No direct action prose is unbound.
- Final pre-review candidates are in `kb-candidates-third-feedback-5498867`.
  They contain 29 changed pages and 2 existing media objects: 15 Czech pages
  plus one media object and 14 English pages plus one media object. KVM is now
  included as a managed replacement. Reciprocal manifests are
  `kb-release-third-feedback-5498867-{cs,en}.yml`; their candidate/media hashes
  and exact contract head were verified locally.
- The mandatory fresh-context review at `5498867` found three Blocking items
  and no Important or Advisory items: `8db995b` bundled firewall explanation
  with the reader/test apt environment split, UFW prose ignored its built-in
  control-traffic allowances, and NixOS prose ignored built-in ICMP/DHCPv6
  allowances and described default drops as rejection. All other candidate,
  annotation, manifest, content, and commit checks passed. The decision is to
  fix every Blocking item before runtime tests: rewrite the unpushed series
  into independently valid explanation and environment commits, correct the
  two policies and claims in the explanation commit, then rerun quick checks,
  candidate generation, and the review closure at the rewritten head.
- The unpublished follow-up series was rewritten on top of `800af9c` to resolve
  all three review findings. The replacement commits are `d7b5954` (firewall
  comments and precise resulting-policy explanations), `1c12b09` (firewall
  reader/test apt environment separation), `83f8259` (the equivalent KVM
  separation), `cacf6e0` (managed-source policy enforcement), `9838a70` (GRE
  wording), and `9019930` (new-member navigation bindings and inventory).
  UFW now distinguishes its built-in loopback/control rules from its default
  policy, while NixOS likewise documents built-in control traffic and default
  drops without claiming that every unmatched packet is rejected.
- The full quick suite passes at rewritten exact head
  `901993010e397232b181022fa9540cd8905f5387`: 40 navigation controls, 32
  target paths, 33 capture concepts, 86 bindings with 9 explicit exceptions,
  4 managed articles, 8 pages, 12 runtime scripts, 19 exact samples, the
  managed-source policy validator, all unit suites, and 120 screenshot
  variants. The intermediate split commits `d7b5954` and `1c12b09` also pass
  the full quick suite independently. The final managed pages and fixtures
  contain no `DEBIAN_FRONTEND` assignment.
- Replacement candidates in `kb-candidates-third-feedback-9019930` contain 29
  changed pages and 2 media objects. Candidate-aware annotation validation
  passes with 86 bindings and 9 exceptions. New reciprocal manifests
  `kb-release-third-feedback-9019930-{cs,en}.yml` contain 15 Czech pages plus
  one media object and 14 English pages plus one media object; all artifact,
  managed-source, registry, and exact-head hashes were verified locally, and
  the combined manifests contain 29 unique page targets.
- Focused closure review found one remaining UFW precision issue: existing
  user rules survive activation, so defaults are fallbacks rather than the
  complete policy. The unpublished series was rewritten again. Commit
  `7940470` now documents retained user and built-in rules and limits the
  defaults to otherwise-unmatched traffic; its intermediate reader-visible
  version passed the full quick suite with its own fingerprints. Commit
  `ad4f663` then performs the firewall reader/test apt-environment separation
  and updates the final fingerprints. The remaining commits replayed as
  `807ed3d`, `d41b25e`, `c3d7926`, and `b68dddb`.
- The final full quick suite passes at exact head
  `b68dddbe4d2dcb7410a87af6920aab8d71b0913d`. Fresh candidates are in
  `kb-candidates-third-feedback-b68dddb-final`; reciprocal manifests are
  `kb-release-third-feedback-b68dddb-{cs,en}.yml`. Candidate-aware annotation
  validation and all registry, source, artifact, media, and exact-head hashes
  pass; the manifests contain 29 unique pages and 2 media objects.
- The same standalone reviewer completed a narrow independent closure review
  at `b68dddb` with no Blocking, Important, or Advisory findings and explicitly
  cleared the planned long runtime tests. The review independently validated
  the corrected UFW semantics, all five firewall result policies, commit split,
  196 source/candidate pages, the 29-page/two-media union, annotation inventory,
  hashes, and clean exact-head worktree. Residual gates are the four focused
  runtime paths, pushed-head CI, and staging verification.
- All four focused exact-head runtime tests pass serially at `b68dddb` without
  retries: Debian iptables in 409.67 seconds, native nftables in 348.90 seconds,
  Ubuntu UFW in 397.83 seconds, and Debian KVM/libvirt in 945.45 seconds. The
  firewall paths exercised IPv4/IPv6 policy, established-flow handling, and
  restart persistence. KVM verified installation, the system libvirt
  connection, and reported KVM support with the harness-only package
  environment injection.
- Feature-branch CI at `b68dddb` passed without retries. Check run
  `31892965767` completed in 6m04s. Managed runtime run `31892965671` completed
  in 37m35s: GRE passed in 3m04s, firewall in 9m21s after waiting for a runner,
  Guix in 30m07s, and KVM in 37m24s. All contract-discovery, preview,
  evaluation, summary, and cleanup steps were green; no failure artifacts were
  produced.
- Per user feedback, the completed runtime workflow is the baseline for a
  focused efficiency refactor. Commit `616ca68` removes the per-article matrix
  and its Ruby discovery helper. A single self-hosted job now previews all 12
  repository scripts and invokes the test runner once with `--jobs auto`, while
  preserving contract checks, isolated state, failure-log upload, result
  evaluation, summaries, and cleanup. Article tags/labels remain contract and
  local-selection metadata.
- Upstream action refs were verified before editing the workflow. The latest
  checkout release is v7.0.1, so the existing `actions/checkout@v7` major ref is
  current. The four pinned vpsAdminOS test actions at `67fcc173...` have no
  action-directory changes relative to current staging `93724f04...`, so the
  reviewed immutable pin remains current in content.
- The workflow refactor passes the full quick suite, actionlint 1.7.12, an
  unfiltered test inventory check for exactly 12 scripts, and `git diff
  --check`. A fresh standalone mandatory review and the new pushed-head one-job
  CI run remain before integration.
- The fresh standalone workflow review found no Blocking issue, one Important
  precision issue, and one Advisory documentation mismatch. The test runner
  enforces memory, shared-memory, and CPU reservations within one invocation;
  it records machine counts but has no separate VM-count capacity, and separate
  runner processes do not share a resource pool. The plan and commit rationale
  were corrected to state the actual guarantees. The obsolete README claim
  that article suites use separate jobs was replaced with the one-job design.
  The amended head is `616ca689209396df1c3d20acbb8124da258f5492`.
- The same standalone reviewer completed the focused closure re-check with no
  Blocking, Important, or Advisory findings and cleared `616ca68` for the
  pushed-head one-job integration run. Independent actionlint, diff, clean-tree,
  and unfiltered 12-script inventory checks passed.
- Exact-head quick run `31895408358` passed after the workflow refactor. The
  first unified runtime run `31895408359` correctly discovered all 12 scripts,
  started all four test groups in one process with aggregate reservations of
  36 GiB memory, 36 GiB shared memory, and 20 CPUs, and preserved diagnostics,
  evaluation, summaries, and cleanup. GRE, firewall, Guix, and 11 of 12 scripts
  passed. `kb/kvm#networking` reproduced the known delegated-IPv6 source flake:
  HTTP to `2001:db8:200::10` succeeded, but the guest reported outbound source
  `2001:db8:200:0:5054:ff:fe12:3010` after accepting an RA and creating an
  EUI-64 address. The uploaded artifact `kb-test-logs-31895408359` confirms the
  routes, firewall, domain, and HTTP service were healthy. No blind rerun was
  attempted.
- Focused commit `fd7d1e5` fixes the synthetic static-network fixture by
  disabling RA and SLAAC before raising `eth0` and binding the default IPv6
  route to the configured source. It changes no article or live member system.
  Nix parsing, the full quick suite, and diff checks pass. A fresh mandatory
  review and focused `kb/kvm#networking` run remain before pushing and rerunning
  the unified workflow.
- A fresh standalone mandatory review of `fd7d1e5` found no Blocking,
  Important, or Advisory issues and cleared the focused networking path. It
  confirmed the sysctls run after `eth0` exists but before link-up, address/DAD
  precede the source-pinned route, NAT/routed/public6 variants retain their
  intended sources, and the existing outbound assertion still observes the
  regression. The residual gap is the not-yet-run VM path and an unused
  `public6` helper branch.
- Exact-head focused runtime `kb/kvm#networking` passed without retries in
  1995.75 seconds at `fd7d1e5`. All nine examples passed, including dual-stack
  NAT, UDP, invalid-record rollback, lifecycle/idempotence, routed-prefix
  placement, stale-route rejection, IPv4 source preservation, and the formerly
  flaky delegated-IPv6 source assertion (which completed in 6.34 seconds).
  Test teardown also completed successfully.
- The reviewed fix was pushed to the feature branch. Exact-head Check run
  `31899436914` passed. Unified managed-runtime run `31899436920` passed on its
  first attempt in 30m02s of test-runner time: one process scheduled all 12
  scripts across four test groups with aggregate reservations of 36 GiB memory,
  36 GiB shared memory, and 20 CPUs. All groups passed, including the corrected
  KVM networking path; result evaluation, summary generation, and cleanup were
  green.
  Fresh candidates in `kb-candidates-third-feedback-fd7d1e5-final` contain 29
  changed pages and two media objects and pin managed-contract head `fd7d1e5`.
  Candidate-aware annotation validation passes with 86 bindings and nine
  exceptions. Reciprocal manifests
  `kb-release-third-feedback-fd7d1e5-{cs,en}.yml` contain 15 Czech pages plus
  one media object and 14 English pages plus one media object; their union is
  29 unique page targets and two unique media targets.
- The successful workflow still made a redundant `test-runner.sh ls` preview
  call before the complete test run. Per user feedback, the final workflow
  removes that step and renames the repository check so there is exactly one
  `test-runner.sh` invocation: the unfiltered full-suite `test` call.
- Focused commit `efdeb26` contains that workflow cleanup. Actionlint 1.7.12,
  the full quick suite, and `git diff --check` pass. A fresh standalone
  mandatory review found no Blocking, Important, or Advisory issues and
  cleared the commit for push. The reviewer independently confirmed that the
  sole remaining runner call is unfiltered, uses `--jobs auto`, prints its own
  selected inventory, and retains repository checks, state handling,
  diagnostics, evaluation, summaries, and cleanup. Exact-head GitHub Actions
  remains the residual gate.
- Final candidates in `kb-candidates-third-feedback-efdeb26-final` and
  reciprocal manifests `kb-release-third-feedback-efdeb26-{cs,en}.yml` pin
  exact managed-contract head `efdeb26`. Annotation validation passes with 86
  bindings and nine exceptions. The 29 page hashes and two media records are
  byte-for-byte identical to the previously reviewed `fd7d1e5` bundle; only
  contract provenance advanced. The combined manifests still contain 29
  unique page targets and two unique media targets.
- Final exact-head Check run `31901188599` passes at `efdeb26`. Unified runtime
  run `31901188550` also passed on its first attempt. Its log contains exactly
  one `test-runner.sh` invocation and no preview/discovery step; all 12 scripts
  across four parallel groups passed in 2607.23 seconds. Result evaluation,
  summary generation, and state cleanup succeeded.
- A fresh detached integration worktree was created from current
  `origin/master` at `800af9c`, fast-forwarded to `efdeb26`, and passed the full
  quick suite. `origin/master` was fetched and rechecked immediately before the
  fast-forward push. Master now points to `efdeb26`; the temporary integration
  worktree was removed and the feature branch was retained.
- Post-merge Check run `31903358495` passes. Managed-runtime run `31903358478`
  ran all 12 scripts; GRE, all five firewall scripts, and all five KVM scripts
  passed, including KVM networking. Guix reconfiguration and reboot passed,
  but deployment failed after `ci.guix.gnu.org` returned repeated 504 Gateway
  Time-outs for the `module-import-compiled` substitute. The uploaded artifact
  `kb-test-logs-31903358478` shows Guix explicitly classified this as a
  networking/substitute failure; the subsequent boot assertion failed only
  because deployment had not completed. This is external to the committed
  change, and the same exact head already passed the complete 12-script suite
  in feature run `31901188550`. A failed-job rerun is justified after this log
  and artifact inspection.
- Failed-job rerun attempt 2 of `31903358478` is in progress. Because the exact
  head already passed the full feature run and the post-merge failure is
  conclusively an external Guix substitute outage, staging preparation
  proceeded in parallel; production remained untouched.
- Staging was reset from production at `2026-08-15T20:03:25Z`, preserving this
  initiative's ownership and leaving no pre-existing pending release. Both
  staging identities are authenticated administrators. All 31 manifest
  page/media targets and all five retirement targets returned ACL 255 before
  their writes.
- The final Czech manifest staged and verified 15 pages plus one media object;
  the English manifest staged and verified 14 pages plus one media object. All
  14 reciprocal page pairs validate. The generic Nginx, old NixOS Nginx and
  getting-started, OpenShift on CentOS, and OpenWrt WireGuard pages were then
  deleted from Czech staging with target-specific Czech summaries; all five
  IDs are absent. These staging-only deletions are recoverable by another
  staging reset from production and intentionally leave no promotable pending
  manifest.
- Both manifests still verify after the retirements. All 29 changed pages
  return rendered DokuWiki content with their expected localized titles (the
  reciprocal navigation page has no article heading by design). The two
  rendered SSH host-key images match manifest SHA-256 hashes. Both Guix pages
  expose their localized GitHub source action without rendering the managed
  marker, and both SSH pages reference the localized host-key screenshot.

## New-member rendering follow-up progress

- User review found that DokuWiki splits the new-member page's SSH, management,
  and advanced lists around screenshots or wrapped continuation lines. The
  Czech title must remain `Informace pro nové členy`, login must be the first
  step, and the member/VPS screenshots must include the horizontal menu.
- The welcome mail templates confirm that the account message contains the
  vpsAdmin URL, case-sensitive login and temporary password, requires a password
  change at first login, and directs a member with a missing message to check
  spam and contact support with the application number.
- The existing `getting-started/members-list` and `getting-started/vps-list`
  captures crop only the content title and first table. Their stable media IDs
  will be retained while a focused capture helper adds `#nav .main` above that
  content for both Czech and English variants.
- The monthly-traffic screenshot will be removed from the landing page while
  its guide link remains. The reciprocal Docker lists will drop Red Hat
  Enterprise Linux and sort Alpine, Arch, Debian, Fedora, NixOS, and Ubuntu
  alphabetically.
- Production remains untouched. Staging is up, still owned by
  `2026-08-14-kb-updates`, and has no pending release record after the prior
  staged retirements.
- The default capture bridge address `172.16.106.53` is occupied by another
  development frontend. The dedicated `kb-new-members-menu` screenshot cluster
  therefore uses local networking; the other session is not modified.
- The first focused capture accepted no output because `#nav .main` has no own
  layout height around its floated links and Playwright correctly considered
  that element hidden. The menu-aware crop now targets the visible clearfix
  container `#nav` while its content box remains bounded by the menu labels.
- All four focused captures wrote complete checkpoint results. The final
  English Members capture then remained in Playwright browser shutdown for
  more than five minutes after `session.finish()` had written the image and
  result file. It was interrupted only after verifying the complete result;
  `bin/validate --update` will accept and verify that result separately.
- Visual inspection confirmed that the full localized menu and active tab are
  visible, but the wider rectangle also exposed a sliver of the unrelated
  right sidebar. The focused helper now hides only `#aside` before capturing so
  the menu, page title, and list table remain the sole documentation context.
- Commit `f7158e4` adds the bounded menu-aware capture helper, applies it to the
  localized Members and VPS-list concepts, refreshes their registry metadata,
  and commits the four visually reviewed PNG variants. Strict capture
  validation passes with 60 concepts, 120 variants, and 120 present images.
- Commit `63344e0` adds explicit login and Members controls and paths, binds the
  new-member actions in both languages, and refreshes the navigation inventory.
  The final exact-head quick suite passes with 42 controls, 34 paths, 90
  annotation bindings, nine exceptions, and all article and Ruby checks green.
- The revised Czech and English landing pages use six images each, keep all
  image blocks outside lists, present password and SSH-key login as separate
  subsections, and keep management, beginner, and advanced links as simple
  one-line list items. The Czech title remains `Informace pro nové členy`.
  Reciprocal Docker pages no longer mention RHEL and list Alpine, Arch Linux,
  Debian, Fedora, NixOS, and Ubuntu in alphabetical order.
- Final candidates are in `kb-candidates-new-member-final-63344e0`. The Czech
  and English manifests `kb-release-new-member-63344e0-{cs,en}.yml` pin exact
  managed-contract head `63344e06f98f71e9df697fdc77d9ce3346c6dc41`, contain
  15 and 14 page writes respectively, and carry three localized media objects
  each. Candidate-aware annotation and manifest/hash validation pass.
- Staging remains up and owned by this initiative with no pending release.
  Both staging identities are authenticated administrators, the new-member and
  Docker targets return ACL 255, and the five prior retirement targets remain
  absent. A fresh standalone mandatory review of the final follow-up is in
  progress before the branch is pushed or the manifests are staged.
- The fresh mandatory review found two Blocking annotation gaps in the first
  candidate: an optional automatic-key setting and an imperative console
  recovery sentence had escaped semantic tags during the list rewrite. The
  beginner page now omits the optional setting and delegates recovery neutrally
  to the dedicated console guide. No navigation contract change was needed;
  the regenerated discovery inventory is byte-for-byte unchanged.
- Focused reviewer closure found no remaining Blocking, Important, or Advisory
  findings. It independently confirmed that drafts and reviewed candidates are
  byte-identical, only the two onboarding pages changed from the initially
  reviewed bundle, all page/media hashes match, candidate-aware annotation
  validation passes, and the two-commit repository series remains clean.
  Residual risk is limited to rendering and media delivery on staging.
- The cleared exact release artifacts are
  `kb-candidates-new-member-reviewed-63344e0` and
  `kb-release-new-member-reviewed-63344e0-{cs,en}.yml`.
- The first staging preflight correctly stopped before writing because the four
  existing Members/VPS-list media objects were marked create-only. Read-only
  production fetches established their SHA-256 baselines; the plan now marks
  those four objects as guarded updates while the absent host-key images remain
  create-only. The same standalone reviewer inspected the correction and found
  no Blocking, Important, or Advisory issue.
- Final staging artifacts are `kb-candidates-new-member-staging-63344e0` and
  `kb-release-new-member-staging-63344e0-{cs,en}.yml`. Both manifests pin exact
  head `63344e06f98f71e9df697fdc77d9ce3346c6dc41`; candidate-aware annotation,
  file/hash, source-guard, and structure checks pass.
- Staging still contained the previous onboarding and Docker drafts. Release
  guards refused to skip these intermediate states. The two onboarding pages
  were restored to their recorded production contents and the two create-only
  canonical Docker pages were removed after fresh identity/ACL checks. No other
  staged page or media object was changed by this baseline restoration.
- The final Czech manifest then staged and verified 15 pages plus three media
  objects. The English manifest staged and verified 14 pages plus three media
  objects, and the Czech manifest still verifies afterward. All 14 reciprocal
  language pairs warm and validate; the five retired Czech page IDs remain
  absent.
- Browser verification of both onboarding pages confirms the exact localized
  titles, separate password/key subsections, uninterrupted 4/5/5-item lists,
  zero images nested in list items, six loaded images per page, and the expected
  908x145 Czech / 940x145 English menu-aware screenshot dimensions. Full-page
  visual inspection shows clean rendering. Both Docker pages render the six
  requested distributions alphabetically with no RHEL mention, and all 29
  staged page URLs return HTTP 200.
- Feature head `63344e0` is pushed. Exact-head GitHub Check run `31912248389`
  passed; unified managed-runtime run `31912248387` is in progress.
- Exact-head unified managed-runtime run `31912248387` passed without retries
  in 40m47s. One unfiltered test-runner invocation ran the complete 12-script
  inventory in parallel; test evaluation, summary generation, and cleanup were
  green. No failure artifact was produced.
- A fresh detached integration worktree was created from unchanged
  `origin/master` at `efdeb26`, fast-forwarded to `63344e0`, and passed the full
  `nix develop --command bin/check --allow-missing` suite. Origin was fetched
  and rechecked immediately before the fast-forward push. `origin/master` and
  the retained feature branch now both point to
  `63344e06f98f71e9df697fdc77d9ce3346c6dc41`; the temporary worktree was
  removed.
- Both staging manifests still verify after integration. Staging remains up and
  owned by this initiative with the English manifest recorded as the pending
  release; production remains untouched. GitHub started duplicate post-merge
  checks for the identical master SHA. The already-completed exact-SHA feature
  runs provide the required integration evidence, so those duplicate current-
  head runs were not cancelled.

## Humanized bilingual writing follow-up progress

- The user selected workspace-only skill copies, a vpsFree Czech adaptation,
  and instruction/review enforcement without an automated Humanizer checker.
- The reviewed upstream sources are English Humanizer v2.9.1 at
  `523374dee72d67c7b2b5f858ea0094ffda49c3ac` and Czech Humanizer at
  `bda1f7ae7129142c476187966cfb59b2a32c0013`, both under the MIT license.
- The current release scope is the same 29 changed pages. Production remains
  untouched; staging is still owned by this initiative and will be reset only
  after the revised exact-head manifests pass review.
- Workspace commit `3a7fe46` pins the reviewed English Humanizer and Czech
  adaptation, adds the vpsFree writing wrapper, and requires it for user-facing
  text. It is pushed on the shared workspace `master`; an unrelated pre-existing
  `AGENTS.md` edit remains unstaged and untouched.
- Contract commits `90d13a9`, `b233082`, and `f46064d` add the repository
  writing instruction, derive localized display comments from one tested
  command stream, and polish the managed firewall/KVM prose. The contract
  worktree is clean at `f46064d`. The full quick suite passes with 4 managed
  articles, 8 pages, 12 runtime tests, 19 samples, 25 article-contract runs/73
  assertions, and the complete 120-image inventory.
- Every changed candidate page was reviewed directly with the pinned
  language-appropriate Humanizer profile. The revised new-member pages retain
  simple uninterrupted lists and external image blocks, keep the Czech title
  `Informace pro nové členy`, and explain the one-week VPS trial before
  payment. Czech managed examples now show Czech comments while their
  executable lines remain derived from the same hashed fixtures as English.
- Exact release candidates are in `kb-candidates-humanized-f46064d`; reciprocal
  manifests are `kb-release-humanized-f46064d-{cs,en}.yml`. They contain the
  same 29 unique page writes, 8 managed pages, and 6 unique media writes as the
  reviewed scope. Candidate-aware navigation validation and all manifest file
  hashes pass. The managed reconciliation still uses production base
  `5bf06beccdd29c333f04bb044a7610cee5ccda3d` and pins head `f46064d`.
- The standalone mandatory review of that preliminary bundle found three
  Blocking issues: polished action paragraphs were missing semantic WebUI
  bindings or an explicit delegation, the candidate-aware navigation inventory
  was stale, and the two GRE connectivity commands were not derived from tested
  fixtures. It found no Important or Advisory issues.
- Contract commits `afdc461`, `501af67`, `49bd55c`, and `5bdf3cc` fix the
  review findings. Navigation discovery now treats semantic tags as
  authoritative; SSH automatic key deployment is bound to its existing path;
  SSH, firewall, and Guix verification/recovery actions delegate to the
  dedicated guides; the complete 90-binding/nine-exception inventory is
  refreshed; and both GRE ping commands are hashed, localized display variants
  that the GRE runtime suite executes.
- The final exact contract head is
  `5bdf3cc4d977a656b69eceadccc74876a9c8b4ea`. Candidates are in
  `kb-candidates-humanized-5bdf3cc`; manifests are
  `kb-release-humanized-5bdf3cc-{cs,en}.yml`. The bundle contains 29 unique
  page writes, eight managed pages, and six unique media writes. All manifest
  hashes and the managed head pin match. Ordered links, media, and semantic path
  targets are unchanged from the prior reviewed release except for the reviewed
  Guix console-link delegation.
- Exact-head `nix develop --command bin/check --allow-missing` passes with 42
  controls, 34 paths, 90 bindings, nine exceptions, four articles, eight pages,
  12 runtime tests, 21 executable samples, four green Ruby suites, and all 120
  screenshot variants. Focused release checks confirm the onboarding pages
  retain six non-list images and uninterrupted 4/5/5 lists; Docker lists six
  supported distributions alphabetically without RHEL; and none of the changed
  pages contains reader-visible `DEBIAN_FRONTEND` or sampled Czech formal/plural
  address. Reviewer closure on this exact head is in progress; the unified
  integration runtime has not started yet.
- Reviewer closure confirmed that all content, contract, and release-safety
  findings were resolved. Its only remaining Important finding was that three
  unpublished commit bodies exceeded the workspace's 80-character message
  limit. The feature history was rewritten to wrap those bodies without
  changing any tree content; all seven commit messages now satisfy the limit.
- The final rewritten contract head is
  `45af9354b72bc1eb67fddec7c87d0e378b4abba3`. Exact candidates are in
  `kb-candidates-humanized-45af935` and manifests are
  `kb-release-humanized-45af935-{cs,en}.yml`. All 29 page files and six media
  files are byte-identical to the reviewer-cleared bundle; only the pinned
  contract commit changed. Candidate-aware navigation, the full quick suite,
  manifest hashes, managed-page hashes, and the 80-character history audit all
  pass on the rewritten head. The review is therefore closed with no remaining
  findings before the unified integration runtime.
- Feature head `45af935` is pushed. Exact-head GitHub Check run `31958339421`
  passed in 5m42s. Unified managed-runtime run `31958339296` is in progress and
  uses one unfiltered test-runner invocation for all 12 scripts with parallel
  jobs; there is no discovery phase.
- At the user's request, a separate fresh-context, read-only security and
  provenance audit of the pinned English Humanizer, Czech adaptation, and
  vpsFree wrapper is running alongside CI. It covers every imported file,
  executable behavior, hidden or conflicting instructions, obfuscation,
  exfiltration risk, upstream/version/license claims, and Czech scope fidelity.
- The independent Humanizer audit completed without any evidence of malicious
  or hidden behavior. All 22 files are ordinary text; there are no symlinks,
  binaries, secret/environment reads, runtime network or shell actions,
  obfuscation, prompt-priority overrides, exfiltration, or destructive
  instructions. English files match upstream v2.9.1 commit `523374d`; Czech
  files match upstream commit `bda1f7a`; recorded hashes are exact.
- The audit found three non-malicious upstream issues: the Czech fork replaces
  rather than preserves the English MIT copyright name, creating a license-
  notice compliance risk; one Czech example removes attribution despite the
  skill's no-meaning-change promise; and its one-dash limit is an editorial
  preference rather than an IJP rule. The vpsFree wrapper already requires fact
  and attribution preservation and protects legitimate Czech range/relation
  dashes. No imported source was changed during this read-only audit; any
  license-notice correction should be an explicit follow-up decision.
- Exact-head managed-runtime run `31958339296` passed without retries in
  37m57s. One unfiltered test-runner invocation ran all 12 scripts in parallel;
  repository validation, result evaluation, summary generation, and cleanup
  were green. No failure-log artifact was needed.
- A fresh detached integration worktree from unchanged `origin/master` at
  `63344e0` fast-forwarded to `45af935` and passed the full quick suite. Origin
  was fetched and rechecked immediately before the fast-forward push. Both
  `origin/master` and the retained feature branch now point to
  `45af9354b72bc1eb67fddec7c87d0e378b4abba3`; the temporary integration
  worktree was removed.
- Staging was reset from current production at `2026-08-16T17:01:25Z`, keeping
  this initiative's ownership. The exact `45af935` Czech manifest staged and
  verified 15 pages plus three media objects; the English manifest staged and
  verified 14 pages plus three media objects. Both manifests still verify
  together and warm all 14 reciprocal pairs.
- After exact ACL 255 checks, the generic Nginx, old NixOS Nginx and getting-
  started, OpenShift on CentOS, and OpenWrt WireGuard pages were deleted again
  from Czech staging with target-specific Czech summaries. All five IDs are
  absent. These direct staging retirements intentionally clear the promotable
  pending-release marker; production remains untouched.
- The durable Playwright check
  `work/2026-08-14-kb-updates/verify-humanized-staging.cjs` verifies all 29
  rendered IDs and HTTP responses, 14 reciprocal pairs in both directions,
  six loaded non-list images on each onboarding page, their 908x145 Czech and
  940x145 English menu captures, uninterrupted 4/5/5 link lists, exact titles
  and first-login step, the one-week trial, Docker's alphabetical six-distro
  list without RHEL, all eight managed GitHub source actions, and localized
  firewall comments. It passes. Full-page Czech and English screenshots were
  inspected visually and show clean layout, complete menu context, and no
  broken images or lists. Staging remains up and owned by this initiative.
- All 29 pretty-path staging URLs independently return HTTP 200. The staging
  service is HTTP-only on the internal review hosts; final review links use
  `http://kb-cs.aitherdev.int.vpsfree.cz` and
  `http://kb-en.aitherdev.int.vpsfree.cz`. Production has not been written.

## Locale-specific Humanizer packaging follow-up progress

- The user selected the clean names `$humanizer-en` and `$humanizer-cs`, with
  no old-name aliases, and chose lean runtime packages instead of keeping
  upstream repository support files.
- A fresh-context security and provenance audit found no malicious or hidden
  behavior in either import or the wrapper. It found no binaries, symlinks,
  shell or runtime network actions, secret access, obfuscation, exfiltration,
  destructive instructions, or prompt-priority overrides. The pinned upstream
  revisions and recorded hashes were accurate before local corrections.
- The audit's three substantive Czech findings are addressed: the local MIT
  notice now retains `Copyright (c) 2025 Siqi Chen`; attributed claims remain
  attributed unless the user approves a content change; and correct Czech en
  dashes are evaluated by function without a fixed count.
- Workspace commits `b29aebe`, `86f6ad2`, `b5f665d`, `23d6107`, and `9993bd0`
  separately rename the locale skills, reduce them to runtime files, preserve
  the original MIT notice, protect attributed claims, and correct Czech dash
  guidance. Their final tree is identical to the previously checked unpublished
  result; history was split for independent review.
- `quick_validate.py` passes for `$humanizer-en`, `$humanizer-cs`, and the
  stable vpsFree wrapper. YAML metadata, folder/frontmatter names, default
  prompts, provenance hashes, regular-file modes, absence of symlinks, file
  counts, stale-name scans, and `git diff --check` all pass.
- Three fresh agents exercised the English skill, Czech skill, and bilingual
  wrapper without editing files. They preserved commands, addresses, hashes,
  links, DokuWiki tags, and formatting; Czech correctly retained `9–17 h` and
  `Praha–Brno`, asked before changing vague attribution, and the wrapper
  reported an intentional cross-language factual discrepancy instead of
  silently normalizing it.
- The standalone review found no final-tree defect, but blocked the first
  three-commit history: two locale-name edits remained in the later Czech
  correction and that commit bundled three independent fixes. The rewritten
  five-commit series moves all naming into its first commit and gives licensing,
  attribution, and typography one focused commit each. Exact content and
  provenance hashes are maintained at every intermediate commit.
- No KB article, contract repository, staging page, or production page changed
  in this follow-up.
- Reviewer closure on exact head `9993bd03a69b49c25be592c72f726ac10cf5288b`
  found no Blocking, Important, or Advisory issues. It independently confirmed
  the focused five-commit split, matching intermediate hashes, valid package
  shape and modes, stale-name and diff checks, and the absence of non-skill,
  KB, contract, staging, or production changes. Residual risk is limited to
  prose behavior being probabilistic; the three fresh-agent runs are samples,
  not deterministic proof.
- The shared workspace remote was fetched immediately before publication and
  remained at the recorded base `3a7fe46`. `master` was fast-forwarded to
  `9993bd03a69b49c25be592c72f726ac10cf5288b` over SSH; local `HEAD` and
  `origin/master` now match. The top-level repository declares no GitHub Actions
  workflows. The unrelated pre-existing `AGENTS.md` edit remains unstaged and
  untouched.

## Production publication

- On 2026-08-16 the user explicitly approved production publication of the
  reviewed KB release. The active session and staging owner were both
  `2026-08-14-kb-updates`; both production API identities authenticated as the
  `aither` administrator.
- Before any production write, both staging manifests verified, every one of
  the five retirement pages matched its previously reviewed production
  SHA-256, and every retirement ACL was 255. The staging pending marker was
  empty because the reviewed direct staging deletes intentionally invalidated
  it.
- The exact Czech manifest `kb-release-humanized-45af935-cs.yml` was restaged,
  verified, and promoted with explicit production approval: 15 pages and three
  media objects. The exact English manifest
  `kb-release-humanized-45af935-en.yml` was then restaged, verified, and
  promoted: 14 pages and three media objects. Both production manifests verify
  byte-for-byte after publication.
- Five obsolete Czech pages were deleted with target-specific Czech revision
  summaries after a final hash and permission check:
  `navody:server:nginx`, `navody:distribuce:nixos:nginx`,
  `navody:distribuce:nixos:zaciname`, `navody:server:openshift_centos`, and
  `navody:server:wireguard:openwrt`. The API now reports all five IDs absent;
  their DokuWiki revision histories allow recovery if needed.
- The production browser suite verified all 29 rendered pages, 14 reciprocal
  pairs, six onboarding images and uninterrupted lists, the alphabetical
  six-distribution Docker sections without RHEL, eight managed-source actions,
  and localized firewall comments. The production home-language switch uses
  the configured pretty path `domů`; DokuWiki normalizes it to manifest page ID
  `domu`, and both addresses resolve to identical content.
- The first production browser invocation did not reach the KB because direct
  Node execution omitted the Nix Playwright wrapper's browser path. Supplying
  both the package's `NODE_PATH` and `PLAYWRIGHT_BROWSERS_PATH` launched the
  packaged Chromium. Workspace commit `0f22dab` records this setup in a durable
  cross-project note and is pushed to `origin/master`.
- Staging had no pending release after promotion. `bin/kb-stage release --yes`
  stopped the container and released ownership while retaining its data.
  Production publication is complete.

## Per-page release summaries follow-up

- The user accepted a schema-4 design with localized per-page summaries visible
  in staging history and first-class guarded page deletions. Existing production
  revision summaries will not be rewritten because DokuWiki cancels no-op page
  saves and the supported API cannot amend revision metadata independently.
- The active session and `VPSFREE_DEV_SESSION_SLUG` both resolve to
  `2026-08-14-kb-updates`. The existing contract worktree is clean at
  `45af935`; workspace `master` is at `0f22dab` and retains one unrelated,
  unstaged `AGENTS.md` edit that must not be committed with this work.
- Compatibility plan: schemas 1–3 and legacy `--summary` generation remain
  accepted for existing artifacts. New documented releases use a bilingual
  changes file and schema 4. Schema-2 cleanup manifests add per-page summaries
  while schema 1 retains its legacy fallback.
- The user authorized a staging-only write/delete smoke test after quick checks
  and mandatory review. Production writes remained outside this follow-up.
- Workspace commits `a00c62d`, `2e0208b`, `322cfe9`, and `266423f` add the
  schema-4 runner, bilingual changes-file generator, schema-2 cleanup summaries,
  and authoring policy. The unrelated `AGENTS.md` session-selection edit remains
  unstaged.
- Contract commit `4189c76` documents changes-file generation, guarded
  deletions, and staging revision-history review.
- The complete workspace Ruby suite passes: 138 runs and 622 assertions. Ruby
  syntax checks and both repository diff checks pass. The contract repository's
  pinned `bin/check --allow-missing` validation passes with 42 controls, 34
  paths, 90 navigation bindings, four managed articles, 12 runtime tests, and
  all 120 screenshot variants.
- An authenticated read-only production check parsed and matched the latest
  Czech SSH revision summary through the same history reader. An initial probe
  against `private:acct` correctly authenticated but used an invalid test
  assumption that the latest historical summary was non-empty; the reader
  returned the valid empty summary. The corrected known-summary probe passed.
- The mandatory standalone review found one Blocking issue: the first revision-
  history implementation duplicated the authoritative wiki endpoint map, so a
  future hostname edit could separate the mutation target from the metadata
  check. The first commit was rewritten so the history URL and authentication
  both derive from `KbPage.wiki_config`; focused tests now assert that both
  providers receive the same wiki key. Reviewer closure against rewritten head
  `266423f` found no remaining Blocking, Important, or Advisory findings.
- The staging-only schema-4 smoke test updated `wiki:playground` with summary
  `Ověření souhrnu úpravy ve staging KB` and deleted
  `drafts:2026-07-02-kb-staging:bot-ignore-test` with summary
  `Ověření souhrnu odstranění ve staging KB`. `kb-release verify` matched both
  summaries in authenticated staging revision history and printed their direct
  history links. Reapplying the same manifest also passed without creating a
  new revision, exercising the summary-checked retry path.
- The smoke postconditions independently confirmed the new playground content
  and the deleted page's absence. Staging was then reset from production at
  `2026-08-16T19:47:37Z`; both original pages matched the freshly fetched source
  files byte-for-byte, the pending release was empty, and staging ownership was
  released with the container down. No production write was made.
- The workspace remote was fetched immediately before publication and remained
  at base `0f22dab`. Commits `a00c62d` through `266423f` were pushed linearly to
  `origin/master`; the unrelated `AGENTS.md` edit remains unstaged and was not
  included.
- Contract branch `2026-08-14-kb-updates` and its retained remote ref point to
  `4189c7661c8dcefb2cb9f9610fe85515e87c9e6f`. Its GitHub `Check` run
  `31968706290` passed. A fresh detached integration worktree fast-forwarded
  current `origin/master` from `45af935` to `4189c76`, passed the full pinned
  `bin/check --allow-missing` suite, and pushed `master` over SSH. The temporary
  integration worktree was removed, and the resulting `master` `Check` run
  `31969001347` passed.

## Branch-safe managed-page links follow-up

- The verified active session remains `2026-08-14-kb-updates`. The contract
  worktree is clean on its retained feature branch at `4189c76`. The workspace
  is on shared `master` at `266423f`; its unrelated pre-existing `AGENTS.md`
  edit remains unstaged and must not be included.
- Planned repositories are `dokuwiki-plugin-vpsadmindoc`,
  `vpsfree-kb-contracts`, and `vpsfree-cz-configuration`, plus the top-level KB
  release tooling. No vpsAdminOS change is needed: the current runner already
  expands `kb/firewall#*` to all five firewall scripts and `kb/*#*` to all 12
  managed scripts.
- The user selected immutable exact-commit links for staging and an enforced
  remote-`master` content check before production promotion. The existing
  staging credential directory is already mounted read-only into the container
  and can carry a non-secret runtime ref file.
- The user will deploy aitherdev. Implementation must stop after reviewed,
  built and pushed configuration is ready, report its exact revision, and wait
  for deployment confirmation before restarting or writing staging. Production
  deployment and KB publication remain separately approval-gated.
- Created clean feature worktrees on branch `2026-08-14-kb-updates`:
  `worktrees/2026-08-14-kb-updates/dokuwiki-plugin-vpsadmindoc` from plugin
  `origin/master` `8ba8897`, and
  `worktrees/2026-08-14-kb-updates/vpsfree-cz-configuration` from configuration
  `origin/master` `f19c6a70`. Both remotes use SSH. The configuration checkout
  hook reported the known missing ambient Overcommit gems after creating the
  clean worktree; existing durable notes document this behavior. Install and
  run Overcommit from the repository's Nix shell before committing.
- Plugin commit `9bf39af455f3bdec694d0c3b2fd92a565924718e` accepts the
  repository-relative page paths and `suite#*` selectors, resolves them from a
  configured repository and revision, rereads an optional revision file on
  every request, retains legacy URL markers, and renders a prominent accessible
  edit warning. Its full Nix-shell plugin and real-DokuWiki checks pass, and the
  feature branch is pushed.
- Contract commit `004a570eab96fb91a7fecbb8fe88a316aaac4131` migrates all
  eight Firewall, GRE, Guix and KVM markers, enforces their registry-derived
  values and complete runtime-suite coverage, and documents exact staging
  provenance. The full `bin/check --allow-missing` suite passes with 32 article
  tests and 94 assertions; `kb/*#*` lists exactly all 12 managed scripts. The
  feature commit is pushed while contract `master` intentionally remains at
  `4189c76`.
- Workspace commits `8380fbf` and `77c4e1f` add committed managed-test
  provenance, validate release selectors and paths, verify exact remote page
  and test hashes, maintain the staging revision file, and block production
  promotion until remote contract `master` matches. All five Ruby suites pass:
  33/173, 39/177, 31/125, 10/33 and 28/144 runs/assertions. The unrelated
  pre-existing session-selection edit in `AGENTS.md` remains unstaged.
- Configuration commit `134b3a8d` pins the plugin feature commit on aitherdev
  and `int.kb`, configures production at `master`, configures staging with
  `/private/kb-staging/managed-repository.ref`, and initializes the public file
  to `master`. Overcommit was installed and signed in the worktree; Nixfmt and
  RuboCop hooks pass. Machine builds and the configuration push remain pending
  until the standalone review.
- A fresh read-only production snapshot contains 114 Czech and 77 English
  pages. All eight managed pages are byte-identical to contract base `4189c76`.
  The generated `kb-candidates-managed-marker-004a570` bundle changes only
  those markers. Its localized manifests contain four pages and four test
  sources per language, pin exact pushed head `004a570`, and use eight distinct
  article-specific summaries. Remote exact-head verification passes for every
  page and test; the production-`master` guard fails as intended while master
  still contains the old markers.
- The first standalone review found four issues: release provenance did not
  fully bind the repository and derived test source rendered by the plugin;
  legacy candidate indexes could generate an explicit empty test list rejected
  by the release consumer; the plugin and workspace histories each bundled two
  independently reviewable changes; and the staging ref readers disagreed on
  surrounding whitespace. No live staging or production operation was run.
- All four findings are fixed. The contract now accepts only
  `vpsfreecz/vpsfree-kb-contracts` and requires each registered test source to
  equal `tests/suite/<suite>.nix`. Workspace validation independently enforces
  the same repository identity, derives the same source, and preserves absence
  of test provenance for legacy candidates. The release tool and plugin both
  reject a ref file with surrounding spaces. Regression tests cover every
  case.
- Unpublished history was rewritten into focused commits. Plugin commits are
  `9d74362` (revision-aware resolver) and `adaff74` (prominent edit warning).
  Workspace commits are `1aae413` (managed test provenance), `258f51a`
  (staging exact ref), and `d46c459` (production remote-master guard). The
  contract head is `7ad8676`; configuration head is `4c702228`.
- Exact-head quick checks pass after the fixes: the workspace has 144 runs and
  666 assertions across its five Ruby suites plus syntax checks; the plugin's
  complete Nix-shell and real-DokuWiki checks pass; the contract's complete
  `bin/check --allow-missing` suite passes with 34 article-contract runs and
  100 assertions; and configuration Overcommit Nixfmt, RuboCop, and commit-
  message hooks pass. All commit-message lines are at most 80 characters.
- The rebuilt exact candidate is `kb-candidates-managed-marker-7ad8676` and
  the reciprocal manifests are
  `kb-release-managed-marker-7ad8676-{cs,en}.yml`. They still contain only the
  eight marker migrations, four pages and four managed test sources per
  language, and eight distinct localized page summaries. Exact remote source
  verification passes at pushed contract revision `7ad8676`.
- The same standalone reviewer is performing closure review of workspace
  `266423f..d46c459`, plugin `8ba8897..adaff74`, contract
  `4189c76..7ad8676`, and configuration `f19c6a70..4c702228`. Configuration
  builds and all deployment actions remain pending until that review closes.
- Closure review found one remaining instance of the provenance mismatch at
  the final release-manifest boundary: a hand-edited candidate or manifest
  could pair `kb/kvm#*` with `tests/suite/kb/gre.nix`. Workspace commit
  `42aec16` now derives and enforces the test source during both manifest
  generation and final manifest loading. Direct tampered-candidate and release-
  loader regressions pass.
- The exact workspace head is now
  `42aec168e6d8a8e3e3a84710a01355ec28e709f4`. Its complete quick suite passes
  with 145 runs and 673 assertions across the five Ruby suites, all seven Ruby
  syntax checks, and clean diffs. Focused reviewer closure is pending before
  configuration builds.
- Reviewer closure at exact workspace head `42aec168` found no remaining
  Blocking, Important, or Advisory issues. It independently confirmed both
  selector/source enforcement points and their direct regressions.
- `confctl build -y cz.vpsfree/machines/aitherdev` produced generation
  `2026-08-16--23-25-52`, including the revised staging container and plugin.
  `confctl build -y cz.vpsfree/containers/int.kb` produced generation
  `2026-08-16--23-28-09`. Neither target was deployed.
- Configuration branch `2026-08-14-kb-updates` was pushed over SSH at exact
  revision `4c7022287d2a17678a5a0b742f8243e24082df21`. Workspace `master` was
  fetched, confirmed linear from unchanged remote base `266423f`, and pushed
  over SSH to exact head `42aec168e6d8a8e3e3a84710a01355ec28e709f4`.
- The user must deploy aitherdev from configuration revision `4c702228` before
  any live staging check. The staging container has not been started and no
  staging or production wiki write was made in this follow-up.
- Exact contract head `7ad8676` passed GitHub Check run `31973055960`. Managed
  article runtime run `31973055958` also passed without retries in 30m05s: one
  unfiltered parallel test-runner invocation ran all 12 scripts, then result
  evaluation, summary generation, and cleanup completed successfully. No
  failure artifact required investigation.
- The user confirmed deployment of aitherdev configuration revision
  `4c702228`. `bin/kb-stage status` showed the new public managed-repository
  ref initialized to `master`, an unowned/down staging container, and no
  pending release. This session claimed and started staging; both API
  identities authenticated successfully.
- The exact `7ad8676` Czech and English manifests staged four managed pages
  each. Before either write, release tooling fetched and hashed the four page
  sources and four derived suite sources at the pushed feature commit. Both
  manifests verify after staging, including all eight localized revision
  summaries and four reciprocal language pairs per manifest.
- A durable Playwright check in
  `work/2026-08-14-kb-updates/verify-managed-marker-staging.cjs` passed for all
  eight live staging pages. Every toolbar source action, edit-warning source
  link, and edit-warning test link uses exact ref `7ad8676`; selectors are the
  complete `kb/*#*` patterns. Authenticated edit views contain one localized,
  accessible alert with the prominent background, border and icon, safe
  external-link attributes, and no configuration diagnostic. Czech and English
  firewall warning screenshots were inspected visually and are readable.
- A request-time ref-file test changed the public ref from `7ad8676` to
  `master` without rebuilding or restarting aitherdev or the staging container.
  All eight toolbar links immediately changed to `master`. The exact staged ref
  was restored, and all eight links immediately returned to `7ad8676`; both
  manifests still verify afterward.
- All eight pretty staging URLs return HTTP 200. A read-only production
  verification fails at the expected pre-access guard because contract
  `master` still has the old firewall marker source. No production API access
  or write occurred. Staging remains running, owned by this initiative, with
  the exact English manifest recorded as pending and the public ref restored to
  `7ad8676`.
- Staging review found that the warning's overwrite sentence overstates the
  risk: repository publication is deliberate. The user requested keeping only
  the automated-test statement. The bilingual writing skill produced the
  concise English `Automated tests do not cover changes made only in this
  editor.` and Czech `Změny provedené pouze v tomto editoru se netestují
  automaticky.`
- Plugin commit `f198173ed15dfa1fe124311fe45ae3c54914e7d3` contains only the
  localized warning copy and matching regressions, including absence checks for
  the overwrite claim. Its full Nix-shell unit and real-DokuWiki checks pass,
  and the feature branch is pushed.
- Configuration commit `3733ab8` updates only the staging and production
  plugin pins to `f198173` with verified source hash
  `sha256-qb5W4tp50CLD1tuczogVzG9NSxumhJvJd7iHWQBZbhk=`. Overcommit Nixfmt and
  RuboCop checks pass. The first ambient-shell commit attempt was correctly
  blocked because `nixfmt` was unavailable; the commit was then made inside the
  repository Nix shell, where all mandatory hooks passed.
- Long configuration builds, the configuration branch push, and deployment are
  pending a fresh standalone review of plugin range `adaff74..f198173` and
  configuration range `4c702228..3733ab8`. The existing staging container still
  renders the prior warning until aitherdev is redeployed; staged page content,
  the exact contract ref, and production remain unchanged.
- The fresh mandatory review found no Blocking, Important, or Advisory issues.
  It confirmed the focused commit split, equivalent natural bilingual copy,
  unchanged accessibility/security behavior, identical staging/production pin,
  published plugin revision, independently reproduced source hash, safe mixed-
  version operation, and previous-pin rollback. Fresh configuration builds and
  post-deployment live bilingual editor checks remain required.
- Exact configuration head `3733ab8` built successfully for both affected
  targets. Aitherdev generation `2026-08-17--09-52-20` includes the new staging
  plugin; `int.kb` generation `2026-08-17--09-54-10` validates the production
  pin. The configuration feature branch was fetched, confirmed one clean
  fast-forward from remote `4c702228`, and pushed over SSH at exact head
  `3733ab8c71b8dcfa2ad29a22ca25ed8f3acc4615`.
- The on-demand staging container was stopped before the deployment handoff so
  it cannot remain on the old running container generation. Ownership, all
  staged data, the pending English manifest, and exact managed ref `7ad8676`
  are retained. The user must deploy aitherdev at `3733ab8`; afterward this
  session will restart staging and repeat bilingual warning/link verification.
- The user confirmed deployment of aitherdev configuration `3733ab8`. Staging
  restarted from the retained data and authenticated both API identities. The
  public managed ref remained exactly `7ad8676`, and the pending English
  manifest remained intact.
- The live Playwright check passed all eight managed pages on the new plugin.
  Every authenticated editor view contains exactly the final localized testing
  sentence and no `overwrite`/`přepsat` wording. Warning prominence,
  accessibility, source/test/guide links, complete selectors, safe external-
  link attributes, and exact feature-commit URLs all remain correct. Fresh
  Czech and English warning screenshots were inspected visually and render
  cleanly.
- Both localized manifests verify after the deployment, including remote page
  and test hashes, per-page revision summaries, and all four reciprocal pairs
  in each language. Staging remains running and owned by this initiative;
  production remains untouched.
- The user requested a complete managed-page terminology migration. The
  canonical contract will become schema 2 at `contract/pages.yml`, with
  `pages`, `variants`, and `kbPage`; new generated provenance will use
  `page_key`. Both translations will carry the identical English KB ID in the
  `<page>` tag. Workspace release schema 5 will emit the new terminology while
  retaining read-only support for existing schema-4 manifests. Implementation
  and verification are in progress; staging still contains contract revision
  `7ad8676` and production remains untouched.
- Contract commits `112ea59` and `326ce03` implement the schema-2 registry,
  page-oriented tools and runtime metadata, and the shared English page-ID
  invariant. The contract worktree is clean at exact head `326ce03`.
- Workspace commits `45ef1c7`, `6aa97b4`, and `89b602f` separately implement
  release-manifest compatibility, schema-5 candidate provenance, and the
  authoring policy. The unrelated development-session edit in `AGENTS.md`
  remains unstaged and unchanged.
- Workspace quick verification passed all five Ruby suites with 148 runs and
  682 assertions, five changed-file syntax checks, and clean task diffs.
  Contract `nix develop --command bin/check --allow-missing` passed with four
  pages, eight variants, 12 runtime tests, 21 executable samples, and all
  focused Ruby checks green. No VM runtime test has run locally.
- The existing `actions/checkout@v7` workflow reference remains the current
  major release; the pinned vpsAdminOS test-runner action commit remains the
  newest compatible revision that still contains the imported action paths.
  No workflow action pin changed.
- The standalone review found one Blocking boundary gap: new schema-5
  artifacts could omit runtime-test provenance. Workspace commit `bf1f640`
  now requires exact test coverage in both candidate generation and final
  schema-5 manifest loading, while direct reads of schema-3/4 artifacts still
  permit the legacy omission. Focused regressions cover both behaviors.
- The review also found that the shared page-ID check allowed a second page
  tag. Contract commit `8d5723c` now requires exactly one opening and closing
  tag and rejects a conflicting duplicate. Commit `1fe36b3` finishes the
  terminology cleanup in the flake description.
- The user clarified that per-page revision summaries should not repeat the
  page title or subject. Workspace commit `d60f34e` records that rule. The
  eight prepared summaries now describe only the source/test binding and, for
  English variants, the corrected shared translation ID.
- Post-fix workspace quick checks pass with 149 runs and 687 assertions across
  all five Ruby suites, plus syntax and diff checks. The complete contract
  quick check passes at exact head `1fe36b3`: 38 page-contract runs with 112
  assertions, four managed-source runs with 10 assertions, and the full
  120-image inventory. Reviewer closure is pending before either branch push
  or the one-shot 12-script runtime workflow.
- Reviewer closure at exact workspace head `d70e1a0` and contract head
  `1fe36b3` found no remaining Blocking, Important, or Advisory issue. It
  independently confirmed all finding fixes, focused history, schema-3/4 read
  compatibility, exact schema-5 test coverage, all eight shared English page
  tags, candidate/manifests, and concise per-page summaries. The single-run
  12-script CI is cleared to begin after pushing both exact heads.
- Contract feature branch push advanced cleanly from `7ad8676` to exact head
  `1fe36b35cebb75f8c61741da77b6861d4e0ece58`; workspace `master` advanced
  linearly from unchanged remote `42aec168` to exact head
  `d70e1a093b4848351f701ea44407487159a60dab`. Both remotes use SSH.
- GitHub Check run `32013289941` and the single-invocation Managed page runtime
  run `32013290003` started for exact contract head `1fe36b3`. No superseded
  run was queued or active. The runtime workflow is expected to execute the
  complete 12-script inventory once with test-runner-managed parallelism.
- Exact-head Check run `32013289941` completed successfully. Managed page
  runtime run `32013290003` also completed successfully in 34m59s without a
  retry: its one unfiltered test-runner invocation ran all 12 scripts, result
  evaluation and log summaries passed, cleanup succeeded, and no failure-log
  artifact was needed.
- The post-CI final candidate
  `kb-candidates-managed-page-schema-final-1fe36b3` contains exactly the eight
  managed page changes. Both generated schema-5 manifests contain four pages,
  four exact runtime-test sources, and contract head `1fe36b3`.
- The first staging attempt stopped safely because the existing staged Guix
  revision already had the old summary; DokuWiki cannot replace a revision
  summary in place. The tool set the public ref but made no page change. Since
  staging was owned by this initiative and held only its superseded bundle,
  `bin/kb-stage reset --yes` mirrored 114 Czech pages, 77 English pages, 226
  shared media objects, and 65 language pairs from production.
- After the reset, both final manifests staged successfully. Their independent
  verification confirms all page/test hashes, exact managed ref `1fe36b3`,
  eight concise localized revision summaries with staging history URLs, and
  all reciprocal language pairs. Production remains untouched.
- The live Playwright check passed all eight staging pages: toolbar and editor
  links point to exact ref `1fe36b3`, test selectors cover complete suites,
  localized warnings retain their accessible presentation and concise testing
  copy, and no configuration diagnostic appears. Czech and English firewall
  warning screenshots were inspected visually and render cleanly.
- The staging-summary mismatch is recorded as the reusable lesson
  `notes/cross-project/2026-08-17-kb-staging-summary-reset.md` in workspace
  commit `c25858e`. Another session advanced shared workspace `master` to
  `df8598d` before this note commit; the note was already based on that commit,
  and the final SSH push fast-forwarded remote `master` to exact head
  `c25858e4a89212abff5ff012ccbfa8d78dbd4892` without touching the unrelated
  `AGENTS.md` working-tree edit.
- After explicit production approval, a fresh temporary integration worktree
  fast-forwarded contract `master` from remote `4189c766` to the reviewed
  feature head `1fe36b35cebb75f8c61741da77b6861d4e0ece58`; no merge commit was
  created. The full `nix develop --command bin/check --allow-missing` suite
  passed in that exact integration worktree before the SSH push, and remote
  `master` now resolves to the same commit.
- An initial Czech promotion command was safely rejected before writes because
  the pending staged release was the English manifest. The exact English
  schema-5 manifest was promoted first, the exact Czech manifest was restaged
  and verified, and then the Czech release was promoted. Each release changed
  four pages and no media or deletions.
- Read-only production verification passes for both manifests. It verifies the
  remote `master` page and runtime-test sources, all eight production page
  contents, reciprocal language mappings, and the distinct localized revision
  summaries. Direct public requests to all eight production page URLs return
  HTTP 200.
- The staging release is fully consumed: `pending_release` is null and the
  retained public managed ref is the exact published commit `1fe36b3`. The
  production API tokens are not DokuWiki WebUI passwords, so the authenticated
  staging browser script cannot be reused against production; this caused no
  write and does not weaken the successful production API verification.
- The push to `master` started duplicate same-commit GitHub runs: Check
  `32023482055` and Managed page runtime `32023482032`. They were still running
  at handoff; exact commit `1fe36b3` had already passed Check `32013289941` and
  the complete 12-script runtime run `32013290003` before integration.
- After production verification, staging ownership was released and its data
  were retained. The temporary `vpsfree-kb-contracts-merge` integration
  worktree was removed; the feature worktree and local/remote feature branch
  remain available as required.
- The initial publication handoff incorrectly omitted the two deployment-side
  default branches. The user caught that production `int.kb` still required
  the new plugin and configuration. Read-only checks confirmed plugin remote
  `master` at `8ba8897` versus reviewed head `f198173`, and configuration
  remote `master` at `f19c6a7` versus reviewed head `3733ab8`; both remote
  masters were clean ancestors of their feature heads.
- Fresh integration worktrees fast-forwarded plugin `master` to
  `f198173ed15dfa1fe124311fe45ae3c54914e7d3` and configuration `master` to
  `3733ab8c71b8dcfa2ad29a22ca25ed8f3acc4615`, without merge commits. The
  plugin's full Nix-shell checks and real-DokuWiki integration check passed.
  The configuration head is unchanged from the exact revision already built
  successfully for both aitherdev and `int.kb`; its diff and target inventory
  were rechecked before publication.
- Both default branches were pushed over SSH and their remote refs verified.
  The temporary integration worktrees were removed; only their generated,
  untracked Nix-shell cache directories were discarded with the temporary
  configuration worktree. Production still requires the operator to deploy
  target `cz.vpsfree/containers/int.kb` from configuration `master`.
- After the operator deployed `int.kb`, production still rendered the old
  plugin's invalid-managed-marker diagnostic. The pages had been rendered
  before the plugin/configuration deployment, so their cached XHTML retained
  that diagnostic. The pinned NixOS DokuWiki module places the two render
  caches at `/var/lib/dokuwiki/kb.vpsfree.cz/data/cache` and
  `/var/lib/dokuwiki/kb.vpsfree.org/data/cache`. Purging only the contents of
  those cache directories should force reparsing with plugin `f198173`; page,
  media, revision, configuration, and authentication data must not be removed.
- Final cleanup verified all three feature heads are contained in their remote
  `master` branches, staging is released with no pending bundle, and the
  feature branches remain intact. The three initiative worktrees and their
  generated development caches were removed. Superseded drafts, fetched
  sources, candidate bundles, release manifests, helper scripts, screenshots,
  and temporary commit-message files under this initiative were also removed;
  this plan and state file remain as the durable record.
