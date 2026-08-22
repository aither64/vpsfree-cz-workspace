# 2026-08-21-vpsadminos-ebpf-program-check

## Repositories

- `vpsadminos`
  - branch: `2026-08-21-vpsadminos-ebpf-program-check`
  - removed worktree:
    `worktrees/2026-08-21-vpsadminos-ebpf-program-check/vpsadminos`
  - initial base: `origin/staging` at `5d74cb39c`
  - integration base: `origin/staging` at `f0657cb4e`
- `vpsfree-cz-configuration`
  - branch: `2026-08-21-vpsadminos-ebpf-program-check`
  - removed worktree:
    `worktrees/2026-08-21-vpsadminos-ebpf-program-check/vpsfree-cz-configuration`
  - initial base: `origin/master` at `c5ec9ea7`
  - integration base: `origin/master` at `942174b8`
- `linux`
  - read-only inspection of public `vpsfreecz/linux` commits; no local
    worktree
- workspace coordination repository
  - shared `master`; only the two task-specific `AGENTS.md` rules were staged
    and committed, preserving unrelated shared-tree changes

## Status

- vpsAdminOS implementation, binary-cache fix, and deterministic lifecycle
  coverage were rebased onto current `origin/staging`, tested, and
  fast-forwarded into `staging` at
  `4ebcaab16c3827834f8a8019ff685d5849623c4a`.
- Mandatory change review completed with no blocking findings. Its one
  important lifecycle-test race was fixed and folded into the first
  implementation commit before the final push.
- The configuration channel update was regenerated from current
  `origin/master` and fast-forwarded into `master` at
  `d5a7df8e6b45c05b3f02e25f425b6f4e84fdca8f`.
- The lifecycle VM test passes with the runner-published kernel outputs.
  Exact-head RSpec, cache publication, both hardware livepatch jobs, and the
  76-test broad suite pass both before and after integration. Both project
  default branches and their remote feature branches point to the intended
  commits. No Node was deployed.

## Commands run

- verified the active development-session slug and inspected shared status
- fetched current `vpsadminos` and `vpsfree-cz-configuration` SSH remotes
- added initiative worktrees through `bin/dev-session worktree add`
- read both repository-local `AGENTS.md` files
- inspected `os/livepatches/ebpf/available.nix`, the eBPF module, loader,
  package generator, and focused tests
- inspected the packaged 6.12.95 Linux revision and public kernel commit
  metadata using read-only Git/GitHub queries
- attempted direct non-interactive SSH to `root@node1.stg.vpsfree.cz`; the
  available identity was not authorized
- attempted read-only `confctl ssh` from the configuration development shell;
  it produced no Node command output
- evaluated the `bpftool -j link show pinned` result supplied by the user
- installed and ran the vpsAdminOS Overcommit hooks from `nix develop`
- ran `./test-runner.sh ls 'ebpf-livepatch*'`
- ran `./test-runner.sh test ebpf-livepatch` before and after adding the CIFS
  retirement boundary
- committed and pushed vpsAdminOS commits `a7b96ebfce449c4b532f9d9127c3c116f3a8bb09`,
  `047259baa22abc3227f6f8ca556bef6c16fd54dd`, and
  `fbd21e0eb2535d2ffa33e5d89d930d0fc95d62ba`
- ran the eBPF lifecycle VM repeatedly while fixing evidence-backed fixture,
  runit synchronization, and `bpftool` handling problems; the final run passed
  all three examples without scheduling a kernel derivation
- committed and pushed the lifecycle-test corrections as
  `5a4917393511f27ffd8c2a33e25d8f2624b094be`
- installed the configuration Overcommit hooks and ran
  `confctl inputs channel set --commit --no-editor
  'staging,os-staging,production' vpsadminos
  5a4917393511f27ffd8c2a33e25d8f2624b094be`
- inspected the unexpected lifecycle-test build graph and stopped each local
  kernel build instead of allowing it to continue
- verified from the derivations that the ZFS-builtin package and CI toplevel
  request only the `dev` output of `boot.kernelForBuiltinsConfig`, not its
  runtime `out`
- traced that dependency to `88ea86fd265a` (`os: live-patches: play nice with
  zfsBuiltin`) from 2024-05-17; it belongs to the legacy kpatch builder and not
  to eBPF livepatch
- compared GitHub Actions history for `1895bbcd`, `2fd6a8ae`, and `5d74cb39`
  and queried both legacy livepatch paths directly in the remote cache
- added and pushed workspace rules in `f31a916` and `a3005b9` requiring
  unexpected kernel rebuild investigation and builder publication of any
  additional required kernel output
- ran `confctl build --max-jobs=0` for staging Node `node1` and production Node
  `node25`; both reached their expected vpsAdminOS 5a49173 top-level and then
  stopped at the unavailable external initrd SSH host key
