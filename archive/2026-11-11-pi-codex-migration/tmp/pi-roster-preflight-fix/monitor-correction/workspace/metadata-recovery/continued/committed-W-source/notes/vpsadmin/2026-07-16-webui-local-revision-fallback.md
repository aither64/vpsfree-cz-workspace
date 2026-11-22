# WebUI revision metadata in local integration tests

Initiative: `work/2026-07-13-security-advisory-automation/`

`./test-runner.sh test 'webui#navigation-readonly'` evaluates the vpsAdmin
worktree as a local Nix flake path. Such an input has neither `rev` nor
`dirtyRev`, so the packaged WebUI `.git-revision` file is intentionally empty
and `/etc/vpsadmin/build-info.json` has a null revision. Requiring a 40-character
revision in this environment fails before Playwright can test the UI.

Test the static application-version fallback when exact metadata is absent.
When metadata contains a full revision, compare both the rendered short hash
and GitHub link against that exact value. Use a pinned bridge dev cluster for
the strict deployed-revision check. This preserves truthful local behavior and
still detects propagation errors in a real deployment-shaped evaluation.

Verified on 2026-07-16: the isolated navigation suite passed, and the running
dev cluster rendered and linked the exact selected vpsAdmin revision while
services, nested-container, live-root, and Node build metadata agreed.
