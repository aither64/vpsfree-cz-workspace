# Bounded index publication acceptance (prepared only)

Lead explicitly authorized one ordinary authenticated CA-verified index-status GET
to demand standard metadata refresh, followed only by published progress reads.
Parent launches this helper through a fresh Luna/low utility. Implementer0 has
syntax-checked it only; no request or wait from this helper has run.

Exact argv:

```sh
python3 /tmp/portal-improvements-index-acceptance.py
```

SHA256: `b275ca563c3ad1e0d454247b7c7ded006a718b3aa0e49746b8f0fbc4a6120671`. Identical durable copy:
[index-publication-acceptance.py](index-publication-acceptance.py).
No dependencies outside the standard Python library and existing SSH/dev-session.
Exact trusted-bound session is checked first. Existing attempt evidence refuses
before any credential read or HTTP demand; there is no automatic retry.

The helper privately reads the configured password through the exact proven
rootSSH target/key/options and fixed configured file, as accepted for smoke.
Password/stdout/stderr stay in memory/private pipes. It uses Basic auth only in
memory and validates TLS with `/var/lib/dev-workspaces/public/ca.pem` against the
canonical hostname `vpsfree-cz.workspace.aitherdev.int.vpsfree.cz`. Redirects are
refused. No credentials/headers/response bodies/rows/names/messages are logged.

One initial GET goes to `/api/index-status` without `progress=1`. This is the ONLY
normal demand. Up to31 subsequent GETs go exclusively to
`/api/index-status?progress=1`, separated by one second. Each response is bounded
to2MiB with10s socket timeout; SSH access has15s timeout. There is no generic outer
timeout wrapper or second normal demand. Every sample and HTTP/access failure is
recorded. The observer should monitor independent files and not retry the helper,
trigger extra full refreshes or expand into other checks.

Absolute evidence directory:
`/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/deployment-index-publication/`.

- `observations.jsonl`: UTC/elapsed time, normal/progress sample kind, HTTP status,
  loading/authoritative/generatedAt, session/operation and cluster
  projection/notice counts. Only known static top-level warnings are retained;
  unexpected text is withheld.
- `status.json`: atomically updated PID/state/counters/last observation, independent
  of the sample log. Records attempted demand before transport, so ambiguous
  response loss never causes a duplicate demand.
- `result.json`: final status/outcome/exit/elapsed and API completion evidence.

Completion requires a fresh publication timestamp after the initial demand,
loading=false, authoritative=true, a nonempty membership and no top-level warning.
It also requires every session's optional cluster projection to be measured or
explicitly noticed and the same ready timestamp in two consecutive progress
samples. This avoids accepting the initial cold membership publication alone:
Bf8 publishes that early snapshot with unknown/no-notice cluster projections,
then the final computation sets each projection to known or an explicit notice.
This observation predicate is specific to the inspected deployed Bf8 code; it
changes no product/API contract or control authority. Genuine cluster notices
produce a warning result rather than silently passing.

Exit0: fresh stable authoritative enriched publication, no warnings/notices.
Exit2: fresh top-level warning or stable cluster notices; actual safe warning or
notice count remains recorded. Exit3:31 observations exhausted; the final actual
loading/authority/time/counts/warnings remain recorded as incomplete. Exit1:
actual access/HTTP/response failure with stage/type/status, no raw secret-bearing
exception/body. No retry/fullsmoke/browser/build/source/ref or service action.

No phase acquires/releases machine ownership. Parent retains claim759b3cc6 while
accepting this bounded deployment evidence. Existing successful deployment/smoke
results are unchanged; this probe does not test naming turns or submission.
