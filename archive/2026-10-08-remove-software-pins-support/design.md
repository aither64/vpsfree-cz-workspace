# Remove software-pin support from confctl

Status: lead-accepted implementation plan, prepared by architect0 on 2026-10-08.
Application changes and verification have not been performed. The lead owns
plan/state/portal updates; this assignment changes only this file.

Repository inspected: `worktrees/2026-10-08-remove-software-pins-support/confctl`,
HEAD `1b56616eff41e760327f3a0dbed8875e4aa9dbec`. The worktree was clean at
inspection. The lead subsequently confirmed the same fetched `origin/master`.
`dev-session current` in the tracking directory matched the trusted session
binding; both shell environment markers were absent. The retained roster gives
architect0 design ownership and workspace-write access, Astra/xhigh.

## Scope and decisions

Implement only in confctl. Completely remove the software-pin CLI, evaluator,
Ruby model, persistence writer/reader, Nix options, runtime metadata readers,
automatic updates, and migration implementation. A cluster must have a
`flake.nix` and expose the existing `confctl` flake outputs. Delete the current
software-pin `example/` and move `example-flake/` to `example/`, including its
hidden files and nested-machine example.

Retain the existing flake contract: channels map dependency roles to root input
names, later channels override earlier roles, and per-machine
`inputs.overrides` wins over channels. Keep raw-source inputs with `flake =
false`, path inputs, follows links, `impureEval`, `legacyNixPath`, and
`legacyNixPathMap`. They are features of flake configurations and do not require
the software-pin implementation. Do not conflate a non-flake input with a
non-flake cluster.

Retain shared deployment, SSH, carrier/netboot, health-check, rollback,
generation/profile, input update/set, Git mirror, logging and hook behavior.
Avoid opportunistic redesign of the input resolver, Nix compatibility retries,
dependency versions, or remote deployment protocol.

This is an intentional breaking change. There is no hidden legacy mode, CLI
alias to the old implementation, schema adapter that reconstructs pin objects,
or automatic migration of stored generations. Keep the migration guide as
historical upgrade guidance explicitly requiring the older v3 confctl; remove
the migration command from the new executable. The source changelog identifies
v3.0.0 as supporting both workflows and announces removal in v4, but this task
does not assign a release number, publish a gem, or assert production adoption.

The intended readers of this brief are the lead, implementer and independent
reviewer. Lasting user contracts and recovery instructions must also be put in
the owning README/manual and migration guide during implementation, so they do
not depend on this private workspace record.

## File and function inventory

All paths below are relative to confctl. Inventory included hidden CI/hook
files, runtime sources, Nix functions/modules, examples, documentation/templates,
specs, integration suites, packaging and repository skills.

### Delete the pin subsystem

| Paths | Action and reason |
| --- | --- |
| `lib/confctl/swpins.rb`, `lib/confctl/swpins/{change_set,channel,channel_list,cluster_name,cluster_name_list,core,deployed_info,spec}.rb`, `lib/confctl/swpins/specs/{base,directory,git,git_rev}.rb` | Delete all pin types, fetching, channel/core/machine state, update/commit helpers and deployed pin metadata parsing. Do not keep a subset for old generations. |
| `lib/confctl/cli/swpins.rb`, `lib/confctl/cli/swpins/{base,channel,cluster,core,utils}.rb` | Delete all software-pin commands. |
| `lib/confctl/cli/migrate.rb`, `lib/confctl/cli/migrate/swpins_to_flakes.rb` | Delete migration CLI and implementation. `load_legacy_channels` explicitly constructs `NixLegacy`; retaining this helper would retain the removed backend. |
| `nix/lib/swpins/{eval,options}.nix`, `nix/modules/confctl/swpins.nix` | Delete pin options/fetch evaluation and `/etc/confctl/swpins-info.json` generation. |
| `nix/evaluator.nix`, `nix/machines.nix` | Delete the `jsonArg`, `<nixpkgs>`/`coreSwpins`, `listSwpinsChannels`, `evalCoreSwpins`, `evalHostSwpins`, and legacy toplevel evaluation interface after replacing option documentation as described below. |
| `nix/lib/machine/{default,info}.nix` | Delete the old system builders and their exclusive helper. They inject `swpins`/`swpinsInfo`; the flake builder has its own machine arguments. |
| Current `example/` including `configs/swpins.nix`, `swpins/core.json`, `swpins/channels/*.json` | Delete the entire legacy example before moving the flake example into its place. |
| `spec/confctl/swpins_spec.rb`, `tests/suite/deploy/swpins.nix` | Delete successful pin-workflow tests; add narrow rejection coverage elsewhere. |

