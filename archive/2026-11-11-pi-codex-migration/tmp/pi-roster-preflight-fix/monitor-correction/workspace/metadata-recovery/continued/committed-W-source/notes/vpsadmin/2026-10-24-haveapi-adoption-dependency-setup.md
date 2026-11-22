# HaveAPI dependency update setup

In session `work/2026-10-24-vpsadmin-haveapi-upgrade`, the repository-local
HaveAPI updater could not run even with `--skip-bundix`: root discovery required
removed `tools/bundix_all.sh`. Its intended four source declarations were updated
directly, then the current scoped `rake vpsadmin:gems:{api,client,download_mounter}`
tasks regenerated metadata. Consult current testing.md/task definitions before
using the old updater. No compatibility script was added.

Use plain `rake` in the root Nix shell for those tasks. `bundle exec rake`
leaked root Bundler settings into Bundix's isolated Ruby wrapper and failed with
GemNotFound after the task deleted its generated API lock. Reconcile actual
files and rerun the owning task; do not interpret missing lock as successful
regeneration. Plain Rake regenerated consistent locks/gemsets with only the
required HaveAPI and generator transitive changes.

The 0.30.1 Rust documentation generator adds native Fiddle. The API development
shell needs libffi and pkg-config; the pinned Nixpkgs packaged Ruby environment
already supplied libffi via defaultGemConfig. Verify the actual derivation before
adding a redundant package override. Existing non-Nix API CI dependency lists
also need libffi-dev/pkg-config. After the narrow shell fix, real loads of both
generator adapters and Fiddle passed with all HaveAPI gems at0.30.1.

Composer2nix requires a root package name for this legacy UI. Supplying the
existing `vpsadmin-webui` identity via `--name` regenerates dependency integrity
metadata without changing composer.json's unrelated metadata or composer-env.nix.

Evidence: `work/2026-10-24-vpsadmin-haveapi-upgrade/package-a/receipt.md`.

The same root Bundler leak affects `bundle exec overcommit --run`: it can
select all repository paths and pass root gems into API hooks. Use ordinary
`git commit -F` from a fresh root `nix develop` so declared hooks select the
component environment; do not wrap Git/Overcommit in the outer bundle.
