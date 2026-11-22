# Push from the root Nix shell when Overcommit versions differ

Related initiative: `work/2026-09-09-vpsadmin-pr-43`.

An ambient `git push` failed with "Signature of configuration file has
changed" even though commits and their hooks had passed and `.overcommit.yml`
and `.git-hooks/` were unchanged from the fetched base. The hook's Ruby loaded
ambient Overcommit 0.71.0; the repository root bundle used 0.73.0. The effective
configuration signatures differed between those versions.

Run `nix develop .#vpsadmin -c git push ...` so the hook uses the same version
and environment as commits. This succeeded without re-signing configuration,
disabling hooks, or changing code. To diagnose, inspect hook/config diffs and
compare `Gem.loaded_specs.fetch('overcommit').version` after requiring the gem
in each environment; the ambient executable may be absent from PATH even when
Ruby can load its gem.
