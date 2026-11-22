# Run PHP client integration tests from the HaveAPI tree

Initiative:
`work/2026-06-15-vpsadmin-events/`

## Symptom

Running `vendor/bin/phpunit` directly in a standalone
`haveapi-client-php` worktree failed in `ClientIntegrationTest` with
`Test server exited early` and no subprocess output.

## Cause

`tests/bootstrap.php` locates the Ruby integration server relative to the
monorepo layout. From `haveapi/clients/php`, walking three parents reaches the
HaveAPI root and finds `servers/ruby`. The same calculation from the standalone
mirror reaches the initiative worktree directory, where no `servers/ruby`
exists.

## Workaround

Run the complete PHP suite in the canonical `haveapi/clients/php` tree, then
verify that the standalone mirror is checksum-identical while excluding local
dependency and cache files:

```sh
rsync -nrc --delete --itemize-changes \
  --exclude '.git' --exclude '.git/' --exclude 'vendor/' \
  --exclude 'composer.lock' --exclude '.phpunit.result.cache' \
  haveapi/clients/php/ haveapi-client-php/
```

For the 0.29.7 release, the canonical suite passed with 51 tests and 144
assertions, and the mirror comparison reported no differences.
