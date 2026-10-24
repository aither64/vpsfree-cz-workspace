# Proposed production-only series: content preview

PREVIEW ONLY. No commit or ref was created. No original worktree/index/source,
branch, remote, registration, package or published history was changed.

- Old range: `7860521f30826c3886c89c35e8ab6f4e082e0a4b..8772bab21cd8739bf4672cdf4976aea2a6e59de3` (old-series.txt).
- Captured target main: `b9f47f06e0877eb4a160053c413c4b87dd4a3d55`; no fresh fetch was performed.
- Proposed dependency tree: `14c9143b8ee3a4bc06363c5b77b169c182b22539` (9 paths).
- Proposed final tree: `69ea72eca2fb2e8df7c4bcab9e8a8c849964f824` (72 paths total).
- Proposed production commit: the remaining 63 paths, including HAVEAPI_CLIENT.md.
- Proposed preserved branch: `dev/haveapi-async-client-before-production-consolidation`
  at `8772bab21cd8739bf4672cdf4976aea2a6e59de3`. This ref does not exist yet and must precede any
  later authorized history replacement.

The proposed new range is b9 -> the dependency tree -> the final tree. New commit
IDs do not exist: user permission and normal commits/hooks come later. Commit1
contains one final archive/provenance/manifest/lock/Nix integration and its package
source checks/PACKAGING documentation. Commit2 contains the actual production
adapter, migrated fixtures/tests/type/structural records and current/runtime
client guide plus dated work-log evidence. There are no add-then-delete pilot
commits, executable pilot entry/runner, opt-in API or duplicate wire transport.
No migrations; one normal dependency stream, source f94e65e/tar41c3c3f unchanged.

## Reconciliation evidence

- b9-to-preview.diff is the complete proposed final patch.
- proposed-1-dependency.diff and proposed-2-production.diff are the exact two
  content partitions; first-paths.txt/second-paths.txt enumerate them.
- 8772-to-preview.diff includes all incoming main changes and adaptations.
- six-path-reconciliation.diff isolates the six overlapping paths.
- evidence-annotation.diff separately identifies two dated-record clarifications:
  old quick results now name tested8772; historical pilot records name0d05/5dd.
- receipt.json and static-reconciliation-checks.json bind the trees and checks.

Only WORK_LOG needed textual conflict resolution; both contributors' entries are
retained. Nodes test now uses the approved real-package XHR fixture and verifies
AbortError/no new send rather than fetch-init identity, keeping GET/no-pagination
and OPTIONS/method-query assertions. E2E union is68 adopted/197 deferred, with
compiler flags, immutable baseline and remaining deferred records unchanged.
94 incoming paths outside overlap are byte/mode identical to b9, including
nodes.ts/helpers and all UI consumers. 64 feature paths outside overlap and the
two evidence annotations are byte/mode identical to reviewed8772. Vendor/Nix and
all dependency-partition blobs equal reviewed8772 exactly.

Inventory generation inputs (the three route files and64 API module names) and
the generated document are unchanged from reviewed8772, so regeneration is not
needed. Full proposed diff whitespace check passes. No app check, npm setup,
server, browser, Nix build or integration operation was run.

Git initially refused the archived checkout's zero-stat private index. An explicit
private update-index --refresh resolved that stat-cache issue; the retained first
apply log proves no index/tree content change before the successful three-way
application. This was preview setup, not an application test or blind rerun.

Original tracked files, HEAD/branch, cached main and index SHA256 match the before
receipt exactly. Review of this concrete preview and explicit user authorization
are required before creating the preserved branch, making normal commits or
replacing/publishing any history. The browser recipe remains held and still
binds8772; it must be rebound only after the final candidate is accepted.
