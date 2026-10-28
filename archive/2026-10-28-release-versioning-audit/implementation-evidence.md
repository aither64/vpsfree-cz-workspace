# HaveAPI implementation evidence

Owner: implementer0. Lead owns plan/state and final review coordination.

Current result: the exact reviewed final head is integrated into remote master;
local, feature-event and new master-event checks passed. No implementer work
remains. Lead owns final state and handoff; all worktrees and refs are retained.

## Source and scope

- Identity: `dev-session current`, both environment variables and thread binding
  agree on this session and `/home/aither/workspace/ai/vpsfree.cz`.
- Initial tracking: workspace commit
  `abdc82d25f893f39d53b9e093a511cc58ad3707a` precedes project commits.
- Fresh fetched base: `2f5156262baaf137800c17a9321e617c2b5df1d5`.
- Canonical worktree: `worktrees/2026-10-28-release-versioning-audit/haveapi`.
- Branch: `2026-10-28-release-versioning-audit`, remote SSH
  `git@github.com:vpsfreecz/haveapi.git`, target `master`.
- No schema, data, protocol, API or configuration migrations. No publication,
  tags, default-branch integration or deployment performed or authorized here.

The existing `make version VERSION=0.31.0` flow updates the 17 maintained
identity/constraint paths. Changelog additions are copied from published
`v0.31.2`, retaining all existing master entries. Elixir and protocol identities
are unchanged. The fixture adaptation originates from released commit
`c9124da141adc258fbbaf67d4ec19ee3f8580849`; master's optional Rust version setup
is retained before ordinary worker receipts, then the released maintenance
overrides apply. There are no other runtime changes.

The guard fetches only `refs/heads/master` into `refs/remotes/origin/master`
before reading its VERSION. It preserves tag/source/latest-branch checks and
compares integer major/minor tuples with patch zero on master. Local master is
detected in ordinary checkouts; `--master` supplies detached CI context. The
existing release workflow now includes VERSION in push/PR paths and passes that
context on actual master refs. Existing tagged recovery uses original tooling
and artifacts. Durable policy and commands are in
`haveapi/doc/agent-instructions/releases.md`.

## Preparation and checks

- Read workspace and repository procedures and accepted architect brief.
- Worktree checkout initially returned failure from Overcommit's unsigned
  configuration, while checkout itself completed. Inspected configuration and
  both custom hooks, installed Overcommit and signed it in the top-level Nix
  environment, then reran `dev-session worktree add` successfully. Registration
  records the exact initial base. No hooks were bypassed.
- Dependency preparation: `nix develop -c make release-deps`, passed in 166s,
  delegated to fresh pinned Luna/low watcher. Full log: `dependencies.log`.
- Metadata update: `HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c make version
  VERSION=0.31.0`, passed. Ignored npm/uv and Rust/TypeScript locks updated by
  the existing workflow; no tracked lock/input/action update.
- Initial release checks: metadata and prepared-input checks passed, 24 focused
  release-policy examples passed; RuboCop style findings corrected. Subsequent
  run clean: `release-quick.log`.
- Workflow YAML parsed successfully; both push and pull_request filters include
  VERSION, so a VERSION-only change selects release validation.
- Official upstream action tags verified before workflow edit: checkout v7.0.1,
  install-nix-action v31.11.3, download-artifact v8.0.2, upload-artifact v7.0.2,
  configure-rubygems-credentials v2.1.0 and gh-action-pypi-publish v1.14.3 match
  existing pinned commits. No action refs changed.
- Initial focused lineage check: 18 examples, one NameError for optional
  `HaveAPI::RustClient` before ordinary worker inputs. Original master setup
  restored at that point; full initial evidence: `lineage-quick.log`.
- Final focused metadata/release-policy, lint and lineage batch passed in 42s
  under a fresh Luna/low watcher: 65 metadata/release-policy examples and 18
  lineage examples, zero failures; four Ruby files lint clean; metadata and
  prepared-input checks valid at 0.31.0. Full output: `final-quick.log`.
