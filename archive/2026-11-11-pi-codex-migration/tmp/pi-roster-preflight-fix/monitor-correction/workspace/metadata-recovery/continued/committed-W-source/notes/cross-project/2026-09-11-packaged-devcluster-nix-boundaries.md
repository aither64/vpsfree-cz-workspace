# Packaged development clusters need Nix startup checks

In the September 11 provider package, both cluster helpers passed their Ruby
status/ownership tests and packaged `--help` checks but failed before VM startup.
`nix eval --impure ... path:<packaged-provider>#cluster-config.drvPath` exposed
removed `default-config.json` references. Evaluating `#runner.drvPath` exposed
`../lib` outside the nested flake's copied source root (`'lib' is too short to be
a valid store path`). The files' presence elsewhere in the outer package does
not make them available inside a nested flake snapshot.

Keep host defaults supplied by `siteConfig`, and either install actual default
and shared-library files inside each packaged flake or give the flake explicit
immutable inputs. `--impure` alone does not repair the source boundary.

The vpsAdminOS provider additionally needs the current OS overlay function
called with `netlinkrb`/`ruby-lxc` inputs and `vpsadminosRubyGemConfig` passed to
its runner bundle. Missing the latter surfaces as a missing `sha256`, because
source-built gems intentionally have no download hash in the generated gemset.

Temporary repaired copies evaluated both configurations and built/loaded both
runners. The existing suite still passed unchanged (46 tests, 516 assertions),
showing why packaged Nix output and runner-load checks must complement it.
These probes do not establish live VM startup/update/restart correctness.

The same investigation found `devcluster_with_lock` calling its callback in
an `if`, which disables Bash `set -e` throughout nested callback execution.
An injected failing command followed by a marker returned success. Start/build
boundaries need explicit failure propagation, including when a previous
`result-config` exists. Preserve callback environment exports and locking when
repairing this; moving callbacks into a subshell changes those semantics.

Related investigation and repair options:
`work/2026-09-11-devcluster-packaging-investigation/investigation.md`.

The organization extension has no default devShell/package. Run focused tools
with `nix shell --inputs-from . nixpkgs#ruby nixpkgs#nixfmt -c ...` to use its pin.
For rendered `pkgs.writeText` JSON, return `{ drvPath = config.drvPath;
text = config.text; }` via `nix eval --json --apply ...` and decode text in the
caller. `builtins.fromJSON config.text` fails when the text carries store-path
context, even though it is valid JSON. For configuration-override checks, bridge
link and node SSH forwarding ports are used by both providers; vpsAdmin's node
memoryMiB currently changes seed capacity but its VM memory is hard-coded.
