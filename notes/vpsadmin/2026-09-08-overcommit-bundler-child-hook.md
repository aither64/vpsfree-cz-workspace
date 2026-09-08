# Invoke Overcommit directly when hooks enter component bundles

Running `nix develop .#vpsadmin -c bundle exec overcommit --run` leaked the
root Bundler setup into the API i18n hook. The hook selected the API Gemfile
but failed to find the expected root RuboCop dependencies in its gem path.

Use `nix develop .#vpsadmin -c overcommit --run`. The normal Git hook already
invokes Overcommit directly; commits should likewise run as `git commit` in
the full shell. Every declared hook and the CI selector passed with this
invocation. No hook disable flag or code change was needed.

Related initiative: `work/2026-08-18-vpsadmin-password-reset/`.
