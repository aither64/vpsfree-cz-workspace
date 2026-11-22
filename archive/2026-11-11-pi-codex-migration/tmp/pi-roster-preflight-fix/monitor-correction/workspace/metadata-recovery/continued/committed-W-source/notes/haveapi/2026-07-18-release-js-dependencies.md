# HaveAPI release requires local JavaScript dependencies

Initiative: `work/2026-07-13-security-advisory-automation`

`nix develop --command make release` can fail at the final gulp step with
`./node_modules/.bin/gulp: No such file or directory`. The top-level Nix shell
provides Node.js but does not install `clients/js` dependencies, and that
component has no lockfile.

Run `nix develop --command npm install --prefix clients/js --no-package-lock`
before the release target. This creates only ignored local dependencies and
does not add a generated package lock. Re-running `make release` then builds
all three gems and the JavaScript distribution successfully.
