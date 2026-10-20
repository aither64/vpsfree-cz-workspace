# Exact 60-advisory publication package

Execution complete. All60 approved advisories were published by the existing
guarded publisher after explicit lead release. Email remained disabled. The
read-only preparation and execution procedure below is retained as the record
of its gates, not as an instruction to repeat the completed operation. The user
had
approved publication of the latest accepted 60 snapshots and separately merging
the changes. The authorization is retained in
`assessment/publication-and-merge-user-authorization.json`. No email is approved.
This owner does not perform integration as part of the publication package.

## Publication result

The original approved batch exited0. All60 exact IDs/revisions published with
valid timestamps from `2026-10-20T13:48:16Z` through `2026-10-20T13:58:04Z`.
The existing publisher verified unchanged reviewed public content, CVE/external
identities and all780 node fields before accepting each published readback.
All60 result rows explicitly report `send_mail:false`. There were no operator
retries or additional API calls for final inspection.

[publication-receipt.json](publication-receipt.json) records every final ID,
revision, timestamp, state and no-mail result;
[published.tsv](published.tsv) is the compact exact60 table. The restricted raw
apply output is `.state/publication-preflight/apply.json`, SHA256
`addd9d8dc9bef7a379ed20c38a7d284072c33c7c7a9d308aa81b7d3170b55ccd`.

Final local proof verified unchanged source
`e6ceb642878dd97546174217676d9861afc38d4e` (81 feature commits), all111
baselines, selected dossiers/public YAML/evaluations, frozen evidence and old
ledgers. All69 consumed boundaries and their actual source parents remain
intact. The whole worktree/index is clean. The exclusive advisory-write slot
was returned to the lead. Integration was independently owned by implementer0;
this publication owner performed no Git mutation or merge. Nix shell94281 is
idle. No email, deployment or lifecycle action occurred.

## Retained read-only result

Completed: all60 repository-required normal readiness calls and the exact normal
batch publication dry-run passed. All60 effective publication permissions were
checked by the existing tool. Exact identities, revisions, remote digests and
no-mail fields match the manifest. All780 node rows are resolved. Source,
selected dossiers/evaluations, all111 submission baselines and frozen evidence
are unchanged; whole worktree/index remain clean. No writes occurred.

[preflight-receipt.json](preflight-receipt.json) is the sanitized result.
[approved-snapshots.tsv](approved-snapshots.tsv) names every CVE, draft ID and
latest revision. Restricted full outputs are under ignored project
`.state/publication-preflight/`; raw publication-preflight SHA256 is
`4c65559a8249f0a74371d428f3bd08dea67e26008cf7d0366b566e76b8d26cdc`.
That preflight was accepted by the lead before the subsequent explicit release.
The architect's final brief and accepted sequence exception were read before
the approved operation. The publisher repeated its mandatory all60 preflight;
no extra readiness loop was run.

[manifest.json](manifest.json) records every CVE, stable draft ID, latest accepted
revision, remote/dossier digest, reviewed node counts, dossier/evaluation hashes,
all111 baseline hashes and prior ledger hashes. [order.txt](order.txt) preserves
the original approved order. Source is
`e6ceb642878dd97546174217676d9861afc38d4e`: 81 consumed feature commits and
69 recovery checkpoints. Special revisions are85/v25,112/v17,113/v17 and106/v27;
the other56 drafts remain revision13. All780 reviewed node rows are resolved:
708 mitigated and72 not affected. No new assessment or content is prepared.

## Read-only gates

Session/environment and retained implementer1 Sol/xhigh/workspace-write access
are verified. Use the existing owned Nix shell with normal hooks, `umask077`
and no hook/source overrides. Require exact source HEAD, clean whole index and
worktree, unchanged all111 baselines, preserved69 actual-parent recovery
boundaries and frozen snapshot SHA-256
`61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274`.

Repository AGENTS step11 requires normal `ready` before publication. Each
read-only `bin/security-advisory ready --evidence .state/evidence.json <CVE>`
reuses the frozen snapshot, compares in memory and verifies the remote draft.
It neither collects evidence nor writes evaluation files. Persist its full
stdout/stderr only in ignored restricted
`.state/publication-preflight/ready/<CVE>.{json,stderr}`. Stop at the first
nonzero result or mismatch. This readiness call is the explicitly allowed
repository-required prerequisite; do not issue separate collect/evaluate/sync.

Then run the ordinary exact batch without the approval switch:

```sh
mapfile -t publication_cves < "$publication/order.txt"
bin/security-advisory publish "${publication_cves[@]}" \
  > .state/publication-preflight/publish.json \
  2> .state/publication-preflight/publish.stderr
```

The existing command preflights every committed evaluation and submission,
exact remote draft identity/digest/revision, full public texts/CVE/node rows,
publication timestamp absence and effective per-advisory publish authorization
through normal OPTIONS. No separate token issuance, rotation or permission
probe is needed. Require `dry_run:true`, `send_mail:false`, exact60 IDs/order/
revisions/digests, each draft state and per-row `send_mail:false`. Raw output
stays restricted. Save a separate sanitized exact-set preflight receipt and
repeat local source/baseline/hash checks afterwards. No write has been released.

## Eventual released write, not executed by preparation

After an explicit lead release naming the accepted exact60 manifest and source,
recheck unchanged source, all baselines, manifest and raw preflight hashes. Use
the same existing batch with `--approved-publication`; that switch attests to
the already-recorded user approval and is never passed during preparation.
The command rechecks the complete batch before its first write, carries exact
revision preconditions and explicitly sends `send_mail:false` for every
publication. It reads every publication back, verifying the reviewed content,
identity, state and publication timestamp. It does not collect, reevaluate,
synchronize content, or rewrite submission baselines. Preserve draft baselines
and consumed history as the recovery boundary; session publication receipts
record the resulting published states separately.

Stop on any drift, nonzero result or uncertain outcome. Preserve returned state,
raw logs, old baselines and completed history; report the precise advisory/stage.
No blind retry, adopt, recreate, content refresh, automatic rollback or email.
The tool's existing read-only recovery may establish whether an ambiguous
publication completed; the operator must not invent another client or retry it
without lead-coordinated outcome reconciliation. Do not infer that an exact
draft readback proves a timed-out publication request cannot still complete.

Final execution acceptance will require exact60 published readbacks, unchanged
approved content/revisions, valid publication timestamps and explicit no-mail
attestation, plus unchanged source/baselines/evidence and clean worktree/index.
Return the result and exclusive slot. Integration is a separate lead/coordinator
operation; no Git mutation, push, merge, deployment or session lifecycle action
is authorized by this preparation packet.
