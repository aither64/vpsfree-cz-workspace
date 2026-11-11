# 2026-11-10-rust-syslog-exporter

## Goal

I'd like you to rewrite syslog-exporter from ruby to rust. It should serve the same function, i.e. read messages from rsyslog and export the same metrics as the ruby code. use idiomatic rust, code formatter, best practices. use github workflows to run tests, inspiration can be taken from session 2026-10-17-confctl-rust-rewrite-plan where we're rewriting confctl to rust.

you can use maintained rust dependencies, e.g. if there's a lib for prometheus exporters.

focus is on performance, we must be able to process the messages rsyslog quicky; the ruby code is not keeping up and we're losing messages e.g. during heavy OOM situations when the log is flooded. the resulting app doesn't need to be published to crates.io. we just need it for log.int.prg.vpsfree.cz from vpsfree-cz-configuration.

suggest a solution, prepare a plan for implementation, integration into vpsfree-cz-configuration and removal of the original ruby code -- it should be entirely replaced by rust. overcommit should be replaced by an alternative solution as well.

## Affected repositories

- `syslog-exporter`: replace the Ruby application, packaging, development tools
  and Overcommit with a Rust binary and Rust checks.
- `vpsfree-cz-configuration`: package selection, rsyslog integration and the
  service on `log.int.prg.vpsfree.cz`.
- Inspect `vpsadminos` only if an existing package/module contract requires it;
  do not expand implementation scope without evidence.

## Approach

The initial proposal phase is complete. The user then authorized implementation
and preparation, explicitly requiring a stop before deploying log.int without
approval. Complete the Rust replacement, configuration preparation, independent
reviews, local builds and measured verification on published feature branches.
Default-branch integration and deployment each need separate explicit direction.
Architect owns the accepted [design.md](design.md); lead owns scope and acceptance.

Implemented solution: a single Rust binary with a dedicated ordered FIFO reader,
reusable bounded framing, indexed host routing, cached metric handles and
monotonic flare expiry. Serve Prometheus text separately with `prometheus` and
Axum/Tokio. Preserve all 18 families and the JSON/FIFO/9102 contracts. Replace
Overcommit with `.githooks` calling shared Cargo checks; replace configuration's
local Ruby package with `rustPlatform.buildRustPackage` and the Puma command with
the Rust CLI. Full interfaces, package sequence, intentional fixes, performance
targets and remaining gates are in the design.

The reference confctl session is inspiration, not authorization to access its
private records or worktrees. Use published/default project sources where useful.

## Decisions

- Preserve existing metric names, types, labels and supported parser behavior;
  inventory incompatibilities and accidental Ruby behavior before choosing any
  intentional change.
- Focus on rsyslog ingestion under OOM floods, keeping scrape work away from the
  processing path. Do not equate a language rewrite with lossless delivery.
- Use maintained dependencies, Cargo.lock, rustfmt, Clippy, tests and GitHub
  Actions. No crates.io publication is needed.
- Replace Overcommit and remove Ruby source/build/runtime dependencies from the
  exporter. Do not remove unrelated Ruby infrastructure in consumer repositories.
- User added disk management: inspect free space and session-owned Cargo target,
  temporary and benchmark output sizes; reuse outputs where useful and remove
  proven owned disposable data promptly once no longer needed. Avoid redundant
  debug/incremental artifacts. Preserve needed source/evidence/recovery data and
  other sessions' files; do not use broad cleanup or Nix-store deletion.

## Compatibility and deployment

Inventory input framing, queues, restart behavior, metric resets, expiry and all
persisted state. Plan mixed old/new component compatibility, a staged deployment
to the log host, correctness/throughput verification and a configuration rollback
that retains the old Ruby generation. Deployment and integration remain separate
future operations requiring the applicable authorization.

## Documentation

Readers: exporter maintainers and log-host operators. Current investigation and
proposal belong in this session; lasting input/metric contracts and performance
instructions are in exporter docs, and site operations are in configuration
docs. Evidence owners write ruby-contract.md and configuration-integration.md.

- [Ruby behavior and removal inventory](ruby-contract.md).
- [Configuration, package graph and rollout investigation](configuration-integration.md).

## Testing plan

Coverage includes real pinned Ruby parity fixtures, parser/state/HTTP and FIFO
regressions, formatter/lint/tests in hooks and Actions, release-mode flood
comparisons on matched inputs/resources, configuration evaluation/package/host
builds, and pinned rsyslog failure experiments. Acceptance covers count correctness,
loss observation, scrape latency and memory as well as messages per second.
Design contains targets; state and linked owner/review/verification records contain
actual commands, results and limitations. A staged production rollout is prepared
only; execution and live usability verification wait for deployment approval.
