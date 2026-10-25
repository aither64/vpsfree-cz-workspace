# 0.30.1 version preparation stopped

The sole maintained `make version VERSION=0.30.1` invocation exited2 at its offline `uv lock` step. The new owning uv cache does not contain registry metadata for `ruff==0.17.1`; the error mentions a supported-Python>=3.15 resolution split. No dependency constraint or supported Python change is inferred. The original command, environment binding, stderr and partial effects are retained.

Exactly12 intended version paths changed before the failure: VERSION, four Ruby version constants, four JavaScript metadata/markers, two PHP files and Python pyproject.toml. Read-only comparison proves only their expected version fields changed. All other tracked files remain exact. Python uv.lock and the Rust lock remain at0.30.0. The approved changelog candidate was not applied.

HEAD remains8591394e, with empty index, no nonignored files and all refs unchanged. Held root7c48, tool root450de and Rust7f51 locks remain exact. No Git commit/push, source workaround, retry, installer, test/compiler campaign, utility, claim or lifecycle action occurred. No process/operation remains; slot is free. The partial12 state is frozen pending a bounded lead-directed cache recovery and resume package. It is not the stable19path input required for owner1's later Python setup.

Lead report7ef5ecc2 and owner1 noticea9e3cf32 were delivered. Owner1 is asked to hold later physical Python setup and route cache diagnosis through the lead. No user permission is requested.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/)
