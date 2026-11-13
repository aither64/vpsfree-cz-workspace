# B0: vpsfree-cz-configuration scheduled updates

Investigation owner: implementer0. Package B0 is ready for acceptance; no
application edits, builds, reruns, pushes, PRs, integration or deployments.
Implementation remains dependent on an accepted architect brief and lead release.

## Scope and identity

- Verified `dev-session current` returns `2026-11-13-scheduled-workflow-fixes`;
  both environment markers match the trusted thread binding and workspace
  `/home/aither/workspace/ai/vpsfree.cz`.
- Read workspace AGENTS, projects, sessions, documentation, verification, git,
  commits and agent-teams procedures, documentation/handoff skills, and the
  configuration repository's AGENTS and README.
- Checked the live same-session roster; implementer0 retains
  `gpt-6.1-sol` / xhigh / workspace_write and effective full access.
- Read repository source only from its canonical bare clone and GitHub API.
  No other session's worktree was accessed. No fetch was needed.
- GitHub default head inspected: `6e9ed6fb3ded5d72fbfa31c3feb4fccfcdfee494`.
  Bare HEAD was older (`86e19685313270d88e4db30038c056ce4b807abd`), so workflow
  evidence uses GitHub's current source and exact run revisions.

## Result

The updater reenters `nix develop` after changing the stable nixpkgs input.
This selects a different Ruby derivation while retaining the repository's
native gems under `.gems/ruby/3.4.0`. The first run in the continuous failure
streak proves the resulting native-library incompatibility. The latest three
runs encounter a hook loading failure earlier, when the Codex update needs a
commit. Their logs exhibit the same Ruby transition, but Overcommit hides the
underlying LoadError; the exact native library responsible for those three
masked failures is not recorded by the runner.

This is a workflow/toolchain consistency problem. The inspected evidence does
not indicate an infrastructure outage, unavailable upstream, GitHub
authentication failure, or stale imported action major.

## Required run sample

All rows are scheduled event, attempt **1**, workflow `daily-update.yml`
(workflow ID `166934900`). Exact attempt job metadata and logs were inspected.

