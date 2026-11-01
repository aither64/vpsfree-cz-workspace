# Package F review packet

Status: source complete, committed and quick-checked; clean worktree. Ready
for lead-assigned mandatory review. Long package checks remain held.

Session: `2026-10-24-vpsadmin-haveapi-upgrade`; lead owns plan/state,
independent review assignment, publication and later installed-package decisions.
Design: [Package F](../design.md#2026-10-26-f-fix-provider-ssh-stdin-and-full-guest-certification).
Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/

## Source and complete history

Repository: `git@github.com:vpsfreecz/dev-workspace.git` (local
`vpsfree-dev-workspace`, not generic dev-workspace).
Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsfree-dev-workspace`.
Branch: `2026-10-24-vpsadmin-haveapi-upgrade-boot-proof`.
Exact base: `767dfd587e346168e1443e65ccdb67ce748f3fe3` (fresh upstream
master confirmed before implementation and again during focused verification).
Final head: `ab9346b0c4b942fccd0da6af760401fad3a55bd1`.
Final tree: `ff22b629479737a274510d395730190a442463ee`.
Complete series: exactly one commit, `ab9346b0c4b942fccd0da6af760401fad3a55bd1`
(`devcluster: require complete guest proof before certifying boot`), parent is
exact base above. [Full author/committer/history](history.txt), [complete final
diff](final.diff), [tested-file hashes](tested-files.sha256). Final SSH read
confirms master still exact base and own feature branch is unpublished.
No refs outside the owned new feature branch were changed.

One functional fix bundles only the two owning proof functions, regressions in
the existing command harness and a five-line provider README contract. Tests and
docs are inseparable support for the corrected certification boundary. No
superseded committed approaches, follow-up commits, repeated dependency/input
streams, pin changes or generated metadata are intended. No migrations: no new
or changed migration, persisted format, schema or transition policy. No F
revision has been merged, released, deployed, installed or externally consumed.

## Requested behavior and implementation

The real public start path must prove every configured guest exactly once before
publishing complete applied selection. The predecessor let proof SSH consume
the here-string driving the loop, then published success after its first guest.

Only noninteractive proof SSH gains `-n`; interactive SSH and script streaming
retain their existing behavior. Full proof captures checked authoritative JSON
keys separately from checked line enumeration, iterates an array, refuses
duplicates and records only successful guests. Sorted successful guest keys must
exactly equal authoritative keys before calling `applied-finish-boot`. Spin
extraction also checks producer status. Query, validity, init, exact-system and
root commands, timeout, refresh ordering, host roots and locking stay intact.
Failure retains native pending state and earlier roots; it does not stop guests
or fabricate provenance.

The vpsAdmin provider owns this internal boundary. Actual call sites are fresh
start and copied-config boot; target update shares the single-guest proof.
`maintenance.rb` retains its existing trusted internal finish interface. The
provider is exported by `nix/organization-tools.nix` and the extension flake,
consumed through generic dev-workspace's provider contract. Existing script
stream consumers use `ssh_cmd` and are outside the changed call. Provider and
root READMEs were read; the retained-boot subsection owns the lasting semantics.

## Focused evidence

Pinned environment: README's `nix shell --inputs-from .` tools and exact
`testEnvironment` exports extracted from `checks.x86_64-linux.tests` evaluation;
no aggregate tests build. See [environment](focused-test-environment.sh),
[toolchain](toolchain.log), and original derivation evaluation
[JSON](../package-f-tests-env.json). Ruby 3.4.9 bundled Minitest, Bash5.3p9,
jq1.8.2, Nix2.34.8. flake.lock SHA256
`b2282ff7b51986f792cdfe5207c928699a085684c2183e539c434e55341a07bb`.

- Predecessor proof: [log](predecessor-regression.log), exact base production
  plus the new harness. Public start exits successfully but only dns-primary
  actually completes proof; expected dns-primary/dns-secondary/node1/services.
  One case, three assertions, one failure, 32.789707 seconds.
- `bash -n dev-clusters/vpsadmin/bin/devcluster` and
  `ruby -c test/devcluster_commands_test.rb`: PASS.
- `ruby test/devcluster_commands_test.rb`: 47 cases/580 assertions, exit0,
  1033.416029s, zero failures/errors/skips; [log](commands.log),
  [status](commands.exit). Original parent-owned handle8022 reconciled complete.
  It began with visible monitor fallback; no duplicate monitor or run.
  Unrelated prior A watcher ownership was refreshed through lead, who verified
  the utility slot was free for the separate maintenance/root batch.
- Maintenance: 31 cases/236 assertions, exit0, 2.283260s.
- Private-local-store roots: 6 cases/141 assertions, exit0, 38.158685s.
  Both have zero failures/errors/skips; [combined log](maintenance-roots.log),
  [status](maintenance-roots.exit), [elapsed](maintenance-roots.elapsed) (42s).
  Fresh pinned-catalog840 Luna/low watcher, matching native
  `dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12`; full access/never.
  Completed handle5413 reconciled, utility slot released.
- `git diff --check BASE HEAD`, staged whitespace and no-unstaged-change checks:
  PASS. No tracked hook framework is declared; `core.hooksPath` is unset and
  actual repository hooks directory contains only `.sample` files. Normal
  `git commit -F package-f/commit-message.txt` succeeded without bypass.
- `sha256sum --check tested-files.sha256` after commit: all four files PASS,
  binding tested source/docs/lock bytes to final committed tree. Only the three
  assigned files changed: 144 insertions/7 deletions. Author/committer use saved
  Jakub Skokan identity; no identity or hook configuration changed.
- Total focused evidence: 84 cases/957 assertions, all passing.

The command harness drives public start and actual fixture query/validity/root
commands, with fake SSH attempting to drain inherited stdin. It checks all four
identities/operations once, final provenance, and finish ordering. Middle query
and root failures refuse further proofs and retain pending. Truncated, duplicate
and failed enumeration cases independently require refusal against a config
still containing four machines. Existing target-update/maintenance assertions
are retained. All fixtures use disposable state; the roots fixture uses a
private local Nix store, no GC/build or live guest.

## Review and remaining gates

Risk: high, because this host-side provider publishes retained boot evidence.
Suggested mandatory lanes: general, architecture/repetition, scope/proportionality and
risk/compatibility. Lead assigns retained independent reviewer0 with saved
`gpt-6.1-sol/xhigh`; no review has been requested on uncommitted work.

After committed quick checks and mandatory review, repository-required
`nix flake check --print-build-logs` and packaged `nix run .#devcluster-check`
remain. No host-migration VM or live-cluster test is assigned. No default merge,
provider install, host profile, envelope repair, cluster restart/reset/update,
or Package C source/ref/PR74 action is authorized by this source package.

Existing schema1/policy3 and on-disk formats stay exact; no coordinated guest
upgrade is required. This source fix does not repair a certificate already
published by the old provider. Selecting a fixed package and reconciliation of
existing state remain separate authorized operations. Reverting restores the
known defect and cannot be used to evade proof refusal. Live vpsAdmin70a/WebUIf10
interfaces stay running untouched.
