# Integration tests

The integration suite uses the vpsAdminOS test runner to boot a local vpsAdmin
cluster and a VM running the packaged `vpsf-status` service.

Useful commands:

```sh
./test-runner.sh ls
./test-runner.sh test status-page
./test-runner.sh test -t ci
```

The application and development shell use the root `nixpkgs` input. VM tests
use `vpsadminos.inputs.nixpkgs` in both `tests` and `testsMeta`, while the status
service package still comes from the application package set. The OS test
composition retains the package set from its upstream lock, so routine
application dependency updates do not change kernel derivations or bypass the
OS binary cache. Update the OS source and its locked dependencies together when
changing the test platform.

Use `./test-runner.sh test -t ci --verbose` to expose periodic per-test build
and execution output. CI captures both output streams in `test.log` and uploads
that log with the per-test logs on failure or cancellation. This distinguishes
package/image preparation from VM startup and test assertions.
