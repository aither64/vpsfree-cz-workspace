# 2026-10-15-portal-cpu-investigation

## Goal

Diagnose excessive workspace-portal CPU use and slow responses, and recommend
an evidence-backed solution. The user requested investigation and a suggestion;
implementation and deployment are outside this task.

## Affected repositories

- dev-workspace: running Go portal, session indexing and background observation.
- codex-web: shared App Server client, activity reads and browser polling.
- Workspace: investigation records only; no feature branches or project edits.

## Approach

Identify the installed generation; measure CPU, endpoint latency and request
patterns; inspect the matching source; use short read-only process observations
to distinguish busy loops, repeated history processing and indexing overhead.
Separate measured causes from hypotheses and propose a bounded fix and validation.

## Decisions

Create a separate coordination-only initiative because `dev-session current`
found no session and this conversation has no environment or developer binding.
Start without another Codex process. Team listing consequently reports no valid
lead thread; there is no retained team to use or modify. Diagnosis stays here.

## Compatibility and deployment

No state, API, package or deployment changes are planned. Proposed fixes must
preserve runtime authority, exact-origin checks, bounded reads, conversation
history, request cancellation and old/new package state compatibility. Do not
recommend merely lifting message limits without addressing full-history reads.

## Documentation

Readers: workspace operator and a future implementer. Store findings and measured
evidence in this initiative and expose a concise findings artifact in the portal.
No project behavior documentation changes are needed for investigation alone.

## Testing plan

Use small local HTTP reads, process counters and bounded profiling/trace samples.
Do not launch builds or integration tests. Do not restart services, stop sessions,
or change browser/session state as part of diagnosis.
