# Consumer refreshes for approved default integration

Preparation only. The lead owns claims, default merges and default pushes. Both
feature publications remain held for the focused independent review. Provider
`822c0e35dbe2549111912f539116b4225dfd3035` and all CI-tool references are unchanged.

| Repository | Reviewed old range | Current target | New local head | Sole adoption patch ID |
| --- | --- | --- | --- | --- |
| HaveAPI | `7ac977a26080d45d44b6608aafad2cadd2ec7f81..c7bfc1aa5af956b6057be8e623f9035c00ccb268` | `1103a3a14b1dc6dec17fc4859df80220a54f111d` | `39909094649b1d14a23f00615775ca7136acf4fd` | `d22c8e70feffbfdd7a216261e41f4ca6606aea66` |
| vpsFree configuration | `50d263d4127c05163d660fae1c4b9b887584032d..5f0f4466adb175ed4fcac9b6d5c8909e87a1fec1` | `bec5556f6c60414e482550dd735321ebe3c3703b` | `25258cd3f483f0116dbab35c7acf89b16eff4bbc` | `70ac780217da706413949a74c988a1050dd5a25b` |

Each range contains exactly one adoption commit. Both range-diffs report `=` and
both ordered stable patch IDs equal their reviewed predecessors. The final trees
equal the clean `git merge-tree` reconstructions exactly. Both repositories are
clean; neither has an active rebase or owned command. The old feature heads remain
in `refs/backup/2026-10-24-flake-update-downgrade-guard-replacement/before-default-integration-refresh`
and on their remote feature refs. There are no migrations or obsolete pin/fixup
commits. Earlier execution receipts retain their original source identities and
are not presented as executions of these new heads.

HaveAPI changes the same three feature paths. All 769 other tracked entries match
the new target. The upstream library-lock deletions, release-tool changes, hook
configuration and both development-document changes are preserved. `flake.lock`,
`flake.nix`, `Gemfile`, AGENTS and custom hook code match all old/new revisions.
The workflow and updater helper blobs equal the reviewed feature exactly. The
development page combines the upstream release/Rust paragraphs with the unchanged
guard/cache instructions. Its final tree is
`60ca6e54445da84bc0e6549a7a172a5dbddb07a0`.

HaveAPI passed its nine nonpublishing shell fixtures, YAML/Bash/cache checks
(14 modeled scheduling cases and two negative controls), helper syntax, diff
checks and ordinary pre-commit/commit-message hooks. The first rebase paused at
the normal Overcommit trust gate for the inspected upstream hook configuration.
Normal signing and the original message through `git commit -F` completed it;
no hook was bypassed. Original advisory text-width warnings were retained.

vpsFree configuration changes only the same workflow, byte-identical to the
reviewed feature. All 471 other tracked entries match the new target. The entire
upstream lock is preserved byte for byte. Only the upstream `devWorkspace` and
`codex-web` nodes changed; their exact old/new metadata is retained in
`vpsfree-cz-configuration/upstream-lock-analysis.json`. Root wiring, confctl and
nixpkgs owning inputs, the tools-shell source, Gemfile/lock, guidance and hook
configuration are unchanged. The changed nodes are outside the confctl input
closure. Its final tree is `31a86081ee586a0e6e08dad67b7539744ed0cf73`.

vpsFree configuration passed its 12 nonpublishing workflow fixtures, YAML/Bash/
cache checks (14 modeled scheduling cases and two negative controls), diff checks
and ordinary hooks. The fixture command unexpectedly took 67.54 seconds including
the tools shell; it completed successfully, with no live update/build/kernel.
The following static command completed in 13.64 seconds. No additional test was
launched after that duration was noticed. Original advisory text-width warnings
were retained.

Per-repository `local-source-inventory.json` files bind full ranges, blobs, tree
preservation, checks and checksummed artifacts. Their adjacent full-index binary
diffs, complete series, range-diffs, upstream diffs and command logs are retained.
Native final comparisons were captured for both exact new ranges. The first
vpsFree capture returned the ordinary session-writer busy refusal; a single later
retry succeeded without changing either source.

The two clean detached targets are under the session worktree group as
`integration-haveapi` and `integration-vpsfree-cz-configuration`. Fresh dependency
and hook preparation is a separate prepared operation, not yet executed by the
owner. No extra project documentation is needed for an equivalent history refresh.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
