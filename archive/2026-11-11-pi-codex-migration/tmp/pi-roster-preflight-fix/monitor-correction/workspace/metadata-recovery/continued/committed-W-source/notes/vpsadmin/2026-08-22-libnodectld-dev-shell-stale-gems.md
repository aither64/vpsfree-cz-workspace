# libnodectld development shell can reuse an incomplete gem tree

## Symptom

Running the focused libnodectld specs through `nix develop .#libnodectld`
failed while requiring `prometheus/client/formats/text`. The configured shared
`/tmp/dev-ruby-gems` contained gem specifications and directory trees, but the
`prometheus-client` library directories were empty. Bundler consequently
reported the bundle as complete while Ruby could not load installed files.

## Cause

The libnodectld development shell uses the fixed, host-wide
`/tmp/dev-ruby-gems` path. An incomplete or concurrent installation can leave
that shared directory internally inconsistent. The event that originally
emptied the gem directories was not identified.

## Workaround

Run Bundler and the affected command with an isolated gem path, removing the
shell's eager Bundler preload from the child environment. For example, set
`BUNDLE_PATH`, `GEM_HOME`, and `GEM_PATH` to a task-specific temporary
directory and invoke the command through `env -u RUBYOPT -u BUNDLE`.

## Verification

After installing the locked bundle in an isolated path, all focused
libnodectld reconciliation and exporter specs passed. This was found while
working on `work/2026-08-22-all-vps-up-monitoring/`.
