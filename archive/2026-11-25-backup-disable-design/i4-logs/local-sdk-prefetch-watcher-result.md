**Result: failed** — the single prefetch command exited with status 1 after 4.7 seconds. No retry or diagnosis was performed.

- Revision: `c723f2fab261153eddf7bee0cc967e5392836efe`
- Command: `nix develop --command prefetch-npm-deps package-lock.json`
- Lock and manifest hashes matched the frozen inputs before and after.
- Measured SRI hash: unavailable.
- Raw log: [local-sdk-prefetch.log](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i4-logs/local-sdk-prefetch.log)
- Evidence: [status JSON](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i4-logs/local-sdk-prefetch-status.json) and [watcher result](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i4-logs/local-sdk-prefetch-watcher-result.md)

The command’s bounded log excerpt reports `couldn't fetch ... vpsadmin-typescript-client-0.6.0.tgz: invalid format`. The command session is terminal and joined.