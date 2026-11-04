# Advisory E2E types verification

- Revision: `3e7f54e8176970cb0c04fc6cff7be85c09bd3ce0`
- Command: `nix develop ... --command bash -e -c` running `npm run typecheck:e2e:core` and Prettier check for `scripts/fixtures/e2e-type-coverage.json tsconfig.e2e.json`
- Exit status: 2
- Elapsed: 15 seconds
- Log: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-advisory-e2e-types.log` (7 lines, 547 bytes)
- Outcome: failed during `typecheck:e2e:core`; the chained Prettier check did not run because the shell uses `-e`.
- Bounded failure excerpt: `e2e/specs/admin/security_advisory_nodes_mobile_actions.spec.ts(118,39): error TS4111: Property 'E2E_SECURITY_NODE_ACTIONS_PROOF_SCREENSHOT' comes from an index signature, so it must be accessed with ['E2E_SECURITY_NODE_ACTIONS_PROOF_SCREENSHOT'].`
- Coverage output: 102 checked, 180 deferred.
- Remaining owned process: none; command exited.
