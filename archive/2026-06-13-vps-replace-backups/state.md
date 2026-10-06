---
lifecycle: abandoned
---
# 2026-06-13-vps-replace-backups

## Repositories

- `vpsadmin`
  - branch: `2026-06-13-vps-replace-backups`
  - worktree: `worktrees/2026-06-13-vps-replace-backups/vpsadmin`
  - base: `origin/master` at `82f39b525`
  - remote: `git@github.com:vpsfreecz/vpsadmin.git`
- `vpsadminos`
  - branch: `2026-06-13-vps-replace-backups`
  - worktree: `worktrees/2026-06-13-vps-replace-backups/vpsadminos`
  - base: `origin/staging` at `a9e857bb9`
  - remote: `git@github.com:vpsfreecz/vpsadminos.git`
- `vpsfree-cz-configuration`
  - branch: `2026-06-13-vps-replace-backups`
  - worktree:
    `worktrees/2026-06-13-vps-replace-backups/vpsfree-cz-configuration`
  - base: `origin/master` at `46a0c48f`
  - remote: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`
- workspace instructions
  - branch: `2026-06-13-vps-replace-backups`
  - worktree: `.`
  - base: `origin/master`
  - remote: `git@github.com:aither64/vpsfree-cz-workspace.git`

## Current Status

- Worktrees are prepared and repository-local `AGENTS.md` files have been read.
- Implementation is committed in all three repositories:
  - `vpsadmin`: API, replace chain, storage/nodectld commands, unit specs,
    integration tests, and vpsAdminOS flake pin.
  - `vpsadminos`: osctld/osctl use the existing remote `from-snapshot`
    behavior and add matching `from-snapshot` support to local copy.
  - `vpsfree-cz-configuration`: production hook skips backup provisioning for
    VPS replacement when old backups are being moved.
- The design was changed after review: osctld now carries the vpsAdmin
  continuity snapshot into the replacement dataset. vpsAdmin no longer
  post-copy-sends that snapshot with low-level `Dataset::Send`/port
  reservation transactions.
- vpsAdmin verifies the continuity snapshot on the replacement dataset with
  `Storage::RecvCheck` before creating replacement-side `SnapshotInPool` rows
  and before rewiring backup DB ownership.
- Review follow-up on 2026-06-14 removed the vpsAdmin-specific
  `preserve-snapshot` osctld option and removed the remote `target_dataset`
  receive override entirely. Remote replacement relies on osctld's deterministic
  target dataset placement from target pool and VPS id.
- Integration tests now verify database snapshot rows against ZFS snapshot
  names for source, backup, and replacement datasets. A remote VPS replacement
  integration test has been added.
- Local-only documentation commits were added after the implementation push:
  - top-level `AGENTS.md` now requires the `mandatory-change-review` skill for
    relevant code/design changes before long integration tests.
  - `skills/mandatory-change-review` was added and validated.
  - vpsAdminOS/vpsAdmin `AGENTS.md` now document that vpsAdminOS is an
    independent general-purpose project, even though vpsAdmin is its main
    consumer.
- The vpsAdmin web UI/API metadata for VPS replacement backup preservation was
  adjusted so checkbox descriptions expand the labels instead of repeating
  them. This follow-up was squashed into the local web UI commit.
- The workspace vpsAdmin devcluster configuration now disables nodectld
  `zfs_send`/`zfs_recv` queue start delays by default using
  `nodectld.zfsTransferStartDelay = 0`, so manual VPS replacement/backup
  testing does not wait for the production 90-minute transfer pacing.
- Devcluster SSH helper ergonomics were updated locally:
  - `dev-clusters/vpsadmin/bin/devcluster ssh` and
    `dev-clusters/vpsadminos/bin/devcluster ssh` now accept the current
    `VPSFREE_DEV_SESSION_SLUG` when the slug is omitted.
  - Both helpers still support explicit `ssh <slug> <node>`.
  - User-facing `ssh` accepts extra SSH options before `--` and a remote
    command after `--`, e.g. `devcluster ssh node1 -t -- bash -l`.
- On 2026-06-15, `vpsadminos` was rebased onto current `origin/staging`,
  force-pushed with lease at `e2b5a7a98`, and vpsAdmin's flake input was
  updated to that exact revision. The vpsAdmin flake history was squashed back
  to one flake input update commit.
- `vpsfree-cz-configuration` was rebased onto current `origin/master`.
- The mandatory review skill now requires review of repeated flake input
  updates and repeated gem dependency/Bundix/Gemfile.lock update commits in a
  feature branch.

## Branch Heads

- workspace instructions: `aefd23f`
  - `6e96b0c workspace: add mandatory change review skill`
  - `fefeb3f devcluster: fix vpsAdmin cluster startup`
  - `55e34e8 workspace: prefer bridge vpsAdmin devclusters`
  - `a9f98fd workspace: require transfer integrity review`
  - `a98bdb9 devcluster: disable transfer queue delay by default`
  - `a63d05d devcluster: use active session for ssh`
  - `b9303da workspace: clarify mandatory change review instructions`
  - `39750da devcluster: grant default pool devices on refresh`
  - `5e835d0 workspace: review repeated dependency updates`
  - `aefd23f workspace: review repeated gem updates`
- `vpsadminos`: local and remote
  `origin/2026-06-13-vps-replace-backups` at `e2b5a7a98`
  - `801151d68 osctld: copy containers from selected snapshot`
  - `a8e5d43b4 tests/firewall: wait for reload to finish`
  - `631c94418 docs: describe vpsAdmin integration boundary`
  - `e2b5a7a98 docs: require transfer integrity assertions`
- `vpsadmin`: local `f3e1ff0d0`, remote still stale until next push
  - `f226cec88 api: preserve backups during VPS replace`
  - `fd6146226 tests: verify VPS replacement backup data integrity`
  - `d3b1b97cf flake: vpsadminos 6f9b2c755 -> e2b5a7a98`
  - `0912827e6 docs: describe vpsAdminOS integration boundary`
  - `f159d4aa4 docs: require VPS transfer data integrity tests`
  - `f3e1ff0d0 webui: expose VPS replace backup options`
- `vpsfree-cz-configuration`: local and remote at `5fafb818`
  - `5fafb818 vpsadmin-config: skip replacement backup provisioning`

## Commands Run

- Session/worktree setup:
  - `bin/dev-session current`
  - `git --git-dir=repos/vpsadmin.git fetch origin --prune`
  - `git --git-dir=repos/vpsadmin.git worktree add -b
    2026-06-13-vps-replace-backups
    worktrees/2026-06-13-vps-replace-backups/vpsadmin origin/master`
  - `git --git-dir=repos/vpsadminos.git fetch origin --prune`
  - `git --git-dir=repos/vpsadminos.git worktree add -b
    2026-06-13-vps-replace-backups
    worktrees/2026-06-13-vps-replace-backups/vpsadminos origin/staging`
  - `git --git-dir=repos/vpsfree-cz-configuration.git fetch origin --prune`
  - `git --git-dir=repos/vpsfree-cz-configuration.git worktree add -b
    2026-06-13-vps-replace-backups
    worktrees/2026-06-13-vps-replace-backups/vpsfree-cz-configuration
    origin/master`

- vpsAdmin focused specs:
  - `nix develop .#api -c bundle exec rspec
    spec/models/transaction_chains/vps/replace/os_spec.rb`
    - latest result: 12 examples, 0 failures.
  - `nix develop .#api -c bundle exec rspec
    spec/models/transaction_chains/vps/replace/os_spec.rb
    spec/api/resources/vps_write_spec.rb
    spec/models/transactions/vps/send_config_spec.rb`
    - latest result: 134 examples, 0 failures.
  - `VPSADMINOS_PATH=.../vpsadminos nix develop .#libnodectld --impure -c
    bundle exec rspec
    spec/nodectld/commands/vps/copy_spec.rb
    spec/nodectld/commands/vps/send_config_spec.rb
    spec/nodectld/commands/dataset/recv_check_spec.rb
    spec/nodectld/commands/dataset/group_snapshot_spec.rb
    spec/nodectld/commands/dataset/rename_spec.rb`
    - latest result: 16 examples, 0 failures.
  - `VPSADMINOS_PATH=.../vpsadminos nix develop .#libnodectld --impure -c
    bundle exec rspec spec/nodectld/commands/vps/send_config_spec.rb`
    - latest result: 2 examples, 0 failures.
  - Review follow-up focused specs on 2026-06-14:
    - `nix develop .#api -c bundle exec rspec
      spec/models/transaction_chains/vps/replace/os_spec.rb
      spec/models/transactions/vps/send_config_spec.rb`
      - latest result: 14 examples, 0 failures.
    - `VPSADMINOS_PATH=.../vpsadminos nix develop .#libnodectld --impure -c
      bundle exec rspec
      spec/nodectld/commands/vps/copy_spec.rb
      spec/nodectld/commands/vps/send_config_spec.rb
      spec/nodectld/commands/dataset/recv_check_spec.rb`
      - latest result: 8 examples, 0 failures.

- vpsAdminOS focused specs:
  - Initial root-level `nix develop -c bundle exec rspec ...` failed because
    the root vpsAdminOS Gemfile contains tooling gems but not `rspec`.
    Correct invocation is from each gem directory.
  - From `vpsadminos/osctl`:
    `nix develop .. -c bundle exec rspec
    spec/osctl/cli/container_spec.rb spec/osctl/cli/send_spec.rb`
    - latest result: 20 examples, 0 failures.
  - From `vpsadminos/osctld`:
    `nix develop .. -c bundle exec rspec
    spec/osctld/local_transfer/log_spec.rb
    spec/osctld/send_receive/log_spec.rb
    spec/osctld/commands/container/local_transfer_spec.rb
    spec/osctld/commands/container/recovery_and_send_spec.rb`
    - latest result: 58 examples, 0 failures.
  - From `vpsadminos/osctld`:
    `nix develop .. -c bundle exec rspec
    spec/osctld/send_receive/commands/receive_skel_spec.rb`
    - latest result: 15 examples, 0 failures.
  - From `vpsadminos/osctld`:
    `nix develop .. -c bundle exec rspec
    spec/osctld/commands/container/provisioning_spec.rb`
    - latest result after updating the copy expectation: 16 examples,
      0 failures.
  - Review follow-up focused specs on 2026-06-14:
    - From `vpsadminos/osctl`:
      `nix develop .. -c bundle exec rspec
      spec/osctl/cli/container_spec.rb spec/osctl/cli/send_spec.rb`
      - latest result: 20 examples, 0 failures.
    - From `vpsadminos/osctld`:
      `nix develop .. -c bundle exec rspec
      spec/osctld/local_transfer/log_spec.rb
      spec/osctld/send_receive/log_spec.rb
      spec/osctld/send_receive/hook_spec.rb
      spec/osctld/send_receive/commands/receive_skel_spec.rb
      spec/osctld/commands/container/local_transfer_spec.rb
      spec/osctld/commands/container/recovery_and_send_spec.rb
      spec/osctld/commands/container/provisioning_spec.rb`
      - latest result: 93 examples, 0 failures.
    - Local test setup note: `libosctl` is loaded from the dirty worktree for
      these focused specs, so `nix develop .. -c bundle exec rake compile` was
      run in `vpsadminos/libosctl` before rerunning specs.
  - A full `osctld` spec run from the gem shell was attempted, but local
    execution cannot load the `lxc` native extension for console/container
    control specs. CI remains the authority for the full suite; focused specs
    covering touched behavior pass locally.

- Integration tests:
  - `./test-runner.sh test vps/replace-with-backups-remote`
    - First rerun failed after 879.05s because nodectld emitted
      `--target-dataset`, while osctl exposes `--to-dataset`.
    - Root cause: transaction payload name and osctl CLI option name differ;
      nodectld must translate `target_dataset` to `to_dataset`.
    - Superseded by 2026-06-14 review follow-up: remote `target_dataset` and
      `--to-dataset` support have been removed from this branch.
    - Latest result after the nodectld fix: successful in 885.07s.
    - After removing remote `target_dataset`, rerun failed in 930.38s. Root
      cause: the test created a destination vpsAdmin hypervisor pool at
      `tank/ct-replace-backups-remote`, but osctld remote send was given pool
      `tank` and deterministically received into `tank/ct/2`. vpsAdmin then
      correctly failed `RecvCheck` against its DB path
      `tank/ct-replace-backups-remote/2`.
    - Fixed the remote replace tests to use `primary_pool_fs` for destination
      hypervisor pools, matching osctld's real container dataset root.
    - Latest result after the test layout fix: successful in 866.47s.
  - `./test-runner.sh test vps/replace-with-backups`
    - Latest result after the 2026-06-14 redesign: successful in 609.96s.
  - `./test-runner.sh test firewall/conntrack#no-conntrack`
    - CI failure root cause was a pre-existing test race: `sv 1 firewall`
      sends the reload signal and can return before the control script has
      rebuilt all firewall chains. The randomized CI order ran the reload
      example first and the protected-rule shape assertion last, exposing a
      partially reloaded ruleset.
    - Fixed by waiting for the reload-ready state: exactly two notrack rules
      and both protected refuse rules present.
    - Latest local result after cleaning ignored Ruby build outputs:
      successful in 252.12s.

