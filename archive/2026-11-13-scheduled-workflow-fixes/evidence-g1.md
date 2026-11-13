# G1: HaveAPI coupled Nixpkgs/Ruff updater

Owner: implementer1. Implemented the architect-owned G1 brief, including the
lead's clarified runtime format/lint gate. Implementation and quick checks are
complete. Lead accepted independent review of exact `3194488d` and released real
coherent-update acceptance after the C1 amendment was reported for acceptance.
Real acceptance has passed (exit 0), and the clean detached HaveAPI target has
passed normal hook preparation (exit 0). G1 is ready for lead acceptance and
integration coordination. No merge/default push or workflow dispatch was done.

## Final review range

- Repository: `git@github.com:vpsfreecz/haveapi.git`.
- Registered branch: `2026-11-13-scheduled-workflow-fixes`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/haveapi`.
- Base: `b606b4b3c32bf05779c05babeaa1c31a33dee6fa`.
- Final head: `3194488d1ab3403bbb83896bdac8089f1195e645`.
- Complete series: one commit, `3194488d utils: synchronize Ruff with guarded nixpkgs updates`.
- Full diff: five files, 369 insertions, 9 deletions.

| File | Purpose |
| --- | --- |
| `utils/update-nixpkgs.sh` | Guard both owned inputs and index, synchronize Ruff, retain Nix checks, run the selected Python shell's format/lint gate, stage the checked pair |
| `utils/sync-ruff.py` | Small stdlib TOML-aware exact-pin synchronization helper |
| `utils/test_update_nixpkgs.py` | Thirteen focused real-Git / stub-Nix/uv control-flow tests |
| `clients/python/CONTRIBUTING.md` | Contributor explanation of the coupled pin/tool update and runtime checks |
| `doc/agent-instructions/development.md` | Updater prerequisites, clean inputs/index, checks and commit boundary |

No workflows, actions, runtime contracts, performance checks/budgets, library
requirements, tracked `flake.lock`, Python Ruff pin or `uv.lock` changed. No
migrations were created, rewritten, merged, released, deployed or externally
consumed. There are no dependency/pin update streams or obsolete transitional
commits in the final one-commit series.

The initial local `c4c19653aebfc31b05dfa2bb5f30a5158dce992f` was unpublished
when the runtime-gate clarification arrived and was amended into the final
logical change. First published `ada1a73926e72735c478819ef60746e3a2b95d5c`
was refreshed only to wrap one commit-message line; `git diff --exit-code`
proved its source tree identical to final `3194488d`. The exact old-head lease
protected that feature-only force push. No deployed or consumed history exists.

## Implementation contract

The helper reads the newly locked host package set using:

```sh
nix eval --impure --raw --expr \
  '(builtins.getFlake (toString ./.)).inputs.nixpkgs.legacyPackages.${builtins.currentSystem}.ruff.version'
```

Python 3.11+/`tomllib` is checked explicitly before mutation. The helper accepts
one exact `ruff==X.Y.Z` dev requirement and a valid three-part Nix version. It
locates a textual replacement that produces exactly the intended parsed TOML
change, then replaces only the version bytes. It preserves unrelated content,
including comments/line endings and identical text in other groups. The same
version returns without writing. Missing, duplicate, malformed or unlocatable
pins and invalid versions fail before checks/staging/commit.

The updater refuses pre-existing staged/unstaged changes in either owned input
and refuses unrelated staged content. It retains confctl's forward-only update,
the no-input-update fast path and existing `nix flake check`. Before staging it
enters the newly locked `.#client-python` shell, runs `uv sync`, then the exact
shared `run_ruff.py format --check .` and `check .` commands through locked uv.
All commands must succeed. It never reformats source, runs a wider client suite,
tracks the local lock, adds a retry or commits unrelated staged content.

Only after checks does it stage `flake.lock` and
`clients/python/pyproject.toml` together and retain the existing generated
subject convention. The unchanged workflow still performs the final old/new
confctl check before a normal non-force push. No workflow was dispatched.

## Verification before final review

Repository AGENTS and routed development/documentation procedures were read.
The initial worktree add created the checkout but exited on a changed Overcommit
configuration signature. Its physical result was inspected; actual config and
custom hooks were read/signed in the repository shell, then `dev-session`
successfully registered the existing own worktree. No hook bypass was used.

Environment preparation used a fresh Luna/low utility under the monitoring
skill. The first utility's timing wrapper failed before Nix began because
`/usr/bin/time` was absent; no process/effect remained. A fresh utility ran the
direct command successfully with no extra timing dependency:

