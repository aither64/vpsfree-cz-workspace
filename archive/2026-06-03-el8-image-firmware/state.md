---
lifecycle: abandoned
---
# EL8 image firmware exclusion state

## Status

- 2026-06-03: Started implementation after CI log investigation identified
  oversized AlmaLinux 8 and Rocky 8 images.
- 2026-06-03: Implemented shared firmware package exclusions for AlmaLinux,
  CentOS Stream, and Rocky image builds and added a rootfs dataset size guard
  to image-script tests.

## Branches and worktrees

- Repository: `vpsadminos`
- Bare repository: `repos/vpsadminos.git`
- Branch: `2026-06-03-el8-image-firmware`
- Worktree: `worktrees/2026-06-03-el8-image-firmware/vpsadminos`
- Base: `origin/staging` at `cb665cd2688c3b2d69e37585449c2ba26276a417`

## Commands and results

- `git --git-dir repos/vpsadminos.git fetch origin staging`: fetched current
  staging.
- `git --git-dir repos/vpsadminos.git worktree add -b
  2026-06-03-el8-image-firmware
  worktrees/2026-06-03-el8-image-firmware/vpsadminos origin/staging`:
  worktree was created, but the checkout hook reported that the Overcommit
  configuration signature needs refresh. No commit has been made.
- `curl -fsSL https://images.vpsadminos.org/v1/INDEX.json`: live image
  repository index was fetched; HTTP headers report it was last modified on
  2026-05-30.
- Live current-image mapping from `./test-runner.sh ls 'image-scripts/*'` to
  `images.vpsadminos.org` covered all 49 generated image-script tests.
  Published ZFS stream sizes showed:
  - above 1 GiB: `rocky-8` at 1,222,046,208 bytes and `almalinux-8` at
    1,217,316,864 bytes;
  - above decimal 1 GB but below 1 GiB: `centos-9-stream` at
    1,006,324,224 bytes.
- `image-scripts/bin/config test list | sort`: confirmed the new
  `rootfs_size` image test is discovered.
- An initial `./test-runner.sh test image-scripts/test@almalinux-8` run was
  stopped after the untracked-test/flakes concern was raised. The new test file
  and helper change were staged so the flake source definitely contains both
  changes.
- `nix flake metadata --json`: confirmed the flake source contains
  `image-scripts/tests/rootfs_size.sh` and the `redhat-family.sh` exclusion.
- `./test-runner.sh test image-scripts/test@almalinux-8`: passed in
  1,727.58 seconds with the new `rootfs_size` test included.
- `./test-runner.sh test image-scripts/test@rocky-8`: two attempts failed
  before image building with `OsVm::TimeoutError` while waiting for the VM
  shell in `wait_for_osctl_pool("tank")`.
- `rm -rf /tmp/os-test-runner/os-test-image-scripts__test__rocky-8-631cd284
  /tmp/os-test-runner/socks/e1f42296-*`: removed stale Rocky test-runner
  state after confirming no Rocky test VM/process remained.
- `./test-runner.sh test image-scripts/test@rocky-8`: clean retry passed in
  1,675.7 seconds with the new `rootfs_size` test included.
- `./test-runner.sh test image-scripts/test@centos-9-stream`: failed before
  image building with `OsVm::TimeoutError` while waiting for the VM shell.
  User requested to keep the exclusion for CentOS Stream despite this local
  verification issue.
- `nix flake metadata --json`: confirmed the final flake source contains
  `image-scripts/tests/rootfs_size.sh` and the final AlmaLinux/CentOS/Rocky
  `redhat-family.sh` exclusion.
- `nix develop --command overcommit --install`: installed Overcommit hooks in
  the worktree.
- `nix develop --command overcommit --sign`: refreshed the Overcommit
  configuration signature.
- `nix develop --command overcommit --run`: passed Nixfmt and RuboCop
  pre-commit hooks.
- `git reset --mixed HEAD~1`: split the combined image-script commit into
  focused commits at the user's request.
- `git commit -F /tmp/vpsadminos-image-firmware-commit.*`: created commit
  `91969db22` (`image-scripts: exclude firmware from EL rebuilds`). Hooks
  passed cleanly.