- Syntax/diff checks:
  - `ruby -c` on touched vpsAdmin API/nodectld Ruby files: all `Syntax OK`.
  - `ruby -c` on touched vpsAdminOS osctl/osctld Ruby files: all `Syntax OK`.
  - `git diff --check` in `vpsadmin`: clean.
  - `git diff --check` in `vpsadminos`: clean.
  - Web UI/API metadata follow-up on 2026-06-14:
    - `ruby -c api/lib/vpsadmin/api/resources/vps.rb`
      - latest result: `Syntax OK`.
    - `git diff --check` in `vpsadmin`: clean.
    - `rg -n "Move existing backup datasets|Back up a replacement snapshot"
      /nix/store/lh6717990bip9qb4qnxs6c0v6jsni19d-vpsadmin-api-dev/api/lib/vpsadmin/api/resources/vps.rb`
      - latest result: both updated descriptions are present in the rebuilt
        API package.
  - Devcluster queue delay follow-up on 2026-06-14:
    - `ruby -rjson -e 'JSON.parse(File.read(ARGV.fetch(0)))'
      dev-clusters/vpsadmin/default-config.json`
      - latest result: success.
    - `nix shell nixpkgs#nixfmt-rfc-style -c nixfmt --check
      dev-clusters/vpsadmin/nix/test.nix dev-clusters/vpsadmin/flake.nix`
      - latest result: success. Nix warned that `nixfmt-rfc-style` is now the
        same as `pkgs.nixfmt`.
    - `git diff --check -- dev-clusters/vpsadmin/default-config.json
      dev-clusters/vpsadmin/nix/test.nix dev-clusters/vpsadmin/README.md`
      - latest result: clean.
  - `nix develop -c bundle exec rubocop configs/vpsadmin/api/hooks.rb`
    in `vpsfree-cz-configuration`: no offenses.
  - `nix develop -c bundle exec rubocop
    osctld/spec/osctld/commands/container/provisioning_spec.rb`
    in `vpsadminos`: no offenses.
  - `nix develop -c nixfmt --check tests/suite/firewall/conntrack.nix`
    in `vpsadminos`: clean.
  - `nix develop -c overcommit --run` in `vpsadminos`: Nixfmt and RuboCop
    passed.
  - Review follow-up on 2026-06-14:
    - `git diff --check` in `vpsadmin`: clean.
    - `git diff --check` in `vpsadminos`: clean.
    - `nix develop -c overcommit --run` in `vpsadmin`: passed. The run
      temporarily reformatted unrelated WebUI PHP files; that generated churn
      was reverted before committing.
    - `nix develop -c overcommit --run` in `vpsadminos`: passed after fixing
      one RuboCop style offense in `send_receive/hook_spec.rb`.
  - Final `nix develop -c overcommit --run` after history rewrites passed
    in both `vpsadmin` and `vpsadminos`. The vpsAdmin PHP fixer again
    reformatted unrelated WebUI files; the generated churn was reverted.
  - Local-only AGENTS follow-up:
    - `nix develop -c overcommit --run` in `vpsadminos`: passed.
    - `nix develop -c overcommit --run` in `vpsadmin`: passed. The vpsAdmin
      PHP fixer again reformatted unrelated WebUI files; the generated churn
      was reverted.
    - `nix shell --impure --expr 'with import <nixpkgs> {};
      python3.withPackages (ps: [ ps.pyyaml ])' -c python3
      /home/aither/.codex/skills/.system/skill-creator/scripts/quick_validate.py
      /home/aither/workspace/ai/vpsfree.cz/skills/mandatory-change-review`:
      skill is valid.