```sh
nix develop --profile /tmp/2026-11-13-scheduled-workflow-fixes-g1-shell \
  -c bash -c 'set -euo pipefail; ruby --version; python3 --version; bundle check'
```

Exact realized profile: `/nix/store/aa4f7j8zvzjs7hygin4nr0v1nd8b0xsx-haveapi-env`.
Ruby 3.4.11, Python 3.11.17 and the root bundle were available. No kernel build
occurred; all utility-owned tool sessions ended. The installed policy remained
package `/nix/store/0s5dljmmfngj7ia2r9lfkxwydnfiz6b6-dev-workspace-0.2.0`,
catalog `f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d`,
native watcher `dw_e792014d07f1ab00a4e052aeb6fbc575674f9dbc9073f569`,
`gpt-6-luna`/low, full access / approval never.

Checks ran in that realized repository environment:

```sh
sh -n utils/update-nixpkgs.sh
ruff check --config clients/python/pyproject.toml utils/sync-ruff.py utils/test_update_nixpkgs.py
ruff format --check --config clients/python/pyproject.toml utils/sync-ruff.py utils/test_update_nixpkgs.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s utils -p test_update_nixpkgs.py -v
```

All passed; the final thirteen-test run took 9.824 seconds. The tests cover:

- Byte-local changed pin, other identical requirement text, comments and CRLF.
- Same pin leaves content and timestamp unchanged.
- Absent/duplicate/non-exact/extras/malformed Ruff declarations and invalid
  versions fail without rewriting the declaration.
- Changed Nix/Ruff produces a real Git commit containing exactly lock and pin;
  unchanged Ruff commits only the changed lock with the declaration identical.
- No Nix input update skips version evaluation, checks and uv, with no commit.
- Dirty staged/unstaged owned inputs and unrelated staged content reject before
  any Nix invocation; unrelated untracked content is never committed.
- Failed forward-only guard cannot reach synchronization or checks.
- Failed Nix check, uv sync, Ruff format or lint leaves the original HEAD and
  empty staging area. The latter three prove later uv commands are not reached.

The first test attempt mistakenly invoked `sh script`, losing shebang `-eu`;
the harness was corrected to execute the actual script, preserving its flags.
The real production entrypoint was already fail-fast. Authored new Python files
were formatted/linted; no existing client Python source was reformatted.

Actual final commit hooks passed cleanly: HaveapiI18n, TextWidth,
SingleLineSubject and TrailingPeriod. Hook install/config/plugin signing used
the declared root bundle; no skips or disable variables. Both prose files had
the lead's direct writing pass after the facts settled; owner inspected both
returned diffs. `git diff --check` passed. Worktree is clean.

## Baseline input identity

Unchanged baseline Nixpkgs: `3ec636362e1816bc2f0888fa0fa2c69f1bc9e504`;
`flake.lock` blob `3ddc189e9205ae4bb650089f082b554ca832e8dd`.
Baseline Ruff is 0.17.2 at
`/nix/store/h2ma8pnvaak721aady3pmvzybga9kzsf-ruff-0.17.2/bin/ruff`.
Focused fixtures use synthetic `a`-40 to `b`-40 Nix revisions and Ruff
1.2.3 to 1.2.4, proving no current release is hardcoded.

The real post-review receipt below now verifies the design's 0.17.2 to 0.17.4
transition. Focused acceptance exercised the requested actual
`python-ruff-parity` and exact uv/shared-Ruff runtime gate. Full `nix flake check`,
including Prettier parity, remains the updater's unchanged production gate and
was not repeated by this focused batch. No generated commit was needed; real-Git
staging/commit boundaries were already exercised by focused tests.

## Publication, documentation and next dependency

Fresh fetch confirmed origin/master remained the base; no rebase was needed.
SSH feature publication and fresh `git ls-remote` proved final feature
`3194488d1ab3403bbb83896bdac8089f1195e645` and unchanged master
`b606b4b3c32bf05779c05babeaa1c31a33dee6fa`.
Comparison capture records this exact range. Superseded old-head queued CI runs
received cancellation after the message-only force push. Python, RSpec and release
confirmed canceled; old performance run `43444681863` remained queued after its
accepted ordinary cancellation and was confirmed canceled after force-cancel.
Current-head CI was not used as a substitute for the real acceptance now
documented below. No merge/default mutation, PR,
deployment, session lifecycle action or external service message occurred.

Documentation placement: contributor workflow belongs in
`clients/python/CONTRIBUTING.md`; updater prerequisites and safety/failure
behavior belong in existing `doc/agent-instructions/development.md`. No public
article was moved, translated or regenerated. Failure, guard and recovery
contracts remain intact. Recovery of a future generated update reverts its lock
and Ruff pin together; recovery of this repair reverts the single updater commit.
No runtime state, schema or deployment ordering changes are involved.

