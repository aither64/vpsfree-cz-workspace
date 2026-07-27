# Exact Go patch assertion can break the pinned Nix shell

Initiative:
`work/2026-07-27-terraform-provider-vpsadmin-issue-11/`

After a scheduled vpsAdmin flake update, all `nix develop` checks failed during
evaluation:

```text
terraform-provider-vpsadmin requires Go 1.26.3, got 1.26.5
```

The provider selected `pkgs.go_1_26` but separately asserted an exact patch
version. A compatible Go patch update in the followed nixpkgs input therefore
made the development shell and Nix package unevaluable. The Go modules declare
1.25.8 as their minimum and CI tests both supported Go release lines, so an
exact 1.26 patch is not a compatibility requirement.

Remove the patch-level assertion and rely on `pkgs.go_1_26` for the Nix build
and shell. Keep the README minimum aligned with the `go.mod` directive. Verify
with `nix develop -c make test`, `nix build`, and `nix flake check`.
