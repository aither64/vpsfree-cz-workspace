# Postreview focused browser verification — PASS

Exact reviewed head `f2765d3fd778927f4cda3563f66615bfcf72b7cf`, tree
`0f4949dc1c346bb4205940655f29965daeb16039`; native batch12890 consumed exit0.

| Released selection | Actual result | Command elapsed |
| --- | --- | --- |
| Whole VPS list-row + profile keys/sessions, Chromium | 13 passed | 69.806s |
| Whole profile transaction spec, Chromium + mobile Chrome | 3 per project / 6 passed | 22.309s |
| Exact lifecycle member-delete case, Chromium | 1 passed | 17.869s |

All20 cases passed on their sole attempt, with zero skipped, flaky or unexpected
results. The actual loaded config used two workers/retries0. Both complete files
reached later assertions; transaction cases retained positive request/recorder and
every-send normalized-location checks; lifecycle reached final navigation.

The ordinary pinned wrapper ran in the exact Gitless export with isolated loopback
Vite servers, E2E_START_SERVER=1 and CI=1 (no existing-server reuse). Runtime:
Node24.21.0/npm11.19.0, Playwright1.61.0, managed Chromium1228/149.0.7827.55,
actual HaveAPI npm0.32.0. Existing rooted FHS runtime matches the current locked
nixpkgs5e2305 and retained NAR/browser hashes. No build/install, policy relaxation or
artificial CPU/Nix caps. The original-owner monitoring fallback remained in effect.

All2489 exported tracked entries still match the reviewed source, locks unchanged;
no untracked environment/runtime-config overrides. All19972 retained private
entries, alias/live inodes, terminal952323/PTY323 and recovery refs remain unchanged.
Canonical live2e32 stays frozen. All owned FHS/server processes exited and all three
loopback ports released; no active owned operation or lifecycle/cleanup action.

This is synthetic mocked-fixture browser evidence, not live backend/deployment
acceptance. Original broad/smoke attempt1 failures and configured retries remain
preserved failures. The initial direct browser loader exit127 remains recorded in
existing-browser.json; retained-runtime reuse resolved setup before test execution.

Exact commands/cases, loaded config and source/input binding: [result.json](result.json).
Final preservation/process evidence: [effects.json](effects.json). Raw logs/results
are private0700/0600 at `/tmp/implementer3-react-e2e-postreview-l6zgw8p8`.

Source writer idle; stopped before publication/PR/default/site/deployment actions.
Lead owns shared tracking and next disposition. Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
