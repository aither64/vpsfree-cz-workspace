# 2026-11-11-session-archival-failures

## Goal

investigate the two failed session archivals. the process is not working correctly. session 2026-11-10-status-theme-responsive-preview started a service that is still available (http://aitherdev.int.vpsfree.cz:4567/?lang=cs). session 2026-11-02-haveapi-vpsadmin-release failed to archive and hasn't been retried for days. find root causes and suggest a solution. when I click on archive, I expect it to work, session services be shut down and removed.

## Affected repositories

- `dev-workspace`: archive workers, persistent lifecycle recovery, temporary-service cleanup and browser status. Investigation only; no feature worktree or code changes planned.
- Site workspace: this session's tracking and findings only.

## Approach

Compare authoritative runtime failures for the two named sessions with the installed source. Establish exact failure phases, service registration/ownership, cleanup ordering, and whether any worker retries accepted archival. Distinguish proven causes from hypotheses and recommend the smallest reliable behavior change.

The retained Full-team architect owns source investigation and solution design; implementer0 owns independent operational evidence. The lead accepts evidence and maintains tracking. Other implementers and reviewer remain unassigned because this request is investigation, not implementation.

## Decisions

- Investigate and suggest a solution; do not retry either archive, stop services, alter lifecycle metadata, implement, deploy or integrate changes.
- Inspect only relevant runtime metadata for the user-named failures, not their worktrees, teams or transcripts.
- Bound reads to relevant archive/service/retry paths and exact failure logs. Stop investigation when both causes and the proposed recovery/fix are supported.

## Compatibility and deployment

Any proposed fix must preserve existing journal policies, exact ownership checks, idempotent recovery, retained Git heads, shutdown-before-supporting-file-removal, and rollback/package-generation rules. Distinguish cleanup failure from asynchronous tracking-Git failure. No deployment is authorized or needed for this investigation.

## Documentation

Readers: user and future implementer. Keep root causes/evidence in `findings-runtime.md` and `design.md`, linked from state. No product documentation changes during investigation.

## Testing plan

Read-only runtime/source correlation and bounded status/log inspection. No long test suites or live mutation. Proposed regression acceptance belongs in the design brief. Findings/tracking alone do not trigger automatic final change review.
