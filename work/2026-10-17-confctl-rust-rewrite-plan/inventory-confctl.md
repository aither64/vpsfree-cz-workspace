# confctl source inventory for the Rust rewrite plan

Status: **COMPLETE — assigned evidence/inventory package finished.**
Owner: implementer0. This is an evidence inventory, not the architecture brief.
No application code, branches, worktrees, production systems or historical
session records were changed. No builds or tests were executed.

Completed: all 29 action leaves and option groups; selection/results/exits,
streams/prompts/automation, TUI/progress/cancellation, Ruby/state/helper owners,
Nix package and GitHub/test surfaces, exact historical Go timing and useful
acceptance tests. Runtime parity gaps are explicitly listed at the end.

## Immutable sources and limits

- **R (Ruby baseline): `cc40679d267165aecfa569128438bb55fe910268`** in
  `repos/confctl.git`; local `master`, `origin/master` and `origin/HEAD` agree.
  No fetch was performed, so this establishes the locally available baseline,
  not fresh remote or deployed identity. All `R:path` citations below refer to
  this exact revision.
- **G (historical Go timing reference):
  `009ca80cfca39634fc72e38b4002108a94194796`** in the same canonical repository.
  Historical session `work/2026-10-09-evaluate-confctl-rewrite-language/state.md`
  identifies this as the accepted, published feature core, paired with
  configuration `0d20866cb59da7761d69cfe076e55f8e779bc843`. It explicitly says
  **no default merge or host deployment** occurred. Automated acceptance was
  recorded; an operator visual walkthrough and an unrelated requested prebuild
  benchmark remained pending. These are historical recorded results, not checks
  rerun for this inventory. All `G:path` citations below refer to the exact core
  revision, inspected through `git show`, never through its worktrees.
- The older reviewed timing anchor
  `45d7b9089589a5187bf39b20556a4b8ba8d96584` is retained, but G is the later
  final assembly anchor. Use G when adopting semantics, including executable
  signal-exit reconciliation before the timing footer.
- Session identity was independently verified with `dev-session current` and
  both matching environment values. Workspace guidance, confctl `AGENTS.md`,
  README and relevant source/docs were read. The documentation skill applies.
- The requested `report_to_lead` tool is unavailable. The public CLI report
  attempt failed before delivery on the read-only external `transition.lock`;
  no permission changes or further retries are planned. Lead reads this artifact.

## Complete built-in action command and option matrix

Authority: **`R:lib/confctl/cli/app.rb`**. There are **29 application action
leaves**, excluding GLI help/documentation plumbing and configuration-supplied
Ruby commands. No software-pin/migration action is registered.

Shared option sets used in the table:

- **F**: repeatable `-a/--attr <expression>` and `-t/--tag <tag>`.
- **Y**: `-y/--yes` (false by default).
- **N**: `-j/--max-jobs <number>` and `--cores <number>`; strings forwarded to
  Nix, no explicit type conversion in the CLI declaration.
- **M**: `--managed y|yes|n|no|a|all`; omitted means managed only.
- **I**: `--[no-]commit` (false), `--[no-]changelog` (true),
  `--[no-]editor` (true), `-d/--[no-]downgrade` (false).
- **L/R**: `-l/--[no-]local`, `-r/--[no-]remote` (both false; when neither is
  specified, local is selected).
- **GC**: `--[no-]gc` / `--[no-]collect-garbage` (true),
  `--max-concurrent-gc <n>` (Integer, default 5).

Except `--list`, `--copy-only`, `--enable-auto-rollback`,
`--disable-auto-rollback` and help, declared switches use GLI's default
negatable behavior. Short aliases and long aliases address the same option.
This includes less-prominent negative forms such as `--no-yes`,
`--no-show-trace`, `--no-reboot`, `--no-parallel`, etc.; exact parser spelling
and abbreviations should be captured from the executable in later parity work.

