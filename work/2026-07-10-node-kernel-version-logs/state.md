---
lifecycle: active
---
# 2026-07-10-node-kernel-version-logs

## Repositories

- `vpsadminos`
  - branch: `2026-07-10-node-kernel-version-logs`
  - worktree:
    `worktrees/2026-07-10-node-kernel-version-logs/vpsadminos`
  - base: `origin/staging` at `ea78b11f3`
  - currently used for source/history inspection; no changes made
- `vpsfree-cz-configuration`
  - branch: `2026-07-10-node-kernel-version-logs`
  - worktree:
    `worktrees/2026-07-10-node-kernel-version-logs/vpsfree-cz-configuration`
  - base: `origin/master` at `e1cc165c`
  - head after the trusted-root simplification: `02451428`
  - implementation committed in three focused commits

## Status

- Active initiative verified through both `bin/dev-session current` and
  `VPSFREE_DEV_SESSION_SLUG`.
- Isolated worktrees are prepared and clean.
- Current and historical vpsAdminOS boot logging has been traced.
- The live `int.log` layout and a sample of retained boot records were checked
  read-only through `confctl ssh`.
- A recommended design and alternatives are recorded in `plan.md`.
- Plan revised after user feedback: the operator CLI will be a
  `vpsfree-cz-configuration` user script, not a `confctl` core feature.
- Plan revised again after user feedback: the threshold query will use the
  generic `version-since` interface and neutral version-comparison vocabulary,
  not vulnerability-specific terminology.
- User approved implementation on 2026-07-10.
- The implementation and tests are committed in `vpsfree-cz-configuration`.
- Repository RSpec, RuboCop, package build, command registration, diff checks,
  and mandatory hooks passed as quick verification.
- The mandatory standalone review completed with one Blocking, five Important,
  and one Advisory finding. All findings were addressed and folded into the
  relevant unmerged commits.
- The full `int.log` configuration build and generated rsyslog validation
  passed.
- The operator interface has been generalized as requested. The fresh
  mandatory review completed, all four findings were fixed and confirmed by
  the reviewer, and final integration verification passed.
- The branch was rebased onto current `origin/master` at `435f63d7` after its
  generated vpsAdmin services input update landed.
- A user-requested standalone read-only safety review subsequently found that
  raw source logs are read-only under the default paths, but the helper does
  not enforce this invariant against state-root overrides or symlink/hard-link
  aliases. The branch must not be deployed until this Blocking finding and the
  review's significant consistency/index-filter findings are addressed.
- User authorized implementation of the read-only safety-review remediation;
  the fixes are committed on the same unpublished feature branch and await
  mandatory standalone review plus final integration verification.
- On 2026-07-13, the user clarified that `int.log` is a trusted,
  root-operated environment and requested that the helper be simplified. The
  branch was rebased onto `origin/master` at `e1cc165c` with the mandatory
  pre-rebase hook. The revised design keeps atomic separate live/backfill
  indexes and raw-log read-only behavior under production paths, but removes
  adversarial path-alias hardening and the retained-file coverage scan.
- No push or deployment has been performed.

## Commands run

- `bin/dev-session current`
- `git status --short --branch`
- `bin/dev-session worktree add 2026-07-10-node-kernel-version-logs vpsadminos --as-is`
- `bin/dev-session worktree add 2026-07-10-node-kernel-version-logs vpsfree-cz-configuration --as-is`
- `git status --short --branch` and `git remote -v` in both worktrees
- read both repository-local `AGENTS.md` files
- `rg` searches for kernel boot messages, rsyslog forwarding, `int.log`, and
  log rotation in both repositories
- `git log`, `git blame`, and `git show` around vpsAdminOS boot/version and
  rsyslog history
