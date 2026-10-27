# Firefox fixture follow-up

The initial final review passed runtime range
`7e6d7c9cdb3388ab7abc720c034c15c21afbd686..ef85bd0ae50714dbce51ba5807c0234875212a53`.
The post-review native run failed at `durable-original-retry` in
[firefox.log](verification/firefox.log). Background title observation, native
discard and restoration had passed; the separate read-budget run passed.

The failure recorded one DOM submission, two HTTP message attempts, two fixture
dispatches and two journal records. The page had an accepted receipt and no
unknown outcome. The fixture closed an accepted request before sending response
bytes. Firefox transparently replayed that transport before JavaScript observed
failure. The application dispatcher issues one fetch and does not automatically
retry network uncertainty; its automatic retries require explicit transient
non-delivery. The stand-in's Send method lacked the real native client's
idempotency, so it counted the replay as another accepted turn. Its previous
quick test called ReconcileSend directly, bypassing the actual HTTP Send path.

The lead accepted a correction confined to `firefox_tabs_test.go`. Send now
serializes reconciliation before dispatch, returns an existing exact receipt,
refuses identity reuse with different content and appends one fsynced acceptance.
After upstream acceptance the loss helper sends 502 headers and an incomplete
JSON body before closing. This exposes uncertainty without zero-byte replay.
Truncated 202 would be unsuitable because the pinned client tolerates unreadable
JSON on successful responses. No production source or recovery behavior changed.

The new HTTP regression exercises the actual handler and shared loss helper:
upstream acceptance precedes truncated 502 plus `io.ErrUnexpectedEOF`, and retry
with the original identity recovers the receipt across exactly two HTTP attempts,
one native dispatch and one journal entry. Duplicate and mismatched input/action
assertions exercise the fixture Send method directly. The native runner retains
its original unknown receipt, cleared draft, explicit Retry original and exact
one-dispatch acceptance assertions.

Quick checks passed on the corrected source:

```sh
nix develop --no-update-lock-file -c gofmt -w portal/internal/web/firefox_tabs_test.go
nix develop --no-update-lock-file -c env \
  DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/document-title-notifications-absent-providers.json \
  go -C portal test -mod=readonly ./internal/web -run '^TestFirefoxFixture' -count=1 -v
git diff --check
```

All three Go fixture tests passed in 0.499 seconds. The unchanged Node/browser
source retains its earlier 75-test and syntax evidence. No long test was rerun
by the implementer. Native verification remains for a fresh utility after
affected independent review and refreshed consumer pins.

The amended final range is
`7e6d7c9cdb3388ab7abc720c034c15c21afbd686..d2099c62656bc2a36c306918a92832ba1e1a0cc0`.
The [range-diff](verification/runtime-fixture-range-diff.txt) shows only this
fixture change and its commit-message explanation since the reviewed head.
Production controller, assets, browser runner, prose and other files are
byte-identical to the reviewed head. The old head remains recorded here and in
the original review and failed-run evidence. The final branch has one focused
commit, seven changed files, 317 insertions and 65 deletions. There are no
migrations, superseded iterations or dependency-pin streams in this repository.
No migration was merged, deployed, released or externally consumed.

No repository or machine claims, deployment or merge occurred in this follow-up.
The lead owns tracking, affected review and rollout. Both consumers must select
the new published runtime head and consolidate their pin streams.
