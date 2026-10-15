---
lifecycle: active
---

# 2026-10-15-portal-cpu-investigation

## Status

Investigation in progress. Running portal PID 2704317 averaged approximately
3.8 CPU cores since start; root page itself responded in 29 ms through the Unix
socket. Recent logs repeatedly report oversized 64 MiB App Server messages for
the evaluate-confctl-rewrite-language activity endpoint.

- [x] Establish a separate initiative and read workspace procedures.
- [x] Identify portal service and initial CPU/HTTP symptoms.
- [ ] Trace expensive work against the deployed source.
- [ ] Record cause, limitations, proposed fix and acceptance checks.

## Next actions

Measure sustained CPU and request latency; inspect activity and observer paths.

## Documentation

## Repositories

No registered feature branches or worktrees; investigation only.

## Commands run

`dev-session current` returned no current session. Created this initiative with
`dev-session start portal-cpu-investigation --no-attach --no-codex --json`.
Read service metadata, process counters, portal logs and local HTTP responses.

## Results

## Open questions

Determine the primary CPU consumer and whether oversized activity messages
account for the persistent portal CPU usage or are a separate symptom.

## Cleanup

No service or runtime mutations. Non-root strace attach was refused by ptrace
policy; use a bounded privileged observation if available, without changing policy.
