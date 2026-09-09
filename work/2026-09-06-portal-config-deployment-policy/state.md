---
lifecycle: active
---

# 2026-09-06-portal-config-deployment-policy

## Repositories

- Workspace branch: `2026-09-06-portal-config-deployment-policy`
- Worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-06-portal-config-deployment-policy/workspace`
- Current workspace base: `b265b22ca0549a5a3574100ecdd7a2ae8d95b880`.
- Current reviewed workspace head:
  `c97b5d8b3ac3d58263f966edd6449c521524a8af`.
- Current change and review scope: workspace repository only. The historical
  configuration substrate branch remains unmerged but is not changed, pinned,
  built, or deployed by this follow-up.

## Status

- Session created without launching a duplicate Codex client. The current API
  agent owns implementation.
- Initial tracking prepared before the workspace feature worktree is created.
- The user corrected the new-session default to `xhigh`. The earlier deployed
  `max` default came from an explicit earlier instruction in the portal thread;
  the newer instruction supersedes it.
- The user expanded the initiative to replace the host-bound portal deployment
  with a hybrid privileged-system/user-service architecture, correct initiative
  completion semantics, add archive reopening, and recover a prematurely
  archived legacy initiative.
- The earlier `xhigh` and deployment-policy commits remain useful inputs, but
  the implementation and configuration feature branches now require a larger
  refactor. The generated configuration pin is obsolete under the chosen
  architecture and will be replaced before the branch is pushed.
- The hybrid implementation is committed on both feature branches. Neither
  default branch has been changed.
- An initial four-lane mandatory review of the earlier commit series found
  unsafe unpaired Codex switching and rollback, a volatile reopen journal, a
  finalization/cluster-release race, privileged password ownership assigned to
  the user, a per-request router keepalive leak, incomplete legacy migration,
  obsolete helpers, and non-reviewable intermediate commits. The implementation
  now addresses every blocking and important finding, and both unpublished
  feature branches have been rebuilt into coherent commits for review reruns.
- Review reruns found and remediated stale conversation queries after cutover,
  incomplete provenance checks on replay and fork, a finalization parser that
  disagreed with the private CLI, unsafe workspace-root replacement, retained
  failed profile generations, and inability to attach a fresh conversation to
  substantive legacy tracking. The unpublished workspace history was rebuilt
  so the rejected migration design never appears in the feature series.
- The user selected `gpt-6-astra` with `xhigh` reasoning as the new-session
  default. The live system Codex catalog advertises that exact model ID and
  effort.
- The user expanded the portal with browser plan-mode switching, explicit
  steer-versus-queue controls, and a one-time restart of six unfinished legacy
  tmux sessions. Their durable tracking and worktrees must be retained, session
  `34` must remain untouched, and the independent password-reset development
  cluster must remain running.
- The user explicitly removed the one-time backward-compatibility requirement.
  The old portal, tmux, Codex process, and conversations may all stop at the
  architecture cutover, including the cgroup session. The final design therefore
  uses a clean restart and removes the drain marker, legacy service shims,
  password-copy path, reverse migration, and their tests. Tracking directories,
  repositories, worktrees, and retained feature branches remain durable.
- Final review of the clean-restart series found additional interrupted-reopen
  and legacy-tracking edge cases. Reopened legacy tracking is now admitted only
  through a journal-bound manifest transition carrying exact plan and state
  digests. Fresh conversation creation consumes that transient provenance, and
  interrupted retries reject self-asserted or ambiguous tracking state.
- The configuration feature was deployed to aitherdev without merging it. The
  final portal application is installed from the unmerged workspace feature as
  user profile generation 3.
- The archived cgroup initiative has been recovered under its original slug,
  exact retained branches, and exact branch heads. It now has a fresh shared
  Codex thread using `gpt-6-astra` at `xhigh`.
- The initial browser extension and retained-initiative adoption checkpoint was
  committed and pushed at workspace head
  `223fc5b69e8d305d5f768b1a5dd9f0054e012920`. The feature remains unmerged;
  live deployment uses that worktree directly through `workspace-host`.
- The six named legacy tmux sessions have been stopped and recreated as shared
  portal/CLI sessions under their original slugs. The unrelated legacy tmux
  session `34` remains attached on the old socket, and the password-reset
  development cluster was neither stopped nor recreated.
- The user reported that Codex 0.153.4 now returns an object in `thread.source`,
  while creation recovery still decodes it as a string. Browser and CLI session
  creation therefore fail before recovery can complete, leaving schema-2
  tracking and exclusive creation journals behind.
- The failed slugs `2026-09-07-vpsfstatus-index-stale` and
  `2026-09-07-vpsfstatus-index-stale-alert` currently remain untracked in the
  shared workspace. They must not be deleted or retried by this implementation
  without a direct user action after the fix is deployed.
- The user clarified that `dev-session remove` must remove a session rather
  than merely clean its worktrees. The new destructive meaning will require
  confirmation, retain repository branches, and preserve discarded tracking in
  a private recovery location. Normal agent-led completion remains `finalize`.
- The requested browser follow-up includes a CLI-like request-input wizard,
  same-thread and named-fresh-session plan implementation, a purple bottom Plan
  control, visible pending steers, and scroll-position preservation. File
  uploads are deferred.
- The user reported that `2026-09-07-vpsfstatus-index-stale-2` answered once and
  then archived and stopped itself. Inspection of its exact rollout showed that
  the agent deliberately started a background finalizer after the turn became
  idle; the portal did not race or infer completion. Current lifecycle and CLI
  rules allowed that process to call `finalize` and `stop` without direct user
  authorization.
- The fix must keep every unarchived session conversational, even when its
  tracking lifecycle says `complete` or `abandoned`. Mutating `finalize` and
  `stop` will require an exact-slug terminal confirmation or a portal-only
  service-cgroup authorization. Agents may prepare terminal tracking but must
  never launch delayed cleanup or interpret a completed answer as permission to
  close a session.
- The archived session retains Codex thread
  `01a07c42-a006-77e2-b4cd-5424d3acdd07` and its rollout. It will be reopened
  under the same slug and recovered through Codex `thread/unarchive`; retries
  must preserve that identity and must not submit the recorded goal again.
- The shared Markdown renderer currently enables base Goldmark only. It will
  enable the table extension and add overflow-safe table styling for transcript
  and artifact views while keeping the existing sanitizer.
- The user selected the strict "never auto-close" policy and terminal exact-slug
  confirmation without a public `--yes` bypass. Live deployment remains gated
  on a separate restart approval after tests and review.
- Rebased the clean unpublished workspace feature branch onto current
  `origin/master` before this follow-up. No live service or session was touched.
- The user approved the final navigation and lifecycle design. Implementation
  continues on the existing unpublished workspace feature branch. The scope is
  empty reasoning-summary suppression, one lazy `Artifacts` tab, deterministic
  journaled `archive`/`delete`/`revive` commands shared by browser and CLI, and
  active-session ordering by real Codex or tracking activity. Archived sessions
  are also ordered by their latest tracking activity. No compatibility aliases
  are kept for the former public command names.
- File upload remains deferred. The current aitherdev portal, Codex processes,
  tmux sessions, and development clusters remain untouched during
  implementation and local verification.
- The final implementation is consolidated into seven coherent commits on
  workspace base `b265b22`: Codex browser interaction, durable portal work
  surface, deterministic lifecycle, user-profile deployment, and operating
  documentation, followed by the strict package-transition runtime contract.
  No configuration repository commit is mixed into this range.
- Exact-head mandatory review found and remediated four cross-process contract
  issues: lifecycle journal producers now derive paths from the shared command
  map; cluster compatibility includes the shared tracking-size limit; every
  mutating host command revalidates its package generation after acquiring the
  transition lock; and custom runtime lifecycle locks use the host's canonical
  runtime root. The unused eager artifact reader was removed.
- The user-profile runtime on aitherdev remains at the previously deployed
  package while review and sandbox verification finish. No live session,
  Codex/tmux process, or development cluster has been restarted by this
  follow-up.
- A clean exact-head review rerun found that portal-owned lifecycle requests
  did not retain the accepting portal's profile identity across their exclusive
  lock wait, and that fail-closed cluster transition semantics were not part of
  the rollback compatibility identity. The portal now binds its startup
  profile-link identity to every mutation, including successful and compensated
  A-to-B-to-A lifecycle waits. The shared cluster contract now versions the
  transition policy independently of the persisted-state schema, so the new
  host refuses rollback to permissive helpers while an old host can still
  accept the forward package.
- The duplicated Ruby profile-token wire format now has one shared source used
  by both the stable host and private session CLI, and the package installs that
  source beside both consumers.
- Exact-head verification passed 233 `dev-session` tests with 2,483 assertions,
  42 development-cluster tests with 464 assertions, and 42 `workspace-host`
  tests with 281 assertions. All portal Go packages, Codex/Web race tests, the
  shipped browser contract, Ruby and shell syntax, diff checks, and the complete
  Nix sandbox build passed. The final package is
  `/nix/store/a44hf7qh4aqq6sb8dpc0nhsgbw21rxl2-workspace-portal-0.1.0`.
- A read-only predeployment audit found all six current-runtime Codex threads
  idle with no pending request or queued message and found no archive, delete,
  or revive journal. The portal/router and Codex/tmux services are active; the
  Codex and tmux processes have not been restarted. The password-reset cluster
  remains running at PID `3779261` with its recorded legacy socket identity.
- The same audit found stopped, stale cluster state for
  `2026-06-15-vpsadmin-events` and
  `2026-08-12-dns-secondary-zone-transfer-failure`. Both retain generic legacy
  socket identities, so the final fail-closed transition policy correctly
  blocks deployment until those session-owned cluster states are explicitly
  reset. No cluster state has been changed.

- The user approved the lifecycle, Codex, repository, cluster, linkable-tab,
  and nonblocking-index plan. Deployment from the unmerged development branch
  is authorized without a separate prompt, but unrelated live sessions and
  clusters must remain intact.
- Archival of `2026-09-08-discourse-disable-chat` is stuck at durable phase
  `thread_retired`. Its archive is committed at workspace head `3a40734`, its
  work path and tmux session `$11` are absent, and no related process remains.
  tmux 3.6a returns success with blank output for the missing `$11` target;
  the current parser turns that blank response into a truthy empty session and
  therefore refuses every retry.
- The next deployment will first fix exact tmux identity validation, recover
  only that stale authority under all lifecycle locks, finish its existing
  archive journal, and deploy the already reviewed index change at workspace
  head `30f8fd3` together with the repair.
- The remaining implementation is split into non-overlapping lifecycle, Codex
  protocol, and repository/cluster backend work. The primary agent owns the
  shared web integration, full review, and live deployment.
- Commit `c97b5d8` binds every managed tmux session to a random identity token,
  journals creation before mutation, and makes start and fork retries
  package-transition safe. Final `xhigh` review reproduced tmux 3.6a expanding
  server-global environment fields for a missing exact target; the parser now
  treats simultaneous empty session ID and name as absence while continuing to
  reject partial or mismatched identities. All three final review reruns are
  clean.
- The supported archive retry completed
  `2026-09-08-discourse-disable-chat`. Its stale archive journal and runtime
  authority are gone, its committed archive at `3a40734` is unchanged, and no
  unrelated tmux session or cluster was changed.
- The reviewed repair was pushed and deployed as workspace profile package
  `/nix/store/kralf8myf6x3yw5whwd0vhy409l22wll-workspace-portal-0.1.0`.
  Portal and router are active, Codex retained PID `2323118`, every managed tmux
  ID is unchanged, and the password-reset cluster retained PID `3779261`.
  Direct portal access and authenticated VPN HTTPS return 200; unauthenticated
  HTTPS returns 401. The live index renders in about 1.7--1.9 seconds.
- Commit `315473b` implements asynchronous lifecycle progress with journaled
  retry parameters, a filesystem-only initial index with bounded cached
  enrichment, exact local-versus-GitHub repository head status, schema-2
  cluster service/account presentation, fragment-linked session tabs, compact
  Codex controls, transcript views, elapsed work status, and colorized diffs.
  It remains on the unmerged workspace feature branch pending exact-head review
  and live activation.
- Quick verification passed all portal Go packages, 272 `dev-session` tests
  with 2,679 assertions, 45 development-cluster tests with 509 assertions,
  JavaScript contracts, shell/Ruby syntax, and diff checks. The complete Nix
  sandbox build passed at
  `/nix/store/gzipi6cp5kd84p5pm7rs4n4jy9allwji-workspace-portal-0.1.0`.
- A separate candidate portal rendered the initial live index in 0.04 seconds
  and its enriched status in 1.04 seconds. The password-reset session page
  rendered in 2.69 seconds with grouped accounts, masked secrets, exact pushed
  revisions, and current-revision workflow results. The candidate was stopped
  afterward; the live portal, Codex, tmux, and cluster processes were not
  changed.
- The unpublished mixed UI change was rebuilt on `c97b5d8` as five focused
  commits. Final head `4ef0e6e` includes deterministic lifecycle progress,
  exact repository revision status, structured cluster services, responsive
  session/index state, and separated Codex message/activity views.
- Final browser reconciliation fixes make revive retry independent of
  conditionally rendered header controls, keep an initially empty index
  polling, and reload membership only from a complete status listing generated
  after the current HTML. Membership includes active/archive placement, so
  completed deletion, creation, archive, and revive changes cannot leave stale
  cards or loop against an older five-second cache.
- Exact-head verification passed all portal Go packages; race-enabled Codex,
  cluster, repository, session, and Web packages; 272 `dev-session` tests with
  2,679 assertions; 45 development-cluster tests with 512 assertions; the
  browser contract; diff checks; and the full Nix sandbox package build.
  General, architecture/concurrency, and risk/compatibility reviews at `xhigh`
  reported no Blocking or Important findings on `4ef0e6e`.
- Pushed exact head `4ef0e6e`. GitHub reports no workflow run for the branch.
  The final pre-switch audit found no active Codex turn, pending prompt, queued
  message, unresolved submission attempt, or lifecycle journal. One retained
  password-reset thread was already in terminal `systemError`; the other
  readable managed threads were idle.
- Switched the aitherdev user runtime from the unmerged workspace feature
  worktree to package
  `/nix/store/qs9avkiqqvbq1467mbjk2vs71qvafq0x-workspace-portal-0.1.0`.
  Portal and router restarted normally. Codex retained PID `2323118`, tmux
  retained PID `2323117`, every managed tmux session ID is unchanged, and the
  password-reset cluster retained PID `3779261`.
- Post-deployment Unix health returns 200. VPN HTTPS returns 401 without Basic
  Auth and 200 with the root-managed credential. The live password-reset page
  contains the service-tab UI. The initial index HTML rendered in 0.03 seconds,
  and cached/enriched index status rendered in 1.10 seconds.

## Commands run

- Rebuilt the final feature history into five focused commits, compared its
  tree byte-for-byte with the reviewed candidate, and pushed it normally as a
  fast-forward from the last deployed feature head.
- Ran the complete Go, race-enabled Go, Ruby lifecycle, Ruby cluster, browser,
  diff, and Nix sandbox verification at exact head `4ef0e6e`.
- Audited live Codex, queue, pending-request, submission, lifecycle, tmux, and
  cluster state, then ran `workspace-host switch --source` from the unmerged
  feature worktree and repeated process, service, HTTPS, and response-time
  checks.
- `dev-session current`
- Re-ran the final tmux/session suite after the missing-target regression: 272
  tests with 2,679 assertions passed. Workspace-host tests passed with 50 runs
  and 309 assertions, all Go packages passed, and the final Nix package build
  completed.
- Recovered the stuck Discourse archive through the candidate generation's
  public `dev-session archive` command under its normal transition and session
  locks, then verified journal, authority, tmux, cluster, and Git state.
- Pushed workspace head `c97b5d8` and switched the aitherdev user runtime from
  the unmerged feature worktree with `workspace-host switch`.
- `dev-session start portal-config-deployment-policy --no-codex --no-attach`
- Inspected the current workspace rules and the configuration repository's
  local instruction topics.
- Created both initiative worktrees with `dev-session worktree add`.
- Ran the focused and complete portal Go tests, Go vet, both flake evaluations,
  and focused diff checks.
- Updated the configuration input with
  `confctl inputs channel set --commit workspace-tools
  aither-vpsfree-workspace 9251c2be8c879fb40bcda995b72b0a1584e679f2`.
- Inspected the current package, NixOS services, CLI lifecycle implementation,
  manifest schema, archive workflow, user systemd state, ports, and Codex
  runtime coupling.
- Verified the retained local and remote branches for
  `2026-09-05-cgroup-v1-shared-device-fix`, its committed legacy archive, its
  lack of a portal manifest or live runtime conflicts, and its original merge
  bases.
- Built the workspace package in a clean Nix sandbox. Its Go, Ruby, JavaScript,
  PKI, password, and installed-wrapper checks passed.
- Validated the packaged App Server protocol contract and default `xhigh`
  support against system Codex `0.153.4`.
- Ran the configuration Overcommit hooks successfully in `nix develop` and
  built the aitherdev configuration generation with `confctl build`.
- Re-ran the complete Ruby session suite after final remediation: 167 tests
  with 1,597 assertions passed. A first run exposed an unrelated timing race in
  a fake-Codex log assertion; the focused test and the repeated complete suite
  passed.
- Re-ran all Go packages through the Nix development shell with module mode;
  all packages passed. The router test now uses a short Unix socket root so it
  also passes with the Nix shell's long `TMPDIR`.
- Rebuilt the unpublished workspace feature into four clean commits on
  `0fb8e95` and started the final mandatory review against the exact rebuilt
  heads.
- The final review used `gpt-5.6-sol` at `xhigh` for general,
  architecture/repetition, scope/proportionality, and risk/compatibility lanes.
  Blocking and Important findings about terminal lifecycle adoption,
  interrupted rename recovery, self-asserted provenance, and a no-goal retry
  were fixed. The final architecture and risk reruns were clean; the last
  general finding was a narrow no-goal retry case covered by the full suite.
- Built the pre-live-smoke workspace package at
  `/nix/store/n6cchaq2apld2ldiad23lhk1rwg4yp38-workspace-portal-0.1.0`.
  Its first sandbox attempt hit the existing 50 ms runner-exit test race; the
  focused test passed and the identical complete derivation then passed.
- Deployed configuration generation `2026-09-06--20-36-13` to aitherdev. Both
  health checks passed, activation completed without the former missing-bash
  error, nginx is active, and the obsolete system-owned workspace services are
  absent.
- Initially switched the user runtime to workspace profile generation 2 at that
  package store path. Router, per-workspace portal, App Server, and tmux user
  services became active, and `/home/aither/bin/{dev-session,workspace-host}`
  pointed into that generation.
- Verified repeat substrate reconciliation preserves the password, CA, leaf
  certificate generation, and key pair. The active certificate validates under
  the generated CA and contains the workspace wildcard plus the legacy exact
  hostname.
- Verified HTTPS through the aitherdev address: unauthenticated requests return
  401 and the authenticated recovered-session page returns 200. No credential
  or private key was printed or copied into tracking.
- Reopened `2026-09-05-cgroup-v1-shared-device-fix`, reconstructed both legacy
  repository registrations, and restored clean worktrees at vpsAdminOS
  `9fb79eb68ba4f7b9d9a9c6e2e985556a10aa725e` and configuration
  `72af910e51cc729e65faa4a8507b9e3e0649be8b`. The configuration checkout again
  emitted its documented ambient-Bundler hook error after Git completed the
  clean checkout.
- The first fresh-thread request raced the App Server's empty rollout file and
  returned an internal read error. Retrying the journaled command recovered the
  same thread without duplicating the initial request; its manifest is ready,
  transient reopen provenance is cleared, and the managed tmux session has
  three repository/session windows. A subsequent CLI start resumed it normally.
- Fixed that observed startup race in workspace commit `26ce0dc`. After
  `turn/start` succeeds, the persistence wait now retries only the exact Codex
  `-32603` empty-rollout response and remains bounded by the command context;
  the initial turn stays outside the polling loop. Ten focused repetitions and
  every Go package passed.
- Ran a fresh four-lane review of `66a7415..26ce0dc` with `gpt-5.6-sol` at
  `xhigh`. No lane reported a Blocking or Important finding. Architecture,
  scope, and risk were clean. General review's sole Advisory was to add negative
  unit cases for near-matching free-form error text; this is accepted because
  the matcher is a direct conjunction and wording drift fails closed without
  resubmitting the goal. The fake server deterministically covers the positive
  race and exactly one `turn/start`.
- The final Nix package build passed all packaged checks at
  `/nix/store/p5vfwbnwx1yh61wd4zprnqcl0b3zhmpp-workspace-portal-0.1.0`.
  Switched the live user runtime to generation 3; all four workspace user
  services remain active and the recovered session remains attached to its
  original fresh thread.
- Committed and pushed the cgroup archive-to-active tracking move on workspace
  `master` as `02a456c`; this coordination commit does not integrate the portal
  feature branch.
- Queried GitHub Actions after the final feature pushes. Neither repository has
  a workflow run for these branches.
- Added browser Default/Plan mode selection, immediate Send/Steer, explicit
  FIFO Queue controls, and retry-safe queued submission. Model and reasoning
  controls remain in the settings dialog rather than consuming chat height.
- Added journaled adoption for retained active initiatives without a portal
  manifest. Adoption preserves committed plan and state bytes, allows dirty
  project worktrees, and registers only safe canonical attached worktrees.
- Fixed a live UTF-8 adoption defect: retained tracking was compared as
  incompatible Ruby encodings even when Git and disk bytes were identical.
  Git content is now compared as binary data; the regression test includes
  Czech UTF-8 content and a state file larger than one MiB.
- Re-ran the complete Ruby suite after the final fix: 181 runs and 1,774
  assertions passed. All Go packages and race-enabled Codex/web packages had
  already passed at the same implementation state, and the final Nix package
  build passed at
  `/nix/store/zy5r1q4kr0w91fyvp55sg5ghpj8m5nyd-workspace-portal-0.1.0`.
- Mandatory review used `gpt-5.6-sol` at `xhigh`. The final general, scope,
  risk, and architecture assessments reported no Blocking or Important
  findings. Accepted Advisories are the bounded persistent queue-attempt ledger,
  retry-ledger loss if the runtime directory itself is lost, reliance on the
  installed Codex rollout format, lack of full browser DOM automation, and
  last-writer-wins simultaneous settings changes imposed by Codex 0.153.4's
  full-settings update protocol.
- Switched the user runtime to profile generation 5 at the final package. The
  router, portal, Codex App Server, and managed tmux services are active.
- Reconciled the legacy sessions to fresh shared threads:
  - `2026-06-15-vpsadmin-events`:
    `01a07bf3-858c-73f0-918f-cfe81aac75f9`;
  - `2026-08-12-dns-secondary-zone-transfer-failure`:
    `01a07bf4-24de-7311-8ff8-436a3d3819ff`;
  - `2026-08-18-vpsadmin-password-reset`:
    `01a07bf4-cc9b-7783-97ca-b25f4f661e1b`;
  - `2026-08-22-osctld-boot-failures`:
    `01a07bf5-7c08-7d50-b912-9e14613c9ea8`;
  - `2026-09-01-vpsadmin-rbac`:
    `01a07bf6-2df3-7923-b13e-4700d822adda`;
  - `2026-09-03-webui-vps-ipv6`:
    `01a07bf6-f00f-7450-8872-3438e96510d1`.
- Adoption warned about and preserved the events initiative's detached HaveAPI
  worktree and auxiliary repositories without canonical bare clones. The DNS
  and password initiatives likewise retained mismatched historical KB capture
  worktrees without registering them. RBAC remains coordination-only. The IPv6
  initiative's three retained, already-merged branches were registered manually
  because their worktrees had already been removed.
- At that checkpoint, verified all 12 portal manifests, authenticated HTTPS,
  browser controls,
  rendered Markdown history, a non-null pending-request array, latest-first
  index ordering, GPT-6 Astra at `xhigh`, Default mode, and the running cluster
  badge. The password-reset runner was PID `2700830`, PPID 1, with its
  original August 24 start time and ready file.
- A shell diagnostic trace accidentally exposed the old Basic Auth password in
  local command output. The password file was immediately replaced, the
  privileged substrate reconciled, nginx reloaded, and the digest verified to
  have changed. The exposed credential is no longer valid; CA and TLS keys were
  unaffected.
- Rechecked GitHub Actions after the final force-push. There are no runs for the
  workspace feature branch, so no superseded jobs required cancellation.
- Committed the urgent structured-thread-source creation fix as pre-rebase
  revision `e604a1b` and
  switched the live user runtime to
  `/nix/store/mgddv9ws3mnxwv740mza2yfck9vq2iwq-workspace-portal-0.1.0`.
  The portal, router, App Server, and tmux user services are active; the App
  Server process was preserved across the switch. Browser and CLI creation can
  now read Codex 0.153.4's structured source objects.
- Implemented the remaining browser follow-up without switching the live
  runtime: CLI-style paged input questions, exact-plan actions, a purple Plan
  control in the composer, correlated send and steer receipts, and scroll
  preservation with an explicit New output control.
- Redefined explicitly confirmed `dev-session remove` as a complete session
  discard. It retires the Codex thread, releases both cluster types, removes
  worktrees, moves tracking and creation state into private recovery storage,
  and retires managed runtime while retaining Git branches. Browser deletion
  uses the same command under an exclusive host transition so a new cluster or
  replacement session cannot race cleanup.
- Quick verification after the follow-up passed all Go packages, JavaScript
  syntax and browser-contract tests, 189 `dev-session` tests with 1,798
  assertions, 22 `workspace-host` tests with 146 assertions, and 20 cluster
  status tests with 243 assertions. Neither failed creation slug was removed or
  retried.
- Committed the complete browser and deletion follow-up, then rebased it onto
  current shared `master`. The final consolidated feature head is
  `6be8e29557c90fa4c0a584947523e45e1f9408a2`; the feature remains unmerged.
- The package-transition preflight found an invalid historical vpsAdmin state
  directory named `--help`, containing only `config.json`. It was moved
  recoverably to private user state before retrying; no real cluster state was
  removed.
- The first deployment attempt then stopped before profile mutation because
  the live Codex protocol corpus lacked samples for five already implemented
  request call sites. Added their exact request shapes and verified the corpus
  against Codex 0.153.4's generated schema.
- A packaged check reproduced a scheduler-sensitive two-second limit in the
  simulated runner-exit race. Raising only the test's polling ceiling to ten
  seconds passed 20 focused repetitions and the final package build; production
  signal behavior is unchanged.
- Final verification passed all Go packages and the race-enabled Codex/web
  packages, 205 `dev-session` tests with 1,961 assertions, 32 `workspace-host`
  tests with 198 assertions, and 34 cluster tests with 364 assertions. The Nix
  package build passed at
  `/nix/store/zal6c09n4c0xvva72yg2xfvf2q3g1v3j-workspace-portal-0.1.0`.
- Mandatory review used `gpt-5.6-sol` at `xhigh`. Architecture, risk, and scope
  reruns reported no Blocking or Important findings on exact range
  `784692786c6eff7def52bc3ac49548e87c19b4bf..6be8e29557c90fa4c0a584947523e45e1f9408a2`.
- Before activation, all five materialized managed threads were idle and there
  were no durable submission ledgers or session-removal journals. User-profile
  generation 7 is now active at the final package. The portal/router restarted;
  Codex PID `2323118` and tmux PID `2323117` were preserved.
- The password-reset cluster had been accidentally interrupted during a
  predeployment migration diagnostic and was immediately restored. It remained
  running and ready through the actual switch at PID `3779261`, with its exact
  legacy socket identity retained and owner-proven.
- The events and DNS-transfer clusters remain as stale durable state. Their
  unreferenced transient legacy socket directories were retired and their
  workspace-scoped socket identities recorded, without removing state or
  images. Provider status and cleanup now consume those canonical identities.
- Post-deployment checks found all four user services active, validated all 15
  portal manifests, and returned HTTP 200 through both the private Unix socket
  and authenticated VPN HTTPS. The default remains `gpt-6-astra` at `xhigh`.
- Reproduced the automatic closure from the retained rollout for
  `2026-09-07-vpsfstatus-index-stale-2`: the agent scheduled an unattended
  `finalize`/`stop` process after replying. The browser was not the initiator.
- Implemented explicit closure authorization. Terminal `finalize`, `stop`, and
  `remove` require an interactive exact-slug confirmation; `remove --yes` no
  longer exists. Browser archive and delete validate the exact slug and invoke
  the helper through a portal-service-only internal path. Complete and
  abandoned tracking remains conversational until it is actually archived.
- Renamed the portal's lifecycle-derived `Closed` state to `Terminal` and made
  repository immutability depend on the archive location. Added durable rules
  forbidding agents and background processes from inferring closure permission
  from lifecycle state, a completed answer, or a handoff.
- Added exact archived-thread restoration with `thread/unarchive` and resume.
  Reopen provenance and the old client version remain unchanged until tmux and
  manifest synchronization succeed, so a failed start can retry the same
  already-active thread without replaying the initial request.
- Enabled sanitized Goldmark pipe tables for plans, artifacts, and transcripts,
  added overflow-safe table styles, and refreshed the Nix Go dependency hash.
- Initial mandatory review found a public `remove --yes` closure bypass, the
  misleading `Closed` model, mixed closure/recovery concerns in one commit, a
  partial fake-Codex log race, version-drift recovery that could become
  unretryable, and ambiguous legacy-reopen documentation. All were remediated;
  the feature was rebuilt into separate closure, recovery, table, and test-race
  commits before targeted review reruns.
- The risk review also observed that a hostile same-uid process could call the
  authenticated browser endpoint. This deployment intentionally trusts the
  `aither` uid, which already reads the Basic Auth password and owns the tmux
  server and session files. The portal now documents that exact prompts and
  service-cgroup checks prevent supported unattended or accidental closure,
  not adversarial same-uid activity; stronger isolation would require a
  separate user-held credential.
- Final local verification passed 212 `dev-session` tests with 2,038
  assertions, 32 `workspace-host` tests with 198 assertions, 34 development
  cluster tests with 364 assertions, all Go packages, the Node browser contract,
  and JavaScript syntax. The cluster suite's runner-exit test flaked once under
  the first parallel run, passed immediately in isolation, and passed in the
  repeated complete suite.
- The first package build exposed the missing fixed-output dependency for
  Goldmark's table subpackage. After updating the dependency hash, the complete
  Nix package build passed. The bundled protocol contract also passed against
  live system Codex `0.153.4`.
- The targeted scope and architecture reruns were clean. Risk found one final
  publication window after tmux synchronization; ready authority is now
  written before the reopen marker is cleared, and a focused failure/retry test
  covers that boundary. The final risk rerun reported no Blocking or Important
  findings. Synthetic cgroup evidence rather than a live unit remains a
  deployment-time verification item.
- Rebased the unmerged feature on shared workspace `master`, preserving the
  reviewed patch exactly, and rebuilt the commits as `0e662e2` (explicit
  closure), `7143e34` (exact archived-thread recovery), `cd64479` (Markdown
  tables and dependency closure), and `050eca2` (atomic fake-Codex launch
  logging). The feature was force-pushed with an exact lease; GitHub has no
  workflow runs for the branch.
- The final package passed all sandbox checks at
  `/nix/store/d7p927w8dmh3iasm60i8c10s6jgnn1rs-workspace-portal-0.1.0`. No live
  service, thread, tmux session, or tracking archive was changed.
- Predeployment audit found all five materialized managed Codex threads idle,
  with no pending requests and no queued messages. No durable submission or
  removal journal exists. The portal and router are generation 7 processes;
  Codex PID `2323118` and tmux PID `2323117` remain unchanged. Browser-local
  drafts cannot be inspected from the host, but the server reports no accepted
  work awaiting delivery.
- The user approved activation after the audit. Switched the user application
  to profile generation 8 at the reviewed package. Portal and router restarted
  as expected; Codex PID `2323118`, tmux PID `2323117`, and development clusters
  were preserved.
- The live portal runs in
  `workspace-portal@vpsfree-cz.service`; its real cgroup contains that exact
  service component. A hidden portal lifecycle request from this ordinary shell
  was rejected before finalization because it lacks deployed runtime authority,
  confirming that the public CLI cannot use the service-only path.
- Reopened `2026-09-07-vpsfstatus-index-stale-2` and started it without an
  initial request. Codex unarchived and resumed exact retained thread
  `01a07c42-a006-77e2-b4cd-5424d3acdd07`; the manifest is active and ready,
  reopen provenance is cleared, runtime authority points to managed tmux
  session `$10`, and the thread is idle with its retained 93-entry transcript.
- Committed only that archive-to-work tracking move on shared workspace
  `master` as `958688c`. Other sessions' working-tree changes remain untouched.
  Direct portal HTTP and authenticated VPN HTTPS return 200, unauthenticated
  HTTPS returns 401, and the live restored transcript includes a rendered
  Markdown table.
- The user reported that the deployed table styling made Codex messages overlap
  in Firefox and that command-output disclosures did not behave reliably.
  Reproduction against the live transcript confirmed that `overflow-x: auto`
  on each Markdown message also made it a vertical overflow container, allowing
  the transcript grid to collapse message rows.
- The unpublished workspace feature now confines horizontal scrolling to
  dedicated table wrappers, constrains transcript grid items, keeps command
  details collapsed with a compact summary, and preserves disclosure and scroll
  state across transcript refreshes. The transcript API and stored session data
  are unchanged.
- The focused Go test first failed because a minimal `nix shell` supplied Go but
  no C compiler for cgo. Re-running with `nixpkgs#gcc` passed, and the reusable
  shell requirement is recorded in
  `notes/cross-project/2026-09-08-workspace-go-cgo-shell.md`.