- inspection of:
  - `vpsadminos/os/modules/misc/version.nix`
  - `vpsadminos/os/modules/services/logging/rsyslog.nix`
  - `vpsadminos/os/modules/system/boot/stage-2-init.sh`
  - `vpsadminos/os/livepatches/available-patches.nix`
  - `vpsadminos/os/livepatches/ebpf/available.nix`
  - `vpsfree-cz-configuration/cluster/cz.vpsfree/containers/prg/int.log/config.nix`
  - `vpsfree-cz-configuration/modules/system/logging/{shared,vpsadminos}.nix`
  - `vpsfree-cz-configuration/configs/node/base.nix`
  - `vpsfree-cz-configuration/scripts/runtime_kernels.rb`
- `nix develop -c confctl --help`
- `nix develop -c confctl ssh --help`
- `nix develop -c confctl ls 'cz.vpsfree/nodes/*/*'`
- read-only `confctl ssh` commands on `cz.vpsfree/containers/prg/int.log` to:
  - list node log files and sizes;
  - sample both kernel boot marker formats from `stg/node2`;
  - count node log files and summarize per-node disk use.
- `nix develop -c bundle lock`
- `nix develop -c bundle exec rspec spec/scripts/kernel_boots_history_spec.rb spec/packages/node_kernel_boots_spec.rb`
- `nix develop -c bundle exec rspec`
- `nix develop -c bundle exec rubocop`
- `nix develop -c nixfmt packages/node-kernel-boots/default.nix overlays/packages.nix cluster/cz.vpsfree/containers/prg/int.log/config.nix`
- `nix build --impure --no-link --expr <node-kernel-boots package expression>`
- `nix develop -c confctl kernel-boots --help`
- `nix develop -c confctl kernel-boots list --help`
- `nix develop -c confctl kernel-boots fixed-since --help`
- `nix develop -c confctl kernel-boots version-since --help`
- `nix develop -c confctl kernel-boots backfill --help`
- `nix develop -c bundle exec overcommit --install`
- `nix develop -c bundle exec overcommit --sign`
- `nix develop -c bundle exec overcommit --run`
- three commits using `nix develop -c git commit -F <tempfile>`
- `GIT_SEQUENCE_EDITOR=true nix develop -c git rebase -i --autosquash origin/master`
- `nix develop -c confctl build -y 'cz.vpsfree/containers/prg/int.log'`
- generated rsyslog validation with the built system's
  `rsyslogd -N1 -f <generated-syslog.conf>`
- an isolated `env -i` backfill with the helper from the final built system
- `git fetch origin`
- `nix develop -c git rebase origin/master`

## Results

- The shared workspace checkout had unrelated changes before this initiative;
  they were not touched.
- Both canonical project remotes already use SSH.
- `vpsadminos` fetched a newer `origin/staging` and the worktree was created at
  `ea78b11f3`.
- The configuration worktree checkout hook initially reported missing bundled
  Overcommit/RuboCop gems in the ambient shell. Git still created a clean
  worktree. This is the already documented behavior in
  `notes/vpsfree-cz-configuration/2026-06-13-overcommit-hooks-need-nix-develop.md`;
  hooks must be installed/run inside `nix develop` before a commit.
- The first final rebase attempt was also rejected by the pre-rebase hook in
  the ambient shell for the same missing bundled gems. Repeating it inside
  `nix develop` passed all hooks and rebased cleanly.
- vpsAdminOS currently emits this post-boot kernel message from
  `boot.postBootCommands`:
  `vpsAdminOS <build-id> with kernel <boot.kernelVersion>`.
- That explicit marker was introduced by vpsAdminOS commit
  `316aa5b9b114aaace48e6ff233c77b6fa6a46d1a` on 2025-06-17.
- The vpsAdminOS rsyslog module has loaded `imklog` since its initial 2018
  implementation. The kernel's standard `Linux version <version> ...` record
  is therefore the historical fallback for boots before the explicit marker.
- A real retained boot on `stg/node2` has records such as:
  - `2026-04-02T15:04:40.876489+02:00 ... kernel Linux version 6.12.79 ...`
  - `2026-04-02T15:04:40.882971+02:00 ... kernel vpsAdminOS 25.11.git.a4bc7a3 with kernel 6.12.79`