| Action | Positional arguments | Command options beyond global help/color |
| --- | --- | --- |
| `init` | none | none |
| `add` | `<name>` | none |
| `rename` | `<old-name> <new-name>` | none |
| `rediscover` | none | none |
| `inputs ls` | `[input-pattern]` | none |
| `inputs update` | `[input-name ...]` | I, `--[no-]all` (false) |
| `inputs set` | `<input-name> <rev>` | I |
| `inputs channel ls` | `[channel-pattern]` | none |
| `inputs channel update` | `<channels> [role]` | I |
| `inputs channel set` | `<channels> <role> <rev>` | I, `--[no-]allow_shared` in registration; manual/error text says `--allow-shared` (see gap below) |
| `inputs machine update` | `<machine> <role>` | I |
| `inputs machine set` | `<machine> <role> <rev>` | I |
| `ls` | `[machine-pattern]` | F, M, `--[no-]show-trace`, `-L/--list` (non-negatable), `-o/--output <attributes>`, `-H/--[no-]hide-header` |
| `build` | `[machine-pattern]` | F, Y, N, `--[no-]show-trace` |
| `deploy` | `[machine-pattern [switch-action]]` | F, Y, N, `--[no-]show-trace`, `-g/--generation <selector>`, `-i/--[no-]interactive`, `--[no-]dry-activate-first`, `--[no-]one-by-one`, `--max-concurrent-copy <n>` (Integer, 5), `--copy-only`, `--enable-auto-rollback`, `--disable-auto-rollback`, `--[no-]reboot`, `--wait-online <value>` (string, `600`), `--[no-]health-checks` (true), `--[no-]keep-going` (false) |
| `health-check` | `[machine-pattern]` | F, Y, `-j/--max-jobs <number>` (Integer, 5) |
| `status` | `[machine-pattern]` | F, Y, `-g/--generation <selector>` |
| `changelog` | `[machine-pattern [role-pattern]]` | F, Y, N, `-g/--generation <selector>`, `-d/--[no-]downgrade`, `-v/--[no-]verbose`, `-p/--[no-]patch` |
| `diff` | `[machine-pattern [role-pattern]]` | F, Y, N, `-g/--generation <selector>`, `-d/--[no-]downgrade` |
| `test-connection` | `[machine-pattern]` | F, M, Y |
| `ssh` | `[machine-pattern [command [arguments...]]]` | F, M, Y, `-p/--[no-]parallel`, `-g/--[no-]aggregate`, `-i/--input-string <data>`, `-f/--input-file <path>` |
| `cssh` | `[machine-pattern]` | F, M, Y |
| `generation ls` | `[machine-pattern [generation-pattern]]` | F, L/R |
| `generation rm` | `[machine-pattern [generation-pattern|old]]` | F, L/R, GC, Y |
| `generation rotate` | `[machine-pattern]` | F, L/R, GC, Y |
| `collect-garbage` | `[machine-pattern]` | F, Y, `--max-concurrent-gc <n>` (Integer, 5) |
| `gen-data vpsadmin all` | none | none |
| `gen-data vpsadmin containers` | none | none |
| `gen-data vpsadmin network` | none | none |

Global `-c/--color always|never|auto` defaults to `auto`. There is no global
config-directory option: configuration is the real current working directory.
`App` uses GLI normal subcommand option handling, strict option ordering and
preserved ARGV. Options belong before positional arguments. Explicit
`require_args!` checks exist for add/rename and input setters/channel/machine
operations; several cluster handlers only read positional slots and rely on
GLI. The table is the advertised signature, not a claim that all surplus
arguments are rejected identically.

GLI 2.22.2 is locked in `R:Gemfile.lock`. Installed source for the same gem was
read under `/nix/store/xf1qx3jgk2fn19bbigcg1vwwrdl20sc8-ruby3.4-gli-2.22.2/`:
`lib/ruby/gems/3.4.0/gems/gli-2.22.2/lib/gli/{app_support,exceptions,option_parser_factory,command_line_token}.rb`.
It supplies `help [command ...]`, `help -c` completion output, root `--help`,
leaf `-h/--help`, hidden `_doc`, command-prefix completion and framework error
handling. `App` does not call `version(...)`; exact `--version` behavior is a
parity fixture to capture, not a normal successful version response to invent.

### Priority observations for the architect

1. The manual documents `deploy --outdated`; **the Ruby App does not register
   it**. Source, help capture and later differential checks must resolve this;
   do not silently add it as presumed baseline functionality.
2. `test-connection` prints per-host failures and a summary, then returns
   normally; failed connectivity alone does not make the command fail.
   `status` also presents offline/outdated rows without raising for those rows.
3. `ssh` uses the non-raising execution path; remote nonzero statuses are
   presented rather than automatically propagated as confctl's exit status.
4. Confirmations are on **stdout**, even when output is piped. `--yes` bypasses
   ordinary selection/confirmation presentation entirely; `--interactive`
   per-host prompts can still require answers. No automatic non-TTY yes exists.
5. Go timing is a deliberate **stderr appendix**, including redirected stderr
   and `CONFCTL_TTY=0`; preserve ordinary stdout/result payloads separately.
6. Ruby's `scripts/` files run as Ruby during library loading, register GLI
   commands and subscribe in-process hooks. Replacing that extension contract
   requires the separately owned explicit compatibility decision; command and
   state parity do not make arbitrary Ruby imports source-compatible.

## Ruby command meaning and observable results

The sources in this section are R. Normal results and prompts go to stdout;
warnings/framework diagnostics/log locators go to stderr. Neither the built-in
list/status commands nor the input readers have a JSON-output flag. JSON files
produced or consumed by Nix/helpers are separate contracts.

### Selection and arguments

`lib/confctl/cli/command.rb:select_machines` resolves an exact machine name
first, then matching `key`, then the pattern. Patterns use Ruby
`File.fnmatch?(..., File::FNM_EXTGLOB)`, including brace alternatives; test
slash handling, literal names and brace/glob precedence in later parity work.
Repeated attr/tag filters are ANDed. Attr tests compare the attribute's Ruby
`to_s` with the supplied value for `=`/`!=`; missing attributes stringify as an
empty string. `^tag` excludes a tag, ordinary tags require membership. Dotted
attribute lookup and name/key/checks pseudo-attributes are in `machine.rb`.
`runnable?` excludes carried machines and machines without a target, but is
independent of `managed?`.

