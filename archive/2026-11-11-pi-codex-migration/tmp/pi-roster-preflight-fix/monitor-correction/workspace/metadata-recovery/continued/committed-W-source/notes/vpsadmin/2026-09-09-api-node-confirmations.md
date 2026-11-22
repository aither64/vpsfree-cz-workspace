# Checking API-built chains with the node confirmation engine

Initiative: work/2026-09-09-ip-release-mechanism/confirmation-check.rb.

The API and libnodectld have separate Bundler environments. For a focused check
that builds real API chains and applies NodeCtld confirmations to the same test
MariaDB connection, use a temporary Gemfile that eval_gemfile's api/Gemfile and
adds libosctl from VPSADMINOS_PATH/libosctl. Install it with BUNDLE_PATH pointing
to the API's ignored .gems directory. Run in nix develop .#libnodectld, which
provides RUBYLIB for the native libosctl extension; the root shell alone fails
with `cannot load such file -- libosctl/native`. No project dependency change is
needed for this one-off cross-component check.

Use NodeCtld::DbTransaction with the raw ActiveRecord MySQL connection so both
components see the example transaction. Temporarily set its query_options[:as]
to :hash for NodeCtld, then restore the entire original options hash before
returning to ActiveRecord. Leaving :hash enabled makes ActiveRecord materialize
nil fields, producing misleading ownership and NOT NULL failures. This is a
harness issue, not a database rollback failure.

Verification: the initiative's actual API/NodeCtld confirmation and close-chain
check passes execute success, execute failure and rollback, including preserved
ownership/quota, restored DNS/PTR/host records, manual retry and final audit.

The component shell sets BUNDLE_GEMFILE and BUNDLE_PATH in its shell hook.
Export the temporary combined Gemfile and API .gems path inside the shell's
`bash -c` command, after that hook, then run bundle install and RSpec from api/.
Passing them only before nix develop was overwritten and loaded the libnodectld
bundle, causing `cannot load such file -- rack/test`. With the post-hook exports,
the rebuilt series passes all 12 confirmation/rollback cases (seed 63630).
