# Native fixed verification result

- Result: failed (exit status 1)
- Tested head: `124be7794936b84c4b26811c7deb74ff3843666b`
- Elapsed time: 11 seconds
- Operation: `nix develop --command env LIVE_SWITCH_CODEX=/nix/store/idil0dg5623qarasafiqsjfc3s2bm2a9-codex-package-0.165.0/bin/codex go -C portal test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -run '^TestNativeSessionCommunicationAuthorizationRoundTrip$' -count=1 -timeout=180s -v`
- Complete output: `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-29-cross-session-communication-authorization/verification/native-fixed.log`
- Bounded evidence: both `idle` and `steer` subtests failed with `Codex RPC -32600: no rollout found for thread id ...`; package result was `FAIL`.
- Remaining process: none; the owned command exited.