| Family | Observable behavior and ordering | Owning source |
| --- | --- | --- |
| `init` | Requires an empty real cwd except `.`, `..`, `shell.nix`, `.confctl`, `.gems`, `.gitignore`. Creates flake/config/data/module/environment skeleton, prints `mkdir`/`mkfile` actions. No consent prompt. | `lib/confctl/cli/configuration.rb` |
| `add`, `rename`, `rediscover` | Require `flake.nix`. Add creates nested machine files and hostname derived from the path; rename moves the directory, without rewriting its internal metadata text. Rediscover recursively finds directories containing both config/module, sorts paths, replaces `cluster/cluster.nix`, then calls the rediscover hook. File/dir modes 0644/0755; mutation actions printed. | same |
| `inputs ls` | Reads root inputs from lock, optional pattern, columns INPUT/TYPE/REF/REV/URL. No confirmation. | `lib/confctl/cli/inputs/root.rb`, `flake_lock.rb` |
| `inputs update/set` | Update requires explicit input names unless `--all`; all requires an existing lock. Update uses `nix flake update <names...>`. Set requires a lock, supports Git/GitHub inputs, applies overrides while restoring original upstream references, writes temporary lock then renames. Optional commit covers `flake.lock`, with editor/changelog/downgrade controls. Prints `No changes.` or changed input revisions. Cached-GitHub-metadata fallback is an error, not accepted update success. | root CLI; `inputs/{updater,setter,git_commit,commit_message,nix_output_guard}.rb` |
| channel input operations | Evaluate `.#confctl.channels`. Pattern selection is sorted; `{a,b}`/comma selector preserves supplied names that exist. Update deduplicates mapped inputs. Set checks sharing outside selected channel/role, errors unless allowed, then prints warning. Per-target summaries use the resolved locked revision, not blindly the supplied symbolic revision. | `lib/confctl/cli/inputs/channels.rb` |
| machine input operations | Machine and role resolve through evaluated inputs-info, not a wildcard fleet update. Mutate its mapped root input and print the resolved locked revision; missing machine metadata/role errors. The root input may be shared by other machines. | `lib/confctl/cli/inputs/machines.rb` |
| `ls` | Managed-only by default; can include unmanaged through M. Columns from `--output` comma list or `confctl.list.columns`. `-L` lists `name` plus module attributes, bypassing normal machine table. Headers uppercase; missing/false/empty values become `-`; columns separated/aligned with spaces. | `cli/cluster.rb:list`, `cli/{command,output_formatter}.rb` |
| `build` | Managed selection, empty selection errors, confirmation. Evaluate input paths, group builds only if legacy NIX_PATH bridge requires distinct maps; otherwise one batch. Print inputs/groups/build-log locator, progress, final generation-to-host groups. Existing toplevel+input-path match reuses a generation and updates current; new builds persist generations. | `cli/cluster.rb:do_build`, `nix.rb:build_attributes`, `generation/build_list.rb` |
| `deploy` | Managed selection, default action `switch`; only `boot/switch/test/dry-activate`. Reboot allowed only for boot. Wait accepts decimal seconds, `wait`, `nowait`; parsed only with reboot. Confirm before deploy hook, build/resolution, status query and effects. Missing generations can require another prompt and ignore those hosts. Already-current targets skipped before copy/activation/reboot/health; copy-only bypasses skip-current filtering. | `cli/cluster.rb:deploy`, `find_generations`, `skip_current_deploy_targets` |
| deploy effects | Default bulk: finish copy stage before sequential activation, then reboot stage, then health checks. Interactive bulk copies sequentially with prompts; otherwise bounded concurrent copy. Copy scheduling puts standalone first and interleaves carried machines across carriers. One-by-one completes each host's copy/activation/reboot/check sequence before next. Copy-only returns after copy. Standalone switch/boot set profile; test/dry-activate do not. Carried activation only updates carrier profile for switch. Disabled auto-rollback wins if both flags are set. | `cli/cluster.rb:deploy_in_bulk`, `deploy_one_by_one`, `sort_generations_for_copy`; `nix.rb` |
| `health-check` | Managed+runnable with configured checks only, error if none; consent then bounded jobs. Logs retries/failures, prints pass/fail counts and per-machine reasons. Standalone command raises if any failures. Deploy checks run for switch/test or boot+reboot; interactive deploy offers continue/retry all/retry failed/abort, `--keep-going` continues noninteractive deploy after failures. | `cli/cluster.rb:health_check`, `run_health_checks`, `run_health_check_loop`; `health_checks/` |
| `status` | Managed machines with target or carried state. Default builds before checking; explicit generation uses saved build, `none` skips target toplevel comparison/build but still checks inputs. Queries concurrently and joins before table. Columns HOST/ONLINE/UPTIME/STATUS/GENERATIONS plus sorted union of input roles. Deployed revision is displayed, color signals same/changed/unknown; offline/outdated rows alone do not raise. | `cli/cluster.rb:status`; `machine_status.rb`; `spec/confctl/cli/cluster_status_spec.rb` |
| `changelog`, `diff` | Consent then query deployed inputs per machine; optional target generation, otherwise current configuration inputs. Offline/no-metadata/unknown/no-changes output is explicit. Roles are sorted union and optional role pattern. Changelog defaults to oneline/max 50 unless verbose/patch; downgrade reverses comparison. Git mirrors/cache and pager are used. Retrieval errors are rendered per entry rather than necessarily failing whole command. | `cli/cluster.rb:compare_inputs_info`, `changelog`, `diff`, `inputs_git_log`; `git_repo_mirror.rb` |
| `test-connection` | Managed filter plus runnable; error on empty. Consent, sequential connection attempts, timeout options, per-host inability lines, counts and failed-machine list. Failed-host results are not raised as a confctl command failure. | `cli/cluster.rb:test_connection`; `machine_control.rb:test_connection` |
| `ssh`, `cssh` | Managed filter plus runnable; empty errors. Exactly one positional machine with no remote command opens interactive shell only when one machine selected; multiple selected gives missing-command error. Zero-argument SSH follows the command path, so capture its edge behavior rather than redesigning it. Input string/file mutually exclusive. Normal remote command path confirms shell-quoted argv. Sequential results follow selected machine order; parallel results accumulate in completion/insertion order. Aggregation groups `[exit_status, stdout]`, sorts host names within each group, prints `Exit status:` and output. Nonzero remote statuses are presented through non-raising execution. CSSH confirms then launches `cssh -l root ...` inside Nix shell. | `cli/cluster.rb:ssh`, `run_ssh_*`, `process_aggregated_results`, `cssh`; `machine_control.rb` |
| `generation ls/rm` | Default local, remote or both selectable. Remote query stage joins before combined selection. Selectors: name/glob, `current`, `old`, `<days>d`, numeric offset. CLI unified selection/sorting differs from per-host deploy selection; do not replace with an assumed common selector. List columns HOST/NAME/ID/PRESENCE/CURRENT/KERNEL + input role columns; sorted NAME then HOST. Remove prints `No generations found` when empty, otherwise confirms, removes generations in selected order, optionally collects changed remote host/carrier garbage. | `cli/generation.rb`; `generation/{build,host,unified}*.rb` |
| `generation rotate` | Retention combines per-machine/global min/max/maxAge, preserves current, stops at min; local requires resolved current. Empty prints `No generations to delete`. Confirms list before removal. Optional remote GC applies config collectGarbage and deduplicates carrier targets. | `cli/generation.rb:rotate`, `generations_rotate` |
| `collect-garbage` | Runnable machines, empty errors, confirms list; bounded jobs, per-host progress/results, aggregate failure raises. Remote remove/rotate can reach same GC owner. | `cli/generation.rb:run_gc`; `nix_collect_garbage.rb` |
| `gen-data vpsadmin ...` | Interactive username/password plus server-specified authentication parameters; protected input echo disabled. Auth token fixed lifetime/60-second interval. `all` does containers then network with memoized client. Replaces data files through `.new` then rename; no generic yes/JSON flag. Reads container node metadata and IPv4/IPv6 network lists, emits Nix. | `cli/gen_data.rb` |