- confirmed `org.vpsadminos/int.gh-runner1` is unmanaged and excluded by
  `confctl build`, then selected managed OS-staging consumer
  `cz.vpsfree/containers/int.vpsfbot`
- dry-ran the OS-staging consumer build, verified that its 96 local derivations
  contained no Linux or ZFS build, and built it successfully
- pushed configuration feature head
  `8afc134338fa101ddd70fb3379cdbe5d927ba864`
- monitored final vpsAdminOS CI run `32539141798` through completion and
  inspected its test log
- fetched both default branches after merge authorization; vpsAdminOS
  `staging` had advanced to `f0657cb4e` and configuration `master` to
  `942174b8`
- rebased the four vpsAdminOS commits onto `f0657cb4e` without conflicts and
  force-pushed the feature branch with an explicit lease at
  `4ebcaab16c3827834f8a8019ff685d5849623c4a`
- reran the 33-example registry suite and three-example lifecycle VM on the
  rebased head; both passed and used cached Linux 6.12.95 outputs
- regenerated all three configuration pins with `confctl` from current master,
  moved the feature branch to generated commit `d5a7df8e`, and force-pushed it
  with an explicit lease
- interrupted one configuration regeneration attempt before it changed the
  lock file after detecting an incorrect revision argument, then reran it with
  the exact full vpsAdminOS revision
- monitored rebased feature-head vpsAdminOS CI run `32555949716` through
  completion and inspected its broad-suite summary
- created fresh detached target worktrees from the current default branches,
  fast-forwarded vpsAdminOS `staging` and vpsfree-cz-configuration `master`,
  reran the focused registry suite from the vpsAdminOS integration worktree,
  and verified the generated channel listing from the configuration
  integration worktree
- pushed vpsAdminOS `staging` at `4ebcaab16` and configuration `master` at
  `d5a7df8e6`, then removed both detached integration worktrees
- monitored post-merge vpsAdminOS RSpec run `32558824389` and CI run
  `32558824376` through successful completion and inspected the broad-suite
  summary
- verified both remote default and feature branch heads, then removed the two
  merged feature worktrees while retaining all local and remote feature branch
  refs

## Results

- `cifs_spnego_guard` is enabled by default for every kernel at or above 5.7.
  Unlike `ptrace_mm_guard`, it has no exclusive `untilKernel` boundary, so the
  Nix registry continues selecting it for kernel 6.12.95.
- The loader attaches the generated LSM skeleton and pins its `bpf_link` under
  the generation directory. The user-supplied result identifies link ID 85,
  program ID 2206, program type `lsm`, and attach type `lsm_mac`; the guard is
  therefore still represented by a live attached link.
- vpsAdminOS packages Linux revision
  `a2384967b90f24d2470c9eb15f0e66d938df7e08` as 6.12.95. Its
  `fs/smb/client/cifs_spnego.c` contains
  `cifs_spnego_key_vet_description()`, introduced by stable commit
  `a3bbda6502a9398b816fa2e71c9a3f955f58013d`, which permits descriptions only
  under the private `spnego_cred`. The eBPF guard is redundant on this kernel.
- The stable fix is absent from inspected vpsAdminOS 6.12.89, 6.12.90, and
  6.12.91 kernel revisions and present in 6.12.93 and 6.12.95. Official stable
  ancestry places it in Linux 6.12.92 and later, making 6.12.92 the likely
  exclusive retirement boundary.
- The service reload handoff removes old pins only when the new generation has
  a same-named replacement. A future program-set change alone can therefore
  leave the retired guard attached until an explicit service stop or reboot,
  unless the lifecycle is changed to support intentional retirement safely.
- The staging configuration enables `services.ebpf-livepatch` for all Nodes
  and currently pins vpsAdminOS staging revision `5d74cb39c`, which still has
  no CIFS guard upper bound.
- Successful reloads now remove every pin from older generations after the new
  complete generation is attached. Failed loads still preserve the old links,
  and an empty configured set removes all previously attached programs.
- `cifs_spnego_guard` now has the exclusive upper bound `6.12.92`; registry
  tests verify inclusion through 6.12.91, exclusion from 6.12.92, current
  kernel selection, and rejected manual selection at the boundary.
- The focused registry suite passes all 33 examples. Overcommit passed in the
  vpsAdminOS worktree. The first commit attempt outside `nix develop` was
  correctly blocked because `nixfmt` was unavailable, after which the commit
  and hooks succeeded inside the development shell.
- A fresh standalone mandatory review found no blocking or advisory issues. It
  identified an asynchronous runit reload race in the lifecycle test; the test
  now waits for old-generation cleanup after successful reloads and for a fresh
  failure log before checking failure preservation.
