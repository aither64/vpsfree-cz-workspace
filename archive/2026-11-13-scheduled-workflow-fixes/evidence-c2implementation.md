# C2a/C2b: full commit-message transport and org consumer pin

Historical C2 execution receipt. Merged provider4c remains preserved beneath
later additive provider ff. The unmerged org687 tool-pin commit was consolidated
into org69 and integrated during C3; C4 now supersedes the workflow-specific
tool-pin approach with sole flake.lock authority. See
[C3](evidence-c3.md) and [C4-org](evidence-c4-implementer1.md) for those successor
boundaries; older exact execution/package evidence below is retained unchanged.

Owner: implementer1. Implemented the sufficient architect-owned C2 brief after
G1 delivery/capacity acceptance. Intended changes are committed and published
for independent final review. Lead accepted the exact confctl/org ranges in all
four review lanes with no findings and released post-review acceptance. No
full-suite/packaged acceptance was started before that review. The first batch
built the exact immutable package, then stopped at a receipt-only metadata
operand error before tests. That error was diagnosed/corrected without source
changes; a fresh utility reused the built package and passed the full suite and
packaged caller proof. Both detached targets then passed normal hook preparation
and were handed back to the lead. Diagnosis is retained in
[evidence-c2.md](evidence-c2.md).

Lead subsequently reported explicit user approval and successful exact-head
integration of confctl `4c636b40` into remote master. Org pin `6874f605` remains
unmerged and undispatched pending the separate C3 changelog-selection provider.

## Exact full review ranges

| Repository | Base | Final head | Complete series / diff |
| --- | --- | --- | --- |
| confctl | `822c0e35dbe2549111912f539116b4225dfd3035` | `4c636b40b53b143fda6d9cad9332ce8b7b86bdb8` | One commit, `inputs: write commit messages through a temporary file`; two files, 163 insertions / 7 deletions |
| vpsadminos-org-configuration | `8306d29d09f1939d1f92d44b5a5e241429b40c2e` | `6874f60516abbf7e96d8fc247036d0aa61d11cd1` | One additive commit, `ci: use file-backed confctl commit messages`; one file, one insertion / one deletion |

Both branches are `2026-11-13-scheduled-workflow-fixes` in their respective
canonical SSH repositories. Worktrees remain under
`worktrees/2026-11-13-scheduled-workflow-fixes/{confctl,vpsadminos-org-configuration}`.
No obsolete/transitional commits, migrations or generated data remain in either
review series. Confctl has no dependency-pin stream. Org has one final immutable
tool-pin update, `822c0e35` to `4c636b40`; no superseded intermediate pin commits.

Merged and hosted-consumed C1 `8306d29` remains an ancestor and was never amended
or rewritten. C2b is a new commit over that exact remote default. The prior C1
history is retained because it is already integrated and consumed, rather than
being consolidated with this new causal repair. No schema/state migration was
created, rewritten, released, deployed or externally consumed.

## Changed source and invariants

C2a changes only `lib/confctl/inputs/git_commit.rb` and new
`spec/inputs/git_commit_spec.rb` (148 lines):

- Explicitly require standard-library `tempfile` in the owning source.
- Create one private block-scoped temporary file, write the complete message and
  flush before invoking Git; pass its absolute path with `-F`.
- Keep the file until synchronous Git/editor/hooks finish, with automatic cleanup
  on success, false/nil process results and exceptions.
- Preserve `git commit` argument order, conditional `-e` only for requested
  editor plus TTY, exact file arguments, conf-dir cwd, inherited environment and
  streams, normal hooks, existing generic failure and raised exceptions.

No staging, message generation, truncation, changelog policy, CLI option,
framework, dependency, Nix input, release/version or other consumer changed.

C2b changes only the existing workflow `CONFCTL_FLAKE` to
`github:vpsfreecz/confctl/4c636b40b53b143fda6d9cad9332ce8b7b86bdb8#confctl`.
The original hooks, cron/manual trigger, actions, auth, channels, final ancestry
guard and normal push remain byte-identical. Configuration `flake.lock` was not
updated. No default push, merge, workflow dispatch, repository claim, production
build/deployment or session lifecycle action was performed by this member.

Compatibility: internal message transport only. Full generated contents retain
Git's existing cleanup behavior; old/new readers can read the resulting commits.
Recovery is an additive source revert and an org workflow-pin revert. Old code
still has the argument-size limitation; no persistent conversion/rollback or
coordinated machine update is needed.