## Mandatory Review

- Ran `mandatory-change-review` with standalone agent
  `019ec660-6a4e-7891-bed6-31cd590860e7` after fixing the skill to forbid
  nested reviewers.
- Result:
  - Blocking: none.
  - Important: none.
  - Advisory:
    - `vpsadminos` commit `fe57c2bb8` has two overlong commit-message body
      lines. Because that commit is already part of the pushed vpsAdminOS hash
      and vpsAdmin currently pins that pushed hash, defer rewriting until final
      integration/push planning. Rewriting it cleanly requires a new
      vpsAdminOS remote hash and then a corresponding vpsAdmin flake-lock
      refresh.
    - `vpsadminos` commit `f49f4180d` fixes an unrelated firewall test race.
      It is isolated and documented; call it out separately during review or
      land it separately if scope requires.
    - Fresh-reinstall/no-common-backup-head and active concurrent-backup
      conflict coverage is mostly indirect through existing
      `Dataset::Transfer` behavior and dataset locks.
- Action taken:
  - Updated `plan.md` to remove stale references to the abandoned
    `preserve_snapshot`, `--to-dataset`, remote `target_dataset`, and
    `skel_dataset` design.
  - Updated `mandatory-change-review` so spawned standalone reviewers do the
    review directly and must not launch nested reviewers/subagents.
  - Extended `mandatory-change-review` to require explicit review of testing
    adequacy, including unit/spec coverage, integration coverage, and
    non-golden paths such as unexpected input, missing/conflicting state,
    rollback/error paths, authorization failures, mixed-version flows, and
    repeated or partially completed operations.
- Ran a follow-up `mandatory-change-review` with standalone agent
  `019ec731-236a-7fa2-ab77-02c684cee02a` for the local, not-yet-pushed
  follow-up commits after the webui form fix and CI-layout fix.
- Follow-up review result:
  - Blocking: none.
  - Important: none.
  - Advisory: none.
  - Reviewer confirmed that the webui exposes/submits both backup preservation
    flags, the descendant replace test now aligns with osctld's deterministic
    receive layout without reintroducing target-dataset behavior, and transfer
    integrity assertions are retained.
  - Residual risks recorded by the reviewer: `webui#vps-admin-ops` still needs
    final CI or local Playwright confirmation after `f80c988f4`; broader
    mixed-version deployment still requires vpsAdminOS/osctld local
    `from_snapshot` support for default same-node history-preserving replace.

## Notable Fixes During Redesign

- `confirm_replacement_snapshot` originally called `t.create(...)` inside a
  `RecvCheck` confirm block. In this transaction DSL the block's receiver is
  the confirmation helper and the block argument is the transaction, so the
  correct call is `create(...)`. The focused API suite caught this.
- vpsAdminOS focused specs must be run from `osctld` and `osctl` gem
  directories, not from the repository root.
- A spec expectation for remote send initially expected relative dataset name
  `/`, but `SendRootfs` records root dataset relative name as `ct1` in that
  call path. The spec was corrected.
- GitHub vpsAdminOS RSpec for commit `e9b381cd2` failed only because the
  full provisioning spec still expected the old `CopyConfig` argument list and
  did not include `preserve_snapshot: nil`. Commit `46c738b0a` fixes the stale
  expectation.
- GitHub vpsAdminOS CI for commit `e9b381cd2` failed in
  `firewall/conntrack#no-conntrack`, unrelated to VPS replace changes. Logs
  showed the traffic checks succeeded, but the final rule-shape check returned
  `0` after the reload example had run first. Commit `3bbec714c` fixes the
  async reload wait in the test.

## Current Validation

- Focused tests are green:
  - vpsAdmin API/model replace coverage.
  - vpsAdmin nodectld command coverage.
  - vpsAdminOS osctl/osctld local-copy and remote-send `from-snapshot`
    coverage.
- vpsAdminOS follow-up focused provisioning spec is green.
- vpsAdminOS isolated firewall reload-race regression is green locally.
- Whitespace checks are clean.
- Same-node and remote backup-preserving integration tests were green after
  the 2026-06-14 redesign and vpsAdminOS flake pin update. They have not been
  rerun after the final review-remediation assertion update that discovers the
  standard datetime replacement snapshot name from DB labels; only quick
  formatting/hook checks were rerun for that assertion-only change.
- `skills/mandatory-change-review` validates through the skill-creator
  `quick_validate.py` helper in a Nix Python shell with PyYAML.
- Edited vpsAdmin replacement-backup Nix tests parse with `nix-instantiate
  --parse`.
- On 2026-06-14 review remediation:
  - vpsAdmin replacement-backup tests were reformatted with
    `nix develop -c nixfmt --check
    tests/suite/storage/remote-common.nix
    tests/suite/vps/replace-with-backups.nix
    tests/suite/vps/replace-with-backups-remote.nix`.
  - vpsAdminOS passed `nix develop -c overcommit --run` after rebase onto
    `origin/staging` at `71b06c976`.
  - `vpsfree-cz-configuration` passed `nix develop -c overcommit --run` after
    rebase onto `origin/master` at `46a0c48f`.
  - vpsAdmin passed `nix develop -c overcommit --run` after the flake/test
    history rewrite. PhpCsFixer reformatted unrelated WebUI files again; that
    generated diff was reversed with `git apply -R`.
  - vpsAdmin flake lock points to vpsAdminOS
    `03b686f7172d9666c4d3574c93da864859f3445c` and has a single flake input
    update commit in the feature branch.