- JavaScript syntax and every Go package passed. The Ruby session, cluster, and
  host suites passed with 278 tests and 2,601 assertions. A read-only Chromium
  smoke test against the feature build rendered 248 live transcript entries
  with no overlapping message rectangles, one correctly wrapped Markdown
  table, hidden collapsed output, and retained expansion and scroll state after
  refresh. The deployed portal and all live Codex and tmux processes remained
  untouched.
- Mandatory review classified the fix as low risk and used the general and
  architecture/repetition lanes with `gpt-5.6-sol` at `xhigh`. Both lanes found
  no Blocking or Important issues. General review was clean. Architecture
  review advised collision-safe transcript invalidation and a stable fallback
  key for the rare entry without upstream IDs.
- Both advisories were folded into the owning unpublished commit. Transcript
  invalidation now serializes the complete entry array, and ID-less entries use
  their occurrence within a turn and event kind rather than their position in
  the sliding transcript window. Focused JavaScript and web tests passed after
  remediation. The narrow changes reduced the reviewed risk and did not require
  a reviewer rerun.
- The complete sandboxed package build passed at
  `/nix/store/mh5dasqldyiz6q35gm0h9l0198fbjsc7-workspace-portal-0.1.0`.
  Workspace commit `4eb6f80` was pushed normally; GitHub has no workflow runs
  for the branch. Live profile generation 8 remains active pending explicit
  approval for the brief portal/router restart.
