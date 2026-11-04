# Quick verification watcher result

- Result: failed (command exited 2).
- Tested revision: `aef727cff377c8368268bf61c881d173efe88ef5`.
- Command: supplied `nix develop ... --command bash -e -c` running `npm run typecheck` followed by the three specified Node tests.
- Working directory: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/vpsadmin-webui`.
- Elapsed: approximately 58 seconds.
- Full output: `w-review-fixes-quick.log`.
- Failure excerpt: `NodeHistoryPanels.test.tsx(37,11)` and `(37,82)` report TS2339: `configured_value` does not exist on a union member `{ id: number; }`.
- The shell used `bash -e`; typecheck's nonzero exit stopped the command before the requested Node test files ran.
- Remaining process: none; the single verification process exited normally.
