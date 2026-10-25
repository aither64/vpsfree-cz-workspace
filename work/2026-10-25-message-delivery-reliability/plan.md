# Message delivery reliability

Make portal message sending recover automatically from proven transient
non-delivery, without replaying a message whose outcome is uncertain. Investigate
and recover the blocked `Implement the plan.` attempt in
`2026-10-24-context-copy-performance-tests` after deploying a verified candidate.

The user initially requested no tracking. Initial implementation and feature
publication used isolated worktrees without records. The user subsequently said
“you can start tracking this session”; these records preserve the existing task scope. The portal requires a managed
conversation rooted in the session directory, so its supported initializer will
create a coordination-only backing conversation. The external investigation chat
remains the implementation coordinator; the backing conversation performs no
implementation and does not create a team. No default-branch integration is
authorized. The accidental archive-storage suggestion is out of scope.

## Scope and approach

- `codex-web`: prove the pre-transmission boundary, restore prepared attempts
  after cancellation during durable admission, expose retryability, and replace
  whole-ledger operations with optional indexed SQLite storage.
- `dev-workspace`: select the shared database, preserve backend-independent
  archive exports, enforce the package compatibility boundary, finish admitted
  plan sends after browser disconnection, and retry transient failures with the
  original browser identity.
- `vpsfree-cz-configuration` and this workspace: pin the same published runtime
  while preserving native Codex, extension and sibling inputs. Build and deploy
  the application from its user profile; use configuration for host contracts.

## Evidence and acceptance

The original error names the Go WebSocket writer's cancellation-sensitive lock.
A deterministic regression reproduces cancellation after persisting `submitting`
and before requesting a writer. The predecessor leaves retries permanently
uncertain. The fixed client restores `prepared` only with proof that no bytes
were handed to the writer. Missing native history alone never permits replay.

The shared live JSON ledger contained roughly 21,000 send records and occupied
about 15.2 MiB of its 16 MiB limit. A synthetic lookup benchmark measured about
396 ms/72 MB allocated for JSON versus 4.9 ms/12 KB for SQLite. Historical stage
timings were absent; the exact delay of the original request remains unknown.

Acceptance requires deadline-race, migration, stale-claim, browser-identity,
disconnection and package-compatibility coverage; independent final review;
packaged/native verification; verified portal continuity after activation; and
revalidation of the exact original stuck attempt before any targeted recovery.

## Compatibility, deployment and recovery

SQLite schema 1 imports deployed schema-3 JSON, retains checksum-named backups
and journals interrupted publication. Schema-4 fences make old JSON readers
refuse migrated state. Ordinary transactions load only the requested identity
or thread; unresolved records have no age purge. Native Codex remains 0.163.0.
HTTP retryability is additive. Browser retries require explicit transient
non-delivery and retain the original identity; uncertain sends are not replayed.

Exclude predecessor application writers through the normal profile transition.
Native turns remain running. After database creation, recover forward with a
compatible package; old JSON backups cannot replace newer receipts. The runtime
contract fences incompatible package selection. No database migration from an
earlier branch iteration is supported or deployed.

Review and build before claiming aitherdev. Hold the exact machine claim through
activation, verification and the required integrated deployed lineage. Deployment
does not supply merge approval. Preserve unrelated work and retained generations.
Only recover attempt `3466274b-d2c6-45f9-8ccb-4fe12ca9a382` on thread
`01a16fb2-77cb-7421-a66c-b7274a178ea2`, using its original UUID and verified
pre-transmission evidence. Reconcile acceptance first; never reset other attempts.

See [design](design.md), [state](state.md), codex-web's
`docs/submission-storage.md` and dev-workspace's `docs/workspace-portal.md`.
