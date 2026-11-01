---
lifecycle: complete
---

# 2026-10-15-portal-cpu-investigation

## Status

Investigation complete; see [findings and recommendation](findings.md). Portal
PID 2704317 measured 363.5% CPU over ten seconds. Two independent sampling
windows attribute 58–61% of portal CPU samples to session loading and another
20–22% to background garbage collection. Per-thread reconnect admission scans
the full active/archive catalog and accounts for 34–38% of portal CPU samples.
Oversized activity responses repeatedly disconnect the shared App Server client;
one direct activity HTTP read also returned 503. The exact offending RPC page
was not captured, so that part of the causal chain remains an explicit inference.

Recommended follow-up: shared validated session/thread ownership indexing and
incremental parsed-summary caching in dev-workspace; bounded incremental activity
history reads plus per-thread error containment/backoff in codex-web. Preserve
fresh runtime/recovery/lifecycle admission checks and accurate activity counters.
No implementation, service restart, deployment or package mutation performed.

- [x] Establish a separate initiative and read workspace procedures.
- [x] Identify portal service and initial CPU/HTTP symptoms.
- [x] Trace expensive work against the deployed source.
- [x] Record cause, limitations, proposed fix and acceptance checks.

Coordination-only initiative with no registered feature branches or remaining
investigation work. Completion does not archive or stop the session.

## Next actions

The requested diagnosis and solution proposal are delivered. Implementation is
a separate follow-up, with the scope and acceptance checks in findings.md.

## Documentation

Registered findings.md as the portal artifact. CPU/HTTP samples and two filtered
profile summaries are linked there. No project documentation update was useful:
the deliverable describes an observed incident and a proposed fix, not changed
supported behavior. Stable portal URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-15-portal-cpu-investigation/

## Repositories

No registered feature branches or worktrees; investigation only.

## Commands run

`dev-session current` returned no current session. Created this initiative with
`dev-session start portal-cpu-investigation --no-attach --no-codex --json`.
Read service metadata, process counters, portal logs and local HTTP responses.
Recorded two ten-second 49 Hz user-space perf samples and normalized their
reports to `workspace-porta`; helper processes were excluded from the reported
CPU percentages. Recorded an independent ten-second `/proc` CPU delta. Derived
the installed source path from Nix derivation metadata and verified hot source
files match the canonical repository HEAD byte for byte. Read pinned codex-web
source at 5f15b9293f9b1eef7469a34d7b2044c743160283.

## Results

- Read-only diagnosis succeeded. No build or integration test was needed.
- Routine investigation/findings/evidence are exempt from automatic review.
- Initial tracking commit: 617d7659. Subsequent findings/state/manifest changes
  stay in the working tree under normal short-initiative tracking cadence.
- Inventory at sampling: 80 work and 194 archive manifests, approximately
  472 KB YAML and 8.21 MB state Markdown per full inventory read.
- Direct HTTP sampling: index 7 ms; root 29 ms; one activity read 244 ms;
  another activity read 503 after 2.443 seconds.
- Raw evidence is local to this initiative. No transcript text or traffic
  payloads were saved; profile stacks contain symbols and local file paths.

## Open questions

The exact oversized App Server reply was not captured. CPU attribution and
the expensive admission path are directly measured; projected gains need
before/after verification if the proposed fix is implemented.

## Cleanup

No service or runtime mutations. Non-root strace attach was refused by ptrace
policy and passwordless sudo was unavailable. Existing store-packaged perf worked
without privilege or policy changes. All sampling commands have exited. Raw
perf data and text reports are retained here; no cleanup of other sessions.
