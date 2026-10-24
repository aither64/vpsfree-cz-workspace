# Package B: guarded updater, CLI and documentation

Status: implemented, quick-checked, committed and feature source published.
Final independent review and longer/package/consumer verification remain pending.
No repository-default integration, release, deployment or lifecycle action occurred.

## Identity and ownership

`dev-session current`, `DEV_SESSION_SLUG`, `DEV_SESSION_WORKSPACE` and trusted
thread binding all matched this initiative. Retained implementer1 access is
`workspace_write`. Implementer0 initially owned confctl Git and the six A files;
after explicit handoff with no unfinished command effects, implementer1 staged
all twenty intended A+B paths and used ordinary hooks for one coherent commit.
Lead performed the required direct user-facing prose pass, including the final
safe errors and JSON listing contract.

## Exact feature history and publication

- Repository: `git@github.com:vpsfreecz/confctl.git`.
- Worktree: `worktrees/2026-10-24-flake-update-downgrade-guard-replacement/confctl`.
- Feature branch: `2026-10-24-flake-update-downgrade-guard-replacement`.
- Freshly fetched base: `cc40679d267165aecfa569128438bb55fe910268` (`origin/master`).
- Final head: `7ba361d22a4aac044cb02abf8397800bcf5726bf`.
- Complete base-to-head series: one commit, `Guard automated input updates with ancestry validation`.
- Final diff: 20 files, 1598 insertions, 34 deletions.
- Fresh SSH `git ls-remote origin refs/heads/2026-10-24-flake-update-downgrade-guard-replacement`
  returned that exact head after successful push. Working tree and index clean.
- Consumer pin: `github:vpsfreecz/confctl/7ba361d22a4aac044cb02abf8397800bcf5726bf#confctl`.
- History disposition: no superseded pin stream or obsolete implementation commits.
  No database, persisted-state or other migrations. No migration was merged,
  released, deployed or externally consumed. Consumers may now use this exact
  source; retain its feature ref if later history work would otherwise remove it.

## Intended paths

B owns:

- `lib/confctl/inputs/updater.rb` and new `guarded_update.rb`.
- `lib/confctl/flake_lock.rb`, `lib/confctl/flake_lock_diff.rb`.
- `lib/confctl/cli/app.rb`, `lib/confctl/cli/inputs/{root,channels,machines,update_result}.rb`.
- `spec/inputs/guarded_update_spec.rb`, `spec/confctl/cli/inputs_forward_only_spec.rb`, `spec/flake_lock_spec.rb`.
- `docs/flake-inputs.md`, `man/man8/confctl.8.md`.

The same commit includes A's three policy/resolver/provider files and three
isolated specs; source and follow-up-fix ownership of those remains implementer0.

## Implemented guarantees and API

Guarded root/channel/machine updates use a cooperating process lock, require an
existing tracked version-7 lock and a clean tracked checkout/index, then snapshot
exact lock/root flake bytes, HEAD and index entries. Nix runs from the original
flake directory with separate reference/output locks on the same filesystem.
Requested follows aliases resolve to terminal update paths without refreshing
parents. No in-place fallback exists. Unmatched-selector and cached-metadata
warnings fail. Full semantic graph validation and snapshot recheck precede
atomic rename and optional commit. Failures before install preserve confctl's
original lock/index/HEAD; concurrent changes are left for their writer to resolve.
A hook failure after install leaves the validated lock available and returns
failure. This is a per-invocation transaction with a single-writer precondition;
it does not freeze external path sources or undo earlier workflow commits.

`check-update --old-lock FILE --new-lock FILE` reads both locks and invokes the
same policy without Nix/update/commit. Exit 0 means accepted/unchanged; known
rejection is 3; unknown/unsupported evidence and tool failures are 1. Neither
nonzero result permits publication. `--downgrade` is still only changelog
selection. Unguarded updates and explicit setters retain existing behavior.

`inputs ls --json [pattern]` emits sorted rows with fields
`{input,type,ref,rev,url}`. Revision is the full follows-resolved revision or null;
an unmatched pattern gives `[]`. The default table stays at eight characters.
There is no separate consumer graph resolver.

