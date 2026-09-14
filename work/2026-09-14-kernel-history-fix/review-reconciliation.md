# Implementation review reconciliation

Reviewed vpsAdmin base `791ab3aa89e2f613979da6090b89785c78245db5` through
`6682da3bafc1212f30c395707319147a8c51fcc9`. Risk: high because of persisted
history/schema changes, historical writes, and a multi-writer rollout. All
reviewers used gpt-5.6-sol at xhigh, directly in their assigned lanes.

- General Blocking, repeated by scope: a comment inside a YAML literal pattern
  block became invalid RSpec path arguments. Removed it. Replayed the workflow's
  exact Bash expansion: all 404 tracked specs are covered once, with no
  nonexistent paths. The initial simplified checker incorrectly removed comment
  text and did not reproduce this failure; it was replaced by the exact check.
- Architecture Important: add provider-level tests for the shared StableState
  contract. Added 9 direct examples covering boot precedence/fallback/unknown
  identity, completeness, transitions, effective IDs, ignored metadata and
  mismatches. All pass. Existing database consumer tests remain.
- Architecture Advisory: centralize boot identity in a three-state relation.
  Retained the existing recorder bootstrap rule and stricter positive-evidence
  helper. Their handling of unknown identity intentionally differs; tests and
  the helper comment document it. Introducing a third-state interface would
  expand this timestamp fix without changing supported behavior.
- Scope: no proportionality findings beyond the duplicate CI defect.
- Compatibility Important: writable normalized child rows can drift before
  discovery despite the event snapshot parent's update guard. Repair now checks
  the reconstructed report digest against the stored snapshot_revision for the
  baseline, target, and supporting evidence. Any mismatch is skipped. This is
  local to repair; no broad persistence or protocol changes. Tests cover
  preexisting drift, absence of intact proof, and falling back to older intact
  evidence. Validation pending below.

Direct remediations add tests, remove rejected CI text, and apply the proposed
local integrity check. Recheck their focused behavior and commit them before
integration. Final heads and test results will be appended after consolidation.

Focused remediation validation: 34 repair/provider examples, 0 failures;
3-file Ruby lint clean. Previous recorder/supervisor suite: 92 examples,
0 failures; isolated migration: 1 example, 0 failures. General reviewer also
independently replayed the corrected engine shell expansion (237 valid files,
zero nonexistent entries). Scope completed without further findings. No reviewer
rerun is required for these direct fixes under skill steps 9-10; exact downstream
pins still receive their separate review checkpoint.

Consolidated vpsAdmin commits after direct fixes and final upstream rebase:
- Recorder + provider contract: `7b4aec6bb9b948ab3d1bdf90a886b99a4ebd4ff5`.
- Repair + integrity check/integration/operator docs: `2a312616b0bf10465c33bbca97c79b31b22e8ec8`.
No outstanding Blocking or Important implementation findings. Final combined
focused specs and push are running before integration and downstream pins.

## Final downstream checkpoint

General and compatibility reviewers (fresh gpt-5.6-sol xhigh) reviewed config
`4145e961...`, KB `0770dcfa...`, exact vpsAdmin pin `2a312616...`, and rollout.
No pin or KB-impact findings. Consumer builds subsequently passed all 11 hosts.

- Important, both lanes: prove supervisor runtime masks, not just inactivity.
  Prepared rollout now checks UnitFileState=masked-runtime and ActiveState=inactive
  for each labelled host before activation, after API1/before migration, and
  before/after API2. Any failure/missing output is a stop condition; confctl's
  overall status is not trusted for per-host SSH outcomes. Final unmask/restart
  and health results require per-host inspection as well.
- Important, compatibility: apply recomputes its candidate set rather than
  consuming an earlier preview. Retained the requested CLI and its per-invocation
  locking contract. The prepared exact-approval procedure now quiesces both
  supervisor writers and other history maintenance, captures an approved preview,
  repeats/cmp-checks exact output before immediate apply while still paused, and
  requires a fresh review if writers resume or output changes. A preliminary
  online dry-run is explicitly not an artifact consumed by apply. This follows
  the reviewer's bounded operational remedy; no new preview-manifest interface
  is introduced beyond the user's task scope.
