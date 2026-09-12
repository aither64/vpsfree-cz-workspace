# Portal file uploads: committed change review

Initiative: 2026-09-12-portal-file-uploads. Coordination root:
/home/aither/workspace/ai/vpsfree.cz. Read work/<slug>/plan.md and state.md.
All project worktrees are under worktrees/<slug>/<project>, and all feature
branches use the initiative slug. Shared coordination checkout stays master.

## Requested outcome and boundaries

User requested drag/drop and picker uploads in the dev-workspace portal, file
cards, progress and removal, reasonable large-file limits, and paths included
in the corresponding Codex prompt. Uploaded bytes must remain outside Git.
User asked for clean shared codex-web support, accepted the detailed plan and
then authorized implementation and deployment to aitherdev through
vpsfree-cz-configuration. Default-branch integration and archival are excluded.

Accepted scope includes initial session creation, attachment-only prompts,
Send, active-turn steering, Queue, seven-day draft expiry, sent-file deletion
only when referencing sessions are idle with no queued/unresolved use, and
retention through archive/revive. Forks inherit references without byte copies.
Explicit session deletion removes owned files, including fork references.
All formats, including images, are local paths; no native image inputs, inline
content, extraction, scanning, previews or external object store.

Limits: 1 GiB/file, 10 files and 2 GiB/prompt, 10 GiB/session,
100 GiB/workspace, 4 MiB chunks, two browser transfers, eight server chunk
requests, 1 GiB free disk reserve. Metadata is bounded at 16 MiB and 10,000
records per category. Retain existing 20,000-byte prompt limit including paths.

## Revisions and commit split

| Project | Base | Head |
| --- | --- | --- |
| codex-web | de83e9c72dec6cb5ff8ec13d5b0b21ed60148117 | 152e353057c6da97c7bbb9ae4393075a2f8cc423 |
| dev-workspace | dc8d6cf7628a6a8db240f2e11ad61e8bc31ddacd | 16c3d78faf6351c6a0a79c479fae2ca36cc3de78 |
| vpsfree-dev-workspace | b37edd0f63fb7a984ba634c2d52d08e9344304b4 | 286a1f1b9c54d5b625712174df47975727d62193 |
| workspace | 94ca59f3f9d17306c2cc5e61099d83313309f4df | f5aa81ce3baf7f4b03d4109d0c5c7df4a0d2db76 |
| vpsfree-cz-configuration | b4e120294696578c3871124259f266205bad4393 | ecf8a52d640407b2e640cf11a70c7f8e6669b528 |

codex-web has one functional commit: optional shared upload interfaces,
transport, browser composer and attachment-aware submissions, with tests/docs.
These comprise the reusable attachment contract. Runtime has a separate provider
pin commit 5f3fd17 (Go/Nix/vendor hash and necessary browser fixture sibling
module support), then one feature commit for storage, portal/CLI ownership and
lifetime policy, corresponding controls, tests and documentation. Organization
and workspace are each one pin commit. Configuration is the unchanged confctl
generated input-set commit, preserving its changelog and width warnings.

All intended changes are committed. Configuration .bin/.bundle are transient
dev-shell tooling, excluded from commits. Project branches were fetched/rebased
before pushing and pins. No default branches were integrated. Coordination
initial plan/state commit is 94ca59f, outside the reviewed workspace feature.

## Ownership and public contract

codex-web owns codex.Attachment and optional DisplayText/Attachments on transcript
and queue entries, conversation.AttachmentProvider, UploadStore, UploadTarget,
NewUploadHandler, uploads.js and uploads.css, and additive attachmentIds on Send
and Queue. It preserves exact wire Text and receipt digests. The generic example
continues as a text-only consumer of the shared conversation module.

dev-workspace imports codex-web in portal/go.mod and pins the same source in its
flake for assets/protocol tests. Its internal/uploads owns private catalog/blob
storage, quotas, frozen prompt references and lifecycle records. internal/web
resolves draft/session scopes through existing origin, host-profile and runtime
checks. Browser app consumes the shared composer and sent-file cards; its durable
attempts retain IDs alongside original text. CLI fork/removal and portal creation
integrate with this same store. Organization flake calls the generic mkPackage;
workspace flake calls organization mkPackage. Configuration devWorkspace input
supplies only the NixOS host module. check-dev-workspace-deployment proves its
runtime revision and site identity match the workspace package.

