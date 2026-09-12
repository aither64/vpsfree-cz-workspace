# Verify core and plugin migration versions separately

A live schema probe using `SELECT MAX(version) FROM schema_migrations` returned
`20260905180000-payments` instead of expected core version `20260831220000`.
Both migrations were installed correctly: plugin versions share the table and
append the plugin name, so the newest plugin can sort after the newest core.

For a core-only version check, filter `WHERE version NOT LIKE '%-%'`. Verify
relevant plugin migration IDs separately, and check the actual schema feature
when appropriate. The corrected password-reset probe confirmed both the core
version and the payments created_at index. No migration or database reset was
needed.

Related: `work/2026-08-18-vpsadmin-password-reset/state.md`, September 12.