| Run (UTC date) | Exact head | Result / failing step |
| --- | --- | --- |
| [533 / Nov 13](https://github.com/vpsfreecz/vpsfree-cz-configuration/actions/runs/43425681836/attempts/1) | `6e9ed6fb3ded5d72fbfa31c3feb4fccfcdfee494` | Failure: Update llm-agents when Codex changes; job `131886408442` |
| [532 / Nov 12](https://github.com/vpsfreecz/vpsfree-cz-configuration/actions/runs/43224121534/attempts/1) | `dda57166bd8bb6d85a74decdd05a8810933bdecc` | Same failure; job `131202778911` |
| [531 / Nov 11](https://github.com/vpsfreecz/vpsfree-cz-configuration/actions/runs/43016930206/attempts/1) | `3c088a4b71881b3649441ce3c4e92c71757708e6` | Same failure; job `130510220986` |
| [517 / Oct 28: last success](https://github.com/vpsfreecz/vpsfree-cz-configuration/actions/runs/40674539688/attempts/1) | `4715580512a4042bea75cb44167efb42b3618f70` | Success, including llm-agents commit, dependency updates and final check/push; job `122769484334` |
| [518 / Oct 29: first continuous failure](https://github.com/vpsfreecz/vpsfree-cz-configuration/actions/runs/40862091609/attempts/1) | `7a254c88b0b54a32300a319b3e4ed32936d9b004` | Failure: Update package dependencies; job `123407600394` |

The 30-run schedule listing shows all runs 518 through 533 failed. An isolated
Oct 26 failure predates two successful schedules and was not expanded. One
additional Nov 9 log (`42623656551`, attempt 1) was inspected to confirm that
the later generic Overcommit failure already existed before the latest sample.
No broad history scan was needed after the toolchain cause became clear.

## Exact failed-attempt evidence

### Latest three schedules

In all three attempts checkout, Nix installation, hook installation, cache
restore and Update inputs succeed. All three input-update commits run the
configured pre-commit and commit-message hooks successfully. Then a fresh
development shell is entered for the llm-agents step.

- Nov 13 at `12:37:10.1990273Z`: Codex `0.165.0 -> 0.167.2`.
  At `12:37:17.9028148Z`, Overcommit reports that the configured Gemfile lacks
  Overcommit; at `12:37:17.9059391Z`, confctl reports `git commit failed`.
- Nov 12 at `13:13:24.4618818Z`: Codex `0.165.0 -> 0.167.2`;
  same errors at `13:13:31.7923075Z` and `13:13:31.7956308Z`.
- Nov 11 at `12:08:45.7542548Z`: Codex `0.165.0 -> 0.167.1`;
  same errors at `12:08:53.8677346Z` and `12:08:53.8706832Z`.

The root [Gemfile](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/6e9ed6fb3ded5d72fbfa31c3feb4fccfcdfee494/Gemfile#L6)
does contain `gem 'overcommit'`. The lock contains Overcommit 0.73.0.
Its [hook template](https://github.com/sds/overcommit/blob/v0.73.0/template-dir/hooks/overcommit-hook#L46)
catches every `LoadError` raised by `require 'overcommit'` and prints this
missing-gem message, so it does not identify the real failed require.

Nov 13's initial shell substitutes Ruby 3.4.9 and its later shell substitutes
Ruby 3.4.11. Earlier commits still use the original shell; the next step
reevaluates the changed lock. Package updates and final check/push are skipped
after the hook failure, so no remote push is attempted.

### First failure after the last success

Oct 29 starts with Ruby 3.4.9, updates stable nixpkgs, then substitutes Ruby
3.4.11 when reentering the dev shell. Codex is already `0.165.0`, so that step
does not need a commit and succeeds. The next step runs
`gem install --no-document bundler` and fails at `11:08:20.3511077Z`:

```text
linked to incompatible /nix/store/3rcm37q1arwggzjxzcnbiz5s8a7c1ppx-ruby-3.4.9/lib/libruby-3.4.9.so.3.4
.../.gems/ruby/3.4.0/gems/date-3.6.0/lib/date_core.so (LoadError)
```

The running interpreter is
`/nix/store/hyrhia8cgzghr216z0r5wnbsqg7gbb9x-ruby-3.4.11`.
This directly proves cross-derivation reuse of a native gem. Oct 28's successful
run updates unstable nixpkgs and vpsAdminOS, leaves the stable toolchain
unchanged, and successfully updates llm-agents, root gems and package gems.

## Source locations and causal chain

- [daily-update.yml:37](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/6e9ed6fb3ded5d72fbfa31c3feb4fccfcdfee494/.github/workflows/daily-update.yml#L37)
  boots the initial shell and installs hooks/gems.
- [daily-update.yml:52](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/6e9ed6fb3ded5d72fbfa31c3feb4fccfcdfee494/.github/workflows/daily-update.yml#L52)
  enters a shell, then line 58 updates stable nixpkgs along with production and
  staging inputs. Subsequent commands in that same shell retain the old Ruby.
- [daily-update.yml:68](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/6e9ed6fb3ded5d72fbfa31c3feb4fccfcdfee494/.github/workflows/daily-update.yml#L68)
  enters a freshly evaluated shell; line 84 invokes pinned confctl and a
  hook-triggering llm-agents commit. Lines 100 and 181 independently reenter
  the shell for package updates and the final check/push.
- [flake.nix:86](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/6e9ed6fb3ded5d72fbfa31c3feb4fccfcdfee494/flake.nix#L86)
  imports the root nixpkgs input for development packages; root nixpkgs follows
  `nixpkgsStable`. The development shell uses Ruby 3.4 and `mode = "tools"`.
- [mk-config-devshell.nix:32](https://github.com/vpsfreecz/confctl/blob/7bee58a52372b95c2198ce3f2a719807a3c2c66b/nix/flake/mk-config-devshell.nix#L32)
  puts gems under `$PWD/.gems/ruby/<ruby_version>`, with Ruby's `ruby_version`
  equal to `3.4.0` for both derivations. It does not encode the full interpreter
  derivation or rebuild already installed native gems when that changes. This
  is the development-shell confctl input (`7bee58a5`), distinct from the
  explicitly selected updater/guard tool (`822c0e35`).
- [nix/package.nix:25](https://github.com/vpsfreecz/confctl/blob/822c0e35dbe2549111912f539116b4225dfd3035/nix/package.nix#L25)
  changes GEM_HOME/GEM_PATH to packaged confctl dependencies, retaining caller
  preload environment. [GitCommit:11](https://github.com/vpsfreecz/confctl/blob/822c0e35dbe2549111912f539116b4225dfd3035/lib/confctl/inputs/git_commit.rb#L11)
  invokes Git normally. This deserves hook-environment regression coverage,
  but does not explain why early commits pass and later commits fail as well
  as the observed shell transition does.

## Fix boundary and remaining verification

Architect decision needed: retain one immutable initial development shell for
the entire automation job, or explicitly replace/rebuild runtime-dependent
tooling when changing shells. Preserve scheduled inputs and changelog intent,
the pinned guard confctl revision, hook enforcement, cache behavior, baseline
and final ancestry checks, and the ordinary final push. Re-signing hooks or
adding Overcommit to Gemfile cannot fix a native-library mismatch.

No full build is needed for this diagnosis. A later implementation should prove
that hook installation, all generated commits, dependency updates and push hooks
use a compatible interpreter and bundle even when stable nixpkgs changes. A
disposable reproduction can expose the masked latest LoadError if necessary;
current runner logs do not include its backtrace. Architect0 owns action-release
validation and reported existing checkout/cache/install-nix major refs current.

No persistent runtime, database, protocol or deployment change has occurred.
No project documentation update is warranted for this investigation-only
package; final workflow rationale can live beside the implementation.

## Evidence retrieval and retention

Used read-only `gh api` for workflow metadata, 30 scheduled run summaries,
`actions/runs/<id>/attempts/1/jobs`, and exact
`actions/runs/<id>/attempts/1/logs`; `git show` inspected existing bare objects.
Raw archives/text are disposable under `/tmp/scheduled-config-<id>-attempt1.*`.
The durable evidence is summarized above with exact attempt links and timestamps.
No credentials were printed or recorded.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-scheduled-workflow-fixes/)