## Devcluster

- The first demo cluster was mistakenly started with network `local`; it was
  stopped, reset, and restarted with the default `bridge` network.
- Running devcluster `2026-06-13-vps-replace-backups`:
  - topology `dual`;
  - network `bridge`;
  - services IP `172.16.106.53`;
  - node1 IP `172.16.106.41`;
  - node2 IP `172.16.106.42`.
- Local devcluster fixes committed in the top-level workspace as `fefeb3f`,
  not pushed:
  - `dev-clusters/vpsadmin/flake.nix` now imports the current vpsAdminOS
    overlay function with `netlinkrb` and `ruby-lxc`.
  - `dev-clusters/vpsadmin/flake.nix` gives the devcluster runner Bundler
    environment `pkgs.vpsadminosRubyGemConfig`, so local first-party gems do
    not need missing gem `sha256` values.
  - `dev-clusters/vpsadmin/nix/test.nix` skips missing optional mail-template
    names when creating dev mail recipients. Without this, the services VM
    database seed failed before API startup.
- Bridge-default guidance committed in the top-level workspace as `55e34e8`.
- The cluster is reachable on normal bridge-network URLs:
  - Web UI: `https://webui.aitherdev.int.vpsfree.cz/`
  - API: `https://api.aitherdev.int.vpsfree.cz/`
  - CA: `.dev-clusters/vpsadmin/certs/default/vpsadmin-ca.crt`
  - SSH via bridge IPs using `.dev-clusters/vpsadmin/ssh/id_ed25519`.
- Prepared VPS for manual replace testing:
  - VPS `#1`, hostname `replace-demo-1`, owner `test-user1`, stopped on
    `dev-node1.lab` (`node_id=101`).
  - Suggested remote replacement target: `dev-node2.lab` (`node_id=102`).
  - Source dataset: `tank/ct/1`, dataset `#1`, source DIP `#1`.
  - Backup pool: `tank/backup-replace-demo`, pool `#3`, backup DIP `#2`.
  - Migration keys generated with chain `#7` for all pools.
- Snapshot/backup layout:
  - Snapshot `#1` `2026-06-14T16:12:31`, label
    `dev replace demo snapshot 1 backed up`, present on source and backup.
  - Snapshot `#2` `2026-06-14T16:13:17`, label
    `dev replace demo snapshot 2 backed up incrementally`, present on source
    and backup.
  - Snapshot `#3` `2026-06-14T16:13:59`, label
    `dev replace demo snapshot 3 local only`, present on source only.
  - Source DIP snapshot limit is set to `max_snapshots=2` after creating the
    three snapshots, so VPS replace should exercise the limit-bypass path.
- Verification:
  - `osctl ct show 1` on node1 reports state `stopped`.
  - ZFS source snapshots exist on `tank/ct/1`.
  - ZFS backup snapshots exist under
    `tank/backup-replace-demo/1/tree.0/branch-2026-06-14T16:12:32.0`.
  - API rows show snapshots `#1` and `#2` confirmed in both source and backup
    pools, and snapshot `#3` confirmed only in the source pool.
  - Known-content files exist in the source dataset:
    `snapshot-1-backed-up.txt`, `snapshot-2-backed-up.txt`, and
    `snapshot-3-local-only.txt`.
  - The devcluster services were updated after commit `f80c988f4`; the
    deployed webui form contains the `preserve_backups` and
    `preserve_backup_history` checkboxes and the submit handler sends both API
    flags. Their API descriptions are now:
    - `preserve_backups`: `Move existing backup datasets to the replacement
      VPS`.
    - `preserve_backup_history`: `Back up a replacement snapshot so future
      backups can continue incrementally`.
  - `dev-clusters/vpsadmin/bin/devcluster update
    2026-06-13-vps-replace-backups services` completed successfully after the
    description follow-up and restarted the services VM.
  - The rebuilt API store path
    `/nix/store/lh6717990bip9qb4qnxs6c0v6jsni19d-vpsadmin-api-dev` contains
    both updated descriptions.
  - The devcluster config was extended with
    `nodectld.zfsTransferStartDelay = 0` and node generation writes that value
    to `vpsadmin.nodectld.settings.vpsadmin.queues.zfs_send.start_delay` and
    `zfs_recv.start_delay`.
  - `dev-clusters/vpsadmin/bin/devcluster update
    2026-06-13-vps-replace-backups node1` completed successfully and restarted
    `nodectld`, `osctld`, and `prometheus-osctl-exporter` on node1.
  - `dev-clusters/vpsadmin/bin/devcluster update
    2026-06-13-vps-replace-backups node2` completed successfully and restarted
    `nodectld`, `osctld`, and `prometheus-osctl-exporter` on node2.
  - Live verification over bridge SSH confirmed `/etc/vpsadmin/nodectld.yml`
    has `start_delay: 0` for both `zfs_send` and `zfs_recv` on node1 and
    node2; `nodectl status` reports both nodes running and does not show any
    queue start-delay status for those queues.

### 2026-06-14 standard replace snapshot names

- Local vpsAdmin commit:
  - `3efb52e5f api: use standard replace snapshot names`
- Design adjustment:
  - Removed the replace-specific `vps-replace-...` ZFS snapshot name from the
    VPS replace flow.
  - `Dataset::GroupSnapshot` again lets nodectld generate the final standard
    datetime snapshot name and persist it to the database.
  - VPS copy/send transactions can now carry an unconfirmed snapshot reference
    (`id`, provisional `name`, `confirmed` state). `nodectld` resolves the
    final name with `get_confirmed_snapshot_name` before calling `osctl`, like
    storage send/recv already do.
  - Replacement-side cloned `Snapshot` rows are synced after backup rewiring
    with `Transactions::Storage::CloneSnapshotName`, extended to copy
    `created_at` as well as `name`, so DB metadata follows the source snapshot
    once nodectld has finalized it.
  - Snapshot labels remain the place where VPS replacement context is recorded.
- Checks:
  - Syntax:
    `ruby -c` on touched API and libnodectld Ruby files.
  - Whitespace:
    `git diff --check`.
  - API focused specs:
    `nix develop .#api -c bundle exec rspec
    spec/models/transaction_chains/dataset/group_snapshot_spec.rb
    spec/models/transactions/vps/send_config_spec.rb
    spec/models/transaction_chains/vps/replace/os_spec.rb`
    completed with 20 examples, 0 failures.
  - libnodectld focused specs:
    `VPSADMINOS_PATH=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-13-vps-replace-backups/vpsadminos
    nix develop .#libnodectld --impure -c bundle exec rspec
    spec/nodectld/commands/dataset/group_snapshot_spec.rb
    spec/nodectld/commands/dataset/clone_snapshot_name_spec.rb
    spec/nodectld/commands/vps/copy_spec.rb
    spec/nodectld/commands/vps/send_config_spec.rb`
    completed with 13 examples, 0 failures.
  - vpsAdmin pre-commit hooks ran during commit through `nix develop`:
    Nixfmt OK, RuboCop OK. Commit-msg hooks passed with warnings only for
    the hook's stricter 72-column preference; message lines are within the
    workspace 80-column rule.
  - Building `libosctl/native` was needed locally before running
    libnodectld specs against the vpsAdminOS checkout. The generated
    `vpsadminos/libosctl/tmp/` directory was removed afterwards.
