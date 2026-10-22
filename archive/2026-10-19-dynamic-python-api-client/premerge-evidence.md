# HaveAPI premerge evidence

- Session: `2026-10-19-dynamic-python-api-client`; verified identity and retained implementer1 workspace_write.
- Exact feature: `c1823f3d70365b0442d0e2171bdf83bd4c6dbe31`; tree `aec5847f4c735ac68a7b6158c76a4f667f6a6a18`.
- Fetched origin/master and merge-base: `c58704a08451a231fdf6c6123437133422af46dc`; baseline unchanged, no rebase needed.
- Canonical SSH origin: `git@github.com:vpsfreecz/haveapi.git`; remote feature matches exact local head.
- Worktree/index clean; diff --check passes.
- Final diff: 62 files changed, 10539 insertions(+), 17 deletions(-).
- Final binary diff SHA-256: `3f0427fc7897efd21b7b5c261eee70d0cad99e28cad2931f04a4ae144781b1bd`.
- Eight logical commits below match the independently reviewed deliverable and later accepted docs-only addition.
- No obsolete/fixup commits, repeated dependency streams or unsupported migration lineage in final ancestry. Original corrections folded into owners; separate docs follow-up has explicit user purpose and independent review.
- NO MIGRATIONS: no schema/persisted server format/state transition; no feature version released/deployed/externally consumed that requires retaining intermediate heads.
- Existing exact-head verification/review retained; no runtime checks repeated and no source changes during premerge.
- capture-comparison succeeded with exact base/head before coordinator integration.
- User approval: "okay, i've created account and added a pending publisher. you can merge the client, but let's not make a release yet."
- Scope: HaveAPI refs/heads/master only through catalog coordinator; no direct merge/push performed. NO RELEASE, tags/version/registry/environment changes.

## Complete base-to-head series

- `9530f371885ef7a8c64b17efd6e77ed6fc743784 clients/python: package clients and document dynamic API usage`
- `ef5af18b93a9aa88cc98ce32449f5c25fd749425 clients/python: add immutable HaveAPI protocol core`
- `4787ad22e3071bf699b6b86bb93edafe99b230cb clients/python: add responses, paging and operations`
- `69699d9c5ca4afe5482fc7b4c1fffe70d73e9760 clients/python: add dynamic clients and authentication`
- `5363633fbfb5b6c1648a6b32dda30fc3b4d4f8c4 clients/python: add guarded vpsAdmin compatibility bridge`
- `87172afb48f475c037ed421d31816974e2ff13e9 clients/python: add VPS examples and public fixture`
- `326c05b78cec149b81e2c516c5cdcb7d1810d678 release: include Python packages in trusted publishing`
- `c1823f3d70365b0442d0e2171bdf83bd4c6dbe31 clients/python: explain the vpsAdmin example context`

## Retained independent evidence

- [review.md](review.md), SHA-256 `85ae6c8f88a1542990b9b542e1c06de2913ad4d1f7edfa2742e40beca7ce0038`.
- [review-followup.md](review-followup.md), SHA-256 `2239233b7ad389dac38cfb309f7d7042c6a7231ce0fedd5b8682497c67f12afc`.
- [token-review.md](token-review.md), SHA-256 `8976f9063727cdeb29a75aee701aaea1132664a8a82385e51d3cc16e4b60a6bb`.
- [readme-context-review.md](readme-context-review.md), SHA-256 `50122f7459f7994ec5d0dac8f32b38eed8f49843e13e0127d9d18802586fd54d`.
- [merge-review-receipt.json](merge-review-receipt.json), SHA-256 `248e9d1a7b358f63cee1c090bf6774586ae79ecc5e9b2810fdfed68ee122a0d8`.

Coordinator submission remains owned by the lead. Recovery refs and original stash preserved.
