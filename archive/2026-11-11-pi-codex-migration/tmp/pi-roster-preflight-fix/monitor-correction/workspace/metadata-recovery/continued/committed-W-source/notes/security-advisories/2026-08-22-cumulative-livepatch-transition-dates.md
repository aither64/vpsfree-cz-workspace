# Cumulative live-patch transitions and mitigation dates

## Symptom

Retrospective CVE evaluations named live patch `.2`, `.3`, or `.5` as the first
fix but reset `vulnerable_until` and `mitigated_since` to the later `.6`
rollout. Repeated Node collection did not help because the defect was in
historical transition evaluation, not evidence freshness.

## Cause

The evaluator bound an already verified loaded patch to the current vpsAdminOS
closure at every historical point and treated all transition observations as a
gap. Linux cumulative replacement can keep tasks on either accepted patch while
the replacement is in progress. The `enabled` flag also expresses direction:
disabled plus transitioning can mean tasks are moving away from a patch but may
still execute it.

Sparse inventory metadata introduced a second risk: inheriting patch identity
without first proving an unchanged nonempty boot ID could carry trusted identity
across a reboot.

## Fix

- Track reviewed patch provenance only within one nonempty boot ID and only
  while the exact module remains loaded.
- Never inherit sparse patch metadata or omitted stable modules across a boot
  boundary.
- Inspect every loaded transitioning module and require both exact patch tuples
  to be accepted for the CVE.
- For an enabled forward transition, require the distinct counterpart to be the
  previously protecting outgoing patch.
- For a disabled reverse transition, require a distinct accepted counterpart
  that is loaded, enabled, and out of transition.
- Fail closed for first-time, multiple, ambiguous, unreviewed, removal,
  missing-boot, and inactive-counterpart shapes.

## Verification

The focused evaluator and dossier suites passed 69 examples, including forward,
reverse, removal, boot-boundary, and unreviewed-transition regressions. All 24
tracked evaluations reproduced exactly from the unchanged 2026-08-22 evidence
snapshot using `persist: false`. The full suite passed 164 examples and RuboCop
reported no offenses across 29 files. Final GitHub Actions passed on
`ea6247687fd02417f87e1e5593fecd8b9055925d`.

Related initiative:
`work/2026-08-22-security-advisories-6-12-95-6/`.
