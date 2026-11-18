# Package C: forward-only updates

Owner: implementer0. Prior package A accepted by lead; capacity confirmed before
starting C. Same-session identity, full environment pair and live roster verified;
implementer0 retains workspace-write access. Lead owns scope, acceptance, final
review and user-facing prose application before commit. Architect0 owns D5 design.

Current: implementation, quick/full checks, independent final review, feature
publication and CI complete; package accepted by lead. No confctl integration
or deployment is authorized.

## Preparation

- Fresh fetched default/base: `ff5e017780a35fb97b549db2a51b570193867c3b`.
- Remote: `git@github.com:vpsfreecz/confctl.git`, default `master`.
- Registered branch `2026-11-18-nixos-channel-update`, worktree
  `worktrees/2026-11-18-nixos-channel-update/confctl`.
- Read local AGENTS/README, flake-input guide, current guarded update/strict
  validator/lock-graph/CLI behavior, tests, man sections, unreleased changelog,
  hooks, Rake tasks and CI. Required unchanged workspace procedures from package
  A remain applicable; scope/phase routes rechecked and writing route added.
- Normal checkout hook refused changed Overcommit signature; reviewed unchanged
  `.overcommit.yml` (Nixfmt/RuboCop + CommitMsg). Documented `nix develop` became
  usable after local Bundler installation; `bundle check`,
  `bundle exec overcommit --install`, `bundle exec overcommit --sign` passed.
  Ruby 3.4.9 and RSpec 3.13 available. No bypass. Bundler 2.5.7 emits duplicate
  RubyGems platform-constant warnings under Ruby 3.4; this did not fail setup.
- No application edits began before architect D5 sufficient brief and lead release.

## Scope and evidence

One narrow confctl package, no configuration input changes, PR, default
integration or deployment. Intended behavior is behind/equal no-update success,
independent forward inputs retained in one atomic update, real errors/rejections
still fatal, strict check-update unchanged. Interfaces and verification follow
accepted D5. Individual package evidence remains here; lasting behavior belongs in
confctl's existing input guide/manual and unreleased changelog. Lead receives
settled changed user-facing prose once before commit.

Final source/history, quick checks, documentation placement and no-migration
conclusion follow, with full checks and publication proof at the end.

## Reviewable implementation

D5 sufficient brief and lead release accepted. Core source, tests and docs are
complete at head `d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49`, based on
`ff5e017780a35fb97b549db2a51b570193867c3b`. One coherent commit:
`inputs: skip behind revisions during guarded updates`. Final diff: 14 files,
452 insertions and 79 deletions. Worktree clean. Complete series has no obsolete
approach, follow-up or repeated input/generated pin stream. No migrations,
release, deployment or external use. This was the source reviewed independently;
feature publication proof follows below.

Changed-file inventory:

- `lib/confctl/inputs/{forward_guard,guarded_update,updater}.rb`
- `lib/confctl/cli/app.rb`
- `lib/confctl/cli/inputs/{update_result,root,channels,machines}.rb`
- `spec/inputs/{forward_guard,guarded_update}_spec.rb`
- `spec/confctl/cli/inputs_forward_only_spec.rb`
- `docs/flake-inputs.md`, `man/man8/confctl.8.md`, `CHANGELOG.md`

Implementation follows D5 without material deviation. The strict validator keeps
its statuses and issues, with typed policy rejections and `behind_only?` added.
The transaction groups/sorts original terminal targets, rechecks all selections,
tries one complete Nix candidate per target against the last accepted lock,
skips only behind-only rejections, validates the final graph against baseline,
checks the checkout snapshot and installs once. Commit composition gets only
accepted selected names. Results add `skipped` and `updated_inputs`; final changes
never include discarded candidates. Shared CLI summaries distinguish skipped
attempts from installed changes and preserve channel/machine role context.

