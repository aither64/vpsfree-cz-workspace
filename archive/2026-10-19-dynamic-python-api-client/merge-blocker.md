# HaveAPI merge blocked by coordinator hook trust

Authorized operation: HaveAPI/master merge only, no release. Exact client head
c1823f3 remains reviewed/published/clean and all applicable CI passes. Coordinator
runa9c23f6e stopped in prepare before any merge job/master write. Session remains
open; no tags, versions, registry publication or runtime edit.

Owner and architect independently found an installed coordinator/Overcommit
incompatibility: preparation checks out feature config then a fresh historical
target config under one shared Git common directory; Overcommit0.73 forces a
single local configuration/plugin signature. Signing one configuration invalidates
the other. Native worktree config/includes and supported environment/alternate
configuration surfaces do not resolve it. Ordinary CLI signing was inspected and
succeeded at each exact snapshot, verification stayed enabled, but no further
alternating retry is valid. Current shared signature is historical689faa.

Architect proposes separate bounded development-runtime correction: resumable,
exact-phase preparation/hook trust handling, retaining exact approved configuration
and plugin hashes, normal signatures/hooks and coordinator queue ownership.
The smallest concrete mechanism/files/verification boundary is being saved by
architect in merge-hook-design.md. No code or runtime/package deployment is granted
by the HaveAPI-only integration direction; do not implement or merge another
repository under that approval. No direct Git bypass of configured coordinator.

Next decision: user authorization for coordinator runtime fix and its independent
review/verification, then resume the same authorized HaveAPI merge. Release remains
explicitly deferred. Preserve original evidence checksums, refs, source and logs.
