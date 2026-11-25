# Final history reconstruction

Execute only after owner4 returns a clean source/index and all owners are terminal.
Use ordinary Git in the registered worktree; no reset/stash/clean, default movement
or publication. Preserve exact final tip/tree under a new review ref first.

Rebuild on a temporary feature branch from537b0b7c4ce1d8a930c5fd24b8f4317271ae4f02,
then return the original registered feature branch to the reconstructed tip. Partition
the complete base-to-final changed path set exactly once:

1. Existing independent fixture lease/isolation behavior and documentation:
   api/spec/support/app_helper.rb,
   api/spec/api/routes/transactional_fixture_connection_spec.rb,
   tests/README.md. Restore final bytes, ordinary commit/hooks.
2. Final generic incident backend, original migration/core schema, typed API,
   incident producers/templates, focused specs and reference docs/CI selection.
   Restore final bytes directly; no abandoned callback/Unknown/additive migration
   ever enters this reconstructed series. Exclude groups1/3/4. Ordinary commit/hooks.
3. All webui paths, incident Playwright scenario and tests/suite/webui.nix fixture:
   final generic Incidents page/forms/alerts. Ordinary commit/hooks.
4. Password-recovery CS/EN HTML only: exact H styling purpose/patch. Ordinary hooks.

Use `git restore --source=<preserved-final> -- <explicit owned partition>` and stage
only that partition. Restore deletions from the final tree as needed. Compare the
full changed-path union/partition with the final diff before committing. Prove final
full tree equals preserved final tree and H final patch equals f746..4f391 H patch.
Record old/new whole series and migration provenance. Do not repeat unchanged quick
checks for a tree-identical history change; declared hooks still run normally.

A source mismatch or failed hook remains owned and is reconciled before proceeding.
Do not hand G3 a moving/intermediate revision. No merge/release/lifecycle authority.
