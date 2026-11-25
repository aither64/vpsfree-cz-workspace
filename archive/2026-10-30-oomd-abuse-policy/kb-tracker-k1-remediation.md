# K1 narrow remediation

Original review head dc608aa8a4ed4dbf67ee5551a5a6d0796cef569d remains at
refs/review/2026-10-30-oomd-abuse-policy/tracker-dc608. Reviewer continues that
frozen range; this is a requested narrow successor, not a new contract.

Successor21d679a085f4af539079d7357216f2b7f46c7a46, tree
9bf384bc70f34d8ec34d0216bfda85c7b3a376c6, is clean and local only. Normal commit
ran in the pinned shell using git commit -F, exit0/no bypass; no declared hook
framework. Three files92+/19-: runner24changed lines, runtime documentation3lines,
focused fixture/assertions. No migrations, pins, schema or control-contract changes.

The existing observe helper now accepts its completion predicate and optional
complete-write request. Discovery, each lifetime_gone? completion/quiesced/
postcleanup observation and final process-receipt write therefore run inside the
same existing rescue/first-error latch. Error returns false; failed ownership stays
incomplete and drain retains its authenticated owner, control socket and claims.
Machine cleanup proved safe before a final-write failure cannot be undone and is
not promised to be undone. The3-line runtime-contract clarification states this.

Negative-before: new barrier tests against originaldc608 production runner failed
both completion-lifetime and final-complete-publication cases, native exit1.
Completion exception unwound before its first-error receipt; publication failure
was an unrescued IOError. Full native failures remain in k1-before.log/result.json.

Positive-after: targeted four new failures plus healthy actual listener stop
PASS5/161. Final affected regression batch PASS14/425, native exit0/18.971s:
before/after/concurrent ready, unexpected tracker exit, drain/join errors, all3
post-discovery lifetime phases, final-complete write, quiesced and postcleanup
retry controls. Tests use existing owned pipe/queue barriers, no sleeps as proof.
They assert first error class/message and incomplete receipt, machine reaped,
authenticated public control still works, phase stopping, control.sock retained,
claims unchanged and stop called once. Postcleanup/finalwrite cases expressly
allow already-completed safe machine finalization/cleanup; earlier errors forbid
it. Later observations/control retain the same first error. Healthy stop remains
positive, including complete exit and ordinary namespace release.

Evidence in kb-tracker-repair-evidence/: k1-before-result.json/log,
k1-after-result.json/log, k1-regression-result.json/log, k1-quick-inputs.json,
k1-committed-provenance.json and k1.patch. Original review packet/evidence unchanged.
No whole-suite rerun, publication, guests, fixture mutation or old-run operation.
Lead direct reconciliation under review step9 is pending; no confirmation-only
review rerun requested. Separate successor retained until review's final report;
then consolidate per lead before final delivery. Original failed7bdee full check
and accepted pin-only exception remain separate and are not relabeled green.
