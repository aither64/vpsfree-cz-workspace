# G0 disposable storage-freeze trial

This is the checklist for this session's **disposable** vpsAdmin storage-topology
cluster. It records a trial, not a reusable production procedure. Use the
final exact vpsAdmin head recorded in `state.md` only after the complete
branch review is clear. Leave strict dispatch, identity publication and
repair APPLY disabled.

## Before starting

- Recheck that the session-owned cluster slot has no retained VM disks or DB.
  At the 2026-09-25 read-only preflight it contained only `config.json` and
  `socket-dir`, with no matching QEMU process; recheck immediately before start.
- Start with bridge networking and storage topology. Record the build revision,
  DB schema version, singleton control row, active API/WebUI/NodeCtld revisions
  and initial mode/epoch. A missing control row is a stop condition, not a
  reason to insert it manually.
- Use a disposable primary Pool and two independent datasets. Record queue
  state before touching it. Use an active direct administrator session and
  separate limited/delegated test sessions. Do not print bearer tokens or a
  test database URL in logs or notes.

## Acceptance sequence

1. `GET /storage_freeze` through the normal authenticated client must show
   `read_write`, epoch `e`, bounded DB counts and `repair_ready=false`. The
   Cluster WebUI must show the same epoch and its database-drain warning.
   Repeated GET must not append a catch-up audit or change state.
2. Anonymous, ordinary, support and delegated sessions must fail their
   respective show/mode authorization checks. A show-only admin scope must not
   change mode. Invalid WebUI CSRF must not change epoch or transition count.
3. Pause the test node's storage queue and submit one snapshot chain on
   dataset A. Prove it is queued before changing mode. If the queue cannot be
   controlled or the fixture cannot be proved, record G0 as partial.
4. Use WebUI or authenticated API to change to `read_only` with the current
   `expected_epoch` and a reason. Verify epoch `e+1`, exactly one transition,
   copied actor user/session/login and reason. Stale epoch, same-mode and bad
   reason attempts must leave state and audit unchanged. A validation failure
   may return HTTP 200 with a false application status; inspect both.
5. While A is paused, status must report its DB blocker and `db_drained=false`.
   New snapshot admission on independent dataset B must fail with
   `StorageReadOnly`, with no new transaction, intent, catalog row or ZFS
   effect. Resume A's queue and let its previously admitted chain complete.
   Inspect blockers again. Even if `db_drained=true`, `repair_ready` must stay
   false; this trial does not prove node or child quietness.
6. If a bounded catch-up smoke is useful, call `settle_observer` while frozen
   with the current epoch, a reason, `limit=1` and a cursor beyond known
   relevant chain IDs. Expect no settlement and a matching requested/completed
   audit pair. Wrong epoch must not create a request event. Do not settle
   arbitrary cluster findings.
7. Restore the exact recorded queue state and change back to `read_write`
   using a freshly read epoch, even if an assertion failed. On a stale-epoch
   conflict, inspect who changed it before retrying. Verify the second mode
   transition, open queue, terminal A chain, healthy API/WebUI reads, and a
   harmless new snapshot on B completing after unfreeze. Remove disposable
   fixtures only through normal API operations when safe, or record them as
   retained test data.

If the API is unavailable while frozen, restore a compatible API service and
use its authenticated epoch-CAS route. There is no supported local freeze CLI.
Do not report the cluster usable while it remains `read_only` or queue-paused.

## Result record

Record exact tested head, cluster generation, schema, initial/final epoch,
transition and catch-up audit counts, queued-chain ID and final status, denied
chain evidence, screenshots or private log paths, and any failed assertion or
recovery action. Keep credentials and raw private captures out of this file.

This G0 trial cannot establish all-queue NodeCtld and child-process quiet,
osctld delayed GC/trash quiescence, stable ZFS inventory, verified scopes or
repair readiness. Those remain G1 and later gates in the session design.

## 2026-09-25 disposable-cluster result

**API admission/CAS smoke passed; complete G0 remains partial.** The cluster
was started on bridge with storage topology from vpsAdmin `a15afb518`; its
runtime and schema are unchanged by the two test-only fixes in published
`5b2814cac`. The fresh DB has schema version `20260924210000` and control row
1. The WebUI responds at `https://webui.aitherdev.int.vpsfree.cz/`. The
session's credentials are available through
`vpsadmin-devcluster urls 2026-09-23-storage-redesign`; none are copied here.

The test fixture used two stopped VPS on node1, each with a distinct root
dataset in the seeded hypervisor Pool. Their creation chains 6 and 7 finished,
and ZFS contained both roots. This exercises normal API admission and Node
dispatch, but it is not the primary-Pool fixture requested above. The
cluster's seeded transaction key was unlocked through the administrator API
before staging a snapshot; the first attempt while it was locked correctly
returned HTTP 503 without a chain.

