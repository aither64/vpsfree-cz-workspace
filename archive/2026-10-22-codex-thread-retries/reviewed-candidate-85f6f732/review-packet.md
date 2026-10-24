# Final independent review packet

All intended deliverables are committed, clean, SSH-published and quick-checked. No independent review, native integration execution, deployment or merge has occurred. Review the complete branches, including generated pins, before longer verification.

Session: 2026-10-22-codex-thread-retries, workspace /home/aither/workspace/ai/vpsfree.cz.
Read plan.md, design.md, native-verification.md, state.md and rollout.md for context. Feature worktrees: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/<repository>.

## Requested result and boundaries

Application-owned automatic new-failure continuation without modifying Codex. Exact authoritative terminal codes serverOverloaded and cyberPolicy only; intermediate errors/refusals/text/quotas excluded. Capacity backoff 15,30,60,120,240,300 seconds then300 indefinitely, positive bounded jitter. Cyber immediate, maximum30 actual automatic submissions per thread in rolling300s, persisted across restarts; exhaustion requires manual action. Default-on managed lead/ready retained members, durable optout. Enrollment watermark excludes old failures and survives restarts. Native children excluded.

Use a visible neutral continuation, preserving history and exact failed execution settings; no replay/rollback/empty starts/model rewriting. Stable submission IDs and unknown outcomes reconcile only. Loaded idle only, no resume/steer/policy writes. Stop/manual/team/queue/settings/provider/package operations must serialize through authoritative admission and generation fences. UI reads server schedule, with toggle/cancel/countdown. Managed queued execution requires exact receipt/content/clientID + native exact turn context + unchanged authorized binding; display caches/defaults are not authority. Missing proof fails closed.

Accepted boundary: unmanaged direct native writers are outside managed admission guarantee. Native protocol has no expected-turn CAS; diagnostic native busy fixture is a post-review compatibility gate, not proof of global exclusion. No implicit lifecycle action, merge or machine release is authorized. Retry cannot promise to prevent a model repeating earlier side effects.

## Review policy and selection

HIGH risk: persisted state, uncertain submissions, concurrent/lifecycle/package authority, public API/protocol and deployment/rollback. Retained reviewer0 is independent, ready, review-purpose, read_only, gpt-6.1-sol/xhigh; use saved settings unchanged. Read ~/.codex/skills/mandatory-change-review/SKILL.md and ALL four references: general-review, architecture-review, scope-review, risk-review. Perform all lanes directly, no nested agents. No long native tests during review. Findings ordered Blocking/Important/Advisory, with evidence and lane. Explicitly conclude whole-branch history, repeated-stream consolidation, migration lineage and documentation adequacy.

## Complete base-to-head inventory

Each <repository>-final-inventory.json contains full commits, final diff stat and remote; matching <repository>-final.diff contains complete patch. Bases below are final reviewed comparison bases; original registrations remain in portal.yml. Workspace/config refreshed onto concurrent documentation/tracking-only defaults, clean range-diff equality; no deployed pre-refresh heads.

### codex-web

Remote git@github.com:aither64/codex-web.git; target master.
Base ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5; head d2d74f931cc50e39345c6c15931748062ee51951.

- af2d5bfe58006892af4c24b5fe891481d9ffcd05 codex: add exact failed-turn continuation and context reads
- 25f115ffc9f188d83452835b68376434887ff850 conversation: expose optional application-owned retry controls
- d2d74f931cc50e39345c6c15931748062ee51951 codex: verify failed-turn retries against a private native fixture

 README.md                              |   3 +-
 codex/client.go                        |   7 +
 codex/continuation.go                  | 167 +++++++++++
 codex/continuation_integration_test.go | 490 +++++++++++++++++++++++++++++++++
 codex/continuation_test.go             | 303 ++++++++++++++++++++
 codex/recovery_integration_test.go     | 152 +++++-----
 codex/timestamps.go                    |  48 +++-
 codex/turn_context.go                  | 330 ++++++++++++++++++++++
 codex/turn_context_test.go             | 115 ++++++++
 codex/turn_state.go                    |  80 ++++++
 conversation/assets/conversation.css   |   4 +
 conversation/assets/conversation.js    |  10 +
 conversation/assets/retry.js           | 108 ++++++++
 conversation/handler.go                |   6 +-
 conversation/retry.go                  |  86 ++++++
 conversation/retry_test.go             | 126 +++++++++
 docs/reference.md                      | 102 +++++++
 flake.nix                              |   2 +-
 test/codex_protocol_contract.py        |   9 +
 test/retry_browser_contract_test.cjs   |  82 ++++++
 20 files changed, 2148 insertions(+), 82 deletions(-)

