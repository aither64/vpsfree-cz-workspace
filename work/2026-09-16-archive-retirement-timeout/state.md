---
lifecycle: active
---

# Archive retirement reliability

## Current status

Implemented and deployed to aitherdev through user-profile generation 48.
The original 2026-09-15-abuse-uceprotect archive completed successfully at
2026-09-16T20:47:21Z. Its journal and runtime authority are gone, conversation
history is archived, and retained feature refs are unchanged. The portal reports
archive/complete and remains read-only, as requested.

All implementation, local checks, four mandatory reviews, runtime CI and deployment
verification passed. Final organization extension CI, including its cluster-packaging
smoke test, also passed.
No remaining implementation or recovery task. Leave this initiative open and active:
all three feature branches remain unmerged, by the accepted scope. Integration
requires follow-up direction. No vpsfree-cz-configuration change was necessary.

## Repositories and deployment

Branch/group: 2026-09-16-archive-retirement-timeout.
Worktree root: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-16-archive-retirement-timeout.
All three feature heads are pushed over SSH; worktrees are clean.

| Worktree | Base | Final head |
| --- | --- | --- |
| dev-workspace | eb658d49e6b8182d5fc07ab98bc897c58490baa9 | 0bd68efa9cadb0589148fac40de7645a06b03468 |
| vpsfree-dev-workspace | 17da396e7fea5d4e31d4af1382da00fe4d140e17 | 90ce0cfe7c39c944aca0c7b27fe1e53a719075a3 |
| workspace | f8d6217a8a6e83bd317a7bef166aa650806ca553 | c60bac9f4ab92eb17a5bdae1b2fa7740c19a0e01 |

Runtime commits split scoped retirement timeout/stage errors (5deb10c) from portal
failure presentation/docs/browser coverage (0bd68ef). Consumer changes only update
pins. Explicit upstream master fetch before pinning confirmed runtime ahead 2,
extension ahead 1, neither behind. No default-branch merge was performed.

Profile 48: /nix/store/bspd81hp98awq942lnr7p93k38i8d8di-dev-workspace-0.2.0.
Previous profile 47 remains available for normal guarded rollback. Codex 0.154.0,
PID 1090021 and tmux PID 435397 were preserved. Portal/router restarted successfully.
The exact build, recovery, package switch and live checks are in [rollout.md](rollout.md).

## Changes and compatibility

Ordinary automatic commands retain 60-second deadlines; retirement gets a scoped
210-second subprocess deadline around the existing 180-second Go deadline. Runner
restores the previous timeout even on failure. Go errors identify the failing
retirement stage. Existing ambiguity, idle, merge and journal identity checks remain.

Portal shows the last failed automatic attempt and its timestamp separately from
the last completed journal step. It matches operation and conversation identities,
coalesces/throttles visible-page refreshes, keeps timestamped evidence after read
failures, and retains running retry state. Pending archives remain read-only.
No format, API, protocol, schema, cluster or host contract changes. Lookup remains
authoritative; lookup optimization and source-session revival were excluded.

## Verification and review

See [verification.md](verification.md) for consolidated evidence.
- Focused Ruby: 24 runs, 371 assertions, no failures/errors; real timeout and
  journal-retry behavior covered.
- Focused Go workspacecodex/web/CLI suites passed, including browser contracts.
- Chromium and Firefox fixture passed in 12.10 seconds: identities, warning,
  throttle/coalescing, visibility, read failures, running retry and completion.
- Runtime normal flake checks, extension full flake suite, final consumer package
  and deployment-contract check passed. Host-module idempotency VM follows the
  repository's master/manual policy; no host activation contract changed here.
- Runtime final CI 35148407354 passed. Extension final CI 35148442339 passed.
  Superseded extension runs 35147019235 and 35147853725 were canceled after repins;
  completed successful runtime runs were retained.
- Live health, served-JavaScript checksum, installed retirement timeout, source
  archive state, automatic timer and Codex/tmux identity checks passed.

Review risk: high, because lifecycle recovery and deployment affect persistent
runtime state. Four fresh gpt-6-astra/xhigh reviewers: general, architecture, risk,
scope. Original reviewed heads and commit split are in [review-packet.md](review-packet.md);
individual reports are review-general.md, review-architecture.md, review-risk.md
and review-scope.md. No Blocking/Important findings.

General advisory fixed in the owning portal/docs commit: manual recovery now
explicitly includes --abandoned for the automatic empty-session tier.
Architecture advisory accepted: behavior tests do not automatically detect future
Go deadline drift. Production hierarchy was inspected as 60/180/210 and documented
together; future deadline changes must revisit both components. Avoid a source-text
parser or new public configuration interface solely for that regression.

Real-browser acceptance found an incomplete test fixture: missing VerifyThread
caused normalization to remove its thread ID. Added a verifier for exact fixture
identity/cwd and a rendered-identity assertion, then both browsers passed. The
fixture correction and doc clarification were folded into the owning commit;
consumer pins were regenerated. Application behavior and reviewed boundaries did
not change, so no review rerun was required.

## Documentation and lessons

Updated runtime docs/dev-sessions.md, discoverable from its README: timeout
hierarchy, distinct worker/journal timestamps, read-only state and ordinary journal
recovery before profile activation. Checked portal deployment guide, extension
README and workspace policy; no host/system documentation change was useful.
Context owner applied vpsfree-user-facing-writing and humanizer-en to UI/docs text.

Reusable lessons:
- notes/dev-workspace/2026-09-16-auto-archive-retirement-timeout.md
- notes/dev-workspace/2026-09-16-archive-browser-fixture.md
- notes/dev-workspace/2026-09-16-getflake-shared-root-copy.md

Initial direct Node invocation lacked its Go fixture URL and Go inherited vendor
GOFLAGS in nix develop. Used the Go harness with -mod=readonly, as the existing
2026-09-11-focused-go-checks-in-dev-shell note prescribes. A previously realized
Playwright output was no longer present; realized the same pinned output and kept
temporary Nix roots through browser verification. No dependency workaround was used.

## Ownership and cleanup

DEV_SESSION_SLUG was absent and dev-session current reported none. Created this
initiative with dev-session start archive-retirement-timeout --no-codex --no-attach;
registered worktrees with explicit slug. Initial plan/state committed as f8d6217
before project commits. Shared master and unrelated dirty/index state preserved.
The external task-owning conversation is not replaced by a new Codex thread.

Keep the three clean worktrees and retained feature branches for integration or
follow-up. Do not archive/delete this initiative. Source archive tracking remains
unchanged at 50ec47f; manual retry made no further tracking commit. Owned transient
logs, commit-message files, temporary browser/build Nix roots and test captures were
removed after results were consolidated into this handoff.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-16-archive-retirement-timeout/
