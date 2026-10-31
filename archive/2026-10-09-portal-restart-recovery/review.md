# Independent restart recovery review

Reviewer: `/root/review_restart_recovery`, fresh standalone fallback selected
from installed `lead_reviewed/reviewer`, GPT-6 Astra / xhigh, read-only.
High risk; general, architecture/repetition, scope/proportionality and
risk/compatibility lanes. No retained session roster exists.

Initial committed review covered codex-web `7dab763..a6a6b78f`, dev-workspace
`6626251..a61cda65`, workspace `87296b1..68a27a1c` and configuration
`1f35699..763f3b95`. Complete sole-commit feature series were coherent, with no
obsolete history, repeated pins or database migrations. Private recovery schema
1 and ledger path import were not merged, released, deployed or externally used.
Supported stable dispatcher and retained MCP calls select the current package;
direct historical package invocation remains outside supported rollback.

| Finding | Severity/lane | Remediation |
| --- | --- | --- |
| Existing watches reconnect with unconditional native resume | Blocking, risk/architecture | Gate implicit resume in the generic client and supply exact durable socket-generation permission for portal and observer. Cover live watches in native fixture. |
| Saved portal queue receipts prevent runtime readiness | Blocking, general/risk | Add known-submission proof accepting verified native queues, preserve resolved/idle retirement gates. |
| Cold team assignment leaves prepared send permanently unresolved | Important, general/risk | Prove the prepared-send/queue pairing through queued or started identity/text; preserve options/context and retire both on deletion. Test observation and lifecycle without browser acknowledgement. |
| Completed Continue receipt reused after later stop/socket recovery | Important, general/risk | Retire after successful root activation; clear stop/new epoch; retain failed activation receipt. |
| Held wrapper loses attachment queue deletion completion | Important, general/architecture | Forward the existing optional completion and reconciliation methods. |
| Helper transport failures become permanent | Important, general | Carry typed transport distinction as diagnostic/exit 75 through helper and coordinator; test retry and permanent refusal. |
| Unfinished creation renders recovery composer and fails CI | Important, general | Gate controls with retained-ready creation/receipt predicate while preserving stopped ready-session draft. |

All findings accepted as defects. The related all-lane rerun covered codex-web
84382a56, runtime b313879b, workspace 589ebdf7 and configuration 2e38ffd3.
Six initial defects are resolved; transport propagation remained incomplete.
The reviewer also found a Blocking hot-to-cold retry path that bypassed an
existing accepted send receipt and queued it again.

The requested narrow corrections use existing ReconcileSend/WithOptions before
cold queueing and check prior send state atomically with queue reservation.
Accepted/submitting attempts cannot become another native submission; exact
nonsteered prepared-send delegation remains supported. Loaded discovery,
metadata, materialization and final root/member rechecks now preserve transport
classification separately from positive identity mismatches. Focused regression
tests cover these boundaries. Main-owned verification of these direct fixes is
sufficient under mandatory review steps 9–10; no new public API or broader
design is introduced.

The rerun explicitly confirmed coherent whole-branch history, consolidated pins
and sound migration lineage: no database migrations or transitional state schema
versions. Stable selected-package CLI/MCP dispatch preserves the supported live
switch contract. Direct historical package invocation is outside that contract.

Advisory verification limits are accepted and retained: the native fixture tests
the reusable client with real native storage and mock inference, the Ruby
fixtures cover canonical CLI recovery, the VM covers actual user-service boot,
and browser status transitions are mocked. The corrected native fixture also
verifies its exact original history marker. There is no single native end-to-end
portal/CLI fixture, and aitherdev will not be rebooted. Do not claim those broader
conditions from the separate fixtures. Final long checks passed; results are in state.md and deployment evidence is
in rollout.md. Final fixture corrections were bounded setup fixes inspected
directly under steps 9–10, with no application/public-contract change.
