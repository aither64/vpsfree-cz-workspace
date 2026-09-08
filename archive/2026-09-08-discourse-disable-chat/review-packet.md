# Discourse chat review packet

## Request and acceptance

User: disable chat on Discourse in vpsfree-cz-configuration and evaluate
declarative config versus runtime UI config. Record a working default using
the existing deployment model, explain override precedence, preserve data,
and be explicit that live activation/verification is outstanding.

## Scope and commits

- Initiative: `2026-09-08-discourse-disable-chat`.
- Workspace root: `/home/aither/workspace/ai/vpsfree.cz`.
- Plan/state: `work/2026-09-08-discourse-disable-chat/{plan,state}.md`.
- Worktree: `worktrees/2026-09-08-discourse-disable-chat/vpsfree-cz-configuration`.
- Base: `08dae58b16abdde30cff1572478b29343ed32fc4`.
- Head: `7cfe3837` (resolve full hash in the worktree).
- One commit: four added lines defining `siteSettings.chat.chat_enabled = false`.
  No independently separable changes, dependencies, docs, or schema changes.
- nixpkgsStable pin: `a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4`.
- Existing Discourse package: 2026.7.1, unchanged.

## Decision and boundaries

Recommend declarative default to record the policy in Git. The UI remains the
runtime override authority; a stored true value must be disabled/reset at
deployment. Immediate UI-only disable remains possible but would leave the
policy solely in the database. Do not introduce custom enforcement services,
remove the plugin, delete data, change retention or disable personal messages.
No reusable interface is changed; only the existing host-local module consumes
the NixOS Discourse settings interface.

## Verification and source evidence

- Installed Overcommit with `nix develop -c overcommit --install`.
- `nix develop -c overcommit --run`: Nixfmt and RuboCop passed.
- `git diff --check`, Nix parse, and host-module chat evaluation passed.
- Exact container toplevel and autoRollback `nix build --dry-run` passed;
  81 derivations await the full build, which has not started.
- Commit hooks passed; tracked implementation is committed and clean.
  `.bin/`, `.bundle/`, and `.rubocop_cache/` are generated untracked caches
  pending cleanup before finalization.
- Pinned nixpkgs source:
  `/nix/store/nqkh6j5xlyvlw4hlrw4ybpq1cis79szf-source`.
  Inspect `nixos/modules/services/web-apps/discourse.nix` and
  `pkgs/servers/web-apps/discourse/nixos_defaults.patch`.
- Pinned Discourse source:
  `/nix/store/41qy7yjm0wr89bd2sjxsy4yhbs1kpdfj-source`.
  Inspect `app/models/site_setting.rb`, `lib/site_setting_extension.rb`,
  `lib/site_settings/defaults_provider.rb`, `plugins/chat/config/settings.yml`.
- SSH authentication to the live host failed; no effective live setting or
  current generation is known, and no production mutation occurred.

## Risk and deployment

High under the skill classification because deployment/rollback and persisted
UI overrides require consideration; the actual implementation is a bounded,
reversible default. All reviewers use gpt-5.6-sol with xhigh effort.
Applicable lanes: general, architecture, scope, risk/compatibility.

Only the Discourse container requires activation. No schema, API, protocol,
or persisted format changes. No fleet coordination. Config rollback restores
the old default but does not clear database overrides. Check/reset any true
override during deployment. Re-enabling after a false UI override requires a
UI action. Existing chat data is retained; no retention policy changes.

Review directly in your assigned lane; do not modify files or spawn agents.
Report findings by severity, or explicitly no findings plus residual gaps.
