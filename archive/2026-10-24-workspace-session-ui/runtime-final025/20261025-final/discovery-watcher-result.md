**Result: failed as expected.** The single authorized runner invocation exited with status `1`; it reported the expected fixed-output hash mismatch for `/nix/store/fa1v6lfd0yf7ribd4y2fxc3kq2s9ijsg-dev-workspace-0.2.0-go-modules.drv`.

- Got SRI: `sha256-FxFVVTHhdpcPqDZFZfYOfAUnKIYmIdjr7u5dTixmHTQ=`
- Runner SHA-256: `ed0fa19485f0f53be508986e2e4e6467300b6be10717d8806eaa4674b4866b16`
- Checkout HEAD: `f8a282af7ceae26625366b0659ae3c43fe5d80a5`
- Before-run frozen-input and derivation checks passed. The runner’s log records exit marker `1`; full raw output is retained at [vendor-discovery.log](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/runtime-final025/20261025-final/vendor-discovery.log).
- Elapsed time: approximately 14 seconds. No process remains running and no cancellation was needed.