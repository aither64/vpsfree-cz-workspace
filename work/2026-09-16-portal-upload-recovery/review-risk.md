# Risk and compatibility review

Reviewer: gpt-6-astra, xhigh; performed directly without delegation.
Risk: high. Reviewed the exact committed series in `review-packet.md`, local
repository guidance, runtime trust-boundary documentation, upload consumers,
tests, and downstream deployment pins.

## Findings

### Important R1: DELETE 404 does not establish that the file is absent

- Changed location: codex-web `conversation/assets/uploads.js:314`, commit
  `20680804ac5301b27b2726b99f1ec4d9281a8305`, reviewed head
  `5c2c77b4649ec9aa6833ad0b7214f7702733e87e`.
- Cross-project evidence: dev-workspace `portal/internal/web/uploads.go:60`
  converts every `resolveConversation` error into HTTP 404. At reviewed head
  `7bb347ccda2eba302d84fc0529ca6bbd6f4d1bc1`,
  `portal/internal/web/server.go:2405` and `:2442` can fail for a temporary
  transition/profile failure or a temporarily noninteractive runtime, before
  the upload store's Delete method runs.
- The new browser handler discards the selection for all those responses. The
  server file remains present, but its draft selection and convenient removal
  path disappear. This violates the requirement to retain retryable failures;
  it can also leave unsubmitted bytes retained until expiry.
- Confirmed with a temporary Go test overlay, without editing project files.
  Both profile-unavailable and runtime-unavailable cases produced
  `DELETE status=404`, `{"error":"Upload scope is unavailable"}`, and a
  subsequent direct store Status returned `ready` for the same file.
- The coordinator's proposed narrow fix is appropriate: after DELETE 404,
  perform the existing authorized list read; clear only when a successful list
  proves the ID absent or deleted. Keep the card and error when listing fails
  or the file remains present. Add coverage for mutation-only refusal plus a
  readable existing file, list failure, and genuinely absent/deleted files.
  This preserves the current endpoints and requires no persisted-state change.

### Important R2: a transient persistence failure can enable submission of a deleted file

- Locations: codex-web `conversation/assets/uploads.js:245`, `:255`, and
  `:317`, commit `20680804ac5301b27b2726b99f1ec4d9281a8305`, reviewed head
  `5c2c77b4649ec9aa6833ad0b7214f7702733e87e`.
- After a successful server deletion, `save(next)` may fail. The catch restores
  `removing=false` and calls `failed(entry, error)`, whose immediate `save()`
  retry can succeed. That clears `persistenceError` while retaining the old
  entry with `state="ready"`. `ready()` ignores the entry's error, and `ids()`
  then returns the deleted server ID. An unrelated successful draft save after
  a longer storage failure has the same effect.
- Confirmed using the shipped browser component and its existing DOM fixture
  in a temporary copy. One `setItem` failure after DELETE followed by successful
  writes yielded: server file absent, card count 1, `ready() === true`, and
  `ids()` containing the deleted ID. The saved entry remained `state="ready"`
  with `error="Storage write failed"`.
- Preserve the completed-deletion state while local cleanup is pending, or
  otherwise keep this entry unready until its selection is durably removed.
  A successful write of the retained erroneous entry must not restore readiness.
  Cover a one-shot write/readback failure and recovery through another entry's
  save, in addition to the existing continuously failing storage test.

## Verification and security assessment

- Temporary Go-overlay reproduction: `go test -overlay <review-overlay>
  ./internal/web -run TestRiskReviewDeletion404RetainsExistingFile -v -count=1`
  under pinned Nix Go/GCC. Both cases passed their reproduction assertions.
- Temporary browser-fixture reproduction: pinned Nix Node with
  `--test --test-name-pattern='Risk review:'`; the stale-readiness reproduction
  passed. Temporary fixtures stayed outside all project worktrees.
- No filename injection or path-escape finding. Names stay in text nodes,
  JSON-serialized prompt references, and MIME-formatted attachment headers.
  Storage still derives from a generated UUID and a restricted extension;
  request size, exact origin, scope resolution, and sent-file deletion guards
  remain in place. The trusted local operator boundary was respected.
- Catalog schema and storage path derivation are unchanged. Older catalog
  readers do not reapply creation-time filename validation when opening a
  completed file. Browser metadata additions are optional and legacy drafts
  are treated as uncertain.
- Pins consistently select provider `5c2c77b`, runtime `7bb347c`, organization
  `471b412`, workspace `54e330b`, and configuration `d7936f7`. The configuration
  consumes only `nixosModules.host`; its host module/path sources are unchanged
  between the previous configuration pin and the new runtime. Application
  deployment remains through the user-profile package.

## Residual gaps

- Real-browser checks of both forms, warmed cache upgrade/rollback, package
  builds, CI, host dry activation, deployment, and live acceptance remain
  pending as stated in the review packet.
- Actual old/new runtime interoperability was inspected in source, not executed
  here. Include completed-file access and uncertain/rejected draft handling in
  the planned rollback acceptance. Creation-time policy precedes idempotent
  lookup, so a file accepted before a validation-policy change can be rejected
  during uncertain-create reconciliation; unsubmitted orphan retention remains
  bounded by the existing expiry policy.
- This is an advisory code review, not a full security audit of unchanged
  lifecycle, authentication, or upload-retention code.

## Exact reviewed revisions

| Repository | Base | Head |
| --- | --- | --- |
| codex-web | `882c88ccfbebfb646fb2cafbe9bc6790141b2d13` | `5c2c77b4649ec9aa6833ad0b7214f7702733e87e` |
| dev-workspace | `5d853b6b0c2608549a1f0e940c680ccb40a14bec` | `7bb347ccda2eba302d84fc0529ca6bbd6f4d1bc1` |
| vpsfree-dev-workspace | `b75cc8a6270219ca2fc25c1e292ce030fc33e45d` | `471b412a17e5a508aa18f56e0495ff07cda3248f` |
| workspace | `94f8add7ca745ae9b35e2ee700e923663a2c5a02` | `54e330b05c9274c242a659cc287454415e812c3f` |
| vpsfree-cz-configuration | `b6e650ad902482b4c4e66b5a89a4275bed92419e` | `d7936f735c4850d447cea3a8e43dc50a0d80abd7` |