- The predeployment audit found six managed sessions with Codex threads. Every
  thread is idle, with no pending request, queued message, or lifecycle
  operation. The seventh managed tmux session has no Codex thread and has no
  lifecycle operation. No removal, archive, or transition journal was found.
  Browser-local drafts remain outside host visibility. The temporary test
  portal, proxy, and browser were stopped after verification.
- The user approved activation of the transcript readability fix. A fresh
  pre-switch audit again found all six browser-managed Codex threads idle with
  no pending requests, queued messages, or lifecycle operations. Switched the
  user application to package
  `/nix/store/mh5dasqldyiz6q35gm0h9l0198fbjsc7-workspace-portal-0.1.0`.
  Portal and router restarted as expected; Codex PID `2323118` and tmux PID
  `2323147` were preserved. The password-reset vpsAdmin cluster remained
  running and ready at PID `3779261`.
- Post-activation Firefox verification rendered 314 real transcript entries,
  including user messages, with no adjacent message overlap and no
  message-level vertical scrollboxes. All 160 command disclosures were hidden
  while closed, visible while open, and hidden again after closing. The live
  Markdown table was wrapped in its dedicated horizontal scroller. The live
  stylesheet no longer makes whole Markdown messages overflow containers.
- The final full local verification passed 233 `dev-session` tests with 2,483
  assertions, 42 development-cluster tests with 466 assertions, and 40
  `workspace-host` tests with 261 assertions across six seeds. All Go packages
  passed, and the Codex and Web packages also passed with the race detector.