- The two marker types arrive milliseconds apart. Exact duplicate standard
  records and repeated same-kernel boots also exist in the sample.
- The `stg/node2` sample shows real transitions from 6.12.79 to 6.12.81 and
  then 6.12.87, as well as repeated boots on 6.12.81.
- `int.log` stores node logs below
  `/var/log/remote/cz.vpsfree/nodes/<location>/<node>/log*` with RFC3339
  timestamps and full cluster hostnames.
- Configuration requests 180 uncompressed daily node rotations. The sampled
  `stg/node2` files currently begin at `log-20260403`, so tools must derive and
  display the actual oldest-evidence date rather than assume 180 days.
- The node log tree has 3,317 files and approximately 217 GiB of allocated
  data. Active configured nodes account for roughly 200 GiB. An on-demand full
  scan is not appropriate for routine advisory queries.
- Current configured non-carried vpsAdminOS nodes number 13. Old log
  directories for retired nodes also remain and should be opt-in query data.
- `/run/booted-system` is set during vpsAdminOS stage 2. Its immutable
  `kernel-modules/lib/modules` directory plus `/proc/stat` `btime` can support a
  current-state check without trusting `uname`, which can be changed by
  livepatch/eBPF code.
- Recommended implementation: a tiny append-only live boot index populated by
  central rsyslog, an idempotent one-time retained-log backfill, a tested query
  helper on `int.log`, and `scripts/kernel_boots.rb` registered as a
  configuration-local `ConfCtl::UserScript`. The `confctl` repository is not
  affected. See `plan.md` for semantics and alternatives.
- Implementation decision: retain original RFC3339 syslog lines in separate
  live and backfill index files. The configuration-local user script performs
  parsing and produces table or JSON output. This avoids maintaining separate
  parsers for raw, backfilled, and live data.
- Implementation decision: retain the compact index indefinitely and include
  the `/run/booted-system` live cross-check by default for threshold queries,
  with an explicit opt-out.
- The first focused spec run failed before examples because Ruby 3.4.9 no
  longer includes `csv` as a default gem while the existing abuse-parser test
  harness requires it. Added the missing test dependency in a separate commit
  and recorded the reusable lesson in
  `notes/vpsfree-cz-configuration/2026-07-10-rspec-ruby34-csv.md`.
- Commit `8ed9798d` (`test: declare csv dependency`) adds the Ruby 3.4 test
  prerequisite only.
- Commit `6bce77bc` (`int.log: index node kernel boots`) adds:
  - a central rsyslog action which copies recognized node boot messages to the
    small, intentionally unrotated live index;
  - the packaged `node-kernel-boots dump|backfill` helper;
  - an atomic, repeatable, merge-preserving backfill running at idle I/O and
    nice level 19;
  - per-node retained boundaries and a persistent live-capture boundary;
  - package/helper specs for matching, deduplication, empty input, repeated
    backfill, live dump ordering, and missing log roots.
- Commit `e7c58a72` (`scripts: query node kernel boot history`) adds:
  - the configuration-local `ConfCtl::UserScript` and CLI registration;
  - parsing of current explicit markers and historical `Linux version` lines;
  - semantic marker-pair and exact-duplicate coalescing;
  - transition-only and all-boots timelines which preserve rollbacks;
  - rollback-aware minimum-version period evaluation plus the actual known
    history boundary;
  - optional/current live checks using `/run/booted-system` and `/proc/stat`
    instead of `uname`;
  - conservative `unknown` output when a requested live check fails;
  - table and JSON output, retired-node querying, parser and command-level
    tests, and detailed README usage/trust documentation.
- The unpublished query commit was amended after user feedback to replace the
  security-specific `fixed-since` interface with generic `version-since`
  terminology. The query now reports `at-or-above`, `below`, `conflict`, or
  `unknown`, with `version_since`, `previous_kernel`, and
  `observed-period-lower-bound` fields/evidence. It still reports the beginning
  of the current uninterrupted period at or above the requested version, so a
  rollback resets the date.
