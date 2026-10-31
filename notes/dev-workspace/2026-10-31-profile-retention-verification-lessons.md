# Profile retention verification observations

Investigation: [2026-10-27 Codex profile generations](../../work/2026-10-27-codex-profile-generations/state.md).

- Nix 2.34.9 prints some process-root names with quotes, such as `"/proc/1906/exe"`. A filter anchored directly at `/proc/` reported zero matches despite live roots. Matching the path within the quoted output found the expected Codex executable roots. This was an inspection-filter error, not missing Nix runtime protection.
- A watcher reported a lock hash from `jq -r '.locks | @json'` after flake metadata evaluation. It differed from `sha256sum flake.lock` because it hashed compact JSON plus a newline. Independently comparing committed/worktree raw bytes and the canonical graph serialization established the same input graph. Label the serialization in receipts; do not treat different representations as source drift.
- Split host test files require helper definitions from `test/workspace_host_test.rb`. Standalone execution failed on missing constants/methods; loading the aggregate harness and filtering the assigned tests passed without changing fixtures.
- The local session-creation VM duplicated an already successful CI check. CI and local logs contained identical check and driver derivation paths at the exact source head. Retaining those identities and the complete committed input graph allowed verification reuse; the interrupted local command remained recorded as canceled, not passed.
- The configuration tools shell expects its writable worktree as CWD for Gemfile and local gem bootstrap. Starting it from the shared workspace or a read-only store checkout failed. Ordinary `nix develop` from the configuration worktree completed setup and required hooks without bypass.
