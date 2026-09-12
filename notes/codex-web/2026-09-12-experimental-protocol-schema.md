# Include experimental Codex App Server schemas

The codex-web client initializes App Server with `experimentalApi: true`.
Generate its validation schema with the exact selected binary and include
`--experimental`:

```sh
codex --version
codex app-server generate-json-schema --experimental --out /tmp/codex-schema
python3 test/codex_protocol_contract.py /tmp/codex-schema codex/client.go
```

Without that flag, existing methods such as `collaborationMode/list` are absent,
so the request corpus fails even when the deployed client is compatible.
The complete corpus, including typed activity and observation fields, passed
against installed Codex 0.154.0 with the flag on 2026-09-12.

For local Nix checks, Go's default cgo mode also needs a C compiler; include
`gcc` alongside `go`. For Python validation, use
`python3.withPackages (ps: [ ps.jsonschema ])`: adding the standalone jsonschema
derivation to a shell does not necessarily add it to the selected interpreter.

Related initiative: `work/2026-09-12-portal-review-experience/`.
