# Separate core schema dumping from full API locale generation

During `work/2026-10-05-network-ipv4-left-counter`, schema generation and
`rake vpsadmin:i18n:update` ran in the same `VPSADMIN_PLUGINS=none` API shell.
The core schema dump was correct, but locale generation removed unrelated
plugin labels and descriptions from both committed language catalogs.

Use core-only mode for `api/db/schema.rb` as repository instructions require.
Use the full plugin environment for the complete API locale catalogs. Inspect
the generated diff rather than accepting a zero exit as proof that its scope
is correct. Restore only the affected owned catalogs from their exact baseline,
reapply intended translations, and regenerate in the correct mode; preserve
unrelated changes. Do not rerun a one-off migration/schema script against its
already-migrated dump merely to repeat locale generation.

The original generator exited zero. The lead rejected its locale output after
diff inspection; recovery and locale health verification are tracked in the
initiative state.
