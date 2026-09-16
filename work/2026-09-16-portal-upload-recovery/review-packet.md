# Portal upload recovery review packet

Review committed changes for initiative 2026-09-16-portal-upload-recovery.
Read the mandatory-change-review skill and your assigned lane. Perform review
personally with gpt-6-astra xhigh; do not delegate. Report file/line and severity.
Do not edit project code. Write findings to the review artifact specified by the
coordinator. Base/head revisions below are authoritative for this review.

## Request and acceptance

The portal rejected an email filename and could not remove the failed card,
even after reload. Remove retried the same rejected creation; persisted metadata
lost its error and offered resume. Expired-file DELETE 404 also kept a card.
User approved the plan and deployment through vpsfree-cz-configuration to aitherdev.
They selected Unicode/punctuation support while retaining control/length limits,
and explicitly required careful escaping.

Acceptance: local rejected/never-started files are removable without creation,
legacy and uncertain creates reconcile with the same identity, missing files
clear, other deletion failures remain retryable, browser storage verifies removal,
form readiness recovers and other attachments remain intact. Names are metadata,
never paths or HTML/shell instructions. Preserve JSON/MIME encoding and UUID paths.

## Ownership and actual consumers

codex-web owns mountUploads, generic UploadStore HTTP transport and browser
persistence. Its mountConversation and dev-workspace existing/new session forms
use this component. dev-workspace owns validation/storage/retention, scoped
permission checks and read-only/sent file policies. Its Go module and flake pin
select the exact provider below. The organization package and workspace follow
that runtime. Configuration devWorkspace supplies only the matching host module;
the application deploys through the user-profile workspace package.

## Commit boundaries and documentation

Provider has separate functional commits for browser recovery (with tests/docs
and nested module cache refresh) and UTF-8 request/header encoding boundaries
(with HTTP tests/docs). Runtime has a filename validation/tests/docs commit and
one provider dependency update (module/sums/vendor hash/flake and consumer cache
identity move together to consume the fix). Organization/workspace/configuration
changes are mechanical pins. Generated confctl commit wording is unchanged.
READMEs in both provider/runtime document current behavior. Plan/state, revisions,
quick logs and later rollout evidence live beside this packet.

## Compatibility and trust boundary

No new endpoint, catalog migration, Codex version/protocol, database, guest/node,
quota or storage path change. Browser optional creation/error metadata retains
legacy drafts. 400/413 indicate rejected creation; other errors keep uncertainty.
Deletion 404 permits local cleanup. Completed files remain readable on rollback;
old clients restore their known UI and validation limitations. Imports refresh
conversation.js v8->v9 and uploads.js v2->v3; CSS unchanged.

The local operator is trusted to administer this host. Review remote untrusted
filenames, origin/auth/scope enforcement, escaping, ordinary mistakes, concurrent
operations, interruption and rollback. Do not add compromised-operator filesystem
hardening. Broad upload redesign, a new cancellation API, default-branch integration,
archival, unrelated feature work and real private email inspection are non-goals.

## Validation and rollout

Quick checks passed: all provider Go packages; 41 shared browser contract tests;
runtime uploads and web Go packages; JS syntax; git diff checks; workspace
Nix deployment-contract check. Configuration Overcommit hooks pass. No framework
is declared/active in provider/runtime/organization/workspace. Review precedes
long package and real-browser acceptance. Browser tools have been prepared only.

Pending after review: real Firefox checks of both actual portal forms including
warmed cache upgrade/rollback, special-name upload/download, rejected and legacy
removal after reload, missing files; package checks/build; current-head CI; build,
dry-activate and deploy aitherdev plus user-profile switch, then live verification.
Retain previous generations and unmerged feature branches. All five branches are
pushed. Deployment is authorized; default-branch integration is not.

Risk classification: HIGH (persistent browser state, deletion, untrusted input,
cross-project compatibility and deployment). Required lanes: general, architecture,
scope, risk. All use gpt-6-astra xhigh.

## Revisions

### codex-web

- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-16-portal-upload-recovery/codex-web`
- Base: `882c88ccfbebfb646fb2cafbe9bc6790141b2d13`
- Head: `5c2c77b4649ec9aa6833ad0b7214f7702733e87e`

### dev-workspace

- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-16-portal-upload-recovery/dev-workspace`
- Base: `5d853b6b0c2608549a1f0e940c680ccb40a14bec`
- Head: `7bb347ccda2eba302d84fc0529ca6bbd6f4d1bc1`

### vpsfree-dev-workspace

- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-16-portal-upload-recovery/vpsfree-dev-workspace`
- Base: `b75cc8a6270219ca2fc25c1e292ce030fc33e45d`
- Head: `471b412a17e5a508aa18f56e0495ff07cda3248f`

### workspace

- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-16-portal-upload-recovery/workspace`
- Base: `94f8add7ca745ae9b35e2ee700e923663a2c5a02`
- Head: `54e330b05c9274c242a659cc287454415e812c3f`

### vpsfree-cz-configuration

- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-16-portal-upload-recovery/vpsfree-cz-configuration`
- Base: `b6e650ad902482b4c4e66b5a89a4275bed92419e`
- Head: `d7936f735c4850d447cea3a8e43dc50a0d80abd7`
