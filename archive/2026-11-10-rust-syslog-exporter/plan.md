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
The user subsequently authorized deployment, then explicitly approved merging
both project branches, and now authorized the confirmed compatibility fixes.
Keep the essential deployed exporter serving during correction preparation;
finish checks/review and exact release verification before replacing it.
Integration remains approved for these same repositories and master targets.
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
that retains the old Ruby generation. The first Rust deployment is verified and retained as the immediate fallback
for the correction. Original Ruby recovery remains available as well.
Deployment and integration use their separately recorded authorizations;
D7 fixes and their actual final release must be verified before cutover.

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
actual commands, results and limitations. The initial deployment and live usability checks passed. D7 adds focused
ASCII/encoding parity regressions and exact-final-binary replay, a small matched
ordinary/OOM comparison and the existing two-consumer scrape smoke. Preserve
previous evidence for its unchanged scope rather than repeat the entire matrix.
Corrected activation uses rollback protection and immediate essential-service
checks followed by a bounded live window. No production synthetic alerts are
injected by the session.

## Follow-up F: flake development shell

User: "syslog-export now has shell.nix, but we're using flakes. migrate it to
flake.nix a nix develop shells." Replace only the exporter development shell and
its current entry-point documentation. Keep the existing nixpkgs718f/Rust1.95
environment, generated committed lockfile and active Git-hook guidance. No new
flake utility dependency, application/package output, runtime change, consumer
pin or deployment is needed. This is a bounded direct-lead-brief exception,
owned by I0; same independent reviewer covers the committed follow-up after
quick shell/check evidence. The merged rewrite891 must not be amended. Publish
one new feature commit; this new follow-up awaits separate merge direction.

## Addition A: routine lockfile automation without PRs

User requests full automation and sufficient verification rather than manual
routine review, explicitly prefers a custom workflow without PR noise, and says
"commit it as github-actions bot". Prepare a scheduled compatible Cargo.lock
update with its own verification gates and direct bot commits only after all
gates pass. Keep manifests/toolchain/configuration/deployment outside the routine
update boundary. Default branch advancement, no-change and failed-check cases
must fail closed or skip safely, with narrowly held publishing credentials.
Architect A settles sufficient implementation/check/recovery brief. This extends
the active source work beyond F; F remains an independently useful separate
commit and the already merged891 history is protected.

## Addition B: Dependabot with automatic merge

The latest user direction replaces custom direct commits with Dependabot PRs
that merge automatically after tests pass. Preserve A as superseded design
history; no custom publisher source was released or implemented. Architect0
revises the brief before I0 source release. Keep monthly compatible Cargo
lockfile-only updates, group routine changes, and require all defined checks
before merging, with a metadata-only privileged merge job and separate read-only
candidate verification. Prepare the exact repository auto-merge/required-check
bootstrap as part of this deliverable. No consumer pin or deployment is needed.

## Addition C: simple weekly/manual custom updater

User rejects the complicated Dependabot auto-merge workflow and directs a custom
workflow matching existing repositories: update dependencies, run tests, commit
as github-actions bot only after success; weekly and manually runnable. This
supersedes unmerged B and its never-activated settings, and does not authorize
resurrecting the older large A publisher mechanism. Architect compares a few
relevant published default workflows and records the smallest sufficient C brief.
One I0 source package will replace the rejected B stream atop independently useful
F99ff, preserving original reviewed/deployed891 and historical B evidence.

Preserve sufficient actual Rust/FIFO/HTTP/parser tests, reproducible Nix checks,
minimal credential/sandbox safety, no-change/failure and stale-normal-push behavior.
Reassess inherited custom performance/helper frameworks against this explicit
simplicity direction; internal previous designs do not expand user scope.
No Dependabot/PR/ruleset/settings/PAT, consumer pin or deployment is needed for C.
Review final committed quick-pass C before long validation; initial default
integration remains separately approval-bound. Weekly green routine bot commits
are requested without per-update human review.
