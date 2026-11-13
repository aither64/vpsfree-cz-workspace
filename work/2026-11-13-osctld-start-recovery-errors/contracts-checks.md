# Start admission, recovery contracts and verification inventory

Package E, implementer3. Read-only diagnosis against vpsAdminOS
`c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62` (worktree HEAD and local
`origin/staging` matched). Consumer comparison used canonical bare vpsAdmin
`origin/master` at `2d0946c4e699aa61092228d8a7cb275477ee46d0`, without fetching,
checking out or modifying it. This file is investigation evidence, not the final
implementation brief. No code edits, commits, builds, test runs or production
commands were performed for this package.

The supplied [incident](incident.md) establishes the reported CT1391 chronology
and successful two-command recovery; it is not an independently observed runtime
trace here. The shutdown initiator and exact early callback response remain
unproved. Package E does not diagnose the callback/import race or inspect July
session records; those are separately owned packages.

## Entry points and admission gates

Paths below are relative to the vpsAdminOS repository at the revision above.
`osctld/lib/osctld/container.rb:413`, `Container#can_start?`, evaluates these
conditions under the container's inclusive lock in this order:

| Order | Rejection condition | Existing facts available for an actionable error |
| --- | --- | --- |
| 1 | `state == :staged` | Container creation/import is incomplete; state is staged. No recovery acknowledgement is implied. |
| 2 | `state == :error` | Container is in an error state. `current_state` sets this when ContainerControl state inspection fails (`container.rb:369`); no stored detailed cause is exposed by this predicate. |
| 3 | `@recovery_tainted` | Previous recovery was incomplete. Aggregate flag is persisted; available interface records can add context, but the flag alone does not identify the failed step. |
| 4 | `netifs.recovery_tainted?` | At least one netif with `host_link_tainted?` is tainted (`net_interface/manager.rb:93`). This remains a distinct gate even when container taint is false. |
| 5 | `!pool.active?` | Pool state is not `:active` (`pool.rb:438`); report actual pool/state rather than prescribing an unconditional enable. |

Preserve the truth table, precedence, boolean API and lock behavior.
`commands/container/start.rb:83`, `Start#start_now`, checks admission **before**
the already-starting/running success return and before every start preparation
step. `force` changes the already-starting/running shortcut only. It cannot
bypass staged/error/tainted/pool rejection. The first start mutations afterward
are accounting-cgroup removal and run-configuration initialization.

| Path | Existing behavior and diagnostic delivery boundary |
| --- | --- |
| Direct `ct_start` | `Start#execute` takes manipulation lock, subscribes to events and calls `start_now`. Its admission failure is a `CommandFailed`. |
| Normal `ct_restart` | `commands/container/restart.rb:16`, `Restart#execute`, stops then invokes Start with `force: true` through `call_cmd!`; the shared rejection must survive. Stop may already have changed state. |
| `ct_restart --reboot` | Guest reboot through `ContainerControl::Commands::Reboot`; it does not invoke fresh-start admission. Preserve this distinction. |
| `ct_boot` / rescue | `commands/container/boot.rb:17`, `Boot#execute`, prepares/imports a temporary dataset, stops the container and installs next run configuration before `Boot#start_ct` calls Start through `call_cmd!` (`:139`). `--force` bypasses Boot's running check, never Start admission. Do not claim Boot is side-effect-free before admission. |
| Queued start, waiting | `Start#start_queued` -> `AutoStart::Plan#start_ct` -> Start with `queue: false`; it can forward the eventual Start result. Plan currently skips a running container, and nil/timeout yields successful `Timed out`. |
| Queued `--no-wait` | Returns queue acknowledgement before admission; eventual error cannot become synchronous command failure. Preserve and document this acknowledgement limit. |
| Automatic boot start | `auto_start/plan.rb:35-36` prefilters by `can_start?`; execution rechecks at `:111`. Blocked CTs can be skipped before Start. This is not a new error-delivery promise. |

The complete `rg can_start?` inventory is Container's predicate, Start's shared
guard and these three AutoStart plan uses. No additional predicate caller was
found under `osctld/lib` or `osctl/lib`.

## Available recovery information and safe prerequisites

There is no existing `recovery_issues` method/API field or durable list of failed
cleanup reasons in this baseline. Existing data are:

- `Container#recovery_tainted?` and `ct show`'s `recovery_tainted` export
  (`container.rb:398`, `:864`). False does not independently prove safe links.
- Configured netif `name`/`type`; veth `host_link_identity` returns recorded
  `[name, veth_ifindex, ifb_ifindex]` and `host_link_tainted?` returns its flag
  (`net_interface/veth.rb:431`, `:469`). The persisted `host_link` map has `name`,
  `ifindex`, `ifb_ifindex`, `boot_id`, `tainted` (`:77`). These are records, not
  assertions that a kernel link currently exists or belongs to this CT.