- `git commit -F /tmp/vpsadminos-rootfs-size-test-commit.*`: created commit
  `812b682f7`, then amended it to `7e49ab3ae` to avoid commit-message
  text-width warnings (`image-scripts: check rootfs size in image tests`).
  Hooks passed cleanly after the amend.
- `git show --stat --oneline
  2d656ae4730d42c2a17ac767447b4bcb1eb89ccd`: confirmed the previous timeout
  decrease touched `osvm/lib/osvm/machine.rb`,
  `test-runner/lib/test-runner/cli/app.rb`, and
  `test-runner/man/man1/test-runner.1.md`.
- `rg -n 'default_timeout|Default timeout for machine commands|default_value:
  (600|900)|defaults to `(600|900)`' osvm test-runner`: checked timeout
  defaults before committing the restoration. Remaining `default_timeout: 10`
  and `60` hits are explicit spec/test helper values, not runtime defaults.
- `rg -n 'default[^\\n]{0,80}(600|10 minutes|10-minute)|600[^\\n]{0,80}default|defaults
  to [` ]600|default_value: 600|default_timeout: 600' .`: found no remaining
  600-second default timeout wording.
- `nix develop --command overcommit --run`: passed Nixfmt and RuboCop
  pre-commit hooks for the timeout restoration.
- `git commit -F /tmp/vpsadminos-timeout-commit.*`: created commit
  `cd8f654d6` (`osvm, test-runner: restore 15-minute command timeout`).
  Hooks passed cleanly.
- `gh run view 26889296877 --job 79310568282 --log`: inspected the CI job
  requested by the user.
- `gh run download 26889296877 -n os-test-logs-26889296877`: downloaded the
  full test log artifact.
- CI artifact `os-test-osctld__restart-b891f158/test-runner.log`: showed
  `clients after abrupt osctld death ct top exits instead of spinning` failed
  because the command exited with `error: Connection reset by peer -
  recvfrom(2)`, while the test expected only the existing normalized osctl
  lost-daemon messages.
- `nix develop --command bash -lc 'cd osctl && bundle exec rspec
  spec/osctl/client_spec.rb'`: initially failed to load because the local
  checkout had no compiled `libosctl/native`.
- `nix develop --command make gems`: started before the osctld/restart
  investigation, was stopped after the user asked to resolve the flaky test
  first, and its partial generated metadata was restored.
- `nix develop --command make gems`: rebuilt packaged gems from the final
  code with build id `25.11.0.build20260603210657`.
- `nix develop --command bash -lc 'cd libosctl && bundle exec rake compile
  && cd ../osctl && bundle exec rspec spec/osctl/client_spec.rb'`: passed
  13 examples, 0 failures.
- `./test-runner.sh test --test-config tests/test-configs/ci.nix -f
  osctld/restart`: passed in 469.5 seconds from the feature worktree using the
  rebuilt packaged gems.
- `git commit -F /tmp/vpsadminos-osctl-client-commit.*`: created commit
  `7018f568a` (`osctl: treat reset osctld socket as closed connection`).
  Hooks passed cleanly.
- `git commit -F /tmp/vpsadminos-gems-commit.*`: created commit
  `a0adfcf74` (`os: update gems to 25.11.0.build20260603210657`). Hooks
  passed cleanly.
- `git --git-dir repos/vpsadminos.git fetch origin staging`: fetched current
  staging before merge.
- `git merge-base --is-ancestor origin/staging HEAD`: confirmed
  `origin/staging` was an ancestor of the feature branch, so no rebase was
  needed.
- `git --git-dir repos/vpsadminos.git worktree add --detach
  worktrees/2026-06-03-el8-image-firmware/vpsadminos-staging-merge
  origin/staging`: created a temporary detached staging merge worktree.
- `git merge --ff-only 2026-06-03-el8-image-firmware`: fast-forwarded the
  staging merge worktree to `a0adfcf74`.
- `git diff --check origin/staging..HEAD`: passed in the staging merge
  worktree.
- `./test-runner.sh test --test-config tests/test-configs/ci.nix -f
  osctld/restart`: passed in 411.01 seconds from the staging merge worktree.
- `git push origin HEAD:staging`: initially failed because the pre-push hook
  loaded ambient Overcommit 0.69.0 while the Nix shell had signed the
  configuration with Overcommit 0.70.0.