- Quick verification after the committed series:
  - RSpec: 31 examples, 0 failures;
  - RuboCop: 34 files inspected, no offenses;
  - `node-kernel-boots-1` Nix package built successfully;
  - all four `confctl kernel-boots` help surfaces loaded successfully;
  - Overcommit Nixfmt and RuboCop hooks passed on every commit;
  - commit-message hooks passed with warnings above 72 columns, while every
    commit message line remains within the workspace 80-column limit;
  - `git diff origin/master...HEAD --check` passed;
  - configuration worktree is clean and three commits ahead of `origin/master`.
- Mandatory standalone reviewer: `/root/mandatory_change_review`. It reviewed
  base `251ee1ee` through pre-fix head `d2e73aee` without launching subagents or
  running long integration tests. Fixups and the later user-requested removal
  of live-index rotation were tested and autosquashed to final head `780c1d0e`.
- Review findings:
  - Blocking: a failed default live probe still left a definitive central-log
    security status.
  - Important: repeat backfills replaced and could erase expired evidence;
    actual evidence boundaries were not stored; the remotely driven permanent
    live file was unbounded; syslog provenance was unauthenticated; and the
    CLI/controller lacked automated specs.
  - Advisory: operator documentation did not define statuses, JSON fields,
    boundaries, failure behavior, or the provenance limitation.
- Follow-up design decisions:
  - requested live-check failures yield `unknown` and retain the central-only
    assessment only as contextual evidence;
  - repeated backfills merge old and new records and preserve per-node oldest
    retained boundaries;
  - live capture records a persistent start boundary;
  - the reviewer recommended bounding the sender-driven live index; after
    implementation, the user explicitly chose an unrotated file because the
    filtered boot-event volume is expected to remain negligible;
  - central syslog's sender-controlled, unauthenticated provenance is accepted
    as an explicit operational limitation for this first iteration and is
    documented; the default SSH live check corroborates only current state;
  - command-level specs cover registration, helper calls, option conflicts,
    central-only behavior, and failed-live-check status.
- Quick verification after review fixes:
  - RSpec after the final no-rotation decision: 39 examples, 0 failures;
  - RuboCop: 35 files inspected, no offenses;
  - `node-kernel-boots-1` rebuilt successfully;
  - command registration/help and diff checks passed;
  - mandatory Overcommit hooks passed for both fixup commits before
    autosquashing.
- Quick verification after the generic-interface revision:
  - focused kernel-boots specs: 19 examples, 0 failures;
  - full RSpec: 39 examples, 0 failures;
  - RuboCop: 35 files inspected, no offenses;
  - `confctl kernel-boots` and `version-since` help loaded successfully and no
    `fixed-since` command is registered;
  - mandatory Overcommit Nixfmt and RuboCop hooks passed;
  - `git diff --check` passed;
  - the pre-review functional commit was `95f957b7`.
- Fresh mandatory review of base `251ee1ee` through head `95f957b7` found one
  Blocking, one Important, and two Advisory issues:
  - a later contradictory central timestamp could override a successful live
    probe;
  - live rsyslog capture omitted bracketed monotonic Linux boot markers;
  - the packaged helper omitted its `gawk` and `gnused` runtime dependencies;
  - per-node coverage always overrode an earlier global capture boundary.
- All fresh-review findings were fixed and autosquashed into the affected
  commits:
  - a successful live probe now determines the current boot, while later
    contradictory central evidence yields `live-central-order-conflict`;
  - live capture recognizes bracketed Linux markers and has regression
    coverage;
  - the packaged helper includes `gawk` and `gnused` and its wrapper completed
    a backfill under an empty environment;
  - coverage selects the earliest applicable per-node or global boundary.
