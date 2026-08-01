# Rebase across hook and flake-input additions

Initiative: `work/2026-08-01-test-framework-ci`

Rebasing a configuration feature range can stop when a replayed commit changes
`.overcommit.yml`: Overcommit correctly rejects that commit until the new
configuration is signed. Sign the configuration only after that patch is in
the index, create the replayed commit with its original message, remove Git's
rescheduled duplicate from the rebase todo, and continue.

The same range added flake inputs while obsolete generated lock commits were
intentionally omitted. Entering a normal `nix develop` at that intermediate
state wrote the missing inputs into `flake.lock`. Use
`nix develop --no-write-lock-file` until the functional rebase completes, then
generate the final lock changes through `confctl inputs ... --commit`.

This procedure preserved all seven functional patches, removed five obsolete
intermediate pins, and produced a clean branch with generated final pins.
