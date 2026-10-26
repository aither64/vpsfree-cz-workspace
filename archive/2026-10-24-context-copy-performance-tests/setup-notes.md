# HaveAPI setup recovery

Setup completed by implementer0 on 2026-10-24. No application edits, project
commits, index changes, branch deletion/recreation or pushes were made.

## Identity and retained Git effects

- `dev-session current`, both environment variables and the trusted thread
  binding agreed on `2026-10-24-context-copy-performance-tests` in
  `/home/aither/workspace/ai/vpsfree.cz`.
- The failed original add had left the expected clean branch/worktree at
  `39909094649b1d14a23f00615775ca7136acf4fd`.
- Worktree: `worktrees/2026-10-24-context-copy-performance-tests/haveapi`.
- Branch: `2026-10-24-context-copy-performance-tests`.
- Git common directory: `repos/haveapi.git`; worktree Git directory:
  `repos/haveapi.git/worktrees/haveapi1`.
- The repository manifest already preserved the genuine initial base above.
  No historical base was inferred or supplied during the retry.
- Origin is the canonical SSH remote `git@github.com:vpsfreecz/haveapi.git`.

## Hooks and dependencies

Read the workspace procedures, HaveAPI `AGENTS.md` and development procedure,
then inspected `.overcommit.yml`, both `.git-hooks/pre_commit/*.rb` plugins and
the existing common Git hook launcher. Normal setup in the top-level Nix shell
completed successfully:

```sh
nix develop -c bash -lc 'bundle exec overcommit --install && bundle exec overcommit --sign'
```

The repository's required plugins run the i18n health check and, for affected
Python files, locked Python formatter/linter checks. RuboCop and PhpCsFixer are
enabled. Signature verification remains enabled; no bypass was used.

A fresh operation-scoped verification watcher used the pinned catalog
`840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa`, its
`gpt-6-luna`/`low` utility policy and full execution access. Dependency
preparation passed in 67 seconds: the top-level bundle and server bundle checks
passed; Overcommit 0.73.0, RuboCop and the Nix PHP formatter were available.
Local ignored gems and component locks are prepared. Rust, JavaScript and Python
component dependencies were not prepared by this task.

- Complete dependency log: [setup-dependencies.log](setup-dependencies.log).
- Exact dependency exit status: [setup-dependencies.exit](setup-dependencies.exit).

## Registration environment lesson

Running `dev-session worktree add` from inside `nix develop` first failed before
Git: the packaged workspace runtime's Ruby 3.4.9 inherited the repository's
`GEM_HOME` and loaded a native JSON extension built with flake Ruby 3.4.11. Its
loader then reported missing `GLIBC_2.44`.

Retrying the ordinary registration command from the ambient workspace shell
avoided that native-gem contamination and succeeded:

```sh
dev-session worktree add 2026-10-24-context-copy-performance-tests haveapi --as-is
```

The ambient toolchain already supplies Overcommit 0.71.0. Repository hook-managed
Git work and Ruby checks should use the repository Nix shell; invoke the packaged
`dev-session` CLI from the ordinary workspace shell. Keep Nix shell startups
serial because they install into the same worktree-local `.gems` directory.
Related existing lesson: `notes/haveapi/2026-10-12-worktree-hook-signature.md`.

## Quick verification

The following ran serially in the top-level Nix shell and passed:

- `bundle exec overcommit --list-hooks` confirmed required hooks enabled.
- `git hook run post-checkout -- <expected-head> <expected-head> 1` passed.
- `git hook run pre-commit` passed with an empty index. File-scoped linters
  therefore did not validate a source change.
- `bundle exec rake i18n:health` passed explicitly.
- `make doc` passed, as required before Ruby server specs.
- Server `bundle check` passed.
- `bundle exec rspec spec/validator_chain_spec.rb` passed: 1 example, 0 failures.

Reusable verified command from the HaveAPI worktree:

```sh
nix develop -c bash -lc 'bundle exec rake i18n:health && make doc && cd servers/ruby && bundle check && bundle exec rspec spec/validator_chain_spec.rb'
```

The worktree remained clean at the original exact HEAD after these checks.
This validates setup only; focused Context checks will follow the architect's
design brief. Implementer0 relinquishes setup Git ownership after reporting;
future commits/index/fetch/push operations require a lead-assigned window.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-context-copy-performance-tests/>.
