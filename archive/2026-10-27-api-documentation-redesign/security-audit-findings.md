# Independent Daybreak audit: accepted correction candidates

Provenance: deliberately shared lead message e47d852b-4e0a-4db1-a088-17f26ea705d8
from2026-10-29-haveapi-security-review. Main has not accessed peer files/team or
transcript. Native provideropenai/Codex subscription, gpt-daybreak-blue-latest,
xhigh. Hardware-key refusal resolved. Exact auditedf6e5c3750c747b33ec869c54ca220bf6f1d9d2d0→
ae46cf27a9afb6558d386c293cec7231dd6c423d/tree27dcf148f9b03867a3dfc65a29c76e77a87682ec,
fivecommits/baseancestor. Peer reports tracked source unchanged/all owned checks
exited. No introduced security regression confirmed. Two confirmed pre-existing
MEDIUM findings need source assessment and fixes under direct user authorization.

1. Ruby CLI generated examples shell injection. ruby_cli.rb18–20 leaves baseURL/
version unquoted;55–66 raw resource/action/path args;117–125 request values use
unescaped single quotes. server.rb243–257 derives baseURL from RackHTTP_HOST.
Attacker needs control over declared example data or Host/forwardedHost accepted
by deployment; victim copies/runs command. Impact is command execution with
victim developer privileges. Local fakehaveapi-cli blocked network and demonstrated
requestvalue quote breakout plus baseURLcommandseparation: two asserted marker
cases/0failures. Sinks predatebase, blame2016/2024. Proposed argv/token escaping,
not a serverHost policy change.

2. curl generated examples shell injection. curl.rb67–74 inserts prettyJSON into
a shell doublequoted argument, leaving shell substitutions active;13–46+74 URLs
are singlequoted without escaping apostrophes. Same attackercontrol+copy/run
requirements/impact. Fakecurl blocked network and two tests confirmed JSON
substitution+URLquote breakout. General sinks predatebase; earlier tokenlogin
quoting improvement leaves these request paths. Proposed escaped JSON/URL
arguments with one appropriate shelltoken serializer across init/auth/request.

Peer evidence: targeted security256/0 after missing declaredJS compiler inputs
prepared (initial2failures dependency-only); findingPoCs4/0; documentation395/0+
assetchecks, generateddocs19/0,TS63/0,Rust161/0,GoCLI92/0. These are peer-reported
results at exact source; no main rerun or broader execution claim. Coverage spans
docs dispatch/search/filtering/caches/HTML+JS+sample escaping/OAuthsessionPKCE/
statecookieOriginCSRFtransport/isolation/identitycleanup/literalcontracts. No
external/live/devcluster/realIdP/proxybrowsermatrix/dependency/unrelatedsubsystem
audit or fixes/merge/deploy. Full declaration anonymous policy treated as policy.

Disposition: architect0 owns static confirmation/minimal design, owner1 complete
fix/test/docs/normalcommit, reviewer0 final affected HIGH4lanes/history, main
inspection/publication and independent Daybreak audit rerun exact correctedhead.
No stale broad suite repeat; targeted defensive localfake-executable regressions.
No merge/default/release/production/deploy/lifecycle authority. Preserve original
reviewae46/deployed1b/source refs. Peer PoC details requested viaa1063814; no direct
peerfile access. Final finding reports remain peer-owned at:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-29-haveapi-security-review/.
