# Historical target hook recovery and shared trust blocker

2026-10-20; implementer1; verified same-session identity and retained
`workspace_write` access. Follow-up to [source recovery](merge-hook-recovery-owner.md).

Coordinator run `a9c23f6e-036d-4680-b06b-4b27701c0393` stopped again in
`prepare`, generation 1, event `482f55fc-a2e4-e7f9-99cc-c4536262d9c2`.
The actual failure was ordinary target worktree checkout at upstream
`c58704a08451a231fdf6c6123437133422af46dc`: configuration signature changed.
Status showed no submitted jobs. The lead retains handoff/resume ownership.

## Exact historical target

```text
/home/aither/.local/state/dev-workspaces/coordination/sources/12333ff7-ea69-40cb-8d9c-18980ff8120b/target
```

The target is detached and clean at that exact upstream commit, tree
`d89acdc74b6e717369a51c79127c08581afeb272`. Its configuration and every
custom hook matched committed upstream bytes:

| Path | SHA256 |
| --- | --- |
| `.overcommit.yml` | `683eac8182c71035af2f47fccab2b31621af8426e2eb1746bb686259adfbad03` |
| `.git-hooks/pre_commit/haveapi_i18n.rb` | `57280b9992d3914434456f3a5ed90060668d6d3369ec9d3313e43405318d7aeb` |

The historical configuration enables HaveapiI18n, RuboCop and PhpCsFixer;
PythonChecks is absent at this revision. The i18n custom hook is identical to
the reviewed feature's hook.

## Signing receipt and timing

Under the initial explicit historical-target signing grant, these ordinary
commands ran from the target in the retained prepared `merge_hooks` environment
`sha256:f1efd997ffdfb5bf4333cac0dea83c57581725164e65b111b400b13cec8f5306`:

```sh
bundle exec overcommit --sign
bundle exec overcommit --sign pre_commit
```

Both exited 0. Plugins were unchanged. The shared configuration signature
changed from feature value
`b60e0548237424002fc3f5930a5c0bf3743f5e7fa671f82d380ae0cf7729a4cb`
to historical value
`689faa60978769404adfbfa8665fda4599f9813868d38b5fe170cb3d6273711a`.
`overcommit.configuration.verifySignatures` remains `1`.

The existing ordinary post-checkout hook, resolved by
`git rev-parse --git-path hooks/post-checkout`, passed under the same prepared
environment with both commit arguments equal to the historical commit and
checkout flag `1`. Final assertions confirmed exact target HEAD and empty
working-tree/index status.

The lead's later instruction to stop historical signing arrived after this
already-launched signing/validation command completed. This timing and the
new shared signature were reported immediately. No coordinator retry or
further signing followed. The historical signature above is the current
shared trust state at this handoff; the feature signature was not restored.

## Why signing alone cannot unblock preparation

Selected runtime:

```text
/nix/store/1i1g6rp8ind51qqayzpww7cn1xp1k1gq-dev-workspace-0.2.0
```

Its `libexec/workspace-coordination-execution.rb` establishes the sequence:

- `retain_commit` at line 203 performs the ordinary feature checkout on every
  preparation, including an already-retained source.
- `prepare_merge` at line 291 then creates a new UUID target worktree at
  historical upstream, using the prepared feature hook environment.

Installed Overcommit 0.73.0 explicitly uses `git config --local` for signature
reads and writes in `lib/overcommit/configuration.rb` (lines 234 and 327) and
`lib/overcommit/hook_signer.rb` (lines 70 and 105). Both checkouts share the
canonical repository configuration. One configuration-signature value cannot
match both distinct inspected configurations. Resuming unchanged after target
signing would return to the feature signature failure; repeatedly signing and
resuming would alternate the failure.

Read-only feasibility checks found no ordinary per-worktree CLI solution:

- Installed Git 2.54.0 documents `--local` as reading only the repository
  configuration. Reading `config.worktree` requires `--worktree` and
  `extensions.worktreeConfig`; Overcommit does not request that scope.
- Git documents includes as disabled by default for explicit configuration
  scopes. A stdin configuration containing only an include of the existing
  canonical configuration returned exit 1 for the signature query; the same
  read with `--includes` returned exit 0 and the stored historical signature.
  These probes wrote no files.
- `GIT_CONFIG=/dev/null` combined with Overcommit's forced `--local` query
  returned exit 129, `only one config file at a time`. It cannot redirect that
  forced scope.
- `includeIf gitdir` matches the resolved Git administration directory for a
  linked worktree, not the checkout's UUID path. Even enabling includes alone
  would leave ordinary signing writing the shared local signature, and the
  target must later accept feature configuration after fast-forward.

The architect received the exact source locations and feasibility findings.
A supported change to trust handling or the preparation/hook environment must
be scoped by the architect and authorized by the lead before application.
No such change has been applied. Preparation remains blocked; this receipt
does not recommend another unchanged resume.

## Preserved boundaries

No source, ref, ledger, coordinator artifact or manual Git configuration edit
was made. Normal signature verification stayed enabled, and normal hooks ran.
Recovery refs/stash and original request-bound evidence remain preserved.
No merge, push, rebase or release operation was performed. The hook/Git slot
is released after reporting; the lead coordinates any next package.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-dynamic-python-api-client/>