Ruby loading uses `require_rel` in `lib/confctl.rb`, `lib/confctl/cli.rb` and
namespace files. Delete namespace loaders with their directories, and search
explicit requires and stubs after the moves; dead files are still loaded by
this mechanism even if the CLI no longer calls them.

### Ruby backend and configuration entry points

| Paths/functions | Required final shape |
| --- | --- |
| `lib/confctl/nix.rb` | Keep `ConfCtl::Nix` as the public facade name, but make it the single flake implementation. Preserve its existing `stateless` method. Move the flake methods and required shared helpers into it; remove backend dispatch and obsolete delegators. |
| `lib/confctl/nix_flake.rb` | Move its actual evaluation/build implementation into `Nix`, then delete this extra class/file. Preserve batched output lookup, machine-name/key mappings, build-plan caching, progress callbacks, lock-write guards and Nix feature/option retries. |
| `lib/confctl/nix_legacy.rb` | Delete after extracting `initialize`, `copy`, `activate`, `activate_with_rollback`, `set_profile`, `set_carried_profile`, `run_command_in_shell`, `collect_garbage`, protected state and `demodulify`. These are currently inherited by `NixFlake`; dropping the parent without moving them breaks deployment. The public facade already owns `stateless`, so preserve that method rather than extracting the parent's duplicate. Do not move `with_argument`, `nix_instantiate`, legacy evaluation/building or pin helpers. |
| `Nix#eval_host_swpins`, `#build_attributes` | Rename the flake build-plan role/path query to `eval_host_inputs(hosts)`; remove `list_swpins_channels`, `eval_core_swpins` and software-pin parameters. `build_attributes(hosts:, time:)` reads each host's input paths from the flake plan. |
| `lib/confctl/nix_build.rb` | Delete the `nix-build`/pin-derived `NIX_PATH` implementation. Keep `nix_build_flake.rb` and its independent progress parser. |
| `lib/confctl/config_type.rb`, `lib/confctl/conf_dir.rb` | Replace the backend predicate with one clear required-flake check, preferably `ConfDir.require_flake!` accepting the explicit configuration path. Delete `ConfigType`. Missing `flake.nix` must raise a user-facing `ConfCtl::Error`, with a pointer to migration using v3, before configuration mutation/evaluation. |
| `lib/confctl/cli/configuration.rb` | `init` always calls the flake initializer; remove `init_swpins`, `swpins_mode?`, `flake_config?` and pin JSON moves in `rename`. `add` always writes `inputs.channels = [ "nixos-unstable" ]`, matching the generated flake channel. Validate `add`, `rename`, `rediscover` before mutation. Preserve nested relative imports and `configuration_rediscover` hook. |
| `lib/confctl/cli/app.rb` | Remove `init --swpins`/`--legacy`, `swpins` tree, `swpins_commands`, and entire `migrate` tree. Update input/changelog/diff/build help to flake input roles and `nix build`. Keep current supported options and argument positions. |
| `lib/confctl/cli/inputs/{root,channels,machines}.rb` | Retain input operations and sharing protections. Route repeated flake guards through the common check; remove suggestions to use swpins. |
| `lib/confctl/settings.rb` | Remove `core_swpin_channels`, `core_swpin_pins`, and legacy `nix_paths`. Keep list/build concurrency and retention settings. |
| `lib/confctl/conf_cache.rb`, caching methods in `conf_dir.rb` | Delete the old Git-file/settings/machine-list cache after removing `NixLegacy#with_cache`: it has no remaining in-repository consumers. Retain `ConfDir` path/hash/cache/generation/log/script directories; these identify live state and GC roots. |

The flake guard must not prevent `confctl init`, help/version, or packaged tool
startup in an empty directory. Do not add a global require-time assertion:
Rake loads `confctl`, and user scripts are loaded at startup. Config-bound Nix
methods enforce the guard; stateless option-document generation and generic
remote helpers need no cluster evaluation. Keep custom user commands usable
under their existing requirements.

`run_command_in_shell` intentionally still invokes `nix-shell` for tools such as
ClusterSSH. That is a host package operation, not a cluster backend.

### Cluster, status, versions, generations and hooks

