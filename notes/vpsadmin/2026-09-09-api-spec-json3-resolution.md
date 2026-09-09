# API specs can resolve incompatible JSON 3 in a fresh development shell

Related initiative: `work/2026-09-09-vpsadmin-pr-43`.

Command: `nix develop .#api -c bundle exec rspec ...` in a fresh worktree.
The untracked development `api/Gemfile.lock` was absent, so Bundler resolved
JSON 3.0.2 together with ActiveSupport 8.1.3.1. Loading `spec_helper` failed
before examples: `JSON.parse: wrong number of arguments (given 2, expected 1)`.
ActiveSupport JSON decoding supplies the options hash positionally, whereas
that JSON release expects keyword arguments.

For review against the committed packaged dependency set, seed the ignored
lockfile with `cp packages/api/Gemfile.lock api/Gemfile.lock`, then reenter
`nix develop .#api`. The packaged lock selects JSON 2.21.2; Bundler installs
the recorded 2.7.2 version if necessary. The rerun passed 20 payment examples
and one isolated migration example. A later combined run passed all 27 payment
and boundary-probe examples. This changes no tracked dependency files.
