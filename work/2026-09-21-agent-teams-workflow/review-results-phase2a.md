# Phase 2A mandatory change-review results

## Review identity and scope

- Reviewer: retained independent `/root/reviewer_xhigh`
- Model/effort: Sol/xhigh
- Packet: `review-packet-phase2a.md`
- `codex-web`: `0a75d720171c52719679c7dd2e356d50f4b81f16..52b8ca6e9ddf2175d1a9163996fa9073f9c1882d`
- Generic `dev-workspace`:
  `39bfa664298443334d12b08dd42a475eef1c38e4..19e56a6c107806c05ab5f7e6b686756edabc7ff0`

The reviewer inspected the exact commit series, final implementations, tests,
documentation, design/schema records and exact-head verification logs. It did
not edit files or rerun tests.

## Findings and disposition

### Blocking: generic commit split contains a superseded protocol

**Accepted.** `19e56a6c` rewrites the catalog/state/storage protocol introduced by
`b085d602`; reverting only the follow-up would expose a known-invalid dormant
schema rather than a usable independent increment. Because these feature commits
are unpushed and unmerged, remediation will fold the final generic tree and the
accepted fixes below into one coherent commit based directly on `39bfa664`.

### Important: history rejects equal values from distinct ID namespaces

**Accepted.** Pending transitions correctly permit `id == request_id`, but
`TransitionOutcome.Validate` still rejects it. Transition IDs and request IDs
are separate namespaces; conversion to applied or cancelled history must retain
the valid identity. Remediation removes the inequality and adds conversion
coverage while retaining uniqueness within each domain.

### Important: history revision ordering is underconstrained

**Accepted.** The current validator permits a non-advancing completion and a
later history record whose base revision predates an earlier completion. The
retained designer confirmed that completion must be greater than the original
caller CAS base, while gaps remain valid after pending publication or unrelated
state updates. Each later retained base must be at least the preceding
completion. The same audit also found that a published pending record must have
its original base below the current state revision. The retained implementer
will enforce these equations and add direct, pending, interleaved and malformed
history coverage.

### Advisory

No advisory findings.

## Clean lanes

- Architecture/repetition: clean. Protocol/ledger identity stays in
  `codex-web`; workspace catalog/state policy stays in generic `dev-workspace`.
- Scope/proportionality: clean. The range contains no manager, live state
  emission, UI/route, agent creation, retention action, publication,
  integration or deployment.
- Risk/security/compatibility outside the accepted history findings: clean for
  this slice. The reviewer accepted strict bounded JSON, package pins,
  filesystem and lock handling, atomic replacement, crash-temp handling,
  zero-option schema compatibility, nonzero option identity, unknown-outcome
  handling and the documented rollback-preflight obligation.

## Gate status

The mandatory review gate is **closed**. The generic range is now exactly one
coherent commit,
`39bfa664298443334d12b08dd42a475eef1c38e4..729e5e08a9d57e537250da157d74720af50003eb`.
A fresh Luna/low watcher passed the focused exact-head test in 33 seconds with a
clean worktree (`logs/phase2a-review-fix-tests-final-exact.log`).

The same retained Sol/xhigh reviewer reran all affected lanes and confirmed:

- the Blocking commit-series finding is resolved;
- completed history accepts equal-byte transition/request IDs while retaining
  per-domain uniqueness;
- pending and completed revision ordering implements the clarified CAS
  equations with valid interleaving gaps; and
- no new Blocking or Important finding was introduced.

General correctness/maintainability, architecture/repetition,
scope/proportionality and risk/security/compatibility are all clean for Phase
2A. Long package/integration verification may proceed under fresh Luna/low
operation watchers.
