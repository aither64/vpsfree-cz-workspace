# Runtime tests and production build tail

- Result: passed (exit status 0)
- Tested revision: `1ab9853312a95b5448e99fd6f83f846453de17a5`
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/vpsadmin-webui` (clean before run)
- Command: `nix develop /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/vpsadmin-webui --command bash -e -c 'npm run test:bff; npm test; npm run build'`
- Elapsed: about 84 seconds, including Nix environment startup.

| Stage | Result |
|---|---|
| `npm run test:bff` | Passed: 58 tests, 0 failures (4.68 s reported by Node) |
| `npm test` | Passed: 343 test files, 2,227 tests |
| `npm run build` | Passed: Vite transformed 3,566 modules; build completed in 28.18 s |

Build emitted the existing Vite notice that some minified chunks exceed 500 kB. No stage failed. The command process has exited; no remaining process was reported.

Full output: `webui-runtime-tests-build-tail.log`. Captured exit status: `webui-runtime-tests-build-tail.exit`.
