# Keep outer Bundler context out of Git hooks and Bundix

In a vpsAdmin Nix shell, use ordinary `git commit` and the documented
`rake vpsadmin:gems:<package>` tasks. Wrapping either in `bundle exec`
exports Bundler activation into their child Ruby processes.

Observed in the documentation repair session: `bundle exec git commit`
made the API i18n hook ask for the root bundle's older lint gems even though
the API bundle was installed and its ignored lock selected newer versions.
Plain Git ran all hooks successfully without changing or bypassing them.
Likewise `bundle exec rake vpsadmin:gems:api` polluted the Nix Bundix process
with root-bundle setup and failed with GemNotFound; plain Rake regenerated
all three affected closures successfully, with only the intended HaveAPI
version/hash changes.

Use each repository's Nix environment and declared hooks. Reinstalling the API bundle did not solve the leaked activation boundary.
Session: `work/2026-10-11-diagnose-vpsadmin-api-exception/`.
