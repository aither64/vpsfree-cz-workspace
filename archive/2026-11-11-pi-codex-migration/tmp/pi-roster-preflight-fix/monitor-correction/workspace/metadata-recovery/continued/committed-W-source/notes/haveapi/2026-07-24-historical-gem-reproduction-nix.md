# Reproducing historical HaveAPI gems in an ambient Nix Ruby

## Symptom

`gem install haveapi-client -v 0.26.5 --install-dir DIR` attempted to build the
newest `json` dependency and failed because the ambient Nix Ruby did not expose
a compiler toolchain to `mkmf`.

## Cause

Installing an old gem without a lock file resolves current transitive
dependencies. The historical HaveAPI code itself did not require the failed
native build, and a compatible `json` gem was already available in the ambient
Ruby environment.

## Workaround

Install the exact historical first-party gem into an isolated temporary gem
home with `--ignore-dependencies`, then run it with a `GEM_PATH` containing
both the isolated gem home and the known-working ambient gem paths. Confirm all
required dependencies load before trusting the reproduction.

Use separate Ruby processes when comparing versions, because RubyGems cannot
activate two versions of the same gem in one process.

## Verification

This method loaded exact `haveapi-client` versions 0.26.5 and 0.29.4 and
reproduced their different exception rendering against the same localized
production API description.

Related initiative:
`work/2026-07-24-vpsfreectl-snapshot-download-fix/`.