Supported source/ancestry/provider limits are documented with A's actual policy:
GitHub sources only for changed immutable revisions; unchanged unsupported
sources may remain; strict path removal/source/extraction/same-SHA locked-change
policy; GITHUB_TOKEN then GH_TOKEN; separate Nix credentials; bounded HTTP waits;
no redirect or automatic retry. Ancestry does not detect later reverts or prove
patch equivalence or compatibility.

## Verification

Declared confctl `nix develop` shell used throughout checks and the successful
commit/push. Compact results are in `package-b-quick.log`.

- `bundle exec rspec spec/inputs spec/confctl/cli/inputs_forward_only_spec.rb spec/confctl/cli/inputs_set_output_spec.rb spec/flake_lock_spec.rb`:
  143 examples, zero failures, 20.99 seconds. Includes A checks plus B's transaction
  byte/index/HEAD preservation, whole-candidate rejection, concurrent lock/flake/
  tracked import/HEAD/index changes, interruption, no-change, hook failure,
  cached-warning/unmatched-selector failures, terminal follows selection and full
  nested summaries, actual CLI 0/3/1 statuses, JSON metadata/null/filter/table
  compatibility and actual legacy settings/channels outputs without moduleOptions.
- Existing `bundle exec rspec spec/confctl/inputs_spec.rb`: one example, zero
  failures, 4.85 seconds; unguarded local-Git update and setter/changelog workflow.
- RuboCop over inputs, reader/diff, CLI app/input commands, inputs specs, JSON CLI
  spec and reader spec: 25 files, no offenses.
- `bundle exec rake md2man:man`: exit 0; generated man output is ignored as expected.
- `git diff --check` and staged diff check: clean.
- Ordinary commit hooks: Nixfmt OK, RuboCop OK; no stash/reset/clean or hook bypass.
  Commit-message hooks passed with soft 72-column body warnings; all lines obey
  the workspace's 80-column requirement.

The first ambient-shell source push was rejected by the Overcommit configuration
signature check before creating the remote branch. Repeating the same intended
push in the declared Nix shell succeeded without changing signatures or bypassing
hooks. Git operations that invoke these hooks must run in that environment.

The initial channels-only fixture failed because existing `Nix.new` settings
initialization evaluates `.#confctl.settings`. The architect verified both old
configuration pins export settings and channels; the accepted fixture includes
`confctl.settings.nix.maxJobs = "auto"` and channels while omitting moduleOptions.
No broad Nix evaluation behavior change was made. This preserves settings-derived
impure evaluation behavior in existing configurations.

## Remaining work

Lead owns final mandatory review for all A/B/C/D deliverables and shared state.
Do not call the branch ready for integration until that gate completes. Long full
suite, package build/CLI checks, seven consumer disposable runs, target-movement
simulation and bounded live API smoke remain post-review work. No long suite was
run by B. The package wrapper sets its own GEM_HOME/GEM_PATH/RUBYLIB and prepends
its bundled Nix; actual package execution in each old configuration shell must
still demonstrate that it selects new code and record the bundled Nix version.
Nix interface minimum is docs-backed 2.19; actual nested selector/transaction
prototype is 2.34.9. Do not claim the complete oldest-version matrix verified.

C owner received the exact published source and JSON schema. D now adopts this
external CI tool in the two configuration workflows and leaves deployment-tool
flake pins unchanged; it requires its separate assignment/roster recheck.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/>

## Documentation-only source refresh

The original development head `d58181a4d8b0de716fdb93c56f524175dd36cce4`
was amended to `7ba361d22a4aac044cb02abf8397800bcf5726bf` after the lead
required publication examples to check an exported `HEAD:flake.lock` snapshot.
Only `docs/flake-inputs.md` and `man/man8/confctl.8.md` differ between those
heads; all application code, APIs and tests are identical. The lead completed
the direct prose pass, man generation and ordinary hooks passed, and the
feature was force-pushed with an exact lease for the previous remote head.
Fresh SSH remote proof returned the new head. The full series remains one
coherent feature commit with no migrations. No released/deployed consumer
boundary exists; all development consumer pins move to the new head together.
Superseded active provider CI Tests run 40092415963 was canceled after the push;
completed old checks and current-head checks were left alone. The new push
automatically triggered current-head CI; no long local suite/package build
was manually started or awaited before final review.
