# Verifying a reconstructed API commit series

Initiative: work/2026-09-09-ip-release-mechanism.

Run migration specs in a separate RSpec process from ordinary model/API specs.
`spec/migration_helper.rb` installs global before-suite and before-example
hooks that switch databases and reset all tables; combining it with
`spec_helper` invalidates model fixtures. A mixed invocation was interrupted
and replaced by sequential, separate RSpec commands. The campaign migration
then passed both directions and uniqueness checks (2 examples, seed 533).

Use `VPSADMIN_PLUGINS=none` for core schema/model checks, but leave it unset
when regenerating the full API translation catalog. A core-only i18n update
removes plugin keys. Restore the intended catalog from the index before the
full update so removed translations are retained. Full regeneration restored
the expected feature-only catalog diff.

When passing changed files explicitly to RuboCop, use `--force-exclusion` or
exclude db/schema.rb from the list. Explicit paths bypass the normal generated
schema exclusion and auto-correction can rewrite the entire schema. Restore
the resolved schema from the index; do not commit that formatting churn.

An Overcommit signature refusal can also occur on rebase or restore while
other worktrees share the hook signature state. Verify the hook configuration
against the intended target, then sign and run the operation in the root Nix
shell. Do not bypass hooks. The six prerequisite commits rebased cleanly after
signing the unchanged configuration.

The lightweight SpecSeed IP resources use numeric defaults. A test of
EnvironmentUserConfig.free_resources dispatch must set the tested resource to
resource_type: :object with free_chain: 'Ip::Free', matching the production
migrations. Otherwise the usage is freed without invoking IP cleanup, and a
dependency test misleadingly reports missing ownership confirmations.
Cross-environment migration fixtures also need a real DatasetInPool diskspace
usage row: OsToOs transfers that mandatory resource and expects a nonempty
result. Initialize it with the ordinary resource provider before firing the chain.