- Dev cluster:
  - `dev-clusters/vpsadmin/bin/devcluster update
    2026-06-13-vps-replace-backups all` completed successfully.
  - Services VM, node1, node2, dns-primary, and dns-secondary were switched.
  - `nodectld`, `osctld`, and `prometheus-osctl-exporter` restarted on both
    nodes. DNS nodectld services restarted as part of the `all` update.
  - `dev-clusters/vpsadmin/bin/devcluster status
    2026-06-13-vps-replace-backups` reports `status: running`,
    `network: bridge`, and `ready: yes`.
  - URLs remain:
    - Web UI: `https://webui.aitherdev.int.vpsfree.cz/`
    - API: `https://api.aitherdev.int.vpsfree.cz/`
  - SSH helper checks after slugless SSH implementation:
    - `bash -n dev-clusters/vpsadmin/bin/devcluster`: passed.
    - `bash -n dev-clusters/vpsadminos/bin/devcluster`: passed.
    - `dev-clusters/vpsadmin/bin/devcluster ssh services -- hostname`:
      printed `vpsadmin-services`.
    - `dev-clusters/vpsadmin/bin/devcluster ssh node1 -- hostname`: printed
      `dev-node1`.
    - `dev-clusters/vpsadmin/bin/devcluster ssh
      2026-06-13-vps-replace-backups node1 -- hostname`: printed `dev-node1`.
    - `env -u VPSFREE_DEV_SESSION_SLUG
      dev-clusters/vpsadmin/bin/devcluster ssh services -- hostname`: printed
      `vpsadmin-services`, confirming fallback through
      `bin/dev-session current`.
    - `dev-clusters/vpsadmin/bin/devcluster ssh node1 -o BatchMode=yes --
      hostname`: printed `dev-node1`, confirming extra SSH options are passed
      before the target host.
    - `dev-clusters/vpsadminos/bin/devcluster status
      2026-06-13-vps-replace-backups` reported `status: stopped`, so no live
      vpsAdminOS SSH smoke was run.
  - Manual VPS 4 backup run on 2026-06-14:
    - `vpsadmin-schedulerctl` is present as `vpsadmin-schedulerctl` in the
      API package, not as `schedulerctl` in PATH. It must be called with
      `/var/lib/vpsadmin/api/scheduler.sock`.
    - The scheduler initially had no tasks, so a temporary `DatasetAction`
      (`backup`, source DIP 5, destination DIP 2) and `RepeatableTask` were
      created with an impossible cron schedule, registered, and run via
      `vpsadmin-schedulerctl ... run-task 1`.
    - The temporary action/task rows were removed after chain creation.
    - Backup chain `23` completed with state `done`, progress `5/5`.
      Transactions were queue reservations, `LocalSend`, and releases;
      rotation ran as part of `Dataset::Backup` but had nothing to prune.
    - DB state now has snapshot `2026-06-14T19:05:04` on both VPS 4 source
      DIP 5 and backup DIP 2. On disk, dev-node1 has it on
      `tank/ct/4@2026-06-14T19:05:04` and backup tree
      `tank/backup-replace-demo/4/tree.0/branch-2026-06-14T16:12:32.0@2026-06-14T19:05:04`.
    - Snapshot retention check after the manual backup:
      - Retention is stored on `dataset_in_pools`, not on `pools`.
      - The devcluster seed config does not set production-style snapshot
        retention for new DIPs. Schema defaults are `min_snapshots=14`,
        `max_snapshots=20`, and `snapshot_max_age=1209600`.
      - The manual replace demo DIPs were adjusted during preparation:
        hypervisor DIPs 1, 4, and 5 have `min_snapshots=0`,
        `max_snapshots=2`, and `snapshot_max_age=31536000`.
      - VPS 4 therefore kept both source snapshots after backup chain 23. It
        would need source DIP 5 `max_snapshots=1` to match production behavior
        where hypervisor-side rotation prunes down to the latest source
        snapshot after it is safely present in backup history.
    - Backup DIP 2 currently has `min_snapshots=0`, `max_snapshots=10`, and
      `snapshot_max_age=31536000`; this was also manual demo state, not
      devcluster seed configuration. Production-like backup retention would
      use `max_snapshots=20`.
  - After the user reinstalled VPS 4 and replaced it with VPS 5:
    - Reinstall chain `24` completed, then replace chain `28` completed.
    - VPS 4 is `soft_delete` and still owns source DIP 5 /
      `tank/ct/4`. Its DB snapshot row and ZFS snapshot
      `tank/ct/4@2026-06-14T19:20:18` remain.
    - VPS 5 is active and owns source DIP 6 / `tank/ct/5`. It has a separate
      DB snapshot row with the same snapshot name,
      `tank/ct/5@2026-06-14T19:20:18`.
    - Backup DIP 2 was moved to dataset 5 and the backup dataset was renamed
      to `tank/backup-replace-demo/5`. Old backup history remains in tree 0
      and the new replacement snapshot is in tree 1.
    - This is expected for the current implementation: VPS replacement marks
      the old VPS as `soft_delete` and does not destroy its source dataset or
      local snapshots. They remain tracked in the DB and visible until the old
      VPS progresses to `hard_delete`. `Vps::Destroy` then runs
      `DatasetInPool::Destroy` with `destroy: false` to clear DB rows and
      `Transactions::Vps::Destroy`/`osctl ct del` removes the old container
      dataset and its ZFS snapshots on vpsAdminOS.
- 2026-06-14 investigation of failed manual remote replace, VPS 5 to
  `dev-node2.lab`:
  - Failed chain: `TransactionChains::Vps::Replace::Os` chain `31`, failing
    transaction `Transactions::Vps::SendConfig` transaction `172`.
  - `SendConfig` used the confirmed on-disk replacement snapshot name
    `2026-06-14T20:04:50`; `tank/ct/5@2026-06-14T20:04:50` existed on node1,
    so this was not a replacement-snapshot name mismatch.
  - Node1 osctld logged the real receiver error from the SSH helper:
    `Error: device 'c 10:200 rwm' not available in group 'tank:/default'`.
    The `error: internal error` reported to nodectld was osctld trying to read
    the receive token after the receiver had exited without printing one.
  - Root cause: the devcluster directly seeds pool rows in the DB and its
    manual node refresh path skipped the device grants normally applied by the
    `pool create` chain, specifically
    `NodeCtld::Commands::Pool::Create#grant_device_access`.
  - Running node2 was patched with the standard `/default` device grants for
    `/dev/net/tun`, `/dev/fuse`, `/dev/ppp`, and `/dev/kvm`.
  - `dev-clusters/vpsadmin/bin/devcluster refresh` now applies the same
    grants idempotently, and the README documents that refresh prepares
    default pool device grants as well as pool working directories.
  - Verification:
    - `bash -n dev-clusters/vpsadmin/bin/devcluster`: success.
    - `dev-clusters/vpsadmin/bin/devcluster refresh
      2026-06-13-vps-replace-backups`: success, restarted nodectld on node1
      and node2.
    - `osctl --pool tank group devices ls /default` on both nodes now shows
      the four standard device grants before inherited defaults.
    - VPS 5 remains present on node1 as `tank:5` in `stopped` state. Node2 has
      no leftover containers from the failed replace.

