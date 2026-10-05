# Payload fixture memory correction review

Session2026-09-23-storage-redesign, workspace/home/aither/workspace/ai/vpsfree.cz.
Tracking plan.md/state.md/design.md section Payload fixture minimum-memory correction.

## Complete committed deliverable

Provider worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/vpsfree-dev-workspace-storage-profile
Base77dd0d0447f48c8d8e667257cef2276738d053a0, published/merged/consumed.
Head0ff827df13e82dfab4b536ff29979280f264e8f5; tree867d2378792da1fb3c2cd707b881c04bd17426c0.
COMPLETE unmerged series: ONE commit, vpsadmin: meet the guest seed memory minimum in the payload fixture.
COMPLETE final diff: TWO paths,51+/1-.
Full-index/binary SHA256e699a0b7bdb04f03967ee63f2269f520dc9af2def6a6cba0fb63781931f4928a.

- dev-clusters/vpsadmin/tests/storage-profile-acceptance.rb
  SHA77f2c2558a8759acaad5bcd0f38e43c9755d2cb6e8af1461d8e60a8599019195.
  Exactly memory512->1024 in actual Guest.prepare! VPS request.
- test/vpsadmin_storage_profile_spec.rb
  SHAfcbdc90ddecc8d5690e44eb08466153d2ddc0276c47ca2d17650fbfa965db98c.
  One actual request/guest seed compatibility regression.

No obsolete unmerged approach/fixup/input stream/unused compatibility path/migration introduced.
Prior77dd history is already merged/consumed and preserved. NO SQL migration, wire,
state-format, CLI/module interface, resource policy, Node or schema delta.
Inherited maintenance2/applied1/schema1-policy3 unchanged. Companion Admin290f's
two previously consumed migrations are unchanged/outside this range.
Require explicit COMPLETE branch obsolete-history/migration conclusions.

## Demonstrated defect and outcome

One installed owning payload attempt failed1/27.444s/stage1: actual guest
ClusterResourceAllocationError rejects512 MiB against selected Admin290f
api/db/seeds/test.nix memory minimum1024. Ordinary API spec seed minimum128
misses this discrepancy. Userchain48/user5 completed; fresh owning SQL shows
done/unfinishedtx0/pendingconfirmation0/chainlock0 and fixtureVPSrows0.
Original protectedDBchanges0. Schedulerstopped; admitted objects/diagnostics
retained, no retry/deletion/cancel/unlock/mode change.

Request1024 MiB, retain CPU1/swap0/disk4096/shared4096 allowance. Regression
projects only unique selected seed memory min/max/stepsize via bounded test-only
Nix, captures actual Guest.prepare! resources at ordinary Operations::Vps::Create.run
and uses finite sentinel before physical staging. Only preceding User-chain/wait/
admitted effects substituted; actual AR member/Pool/template. Verify meaningful
coverage/proportionality/failure ownership. Actual creation/transfers remain owning
retained scenario after immutable delivery.

## Supplied quick verification and documentation

Ruby syntax2/diff0. Fresh Luna/low full existing AR provider profile file on exact
Admin290f:48examples/0failures/65.106s; provider nix flake check --no-build
--print-build-logs:0/13.224s. Batch0/78.929s/parity1. No processrunning.
Lead inspected frozen diff/hashes/normal new commit. No declared provider hooks
framework found; normal git commit used. Source/index clean.
Private /tmp/storage-retained-resume-20261005 evidence is supplied only;
reviewer MUST NOT read private logs or rerun checks.

Exact full harness FROM registered Adminroot (shell enters api itself):
nix develop /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/vpsadmin#api -c /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/vpsfree-dev-workspace-storage-profile/dev-clusters/vpsadmin/tests/run-storage-profile-api-specs.sh
ConfiguredDB refusal/automatic disposableDB/controlledRSpec options unchanged.

Existing provider README Storage profile verification owns fixture/deployment/
failure semantics; no interface/procedure change requires another lasting page.
Spec comment explains seed mismatch. Routine design/state/rollout and reusable
note record this failed trial separately. No new native/Node/VM/CI gate or CIwait.

## Consumers, compatibility and pending delivery

Installed77dd/wg7 builds its relative CLUSTER_DIR and embeds acceptanceSEED_FILE
in ordinary guestwrapper; worktree/hostscript edit cannot alter guest immutable body.
Rootc754 pins77dd/generic3ed/Codex3d07/disableddefaultAPI5c76+OS158. Actual enabled
retained guest uses Admin290f/selectedOS feature sources. Provider inputs/lock/
all other source exact77dd.

After review lead may publish feature, generate normal consumer pin and prove
package/scripts. External-idle public activation, ordinary services update and
actual guestSEED_FILE/preservation proof precede ONE justified new fixture/key.
No provider override/private helper/store edit. Faileduser5 preserved.
New default merge approval NOT inferred; API/OS/config/WebUI remainfeatureonly.
Source/package proof is not payload/retirement/quiet/repair/APPLY acceptance.

## Assignment

High risk classification from retained guest host behavior/deployment-order context;
small reversible request change/interfaces unchanged. Review ALL4lanes:
general,architecture/repetition,scope/proportionality,risk/compatibility.
Saved reviewer0 gpt-6.1-sol/xhigh/read_only, no override/fallback.
Read canonical mandatory-change-review SKILL and ALL4references plus applicable
workspace/provider/Admin guidance and verify exact binding/roster.
Direct independent committed COMPLETE range review; no nestedreviewer/edits/
private reads/tests/build/DB/network/ref/index/cluster actions.
Findings first,severity/file/line/commit; explicit obsoletehistory/migration
conclusions and residual gates, no default integration/runtime clearance.

## Accepted independent result, 2026-10-05

reviewer0 completed the exact committed77dd..0ff review with saved
Sol/xhigh/read_only settings and no Blocking, Important or Advisory findings
in all four assigned lanes. It confirmed complete one-commit history, exact
two-path51+/1- final delta/tree867d2378 and packet hashes, no obsolete artifacts
and NO SQL migrations. Request compatibility coverage is48/0 lead evidence;
real VPS creation/transfers and immutable delivery remain separate pending
gates. Consumed77dd and faileduser5/chain48 are preserved. No default integration,
activation or runtime acceptance follows from this result.
