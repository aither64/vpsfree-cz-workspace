# KB closed-client fixture — affected final review packet

Source frozen for lead's affected review; no push/full source suite/CI request.
Owner3 owns source/Git/follow-up. Lead is sole CI observer; no provider polling,
retry or dispatch occurred. No images, guests, captures, dependencies, old-state,
claim, socket, registry, lifecycle or default-branch operations.

## Failure and bounded diagnosis

Authoritative failure: Managed43531750327 attempt1/head d41870f8e0ee3ccbec4b0ebfbefef1df0f7f9f4e,
job132250903127, Check repository failed. First failure is
RunnerSessionTest#test_first_valid_stop_notifies_once_when_its_acknowledgement_hits_a_closed_client,
tools/test-machine.rb:1025. Full machine group45/1443 had1failure0errors. Native
log also reports secondary fixture cleanup timeout1117. Integration preparation/
run/evaluation were skipped; artifacts empty. Ordinary Check43531750291 succeeded
on the same head. Neither is rewritten as acceptance of the failed Managed run.

Exact run/jobs/failed-log/artifacts are retained in
ci-parent-observation/kb-managed/. Failure log SHA256
b2b9dd187d7d3e7cee3e372c198fd9fcf5149d8be06ccc556abbdcf602df1f84.
No remote failure.json was available, so the historical captured tuple and exact
field transition are unknown. Do not claim a proved pre-exec/helper/argv mechanism.

The first assertion authenticates a full /proc snapshot immediately after spawn,
before the existing ready-marker barrier. A second full read in runner_matches?
can refuse a different startup sample. No invalid/valid stop request or closed-
client exchange has occurred at that line. This is a fixture ordering assumption;
there is no observed production control or exactly-once shutdown failure.

A bounded local readiness guard around the actual first full authentication
rejected original source: nativeexit1,1test/1assertion/1failure. It observed
published_ready=false, native_full_match=true, changed_fields=[] in this sample.
Thus it proves the premature acquisition boundary, not the exact CI transient.
Its normal directly-owned fixture cleanup completed with no secondary error.

## Minimal correction and focused proof

Only tools/test-machine.rb changes,3+/1-: retain the initial tuple for existing
strict failure cleanup; after the existing ready barrier, refresh the tuple and
perform the SAME full runner_matches? assertion. Exact directly spawned PID,
published control tuple equality, native real-socket EPIPE, invalid-request
refusal, first/repeat stop, one machine stop, retained-child/claim checks and
ordinary exit/resource cleanup assertions remain intact. No sleep/retry/assertion
weakening, runtime schema/control change or production source change.

Untracked readiness guard on corrected source PASS1/55 and observed
published_ready=true/native_full_match=true. The original closed-client case plus
three existing nearby shutdown cases PASS4/213. Syntax and whitespace PASS.
Keeping the original early cleanup sample was rechecked with final guarded case
PASS1/55/11.332seconds; actual case runtime0.608seconds. Raw before/after/final
native logs, argv/exit/elapsed, test-file SHA256 and guard are retained under
nov14-ack-loss-evidence/. Guard changes no production code and runs no guest.
No broad/full source-suite rerun was made for green.

## Exact final source/history and scope

Repository git@github.com:vpsfreecz/vpsfree-kb-contracts.git, worktree
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/vpsfree-kb-contracts.
Base cb7825245ea786fb0f51c469d1a7dc5c6a1ececc. Final clean local head
edf5c326d253e750ad84ca61994ff3275ba4744c, tree
4c13b7548ad8a93b11e65dab31f3da25b16e7897. Tree equals the independently retained
standalone fix and the quick-checked final test blob. Source delta from published
d418 is only that one fixture. Full final series:

1.91d349c8da837d26a45db426c154fe24a988c9e4 — corrected runtime repair.
2.edf5c326d253e750ad84ca61994ff3275ba4744c — one final backend pin.

Normal Nix git commit -F followed by normal fixup rebase completed0/no hook bypass.
No hook framework is declared; saved instructions/settings unchanged. Standalone
fix5cb3cb9 source and originald418 preserved under refs/review/.../nov14-ack-loss-fix
and nov14-ack-loss-d418. Existing consumed7bdee/56d/review/K1 refs and all failures
remain. Final history has no obsolete follow-up/fixup or repeated pin commit.
No migrations. All five pin files and entire lock graph are byte-identical to
accepted d418: backend7919441ccb8e9587ad0afc84674b074ca9c5a880, unchanged OS/other
nodes/edges. No baseline refresh, fingerprints, prose, scenarios or media changes.

Evidence: committed-packet.json, fold-provenance.json, final-series.txt,
final-range-diff.txt, final-source-fix.diff and full-base-to-head.diff beneath
nov14-ack-loss-evidence/. Existing original all4lane review and K1 closure remain
scoped to unchanged runtime; this fixture delta requires lead's affected final
assessment before any full535suite/new hosted push. Historical full535.78s pass
is not claimed for the new head. Runtime/strict/media acceptance remains separate.

