# Session devcluster demonstration

> Current refreshed result (2026-11-18): **delivered for lead acceptance** — [packet](postreview-2026-11-18/packet.md), [completion](postreview-2026-11-18/completion.json). Cluster running/ready; both fixture VPSes stopped by enforcement. Earlier sections below are retained historical snapshots.

The released brief is [design.md](../design.md#current-dev-cluster-demonstration--released-execution-brief-2026-11-17).
This record belongs to implementer0; root owns the main plan and state.

The normal fresh single/bridge start was invoked once at 19:52:12 UTC on
2026-11-17 through the installed stable command. Native session 57372 owns the
command. It completed with status 0 at 20:45:26 UTC (53m14s); the redactor also
exited 0 and the native session was joined. `start.sh` limits Nix to one build
job/core and redacts credential-related output. The stable host wrapper buffers
provider output while it is running;
an empty outer log is not a failed or stalled result. Bounded parent observation
replaced a setup-only Luna watcher whose handle messages arrived unreadable.

`preflight.json` binds the clean published sources, runtime/provider, local OS
staging identity and capacity. The only per-cluster configuration change is
`dns.enable=true` to `false`; the original private JSON remains with cluster state.
Mailpit capture remains enabled. No template alias, provider change or source edit
was made. The actual services runner descriptor declares 8192 MiB, 4 CPUs and
4 cores; bind the emitted runner configuration after it exists.

The selected reviewed template tree is archived in `templates-d42.tar`, with
393 file hashes in `template-bytes.json`. The exact site policy is retained as
`incident_escalation.rb` (SHA256
`f80804159bebf631501dceebfcd9db87842aed6cac7cabb2b38b7ec8a4bffd8f`).
All five incident families' CS/EN subject/plain/HTML fields were reconciled through
the public rake task before fixtures. All 30 DB fields match the reviewed source
(subject follows the parser's normal trailing-newline removal). API, supervisor
and database package loads independently report the exact policy digest. The
regular files are mode 0440 with the corresponding component owner; API,
supervisor and scheduler were restarted and are healthy. Both additive migrations
are installed. `loaded-inputs.json` and `guest-load.log` retain the proof.

Actual nodectld mail transport is `127.0.0.1:1025`, with Mailpit capturing on that
loopback port and HTTP 8025. No external SMTP was used. Initial capture count was
zero. The only simulated source events are the 20 retained nonfuture, whole-second
tuples in `events-final.json` (SHA256
`126ecd48f955c550e47b9376dfc57ea28f57ce711915d27c68accf430bca191f`).
They were saved before publishing to the normal node-scoped `vps_events` protocol;
source keys exactly cover the resulting 20 ordinary reports. These are synthetic
memory-pressure events, not claims of a real daemon resource diagnosis.

| Fixture | CS | EN |
| --- | --- | --- |
| Owner | test-user1 (ID 2) | test-user2 (ID 3) |
| VPS | incident-demo-cs (ID 1) | incident-demo-en (ID 2) |
| First ordinary report | 1 | 2 |
| Warning / source report | 7 / 6 | 12 / 11 |
| Confirmed stop / source report | 23 / 17 | 24 / 22 |
| Stop action / real Stop chain | 3 / 19 | 4 / 25 |
| Stopped MailLog | 23 | 24 |

The normal API created two 1 CPU/1 GiB/4 GiB VPSes, with no IP allocations, under
the dedicated seeded owners. Both create chains completed and node1 proved both
running before ingestion. Only the fresh demo's global mode changed to enforce;
site base limits remain 5/10 with no overrides. Ordinary mail was verified after
one event each, warning mail after five each, before publishing events six to ten.
All four summary actions are completed, all four mail states are sent, and their
mail transactions are done/status 1. Both Stop chains are done with every physical
transaction successful. Node1 independently reports both VPSes stopped. Both UI
counts are 10/10; callback-derived live limits/status correctly remain unavailable.
`fixture-final.json` and `node-final.log` retain these results.

Mailpit captured 24 incident messages (20 ordinary, two warning, two stopped), each
with plain and HTML bodies. Six later normal login-notification messages resulted
from authenticated UI checks; final inbox/SMTP accepted count is 30, with no SMTP
rejections. No messages were removed. Actual Mailpit HTML and Text views were
inspected for both languages and all three message kinds. `mailpit-paired.log`,
the rendered text and screenshots retain that evidence.

All 24 authenticated page visits passed across PHP/React, admin/CS owner/EN owner
and VPS/history/ordinary/stopped views. Notice links point to the correct source
report. Owner pages contain only their own fixture. PHP follows the owner language;
the React browser checks used English UI locale while the CS owner still received
Czech mail. `ui-auth.log` retains route evidence and screenshots show actual guest
data. All seven input repositories remain clean at their original heads.

## Browse the result

- [PHP UI](https://webui.aitherdev.int.vpsfree.cz/)
- [React CS fixture](https://newadmin.aitherdev.int.vpsfree.cz/app/vps/1)
- [React EN fixture](https://newadmin.aitherdev.int.vpsfree.cz/app/vps/2)
- [CS stopped email](https://mailpit.aitherdev.int.vpsfree.cz/view/52kxFGCNhkgDgIYonpdQIp)
- [EN stopped email](https://mailpit.aitherdev.int.vpsfree.cz/view/0AHqRQ34PZ2UTfA2Y1hGQl)
- [Mailpit inbox](https://mailpit.aitherdev.int.vpsfree.cz/)

Retrieve admin/demo-user and Mailpit login values from the session portal's
existing Accounts fields; no credentials are included here. The cluster remains
running and ready, with no pending applied operation. No source, default branch,
provider, SDK or production change was made. No reset, cleanup or lifecycle action
was taken. The site policy files and template DB reconciliation are explicit local
demo configuration, not a claim of declarative production activation.

## Retained setup corrections

The initial read-only SSH script supplied on stdin did not reach the guest through
the stable wrapper. File transfer plus ordinary SSH command arguments replaced it.
The first fixture CLI used the test suite's old API hostname and failed metadata
authentication before creating a VPS; a readback proved zero VPSes/reports. A private
copy of the declared test credentials now selects the actual cluster API URL,
preserving the original config. The event-plan guard compared a confirmation symbol
with a string and refused before writing tuples; the publisher refused the absent
plan. Both failed artifacts remain. The corrected `confirmed?` guard saved the exact
tuples before their first successful publication. No uncertain event or creation
command was blindly repeated.

The 100 GiB incremental disk plus 20 GiB shared floor, 48 GiB available RAM and
20 GiB shm operating allowances are prospective assessments, not measured peaks.
Initial free disk was 209,086,427,136 bytes, available RAM 67,249,452 KiB and shm
50,613,465,088 bytes. Existing shared use is included once in those free values.
Preserve all retained cluster/private KB/SMTP state on failure; no reset, cleanup
or session lifecycle action is authorized.

## Postreview refresh — 2026-11-18 (preparation; native window held)

The lead released the complete bounded refreshed-demo package under
[the postreview addendum](../design.md#postreview-verification-and-one-refreshed-demo-2026-11-18).
The preceding demonstration, failures and artifacts are historical evidence and
remain unchanged. New artifacts are isolated in `postreview-2026-11-18/`.
No reset, start, build, event or guest mutation has occurred in this phase.

Preparation binds the selected `sm3pyk` runtime and `xgghi0ln` provider, clean
backend `ee9025a8`, React `d26cfea0`, templates `125f132a` and declaration
configuration `1efed32a`. Without an OS worktree the provider selects local
`origin/staging` `ccd51ed38ebffa2e744f7f8847668bc2e3413378`; no fetch or source
registration was performed. The provider's actual composed outputs and complete
applied input/system graph are pending its authorized start. The accepted React
five-target package is reused for its original inputs; a read-only local
residency query found its prior standalone BFF output currently unavailable.
No package check or build was repeated to repair that observation.

Public status returned success for the old running/ready `single`/`bridge`
cluster. The complete recorded runner/state/socket/PID/ready tuple matches;
applied pending is null and no maintenance hold was reported. The intended
regular per-cluster configuration is preserved outside the reset directory in
an ignored, untracked mode-0600 private file, SHA256
`784e5d3b45d343068435cb931c464dff82d61a84b8a19c9cf692fa39d8cf21ef`.
DNS remains disabled, React and Mailpit enabled, and storage profile disabled.
Old applied envelopes, disks and WebUI credential bundles are not restoration
inputs; the intended regular configuration retains its seed-account settings.

The new exact template archive has SHA256
`b347d07901a2f50993b72eefae404d4f2d1f34080de0df589452fa132c209f75`;
the exact declaration has SHA256
`f3b4549ab502d40fe8bb72de6f4a22e1d9ec4dfdf8aa692ff5e25003a3df5e78`.
All 393 template file hashes are retained. Adapted local scripts use evaluation
memberships and collection summaries, actual fixture IDs, the Incidents routes,
the single migration, saved source hashes and bounded publisher attempt records.
The successful 16-file syntax batch is preparation evidence, not guest loading,
DSL activation, mail delivery or UI acceptance.

[Preparation facts](postreview-2026-11-18/preparation.json) and
[artifact hashes](postreview-2026-11-18/preparation-files.json) retain the exact
inputs, current capacity sample, scripts and remaining runtime facts. The sample
includes shared integration use once; available RAM is presently below the
eventual 48 GiB allowance, so it cannot admit a reset/start. Capacity, source,
generation, socket/applied state and address ownership must be refreshed at the
boundary after the lead returns the native window. Owner1's alerts lane and
owner4's WebUI lane must first return terminal PASS/input handoffs. No active
peer logs were polled and no check was duplicated. The one authorized reset is
unconsumed; canonical KB media/capacity and all old uncertainty remain parked.

### Final inputs and admitted execution — 2026-11-18 06:41 UTC

Root returned the exclusive native window with all required dependencies
accepted. The original preparation/manifest remain byte-exact. The compact
[final-input addendum](postreview-2026-11-18/final-input-addendum.json) binds final
backend `0117035f` and React `b1fb37b0`, retaining the actual d304 alerts and 011
PHP evidence separately and leaving literal 5aa1 consumer provenance intact.
Final backend hosted CI is pending and owned by root, not inferred successful.

Fresh admission passed with 170,173,456,384 bytes free disk, 57,770,332,160 bytes
available RAM and 37,839,179,776 bytes free shm. These include shared use once
and are boundary observations against the allowances, not measured peaks.
The exact old runner/socket tuple and non-pending applied state were verified;
this was the only active registered cluster. The selected local OS staging
remained ccd51ed3 without fetch.

The one authorized stable public reset was consumed at 06:41:58 UTC and exited
0. Supported public config initialization exited 0, then only the saved intended
regular configuration was restored. The normal public single/bridge start is
active under native handle 89743, observed by fresh installed-policy Luna/low
CLI handle 18202. No second reset, separate stop, private helper, old applied
payload restoration or unrelated cleanup was performed. Build/boot and loaded
source acceptance are pending; the selected provider's actual outputs will be
bound after the command terminates.

### Start terminal; React output provenance hold — 2026-11-18 07:01 UTC

The same one-reset/start wrapper completed exit 0 at 07:01:09 UTC (19m11s).
Parent native 89743 and fresh Luna observer 18202 are joined with exit 0;
read-only graph-query handles 39762 and 29092 are also joined. The observer saw
no unexpected local kernel compilation. Intentional runner 719334 and services/
node1 remain running. Public status is ready, and applied pending is null.
The provider's actual applied system/closure proofs and complete runner tuple
are bound in [start-terminal.json](postreview-2026-11-18/start-terminal.json).
This is successful command completion, not final demo acceptance.

Actual config is `/nix/store/127hdsydqcmz5ydnsqhkavzxcszk61rz-os-test-vpsadmin-devcluster-2026-10-30-oomd-abuse-policy.json`.
Its actual input graph has 6,707 derivations and 869 source inputs (private raw
SHA256 `fe6ac8654fd407541279583d4f86ce0d09fb5cf856d7f4519b23145933aa8c0d`);
the runtime closure graph has 1,831 paths. Private logs/config remain restricted.
An initial graph reader used the older JSON shape; its failure and zero-source
summary were retained and corrected from the same raw data without another build.

The config labels clean React b1fb, but both actual frontend/BFF build-info files
report `commit: unknown`, `dirty: true`, `source: unavailable`. Those bytes are
preserved. Both derivations consume the same cleaned source (BFF its `bff/`
subdirectory); all 2,835 retained files/symlinks match reviewed b1fb Git blobs.
This proves source binding, not full-b1fb output metadata or standalone package
equality. Root accepted this as an unresolved provenance limit and assigned
architect0 the packaging-contract recommendation. Load, fixtures and events are
held pending that assessment; no event plan or mail effects have started.
The actual backend common source also retains all 2,996 reviewed tracked files:
2,986 byte-equal plus 10 ordinary shebang substitutions with identical remaining
bytes. Ignored/generated files in its raw source payload are inventoried separately.
No claim that those generated files are reviewed source is made.

The start consumed no second reset, provider change, rebuild, downgrade or cleanup.
All historical preparation, d26/ee/d304 evidence, literal 5aa1 consumer provenance
and uncertainty outside this exact reset cluster remain unchanged. Successful
fresh guests remain running while the output-identity hold is assessed.


### Refreshed demo delivered — 2026-11-18

The current [packet](postreview-2026-11-18/packet.md), [completion](postreview-2026-11-18/completion.json) and [exact result identities](postreview-2026-11-18/result-identities.json) supersede the pending current-state passages in the historical preparation/start snapshots above. Those original bytes and failures remain retained. Root resolved the React hold by accepting the actual provider outputs as externally source-bound DEVELOPMENT packages: active nginx root/BFF executable bind exact0fb/jrc outputs,2835 cleaned-source blobs match reviewedb1fb, and unknown/dirtytrue/sourceunavailable metadata remains unchanged. No clean-release or standalone-output equality is claimed.

The sole authorized public reset/init/start completed exit0; no second reset or rebuild occurred. Actual backend011/Reactb1fb/templates125f/config1efe and selected local OSccd51 identities, full6707-derivation graph, actual systems/packages and runtime closure are bound in the packet. All seven source worktrees remain clean. Literal5aa1 SDK/export/KB provenance and actuald304 alerts evidence remain unchanged.

Ordinary template reconciliation proved all30 fields across five families and both languages. Regular component-owned0440 declaration files at actual configDirectories and normal restarts/package loads prove digestf3b4549a for API/supervisor/database; saved running-supervisor evaluations retain that digest. Exactly one20261030180000 migration follows20261006120000, obsolete20261115120000 absent. Mail delivery is capture-only to127.0.0.1:1025/Mailpit.

Two isolated CS/EN owners/VPSes were created through the ordinary API,1CPU/1GiB/4GiB/noIP. Create chains1/2 and independent physical-running evidence precede all source events. Cached is_running=NULL is preserved. The original create/failed effects-read/baseline failures remain; corrected no-effects proof and the actual packaged-Ruby offline argv control preceded the single guarded two-create continuation. Observer12870 reported INCOMPLETE/no observation despite CLIexit0; the explicit active-parent13816 exit0/join/command/log/time/effects receipt supplies the accepted fallback, not watcherPASS.

One saved20-unique-event plan was published once in three milestone ranges, with20 attempt markers and confirmations and no replay. The final result is20 source+2warning+2confirmed-stop reports,20 saved recorded evaluations,4completed/sent actions,2successful physical Stop chains29/35 and24delivered incident MailLogs. Node1 independently reports both VPSes stopped. Physical Stop transactions45/51 and all24 SMTP transactions are done/status1. Contributor snapshots remain bounded5shown/10total for stops.

First ordinary plain/HTML mail was inspected before later events, warning before events6–10. Final Mailpit has41messages:24incident+17login. All24incident messages have plain and HTML. Actual Mailpit HTML/Text views and screenshots were inspected for ordinary/warning/stopped in both languages. No messages were removed.

Authenticated acceptance covers24baseline views,8warning views,40unique final own views and4foreign-report denials across PHP and packagedReact. Current declared limits/counts, threshold links to Incidents, saved first-history values, admin/owner controls and owner isolation were inspected. Local Czech-denial regex and React asynchronous-loading assertion failures remain; only remaining views/settled denials were continued. [UI acceptance](postreview-2026-11-18/ui-acceptance.json) distinguishes passed views from failed/incomplete batches.

Final read-only native62579 exited0 and is joined. [Final health](postreview-2026-11-18/final-health.json) proves cluster running/ready/pendingnull, exact counts and clean sources. All owned command/utility work is terminal/joined; intentional runner719334 and services/node1 remain running. [Native effects](postreview-2026-11-18/native-effects.json) preserves actual failed/incomplete utility outcomes and item completion accounting. Private files remain restricted/ignored/untracked.

Root retains hosted CI observation/final acceptance and state.md. No hosted-success inference, production/default integration, registry release, canonical KB capture/staging, cleanup or session lifecycle action is claimed. The session stays open; capacity is available after delivery. Credentials remain only in the established portal Accounts/secret channel.

Current links: [PHP CS Incidents](https://webui.aitherdev.int.vpsfree.cz/?page=adminvps&action=incidents&veid=1), [React CS](https://newadmin.aitherdev.int.vpsfree.cz/app/vps/1/incidents), [React EN](https://newadmin.aitherdev.int.vpsfree.cz/app/vps/2/incidents), [CS stopped mail](https://mailpit.aitherdev.int.vpsfree.cz/view/6UorASrljwGRvw9thJP6sp), [EN stopped mail](https://mailpit.aitherdev.int.vpsfree.cz/view/4XTwanzfVtc0sIDu7a5Un6), [session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/).
