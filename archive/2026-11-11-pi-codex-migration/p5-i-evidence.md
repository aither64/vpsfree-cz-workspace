# P5-I domain codec and utility-boundary evidence

Status: source and focused checks committed; lead writing pass closed and D
index/commit window released. Source/fake package acceptance is pending the lead's
assessment; production writers and utility execution remain gated. Implementer3
retains fixes ownership.

Session: `2026-11-11-pi-codex-migration`.
Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-pi-codex-migration/dev-workspace`.
Verification base: `a74ae62bfb57cdb1858381a8c66855e2ab9f2b5b`.
Peer commits advanced D before the exclusive window. Final exact source range:
`a12c01ee4babf72cf0994d6b49f2f8b834e2be5e..e457834e23a2bda09e528ac8c532c16e912c33b2`.
The 28-path final manifest SHA256 is
`a7f519190d754581670aa89e7dad368ef33ba747dbc6bd3c37f75ffeebbb76ce`.
The index was empty before staging and after committing; owned paths are clean.
Peer edits remain untouched. Session/current, both absent environment values and
retained Sol/xhigh/workspace_write were rechecked before staging.

## Scope and implementation

Accepted brief: [TEAM-I addendum](pi-team-plan.md#team-i-addendum-production-records-and-utility-authority)
and [design acceptance](design.md#team-i-sufficient-production-codec-and-utility-authority-continuation),
followed by the lead's explicit P5-I source release. H0 and the independent P5
slice were already accepted at `23b35d5368a27bd189ef7b895dbbfbde4dc0d331` and
`7584b9077b84c4a7e40d6c8da13f9571d40c9126` respectively.

- Schema-2 Pi roster, monitor operation, communication aggregate and observer
  codecs use existing paths, locks and private atomic writes. Shared data-only
  reference/strict JSON helpers live in the existing lower monitoroperation
  package; import direction remains unchanged.
- Legacy schema-1 values/executors remain supported. Communication upgrades its
  single aggregate atomically while retaining old grants/messages/options/
  receipts/pending obligations; legacy delivery can continue only through its
  current-package `Schema2Write` admission before domain locks.
- `PiTeamWriteAdmission.WithPiTeamWrite` is a consumer port. Absent admission or
  a skipped callback refuses. Ready roster writes additionally require current
  read-only P2 proof inside outer admission, before team/file locks. An initial
  input ID alone is insufficient. Production composition is unregistered.
- First member assignment reserves the real original message ID and existing
  envelope/context/settings. Publication delegates only the original references
  to P2 after delivery/init ownership is released; no synthetic materialization
  input or direct P2 writer is supplied.
- Monitor utility create intent precedes an effect, with immutable original
  operation/policy/incarnation/input. Per-effect authority holds no short monitor
  file lock during native callbacks. Domain JSON projections do not fabricate
  runtime UtilityRef exports or a native engine.
- Utility status uses read/recovery admission. Original immutable report slots
  can become durable before callback drain. Settlement separately requires
  current source/input/resource/tool/callback/utility-exit proof. Cancel preserves
  receipts and unresolved command effects. Legacy quiescence cannot infer utility
  drain from missing Codex fields; Pi needs current utility verification.
- Communication reconciliation has Lookup only, preserves original IDs/settings,
  and never sends/reloads/configures as recovery. Terminal negative/Unknown remain
  held; revocation retains submitted obligations.
- Utility tools bind a distinct trusted caller. Only exact monitor status/report
  are allowed. Node `createMonitorTools` in existing `reporting.mjs` forwards the
  SDK nativeToolCallID and signal outside model arguments; report success requires
  the durable original event-ID string. No session_communication factory or
  retained-member utility identity is advertised. Go HostTools defaults to none.

## Exact owned inventory

The final source manifest is [p5-i-final-source-sha256.txt](p5-i-final-source-sha256.txt).
It has these 28 paths, including the final lead-pass prose:

```text
docs/pi-teams.md
pi-runtime/src/host-tools/reporting.mjs
pi-runtime/src/host-tools/reporting.test.mjs
portal/internal/communication/pi_records.go
portal/internal/communication/pi_records_test.go
portal/internal/communication/pi_recovery.go
portal/internal/communication/pi_recovery_test.go
portal/internal/communication/service.go
portal/internal/communication/store.go
portal/internal/monitoroperation/lifecycle.go
portal/internal/monitoroperation/pi_operation.go
portal/internal/monitoroperation/pi_operation_test.go
portal/internal/monitoroperation/pi_records.go
portal/internal/monitoroperation/pi_service.go
portal/internal/monitoroperation/service.go
portal/internal/monitoroperation/store.go
portal/internal/monitoroperation/types.go
portal/internal/pihosttools/team.go
portal/internal/pihosttools/team_test.go
portal/internal/pihosttools/utility.go
portal/internal/pihosttools/utility_test.go
portal/internal/progressobserver/pi_records.go
portal/internal/progressobserver/pi_records_test.go
portal/internal/progressobserver/state.go
portal/internal/teamruntime/pi_initial_assignment.go
portal/internal/teamruntime/pi_initial_assignment_test.go
portal/internal/teamruntime/pi_roster.go
portal/internal/teamruntime/pi_roster_test.go
```

No central session/main/preflight/metadata, P3 runtime/worker, P4 provider, P7
package/flake/pins or H0 source is included. Only these exact paths were staged
and committed in the exclusive window. Peer working-tree changes are not part
of this inventory.

## Verification and applicability

Cached exact D shell used throughout:
`/nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv`.
No current-flake development shell was evaluated during this final preparation;
P7 owns composition and lock inputs. Every Go command used `-mod=readonly`.

Fresh Luna/low watcher ran this six-package batch once against HEAD `a74ae62b`
plus the owned frozen 22-code-file manifest and concurrent peer source:

```sh
nix develop /nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv --command \
  go -C portal test -mod=readonly ./internal/teamruntime ./internal/agentteams \
  ./internal/monitoroperation ./internal/communication ./internal/progressobserver \
  ./internal/pihosttools -count=1
