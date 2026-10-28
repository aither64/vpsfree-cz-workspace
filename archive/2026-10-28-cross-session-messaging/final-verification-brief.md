# Final verification and build batch

Fresh one-operation verification utility, installed gpt-6-luna/low, explicit
full access/never. Read /home/aither/.codex/skills/dev-session-monitor/SKILL.md
and each affected repository's AGENTS before command execution. No source or
tracking edits, diagnosis, retries, deployment, approval or nested agents.
Only logs and the final result artifact below may be written.

All worktrees are under
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-cross-session-messaging.
Use complete logs under shared
/home/aither/workspace/ai/vpsfree.cz/work/2026-10-28-cross-session-messaging.
Verify exact HEAD before each relevant command. Stop on first failure and report;
do not run a command twice. No quiet-output deadline. Expected 15-30 minutes
for this related final acceptance/build batch. If an unexpected local Linux
kernel compilation starts, stop only this owned batch and report it. Do not
cancel unrelated builds. Keep any active handle accounted for.

1. In dev-workspace at e9153e614e44766d0f0efd6721b34b7bf2f4c14a:
   `nix flake check --print-build-logs`
   Log final-flake-check.log. This includes package, Ruby and native VM checks.
2. Same directory/head:
   `nix develop --command bash -c 'set -e; npm install --prefix /tmp/cross-session-messaging-playwright --no-audit --no-fund @playwright/test@1.59.1; export NODE_PATH=/tmp/cross-session-messaging-playwright/node_modules; export PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers; export PORTAL_BROWSER_TEST=1; export DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/cross-session-messaging-no-provider-catalog; go -C portal test -mod=readonly ./internal/web -run "^TestQuestionBrowser/communication_browser_test.cjs$" -count=1 -v'`
   Log final-browser.log.
3. In workspace at 31a3deb3449aa4357bb8ff942e9f30ae948625e0:
   `nix build --json --out-link /tmp/cross-session-messaging-profile .#default`
   Log final-profile-build.log, retain output package and derivation identities.
4. In vpsfree-cz-configuration at b4b0c17b11a873bc0b864cb8a6e91345d76653a3:
   `nix develop --command confctl build cz.vpsfree/machines/aitherdev`
   Log final-system-build.log, retain built system and generation identities.
5. Runtime CI exact run 40678431473, head e9153e61:
   `gh run watch 40678431473 --repo aither64/dev-workspace --exit-status`
   Log final-runtime-ci.log. On failure, collect `gh run view --log-failed` for
   this exact run into final-runtime-ci-failed.log; no rerun or diagnosis.

Return a compact result with exact heads, command results, elapsed time,
store/derivation paths, logs, failure excerpt or pending work. Output is captured
as final-verification-result.md by the launcher. Do not edit state.md.
No deployment command is authorized in this verification role.

Execution correction after the prior utility omitted log capture and accidentally
restarted a failed check: run only `python3 verification-batch-2.py` from this
tracking directory. The supplied driver executes the five commands above once,
checks exact heads, captures full logs and records real monotonic elapsed time
and process identity in verification-batch-2-status.json. Its exclusive started
marker prevents accidental duplicate runs. Do not remove that marker or bypass
the driver. If it already started, observe its status and original handle.
Read status and tail the current named log as needed; stop only an unexpected
local kernel build, otherwise report failures without retries or source changes.
The driver is the parent-selected operation, not permission to change commands.
Use the actual recorded time, not sums of requested poll durations.
