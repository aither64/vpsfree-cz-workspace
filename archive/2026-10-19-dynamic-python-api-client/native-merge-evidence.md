# Native HaveAPI master integration

2026-10-20; implementer1; session identity and retained `workspace_write`
verified. User authorized merging the Python client into HaveAPI master and
explicitly requested **no release**. The lead granted native fast-forward and
SSH publication after accepting the fresh unchanged-baseline preflight.

## Ownership and exact revisions

- Claim: `fa9aac60-c9e4-45fb-b21e-6433a2e609b6`, revision 1, `held`.
- Owner: `e51277e3-c4c3-43eb-b889-90e84d91b5bf`, this exact session.
- Resources: canonical `repos/haveapi.git` common Git directory and
  `repository:github.com/vpsfreecz/haveapi`; no machines.
- Selected claim guide:
  `/nix/store/i2q0yyjkyvd0x3qa3cy9jafr1jmgxc70-dev-workspace-0.2.0/share/dev-workspace/coordination.md`.
- Old fetched/local/remote master:
  `c58704a08451a231fdf6c6123437133422af46dc`.
- Reviewed feature and final local/remote master:
  `c1823f3d70365b0442d0e2171bdf83bd4c6dbe31`.
- Final tree: `aec5847f4c735ac68a7b6158c76a4f667f6a6a18`.
- Canonical fetch/push remote: `git@github.com:vpsfreecz/haveapi.git`.

Authoritative claim status was rechecked before the mutation phases. The
selected claims flow superseded the old automatic-executor instructions for
this operation, as directed by the lead. The canceled, unsubmitted legacy
integration was not resumed; its receipts and retained payloads were preserved.

Fresh SSH fetch and remote queries confirmed no baseline drift. The clean
feature, complete eight-commit series, and final diff matched the retained
independent review and accepted documentation follow-up in
[premerge-evidence.md](premerge-evidence.md). Diff: 62 files, +10539/-17;
binary diff SHA256
`3f0427fc7897efd21b7b5c261eee70d0cad99e28cad2931f04a4ae144781b1bd`,
exactly unchanged. No obsolete fixes, repeated update streams or migrations;
no supported state or intermediate consumer boundary required preserving
superseded history. No rebase or new source change was needed.

## Native commands and actual hook results

All mutation shells used `set -euo pipefail`; child exit codes and hook output
were checked. Existing prepared Nix hook environment
`sha256:f1efd997ffdfb5bf4333cac0dea83c57581725164e65b111b400b13cec8f5306`
was verified as `merge_hooks` for HaveAPI at the exact reviewed feature.
Only its declared environment values were overlaid on command processes;
neither environment contents nor credentials were dumped. Hook-disabling
environment overrides were absent. Dependencies were already available.

Fresh temporary integration worktree:

```text
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-dynamic-python-api-client/haveapi-native-merge-target
```

The native sequence was:

1. `git worktree add <target> master` checked out exact old master with the
   already-inspected historical signature. Native checkout succeeded; an
   explicit invocation of the existing normal post-checkout hook also exited
   0 with old/new arguments both equal to old master and checkout flag `1`.
   Target was clean, and its historical configuration/custom-hook hashes
   matched the previously inspected committed upstream bytes.
2. In the unchanged feature worktree, compare final configuration and both
   custom hooks to their exact reviewed SHA256 values, then run ordinary
   `bundle exec overcommit --sign` and
   `bundle exec overcommit --sign pre_commit`. Both exited 0; plugins were
   unchanged. This happened before the merge, so the post-merge hook would
   see matching final trust. Configuration signature is
   `b60e0548237424002fc3f5930a5c0bf3743f5e7fa671f82d380ae0cf7729a4cb`;
   `overcommit.configuration.verifySignatures` remained `1`.
3. In the target, run
   `git merge --ff-only c1823f3d70365b0442d0e2171bdf83bd4c6dbe31`.
   Git reported a fast-forward and no hook failure. The existing normal
   post-merge hook was then explicitly invoked with argument `0` and exited
   0, confirming actual hook success independently of Git's merge exit code.
4. Recheck remote master still equals the expected predecessor, target/feature
   cleanliness, SSH remote and held claim. Invoke the existing normal
   pre-push hook with the actual `refs/heads/master` old/new update as stdin:
   exit 0. Run ordinary, non-force
   `git push origin refs/heads/master:refs/heads/master`. Its native pre-push
   hook passed and the push reported `c58704a..c1823f3 master -> master`.
5. `git ls-remote --heads origin refs/heads/master
   refs/heads/2026-10-19-dynamic-python-api-client` confirmed both refs equal
   the exact reviewed feature. Local master had the same commit/tree; target
   and feature were clean.

No hook was skipped or disabled, and no signature value was written manually.
The installed hook entrypoints ran in the prepared repository environment.
The existing unused debug/native-extension warning remained nonfatal; there
was no checkout, merge or push hook failure in this native sequence.

Command outputs and exact exit codes are retained in
[verification/native-merge/commands.log](verification/native-merge/commands.log),
SHA256 `0bc214651d1211894d4f8aa4112ddca93228e6e86be4d16dc5bb7c342e53c87a`.

## CI inventory and cleanup

One read-only exact-head master CI inventory was captured in
[master-ci-initial.json](verification/native-merge/master-ci-initial.json).
No CI waits, reruns, cancellation or new watcher were started:

| Workflow | Run | Observed state |
| --- | --- | --- |
| clients/python | [39487820831](https://github.com/vpsfreecz/haveapi/actions/runs/39487820831) | in progress |
| servers/ruby RSpec | [39487820870](https://github.com/vpsfreecz/haveapi/actions/runs/39487820870) | in progress |
| RuboCop | [39487821041](https://github.com/vpsfreecz/haveapi/actions/runs/39487821041) | in progress |
| release | [39487821053](https://github.com/vpsfreecz/haveapi/actions/runs/39487821053) | in progress |
| i18n health | [39487820847](https://github.com/vpsfreecz/haveapi/actions/runs/39487820847) | success |

Prior reviewed exact-head local and CI evidence remains applicable; no local
tests were repeated. The workflow named `release` is a normal master-push CI
run, not a tag or publishing action initiated by this operation.

After remote effects, clean target, exact tree and retained logs were verified,
only the freshly created target was removed with ordinary
`git worktree remove <exact-target>`, exit 0. All local refs were equal before
and after that removal, the retained recovery stash object was still present,
and the feature remained clean. Feature/recovery refs, old coordinator payloads
and stash were preserved. All native commands have exited; no mutation child
remains from this package.

The lead owns claim release after accepting this receipt. No source/history
rewrite, unrelated ref push, tag, version, registry, protected environment,
release, PR, deployment or session lifecycle action was performed.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-dynamic-python-api-client/>