### Exit, stream, prompt and automation contract

`R:lib/confctl/cli/app.rb:on_error` prints a leading newline and `Log file: ...`
to stderr when a log is open, then lets GLI handle the exception. GLI 2.22.2
source returns 0 after a normally completed action regardless of its Ruby return
value; `BadCommandLine`/unknown command exit 64; ordinary exceptions exit 1.
Its error handler writes `error: ...` to stderr, and usage-related errors also
render help on stdout. Exact OptionParser exception classes/statuses, signal
delivery, missing newline details and version behavior remain runtime fixtures.
Do not infer that confctl universally propagates subprocess status.

`R:lib/confctl/cli/command.rb` owns prompts:

- Normal confirmation writes `\nContinue? [y/N]: `, flushes stdout, reads
  `stdin.readline.strip.downcase`, and accepts only `y` or `n`. Blank input,
  `yes` and other text loop despite the displayed default. EOF raises.
- `--yes` returns before yielding the selection/description block, so it
  suppresses that presentation as well as the question.
- `always: true` bypasses yes, used for interactive copies/reboots and some
  generation choices. `ask_action` displays keys and loops until an explicit
  valid key; an uppercase displayed default does not make blank input valid.
- Non-TTY streams do not suppress prompts. Scripts must deliberately supply
  yes or input; a rewrite must not auto-confirm or silently stop reading stdin.

`R:lib/confctl/logger.rb` opens
`.confctl/logs/<local-time>-confctl-<command-path>.log`, records CLI metadata
and raw command logging, flushes writes, feeds optional live readers. Successful
commands unlink logs unless retained; failed attempts/health retries may retain
them. Exceptions can leave the log for inspection. Preserve raw logs separately
from rendered tables/tails and from the new timing footer.

TTY feature admission is `stdout.tty? && stderr.tty?`, unless `CONFCTL_TTY=0`
(`R:lib/confctl/ui.rb`). Redirecting either stream selects plain progress;
color selection is a separate Rainbow policy. Nonblank `NO_COLOR` disables auto
color; explicit always/never selects it. Comparison paging requires TTY
admission and nonblank `PAGER`. `CONFCTL_SSH_CONFIG` adds `ssh -F`;
nondefault SSH ports and `NIX_SSHOPTS` matter for closure copies. Under
`IN_NIX_SHELL`, App forces TMP/TMPDIR to `/tmp`. Cache honors XDG_CACHE_HOME.

### Ruby live display, concurrency and cancellation

