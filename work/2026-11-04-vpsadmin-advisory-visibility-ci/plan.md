# Advisory visibility CI investigation

Investigate the anonymous CVE visibility failure in public vpsfreecz/vpsadmin run
41822368583 at source 4ac49f49e63545200df8afa920c6eafda8722523. Deliver an
evidence-backed diagnosis and smallest proposed solution, or exact remaining
uncertainty with a bounded next experiment. This is a new, separately bound
Full-team session; no access to originating-session records or communication.

## Scope and ownership

Primary project: vpsadmin, public Git and CI. Read public HaveAPI only to trace
actual resource validation. Architect0 owns substantive investigation/design and
work package boundaries. Implementer0 and implementer1 execute independent
packages after scoping. Lead coordinates, accepts evidence and maintains records.
Saved delegated roster: Astra/xhigh architect; Sol/xhigh implementers and reviewer;
Sol/xhigh observer; lead settings retained. All editing members have workspace_write.

## Approach and acceptance

1. Independently retrieve failed and passing public native results, environment,
   logs and effective locks; record exact source/input graphs and hashes.
2. Trace intended visibility through fixture state, validation, authorization,
   query filtering and included parents. Preserve the exact validation rejection.
3. Reproduce the existing example/topic using fixed source, seed and dependency
   graph. Vary dependencies and order independently only as warranted. Preserve
   counterexamples; a green rerun alone proves no causal conclusion.
4. Explain a demonstrated mechanism or precisely bounded uncertainty. Recommend
   the smallest owning-component solution and focused security/regression checks.

## Constraints and compatibility

Diagnosis and proposal only. Disposable reproduction and isolated diagnostic
instrumentation/prototypes are allowed. No merge, publication, production access,
deployment, changes to the originating session, or session lifecycle actions.
Do not weaken authorization, assertions or visibility; no retries/skips/freezes as
fixes. HaveAPI remains generic. Preserve current public defaults and supported
source/migration lineage; record historical source separately from current default.
No schema/protocol/deployment changes are planned. Any proposed change must assess
old/new consumers, persistence, authorization, mixed-version behavior and rollback.

## Verification

Architect writes design.md before substantive implementation. Prefer narrow exact
reproductions over full matrices. Fresh pinned Luna/low utilities launch/watch long
or uncertain checks using dev-session-monitor; stop unexpected kernel builds.
Findings/evidence alone need no mandatory change review. Completed substantive
patches require commits, quick checks, independent final review before long checks.
All proposed patches remain explicitly unmerged and undeployed.
