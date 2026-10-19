# Aitherdev rollout

Current status at managed pickup (15:09 UTC, coordinator revision 3660): system
job waiting_resource behind the existing aitherdev review reservation; dependent
profile job waiting_dependency. Neither has an attempt. Bounded continuation
accepted by the retained managed root; see deployment-handoff-ack.json. Resume
on coordinator notices, with no reservation polling or checkpoint commit.

User authorized deployment through vpsfree-cz-configuration with the original fix
request and implementation instruction. No default-branch integration authorized.
System activation and user-profile application share vpsfree:aitherdev reservation.

Reviewed source:
- runtime a0d4c202a2e68646aea2d93ce1f0cebaae59175b
- workspace dac911fc1327dfca1b3cbc8bcfa5cad9ac3e2ff7
- configuration b42482379cd759a508b62423ea121fa7519c87f9

Independent final review and final history/pin follow-up accepted, with one narrow
retry finding fixed and verified in Chromium/Firefox. All packaged checks and the archive lifecycle VM passed under archive_verification.
Composition contract passes matching runtime/hash and unchanged extension siblings.
All feature branches published; none integrated.

In progress: coordinator machine preparation via
prepare.py (lead launches, verification watcher observes separate result files),
then exact user-instruction deployment approval and reservation, system job first,
profile job depends on system. Keep reservation through deployment acceptance.
Recover only original uncertain attempts and preserve receipts/roots. No reboot.
Package rollback is unsupported; recover forward with same approved artifact.

Another session held aitherdev at last status read. Do not bypass its reservation.
The ordinary saved archive retry already completed on the installed runtime, with
tracking synchronized; see state.md. No further target mutation is needed.

## Preparation results

Profile preparation (first request) refused because another independently owned
archive has an unfinished journal/cleanup sidecar. This is a correct guard; it
made no package switch. Keep the original result/log. Retry with a fresh request
only once that operation has settled. System preparation remains in progress;
no deployment approval, reservation or activation job has been submitted yet.

Machine preparation succeeded with snapshot
sha256:652bbf390066517744868e623cd23a62cd4e5bb684929e800ebb71030179496c
and coverage configuration b4248237/runtime a0d4c202. No activation submitted.
Application package build proceeds independently of profile transition admission.

Application package build passed (421s) at workspace dac911fc; build output and
logs retained in application-build.stdout/.log and application-build-result.json.
No activation has occurred. Archive lifecycle VM verification remains active.

## Final prepared artifacts

Long verification and CI passed at the final runtime revision. Second system
preparation passed with snapshot a17a9e6f; application preparation passed with
snapshot e667d570. Both bind current package generation456bih1i and catalog
d4f1b57f. Full immutable snapshots are machine-snapshot.json and
profile-snapshot.json. No activation executed yet; queue behind the existing
aitherdev owner with system first and profile depending on it.

## Submitted queue

Reservation request 1ce9be0f-bd17-4c85-ab64-1a94fd352c4c. System job
deface17-2075-4075-a527-69f57e202812; profile job
c40881f1-6771-436a-94a9-597573448c97 depends on the system job. Both carry
exact snapshot approvals. No activation confirmed. Continuation is handed to
the existing managed lead under deployment-handoff.md, with native coordinator
notifications. Keep machine ownership through review and explicit integration.
