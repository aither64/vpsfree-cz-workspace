# UCEPROTECT implementation review

## Outcome and user decisions

Create separate incidents for every valid explicitly reported IP/event in MasterDC UCEPROTECT notices, resolving each owner at event time. The input email contains two IPs but the old prose matcher returns the first; CSV also uses find. The user explicitly selected processing valid entries and logging rejected ones for manual RT recovery. No mailbox retry, cross-message deduplication, database/API changes, production deployment or ticket replay. Preserve SPFBL/SBL and unambiguous single-entry output. Full accepted intent: plan.md plus the operational correction and partial-success decision below.

## Commits and ownership

- Initiative: 2026-09-15-abuse-uceprotect
- Tracking: /home/aither/workspace/ai/vpsfree.cz/work/2026-09-15-abuse-uceprotect
- Configuration worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-15-abuse-uceprotect/vpsfree-cz-configuration
- Base: 713fb3ba48ae31c87519e75892d1413a48a22fb0
- Review head: 81d827c269c09db55a7dc97783696ec803cfb37c
- One functional commit includes parser behavior, supporting specs/synthetic fixture and owning documentation because these describe and validate the same behavior. No independent refactor, dependency change or deployment bundled.
- Consumer: vpsAdmin API loads configs/vpsadmin/api/incident_reports.rb, routes to MasterDc, accepts IncidentReports::Result arrays, then sends each incident to its own user. The consumer is unchanged. Bare source is /home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin.git; pinned vpsadminServices revision is c38839d5be62e9d40d055b23a84844e2037ba4db.
- No project worktrees for vpsAdmin; read bare refs or pinned source as needed. Do not alter other initiatives.

## Implementation boundary

Explicit Czech/English source lists and recognized inline CSV tables, canonical IPv4/IPv6, row timestamps with date fallback only for empty values, CSV-over-prose precedence, per-message IP/time deduplication, separate assignments and isolated multi-entry text. Generated evidence projects only IP/timestamp fields; the original remains in RT. A malformed table excludes prose fallback in the same MIME section; independent sections and tables can succeed. A subject-only multi-IP list is explicitly rejected rather than silently selecting its first IP. Original single-entry subjects/bodies remain when unambiguous.

All matched MasterDC messages retain current handled semantics, including partial/all rejected input. Mail::Tasks already deletes fetched messages independently of handler return, so false processed? does not retain mail. Diagnostics and manual RT recovery are the chosen policy. Database exceptions propagate under existing persistence semantics; this is not an exactly-once delivery redesign.

## Verification and documentation

- Full config suite: nix develop -c bundle exec rake spec, 114 examples passed before final subject-only guard/shared persistence extraction.
- Final focused parser + handler suite: 48 examples passed at review head, including existing SPFBL/SBL and single UCEPROTECT fixtures.
- Full Ruby lint: 34 files, no offenses; final commit hooks Nixfmt/RuboCop/commit-msg passed.
- Original upload offline dry-run passed: two incidents with controlled distinct owner assignments, isolated evidence, expected mail timestamp, no writes. The upload remains outside git; do not copy it into fixtures or review artifacts.
- Project docs: README.md entry link, configs/vpsadmin/api/README.md covers parsing, evidence ownership, partial diagnostics, deletion/recovery and rollback. User-facing generated prose reviewed by main agent with vpsfree-user-facing-writing/humanizer-en.
- No long integration tests started. An offline test of the unchanged vpsAdmin routing boundary is being prepared separately.

## Risk and review instructions

High risk classification because incident ownership and member-visible report evidence cross tenant boundaries. All four lanes are required: general, architecture/repetition, scope/proportionality, risk/compatibility. Use gpt-6-astra / xhigh. This is configuration-only, backward/forward compatible with the existing incident-array interface; no migration or node coordination, rollback cannot retract notifications.

Read ~/.codex/skills/mandatory-change-review/SKILL.md and your lane reference. Review committed changes directly, independently, without nested reviewers. Do not edit code, tracking, or shared environment. Return findings with severity, file/line, evidence and suggested narrow remediation; say clearly if none. Generated .bin/.bundle/.rubocop_cache are local dev-shell artifacts and are not intended changes. Prefer inspection; if a reproduction needs Ruby, use nix develop and do not mutate tracked files.
