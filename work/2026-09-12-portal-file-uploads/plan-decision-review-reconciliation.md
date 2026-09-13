# Plan decision review reconciliation

Risk: high for provider API, recovery of durable requests, and package deployment.
All lanes use fresh gpt-5.6-sol reviewers with xhigh effort. General/architecture
used collaboration agents; risk/scope used ephemeral read-only Codex CLI processes
after the collaboration tool reached its lifetime thread quota. Reruns followed
only new request/recovery design. Reports preserve the reviewed commit references;
final corrected heads are in plan-decision-revisions.json.

- Initial general and scope: no findings.
- Initial architecture Important: pending implementation was classified by text
  alone. Fixed by exact message and plan-context matching in the shared helper.
- Initial risk Blocking: identical later plan text could reuse an accepted earlier
  request. Fixed with version 2 turn-and-digest identities; focused tests cover a
  held receipt and later identical plan.
- V2 general: no findings.
- V2 architecture Blocking and risk Important (duplicate): rejecting an old
  prepared attempt left a lifecycle blocker. Provider now owns exact, atomic
  retirement of prepared attempts; the portal recovers without submitting.
- V2 risk Blocking: an already open old page could confuse an old receipt with
  approval of a later identical plan. Unversioned implementation requires reload
  before any receipt lookup. Fresh pages use a separate recovery-only action.
- V3 architecture: no findings. Accepted bounded gaps are recorded in its report:
  recovery needs retained browser retry identity, and existing ledger primitives
  own write-failure/concurrency handling; no new migration framework is justified.
- V3 general Important: padded source IDs or missing same-turn plan entries could
  bypass retention. Narrowed retirement to a known latest turn different from the
  trimmed source ID. Whitespace/current/unproven/missing/newer regressions pass.
  This direct narrowing does not require a confirmatory review rerun.
- V3 risk: the same retention gap (Blocking) was already fixed above. Important:
  recovery could finish after transcript observation skipped acknowledgement of
  the in-flight request, leaving an accepted receipt until another event. Added
  the existing acknowledgement operation after recovery clears in-flight state;
  only digest-proven observed receipts are eligible. Browser acceptance will hold
  recovery until after observation and verify acknowledgement without a new event.
- V3 scope: no findings; inspected the final narrowed predicate and acknowledgement
  follow-up at 8a43d3b and the current mechanical pins.

Provider full Go suite, runtime full Go suite, focused final recovery tests,
JavaScript syntax and browser contract checks passed. The final workspace and
configuration deployment contract selects the same runtime revision. All findings are resolved. All 10 real-browser checks, packaged checks, final-head
CI and aitherdev deployment/health checks passed after review.