- One initial sandbox build exposed a failure in the inherited transition-lock
  test. The exact seed and 20 focused repetitions passed locally; after the
  review remediations the complete host suite passed repeatedly.
- The final compatibility review found that an intermediate commit advertised
  transition policy 2 before the strict helper behavior existed. The unpublished
  series was rewritten so intermediate commits carry no transition-policy
  declaration; final commit `c7ac48f` introduces policy 2, monotonic forward
  compatibility, fail-closed socket identity enforcement, and rollback tests
  together. Duplicated legacy socket derivation was also centralized.
- Exact-head verification passed 233 `dev-session` tests with 2,483 assertions,
  44 development-cluster tests with 495 assertions, and 43 `workspace-host`
  tests with 283 assertions. All portal Go packages, race-enabled Codex and Web
  packages, JavaScript and shell/Ruby syntax, diff checks, and the complete Nix
  sandbox build passed. The package is
  `/nix/store/2b90h7bs1sp93npjxnmdz1svqhxa96jf-workspace-portal-0.1.0`.
- General, architecture/repetition, and risk/compatibility review reruns used
  `gpt-5.6-sol` at `xhigh` and found no actionable findings on exact head
  `c7ac48f`. The final scope/proportionality rerun is in progress. No live
  service, session, Codex/tmux process, or development cluster was changed.
