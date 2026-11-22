# Run WebUI commands relative to `webui/` in the component shell

## Symptom

Running `nix develop .#webui -c webui/lang/scripts/locales-update` from the
vpsAdmin repository root failed with a doubled `webui/webui/...` path.

## Cause

The `.#webui` development shell changes its working directory to the
repository's `webui/` directory before executing the requested command.

## Workaround

Pass paths relative to `webui/`, for example:

```sh
nix develop .#webui -c lang/scripts/locales-update
nix develop .#webui -c vendor/bin/phpunit tests/Regression/ExampleTest.php
```

Install PHP dependencies with `nix develop .#webui -c composer install` when
`vendor/` is absent.

## Verification

The corrected locale update command regenerated the gettext catalogs, and the
component-shell PHPUnit command ran the focused regression test.

Related initiative:
`work/2026-08-03-webui-dataset-used-czech-fix/`.
