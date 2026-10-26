# Design and verification brief

The lead owns this bounded implementation (no managed roster). Reuse the portal's
verified repository reader, activity snapshots and Codex thread metadata. At a due
check, provide committed and current diffstats with category/path hints, previous
totals, per-member recorded working minutes and coverage, current user excerpts,
and exact same-session conversation/source paths for read-only inspection. Do
not sum overlapping member clocks or infer work from session age. Existing
working counters exclude waits; show this limitation instead of inventing a
new timer. Observer judges elapsed work and milestones before inspecting code.

Keep snapshots small and optional. Preserve pending request identity and idle,
pause, interval, lifecycle and three-minute cancellation behavior. First concern
is visible immediately; unresolved concern re-challenges only during active work.
On-track needs independent evidence; clearing an open concern additionally
requires its exact key and concrete resolution evidence. Missing evidence keeps
the concern and marks observation unavailable.

Recognize only the exact released stock observer instruction text when applying
the updated scheduled-check instructions; custom instructions and stored roster
settings remain untouched. Scheduled checks retain model, effort and access.
All observers receive the new evidence packet, but no general roster migration
or policy refresh mechanism is introduced.

Workspace guidance makes scope/diffstat/time the first review question and calls
for automatic simplification and a 30-working-minute small-task reassessment.
Complete execution packages, one implementer for narrow work, existing checks,
and user-added milestones limit orchestration overhead.

Additive optional fields in private schema-1 progress records; no migrations.
Old packages may discard new fields or use old concern semantics; forward
deployment uses runtime plus workspace catalog. No lifecycle behavior changes.

Acceptance: focused Go tests for Git stats/untracked files, timing exclusions,
missing evidence, stock/custom instructions, concern persistence/rechallenge and
existing idle/manual scheduling. Quick Nix syntax/catalog checks. Final committed
review then one composed package build with existing checks, no new inspectors.