No new flags, solver, retry loop, workflows, pins, dependencies or lock schema.
Conservative skips of interdependent attempts are an accepted bound. Both
configuration repositories' daily jobs remain consumers of their old pinned
confctl until a separately authorized pin update. Old/new tools read the same
lock format; returning to the old binary restores behind-is-error behavior.
Strict `check-update`, unguarded update and explicit `set` retain their policies.
Source compatibility covers additive Ruby result fields and a local
GuardedUpdate/Updater callback change; no external callback users were found.

## Quick checks and fixes

Inside repository `nix develop`:

```sh
bundle exec rspec spec/inputs/forward_guard_spec.rb spec/inputs/guarded_update_spec.rb spec/inputs/commit_message_spec.rb spec/inputs/lock_graph_spec.rb spec/confctl/cli/inputs_forward_only_spec.rb
```

Final result: 128 examples, 0 failures in 25.91 seconds. Changed-file RuboCop:
11 files, no offenses. `bundle exec rake md2man:man` succeeded; generated output
is ignored. `git diff --check` passed. Commit hooks passed Nixfmt/RuboCop and
SingleLineSubject/TrailingPeriod. TextWidth emitted 72-column warnings only;
all actual commit lines satisfy the workspace 80-column limit. No Nix files
changed, so no Nix fixture formatting change was needed.

Focused coverage proves exact bytes/index/HEAD and no commit for behind/no-op;
accepted descendants; deterministic order and alias deduplication; one final
rename/one commit for independent mixed outcomes; accepted-reference sequencing;
discarded rejected references; nested and shared dependency protection; selected
alias redirection failure; final strict baseline validation; later policy,
evidence and Nix failure atomicity; mixed behind/hard-failure rejection. Existing
concurrent-writer, cached-response, interruption and post-install hook failure
regressions remain. Strict CLI `check-update` still rejects a behind artifact
with status 3. A real two-local-path Nix fixture exercises sequential
reference/output lock generation without live upstream resolution; supported
Git ancestry is separately covered through existing provider/guard fixtures.

Initial 128-example run had eight new fixture/assertion failures (six invalid
RSpec double wrappers, one commit-summary whitespace expectation, one synthetic
initial lock missing `original`). Fixture fixes led to one isolated missing
Logger dependency in the real-Nix test; using a real quiet TTY executor made
all 38 transaction cases pass in 7.41 seconds. Final combined run above passed.
Changed lint then corrected seven layout/tempfile cleanup offenses; final lint
and hooks passed. These were test/setup corrections, with no hidden failed
product check or skipped required assertion. Logs are disposable in
`package-c-raw/{focused,repair-focused,quick-final,commit}.log`.

## Documentation and review routing

| Topic | Reader / class | Authoritative home | Evidence |
| --- | --- | --- | --- |
| Guarded transaction, selection order, skip/error and publication semantics | Operators / reference and how-to | `docs/flake-inputs.md`, already linked from README | D5 and focused transaction/CLI regressions |
| Command flags, strict checker and recovery contracts | CLI users / reference | `man/man8/confctl.8.md`, `cli/app.rb`, shared result helper | Help specs and successful man generation |
| Intentional exit-3 to success compatibility change for behind update attempts | Maintainers / unreleased change note | `CHANGELOG.md` Unreleased | Strict check-update remains unchanged |
| Exact branch, checks, individual execution | Lead/reviewer / session evidence | This file | Logs and complete Git range |

Lead directly applied vpsfree-user-facing-writing/humanizer-en to settled prose
and returned exact wording corrections. All were applied before commit; existing
post-install-hook-failure and source recovery constraints are retained. No
separate project receipt or options-reference regeneration was added.

Complete final packet reported via `3d447b90-7d00-4b11-a6e8-c507f0be2a2e`.
Suggested risk is high because CLI exit/atomic installation contracts change;
general, architecture, scope and risk lanes apply. Lead owns independent reviewer
selection/assignment and final packet completeness. No full suite, full repo
lint, CI or publication has run yet; awaiting final independent review before
that phase. No live fleet build or deployment belongs in this package.

Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-18-nixos-channel-update/

## Independent review and full checks

