---
lifecycle: complete
---
# 2026-06-10-vpsadminos-cgroup-bug

## Repositories
- `vpsadminos`
  - bare clone: `repos/vpsadminos.git`
  - target branch: `staging`
  - feature branch: `2026-06-10-vpsadminos-cgroup-bug`
  - remote branch: `origin/2026-06-10-vpsadminos-cgroup-bug`
  - worktree: `worktrees/2026-06-10-vpsadminos-cgroup-bug/vpsadminos`

## Status
- The immediate staging container start incident was mitigated live by enabling
  missing cgroup v2 subtree controllers.
- Merged the local `2026-06-10-osctld-crash` functional work into this branch.
  The older crash-session gem rebuild commit was intentionally skipped.
- Added the cgroup v2 delegation repair fix and a focused spec.
- GitHub CI on the first push failed in the test-suite job because the
  cherry-picked shared-dir cleanup tolerated `not mounted` but not util-linux
  `not found` for an already absent shared mount directory.
- Squashed the cleanup follow-up into `osctld: harden broken container cleanup`
  as requested. The same squashed commit also removes `umount -R` and uses
  non-recursive `umount -f`.
- Found the root cause of the console restart problem: during restart, osctld
  can see a tty0 socket path before a listener is accepting connections, or
  while a previous wrapper socket is being replaced. `Console#connect` retried
  only `ENOENT`, so transient `ECONNREFUSED` escaped as an internal start
  failure even though the container continued to reach `RUNNING`.
- Added console retry handling for `ECONNREFUSED`, preserving the existing
  retry budget and keeping an exhausted tty0 connection failure non-fatal in
  the container start command.
- Rebuilt packaged gems once for the final combined branch with build id
  `26.05.0.build20260610185909`.
- Branch history was rewritten to keep the shared-dir fix squashed, the console
  fix before the gem rebuild, and a single final gem rebuild commit.
- Force-pushed the rewritten branch to origin. GitHub Actions for
  `c2f5575a0d475fa006dc3a291e759a80c2331b65` are all green.
- Merged the feature branch into `staging` with a fast-forward-only merge from
  a temporary staging worktree and pushed `staging`.
- Removed the temporary staging merge worktree and the feature worktree. The
  older `2026-06-10-osctld-crash` vpsadminos worktree was already absent.

