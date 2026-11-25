# Integration progress checkpoints

Superseded checkpoints; final status is in [state.md](state.md).


# Archive failure fix: approved integration in progress

Approved integration in progress. Root cause fixed and deployed in the workspace
user profile. Independent review, CI and all four final verification targets
passed. Passive deployment/usability verification passed. The original failed
archive was not retried; no session lifecycle operation was performed.

User approval in the current conversation: "ok, merge and release aitherdev".
This explicitly accepts the preceding named master merges for dev-workspace,
workspace and vpsfree-cz-configuration and release of this session's aitherdev hold.
No lifecycle action is authorized. Integration is in progress; release only after
fresh verified remote integration and deployed-lineage/effect evidence.
Keep this session open.

## Phase checklist

- [x] Investigation and architect-owned design
- [x] Committed implementation and quick checks
- [x] Independent final review; mechanical refresh proof
- [x] Required package / archive VM / app / composition verification
- [x] Profile-only deployment and passive usability verification
- [x] Explicit master integration approval
- [ ] Approved integration, fresh remote proof and machine release

## Root cause and fix

The browser repeated native-monitor safety proof already returned as quiescent by
CLI archive-check, within the same 30-second admission deadline. The failed ordinary
archive had completed all six readiness checks, then timed out before executor
handoff. Its 59 retained native monitor records made the duplicated work costly;
individual RPC timing was not logged.

The fix consumes the validated typed quiescent result immediately in the same
admission, after checking cancellation. Missing proof and blocked/quiesceable
observer assessment/owner/join/recheck paths remain. The executor still freshly
validates readiness before shutdown/removal. No timeout, cache, schema or authority
change. See [design.md](design.md) and [core-evidence.md](core-evidence.md).

## Final published branches

All use branch `2026-11-25-archive-failure-investigation` under this session's
worktree group. No default-branch integration was executed.

| Repository / target | Current final head | Prepared master base |
| --- | --- | --- |
| dev-workspace / master | f6d60bf87002fb1896599f35f0284743c16d7e6f | 91cafd4c0c50ffb7208498a605707c4c3b1b1174 |
| workspace / master | 30b74dc3278728ab36197e0d2ef2cf76c66cf791 | e7b876f69aca4554d52a3ac19ed097263847ad43 |
| vpsfree-cz-configuration / master | fdcb0a2c3f6413224a8e32b4b887eaf2ca8ecf81 | 9bdb0c68b47ceebde450fcdf018727b382cacc09 |

Clean detached runtime/config targets and declared hooks are ready; shared workspace
stays on master with unrelated records/index preserved. Follow
[integration-preparation.md](integration-preparation.md), fresh target checks and
one short repository claim at a time only after explicit approval. Shared workspace
also takes its nonblocking tracking lock after the claim. Release ownership before
CI, records or cleanup; stale/intervention cases return to unlocked preparation.

## Verification and review

- Final quick archive and monitor checks passed; source commits/SSH publication
  and ordinary hooks are documented in core/deployment evidence.
- Final CI run45636961676, workflow354263807, attempt1, exactf6: SUCCESS.
  Session-creation smoke and essential application contracts passed; extended
  archive job was skipped and was covered by the explicit local VM check.
- Independent reviewer0, retained Sol/xhigh/read_only, HIGH risk/all four lanes:
  no Blocking, Important or Advisory findings. Complete history/consolidation,
  no migrations and documentation preservation explicitly accepted.
  [review.md](review.md) preserves the returned report verbatim.
- Refreshed generated pins retain that review through coordinator complete-tree
  reconstruction and exact complete-input/application/composition derivation
  equality: [mechanical-refresh-review.md](mechanical-refresh-review.md).
- One final immutable four-target Nix batch passed exit0, 15:04:23–15:35:08Z,
  1845s (30m45s): packagecheck, isolated archive-lifecycle VM, composed application,
  site composition. VM1689.35s + normal QEMU cleanup0.77s. No retry, unexpected
  local kernel compilation or surviving utility effects. Overrun was reassessed
  against actual fixture transitions. [verification-evidence.md](verification-evidence.md)
  owns full refs/graphs/derivers/outputs/NARs/logs and exact G reuse proof.
- Runtime final-head comparison already exists for reviewed65544340..f6, saved
  2026-11-25T14:45:38.545868993Z. A later ordinary capture refused to replace that
  head's original base; owner verified the existing receipt read-only (SHA256
  acb857630f64ec36184b7ce0d8a74b2bb139397a0b203d4a3e3b9918eb540122).
  Capture requirement is satisfied; do not overwrite it. G captures are current.

## Deployment, effects and held resource

User authorized aitherdev deployment. Accepted actual-host/helper/service/native
proof supports profile-only rollout; system was not switched for provenance-only
configuration metadata. Complete input and host/source graphs are in
[deployment-preflight.md](deployment-preflight.md),
[deployment-evidence.md](deployment-evidence.md) and [rollout.md](rollout.md).

- Selected app: `/nix/store/apjaqip0xj9cy297z2wmb8hmfqn2c8x1-dev-workspace-0.2.0`.
- Deriver: `/nix/store/m9pdsbnrrlwkyhp87d3cic5am7c10rbs-dev-workspace-0.2.0.drv`.
- App NAR: `sha256-RkOrVrQUH16XU9dN3JhiFumWgZGJGI2KyvgLRpUWIQs=`.
- Runtime source: `/nix/store/hh81k6nk1r1x0jhi0v8a1l9d53jr0h4n-source`, exactf6;
  full source/input identities match the accepted G proof.