- The scope rerun advised removing the unused archived-lifecycle reader and the
  private finalization wrapper that retained obsolete `check` and `prepare`
  modes. Commit `61295dc` removes that production surface, keeps isolated move
  testing in a test-only core helper, and routes the active-turn refusal test
  through supported `archive`. The exact-head `dev-session` suite now passes
  230 tests with 2,435 assertions, and the final package passes at
  `/nix/store/lgh2l8ab6af96zngap2crc43c1m84lxg-workspace-portal-0.1.0`.
- General, architecture/repetition, scope/proportionality, and
  risk/compatibility review reruns are clean on exact head `61295dc`. All used
  `gpt-5.6-sol` at `xhigh`.
- Force-pushed the rewritten unpublished feature branch with an exact lease.
  GitHub reports no workflow run for the branch, so there is no superseded run
  to cancel and no CI result to await.
- A final read-only activation audit found all eight materialized Codex threads
  idle, with no pending request, queued message, or unresolved submission. No
  archive, delete, revive, or submission journal exists. The two stopped
  vpsAdmin cluster states have canonical workspace-scoped socket identities;
  the running password-reset cluster retains its explicit owner-proven legacy
  socket identity. No session or cluster state was changed.
- Activation now requires the user's explicit approval for the brief portal and
  router restart. The switch is designed to preserve the Codex App Server,
  managed tmux server, conversations, and all development clusters.
