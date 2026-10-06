# Keep declared exclusions in explicit-file RuboCop checks

During `work/2026-10-05-network-ipv4-left-counter`, a scoped RuboCop command
passed every changed Ruby filename explicitly. RuboCop inspected the generated
`api/db/schema.rb` despite its exclusion in the root configuration and reported
thousands of unrelated formatting offenses.

Use `bundle exec rubocop --force-exclusion ...` when supplying explicit changed
paths. Keep a separate `ruby -c` check for the generated schema. Do not format
the dump or weaken lint rules to compensate for the command's file selection.
The corrected scoped check inspected 34 files without offenses; the schema
retained its generated form.
