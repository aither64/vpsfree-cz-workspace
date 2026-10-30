Result: failed
Exit status: 1
Tested revision: c43904a72d705562b79dcf9d59a29cf743bc9de7
Command: nix develop --command env LIVE_SWITCH_CODEX=/nix/store/idil0dg5623qarasafiqsjfc3s2bm2a9-codex-package-0.165.0/bin/codex go -C portal test -mod=readonly -tags live_switch_integration ./cmd/workspace-portal -run ^TestNativeSessionCommunicationAuthorizationRoundTrip$ -count=1 -timeout=180s -v
Elapsed: 10.1s
Model/effort: gpt-6-luna/low
Execution policy: full_access; standalone launch policy explicitly danger-full-access / approval never; utility identity dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96
Log: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-29-cross-session-communication-authorization/verification/native.log