- The user approved activation. The first real command contained a mistyped
  worktree path and stopped before doing anything. The corrected switch passed
  package selection but its Codex preflight found that the new activity-index
  `thread/list` call was absent from the protocol request corpus. It stopped
  before profile mutation or service restart.
- Commit `00f75ce` adds the exact request sample and a schema-independent corpus
  coverage mode to the sandbox package checks. The complete package rebuilt at
  `/nix/store/k3xysa77lwqw20zhnhqcqv534rpm5fs1-workspace-portal-0.1.0`, and
  its full activation-time validator accepts installed Codex 0.153.4. A narrow
  general and risk/compatibility review at `xhigh` found no actionable finding.
- Repeated the idle, journal, cluster, and GitHub Actions audit, then switched
  user profile generation 10 from the unmerged feature worktree. The deployed
  package is
  `/nix/store/zcpy4xp2ivs348b66rg5zdnx79z2wvnc-workspace-portal-0.1.0`.
  Portal and router restarted successfully. Codex PID `2323118`, tmux PID
  `2323117`, and password-reset cluster PID `3779261` were preserved; both stale
  cluster states also remain unchanged.
- Direct Unix-socket access returns 200. VPN HTTPS returns 401 without
  credentials and 200 with the root-managed Basic Auth credential; the deployed
  session page contains the Artifacts interface. The current long-lived shell
  predates membership in `workspace-portal-owner`, so the authenticated check
  used a fresh process with that supplementary group and did not print the
  password.
