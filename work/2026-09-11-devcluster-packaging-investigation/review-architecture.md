# Architecture and repetition review

Reviewed organization commits `0a9c974994746e2a6d9d74e83cde8abbf0e65f0a..54b1d7a3f3cbfc4261abbe2fc3632d0908599696`, including the amended smoke-test commit, against the workspace consumer, generic runtime `bcbaf825d71285cbbd05b56e78bc386f2df480bd`, vpsAdmin `8d0ccafd5b307115ddc4b1f24152ba30ed52e893`, and vpsAdminOS `3eaf7b7320754715b38fc629e7f0ce23d13402cd`.

## Findings

### Important: the providers duplicate a private vpsAdminOS runner contract instead of consuming the owning flake API

Commit `30516d8c514fe43d70cef51eb4e1a27ab31877e3` changes `dev-clusters/vpsadminos/flake.nix:39-44` and `:69-78` to reproduce the integration already present in `dev-clusters/vpsadmin/flake.nix:60-65` and `:104-115`: both import `os/overlays` through `vpsadminos.outPath`, rethread the raw `netlinkrb` and `ruby-lxc` inputs, and reconstruct the test-runner Bundler environment from private files under `os/packages/test-runner`.

The pinned vpsAdminOS revision already owns and exports this wiring. Its `flake.nix:223-231` exposes `overlays.all` and `overlays.default`; commit `6f9b2c755143197bd9c3452e1c0121b22e978c4d` introduced that public interface specifically so external consumers would not import `os/overlays` and recreate its source-input wiring. The upstream `test-runner/nix/package.nix:3-24` likewise owns the Ruby, gem configuration, dependency bundle, and source-library paths that the two provider flakes repeat.

This is an observed drift failure, rather than a hypothetical cleanup. The vpsAdmin provider received the overlay arguments and `vpsadminosRubyGemConfig` in earlier commit `c7dc9554`; the sibling vpsAdminOS provider did not, and the resulting split is one of the failures repaired by `30516d8`. If vpsAdminOS adds another source input, changes its gem configuration, or moves the private gem metadata again, its exported overlay/package can remain valid while one or both packaged providers fail evaluation or load a runner with incomplete source-gem handling.

Use `vpsadminos.overlays.all` (or the documented composed overlay) in both provider flakes now. The runner dependency environment should also have one owning constructor: preferably a vpsAdminOS-exported builder for an alternate runner entry point, or otherwise one shared organization-side Nix helper consumed by both packaged provider subtrees. Provider-specific runner names and priority-machine arguments can remain local. Verify both provider runners through `devcluster-check` after changing this boundary.

No Blocking or Advisory findings.

## Residual gaps

- The final `devcluster-check` rerun for amended head `54b1d7a` was still in progress when this review was written. Static inspection confirms that the amendment only moves rendered JSON parsing from Nix to Ruby.
- Per the review constraint, no live VM start, update, stop, restart, retained-disk, or mixed-generation exercise was performed.
- Explicit shell failure propagation remains a manually maintained contract because lifecycle callbacks execute under a conditional. The focused tests cover credential tools, configuration builds, copies, activations, refresh SSH, retained results, environment propagation, and lock release; they do not inject failures into every post-build filesystem/log/launcher operation.
