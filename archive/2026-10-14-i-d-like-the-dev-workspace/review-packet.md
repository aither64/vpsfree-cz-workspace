# Final review packet (draft)

Status: runtime final review, complete committed substantive deliverable. All
intended source/docs/tests are committed and quick checks passed. Deployment
composition's generated pin commits follow runtime publication and will receive
their own complete-series inventory/conclusion before branch readiness.

## Outcome and bounds

Compact session title attention/reservation markers, focus acknowledgement,
session-wide notification mute in creation/settings, and useful browser push
delivery without any portal tab. Targets are Firefox/macOS and Chrome/Chromium,
browser running minimized or unfocused. Fully quit-browser delivery is not
required. No page-only fallback is acceptable. No master merges authorized.

## Context and repositories

See [plan](plan.md), [implementation brief](design.md), [state](state.md) and the
separate [rollout record](rollout.md). All feature worktrees use this session slug.
Primary owning component is dev-workspace; existing pinned codex-web provides
stable prompt/turn identities, so no shared-library change is intended.

Deployment composition includes workspace's direct nested runtime selection
through the retained vpsfree extension and vpsfree-cz-configuration's existing
`dev-workspace/devWorkspace` channel. Extension pin, sibling inputs and follows
relationships must remain unchanged.

## Risk and reviewer selection

Risk: high, due to private persisted browser subscription/VAPID/event state,
authenticated mutations, outbound push destinations, service workers and
system/profile deployment. Review lanes: general; architecture/repetition;
scope/proportionality; risk/compatibility.

Expected retained independent reviewer: `reviewer0`, saved GPT-6.1 Sol/xhigh,
read_only, no authorship. Reverify live same-session roster before assignment;
do not override saved model/effort. Reviewer must read mandatory-change-review
skill and every selected lane reference, and review directly without subagents.

Trust boundary: local workspace operator is trusted to administer host state;
remote HTTP clients, push endpoints and browser payloads remain untrusted.
Preserve exact-origin checks, authorization, private permissions, input bounds,
session incarnation identity, request retry and reservation authority.

## Exact runtime inventory

Repository/worktree: `worktrees/2026-10-14-i-d-like-the-dev-workspace/dev-workspace`.
Review base: `ba8669b14536f72b559abc912bba8eac430111e4`; clean head:
`a7000a2ae803c21274eb65d23ee63d2097fb8829`.

Complete own series:

1. `0bddd69473c1c18d7574fa195215910e680484e0`: maintained Web Push dependency,
   module metadata and corresponding vendorHash.
2. `a7000a2ae803c21274eb65d23ee63d2097fb8829`: session attention and background
   Web Push, interdependent observer/store/sender/worker/creation/settings,
   focused tests and feature/operations docs.

Feature diff: [runtime-final.diff](runtime-final.diff), 34 files, 2658 additions,
61 deletions. Full commit messages: [runtime-commits.txt](runtime-commits.txt).
The initial assigned base was `92b2576d82a850fa4e24f889a8ff592a1e7f3e42`;
the rebase additionally preserves already-upstream `273a08c` and `ba8669b`
sensitive-session changes. There are no superseded own commits or repeated pin
streams. No migration/schema rewrite; no DB/lifecycle/roster/runtime-contract or
Codex protocol change. codex-web stays `5f15b9293f9b1eef7469a34d7b2044c743160283`.

New optional private browser notification store is initial schema 1, with no
older notification format. Unmerged, unpublished, undeployed, unconsumed.
Creation receipts gain optional strict boolean `browserNotificationsEnabled`;
old omitted requests keep old identity/digest, explicit false survives retry.
New flagged receipts require capable bundled Go/session/host readers. Supported
recovery uses the same or a compatible successor, under forward-only selection
and existing creation-transition fences. Inspect this contract in both Ruby
readers. No historical receipt rewrite or predecessor-format migration.

## Verification and documents

Prepared declared Nix env: `runtime-dev-env.sh`; Go 1.26.6, Node 24.19.0,
Ruby 3.4.9. GOCACHE `/tmp/session-attention-go-build`, GOMODCACHE
`/tmp/session-webpush-mod`, GOFLAGS `-mod=readonly`, GOPROXY `off`, absent test
provider catalog. Repository declares no hook framework. After rebase:

- Portal `go test -mod=readonly ./internal/web -run
  '^Test(Attention|Notifications|Creation.*|Preparation.*|Sensitive.*)'` passed,
  19.389s; real-browser opt-in tests skipped.
- `node portal/internal/web/attention_browser_test.cjs`: 6 passed.
- Existing preparation browser contracts: 22 passed.
- `ruby test/dev_session/agent_team_creation_test.rb -n /browser_notification/`:
  1 test, 5 assertions passed.
- `ruby test/workspace_host/agent_team_registration_test.rb -n
  /notification_preference/`: 1 test, 10 assertions passed.
- Changed JS and both Ruby helpers syntax, diff checks passed.
- Final tracked-source dependency-only forced hash confirmed
  `sha256-iyydGWryLmh8P+YxQcQ2SqGIj1Lds+WBDgsKQV4uFqA=`. Exact expected
  mismatch evidence in `vendor-hash-final.log`/`.status`; known quick check.

Changed docs: `docs/browser-notifications.md`, operations companion and portal
guide entry link. Lead directly applied user-facing writing/copy pass before
commit; rollout evidence stays in this session. No long integration, full flake
suite, live provider send or macOS display proof yet. Those follow this review.

## Review deliverable

Send the review report to the lead; saved read_only access remains in force for
all files. The lead persists it as `review.md` in this session directory.
Findings ordered Blocking/Important/Advisory with concrete references. Explicit
conclusions on complete history, absence/presence of obsolete iterations,
repeated update streams and migration lineage. Review all four selected lanes
and representative pinned consumers. Do not edit source or launch long tests.

## Later composition inventory

- Complete deployment composition base-to-head series and final diff for workspace/configuration.
- Logical commit split and rationale for any bundled changes.
- Obsolete-history inventory and each repeated dependency/channel update stream,
  final revision and consolidation disposition.
- Migration/private-format provenance: merged, released, deployed or externally
  consumed; explicitly state absent database/lifecycle migrations if confirmed.
- Final composition quick-check commands/results and known coverage gaps.
- Owning-project feature/operations documentation changes and copy pass.
- Exact source/dependency pins and deployment composition contract evidence.

Require explicit reviewer conclusions on full history, repeated update streams
and migration lineage. Blocking findings must be fixed before long verification.
Apply the workflow's narrow-fix policy rather than rerunning unaffected lanes.
