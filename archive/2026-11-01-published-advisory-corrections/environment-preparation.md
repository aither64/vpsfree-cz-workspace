# vpsAdmin environment preparation

Prepared by implementer0 on 2026-11-01. Application edits await the architect's
design and lead assignment. No project source changed and no project commit,
application test, deployment, resource claim or lifecycle cleanup occurred.

## Repository identity

- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-published-advisory-corrections/vpsadmin`
- Branch: `2026-11-01-published-advisory-corrections`
- Clean HEAD and registered initial base:
  `610a96f8ce523afbcd3e4374a70047dbe3264b0d`
- Canonical `origin/master` matched that exact base at preparation. Stale local
  `master` was not used.
- `dev-session current`, both identity environment variables and the trusted
  conversation binding matched this session and workspace.

## Checkout and hooks

The assigned `dev-session worktree add ... --base 610a96f8ce523afbcd3e4374a70047dbe3264b0d --no-fetch`
created the branch and worktree, then returned exit 1 because the existing
Overcommit post-checkout hook rejected its configuration signature. The worktree
was already clean at the intended HEAD and `portal.yml` already registered its
exact initial base. No checkout retry was needed. This matches the existing
[checkout recovery note](../../notes/vpsadmin/2026-09-30-overcommit-worktree-checkout.md).

After reading `.overcommit.yml` and all four `.git-hooks/pre_commit/*.rb` files,
the root Nix shell successfully ran `bundle exec overcommit --install` and
`bundle exec overcommit --sign`. `bundle exec overcommit --sign pre-commit`
reported no changed plugin signatures. Direct replay of post-checkout with the
original new-worktree arguments passed. Direct pre-commit invocation passed with
an empty index; this establishes framework readiness, not validation of later
source changes. `git diff --check` passed and the worktree remained clean.

Use the repository root Nix shell for future Git operations so Overcommit has
the expected Ruby and tools. Git operations remain assigned exclusively to
implementer0 until the lead releases that ownership.

## Dependency evidence

A fresh standalone verification watcher ran the two preparation commands below:

```sh
nix develop .#vpsadmin --command bash -c 'set -e; bundle check; bundle exec overcommit --version; ruby --version; command -v nixfmt php-cs-fixer php msgfmt'
VPSADMIN_PLUGINS=all nix develop .#api --command bash -c 'set -e; bundle check; ruby --version; bundle exec rspec --version'
```

Both exited 0: root preparation took 46 seconds, API preparation 66 seconds.
Ruby is 3.4.9, Overcommit 0.74.0 and RSpec 3.13. Both bundles are satisfied.
The requested root tools are present; PHP resolves through the installed user
profile. Bundles and generated lockfiles are ignored worktree preparation data.
No test database was started.

Watcher: `01a19806-3b53-73f0-83f0-a7c830b50c2a`, GPT-6 Luna/low, native utility
`dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`, retained/installed catalog
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`.
Launch output verified `danger-full-access`, approval `never`, and codex-lb.
The watcher completed without a remaining process, retry or cancellation.

Raw logs and its final report are disposable artifacts under
`/tmp/2026-11-01-published-advisory-corrections-preparation/`:
`root-shell.log`, `api-shell.log`, `watcher-console.log`, `watcher-result.md`.

## Verification commands available for the design brief

Repository procedures are authoritative:
`docs/agent-instructions/development.md` and
`docs/agent-instructions/testing.md`.

The API shell enters `api/`. Existing advisory specs can be selected with
`VPSADMIN_PLUGINS=all nix develop .#api --command bundle exec rspec` followed by
these relative paths:

- `spec/models/security_advisory_spec.rb`
- `spec/api/resources/security_advisory_spec.rb`
- `spec/api/plugins/outage_reports/security_advisory_spec.rb`

The architect selects the final bounded checks and required core-mode coverage.
Automatic isolated MariaDB startup is available because this worktree has no
`api/config/database.yml`; no manual database configuration is needed. Any long
or uncertain check batch requires a fresh operation-only watcher.

Use the appropriate component's `bundle exec rubocop` for touched Ruby files;
the commit itself must pass the installed Overcommit hooks from the root Nix
shell. New API resource specs matching `security_advisory*` already belong to
the static `platform-operations` topic; new model specs belong to `foundation`.
No test or CI selection file was changed.

Next dependency: accepted architect design and an application execution package.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/>