| Paths/functions | Required change |
| --- | --- |
| `lib/confctl/cli/cluster.rb`: `status`, `changelog`, `diff` | Promote the current `*_flake` implementations to the ordinary entry points; delete software-pin branches and `compare_swpins`. Preserve selected-generation comparison, role filters, downgrade direction, grouped Git logs, diff output and offline/unknown reporting. |
| Same: `do_build`, `do_build_group`, `swpin_build_groups` | Delete `autoupdate_swpins` and `check_swpins`, including "skipping swpins" messages. Use `eval_host_inputs`, input names and the reduced build signature. Preserve a single batch by default, and input-path grouping when `legacyNixPath` is true so mixed-role paths never share conflicting `-I` arguments. Rename grouping accordingly. |
| Same: `list_generations`, `flake_generation?`, all `MachineStatus#query` calls | Display only flake input revisions. Remove pin columns/collision logic, format forks and `swpins:` keywords. Preserve kernel/name columns and noninteractive output. |
| `lib/confctl/machine.rb#nix_paths`; `nix/modules/cluster/default.nix` `nix.nixPath` | Delete this legacy per-machine mapping. In the current flake backend these paths only affect grouping; actual `-I` mappings are read from flake inputs again. Do not revive an ignored mapping as new functionality. |
| `lib/confctl/machine_status.rb` | Remove `SwpinState`, `target_swpin_specs`, `swpins_info`, `swpins_state`, pin query/read methods and the old pin-based `evaluate`/unused status accessors after checking callers. Keep uptime, profiles, `target_toplevel`, `inputs_info`, `target_inputs_info`, `InputsInfo.normalize`, and carried-machine fallback from `machine.json` to the profile's `etc/confctl/inputs-info.json`. |
| `lib/confctl/generation/build.rb` | Keep only flake creation/load/save/destroy and input GC roots; remove pin attrs/spec reconstruction, `create`'s legacy signature, `swpin_path`, mode forks and `pin_paths`. Keep `create_flake` or rename it consistently to a flake-only constructor. Preserve the existing serialized flake format. Apply the unsupported-record policy below before accessing payload fields. |
| `lib/confctl/generation/build_list.rb` | Match generations by toplevel and input paths, without legacy default mode. Add explicit skipped-record reasons/current-state handling; remove silent fallback when the `current` link names a rejected record. |
| `lib/confctl/generation/unified.rb`, `cli/generation.rb` | Remove pin delegation/columns and replace `pin_paths` comparison with `inputs`. Preserve remote-only generations with no local input metadata, host/build matching, retention, local/remote selection and profile deletion. |
| `nix/modules/confctl/carrier/netboot/build-netboot-server.rb`, `Generation#to_json` | Remove exported `swpins_info`. Expose existing `inputs-info` metadata as `inputs_info` if present, following `docs/carrier.md`'s machine JSON. Do not change boot paths, versions/revisions, MACs, variants, kernels or PXE parameters. In-repo `kexec-netboot` does not consume the pin field. |

`lib/confctl/hook.rb`, `user_script.rb`, `user_scripts.rb`, `git_repo_mirror.rb`,
`inputs/**`, `flake_lock*.rb`, `inputs_info.rb`, Nix copy/GC helpers,
`machine_control.rb`, health-check code and `libexec/auto-rollback.rb` stay.
`GitRepoMirror` is used by flake changelogs and input commit messages; it is not
a pin-only dependency. Both registered hooks (`cluster_deploy` and
`configuration_rediscover`) remain with their existing payloads. External
scripts using removed pin constants or backend/cache internals intentionally
break and need operator review; there is no evidence of their deployed usage.

### Nix API, documentation evaluation and shells

| Paths | Required change or retention |
| --- | --- |
| `nix/modules/cluster/default.nix` | Remove `swpins.channels`, `swpins.pins`, `swpinOptions`, and legacy machine `nix.nixPath`. Preserve input channels/overrides, all host/build/health/carrier options and custom cluster submodule extensibility. Remove pin-related wording from descriptions. |
| `nix/modules/confctl/nix.nix` | Remove global `confctl.nix.nixPath` (only consumed by legacy `NixBuild`); retain `maxJobs`, `impureEval`, `legacyNixPath`, `legacyNixPathMap`. Update build command wording. |
| `nix/lib/default.nix` | Retain callable `findMetaConfig`, `getClusterMachines`, `getAllAddressesOf`, `mkNetUdevRule(s)`, `mkOptions.addresses`, `corePkgs` and `coreLib`. Remove import of `./machine`, `buildConfig` and lazy legacy `makeMachine.build` construction; metadata enumeration/carrier expansion must remain usable without forcing a system build. Keep the existing import argument shape to avoid unrelated churn. |
| `nix/flake/mk-confctl-outputs.nix` | Preserve flake outputs `settings`, `channels`, `machineNames`, `machineKeys`, `machines`, `machinesJson`, `buildPlan`, `inputs`, `inputsInfo`, `build`, `toplevel`, `lib.mkMachineKey`. Keep NixOS/vpsAdminOS evaluation and current module arguments. Add a flake-native option-documentation output as below. Do not replace role names with root input names in machine arguments. |
| `nix/modules/module-list.nix`, `flake.nix` | Remove imports/export `nixosModules.swpins`. Keep remaining exports. A cleaned module list is still useful to the documentation evaluator even where the flake builder imports modules directly. |
| `nix/modules/system-list.nix`, `confctl/{host,inputs-info,configuration-info,generations,cli}.nix`, carrier/kexec Nix modules | Retain and include actual confctl-owned system options in generated documentation. No new metadata schema is needed. |

