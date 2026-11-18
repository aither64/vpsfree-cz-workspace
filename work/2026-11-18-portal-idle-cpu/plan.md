# Portal idle CPU: design and handoff

Goal: hand the measured portal CPU issue and a bounded fix/test proposal to
`2026-11-11-pi-codex-migration`, which owns portal implementation. This session
owns tracking, design and one deliberate lead-to-lead send. No implementation,
source branch, deployment or renewed profiling here; do not await implementation.

## Authority and ownership

Verified identity: `2026-11-18-portal-idle-cpu`, workspace
`/home/aither/workspace/ai/vpsfree.cz`; `dev-session current` and both environment
markers agree. Live `team list --as-is` returned `roster: null`; lead owns design.

Communication approval, quoted from the current user's task:
“The operator explicitly requests communication from this new tracking initiative
to precisely that existing migration session.” The same request says to “send the
design path, actionable summary and bounded performance test to the other lead
via session communication.” Exact pair: this session and
`2026-11-11-pi-codex-migration`.

Reference: this thread `01a1ef33-28a4-7ea2-a063-28e8ce0ea786`, 2026-11-18 user
message beginning “Track the portal CPU investigation as a design and handoff
only.” It identifies the external 2026-11-18 aitherdev workspace-portal CPU
conversation, user follow-up immediately after the CPU profile report:
“okay, you can start tracking. design a fix and send it to session
2026-11-11-pi-codex-migration, which currently works on the portal, so it will
include the fix.. I'd like some performance testing so that this sort of waste
doesn't reoccur. don't let it waste too much time however.”
Approval covers communication, not merge, deployment or lifecycle actions.

## Scope and approach

Affected project: `dev-workspace` portal workers and their monitor/communication
stores. Only coordination records change here on shared workspace `master`.
[Design](design.md) carries supplied measurements, exact inspected source,
actionable changes, invariants and acceptance checks. A disposable compact work
view removes repeated settled-history decoding; fresh locked authority checks
remain at action boundaries. Maintenance optimization is deferred until a later
post-fix profile justifies it. No migrations, persistent queue or new CI system.

Persisted formats, APIs, CLI/client contracts, configuration and protocols remain
unchanged. Existing legacy/Pi records and out-of-process writers remain supported.
Cold/restart discovery rebuilds the view; recovery uses the migration session's
normal authorized forward package workflow. No coordinated node update is needed.

## Delivery and verification

| Package | Owner | Acceptance / dependencies | Status |
| --- | --- | --- | --- |
| Plan, state, design and single handoff | This lead | Commit initial records before allow/send; check paths and invariants; record actual delivery ID/status | In progress |
| Implementation and bounded tests | Migration lead, through its own roster | Design proposal; deterministic real-pass counters plus one short before/after benchmem comparison | Handoff only |

Use local synthetic settled history and fake time through the real worker pass.
Require zero repeated history body reads/decodes or terminal-only action calls
on warm idle passes, next-tick external-change discovery, and preserved delivery,
revalidation and receipt handling. Keep tests in the existing Go lane. Details
and a small/larger benchmark budget are in the design. No tests run here.

Readers: migration lead/implementers and the external investigating lead, who
will verify this handoff. Keep the proposal in this tracking directory; the
implementation owner maintains lasting project comments/docs with its eventual
change. Routine design/planning/evidence does not trigger automatic final review.
Leave this session open for verification and follow-up.
