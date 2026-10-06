---
lifecycle: active
---
# vpsf-status integration tests state

## Current status

Merged to `master`; local feature and merge worktrees have been removed.

## Initiative

- Slug: `2026-06-01-vpsf-status-integration-tests`
- Tracking directory:
  `/home/aither/workspace/ai/vpsfree.cz/work/2026-06-01-vpsf-status-integration-tests`

## Repositories and worktrees

### vpsf-status

- Bare repository:
  `/home/aither/workspace/ai/vpsfree.cz/repos/vpsf-status.git`
- Remote:
  `git@github.com:vpsfreecz/vpsf-status.git`
- Branch:
  `2026-06-01-vpsf-status-integration-tests`
- Worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-01-vpsf-status-integration-tests/vpsf-status`
- Base:
  `origin/master` at `c6fab24`
- Commit:
  `b481a8c` (`Add vpsAdmin integration tests`)
- Remote branch:
  `origin/2026-06-01-vpsf-status-integration-tests`
- Merged into:
  `origin/master` at `b481a8c`
- Status:
  complete; initiative worktrees removed

Reference repositories read during implementation:

- `vpsadminos`
- `vpsadmin`
- `confctl`
- `terraform-provider-vpsadmin`
- `vpsfree-irc-bot`

No reference repository worktree was edited.

## Files changed

In `vpsf-status`:

- `.github/workflows/integration-tests.yml`
- `Makefile`
- `flake.lock`
- `flake.nix`
- `nix/module.nix`
- `test-runner.sh`
- `tests/README.md`
- `tests/all-tests.nix`
- `tests/make-test.nix`
- `tests/runner/extensions/vpsadmin_services.rb`
- `tests/suite/status-page.nix`

In workspace notes:

- `notes/cross-project/2026-06-01-test-runner-socket-mcast.md`

## Commands run

Setup and inspection:

```sh
git fetch --prune origin
git worktree add -b 2026-06-01-vpsf-status-integration-tests \
  ../../worktrees/2026-06-01-vpsf-status-integration-tests/vpsf-status \
  origin/master
find .. -name AGENTS.md -print
sed -n '1,220p' AGENTS.md
```

Implementation and evaluation:

```sh
nix flake lock
nix eval .#testsMeta.x86_64-linux.status-page.name
./test-runner.sh ls
./test-runner.sh ls -t ci
nix develop --command go test ./...
nix build .#vpsf-status --no-link
./test-runner.sh test status-page
git diff --cached --check
nix develop --command make hooks
git commit -F <tmpfile>
nix develop --command git commit --amend -F <tmpfile>
git push -u origin 2026-06-01-vpsf-status-integration-tests
gh run watch 26761760980 --exit-status
```

Merge and cleanup:

```sh
git fetch --prune origin
git worktree add \
  ../../worktrees/2026-06-01-vpsf-status-integration-tests/vpsf-status-merge-master \
  origin/master
git merge --ff-only 2026-06-01-vpsf-status-integration-tests
nix develop --command go test ./...
nix build .#vpsf-status --no-link
./test-runner.sh ls -t ci
git push origin HEAD:master
gh run watch 26762672654 --exit-status
git worktree remove \
  ../../worktrees/2026-06-01-vpsf-status-integration-tests/vpsf-status-merge-master
git worktree remove \
  ../../worktrees/2026-06-01-vpsf-status-integration-tests/vpsf-status
rm -rf /tmp/os-test-runner
rmdir ../../worktrees/2026-06-01-vpsf-status-integration-tests
```

## Validation results

- `./test-runner.sh ls`: passed, listed `status-page`.
- `./test-runner.sh ls -t ci`: passed, listed `status-page`.
- `nix develop --command go test ./...`: passed.
  - `github.com/vpsfreecz/vpsf-status`
  - `github.com/vpsfreecz/vpsf-status/config`
  - `github.com/vpsfreecz/vpsf-status/json`
- `nix build .#vpsf-status --no-link`: passed.
- `git diff --cached --check`: passed.
- `nix develop --command make hooks`: installed Lefthook pre-commit hook.
- `nix develop --command git commit --amend -F <tmpfile>`: passed Lefthook
  pre-commit hook; `gofmt` skipped because no Go files were staged.
- `git push -u origin 2026-06-01-vpsf-status-integration-tests`: pushed
  `b481a8c` and set upstream tracking.
- GitHub Actions run `26761760980` (`Integration Tests`): passed.
  - URL:
    `https://github.com/vpsfreecz/vpsf-status/actions/runs/26761760980`
  - Job: `Run ci-tagged integration tests`
  - Duration: 10m22s
  - Completed: 2026-06-01T14:47:56Z
- `./test-runner.sh test status-page`: passed all 6 examples on
  2026-06-01 at 15:24:17 +0200.
  - Runtime: 788.89 seconds.
  - Covered baseline JSON, metrics, ping loss/recovery, nodectld
    loss/recovery, vpsAdmin HTTP loss/recovery, and outage reports.
- Merge worktree validation before pushing `master`:
  - `nix develop --command go test ./...`: passed.
  - `nix build .#vpsf-status --no-link`: passed.
  - `./test-runner.sh ls -t ci`: passed, listed `status-page`.
- Fast-forward push to `master`: updated `origin/master` from `c6fab24` to
  `b481a8c`.
- GitHub Actions run `26762672654` (`Integration Tests`) on `master`: passed.
  - URL:
    `https://github.com/vpsfreecz/vpsf-status/actions/runs/26762672654`
  - Job: `Run ci-tagged integration tests`
  - Duration: 6m38s
  - Completed: 2026-06-01T15:00:04Z

After the full pass, only example descriptions/indentation were adjusted in
`tests/suite/status-page.nix`; `./test-runner.sh ls -t ci` was rerun and passed.

## Implementation notes

- The vpsAdmin seed node is exposed to vpsf-status as
  `vpsadmin-node1.lab`; the public status API reports the domain, not the short
  node seed name.
- The seeded vpsAdminOS node reports `pool_state = "unknown"` and
  `pool_scan = "unknown"` while `pool_status = true`; the test asserts that
  exact fixture behavior instead of forcing synthetic online pool state.
- `nodectld` can have a transient socket/reset window after service startup.
  The readiness helper waits for the service, socket, and `nodectl ping`.
- vpsAdmin outage report models are plugin models, so the direct Ruby fixture
  helper loads `plugins/outage_reports/api/models/*.rb`.
- The services/node/status machines use socket multicast port `22131` to avoid
  collision with other local test-runner processes using the default port.
- `vpsf-status.service` needs `CAP_NET_RAW` for ICMP ping checks when run as
  the module-created system user.

## Known non-blockers

- Full `./test-runner.sh test -t ci` was not rerun separately after the last
  description-only cleanup. `status-page` is the only `ci` tagged suite and was
  run directly.
- A separate, unrelated `vpsfree-irc-bot` test-runner process was active during
  part of validation and increased wall time. It was not modified or stopped.

## Cleanup notes

- Removed:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-01-vpsf-status-integration-tests/vpsf-status`
- Removed:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-01-vpsf-status-integration-tests/vpsf-status-merge-master`
- Removed local scratch directory `/tmp/os-test-runner` after confirming no
  related test-runner or QEMU processes were active.
- Removed empty initiative worktree group directory.
- Kept local and remote feature branch refs as required by workspace policy.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