`R:lib/confctl/cli/log_view.rb` paints stdout with TTY cursor operations,
header/title/bounded tail, shared reentrant console lock, feeder and renderer
threads; renderer checks at 0.1 seconds, strips line ends, replaces tabs with
two spaces, truncates to width, reacts to WINCH. It clears/repaints the screen;
stop joins its threads and restores WINCH to default. `flush` is a one-second
wait, not a byte-drain guarantee. Auto-size reserves operation rows but enforces
at least ten tail rows; tiny-terminal behavior is not a proven contract.

| Operation | Ruby TTY presentation | Plain presentation |
| --- | --- | --- |
| Build | Command/build-group/full-log header, live raw-log tail, overall `nix build` plus Building and Fetching bars | Header and `[build|fetch] progress/total path` lines |
| Single/bulk copy | Live tail, copy bar(s), per-host bars in bulk | `[host] [i/n] path`, failures |
| Activate | Deploying-to header and live command log | Log view disabled; retain command/error behavior from actual runner |
| Reboot | Spinner, seconds left or elapsed, final online duration | Waiting/time-left lines, final online duration |
| Health | Full-log locator, tail of per-check progress, checks bar | Descriptions, retries, success/error, final summary |
| Parallel SSH | Executing header, log tail and aggregate command progress | Executing line, final per-host/aggregated output |
| GC | Per-host and aggregate bars, tail of GC progress | Host-prefixed progress and result/failure summary |

`R:lib/confctl/nix_build_flake.rb` parses human Nix stderr: old/new summary
forms, `building '...'`, `copying path '...'`; work may arrive before totals,
so zero total means indeterminate. Copy and GC parse their own human progress.
These are progress observations, not elapsed-time measurements.

`R:lib/confctl/parallel_executor.rb` queues work, starts the requested thread
count, joins all workers; return array is completion order. App enables
Thread.abort_on_exception. Core confctl contains no unified cancel token,
stdin owner or INT/TERM process-group protocol. TTY-command and interactive
Kernel.system govern child behavior; exact real signal exits/descendant joins
need later tests. Do not label the richer historical Go cancellation contract
as a proven Ruby implementation guarantee.

## Core files, persistence and remote boundaries

| Responsibility | Ruby sources at R |
| --- | --- |
| Entrypoint and command registry | `bin/confctl`, `lib/confctl.rb`, `lib/confctl/cli.rb`, `cli/{app,command,cluster,generation,configuration,gen_data}.rb` |
| Configuration and selection | `conf_dir.rb`, `settings.rb`, `machine{,_list,_status,_control}.rb`, `cli/{attr_filters,tag_filters,output_formatter}.rb`, `pattern.rb` |
| Nix external operations/progress | `nix.rb`, `nix/args.rb`, `nix_build_flake.rb`, `nix_copy.rb`, `nix_collect_garbage.rb`, `system_command.rb`, `std_line_buffer.rb`, `line_buffer.rb` |
| Input changes and comparison | `cli/inputs/*.rb`, `flake_lock{,_diff}.rb`, `inputs_info.rb`, `inputs/*.rb`, `git_repo_mirror.rb` |
| Persistence/retention | `generation/{build,build_list,host,host_list,unified,unified_list}.rb`, `gcroot.rb`, `utils/file.rb` |
| Health | `health_checks.rb`, `health_checks/{base,run_command}.rb`, `health_checks/systemd/*.rb` |
| UI/log/extensions | `ui.rb`, `cli/log_view.rb`, `logger.rb`, `null_logger.rb`, `parallel_executor.rb`, `user_script.rb`, `user_scripts.rb`, `hook.rb` |
| Installed remote helpers | `libexec/auto-rollback.rb`, `nix/modules/confctl/carrier/carrier-env.rb`, `carrier/netboot/build-netboot-server.rb`, `kexec-netboot/kexec-netboot.rb` |

The above paths are under `lib/confctl/` unless shown otherwise.

Persistence is not stateless merely because README describes the tool that way:
`.confctl/generations/<host-with-slashes-replaced-by-colons>/<generation>/`
contains `generation.json`, `toplevel`, `auto_rollback`, `<role>.input` links,
with host `current` symlink. JSON accepts only explicit `mode: "flakes"` and
keeps `date`, `toplevel`, `auto_rollback`, `inputs`, `inputs_info` (also accepts
`inputsInfo` when reading). Names are local `%Y-%m-%d--%H-%M-%S`; saved date is
ISO8601. GC roots use the real configuration path SHA256 prefix (8 hex), login,
escaped host, generation and suffix; moving cwd can change the root namespace.
Sources: `R:lib/confctl/conf_dir.rb`, `R:lib/confctl/generation/build.rb`,
`R:lib/confctl/generation/build_list.rb`, `R:lib/confctl/gcroot.rb`.

Unsupported/malformed generations are warned about and excluded, with files and
roots untouched. Numeric local selectors refuse when exclusions make inventory
ambiguous. Invalid current links block current/old/rotation rather than silently
selecting another generation; absence of a link may select newest supported
generation. Successful builds may update current. Remote-only listing/removal
remains independent. `R:spec/generation/build_modes_spec.rb` and
`R:docs/swpins-to-flakes.md` establish backward readability/rollback constraints.