The options reference needs real implementation work, not just text deletion.
`NixLegacy#module_options` currently uses `nix/evaluator.nix`; `NixFlake`
returns `[]`. Therefore `rake confctl-options` at a flake root can succeed while
emptying the reference, and `confctl ls -L` has the same hole.

Implement a focused shared Nix documentation function (suggested
`nix/module-options.nix`) using the already locked nixpkgs library/evaluator and
the cleaned module lists. Evaluate options without building hosts. Supply
`confLib` and inert machine/module arguments, include confctl's carrier and
kexec modules, and select only public confctl-owned options. Preserve normalized
option types/defaults/examples/declarations expected by `ModuleOptions`.
Do not include every upstream NixOS service option.

Expose cluster-specific `confctl.moduleOptions` from `mkConfctlOutputs`,
including `modules/cluster/default.nix` so `confctl ls -L` can list user-defined
metadata. Expose a package-local documentation output in the root flake from
the same evaluator for the Rake task, independent of the caller's cluster.
Wire `Nix#module_options` to the cluster output and give the Rake task an
explicit package-documentation path. If compatibility with existing v3 flake
outputs lacking the new attribute is needed, use the same new evaluator against
that configuration with explicit locked inputs; do not keep the old evaluator
as a fallback. Prefer updating the configuration's confctl input alongside the
tool (see deployment contract) to avoid that extra path.

In `Rakefile`, `lib/confctl/module_options.rb`, and
`template/confctl-options.nix/{main,options}.erb`, remove the software-pin
category/filter and the empty SERVICES category. Group runtime carrier/program
options under a meaningful machine-system section, distinct from operator
settings in `configs/confctl.nix`. Adjust declaration-path normalization if
flake store paths do not contain `/confctl/`; do not hard-code that checkout
basename. Regenerate `man/man8/confctl-options.nix.8.md` and rendered man pages.

Lead-approved correction from source inspection: no module here declares
`services.*`; netboot only sets upstream service configuration. Require
nonempty `confctl.*`, `cluster.*`, `confctl.carrier.*`, and
`confctl.programs.*` documentation, plus input/metadata options. The old
SERVICES section was already empty. No new services API is to be invented.

There is **no root `default.nix` at the inspected HEAD**. The relevant
`default.nix` files are Nix module/library entry points or data sets, not
automatically legacy cluster backends. Keep `nix/lib/default.nix` after the
targeted refactor, `nix/modules/cluster/default.nix`,
`nix/modules/confctl/kexec-netboot/default.nix`, and example `data/default.nix`.

Keep root `shell.nix`: it is a confctl source development/Bundler shell importing
host `<nixpkgs>`, not a configuration evaluator or software-pin package API.
Document it only as a developer convenience. Preserve
`example-flake/shell.nix` as `example/shell.nix` during the rename: it imports
the retained root developer shell and has no pin dependency. Document
`nix develop` as the cluster workflow; the wrapper remains an optional
developer convenience.
Keep `mkConfigDevShell` modes and `legacyCompat` (the latter only supplies a
temporary Gemfile for bundled-confctl); none implement pin configuration.
Keep `nix/package.nix` and the flake package APIs.

Remove `nix-prefetch-git` from all of `flake.nix`'s RSpec runtime/native inputs,
`nix/package.nix`, both `nix/flake/mk-*-devshell.nix` files, root `shell.nix`,
and `.github/workflows/rspec.yml`. Its only executable caller is the deleted
`Swpins::Specs::Git`. The `CONFCTL_TEST_NIXPKGS`/`NIX_PATH` setup is likewise
pin-spec-only in the RSpec suite and can go after confirming no added test
requires it. Keep Nix, Git and SSH: the remaining input specs use local Git
repositories and actual `nix flake` commands. No Ruby dependency removal is
currently justified; `Gemfile.lock`/`gemset.nix` need no unrelated refresh.

### Examples, documentation and tests

