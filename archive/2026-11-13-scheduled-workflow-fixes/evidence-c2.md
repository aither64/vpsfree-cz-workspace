# C2: hosted os-staging commit fails before Git starts

Owner: implementer1. Bounded read-only diagnosis after C1's actual integrated
run. No rerun, application edit, source release, merge/default write or cache
download. Integrated `8306d29` history must be preserved; any repair needs a new
focused commit under a sufficient brief and lead allocation.

## Hosted evidence and availability

[Run 43448052982](https://github.com/vpsfreecz/vpsadminos-org-configuration/actions/runs/43448052982),
attempt 1, event `workflow_dispatch`, ref master, event and actual checkout head
`8306d29d09f1939d1f92d44b5a5e241429b40c2e`.
[Job 131962638455](https://github.com/vpsfreecz/vpsadminos-org-configuration/actions/runs/43448052982/job/131962638455)
failed `Update flake inputs` (step 8); final check/push was skipped. Cache save
succeeded. Lead's hosted watcher is terminal with no unfinished effects.

The exact failed-attempt log is retained at
`/tmp/scheduled-workflow-fixes-org-migration-hosted/run43448052982-failed.log`.
The full exact-attempt log was also inspected via `gh run view --attempt 1 --log`.

- At 15:03:23-24 UTC, Nixfmt and every commit-msg hook passed. Generated local
  runner commit `447f6d1` updated nixpkgs and `vpsadminos/nixpkgs` to `ac588ef1`.
  The stable channel command completed and printed its update summary.
- The subsequent os-staging command's log starts at 15:03:26. At 15:07:46 it
  reports only `error: git commit failed`, with no second Git or hook output.
- Its internal log path is
  `.confctl/logs/2026-11-13--15-03-26-confctl-inputs-channel-update.log` inside the
  terminated hosted checkout. That file and candidate lock were not uploaded.
- The artifacts endpoint returned no artifacts. Cache metadata confirms
  `confctl-cache-Linux-43448052982`, ID `10481320430`, size 6,084,585,650 bytes,
  ref `refs/heads/master`. The workflow caches only `~/.cache/confctl` mirrors,
  not repository `.confctl/logs`; downloading it would not recover that log.

This proves the original plugin-signing fix worked. A second hook failure is
not present in the retained log and must not be invented.

## Causal mechanism and exact source

The pinned guard/tool and current confctl remote master are both
`822c0e35dbe2549111912f539116b4225dfd3035`. Local `origin/master` agrees; the
bare repository HEAD `cc40679d` is stale and was not used for conclusions.

- [`GitCommit.commit!`, lines 4-12](https://github.com/vpsfreecz/confctl/blob/822c0e35dbe2549111912f539116b4225dfd3035/lib/confctl/inputs/git_commit.rb#L4-L12)
  places the entire message in one `git commit -m MESSAGE` argv element and
  raises the generic `git commit failed` if `Kernel.system` returns false/nil.
- `ForwardGuard.validate` collects changed paths throughout the lock graph.
  `GuardedUpdate.run!` converts these through `FlakeLockDiff.from_guard` and
  passes all descendant changes to the commit callback after installing the
  validated candidate.
- [`CommitMessage.build_changelog_group`](https://github.com/vpsfreecz/confctl/blob/822c0e35dbe2549111912f539116b4225dfd3035/lib/confctl/inputs/commit_message.rb#L33-L57)
  groups identical source/revision ranges and includes the full oneline Git log
  for each group. `GitRepoMirror.log` uses
  `--no-decorate --left-right --cherry-mark --oneline`.

The root org staging pin is `e2b2b9186de6e0aec66f87a0e4d16e86bc2d7854`
(`root.inputs.vpsadminos` resolves to node `vpsadminos_2`). Its old unstable
Nixpkgs descendant is `02c087f3fe673c9e317f206a627cb6b910336dbe`. Do not confuse
the root staging pin with the older `a169291a` node under confctl's own input.

Current upstream staging is `c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62`, whose
commit timestamp 14:58:23 UTC predates this 14:59 dispatch. Its unstable
Nixpkgs pin is `d4f25a3e562008648d45bcf2d70bcc7422cad84e`. Since the actual
hosted candidate lock was not retained, identifying this exact candidate as the
hosted one is an explicit inference. The mechanism below is independently
reproduced against exact immutable sources/ranges.

The actual staging-root changelog alone is small (2,907 bytes). The unstable
Nixpkgs descendant log is **1,200,140 bytes**, before title/summaries/other
groups. Read-only command against the already-present mirror:

```sh
git --git-dir=/home/aither/.cache/confctl/git-mirrors/fd81e3fd09cfd0b8761b459a157eca324168710dd00674260bad19686833ed94 \
  log --no-decorate --left-right --cherry-mark --oneline \
  02c087f3fe673c9e317f206a627cb6b910336dbe..d4f25a3e562008648d45bcf2d70bcc7422cad84e | wc -c
```

This descendant is included by the guard's complete-change callback, so its
message is already too large to be one process argument. No truncation or
changelog removal is needed to identify the cause.

## Small local execution proof

Exported the exact pinned `git_commit.rb` to the disposable file
`/tmp/2026-11-13-scheduled-workflow-fixes-c2-git-commit.rb`; no repository source
was changed. In the declared C1 repository environment, tested a 200,000-byte
message with two calls:

```ruby
Process.spawn('git', 'commit', '-m', message, 'flake.lock')
ConfCtl::Inputs::GitCommit.commit!(conf_dir: '/tmp', message: message,
                                 editor: false, files: ['flake.lock'])
```

The first call raises `Errno::E2BIG`. The exact pinned helper reports only
`"git commit failed"`, child status 127, with no Git/hook output. Both fail at
process launch, before Git or hooks can execute. The measured real descendant
changelog is six times this failing diagnostic payload size.

Thus the source, message size and execution behavior explain the hosted
failure: an oversized `-m` argument prevents Git from starting. The literal
hosted errno is unavailable because the implementation masks the launch
failure and the internal log was not retained; do not claim an observed hosted
`Errno::E2BIG` exception. There is no retained evidence of an authentication,
upstream availability, Nixfmt or Ruby native-gem failure at this second commit.

## Repair boundary and next dependency

Architect0 has the exact source/byte/exec evidence and is settling the narrow
contract. The likely source repair is confctl's commit helper using a temporary
message file and `git commit -F`, preserving full text, editor selection, owned
file arguments, normal hooks and failure semantics. The org workflow then
consumes the reviewed immutable tool revision. No repair is released by this
investigation; lead owns cross-repository allocation.

Existing test entry points at exact confctl master:
`spec/inputs/commit_message_spec.rb` (aggregation) and
`spec/inputs/guarded_update_spec.rb` (commit boundary). There is no dedicated
GitCommit spec yet and no existing Tempfile / `git commit -F` helper under
`lib/` at that revision. Focused RSpec runs belong in confctl's declared Nix
environment. No further historical exploration, full cache download or hosted
rerun is necessary before that bounded source/test brief.

G1 remains parked with implementer1 owner. Its already-running utility has now
passed the real coherent Ruff parity and exact runtime gate, exit 0, with all
tool sessions ended; result is retained for later lead release. No new G1 target
preparation or application operation was started during C2 diagnosis.