- Actual system and system profile remain
  `/nix/store/k79k3l35lnhfikw65zwnacag112w7z9p-nixos-system-aitherdev-26.05.20261121.94c3211`.
  This is not a deployment of the prepared new configuration toplevel.
- Root ordinary switch ran once, source30b74dc3, 15:38:21.822–15:41:04.277Z,
  exit0 /162.454s. Driver/tool73258 joined; PIDs164111/164393 absent. Logs/result:
  `/tmp/archive-failure-profile-run-51ed48c0/`.
- Native protocol and local semantic observation preflights passed. Watcher dispatch
  waited across the package switch and rejected as superseded; root used visible
  bounded parent observation, then retried the read-only assignment at new generation.
  No activation retry or unnecessary postterminal watcher.
- I passive verification15:43:45–15:45:23Z: selected package/deriver/source/input
  equality; unchanged native PID3138515/startTicks180371132/exe2rq; portal/router/
  coordinator/Codex active. Own health/page/details200, interactive active root,
  no pending lifecycle/execution hold, own tmux$125 retained. Naming process/socket
  provenance checked; no naming inference/conversation send or session creation.
  [deployment-verification.md](deployment-verification.md) owns exact evidence/limits.

This session owns held machine claim `51ed48c0-8052-4e9b-ad36-399562a20020`,
owner `b6290bcd-8006-434c-a1c8-8c3140699c31`, canonical target
`machine:github.com/vpsfreecz/vpsfree-cz-configuration:cz.vpsfree/machines/aitherdev`
(legacy alias `machine:vpsfree:aitherdev`). Binding source is configfdcb0a2c;
physical resource cb771535... held since15:37:51Z. Effects are verified, but complete
final lineage is not integrated. Keep held until approved remote-default integration
is proven, then explicitly release this exact claim promptly and verify released
state. No extra UI acceptance/release direction is required. Do not archive/delete/
stop this session or invoke lifecycle helpers as release/cleanup substitutes.

## Ownership and next action

| Package | Owner | Status |
| --- | --- | --- |
| A design/diagnosis | architect0 | Accepted; design reconciled |
| B/D/F/G/H preflight, pins, live proof, refresh, targets | implementer1 | Accepted; current heads/evidence frozen |
| C/E core and required verification | implementer0 | Accepted; no gaps, all owned effects complete |
| I deployment verification | implementer1 | Accepted; passive reads only, no uncertainty |
| Final review | reviewer0 | Accepted, retained settings unchanged |
| Authority/claims/integration/activation/tracking | lead | Waiting for user's named master-merge approval |

Next: obtain the pending explicit three-repository/master approval, record its
wording/source, perform only fresh prepared fast-forward integrations with ordinary
hooks/SSH/remote verification under separate short claims, then prove complete
lineage and release machine20. Preserve prior review/rebase receipts if freshness
changes; a substantive change needs affected review/checks and renewed direction
as applicable. No additional source fix, test, live archive retry or cleanup is
currently needed. Initial tracking checkpoint172c14576; later records intentionally
updated locally under tracking cadence. See [progress-history.md](progress-history.md)
for superseded checkpoints.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-archive-failure-investigation/

## Current integration approval

Source: current user message, exact wording "ok, merge and release aitherdev", in response to the three named master merge request. Scope: dev-workspace/master, workspace/master, vpsfree-cz-configuration/master, and own aitherdev release after existing prerequisites. Selected apja coordination/operations guides are byte-identical to the fully read predecessor guides; selected guide rechecked. No archive/delete/stop/cleanup requested.

Final pre-merge freshness checked after user approval: remote master91/e7/9bdb and exact featuref6/30b74/fdcb unchanged; prepared targets at those bases, no staged changes or dirty flake paths. Complete current series is one final commit per repository, exact reviewed/certified final diff, no obsolete updates or migrations. Original independent report and mechanical reconstruction remain applicable. No new tests or source changes needed.

## Current integration progress

User-approved runtimef6 merged/pushed to master, remote exact equality verified; repo claim30 released16:12:10Z. Configuration target fast-forwarded tofdcb while remote remained9bdb; declared shell unexpectedly hydrated tool dependencies, so root reconciled known local-only effect and released claim31 before further preparation. Owner1 prepared frozen final environment outsideownership. Fresh claim33 then admitted normal SSHpush of fdcb toconfiguration/master, exact remoteproof/clean target established, claim33 released16:18:47Z. No hook bypass or product test/build iteration.

Workspace claim32 preflight detected a concurrent tracking-only localmaster advance before any merge; root held trackinglock through reconciliation, then unlocked/closed driver78818 and released claim32 at16:16:17Z. No workspace feature mutation or remote publication by that attempt. Owner0 handles clean mechanical pin refresh outsideclaims, preserving old deployed30 and exact app/inputs; approval remains valid only for equivalent patch. Owner1 independently prepares bounded fresh release evidence. Machine20 remainsheld; no repository claim currently held.

Final workspace successor accepted via coordinator independent complete-tree/bytepatch/full-lock/actual-derivation proof: old deployed30 on e7 -> new f1741f4982a3bfef710fc3837f8929b3fa4d8f76 on tracking-only97bf. Original30 retained; do not call it literally merged. Stablepatch3a3e8dcf13db76da2ba49e602f41c2e616ba76b6 and unchanged appm9/apja/fullinputs support integrated-equivalent lineage after fresh remoteproof. User approval retained for clean equivalent patch; schema1 receipt workspace-final-refresh-review.md binds original reviewer and ranges/no migrations. No tests or redeployment repeated.