- The VM lifecycle test attempts exposed a pre-existing binary-cache omission:
  the ZFS-builtin kernel has always consumed the plain
  `kernelForBuiltinsConfig.dev` output, but the CI toplevel retained only the
  final ZFS-builtin kernel development output. The eBPF test did not change a
  kernel derivation and does not need the plain runtime kernel. Commit
  `fbd21e0eb` retains only the missing pre-ZFS `dev` output for runner
  publication.
- The direct trigger was not an eBPF or kernel derivation change. Production
  commit `1895bbcd` had a normal CI run and cached its `livepatch_5`. Stable
  nixpkgs update `2fd6a8ae` changed that legacy livepatch derivation, but it ran
  only update and kernel workflows; no normal OS CI published the replacement.
  Building the missing legacy livepatch then exposed its ZFS-builtin dependency
  on the pre-ZFS kernel development output.
- `boot.kernelForBuiltinsConfig` and the ZFS-builtin kernel were introduced by
  `99570e6e222a` in May 2024. Legacy livepatch has consumed `zfsBuiltinPkg`
  since `88ea86fd265a` on 2024-05-17. This is therefore a longstanding build
  dependency, not one added by the current eBPF work.
- The vpsAdminOS feature branch and `staging` point to
  `4ebcaab16c3827834f8a8019ff685d5849623c4a`. Its rebased exact-head RSpec,
  cache publication, AMD and Intel livepatch lifecycle jobs, and broad suite
  all passed before integration.
- The eBPF lifecycle VM passes all three examples: initial pins are attached,
  a forced activation failure preserves the exact link IDs and generation, and
  deploying an empty configuration unloads every old link and leaves one empty
  authoritative generation. Its build used cached Linux 6.12.95 outputs.
- `bpftool 6.18.7` returns status 255 while printing valid JSON for pinned
  tracing links on this kernel. The test accepts only 0 or 255 and still parses
  and validates the JSON link ID; the reusable finding is recorded in
  `notes/vpsadminos/2026-08-22-bpftool-pinned-tracing-exit-status.md`.
- Generated configuration commit
  `d5a7df8e6b45c05b3f02e25f425b6f4e84fdca8f` pins `staging`, `os-staging`,
  and `production` to the integrated vpsAdminOS revision. Its changelog records
  the feature commits for staging channels and the accepted existing staging
  delta plus those commits for production.
- The final-head vpsAdminOS action published its closure in about four minutes;
  neither it nor the local lifecycle test rebuilt Linux. Both final-head AMD
  and Intel legacy livepatch lifecycle jobs passed.
- Managed OS-staging consumer `cz.vpsfree/containers/int.vpsfbot` built
  successfully. Its dry run contained no Linux or ZFS derivation. Staging Node
  `node1` and production Node `node25` both evaluated to vpsAdminOS 5a49173 but
  cannot complete in this environment because the external
  `/secrets/nodes/initrd/ssh_host_ed25519_key` is intentionally unavailable.
- Direct final-head `.#ci-toplevel` dry-run evidence shows the Linux 6.12.95
  runtime output and the pre-ZFS `linux-6.12.95-dev` output are available as
  cache downloads; no Linux or ZFS derivation is scheduled.
- Final vpsAdminOS CI run `32539141798` passed completely. Its cache job took
  3m46s, AMD and Intel livepatch lifecycle jobs took 2m25s and 3m48s, and the
  broad suite reported 76 tests successful. The new
  `ebpf-livepatch-lifecycle` test passed in that suite in 65.83s.
- An initial `confctl` attempt used an incorrect expanded revision and failed
  with GitHub HTTP 404 before changing `flake.lock`; the command was rerun with
  the exact pushed revision and succeeded with hooks active.
- Rebased feature-head CI run `32555949716` completed successfully: its broad
  suite ran 266 scripts across 76 tests with no unexpected outcomes, and
  `ebpf-livepatch-lifecycle` passed in 96.79 seconds. The fresh integration
  worktree's focused registry suite also passed all 33 examples.
- Both default branches were updated by fast-forward only. Configuration
  `master` contains the three exact `4ebcaab16` input revisions. No deployment,
  service reload, or other live Node change was performed.
- Post-merge vpsAdminOS RSpec and CI passed on `staging`. The CI cache job took
  three minutes, both hardware livepatch jobs passed, and the broad suite ran
  266 scripts across 76 successful tests with no unexpected outcomes.
  `ebpf-livepatch-lifecycle` passed in 67.49 seconds. No push-triggered workflow
  exists for the configuration repository.

## Open questions

- None. The user authorized both default-branch fast-forwards and will perform
  deployment. The existing staging vpsAdminOS delta is intentionally promoted
  to the production channel.

## Cleanup

- All feature, detached integration, and configuration regeneration worktrees
  for this initiative were removed after clean-status checks.
- Ignored `.gems/`, `.confctl/`, `Gemfile.lock`, and `result` development
  artifacts inside the removed feature worktrees were discarded with the
  worktrees; they are reproducible from the repositories and Nix store.
- Local and remote feature branch refs were retained as required.