- Existing `ct netif ls` returns `veth` but omits recorded ifindices and taint
  (`commands/net_interface/list.rb:7`). `ct assets` returns asset `state/errors`
  for datasets, files and directories; those are not host-link recovery causes
  (`utils/assets.rb`, `Container#assets`).
- `Container::Recovery#cleanup_or_taint` logs individual cgroup, netif-down,
  route-cleanup and released-owner failures, then preserves/clears the aggregate
  taint (`container/recovery.rb:96`). These log strings are not persisted causes.

Errors may report these available fields and recommend inspection, with a generic
fallback for aggregate taint without matching interface detail. Do not infer a
missing link, failed cgroup step or original initiator solely from the flag.
Diagnostic formatting should not probe netlink, take links down, run recovery,
or change configuration as a side effect.

Existing maintained recovery reference is `osctl/man/man8/osctl.8.md:2627-2682`.
Its consequential safety details must survive any expansion:

1. Inspect the named pool/container and its state, netifs, relevant daemon/LXC
   logs and asset errors. `ct recover state` is an explicit recheck and can
   perform stop hooks/cleanup; it is not a read-only inspection command.
   `--no-lock` bypasses manipulation locking and is not routine advice.
2. Full cleanup of a recovery-tainted container calls `ensure_stopped!` before
   any cleanup, even with force (`commands/container/recover_cleanup.rb:18`).
   `ensure_stopped!` requires a fresh forced LXC state of stopped **and**
   nonpositive init PID (`container/recovery.rb:140`). A query error is not
   stopped proof. Partial `--cgroups`/`--network-interfaces` cleanup is not the
   full pass that clears the separate recovery taint.
3. An absent recorded host link can require explicit privileged
   `ct recover forget-host-link CT INTERFACE`. This holds the manipulation lock,
   requires the stopped proof, verifies the configured veth owner under the
   registry lock, then checks **both recorded name and recorded ifindex** for
   absence. If IFB is recorded, both IFB selectors must also be absent. A live,
   replacement or reused name/index refuses; failed kernel queries refuse.
   It deletes no kernel links (`Recovery#forget_host_link`,
   `Veth#forget_absent_host_link!`, `veth.rb:438`).
4. Only after a justified acknowledgement, run full `ct recover cleanup` to
   finish cleanup and clear the aggregate taint. It preserves unrelated
   configuration/runtime errors. Matching live links belong to ordinary
   identity-checked cleanup; mismatched/reused links require diagnosis, never
   blind deletion or a suggested force bypass.

The supplied CT1391 acknowledgement followed by full cleanup succeeded, but that
does not make this sequence unconditional advice for every tainted container.
Recovery needs neither a node reboot, draining other CTs nor hand-editing daemon
YAML. Start's force flag does not authorize any of these recovery operations.

## Error envelope and consumers

`commands/base.rb:76`, `#call_cmd!`, forwards a failed subcommand's message
verbatim using `error!`; `#error!` raises `OsCtld::CommandFailed` (`:135`).
`generic/client_handler.rb:175-201` converts this to the existing newline-JSON
failure envelope `{status: false, message: String}`. Unexpected exceptions yield
`internal error`, so diagnostic code must remain safe for known gate states.
No structured code, payload or protocol version is needed for richer wording.

`osctl/lib/osctl/client.rb:111-135` raises `OsCtl::Client::Error` with that same
message from bang response/data methods. `cli/command.rb:23-55` uses those for
ordinary `osctld_fmt` calls; `--json` controls successful output formatting, not
a replacement error envelope.

Baseline foreground start/restart/boot (`cli/container.rb:364`, `:444`, `:989`)
only checks `Response#error?` and closes the console; it discards the diagnostic
message. Lead explicitly added a minimal CLI propagation correction plus
regression to package A after this finding. Implementer0 owns those edits;
architect0 owns the settled brief. Existing raw JSON console mode also does not
invoke the operation block (`open_console_raw`); no asynchronous/console rewrite
is part of package E or its recommendation.

At the vpsAdmin comparison revision, `libnodectld/lib/nodectld/utils/osctl.rb`
shells `osctl -j`; `vps.rb:21-41` uses start/restart with infinite wait and
`commands/vps/boot.rb:6-20` uses force for rescue boot. Failure is process status
and captured command output: `Command#safe_call` records `cmd`, `exitstatus`,
and bounded `error` output (`command.rb:527`). Complete committed-tree searches
for `start not available`, `recovery_tainted` and `ct_recover` found no consumer
matches. This supports changing free-form wording without a consumer update;
it does not prove the behavior of uninspected/deployed consumer versions or
external scripts. The local exact old-message assertion is
`osctld/spec/osctld/commands/container/lifecycle_spec.rb:98`.

Compatibility: a message-only change retains state/YAML and socket schemas,
existing gates, mixed userspace operation and rollback loading. No coordinated
all-node update or vpsAdmin source change follows from this inventory.

## Minimal regression and check plan for implementer0

