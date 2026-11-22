# `nix flake check` Rejects the `overlays.all` List

Related initiative:
`work/2026-07-20-vpsadminos-kernel-prune`.

Command:

```text
nix flake check
```

Symptom:

The checker stops at `overlays.all` with `overlay is not a function, but a list
instead`. It does not reach the remaining flake outputs.

Cause:

`flake.nix` intentionally exposes `overlays.all` as the raw `osOverlays` list,
while the generic flake checker treats every member of the `overlays` output as
one overlay function. The failure reproduces unchanged on vpsadminos staging
commit `702155fb91effd7102a92b568f684c7b0d948b1f`.

Workaround:

Evaluate the affected outputs directly, for example `.#lib.kernelVersions`,
specific package derivation paths, or the relevant test-runner cases. Do not
treat a repeated `nix flake check` run as useful validation until the output
shape is corrected or the raw overlay list is moved outside `overlays`.

Verification:

The feature head and a clean detached worktree at the staging base failed with
the same error. The temporary base worktree was removed after comparison.
