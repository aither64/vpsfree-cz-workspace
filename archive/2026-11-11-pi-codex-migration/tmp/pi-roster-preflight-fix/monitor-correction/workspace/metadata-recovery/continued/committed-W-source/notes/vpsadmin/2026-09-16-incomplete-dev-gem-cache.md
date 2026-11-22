# Incomplete shared libnodectld gem cache

`nix develop .#libnodectld -c bundle exec rspec ...` reported installed gems,
then failed loading ActiveRecord and RSpec files. The shared `/tmp/dev-ruby-gems`
had gem metadata/directories but was missing library files. Bundler therefore
considered the cache complete. Do not alter a shared cache used by other sessions.

Use an initiative-specific temporary GEM_HOME/GEM_PATH/BUNDLE_PATH and install
Bundler plus the existing locked bundle there. Keep the shell's BUNDLE_GEMFILE,
VPSADMINOS_PATH and RUBYLIB; unset its stale RUBYOPT for the isolated installation.
The same three confirmation-engine specs passed with the isolated bundle. This
is an environment workaround, not a dependency or production-code change.

Related initiative: work/2026-09-09-ip-release-mechanism.
