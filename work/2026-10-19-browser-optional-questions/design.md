# Optional questions: design and verification brief

The lead owns this design and application edits. Scope and accepted interaction
are in plan.md. Substantive design uses xhigh effort.

## Interfaces and invariants

codex-web owns additive transcript fields for agent questions/delivery and parsed
native user replies. A question identity is JSON.stringify of
[request_user_input_async, native item ID, original question index]. Preserve
raw wire text and its digest; display answers as quoted question plus answer.
Encode replies in the pinned CLI's send_user_message_question_reply JSON array
envelope. Use normal authorized durable sends, never fake pending RPC requests.

Shared browser controller owns ordered transcript reconciliation, pin eligibility,
drafts, dismissal, in-flight identity and answer state. Separate controls render
inline and in a bounded pinned region outside transcript scroll. Every question
supports suggestions and free text. A submission disables both views until
accepted/reconciled. Do not remove uncertain attempts or regenerate their IDs.
Maintain composer and attachments independently. Arrival never steals focus.

Pin questions only from an active live turn, stop pinning after accepted normal
follow-up or turn finalization. Preserve drafts on unpinning. Inline unanswered
questions remain answerable after unpinning; answered questions show the answer.
Answering one question does not clear peers. Dismiss sends no model message.
No countdown/autosend. Replay and paged refresh cannot repin handled questions.
Canonical user reply envelopes resolve browser and terminal answers; matching
the old whole-item identity resolves all that item's questions.

Remote clients remain untrusted; all sends retain existing origin, authorization,
payload, retry and trusted-target checks. No browser-provided sockets/cwd/thread
authority. Local operator trust is unchanged.

## Compatibility, deployment and recovery

No native upgrade or state migration. Additive JSON, optional types and separate
browser keys preserve old readers. Maintain existing send digests and ledgers.
No database/API client/CLI/Terraform/Nix module/protocol format changes beyond
exposing already-supported native question metadata. Mixed browser/server
versions degrade to text; version assets together. Runtime composes published
codex-web; workspace/configuration select identical reviewed runtime revisions.
Use coordinated system then user-profile activation with aitherdev reservation;
forward-only application recovery. Feature deployment is not merge permission.

## Acceptance and checks

Go normalization and reply-envelope tests, shared browser state tests, rendered
controls and durable-send tests, portal Playwright flow with real templates,
mobile/keyboard/focus checks, legacy mandatory request regressions. Test live
turn completion, follow-ups, dismiss, replay, pagination, reload, thread/member
switching, identical titles, cross-client answers, late inline reply, read-only
capabilities and transport uncertainty. Quick checks precede final committed
independent review; longer native/browser/package checks follow it. Record
commands and evidence in state, use fresh utility watcher for long operations.

## Authorized stale deployment refresh

The first system attempt ended before mutation because its prepared source would
drop already-integrated machine coverage. Keep the original jobs, reservation,
approval scope and review/check receipts. Refresh the same four registered
feature branches over their current remote defaults, preserving the optional
question patch and the selected Codex0.163.0. No default-branch integration,
reboot, runtime-contract expansion or lifecycle action is authorized.

Inspect complete baseline deltas before rebasing. Regenerate runtime and composed
workspace/configuration pins in dependency order with their existing tools;
consolidate each pin stream. Prove patch equivalence for unchanged feature code,
check matching final inputs, capture complete final history/migration inventory,
and obtain only the applicable review for conflicts or substantive interaction.
No new migrations are intended. Preserve original inventory and rollout SHAs.
Run changed-baseline checks and rebuild exact prepared system/profile artifacts
outside claims with a fresh utility watcher for long verification. The installed coordinator cannot refresh terminal jobs: retain the failed
original system job, cancel only its superseded unclaimed profile dependency,
and submit approved successor jobs under the same reservation with an explicit
system-to-profile dependency.


## Archive recovery repair (2026-10-20)

User explicitly directed fixing the erroneous Git administration-name collision
without touching live sessions. Lead owns design and code (no retained roster).
Fix ArchiveCleanup absence proof to distinguish the sealed removed admin identity
from a positively registered replacement at another checkout path. Require old
checkout and its registration absent; reject dangling/malformed/same-identity
admin entries. Read-only proof of replacement, never edit/move/prune live data.
Add real-Git regression with natural admin-name reuse and unchanged live files.

Extend existing candidate recover-archive path narrowly for matching modern
sidecar journals already past tracking move and with all checkouts/containers
removed. Bind exact candidate source, selected predecessor/token/Codex, same
runtime contract, recorded operation/root, tracking digest and cleanup inventory.
Use capable candidate's ordinary archive executor under existing generation and
session/transition locks to finish retained proof/conversation/receipt retirement.
No profile selection, journal edits or new archive operation. Preserve legacy
no-sidecar recovery as-is. Explicit local recovery direction is this user's
request; no master integration is authorized. Recovery must not depend on
startup changes or select a candidate with incompatible persistent contracts.

Separate commit for archive repair from existing optional-question commit.
No format migration: current journals/sidecars unchanged; predecessor remains
readable but cannot recover name reuse. Candidate recovery operates only within
recorded removed-resource boundary. New candidate runtime/workspace/config pins
remain consolidated; exact reprepare after review.

Quick: Ruby syntax, focused real-Git cleanup and host recovery tests, matching
lock check. Independent final affected general/architecture/scope/risk review
before long packaged suites/native preparation. Fresh utility owns long checks.
Then candidate recovery of exact two old archive operations, verify live worktree
head/status/admin identities unchanged, normal profile preparation, approved
coordinated system then profile activation and browser acceptance.
