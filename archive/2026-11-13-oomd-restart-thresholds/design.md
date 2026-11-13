# node25.prg osctl-oomd thresholds

## Decision and release boundary

Package D is ready for lead acceptance and implementation dispatch. Set
`restart_hits = 4` and `load_multiplier = 1.5` only on node25.prg. The lead relayed
the user's explicit 1.5× choice; it supersedes the initial 1.8 proposal. At an
identical median this lowers the activation threshold by 25% from its current
2.0 multiplier. All other selection criteria, sampling and stop behavior remain
unchanged. No design blocker remains for this configuration edit.

Architect0 owns this design record. Lead owns plan/state/portal and release
acceptance. Implementer0 is the intended sole owner of package I after lead
dispatch. No application edits, commits, deployment, repository claims or machine
reservations were made during D. Live configuration was not read; the baseline
below is established from configuration and its pinned daemon source. The user
explicitly limited this task to configuration changes in
`vpsfree-cz-configuration`; no node access, live checks, deployment or machine
claims are in scope. An unverified running baseline is not a blocker to this
configuration package. Deployment/recovery notes below are operator context for
a separately authorized future operation only.

## Source evidence and current behavior

Initial inspected configuration `origin/master` was
`d0674cc68ed2cb1c71606caa50fe31227ea3521a`. Before implementation, the lead's fresh
base advanced to `1a948a872f84bdb4643926b357cf15534de1d313`; only `flake.lock`
changed between these configuration revisions. Architect0 rechecked the relevant
daemon and module contracts at the refreshed pin below. The bare repository's
local `master` was older; use the lead-prepared current feature base rather than
that stale local ref.

Node metadata in `cluster/cz.vpsfree/nodes/prg/node25/module.nix` selects the
`production` channel, mapped by `flake.nix` to `vpsadminosProduction`. The initial
lock selected vpsAdminOS `2abbe3cc1c102a4b39022d3f73ef4a432ad4d616`; the current
implementation base selects `c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62` and
`vpsadminProduction` `2d0946c4e699aa61092228d8a7cb275477ee46d0`.
Node25's `config.nix` has no oomd override. The inherited
`cluster/cz.vpsfree/nodes/common/all.nix` enables `osctl.oomd` and sets only
`settings.verbose = true`.

The pinned `os/modules/osctl/osctl-oomd.nix` accepts freeform JSON settings and
passes the generated `osctl-oomd-config.json` to the runit service with
`osctl-oomd --config`. `os/overlays/osctl.nix` selects source-built oomd gems
from the pinned repository, so the inspected Ruby source determines this
configuration's daemon behavior.

The old-to-new vpsAdminOS comparison is byte-identical for `cli.rb`,
`host_load.rb`, `watcher.rb`, `ct_top.rb`, the oomd Nix module, `os/overlays/osctl.nix`
and `os/packages/ruby-source-gem-config.nix` (`git diff --exit-code` passed).
The only oomd implementation change is in `killer.rb`: a queued miss for a
missing/pruned container is now ignored instead of creating an empty record.
Its new specs cover that race and preserve existing counter/threshold behavior.
The packaged `io-console` dependency advances from 0.9.4 to 0.9.5. These changes
do not alter this brief's options, defaults, load gate, hit/stop thresholds,
counter resets or state format. This is a focused contract check, not a claim
that the complete old and new OS inputs are equivalent. A separately authorized
future deployment would need its own live-baseline comparison. No configuration
pin is changed by package I.

| Setting | Current effective source default | Intended node25 value |
| --- | --- | --- |
| `restart_hits` | 8, derived as `120 / interval` | 4, explicit |
| `load_multiplier` | 2.0 | 1.5, explicit |
| `interval` | 15 seconds | Unchanged |
| `stop_hits` | 40, derived as `600 / interval` | Unchanged |
| `memory_percent` | 95 | Unchanged |
| `cpu_percent` | 90 | Unchanged |
| `load_top` | 5 | Unchanged |
| `verbose` | true from shared configuration | Unchanged |

Relevant files under the pinned `osctl-oomd/lib/osctl/oomd/`:

- `cli.rb`: merges configuration into defaults, then derives unspecified restart
  and stop hit limits from the final interval. Explicit `restart_hits` does not
  change `stop_hits`.
