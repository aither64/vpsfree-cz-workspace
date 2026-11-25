Result: failed (exit status 2).

- Revision: `5ffdb67df9d31de8a2de0952c73b92c9a234b424`.
- Input identity: `react-rebase-nov13/r1-tested-input.json` (as supplied).
- Command: `nix develop --command bash -c 'npm run typecheck && npm test -- src/pages/app/vps/VpsIncident.test.tsx src/pages/app/vps/vpsIncidentEscalation.test.ts && npm run lint:patterns && npm run audit:ui-strings:check && npm run audit:structural && npm run audit:component-contracts && npm run audit:mutations:check'`.
- Elapsed: 57.5 seconds (wall-clock from launch to exit).
- Complete log: `react-rebase-nov13/r1-affected-checks.log`.
- First step `npm run typecheck` failed. TypeScript reported TS7053 at `src/pages/app/vps/VpsIncidentSettingsForm.locks.test.tsx:18:77`: a `string` expression cannot index the inferred translation object without an index signature. Shell `&&` stopped subsequent commands. The five lock integration tests were not rerun.
- All watcher-owned command work completed; no sessions remain running.
