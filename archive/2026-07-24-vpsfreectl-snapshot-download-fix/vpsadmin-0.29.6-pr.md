## Summary

- update every vpsAdmin HaveAPI consumer to the coordinated 0.29.6 release
- refresh Ruby, Composer, Nix, and bundled JavaScript dependency artifacts
- prepare the shared 4.2.1 version and vpsadmin-client changelog

## Compatibility

This is a client dependency update with no API wire, database, persisted-state,
or server deployment change. HaveAPI 0.29.6 is already public. The standalone
vpsadmin-go-client repository is intentionally unchanged.

## Verification

- all configured Overcommit hooks
- vpsadmin-client: 23 examples, 0 failures
- WebUI: 82 tests, 332 assertions
- repeated version and package generation is clean
- both bundled JavaScript clients match the HaveAPI 0.29.6 artifact
- isolated gem install loads vpsadmin-client 4.2.1 with haveapi-client 0.29.6
- temporary Go client generated from the live API builds and tests
