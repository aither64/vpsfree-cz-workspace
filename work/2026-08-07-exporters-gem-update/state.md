# 2026-08-07 exporters gem update

## Repositories

- `ssh-exporter`
  - Branch: `2026-08-07-exporters-gem-update`
  - Worktree: `worktrees/2026-08-07-exporters-gem-update/ssh-exporter`
  - Base: `origin/master` at `b7577a544e52d967f064309cb2198c2784d5c6fd`
- `syslog-exporter`
  - Branch: `2026-08-07-exporters-gem-update`
  - Worktree: `worktrees/2026-08-07-exporters-gem-update/syslog-exporter`
  - Base: `origin/master` at `f3f7a7aeb31f2ee8c850ebe5f8cda42c3587f052`
- `vpsfree-cz-configuration`
  - Branch: `2026-08-07-exporters-gem-update`
  - Worktree: `worktrees/2026-08-07-exporters-gem-update/vpsfree-cz-configuration`
  - Base: `origin/master` at `3c3de36a1adf8dee2ba5938d2a3921123e009c9e`

## Status

- Complete: all changes are committed, verified, pushed, and integrated into
  the three upstream `master` branches.
- Selected targets: Ruby 3.4, Puma 8.0.2, and exact Git pins for both
  configuration packages.
- Mandatory change review skipped under the dependency-only exemption: the
  commits change dependency and compatibility metadata, CI version selection,
  and generated package locks, with no application code or design change.

## Commands run

- `bin/dev-session current`
- Fetched all three canonical bare repositories from their SSH remotes.
- Inspected repository guidance, dependency manifests, package definitions,
  service modules, affected hosts, release history, and upstream advisories.
- Resolved and tested the proposed Puma 8 dependency set in disposable Nix
  toolchains during planning.
- Created all three initiative worktrees with `bin/dev-session worktree add`.
- In both exporter worktrees: resolved dependencies, ran RSpec and Rake, built
  gems, installed and ran Overcommit, ran full RuboCop, actionlint, and
  Bundler Audit, and pushed the feature branches.
- In vpsfree-cz-configuration: installed Overcommit in `nix develop`, ran
  Bundix and nixfmt for both packages, ran package-lock audits and hooks, built
  both package derivations, and smoke-tested Puma root and metrics endpoints.
- Ran `nix flake check --no-build --accept-flake-config`.
- Ran targeted confctl builds for `cz.vpsfree/machines/build` and
  `cz.vpsfree/containers/prg/int.log`.
- Reproduced the build-machine failure from an untouched detached
  `origin/master` worktree.
- Inspected GitHub Actions runs for both exporter feature branches.
- Created fresh integration worktrees, merged only with `git merge --ff-only`,
  repeated repository checks, and pushed exporter masters before
  vpsfree-cz-configuration master.
- Removed all initiative feature, integration, and detached diagnostic
  worktrees after moving generated caches to the task-specific temporary
  directory.

## Results

- Planning trials resolved Puma 8.0.2, Rack 3.2.6, prometheus-client 4.2.5,
  and nio4r 2.7.5 under Ruby 3.4.9.
- The planning trials passed 7 ssh-exporter examples and 17 syslog-exporter
  examples, plus both default Rake tasks.
- The current nixos-stable input resolves Ruby 3.4.9.
- The configuration worktree checkout hook returned nonzero because locked
  Overcommit gems were absent from the ambient shell. The worktree was created
  correctly at the intended commit. Existing workspace notes document this
  behavior; hook installation and execution will use `nix develop`.
- Initial exporter hook runs exposed that ad-hoc `gem install rubocop` fails
  to build Prism 1.9.0 under Nixpkgs Ruby 3.4.9. Both shells now use the
  Nix-provided RuboCop package and retain local Overcommit installation. The
  reusable workaround is documented in
  `notes/cross-project/2026-08-07-ruby34-rubocop-prism-nix.md`.
- Exporter commits:
  - `ssh-exporter` `c1b481a68e00d90802aeb36730c68a19f3c17711`
  - `syslog-exporter` `7c5a8e74e44a704cceb99cd05716af6800d78efd`
- Configuration commits:
  - `e545e369b17657e8772d293208340dced4106e1d`
    `ssh-exporter: update dependencies`
  - `c3e7fbf3c792b400cd0e7787e5863bd02c10dc7c`
    `syslog-exporter: update dependencies`
- Both generated locks contain Puma 8.0.2, Rack 3.2.6,
  prometheus-client 4.2.5, and nio4r 2.7.5. Bundler Audit found no
  vulnerabilities against ruby-advisory-db `36427421`.
- Both Nix package derivations built. Each packaged Puma reported 8.0.2 and
  served HTTP `OK` plus a Prometheus metrics response using a minimal config.
- `nix flake check --no-build` passed with the existing unknown `confctl`
  output warning.
- `confctl build -y cz.vpsfree/containers/prg/int.log` passed as generation
  `2026-08-07--16-47-00`.
- `confctl build -y cz.vpsfree/machines/build` is blocked by an infinite
  recursion in vpsadminos `os/overlays/osctl.nix`. The same command fails at
  untouched configuration `origin/master` `3c3de36a`, proving the exporter
  commits are not the cause. The reusable evidence is recorded in
  `notes/vpsfree-cz-configuration/2026-08-07-build-machine-osctl-recursion.md`.
- GitHub Actions RSpec passed for SSH run `31188664033` and syslog run
  `31188664513`, both on the expected feature heads.
- Integration-worktree checks repeated successfully for both exporters:
  RSpec, Rake, full RuboCop, Overcommit, actionlint, Bundler Audit, and Puma
  version checks all passed.
- Configuration integration checks repeated successfully: Overcommit,
  package-lock audits, nixfmt, flake evaluation, both package builds, Puma
  version checks, and `int.log` generation `2026-08-07--16-52-24`.
- Upstream master heads:
  - `ssh-exporter` `c1b481a68e00d90802aeb36730c68a19f3c17711`
  - `syslog-exporter` `7c5a8e74e44a704cceb99cd05716af6800d78efd`
  - `vpsfree-cz-configuration`
    `c3e7fbf3c792b400cd0e7787e5863bd02c10dc7c`
- Master GitHub Actions RSpec passed for SSH run `31189637404` and syslog run
  `31189639318`. vpsfree-cz-configuration has no push-triggered workflow; its
  next scheduled Daily update remains an end-to-end updater check.

## Open questions

- None.

## Cleanup

- Removed all worktrees under
  `worktrees/2026-08-07-exporters-gem-update/` and the detached baseline
  worktree.
- Moved generated gem, Bundler, RuboCop, build, and confctl caches to
  `/tmp/vpsfree-exporters-gem-update/`; none were committed.
- Preserved local and remote feature branches as required. Local integration
  branches were also preserved at the merged heads.