## Commands run
- `bin/dev-session current`
- `ls -la work/2026-06-10-vpsadminos-cgroup-bug`
- `find worktrees/2026-06-10-vpsadminos-cgroup-bug -maxdepth 2 -type d -print`
- `sed -n '1,220p' work/2026-06-10-vpsadminos-cgroup-bug/plan.md`
- `sed -n '1,260p' work/2026-06-10-vpsadminos-cgroup-bug/state.md`
- `ls -la repos/vpsadminos.git`
- `git --git-dir repos/vpsadminos.git remote -v`
- `git --git-dir repos/vpsadminos.git branch --show-current`
- `git --git-dir repos/vpsadminos.git symbolic-ref refs/remotes/origin/HEAD`
- `git --git-dir repos/vpsadminos.git fetch origin`
- `git --git-dir repos/vpsadminos.git worktree add -b 2026-06-10-vpsadminos-cgroup-bug worktrees/2026-06-10-vpsadminos-cgroup-bug/vpsadminos origin/staging`
- `git stash push -m cgroup-delegation-fix -- osctld/lib/osctld/cgroup.rb osctld/spec/osctld/cgroup_spec.rb`
- `nix develop .#vpsadminos -c git cherry-pick aeef64ff0 221586335 a5238f3d5`
- `git stash pop`
- `nix develop .#vpsadminos -c bash -lc '<focused osctld RSpec command>'`
- `nix develop .#vpsadminos -c bundle exec rubocop <12 touched Ruby files>`
- `nix develop .#vpsadminos -c bash -lc '<overcommit install and commit cgroup fix>'`
- `nix develop .#vpsadminos -c make gems`
- `nix develop .#vpsadminos -c bash -lc '<commit generated gem metadata with git commit -F>'`
- `./test-runner.sh test osctld/resilience`
- `git diff --check origin/staging..HEAD`
- `nix develop .#vpsadminos -c git push -u origin 2026-06-10-vpsadminos-cgroup-bug`
- `gh run list --repo vpsfreecz/vpsadminos --branch 2026-06-10-vpsadminos-cgroup-bug --limit 10 --json databaseId,workflowName,displayTitle,status,conclusion,createdAt,headSha,url,event`
- `gh run watch 27287422646 --exit-status --interval 60`
- `gh run view 27287422646 --job 80598739969 --log`
- `gh run download 27287422646 -n os-test-logs-27287422646 -D /tmp/vpsadminos-ci-27287422646`
- `nix develop .#vpsadminos -c bash -lc '<shared_dir focused RSpec command>'`
- `nix develop .#vpsadminos -c bash -lc '<commit fixup and autosquash into cleanup hardening>'`
- `nix develop .#vpsadminos -c make gems`
- `nix develop .#vpsadminos -c bash -lc '<amend generated gem commit to 26.05.0.build20260610184028>'`
- `./test-runner.sh test osctl/ct-map-mode`
- `git diff --check origin/staging..HEAD`
- `nix develop .#vpsadminos -c bash -lc '<focused osctld RSpec command>'`
- `nix develop .#vpsadminos -c bash -lc '<RuboCop on touched Ruby files>'`
- `git reset --mixed HEAD~1`
- `git branch backup/2026-06-10-vpsadminos-cgroup-bug-before-console-fix`
- `nix develop .#vpsadminos -c bash -lc '<focused console RSpec command>'`
- `nix develop .#vpsadminos -c bash -lc '<commit console retry fix>'`
- `nix develop .#vpsadminos -c make gems`
- `nix develop .#vpsadminos -c bash -lc '<commit final generated gem metadata with git commit -F>'`
- `git diff --check origin/staging..HEAD`
- `nix develop .#vpsadminos -c bash -lc '<focused osctld RSpec command including console, shared_dir, cgroup, monitor specs>'`
- `nix develop .#vpsadminos -c bundle exec rubocop <8 touched Ruby files>`
- `./test-runner.sh test osctl/ct-map-mode`
- `nix develop .#vpsadminos -c git push --force-with-lease -u origin 2026-06-10-vpsadminos-cgroup-bug`
- `gh run list --repo vpsfreecz/vpsadminos --branch 2026-06-10-vpsadminos-cgroup-bug --limit 10 --json databaseId,workflowName,displayTitle,status,conclusion,createdAt,headSha,url,event`
- `gh run watch 27293012737 --repo vpsfreecz/vpsadminos --exit-status --interval 30`
- `gh run watch 27293013140 --repo vpsfreecz/vpsadminos --exit-status --interval 60`
- `gh run view 27293013140 --repo vpsfreecz/vpsadminos --json status,conclusion,jobs,url`
- `gh run list --repo vpsfreecz/vpsadminos --branch 2026-06-10-vpsadminos-cgroup-bug --limit 5 --json databaseId,workflowName,displayTitle,status,conclusion,createdAt,headSha,url,event`
- `git --git-dir repos/vpsadminos.git fetch origin staging 2026-06-10-vpsadminos-cgroup-bug`
- `git --git-dir repos/vpsadminos.git worktree add --detach worktrees/2026-06-10-vpsadminos-cgroup-bug/vpsadminos-staging-merge origin/staging`
- `nix develop .#vpsadminos -c git merge --ff-only origin/2026-06-10-vpsadminos-cgroup-bug`
- `git diff --check origin/staging..HEAD`
- `nix develop .#vpsadminos -c git push origin HEAD:staging`
- `gh run watch 27297150059 --repo vpsfreecz/vpsadminos --exit-status --interval 30`
- `gh run watch 27297150101 --repo vpsfreecz/vpsadminos --exit-status --interval 30`
- `gh run watch 27297150023 --repo vpsfreecz/vpsadminos --exit-status --interval 60`
- `gh run view 27297150023 --repo vpsfreecz/vpsadminos --job 80632914094 --log`
- `gh api repos/vpsfreecz/vpsadminos/actions/runs/27297150023/artifacts --jq '.artifacts[] | {id,name,size_in_bytes,archive_download_url,expired}'`
- `gh run download 27297150023 --repo vpsfreecz/vpsadminos -n os-test-logs-27297150023 -D /tmp/vpsadminos-staging-ci-27297150023`
- `gh run rerun 27297150023 --repo vpsfreecz/vpsadminos --failed`
- `gh run watch 27297150023 --repo vpsfreecz/vpsadminos --exit-status --interval 60`
- `git --git-dir repos/vpsadminos.git worktree remove worktrees/2026-06-10-vpsadminos-cgroup-bug/vpsadminos-staging-merge`
- `git --git-dir repos/vpsadminos.git worktree remove worktrees/2026-06-10-vpsadminos-cgroup-bug/vpsadminos`
- `git --git-dir repos/vpsadminos.git branch -D backup/2026-06-10-vpsadminos-cgroup-bug-before-console-fix`
- `git --git-dir repos/vpsadminos.git worktree prune`
- `git --git-dir repos/vpsadminos.git fetch origin staging`
- `rm -rf /tmp/vpsadminos-staging-ci-27297150023 /tmp/vpsadminos-ci-27287422646`

