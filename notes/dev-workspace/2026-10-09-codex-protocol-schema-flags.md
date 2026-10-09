# Validate experimental App Server methods from the selected Codex

The workspace may retain a different native Codex than system PATH. Generate
protocol schemas using the executable resolved from the workspace profile's
active Codex link. Include `--experimental` for the full request corpus:

```sh
/home/aither/.local/state/dev-workspaces/codex/current/bin/codex \
  app-server generate-json-schema --experimental --out /tmp/codex-schemas
```

Without the flag, validation in this initiative failed on `project/create`
because its experimental schema was omitted; that was not a request-shape
regression. The selected 0.160.0 schema corpus passed with the flag.

Focused Nix `go test` source runs require `-mod=readonly` as documented in
[the focused-Go note](2026-10-04-focused-go-checks-in-nix.md). A minimal
`nix shell` also needs GCC for CGO-enabled tests; Go and Node alone stopped
before compilation. Neither failure justified changing project dependencies.
