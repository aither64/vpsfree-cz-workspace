# Verification result

- Tested HEAD: `bee19b312ac3f2267053d51bc0e886bdcc05ec93`
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/vpsadmin-webui`
- Command: `nix develop … --command bash -e -c` running nested BFF `npm ci`, `npm run ci:tests`, then `npm run build` (stops on first failure).
- Exit status: 1
- Elapsed seconds: 25
- Full log: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-full-tests-build.log`
- BFF dependency install: `npm --prefix bff ci --no-audit --no-fund` completed; 89 packages added.
- Stage result: `npm run ci:tests` stopped in `test:scripts`; 239 passed, 1 failed (240 total). `test:bff`, `npm test`, and `npm run build` were not reached.
- Failure excerpt: `scripts/test-buckets.test.mjs:18` expected `node --test scripts/*.test.mjs` but observed `node --test scripts/*.test.mjs scripts/integration/*.test.mjs`.
- No verification process remains running. No source, lock, tracking, or Git files were edited by this watcher.