## Results
- Active initiative slug is `2026-06-10-vpsadminos-cgroup-bug`.
- `repos/vpsadminos.git` uses SSH remote `git@github.com:vpsfreecz/vpsadminos.git`.
- Default upstream branch is `origin/staging`.
- Branch commits:
  - `f899105d0 osctld: mark containers without rootfs as errored`
  - `3fcbdf524 osctld: harden broken container cleanup`
  - `455f6b092 tests: cover osctld broken container resilience`
  - `5df5c6c5a osctld: repair cgroup v2 delegation on existing paths`
  - `4bc97fead osctld: retry refused tty0 console connections`
  - `c2f5575a0 os: update gems to 26.05.0.build20260610185909`
- Focused RSpec passed after the console fix: 85 examples, 0 failures.
- RuboCop passed after the console fix: 8 files inspected, no offenses.
- `./test-runner.sh test osctld/resilience` passed: 5 examples, 1 test
  successful in 263.57 seconds.
- `git diff --check origin/staging..HEAD` passed.
- Before the console fix, local `./test-runner.sh test osctl/ct-map-mode` no
  longer failed at `osctl ct del testct`; shared-dir cleanup succeeded with
  non-recursive `umount -f`. The same run later failed at
  `osctl ct restart testct` with `Connection refused - connect(2)` for
  `tty0.sock`; the container continued to `RUNNING` afterward.
- After the console fix and final gem rebuild, local
  `./test-runner.sh test osctl/ct-map-mode` passed: 1 test successful in
  369.27 seconds. The run covered two successful `osctl ct restart testct`
  calls, final `osctl ct del -f testct`, and `poweroff -f`.
- Pushed branch is synchronized with origin at
  `c2f5575a0d475fa006dc3a291e759a80c2331b65`.
- GitHub Actions for the final push:
  - RuboCop `27293012703`: success.
  - RSpec `27293012737`: success in 4m45s.
  - CI `27293013140`: success; build/cache job passed in 1m7s and test-suite
    job passed in 59m27s.
- `staging` was fast-forwarded from
  `b4ce02d3815d7765e359e34823f53612ffd0abb4` to
  `c2f5575a0d475fa006dc3a291e759a80c2331b65`.
- The initial ambient-shell temporary worktree add and push attempts were
  blocked by Overcommit not being available outside the Nix shell; rerunning
  the repository commands inside `nix develop .#vpsadminos` succeeded.
- GitHub Actions for the `staging` push:
  - RuboCop `27297150059`: success in 37s.
  - RSpec `27297150101`: success in 4m40s.
  - CI `27297150023`: first attempt failed in `firewall/conntrack#no-conntrack`.
    The downloaded artifact showed a refused-source TCP probe receiving
    `protected-tcp` and the expected protected-denial jump count as `0`. The
    merge diff contains no firewall, netfilter, or kernel-module changes, and
    the same commit's feature-branch CI had already passed, so this was treated
    as an unrelated firewall test race after inspecting logs.
  - CI `27297150023` attempt 2: success; build/cache job passed in 35s and the
    rerun test-suite job passed in 47m56s.
- Cleanup:
  - Removed `worktrees/2026-06-10-vpsadminos-cgroup-bug/vpsadminos`.
  - Removed `worktrees/2026-06-10-vpsadminos-cgroup-bug/vpsadminos-staging-merge`.
  - Removed transient local backup branch
    `backup/2026-06-10-vpsadminos-cgroup-bug-before-console-fix`.
  - Pruned stale vpsadminos worktree metadata.
  - Removed downloaded temporary CI artifact directories from `/tmp`.
  - Preserved local and remote feature branch refs.

## Open questions
- None.

## Cleanup
- Completed for vpsadminos worktrees created by this initiative.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