- `watcher.rb`: samples host **one-minute** load; activates when that load is
  **greater than or equal to** `median * load_multiplier`. This is neither a
  fixed absolute load threshold nor a threshold scaled by the CPU count. The
  latest sample is included in the median before comparison.
- `host_load.rb`: keeps at most `86400 / interval` samples, or 5760 at 15 seconds.
  This is approximately 24 hours of continuous sampling, with a shorter history
  during initial collection. Samples have no timestamps, so pauses/restarts do
  not imply a strict 24-hour wall-clock expiration. The version-2 buffer is saved
  to `/run/osctl/oomd/host-load.yml` about once a minute and loaded on daemon
  startup.
- `watcher.rb`: an active-host sample counts a hit for a container only when it
  has a memory limit, consumes at least 95% of that limit, consumes at least 90%
  of its CPU limit if CPU-limited, and ranks in the top five containers by
  one-minute load. Containers without a CPU limit skip the CPU guard.
- `killer.rb`: a hit increments both restart and stop counters. An active-host
  sample that fails selection decrements existing counters by one, floored at
  zero. Inactive-host samples skip both hits and misses. Thus hits are accumulated
  scores, not strictly consecutive samples and not a timed window. Four
  continuously qualifying samples give a nominal one-minute restart threshold
  instead of two minutes, but no exact elapsed-time guarantee.
- `killer.rb`: stop takes priority at 40 hits. Successful restarts reset only the
  restart counter; successful stops reset only the stop counter. The daemon runs
  `osctl ct restart --kill` or `osctl ct stop --kill` on the selected container.
  Hit counters live in memory; restarting oomd resets them, while its saved load
  history can survive the daemon restart. A node reboot clears the `/run` state.

The pinned CLI and watcher specs corroborate the defaults, configuration merge,
host activation gate and container guards. They were inspected, not executed;
there is no daemon code change requiring their execution in this package.

## Implementation package I

Owner: implementer0 after lead assignment. Dependency: lead acceptance of this
brief and a session-owned configuration worktree based on the current approved
development baseline. D's relevant contracts are settled. No parallel
application package or shared-output dependency is needed.

Only application file:
`cluster/cz.vpsfree/nodes/prg/node25/config.nix` in `vpsfree-cz-configuration`.
Add the following block near the existing osctl settings, using local formatting:

```nix
  osctl.oomd.settings = {
    restart_hits = 4;
    load_multiplier = 1.5;
  };
```

Use ordinary module merging so inherited `verbose = true` stays present. Do not
change shared node configuration, option definitions, source/input pins, sample
interval, CPU/memory/load-ranking guards, stop threshold or daemon code. No
`mkForce` is needed. There are no generated clients, schema migrations, API or
wire-protocol changes and no repository documentation update is needed for these
existing settings; this session record preserves the site-specific rationale.

Acceptance and evidence:

1. The final diff contains only those two settings in node25's configuration.
   The implementation owner reports exact base/head, file inventory and confirms
   no input-lock change, migrations or transitional history.
2. The changed file parses and passes the repository's Nix formatter/hooks in its
   pinned development environment. `git diff --check` is clean. These are quick
   checks, expected under a minute once the shell is ready; uncertain shell setup
   or longer checks follow the verification watcher procedure.
3. Focused node evaluation yields merged settings
   `{ restart_hits = 4; load_multiplier = 1.5; verbose = true; }`. Check the actual
   generated service configuration as part of the build. Unspecified settings
   retain the pinned defaults above. Use the pinned confctl evaluation interface;
   do not assume a new flake output or add a custom test framework.
4. Required full-node check after commit, quick checks and independent review:
   `confctl build --yes cz.vpsfree/nodes/prg/node25` from the repository's `nix develop`
   environment. This is a long/uncertain check for a fresh utility watcher. Record
   the exact revision, command, result and build/input receipts. Stop and diagnose
   an unexpected local kernel build; do not expand scope to fix unrelated inputs.
5. A one-node build/evaluation and the narrow diff are sufficient scope proof;
   no fleet build, metrics campaign, synthetic production pressure or production
   container restart is required to test these literals. A build/runtime failure
   is a concrete blocker to diagnose and report, not permission to broaden work.

## Verification recovery after the missing initrd secret

