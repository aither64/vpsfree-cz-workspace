---
lifecycle: active
---

# 2026-09-06-portal-config-deployment-policy

## Repositories

- Workspace branch: `2026-09-06-portal-config-deployment-policy`
- Planned worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-06-portal-config-deployment-policy/workspace`
- Registered workspace base:
  `c561cb9859b3217c0a8e5476af37c07a4332f060`; the feature was rebased and
  rebuilt as a clean linear series on current workspace `master` at
  `531fbf857f7a6797d4a79e208bebbf62e6347eb7`.
- Configuration branch: `2026-09-06-portal-config-deployment-policy`
- Planned configuration worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-06-portal-config-deployment-policy/vpsfree-cz-configuration`
- Configuration `master` baseline:
  `4d570e3053b114518ada59c2a45d5e9d8644347b`. It may advance only to the
  isolated repository-rule commit, never to the later portal pin.

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

## Commands run

- `dev-session current`
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
- The committed and pushed workspace feature head is
  `050eca27c95e557357c84339c0d86ee1ffa35325`; the committed and pushed
  configuration feature head is
  `e96431958b058ef495f491420655cfb7a4085fde`.
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