### dev-workspace

Remote git@github.com:aither64/dev-workspace.git; target master.
Base bf6d4b0c49600c15e17fe71248807ef43424e932; head 85f6f7327e6948a13ad110c4c058d8b96b6ab2b9.

- 259fcd636ecb4afa0c7c4a2384c6f91d7ef8b353 turnretry: retain bounded retry policy and admission state
- 1f76716cdec2348d65039220cfc33616702b1e80 runtime: require retry-capable package transitions
- 0398d16bb166ccc2e16b683b9d45672172961d0c portal: continue new managed failed turns through durable retry admission
- 85f6f7327e6948a13ad110c4c058d8b96b6ab2b9 deps: pin codex-web failed-turn continuation support

 README.md                                          |   2 +
 docs/turn-retry-recovery.md                        | 108 +++++
 docs/workspace-portal.md                           |  43 ++
 flake.lock                                         |   8 +-
 flake.nix                                          |   2 +-
 libexec/dev-session                                |   7 +
 libexec/workspace-host                             |  13 +
 nix/workspace-portal.nix                           |   2 +-
 .../cmd/workspace-portal/codex_provider_scoped.go  |   8 +
 portal/cmd/workspace-portal/main.go                |  52 +++
 portal/cmd/workspace-portal/recovery.go            |  17 +
 .../turn_retry_native_integration_test.go          | 256 +++++++++++
 portal/go.mod                                      |   2 +-
 portal/go.sum                                      |   4 +-
 portal/internal/session/runtime-contract.json      |   1 +
 portal/internal/teamruntime/runtime.go             |  29 ++
 portal/internal/turnretry/controller.go            | 192 ++++++++
 portal/internal/turnretry/controller_test.go       | 176 +++++++
 portal/internal/turnretry/state.go                 | 345 ++++++++++++++
 portal/internal/turnretry/state_test.go            | 293 ++++++++++++
 portal/internal/turnretry/store.go                 | 339 ++++++++++++++
 portal/internal/web/server.go                      |  40 +-
 portal/internal/web/static/app.js                  |   6 +-
 portal/internal/web/templates/session.html         |   3 +-
 portal/internal/web/turn_retry.go                  | 237 ++++++++++
 portal/internal/web/turn_retry_test.go             | 180 ++++++++
 portal/internal/workspacecodex/client.go           |   7 +
 portal/internal/workspacecodex/observation.go      |  17 +-
 portal/internal/workspacecodex/recovery.go         |   2 +-
 portal/internal/workspacecodex/turn_retry.go       | 508 +++++++++++++++++++++
 portal/internal/workspacecodex/turn_retry_proof.go | 239 ++++++++++
 portal/internal/workspacecodex/turn_retry_test.go  | 187 ++++++++
 test/workspace_host/profile_transition_test.rb     |  23 +
 33 files changed, 3331 insertions(+), 17 deletions(-)

### workspace

Remote git@github.com:aither64/vpsfree-cz-workspace.git; target master.
Base 9f6968ebae4f1fbb26ff548ddcbd6cf8332a5b8b; head 31dc79ec37f3fffc8b0940e15ba532be3051c00c.

- 31dc79ec37f3fffc8b0940e15ba532be3051c00c workspace: select the failed-turn retry runtime

 flake.lock | 16 ++++++++--------
 flake.nix  |  2 +-
 2 files changed, 9 insertions(+), 9 deletions(-)

### vpsfree-cz-configuration

Remote git@github.com:vpsfreecz/vpsfree-cz-configuration.git; target master.
Base c1057731d34513b6ee3bb1dfb4a3e4832fdc67c9; head 37af6aaf2e635146de6c449f088088e1165c4ab7.

- 37af6aaf2e635146de6c449f088088e1165c4ab7 inputs: set devWorkspace to 85f6f732

 flake.lock | 14 +++++++-------
 1 file changed, 7 insertions(+), 7 deletions(-)

## History, migrations and pin streams

Nine logical commits total: client primitive/context plus adjacent tests/docs; optional browser/API; separate native fixture/harness; runtime durable core; package compatibility; runtime integration and adjacent tests/docs; library dependency; workspace pin; generated configuration pin. Runtime integration is kept together because capture, admission and dispatch establish one settings/recovery invariant.

Obsolete unpublished core aac0629 folded into259fcd6. Superseded unmerged A test8ccc536 amended into d2d74f9. Unpublished C pre-rebase bcccf30b/b4d16d53 replaced patch-equivalently. No obsolete approaches or transitional schema versions intended in final series. Independently verify.

