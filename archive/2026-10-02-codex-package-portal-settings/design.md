# Codex package assembly and portal settings design

Status: implementation brief, 2026-10-02. Prepared by architect0 using the
retained design role (GPT-6 Astra, xhigh, workspace_write). The external lead
owns implementation assignment, revision propagation, verification, review and
deployment. This document records planned checks, not completed verification.

## Scope and evidence

Repair ordinary Codex startup by assembling the complete package around the
unchanged upstream native binaries. Export
`dev-workspace.lib.mkCodexPackage { pkgs; codex; }` and use it for both the
workspace-private Codex and aitherdev's `codex`/`codex-ds`. Freeze llm-agents at
`6334544a4bfd921086a252caccc6c1c6eb1d18c7` (0.160.0) throughout the consuming
dependency graph. Remove the portal's unsaved-settings notice, retain its draft
and Apply/Cancel semantics, and keep status below the controls.

The assembly reference is [llm-agents PR #9889](https://github.com/numtide/llm-agents.nix/pull/9889),
with the [0.160.0 package-builder contract](https://github.com/openai/codex/blob/rust-v0.160.0/scripts/codex_package/README.md)
as the upstream layout reference. [PR #10132](https://github.com/numtide/llm-agents.nix/pull/10132)
includes that layout plus a Rust daemon-lifecycle change; the latter is outside
this initiative. Do not switch to either PR's moving head, patch Rust, rebuild
Codex with different flags, replace daemon copying with store execution, or
change the upstream updater as part of assembly.

Inspected local evidence:

- Generic runtime base: `869b8d4728394127ba949dc76724dce56eae136b`.
- Initially observed 0.160.0 input: `/nix/store/a3gjgsziqlvgz5lq20vwkcnmg914qdcl-codex-0.160.0`;
  llm-agents source: `/nix/store/sz8z8lsh59fx3zjb45rhyaadjzl836xv-source`.
- The input's native executables are in `libexec/codex/bin/`: `codex`,
  `codex-code-mode-host`, and `logs_client`. Public `bin/codex` is a shell
  wrapper with an absolute target in the input package. Bash, fish and zsh
  completions already exist in `share/`.
- The input has no `codex-package.json` or bundled `rg`; its `bwrap` is an
  absolute symlink outside the package root. Reusing its public launcher
  verbatim would continue executing the incomplete input package.
- The live-settings controller is in `portal/internal/web/static/app.js`;
  `team_settings_browser_test.cjs` already covers draft persistence, Cancel,
  successful Apply, stale polling and unconfirmed failed saves.
- The lead verified the complete GitHub trees for 0.159.2
  (`ff6aec96948b70d94983af2641a6b67c94faeff5`) and 0.160.0
  (`a956835d020762cb2b570053af06f643a11c0ecc`): each contains 73 SQL files,
  with identical paths and Git blob SHAs across all of them. This supersedes
  the initial main/queue/thread-history-only comparison. It establishes no
  SQL-file change, not general old-reader compatibility.

Shell DNS and Nix daemon access are unavailable in the architect's sandbox.
Direct PR #9889 patch retrieval was unsuccessful; the lead must retain its
previously inspected diff or provide a readable copy for the implementation
packet. The PR #10132 description and selected-version package guide confirm
the package layout. No build, daemon, real-state or browser probe was run here.
The initially observed 0.160.0 output disappeared before a later `--help`
inspection; its cause is unknown. Realize and retain the candidate closure
before verification rather than assuming an earlier cached path still exists.

## Interfaces, files and ownership

All feature paths below are relative to their dedicated worktrees under
`worktrees/2026-10-02-codex-package-portal-settings/`.

| Repository | Implementation surface | Boundary |
| --- | --- | --- |
| dev-workspace | `nix/codex-package.nix` (new), `flake.nix`, `flake.lock`, focused package check under `nix/tests/` | Export helper; pass assembled Codex to the existing `mkPackage` constructor. Keep its private `libexec/codex` interface. |
| dev-workspace | `portal/internal/web/static/app.js`, `static/style.css`, `templates/session.html`, `team_settings_browser_test.cjs` | Presentation and focused browser assertions; preserve settings API and controller state machine. |
| dev-workspace | A focused disposable Codex state-compatibility fixture under `test/` | Upgrade/old-reader gate with explicitly supplied old/new executables and private synthetic state; no production access. |
| dev-workspace | README Nix interface, `docs/workspace-portal.md` or a linked package-contract page, relevant session-runtime paragraph | Authoritative reusable package/GC contract and supported upgrade checks. |
| vpsfree-cz-configuration | `cluster/cz.vpsfree/machines/aitherdev/config.nix`, channel-owned lock updates | One assembled `codexPackage` used by system packages and `codexDs`; existing key/profile behavior unchanged. |
| vpsfree-cz-configuration | `docs/operations/codex-deepseek-aitherdev.md` and a linked site operation page if useful | Site use, version checks, retention and recovery; no copy of the generic assembly implementation. |
| vpsfree-dev-workspace | `flake.nix`, `flake.lock` | Exact generic-runtime pin only; preserve site configuration and extension catalogs. |
| workspace | Feature-worktree `flake.nix`, `flake.lock` | Exact extension pin and full consuming package; preserve site/team/provider configuration. |
| workspace tracking | This `design.md`; lead-owned plan/state/portal records | Exact rollout evidence and pending gates remain with this session. |

The architect edits only this document. The implementer owns application edits;
the lead owns short dependent pin/coordination steps and sends consequential
deviations back through design. No codex-web changes are planned. A failed
protocol check is a scope decision for the lead, not permission to relax the
validator or update codex-web opportunistically.

## Assembly contract

The helper takes the consumer's `pkgs` and an already selected upstream Codex
derivation. It returns a lightweight assembled derivation with the input
version, an executable public `bin/codex`, public helper commands, completions,
and the complete runtime root at `$out/libexec/codex`.

```text
bin/codex                         launcher into this output's runtime root
bin/codex-code-mode-host          launcher/link to the copied native helper
bin/logs_client                  launcher/link to the copied native helper
share/...                        existing shell completions
libexec/codex/
  codex-package.json
  bin/codex                      native executable, not the input wrapper
  bin/codex-code-mode-host        native executable
  bin/logs_client                 retain the existing extra public helper
  codex-path/rg                   materialized executable
  codex-resources/bwrap           materialized executable on Linux
```

Generate metadata with `builtins.toJSON`, matching the upstream package
builder's fields: `layoutVersion = 1`, `version = codex.version`, the host Rust
`target`, `variant = "codex"`, `entrypoint = "bin/codex"`,
`resourcesDir = "codex-resources"`, and `pathDir = "codex-path"`.
For this rollout the target is `x86_64-unknown-linux-gnu`, not a musl release
target. Derive it from the host platform, never the build host or a literal
shared between unlike architectures. No new platform support is advertised:
the existing runtime exports and deployment checks cover x86_64-linux. Reject
unsupported input/platform layouts clearly rather than selecting an arbitrary
executable. Broader platform support requires its own evidence.

Use `pkgs.runCommand` or an equivalent assembly derivation consuming the exact
Codex output. Do not override its Rust derivation. Copy the native `bin/`
contents from the known input runtime root, preserving executable bits and
bytes. Copy resources that the input supplies and supply `pkgs.ripgrep` and,
on Linux, `pkgs.bubblewrap` at their canonical locations. Dereference both file
and directory links during materialization (`cp -RL` semantics); fail on
dangling links or cycles. The simplest invariant is **no symlinks anywhere
inside the runtime root**, including the manifest. Check it after assembly,
not just for the two named helpers. Do not add shell-zsh-fork support or other
optional upstream resources that are absent from the selected package.

Outside the runtime root, public helper links and completion links are allowed.
Regenerate the public Codex launcher to execute this output's native binary,
forward every argument and exit status, and preserve the existing bubblewrap
PATH behavior. It must never exec the original input's `bin/codex`. Copy or
link the existing completion tree; no Rust rebuild or regenerated completion
behavior is needed. Keep normal `codex`, `resume`, `fork`, `exec`,
`app-server`, `completion`, and `--version` interfaces.

`mkPackage` should assemble exactly once before passing `codex` to
`nix/workspace-portal.nix`. Its current
`$workspace/libexec/codex -> $assembled` reference remains valid, including
`$workspace/libexec/codex/bin/codex`. In configuration:

```nix
codexPackage = flakeInputs.${devWorkspaceInput}.lib.mkCodexPackage {
  inherit pkgs;
  codex = llmAgentsPkgs.codex;
};
```

Use `codexPackage` for `environment.systemPackages` and
`${codexPackage}/bin/codex -p ds "$@"` in `codexDs`. Do not install the
workspace application through the system configuration.

## Nix closure, daemon copies and version ownership

Materializing executable files does not make them statically linked. Preserve
their ELF interpreter, RPATH and store references; Nix's output reference scan
must retain those dependencies in the assembled closure. Do not strip store
references, repatch the binaries or disable reference scanning. Verify the
copied entrypoint, helpers, rg and bwrap against the input files and inspect the
assembled output's requisites. A filesystem link ban within the runtime root
does not ban ELF references to the Nix store.

Upstream may copy that runtime root below
`$CODEX_HOME/packages/app-server-daemon/`. Those ordinary files **are not Nix
GC roots**. Existing workspace retention resolves the selected command to its
own store output and roots it at
`~/.local/state/dev-workspaces/codex/{current,generations/<generation>}`.
The new launcher must therefore resolve within the assembled output. Retained
roots then retain the scanned dependency closure used by daemon copies.
System generations independently retain the system package and its closure.
The two consumers can use different dependency closures despite an identical
Codex version; prove retention for both, not merely equality of version strings.

Do not prune existing workspace Codex roots or system generations in this
initiative. Before an eventual generation cleanup, the operator must establish
that no remaining daemon copy needs that closure, or retain the exact
assembled output independently. No production garbage collection is needed to
prove this: inspect references/requisites and root links.

The immutable package pin governs the workspace's explicit App Server and
terminal pair. It does not by itself turn upstream's mutable native-daemon
release selection/updater into a Nix-managed service. Plain CLI startup may
encounter a pre-existing daemon release. Test and record the selected native
daemon version separately. A release different from the tested 0.160.0 is a
deployment concern to resolve through the lead; do not quietly patch upstream
lifecycle, rewrite `current`, or claim the native daemon is permanently pinned.

## Portal settings presentation

Keep the settings controller's draft key, valid-pair logic, dirty/saving state,
write-generation checks, confirm-on-read recovery, and API calls intact. In
`render()`, dirty alone produces no status text. Preserve the current saving
and unconfirmed-save messages. Set both status text and `hidden` consistently
on every render/transition, including an in-flight save; changing text directly
without clearing `hidden` would hide saving feedback.

Move `#codex-settings-status` outside `.composer-controls`, below the desktop
`.chat-actions` controls. It begins hidden, remains an `aria-live="polite"`
status, wraps long error messages and occupies no space when empty. Retain
its ID and existing button/select IDs. Scope CSS to this status/control row
rather than altering all `.lane-status` elements or collaboration-mode notices.

At 1280 and 1440 CSS pixels, the visible action controls must fit on one row
with the ordinary sidebar: attachment/send group, available mode control,
Model, Reasoning, Apply, Cancel and Interrupt. Size/shrink the selects and gaps
locally if needed; do not force fixed widths that cause horizontal scrolling.
At existing narrow breakpoints, preserve wrapping and readable labels. Apply
and Cancel remain visible with their existing enablement; dirtiness is conveyed
by available actions without a replacement warning.

Add only focused assertions to `team_settings_browser_test.cjs`:

1. Clean and dirty states have empty, hidden settings status. Selecting model
   and effort sends no request; Apply/Cancel enable. Drafts survive focus and
   reload, and Cancel restores the last confirmed pair and hides status.
2. Hold one settings response with an explicit promise. While saving, status
   is visible and says the existing saving text; controls obey current
   disabling. Release it and verify success clears/hides status. Keep existing
   stale-poll protection assertions.
3. Reuse the failing-write/failing-read case: draft survives, error is visible,
   actions recover, and Cancel or a successful retry clears/hides status.
4. At 1280x900 and 1440x900, measure visible controls after layout settles,
   both dirty and with saving/error status. Their vertical intervals must
   share a row (center tolerance up to 2 CSS px for like-sized controls),
   remain within the composer bounds and not overlap. Status top must be at
   or below the greatest control bottom, allowing 1 px rounding. The status
   must not shift controls onto another row. Include realistic model/effort
   labels and a visible mode control so a short mock label does not hide a
   width regression.
5. At 390x844, confirm no document/composer horizontal overflow (1 px rounding
   allowance), visible nonoverlapping controls within the viewport, and a
   usable model change plus Apply/Cancel. Wrapping is expected. Scroll into
   view where needed; do not require a desktop row or fixed vertical position.

Use bounding-box assertions in the existing regression, not a new screenshot
framework or exact font-width snapshots. Keep screenshots only as rollout
evidence. No API, translation or knowledge-base contract changes are needed.

## Compatibility and state-loading gate

| Boundary | Contract and required evidence |
| --- | --- |
| Old package / old Codex state | Preserve the retained 0.159.2 package and source identity; known incomplete native daemon startup is not a new regression. |
| 0.160.0 reads 0.159.2 state | Exercise upgrade on disposable state, including persisted threads, resume/fork, settings and available history/queue fixtures. |
| 0.159.2 reads state written by 0.160.0 | Sequentially reopen the disposable post-upgrade state with the exact old executable; assert no migration/checksum/parse failures and preserved thread content/settings. This remains unverified until executed. |
| Portal/client versus App Server | Generate experimental schemas from the selected package and run the installed codex-web contract validator. Browser and terminal use one selected profile version. |
| Browser draft versus portal update | Keep existing storage key and value format. Existing drafts reload and Cancel/Apply remain compatible. |
| Workspace persisted formats | No session manifest, runtime authority, team registration, upload catalog, lifecycle journal or cluster schema changes. Existing transition, ownership and generation checks remain authoritative. |
| Nix/system configuration | Additive library export and consumer expression change; existing public commands and host-module options retain their interfaces. |

The lead's completed SQL comparison covers all 73 SQL files, including every
migration tree, with identical paths and blob SHAs; retain that evidence and
the two exact upstream revisions in the review packet. Do not add migrations or
schema-existence guards. Identical SQL does not cover enum variants, rollout
JSON/JSONL, queue serialization, thread-history entries, daemon settings, or
experimental RPC shapes. A parser failure or unsupported old-reader behavior
blocks real-state cutover pending a lead-approved compatibility decision.

Disposable probes use a fresh private `CODEX_HOME` and isolated sockets; they
must not inherit production authentication or connect to a real App Server.
Create synthetic threads without model turns where supported, then stop the
owned probe server before opening the same state with another version. Use
actual 0.159.2 and 0.160.0 executables, not two launchers accidentally selecting
the same native daemon. Record `--version`, initialize response/server identity,
state integrity and representative read results. Use copied synthetic fixtures
for paths that cannot be populated without a paid/network model turn.

Only after these gates pass may deployment use real state through the existing
switch procedure. Prepare the private online database baseline defined below;
it is transaction-consistent per database, not a global state restore point.
Do not log credentials, thread content or private database rows. Real-state
validation should report IDs/counts/integrity outcomes and version evidence.
No coordinated fleet upgrade or vpsAdminOS node update is required.

### Disposable reasoning-setting fixture clarification

Read-only diagnosis of `verification-runtime-4.log` and its private fixture
`/tmp/codex-package-state-1151236433` found that the failure is the **fork's**
`medium` assertion at `compat_probe.go:178`. The original thread's new-reader
`high` assertion and subsequent `medium` update/read already passed. The
original 0.159.2 rollout contains `turn_context.effort=high`, followed by
thread-owned settings snapshots with `high` and `medium`. The 0.160.0 child
contains an effective settings snapshot with null reasoning effort; the
read-only metadata query agrees (parent `medium`, child NULL). The failed run
never reached its final 0.159.2 reader. This is partial upgrade evidence, not
a passing old/new/old gate.

The initial override is persisted by this fixture's history preparation:
`inject_response_items` captures the initial context when absent and calls
`checkpoint_preparation`. Adding an initial `thread/settings/update` is not
needed to repair this failure. This behavior is present in both exact release
sources: [0.159.2 `codex_thread.rs`](https://github.com/openai/codex/blob/rust-v0.159.2/codex-rs/core/src/codex_thread.rs#L702-L745)
and [0.160.0 `codex_thread.rs`](https://github.com/openai/codex/blob/rust-v0.160.0/codex-rs/core/src/codex_thread.rs#L702-L745).

Forking is a different operation from resuming the parent. Both release
handlers load fork configuration from request overrides and normal config;
the inherited settings in this path cover approvals and permissions, without
copying the parent's model/effort. Both core implementations then persist the
effective child settings so a later resume does not mistake ancestor settings
for the child's settings. Sources:
[0.159.2 fork configuration](https://github.com/openai/codex/blob/rust-v0.159.2/codex-rs/app-server/src/request_processors/thread_processor.rs#L4781-L4882),
[0.160.0 fork configuration](https://github.com/openai/codex/blob/rust-v0.160.0/codex-rs/app-server/src/request_processors/thread_processor.rs#L4781-L4882),
[0.159.2 child checkpoint](https://github.com/openai/codex/blob/rust-v0.159.2/codex-rs/core/src/session/mod.rs#L1553-L1604),
and [0.160.0 child checkpoint](https://github.com/openai/codex/blob/rust-v0.160.0/codex-rs/core/src/session/mod.rs#L1558-L1609).
The observed null therefore matches the shared fork behavior; it does not
demonstrate loss of the parent's persisted override during upgrade.

Recommended bounded fixture correction, for the lead/implementer to apply:

- Keep the original `thread/start` override and every exact parent `high` then
  `medium` assertion. In the already restarted old-server phase, also read the
  parent and require `high` before starting the new executable. Keep the queue
  thread separate and unloaded throughout.
- Add `model: "gpt-6.1-sol"` and
  `config: {model_reasoning_effort: "medium"}` to the `thread/fork` request.
  Continue requiring the child's exact `medium` value in both the new process
  and the final cold old-reader process. This establishes an explicit child
  setting whose preservation can be tested. Do not accept null, supply a
  default in assertions, or override settings on the validating resumes.
- Keep content, queue, identity and integrity assertions. Report the phase,
  parent/fork role and expected value in failures so they cannot be confused.
  If `thread/settings/update` is used instead to initialize the child, await
  its matching applied-settings notification before checking it; the existing
  parent update remains part of the compatibility exercise.

This clarification recommends a fixture change only. It does not authorize a
probe retry, model turn, real-state access or cutover. The lead must obtain a
complete passing old/new/old run through its watcher before the deployment gate
is satisfied; no preservation assertion is waived.

### Pre-cutover baseline and recovery limits

**Recommendation:** a verified online SQLite baseline, the identical paths and
blob SHAs for all 73 upstream SQL files, the disposable old/new/old probe and
the ordinary supported switch
are proportional for this forward-only package cutover. No additional manual
quiesce, freeze, checkpoint, stop or backup hook is required. This recommendation
does **not** promise a lossless rollback of all Codex state. Normal recovery
keeps current data and moves forward to a corrected package; the baseline is
for diagnosis and narrowly reviewed salvage. If a complete point-in-time
restore is required, that is a different operational requirement and this
baseline is insufficient.

The reason for this boundary is the actual storage split, rather than the
database filenames alone:

- In both [0.159.2](https://raw.githubusercontent.com/openai/codex/rust-v0.159.2/codex-rs/thread-store/src/local/live_writer.rs)
  and [0.160.0](https://raw.githubusercontent.com/openai/codex/rust-v0.160.0/codex-rs/thread-store/src/local/live_writer.rs),
  the inspected live-writer path durably writes rollout JSONL before projecting
  paginated history into SQLite. The latter projection can lag after failure.
  This does not make every SQLite table disposable or authorize deleting a DB.
- The [selected local store](https://raw.githubusercontent.com/openai/codex/rust-v0.160.0/codex-rs/thread-store/src/local/mod.rs)
  resolves history and metadata across rollout files, the state index and
  compatibility metadata. A DB copied at one time need not agree with a
  rollout or name-index file observed later.
- [Queue storage](https://raw.githubusercontent.com/openai/codex/rust-v0.160.0/codex-rs/thread-store/src/queue_store.rs)
  is independently durable. Restoring an older queue can replay already handled
  submissions or lose newer messages, even if each database passes integrity
  checks. Workspace submission/deletion receipts add another independent state
  boundary. Goals and memories likewise must not be assumed reconstructible
  from conversation history.
- [The SQLite path contract](https://raw.githubusercontent.com/openai/codex/rust-v0.160.0/codex-rs/state/src/sqlite.rs)
  names state, queue, thread-history, logs, goals, memories and memories-v2
  stores. Resolve the actual SQLite home, including any `CODEX_SQLITE_HOME`
  override, before backing up; do not assume every store always uses the
  process's `CODEX_HOME`. Back up all existing top-level `.sqlite` files in
  that selected home, not only the three already compared migration trees.

The [SQLite online backup API](https://sqlite.org/backup.html) copies committed
database state through SQLite, including its WAL, while allowing concurrent
activity. It provides one consistent database image. Sequential backups of
several databases have different capture intervals and no shared application
transaction boundary. Do not use `immutable=1` on live inputs, copy live
database/WAL/SHM files, force a source checkpoint, or use a write lock to make
the collection appear atomic. Integrity checks prove file integrity, not
cross-store consistency or application semantics.

No project/site-wide Codex backup or public backup barrier was found in the
inspected runtime guides, `workspace-host`, or aitherdev operation guidance.
The configured root filesystem is ext4; the configuration does not establish
a usable atomic volume-snapshot workflow. Do not infer one from the host being
a VM. `workspace-host switch` performs compatibility probes before its normal
quiescence and has no supported pause between quiescence and activation. Its
transition lock is not a general lock on every Codex/native-daemon writer.
Therefore run the online baseline **before the first candidate command using
real state**, including an ordinary switch, and never insert a private hook.

Prepare the following method for the external lead, not the native observing
lead. This block is a procedure, not an action performed by the architect.
Resolve the selected SQLite directory read-only first. For the reported default
layout it is `/home/aither/.codex`; use the verified override if one exists.
Keep the destination outside Git, the portal artifact tree and `CODEX_HOME`,
with mode 0700 and files restricted by umask 077. Budget for the databases plus
WAL size and free-space margin, not another copy of the 11 GiB session tree.
Use the generic repository's pinned Python/SQLite environment and a fresh
verification watcher for an uncertain-duration execution.

```sh
sqlite_root=/home/aither/.codex
baseline_parent=/home/aither/.local/state/dev-workspaces/backups/2026-10-02-codex-package-portal-settings
nix shell --inputs-from "$generic" nixpkgs#python3 -c python3 - \
  "$sqlite_root" "$baseline_parent" <<'PY'
import datetime, hashlib, json, os, pathlib, shutil, sqlite3, sys, tempfile, time

os.umask(0o077)
source = pathlib.Path(sys.argv[1]).resolve(strict=True)
parent = pathlib.Path(sys.argv[2])
parent.mkdir(parents=True, exist_ok=True, mode=0o700)
if parent.stat().st_uid != os.getuid() or parent.stat().st_mode & 0o077:
    raise SystemExit('backup parent must be private and owned by this user')
paths = sorted(source.glob('*.sqlite'))
required = {'state_5.sqlite', 'queue_1.sqlite', 'thread_history_1.sqlite'}
if not required <= {p.name for p in paths}:
    raise SystemExit('expected stores missing; resolve SQLite home before proceeding')
if any(p.is_symlink() or not p.is_file() for p in paths):
    raise SystemExit('resolve non-regular SQLite paths before proceeding')
estimate = sum(p.stat().st_size for p in paths)
estimate += sum(p.stat().st_size for p in source.glob('*.sqlite-wal'))
if shutil.disk_usage(parent).free < 2 * estimate + 1024**3:
    raise SystemExit('insufficient backup space with safety margin')
destination = pathlib.Path(tempfile.mkdtemp(prefix='online-', dir=parent))
utc = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
record = {'kind': 'per-database-online-baseline', 'global_snapshot': False,
          'sqlite_version': sqlite3.sqlite_version, 'started_at': utc(), 'files': []}
for path in paths:
    item = {'name': path.name, 'started_at': utc()}
    output = destination / path.name
    deadline = time.monotonic() + 180
    def progress(status, remaining, total):
        if time.monotonic() > deadline:
            raise TimeoutError('database backup exceeded its time budget')
    src = sqlite3.connect(path.as_uri() + '?mode=ro', uri=True, timeout=5)
    dst = sqlite3.connect(output)
    try:
        src.backup(dst, pages=256, progress=progress, sleep=0.05)
        # Normalize only the private destination to a standalone database file.
        dst.execute('PRAGMA journal_mode=DELETE')
        if dst.execute('PRAGMA integrity_check').fetchall() != [('ok',)]:
            raise RuntimeError('backup integrity check failed')
    finally:
        dst.close()
        src.close()
    with output.open('rb') as saved:
        digest = hashlib.file_digest(saved, 'sha256').hexdigest()
        os.fsync(saved.fileno())
    item.update(finished_at=utc(), bytes=output.stat().st_size, sha256=digest,
                integrity='ok')
    record['files'].append(item)
if [p.name for p in sorted(source.glob('*.sqlite'))] != [p.name for p in paths]:
    raise RuntimeError('database inventory changed; baseline is incomplete')
record['finished_at'] = utc()
with (destination / 'complete.json').open('x') as manifest:
    json.dump(record, manifest, indent=2)
    manifest.write('\n')
    manifest.flush()
    os.fsync(manifest.fileno())
directory_fd = os.open(destination, os.O_RDONLY | os.O_DIRECTORY)
try:
    os.fsync(directory_fd)
finally:
    os.close(directory_fd)
print('Private SQLite baseline complete:', destination)
PY
```

The script reads no SQL rows for reporting and prints only the destination.
It copies sensitive database bytes privately; neither these files nor their
contents belong in the portal, Git, prompts or logs. It deliberately excludes
credential/config files, sessions, archived sessions, daemon releases, live
sockets/locks and workspace lifecycle/team/upload records. Record the exact
source/package identities separately using existing metadata-only checks.
Absence of `complete.json`, an error, busy timeout or disk-space failure means
the baseline did not complete: report it and defer cutover, without stopping
writers or discarding a partial directory. Integrity checks run on the copy,
not the live database. Record intervals and checksums from the manifest as
private operator evidence; the public session record needs only completion,
location and the explicit absence of a global-snapshot guarantee.

The 11 GiB `sessions/` tree remains in place. Its size is not a reason to call
SQLite the authoritative copy of all history. This rollout neither erases it
nor needs a full duplicate merely to change the assembly. This choice leaves
no new point-in-time backup of rollout content and supplies no host-loss or
zero-data-loss recovery guarantee. A background filesystem copy of that tree
would not repair the global consistency gap, so it is not a required extra
step. Existing independent backups, if any, remain a separate protection; none
were assumed or verified here.

Before accepting this narrower baseline, retain the already required source
review and synthetic probe evidence: identical SQL does not exclude startup
rewrites, new serialization or automatic recovery behavior. If review finds a
new destructive conversion, the compatibility probe fails, or the operator
requires whole-home rollback, defer cutover. Establish a separately approved
and documented offline or storage-snapshot operation that accounts for every
writer and all related state; no such operation is authorized by this design.
Do not manufacture that barrier with custom kills, freezes, database locks,
private lifecycle calls or another session's commands.

Safe recovery remains:

1. For package/activation failure, preserve current data, journals and retained
   roots; retry the supported forward switch or use a corrected newer package.
   Do not automatically restore baseline files or force a refused transition.
2. For suspected persisted-data damage, preserve the failing state and inspect
   copies offline first. Baseline files may support a specifically reviewed
   repair; they are not a set to overwrite live `CODEX_HOME`. Restoring a queue,
   index or history DB independently needs reconciliation against current
   rollout history, submission receipts, goal/memory state and newer writes.
3. Any actual data restore or broader maintenance must be separately scoped
   and authorized, with supported writer shutdown and validation. The
   old/new/old probe permits only its tested reader-compatibility claim; it
   does not grant permission to run an older live profile or rewind user work.

## Pin propagation, deployment and recovery

The dependency sequence is generic runtime -> extension -> consuming workspace.
Configuration separately selects the same exact generic-runtime revision and
the same llm-agents revision. Inspect the complete lock graph, including nested
llm-agents nodes. Required mappings in configuration are channel `llm-agents`,
role `llm-agents`, input `llm-agents`; and channel `dev-workspace`, role
`devWorkspace`, input `devWorkspace`.

1. Implement and quick-check the generic assembly and portal change, commit
   them, and pin the generic flake's llm-agents input exactly. No unrelated
   nixpkgs or codex-web refresh.
2. After normal fetch/rebase discipline, push only feature revisions needed by
   consumers. Update extension and consuming workspace exact pins. Preserve
   the full consuming package's site settings, providers, skills and team
   catalog. Use `confctl inputs channel set --commit` for both configuration
   input pins; keep generated lock/history commits and `--no-changelog` for
   llm-agents. Inspect expected transitive changes.
3. Complete quick checks, commit intended changes, inventory every branch's
   complete base-to-head history/final diff and migration provenance, then run
   mandatory independent review. Only after findings are resolved or accepted
   start longer checks through the lead's fresh Luna/low watcher.
4. Complete package, browser, generated-protocol and disposable-state gates;
   build only `cz.vpsfree/machines/aitherdev`. Stop an unexpected local kernel
   build and investigate. No full-fleet deployment.
5. Record exact package/store paths and current generations. Validate persisted
   session/cluster state and check for pending transition/lifecycle journals.
   Complete the online database baseline above before any candidate access to
   real state; retain its limited, per-database consistency claim.
   Do not bypass a refusal or invoke private recovery helpers. Lifecycle
   operations on this or any other session require their own exact authority.
6. Dry-activate and deploy the aitherdev system configuration from its feature
   branch. Then run the installed stable `workspace-host switch --source`
   against the **workspace feature worktree**, not generic runtime or extension
   source. The existing switch preflight, lock, quiescing and deferred retry
   behavior govern active sessions; do not kill this team to force activation.
7. Verify installed versions, retained roots, system `codex-ds`, workspace
   services, a normal native startup and portal settings. A deferred switch is
   pending deployment, not success. The lead records exact deployed heads and
   remaining readiness gates.

System recovery retains the prior system generation and uses the site's normal
configuration recovery procedure. Workspace package transitions are
forward-only: repeat the interrupted supported switch or publish a corrected
newer generation. Do not use `workspace-host rollback`, manually repoint the
profile, replace daemon release links, remove journals or restore live state
under writers. If the new Codex state cannot be read by an intended recovery
version, preserve it and route recovery through the lead; no rollback claim
may exceed the disposable-state evidence. Assembly changes neither SQL nor
workspace state schemas, so no down migration is introduced.

Deployment is authorized. Default-branch integration is not. Retain feature
refs and the active session, including after successful deployment. Completion
of this design does not authorize any session lifecycle action.

## Verification commands and acceptance

The following commands are for the implementer/lead and its watcher. They have
not been executed by the architect. Use repository-pinned Nix tools, private
temporary output paths and existing hooks. All builds, uncertain-duration test
runs, CI and deployment waits belong to a fresh Luna/low utility watcher
launched by the external lead; the watcher does not deploy or diagnose.

Use these path variables in the lead's shell:

```sh
initiative=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-codex-package-portal-settings
generic="$initiative/dev-workspace"
extension="$initiative/vpsfree-dev-workspace"
configuration="$initiative/vpsfree-cz-configuration"
consumer="$initiative/workspace"
```

Quick checks before review, from the generic worktree unless stated otherwise:

```sh
git diff --check
nix-instantiate --parse flake.nix >/dev/null
nix-instantiate --parse nix/codex-package.nix >/dev/null
nix flake check --no-build --show-trace
nix shell --inputs-from . nixpkgs#nodejs -c node --check portal/internal/web/static/app.js
nix shell --inputs-from . nixpkgs#nodejs -c node --check portal/internal/web/team_settings_browser_test.cjs
nix shell --inputs-from . nixpkgs#ruby -c ruby -c libexec/workspace-host
```

The Ruby syntax check is useful if a runtime edit proves necessary; no Ruby
change is planned. Use focused existing Go/template and Ruby/package-root tests
appropriate to the actual diff, without running a large suite inline. Before
calling any check quick, ensure its pinned environment is already available;
otherwise put realization and the check with the watcher.

Exact channel updates, after substituting the final generic feature SHA, from
the configuration worktree's Nix development environment:

```sh
confctl inputs channel ls
confctl inputs channel set --commit --no-changelog llm-agents llm-agents 6334544a4bfd921086a252caccc6c1c6eb1d18c7
confctl inputs channel set --commit dev-workspace devWorkspace "$generic_feature_sha"
```

From the consumer worktree, check the site/runtime contract and all selected
llm-agents lock-node identities before deployment:

```sh
nix shell --inputs-from . nixpkgs#ruby -c ruby bin/check-dev-workspace-deployment --configuration-root "$configuration"
```

Longer checks, launched by the lead's watcher after review:

```sh
nix build --no-link --print-build-logs "$generic#checks.x86_64-linux.codex-package"
nix build --no-link --print-build-logs "$generic#checks.x86_64-linux.package"
nix flake check --print-build-logs "$extension"
nix flake check --print-build-logs "$consumer"
nix build --print-build-logs --out-link "$consumer/result" "$consumer#default"
```

`codex-package` is the proposed focused assembly check name. It must assert
manifest values, all required executable paths, native bytes, completions,
no runtime-root symlinks and launcher destination. Include a synthetic input
with file and directory links and a missing-required-file failure so a future
copy refactor cannot silently reintroduce escaping links. Run real daemon
probes separately from sandboxed derivation checks.

Focused settings browser invocation from `$generic/portal`, using matching
Playwright modules and browsers from the same pinned nixpkgs:

```sh
driver=$(nix build --no-link --print-out-paths --inputs-from "$generic" nixpkgs#playwright-driver)
browsers=$(nix build --no-link --print-out-paths --inputs-from "$generic" nixpkgs#playwright-driver.browsers)
nix shell --inputs-from "$generic" nixpkgs#go nixpkgs#nodejs -c env \
  NODE_PATH="$driver/lib/node_modules" PLAYWRIGHT_BROWSERS_PATH="$browsers" \
  PORTAL_BROWSER_TEST=1 \
  go test ./internal/web -run '^TestQuestionBrowser/team_settings_browser_test.cjs$' -count=1 -timeout=5m
```

The real server harness needs its existing packaged review assets if that
checkout's tests require them; supply them by the repository's existing asset
build path rather than replacing the page with a synthetic settings fragment.
Run the ordinary packaged Go/Ruby/JavaScript suite once; broaden browser testing
only if shared composer CSS or a failure warrants it.

With the built consuming package, protocol/startup and closure checks:

```sh
candidate=$(readlink -f "$consumer/result")
assembled=$(readlink -f "$candidate/libexec/codex")
probe_root=$(mktemp -d /tmp/codex-package-compat.XXXXXX)
mkdir -m 700 "$probe_root/codex"
env CODEX_HOME="$probe_root/codex" "$candidate/bin/workspace-host" \
  check-codex --codex "$candidate/libexec/codex/bin/codex"
"$candidate/libexec/codex/bin/codex" --version
nix-store --query --references "$assembled"
nix-store --query --requisites "$assembled"
```

The compatibility checker generates experimental schemas, validates the pinned
client's requests, and probes a private App Server socket. Supplement it with
the new disposable upgrade/old-reader fixture and a native-daemon lifecycle
probe using the selected version's `app-server --help`/daemon subcommand
syntax. Do not guess flags from another Codex release. That probe must use the
private `CODEX_HOME`, assert the running daemon's version and copied package
layout, restart it successfully, and stop only its owned process. Run normal
CLI, resume and fork startup in an isolated PTY; an expected login/model-choice
screen is acceptable without a paid turn, a package/loader error is not.

Provide a focused Python fixture, proposed as
`test/codex_state_compatibility.py`, with this command interface (the implementer
may use the existing harness language after reporting the final command):

```sh
nix shell --inputs-from "$generic" nixpkgs#python3 -c python3 \
  "$generic/test/codex_state_compatibility.py" \
  --old-codex "$old_codex" \
  --new-codex "$candidate/libexec/codex/bin/codex" \
  --work-dir "$probe_root/state-compat"
```

`old_codex` is the exact retained 0.159.2 executable, verified and rooted before
the run. The fixture must implement the old -> new -> old sequence above, use
the existing protocol client/harness where possible, check all available
persisted stores, and assert values rather than only zero exit status. It must
fail if the work directory already contains unrelated state or either observed
server version differs. This is a runtime compatibility gate, not a schema-hash
test. Record any fixture limitation before authorizing real-state cutover.

Build/deployment command forms from the configuration development shell:

```sh
confctl build cz.vpsfree/machines/aitherdev
confctl deploy cz.vpsfree/machines/aitherdev dry-activate
confctl deploy cz.vpsfree/machines/aitherdev switch
workspace-host switch --source "$consumer"
```

The lead performs authorized mutations and delegates their long waits as the
monitor skill permits. Check the installed state with `workspace-host status`,
`dev-session validate`, `/run/current-system/sw/bin/codex --version`, the
selected profile's private Codex `--version`, and
`codex-ds --strict-config --help`; the latter must not expose its API key.

Acceptance requires all of the following:

- All consumers resolve the frozen llm-agents revision and intended generic /
  extension revisions; no unintended dependency or Rust build change.
- Public commands/completions work, all native helpers survive assembly,
  manifest version/target are correct, and runtime-root file/directory links
  cannot escape because none remain.
- A clean native daemon copy starts/restarts at 0.160.0; plain CLI, resume and
  fork no longer fail with an incomplete-package or escaping-link error.
- Copied binaries' Nix dependencies are reachable from retained assembled
  roots; retained old generations remain available.
- Generated-schema validation and disposable old/new/old state checks pass,
  with any unsupported path made explicit before real-state access.
- Settings drafts, Apply, Cancel, saving, stale refresh and error recovery pass
  the existing regression plus 1280/1440 desktop and 390px mobile assertions.
- Whole-branch independent review is complete, aitherdev dry activation and
  system activation pass, the full consuming user-profile switch actually
  completes, and live versions/services/UI are verified.
- Reusable contract and site operation docs agree with implementation; state
  records distinguish verified deployment from merge readiness. Feature
  branches remain active pending explicit integration direction.

Session: [portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-codex-package-portal-settings/).