- Quick verification after the review fixes:
  - focused kernel-boots specs: 27 examples, 0 failures;
  - full RSpec: 42 examples, 0 failures;
  - RuboCop: 35 files inspected, no offenses;
  - mandatory Overcommit Nixfmt and RuboCop hooks passed;
  - the isolated `node-kernel-boots` wrapper backfill passed;
  - pre-rebase commits were `19cfdba1`, `ccdc3341`, and `b1fafed9`.
- The standalone reviewer confirmed that all fresh-review findings were
  resolved at pre-rebase head `b1fafed9`, with no regressions or new
  significant findings.
- Final verification after rebasing onto `435f63d7`:
  - full RSpec: 42 examples, 0 failures;
  - RuboCop: 35 files inspected, no offenses;
  - mandatory Overcommit Nixfmt and RuboCop hooks passed;
  - `confctl kernel-boots` and `version-since` help loaded successfully;
  - `git diff origin/master...HEAD --check` passed;
  - final commits are `8ed9798d`, `6bce77bc`, and `e7c58a72`.
- Long integration verification:
  - `confctl build -y 'cz.vpsfree/containers/prg/int.log'` succeeded;
  - final built generation after removing rotation: `2026-07-10--18-30-32`;
  - the build produced the new package, initializer service, tmpfiles, rsyslog
    configuration, and complete NixOS system without a dedicated live-index
    logrotate rule;
  - generated initializer is ordered before `syslog.service` but is only
    wanted, not required, so a metadata failure cannot block central logging;
  - built rsyslog 8.2512.0 accepted the generated configuration at validation
    level 1 with no errors.
  - the final post-review/rebase `int.log` build also succeeded as generation
    `2026-07-10--19-29-41`;
  - its generated rsyslog 8.2512.0 configuration includes the bracketed Linux
    marker condition and passed validation level 1;
  - the exact helper from the built system completed an isolated backfill with
    an empty environment, and its closure references `gawk` and `gnused`.
- An end-to-end live probe against `stg/node2` could not authenticate from this
  development environment. Direct SSH showed missing host-key trust followed
  by missing key authorization. The command correctly treats such a probe as
  failed/unknown; the hidden `confctl ssh` diagnostic behavior is recorded in
  `notes/confctl/2026-07-10-ssh-merged-stderr-hidden.md`.
- Standalone read-only safety reviewer:
  `/root/node_kernel_boots_readonly_review`. It made no repository or remote
  changes and used temporary local paths for its reproducer.
- Read-only safety review findings:
  - Blocking: unrestricted state-root overrides and followed symlink/hard-link
    entries can redirect helper writes into raw logs. The reviewer reproduced
    `live.log` changing a raw target's mode and `backfill.lock` truncating a raw
    target.
  - Important: `backfill.log` and `coverage.tsv` are published separately, so
    interruption or a concurrent query can observe inconsistent generations.
  - Important: live rsyslog matching accepts any `vpsAdminOS ` kernel message,
    while the parser/backfill require the full boot-marker grammar; irrelevant
    sender-controlled messages can therefore grow the unrotated index.
  - Advisory: coverage extraction assumes conventional filenames and a valid,
    ordered first log line.
  - Confirmed: with default trusted paths, raw `log*` files are passed only to
    read/stat operations; `list` and `version-since` execute only `dump`,
    `coverage`, and the read-only live probe; the rsyslog index action is
    additive and does not divert ordinary per-node logging.
- Read-only safety remediation committed and autosquashed:
  - canonical raw/state roots must be disjoint; the state directory must be
    owned by the effective user and not writable by group/others;
  - writable state entries reject symlink and hard-link aliases before any
    chmod/open, the lock is opened without truncation, and replacements use
    `mv -T`;
  - records and retained coverage are published together in one atomic
    `backfill.snapshot`, and queries retrieve it through one read-only helper
    invocation;
  - malformed coverage timestamps and unexpected node-directory names fail
    conservatively;
  - live rsyslog capture uses the full explicit-marker grammar and is gated by
    a boot-local readiness environment file written only after safe state
    initialization; ordinary logging remains active if initialization fails;
  - regression tests reproduce state-root overlap, filesystem-root, symlink,
    hard-link, lock, snapshot, and malformed-boundary cases using temporary
    directories and verify raw log contents/modes remain unchanged.