## GitHub Actions

- Previous `vpsadminos` branch tip `3bbec714c`; superseded by force-push to
  `f49f4180d`.
  - RuboCop `27482412986`: success in 41s.
  - RSpec `27482412994`: success in 4m45s.
  - CI `27482412984`: success in 50m32s.
- `vpsadminos` branch pushed at `f49f4180d`:
  - RuboCop `27493672727`: success.
  - RSpec `27493672735`: success.
  - CI `27493672729`: success.
- Previous `vpsadmin` branch tip `588f3e361`; superseded by pending force-push
  to `a379dd319`.
  - Client Specs `27482479469`: success in 1m47s.
  - Webui PHPUnit `27482479466`: success in 1m39s.
  - libnodectld Specs `27482479475`: success in 3m2s.
  - CI `27482479467`: success in 4h6m6s.
  - Older superseded vpsAdmin CI `27481783881` was cancelled.
- `vpsadmin` branch pushed at `a379dd319`:
  - Client Specs `27495006273`: success.
  - RuboCop `27495006281`: success.
  - Webui PHPUnit `27495006282`: success.
  - libnodectld Specs `27495006278`: success.
  - API Specs (topic parallel) `27495006274`: success.
  - CI `27495006277`: failed.
    - `vps/replace-with-descendants-and-mounts` failed because the test used
      target vpsAdmin pool filesystem `tank/ct-replace-desc` while osctld
      remote receive placed the replacement under its deterministic pool layout
      `tank/ct/2`. The new replacement snapshot `RecvCheck` correctly checked
      the vpsAdmin target path and exposed this mismatch.
    - `webui#vps-admin-ops` failed from the same class of issue after the
      replace form omitted the new preservation flags; API defaults enabled
      preservation and the browser fixture target pool used `tank/webui-node2`.
      Local commit `f80c988f4` adds the form fields and makes that Playwright
      helper submit both flags explicitly.
- Local follow-up after CI failure:
  - `e5c12ec4f tests: align replace target pool with osctld layout` updates
    `vps/replace-with-descendants-and-mounts` to use `primary_pool_fs` for the
    target hypervisor pool. This keeps the test within osctld's general remote
    receive contract without reintroducing vpsAdmin-specific target dataset
    support in vpsAdminOS.
  - Verified with
    `./test-runner.sh test vps/replace-with-descendants-and-mounts`: success in
    1135.47s. The example itself succeeded in 574.88s and retained the root and
    descendant sentinel files.
## Review Remediation On 2026-06-14

- A mandatory-change-review pass found three blocking issues:
  - vpsAdmin replacement-backup integration tests still reconstructed the old
    custom `vps-replace-...` snapshot name instead of checking the standard
    datetime snapshot recorded in the DB.
  - vpsAdminOS was based on old `origin/staging`, so review against current
    staging included unrelated flake-lock reversions.
  - `vpsfree-cz-configuration` was based on old `origin/master`, so review
    against current master included unrelated configuration reversions.
- vpsAdmin remediation:
  - `tests/suite/storage/remote-common.nix` gained
    `snapshot_row_by_label`.
  - Same-node and remote replacement-backup tests now find the replacement
    snapshot by label, assert that source/replacement DB rows use the same
    confirmed standard datetime name, and compare DB rows against ZFS state.
  - The test fix was squashed into
    `31d0c53d4 api: preserve backups during VPS replace`.
  - `tools/update_vpsadminos_flake.sh
    github:vpsfreecz/vpsadminos/03b686f7172d9666c4d3574c93da864859f3445c`
    created the flake update, then history was rewritten so there is one
    `vpsadminos` flake input update commit:
    `cba7c976d flake: vpsadminos 6f9b2c755 -> 03b686f71`.
- vpsAdminOS remediation:
  - Rebasing onto current `origin/staging` succeeded cleanly.
  - The first commit message was rewrapped and now passes commit-msg hooks.
  - `nix develop -c overcommit --run` passed.
  - The rebased feature branch was force-pushed with lease at `03b686f71` so
    vpsAdmin can lock the exact GitHub revision.
- `vpsfree-cz-configuration` remediation:
  - Rebasing onto current `origin/master` succeeded cleanly.
  - `nix develop -c overcommit --run` passed.
  - Transient `.bin/`, `.bundle/`, and `.rubocop_cache/` files from the dev
    shell/hook run were removed.
- Workspace review-process remediation:
  - `skills/mandatory-change-review/SKILL.md` now requires review of repeated
    updates to the same flake input.
  - It also requires the same check for repeated gem dependency,
    `Gemfile.lock`, Bundix output, or generated gem metadata commits within
    one update stream.
  - The skill was validated with
    `nix-shell -p 'python3.withPackages (ps: [ ps.pyyaml ])' --run 'python
    /home/aither/.codex/skills/.system/skill-creator/scripts/quick_validate.py
    skills/mandatory-change-review'`.
- Mandatory review rerun:
  - Ran `mandatory-change-review` with standalone agent
    `019ec7f9-c6ef-7cc0-8f66-68aad262c176`. The reviewer was explicitly told
    to perform the review itself and not spawn nested reviewers.
  - Result:
    - Blocking: none.
    - Important: none.
    - Advisory: workspace commit `896a160 workspace: review repeated gem
      updates` had one overlong commit-message body line.
  - Action taken:
    - Amended that workspace commit message to wrap the body; new commit hash
      is `aefd23f workspace: review repeated gem updates`.
  - Residual risks noted by the reviewer:
    - Long same-node and remote backup-preserving replacement tests were not
      rerun after the final assertion-only DB-label snapshot-name test update.
    - Web UI flag plumbing still needs post-change Playwright/CI confirmation.
    - Mixed-version deployment still requires vpsAdminOS with local
      `ct cp --from-snapshot` before default same-node
      history-preserving replace, or use `preserve_backups=false`.
- Pushes after review:
  - `vpsadminos` was already pushed at `03b686f7172d`.
  - `vpsadmin` was force-pushed with lease:
    `a379dd319` -> `6f659e66c2e9`.
  - `vpsfree-cz-configuration` was force-pushed with lease:
    `13b4d2b2` -> `5fafb818034a`.
  - workspace instructions were pushed as a new remote branch at
    `aefd23f191a3`.
  - The `vpsfree-cz-configuration` dev shell created transient `.bin/` and
    `.bundle/` directories during push; they were removed.
- Post-review GitHub Actions:
  - `vpsadminos` head `03b686f7172d`:
    - RuboCop `27511854932`: success.
    - RSpec `27511854927`: success.
    - CI `27511854948`: success in 42m29s.
  - `vpsadmin` head `6f659e66c2e9`:
    - RuboCop `27512491609`: success.
    - Webui PHPUnit `27512491606`: success.
    - Client Specs `27512491600`: success.
    - libnodectld Specs `27512491605`: success.
    - API Specs (topic parallel) `27512491603`: success.
    - CI `27512491594`: failed after 7h7m with two failures:
      `vps/replace-with-backups` and `vps/replace-with-backups-remote`.
      The replace and post-replace backup flows completed, but the final data
      integrity check tried to read `post-*-replace-backup.txt` from the top
      backup dataset mount. Backup data is stored in the current head branch
      dataset under `tree.0/branch-*`, so the assertion was checking the wrong
      on-disk path.
  - `vpsfree-cz-configuration` and workspace instructions had no listed
    workflows for this branch.