- All final commits passed declared Overcommit hooks. Logs:
  `fixture-amend.log`, `version-commit.log`, `policy-commit.log`. The original
  fixture message produced 72-column warnings; it was rewrapped and amended
  before the final series. The final message hooks pass without warnings.
  The explicit metadata staging command warned about the ignored dist parent;
  inspection confirmed the tracked bundle version update is included in the
  metadata commit and no intended metadata path remained unstaged.
- Committed checks passed: source-only `check-clean`, `check-clean --master`
  and `make release-check` in the top-level Nix shell. Full output:
  `committed-check.log`. Tracked checkout is clean.

## Final committed review range

Base: `2f5156262baaf137800c17a9321e617c2b5df1d5`.
Head: `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`.

1. `29fae9e00bdc0f340196cda953c5c7b2408aec21`
   `servers/ruby: isolate maintenance lineage test versions`
2. `ae909bef9ee27d01d5497f4b511e27b72f6dd60e`
   `version: synchronize master to 0.31.0`
3. `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`
   `release: enforce master version policy`

Complete final diff: 24 files, 375 insertions, 51 deletions. One version-update
stream and one final logical guard implementation; no superseded follow-up
commits or dependency/action/pin updates remain. No migrations exist in the
series or final diff. No new migration or compatibility path was consumed,
deployed or released. The fixture's previously released provenance is retained
in its commit body; this port does not make the original release commit a
literal ancestor of master.

Fresh post-commit SSH fetch and `ls-remote` confirmed remote master remains the
exact base above. `haveapi-0.31` and peeled `v0.31.2` remain
`819bba5110e089465535ecd71ca2eb37a7d39caa`; tag object remains
`815c033be8cfca22822d0b2f80c022e959c5d0c4`. `git diff --check` passes for the
complete range. `dev-session worktree capture-comparison` saved this exact
base/head pair. No rebase was needed.

## Post-review verification and feature publication

Final independent review passed all four lanes without findings on the exact
base/head range above. `review.md` records the retained reviewer's complete
history, consolidation and no-migrations conclusions. Lead authorized the
bounded `make release-test` plus `make test-performance` batch, feature-branch
SSH publication after success and exact-head CI monitoring. No local duplicate
full package build or full `make test` is planned: build-only release CI already
runs those commands and packaging smokes.

The fresh pinned Luna/low utility `post_review_local_checks` completed the local
batch successfully at the exact reviewed head: 143 seconds,
2026-10-28 11:05:34–11:07:57 UTC. Full `make release-test` passed 236 Ruby examples
and six Python tests; `make test-performance` passed 172 deterministic examples.
Full output and milestone timestamps: `post-review-local.log`. The only checkout
effect was an untracked `python_artifacts.cpython-311.pyc`; inspected and removed
that owned generated bytecode. No source changes or review rerun were needed.

A fresh SSH fetch confirmed master still equals the reviewed base; no rebase
was required. The exact comparison was captured again. Feature-only SSH push
with installed hooks succeeded, and `git ls-remote` independently confirmed:

- `refs/heads/2026-10-28-release-versioning-audit`:
  `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`
- `refs/heads/master`: `2f5156262baaf137800c17a9321e617c2b5df1d5`

Push output: `feature-push.log`. No PR, tags, default-branch write, package
publication or deployment was performed.

Eleven push workflows started for this exact feature head at
2026-10-28 11:08:58 UTC. Fresh pinned Luna/low utility `feature_ci_monitor` owns
their monitoring. Full observations/status: `ci-monitor.log`, `ci-status.json`.
All eleven workflows completed successfully on the exact reviewed/published
head. The CI window was 2026-10-28 11:08:58–11:17:23 UTC (8m25s). Release ran
build-only, including the full package build/test and smoke checks; publication
was skipped. No failures, retries, cancellations or unexpected kernel builds
occurred, and no workflow remains running.

