# Go Unix socket tests and Nix shell TMPDIR

## Symptom

Running the portal tests with `nix develop -c go test -mod=mod ./...` can fail
in the router test with `listen unix ...: bind: invalid argument`.

## Cause

The Nix development shell gives `TMPDIR` a long per-shell path. Go then nests
its test directory below it, and the router's Unix socket path exceeds the
kernel limit.

## Fix and workaround

Tests that create a nested router socket now use a short `/tmp` runtime root
instead of nesting that socket below `t.TempDir()`.

For any similar test that has not yet been adjusted, run it with a short
temporary root:

```sh
nix develop -c sh -c 'cd portal && TMPDIR=/tmp go test -mod=mod ./...'
```

The adjusted router test and this command passed all portal packages for initiative
`2026-09-06-portal-config-deployment-policy`.
