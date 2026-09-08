# 2026-09-08-discourse-disable-chat

## Goal

disable chat on discourse in vpsfree-cz-configuration. evaluate whether we should do it through declarative config or runtime config through discourse UI.

## Affected repositories

- `vpsfree-cz-configuration`, Discourse container configuration at
  `cluster/cz.vpsfree/containers/discourse/config.nix`.
- Workspace coordination records only; no other project changes expected.

## Approach

1. Inspect the pinned NixOS module and Discourse settings loader to compare
   declarative defaults with database-backed settings changed through the UI.
2. Check the current runtime setting read-only if trusted SSH access permits.
3. Prefer the existing `services.discourse.siteSettings` mechanism if it
   reliably supplies the chat plugin default. Explain persisted UI overrides
   and any required runtime action. Avoid custom enforcement machinery for
   a single application setting.
4. Commit the smallest justified configuration change, run quick checks and
   mandatory change review, then build the affected container.
5. Report the recommended approach, verified behavior, and remaining
   integration/deployment action with the session portal link.

## Compatibility and deployment

- Disabling chat is a reversible application setting. Do not remove its plugin,
  delete chat messages/channels, or change retention settings.
- No database schema, on-disk format, API/client, CLI, Terraform, or service
  protocol changes are intended. Existing versions can read existing state.
- Only `cz.vpsfree/containers/discourse` is affected; no coordinated node or
  fleet update is needed.
- NixOS documents `siteSettings` as defaults that UI/database settings override.
  Confirm plugin load ordering before relying on that mechanism.
- Declarative changes need activation of the Discourse container generation;
  UI changes apply at runtime. A stored override survives system rollback.
  Record the exact rollback action once the mechanism is selected.
- Keep dependency inputs and the Discourse package version unchanged. Building
  current configuration is distinct from activating any pending package updates.

## Testing plan

- Verify Overcommit installation and run required formatting hooks in
  `nix develop`.
- Inspect exact pinned sources and check the resulting setting/configuration.
- Run required review after the implementation commit and quick checks.
- Run `nix develop -c confctl build --yes cz.vpsfree/containers/discourse`
  if a declarative change is chosen.
- Runtime verification must distinguish generated defaults, stored database
  overrides, and the effective setting. Do not claim a live change from a
  successful evaluation/build alone.
