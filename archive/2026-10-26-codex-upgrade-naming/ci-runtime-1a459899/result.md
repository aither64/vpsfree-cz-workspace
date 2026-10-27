# Runtime1a459899 CI result

One requested read-only capture at 2026-10-26 20:14:27 UTC found
[Check40390947914](https://github.com/aither64/dev-workspace/actions/runs/40390947914)
completed **failure** on exact head
`1a459899ca7c51649e1c3dd5a2fa18caa546c118`.

| Job | Result | UTC start–completion |
| --- | --- | --- |
| archive121811468667 | success | 19:54:48–20:07:58 |
| creation121811469269 | success | 19:54:47–20:09:46 |
| fast121811469077 | failure | 19:54:48–20:04:07 |
| host121811471577 | skipped | feature push policy |

Actual status: [snapshot](status-snapshot-1.json). Complete failed fast log:
[fast-job-121811469077.log](fast-job-121811469077.log), 277753 bytes, SHA256
`d6e777bdb600ab2a88ce05509a8322340bc3ddb038666ca104f3ba5ecf681936`.

The failing test is
`TestCreationEvidenceGapDeletionRetiresTheExactRequest/direct-new-schema3/failed`:
`creation_test.go:1578: receipt reconciliation dispatched creation <nil>`.
The `portal/internal/web` package fails after111.042s, causing
`/nix/store/f27c51pbx3xz0jwk0vc9qfg3k78z5vsp-dev-workspace-0.2.0.drv` and then
its `user-namespace` dependent check to fail. Owner0 received the complete log
for diagnosis in message `c7c101f1-5948-43ca-982a-03bce6784b32`.

No root cause or rerun acceptance is claimed. No CI dispatch, rerun, local check,
watcher or long poll was launched. Prior391d evidence remains separate;
the archive setup fix passed at1a459899, but full final-input CI has not passed.
