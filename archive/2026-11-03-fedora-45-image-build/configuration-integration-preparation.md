# Configuration master integration preparation

The lead relayed the user's explicit approval to integrate
`vpsfree-cz-configuration/master`. Implementer1 owns preparation only; the lead
owns the short repository claim, final checks, fast-forward merge, SSH push,
remote proof and claim release. No deployment or lifecycle action is authorized.

## Exact prepared target

- Canonical repository:
  `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`
- Detached target:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-fedora-45-image-build/vpsfree-cz-configuration-master-integration`
- Fresh `origin/master` and target base:
  `c4107822060e9e34b24a83950d618c9f28a7722b`
- Reviewed/tested feature:
  `e3ac35780cc909764a3bb059b4d9dfa23cf60867`
- Target and feature clean; base is an ancestor of feature. No rebase or source
  change was needed. No claim, merge or push was performed during preparation.

Bound session identity was reverified (`current` matched, both environment
identity variables absent). Repository AGENTS and Overcommit configuration were
reread. The selected package's `workspace-host coordination guide` and complete
installed coordination/operations guides were read, package
`/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0`, coordination
catalog SHA256 `b17a5618c6ce3988022bd02962d4dad95d735568fc4b2717ce462364e41eab6d`.

## Hooks and minimal environment

Existing feature Nix and gem caches were reused; no package build or dependency
installation was needed. Detached target creation's post-checkout hook passed.
Overcommit installation and explicit `post-merge`/`pre-push` signing passed.
Both active hooks were invoked directly without merging or pushing and passed.
Ruby is 3.4.9; Bundler is 4.1.0.beta3.

The minimal captured environment is:

`work/2026-11-03-fedora-45-image-build/configuration-integration-git-env.json`

It contains only `PATH`, `GEM_HOME`, `GEM_PATH`, `BUNDLE_PATH`,
`BUNDLE_APP_CONFIG`, `BUNDLER_VERSION`, and target-specific `BUNDLE_GEMFILE`.
Paths reuse this session's prepared feature `.gems`/`.bundle`; preserve the
feature worktree during integration. It contains no complete environment or
secrets. Apply these values only to Git child processes. Keep workspace/session
CLI commands in their normal environment to avoid the earlier Ruby collision.

An independent invocation **outside Nix** removed inherited Ruby/Bundler/Gem
variables, applied only that captured allowlist, then passed `bundle check`,
`git hook run post-merge -- 0`, and `git hook run pre-push -- origin
git@github.com:vpsfreecz/vpsfree-cz-configuration.git`. The target remained clean
at the exact base. No Nix entry or installation is needed inside the claim.

Evidence: `configuration-integration-preparation.json` and complete
`config-integration-preparation.log`. If final remote target or hook trust moves,
inspect effects and return to preparation outside ownership under the installed
claim guide. Git can return zero after a post-merge hook failure, so the lead
must inspect its hook result before pushing.

Final fresh SSH proof still matched target base `c4107822` and feature
`e3ac3578`. No pending command remains. Serial configuration Git ownership was
handed to the lead in report `105e6264-7be3-4d42-91bb-356ca37df92b`; implementer1
will make no further configuration Git operations during the lead's integration.