`R:nix/flake/mk-confctl-outputs.nix`, `nix/modules/cluster/default.nix` and
confctl Nix modules own public outputs/options and generated metadata. Preserve
`confctl.lib.mkConfctlOutputs`, channels/overrides and machine keys, pure flake
default, optional impure legacy NIX_PATH bridge, moduleOptions and module exports.
`R:lib/confctl/nix.rb` invokes Nix eval/build JSON, disables lock writes/updates,
retries recognized unsupported-flag/experimental-feature errors, batches build
outputs and creates/reuses generations. Do not change Nix argv/retry policy as
an incidental language port. Normal builds never intentionally update inputs.

Remote contracts include `/run/current-system`, system/carrier Nix profiles,
`/etc/confctl/{inputs-info,configuration-info}.json`, closure-copy behavior,
auto-rollback helper/check-file states (`switching`/`switched`/`confirmed`),
netboot JSON/boot paths and carrier onChange commands. `MachineControl` executes
literal argv locally; remote argv is shell-quoted into one SSH command argument,
root login, extra options before host. Copy runs nix-copy-closure and preserves
nondefault port behavior. Reboot polls uptime using fixed connection timeouts.
Mixed old/new nodes and rollback need these existing files/programs readable.

The helper surface is distinct from the 29 main actions:

| Helper | Arguments/options to retain in scope |
| --- | --- |
| auto rollback | `[-t/--timeout <Integer>] <toplevel> <action> <check-file>`, `-h/--help`; existing system switch/confirm/rollback effects |
| carrier-env | `-p/--profile <path>` plus `--set <generation>` or `--delete-generations <generations>`; invokes nix-env then configured onChange command |
| build-netboot-server | Carrier config/profile consumer and index/boot tree generator; no main-confctl action |
| kexec-netboot | `-s/--server-url`, `-m/--machine`, `-g/--generation`, `-v/--variant`, `-i/--interactive`, `-a/--append`, `-e/--exec`, `-u/--unload`, `-y/--no-sync`; defaults to boot-server/latest generation selection, rejects exec+unload, interactive choices/download/load and existing cleanup semantics |

## Exact historical Go elapsed-time behavior to adopt

Authority: **G `internal/core/invocation_timing.go`, `cli.go`,
`internal/ui/live.go`, `internal/core/live_view_linux.go`,
`docs/live-operations.md`**. Historical design:
`../2026-10-09-evaluate-confctl-rewrite-language/invocation-timing-design.md`.
The design's IT-F1 correction resolves the executable's final signal status
before freezing/rendering the footer. This is implemented historical feature
behavior, not merely an unimplemented proposal, but not default/deployed Ruby.

- One ledger per admitted invocation. Start captured at Main entry, before
  parse/setup, so accepted command Total includes that earlier time. Admission
  follows successful parse/help/availability checks, before Engine/log creation.
- Admitted: build, status, deploy, health-check, SSH remote-command mode,
  test-connection, collect-garbage, generation rm/rotate (even without actual GC).
  Excluded: interactive SSH (exactly one positional arg), CSSH, help/version,
  parse/availability rejection, comparisons/input/data/list/other commands.
  Zero-arg SSH keeps its existing command-mode/error admission edge.
- Monotonic elapsed intervals; local wall timestamps for display. Nested and
  parallel calls in the same phase are **unioned**, not summed. Work unions all
  work phases; prompt wait independently unions actual blocking line reads.
  Prompt/work overlap is retained. **Other = max(Total − (Work + Prompt −
  Overlap), 0)** before rounding. Separate phase totals may overlap, so summing
  phases is not Total. Duplicate ends and post-finish changes do not alter the
  frozen result. No per-path, per-derivation or separate Fetch timing.

| Phase, in footer order | Actual timed boundary at G |
| --- | --- |
| Evaluation | Each actual Nix eval child call after admission through joined run return; `build_nix.go` and `engine.go` |
| Build | Each actual Nix build child call, includes fetching inside that child; retries timed individually |
| Copy | Each deploy copy call through return |
| Deployment | Actual activate/rollback-activate/set-system-profile/set-carried-profile calls; no encompassing double-counted deploy timer |
| Status checks | Status query batch through worker join; deploy target-query calls |
| Reboot wait | Actual reboot-and-wait body, including down/up waits and no-wait path |
| Health checks | Each real health round through runner join, including cooldown; ends before view close/retry decision |
| SSH commands | Each remote-command runner invocation through return, unioned across parallel hosts |
| Connection tests | Each actual connection runner call through return |
| Garbage collection | Prepared GC execute call through return, including GC reached by rm/rotate |

Prompt timing wraps the existing line-read function exactly once; it does not
invent a simultaneous prompt/work operation or change queued-input/EOF/cancel
behavior. Decode, formatting, local mutation and cleanup outside listed calls
are Other. Instrumentation does not depend on a TTY/view and adds no scheduler,
observer process, dependency or persistent format.

Live header inserts `Started: <local RFC3339>  Elapsed: <whole-second duration>`
after Command and before operation/group/Full log. Full log remains last.
Elapsed updates from existing paint ticks, includes prompt suspension time on
next paint, and is not a CPU-time estimate. Format truncates: `0s`, `1m 1s`,
`1h 0m 1s`. Zero StartedAt disables the line. At 80x24, four headers cap tasks
at five including overflow, leaving twelve log rows; tiny frames can omit the
timing line. Close emits missing rows/locator as required but no replayed
header/timing block. One terminal painter remains owner; no timing key reader.

