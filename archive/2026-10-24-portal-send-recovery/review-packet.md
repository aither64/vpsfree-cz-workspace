# Final source review: portal delivery recovery

Read `/home/aither/.codex/skills/mandatory-change-review/SKILL.md` and all four
lane references (general, architecture, scope, risk). Review directly without
subagents and remain read-only. This is a completed committed substantive source
deliverable; long integration checks and mechanical rollout pins follow review.

Workspace `/home/aither/workspace/ai/vpsfree.cz`; initiative
`2026-10-24-portal-send-recovery`, plan/design/state under `work/` there.
User explicitly selected portal recovery instead of native Codex deduplication,
then approved implementation and aitherdev deployment. No master integration.

## Exact series

- codex-web worktree `worktrees/2026-10-24-portal-send-recovery/codex-web`:
  base `11ec57d2203fc735696fe75a837d47da55a5c6af`, head
  `2c4c3460ac6d109699d05115b0ebb9e6eb3410df`. One commit:
  `codex: preserve retryable sends before write admission`.
- dev-workspace worktree `worktrees/2026-10-24-portal-send-recovery/dev-workspace`:
  base `b3a6eb2fc0b41cf0cb965bf4c39991815d9df734`, head `8ccdd2e4`.
  Complete series: `4d2c7069 portal: recover uncertain messages and clear stale
  feedback`; `8ccdd2e4 deps: select message delivery admission recovery`.
  Functional and dependency changes are separate. Tests/docs accompany their
  owning behavior. No obsolete designs, repeated pin streams or migrations.
  Neither source has been deployed by this initiative. codex-web feature is
  published because the companion dependency needs its exact source revision.

## Acceptance and boundaries

Cancellation before mutation Write must retain prepared retryable state.
Write/reply uncertainty must never authorize automatic duplicate delivery.
Existing uncertain records remain uncertain. Explicit protocol refusals may
restore prepared state. Immutable message/context/options bindings remain.
HTTP sends finish admitted work after browser cancellation within deadline and
server shutdown. No native protocol or schema-3 ledger change.

The portal preserves individual unknown receipts and offers confirmed duplicate-
aware replacement. It reconciles first, persists a stable replacement ID and
retains original records. Drafts/attachments and execution holds survive.
Successful newer sends/queues clear old composer errors; stale older failures
cannot restore them. Authorization, origin checks and private error details
must remain protected. Host operator trusted; remote clients untrusted.

Provider owner is codex-web, consumed by dev-workspace through its Go module and
Nix pin; inspect the companion wrapper/consumer as necessary. Public addition:
MessageNotSentError plus message_not_sent/message_delivery_unknown HTTP codes.
Browser replacement metadata is additive; older clients ignore it. Generic
Send uncertainty remains conservative. Native Codex stays 0.163.0.

Docs: codex-web docs/reference.md and dev-workspace docs/workspace-portal.md.
Deployment will select identical reviewed runtime in the workspace composition
and confctl dev-workspace/devWorkspace channel, build aitherdev, and activate
host then user application under ordinary machine ownership. Keep other
sessions' lineage and forward profile recovery. No original-message replay.

## Completed checks

Focused client Go selectors `(Send|CanceledWrite|AlreadyCanceledWrite|OperationTimeout)`
pass, as do 47 conversation/upload Node contracts and protocol corpus coverage.
Portal notice/composer Node regressions and focused portal Go selectors
`(SubmissionNotice|ComposerHandoffRetains|PortalSendResponseLoss)` pass. New real
Chromium/Firefox regression is committed but awaits post-review integration.
Full packaged/native checks await this gate. No declared hook framework.

Overall risk high: durable delivery semantics, HTTP lifetime and cross-project
deployment. Reviewer resolved from installed default development team policy:
gpt-6.1-sol/xhigh. No retained reviewer exists for threadless tracking.

Report findings with severity and file/line. Explicitly assess complete series,
pin consolidation, migration lineage (none) and residual verification gaps.
Write your report to this initiative's review-report.md and notify the parent.
