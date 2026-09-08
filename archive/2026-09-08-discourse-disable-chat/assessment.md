# Discourse chat configuration

Use the existing declarative site settings to record that chat should be off:

```nix
services.discourse.siteSettings.chat.chat_enabled = false;
```

The change is committed as `7cfe38378a1b40952b8019cd895942cda7c32233` on
`2026-09-08-discourse-disable-chat` in `vpsfree-cz-configuration`.

| Choice | Takes effect | Persists in | Role |
| --- | --- | --- | --- |
| NixOS `siteSettings` | After activation and Discourse restart | Git and the generated configuration | Default for this deployment |
| Discourse admin UI | At runtime | Discourse database | Immediate change; overrides the NixOS default |

NixOS explicitly documents `siteSettings` as defaults that the UI can
override. This means a saved `chat_enabled = true` would keep chat enabled
after deployment. The UI setting persists across restarts; it is not a
temporary toggle. [NixOS Discourse module](https://github.com/NixOS/nixpkgs/blob/a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4/nixos/modules/services/web-apps/discourse.nix)

The pinned Discourse 2026.7.1 source loads plugin defaults before the NixOS
defaults. Its bundled chat plugin defines `chat_enabled` with a default of
`true`. The NixOS patch therefore applies the configured `false` value after
the plugin default. The generated pre-start script contains
`"chat":{"chat_enabled":false}`. The setting controls the bundled chat
feature; it does not remove the plugin or delete its data.
[Discourse chat settings](https://github.com/discourse/discourse/blob/v2026.7.1/plugins/chat/config/settings.yml),
[NixOS defaults patch](https://github.com/NixOS/nixpkgs/blob/a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4/pkgs/servers/web-apps/discourse/nixos_defaults.patch)

For deployment:

1. Integrate the feature commit, then build and activate
   `cz.vpsfree/containers/discourse` through the normal confctl workflow.
2. In Discourse Admin settings, search for `chat enabled` and ensure it is
   disabled. If a saved true override exists, disable it or reset it after
   the declarative default is active.
3. Refresh an authenticated browser and verify that chat is unavailable.

For an immediate disable before deployment, turn off `chat enabled` in the
admin UI. Keep the declarative change for subsequent deployments.

The configuration change has no schema or format migration. Reverting it
restores the old default, but a false value saved through the UI still wins;
change or reset that UI value to re-enable chat. Existing retention settings
are unchanged. Discourse pauses scheduled deletion of old chat messages while
chat is disabled. Re-enabling chat resumes that cleanup, so check retention
settings first and back up messages that need to remain available.

Live state remains unverified: SSH authentication to the Discourse host was
denied, so this session has not read or changed the production setting. See
`state.md` for the current review and build results.

Formatting hooks, Nix parsing/evaluation, and all required review lanes
completed without blocking findings. The full targeted confctl build passed
and produced generation `2026-09-08--12-12-59`. The user then requested merge
and cleanup. Commit `7cfe3837` was fast-forwarded into `master` and pushed;
hooks and the full build passed again from the merge worktree with generation
`2026-09-08--12-32-49`. Production activation remains a separate operator step.