```

All passed. [Output](p5-i-domain-regressions.log); frozen
[manifest](p5-i-source-sha256.txt) SHA256:
`90b02b00a3edfbfbee170124390136e7582becb1acfa59b72b8293bfa70c651e`.
The full working tree was shared and dirty, so this identifies owned source and
base, not a complete immutable whole-package snapshot. Package timings in the
log are authoritative; the watcher's approximate wall-time report was
inconsistent with them and is not used. The watcher ran `dev-session current`
from the repository CWD and got no current session; the main agent reverified
from the bound session directory and reported this procedure gap to the lead.
No command was duplicated to repair the report.

Subsequent checks were limited to changed packages, using the same exact shell:

| Final affected inputs | Result / scope |
| --- | --- |
| Utility lifecycle/status changes | Full monitoroperation suite passed, 5.416s; pihosttools passed, 0.019s. |
| Required create intent / omission of unmapped native identity | Focused TestPi monitoroperation and pihosttools passed, 0.346s / 0.024s. |
| B1 native anchor forwarding and HostTools projection | Full pihosttools suite passed, 0.023s. |
| Shipped report/monitor factories | Node syntax plus all five reporting.test.mjs cases passed, about 0.190s. |

These results were captured in terminal outputs during implementation. No
unchanged six-package batch was repeated. Whitespace and Go formatting checks
passed for the owned source. Final frozen code bytes remained identical through
the writing pass and commit; only documentation wrapping changed. Node syntax
and factory evidence therefore remain applicable without a duplicate check.

Fixtures cover legacy/Pi roundtrip and mixed/unknown/duplicate/null refusal;
missing/stale generation admission before file creation; original input
immutability; InitialInputID-only ready refusal; first-real-assignment replay
and publication outside the team lock; utility cross-owner rejection; create
intent before a lost reply; UUID/32hex distinct operation paths; durable report
with callback still active; cancellation retaining input/settlement holds;
legacy communication pending preservation and continued single send; Lookup-only
lost-ACK/Unknown/negative recovery; observer owner/path separation; and inert
host factory identity/action refusals.

All own watcher agents and launched checks are terminal. No long integration,
VM, installed permission, model, credential or live lifecycle check was run by
this package. Combined final independent review remains lead-owned after all
intended deliverable source is committed.

## Integration handoff and remaining proof

| Owner | Required gate |
| --- | --- |
| P2 / implementer2 | Implement lock-safe current WithPiTeamWrite / read-recovery admission, final ready-proof validation, complete piTeamRecords map and package preflight over every retained store. Retain recognized schema-4 creation journal while any dependent Pi domain/utility record remains, beyond binding retirement. Prove actual older candidate refusal before enabling writers. No P5 central edit or optimistic metadata publication. |
| P3 / implementer1 | Actual distinct utility API/tagged shared mapping/receipt engine and UtilitySubmissionDigest export, owner/root separation, native first-input witness and per-effect grant checks. Freeze exact returned utility ref/input/settings digest in original domain record before Send; Bind is not reservation. Domain-only fixtures do not prove this engine. |
| B1 / implementer1 | Authenticated callback subject/native anchor/original Accepted witness and transport/drain proof before domain handlers; consume shipped status/report factory and optional approved HostTools projection. No raw handler advertising. |
| P7 / implementer0 | Package only implemented exports after its coherence proof; own current flake/lock/manifest/check exports and later docs entry links. |

The full target map remains
`{policy:1,roster:2,monitorOperation:2,communication:2,progressObserver:2,utilityReceipt:2}`.
P5's codec fixtures exercise schema-reader refusal; they do not replace an actual
old-candidate package transition fixture, retained-journal scan, native utility
execution, installed callback registration, or Launch-ready permission proof.
Missing owners refuse. Busy enqueue, automatic negative retry and fresh-reviewer
fallback remain unavailable. Retained independent reviewers remain supported;
mandatory review and reviewer independence are unchanged.

## Documentation, history and migration provenance

Feature/domain contracts belong in `docs/pi-teams.md` for developers/operators.
It describes schema boundaries, real first input, writer ordering, original
receipts and settlement without requiring session history. This session evidence
owns temporary heads, commands, source hashes and unresolved integration proof.
P7 owns later README/session-guide entry links; no duplicate rollout guide was
created. The lead read the full feature document, visible reporting/monitor
wording and evidence packet. Its context-owning writing pass closed with two
documentation line wraps; reporting module wording/bytes were accepted unchanged.

No database, conversation, history, retirement, converter, removal or default
switch migration is introduced. Communication's schema1-to-schema2 aggregate
upgrade is the intentional forward codec transition; old-package rollback must
refuse while its Pi obligations remain. All new writers remain unregistered.
No P5-I state was deployed, released or externally consumed by this package.
One logical P5-I source commit was made; full combined branch consolidation
and migration-lineage review remain with the lead/reviewer. No merge or push
was performed and no repository or machine claim was acquired.

Stable session URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/

## Final writing/index packet

Lead granted the exclusive D window after P2-C. Before staging, exact HEAD was
`a12c01ee4babf72cf0994d6b49f2f8b834e2be5e` and the index was empty. All frozen
code hashes matched existing evidence; only `docs/pi-teams.md` changed through
the writing pass. Its final SHA256 is
`f03f0e9e6af1189c0139cb2714049e3c459cbb30a3a0313a6f7e562e18707153`.

Commit `e457834e23a2bda09e528ac8c532c16e912c33b2`, subject
`pi: add admitted team records and utility domain boundaries`, has exactly the
28 paths above (3225 insertions, 30 deletions). Staged and committed blob hashes
were verified against the final manifest. Commit used a temporary message file
and normal `git commit --only -F ... -- <exact paths>`; no hook bypass was used.
No declared hook framework or active executable hook was present. Owned paths
were clean and the index empty after commit. No new check was launched.

The index window was immediately released through report_to_lead message
`031176f2-6b59-4c03-9509-a0948e0b4cc6`. The raw local commit receipt is
`p5-i-commit-receipt.json`. No own check/watch process is running. Await source/fake
acceptance; retained H0/P5 fixes ownership continues and no additional package
is queued or accepted. This packet makes no production readiness claim.

## Retained correction: original roster creation receipt

P2-TEAM-FENCE source inspection found the schema2 roster CreationID validator
using the UUID-or32hex message-ID pattern even though the accepted P2 creation
receipt reference is original64lowerhex. Lead confirmed the retained P5 fix:
no global ID widening, migration or deployed-state claim, and no change to
initialInputId, utility IDs or legacy Codex behavior.

The narrow roster edits are `portal/internal/teamruntime/pi_roster.go` and
`pi_roster_test.go`: use the existing64hex digest pattern only for CreationID,
correct the source-only fixture to the original64hex receipt, and exercise
exact unchanged UUID/32hex initialInputId values. Invalid32hex/UUID/uppercase/
wrong-length/space-suffixed creation references and64hex input IDs refuse.
No normalization or replacement ID is added.

At D `fa43219096e3e8b9e5002cb28efccadf73a1a2ce` plus these owned edits,
cached D Nix `go -C portal test -mod=readonly ./internal/teamruntime -run
'^TestPiRoster' -count=1` passed0.061s, with gofmt/whitespace checks passing.
Log: `p5-roster-creation-id.log`. No unchanged package/Node suite was rerun;
no index window or staging is assumed.

Diagnosis also found the same incorrect CreationID check in
`PiInitialAssignment.Publish` in `pi_initial_assignment.go`. Lead explicitly
extended this same retained correction to its one-line validator change and
existing `pi_initial_assignment_test.go` regression. That regression now reserves
each original UUID/32hex input before publication, passes the full64hex P2 receipt
and original input unchanged to the existing publisher, and retains the outside-
team-lock/native-witness refusal checks. Invalid UUID/32hex/uppercase creation
references and64hex input IDs refuse without invoking the publisher.

The newly affected first-assignment test passed0.053s under the same cached D
Nix environment with explicit `-mod=readonly`, on D
`fa43219096e3e8b9e5002cb28efccadf73a1a2ce` plus owned source. Command:
`go -C portal test -mod=readonly ./internal/teamruntime -run
'^TestPiFirstAssignmentReservesRealIDAndPublishesOutsideDomainLocks$' -count=1`.
Log: `p5-creation-publish.log`. Prior unchanged TestPiRoster0.061s evidence is
retained. No broad/Node repeat was run; Go formatting/whitespace checks passed.

Final exact four owning code/test paths:

```text
portal/internal/teamruntime/pi_roster.go
portal/internal/teamruntime/pi_roster_test.go
portal/internal/teamruntime/pi_initial_assignment.go
portal/internal/teamruntime/pi_initial_assignment_test.go
```

Manifest `p5-creation-id-source-sha256.txt` SHA256:
`7eb416d44fc68db45ea5dfb42258c7adf77e4bd20ca5c2da77f824159370fd9c`.
The complete retained correction is58 insertions/3 deletions. Owning feature
documentation already states that creationId is the original P2 receipt
reference; no product documentation, visible error, global helper, central/P3
source, format migration or deployed-state behavior was changed. The source-only
invalid fixture IDs were never claimed as a supported deployed contract.
The lead granted the short exact-path window. Final retained-fix commit:
`1eeecfb575220d7f8d152bc42b6b9e91c77c995b`, exact parent
`fa43219096e3e8b9e5002cb28efccadf73a1a2ce`.
Subject: `teamruntime: preserve original Pi creation receipt references`.
All four staged, committed and current file hashes match the manifest above;
the completed commit contains exactly58 insertions and3 deletions. Owned paths
are clean and the post-commit index is empty. Normal tempfile `commit -F`
and exact `--only` paths were used; no declared hook framework or active
executable hook was present and no bypass was used. All peer paths were excluded.

Before committing, current/env/retained roster and exact parent/empty index were
verified. The existing digestPattern was present in that committed parent.
An isolated git archive of the exact parent with only these four frozen files
compiled successfully under cached D Nix with `go -C portal test -mod=readonly
./internal/teamruntime -run '^$'`:0.021s, no tests run. This proves the correction
builds without uncommitted peer inputs; it does not repeat the accepted scoped
behavioral checks. Log: `p5-creation-id-committed-build.log`; disposable source
copy `/tmp/p5-creation-committed-parent-zwv33b00` is recorded in
`p5-creation-id-committed-snapshot.txt`.

The index window was released immediately through report_to_lead, with exact
head receipt message `c35d5ba4-6090-46da-b916-c0bd4cac8f31` and raw local
`p5-creation-id-commit-receipt.json`. No partial push/merge/live action occurred;
all own commands are terminal. The coherent retained correction is reported for
lead acceptance; H0/P5 fixes ownership continues and capacity is available after
acceptance. No next execution package is queued.

Exact observational path handoff to P2 corrected an earlier shorthand:
roster uses `codex-teams/<basename(workspace)>-<first8 SHA256 bytes in hex>/`,
through `userstate.WorkspaceDirectory`; monitor/communication/observer use the
full64hex workspace SHA256. The communication codec supports mixed Pi/Codex
and cross-session pairs within its aggregate workspace, and rejects Pi endpoints
from a different workspace. Retired/terminal records remain codec obligations
while present; no live binding filter is part of these readers.

## P5-PREFLIGHT-HELPER pure communication validation

After accepting CreationID correction `1eeecfb575220d7f8d152bc42b6b9e91c77c995b`,
lead confirmed capacity and released this bounded two-file helper package for
P2-TEAM-FENCE's missing pure legacy/union validation seam. Session/env/retained
roster and repository guidance were verified; source remains in D.

Exact owning paths:

```text
portal/internal/communication/store.go
portal/internal/communication/pi_records_test.go
```

`ValidateCommunicationRecord(data []byte, workspace string) error` bounds raw
bytes by existing maxStateBytes, unmarshals through the existing private
state.UnmarshalJSON schema1/schema2 decoder, checks schema1|2 and exact workspace,
then calls existing state.validate. Existing imports and error text are reused.
No new Store, file access, lock, native operation, writer, schema rewrite or
parallel legacy validator exists in this path. Retained legacy payload/null
semantics and current schema2 strict decoding remain with their existing owners.

P2 caller still checks bounded private files, expected paths and ownership;
DecodePiCommunication remains the typed schema2 Pi endpoint/owner extractor.
This pure codec helper does not authorize a package transition, relax the
orphan-schema2 rule, provide a Pi fence owner or register any live writer.
Scanner/main source and package/retained-journal gates remain P2/lead-owned.

Focused fixture builds a real retained pending legacy message with explicit
null options/receipt and a mixed schema2 Pi aggregate. It checks unchanged
legacy values/bytes; valid Pi; wrong workspace/version/size; duplicate/unknown
schema2 fields, null Pi identity, legacy missing grant/delivery identity, unknown
legacy fields and trailing JSON refusal; and an empty scratch directory after
all validation calls (no workspace/state/lock creation).

On committed base `1eeecfb575220d7f8d152bc42b6b9e91c77c995b` plus these owned
files/current peer source, cached D Nix check
`go -C portal test -mod=readonly ./internal/communication -run
'^TestValidateCommunicationRecordDelegatesWithoutFilesystemEffects$' -count=1`
passed0.104s. Log: `p5-preflight-helper.log`. Go formatting and whitespace checks
passed. No unchanged full/Node suite was rerun; no native/auth/model/lifecycle
action ran and no index window is assumed.

Exact two-file manifest `p5-preflight-helper-source-sha256.txt` SHA256:
`8e5ec9a77596663aee6d5458fb3f06dc6e69de71977212526579041e5b39d4e6`.
The source is85 insertions across those two files. No product documentation or visible wording change is
needed for this pure delegate; caller responsibilities are unchanged. No
migration, deployment or native readiness is claimed.

Final helper commit: `0a647bdfcdfbf900b614cec7935f147dba79997d`.
Exact parent: `74c5646455e1e40f03732347c5eb567dd90d8fbc`.
Subject: `communication: expose pure retained-record validation`.
The lead granted the sole short index window; fresh binding/env/retained roster,
exact parent and empty index were verified before staging. The unowned union
decoder in communication/pi_records.go, state.validate in communication/service.go
and shared strict decoder in monitoroperation/pi_records.go were byte-identical
across the checked base, committed parent and current source. Dependency hashes
are recorded in `p5-preflight-helper-committed-dependencies-sha256.txt`.

An isolated git archive of exact parent with only the two frozen owned files
compiled under cached D Nix using `go -C portal test -mod=readonly
./internal/communication -run '^$'`:0.020s, no tests run. This proves no
uncommitted source dependency without repeating the accepted focused behavioral
check or an unchanged broad suite. Log: `p5-preflight-helper-committed-build.log`;
disposable copy `/tmp/p5-preflight-committed-parent-9m4ukl51`, recorded in
`p5-preflight-helper-committed-snapshot.txt`.

Exactly the two owning paths were staged/committed; staged, committed and current
hashes match manifest
`8e5ec9a77596663aee6d5458fb3f06dc6e69de71977212526579041e5b39d4e6`.
Normal tempfile `commit -F` and exact `--only` paths were used. No declared hook
framework or active executable hook was present; no bypass was used. Owned2
paths are clean and the post-commit index is empty. P2/P3/P6 and all peers were
excluded; no partial push or live claim was made. The index window was released
immediately via report_to_lead `c6590853-2c83-48a1-adf1-809af463ac62`; raw
receipt is `p5-preflight-helper-commit-receipt.json`.

Committed export handoff to implementer2 used message
`f1557b26-0106-4e0b-b640-4b75653efb59`. Source package is reported for lead
acceptance; H0/P5 fixes ownership remains and capacity is available after
acceptance. No additional package is queued. All own commands are terminal.