- A post-switch read-only audit found a newly active turn in
  `2026-06-15-vpsadmin-events`; it became active after the clean pre-switch
  audit and continues on the preserved App Server. It was not interrupted or
  inspected. The other seven materialized threads are idle, and no lifecycle
  or submission journal exists.
- A direct post-deployment index probe then exposed a live performance defect:
  the request spent its deadline starting both cluster helpers for every active
  and archived session, and the unscoped Codex `thread/list` activity scan could
  not finish against the long-lived rollout store. Session pages and exact
  thread RPCs remained responsive; no Codex or cluster process failed.
- Commit `30f8fd3` reads activity only for exact manifest thread identities,
  skips cluster helpers when no provider state entry exists, and inspects the
  two providers concurrently. The shared lock-directory initializer now safely
  postvalidates a concurrent creator. Race-enabled cluster/Codex/Web tests, all
  44 cluster tests with 495 assertions, and the complete package build passed.
  A separate candidate portal rendered the live index in 1.716 seconds while
  the events turn remained active. Review is in progress before redeployment;
  the temporary portal and its socket were removed.

## Results

- No existing development session belongs to this process.
- Workspace code and rules now implement the hybrid runtime. Configuration
  contains only the privileged substrate and ordinary system Codex package;
  its obsolete workspace flake input and development pin have been removed.
