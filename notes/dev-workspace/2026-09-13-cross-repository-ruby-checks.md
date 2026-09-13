# Run workspace Ruby tests outside configuration's Bundler shell

Running `ruby ../workspace/test/deployment_contract_test.rb` from the
configuration repository's `nix develop` failed to load `minitest/autorun`.
That shell uses the configuration project's Ruby/Bundler environment, which is
not the workspace test environment. Run `nix shell nixpkgs#ruby -c ruby
test/deployment_contract_test.rb` from the workspace feature worktree instead.
The suite passed with 3 runs and 14 assertions. The actual deployment checker
itself ran successfully from the configuration shell.

Related initiative: work/2026-09-13-portal-file-links/.