Reuse existing fixtures/suites, rather than introducing a parallel test package:

| Existing source | Meaningful addition/reuse |
| --- | --- |
| `osctld/spec/osctld/container_spec.rb` | Existing staged/error/inactive pool and taint provenance tests. Add each gate's diagnostic and precedence; include netif-only taint and generic aggregate-taint fallback. Preserve boolean success for eligible CT. |
| `commands/container/lifecycle_spec.rb` | Replace generic error assertion; reject before accounting/init/mount/spawn with force both false/true and with starting/running state. Preserve eligible no-op. Reuse restart delegation and boot fixtures to prove shared message survives subcommand propagation. |
| `commands/container/start_spec.rb` | Existing impermanence preparation regression remains valid; do not duplicate it merely to test wording. |
| `container/recovery_spec.rb`, `net_interface/veth_spec.rb`, `commands/container/recovery_and_send_spec.rb` | Existing stopped/init proof, four name/index selector refusals, query failure, unrelated `:error` retention, aggregate-taint cleanup and force ordering. Reuse them to protect safety; no new cleanup implementation is requested. |
| `generic/client_handler_spec.rb`, `osctl/spec/osctl/client_spec.rb` | Existing socket failure-envelope and bang-method message tests. One representative rich message through real forwarding is sufficient; no new protocol suite. |
| `osctl/spec/osctl/cli/container_spec.rb` | Minimal foreground regressions should prove the message is visible and failure status survives start/restart/boot, with existing console handling preserved. Lead/architect settle the exact shared helper approach. |

Candidate focused commands below are **planned, not executed by E**. Run in the
owning worktree with its prepared dependencies/native extensions. Component Nix
shells derive `BUNDLE_GEMFILE` from CWD, so enter the component directory first:

```sh
(cd osctld && nix develop ..#osctld --command bundle exec rspec \
  spec/osctld/container_spec.rb \
  spec/osctld/commands/container/lifecycle_spec.rb \
  spec/osctld/commands/container/start_spec.rb \
  spec/osctld/container/recovery_spec.rb \
  spec/osctld/net_interface/veth_spec.rb \
  spec/osctld/commands/container/recovery_and_send_spec.rb \
  spec/osctld/generic/client_handler_spec.rb)
(cd osctl && nix develop ..#osctl --command bundle exec rspec \
  spec/osctl/client_spec.rb spec/osctl/cli/container_spec.rb)
nix develop --command overcommit --run
```

Shell/dependency preparation and uncertain-duration checks need the installed
monitor workflow; E has not launched them. Component shells are declared in
`flake.nix:454-617`; the canonical CI preparation script is
`.github/workflows/scripts/run-rspec-all.sh` (bundles per component and prepares
libosctl/osctld/ruby-lxc extensions). Its full invocation, when required by lead:

```sh
nix develop .#vpsadminos -c env GITHUB_WORKSPACE="$PWD" \
  bash .github/workflows/scripts/run-rspec-all.sh
```

Do not run all suites solely because this inventory names the script. Baseline
flake checks at `flake.nix:753` contain OS/storage checks, not a separate Ruby
RSpec output; do not invent a `checks.*.ruby` target or use full flake check as
the focused gate. Hooks remain mandatory; implementer0 alone owns their setup
and the index/commit window. For changed man prose, use osctl's declared md2man
Rake tasks from `osctl/Rakefile` and inspect rendering; MkDocs `make doc` does not
validate the osctl man page.

After intended commits, hooks/quick checks and mandatory independent final
review, the smallest relevant packaged VM regression is:

```sh
./test-runner.sh test osctld/resilience
```

`tests/suite/osctld/resilience.nix:160-199` already exercises lost host-link
ownership, refusal on live/reused link, explicit acknowledgement, full cleanup
and subsequent successful start. Extend its error assertion if packaged CLI
coverage is needed. It is registered at `tests/all-tests.nix:281`.
`osctld/restart` covers daemon/client continuity, while `osctld/direct-start`
covers unmanaged LXC starts; neither is necessary solely for diagnostic wording.
Select those only if final accepted race/entry-point edits affect their behavior.
Use a fresh watcher for VM tests and stop an unexpected local kernel build under
workspace verification policy. No long checks are authorized for package E.

## Evidence and handoff

Executed inspection consisted of `dev-session current` plus environment binding,
same-session roster check, `git rev-parse`, bounded `rg`/`sed`/`cat` source reads,
and `git --git-dir=repos/vpsadmin.git show/grep` against the exact ref above.
Source and docs were read; no test success is claimed. The evidence gaps are
runtime consumer version, final diagnostic wording/implementation, and future
quick/long test results. The callback response and shutdown intent remain with
the incident/race investigation owners.

Findings were sent directly to architect0 and implementer0; lead owns acceptance,
state/manifest links and any tracking commit. Package E's sole changed path is
this file. Capacity is available after reporting this package for acceptance.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-osctld-start-recovery-errors/)
