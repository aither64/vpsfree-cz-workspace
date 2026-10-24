# Proposed checks after explicit B handoff — NOT EXECUTED

Preconditions: parent serializes imp2's Firefox and imp3's other fixture work,
applies the accepted three-path candidate, assigns the final B/Git owner and
binds the exact final published source head in the fresh utility's guard.
`candidate.patch` is based on d617; use `manifest.json`'s three original file
hashes to identify unchanged applicability. No pin/head is invented here.

Quick syntax from B's declared environment, once application is authorized:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
nix develop --no-update-lock-file -c bash -c 'set -e
node --check portal/internal/web/portal_improvements_browser_test.cjs
node --check portal/internal/web/team_settings_browser_test.cjs
node --check portal/internal/web/paging_browser_live_test.cjs
'
git diff --check
```

Decisive actual-browser argv, launched/monitored only by the parent's fresh
retained Luna/low utility after direct narrow inspection and final commit/guard:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/dev-workspace
PORTAL_BROWSER_TEST=1 \
DEV_SESSION_SLUG=2026-10-20-dev-workspace-portal-improvements \
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/portal-followup-absent-providers.json \
NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules \
PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers \
nix develop --no-update-lock-file -c go -C portal test -mod=readonly \
 -overlay /tmp/portal-followup-browser-assets-overlay.json ./internal/web \
 -run '^TestQuestionBrowser$/^(portal_improvements_browser_test[.]cjs|team_settings_browser_test[.]cjs|paging_browser_live_test[.]cjs)$' \
 -count=1 -timeout=20m -v
```

Use the same rooted PW1.59.1/browser set and pinned review-assets overlay as the
failed run; require the provider sentinel absent and both executable prerequisites.
Generate/verify the overlay through the already inspected preparation logic,
without editing application sources. Do not change TLS policy based on unrelated
loopback warnings. The exact command selects **only these three** actual browser
scripts; it does not rerun the other ten Question scripts, the three already
passed other wrappers, A/C checks, notifications or rawFirefox50.

Retain full output, exit code and wall time in a NEW receipt directory; never
overwrite failed evidence or reuse its PASS/FAIL record. Each subtest must reach
its later assertions; an early step passing is not complete fixture acceptance.
Report a later concrete failure before broadening. No repeated blind attempt,
longer budget, forced hidden action or weakened scroll tolerance.
