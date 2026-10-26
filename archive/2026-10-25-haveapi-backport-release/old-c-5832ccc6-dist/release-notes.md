# Sun Oct 25 2026 - version 0.30.2
## Ruby server
- Reduce copying when deriving documentation contexts while preserving isolation
  from caller-owned data.
- Add regression tests and benchmarks for documentation rendering and API
  endpoint performance.

## Rust client generator
- Normalize only the selected documentation data instead of traversing the
  complete schema for each example.

## Development tooling
- Add paired endpoint performance checks with fixed regression budgets in CI.
- Reject automated Nix input updates that cannot prove forward ancestry.