- `ruby /home/aither/.gem/ruby/3.3.0/gems/overcommit-0.69.0/bin/overcommit
  --sign`: updated the shared hook signature with the same Overcommit runtime
  used by the Git pre-push hook.
- `ruby repos/vpsadminos.git/hooks/pre-push origin
  git@github.com:vpsfreecz/vpsadminos.git </dev/null`: passed after ambient
  signing.
- `git push origin HEAD:staging`: pushed `staging` from `cb665cd26` to
  `a0adfcf74`.
- `git --git-dir repos/vpsadminos.git worktree remove
  worktrees/2026-06-03-el8-image-firmware/vpsadminos-staging-merge`: removed
  the temporary merge worktree.
- `git --git-dir repos/vpsadminos.git fetch origin staging` and
  `git --git-dir repos/vpsadminos.git rev-parse --short=10 origin/staging`:
  confirmed `origin/staging` is `a0adfcf748`.
- `git status --short --branch`: feature worktree was clean and aligned with
  `origin/staging`.
- `rm -rf /tmp/vpsadminos-run-26889296877
  /tmp/os-test-runner/os-test-image-scripts__test__almalinux-8-b181ba33
  /tmp/os-test-runner/os-test-image-scripts__test__centos-9-stream-ff7b29eb
  /tmp/os-test-runner/os-test-image-scripts__test__rocky-8-631cd284
  /tmp/os-test-runner/os-test-osctld__restart-b891f158 ...`: removed local
  test logs, downloaded CI artifacts, and stale sockets from this initiative.
- `git --git-dir repos/vpsadminos.git worktree remove
  worktrees/2026-06-03-el8-image-firmware/vpsadminos`: removed the completed
  vpsadminos feature worktree.
- `rmdir worktrees/2026-06-03-el8-image-firmware`: removed the empty initiative
  worktree parent directory.

## Findings

- Upstream AlmaLinux 8 and Rocky 8 `core` comps metadata includes
  `linux-firmware`, multiple `iwl*-firmware` packages, and `microcode_ctl` as
  default packages.
- These packages are not needed in container images because containers use the
  host kernel and hardware initialization.
- The same reasoning applies to CentOS Stream images; current CentOS 9 Stream
  is close to the proposed size threshold in the live repository.
- In `osctld/restart`, killing osctld while `osctl ct top` waits in
  `recv(2)` can produce `Errno::ECONNRESET` instead of EOF, depending on Unix
  socket teardown timing. The command already exits; the flaky part was the
  unnormalized client error message.

## Changes

- `image-scripts/include/redhat-family.sh`: for `almalinux`, `centos`, and
  `rocky`, set yum/dnf excludes for `*-firmware` and `microcode_ctl`.
- `image-scripts/tests/rootfs_size.sh`: fail image tests when the created
  container root dataset uses more than 1 GiB.
- `osvm/lib/osvm/machine.rb`: restore the 900 second default timeout and nil
  fallback.
- `test-runner/lib/test-runner/cli/app.rb`: restore 900 second default CLI
  timeouts for `test` and `debug`.
- `test-runner/man/man1/test-runner.1.md`: document the 900 second default.
- `osctl/lib/osctl/client.rb`: normalize `Errno::ECONNRESET` from
  `UNIXSocket#recv` to the existing `osctld closed connection` client error.
- `osctl/spec/osctl/client_spec.rb`: cover socket reset handling.
- `os/packages/*`: rebuilt packaged gems to
  `25.11.0.build20260603210657`.

## Commits

- `91969db22` `image-scripts: exclude firmware from EL rebuilds`
- `7e49ab3ae` `image-scripts: check rootfs size in image tests`
- `cd8f654d6` `osvm, test-runner: restore 15-minute command timeout`
- `7018f568a` `osctl: treat reset osctld socket as closed connection`
- `a0adfcf74` `os: update gems to 25.11.0.build20260603210657`

## Cleanup

- Temporary staging merge worktree was removed after push.
- Feature worktree was removed after the user requested cleanup.
- Local branch `2026-06-03-el8-image-firmware` remains at `a0adfcf748`, the
  same commit as `origin/staging`.
- Plan, state, and durable notes remain under `work/` and `notes/`.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
