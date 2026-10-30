# Final f715 completed-job acceptance

Repository: `vpsfreecz/vpsadminos`. Run
[40217314767](https://github.com/vpsfreecz/vpsadminos/actions/runs/40217314767),
attempt 1, exact head `f715e9d99b56a2f0e52d17b15f086b99cc926e13`.
Run and completed-job metadata were read before log retrieval. This receipt
does not declare the entire workflow complete or inspect running aged-v5.

| Completed job | Result | Completed UTC |
| --- | --- | --- |
| Native suite, `121244289003` | success | 2026-10-25 20:50:11 |
| AMD aged-v6, `121244289109` | success | 2026-10-26 01:06:56 |

Both job responses independently name the exact head, run and attempt. Native
Run tests and Evaluate test results steps succeeded. Its final log reports
317 scripts of 109 tests in 7693.91 seconds and 109 successful tests. There are
109 terminal test-success rows; no skipped test/example or expected-failure,
unexpected-failure or unexpected-success outcome is reported. This is the
reported test-level aggregate, not a reconstructed per-example total.

Native log line 1674 reports `impermanence-from-2abbe3cc1c10@v1` successful in
139.75 seconds; line 2573 reports `@v2` successful in 141.75 seconds. Both ran
the ordinary default script. Their terminal success binds to the reviewed f715
template's single sequential scenario: real stale-state import/repair, retained
run and payload, daemon reload, new-writer persistence, payload/reload continuity,
old/new dataset retirement and final container deletion. These later assertions
were reached successfully according to the runner's terminal result; the prior
cb4 first-import failure no longer truncates either scenario in this run.

The successful native job skipped **Upload full test logs**. No native archive
was published, so no independent per-phase JSON or per-case result file was
downloaded. The conclusion above uses the exact-head terminal runner results
and the already-reviewed scenario, not invented phase captures. Native stdout
and metadata are retained, with the four relevant rows in `native-summary.txt`.

Native log SHA256:
`f8b4f9e316e38a4e1cab4e6ad3d0157cd2b16d495f93292eec594adbbfd1a12d`
(1,046,737 bytes). Summary SHA256:
`b3ede38522d0b556cac2565c94631c157b8b31f2fd0692cdcf21b1ee8fc57cf8`.

Aged-v6 success is independently confirmed by completed-job metadata; its full
artifact was unnecessary to download. Published artifact `12621117297`,
`os-test-logs-40217314767-1-livepatch-amd-scale-aged-v6`, is 1,939,569 bytes;
GitHub advertises digest
`sha256:8761505dcca014d5cafaffa960d12bd9d76eee326fd54d71092ed92cde6ac0c9`.
That is metadata provenance, not a locally verified artifact hash. This passing
run does not establish the cause of the retained prior aged-v6 RCU stall.

The first native-log read was refused by gh's escape-sequence output guard;
one corrected read explicitly retained raw log bytes. Conservatively charge
both 1,046,737-byte responses (2,093,474 bytes) plus the small metadata/HEAD
responses against the selected 8 MiB transfer cap. No archive was downloaded
or unpacked; retained text is about 1.01 MiB, below the 16 MiB unpack cap.
No images, extra job logs, source/Git actions, tests, retries, cancellations,
Nix/builds, VMs or live probes were performed. Running aged-v5 remains owned
by its separate watcher.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/
