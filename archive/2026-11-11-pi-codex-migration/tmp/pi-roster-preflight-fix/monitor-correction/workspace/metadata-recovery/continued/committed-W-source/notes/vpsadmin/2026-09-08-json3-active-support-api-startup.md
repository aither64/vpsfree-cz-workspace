# JSON 3 prevents ActiveSupport 8.1 API startup

Fresh CI dependency resolution and the scheduled packaged API dependency
update selected JSON 3.0.1. API topic specs and i18n health failed before
examples ran: ActiveSupport 8.1.3.1 calls `JSON.parse(json, options)`, but
JSON 3 removed the second positional argument. Retained development locks
using JSON 2.21.2 hid the failure locally.

Constrain `json` below 3 in the API Gemfile and regenerate API package metadata
with `nix develop .#vpsadmin -c rake vpsadmin:gems:api`. Verify a fresh local
lock resolution, API startup/specs, i18n, and exact-head CI. Remove the bound
only once the owning ActiveSupport version supports the new JSON interface.

Initial evidence: vpsAdmin runs 34274171719 and 34274171547. Related initiative:
`work/2026-08-18-vpsadmin-password-reset/`.
