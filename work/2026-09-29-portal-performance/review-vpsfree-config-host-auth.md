# Review: aitherdev portal bcrypt cost deployment unit

## Assignment

Independently review the committed `vpsfree-cz-configuration` deployment unit
for correctness, security, compatibility, scope and verification gaps. This is
a High-risk authentication and deployment change. Apply the General,
Architecture and repetition, Scope and proportionality, and Risk and
compatibility lanes from the mandatory-change-review workflow. Report findings
as Blocking, Important or Advisory with exact file/line evidence, then state
explicitly whether the unit is ready for the long build and deployment checks.

## Repository and commits

- Worktree: `worktrees/2026-09-29-portal-performance/vpsfree-cz-configuration`
- Base: `6c827ca2c1b18fe79171ecc8fea03ad80b803f82`
- Head: `bfb7b883f02df270cb93fb984793ef287c191b5a`
- Commits:
  - `52314246 inputs: set devWorkspace to ec05cb9f`
  - `bfb7b883 aitherdev: reduce workspace portal bcrypt cost`
- Diff: `git diff 6c827ca2c1b18fe79171ecc8fea03ad80b803f82..bfb7b883f02df270cb93fb984793ef287c191b5a`

The input bump is isolated in the confctl-generated `flake.lock` commit. The
functional site setting is a separate commit so configuration integration and
rollback remain auditable.

## Intended contract

- Pin `devWorkspace` to reviewed and VM/CI-verified revision
  `ec05cb9f008cc8d6bccfd23e9b15a69d9a66fa40`.
- Set only aitherdev's `services.dev-workspaces.auth.bcryptCost` to `5`.
- Preserve the generic module default of 12 on every host without this explicit
  setting.
- Preserve the existing 64-lowercase-hex generated password, TLS, Basic Auth,
  owner/group/mode checks and atomic htpasswd regeneration.
- A system rollback to the previous configuration removes the site override
  and regenerates a cost-12 hash from the unchanged password.

## Compatibility and migrations

There are no database, API, protocol, session, package-state or on-disk format
migrations. Old and new configurations use the same password and htpasswd file
shape. Switching changes only the encoded bcrypt cost. Mixed application and
system versions remain compatible because nginx Basic Auth consumes the same
file contract. Rollback preserves credentials and restores cost 12, accepting
the prior latency as the recovery tradeoff.

## Evidence before review

- Dev-workspace focused evaluation and host-auth benchmark checks passed.
- Dev-workspace NixOS host-module idempotency VM check passed at exact revision
  `ec05cb9f008cc8d6bccfd23e9b15a69d9a66fa40` in about 3m07s.
- Dev-workspace GitHub Actions `Check` run `36656964160` passed at that exact
  revision; its host job was skipped, so the separate local VM result remains
  the host integration evidence.
- Configuration `nix flake check --no-build --show-trace` passed.
- `nix flake metadata --json` resolves `devWorkspace` to the exact target.
- Nix formatting hooks and `git diff --check` passed.

## Remaining gates

- Review reconciliation and any required focused rerun.
- Push the exact configuration feature head.
- Fresh Luna/low watcher runs `confctl build` for aitherdev.
- Fresh watcher runs dry activation and the authorized system switch.
- Verify encoded cost 05 without printing the hash or password, file
  ownership/mode, correct-password success, unauthenticated/wrong-password
  denial, TLS and reconciler idempotence.
- Run the 30-load no-scan and 30-load overlapping dry-run-scan browser gates.
- Complete whole-branch history/migration review before authorized default
  branch integration.