- Quick verification of the committed remediation before mandatory review:
  - full RSpec: 48 examples, 0 failures;
  - RuboCop: 35 files inspected, no offenses;
  - ShellCheck 0.11.0 passed;
  - mandatory Overcommit Nixfmt and RuboCop hooks passed;
  - Nix parsing and both kernel-boots help surfaces passed;
  - the installed helper completed isolated `backfill` and `snapshot` commands
    under `env -i`;
  - pre-review commits were `8ed9798d`, `bf8e62f5`, and `26e92857`.
- Mandatory standalone review of pre-fix head `26e92857` found one Blocking,
  one Important, and two Advisory issues:
  - bind-mount aliases could bypass canonical path/link-count checks and expose
    an existing raw log to `chmod`; the reviewer reproduced this in a temporary
    unprivileged user/mount namespace;
  - live Linux-message filtering still accepted nonnumeric messages outside
    the parser/backfill grammar;
  - coverage still depended on file mtime/first-file selection and lexical
    RFC3339 ordering;
  - the temporary cleanup trap was installed after the first `mktemp`.
- All mandatory-review findings were fixed and autosquashed:
  - state/log roots must share the same non-aliased mount context, individual
    state entries must not be mountpoints, and helper operations use an open
    state-directory file descriptor;
  - existing files are mode-checked without mutation, new files are created
    off-path and atomically renamed, and the backfill lock uses the directory
    inode rather than a writable lock file;
  - temporary cleanup is active before the first allocation;
  - both Linux and explicit vpsAdminOS rsyslog branches require numeric marker
    grammar;
  - coverage examines every retained file's first record, compares timestamps
    by epoch, and normalizes previous/new coverage before selecting the oldest
    instant;
  - user/mount-namespace specs reproduce both file and directory bind aliases
    and verify the raw targets remain unchanged.
- Mandatory-review follow-up confirmed the bind-mount, descriptor/lock,
  rsyslog grammar, coverage ordering, and cleanup fixes. It found one remaining
  Important gap: existing capture/snapshot files did not yet require exact
  non-writable modes.
- Exact `0640` mode validation now applies uniformly to `live.log`,
  `capture-started-at`, and `backfill.snapshot`; a regression verifies that
  group-writable `0666` state is rejected rather than consumed.
- Mandatory-review final verification gave a clear pass at pre-cosmetic head
  `1aa6e702`: both `0666` reproducers failed safely, all validator call sites
  were covered, and there were no regressions or new significant findings.
- Post-review full verification passed with 52 RSpec examples, RuboCop,
  ShellCheck, Overcommit hooks, CLI help, diff checks, and the installed helper
  under `env -i`.
- The first final `int.log` system build succeeded as generation
  `2026-07-10--22-57-13`, but generated rsyslog validation correctly failed:
  RainerScript requires regex `$` anchors to be escaped inside double-quoted
  strings. Both anchors were fixed and the reusable lesson was recorded in
  `notes/vpsfree-cz-configuration/2026-07-10-rsyslog-regex-dollar-escape.md`.
- The corrected generation `2026-07-10--23-00-43` passed rsyslog validation
  and a local semantic test accepted three valid marker forms while rejecting
  four malformed forms. Generated-script inspection then found that
  `writeShellScript` does not imply fail-fast behavior; explicit `set -eu` was
  added so a failed helper cannot create the rsyslog readiness marker.
- Final integration generation `2026-07-10--23-04-24` succeeded. Its generated
  rsyslog 8.2512.0 configuration passed validation level 1, and the generated
  systemd units contain the expected ordering, runtime directory, optional
  environment file, and fail-fast initializer.
