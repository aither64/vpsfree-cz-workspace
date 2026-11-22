# OSVM RSpec Shell

Related initiative: `work/2026-05-30-dev-vpsadmin-clusters`.

Symptom:

- `nix develop .#test-runner --command bundle exec rspec
  osvm/spec/osvm/machine_config_spec.rb` used Ruby 3.3.10 and failed to solve
  the bundle because the local `osvm` gem requires Ruby 3.4.0 or newer.
- Running from `osvm` in the default development shell reached RSpec but failed
  to load `libosctl/native`.

Workaround:

Use the `vpsadminos` development shell, install the `osvm` bundle, build the
`libosctl` native extension as the CI helper does, and run the spec from the
`osvm` directory:

```sh
nix develop .#vpsadminos --command bash -lc '
set -euo pipefail
export BUNDLE_GEMFILE="$PWD/osvm/Gemfile"
export BUNDLE_PATH="$PWD/.gems"
if [ ! -f libosctl/lib/libosctl/native.so ]; then
  (cd libosctl/ext/libosctl && ruby extconf.rb && make && cp native.so ../../lib/libosctl/native.so)
fi
cd osvm
bundle install >/dev/null
bundle exec rspec spec/osvm/machine_config_spec.rb
'
```

Verification:

- `spec/osvm/machine_config_spec.rb`: 18 examples, 0 failures.
