# Development cluster Stop + Release — completed

The exact `2026-11-01-typescript-client-migration` vpsAdmin development cluster
is stopped and released. The session remains open.

WebUI/main and the public feature were first verified by the parent at
`babe51421bd1df61a548e7b2f047053df14ff3eb`, tree
`95f01c23a06e2c385756daa61305413af24403d9`. Its repository merge claim was
released. Integration receipt SHA256:
`80ec09e6d53fdb71398b1eac968653c89cfa7873329fec8d52fbaf08f0b7f2a7`.

Normal Stop ran from the workspace root at00:54:08Z and returned native0 at
00:54:30Z (21.824s). Filtered status then showed stopped/not-ready. All39
positively bound runner/descendant identities were absent; retained disks,
config, per-cluster credentials and applied envelope were checked before Release.

The first public Release attempt refused TLS locally (curl60, HTTP000, body0).
No success or provider exit was inferred. The documented workspace CA resolved
TLS; the public portal required normal Basic authentication. Credentials were
read only into memory and passed using curl-config stdin, without values in
argv, logs or receipts. A read-only authenticated portal GET returned200 after
an unsupported HEAD returned404. Exact-session stopped state and process absence
were reconciled before the corrected public Release attempt.

The normal public Release POST used the exact-session URL, body
`{"kind":"vpsadmin"}`, required Origin and ordinary CA/hostname validation.
It returned client0 / HTTP200 / `{"ok":true}` at00:57:24Z (1.956s). The endpoint
reports provider success through its documented contract; its internal native
exit is not independently exposed.

Final public status returned0 with schema2, kind vpsadmin, found=false. This
cluster's directory and recorded socket are absent. All39 original process
identities remain absent. Shared br0 still exists; workspace-wide CA/SSH files
outside the cluster match their prior bytes and modes. Original preparation,
refresh and integration records remain unchanged. Prior source/Nix/preview
records were retained; no store GC or unrelated root removal was requested.

One fresh pinned Luna/low/full-access utility passively observed only the durable
final result. Its fixed observer exited0 and its Codex CLI exited0. No cluster
operation or watcher remains running. Operation ownership is explicitly returned
to the lead. No session lifecycle, direct reset/private helper, manual signals,
other-cluster action, source/Git/CI/config/claim/deployment or unrelated cleanup
was performed.

[Execution receipt](devcluster-stop-release-0f3caee36292/final.json),
[completion/ownership receipt](devcluster-stop-release-0f3caee36292/completion.json)
and [passive observer result](devcluster-stop-release-0f3caee36292/watcher-result.md).
Native stop output is retained privately; raw status/credentials were not saved.

Session stays open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/
