# HaveAPI 0.32.2 backport and publication

## Goal and scope

Backport applicable commits from HaveAPI `master` into `haveapi-0.32`,
prepare patch release 0.32.2, and publish it as requested by the user.
Affected project: `haveapi` only. No downstream configuration rollout.
The user's explicit branch instruction authorizes HaveAPI integration into
`haveapi-0.32`; it does not authorize integration into `master`.

## Approach and owners

1. Architect `architect0` inventories source/target history, patch equivalence,
   compatibility and the repository's version/publication contract; records
   `design.md` before implementation.
2. Implementer `implementer0` owns one serialized execution package: backports,
   release metadata, required documentation, hooks, quick checks and commits.
3. Independent retained reviewer `reviewer0` reviews the complete committed
   base-to-head history and final diff, including migration provenance.
4. Complete required longer checks, publish development branch, integrate the
   approved release target under a short repository claim, tag/publish using
   repository instructions, and independently verify public artifacts.

## Compatibility and recovery

Preserve supported HaveAPI 0.32 API/client behavior and mixed-version consumers.
Inventory persisted state, schemas, protocol and dependency changes before
selecting backports. Do not pull incompatible next-release work into a patch
release. Record necessary ordering and rollback limits in the design.
Publication is requested; do not republish an existing immutable version or
rewrite published branch/tag history. Reconcile partial publication before retry.

## Documentation and acceptance

Readers are HaveAPI maintainers and package consumers. Existing repository
release notes/version files are the likely public documentation destination;
individual publication evidence belongs in this session's state/release receipt.
Acceptance: agreed backports present on remote `haveapi-0.32`, release 0.32.2
versions consistent, required checks and independent review pass, release tag
and intended package artifacts publicly verifiable. Leave the session open.

## Testing

Derive exact commands from HaveAPI's own instructions, manifests and CI.
Quick checks precede final independent review; long or uncertain checks use the
mandatory fresh utility watcher. Bound verification to backport/release risks.
