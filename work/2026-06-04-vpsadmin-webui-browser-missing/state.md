---
lifecycle: active
---
# vpsadmin webui browser missing investigation

## Status

- Fix implemented and verified with a representative webui browser script.

## Repositories

- `vpsadmin`
  - Worktree: `worktrees/2026-06-04-vpsadmin-webui-browser-missing/vpsadmin`
  - Branch: `2026-06-04-vpsadmin-webui-browser-missing`
  - Base: `origin/master` at `15d561f9ac1c6477d60efd37fc6f2bc06b5a7692`
  - Commit: `77e6e4c3f` (`tests: fix webui Chromium executable path`)
  - Remote branch:
    `origin/2026-06-04-vpsadmin-webui-browser-missing`
  - Commit under investigation: `4f413dfd0e5a49aa0d1e08ec49ca24929072422d`
  - GitHub Actions run: `https://github.com/vpsfreecz/vpsadmin/actions/runs/26969448540`

## Findings

- The failing job was `Run selected ci-tagged tests`.
- The unexpected failed test was `webui`; its split scripts all failed once
  Playwright could not launch Chromium.
- Artifact downloaded to `/tmp/vpsadmin-test-logs-26969448540`.
- First Playwright failure:
  `/nix/store/2syav3jl7mja3sn8wv4ihma5719jpkgg-playwright-browsers/chromium-1217/chrome-linux/chrome`
  did not exist in the services VM.
- The browser path was copied into the VM image according to `test-runner.log`,
  but image construction also logged `Invalid argument` while reading that
  store path under `/build/root/nix/store`.
- The copied Nix browser package itself contains the x86_64 Chromium layout:
  `/nix/store/2syav3jl7mja3sn8wv4ihma5719jpkgg-playwright-browsers/chromium-1217/chrome-linux64/chrome`.
  It does not contain `chrome-linux/chrome`.
- Playwright 1.59.1 maps Chromium executable paths by short platform:
  `linux-x64` uses `chrome-linux64/chrome`; `linux-arm64` uses
  `chrome-linux/chrome`.
- The services VM booted as `NixOS 26.05pre-git (x86_64)`, and the API Ruby
  process logged `x86_64-linux`.
- Reproducing the same package locally on x86_64 resolves Chromium to the
  existing `chrome-linux64/chrome` path. Forcing
  `PLAYWRIGHT_HOST_PLATFORM_OVERRIDE=ubuntu24.04-arm64` resolves to the exact
  failed CI path, `chrome-linux/chrome`.
- Correction from follow-up inspection: the failed path is produced by
  `tests/playwright/webui/playwright.config.cjs`, not by Playwright's internal
  platform resolver. The config hardcodes
  `path.join(browsersPath, chromiumDir, 'chrome-linux', 'chrome')`.
- Root cause: vpsadmin's webui Playwright config hardcodes the old/ARM64
  Chromium executable subdirectory while nixpkgs 26.05 packages x86_64
  Chromium under `chrome-linux64/chrome`. The webui assertions did not run.
- Switching to Firefox would avoid this exact Chromium subdirectory mismatch
  because Firefox's Playwright executable path is `firefox/firefox` for both
  Linux x64 and arm64, but it is a workaround with browser-compatibility risk.
  The direct fix is to stop hardcoding the Chromium path, or to check both
  `chrome-linux64/chrome` and `chrome-linux/chrome`.
- vpsAdminOS `origin/staging` moved on 2026-06-05 to
  `62de2d8b03876d84a997fcfd5fc30740da786ddf`, updating nixpkgs 26.05 from
  `b51242d7d` to `6b316287b`. Latest nixpkgs 26.05 still packages x86_64
  Chromium as `chrome-linux64`, and `pkgs.playwright-driver.version` remains
  `1.59.1`, so the nixpkgs update does not fix vpsadmin's hardcoded path.
- Implemented fix in `tests/playwright/webui/playwright.config.cjs`:
  `chromiumExecutable()` now checks both `chrome-linux64/chrome` and
  `chrome-linux/chrome`, returning the first executable that exists and failing
  early with a clear error if neither is present.

## Verification

- `git diff --check`: passed.
- Config-level check against the failed run's browser package:
  resolved `/nix/store/2syav3jl7mja3sn8wv4ihma5719jpkgg-playwright-browsers/chromium-1217/chrome-linux64/chrome`.
- Config-level check with a temporary old-style `chrome-linux/chrome` layout:
  resolved the fallback executable.
- `./test-runner.sh ls 'webui#navigation-readonly'`: listed
  `webui#navigation-readonly`.
- `./test-runner.sh test 'webui#navigation-readonly'`: passed on
  2026-06-05. The example
  `webui read-only navigation browser flow passes Playwright read-only navigation tests`
  succeeded, and the script finished successfully in 350.27 seconds.
- `bundle exec overcommit --sign` and
  `bundle exec overcommit --sign pre-commit`: updated local Overcommit
  signatures so installed hooks could run.
- `git commit -F <tmpfile>`: created commit `77e6e4c3f`. Pre-commit hooks
  passed. Commit-message hooks passed with text-width warnings at 72 columns;
  all commit-message lines are within the workspace 80-column requirement.
- `git push -u origin 2026-06-04-vpsadmin-webui-browser-missing`: pushed the
  feature branch.
