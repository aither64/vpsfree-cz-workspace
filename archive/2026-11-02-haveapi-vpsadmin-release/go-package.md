# Go client package B: complete, no code change

The released HaveAPI 0.32.2 generator reproduces all **682 generated Go files**
byte-for-byte. Two fresh generation trees and regeneration in the owned worktree
are identical to the existing client. Added/changed/stale paths: **0/0/0**.
The lead accepted the conditional no-release conclusion: no v0.2.0, project
commit, release prose or publication is needed. Formatting and compilation pass.

## Final branch, history and remote proof

- Owner: implementer1, verified session
  `2026-11-02-haveapi-vpsadmin-release` in
  `/home/aither/workspace/ai/vpsfree.cz`; `dev-session current` and both
  environment markers agree with the trusted thread binding.
- Repository: `git@github.com:vpsfreecz/vpsadmin-go-client.git`, target `master`.
- Registered branch: `2026-11-02-haveapi-vpsadmin-release`.
- Worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-haveapi-vpsadmin-release/vpsadmin-go-client`.
- Initial base = final feature head = freshly fetched `origin/master` = remote
  `refs/heads/master`:
  **`134a9e69f9aa6ddec5c94b53744865c6f81ecdd0`**.
- Fresh SSH fetch/ls-remote and ancestry proof completed immediately before
  `2026-11-02T22:12:10Z`. `git merge-base --is-ancestor HEAD origin/master`
  exits 0. The complete base-to-head range contains zero commits; its diff and
  the staged/unstaged diffs are empty. Working tree is clean.
- Whole-history conclusion: no new or superseded commits, dependency update
  streams, transitional behavior or migrations. No migrations were created,
  changed, deployed, released or externally consumed by this package.
- `capture-comparison` with implicit refs refuses an unavailable comparison
  base; an explicit exact base/head pair also refuses because they are identical.
  Zero-range portal comparison is unsupported; the exact range is recorded here.
- No merge claim is needed for this no-op branch. No integration, tag push,
  package publication, deployment, branch/worktree removal or session lifecycle
  action occurred. The lead confirmed routine evidence needs no standalone
  change review. The worktree and branch remain available.

Fresh tag and module-proxy checks show only `v0.1.0`; its annotated tag object is
`54a265db8d133cfebd58fb27a38dfdd5e5bba279`, peeled to the same final head.
Existing supported client behavior/runtime pairing, module import path and
`go 1.16` directive are unchanged; no dependency was added.

## Exact generation inputs

- HaveAPI tag `v0.32.2`, annotated object
  `7f8f656ca7655bafaf2cf5e7095573806085a442`, peeled source
  `1ef9b204ba45bb261d3334be5c555cc1856b713b`, source tree
  `fda4d5c159746ffa91887ead63197e7b788e0a64`.
- Detached input checkout:
  `worktrees/2026-11-02-haveapi-vpsadmin-release/haveapi-go-tools`.
  This is tooling only, not a HaveAPI feature registration. Tracked source is
  unchanged. The inherited post-checkout hook's signature refusal happened after
  checkout; exact head/clean tracked tree reconciled its effects, with no hook
  bypass or shared signature change. The Go client declares no hook framework;
  `core.hooksPath` is unset and its hook directory contains only samples.
- Publication receipt: lead confirmed run `41529223599`, attempt 1, succeeded.
  Public [release manifest](https://github.com/vpsfreecz/haveapi/releases/download/v0.32.2/release-manifest.json)
  retained as `go-evidence/release-manifest.json`, SHA-256
  `7c53624cc059434279e6eba6f8a9ec151a57897f41e96f0b1d261e1b58fa728b`.
- Exact released Go component lock was restored into the owned checkout and
  installed frozen, with isolated gem/bundle directories. Retained lock:
  `go-evidence/generator.Gemfile.lock`, SHA-256
  `f75dfbefc8ced373a643517b9a416ac8886695b9ac74e2cf8bd2eabd0be1afc5`;
  unchanged after setup/generation.
- Loaded generator and shared Ruby client: **0.32.2**, Ruby **3.4.11**.
  Shared-schema source SHA-256:
  `d704e6c155f9f2ec82bdf627857bdc23aa08a1d2133806df1f8ed5beb2d8c439`.
- Capture: unauthenticated public OPTIONS from
  `https://api.vpsfree.cz/v7.0/` at `2026-11-02T22:07:54Z`, API **7.0**,
  protocol **2.0**, profile **public**, mount `/`. Sanitized schema reviewed;
  151 application resources/519 actions plus one token-auth resource/5 actions.
  No credentials were used. Retained schema `go-evidence/schema-api-7.0.json`,
  SHA-256 `b588b42f5b431e3707c6f919baa46d4a105474780a3780ff102dbb8c746aa2fa`.
- Generation command: `haveapi-go-client generate --schema <saved-schema>
  --api-version 7.0 --output <client-dir> --package client`; **no `--module`**.
  Both fresh roots copied the original `go.mod` unchanged. Worktree `go.mod`
  SHA-256: `b6512dde7aae8cef8a81d4e3630db5194e851338c0abf2acb7b2f016b7173e2a`.
- Formatter/compiler: repository `nix-shell`, Go **1.26.8**. Generation also
  explicitly used this Go executable. Nixpkgs resolves to
  `/nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source`;
  Go executable `/nix/store/h3rc4y3szd0391wryw9hslrijdvni030-go-1.26.8/bin/go`.

## Verification and retained evidence

| Check | Result | Evidence under `go-evidence/` |
| --- | --- | --- |
| Frozen isolated tooling setup | Pass, exit 0, 44s | `tool-setup.log` |
| Explicit public saved capture | Pass, exit 0, 24s | `capture-public.log`, `schema-provenance.json` |
| Two fresh generations | Pass, exit 0, about 19s; identical | `generate-fresh.log`, `generation-watch-result.md` |
| Generated file comparison | 682 equal; added/changed/stale 0/0/0 | `generation-comparison.json` |
| Owned worktree regeneration | Pass, exit 0; identical to both fresh trees | `generate-worktree.log` |
| `gofmt -l client` | Empty | `quick-checks.log` |
| `go test ./...` | Pass; package compiles, no test files | `quick-checks.log` |
| Diff/index/cleanliness checks | Pass, exit 0 | `quick-checks.log` |

Complete source/input graph: `go-evidence/tool-inputs.json` retains the exact
source tree and 81 generator/shared-client/input file hashes. Generation output
hashes are in `generation-comparison.json`. These raw artifacts are untracked,
disposable session evidence; this Markdown retains the exact identities.

Uncertain operations used fresh Luna/low verification utilities under retained
catalog `495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`,
with native/CLI execution `danger-full-access`, approval `never`. The final
compile watcher passed in 23 seconds. No watcher/process remains running.
No optional tests or long CI wait ran. No project documentation update is useful
because generated code and supported behavior did not change.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-haveapi-vpsadmin-release/
