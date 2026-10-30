# Profile mount resource-page assertions

The failed quick batch tested exact head
`a0c78d1c0e5ef84b5e746d9bba4bc51830c77139`, tree
`3c62ce89c1ac356116aef9c59cf34398bd3130bf`. Its original receipt/logs remain
unchanged in `../quick-packaging-a0c78d1c/`.

Both failures requested `/mounted/api/v1/`, and the recorded HTML explicitly
had `data-page="overview"`. The tests expected an action's localized description
and privileged sample on that page. The accepted UI contract renders init/client
content on the overview and action samples on `?resource=widget`; the failures
were stale assertions rather than a profile or authorization regression.

Only `servers/ruby/spec/client_examples/profile_mount_spec.rb` changed:

- The existing request helper accepts an optional resource selector, retaining
  mounted URLs, explicit identity and locale headers.
- Overview requests still check initialization, dynamic/generated client panels
  and configured package identities, with no private sample disclosure.
- Resource requests check admin sample presence, member private field/action/
  sample absence, localized action descriptions and exact filtered adapter input.
- Both simple and thorough adapter contexts are checked for the actual samples.

All original private-schema omission, adapter initialization-count, filtered
sample, version-URL and locale assertions remain covered. No production source,
input lock, auth behavior or package metadata changed. The narrow patch belongs
in history group C because it adapts integration coverage to resource-page UI.

Focused command from the HaveAPI root:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop --command bash -euc '
  make doc
  cd servers/ruby
  export BUNDLE_GEMFILE="$PWD/Gemfile"
  bundle exec ruby -I../../clients/ruby/lib -I../../clients/typescript/lib \
    -S rspec spec/client_examples/profile_mount_spec.rb \
    --seed 50232 --format documentation
'
```

Observed result: **7 examples, 0 failures**, seed 50232; examples took
0.514 seconds and load took 1.00 second. The declared Nix shell restored its
existing tool paths from binary caches before running; no dependency graph was
refreshed. After correcting one test-only argument-alignment offense, the final
focused `bundle exec rubocop servers/ruby/spec/client_examples/profile_mount_spec.rb`
passed with one file and no offenses. `git diff --check` passed.

Exact uncommitted patch is retained as `profile-mount-route-fix.patch`.
No Git mutation/hooks, broad suites, package build, exports, live preview,
OAuth/TLS or integration gate ran. No verification process remains active.
