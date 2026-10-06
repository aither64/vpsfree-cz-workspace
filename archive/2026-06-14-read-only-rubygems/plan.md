# 2026-06-14-read-only-rubygems

## Goal

Make the Geminabox service on `rubygems.int.vpsfree.cz` read-only. Existing
gem files must remain available to RubyGems/Bundler clients, but new gem
uploads should be rejected. The gem garbage-collection service can be disabled.

## Affected repositories

- `vpsfree-cz-configuration`

## Approach

- Change only the `cz.vpsfree/containers/int.rubygems` configuration unless the
  local Geminabox module needs a reusable option.
- Use Geminabox's built-in `allow_upload = false` setting, while keeping
  `allow_replace = false` and `allow_delete = false`.
- Disable `services.geminabox.garbage-collector` for the container and remove
  the now-unused GC scripts from this host configuration.

## Compatibility and deployment

- Existing gems under the Geminabox state directory remain in place and are
  still served over HTTP.
- Clients that resolve/install gems continue to use GET/HEAD endpoints. Upload
  clients using `/upload` or `/api/v1/gems` will receive a rejection from
  Geminabox after deployment.
- Disabling the GC service stops moving old gems to the trash directory. It does
  not delete or migrate persisted state.
- Rollback is straightforward: restore `allow_upload = true`/remove the setting
  and re-enable the GC service. Mixed-version operation is not relevant because
  this is a single container service behind the proxy.

## Testing plan

- Format changed Nix files with `nixfmt`.
- Evaluate/build `cz.vpsfree/containers/int.rubygems` with `confctl build`.
