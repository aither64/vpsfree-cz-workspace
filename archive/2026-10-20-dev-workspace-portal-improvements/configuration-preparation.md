# Configuration package and prepared deployment commands

Implementer0 took complete configuration ownership from implementer1. No work
remains running in the handed-off package. This record prepares commands; it
reports no system/application build or activation. Lead owns review acceptance,
physical-machine reservation, actual activation and deployment acceptance.
Default-branch integration remains unapproved. Independent feature work used no
repository claim under the selected short-merge rules.

## Published source

Configuration base `37a338b25192d9271ee211110800c2dc6a094a57`, final
`450e1ff538c1e94c1ec74f57b50fbe2efb31502b`, canonical SSH branch
`2026-10-20-dev-workspace-portal-improvements`. One generated commit:
`inputs: set devWorkspace to f8f2938b`. The generated body is preserved, including
history and long lines. Nixfmt pre-commit passed; commit-message hooks passed with
the generated width warning. Normal Overcommit 0.73.0 hooks were installed and
signed; none were bypassed. Idempotent worktree registration returned the same
existing path/branch and retained its original base. No checkout reset/recreation.

Only flake.lock changed (+7/-7): `devWorkspace` selects B
`f8f2938b4e2cfd6e5b82657d08f014357817808f`; transitive `codex-web` selects A
`852e8c51091512bc79ca6c921ef1f5ccc46a9535`. All other nodes, follows edges, host
source, authentication, TLS, provider settings and keys are unchanged. Exact SSH
head/default and clean-tree checks passed. No migrations, durable state changes,
obsolete pins or extra commits exist in this one-commit range. Existing operations
docs remain correct; a product documentation change was unnecessary for this pin.

The final C lock selects the same B/A and extension `767dfd5`. Deployment graph
checker passed against C's current lock. Lead must bind its final reviewed C head
and exact realized artifacts before executing. C instruction affected-lane review
is separate from this mechanical pin. No old output may substitute for a refreshed
candidate just because its package version matches.

## Toolchain and focused evidence

The first watcher failed before Nix setup because /usr/bin/time was absent (127).
The corrected fresh Luna/low setup/probe passed in 66.296s: Ruby 3.4.9,
Overcommit 0.73.0, bundle satisfied in ignored worktree-local .gems. Logs remain in
`verification/config-toolchain-37a338b2-retry/`. No Gemfile/lock changes were needed.

The explicit upstream Overcommit fixture initially failed before tests because
config's Bundler group does not include minitest. The meaningful run used B's
declared Ruby/minitest environment with the resolved exact 0.73.0 gems exposed via
GEM_HOME/GEM_PATH. `coordination_claims_overcommit_test.rb --name /overcommit/`
passed 1 run, 52 assertions, 0 failures/errors/skips in 10.424557s. Its hooks/trust,
checkouts, deliberate failures, claims and pushes all stayed in disposable fixtures.
No assertion was weakened and no common hook trust was modified by that test.
The earlier B claims suite passed 24 runs/128 assertions; feature/lead/member quick
checks and exact rebase reconstruction remain recorded separately by lead.

## Exact configured SSH readiness

The host declaration sets aitherdev's target to `172.16.106.40`; normal confctl SSH
is root. Both ordinary configured-route and explicit existing-key probes returned
UID 0 and identical live/system-profile paths `75w4s3z...nixos-system-aitherdev...`.
No password/secret was read. The explicit proven argv is:

```sh
ssh -o BatchMode=yes -o StrictHostKeyChecking=yes -o IdentitiesOnly=yes -o ConnectTimeout=10 -i /home/aither/.ssh/id_ed25519 root@172.16.106.40 'id -u; readlink -f /run/current-system; readlink -f /nix/var/nix/profiles/system'
```

This uses the existing identity and known-host trust; no SSH/auth/sudo configuration
or permissions changed. The session-only smoke helper supports explicitly selected
`PORTAL_SMOKE_PASSWORD_READ_MODE=ssh` through that fixed route and password path,
with private pipes/in-memory httpCredentials and generic failure output. Its
credential reader has not run independently. See [deployment-smoke.md](deployment-smoke.md).

## Prepared commands, not executed

The completed exact argv/receipt/root/log/claim packet is
[configuration-command-packet.md](configuration-command-packet.md). It supersedes
the preliminary wrapper details below. Final C530/Bf8/config450 review gate is
accepted; execution remains with parent/fresh utilities as assigned.

Pinned confctl executable:
`/nix/store/j5wxvlxdnsh2gyc6wbjx8xxfllqp4zmv-confctl/bin/confctl`.
Its actual CLI help confirmed generation ls, build, --generation, --copy-only,
--dry-activate-first and --no-reboot. The no-build deployment graph check was:

```sh
ruby /home/aither/workspace/ai/vpsfree.cz/bin/check-dev-workspace-deployment --workspace-root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/workspace --configuration-root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-dev-workspace-portal-improvements/vpsfree-cz-configuration
```

After final review gate, fresh utility argv for the exact configuration build is
`["bash", "/tmp/portal-improvements-configuration-build.sh"]`. It checks clean
450e1ff5, retains the resolved toolchain roots, runs only the following and lists
the resulting local named generation. It does not copy or activate:

```sh
nix develop --no-update-lock-file -c confctl build --yes cz.vpsfree/machines/aitherdev
nix develop --no-update-lock-file -c confctl generation ls --local cz.vpsfree/machines/aitherdev
```

Lead selects `PORTAL_DEPLOY_GENERATION` from that exact build's named generation,
verifies its embedded clean configuration revision/runtime and retains its store
output/derivation roots. Never use latest/current/default as a substitute for that
receipt. Copy preparation (after build, outside machine ownership when supported):

```sh
nix develop --no-update-lock-file -c confctl deploy --generation "$PORTAL_DEPLOY_GENERATION" --copy-only --yes cz.vpsfree/machines/aitherdev
```

Only lead, after the physical-machine claim is held and fresh identities match,
executes dry activation and no-reboot switch from the clean configuration worktree:

```sh
nix develop --no-update-lock-file -c confctl deploy --generation "$PORTAL_DEPLOY_GENERATION" --no-reboot --yes cz.vpsfree/machines/aitherdev dry-activate
nix develop --no-update-lock-file -c confctl deploy --generation "$PORTAL_DEPLOY_GENERATION" --dry-activate-first --no-reboot --yes cz.vpsfree/machines/aitherdev switch
```

No auto-rollback or health check disabling flag is used. Preserve configured
rollback/generation behavior. Verify both /run/current-system and the system
profile, clean embedded configuration revision and B pin before profile selection.
Then lead uses the ordinary stable workspace-host switch on final C with the SAME
machine claim and exact session pair, as architect's design specifies. This record
contains no automatic activation driver, private lifecycle helper or cleanup.

Stop an unexpected local kernel build and escalate. After the refreshed package
build, parent may run the prepared minimal actual-browser composition argv
`["bash", "/tmp/portal-improvements-final-browser-rooted.sh"]`; it checks clean
f8f2938 and retains exact Playwright/browser/review-asset roots before running the
single portal fixture. No broad suite or browser ran during this preparation.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
