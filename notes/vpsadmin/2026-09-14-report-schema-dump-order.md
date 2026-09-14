# Preserve existing order after a focused core schema dump

Related initiative: `work/2026-09-14-daily-report-sessions`.

A core-only ActiveRecord schema dump after adding four report indexes produced
326 changed lines because existing table, column, index, and foreign-key
declarations were not in the dumper's canonical order. The database schema
itself changed only by four indexes.

Load the committed core schema in an isolated test database, apply the new
migration, record its version, and dump through ActiveRecord::SchemaDumper.
Before committing, compare generated blocks against the original and restore
only declaration order when the sets of complete declarations are identical.
Keep generated definitions for the affected tables. This reduced the report
migration schema diff to the version and four index declarations.

Do not replace a database dump with hand-written schema changes, and do not
include unrelated schema reorderings in a focused migration commit.