Final report goes to the **original stderr exactly once**, after operation,
input/view/child joins and log cleanup. It is present for redirection or disabled
TTY, with no environment opt-out and no periodic plain timing lines. Stdout,
JSON, child captures/logs and ordinary diagnostics keep their bytes. Exact G
grammar (including initial separating LF and terminal LF):

```text

Timing: completed (exit 0)
  Started: <local RFC3339>
  Ended: <local RFC3339>
  <seen work phase in the table's order>: <duration>
  Prompt wait: <duration>
  Prompt/work overlap: <duration, only if positive>
  Other: <duration>
  Total: <duration>
  Note: phase times overlap; total is wall time.
```

Only seen work phases print; Prompt wait/Other/Total always print. The Note is
conditional on sum(phase durations) > Work. Duration formatting truncates to
exactly three fractional digits: `0.012s`, `1m 1.000s`, `1h 0m 1.000s`.
State is completed for exit 0, failed for nonzero, canceled for actual cancellation
with `(exit N)` matching final executable status. Individual failed connection
tasks can still appear under completed/exit 0. Normal Go executable maps INT and
TERM to 1; prototype maps INT to 130, TERM to 143. These are distinct historical
entrypoint policies, not a requirement to create a Rust prototype.

Footer-write failure returns 1 if otherwise successful, preserves an existing
nonzero result, does not recurse/retry; a failed write cannot promise a complete
footer. Final freeze precedes write. The report measures through cleanup, not
its own write. User adoption of timing therefore deliberately changes Ruby
stderr, which must be documented narrowly instead of normalizing all stderr.

The same G change fixes canonical live row order: Building, Fetching, optional
observed nix-build, nix-eval, regardless of registration timing; overflow chooses
priority membership then renders canonical order. It is useful historical TUI
evidence, not elapsed accounting from display counters.

## Packaging, tests and GitHub workflow inventory

| Surface | Baseline R evidence and rewrite acceptance relevance |
| --- | --- |
| Main package | `nix/package.nix`: shell wrapper exporting Ruby GEM_HOME/GEM_PATH/RUBYLIB/PATH and executing bin/confctl; Bundler env from lock/gemset, git/openssh/nix runtime tools. Replacing the main executable alone leaves remote/helper Ruby in scope. |
| Flake platform/API | `flake.nix`: packages/devShells on x86_64-linux and aarch64-linux; RSpec check both, VM framework/tests/test-runner x86_64 only. Public lib/module/check/test outputs are consumer API. |
| Configuration shell modes | `nix/flake/mk-config-devshell.nix`: minimal, tools, bundled-confctl, optional legacyCompat; pinned package/man path plus different Bundler bootstrap/command precedence. `mk-confctl-devshell.nix` bootstraps development Bundler and formatter tools. Keep actual downstream shell compatibility visible in plan. |
| Ruby packaging/docs | `confctl.gemspec`, Gemfile/lock/gemset, Rakefile. Runtime Ruby requirement >=3.3 vs stale AGENTS style target 3.1; package prefers Ruby 3.4. Rake generates md2man and option references. GPL-3.0-only; notices/helper packaging remain deliverables. |
| Hooks/formatting | `.overcommit.yml` enables Nixfmt/RuboCop; `.git-hooks/pre_commit/nixfmt.rb`, `.rubocop.yml`, `.editorconfig`. Existing Nix formatting continues during a Rust change; Rust formatting/tests require new planned workflow/package wiring, not an existing baseline claim. |
| Fast source tests | `spec/`: configuration initialization/add/rename/removed-route rejection; Nix flake JSON/options/impurity behavior; input update/set/commit output and cached fallback guard; exact SSH quoting/options; runnable/health selection; current-deploy skipping; status unknown/offline/input revisions; generation schema/excluded/current/root safety. Run context declared in AGENTS; none run here. |
| VM test registry | `tests/all-tests.nix`: carrier/deploy, carrier/netboot, deploy/flakes, auto_rollback. `tests/make-test.nix` + runner extensions supply fixtures/native framework. `test-runner.sh` delegates to `nix run .#test-runner -- ...`. |
| VM behavior coverage | `tests/suite/deploy/base.nix`: both NixOS/vpsAdminOS; copy-only, four activation actions, repeated-current skip/reboot, named/current/numeric generation, one-by-one/dry-first, status/comparison, inputs commit/update, health, generation listing, SSH/connectivity. Carrier tests cover separate standalone/carried profiles, repeat skip, preservation across updates; netboot tests cover index input metadata/PXE/kexec selected/latest. auto_rollback covers address/route/link failures and restored profiles/system. |
| Hosted Ruby tests | `.github/workflows/rspec.yml`: every push, ubuntu-latest, Ruby 3.3/3.4/4.0 matrix, checkout@v7, install-nix@v31, gcroot setup, Ruby bundler cache, bundle exec rspec. contents:read. |
| Hosted lint | `.github/workflows/rubocop.yml`: every push, ubuntu-latest Ruby 3.4, checkout@v6, bundler cache, RuboCop parallel/force-exclusion. |
| Native infrastructure tests | `.github/workflows/tests.yml`: path-filtered push + workflow_dispatch, self-hosted, 360-minute job; `./test-runner.sh test -f --jobs auto -t ci --state-dir ...`, optional stop-on-failure, log upload/evaluation/summary and runner-state cleanup. VM/host operations are not appropriate for this inventory. |

