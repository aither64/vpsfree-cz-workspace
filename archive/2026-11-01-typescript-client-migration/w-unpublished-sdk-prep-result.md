# Unpublished SDK preparation verification

- Session/workspace: `2026-11-01-typescript-client-migration` / `/home/aither/workspace/ai/vpsfree.cz`
- Tested source revision: `a9e2049f5f3445691e4025bca496e342443494f2`
- Working directory: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/vpsadmin-webui`
- Full captured output: `w-unpublished-sdk-prep.log`

| Ordered step | Elapsed | Exit | Bounded result |
|---|---:|---:|---|
| `nix develop … --command npm ci --no-audit --no-fund` | 18.2 s | 0 | Added 410 packages. |
| `nix develop … --command node --input-type=module -e '…'` (installed SDK ESM export assertions) | 1.1 s | 0 | `Installed SDK ESM exports resolved` |
| `nix develop … --command npm test -- src/lib/api/sdk.test.ts src/lib/api/sdk.wire.test.ts src/lib/api/apiRequestPolicy.test.ts src/lib/api/apiOutput.test.ts` | 10.2 s | 0 | 4 files and 38 tests passed. |
| `nix build --no-link --print-out-paths …#frontend.npmDeps` | 10.0 s | 1 | Fixed-output hash mismatch; specified `sha256-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=`, got `sha256-utOpabPprstf97qzc/yre2O/EW36u6SsfS0o2Aas36k=`. This is hash-discovery evidence, not package success. |

Stopped after the final command's nonzero status; no retries or edits. No owned process remains running.

Complete outputs recovered without rerunning from native JSONL into w-unpublished-sdk-prep-complete.log; original log contained step1 only.