No database migrations. Private retry schema1 is introduced directly; existing native submission schema3 and roster/history formats are unchanged. New retry records require turnRetryStateSchema=1 package capability, including cancelled records; unsupported downgrade refuses, forward recovery preserves IDs. No new feature/state version has been merged, released, deployed or externally consumed. Feature branch publication only; B dependency consumer is this same undeployed branch. Existing baseline formats remain supported.

Three separate owning pin streams, each consolidated once: B codex-web=d2d74f9 (flake/Go/vendor); workspace nested generic runtime=85f6f73; config dev-workspace channel/devWorkspace=85f6f73. No repeated superseded pins retained. final-input-graphs.json contains full graphs and evidence: extension767dfd587e346168e1443e65ccdb67ce748f3fe3 unchanged, only runtime+library nodes change, unrelated nodes/follows preserved. Runtime source nar sha256-wF7KqYtF8XMsgvtoSNMrql5d41WWisshgdhTd2s2MLs=; library nar sha256-O3GWvvYTSDKG3Ybsj0xbmEzGMLLSF09wv4iKc2DeIsU=.

## Ownership and consumers

codex-web owns ReadTurnState, exact ReadTurnContext, ledger-backed ContinueFailedTurn and optional Target.Retry provider/Capabilities.Retry HTTP/UI extension. Existing required Client interface and other embeddings remain compatible. Concrete dev-workspace consumer owns policy/store/admission/scheduling/authorization; discover imports/wrappers/pins rather than assuming consumer completeness. Workspace and configuration compose matching runtime selections; extension unchanged. Application is user-profile deployed, system config supplies host contract only. Read local AGENTS.md and applicable procedure routes in every affected repository.

## Quick evidence and documentation

A: focused state/context/continuation/reconciliation/idle-ledger Go tests PASS(~1s); retry API tests PASS; browser new+existing contracts PASS7groups; Node syntax PASS; pinned0.163.0 generated protocol contract/exact enum assertions PASS; diff PASS. Native compile-only and binary list PASS, both selectors present. No hook framework declared. Third test-only commit compile and affected fake tests PASS.

B: implementer1-evidence.md has exact commands, logs, diagnosed failures and corrections. Final normal core/workspacecodex/web PASS0.146/0.113/2.368s; race PASS1.253/1.272/1.626s; command regressions PASS1.516s; committed core PASS0.333s; tagged native compile/list PASS0.045s and expected top-level test present. Ruby aggregate retry gate1run5assertions0fail/error/skip; syntax/pins/diff PASS. All corrected failure causes recorded, no blind accepted reruns.

C: check-dev-workspace-deployment final pair PASS; deployment_contract_test4runs19assertions0fail/skip; Nixfmt/diff PASS. Config generated by confctl channel set --commit, active Overcommit Nixfmt+commit-msg passed (generated width warnings preserved). Both remote feature/default heads verified; all four clean final worktrees independently checked by lead.

A docs: README.md, docs/reference.md client/context and optional controls. B docs: README pointer, docs/workspace-portal.md Automatic turn retries, docs/turn-retry-recovery.md. Main lead direct user-facing writing pass completed before commits. Feature semantics/recovery in owning docs; individual prepared rollout in rollout.md. Routine generated pins need no extra docs per config instructions.

CI: old A25f run39796288718 green; final d2 run39800070219 not yet monitored. Superseded8ccc run cancellation rejected403 Actions-write; no cancellation/workaround, final run untouched. Not a source test failure.

## Post-review gates and rollout

native-verification.md owns exact selectors/subcase manifest/source-confirmed SSE and private pinned0.163.0 noauth loopback harness. A: TestPinnedCodexFailedTurnRetryContract plus existing cold recovery fixture. B: TestNativeTurnRetryController (one top-level, no subcases) plus existing live switch. Compile/list only so far, no native run. Require explicit selected PASS events, no skips/zero matches; direct native race acceptance/replacement fails gate and escalates.

After review/remediation, fresh Luna/low utility launches native and full package checks/builds. Builds/copies before machine-only reservation; exact aitherdev activation with matching system/profile sources, no reboot. Verify portal/naming/conversation continuity and retry UI, old-failure exclusion and restart. Forward package capability protects new state; older package cannot ignore it. Record exact store paths/graphs/head ancestry in rollout receipt. Existing package/operation recovery contracts remain authoritative.

Deployment is authorized by implementation plan; integration requires separate explicit user direction. Retain deployed machine until approved lineage integration, user acceptance and exact explicit release instruction. Session remains open. No claims/activation/merge/lifecycle mutation has occurred.

Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