The actual required build at reviewed feature head
`08d68a85f24a95b70b2d806f995f04b236e4d89a` failed while forcing the toplevel
`buildCommand`: `/secrets/nodes/initrd/ssh_host_ed25519_key` is absent. Preserve
[the failed build log](node25-build-yes.log) and the existing
[environment note](../../notes/vpsfree-cz-configuration/2026-07-13-confctl-node-build-initrd-secret.md).
The node's unchanged `common/netboot.nix` declares the external initrd keys. Do
not fabricate a key, change boot options or repeat the unchanged full build.
Full-node build success has not been established.

The concrete blocker justifies a focused fallback for merged oomd settings.
Package V is for implementer0 after lead acceptance/dispatch; it changes no
application file or input. The original recommendation against duplicating the
private confctl module stack still applies. Use the actual canonical toplevel
derivation's lazy `activationScript` attribute, which the pinned
`os/modules/system/activation/top-level.nix` takes directly from
`config.system.activationScripts.script`. Inspecting that attribute's string
context should avoid forcing the failing `buildCommand` and initrd branch.

From the unchanged final worktree in its pinned shell, the proposed first check
is:

```sh
nix eval --json --impure --no-write-lock-file --no-update-lock-file \
  --apply 'x: builtins.filter (p: builtins.match ".*-etc[.]drv" p != null) (builtins.attrNames (builtins.getContext x))' \
  '.#confctl.build.m_cz_vpsfree_nodes_prg_node25_5e1cc944.toplevel.activationScript'
```

This is source-derived and not yet executed by the architect. Bound this first
projection to under a minute. Require exactly one `etc.drv` dependency, then
inspect its direct derivation inputs for exactly one `sv-osctl-oomd-run.drv`.
Inspect that service derivation's direct inputs for exactly one
`osctl-oomd-config.json.drv`. Retain this exact dependency chain in the verification
evidence. The pinned `formats.json` generator serializes the real merged
`cfg.settings` into structured derivation attribute `value`, then formats it with
`jq`. Read only that leaf's JSON value (decoding structured attributes if needed)
and require exactly `{"restart_hits":4,"load_multiplier":1.5,"verbose":true}`.
Alternatively, realize only that JSON leaf and inspect its output, with a fresh
verification watcher for a long/uncertain build.

Do not print full unrelated derivations or activation scripts. Missing or
ambiguous dependency edges, another missing-secret evaluation, or an overrun
stop this bounded attempt and return a concrete blocker to the lead. No
replacement evaluator, module-option override, synthetic secret, node access or
deployment is part of V. A successful result proves only actual merged oomd
JSON on the reviewed source/input graph, not a full system build or running-node
behavior. Preserve exact feature head, command, dependency paths and result in
the existing implementation/state evidence; the lead decides acceptance for
the configuration-only integration with the full-build limitation explicit.

## Compatibility and operator recovery context

This session delivers configuration and validation only. The operational notes
in this section do not require or authorize node access, live verification,
deployment, reservations or repository integration.

The pinned daemon already supports both settings. The change preserves its JSON
configuration interface and host-load state version. There are no database,
persisted-format, API, CLI, Terraform or cross-service protocol changes. Only
node25 needs activation; other nodes can retain their settings indefinitely.
No coordinated fleet update or reboot is needed for the threshold change.

The intended operational effect is earlier forced restarts of qualifying
containers: a lower host-load gate and half the restart hit score. The unchanged
stop counter can also receive hits during the newly active load range, so
leaving `stop_hits = 40` does not promise identical stop timing. Successful
restarts do not clear that stop score. This follows the existing behavior and
should remain explicit in the lead's operational assessment.

For a future operator deployment, the running source/input graph and system
baseline need comparison with the candidate, including unrelated activation
effects from the refreshed production inputs. Oomd parses configuration only at
process startup, so loading the new settings requires daemon restart through the
normal activation path. Service health, installed JSON and a fresh verbose
record showing `threshold = median * 1.5` would establish the intended effect
without deliberately killing a container. These are future operator checks,
not acceptance criteria or pending work for this session.

Recovery restores the previous node configuration/system using the recorded
baseline and restarts oomd through the normal service activation path. Removing
the two overrides restores source defaults 8 and 2.0. The old daemon can read
unchanged version-2 host-load state, but restarting it resets in-memory hit
counters. Reverting settings cannot undo a container restart/stop already taken.
Any future recovery should verify service health and the restored settings.

Build validation does not authorize default-branch integration. The lead retains
the existing separate integration-approval boundary. This brief does not
authorize session lifecycle actions.
