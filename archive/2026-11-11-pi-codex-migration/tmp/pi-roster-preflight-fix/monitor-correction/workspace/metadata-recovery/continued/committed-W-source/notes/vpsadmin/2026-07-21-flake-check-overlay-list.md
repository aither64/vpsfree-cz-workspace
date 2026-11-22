# vpsAdmin flake check rejects the overlay list output

Related initiative:
`work/2026-07-21-node-software-revision-links`

## Symptom

Running `nix flake check` at the vpsAdmin repository root fails while checking
`overlays.list`:

```text
error: overlay is not a function, but a list instead
```

## Cause

The flake publishes both `overlays.default`, which is a valid composed overlay
function, and `overlays.list`, which is intentionally a list of overlay
functions. Nix treats every attribute below the conventional `overlays`
output as an individual overlay and therefore rejects the list before checking
the remaining outputs.

This failure predates the node software revision-link correction and reproduces
at its clean base commit `1bb84ae9bc792eef5650a030f850409c737b6a91`.

## Workaround

Build the relevant check directly, for example:

```sh
nix build .#checks.x86_64-linux.webui-software-revision-links --no-link
```

Do not report a full `nix flake check` as green until `overlays.list` is moved
outside the conventional flake output or otherwise represented validly.

