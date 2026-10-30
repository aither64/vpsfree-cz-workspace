# Native production verification result

- Result: failed (exit status 1)
- Revision: `a6c0e10f4d0c828631a4bbf02da16fa3b6d556f5`
- Operation identity: `dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`, `gpt-6-luna/low`, `full_access/danger-full-access/approval never` (per retained catalog record supplied for this operation)
- Command:
  `nix develop --command env LIVE_SWITCH_CODEX=/nix/store/idil0dg5623qarasafiqsjfc3s2bm2a9-codex-package-0.165.0/bin/codex go -C portal test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -run '^TestNativeSessionCommunicationAuthorizationRoundTrip$' -count=1 -timeout=180s -v`
- Elapsed: 161 seconds total; Go test reported 150.534 seconds.
- Complete output: `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-29-cross-session-communication-authorization/verification/native-production.log`
- Remaining process: none; the captured command exited.

Bounded evidence from the run:

- `idle` and `steer` subtests failed; each reported `context deadline exceeded` after approximately 75 seconds.
- Final test summary: `--- FAIL: TestNativeSessionCommunicationAuthorizationRoundTrip (150.48s)` and `FAIL github.com/aither64/dev-workspace/portal/cmd/workspace-portal 150.534s`.
- Nix emitted the evaluation warning: `'system' has been renamed to/replaced by 'stdenv.hostPlatform.system'`.
