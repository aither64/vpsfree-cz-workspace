# vpsAdmin CI path-flake disk image churn

## Symptom

A full vpsAdmin integration run can fill a roughly 500 GiB Nix store even when
all reported GC roots are live and workflow `/tmp` usage is small.

## Cause

The test framework evaluates each test with a path-valued
`builtins.getFlake`. vpsAdmin CI writes a growing `test.log` and selector files
inside that path, and the vpsAdmin package source filter does not exclude them.
Repeated test evaluations can therefore produce different `vpsadmin-source`
derivations during one workflow.

NixOS test machines compound the churn by including the logical test name in
the raw base-image derivation. Tests with otherwise identical services machine
configuration therefore build separate approximately 3.3--3.9 GiB physical
store outputs. Per-test config output links retain completed tests' images until
the whole workflow cleans its state.

## Evidence

- A canceled-run artifact contained 19 distinct disk-image derivations after
  19 tests had started and 23,301 closure-copy log entries.
- Fourteen of those tests built distinct `vpsadmin-source-unknown`
  derivations.
- Full CI selected 118 tests.
- Host evidence showed about 6.2 GiB in `/tmp` but about 550 GiB used on the
  filesystem containing `/nix/store`.

## Fix direction

Keep all workflow scratch and live log files outside the checked-out flake,
then make NixOS base-image identity depend on machine content rather than the
logical test name. Verify identical configurations share an image and record
peak store growth in a full run. Releasing completed-test config output links is
useful, but runner-wide GC is intentionally deferred while a job is active.

## Verification

After moving workflow scratch outside the flake and making the image name
stable, a deliberately partial CI run started 40 tests and completed 36. Its
logs contained one `vpsadmin-source-unknown` derivation, seven distinct NixOS
disk-image derivations, and 9,005 closure-copy entries. This is a large
reduction from the pre-fix sample's 14 source derivations, 19 images, and 23,301
copy entries after only 19 started tests. The reviewed vpsAdminOS head also
passed its complete GitHub Actions CI workflow.

## Related initiative

`work/2026-08-03-gh-runner-gc/`