Node1's storage queue was recorded open and then paused. Snapshot chain 9 for
dataset A was queued with transaction 31 waiting and an unconfirmed Snapshot;
the queue reported one item. An authenticated direct-admin POST changed
`read_write` epoch 0 to `read_only` epoch 1. Exactly one transition stored the
prior/new mode and epoch, copied user ID 1, session ID 3, login and reason.
Stale-epoch and same-mode POSTs returned 409 without another transition.
While chain 9 was waiting, status reported one active chain, one waiting
transaction, two pending confirmations, one prepared intent, a retained lock,
`db_drained=false` and `repair_ready=false`. A new snapshot request on the
independent dataset B returned HTTP 423; it staged no Snapshot, chain, intent
or ZFS snapshot. Anonymous show returned 401 and an ordinary-user show 403.

An observer catch-up request with stale epoch returned 409 and made no audit
row. A bounded request at epoch 1, cursor 1000000 and limit 1 examined zero
chains and settled zero intents; it wrote matching requested/completed audit
rows. The storage queue was resumed. Chain 9 finished and confirmed its
Snapshot, and status then reported `db_drained=true` with
`repair_ready=false`. A fresh authenticated POST returned the cluster to
`read_write` epoch 2 with exactly one second mode transition. The queue was
open and empty. A post-unfreeze snapshot on B completed as chain 11 and both
physical snapshots were visible in ZFS. The final control row is
`read_write`, epoch 2; there are two transition rows and two catch-up rows.

The live WebUI login, safety warning, read-write status and epoch-2 review
form passed in a headless browser. The review preserved its reason and did
not submit the final mode change; the DB remained at epoch 2 with two
transitions. The browser used the disposable cluster's HTTPS exception, so
this run did not validate certificate trust. Support, delegated and show-only
scope negative cases remain covered by focused specs but were not exercised
in the live cluster. The fixture's stopped VPS and snapshots are retained as
disposable cluster data.
Private request/response evidence is under
`/tmp/storage-review-split-2026-09-23/` with restricted permissions; no
credentials or signing material are in this record. No identity publication,
repair action, strict production dispatch or node/GC quietness was tested.

## 2026-09-26 reviewed-head refresh

Before switching VMs, the retained cluster was running on the bridge with
storage topology. The freeze control remained `read_write`, epoch 2. SQL
preflight found zero unfinished transactions, active chains and blocking
intents. A private mode-0600 database dump is stored at
`/tmp/storage-g0-preupdate-vpsadmin-20260926.sql.gz`; it contains development
credentials and must not be published. The previous system generations are:

| Machine | `/run/current-system` before refresh |
| --- | --- |
| services | `/nix/store/f5qh96dpb2461r9bbhx4asc6p4zapj7s-nixos-system-vpsadmin-services-26.05pre-git` |
| node1 | `/nix/store/l8dvg4vc2635as29cy8lw30hpynsz9bp-vpsadminos-system-dev-node1-26.05pre-git` |
| node2 | `/nix/store/7plhgy2gfdpy9ig8qji9w6w8kvdy85wp-vpsadminos-system-dev-node2-26.05pre-git` |
| storage1 | `/nix/store/xml3dv479nb6j7ns14skqxdqriv4la85-vpsadminos-system-dev-storage1-26.05pre-git` |

The update targets reviewed vpsAdmin `ebe4d8834` and reviewed vpsAdminOS
`dcad075a1` from the session worktrees. Node1, node2 and storage1 updated
sequentially. Their new system generations are respectively
`fbny0b6jcc9jinzm35yy9yn3y483by03`,
`iwiy9nl3n0q7qsidd2f7sa7mqc3kc5c3`, and
`pini6v3liky8vhs22hyrnqdjfybm17zd`; NodeCtld and osctld were running
on each node after its switch.

The services switch installed system generation
`s6a5yqp8ihh67aliin0kjdp11s6rhqnp`, containing the `ebe4d8834`
API. The update helper returned failure because a payments timer ran during
a brief MariaDB connection interruption. After the database and API were
healthy, the same payments task succeeded on explicit retry; its failed
systemd state was cleared. The helper had stopped before its refresh step,
so `vpsadmin-devcluster refresh` was run explicitly and completed. The
cluster then reported running and ready on the bridge with storage topology.
The API, supervisor, nginx, NodeCtld and osctld services were healthy.

The database retained migration `20260924210000`, control row
`read_write` at epoch 2, and no unfinished transaction or active chain.
Authenticated freeze status returned HTTP 200 with `repair_ready=false`
and no blocking counts. A live headless browser login showed the safety
warning and epoch-2 review form, then returned without submitting a mode
change. An ordinary snapshot request through the updated two-worker API
completed without unlocking the process-local signer: chain 24 was terminal,
snapshot 5 was confirmed, observer intent 12 was terminal, and
`tank/ct/2@2026-09-26T09:53:59` existed on node1. The final freeze mode
remains `read_write` at epoch 2 so the user can try the control.

This refresh confirms the updated API/WebUI/Node packages run together in
the disposable cluster and that ordinary unsigned observer snapshots work.
The earlier bounded freeze trial used the prior runtime-equivalent package;
the new browser run checked the updated UI but did not repeat the mode
toggle. G1 child lifetime, full node quietness, verified scopes and repair
remain unproved.