- CI failure remediation:
  - Updated both VPS replacement backup tests to record the backup head branch
    before and after the post-replace backup, assert that the branch remains
    stable, and read the known data file from that branch dataset.
  - `nix develop -c nixfmt --check tests/suite/vps/replace-with-backups.nix
    tests/suite/vps/replace-with-backups-remote.nix` passed.
  - `./test-runner.sh test vps/replace-with-backups` passed locally in
    652.21 seconds.
  - `./test-runner.sh test vps/replace-with-backups-remote` passed locally in
    853.02 seconds.
- Mandatory review rerun after the CI assertion fix:
  - Ran `mandatory-change-review` with standalone agent
    `019ec9b2-762f-7eb0-9dcb-a666e44dfe8b`. The reviewer was explicitly told
    to perform the review itself and not spawn nested reviewers.
  - Result:
    - Blocking: none.
    - Important:
      - The vpsAdminOS branch was not based on the current `origin/staging`
        head, so final integration could not fast-forward and vpsAdmin would
        need another flake pin later.
      - The vpsAdmin API implementation commit still bundled the initial long
        VPS replacement integration tests. The tests should be split into their
        own logical commit.
    - Advisory:
      - The vpsAdminOS firewall race-test commit is unrelated to the VPS
        replacement feature and should remain explicitly called out.
      - The initiative state needed to be refreshed after the latest head
        rewrites.
  - Action plan:
    - Rebase vpsAdminOS onto current `origin/staging`.
    - Refresh the single vpsAdmin flake pin to the rebased vpsAdminOS head.
    - Rewrite vpsAdmin history so the integration tests are separate from the
      API implementation and still include the data-integrity assertion fix.
    - Rerun quick verification/review as needed before pushing updated heads.
- Review remediation after the rerun:
  - vpsAdminOS was rebased onto current `origin/staging`; the merge-base is now
    `a9e857bb9`, and the rebased branch head is `e2b5a7a98`.
  - `nix develop -c overcommit --run` passed in vpsAdminOS after the rebase.
  - The rebased vpsAdminOS branch was force-pushed with lease so vpsAdmin can
    pin the exact GitHub revision.
  - vpsAdmin history was rewritten to split the API implementation and the
    backup-preserving replacement integration tests:
    - `f226cec88 api: preserve backups during VPS replace`.
    - `fd6146226 tests: verify VPS replacement backup data integrity`.
  - The vpsAdmin flake input was refreshed to the rebased vpsAdminOS commit
    and squashed into a single flake update commit:
    `d3b1b97cf flake: vpsadminos 6f9b2c755 -> e2b5a7a98`.
  - The vpsAdmin branch head after rewriting is
    `f3e1ff0d0 webui: expose VPS replace backup options`.
  - `nix develop -c overcommit --run` passed in vpsAdmin after the rewrite.
    PhpCsFixer again touched unrelated WebUI files; that generated diff was
    reversed with `git diff ... | git apply -R`, leaving the worktree clean.
- Final mandatory review rerun after remediation:
  - Ran `mandatory-change-review` with standalone agent
    `019ec9c6-4e60-75c3-9675-c1ab065b58e7`. The reviewer was explicitly told
    to perform the review itself and not spawn nested reviewers.
  - Result:
    - Blocking: none.
    - Important: none.
    - Advisory: `state.md` still had stale branch/base/head references after
      the latest rewrites.
  - Action taken:
    - Updated the repository base/head summaries, vpsAdminOS rebased head,
      vpsAdmin rewritten series, and remaining-work notes in this file.
  - Residual risks noted by the reviewer:
    - Late backup dataset rename/DB rewire rollback and partial-failure
      behavior is covered mostly by transaction structure and unit
      expectations, not an end-to-end forced-failure integration scenario.
    - Mixed-version same-node replacement still requires vpsAdminOS to be
      updated before default history-preserving replaces, or callers must use
      `preserve_backups=false`.
- Post-review integration checks on final heads:
  - `./test-runner.sh test vps/replace-with-backups` passed locally in
    744.83 seconds on vpsAdmin head `f3e1ff0d0` with vpsAdminOS flake pinned to
    `e2b5a7a98`.
  - `./test-runner.sh test vps/replace-with-backups-remote` passed locally in
    857.57 seconds on the same heads.
- Pushes after final review:
  - vpsAdminOS was force-pushed with lease:
    `03b686f71` -> `e2b5a7a98`.
  - vpsAdmin was force-pushed with lease:
    `6f659e66c` -> `f3e1ff0d0`.
  - No superseded active runs were found after the vpsAdmin push; previous
    vpsAdmin runs were already completed.
- GitHub Actions after final pushes:
  - `vpsadminos` head `e2b5a7a98`:
    - RuboCop `27526032944`: success.
    - RSpec `27526032925`: success.
    - CI `27526032920`: success.
  - `vpsadmin` head `f3e1ff0d0`:
    - RuboCop `27527898643`: success.
    - libnodectld Specs `27527898624`: success.
    - CI `27527898725`: success in 3h49m35s.
    - API Specs (topic parallel) `27527898615`: success.
    - Webui PHPUnit `27527898613`: success.
    - Client Specs `27527898633`: success.
  - The vpsAdmin, vpsAdminOS, and vpsfree-cz-configuration worktrees are clean
    against their pushed feature branches after CI completed.

## Merge Prep On 2026-06-15

- User requested rebasing onto upstream default branches, skipping expensive
  test runs, running a final review, and then merging to defaults.
- Rebase checks:
  - `vpsadmin` is already up to date with `origin/master`.
  - `vpsadminos` is already up to date with `origin/staging`, its upstream
    default branch.
  - `vpsfree-cz-configuration` is already up to date with `origin/master`.
- vpsfree-cz-configuration channel updates:
  - `nix develop -c confctl inputs channel set --commit
    '{production,staging,os-staging}' vpsadminos
    e2b5a7a987e5c57b31a67344c885c5b5dac2da7d`
    created commit
    `c042f953 inputs: set vpsadminosOsStaging, vpsadminosProduction, vpsadminosStaging to e2b5a7a9`.
  - `nix develop -c confctl inputs channel set --commit
    '{production,staging,vpsadmin}' vpsadmin
    f3e1ff0d099d742b72831e881e53c27ee90a337c`
    created commit
    `e0500614 inputs: set vpsadminProduction, vpsadminServices, vpsadminStaging to f3e1ff0d`.
  - The generated `confctl` commit messages triggered only the expected
    generated-message width warnings; hooks passed.
  - `nix develop -c confctl inputs channel ls
    '{production,staging,os-staging,vpsadmin}'` verified:
    - `production`: `vpsadminos=e2b5a7a9`, `vpsadmin=f3e1ff0d`.
    - `staging`: `vpsadminos=e2b5a7a9`, `vpsadmin=f3e1ff0d`.
    - `os-staging`: `vpsadminos=e2b5a7a9`.
    - `vpsadmin`: `vpsadmin=f3e1ff0d`.
  - Transient `.bin/` and `.bundle/` directories from the confctl dev shell
    were removed.