Raw disposable logs: `/tmp/2026-11-13-scheduled-workflow-fixes-g1-environment-retry.log`,
`...-g1-quick-gate.log`, and `...-g1-commit-final.log`. Lead owns state/package
acceptance and independent review dispatch. Implementer1 retains review-finding
and post-review actual-acceptance ownership. Branch is ready for lead
integration coordination; integration approval and repository claims remain
lead-owned. The member has performed no default-branch mutation.

## Post-review real acceptance (passed)

Exact reviewed source `3194488d1ab3403bbb83896bdac8089f1195e645` was cloned into
`/tmp/2026-11-13-scheduled-workflow-fixes-g1-acceptance.CwBw79/repo`. Its only
remote was removed and initial tree/HEAD cleanliness verified. The feature
worktree and its input pins are untouched.

Fresh policy-matched Luna/low watcher executes:

```sh
nix develop /tmp/2026-11-13-scheduled-workflow-fixes-g1-shell \
  -c bash /tmp/2026-11-13-scheduled-workflow-fixes-g1-acceptance.CwBw79/acceptance.sh
```

The parent-authored driver selects Nixpkgs once through pinned confctl's
forward-only guard, synchronizes Ruff with the real helper, saves old/new
complete locks/declarations and tool identities, builds host
`python-ruff-parity`, then runs the exact runtime uv/shared-Ruff gate. It never
stages, commits, pushes, dispatches or reformats source. Real-Git commit/staging
boundaries already have focused-test coverage; no generated commit is needed
to exercise the requested real checks.

The batch passed, exact exit 0, in about 14 minutes. Guard candidate generation
took 134 seconds; subsequent quiet time was active Git ancestry work, verified
by bounded parent inspection of separate internal logs/process metadata. No
error, retry, guard bypass or kernel build occurred. All operation-owned tool
sessions/cells ended. The exact runtime gate reported `39 files already
formatted` and `All checks passed!`.

| Receipt | Exact identity/result |
| --- | --- |
| Tested repair source | `3194488d1ab3403bbb83896bdac8089f1195e645` |
| Old Nixpkgs | `3ec636362e1816bc2f0888fa0fa2c69f1bc9e504`, NAR `sha256-rZLrzrC6i+jnTAlvPZHogKDulY7WWDEv9hJeHieO7Zw=` |
| New Nixpkgs | `d4f25a3e562008648d45bcf2d70bcc7422cad84e`, NAR `sha256-x9sADJvoVG0L6RejZB+/BB4YiGZFBZrfTlhF4uBq1tQ=` |
| Selected system | `x86_64-linux` |
| Pinned guard source | `github:vpsfreecz/confctl/822c0e35dbe2549111912f539116b4225dfd3035#confctl` |
| Actual guard executable | `/nix/store/nd9w86b14i55h95azazdn1rs7g8z1qgd-confctl/bin/confctl` |
| Ruff pin / native / installed distribution | All 0.17.4, from original 0.17.2 |
| Native Ruff | `/nix/store/ga0q41kp03fjjq06b488jrln4bfjrfd0-ruff-0.17.4/bin/ruff` |
| Ruff derivation | `/nix/store/z6x6j3q1aj2p6k3bbxr06cwngh7k4pv6-ruff-0.17.4.drv` |
| Actual parity check | `/nix/store/wsf84npzyq9rysxvf60b2zdjalzira06-python-ruff-parity.drv` |
| Successful parity output | `/nix/store/4hsrhrqp36waj5pp808jz3yvn96qp2pm-python-ruff-parity` |
| Selected Python shell | `/nix/store/96j7ja1d2qxyc3a79vfpjdip7q3vbniv-haveapi-client-python.drv` |
| Runtime Python | 3.11.18, `/nix/store/p7r9fcn9aac2ipqjx5mcy16k4pr75697-python3-3.11.18/bin/python3.11` |
| Runtime uv | 0.13.7, `/nix/store/9nvvwcmpp4vg28biqg9jhrlnvijwilwj-uv-0.13.7` |

The old/new complete source/input graphs are retained as `old-flake.lock` and
`new-flake.lock` beside the isolated clone. This HaveAPI graph has one root
Nixpkgs input. The immutable guard's complete source graph is `guard-flake.lock`.
Actual Nix input derivation graphs are `parity-derivation.json` and
`python-shell-derivation.json`. The resolved Python dependency graph remains in
the isolated clone's ignored `clients/python/uv.lock`.

