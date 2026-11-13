# Scheduled workflow repairs: design and verification brief

Architect: architect0. Lead owns package allocation, acceptance and final state.
The final named-configuration architecture is C4: normal flake.nix declarations,
flake.lock as the only confctl revision authority, and the declared tools-shell
executable for updates and final guard. Both C4 repair heads are integrated after
final review and focused acceptance. Org's fresh hosted run passed; vpsFree's
fresh run remains with the lead's sole monitor. C3's selected-only commit-message
contract and full dependency guard remain active.

Earlier package briefs and workflow-pin receipts below are retained design
history where superseded by C4. User approvals, integrated ancestry and current
execution state are recorded in state.md and owner evidence. No production
deployment, PR or session lifecycle action was performed by this design package.

## Scope and invariants

Repair demonstrated scheduled-workflow failures, starting with the two named
configuration repositories. Preserve cron times, updater targets, permissions,
token handling, normal Git hooks, forward-only input selection and the final
old/new lock check before push. Do not disable checks or sign hooks globally.
No production channel or machine build is needed for these repairs. C4 adopts
the normal confctl tool input and its owned dependencies in flake.lock; ordinary
authorized workflow executions may publish their generated updates. No schema, API, protocol, on-disk or
deployed system-format changes are intended. Each repository is independent;
application edits belong to its assigned implementer in this session's worktree.

## C1: sign the vpsadminos.org pre-commit plugin (sufficient)

- Proposed owner: implementer1, following lead allocation. Exclusive source:
  `vpsadminos-org-configuration/.github/workflows/daily-update.yml`.
- Dependency: accepted C0 evidence; no dependency on B or the remaining inventory.
- Cause: `overcommit --sign` signs configuration, not plugin code. The workflow
  installs the custom Nixfmt pre-commit plugin but never signs it. This is
  established by the first failure and latest three attempt-1 logs and the locked
  Overcommit 0.68.0 CLI's separate configuration/plugin signing branches.
- Change: retain the configuration signing command and add
  `nix develop -c bundle exec overcommit --sign pre-commit` in the same install
  hooks step before any updater can commit. Keep latest-compatible existing
  action majors; all three were checked against official upstream releases.
- Acceptance: a fresh disposable Git repository containing this repository's
  actual hook/config and locked bundle can install and sign both configuration
  and Nixfmt, then make a real commit of a formatted Nix fixture with hooks
  enabled. A deliberately unformatted fixture must be rejected, demonstrating
  the fix signs the plugin without bypassing it. Do not update or push real
  configuration inputs merely to exercise the hook.
- Quick checks: workflow YAML/actionlint or equivalent repository-appropriate
  lint; shell syntax of edited run block; active repository hooks on the final
  commit. Run the real hook fixture in the repository Nix environment. If
  bootstrapping its environment is long/uncertain, route it through the monitor
  skill rather than repeatedly trying it inline.
- Evidence: base/head, changed file, exact commands/results and fixture outcome;
  no migrations. Then final independent review before any long checks.
- Compatibility/recovery: existing schedule and update semantics unchanged;
  signing is local to the disposable Actions checkout. Revert workflow commit to
  recover source behavior. No machine deployment or coordinated update needed.
- Validation limit: local fixture does not establish current remote inputs can
  complete all updater stages. Actual scheduled execution needs the fix on the
  default branch after separate explicit integration approval. Do not dispatch
  the existing workflow as a feature test: it checks out and pushes master.

## B1: keep the vpsFree updater Ruby environment stable (sufficient)

- Proposed owner: implementer0. Source boundary: daily-update workflow only,
  unless a faithful reproduction identifies a separate required source repair.
- Evidence: initial steps use Ruby 3.4.9. Updating stable nixpkgs changes the next
  `nix develop` to Ruby 3.4.11 while both use `.gems/ruby/3.4.0`. Oct29 failure
  explicitly reports a native date extension linked to incompatible libruby
  3.4.9. Current runs fail while loading Overcommit after the same shell
  transition; its missing-gem message masks LoadError. Last success lacked the
  stable input transition.
- Change: record the original development shell in a runner-temporary Nix
  profile during initial hook installation, with
  `nix develop --profile "$RUNNER_TEMP/daily-update-dev-shell" -c ...`.
  Use `nix develop "$RUNNER_TEMP/daily-update-dev-shell" -c ...` for the rest
  of initial hook setup and **all** later development-shell entries, including
  input updates, conditional llm-agents update, dependency refresh and final
  guard/push. The first profile-producing command precedes every input update;
  subsequent entries must never recreate/overwrite the profile. A dedicated
  preparation step with `-c true` is also acceptable if it makes that ordering
  clearer. `CONFCTL_FLAKE` remains the separate pinned guard-aware executable.