| Paths | Work |
| --- | --- |
| Renamed `example/` | Keep the flake skeleton, channels `nixos`/`vpsadminos`, nested machine and raw source imports via `inputs`. `confctl.url = "path:.."` still works at the same depth. Explain changing this URL when copying the example elsewhere. |
| `example/README.md`, `example/configs/confctl.nix`, generated snippets in `cli/configuration.rb` | Correct nearby stale names: actual directory is `vpsfreecz-vps`; target option is `host.target`; input updates need explicit names or `--all`; columns are `confctl.list.columns = [ ... ];`, not `listColumns = { ... };`. Keep generated `nixos-unstable` channel consistent with `add`; example's independent `nixos` channel is intentional. |
| `README.md` | Make flakes the sole workflow, remove legacy setup/pin sections/tree entries, add `flake.lock`, describe channels/overrides and current module arguments, remove `swpins`, repair heading anchors and settings snippets. Link the renamed example, flake-input guide and version-scoped migration/rollback instructions. Preserve unrelated deployment/health/hook documentation. |
| `docs/flake-inputs.md` | Canonical channel/role semantics, raw inputs and retained NIX_PATH options; ensure skeleton contains root `nixpkgs` required by `mkConfctlOutputs` (current skeleton only defines `nixpkgsStable`). Avoid claiming every source has revisions or flake exports. |
| `docs/swpins-to-flakes.md` | Retain as upgrade guidance for v3 -> flake-only confctl. Explicitly run automated commands with v3 before updating the tool/input; no claim that the new executable has `migrate`. Add local-generation/GC-root/tool rollback contract below. Preserve manual conversion guidance and scope old pin examples to that source version. |
| `docs/carrier.md` | Already uses `inputsInfo`/`inputs-info`; preserve its contract and reconcile the netboot JSON change. |
| `man/man8/confctl.8.md` | Remove all swpins commands and obsolete `--outdated-swpins` documentation, update init/build/status/changelog/diff/input wording and generation limitations. Preserve input command documentation and actual CLI options. |
| `CHANGELOG.md` | Add an unreleased breaking-change entry; preserve historical v3 and earlier release descriptions. Do not fabricate release date/version. |
| `AGENTS.md` | Replace swpins/example description and manual-check guidance with the supported flake paths and generation checks. |
| `tests/runner/extensions/confctl_helpers.rb` | Change `prepare_fixture_dir!` default to `example`; remove pin-state cleanup/comment. Preserve fixture isolation and SSH helpers. |
| `tests/suite/deploy/base.nix`, `flakes.nix`, `tests/all-tests.nix` | Drop `deploy/swpins` registration and all `deployMode`, legacy config writers/update branches. Keep `deploy/flakes` as the stable test selector; simplify its import/base structure without losing either NixOS or vpsAdminOS assertions. |
| `spec/generation/build_modes_spec.rb` | Replace successful mixed-mode support with flake round trips and explicit unsupported-record behavior. Seed old JSON as inert fixtures; never construct old pin objects. |
| `spec/confctl/nix_flake_spec.rb`, `cli/cluster_status_flake_spec.rb`, `cli/inputs_set_output_spec.rb` | Update renamed classes/methods and ConfigType stubs. Preserve assertions for built machine JSON, deployed revision display and resolved set revisions. Rename spec filenames if clearer. |
| `spec/confctl/configuration_spec.rb`, new focused specs | Cover removed CLI/flags, flake requirement, generated channel/snippet correctness, retained grouping and documentation output. |
| `.github/workflows/tests.yml` | Keep ci-tagged integration execution; add `example/**` to paths if changing this workflow so future template-only edits exercise their consumers. Removing a suite requires no separate hand-maintained CI matrix update. |

The only current literal `example-flake` consumers outside the directory are
`tests/runner/extensions/confctl_helpers.rb` and
`tests/suite/deploy/base.nix`. README links already point at `example/` but
their target currently means the wrong workflow. Perform a final hidden-file
search after the rename. `tests/suite/{auto_rollback,carrier/deploy,carrier/netboot}.nix`
use the shared fixture and stay; so do runner extensions, `test-runner.sh`,
`tests/make-test.nix`, RSpec helpers, hooks and the repository's release and
configuration-update skills. No integration command is to run during planning.

## Persisted generations and recovery contract

Keep the existing flake `generation.json` format exactly: `mode: "flakes"`,
`date`, `toplevel`, `auto_rollback`, `inputs`, `inputs_info`. Retain read support
for the existing `inputsInfo` spelling where already supported. Preserve
directory names, `current` symlink, `*.input` links, `toplevel`,
`auto_rollback`, and current GC-root names. Do not omit `mode` now that only
one format is accepted: v3 readers use it to distinguish generations.

1. `Build#load` accepts only explicit `mode == "flakes"`. Missing mode,
   `"swpins"` and unknown modes produce a typed unsupported-format error before
   parsing pin contents. Do not infer flakes from the presence of `inputs` or
   treat missing mode as flakes. Malformed flake JSON is a separate invalid
   generation error.
