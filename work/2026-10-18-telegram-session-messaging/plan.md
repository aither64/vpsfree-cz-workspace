# 2026-10-18-telegram-session-messaging

## Goal

I'd like to investigate the idea of telegram integration in dev-workspace. I imagine it so that the bot would send me notifications to telegram, like we have browser notifications now. This way, I could be in touch even when afk.

I have several requirements:

- Notifications would always specify what session they're about and link the portal
- I must be able to respond to the messages and have a conversation with the lead in individual sessions
- I must be able to send voice messages
- I must be able to turn the telegram notifications on/off globally and per session

This will allow me to easily schedule work even while having only my phone, for example.

Suggest how this could be implemented.

## Affected repositories

- `dev-workspace`: likely owner of Telegram transport, settings and session routing.
- `codex-web`: inspect reusable conversation/notification interfaces; changes only
  if an actual shared capability gap requires them.
- Site configuration is a future deployment concern, not part of this investigation.

## Approach

Investigate existing code and current official Telegram interfaces, then propose
an incremental design. No application implementation, bot provisioning, external
messaging or deployment is requested. The architect owns `design.md`; the lead
owns scope, acceptance and session tracking.

| Owner | Expected result | Acceptance | Dependencies/checks |
| --- | --- | --- | --- |
| architect0 | Proposed design and package boundaries | All four requirements, routing, reliability, security, compatibility and verification covered | Canonical-source inspection; integrate supporting research |
| implementer0 | Existing notification/conversation findings | Concrete revision/path evidence and reusable interfaces | Read-only canonical repositories |
| implementer1 | Telegram platform findings | Official sources for replies, voice, pairing and transport | Current official API documentation |
| lead | Reconciled recommendation and tracking | Clear user flow, choices and limits; stable portal link | Assess architect and research reports |

## Decisions

- Investigation and proposal only; all implementation choices remain proposed.
- Preserve the existing session lead conversation rather than create a second
  independent assistant conversation in Telegram.
- Do not change retained team settings or invoke session lifecycle actions.

## Compatibility and deployment

The proposal must consider old/new portal and transport behavior, durable message
state, queue replay and deduplication, schema rollback, optional configuration,
credential storage and deployment ordering. No live state formats or packages
change during this investigation.

## Documentation

Readers: the user deciding scope, and implementers of a future integration.
Keep proposed behavior, evidence and open choices in this session's design and
research artifacts. Accepted feature/operator documentation belongs in the
owning repositories when implementation is authorized.

## Testing plan

Validate the proposal against canonical source paths and current official API
documentation. Record future quick checks and integration acceptance scenarios;
do not run builds or tests for a read-only investigation. Routine investigation
and planning do not trigger mandatory final change review.
