# Provider specs using the vpsAdmin API test helper

Run provider-owned ActiveRecord specs in the selected API's Nix shell, which
already enters `api/` and exports `VPSADMIN_REPO_ROOT`. Refuse an inherited
`DATABASE_URL` or configured database before loading the API helper/schema.

The API's `.rspec` automatically requires `spec_helper`. That helper starts a
disposable MariaDB and sets `DATABASE_URL` before RSpec loads a provider spec.
A second inherited-database guard at the top of that spec then rejects the
legitimate temporary database. The failed command ran zero examples.

For a provider spec that performs its own guarded, explicit helper load, use
RSpec's custom options file to prevent the automatic preload:

```sh
bundle exec rspec --options /dev/null --format documentation \
  /absolute/provider/test/vpsadmin_storage_profile_spec.rb
```

The locked RSpec 3.13.6 `ConfigurationOptions#file_options` selects the custom
file instead of project/local/global options. Keep the wrapper's preflight and
the spec's pre-helper guard; accepting arbitrary loopback database URLs is not
a substitute. Use the normal API automatic DB and a short private `TMPDIR`.

This correction reached all 15 semantic examples, exposing separate model-query
failures; it did not itself certify the profile. See the
[session evidence](../../work/2026-09-23-storage-redesign/state.md).

When delegating the wrapper, provide an exact argument vector or a separate
command block. Its remaining arguments are passed to RSpec. An accidental `.`
from command punctuation therefore adds the API directory and selects the
whole suite alongside the provider file. One such run was explicitly stopped;
retry the intended file alone after confirming its disposable DB exited.