- A local rsyslog semantic test accepted standard Linux, bracketed Linux, and
  explicit vpsAdminOS markers while rejecting four malformed variants.
- Generated initializer tests in temporary unprivileged user/mount namespaces
  confirmed both paths:
  - valid state creates `NODE_KERNEL_BOOTS_READY=1` with mode `0640`;
  - an unsafe symlinked state path exits nonzero, removes a stale readiness
    marker, and does not recreate it.
- A final output-only cleanup makes the backfill message print the stable state
  path instead of `/proc/self/fd/8`; it was autosquashed without behavioral
  changes.
- The trusted-root simplification reduced `node-kernel-boots.sh` from 332 to
  104 lines. Backfill is now recursive `grep`, merge, exact deduplication, and
  atomic rename into a plain `backfill.log`. It retains a small initializer and
  read-only snapshot command, but removes path canonicalization, mount/link
  defenses, locking, per-file retained coverage, and the combined snapshot
  format.
- `history_since` now selects the earliest observed boot or live-capture
  boundary. This preserves explicit lower-bound semantics without a second scan
  of every retained file for coverage metadata.
- At the user's request, the backfill matcher uses a GNU grep PCRE pattern. A
  shared kernel-version fragment and non-capturing groups make the accepted
  Linux/vpsAdminOS forms easier to read; fixture coverage includes malformed
  lookalikes which must be rejected.
- Quick verification of the committed simplified tree passed:
  - full RSpec: 43 examples, 0 failures;
  - RuboCop: 35 files, no offenses;
  - ShellCheck 0.11.0;
  - mandatory Overcommit Nixfmt and RuboCop hooks;
  - `git diff --check`.
- Mandatory standalone reviewer
  `/root/mandatory_review_simplified_kernel_boots_final` reviewed committed
  head `662efb9a` without touching the worktrees. It found no Blocking or
  Important issues and one Advisory: the backfill PCRE accepted arbitrary
  bracket contents while live rsyslog and Ruby accept only a numeric monotonic
  timestamp.
- The Advisory is fixed and autosquashed: the PCRE now requires the same
  numeric bracket form and the helper spec rejects `[not-a-clock]`. Focused
  RSpec, RuboCop, ShellCheck, hooks, and diff checks passed.
- Current commits after the 2026-07-13 rebase and autosquash are `022ca857`,
  `20cb53ba`, and `02451428` on base `e1cc165c`.
- The same reviewer confirmed at `20cb53ba` that `[not-a-clock]` is rejected,
  numeric bracketed markers remain accepted, and the Advisory is resolved
  without regression. The mandatory review is complete with no remaining
  findings.
- Final integration verification passed:
  - `confctl build -y cz.vpsfree/containers/prg/int.log` produced generation
    `2026-07-13--10-22-02`;
  - generated rsyslog 8.2512.0 passed `-N1` validation, retains ordinary remote
    logging before the optional boot-index action, and includes the expected
    readiness gate;
  - the exact packaged helper ran `backfill` and `snapshot` under `env -i`,
    confirming GNU grep PCRE support and accepting the standard, numeric
    bracketed, and explicit markers while rejecting malformed versions and
    `[not-a-clock]`;
  - the generated initializer unit has the expected ordering, runtime
    directory, and optional syslog environment file;
  - final full RSpec passed with 43 examples, RuboCop passed with 35 files, and
    all three `confctl kernel-boots` help surfaces loaded successfully.
- The implementation is complete and remains unpushed, unmerged, and
  undeployed.

## Open questions

- A later initiative should define how livepatch and eBPF remediation evidence
  composes with booted-kernel evidence; it is intentionally out of scope here.

## Cleanup

- Worktrees remain active for inspection; nothing has been pushed, merged, or
  deployed.
- Development-shell `.bin`, `.bundle`, and `.rubocop_cache` artifacts created
  during verification were removed. No result symlink is present.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
