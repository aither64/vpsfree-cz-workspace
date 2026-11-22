# libnodectld shared gem cache can contain truncated gems

Related initiative:
`work/2026-07-13-security-advisory-automation`.

## Symptom

`nix develop .#libnodectld --command bundle exec rspec` loaded the suite, but
existing examples failed with `LoadError` for RSpec built-in matcher files.
Inspecting `/tmp/dev-ruby-gems` also found missing Bundler files such as
`lib/bundler/env.rb` and `lib/bundler/cli/show.rb`.

## Cause

The shared `/tmp/dev-ruby-gems` directory contained incomplete gem trees even
though Bundler initially reported the bundle as installed. This was a
development-cache failure, not a product test failure.

## Fix

After confirming that no bundle or Ruby process was using the cache, preserve
it under a timestamped backup and let the declared development shell rebuild
it:

```sh
pgrep -af '/tmp/dev-ruby-gems|bundle|ruby' || true
mv /tmp/dev-ruby-gems \
  /tmp/dev-ruby-gems.incomplete-YYYYMMDDHHMMSS
nix develop .#libnodectld --command bundle exec rspec
```

## Verification

The clean cache rebuild completed the full libnodectld suite with 419 examples
and no failures.
