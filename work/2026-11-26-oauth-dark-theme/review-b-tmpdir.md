# B final narrow review: hosted temporary-directory correction

Reviewer0 returned no findings: no Blocking, Important or Advisory issue in the
new environment boundary. Original complete B and accepted62 source/cache/
workflow review conclusions remain applicable. This record condenses the returned
full report in the lead conversation, “Final narrow affected review — B hosted
temporary-directory correction”.

Bound session/current/live reviewer verified: thread
01a2178b-ad92-7421-94c0-062258b3674b, purpose review, saved
Sol/xhigh/read_only, no override/fallback/nested reviewer/team change.
General+risk lanes only. Read-only source/evidence review, no commands that
check/build/mutate/publish/deploy.

Repository vpsfreecz/vpsadmin,target master. Base
1bf7c120beaf21f7fd30f4b75441d4b835bc57af → reviewed clean final
913806a998d66f80fcc81757d402d1797f127c43,
tree164bf40a114ebf05fc4e44789693debdb096cc4c. HEAD/tree/merge-base/index verified.
One consolidated feature commit,45files+852/-105. Exact62cc1e3a..913806a9:
only4workflow additions, symmetric causal comment and TMPDIR:/tmp in Run RSpec
step env. Runtime/docs/source/cache/pin/runner/spec/manifests/aggregate/actions
unchanged. No obsolete approach/fixup/shim/redundant update, no migrations or
transitional version lineage, no repeated input/generated stream.

Representative exact62 hosted failure: canonical source guard passed, MariaDB
initialization EACCES below inherited runner temp,0examples/one outside error.
Official install-nix-action sets TMPDIR from RUNNER_TEMP when initially absent;
DB runner uses default Dir.mktmpdir root. No AppArmor mechanism asserted.
Step env restores prior host/tmp location only for RSpec/descendants. No widened
permissions, disabled confinement, added privilege, external DB or service
reconfiguration. Existing unique private Dir.mktmpdir directory, per-instance
socket/PID/log/data paths, local connection and owned shutdown/prune unchanged.
No shared fixed data directory or cleanup broadening. Both matrices symmetric;
other steps/Nix/Bundler source and result/coverage handling retained.

Quick proof covers actual parsed step-env precedence, Ruby temp-directory
selection, shell/actionlint and normal hooks. No local DB/spec check claimed to
reproduce hosted enforcement. Required actual hosted bootstrap and full/core
examples remain open. Prior62 installed graph/payload/source evidence stays
scoped, not a913 hosted/artifact pass.

Superseded1d/62 nonancestor verification/provisional E receipts preserved without
literal merge/final-successor claims. Final artifact, publication and E graph
remain later evidence. No default integration/release/deploy authority.

Inline causal comment is the smallest lasting explanation, without a guessed
AppArmor cause or private failure receipt. Existing testing docs remain accurate;
no prerequisite, DB safety/cleanup, coverage/compatibility/recovery guidance lost.
Explicit placement/preservation conclusion: no finding.

Lead accepted exact913 reviewed boundary after targeted4line diff inspection.
Feature publication/final metadata artifact released. First hosted verification
checkpoint is successful nonzero examples in one small full/core topic, then
required complete coverage. E waits this checkpoint before final input batch.
The existing workflow has dispatch without topic selector; a separate faithful
hosted probe would require new workflow machinery, while local Nix lacks the
host's distro permission boundary. No new framework or broad local diagnostic
repeat is justified. Progress response ci-bootstrap-loop records this choice.

[Owner evidence](vpsadmin-evidence.md), [state](state.md).
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-26-oauth-dark-theme/