2. `BuildList` records rejected names and reasons, skips them as usable
   generations, and reports each path plus its reason to stderr (and the normal
   log), including instructions that records/roots were left untouched and v3
   is required for old pin generations. Do not silently swallow exception
   details. A rejection index containing only name/path/reason is diagnostic
   state, not an old-generation reader or compatibility implementation.
3. If an existing `current` symlink points to an unsupported, invalid or missing
   record, leave it unchanged and do not substitute the newest flake record in
   memory. `current` selection fails with its concrete reason. An absent link
   may retain the existing newest-supported-generation convention, but report
   that selection when rejected records are also present. Use symlink-aware
   checks so broken links are not mistaken for absent ones.
4. Explicitly selecting a rejected name or `current` target must fail before
   copying/activating any host, even with `--yes`; do not downgrade it to the
   generic partial-host "not found" flow. Numeric selectors become ambiguous
   when records have been excluded. Reject numeric selection for an affected
   local inventory containing rejected records, including generation CLI
   selection, and ask for an explicit supported name. Remote-only profile
   selectors are unaffected. This avoids silently shifting an existing offset.
5. Normal new builds can proceed in a mixed directory: save a flake generation
   and deliberately update `current` through the normal successful build path.
   Existing unsupported directories and their roots remain unchanged. Local
   lists/retention counts describe supported flake generations and warn about
   excluded records. Local `rm`/`rotate` cannot delete rejected records; do not
   add a "force legacy cleanup" feature. Block local `old`/automatic rotation
   if its current identity is unresolved, so loss of the current flag cannot
   expand deletion unexpectedly. Explicit supported-name operations retain
   normal confirmation and selection behavior.
6. Leave `*.swpin`, old JSON, `.confctl/build` caches, core/channel pin artifacts
   and all associated old GC roots untouched. The root directory is
   `/nix/var/nix/gcroots/per-user/<login>/confctl-<ConfDir.short_hash>`; names
   include host, generation, and `swpin.<name>`/toplevel/rollback suffixes.
   Removing the code does not release these roots and may leave disk usage
   above the new tool's retention count. This is intentional recovery
   preservation, not supported pin operation.
7. Operators can remove unwanted legacy generations with retained v3 confctl
   using its ordinary local generation commands while it can still load the
   records, or keep them until rollback is no longer needed. Cleanup of broader
   legacy caches/roots is a separately inventoried operator action, never a
   wildcard deletion recommended by the new tool. Do not move/delete `.confctl`
   casually: roots point into it, and the root namespace depends on the real
   configuration path. JSON backups alone do not preserve store closures.

Generic remote profile generations remain listable/removable through existing
Nix/carrier profile operations regardless of what produced their closures.
This does not resurrect local software-pin metadata or allow the new tool to
build/redeploy a rejected local generation. Local roots do not protect remote
copies. Operators retaining rollback must avoid deleting required remote
profiles and running GC that removes their closures.

For tool rollback, retain a runnable v3 binary/source/environment, the previous
configuration Git revision/lock, and relevant local/remote roots. v3 can read
new generations because the flake schema stays unchanged; v2 cannot use these
flake configurations. Restoring a pre-flake configuration requires restoring
its matching config/pin files and using the older tool. New builds may have
changed `current`; select the required old generation explicitly with v3.
Never promise that a removed or garbage-collected closure can be recovered by
changing the tool version.

## Compatibility, deployment and invariants

- CLI removal includes `swpins`, `migrate swpins-to-flakes`, `init --swpins`,
  `init --legacy`; pin Nix options and `nixosModules.swpins` disappear. Legacy
  generated `NIX_PATH` options disappear, whereas flake `legacyNixPath` remains.
- Flake tool and configuration input should be updated together, because the
  package-documentation/cluster-option output is new. Existing primary
  build/deploy/input outputs and module argument shapes remain stable. Preserve
  Nix input identities, role precedence and machine keys (including nested and
  carried names). No background input updates occur during build/deploy.
- No database, API client, daemon message or Terraform migration is involved.
  Local flake-generation JSON and deployed `inputs-info.json` /
  `configuration-info.json` remain compatible. Pin-derived metadata is no
  longer read or written. Netboot's optional `swpins_info` field disappears;
  external consumers are unknown and must be checked before site rollout.
- Old running nodes can remain while the operator/configuration tooling moves
  to flakes. SSH copy/activation/profiles and auto-rollback remain unchanged.
  Nodes lacking input metadata report unknown inputs; there is no fallback to
  swpins-info. After a successful new build/deploy they acquire flake metadata.
  This confctl-only change does not require a coordinated update of all
  NixOS/vpsAdminOS nodes or change on-disk node state.
