# Lead pre-integration acceptance

User authorization: [release-authorization.md](release-authorization.md).
Repository/target: `vpsfreecz/haveapi`, `refs/heads/master`.

Lead rechecked the current complete 22-commit base-to-head series and final tree
against the accepted [final review](go-query-final-review.md):

- Base `a32b15e379f44fc6dae4b15ef4ec17a142e5f465`.
- Head `b64fb25bea8d8222fb3263b99956c0b61438a859`.
- Tree `05384a632290653cb4560c7451b3897acd5956c8`.
- Actual complete binary diff SHA-256
  `5110c3301e70a0abd82cba9d7b93033ac8f814d89c8cfab0949f8884f515b6ec`
  equals `go-query-final-diff.patch`.
- Final one-line message exactly `Version 0.30.0` with no body.
- Review explicitly accepts the consolidated update streams, no obsolete history
  or redundant updates, and **no migrations**. No source changes since review.
- All ten feature-head CI runs and final local artifact/Go acceptance passed;
  dynamic/Rust results retain their reviewed input-equivalence evidence.

Clean detached target preparation and enabled hooks are owned by implementer0.
Acquire a single HaveAPI repository claim only after preparation completes and
immediately before fresh exact remote/source/cleanliness checks, ff-only merge,
normal SSH master push and remote proof. Release before CI or record updates.
A moved target or hook intervention returns to unlocked preparation after
reconciling actual effects. Retain the feature ref and all artifacts.

This document records readiness inspection, not a claim or proof of integration.
The exact execution receipt will record final master head and released claim.
