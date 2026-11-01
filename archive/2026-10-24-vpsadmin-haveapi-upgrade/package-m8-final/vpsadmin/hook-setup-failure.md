# Mandatory hook setup failure

First quick/commit operation exited1 before any commit/rewrite. Ruby syntax,
Nix parse/format and RuboCop passed. MigrationSpecs/Nixfmt/WebuiI18n/RuboCop hooks
passed, but VpsadminApiI18n could not load new511 checkout from the retained
local API development bundle: Bundler::GitError/PathError, not yet checked out.
Exact original quick-commit.log/exit preserved. Tracked source and staged four
metadata paths remain intact, head2a4 unchanged. No native test/build/guest started.

Resolve with the repository's normal `nix develop .#api` bundle installation,
assert both full locks unchanged, then retry only ordinary commit/consolidation
with all mandatory hooks. No source or hook bypass.
