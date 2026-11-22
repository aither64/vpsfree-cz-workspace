# Selecting a team after committing initial tracking

Committing substantive plan/state before creating a conversation makes its slug
a retained-tracking destination. `dev-session start <slug> --as-is --team
delegated ...` then refuses with "agent team selection is only valid for a fresh
session destination". Do not remove tracking to make it appear fresh.

For an initiative just created by the same lead, start the retained tracking
without `--team`, then explicitly apply the installed preset to its empty roster
with `dev-session team preset <slug> delegated --as-is`. Verify exact session
identity and saved role settings before assigning work. This succeeded in
`work/2026-10-04-session-modes-review-timing/` and preserves initial tracking.

`team list` returns `{roster, presets}`; the preset command returns the roster
directly. Select `.roster.members` when inspecting list output.
