**No Blocking or Important findings. One Advisory finding:**

- **Advisory — General/testing:** [restart.nix:379](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-23-stable-kernel-update/vpsadminos/tests/suite/osctld/restart.nix:379), commit `a9ec316a0dbb`: failed readiness, baseline or EOF assertions leave the sampler job running without an `ensure` cleanup. Until the enclosing shell timeout expires, it can occupy `client` and cascade into later examples. Retain an exact guest process handle and terminate/reap that process and join its job on failure, preserving the original assertion.

Reviewed all four lanes for exactly:

`82866bedb4b80b4368faaec1cbf1b0f032ef3058..a9ec316a0dbb640839b7e1ec8709d5552b08ea81`

The Git series and final diff match both supplied exports byte for byte: two commits, 13 files, +293/−42.

- **History and scope:** Two sound logical owners: `b524d53b6f39` owns kernel selection; `a9ec316a0dbb` owns JSON termination, cleanup, tests and documentation. No obsolete approaches, follow-up fix residue or repeated update streams remain in this range. **No migrations.** The old OS candidate remains outside the reviewed series on its backup ref.
- **Kernel linkage:** The staging loader and all nine existing catalog records are preserved. Stable selects `.119`; unstable and explicit `.118` remain available. Linux revision `36574eefad15c11d26ad7adb0b8e15e6bcfe2ec5` and ZFS identities match the previously reviewed inputs. Independently hashing the stored archive reproduced the catalog’s SRI. Built-in/external ZFS retain the kernel patch; userspace retains the same source without it. Publication is supported by the existing receipt; I did not re-query the remote ref.
- **Architecture and behavior:** The model owns sticky loss state and wake-up; the exporter checks before acquisition/publication, restores `USR1`, and returns through normal CLI error handling. Cleanup stops owned workers and closes connections. Ordinary partial samples and the TUI remain supported. No speculative reconnect framework or consumer changes were added. Unrelated blocked I/O can still delay termination.
- **Compatibility:** At vpsAdmin `4062a8da3314`, `nodectld` already reaps and relaunches on EOF; its lock pins OS `e9d55bada43c`. `osctl-oomd` likewise invalidates input and relaunches. No new argv or coordinated fleet update is required. Older producers retain the recovery gap; unsupervised readers must handle EOF and establish a fresh epoch/baseline.
- **Documentation:** The manual owns the stream contract; the README/MkDocs-reachable administration guide explains recovery. Both agree with the implementation. Existing kernel guidance preserves module, pool-format and rollback constraints. No consequential guidance was removed or misplaced.

Remaining verification: exact final-head closure build, ordinary seven-example restart suite, stable NFS and both ZFS modes, packaged `nodectld` recovery with existing/new VPSes, and final-head CI. The reported 81/0 specs and quick checks were **not rerun**; old-lock VM results do not establish final-head success.

Read-only review complete. No builds, tests, exploit reproduction, delegation or mutations performed.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-23-stable-kernel-update/)