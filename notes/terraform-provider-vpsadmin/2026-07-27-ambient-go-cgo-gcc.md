# Ambient Go probes may need CGO disabled

Initiative:
`work/2026-07-27-terraform-provider-vpsadmin-issue-11/`

Running a standalone Go request-capture probe with `go run .` in the ambient
workspace shell failed while building `runtime/cgo`:

```text
cgo: C compiler "gcc" not found
```

The ambient Go toolchain enables CGO but the ambient `PATH` has no C compiler.
For a pure-Go probe, use `CGO_ENABLED=0 go run .`. For repository builds and
tests, prefer the repository's `nix develop` shell instead. The issue #11 probe
completed successfully with CGO disabled.
