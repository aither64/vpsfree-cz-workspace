# HaveAPI Go generator Language collision

Related initiative: `work/2026-06-15-vpsadmin-events`

`haveapi-go-client` from HaveAPI 0.29 generates a `Client.Language string`
field for localization. vpsAdmin also exposes a top-level `Language` resource,
so regeneration produces two `Client.Language` fields and `go test ./...`
fails:

```text
client/client.go:96:2: Language redeclared
client/client.go:281:15: cannot use NewResourceLanguage(c) as string
```

Until the generator resolves resource/property name collisions, generate the
vpsAdmin client with HaveAPI tag `v0.28.0`. Generate into a fresh directory
inside the Go module, synchronize that complete directory into `client/`, and
run `go fmt ./...` plus `CGO_ENABLED=0 go test ./...`. A fresh destination is
important because the generator does not remove files for API resources that
no longer exist.

This workaround was verified on 2026-07-23: the v0.28-generated client
compiled successfully and removed stale OOM report rule types.
