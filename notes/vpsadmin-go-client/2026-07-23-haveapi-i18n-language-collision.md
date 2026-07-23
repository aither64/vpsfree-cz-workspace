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
vpsAdmin client with HaveAPI tag `v0.28.0`. Apply the HaveAPI Go filename fix
from commit `6bd391b9737d40d4f678c9c4e3cda6dd2e4f504d` first: an API resource
or action named `test` otherwise generates package code in `_test.go`, which
normal `go build` silently excludes. Generate into a fresh directory inside
the Go module, synchronize that complete directory into `client/`, and run
`go fmt ./...`, `CGO_ENABLED=0 go build ./...`, and
`CGO_ENABLED=0 go test ./...`. A fresh destination is important because the
generator does not remove files for API resources that no longer exist.

The HaveAPI Go development shell installs only client-side Ruby dependencies.
Its integration generator spec also boots the Ruby test server. If those
server gems are absent, install them into the existing client gem path with
the server Gemfile and clear the shell's forced Bundler setup for that install:

```sh
nix develop .#client-go -c bash -lc \
  'RUBYOPT= BUNDLE_GEMFILE=../../servers/ruby/Gemfile bundle install'
```

This workaround was verified on 2026-07-23: the v0.28-generated client
compiled successfully, exposed the Event `test` action under a buildable
collision-resistant filename, and removed stale OOM report rule types.
