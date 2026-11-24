# Runtime monitor ownership and Pi coverage

## Goal

Investigate why an active Codex session lead can receive an ownership refusal
from the runtime monitor before launch. Separately check whether Pi sessions
expose an equivalent monitor and can resume their exact lead on a result.
The original incident details are retained in the conversation, not in Git.

## Affected repositories

Start with `dev-workspace` (monitor service, backend adapters and installed skill).
Inspect `codex-web` and Codex as dependency boundaries; no change there without
source evidence. No vpsAdminOS changes or repeat of the reported check.

## Approach

Trace the Codex and Pi cases separately. Establish the serving package and
authenticated caller where available, then compare with the exact roster.
Distinguish known defects from conditions that could not be reconstructed.

## Decisions

Do not infer authority from working directory, environment alone, arguments,
or a model prompt. Do not test with the reported command or operation ID.
Preserve the roster, idempotent launches and exact-lead delivery.

## Compatibility and deployment

Retain old bindings and stored operations only where they remain verifiable.
Assess subprocess and resumed-conversation behavior before choosing a fix.
No production package activation, session restart or integration is approved.

## Documentation

Record generalized evidence and limits in state/design. If a supported tool or
capability changes, update the runtime's owning docs and installed skill as needed.

## Testing plan

Use isolated adapter-to-monitor fixtures and disposable commands/state. Test
exact lead, retained member, foreign lead, stale caller and a valid thread binding
without shell variables. Separately test malformed inputs, unchanged ID retries,
exact-lead delivery, and Pi capability or fallback behavior supported by the
evidence. Review a committed candidate after quick checks and before longer checks.