Documentation: existing `README.md`/`docs/flake-inputs.md` describe complete
changelogs and existing flags; those contracts remain accurate. A nearby source
comment explains the process-argument limit. Additional user-facing prose was
unnecessary for this internal transport repair, so no documentation article or
writing window was added. Detailed diagnosis and validation live in session
evidence; no deployment/run receipt was added to a project repository.

## Setup and quick checks

Verified session/environment identity and live saved roster. Read confctl's
current AGENTS, declared shell/hooks/style, existing helper/specs and relevant
input-update docs; current remote base was checked rather than stale bare HEAD.
The new worktree was physically created, then post-checkout rejected changed
hook configuration before registration. Inspected/signed declared config/hooks
in the repository shell and registered the existing own worktree successfully;
no bypass or blind checkout retry. Portal's warning about the existing
`merge-targets` container directory did not affect this registration.

Uncertain environment bootstrap used a fresh policy-matched Luna/low utility;
exit 0 in 96 seconds, no running effects or kernel build. Exact command:

```sh
nix develop --profile /tmp/2026-11-13-scheduled-workflow-fixes-c2-shell \
  -c bash -c 'set -euo pipefail; ruby --version; bundle check'
```

Realized profile `/nix/store/vha0zqm64yp7pijfx4jf7b82dzk3lkpi-nix-shell-env`,
Ruby 3.4.9 at `/nix/store/pnyd647xzsszp5r6vicpsl7q9fsz5xyk-ruby-3.4.9/bin/ruby`,
declared Bundler 2.5.7. Baseline RubyGems constant-redefinition warnings were
recorded; they did not fail commands or justify dependency changes.

| Quick check | Result |
| --- | --- |
| `ruby -c` on both changed Ruby files | Passed |
| `bundle exec rspec spec/inputs/git_commit_spec.rb spec/inputs/commit_message_spec.rb spec/inputs/guarded_update_spec.rb` | 37 examples, 0 failures; 4.32 seconds |
| Final changed `git_commit_spec.rb` after one interpolation-style correction | 9 examples, 0 failures |
| Targeted RuboCop on both changed Ruby files | 2 files, no offenses |
| `nixfmt --check` on all 50 tracked Nix files | Passed; no formatting writes |
| Actual confctl commit hooks | Nixfmt, RuboCop and all commit-msg hooks passed cleanly |
| Org YAML / all five extracted `bash -n` bodies | Passed |
| Org inverse-pin byte and YAML comparison to merged base | Passed; exactly one pin replacement |
| Actual org commit hooks | Nixfmt and all commit-msg hooks passed cleanly |
| Full-range `git diff --check` | Passed in both repositories |

The real-Git regression commits a **1,260,024-byte** message, reads the complete
raw commit body back unchanged, and proves an actual hook can read the still-live
message file. Only supplied `flake.lock` enters the commit; unrelated staged
content stays staged. A rejecting actual hook leaves HEAD unchanged and propagates
the existing failure. All four editor/TTY combinations preserve exact argument
ordering/file arguments without opening an editor. Separate false, nil and
raised-launch cases verify cleanup; cwd restoration, absolute path, private mode
and flushed complete contents are checked. The old-source E2BIG reproduction
remains in C2 diagnosis, so no obsolete implementation was reapplied to get red.

Raw disposable logs:
`/tmp/2026-11-13-scheduled-workflow-fixes-c2-environment.log` and `.exit`,
`...-c2-quick.log`, `...-c2-quick-final.log`,
`...-c2-confctl-commit.log`, `...-c2-org-commit.log`.
Org validation script is `...-c2-org-check.rb`. Both commits used temporary
message files and normal hooks; no hook-disable variables/skips.

## Source/input identities and publication

Confctl's tracked lock inputs are unchanged:

| Input | Git blob / SHA-256 |
| --- | --- |
| `flake.lock` | `44c1c33362f46199cce1965ea45ad20de861bc23` / `17af06ae76afeba640d695a8e974d76be742e795977d026771c178c523a4eaba` |
| `Gemfile.lock` | `1ee9743de27648c30a9eefa2b47029bb10ffc875` / `c3b51191315f5aa46da39fbd19a7238db3772e52223122b6cbd066878d59391e` |

Fresh fetches confirmed the named bases before commits/publication; no rebase or
force push was needed. SSH feature publication, fresh `git ls-remote` and
comparison capture preserve the exact ranges above. Both worktrees are clean.
No superseded branch runs were created by rewriting history.

