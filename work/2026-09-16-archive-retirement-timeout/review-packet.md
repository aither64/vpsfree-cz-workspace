# Archive retirement reliability review

User request: implement the approved plan to fix automatic archive deadlines,
show clear failures, recover 2026-09-15-abuse-uceprotect and leave it archived,
and deploy aitherdev. No default-branch integration or new-session archival.
The user explicitly excluded history-lookup optimization and session revival.

Tracking: work/2026-09-16-archive-retirement-timeout/{plan,state}.md.
Worktree root: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-16-archive-retirement-timeout

| Repository | Base | Head |
| --- | --- | --- |
| dev-workspace | eb658d49e6b8182d5fc07ab98bc897c58490baa9 | a65583d45b707eb23feb7d490ba177e8360dfb8d |
| vpsfree-dev-workspace | 17da396e7fea5d4e31d4af1382da00fe4d140e17 | 1a0bc7db6c968bde9cb9ecbd737d8b1b6f28de44 |
| workspace | f8d6217a8a6e83bd317a7bef166aa650806ca553 | 3610be86615b8710b2e1bfe8a53b9771bad15fdf |

Read repository AGENTS.md. All changes are committed. Runtime series separates
retirement timeout/stage errors/tests (5deb10c) from portal presentation and its
tests/docs (a65583d). Consumer pins have one generated update commit each.

Acceptance: ordinary commands remain bounded at 60 seconds; retirement receives
210 seconds around its existing 180-second internal deadline; prior timeout is
restored even on error. Automatic retry after tracking_committed preserves exact
journal identities and does not recommit tracking. Failure banner shows a
matching worker attempt with its own timestamp and distinguishes last completed
step. Refresh coalesces/throttles visible pending archives, retains timestamped
failures during read failures, ignores stale identities, and does not overwrite
a running retry. Pending archives remain read-only; completion removes warnings.

Owner is generic dev-workspace. Existing codex-web APIs and Codex 0.154.0 remain
pinned unchanged. Organization consumes runtime via flake.nix/lock and packages
its extensions; workspace consumes organization and supplies site config. No
vpsfree-cz-configuration/module/host contract change is necessary. Lookup remains
authoritative; index-only shortcut was rejected in previous deployed work.

Risk: high (lifecycle cleanup, interrupted-operation recovery, profile deployment).
All four mandatory lanes apply, gpt-6-astra/xhigh. Operator is trusted to administer
this host; retain ordinary concurrency/identity checks and remote trust boundaries.
No state schema, public API, protocol or journal format changes. Existing readers
and previous package remain compatible. Package switch refuses pending journals;
first recover the exact source archive with installed normal manual archive,
then switch the reviewed consumer workspace package. Do not edit/delete journals
or restart the shared Codex service. Preserve conversation history and branch refs.

Docs: runtime docs/dev-sessions.md (linked by README) now explains timeout hierarchy,
failure display and normal recovery. Existing portal deployment guide, extension
README and workspace policy checked. Site-specific exact rollout is recorded in
this initiative, not copied into generic runtime. New UI prose passed context-owner
vpsfree-user-facing-writing + humanizer-en.

Quick verification (Nix environment):
- Ruby dev_session_test --name '/retirement|automatic/': 24 runs, 371 assertions,
  zero failures/errors. Includes actual short-deadline subprocess timeout/retry.
- go test -mod=readonly ./internal/workspacecodex ./internal/web ./cmd/workspace-portal:
  passed, including browser-contract JavaScript fixture and archive template test.
- git diff --check passed; workspace deployment-contract build passed.
- Real Chromium/Firefox fixture is written but intentionally runs after review,
  along with packaged suite and isolated automatic-archive acceptance.

Review your assigned lane directly; do not spawn subagents. Write your findings to
work/2026-09-16-archive-retirement-timeout/review-LANE.md and return concise findings
with severity, commit/file/line references, or clearly state none. Do not edit code.