- Workspace commits:
  - `cdd7dd1`: durable feature-branch deployment and integration rule;
  - `55864fe`: exact merged-head completion, journaled reopen, fresh legacy
    conversation adoption, runtime provenance, and cluster-gated lifecycle;
  - `de7a780`: browser and terminal session UI, GPT-6 Astra with `xhigh`, and
    multi-workspace Host routing;
  - `982ade9`: transactional user profile runtime, retained Codex generations,
    registration, safe retirement, and clean cutover;
  - `66a7415`: journal-bound adoption of retained legacy tracking and safe
    interrupted-reopen recovery;
  - `26ce0dc`: bounded handling of Codex's initial empty-rollout persistence
    race without another initial submission.
- Configuration commits:
  - `e06c183e`: durable repository-local deployment/integration rule;
  - `f66ba792`: privileged wildcard HTTPS, credentials, router socket, linger,
    and removal of the system-owned workspace application;
  - `e9643195`: declarative workspace DNS wildcard and updated SOA serial.
- Configuration `master` remains at `4d570e30`; the implementation is unmerged.
- All portal Go packages passed. Workspace and configuration flake evaluation
  passed. The resolver regression verifies `xhigh` for the default model, an
  explicit effort override, and fallback to an explicitly selected model's
  advertised default when it lacks `xhigh`.
- The obsolete workspace-side PKI and password helpers and their tests have
  been removed because NixOS is now the sole privileged substrate owner.
- Aitherdev is running configuration generation `2026-09-06--20-36-13` built
  directly from the unmerged configuration feature worktree.
- Configuration worktree creation again completed in Git but returned exit 78
  because its post-checkout Overcommit hook could not load Nix-provided gems in
  the ambient shell. Both configuration commits ran their declared hooks
  successfully inside `nix develop`; its untracked `.bin/` and `.bundle/`
  development-shell caches are excluded from commits.
- The current reviewed workspace feature head is
  `4ef0e6ef1b6422022549a690425ef8c0dc06854f`. It is pushed and deployed from
  the unmerged feature worktree; it remains unmerged. The historical
  configuration feature head
  remains `e96431958b058ef495f491420655cfb7a4085fde`; it is outside this
  follow-up.
- The handoff helper cannot bind this API-owned process to an initiative because
  `VPSFREE_DEV_SESSION_SLUG` is unset. The explicit initiative is unchanged;
  its canonical post-deployment URL is
  `https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-06-portal-config-deployment-policy/`.
- The clean-restart review found and fixed an archive/message lock inversion,
  obsolete activation-time conversation rebinding, incomplete update
  compensation, a reopen rename durability window, cluster starts outside the
  archive barrier, missing cluster checks in direct finalization, stale services
  after workspace retirement, divergent Go/Ruby registry validation, an
  unnecessary nginx restart trigger change, and non-atomic fresh CA creation.
  Focused Ruby and Go tests pass after these fixes.
- First-install rollback has no preceding generation. The documented and
  accepted behavior is to leave the validated candidate installed and retry the
  same `workspace-host switch`. Privileged CA/password reconciliation,
  ownership, modes, key-pair matching, SANs, nginx, and Basic Auth were verified
  after deployment.
- Failed later profile generations are deleted after compensation, so a future
  rollback cannot select an application that failed activation. Unregistering
  retires name-scoped runtime sockets and authority before that name can be
  assigned to a different workspace root.
- The public switch command always activates the selected generation. A
  nonactivating switch was removed because it could leave old services running
  behind new stable CLI links.
- The internal DNS zone now carries the wildcard record used by the canonical
  multi-workspace hostname. `named-checkzone` accepted serial `2026090600`.
  The user has since deployed the internal DNS configuration.
- Unregister compensation now runs even when a multi-unit systemd disable
  partially succeeds before returning an error, restoring both unit state and
  quiesced clients.

## Open questions

- No design questions remain.

## Cleanup

- Keep both portal feature worktrees and branches while they remain unmerged.
  Remove the worktrees without force only after integration or explicit
  abandonment, retain the branches, and archive this initiative only after the
  final merged-head checks pass.