- Advisory, compatibility: added exact configuration HEAD, tracked-tree/index
  cleanliness and vpsadminServices pin assertions before future deployment.
- Advisory, compatibility: confirmation verification now asks the operator to
  select a known complete stable node; node 400 remains the separate repair target.

Applied the user-facing writing skill directly to these prepared instructions.
These are direct documented safeguards requested by review, with no new code,
protocol, or design boundary; no reviewer rerun is required by skill steps 9-10.
No remaining Blocking/Important findings. Rollout and repair remain unexecuted.

## Integration wait correction

Local execution found that runit's default seven-second wait rejected both
status examples before report ingestion. The correction is consolidated at
`b851ea971ed1cdcec2548395ec1ea493e8344cb6`, changing only five lines of test
orchestration: explicit 90-second sv waits, 120-second runner bounds, and stops
inside existing ensure-protected blocks. Fresh general review at gpt-5.6-sol
xhigh found no findings. The wrapper's 60-second deadline fits within those
bounds; its existing ESRCH propagation should allow runit to observe it down.
All 11 examples are being rerun to verify that residual runtime assumption.

## Repair entrypoint and synthetic fixture correction

The corrected sv waits passed in both examples. The synthetic version string
then hit the schema's 25-character limit; a DB preflight reproduced the failure.
Shortened the fixture. Preflighting the public Rake task also found that the
shared dispatcher singularized Bounds and could not find the class. Renamed its
internal class/file/key to NodeKernelHistoryBoundsRepair, kept the public task
unchanged, added a public Rake preview/apply/idempotence spec, and used the
existing packaged bundle exec rake pattern in the VM scenario.

Consolidated head feaa152436cf66e980c4e53f86a541bb10daae16 passes106 combined
focused examples,26 repair examples, the exact-payload preflight, lint, selector
and commit hooks. Fresh general review by gpt-5.6-sol xhigh found no findings;
review-repair-entrypoint.md records its independent checks. Other lanes have no
new design or contract to reassess. Full supervisor integration started after
this review. Final downstream pins remain pending that test.

## Standalone synthetic evidence

The feaa1524 VM run passed the other10 examples but the new example read an
empty current snapshot after the legacy sample, before publishing any evidence.
The per-node reporter's first fresh evidence is asynchronous. Removed that test
input dependency and defined a complete standalone synthetic report directly in
the example (all required software identities included), matching the explicit
synthetic-evidence acceptance criterion. No product implementation changed.
The exact literal passes PayloadParser, ingestion, transitions/restart/removal,
and public Rake repair in a disposable DB preflight (2 examples0fail). Nixfmt
caught an empty Ruby single-quoted string terminating the Nix string; changed it
to equivalent double quotes. This is a direct fixture correction with no new
design/contract/operational boundary; focused checks and a full VM rerun follow.

The exact-pin reviewer found no consistency findings at feaa1524/fc7c37b2/09e09f0,
but marked those heads intermediate. Both downstream pins and rollout assertions
will be regenerated after the standalone-fixture integration passes and receive
a final bounded consistency checkpoint. All11 intermediate consumers built at
generation2026-09-14--12-33-18; repeat the final exact pin build as requested.

## Final exact revisions

The final standalone synthetic scenario passed all 11 VM examples at
`337c9257f5e11f36afe81eba4951e267b83e2fc7`. Configuration
`09b3370c2d628bcc7ab5eb7bbdf19edbcf8be347` and KB
`61aaf95d3dc0968728131a2cf4d4740dae6e9250` pin this exact tested head.
All 11 final consumers built as generation `2026-09-14--13-07-10`; the final
canonical KB check passed without prose or capture changes.

Fresh general exact-pin review at gpt-5.6-sol xhigh found no Blocking, Important
or Advisory findings. See review-final-pin.md for the bounded scope and checks.
All three final feature heads are now pushed over SSH and remote refs verified.
Final portal comparisons are captured. All final-head remote workflows passed,
including 135 integration scripts across 118 tests and all 26 API topic jobs
plus coverage. Both final KB workflows passed. No further product or pin edits
are part of the delivered kernel fix.