| Workflow | Exact-head run | Conclusion |
| --- | --- | --- |
| RuboCop | [40677688087](https://github.com/vpsfreecz/haveapi/actions/runs/40677688087) | success |
| clients/go RSpec | [40677687770](https://github.com/vpsfreecz/haveapi/actions/runs/40677687770) | success |
| clients/js tests | [40677688172](https://github.com/vpsfreecz/haveapi/actions/runs/40677688172) | success |
| clients/php PHPUnit | [40677687921](https://github.com/vpsfreecz/haveapi/actions/runs/40677687921) | success |
| clients/python | [40677687902](https://github.com/vpsfreecz/haveapi/actions/runs/40677687902) | success |
| clients/ruby RSpec | [40677687980](https://github.com/vpsfreecz/haveapi/actions/runs/40677687980) | success |
| clients/rust | [40677687905](https://github.com/vpsfreecz/haveapi/actions/runs/40677687905) | success |
| i18n health | [40677688257](https://github.com/vpsfreecz/haveapi/actions/runs/40677688257) | success |
| release | [40677687767](https://github.com/vpsfreecz/haveapi/actions/runs/40677687767) | success |
| servers/ruby RSpec | [40677687828](https://github.com/vpsfreecz/haveapi/actions/runs/40677687828) | success |
| servers/ruby performance | [40677687909](https://github.com/vpsfreecz/haveapi/actions/runs/40677687909) | success |

Performance was a measured quick-profile pass against baseline
`2f5156262baaf137800c17a9321e617c2b5df1d5`, candidate
`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`: 14/14 cases, 28 timing
classifications and 14 allocation classifications passed. It was neither
inconclusive nor a no-work selection. Report and immutable event/source
selection are retained at `ci-artifacts-40677687909/results/report.json` and
`ci-artifacts-40677687909/selection.json`; the workflow retains its full evidence
artifact as `performance-40677687909-1`.

Final read-only SSH remote proof after CI again confirms the feature head above
and unchanged master `2f5156262baaf137800c17a9321e617c2b5df1d5`. Local tracked
and untracked status is clean. All checks/review apply to the same final head;
no rebase, equivalence substitution or source follow-up occurred.

Implementation, local checks, independent review and exact-head CI are complete.
The feature branch is ready, awaiting merge approval. Default-branch integration
needs separate user direction. No package release, tags or deployment occurred.


## Approved integration preparation

Lead relayed the user's explicit HaveAPI/master approval, “all right, merge it”.
Implementer preparation occurred outside claims; lead owns acquisition, the
short merge/push critical section and explicit release.

Reverified session identity and read current workspace Git, coordination and
commit procedures, repository instructions and the full selected
`workspace-host coordination guide`. Selected package:
`/nix/store/pjmi2cz75r9cwynh4lin706jdzlp4xb9-dev-workspace-0.2.0`;
coordination catalog SHA-256:
`9936fc4d7605c6a2790167473cfa75a688682b77d57d5cd48b59b7ad2947783e`.

Fresh fetch still proves target master is the reviewed base
`2f5156262baaf137800c17a9321e617c2b5df1d5` and local/remote feature is the exact
reviewed `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`. Full final series remains
the same three reviewed commits above, 24 files +375/-51, no migrations or
obsolete update streams. No rebase or content substitution was needed.
Full-index binary final diff SHA-256:
`426ab56641ee6c91a1cc596a5d46f318eeaff081b6a2d0bb6f64d8ec85c96cf3`;
feature tree: `123020cb5dfe6490a1335c0f3ff041b93bcc9550`.

New clean session-owned detached target:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-release-versioning-audit/haveapi-merge-target`.
Its HEAD remains the exact base above. No existing worktree or ref was removed
or switched. Its ignored `.gems` points to this session's prepared feature
tooling gems, and its ignored root `Gemfile.lock` is copied byte-for-byte from
the prepared source. Nix shell evaluated successfully; `bundle check` passes.
Overcommit installed and signatures trusted. Normal post-merge and pre-push
entrypoints ran successfully with no work (no PostMerge/PrePush checks are
configured); required pre-commit and message hooks remain installed and enabled.
Both tracked and untracked target status are clean.

After the lead's fresh exact-head/remote-target/cleanliness checks under its
repository claim, the prepared commands from that target directory are:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c git merge --ff-only f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c git push origin HEAD:refs/heads/master
git ls-remote origin refs/heads/master
```

These commands were prepared, not executed by implementer0. The lead subsequently
performed the approved fast-forward and normal SSH push, verified remote master
and retained feature at the exact final head and explicitly released claim
`897accbe-acc0-4d47-91a8-5f5682d2482c`. Independent claim status confirmed
released, revision 2, at 11:32:05 UTC. `integration.md` records the critical
section. No claim was acquired during implementer preparation; post-merge CI
observation is outside ownership. No machine reservation exists.

## New master-push CI

Fresh CI inventory selects branch `master`, event `push`, exact head
`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`, creation 2026-10-28 11:31:52 UTC.
These are eleven new master-event runs; the earlier feature runs with the same
head are retained separately. Fresh pinned Luna/low utility
`master_push_ci_monitor` owns all new IDs, including release `40680667625` and
performance `40680667726`. Outputs: `master-ci-status.json`,
`master-ci-monitor.log`, `master-release-workflow.log` and performance artifact
under `master-ci-artifacts-40680667726`. Prior feature/local checks remain valid;
no extra local tests or source changes were needed.

All eleven new master-push workflows concluded success in 7m53s, from
2026-10-28 11:31:52 to 11:39:45 UTC, at the exact final head above:

| Workflow | Master-push run | Conclusion |
| --- | --- | --- |
| RuboCop | [40680667692](https://github.com/vpsfreecz/haveapi/actions/runs/40680667692) | success |
| clients/go RSpec | [40680667904](https://github.com/vpsfreecz/haveapi/actions/runs/40680667904) | success |
| clients/js tests | [40680667669](https://github.com/vpsfreecz/haveapi/actions/runs/40680667669) | success |
| clients/php PHPUnit | [40680667675](https://github.com/vpsfreecz/haveapi/actions/runs/40680667675) | success |
| clients/python | [40680667823](https://github.com/vpsfreecz/haveapi/actions/runs/40680667823) | success |
| clients/ruby RSpec | [40680667701](https://github.com/vpsfreecz/haveapi/actions/runs/40680667701) | success |
| clients/rust | [40680667634](https://github.com/vpsfreecz/haveapi/actions/runs/40680667634) | success |
| i18n health | [40680667714](https://github.com/vpsfreecz/haveapi/actions/runs/40680667714) | success |
| release | [40680667625](https://github.com/vpsfreecz/haveapi/actions/runs/40680667625) | success |
| servers/ruby RSpec | [40680667978](https://github.com/vpsfreecz/haveapi/actions/runs/40680667978) | success |
| servers/ruby performance | [40680667726](https://github.com/vpsfreecz/haveapi/actions/runs/40680667726) | success |

Master-context metadata evidence: `master-release-run-evidence.json` binds
release run `40680667625` to `push`, branch `master` and the exact final head.
`master-release-workflow.log` lines 750–762 show the checked-out conditional
routing an empty `RELEASE_TAG` and `refs/heads/master` to
`check-clean --master`; line 1104 records `Release metadata valid: 0.31.0`.
The branch selection is established by those event inputs and the logged
conditional. The publish job was skipped and no packages were published.

Performance run `40680667726` selected the actual master push pair:
`2f5156262baaf137800c17a9321e617c2b5df1d5` baseline and
`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0` candidate. Its quick report is a
measured pass: 14/14 cases, 14 wall-time, 14 CPU-time and 14 allocation
classifications passed; zero inconclusive or no-work cases. Retained artifact:
`master-ci-artifacts-40680667726/performance-40680667726-1/`, including
`results/report.json` and `selection.json`. No failure, rerun or cancellation
occurred, and no workflow remains active.

Final fresh read-only SSH proof at 2026-10-28 11:41:28 UTC: after `git fetch
origin`, `git ls-remote` independently returns both master and retained feature
at `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`. Fetched origin/master agrees,
and `git merge-base --is-ancestor` proves the exact final feature head is
integrated into that remote master. Feature checkout status is clean. No
history refresh, equivalent-successor substitution or follow-up source change
was needed. All session worktrees and branch refs remain available.


Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-release-versioning-audit/
