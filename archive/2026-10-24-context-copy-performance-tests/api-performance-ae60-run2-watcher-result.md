Result: **passed**. The authorized batch completed with child exit status **0** in **71.11 seconds**.

- Tested HEAD: `ae60e0fdbc892d248c1cd4bff9a52ee74a0cfc43` (tree `e83aff21574490a79282f58fc5cbe28bb2d8170b`)
- Command: `HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -euc 'make doc && (cd servers/ruby && bundle exec rspec) && make test-rust-unit && make test-documentation-assets'`
- Capture script reports the batch started and wrapper exit status 0.
- The script wrote the requested `.log`, `.exit`, `.metrics.json`, and `.started` artifacts in `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-context-copy-performance-tests/`. The exact artifact basenames are `api-performance-ae60-run2`.
- No operation remains running.

The wrapper’s completion record does not include the server/Rust example totals or an asset summary; those details are in the retained log for the parent to interpret.