- Interface verified against official Nix 2.35.6
  [nix develop manual source](https://github.com/NixOS/nix/blob/2.35.6/src/nix/develop.md):
  `--profile /tmp/my-build-env` records a build environment and
  `nix develop /tmp/my-build-env` reuses it. The existing installer currently
  supplies Nix 2.35.6. This avoids designing a new environment cache protocol.
- Realize one development-shell environment before input updates and reuse that
  exact environment for every later workflow step.
  Preserve current inputs being updated, the pinned confctl command, hook
  execution and all dependency/security checks. Avoid deleting shared caches,
  relaxing hook checks or continually re-signing to mask environment drift.
- Acceptance: workflow structurally has one profile creation before input
  mutation and every later shell consumes that profile. A disposable checkout
  using the repository's actual initial shell records exact Ruby executable,
  GEM_HOME and successful `require 'date'`/Overcommit loading; after changing its
  flake definition to a deliberately failing evaluation, entering the saved
  profile must still use the same Ruby and load those gems. A real local commit
  through the configured hook must succeed. This tests reuse without fetching
  arbitrary moving inputs, pushing commits or building production machines.
  Keep fixture changes outside the feature source and never disable hooks.
- Quick checks: workflow lint, extracted shell syntax, profile ordering/coverage
  inspection and ordinary commit hooks. Use the existing monitor workflow for
  uncertain shell bootstrap/fixture execution. No application test subsystem
  or production system build is necessary for this workflow repair.
- Evidence: exact initial/reused environment paths, command/results, base/head,
  full final diff/history and no-migration conclusion. If native loading still
  fails with a stable environment, stop and report its exact exception before
  expanding scope; the latest Overcommit message's precise masked LoadError
  remains an inference from the established environment transition.
- Compatibility/recovery: input selection/output, token permissions, hooks and
  security checks remain unchanged. Dependency resolution consistently uses the
  initial supported Ruby for one run; the next scheduled run starts with its
  newly selected shell. Runner-temporary profile disappears with the runner.
  Revert workflow commit for recovery; there is no state migration or machine
  rollout. C1 and B1 can proceed independently.

## G1: synchronize Ruff when the HaveAPI updater advances Nixpkgs (sufficient)

- Owner: next available implementer selected by lead. Source boundary:
  `haveapi/utils/update-nixpkgs.sh`, a small adjacent helper/test only if useful,
  and `clients/python/CONTRIBUTING.md` plus the existing updater paragraph in
  `doc/agent-instructions/development.md` where needed to explain the coupled
  update. The implementation does not need to advance today's tracked
  `flake.lock` or Ruff pin; the repaired updater must produce their next pair.
- Cause: the updater changes only `flake.lock` then runs `nix flake check`.
  The required Python/Nix Ruff parity check correctly rejects the new Nix Ruff
  version against the unchanged exact Python dev pin. Both newest schedules
  failed; latest reports 0.17.2 versus 0.17.4.
- Change: after the guarded Nixpkgs advance and before checks, determine Ruff's
  version from the newly locked Nixpkgs for the host system. Validate exactly
  one existing exact Ruff dev requirement and replace only that requirement's
  version in `clients/python/pyproject.toml`. Preserve unrelated TOML bytes,
  Python runtime constraints and every other dependency. Do not hardcode today's
  0.17.4, relax/remove parity, use an unpinned channel, or track `uv.lock` (library
  locks are deliberately ignored). Avoid a general dependency synchronization
  framework. Fail closed on absent/duplicate/malformed pins or invalid version.
- Preserve the no-update path, forward-only confctl selection, final guard,
  non-force push and generated commit-subject convention. Guard both owned input
  files against pre-existing modifications before editing; do not commit
  unrelated staged content. Stage the lock and synchronized declaration together
  only after checks pass. No-change versions leave pyproject byte-identical.
- Checks: focused helper/script cases cover changed/same Ruff, malformed/multiple
  pin rejection, pre-existing dirty input and failed-check/no-commit behavior.
  Keep existing `nix flake check` gating, including Prettier parity; unrelated
  formatter drift fails rather than silently broadening automatic edits.
- Runtime gate clarified and accepted by lead: every actual Nixpkgs update runs
  the following block from the repository root, after pin synchronization and
  the existing `nix flake check`, but before staging or generated commit:

  ```sh
  nix develop .#client-python -c bash <<'EOF'
  set -euo pipefail
  cd clients/python
  uv sync
  uv run --locked python utils/run_ruff.py format --check .
  uv run --locked python utils/run_ruff.py check .
  EOF
  ```

  The newly locked input supplies the client-python shell, Python, uv and
  `HAVEAPI_RUFF`; `uv sync` prepares the local ignored environment/lock from the
  synchronized declaration. The shared entrypoint verifies exact executable
  parity before formatting/linting. Any shell, sync, format or lint failure must
  stop before staging/commit. The existing no-input-update fast path remains.
  No automatic source reformat, wider client suite, fallback or retry mechanism
  is added. This gate is part of each scheduled update, not only acceptance of
  the repair branch; one-time acceptance cannot protect future formatter pins.
- Extend focused control-flow coverage to prove sync/format/lint failures cannot
  stage or commit. Preserve unchanged passing quick evidence. After final review,
  the real disposable coherent-update acceptance exercises both parity and the
  exact runtime gate above under a fresh utility watcher.
- Quick script syntax, focused tests and hooks precede commit/review; longer
  real Nix checks use the monitor skill after final review. No broad API runtime
  integration is needed for an updater-only patch. A deliberately isolated
  test repository must receive any generated commit; no default branch writes.
- Evidence: old/new Nixpkgs and Ruff values, exact selected package path/version,
  final generated-file boundary, tests and failed-check exit/commit behavior,
  base/head and no migrations. No imported action changes are needed for a
  script-only repair; if workflow edits become necessary, validate each imported
  action from official upstream before selecting refs.
- Compatibility/recovery: developer-only formatter pin changes alongside its
  Nix toolchain; published runtime/library requirements and schema stay intact.
  Future updater commits remain ordinary guarded commits. Revert the paired
  pin/lock update together if recovery is required; no deployment is involved.

## F1: correct raw migration-default assertions (sufficient)

- Proposed owner: implementer3; lead allocates. Exclusive source: the nine
  `api/spec/migrations/*_spec.rb` files listed in the complete expectation table
  in [F0 evidence](evidence-vpsadmin-migrations.md). Eleven assertion values
  change: false/zero to the raw string `'0'`, true to `'1'`. A short comment
  explaining raw adapter defaults at the existing helper is optional, but the
  helper's return/behavior must not change.
- Cause: `column()` returns the actual MySQL adapter Column. ActiveRecord
  8.1.4.1 passes the database field default through unchanged; typed model
  deserialization occurs elsewhere. The existing specs conflate raw metadata
  with typed model attributes. All nine latest failures share this mismatch;
  capacity's later memory/swap assertions expose two more identical mistakes.
- Preserve every migration byte, nil default, column type, nullability,
  unsignedness, existing data and rollback assertion. No broad `.to_i` or boolean
  coercion and no migration guards. No source schema, model/API behavior or
  generated client change is needed. Existing raw nil-default checks remain.
- Acceptance: all eleven raw defaults match supported MariaDB/ActiveRecord
  metadata and all existing migration examples remain effective. Run the exact
  nine-file batch from F0 in `VPSADMIN_PLUGINS=none nix develop .#api`, with
  `bundle exec rspec --options /dev/null --format documentation ...`; use the
  repository's automatically isolated MariaDB, never a real database. This is a
  focused check once dependencies are prepared (failed run's 84 examples took 5 seconds).
  Ruby syntax/RuboCop and normal hooks are quick checks before final commit.
- After independent review, one full migration batch with the same options and
  `spec/migrations/*_spec.rb` verifies no additional raw-default mismatch remains.
  Uncertain Nix/bootstrap/check duration uses the monitor skill. No VM integration,
  schema regeneration or generated-client synchronization is needed for this
  expectation-only change; record the no-API-contract-impact assessment.
- Evidence: exact nine paths/eleven changes, core-mode environment/database and
  ActiveRecord versions, narrow/full commands/results, base/head, full history
  and an explicit conclusion that no migrations were created or rewritten.
- Compatibility/recovery: test metadata expectations only, no persisted state
  or deployed behavior changes. Existing migration lineage is preserved. Revert
  the test commit to recover source; no machine deployment or ordering needed.

## E1: isolate IRC dependency generation from Bundler preloads (sufficient)

- Proposed owner: implementer2, following lead allocation. Source:
  `vpsfree-irc-bot/.github/workflows/daily-update.yml`; a short workflow comment
  should preserve why Bundler preloads are removed. No bot behavior or package
  source changes, and no one-off generated dependency refresh is required for
  the repair branch.
- Documentation addition proposed to lead: `README.md`'s existing Bundix recipe
  repeats the exact failing login-shell/preload sequence. Update only that
  recipe and its short explanation to the same non-login, fail-fast,
  preload-free generation and bundle-install ordering. No automatic commit/push
  belongs in the contributor snippet. Lead accepts this adjacent file boundary
  and applies the required user-facing writing pass before commit.
- Cause: the shell installs a platform-native Ruby 3.3 bundle and exports
  `RUBYOPT=-rbundler/setup`. The inner shell then forces Ruby-platform resolution
  and removes the lock while that preload is still active; `bundle lock` tries
  to activate a not-yet-installed source-platform Nokogiri. Without fail-fast,
  execution continues to Bundix's own Ruby/bundle, where the same project
  preload cannot find Overcommit. Both errors occur before Git commit. Correct
  the inventory's initial suggestion that the second error was a commit hook.
- Change: use a non-login, fail-fast Bash body within one `nix develop`, unset
  `RUBYOPT` before lock/gemset mutation and Bundix invocation, and retain forced
  Ruby-platform generation. Install the refreshed bundle under this shell's
  actual Ruby before hook setup and commit. Preserve the existing
  `NIX_ENFORCE_PURITY=0` contract for native prism installation. Keep staging,
  change detection, mandatory Overcommit install/signing and commit inside the
  same Ruby environment. No generated commit on generation/install/check error;
  no-change exits successfully. The later push remains conditional on the
  successful updater and uses ordinary non-force semantics.
- Do not disable Bundler globally, change bot Ruby, omit native source-platform
  requirements, skip hooks, or run package generation outside the declared Nix
  environment. A scoped unset for this updater is sufficient; flake shell
  behavior for ordinary contributors remains intact.
- Imported actions: checkout's current compatible release is v7.0.1 and major
  `v7` points there; replace the old v6 reference when editing this workflow.
  Existing install-nix-action v31 already points to v31.11.5. Official ref/action
  source verification is recorded in audit.md.
- Quick checks: YAML/action lint, extracted Bash syntax and a focused control-flow
  check proving a failed lock or Bundix step cannot reach Git staging/commit.
  Install/verify repository hooks and pass them for the workflow commit before
  independent final review. Do not needlessly create a general CI test harness.
- Longer acceptance after review: clean disposable checkout runs the exact
  generation/install/hook-commit block, with no push. Verify `RUBYOPT` is absent
  for lock/Bundix, refreshed source-platform Nokogiri is installed under the bot
  Ruby, gemset/lock agree, and the real commit runs enabled hooks. Repeat once
  immediately to check no-change behavior; any changed upstream resolution must
  be explained rather than treated as idempotence failure. Use a fresh utility
  watcher for native dependency installation. Network/native build failures
  remain explicit and stop the batch; do not rerun to chase green.
- Evidence: first failing layer, Ruby/Bundler/Bundix identities and input pin,
  exact commands/results, generated-file inventory in disposable repository,
  hook execution and no-change result, base/head and no migrations. No live IRC
  credentials, deployed service restart or message to a real channel is needed.
- Compatibility/recovery: dependency update intent and generated package formats
  remain unchanged; Ruby and hook environments become consistent. No deployed
  state/API migration. Revert workflow commit for source recovery; newly generated
  dependency updates can be reverted as their own ordinary commits if needed.

## H1: require the complete KB firewall listener fixture (sufficient)

- Proposed owner: implementer0 after B1 acceptance and capacity confirmation;
  lead allocates. Exclusive source:
  `vpsfree-kb-contracts/tests/suite/kb/firewall.nix`. No KB page/example edits,
  pin changes, capture/publication operations or generic runner changes.
- Demonstrated fixture defect: initial listener setup and restart readiness
  succeed when **any** listed port exists. The initial retained output contains
  only 22/443 despite requiring 22/80/81/443. After restart the helper again accepts
  any 22/80/443; the subsequent port 22 connectivity assertion fails immediately.
  This proves incomplete readiness; the exact underlying post-restart SSH state
  was not retained and remains unknown until the focused runtime check.
- Change: introduce/reuse a bounded helper requiring local listening sockets
  for **each** of 22, 80, 81 and 443 before firewall assertions. Use it after initial
  listener setup and after restart for all scripts sharing those helpers.
  Port 81 must be listening too: later denial assertions must test firewall
  policy against a live service. Use the existing test-runner readiness wait
  primitive and a single bounded deadline (the existing 120 seconds is sufficient as
  the initial contract). Do not retry the firewall policy assertions or silently
  start services during verification to conceal broken persistence.
- Preserve existing dual-stack external allow/deny, ICMP, established-connection,
  public-zone and restart persistence checks verbatim. On readiness failure,
  retain bounded local socket/service-state diagnostics from the disposable
  container, then fail; do not swallow the failure. Service command failure in
  initial setup must also fail promptly rather than being masked by a final
  successful grep. Keep all fixture command/units and source-page hashes intact.
- Quick checks: Nix parse/format, generated Ruby syntax where available, and a
  compact helper exercise demonstrating a partial socket listing cannot satisfy
  readiness, a complete listing can, and a persistently missing listener fails.
  Prefer a disposable check over adding a general test framework. Normal hooks
  and the repository's relevant static contract validation must pass before
  final commit/review. No authored/member prose changes means no publication.
- Longer acceptance after independent review: one focused actual
  `./test-runner.sh test --fresh 'kb/firewall#firewalld'` using the repository's
  pinned environment and fresh utility watcher. Keep exact source/input identity,
  resolved Fedora image, before/after restart listener evidence and full native
  test result. Stop and investigate unexpected local kernel builds under the
  workspace verification procedure. Do not launch the whole KB suite to check
  this repair. If SSH remains unavailable, report the retained service/socket
  evidence and resolve the demonstrated cause before claiming H1 complete;
  do not increase timeouts or repeat unmodified runs to chase green.
- Compatibility/recovery: test readiness only, no production API/state/schema
  or deployed firewall behavior. The shared helper already assumes these ports
  for all firewall variants; requiring all strengthens its existing contract.
  Revert fixture commit to recover source behavior. No physical machine deploy
  or KB write is needed; test-owned guests use the runner's normal ownership.
- Evidence: exact base/head/diff, helper checks, static validation, one focused
  runtime receipt and no migrations. Runtime failure may reveal a separate
  service/persistence defect; route a material scope change through lead.

## C2: preserve large generated commit messages (sufficient; lead scope accepted)

- Historical policy note: C3 below supersedes the assumption that every changed
  descendant should supply a Git changelog. The tempfile transport repair remains
  valid independently and was integrated at `4c636b40` with explicit user approval.
  Do not rewrite that merged history or truncate selected component messages.
- Lead accepted the causal addition of confctl as a seventh repository. Its
  initial separate confctl/master integration approval requirement was later
  satisfied by the user's explicit direction recorded in state.md; C2 is merged.
  Feature implementation, publication and review were authorized. Lead
  owns release after implementer1 finishes C2 evidence and G1 target preparation;
  this brief does not assign concurrent work to that owner.
- Evidence: C1's hook repair passed in integrated run 43448052982 attempt 1 and
  its first generated commit succeeded. The later os-staging update collects
  descendant changes through `FlakeLockDiff.from_guard` and `CommitMessage`.
  Nixpkgs range `02c087f3fe673c9e317f206a627cb6b910336dbe` to
  `d4f25a3e562008648d45bcf2d70bcc7422cad84e` alone generates 1,200,140 bytes with
  the pinned mirror's Git-log flags. Exact pinned `GitCommit` passes the complete
  message as one `-m` argument. Its local reproduction fails before Git/hooks;
  direct spawn exposes `Errno::E2BIG`. The hosted candidate was not exported,
  so its identity remains inferred from the staging revision/time. The old May
  pin is confctl's transitive OS input, not the root staging input; it is not the
  cause argument. No further cache/history download is required for this repair.
- Package C2a, proposed owner implementer1 after lead release: confctl
  `lib/confctl/inputs/git_commit.rb` and one focused
  `spec/inputs/git_commit_spec.rb`. Base is current remote master
  `822c0e35dbe2549111912f539116b4225dfd3035`; bare HEAD is stale and must not be
  used. No library-wide helper, new CLI option, package release or consumer sweep.
- Require Ruby's standard `tempfile` explicitly in the owning source file.
  Create one private temporary file with block-scoped cleanup, write the complete
  supplied message and flush it before invoking Git. Supply its absolute path
  through `-F` instead of putting message bytes in argv. Preserve the current
  `git commit` argument order, conditional `-e` only when requested and stdout is
  a TTY, exact `files` arguments, configuration-directory working directory,
  caller environment and inherited standard streams. Keep the file alive until
  the synchronous Git/editor/hooks finish; ensure removal on success, false/nil
  process result and exceptions. Preserve existing failure propagation. Do not
  truncate changelogs, suppress hooks, route through a shell or change staging.
- Quick acceptance uses a disposable real Git repository and a message larger
  than the Linux single-argument limit (at least 200,000 bytes; roughly 1.2 MB
  matches observed scope). A real commit must retain the complete expected
  message under Git's existing cleanup behavior and commit only the supplied
  paths. A real hook must execute; a rejecting hook must leave HEAD unchanged and
  propagate failure. Cover conditional editor arguments without opening an
  interactive editor, and temporary-file lifetime/removal on success/failure.
  Reuse normal spec helpers where practical. Run the focused spec, existing
  message and guarded-update specs as appropriate, syntax and targeted RuboCop
  inside confctl's Nix shell; ordinary repository commit hooks remain required.
- Final committed C2a needs whole-branch independent review. After review, run
  the repository-required suite/checks with a fresh verification utility where
  duration is uncertain. The packaged CLI acceptance should exercise the same
  oversized real-commit boundary and caller hook environment, retaining package
  store path/input identities; reuse existing package-environment scaffolding
  instead of a new framework. No production configuration build or update is
  needed for source acceptance. Record exact revision, source diff and focused
  real-Git proof before requesting confctl/master integration approval.
- Package C2b, same owner after C2a's immutable final revision is available:
  change only `CONFCTL_FLAKE` in
  `vpsadminos-org-configuration/.github/workflows/daily-update.yml` to that exact
  reviewed confctl revision. Keep its `#confctl` output, all channel/update/check
  commands, hooks, cron/manual trigger, authentication and push semantics.
  Do not update the configuration flake lock or other consumers. C1 is already
  merged; this must be an additive new commit, never history consolidation across
  merged C1. Validate YAML, all shell blocks and exact one-pin source delta;
  inspect normal hooks and independently review the affected workflow lane.
- Integration order: lead obtained the separate confctl/master approval and
  integrated its verified exact head; then integrates the reviewed org pin under
  its existing target approval. An immutable published feature revision can be
  used to prepare C2b earlier, but do not dispatch the org updater before the
  dependency's accepted integration and both final reviews/checks. One fresh
  integrated-master dispatch must prove os-staging's full-message commit and
  unchanged final forward-only check/push. Do not rerun the unfixed old SHA.
- Compatibility/recovery: internal message transport changes only. The Ruby API,
  CLI, generated message contents, path selection and normal hooks retain their
  contracts; no schema, state format, configuration output or deployed component
  change. File transport also retains interactive editor/stdin behavior. No
  coordinated production rollout is required. Recovery is an additive source
  revert and workflow-pin revert; old code can read every generated commit but
  still has the large-message limit. Preserve merged history and existing
  successful C1 evidence.

## C3: keep guarded commit messages scoped to selected inputs (sufficient provider brief)

- User correction, recorded verbatim in state.md: "well that's cool, but we're
  not supposed to include nixpkgs changelog in channel update commit messages,
  precisely because it's large and useless"; then "so yeah the confctl change
  can be merged, but nixpkgs updates are supposed tobe done with --no-changelog".
  The user then clarified: "yeah, I actually don't like those transitive inputs
  to be visible in the commit messages. since when are they being added? it's
  not something I asked for afaik". Current sufficient contract: the entire
  commit message describes only explicitly selected inputs. Full graph guard,
  callback and result remain unchanged. Both C2's all-descendant-log assumption
  and the first C3 proposal retaining descendant revision summaries are
  superseded. That proposal retained summaries to cover descendant-only updates;
  the title-only fallback below now handles that case without disclosing them.
- C3a owner: implementer1 after lead release, additive above now-merged confctl
  `4c636b40b53b143fda6d9cad9332ce8b7b86bdb8`. Source boundary:
  `lib/confctl/inputs/updater.rb`, `lib/confctl/inputs/commit_message.rb`, focused
  additions to `spec/inputs/commit_message_spec.rb` and
  `spec/inputs/guarded_update_spec.rb`, and a short clarification in
  `docs/flake-inputs.md`. No CLI, guard, lock-graph, setter, transport or framework
  changes. No new option, repository-name heuristic or global default filter.
- Contract evidence: introduction `550717765d58e9f28d960ea5bca3459ace86eb9e`
  ("Guard automated input updates with cached Git ancestry", committed October
  24, 2026 at 19:24:07 +0200; Git author/committer metadata Jakub Skokan) feeds
  `FlakeLockDiff.from_guard`'s complete changed-path list into the guarded commit
  callback. Its immediate parent `cc40679d267165aecfa569128438bb55fe910268` and
  the current manual updater both use
  `FlakeLockDiff.diff(..., inputs: inputs)` for messages. Current Setter has no
  guarded branch/callback and already uses that selected-input diff; leave it
  unchanged. History inspection stops at this introduction and its parent.
- Preserve the complete changed-path callback and result. The guarded updater
  passes its nonempty requested logical input paths to CommitMessage through a
  minimal internal optional selection, named for message selection rather than
  only changelogs (for example `selected_inputs:`). With explicit selection,
  filter message changes by exact logical path before existing title, body and
  group construction. Do not mutate the original full changes array. No excluded
  descendant names, revision summaries, hashes or log blocks enter the message.
- Missing/nil selection retains existing CommitMessage/manual/Setter behavior.
  True nil/empty original changes still raise the existing no-changes error;
  no empty-selection mode is needed because Updater already rejects empty inputs.
  `changelog: false` suppresses all log queries exactly as before while retaining
  only selected revision summaries. Changelog-enabled messages retain existing
  selected-source grouping/deduplication and downgrade direction. A selected
  alias appears by its requested logical name; unselected terminal/other aliases
  do not leak through grouped summaries.
- A valid full-graph update can have no changed selected revision. Only in this
  explicit guarded-selection case, emit the conventional title
  `inputs: update <sorted requested input names>` with no body. For example,
  selecting `vpsadminos` yields exactly `inputs: update vpsadminos`. Include no
  `to <rev>`, revision arrow, fabricated root change, descendant detail or Git-log
  query. This fallback describes the requested input update without claiming its
  root revision moved. Preserve the full validated lock installation and commit;
  do not turn this into a no-op or leave an accepted change uncommitted.
- Full graph ancestry, snapshot/race checks, callback timing, installation,
  result statuses, changed-path coverage and final check-update remain untouched.
  Excluding a dependency from the message does not exclude its ancestry
  comparison, reject condition or returned change record. Preserve C2's tempfile message transport and
  normal commit hooks.
- Quick tests: mixed selected OS plus transitive Nixpkgs emits only OS title,
  revision summary and log while returning both change records; selected Nixpkgs
  with `--no-changelog` emits only its selected summary and no log query;
  descendant-only success emits exactly the requested-input title with no body;
  nested/follows selection and duplicate selected groups query only selected
  groups once and expose no unselected alias/descendant names. An excluded
  descendant rewind still rejects the complete candidate without changing
  lock/index/HEAD. Preserve nil/default/manual/Setter behavior, true original
  no-changes errors and all-logs-off coverage. Update superseded quick tests
  rather than retaining contradictory full-summary assertions. Use distinct
  small log markers, not another megabyte history download. Run affected specs,
  existing guard/lock-graph specs, syntax, targeted RuboCop and ordinary hooks in
  the repository Nix shell. Lead applies the writing pass to the short technical
  doc clarification before commit; no separate documentation subsystem.
- After final committed review, use the existing packaged CLI fixture for one
  mixed-input selection proof with complete guard/rejection evidence; reuse
  unchanged C2 transport/package evidence only within its exact source/input
  scope. Run required full checks under a fresh watcher where duration is
  uncertain. Final named-workflow acceptance inspects generated component commit
  messages: only selected OS names/revisions/logs present, no transitive Nixpkgs
  name/summary/log, and the final full-graph check preserved. No unnecessary full
  dependency regeneration is required just to test message formatting.
- Historical C3b consumption (superseded by C4): implementer1 owned the org
  workflow pin after lead release.
  Consolidate its unmerged `6874f605` pin into one final immutable C3 provider pin
  above integrated C1 `8306d29`; keep every command/flag and configuration lock
  unchanged. The vpsFree daily OS call has the same provider callback and needs
  the same one-line `CONFCTL_FLAKE` refresh, additive over current master/B1.
  Lead assigned that vpsFree B2 consumer to implementer0 after capacity
  confirmation. Current-default and hook preparation are released; the actual
  pin edit waits for the final committed provider hash and lead release.
  Implementer1 executes provider plus org consumption. Do not sweep unrelated
  consumers. Each changed workflow needs
  exact pin-only comparison, YAML/Bash/action checks, normal hooks and affected
  final review. Integrate the provider before either consumer or hosted dispatch.
- Compatibility/recovery: existing CLI flags and defaults are unchanged; only
  guarded message presentation returns to explicit input selection. No schema, API,
  persisted format, deployed service or configuration output change. Old/new
  Git readers accept every commit. Reverting C3 restores verbose descendant
  messages, while C2 still handles large messages. Preserve merged C1/C2/B1 history;
  user approval and lead integration coordination remain as recorded in state.

### C3 bounded call inventory

| Inspected caller | Actual Nixpkgs/message contract | Disposition |
| --- | --- | --- |
| vpsFree daily workflow at `355e269f`, lines 60–63 | Both genuine Nixpkgs calls have `--no-changelog`; OS call selects `vpsadminos` role with normal logs | Flags correct; consume C3 provider for OS descendant selection |
| org daily workflow at `6874f605`, lines 59–60; channel mapping in flake.nix | nixos-stable has `--no-changelog`; os-staging maps only the root vpsadminos input | Flags correct; consume C3 provider without suppressing OS log |
| HaveAPI `utils/update-nixpkgs.sh` at `3194488d` | Guarded Nixpkgs update has no `--commit`; script writes compact revision-only message | No confctl changelog is generated; no change |
| IRC `tools/update_nixpkgs_flake.sh` at `f15bf557` | Guarded Nixpkgs update has no `--commit`; script writes compact revision-only subject | No change |
| vpsAdminOS flake-update workflow/helper at `0d3fa0a2` | Guarded `--all` has no `--commit`; JSON lock helper writes revision summaries | No change |
| vpsAdmin daily workflow at `6f71da97` | Direct component lock override and custom dependency messages; no confctl Nixpkgs commit call | No change |

This inventories relevant already-audited updater paths, not a second full
workspace inventory. Other scheduled test/performance jobs do not define the
confctl commit-message policy. No application edits or tests were run by architect.

## C4: use the repository-locked confctl input (sufficient)

- Final delivery status from lead: all four final-review lanes passed without
  findings; both packages passed focused acceptance and were integrated.
  Org repair head is `15352aeb13c4011b5dd1a1f78d1fdcb08f7c2420`; vpsFree repair
  head is `7d9807e021e6106d628c021da45f5f55077b2e9c`. Each retains a separate
  generated confctl lock update followed by the workflow correction. No
  `CONFCTL_FLAKE` remains; normal flake.nix URLs and B1 shell/guard contracts are
  unchanged. The implementation/acceptance requirements below are fulfilled
  except the remaining vpsFree hosted result described here.
- Org's final actual run 43484020423 attempt 1 passed all update/final-guard/push
  steps, 18:34:57–18:39:14 UTC, with no generated change. VpsFree's final actual
  run 43484770367 attempt 1 is pending with sole lead-managed monitor `e8ad4567`;
  architect and peers do not observe it independently. Both repository merge
  claims were released and verified. No physical deployment/lifecycle action.
  See [org C4 evidence](evidence-c4-implementer1.md) and
  [vpsFree C4 evidence](evidence-c4-implementer0.md) for full ranges, review,
  package/input identities and focused results.
- User correction: "srsly wtf is this? confctl pin is supposed to be in flake.nix,
  why is there another pin in .github/workflows/daily-update.yml? makes no sense
  to me"; clarified as "there's not supposed to be any pin in the workflow. we
  have flake.lock for that". The existing normal
  `confctl.url = "github:vpsfreecz/confctl"` declaration stays unchanged.
  `flake.lock` is the sole immutable revision authority. C2/C3 workflow-specific
  provider pins are superseded; their merged history and accepted provider
  functionality remain preserved.
- Packages: C4-org owner implementer1; C4-vpsFree owner implementer0, each after
  lead release/capacity confirmation. Each owns only `flake.lock` and
  `.github/workflows/daily-update.yml` in its configuration repository. No
  `flake.nix` hash, extra package output, registry, provider environment override,
  channel, wrapper framework, unrelated consumer or confctl source change.
- Preparation must start from fresh current remote defaults. Lead reports C3
  master runs org 43477762211 and vpsFree 43478026385 completed successfully and
  published generated updates. Fetch and normally fast-forward each existing
  branch before the input update; preserve all merged C1/B1/C2/C3 and generated
  history. Earlier inspected workflow heads were org `69edee80` and vpsFree
  `07a85cae`; they are evidence boundaries, not assumed current merge bases.
- Both configurations use `confctl.lib.mkConfigDevShell` in `tools` mode. Its
  unchanged contract puts `self.packages.${system}.confctl/bin` first in PATH,
  ahead of project binstubs, and bootstraps the declared repository bundle.
  Thus plain `confctl` inside each existing `nix develop` block is exactly the
  declared input's executable. The provider wrapper preserves caller settings
  for Git hooks, covered by accepted C2/C3 evidence; no `bundle exec confctl`
  substitution or ambient-host invocation is needed.
- No channel in either configuration owns the root `confctl` input. Adopt the
  normal published input with the repository command
  `nix develop -c confctl inputs update --commit confctl`, from a clean tracked
  checkout/index and prepared normal hooks. Do not hand-edit lock JSON or use
  an exact-revision override in flake.nix. Expected upstream provider is accepted
  `ff5e017780a35fb97b549db2a51b570193867c3b`; record fresh resolved identity and
  inspect any unexpected upstream advancement before accepting its scope.
  Keep the generated input update separate from the workflow source commit,
  following repository input-update conventions. No automatically scheduled
  confctl self-update is added to these workflows.
- Inspect semantic old/new lock paths, not generated node IDs. Only the root
  confctl source and its owned transitive dependency graph may advance; preserve
  unrelated roots, channel selections and follows relationships. Expected
  provider graph: confctl `ff5e0177`, `confctl/vpsadminos` `67fcc173`,
  `confctl/nixpkgs` `8b8c811c`, and its OS unstable Nixpkgs `f13ff45a`.
  Do not silently promote this tool dependency refresh into production channel
  updates or incidental deduplication changes.
- Remove `CONFCTL_FLAKE` entirely from workflow env. Replace its three org and
  five vpsFree nested `nix shell ... -c confctl` invocations with plain `confctl`
  in the same existing declared-shell blocks, including the final check-update.
  Preserve channel/role selection, `--forward-only`, `--no-changelog`, baseline
  and final lock files, authentication, schedules, permissions and ordinary
  push. Both updater and final guard must resolve to the same declared package.
  For vpsFree's llm-agents block, move the removed wrapper's Nix-only
  `--accept-flake-config` onto that block's existing `nix develop` invocation;
  keep its explicit `nix eval` flags. Do not pass Nix flags to confctl.
- Preserve vpsFree B1's original `--profile` producer and every saved-profile
  consumer, including final guard/push. Its tooling pkgs come from root
  `nixpkgsStable` with the existing Ruby 3.4 overlay, independent of confctl's
  package dependencies. Org uses mkConfigDevShell's default pkgs from
  `confctl/nixpkgs`: its initial tooling Ruby can change during this one-time
  provider adoption, but daily nixos-stable/os-staging updates do not target that
  subtree. Keep the existing org shell structure; no additional profile scheme.
  Bootstrap local verification in an isolated compatible bundle and record actual
  Ruby/Bundler/native identities; do not reuse native gems across a changed Ruby
  merely because its ABI directory matches. Fresh hosted jobs bootstrap normally.
- Quick checks: lock JSON and semantic graph scope, unchanged normal input URL,
  YAML/actionlint/Bash, absence of workflow provider pin/override, all confctl
  calls inside declared shells, retained B1 profile coverage, unchanged updater
  arguments/final guard/push, and normal commit hooks. Evaluate the configuration
  channels/machine inventory with the adopted input; no node or kernel build.
  Record declared shell/package derivation identity as part of preparation.
- After committed whole-range review, focused configuration-environment
  acceptance records `command -v confctl`, its package source matching the sole
  lock revision, actual Ruby/bundle identities and a real final check-update
  invocation through that executable. The vpsFree saved profile must retain its
  exact tool/Ruby identity across a representative lock mutation. Reuse accepted
  C3 selected-only message/guard and C2 transport proof when package/source/input
  identity matches; do not repeat the provider suite. Use existing hook fixtures
  or normal source-hook receipts to cover changed caller environments, and a
  fresh watcher for uncertain duration. Lead then integrates and runs the new
  actual master workflows; C3's passing historical runs are not C4 acceptance.
- Compatibility/recovery: normal published confctl adoption also advances its
  library/tool dependencies. The shell interface is compatible (the inspected
  shell diff only removes unused nix-prefetch-git). Org's older library gains
  existing configuration-info metadata for future generated systems; vpsFree
  already had that support. Evaluate exposed configuration contracts, retain
  existing schemas/rollback paths, and perform no production deployment. Recover
  through additive input/workflow corrections while retaining the sole lock
  authority. An older provider may lack the required guard/C3 behavior; do not
  claim that rolling it back preserves automation or waive guards to publish.
  Do not restore an independent workflow pin or rewrite integrated history.

### C4 inspected lock baselines

| Path | vpsFree at 07a85cae | Org at 69edee80 | Accepted provider graph |
| --- | --- | --- | --- |
| confctl | 7bee58a52372b95c2198ce3f2a719807a3c2c66b | af164b442100b92b8d93c0d67b315eff982e0180 | ff5e017780a35fb97b549db2a51b570193867c3b |
| confctl/vpsadminos | 6f9b2c755143197bd9c3452e1c0121b22e978c4d | a169291a51b9a5d1cab3e084d3b6a1c0280a10b3 | 67fcc17372d175b036706a1459a8b471bfc225e0 |
| confctl/nixpkgs | bd0ff2d3eac24699c3664d5966b9ef36f388e2ca | 26ef669cffa904b6f6832ab57b77892a37c1a671 | 8b8c811c7c2541c30382c5de7ed26be055569c60 |
| confctl/vpsadminos/nixpkgsUnstable | 9ae611a455b90cf061d8f332b977e387bda8e1ca | 15f4ee454b1dce334612fa6843b3e05cf546efab | f13ff45afd1bb73e640eaa08a7066dbed07e3238 |

The exact mkConfigDevShell default-pkgs expression and dependency revisions are
verified. The design-time 30-second version probe timed out and made no runtime
claim. Owner preparation subsequently resolved the identities: org tool Ruby
3.3.10 became Ruby 3.4.9 with Bundler 4.0.7; vpsFree uses Ruby 3.4.11 and its
preserved saved-shell contract. Org's plain final-check/native acceptance passed
in 20 seconds; vpsFree's saved-profile/native/final-check acceptance passed in
23 seconds. Both resolved the exact accepted C3 confctl package/source/derivation,
with full paths and matching input receipts in the linked owner evidence; the
provider suite was reused within that proven identity rather than repeated.

## E1 actual-hook environment amendment (sufficient)

- Owner: implementer2 after lead release; only the daily workflow changes.
  Reviewed source is `9629a74c154a36f0a209a49cca8e71b25424003f`.
- Actual acceptance reached successful generation, native bundle installation and
  hook install/signing, then plain `git commit` failed. The generated hook's
  `#!/usr/bin/env ruby` directly requires Overcommit because this repository's
  configuration has no `gemfile` setting. Its exact LoadError is for `overcommit`.
  RubyGems searches `.gems`, whereas Bundler installs the project gem under
  `.gems/ruby/3.3.0`; clearing the maintenance preload correctly isolated Bundix
  but also removed automatic bundle activation for the final Git hook process.
- One-line repair: replace final `git commit -F "$msg"` with
  `bundle exec git commit -F "$msg"`. Keep `RUBYOPT` cleared during generation;
  activate the refreshed project bundle only for Git and its hook children.
  No `.overcommit.yml`, README, Ruby, generated-data, publication or other
  workflow change. Do not manually construct GEM_PATH or skip hooks.
- Owner reproduced the actual hook failure and proved the proposed command
  against the already prepared bundle: same Ruby 3.3.13, Bundler 4.0.24,
  source-platform Nokogiri 1.19.7 and Overcommit 0.76.0. Real PreCommit and
  CommitMsg hooks passed and made detached generated-only fixture commit
  `d77adcb6ec602584ae53840468a9ae416f759f08`. Retain those exact package paths and
  dependency/output identities in E1 evidence. No repeated generation is needed
  to diagnose this already isolated final-stage failure.
- Quick checks: update focused control-flow expectations to require bundled Git
  commit and preserve failure/no-publication cases; YAML/Bash/action lint and
  normal source commit hooks. Consolidate the unmerged branch, retain old/new
  review ranges and obtain affected-lane final review. Reuse successful unchanged
  generation/native prefix evidence only with its exact identities; run the
  final scoped no-change acceptance after review as directed by lead. Final
  integrated-master workflow still supplies end-to-end hosted acceptance.
- Compatibility/recovery: caller environment only, existing hooks and package
  output remain intact. No runtime state migration. Revert the workflow change
  for source recovery; published/default history is never rewritten.

## E2: activate the IRC bundle for pre-push hooks (sufficient)

- Owner: implementer2 after lead release. Only
  `vpsfree-irc-bot/.github/workflows/daily-update.yml`; additive commit above
  already merged `7f6fb0e5f58c5f76b573dc4df7124a4cae744dfd`. Preserve merged E1
  history. Existing user approval for IRC/master applies; lead owns integration
  and the next hosted run. No new repository or production deployment.
- Hosted run 43454018549 attempt 1 passed generation and the real bundled Git
  commit, then failed in the separate Push updates step. The ambient host
  environment could not activate Overcommit in the pre-push hook. E1 local
  acceptance proved commit/no-change behavior but omitted this process boundary.
  Keep its successful generation evidence; repeating generation cannot resolve
  this already isolated push environment problem.
- Replace only `git push origin HEAD:master` with
  `nix develop -c bundle exec git push origin HEAD:master`. Exact current
  `flake.nix` builds the dev shell from locked Nixpkgs Ruby 3.3 and tools, without
  consuming the generated gemset as a shell package. E1 leaves flake inputs and
  flake.lock unchanged; re-entry therefore selects the same Ruby/tool graph.
  Its existing shellHook selects the project bundle path, installs from the
  refreshed lock and sets Bundler setup. Explicit `bundle exec` retains the
  refreshed project bundle for Git and its pre-push children.
- Preserve the existing `steps.update.outputs.committed == 'true'` condition,
  output producer, checkout/authentication, normal Git push, exact origin/refspec,
  workflow permissions and all other steps. No regenerated pins, profile
  framework, hook bypass/configuration change, README edit or action update.
- Quick checks: YAML/actionlint and shell syntax; exact one-command delta;
  focused push-step coverage requiring the Nix/bundle invocation, unchanged true
  gate and no push on false. Normal source commit hooks remain required. Commit
  the additive change and obtain affected-lane independent final review before
  any uncertain-duration runtime acceptance. Existing E1 review/ranges stay
  retained, with the new base/head and source delta supplied separately.
- Required focused actual acceptance uses the retained generated bundle/source
  receipts and a disposable local bare Git remote only. Seed that receiver's
  `refs/heads/master` with a known ancestor of the candidate, matching the existing
  GitHub master branch. An empty receiver cannot resolve the unchanged unqualified
  `HEAD:master` destination from the detached fixture and fails before hooks;
  that is a fixture setup failure, not evidence about the repaired hook boundary.
  Execute the exact new
  push command with its real installed Overcommit pre-push hook; prove it loads
  the same Ruby/refreshed bundle and advances remote master to the expected
  local commit. Then use a deliberately rejecting fixture-only PrePush hook and
  a further local commit: the same command must return failure while the bare
  remote ref remains unchanged. Preserve the hook's normal stdin/arguments and
  record positive/negative remote SHAs. Fixture instrumentation is not source
  configuration. No hosted push or fresh dependency generation belongs in this
  test. Use a fresh watcher if duration is uncertain; do not reuse the earlier
  commit-only proof as pre-push acceptance.
- After that result, lead integrates the reviewed additive head and dispatches
  a fresh master run; full acceptance includes the previously failing push step.
  Record checkout/source and generated commit identity even if upstream
  dependencies moved since local evidence. No old-SHA rerun as fix validation.
- Compatibility/recovery: workflow process environment only; no application,
  schema, API, persistent format or deployed system change. Existing Git hooks
  and GitHub authorization remain in effect. Additive revert restores the old
  command, including its known hook-environment failure; never rewrite merged
  E1 history or generated commits already published by authorized automation.

## H1 persistent Fedora SSH activation amendment (sufficient)

- Owner: implementer0 after lead release; still only
  `vpsfree-kb-contracts/tests/suite/kb/firewall.nix`. Reviewed old head
  `2cfbde649769509e2628600535e3023d872f1735` remains the original review boundary.
- The reviewed focused run failed after restart: all socat listeners were ready,
  but TCP 22 never appeared. SSH had started and shut down cleanly before that;
  post-restart logs show no standalone SSH activation. The all-port wait correctly
  rejected the fixture. Package/version and exact run evidence remain owner-held.
- Published Fedora 45 image inspection proves both persistent target links:
  `multi-user.target.wants/sshd.service` and `sockets.target.wants/sshd.socket`.
  The socket unit declares `Conflicts=sshd.service`, `ListenStream=22` and
  `Accept=yes`. Enabling/starting the service does not disable the conflicting
  socket's next-boot membership. This fixture therefore selected a running
  service without selecting a consistent persistent activation mode. The exact
  failed boot's transaction arbitration was not retained and is not claimed.
  The image predates the run, but its exact archive hash was not captured by
  that run; preserve this association limit rather than invent exact provenance.
- Repair only the Fedora firewalld setup: run
  `systemctl disable --now sshd.socket` before the existing
  `systemctl enable --now sshd.service` path. Keep the vendor service, host-key
  handling and all existing listener units. Assert/record the socket is disabled
  and inactive and the service enabled and active before the firewall exercise
  and after restart. No forced start after restart, socket substitution, new
  service implementation, firewall-policy change, timeout growth or retries.
- Keep H1's all-port readiness and unchanged dual-stack/established/denied-port
  assertions. Include explicit `sshd.service` and `sshd.socket` in failure status
  diagnostics so an unloaded failed-to-start service is not omitted by wildcard
  matching. Other distributions' activation selection remains unchanged.
- Quick checks: Nix format/parse, generated Ruby syntax, existing readiness probe,
  and a narrow setup-order/control-flow check proving socket disable precedes
  service enable and failure prevents progression. Reuse unchanged static contract
  evidence where its inputs are unchanged. Commit/consolidate unmerged history,
  retain old/new range and final diff, then affected-lane independent review.
- After review, one additional focused firewalld runtime on the repaired head
  must prove initial and post-restart service/socket mode, every listener and all
  original firewall assertions. Preserve exact image/source/dependency identities
  and native runner result. This is verification of changed source, not an
  unmodified retry. No broad KB run or image/package/configuration pin expansion.
- Evidence: published image archive SHA256
  `b63c150090d0c594d2348a272bb493e9e7fb644bb81a19b4142210742cce46c4`, ETag
  `6aeed93c-fa8bc00`, last modified 2026-11-07; unit inventory is retained by
  owner. Independent read-only extraction of the official OpenSSH
  `10.5p1-1.fc45` RPM confirms vendor `WantedBy=multi-user.target`; the systemd
  local-unix SSH generator does not establish TCP activation. See audit.md.
- Compatibility/recovery: fixture setup explicitly selects the same standalone
  service it already starts. No production daemon/page/example behavior or
  persistent schema changes. Revert the fixture commit for source recovery;
  test-owned guests retain ordinary runner cleanup/ownership.

## C1/E1 manual-trigger amendment (sufficient)

- Reason: the user approved immediate actual workflow runs after integration.
  Both repaired daily workflows currently accept only schedule events. Re-running
  an old failed run retains its original event SHA/ref and does not validate the
  new workflow definition. GitHub documents the
  [manual trigger/default-branch requirement](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow)
  and [rerun identity](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/re-run-workflows-and-jobs).
- Exact source verified from this session's feature refs:
  `vpsadminos-org-configuration` at
  `cdb886678ba30d10b5114cab279d5eb602209954` has only schedule `40 4 * * *`;
  `vpsfree-irc-bot` at `41fd2f146d1fe7aa548e68b859a5d60cf2c55ba4` has only
  schedule `30 4 * * *`. Both files are `.github/workflows/daily-update.yml`.
- Owners: implementer1 for C1; implementer2 for E1, allocated by lead only after
  current work is explicitly parked/reported and capacity confirmed. The two
  edits are independent. Add an empty `workflow_dispatch:` mapping entry beside
  `schedule:` in each file. No inputs, additional schedules, branch framework,
  permissions, authentication, action refs, checkout behavior, jobs, update
  commands, guards or push semantics change. Existing upstream action checks
  remain applicable because no `uses:` ref is selected or changed.
- Acceptance/quick checks: YAML/action lint accepts both triggers and unchanged
  cron; normalized comparison proves removing only the new trigger reproduces
  the prior workflow structure. Normal repository hooks pass. Original final
  review completes on the exact heads above; owners then commit the trigger-only
  change, consolidate final branch history under ordinary rules, and provide
  old/new ranges and final diff for affected-lane follow-up review. No repeat of
  unchanged expensive updater fixtures is required solely for this event addition.
- Lead runs the new dispatch **after** reviewed final heads are integrated and
  verified on remote master, explicitly selecting `--ref master`. Do not run
  these default-branch-writing updaters on the feature ref. Record repository,
  workflow, event, run ID/attempt, event head, actual checkout head when different,
  and final result; current package owners retain failure diagnosis. C1 already
  explicitly checks out master; E1 uses the event source and still pushes master,
  so selecting the approved master ref is essential. No pre-integration dispatch
  or rerun of an old failed event substitutes for this acceptance.
- Compatibility/recovery: scheduled behavior and updater output contracts remain
  unchanged. The additional entry point uses existing repository write-access
  controls and has no custom parameters. Removing the trigger reverts manual
  invocation availability; no persistent format or deployed-system change.

## Settled audit dispositions and remaining work

All 26 project-map repositories are covered: the named pair plus 24 others.
Implementation briefs B1, C1, E1, F1, G1, H1 are sufficient and independent except
for normal owner-capacity sequencing. Lead tracks allocations/acceptance in
state.md; this document does not queue work on busy implementers.

HaveAPI performance is a separate product regression, as recorded in audit.md;
leave the workflow, reference and budgets unchanged. KB NixOS's evidenced GitHub
HTTP 504 needs no speculative retry code. The latest vpsAdmin general weekly CI
passed; its older failure is not a demonstrated current regression. Syslog's
schedule has no retained runs, so its execution is explicitly unverified.
These dispositions do not block the automation repairs and must remain visible
in the final report. Stop additional inventory/history expansion now; remaining
architecture work is current-package clarification and checking deviations.

## Evidence and delivery

See [audit](audit.md), [vpsadminos.org evidence](evidence-vpsadminos-org-configuration.md)
and incoming per-repository evidence. Implementers preserve normal hooks, commit
all intended edits, supply full base-to-head history and no-migration conclusions,
and publish feature branches. Lead accepts packages and invokes final independent
review. No new runtime service, machine claim or merge claim is needed.
