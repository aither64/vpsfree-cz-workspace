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

This phase produces a proposed solution and an executable implementation plan.
It does not change application code, configuration, production or default
branches. Establish the Ruby input/metrics contract and actual consumer graph,
then choose a small Rust design with measurable burst throughput and explicit
backpressure and loss semantics. Architect owns [design.md](design.md).

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

## Compatibility and deployment

Inventory input framing, queues, restart behavior, metric resets, expiry and all
persisted state. Plan mixed old/new component compatibility, a staged deployment
to the log host, correctness/throughput verification and a configuration rollback
that retains the old Ruby generation. Deployment and integration remain separate
future operations requiring the applicable authorization.

## Documentation

Readers: exporter maintainers and log-host operators. Current investigation and
proposal belong in this session; lasting input/metric contracts and performance
instructions will belong in exporter docs, and site operations in configuration
docs. Evidence owners write ruby-contract.md and configuration-integration.md.

## Testing plan

Plan parity fixtures from the existing Ruby implementation; parser/state/HTTP and
real rsyslog transport tests; formatter/lint/tests in local hooks and Actions;
release-mode flood benchmarks against Ruby on the same corpus and hardware;
configuration evaluation/build and a bounded staged rollout. Acceptance must cover
count correctness, queue/loss observation, scrape latency and memory as well as
messages per second. Exact commands and thresholds follow inspected evidence.