- Final mandatory review before merge:
  - Ran `mandatory-change-review` with standalone agent
    `019ecad6-375d-7522-bf2f-b992bdd316cb`.
  - Result:
    - Blocking: none.
    - Important: none.
    - Advisory: none.
  - Clean-history check passed, including repeated flake/gem update checks.
  - Reviewer noted that final expensive tests were intentionally skipped by
    user request, and that prior CI/integration tests were green on vpsAdmin
    `f3e1ff0d0` and vpsAdminOS `e2b5a7a98`.
  - Reviewer also noted the unrelated dirty top-level `AGENTS.md`; workspace
    changes must be merged from a clean temporary worktree if merged.
- Fast-forward merges:
  - Created clean merge worktrees under
    `worktrees/2026-06-13-vps-replace-backups/merge/`.
  - `vpsadminos` was fast-forward merged from `origin/staging` to
    `e2b5a7a98` and pushed to `staging`.
  - `vpsadmin` was fast-forward merged from `origin/master` to `f3e1ff0d0` and
    pushed to `master`.
  - `vpsfree-cz-configuration` was fast-forward merged from `origin/master` to
    `e0500614` and pushed to `master`.
  - The top-level workspace was fast-forward merged from a clean temporary
    worktree to `aefd23f` and pushed to `master`; the unrelated local
    DokuWiki `AGENTS.md` edit in the main workspace was not included.
- GitHub Actions after default-branch pushes:
  - `vpsadminos` `staging` at `e2b5a7a98`:
    - RuboCop `27540907754`: success.
    - RSpec `27540907795`: in progress.
    - CI `27540907779`: in progress.
  - `vpsadmin` `master` at `f3e1ff0d0`:
    - RuboCop `27540922767`: in progress.
    - Client Specs `27540923086`: in progress.
    - Webui PHPUnit `27540923112`: in progress.
    - libnodectld Specs `27540923116`: in progress.
    - API Specs (topic parallel) `27540923102`: queued.
    - CI `27540923168`: in progress.
  - `vpsfree-cz-configuration` has only an unrelated scheduled Daily update
    running on old head `46a0c48f`.
  - The top-level workspace repository has no listed workflow runs.
- vpsAdminOS RSpec run `27540907795` failed after the default-branch push.
  - The failure was isolated to the `libosctl` suite; other RSpec suites
    passed.
  - Logs show a Ruby segmentation fault in
    `libosctl/lib/libosctl/exporter/zfs.rb:152` (`gz.write(data)`) while
    running `libosctl/spec/libosctl/exporter/zfs_spec.rb:91`, preceded by the
    expected negative-path `tar` error for a missing file.
  - This feature branch does not modify `libosctl/`, and the same vpsAdminOS
    head `e2b5a7a98` previously passed RSpec in GitHub Actions run
    `27526032925`.
  - Local focused reproduction on the pushed head passed:
    `GITHUB_WORKSPACE=$PWD nix develop .#vpsadminos -c bash -lc 'export
    BUNDLE_GEMFILE="$PWD/libosctl/Gemfile"; export BUNDLE_PATH="$PWD/.gems";
    cd libosctl; bundle install; bundle exec rake compile; bundle exec rspec
    spec/libosctl/exporter/zfs_spec.rb --format documentation'` reported
    `9 examples, 0 failures`.
  - Conclusion before rerun: this is an unrelated intermittent Ruby/Zlib/tar
    crash in an untouched test area, not evidence of a VPS replacement
    regression. The failed RSpec workflow can be rerun after this
    investigation.
- vpsAdminOS RSpec rerun `27540907795` then passed.
- vpsAdminOS staging CI `27540907779` passed after 47m25s.
- vpsAdmin master API Specs `27540923102` passed.
- vpsAdmin master CI `27540923168` failed after 6h5m.
  - Job log summary: 115 tests successful, 1 unexpected failure:
    `storage/dataset-migrate-rsync-remote`.
  - Downloaded artifact `vpsadmin-test-logs-27540923168` to
    `/tmp/vpsadmin-ci-27540923168-artifacts`.
  - The failing script's `test-result.txt` contains `unexpected_failure`.
  - Its `test-runner.log` shows the script did not reach its test body. It
    failed while building test JSON:
    `error: path
    '/nix/store/mpyynadg8yxl0z95va483l1q2zm5hbmg-sv-osctl-exportfs-log-run'
    is not valid`, followed by `nix-build ... evaluate-tests.nix ... --argstr
    testPath storage/dataset-migrate-rsync-remote failed (1)`.
  - The node/service logs in the same artifact directory appear to be stale
    leftovers for this deterministic test log path; they show the migration
    data hashes matching, but the current `test-runner.log` ends at Nix
    evaluation.
  - The only changed file under `tests/storage`, `.github/workflows/ci.yml`,
    `flake.nix`, `flake.lock`, `nixos`, or `packages` for this vpsAdmin branch
    is `flake.lock`.
  - The same vpsAdmin head `f3e1ff0d0` passed CI earlier in run
    `27527898725`, and that log shows
    `storage/dataset-migrate-rsync-remote` passed in 423.26 seconds.
  - Conclusion before rerun: this is a runner/Nix store validity failure during
    test configuration build, not a VPS replacement regression. Rerunning the
    failed CI job is justified after this log inspection.
  - User asked whether this could have been caused by `nix-collect-garbage`
    running during tests. This fits the observed Nix error shape, although the
    uploaded logs do not prove a host GC occurred. The vpsAdmin workflow/test
    code does not run `nix-collect-garbage`; any such interference would be
    from the self-hosted runner/host cleanup or stale/corrupt Nix store state.
  - Attempt 1 ran on `gh-runner2.int.vpsadminos.org`; the rerun is running on
    `gh-runner1.int.vpsadminos.org`. The configuration repository has a
    pressure-triggered `nix-collect-garbage` timer on `aitherdev`, but the
    GitHub runner containers are marked `managed = false` in
    `cluster/org.vpsadminos/cluster.nix`, so their local GC policy is not
    visible in this checkout.
  - Rerun attempt on `gh-runner1.int.vpsadminos.org` passed in 4h17m19s.
    The original failure is therefore recorded as an investigated runner/Nix
    store validity failure on `gh-runner2.int.vpsadminos.org`, not a VPS
    replacement regression.
- Final GitHub Actions sweep:
  - `vpsadmin` `master` at `f3e1ff0d0`: RuboCop, Webui PHPUnit, Client
    Specs, libnodectld Specs, API Specs, CI, and Daily update all passed.
  - `vpsadminos` `staging` at this feature's pushed head `e2b5a7a98`:
    RuboCop, RSpec, CI, and Daily update passed.
  - `vpsadminos` `staging` later advanced to unrelated commit `c3e7e0cf5`
    (`os: restore 6.12.91 live kernel pin`). Its CI failed in
    `firewall/conntrack#no-conntrack` on a compatibility refuse-chain
    assertion. This is after this feature's merge and channel pin, and not
    caused by the VPS replacement work. The same artifact also contains a
    stale `web` failure directory from before that run started; the CI summary
    counted only the firewall failure.
  - `vpsfree-cz-configuration` has no push workflow for `e0500614`; the only
    listed failure is an unrelated scheduled Daily update on old head
    `46a0c48f`.
  - The top-level workspace repo `aither64/vpsfree-cz-workspace` has no
    listed workflow runs.

## Remaining Work

- None for this initiative.

## Cleanup

- Worktrees are intentionally kept for review.
- Transient build/cache output has been removed from the tracked worktrees.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
