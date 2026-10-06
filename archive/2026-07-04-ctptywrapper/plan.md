# 2026-07-04-ctptywrapper

## Goal

Answer how the current Rust `ctptywrapper` behaves when osctld disconnects
or restarts, and compare it with earlier wrapper implementations.

## Affected repositories

- `vpsadminos`

## Approach

- Inspect current `ctptywrapper/src/main.rs` event loop.
- Inspect osctld console reconnect path.
- Compare with the historical Ruby `osctld-ct-wrapper` and Go prototype.

## Compatibility and deployment

Read-only investigation. No code or deployment changes.

## Testing plan

No test execution planned. Existing integration coverage was inspected for
osctld restart console behavior.
