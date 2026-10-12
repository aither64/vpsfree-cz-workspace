# Scope and proportionality review

Reviewed the complete committed series and pinned consumers at the packet heads:

- `codex-web` `de83e9c72dec6cb5ff8ec13d5b0b21ed60148117..152e353057c6da97c7bbb9ae4393075a2f8cc423`
- `dev-workspace` `dc8d6cf7628a6a8db240f2e11ad61e8bc31ddacd..16c3d78faf6351c6a0a79c479fae2ca36cc3de78`
- `vpsfree-dev-workspace` `b37edd0f63fb7a984ba634c2d52d08e9344304b4..286a1f1b9c54d5b625712174df47975727d62193`
- `workspace` `94ca59f3f9d17306c2cc5e61099d83313309f4df..f5aa81ce3baf7f4b03d4109d0c5c7df4a0d2db76`
- `vpsfree-cz-configuration` `b4e120294696578c3871124259f266205bad4393..ecf8a52d640407b2e640cf11a70c7f8e6669b528`

## Important

### The catalog's safety bounds become irreversible lifetime quotas

Commit `dev-workspace` `16c3d78faf6351c6a0a79c479fae2ca36cc3de78` caps every catalog category at 10,000 records (`portal/internal/uploads/store.go:28-29,166-167`) and refuses new drafts or files based on total map length (`portal/internal/uploads/store.go:211-215,427-428`). However, expiry and deletion only change records to `deleted` and unlink bytes; they never remove entries from `Files`, `Scopes`, or `Submissions` (`portal/internal/uploads/store.go:808-855,857-880`). This means removing unused files cannot recover the capacity that the error at `portal/internal/uploads/store.go:182-183` tells the operator to recover. Completed files also retain and repeatedly serialize every per-chunk checksum even though prefix verification applies only while an upload is incomplete (`portal/internal/uploads/store.go:514-555,330-349`; `codex-web/conversation/assets/uploads.js:94-107`).

The unnecessary accumulation is not limited to actual uploads. The creation page allocates a durable draft scope during initialization before a file is selected (`portal/internal/web/static/app.js:961-987`). Each browser profile therefore consumes a scope even if it never uploads, and each accepted creation causes the adopted draft to become unavailable under the draft URL so a later visit allocates another. Empty and deleted scopes are never reclaimed.

At the fixed record or 16 MiB catalog limit, uploads fail permanently for that workspace even after every removable file has been deleted. That is disproportionate tombstone retention and a credible operational failure, rather than a useful compatibility guarantee. Keep records needed to decorate transcripts and preserve live/fork references, but reclaim expired empty drafts and records whose owning and referencing scopes are all deleted. Clear chunk checksums when completion makes resume verification obsolete. Add a focused test proving that expiry and completed session removal release record capacity; alternatively, record an explicit decision that 10,000 is an intentional lifetime ceiling and change the user-facing remediation so it does not claim deletion frees space.

## Residual risks and test gaps

The remaining upload mechanisms map to explicit accepted behavior: bounded resumable chunks, response-loss recovery, frozen prompt associations, fork references, archive/revive retention, and journaled session deletion. The public `codex-web` surface has a current `dev-workspace` consumer and does not introduce an external storage framework or protocol change.

The configuration pin also advances `devWorkspace` from `bcbaf825` through the previously reviewed and live-accepted portal-review series before selecting `16c3d78`; its generated commit message exposes that full range. I found no new scope finding in that already-integrated base range, but deployment validation must use the complete pinned package rather than treating the host pin as an upload-only delta.

The packet correctly leaves real-browser large-file validation, live App Server acceptance, package checks, and deployment until after review reconciliation. No extra conformance framework is warranted for those checks.
