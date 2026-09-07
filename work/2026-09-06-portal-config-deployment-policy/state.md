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
  `0fb8e95dcd4271e5ca75d4738a4d16d1c1a15dd2`.
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
- The browser extension and retained-initiative adoption are committed and
  pushed at workspace head
  `223fc5b69e8d305d5f768b1a5dd9f0054e012920`. The feature remains unmerged;
  live deployment uses that worktree directly through `workspace-host`.
- The six named legacy tmux sessions have been stopped and recreated as shared
  portal/CLI sessions under their original slugs. The unrelated legacy tmux
  session `34` remains attached on the old socket, and the password-reset
  development cluster was neither stopped nor recreated.

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
- Verified all 12 portal manifests, authenticated HTTPS, browser controls,
  rendered Markdown history, a non-null pending-request array, latest-first
  index ordering, GPT-6 Astra at `xhigh`, Default mode, and the running cluster
  badge. The password-reset runner remains PID `2700830`, PPID 1, with its
  original August 24 start time and ready file.
- A shell diagnostic trace accidentally exposed the old Basic Auth password in
  local command output. The password file was immediately replaced, the
  privileged substrate reconciled, nginx reloaded, and the digest verified to
  have changed. The exposed credential is no longer valid; CA and TLS keys were
  unaffected.
- Rechecked GitHub Actions after the final force-push. There are no runs for the
  workspace feature branch, so no superseded jobs required cancellation.

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
- The committed and pushed workspace head is
  `223fc5b69e8d305d5f768b1a5dd9f0054e012920`; the committed and pushed
  configuration head is
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
