# osctld-oomd exceptions on node23.prg

Investigate exceptions reported on the central log server
`log.int.prg.vpsfree.cz`, including svlogd messages filed under `localhost`.
Deliver an evidence-backed root cause, affected behavior, confidence limits and
the smallest recommended remedy. Investigation completed; user then requested
"ok, implement the fix". Implement and publish the focused vpsAdminOS correction
with regression coverage and independent review. Production remains unchanged.

Implementation scope is vpsAdminOS `osctl-oomd` event processing and focused
tests. The architect design prescribes creating records only for hits and
ignoring absent-record misses within the existing mutex. Do not change action
thresholds, supervisor behavior or event queue architecture. Deployment and
integration are not requested. There are no schema, protocol or persisted-state
changes. Nodes can update independently; rollback reintroduces the bug but has
no state-format incompatibility.

## Owners and acceptance

- architect0: locate exceptions, establish node attribution and causal chain;
  maintain `design.md` with findings and a verification brief.
- implementer0: own fix, regression tests, relevant technical documentation,
  quick checks, commit/publication and follow-up review fixes in a session-owned
  vpsadminos worktree. Source tracing and stale-miss reproduction are complete.
- reviewer0: independently review final committed changes after quick checks,
  including whole-branch history/migration conclusion.
- Lead: coordinate, assess evidence, keep plan/state and deliver the explanation.

Accept when the exception has exact evidence, the suspected operation is traced
to deployed behavior, competing causes are assessed and uncertainty is explicit.
For implementation accept when the exact stale-miss failure is prevented,
unknown misses create no record, and normal hit/miss decay and pruning remain
correct. Run focused unit checks and declared hooks first; final independent
review precedes any justified longer integration tests. Avoid unrelated builds.

Readers are the requesting operator and future maintainers diagnosing the same
failure. Keep incident evidence here; explain the non-obvious invariant near
the implementation/tests where useful rather than creating a new manual.