Automatic confctl push CI at exact `4c636b40`: RSpec run `43455046709` and
RuboCop run `43455046559` were already successful; Tests run `43455046662` was
in progress at inspection. This is recorded automatic feedback, not a manually
started pre-review long acceptance. Org branch has no automatic push workflow;
no updater was dispatched.

## Review and acceptance dependencies

Lead accepted independent final review of both exact complete ranges in all four
lanes with no findings, including whole-history/no-migration and the org one-pin
lane. This member did not invoke review. The released post-review full repository
checks and packaged caller/oversized proof have now passed, as recorded below.

Existing packaged caller scaffold is
`spec/confctl/cli/package_environment_spec.rb`, enabled with `CONFCTL_BIN` set
to the built immutable package; the flake's `checks.<system>.rspec` also selects
the packaged CLI. Acceptance reused that scaffold and exact caller-hook
environment through a disposable adaptation rather than adding a framework or
unrelated source. No production system build was required.

Confctl/master required separate explicit user approval; the original six-repo
approval alone did not cover it. Lead has now reported that approval and the
exact integration below. The org pin and its final integrated-master dispatch
remain held for C3. Lead owns later acceptance of os-staging's full commit plus
final guard/push. Do not rerun the unfixed old event SHA. Member retains both
package review findings and subsequent proof/hosted-failure diagnosis ownership.

## Post-review terminal acceptance

Fixed reviewed source remained `4c636b40b53b143fda6d9cad9332ce8b7b86bdb8`;
org remained `6874f60516abbf7e96d8fc247036d0aa61d11cd1`. No code, lock, pin,
release or history change occurred after review. Fresh Luna/low utilities used
the same validated installed policy already recorded above.

Artifact root: `/tmp/2026-11-13-scheduled-workflow-fixes-c2-postreview.7KYwYt`.
The initial operation built the exact immutable GitHub feature package, then
exited 1 because the receipt command supplied `#confctl` to `nix flake metadata`,
which accepts a flake reference without an output fragment. No test had run.
The operand was corrected; immutable metadata was verified and the existing
successful package build reused. Original `acceptance.log`/`acceptance.exit`
retain this driver-only failure. No source diagnosis/repair or build repetition
was needed.

The remaining batch passed exit 0 in about 79 seconds. Source checks were not
repeated merely to recover reporting: this was the first full-suite/package
execution after the metadata fix.

| Released check | Terminal result |
| --- | --- |
| Full `bundle exec rspec`, actual `CONFCTL_BIN` enabled | 212 examples, 0 failures |
| Full `bundle exec rubocop` | 110 files, no offenses |
| Disposable adaptation of existing packaged caller scaffold | 1 example, 0 failures |
| Source/index after the batch | Clean, exact reviewed head |

The packaged scenario committed a **1,260,021-byte** message and compared its
complete raw Git body. Its real caller Ruby/Bundler hook opened the still-live
private `confctl-commit-*` file and copied the complete body. The selected path
alone was committed and unrelated staged content was preserved. After success,
no message tempfile remained. The same scenario then made the actual caller
hook reject another update: CLI failure propagated, HEAD/index selection stayed
unchanged, and the temporary file was removed. No guard/input update or source
reformat was involved. Editor/TTY and false/nil/raised-launch cases retain the
passing exact-source focused evidence above and were also included by the full
repository suite.

The scenario is a 35-insertion/6-deletion disposable adaptation of
`spec/confctl/cli/package_environment_spec.rb`. Only the adapted oversized
scenario ran; the unchanged startup/caller scenarios already ran in the full
suite. It retains the original local `confctl-caller-fixture` 1.0.0 Gemfile,
preload and caller Ruby assertions. Source repository files were never altered.
`make-packaged-proof.rb`, generated `packaged_oversized_spec.rb`, fixture
preflight, `full-rspec.log`, `full-rubocop.log`, `packaged-proof.log` and
`acceptance-resume.log`/`acceptance-resume.exit` preserve commands/results.
All utility-owned sessions/cells ended. Native fallback reports were used;
an attempted runtime report correctly refused an unregistered monitor and did
not alter the completed result. Terminal results were reported promptly to lead
before extended receipt formatting.

## Exact package and complete source/input graph