- Upgrade sequence for an old configuration: retain rollback assets; migrate
  with v3 and review channel/override mappings; verify a representative flake
  build while v3 is retained; remove obsolete configured options/hooks; then
  select the new confctl tool/input and verify list, input status, generation
  selection and a representative build. Deploy only under a separately
  authorized rollout, keeping old profiles. Configuration repositories are
  deployment consumers, not part of this implementation's edit scope.
- Configuration/tool rollback restores their prior revisions and the retained
  environment; machine rollback uses preserved system profiles/closures. No
  automatic state migration needs reversal. Avoid production cleanup until the
  rollback window is intentionally closed.

## Ordered implementation units

1. **Establish flake-only validation and backend.** Move shared/flake Ruby
   implementation to `Nix`, replace guards, remove legacy init/CLI/backend/cache
   paths, and simplify cluster build/status/comparison. Preserve common helpers
   and input behavior. Remove corresponding runtime namespaces atomically so
   `require_rel` cannot load dangling legacy classes.
2. **Make persistence exclusively flake-based.** Simplify build/unified
   generations and display, implement unsupported-format diagnostics/current
   and selection rules, preserve roots and round-trip schema. Add meaningful
   generation regression specs before calling this unit complete.
3. **Remove Nix pin support and restore documentation evaluation.** Delete pin
   evaluators/modules/legacy builders, refactor metadata-only `confLib`, clean
   exports/options, introduce the shared option evaluator and connect both
   cluster `ls -L` and Rake. Remove carrier pin metadata without touching boot
   behavior. Retain explicitly identified shell and flake compatibility APIs.
4. **Rename examples and adapt tests/dependencies.** Delete/move example trees,
   remove swpins suite, simplify deploy fixture to the single workflow, update
   spec class/guard usage and all template references. Prune nix-prefetch-git
   everywhere. Extend focused coverage described below.
5. **Finish supported documentation and prepared upgrade instructions.** Update
   README, input/migration/carrier guides as needed, CLI/options manuals,
   snippets, changelog and AGENTS. Generate artifacts, reconcile actual option
   names/CLI behavior, and apply the user-facing-writing skill directly before
   committing user-facing prose.
6. **Lead-owned verification/review gate.** Quick checks, intended commits,
   whole-branch diff/history/migration inventory and mandatory independent final
   review precede long integration runs. Consolidate obsolete unmerged
   transitional edits. Record "no database migrations; existing flake JSON
   retained, old pin records deliberately unsupported" for review. This plan
   itself does not trigger automatic review or authorize implementation.

The units describe dependency order, not a requirement to publish broken
intermediate states. The implementer may combine closely coupled units; route
material changes to persistence, compatibility or output contracts through the
lead. Only the lead updates session state/manifest and assigns implementation.

## Acceptance and verification plan

All commands here are planned, not executed. Use the repository's `nix develop`
environment; `.overcommit.yml` enables RuboCop and `.git-hooks/pre_commit/nixfmt.rb`.
The gemspec requires Ruby >= 3.3 even though AGENTS still mentions a 3.1 style
target. RSpec CI currently exercises Ruby 3.3, 3.4 and 4.0.

### Quick/static checks and focused behavior

Run known quick checks inline only after the environment exists. Delegate any
uncertain or >1-minute setup/build/test to a fresh utility watcher under the
monitor skill; no such command is authorized in this planning assignment.

```sh
git diff --check
nix develop -c bundle exec rubocop --parallel --force-exclusion
nix develop -c bundle exec rspec
nix develop -c bundle exec rake confctl-options
nix develop -c bundle exec rake md2man:man
```

Use `nixfmt --check` on the actual changed Nix files (the hook does this too).
Rake's options command must yield a meaningful nonempty reference, not just
exit zero. Snapshot/inspect generated declarations, defaults and examples, and
assert representative options such as `confctl.nix.legacyNixPath`,
`confctl.inputsInfo`, `confctl.configurationInfo`,
`cluster.<name>.inputs.channels`, `cluster.<name>.inputs.overrides`,
`confctl.carrier.netboot.enable`, and
`confctl.programs.kexec-netboot.enable`. Verify `confctl ls -L` includes custom
cluster metadata using a disposable flake fixture.

Required focused coverage:

- `init` succeeds outside a flake and produces only the supported skeleton;
  removed commands/flags are unrecognized and absent from help. Missing-flake
  cluster operations fail clearly before mutation or launching legacy Nix.
- Flake build/load/save/dedup/destroy round trips preserve JSON/input links/GC
  roots and kernel extraction. Explicit swpins, absent-mode, unknown-mode and
  corrupt JSON fixtures are rejected without pin classes. Diagnostics contain
  path/reason; current and numeric safeguards work; rejected files/symlinks and
  roots are byte-for-byte unchanged after list/build/retention activity.
