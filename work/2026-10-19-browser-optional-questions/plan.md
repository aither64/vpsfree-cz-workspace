# 2026-10-19-browser-optional-questions

## Goal

Make native optional Codex questions answerable in codex-web and the workspace
portal, both inline and in a panel pinned below output. Keep ordinary input
available. Clicking an option sends immediately; free text uses Send answer.
Show answered state and the actual answer. Dismiss only unpins. Clear pins on
live turn end or accepted ordinary follow-up, while retaining inline replies.

## Affected repositories

- codex-web: transcript metadata, shared question controller and browser UI.
- dev-workspace: consume shared UI/controller, dependency selection and portal.
- workspace: matching nested runtime pin.
- vpsfree-cz-configuration: matching dev-workspace channel for aitherdev.

## Approach

Preserve agentMessage questions/delivery and recognize native question-reply
envelopes in user messages. Use the existing durable message endpoint with
native stable question identifiers; active sends steer, idle sends start turns.
Share the state and controls across the two renderers. Preserve raw text/digests
while displaying human-readable replies. Reconcile canonical transcript replies,
including other clients; scope local drafts/dismissals to conversation/thread.

## Decisions

User selected normal composer plus pinned questions, CLI turn/follow-up lifetime,
manual dismissal, immediate option sends, late inline replies, and visible answers.
No automatic timed dismissal or answer. No Codex version upgrade or new RPC.
No default-branch integration authorized. External conversation created a new
threadless initiative rather than adopting another session. Lead owns design
and implementation; mandatory standalone review uses installed catalog policy.

## Compatibility and deployment

Additive transcript JSON/types and browser storage only. Preserve submission
ledger, session formats, native protocol, schema and old-client text fallback.
No DB migrations, node updates, or coordinated infrastructure upgrades. Publish
codex-web, select it in runtime, compose exact runtime in workspace/configuration,
then verify matching locks. Use aitherdev coordination reservation for system
and user-profile activation. App remains in user profile. Recovery follows
forward-only switch policy. Deployment does not authorize master merges.

## Documentation

Readers: browser users and embedding developers. Owning references are
codex-web/docs/reference.md and dev-workspace/docs/workspace-portal.md. Keep
release-specific deployment evidence in initiative records.

## Testing plan

Normalize structured metadata and replies; malformed/ordinary message fallback;
stable indices with duplicate titles; option and text sends; both view sync;
failure/unknown outcome and retry; composer preservation; turn/follow-up/dismiss
lifetime; reload/pagination/member scoping and cross-client answers; keyboard,
mobile and read-only behavior. Quick checks before committed final independent
review, longer browser/native/package checks afterwards with utility watchers.
