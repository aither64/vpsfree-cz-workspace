# Update HaveAPI to 0.29.5 and prepare vpsAdmin 4.2.0

## Summary

- update every active vpsAdmin Ruby consumer from HaveAPI 0.29.4 to 0.29.5
- refresh the Ruby/Nix, PHP/Composer, and bundled JavaScript artifacts from
  the published 0.29.5 releases
- prepare vpsAdmin and its first-party components as version 4.2.0, including
  the accumulated vpsadmin-client fixes
- keep packaged local-gem pins synchronized in the version task

HaveAPI 0.29.5 fixes localized choice conversion in generated clients. This
allows operations such as `vpsfreectl snapshot download` to submit the selected
snapshot ID instead of the localized display label.

## Compatibility

This changes client dependencies and generated package metadata only. It does
not change the vpsAdmin API contract, database schema, persistent state, or
service protocol, so components can be updated incrementally and rolled back
without data migration.

## Verification

- repository pre-commit and commit-message hooks
- dependency regeneration is idempotent
- vpsadmin-client specs: 23 examples, 0 failures
- WebUI PHPUnit: 82 tests, 332 assertions
- WebUI Composer install/validation with HaveAPI client 0.29.5
- syntax checks for both bundled HaveAPI JavaScript clients
- Nix builds of `libnodectld`, `nodectl`, and `nodectld` at version 4.2.0

A standalone change review found stale 4.1.0 pins in the three node package
Gemfiles. The pins, generated lockfiles, and version task were corrected before
submission.