Go tests worth translating as behavior specifications, all at G:

| Existing test owner | High-value assertions for the Rust plan |
| --- | --- |
| `internal/core/invocation_timing_test.go` | Nested/same-phase union, 32 parallel callers unioned, prompt union/overlap/residual, offset-independent duration, nil/zero/frozen/duplicate-end behavior, exact footer and duration, write-failure precedence including 130/143, real SSH call boundary/result identity, buffered answers/EOF. |
| `internal/core/invocation_timing_cli_test.go` | Admission/exclusion, redirected success/errors and untouched body, local timestamp/cancellation, one final exit-policy decision after cleanup, strict terminal footer splitter rejecting malformed/duplicate suffixes. Preserve raw stderr separately from parsed footer. |
| `build_nix_test.go`, `build_test.go`, `build_presentation_test.go` in internal/core | Per-attempt Nix eval/build timing; runner admission/failure; prompt read/Engine clone; canonical rows through early eval/late build registration. No timers inferred from parser events. |
| `connection_timing_test.go`, `deploy_timing_test.go`, `generation_timing_test.go`, `health_timing_test.go`, `status_timing_linux_test.go` in internal/core | Actual boundary ends before formatting/diagnostics, error/result identity, failed-host exit-0 policy, no work phase on pre-run refusal, reboot and query joins, cooldown in health round, generation without GC, queued prompt input. |
| `internal/ui/live_timing_test.go` | Atomic immutable display-rank validation; priority membership/canonical output; elapsed formatting; four-header/five-task/twelve-log 80x24 geometry; tiny/no-log/color/Close behavior. |
| `internal/core/live_view_linux_test.go`, `build_status_delivery_linux_test.go` | Elapsed visibly advances while an actual held child is alive; catch-up after prompt, raw footer once and after joins. Final-frame tokens alone do not prove live progress. |
| `cmd/confctl/main_test.go`, `cmd/confctl-go-prototype/main_test.go` | Actual signal-exit helper policy, single consumption, resolved footer matching executable exit. Historical acceptance additionally ran real INT/TERM executable cases; helper-only tests do not establish OS signal/process behavior. |

## Acceptance gaps and disposition for the lead

This inventory establishes source coverage and immutable reference anchors; it
does not claim runtime parity, fresh CI success, deployed identity or readiness
to implement without the architect's brief.

1. Capture executable Ruby help/routes/option parsing before committing to exact
   compatibility: abbreviation/ambiguity, help/version, options after args,
   negative switches, `--`/remote argv, surplus/omitted args, Integer parsing,
   underscore/hyphen alias behavior. The matrix is complete for App registrations.
2. Decide discrepancies explicitly: manual-only `--outdated`; `allow_shared`
   declaration versus hyphenated docs/error; Ruby template/rename quirks; exact
   framework diagnostics and path-bearing logs. Do not silently preserve every
   apparent bug or silently reinterpret it as a new feature.
3. GC source has a specific unresolved inconsistency:
   `R:lib/confctl/cli/generation.rb:run_gc` calls `progress.line`, but
   `R:lib/confctl/nix_collect_garbage.rb:Progress` exposes `path` and `to_s`,
   with no `line` reader. This is static evidence of a reached-path risk,
   not a runtime-reproduced finding. Keep normal/error/empty GC cases in parity
   acceptance and resolve via the design owner rather than adding scope here.
4. Capture independent stdout/stderr with either/both redirected, forced/plain
   TTY, color/NO_COLOR/PAGER combinations, success/failure/EOF/cancel, plus live
   resize/small frames. Adopt the timing appendix explicitly; do not hide all
   stderr or compare only normalized final screens.
5. Verify real child/process joins, INT/TERM statuses, interactive SSH terminal
   ownership and failed-host semantics. Baseline does not contain a single
   explicit process-owner abstraction, so source inspection is insufficient.
6. Preserve on-disk generations/links/roots and current selection both ways,
   old-node metadata absence, system/carrier profiles, rollback handshake,
   netboot and configuration shell exports. Helpers and arbitrary in-process
   Ruby extensions need deliberate scope/disposition; no automatic migration
   or new protocol is inferred by this inventory.
7. User requested maintained Rust crates/GitHub tests/formatting: these are
   architect/other-owner selections, not evidence that baseline already has a
   Rust toolchain/workflow. This package does not choose architecture/crates.

Lead owns state/plan/portal registration and serialized commits. Only this file
was written. No application checks were selected or run, no fetch/push occurred,
and the session remains open. Static readback counted all 29 App action
registrations, checked report whitespace and confirmed the cited Ruby/Go objects
exist in the canonical bare repository. This is inventory validation, not
application/runtime test evidence.

Handoff: [stable session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-17-confctl-rust-rewrite-plan/).
Lead can register this completed artifact and reconcile it into architect0's
design. No evidence-package blocker remains; exact parser/terminal/deployment
acceptance gaps above belong to subsequent planned execution.