## Compatibility and trust boundary

High risk: new private persistent state, upload authorization, file deletion,
cross-project browser/Go APIs, rollback and deployment. All four lanes required;
all reviewers use gpt-5.6-sol xhigh and perform their own lane directly.

The local development-host operator is trusted, as repository AGENTS.md says.
Do not invent protection against an already compromised operator controlling
filesystem mounts/locks. Remote browser requests remain untrusted. Retain normal
path/configuration checks, concurrency, data integrity and exact session identity.

Uploads live beneath selected user state portal/<workspace-id>/uploads, outside
workspace/worktrees. Completed files are immutable 0400. One locked, atomically
replaced catalog owns reservations, offsets, hashes, associations and tombstones.
Append writes/syncs bytes before catalog offset; retry truncates uncommitted suffix.
Complete renames/syncs before marking ready. Delete persists tombstone then GC.

Existing session manifests, creation receipts, lifecycle journals, Codex ledgers
and App Server protocol/version remain unchanged. Older packages ignore private
upload state and retain files; paths remain ordinary prompt text. Forward GC uses
completed deletion-history proof, never absent paths. Initial creation retains
accepted receipt goals and adopts via manifest goal digest; draft names cannot
be rebound across accepted creations. Forks match known exact wire prompts in
the actual fork transcript, including source submissions not yet observed.

Sent-file deletion serializes against browser mutations for referencing sessions
and checks live App Server status. Native terminal clients are external writers;
documentation requires them to remain idle during deletion. No protocol offers
an atomic external-client lease, and that broader protocol change is excluded.

Provider-to-consumer deployment order: codex-web, runtime, organization, workspace.
Build/test user-profile package and aitherdev system from these feature trees;
keep App Server version unchanged, then deploy config and profile. No changes
to databases, generated external clients, daemons or cluster-state contracts.

## Quick verification already passed

Use flake-derived tooling shell (go/gcc/nodejs/ruby) via
source /tmp/portal-uploads-dev-env; export TMPDIR=/tmp. Go mode for exact pins:
GOWORK=off GOFLAGS=-mod=mod. A temporary Go workspace was used during development
but the full portal suite also passed against the exact pushed module.

- codex-web: go test ./...; node --test test/conversation_browser_contract_test.cjs
  test/uploads_browser_contract_test.cjs. Origin/body/path controls, attachment
  download disposition, attachment-only Send/Queue, lost chunk/complete responses,
  prefix checks and durable browser identity covered. CI 34718576772 passed.
- Runtime: full portal go test ./...; go test -race ./internal/uploads; focused
  store/HTTP and creation/queue/transcript tests passed. Includes data bytes,
  crash suffix, restart, empty/duplicate names, quotas/concurrency/disk reserve,
  scope isolation, expiry, accepted creations, fork references, deletion epoch.
- Ruby removal/fork selection: 68 tests/612 assertions passed; new cleanup
  failure/retry test: 1 test/10 assertions passed.
- Workspace deployment contract: 3 tests/14 assertions passed; live configuration
  site and exact runtime pin check passed at 16c3d78.
- Configuration confctl generated pin Nixfmt and commit hooks passed.
- git diff --check passed. No long local integration, real-browser 1 GiB test,
  live App Server acceptance or deployment tests have started yet.

Automatic runtime CI is running after dependency publication. Cancelling its
superseded old head returned HTTP 403 because the token lacks Actions cancellation;
only current-head results will be accepted. Existing known limitation recorded.

Session tracking portal initialization hit the existing exact-cwd thread/list
60-second timeout in the large shared Codex history. No thread ID was recorded.
Retain the journal; do not reset shared services or allocate a replacement thread.
Tracking is current in state.md, with original retained hashes still available
from 94ca59f for a normal retry. This predates upload implementation and does not
block isolated App Server acceptance after review.

Report concrete findings with severity, file/line and commit references. Write
results to work/<slug>/review-<lane>.md. Do not edit implementation or launch
nested agents. Review the committed series and current pinned consumers.
