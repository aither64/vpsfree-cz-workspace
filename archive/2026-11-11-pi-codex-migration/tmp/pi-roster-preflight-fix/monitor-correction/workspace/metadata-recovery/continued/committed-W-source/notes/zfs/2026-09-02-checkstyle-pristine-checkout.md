# OpenZFS checkstyle needs a generated Makefile

## Symptom

Running `make checkstyle` in a pristine OpenZFS checkout fails with
`No rule to make target 'checkstyle'` even though `Makefile.am` declares it.

## Cause

The repository does not track the generated top-level `Makefile`. The documented
target is available only after running the autotools/configure setup.

## Workaround

Before a configured build is available, run the checks relevant to changed
source directly, including `scripts/spdxcheck.pl`, `scripts/cstyle.pl -cpP` for
changed C/header files, and `scripts/commitcheck.sh` for committed changes. Run
the complete `make checkstyle` target from the configured build afterward.

Verified while working on
`work/2026-09-02-vpsadminos-chattr-test`.
