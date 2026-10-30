# osctld-oomd exceptions on node23.prg

Investigate exceptions reported on the central log server
`log.int.prg.vpsfree.cz`, including svlogd messages filed under `localhost`.
Deliver an evidence-backed root cause, affected behavior, confidence limits and
the smallest recommended remedy. Production systems remain unchanged.

Scope is read-only logs, deployed source/version inspection and source tracing
in vpsAdminOS. Site configuration may be consulted to explain log routing.
No implementation, deployment or integration is requested. There are no schema,
protocol or persisted-state changes and no upgrade or rollback operation.

## Owners and acceptance

- architect0: locate exceptions, establish node attribution and causal chain;
  maintain `design.md` with findings and a verification brief.
- An implementer will trace the implicated source once the exception identifies
  a bounded independent package. No speculative application edits.
- Lead: coordinate, assess evidence, keep plan/state and deliver the explanation.

Accept when the exception has exact evidence, the suspected operation is traced
to deployed behavior, competing causes are assessed and uncertainty is explicit.
Use bounded log queries and small reproductions where useful; avoid builds and
long integration tests for a read-only diagnosis.

Readers are the requesting operator and future maintainers diagnosing the same
failure. Keep incident-specific evidence here; project documentation changes
are unnecessary unless a later implementation is requested.
