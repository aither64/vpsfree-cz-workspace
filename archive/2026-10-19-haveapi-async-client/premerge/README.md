# HaveAPI premerge evidence

## Current HaveAPI premerge preparation: 19c20c90

The user explicitly approved **HaveAPI -> master only**: “so let's merge the
haveapi client. keep the vpsadmin-webui PR open”. This owner package prepares the
branch; lead alone owns the supported coordinator merge. WebUI PR74 is untouched.
No npm/tag release, deployment, default-branch push or lifecycle action ran.

- Reviewed prior range: `c14e7d3158b91c134c2817b489cd29772fc09f82..f5320eae05cbf8256a40cb04358be876ea7bde75`.
- Fresh SSH upstream/final base: `c58704a08451a231fdf6c6123437133422af46dc`.
- Rebased feature head: `19c20c90cc957d4225ece50a92e190855f252710`.
- Final tree: `0ef10a638118397c07f537b6a33159ec2ee21fe1`, clean index/worktree.
- Normal Nix rebase replayed five commits without conflicts or manual resolution;
  authors/messages preserved, committer Jakub Skokan `<jakub.skokan@havefun.cz>`.

| Reviewed commit | Rebased commit | Purpose |
| --- | --- | --- |
| `34f431e76d52508233a1753eab1bd7d096b54f19` | `991101f212eb7da24b5ba71e679eb4b59baef56d` | clients/js: capture callback bundle compatibility |
| `0e63360e46a40dcbe744d7ee7475fb0151f8d37b` | `0d2111e5a93490abbad2f5167d45dea026f663f3` | clients/js: author callback client in TypeScript |
| `81994d25cf6dc50754a7e9b2820aafc8fa00f0e2` | `8f8e5766b8be9c99d2bf39a9e1fe7f80220fade5` | clients/js: add an independent typed Promise client |
| `76f190f9561eabee3414919ddd26e62e48c43f58` | `f3fcd33fdbc1d00461535d95f0337c44aa0d12d4` | clients/js: document TypeScript source workflow |
| `f5320eae05cbf8256a40cb04358be876ea7bde75` | `19c20c90cc957d4225ece50a92e190855f252710` | clients/js: expose the callback client as CallbackClient |

Ordered stable patch IDs and message hashes match for all five commits;
`premerge/range-diff.txt` reports five `=` pairs. Two independent private-index
reconstructions reproduce the exact final tree: old reviewed f5320eae plus the
upstream three-path patch, and latest c58704a0 plus the complete reviewed feature
patch. The active index/worktree were never used for reconstruction. The old
reviewed history is retained in the evidence bundle; original review/check
receipts remain unchanged.

The only old-head-to-new-head source difference is upstream release guidance,
`utils/release/publish.rb` and its spec. Feature release changes still only use
`client.ts` for version replacement/checking and add one mismatched authored-TS
version spec around line 50. Upstream adds separate GitHub release-preparation
coverage around line 172; there was no conflicting edit or publisher change in
the feature. Combined release tests pass. The entire `clients/js` subtree and
all emitted artifacts/bodies are identical to f5320eae. Every file in the
historical alias tar SHA256 `23cad7163435c9d2cd51e83b9d6751db895ddbbfb3c586f1343f42f7070e9647`
also equals its rebased committed bytes; no new pack or renamed test execution is
claimed.

Quicks on this exact head passed in top-level Nix: strict TypeScript, build,
callback 26/26, both emitted type consumers, `make release-check` and
`make release-test` (31 examples, zero failures). The build left all tracked
outputs unchanged. Release tests use disposable local Git fixtures; their local
fixture tag/push messages are not actual package publication. No long local
server/WebUI run was selected for unchanged client bytes.

No database, protocol, disk or persistent-state migrations exist in the complete
feature range. Dependency/update streams and retained functional build boundaries
are unchanged from review; no superseded update or design is introduced by the
rebase. This is owner lineage evidence, **not installed `certified_equivalent`**:
substantive upstream release changes do not qualify for that driver proof.
The same retained reviewer must assess the affected final range/upstream
interaction before feature force-push and coordinator integration.

Compact exact-range evidence is under this session's `premerge/`:
`lineage.json`, `verification.json`, `range-diff.txt`, `final-series.txt`,
`final-source-delta-stat.txt`, `upstream-three-paths.diff`, `quick-summary.txt`.
Full source patches/history bundle/rebase and quick logs are under
`/tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/premerge/`.

Pending: affected reviewer acceptance, then explicitly leased feature publication
against old remote f5320eae and exact-head automatic CI. The lead will submit the
supported coordinator merge only after those gates. No force-push or default
integration has run in this preparation package.