Lead accepted [confctl-review.md](confctl-review.md): reviewer0 retained
gpt-6.1-sol/xhigh, all four lanes, exact original base to `d8ab7d4`. No Blocking,
Important or Advisory findings. Whole history, no migrations, source boundaries,
recovery contracts, focused coverage and documentation routing accepted. No
source changes were required. Full checks were then explicitly released by lead.

Fresh watcher `/root/c_full_checks` (gpt-6-luna/low) owns the documented Nix-shell
batch of full `bundle exec rspec` and `bundle exec rubocop`, exact reviewed head
`d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49`. Installed utility package
`/nix/store/zdr7y043hi6y4sbfbsixsrlgbvd530nk-dev-workspace-0.2.0`, catalog digest
`780db421a46b2a3bb6128dcc60b706de0753bd2a564c2e5f3c310344f3fce0bb`,
utility native identity `dw_32fc0df129055f50f5e6054c8d971d33430112edeba8b88d`,
full_access/never reverified. Exact launcher and separate logs/status are in
`package-c-raw/`. No repeat man generation or extra integration test was added.
Batch passed: RSpec status 0, 245 examples, 0 failures, 2 expected pending;
RuboCop status 0, 110 files, no offenses. Script start/finish
2026-11-18T18:40:33Z–18:41:45Z (72 seconds; RSpec 65.44 seconds). Invocation
`82fcdf52-5012-4e30-a793-5f3c075cf5e3`, command session 60420 finished exit 0;
all operation effects quiescent. Pending cases are the two existing packaged CLI
caller-environment examples in `package_environment_spec.rb` requiring
`CONFCTL_BIN` to point at a Nix-built package. No source-suite example failed.
They remain an honest package-binary coverage gap; push CI owns its matrix.

## Publication and final handoff

Fresh fetch after full checks showed unchanged `origin/master`
`ff5e017780a35fb97b549db2a51b570193867c3b`, zero commits behind and one ahead.
No rebase or reviewed patch change occurred. Ordinary
`nix develop --command git push --set-upstream origin HEAD:refs/heads/2026-11-18-nixos-channel-update`
over SSH succeeded with hooks intact. Fresh `git ls-remote --heads origin
refs/heads/2026-11-18-nixos-channel-update` equals
`d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49` exactly. Source worktree clean.
Ordinary comparison capture recorded exact original base and final head.

One bounded Actions API read discovered these runs for exact final head,
attempt 1, all in progress at handoff. Lead owns CI monitoring; no duplicate
observer was launched.

| Workflow | Workflow ID | Run ID / URL |
| --- | --- | --- |
| Tests | 242179286 | [44372697108](https://github.com/vpsfreecz/confctl/actions/runs/44372697108) |
| RSpec | 240426206 | [44372697114](https://github.com/vpsfreecz/confctl/actions/runs/44372697114) |
| RuboCop | 240426208 | [44372697153](https://github.com/vpsfreecz/confctl/actions/runs/44372697153) |

Complete package reported to lead with exact local/remote proof and remaining CI
dependency. No default merge, PR, consumer pin, release, activation or lifecycle
action occurred. Implementation owner retains follow-up fixes for this package.

## CI completion follow-up

Lead requested one bounded read-only runner diagnostic while retaining
authoritative GitHub observation of Tests run 44372697108/job 135043484447.
Existing SSH access worked. Exact confctl checkout ref on the runner matched
`d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49`. Its test log bound the run through
state directory `/tmp/os-test-runner-309099429-44372697108-1` and ended at
19:09:28 UTC: four test scripts successful in 1532.96 seconds. The slower tail
was progressing through carrier/deploy builds and activation assertions;
carrier/deploy succeeded in 1532.94 seconds. The runner had moved to another job
by the read-only process snapshot. No stalled test or blocker remained.

Lead independently confirmed authoritative GitHub SUCCESS at 19:09:36 UTC with
no failed steps, then accepted package C including CI. Final SSH read joined
exit 0; no remaining diagnostic command, watcher or tool session. No remote
writes, credentials/environment reads, setup, retries, cancellation, restarts,
source changes or additional tests occurred. Integration direction remains a
separate lead/user dependency; no consumer pin or deployment is authorized.
