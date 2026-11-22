# CHECK ordering in an ActiveRecord schema dump

In `work/2026-09-23-storage-redesign`, guarded core schema generation emitted
exactly the intended five audit columns and one changed CHECK, but its private
byte validator refused the dump. ActiveRecord 8.1.4 `SchemaDumper` sorts rendered
CHECK statements. Changing the owning CHECK text can therefore move it relative
to otherwise unchanged statements.

For a bounded schema comparison, extract exactly one named owning CHECK from
both predecessor and result before comparing all remaining table bytes and
order. Validate that CHECK and the intended columns separately, then reconstruct
the entire predecessor dump and require exact bytes. Do not accept a failed
validator's output merely because the migration exited zero.

The corrected private projection passed a fresh core-only generation with 180
unchanged tables, five audit columns and no unrelated schema changes. The first
failed result remains retained; no application, SQL or database-helper change
was needed.
