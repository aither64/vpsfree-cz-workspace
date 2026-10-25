# Native publish archive repair: committed for affected review

The helper and workflow fix is committed at `b6f84679d33ff041388535dcf4dc060aeb0d1b9d` (tree `01d683f0c21ba447b8eb2d6ada3eaed68da87cbc`). The worktree/index are clean and source/runtime ownership is yielded. The public `v0.1.0` tag and all three prior published commits remain unchanged.

[receipt.json](receipt.json) records the exact five paths, 18 passing synthetic/stub helper cases, syntax checks and unchanged 686 generated Rust/runtime/schema/pin proof. [repair-only.diff](repair-only.diff) is the affected source delta; [complete-history.txt](complete-history.txt) and [complete-base-to-head.diff](complete-base-to-head.diff) cover the complete ff876-to-head series. There are no migrations, repeated pin streams or obsolete intermediate fixes. The original public commit boundary requires retention.

The helper captures the guarded native Cargo scratch archive synchronously before validation, preserves bytes or absence and native exit on failures, and binds candidate/actual content, source, root lock and tools. Workflows keep the protected credential timing and retain failed reports. The lead finalized the development documentation. Fixture quicks are not native Cargo acceptance. No compiler/package/dry-run/generation/API/push/tag/registry effects were run.

Affected final review comes next. A separately authorized, fresh-watcher actual SDK candidate dry run must then prove the scratch contract with the retained release-run lock. Public-tag recovery remains a lead-owned explicit decision; no version or tag movement was chosen.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/)