- GitHub Actions run
  `https://github.com/vpsfreecz/vpsadmin/actions/runs/27020058713`: completed
  successfully. The selected CI filter was `tag=ci && (tag=webui)` because the
  change matched one runtime path. CI ran all 18 webui scripts and reported:
  `Run 18 test scripts of 1 tests in 9159.96 seconds`; `1 tests successful`.
  Job URL:
  `https://github.com/vpsfreecz/vpsadmin/actions/runs/27020058713/job/79745263330`.
- Merged into `master` from a detached temporary worktree at
  `worktrees/2026-06-04-vpsadmin-webui-browser-missing/vpsadmin-master-merge`.
  The merge was a fast-forward from `15d561f9a` to `77e6e4c3f`.
- Post-merge `git diff --check HEAD~1..HEAD`: passed.
- `git push origin HEAD:master`: pushed `master` from `15d561f9a` to
  `77e6e4c3f`.
- GitHub Actions master run
  `https://github.com/vpsfreecz/vpsadmin/actions/runs/27033565259` started for
  commit `77e6e4c3f` and completed successfully. It selected
  `tag=ci && (tag=webui)`, ran all 18 webui scripts, and reported
  `Run 18 test scripts of 1 tests in 6879.23 seconds`; `1 tests successful`.
  Job URL:
  `https://github.com/vpsfreecz/vpsadmin/actions/runs/27033565259/job/79791737139`.
- Removed initiative worktrees:
  `worktrees/2026-06-04-vpsadmin-webui-browser-missing/vpsadmin-master-merge`
  and `worktrees/2026-06-04-vpsadmin-webui-browser-missing/vpsadmin`.
  Removed the empty parent worktree directory. The local and remote feature
  branch refs were intentionally kept.

## Commands Run

- `gh run view 26969448540 --repo vpsfreecz/vpsadmin --json ...`
- `gh run view 26969448540 --repo vpsfreecz/vpsadmin --job 79580562775 --log-failed`
- `gh run download 26969448540 --repo vpsfreecz/vpsadmin --name vpsadmin-test-logs-26969448540 --dir /tmp/vpsadmin-test-logs-26969448540`
- `git --git-dir repos/vpsadmin.git worktree add --detach worktrees/2026-06-04-vpsadmin-webui-browser-missing/vpsadmin 4f413dfd0e5a49aa0d1e08ec49ca24929072422d`
- `find -L /nix/store/2syav3jl7mja3sn8wv4ihma5719jpkgg-playwright-browsers/chromium-1217 -maxdepth 2 -type f -name chrome -print`
- `NODE_PATH=/nix/store/1i3ahl6fk8llj3f0qnpzmi6rvks5fxdi-playwright-test-1.59.1/lib/node_modules PLAYWRIGHT_BROWSERS_PATH=/nix/store/2syav3jl7mja3sn8wv4ihma5719jpkgg-playwright-browsers node -e ...`
- `PLAYWRIGHT_HOST_PLATFORM_OVERRIDE=ubuntu24.04-arm64 ... node -e ...`
- `git --git-dir repos/vpsadmin.git show origin/master:tests/playwright/webui/playwright.config.cjs`
- `git --git-dir repos/vpsadminos.git show --no-patch --format='%H %ci %s' origin/staging`
- `nix eval --raw github:NixOS/nixpkgs/nixos-26.05#legacyPackages.x86_64-linux.playwright-driver.browsers-chromium.drvPath`
- `git switch -c 2026-06-04-vpsadmin-webui-browser-missing origin/master`
- `git diff --check`
- `./test-runner.sh ls 'webui#navigation-readonly'`
- `./test-runner.sh test 'webui#navigation-readonly'`
- `bundle exec overcommit --sign`
- `bundle exec overcommit --sign pre-commit`
- `git commit -F <tmpfile>`
- `git push -u origin 2026-06-04-vpsadmin-webui-browser-missing`
- `gh run view 27020058713 --repo vpsfreecz/vpsadmin --json ...`
- `gh run view 27020058713 --repo vpsfreecz/vpsadmin --job 79745263330 --log`
- `git --git-dir repos/vpsadmin.git fetch origin master 2026-06-04-vpsadmin-webui-browser-missing`
- `git --git-dir repos/vpsadmin.git worktree add --detach worktrees/2026-06-04-vpsadmin-webui-browser-missing/vpsadmin-master-merge origin/master`
- `git merge --ff-only 2026-06-04-vpsadmin-webui-browser-missing`
- `git diff --check HEAD~1..HEAD`
- `git push origin HEAD:master`
- `gh run list --repo vpsfreecz/vpsadmin --branch master --commit 77e6e4c3fc106c83fe9f209d728b3421e586dac4 --limit 5 --json ...`
- `gh run watch 27033565259 --repo vpsfreecz/vpsadmin --exit-status`
- `git --git-dir repos/vpsadmin.git worktree remove worktrees/2026-06-04-vpsadmin-webui-browser-missing/vpsadmin-master-merge`
- `git --git-dir repos/vpsadmin.git worktree remove worktrees/2026-06-04-vpsadmin-webui-browser-missing/vpsadmin`
- `rmdir worktrees/2026-06-04-vpsadmin-webui-browser-missing`
- `gh run view 27033565259 --repo vpsfreecz/vpsadmin --json status,conclusion,jobs,url,headSha,createdAt,updatedAt`
- `gh run view 27033565259 --repo vpsfreecz/vpsadmin --job 79791737139 --log | rg ...`

## Notes

- Worktree creation triggered Overcommit's config signature warning, but no
  commit is being made.
