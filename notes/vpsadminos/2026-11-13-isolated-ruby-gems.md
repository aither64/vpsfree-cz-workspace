# Isolate Ruby gems when the shared component cache has another ABI

In the start-diagnostics session, the component shell's shared
`/tmp/dev-ruby-gems` contained a `date` extension linked against Ruby 3.4.9,
while `.#osctld` selected Ruby 3.4.11. Bundler failed before tests ran.
Preserve the shared directory because other sessions can use it.

The repository's root `nix develop` provided a working patched Ruby 3.4.9.
Inside that environment, a session-owned gem directory supplied `GEM_HOME`,
`GEM_PATH` and `BUNDLE_PATH`; each component retained its own development
`BUNDLE_GEMFILE` and the shell's locked netlinkrb/ruby-lxc inputs. Unset
`RUBYOPT` before preparing that bundle. Compile libosctl, osctld and ruby-lxc
with that same Ruby using the native preparation steps in
`.github/workflows/scripts/run-rspec-all.sh`. Keep the hook environment separate.
Focused daemon and CLI checks then passed (236 and 40 examples).

Evidence: `work/2026-11-13-osctld-start-recovery-errors/` and its package A
reports. This was environment preparation, with no dependency or shell edits.

Run feature pushes through the declared root Nix environment as well. An ambient
Git push refused the Overcommit trust signature, while `nix develop --command git
push ...` used the prepared trusted hook environment and passed without bypass.
