---
lifecycle: active
---

# 2026-09-10-netcraft-abuse-reports

## Repositories

- `vpsfree-cz-configuration`
  - branch: `2026-09-10-netcraft-abuse-reports` (pending creation)
  - worktree:
    `worktrees/2026-09-10-netcraft-abuse-reports/vpsfree-cz-configuration`
    (pending creation)
  - inspected base: `origin/master` at
    `7481618dacab04bfd5b09bc730c373c2d2bf14d7`

## Status

Planning and source-message inspection are complete. Initial workspace tracking
is being prepared before the project branch and worktree are created.

## Commands run

- `dev-session current` from the workspace root (no pre-existing session)
- Read-only inspection of the current parser, decoder, specifications, and
  repository-local `AGENTS.md` from the canonical bare repository
- MIME and JSON inspection of both supplied Netcraft messages
- Semantic comparison of both JSON attachments
- Read-only inspection of the official legacy XARF version 1 schema
- `git ls-remote` verification that upstream `master` remains at
  `7481618dacab04bfd5b09bc730c373c2d2bf14d7`
- `dev-session start netcraft-abuse-reports --no-attach --no-codex --json`

## Results

- Both messages contain one XARF feedback part and one `xarf.json` attachment.
- Netcraft emits legacy XARF version 1 with `Activity` / `Spam` /
  `Extortion Mail Server`, a source IP, UTC event time, reporter case ID,
  reporter notes, disclosure enabled, and one Base64-encoded
  `message/rfc822` sample.
- The RT originator is dynamic and contains the same case ID as the JSON.
- The second message is a reminder: its decoded JSON object and evidence are
  identical to the initial report despite JSON key reordering and a `Re:`
  subject prefix.
- The existing parser rejects the messages because only the exact Abusix
  originator is trusted and the decoder accepts only XARF versions 3 and 4.
- The affected repository's upstream and local `origin/master` agree at the
  inspected base. Its canonical SSH origin is configured correctly.

## Open questions

- None. The user accepted the strict provider policy and duplicate-suppression
  design in the implementation plan.

## Cleanup

- Keep the supplied messages only under ignored `tmp/netcraft-emails/`; never
  add them to a commit or portal artifact.
- The initiative remains active. Do not archive or delete it without an
  explicit user request.