| Artifact | SHA-256 |
| --- | --- |
| `old-flake.lock` | `187d63f65b46f5cfa3ac830a5d0c182693cd0ca7ab8e486c3876fcf4b4f6d4f4` |
| `new-flake.lock` | `c0633582c6b11d33202d720397d4f9b2d5b0d0a7933d6af501cbba11e98aedc6` |
| `guard-flake.lock` | `17af06ae76afeba640d695a8e974d76be742e795977d026771c178c523a4eaba` |
| `old-pyproject.toml` | `cd2aa37506449ef190b5d0bcded1f976452d67bf6d68901994f34ab740e740e1` |
| `new-pyproject.toml` | `67654e5a2fd7eedb68b637a2a14d61523ff3718b351efbaeb803310f62e91afc` |
| Ignored Python `uv.lock` | `6c567981b22b57f236cb4a0a2361c15c1d7a662d8b474fa9a12d348257bec661` |

`acceptance.log` and `acceptance.exit` retain the full command result. The final
fixture diff is exactly two owned files (four insertions/four deletions): Ruff's
single dev version and Nixpkgs revision/NAR/timestamp. No other dependency,
Python source or runtime constraint changed. Index is empty; no commit, remote,
push or dispatch exists in the fixture. The feature branch stays unchanged.

## Detached target and final readiness

After acceptance concluded and lead released this preparation, fetched origin
and verified remote master `b606b4b3c32bf05779c05babeaa1c31a33dee6fa` and feature
`3194488d1ab3403bbb83896bdac8089f1195e645`. Created the assigned detached target:

`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/merge-targets/haveapi`.

The initial `git worktree add --detach` populated the correct clean checkout,
then its post-checkout hook refused the unrecorded initial configuration
signature. That partial result was inspected/reconciled, not blindly retried.
Actual configuration/custom hooks were inspected and AGENTS/hooks/flake/Gemfile
verified byte-identical to the trusted reviewed source.

Fresh Luna/low utility then passed the authorized preparation command in about
34 seconds, exit 0:

```sh
nix develop /tmp/2026-11-13-scheduled-workflow-fixes-g1-shell \
  -c bash /tmp/2026-11-13-scheduled-workflow-fixes-g1-target-prep.sh
```

Declared bundle is ready (33 gems), Overcommit installed, configuration/plugin
signatures verified, executable pre-commit and commit-msg hooks present. Target
Ruby is 3.4.11 under the unchanged realized root environment
`/nix/store/aa4f7j8zvzjs7hygin4nr0v1nd8b0xsx-haveapi-env`.
Exact target Ruby executable is
`/nix/store/jnjll1yxfq02bdcw5pjf9gl86wh8gfhq-ruby-3.4.11/bin/ruby`; `GEM_HOME`
is the assigned target's `.gems` directory. The prepared root `Gemfile.lock`
retains the complete resolved hook-tool dependency graph locally in that target.
Its SHA-256 is `2c3e4a148d44216c88dc024c417c4abd74b6776b6246bea0ccaa933610d0d0b3`.
Preparation logs and authoritative exit are
`/tmp/2026-11-13-scheduled-workflow-fixes-g1-target-prep.log` and `.exit`. The
utility initially omitted disk artifacts; it subsequently preserved the already
captured native output with provenance and exit 0, without rerunning setup.
All operation-owned sessions/cells ended.

At preparation handoff, target HEAD was detached at `b606b4b3` and tracked/index
status was clean.
Normal hook paths are
`/home/aither/workspace/ai/vpsfree.cz/repos/haveapi.git/hooks/pre-commit` and
`.../hooks/commit-msg`. Feature worktree is clean at exact reviewed `3194488d`.
Fresh `git ls-remote` at handoff proved unchanged master/feature heads. Target was an
ancestor of the reviewed feature head, so the full reviewed one-commit series
remains eligible for fast-forward integration; no rebase or new source occurred.
Review, quick checks and actual focused acceptance all apply to that exact head.

No repository claim, merge, default push, configuration deployment, workflow
dispatch or session lifecycle action was performed by this member. Lead owns
the required fresh target check under any later approved integration claim.
G1 is delivered for acceptance/capacity; C2 source work remains parked until
lead allocation.

A later read-only metadata check after delivery observed target HEAD at reviewed
`3194488d`, with a clean status. This member performed no merge, reset or push;
subsequent target use/integration receipts belong to the lead. The preparation
receipt above preserves its actual pre-integration base and fresh remote proof.

Lead subsequently confirmed approved integration of exact `3194488d` into remote
master with normal hooks and remote proof, and repository claim release at
15:28:44 UTC. Lead owns actual workflow run `43453002644` and its monitoring.
This member performs no further target operations or duplicate run monitoring.
