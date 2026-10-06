# Outage labels and wire rename

## Goal

Rename outage report type wire values in vpsAdmin and its consumers:

- `maintenance` -> `planned_outage`
- `outage` -> `unplanned_outage`

English user-facing text should use "planned outage" and "unplanned outage".
Czech wording remains unchanged: `odstavka`/`vypadek` wording in existing
Czech texts must continue to render as before.

Also improve impact presentation while keeping impact wire values unchanged.

## Affected repositories

- `vpsadmin`
- `vpsf-status`
- `vpsfree-irc-bot`
- `vpsfree-mail-templates`
- `web`
- `vpsfree-cz-configuration`

## Compatibility

vpsAdmin stores outage type as an integer enum. The implementation will change
the enum names using an explicit mapping, so existing rows keep their stored
integer values and are exposed with the new names.

The API will not accept old type names after the change. Dependent services
must be deployed with the vpsAdmin update so they use `planned_outage` and
`unplanned_outage`. Local downstream caches/history may normalize old values
only to render old local data safely.

Impact values remain unchanged on the API and in stored data. Only presentation
changes.

## Deployment notes

Update `vpsfree-cz-configuration` after dependent code commits exist:

- flake inputs for vpsAdmin, vpsf-status, and web
- `packages/vpsfree-irc-bot/default.nix` source rev/hash

No vpsfree-mail-templates source pin was found in vpsfree-cz-configuration.

## Testing

- vpsAdmin outage/outage_update specs and focused web UI regression/tests
- vpsf-status `go fmt ./...` and `go test ./...`
- vpsfree-irc-bot Ruby syntax check
- vpsfree-mail-templates ERB/meta syntax checks
- web text verification
- vpsfree-cz-configuration targeted `confctl build` where feasible
