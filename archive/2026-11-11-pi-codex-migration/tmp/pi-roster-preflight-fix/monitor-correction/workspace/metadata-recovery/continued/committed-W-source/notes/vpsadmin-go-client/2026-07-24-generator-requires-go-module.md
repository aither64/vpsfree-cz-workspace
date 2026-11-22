# HaveAPI Go generator requires a module before generation

Related initiative:
`work/2026-07-24-vpsfreectl-snapshot-download-fix/`

## Symptom

Generating into an otherwise empty temporary directory fails after writing the
client files:

```text
go: go.mod file not found in current directory or any parent directory
haveapi-go-client: go fmt failed
```

## Cause

`haveapi-go-client` runs `go fmt` before returning. The destination therefore
has to be inside an existing Go module even when the caller intends to create
the module only for a temporary compile check.

## Fix

Create or copy `go.mod` into the destination's parent directory before running
the generator. Generate into a fresh child directory, then run `gofmt`,
`CGO_ENABLED=0 go build ./...`, and `CGO_ENABLED=0 go test ./...`.

## Verification

With `go.mod` present first, public `haveapi-go-client` 0.29.6 generated the
current vpsAdmin API client. The generated `Language` resource was present and
both the build and test commands passed.