- Mixed inventories do not substitute another generation for current or an
  offset. Explicit unsupported selection fails before any copy/activation,
  including mixed-host commands. New builds can install their supported current
  generation. Remote-only generation listing/removal still works.
- Status/diff/changelog show input revisions, keep generation selectors and
  downgrade semantics, and gracefully show unknown metadata on old nodes.
  Shared Git changelog/commit code remains exercised by existing input specs.
- Normal builds batch hosts; `legacyNixPath` requires `impureEval` and splits
  incompatible input path maps. `flake = false` and role overrides remain
  supported. Retain no-write/no-update-lock behavior and feature retries.
- Generated/init/example docs use valid list syntax and matching channel
  names; renamed fixtures retain nested machines and NixOS/vpsAdminOS coverage.
  Module-option extraction includes carrier/program options and no pin options.

Final source audit:

```sh
rg -n --hidden -g '!.git' 'swpins|Swpins|swpin|software.pin|example-flake|NixLegacy|ConfigType' .
rg -n --hidden -g '!.git' 'nix-prefetch-git|coreSwpins|evalHostSwpins|evalCoreSwpins' .
```

Review every match. Only historical changelog/upgrade text, explicit rejection
diagnostics, and inert negative fixtures may mention software pins. No supported
runtime pin API, loader, example, success test or dependency remains. No
`example-flake` path remains. Search is not a substitute for dynamic tests.

### Longer package, evaluation and integration verification

After committed deliverable review, use the monitor skill/watcher for these
existing repository interfaces:

```sh
nix build .#confctl
nix build .#checks.x86_64-linux.rspec
./test-runner.sh test deploy/flakes
./test-runner.sh test auto_rollback
./test-runner.sh test carrier/deploy
./test-runner.sh test carrier/netboot
```

Alternatively the CI selection is `./test-runner.sh test -f --jobs auto -t ci`;
do not duplicate the complete suite without a reason. The tests are registered
through `tests/all-tests.nix`, `tests/make-test.nix` and the pinned vpsAdminOS
test framework. The existing four retained selectors cover copying, all switch
actions, skips, explicit/current/numeric generations, updates, status/diff/log,
health checks, auto-rollback, carried profiles and PXE/kexec behavior. Add
assertions that new deployments contain input metadata and no generated pin
metadata, including the carrier JSON output. The deleted swpins suite must not
appear in the resolved test set.

Also evaluate a disposable copy of the renamed example and an init-generated
configuration: generate their lock through Nix, verify machine names/keys,
channels/settings/buildPlan, `confctl ls`/`ls -L` and input listing, then build
representative NixOS/vpsAdminOS configurations where practical. Use fixture
rewrites/local overrides as the existing test helpers do; do not update the
real repository lock or production configuration for a smoke test. Check raw
source input and optional NIX_PATH behavior through focused fixtures. These
may fetch/build and belong to the longer monitored phase.

Build/check package on aarch64 if an appropriate existing builder is available;
only x86_64 has the repository's integration-test outputs. Preserve all CI Ruby
matrix jobs. Inspect the built executable/help and packaged files to ensure no
deleted loaders/examples survive. Do not run a version release task or publish
a gem merely to verify the package.

An unexpected local Linux kernel build must stop the verification and be
investigated under the workspace procedure. Use caches/normal runners; this
change does not modify kernels. CI failures require diagnosis, not a blind
rerun. If workflow action refs are edited, verify current official versions at
implementation time; this plan has not researched or changed them.

## Remaining decisions and evidence limits

- The lead accepted the strict numeric/current selection policy for unsupported
  generations and updating the tool/configuration input together for the new
  module-options output. The lead also accepted the inventory and verification
  sequence, with the retained example shell and preserved facade `stateless`
  clarifications incorporated above. These are planned contracts, not claims
  of implemented or verified behavior.
- Production use of legacy configurations, Ruby hooks/internal APIs, imported
  library builders, `nixosModules.swpins`, netboot pin JSON, shell compatibility
  switches and old local roots is unknown. No other repository or live host was
  inspected. Site rollout must inventory actual consumers separately.
- Real evaluation of the replacement option extractor is still required,
  especially submodule defaults/declarations and custom cluster options. The
  old evaluator excluded service options and the flake method returned empty;
  passing the old task is not useful baseline evidence.
- Version publication, downstream configuration updates, live deployment,
  remote/default-branch integration and cleanup are outside this request. No
  tests/builds, commits, pushes, deployments or lifecycle changes were done by
  the architect.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-08-remove-software-pins-support/
