# Superseded570 CI failure and fixture correction

Run39974175490 attempt1 tested exact B570d900a4b7bbfe5c716cfd234f9dc89bbedc746.
Completed failed jobs:

- fast120484350114, step5 Build package and focused checks;
- creation120484350665, step5 Packaged browser and native session creation;
- archive120484350732, step5 Packaged browser archive, recovery and revival.

All three complete job logs show the same concrete failure:
`TestCoordinationNotificationRetainsSettingsAndDeduplicatesNativeDelivery`,
both active=false and active=true. At coordination_test.go127 the caller times
out after20s; main_test.go294 records the actual fake-server rejection:
`unexpected notification RPC: thread/items/list`. The generic reconciliation
added by the hotfix requires this supported history read before fresh capture.
The old fixture handled metadata, turns, resume and native send/steer, but
omitted items/list. H1's subsequent Pending-preservation change did not affect
this path, so the evidence also applied to5a5583a.

Lead released a test-only remedy. Final ed2a75b adds exactly two lines to the
fixture: items/list returns an explicit empty data page and nil nextCursor.
Settings, exact native method/client ID, expected active turn, exact-one-send
and replacement-owner assertions remain unchanged. The exact selector passes
both cases normally0.184s and with races1.485s. No production relaxation or
failed CI rerun was used as validation.

Complete files: implementer1-hotfix-570-ci-{fast,creation,archive}.log. Creation
also retains its original raw log. Hashes are in
implementer1-hotfix-570-ci-logs.sha256. The first creation log fetch returned EOF;
a direct raw API fetch was then blocked by gh's terminal-escape output guard.
The corrected raw fetch explicitly allowed escape bytes only into an owned
artifact, with a normalized copy used for diagnosis. No raw escape output was
printed to the terminal. These were artifact-retrieval errors, not test results.

Final branch snapshot shows current ed2 run39976880008 attempt1 in progress.
Superseded5a run39975956680 remained active; policy-required cancellation was
attempted once and rejected HTTP403, Resource not accessible by personal access
token. See implementer1-hotfix-superseded-cancel.txt. No credential workaround,
current-head cancellation, failed-job rerun, wait, native or build was performed.
