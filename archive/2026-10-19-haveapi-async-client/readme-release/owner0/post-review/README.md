# Prepared installed npm release smoke

Prepared only. Do not launch before final committed review and lead release.
The script binds docs head `349aacd53790c6c820fe2dacc8cb6d151c92d0fc`, tree
`c80eaddb6e42633d154c15b020e4e74b9faa8d76`, the normal Nix lock and existing
client/compiler/tool inputs. It requires a clean checkout before and after.

After release, one fresh retained-catalog Luna/low/full-access watcher owns this
single command from the HaveAPI worktree:

```sh
export OUT="$(mktemp -d /tmp/2026-10-19-haveapi-async-client-release-smoke.XXXXXXXX)"
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-haveapi-async-client/readme-release/owner0/post-review/smoke.sh
```

The script enters ordinary top-level `nix develop`, builds the client, packs once
with `npm pack --ignore-scripts`, copies the matching browser bundle and calls
the actual `Artifacts.smoke_npm` helper. That helper installs the retained tar
normally in a private temporary consumer, scripts disabled and NODE_PATH unset,
then checks package-name CommonJS exports and pinned TypeScript consumption.
No npm ci, multi-language release build, registry write or WebUI operation runs.

All 51 packed files must equal their final committed blobs. Runtime plus all 44
declarations must equal committed f94; only README bytes may differ. The output
retains exact tar SHA256/integrity, per-file inventory, script/hash, tool/input
hashes, head/tree/status before and after, command tracing, complete operation
and phase logs, explicit phase/overall exits and elapsed time.

Stop at the first failure; no watcher diagnosis, retry or source changes. Report
any unexpected local kernel compilation promptly and stop only this owned run.
Do not remove the retained output. Parent reconciles raw evidence and cleanup
state after completion. The WebUI vendored f94 archive remains unchanged.