Requested disposition: assess this narrow fixture timing correction and explicit
whole-series/no-migration/pin-graph preservation, then authorize only the next
required verification/publication scope. No request for new product permissions.

## Final review and feature publication

Lead reports retained reviewer0 completed final affected all4/HIGH review exact
cb782..edf5/tree4c13, no Blocking/Important/Advisory findings, complete history/
no-migration/pin/runtime/doc conclusions satisfactory. Report retained at
nov14-ack-loss-review.md; historical CI tuple remains explicitly unproved.

Normal SSH feature push completed0 with actual fresh d41870f8lease. Independent
afterproof confirms remote edf5c326d253e750ad84ca61994ff3275ba4744c and unchanged
mastercb7825245ea786fb0f51c469d1a7dc5c6a1ececc. Comparison refreshedcb782→edf5.
Old refs/failure evidence retained; no default integration.

One initial automatic provider inventory: Managed43539527454/workflow336079991/
attempt1/job132276549208 queued; Check43539527756/workflow330789667/attempt1/
job132276550196 in_progress. All old branchruns terminal; no cancellation.
Full inventory/jobs/brief saved under nov14-ack-loss-evidence/. Lead now owns sole
active-parent observation; owner3 launches no observer and makes no further polls.
No local full535repeat, manualdispatch/retry, images, guests, captures or oldstate
operations. New exacthead full source/hosted verification is pending automatic CI;
source publication/review is not runtime/strict inventory/media acceptance.

## Terminal acceptance interpreted from native evidence (offline)

Current exacthead edf5c326d253e750ad84ca61994ff3275ba4744c/tree
4c13b7548ad8a93b11e65dab31f3da25b16e7897 has successful automatic
Check43539527756 attempt1/job132276550196 and
Managed43539527454 attempt1/job132276549208. Retained checkout `git log -1` lines
independently show exactedf5. Use terminal checkpoint-2 jobs forCheck and
checkpoint-4 run/jobs/terminal-proof forManaged; earlier summary.json snapshots
are nonterminal history, not current authority. No new provider call was made.

Both actual source commands are `nix develop --command bin/check --allow-missing`.
Each log reports runtime109runs/1304assertions/0failures/0errors/1skip, and
machine45runs/1495assertions/0failures/0errors/0skips. Other source unit groups
complete without reported failures/errors; exact totals/loghashes are in the
coverage JSON. The one runtime skip is explicitly retained: these nonverbose
logs do not identify its name/reason, so host-specific skipped coverage is not
claimed. No local rerun was performed to expand that evidence. The formerly
failing machine group now passes; oldd418failedManaged remains failed history.

Managed native command was `./test-runner.sh test --state-dir
"$TEST_RUNNER_STATE_DIR" --fresh --jobs auto`. Completion records, not selection
or job status alone, prove these actual script successes:

| Suite | Successful script IDs | Successful example lines |
| --- | --- | --- |
| kb/gre | tunnel | 3 |
| kb/firewall | iptables, nftables, firewalld, nixos, ufw | 5 |
| kb/guix | reconfigure | 5 |
| kb/kvm | networking, platform-defaults, storage, nfs-locking, libvirt | 17 |

Native final totals:12scripts across4tests/suites in1727.4seconds,4tests successful;
all12distinctscript successful lines and30distinctexample successful lines are
preserved with names/times/logline numbers in offline-terminal-coverage.json.
Evaluate and summarise actions explicitly complete success; cleanup action logs
`Removed test-runner state directory: /tmp/os-test-runner-1296704888-43539527454-1`.
Prepare/Run/Evaluate/Summarise/Cleanup/Complete runner allsuccess; uploadfailure
logs is expectedskipped. Native log extraction exits0 for both runs.

Source/input scope: exact committed2commit cb782→edf5 series91d349runtime +edf5
solepin, no obsolete fixup/repeatedpin/no migrations; accepted backendpin7919441,
OS6bdf458 and all other reviewed lock nodes/edges unchanged. This is source and
managed-page-suite acceptance at that snapshot. It does not establish the original
four approved CS/EN VPS-list PNGs, strict exported/fullmedia validation, visual
acceptance or current finite publicbridge capture/start/stop qualification.
Original incomplete runtime/claims/socket remains untouched; explicitly discarded
services-root cannotresume. No productionKB write, defaultmerge/deployment or
session lifecycle action occurred. Templatesunchangedbf327 remain accepted.

Raw authoritative evidence: ci-parent-observation/kb-fixed-{check,managed}/
complete.log with terminal jobs/checkpoint receipts, and Managedterminal-proof.
Offline compact extraction: nov14-ack-loss-evidence/offline-terminal-coverage.json.
This final interpretation used only retained files; no source/Git edit, test,
CIrerun/dispatch, providerquery or runtime/guest/image/claim/lifecycle action.
