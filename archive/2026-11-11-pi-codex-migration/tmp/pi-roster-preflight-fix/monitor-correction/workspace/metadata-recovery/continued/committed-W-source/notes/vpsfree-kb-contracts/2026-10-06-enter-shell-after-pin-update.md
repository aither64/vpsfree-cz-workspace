# Refresh the KB shell after changing its source pin

The KB devShell exports `VPSADMIN_KB_VPSADMIN_SOURCE` from its locked vpsAdmin
input. Updating `flake.lock` inside that shell does not refresh the environment
of the already-running shell. `tools/check-contract.rb` and its tests read this
exported path, so a direct `bin/check` can inspect the previous source even when
the on-disk revision records agree on the new pin.

Generate the targeted pin first, then enter a fresh pinned shell for `bin/check`,
as the canonical `docs/webui-change-workflow.md` sequence requires. For command
provenance, compare the new shell's export with:

```sh
nix eval --raw .#devShells.x86_64-linux.default.VPSADMIN_KB_VPSADMIN_SOURCE
```

Keep the revision/lock-graph guards too; the source-path comparison supplements
them. A shell that was opened before a pin mutation is not evidence that checks
used the new source. This matters even when the changed component does not alter
the WebUI fingerprints.

Source inspection and the prepared correction are recorded in
`work/2026-10-05-network-ipv4-left-counter/visibility-final-pin-operation.sh`.
Execution of the corrected pin/check is still pending at this checkpoint.