| Identity | Value |
| --- | --- |
| Immutable build reference | `github:vpsfreecz/confctl/4c636b40b53b143fda6d9cad9332ce8b7b86bdb8#confctl` |
| Package output | `/nix/store/lqbs50p95i66y4s1qaa0i7kjavfs0x2l-confctl` |
| Package derivation | `/nix/store/i3i90kjj0qhrn0aqc3m9nbyxmx5xyn0r-confctl.drv` |
| Package NAR | `sha256-GoTbPicwTBqBaD4vUjHtVIbVd6ujNm3+GQKQEvjsdmY=`; 1,248 bytes |
| Exact source store | `/nix/store/msjbjb2cradhq1f7awk750yvgxzgqwh1-source` |
| Source revision / NAR | `4c636b40b53b143fda6d9cad9332ce8b7b86bdb8` / `sha256-cJNO9Sm7xbJqnTn+vFVbpT/vQVV2eU75cjSZ0nri4u0=` |
| Packaged dependency environment | `/nix/store/jx5mrkmb54lhgx1pla635q7072xq5s68-confctl-deps/lib/ruby/gems/3.4.0` |
| Package and asserted caller Ruby | `/nix/store/pnyd647xzsszp5r6vicpsl7q9fsz5xyk-ruby-3.4.9/bin/ruby` |
| Package shell | `/nix/store/1sr8rmx4v0v994lkbzhwc1f0qr1gxxs9-bash-5.3p9` |
| Package Git | `/nix/store/j7fnzcrbbxc1r2b3b9fhqkha6hqb0jh1-git-2.54.0` |
| Package OpenSSH | `/nix/store/4lh63ihbvf9jl83pgykm70avydcrxw58-openssh-10.4p1` |
| Package Nix | `/nix/store/azi9n31ia037jml4ibi4nfwz1v4hmrj6-nix-2.34.8` |

The wrapper retains its `--disable=rubyopt` startup behavior and caller
environment for Git hooks; the actual caller proof passed with the caller's
Ruby, local bundle and preload. The verification shell reported Bundler 2.5.7,
Nix 2.34.9 and Git 2.54.0. A retained indirect root `accepted-package` beside the
artifacts keeps the already-built output available; creating it did not rebuild.

The complete pinned GitHub input nodes from actual immutable metadata are:

| Node / repository | Revision | NAR hash |
| --- | --- | --- |
| home-manager / nix-community/home-manager | `c47b2cc64a629f8e075de52e4742de688f930dc6` | `sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg=` |
| impermanence / nix-community/impermanence | `7b1d382faf603b6d264f58627330f9faa5cba149` | `sha256-03+JxvzmfwRu+5JafM0DLbxgHttOQZkUtDWBmeUkN8Y=` |
| netlinkrb / vpsfreecz/netlinkrb (raw) | `d9de53d843d2586ffa5b7b404887fa801c697ddf` | `sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg=` |
| nixpkgs / nixos/nixpkgs | `e4bae1bd10c9c57b2cf517953ab70060a828ee6f` | `sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc=` |
| nixpkgsUnstable / NixOS/nixpkgs | `f13ff45afd1bb73e640eaa08a7066dbed07e3238` | `sha256-zDSUbpoeo/9ZmD2+wXnzxoo1+uhL8vxc0b8yuYMKYq0=` |
| nixpkgs_2 / NixOS/nixpkgs | `8b8c811c7c2541c30382c5de7ed26be055569c60` | `sha256-CiOTEjmwAmG2AWnaIno9YaCJJmpca2FXPhMAsnrolCg=` |
| ruby-lxc / vpsfreecz/ruby-lxc (raw) | `004bf35eb90d41ba60b347b5b1e73d868a4f95d9` | `sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE=` |
| vpsadminos / vpsfreecz/vpsadminos | `67fcc17372d175b036706a1459a8b471bfc225e0` | `sha256-HOL3ACMUyRFhA4Cd2zk5qhnUf0zaEifHsQv86hwHgSc=` |

All graph edges/follows are retained here (`raw` nodes have `flake = false`):

```text
root: nixpkgs follows [vpsadminos,nixpkgs]; vpsadminos -> vpsadminos
vpsadminos: impermanence -> impermanence; netlinkrb -> netlinkrb;
  nixpkgs -> nixpkgs_2; nixpkgsUnstable -> nixpkgsUnstable; ruby-lxc -> ruby-lxc
impermanence: home-manager -> home-manager; nixpkgs -> nixpkgs
home-manager: nixpkgs follows [vpsadminos,impermanence,nixpkgs]
```

