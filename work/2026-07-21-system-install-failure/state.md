# 2026-07-21-system-install-failure

## Repositories

- Repository: `vpsadminos`
- Branch: `2026-07-21-system-install-failure`
- Worktree:
  `worktrees/2026-07-21-system-install-failure/vpsadminos`
- Integration worktree:
  `worktrees/2026-07-21-system-install-failure/merge/vpsadminos`
- Base: `origin/staging` at `81a945228af4527de05f6cdbdcc243da0e9d44e1`

## Status

Complete. The fix is merged and pushed to staging, local verification passed,
and initiative worktrees and temporary artifacts were cleaned up. Staging CI
is queued for shared self-hosted runner capacity.

## Commands run

- `bin/dev-session current`
- `gh run view 29815572098 --repo vpsfreecz/vpsadminos ...`
- `gh run download 29815572098 --repo vpsfreecz/vpsadminos ...`
- Inspected the `system/install` artifact logs and relevant test/service code.
- `bin/dev-session worktree add 2026-07-21-system-install-failure vpsadminos
  --as-is --base origin/staging`
- `./test-runner.sh ls system/install`
- `nix develop --command overcommit --install`
- `nix develop --command overcommit --run`
- `nix develop --command git commit -F
  /tmp/vpsadminos-system-install-commit-message-20260721.txt`
- `./test-runner.sh test system/install` (first integration attempt; failed
  during Nix evaluation before VM startup)
- Reproduced the failed evaluation with `nix-build --show-trace`.
- `VPSADMINOS_CONFIG=/tmp/vpsadminos-system-install-test-config-20260721.nix
  ./test-runner.sh test --test-config tests/test-configs/ci.nix system/install`
- In the integration worktree: `git merge --ff-only
  2026-07-21-system-install-failure`
- In the integration worktree: `./test-runner.sh ls system/install`
- In the integration worktree: `nix develop --command overcommit --run`
- `git push --atomic origin 2026-07-21-system-install-failure staging`

## Results

- CI ran commit `81a945228` and reported 74 successful tests plus one
  unexpected failure: `system/install`.
- The failed assertion was `test -d /tank/conf/pool` at 16:32:50.
- The test's readiness loop returned as soon as
  `org.vpsadminos.osctl:active=yes` became visible. `osctl pool install` sets
  that property before osctld finishes importing the pool and creating its
  configuration directories.
- Logs show osctld was still creating `tank/conf` and the remaining datasets
  while the assertion ran. Pool import completed at 16:32:50.628 and the
  `pool-tank` one-shot service completed at 16:32:51.298.
- The triggering eBPF change is unrelated; its build and dedicated exporter
  tests passed.
- `system/install` discovery/evaluation passed.
- All Overcommit pre-commit hooks passed (Nixfmt and RuboCop).
- A first commit attempt from the ambient shell was stopped by the active
  Nixfmt hook because `nixfmt` is provided by the Nix development shell. The
  commit will be retried through `nix develop`; no hook is bypassed. This is
  recorded in
  `notes/vpsadminos/2026-07-21-commit-hook-needs-nix-develop.md`.
- Fix committed as `173ebb6` (`tests: wait for installed pool service`). The
  single commit contains only the system installation test synchronization
  change.
- Mandatory standalone change review of `173ebb605` passed with no blocking,
  important, or advisory findings. The reviewer independently confirmed the
  artifact timing, the one-shot service completion contract, the focused
  commit, and the lack of runtime or compatibility impact. The only residual
  gap was the intentionally deferred targeted integration test; proceeding
  with it was recommended.
- The first targeted integration attempt failed after 19 seconds, before VM
  startup, because `system.vpsadminos.revision` evaluated to null in the linked
  Git worktree. `os/modules/misc/version.nix` recognizes only a `.git`
  directory, while linked worktrees use a `.git` file; channel-registration
  tried to interpolate the null revision. The CI checkout is a normal clone and
  had revision `81a9452`, as confirmed by its artifact. The failure is local
  test-environment metadata, unrelated to the committed assertion change.
- A temporary Nix module at
  `/tmp/vpsadminos-system-install-test-config-20260721.nix` supplies the exact
  feature commit revision and suffix for the retry; it does not alter the
  repository or tested code.
- The targeted retry passed all six examples. `system/install` completed
  successfully in 2,186.88 seconds; the pool initialization regression example
  passed in 33.58 seconds and retained all original state assertions.
- The linked-worktree revision issue and verified workaround are recorded in
  `notes/vpsadminos/2026-07-21-system-install-worktree-revision.md`.
- After a final fetch, `origin/staging` still matched the verified base
  `81a945228`; no rebase was needed. Local staging was fast-forwarded to
  `173ebb605` in the fresh integration worktree.
- Integration-worktree test discovery passed and all Overcommit hooks passed.
- The feature branch was preserved on GitHub and staging was pushed to
  `173ebb605` atomically.
- Staging CI run 29869018177 is queued:
  `https://github.com/vpsfreecz/vpsadminos/actions/runs/29869018177`.

## Open questions

- None.

## Cleanup

- Removed the feature and staging integration worktrees.
- Removed the downloaded CI artifact, targeted test state, temporary commit
  message, and temporary revision override (approximately 447 MiB total).
- Preserved local and remote branches `2026-07-21-system-install-failure` and
  `staging`, both at `173ebb605`, as required.
- CI run 29869018177 was still queued after 18 minutes. The original run waited
  more than four hours for the same self-hosted build job, so this is recorded
  as external runner capacity rather than a failure. No CI failure or rerun was
  left uninvestigated.
