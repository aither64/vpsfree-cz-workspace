# 2026-10-26-document-title-notifications

## Goal

seems to me that document title icons in the dev-workspace portal aren't working as they should. I have a session that is waiting for my input (asking if it should implement the plan) and yet it's document title has no marker. the codex tab has a badge as it should, but document title doesn't signal anything. please investigate.

## Affected repositories

- `dev-workspace`: portal document title and session notification aggregation.
- `codex-web`: Codex tab badge and conversation attention semantics (reference
  investigation until evidence establishes a change is needed).

## Approach

Investigate only. Compare the two notification paths, their attention and focus
rules, and the installed runtime with current source. Architect `architect0`
owns source investigation and a concise evidence-backed design/findings brief.
The lead owns acceptance inspection, tracking and the user report. No application
changes, integration, deployment or other-session access are part of this request.

## Decisions

- Keep investigation bounded to the missing browser title marker.
- Do not infer a need for protocol changes or new notification infrastructure.

## Compatibility and deployment

Investigation changes no persisted state, schema, API, protocol, configuration or
runtime. Any proposed fix must identify mixed-version behavior and rollback
implications before implementation; deployment would be a separate milestone.

## Documentation

Readers: the user and a future implementer. Preserve findings and a minimal fix
brief in `design.md`, with current phase and conclusions in `state.md`. Product
documentation is unnecessary for an investigation without behavior changes.

## Testing plan

Use source tracing and existing targeted tests first. A bounded disposable
reproduction may establish the exact title/badge divergence. Avoid broad builds
or integration suites; long or uncertain checks require the monitor skill.