`flake-metadata.json`, `package-derivation.json` and `package-info.json` preserve
the full native graph/receipt. SHA-256 fingerprints: metadata
`9b9eaaf435ae27b9b58f1822c22c230fdf2ca8f49c67f6ed1e3c5235425564e0`,
derivation `0412c0e9bba09d7d2aed92f11dc26c771e4017f240fb09fa8aa1014282a277a0`,
adapted proof `a49da8ddb3d97f5471e8cc1fdf3563f415ea404bbdb80391a05268f08824b028`.

## Detached target handoff (passed)

Preparation began only after acceptance passed and the lead released its
existing org target window. Fresh remote defaults matched expected bases;
feature heads remained exactly reviewed. New confctl target creation populated
the correct detached checkout, then post-checkout refused its initial untrusted
configuration. This physical result was inspected/reconciled; no blind checkout
retry or hook bypass occurred.

Both targets passed sequential normal bundle/hook install/signature checks,
exit 0 in about 9 seconds. Confctl reused only the `.gems/ruby` child alias to
its same-session feature cache after exact unchanged Gem/flake/hook input proof;
its private `.bin` remained independent. Existing org aliases were preserved.
No tracked file, index, reviewed head or pin was changed.

| Target under `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/merge-targets/` | Prepared detached base | Environment |
| --- | --- | --- |
| confctl | `822c0e35dbe2549111912f539116b4225dfd3035` | `/tmp/2026-11-13-scheduled-workflow-fixes-c2-shell` -> `/nix/store/vha0zqm64yp7pijfx4jf7b82dzk3lkpi-nix-shell-env`; Ruby 3.4.9 |
| vpsadminos-org-configuration | `8306d29d09f1939d1f92d44b5a5e241429b40c2e` | `/tmp/2026-11-13-scheduled-workflow-fixes-c1-shell` -> `/nix/store/hzcy03kfm6qbyir2zjzp037zwn02k9vz-nix-shell-env`; Ruby `/nix/store/y1jhbdp5hazr8ayacvkjzxwhfcajbzsr-ruby-3.3.10/bin/ruby` |

`GEM_HOME` is each target's `.gems/ruby/<ABI>`. Its `.gems/ruby` alias resolves
to the corresponding same-session feature's `.gems/ruby`; these are the complete
existing locked tool inputs, not another session's cache. Executable normal
hooks live in the corresponding canonical bare repository's
`hooks/pre-commit` and `hooks/commit-msg`. `target-prep.log`/`target-prep.exit`
retain actual paths and proof; all utility sessions/cells ended.

At handoff, both targets were detached/clean, each was an ancestor of its
reviewed feature, and post-preparation `git ls-remote` proved confctl
master `822c0e35` / feature `4c636b40`, org master `8306d29` / feature `6874f605`.
No source rebase was needed. Readiness was reported before this extended
formatting; target ownership was returned to lead and no later member target
operation occurred. Future lead integration must keep its own fresh target,
claim, hook, push and remote-proof requirements. At that handoff, separate
confctl/master approval and lead-owned integration/final org dispatch remained
external dependencies; the subsequent milestone below records the confctl
approval/integration. This member has made no default mutation.

## Lead-reported C2a integration milestone

Lead reported that the user explicitly approved confctl/master at exact
`4c636b40b53b143fda6d9cad9332ce8b7b86bdb8`. Lead fast-forward merged from the
prepared target, ran normal hooks, pushed and verified that exact remote head.
Repository claim `40b5a756-735a-4b2b-8d21-268b001de1ef` was held from 17:13:39
to 17:14:35 UTC, then released and verified with no unfinished effects. Existing
RubyGems constant warnings were baseline noise; hooks and commands exited 0.
These are the lead's authoritative operation/remote-proof reports, not a
duplicate target inspection by this member. Prepared-base snapshots above remain
historical receipts and were not rewritten.

C2a's merged history is preserved. C2b org `6874f605` is explicitly **not merged
or dispatched**: lead is awaiting the new C3 policy provider. Accepted C3 design
preserves the full guard, callback/result changes and summaries; only explicitly
selected inputs produce Git logs and `--no-changelog` produces none. Exact
implementation files/edge cases remain architect-owned until a sufficient brief
and lead allocation. Implementer1 has confirmed capacity but has started no C3
edit or duplicate investigation and will not touch the confctl target without a
new released window.
