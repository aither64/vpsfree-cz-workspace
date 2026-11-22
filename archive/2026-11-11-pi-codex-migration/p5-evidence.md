# P5 independent team policy/delivery source

Owner: implementer3. Lead released the sufficient independent source slice in
pi-team-plan.md and design.md after H0 acceptance/capacity. H0 fixes ownership
is retained; no extra TEAM-I/codec/utility implementation package is accepted.

## Current status and exact scope

Twenty additive files, 1400 lines total including technical documentation and
fixtures. Lead writing pass is complete and the coherent tested P3 core is committed as
`daa780d1781df025aa918970310f4fb0f5f66a83`. P5 committed as `7584b9077b84c4a7e40d6c8da13f9571d40c9126`, parent
`f8cd2941626eac5fbe8e12c4e5a3fee9e309735a`, in the lead-granted D window
after P4. All20 final hashes matched before staging; exactly those20 paths
were staged/committed with normal git commit -F tempfile --only exact paths.
No declared framework, active non-sample hooks or core.hooksPath. Index was
empty before/after, owned paths clean, and D window closed promptly for P6.
First D source checkpoint: `4f390101de7ca5047d9e41faa0b483088d591185`;
full regression checkpoint: `67e08f2f10faa288aefb7e97e2d3eb19d8819eb6`
plus P5 source and concurrent uncommitted P3 dependency. P5 content is frozen
in `p5-source-sha256.txt` for these checks; update it after any writing fix.

Owned paths:

- `portal/internal/teamruntime/pi_{types,policy,delivery,reporting}.go` and tests;
- `portal/internal/agentteams/pi_policy.go` and test;
- `portal/internal/monitoroperation/pi_{types,policy}.go` and test;
- `portal/internal/communication/pi_delivery.go` and test;
- `portal/internal/progressobserver/pi_policy.go` and test;
- `portal/internal/pihosttools/team.go` and test;
- `pi-runtime/src/host-tools/reporting.mjs` and fake test;
- `docs/pi-teams.md`.

No existing executor, store/codec, central composition, P3 worker/transport,
provider, H0 or packaging file edited by P5. No new ledger, registry, scheduler,
daemon, grant, migration, history conversion, default/backend switch or writer.
No live service, auth/model call, utility launch, activation, merge, deployment
claim or session lifecycle operation.

## Source and policy meaning

PiAdmission owns current admission/locks through its callback. Structural
identities do not confer authority. The delivery adapter calls the native port
at most once and distinguishes held/unavailable from attempted. Raw native
result/error are preserved; interpreted outcome remains Unknown on missing or
contradictory evidence. Explicit reports use existing assignment envelopes and
ActionContext; no final answer is forwarded. IDs retain exact UUID/32hex bytes.
Retained reviewer/model/effort/instructions/access remain saved selections, with
installed execution policy reported separately.

Inert host and worker factories bind the host-captured caller outside model
JSON. Unknown/duplicate/identity fields refuse. Utility handles stay distinct
from retained-member handles and launch is hard unavailable. Communication uses
only a current read-only existing-grant projection under its owner's locks;
missing typed endpoints refuse. Observer policy retains State.Due and rejects
unavailable/stale/wrong-generation activity, excluding observer-only work.
None of these pure projections writes a new backend record.

## Checks and command effects

Pinned environment: prior exact D shell derivation
`/nix/store/51fz459vcnqki0pl4jabk67f926yh2pz-nix-shell.drv`.
Go commands explicitly set `-mod=readonly` on current source.

- First focused Go TestPi fixture watcher passed in 5.5s;
  `p5-first-go.log` records teamruntime result.
- Final focused `go -C portal test -mod=readonly` for teamruntime, agentteams,
  monitoroperation, communication, progressobserver and pihosttools with
  `-run '^TestPi' -count=1` passed. Fifteen top-level new Go tests include
  table/subcase coverage of caller/scope/generation/retirement/materialization,
  held/cold/busy states, one-send/raw result/error, original-ID/native receipt
  replay/conflict fake, explicit report, strict tools, grant revocation,
  observer staleness and utility snapshot/slot/settlement refusal.
- Worker Node test: `node --test pi-runtime/src/host-tools/reporting.test.mjs`,
  3 tests passed in 0.22s. Stable payload, forbidden authority, invalid IDs,
  unavailable/held/missing/contradictory outcomes and cancellation checked.
- Complete existing Go suites for those same six packages passed once under a
  fresh installed-catalog Luna/low full-access watcher in ~20s.
  `p5-go-regressions.log` has exact package results. No command remains running.
- All owned Go files formatted with repository Nix tools; owned whitespace
  checked. No hooks bypassed or Git index written.

Current-source nix develop failed before first formatter execution because the
concurrent partial P7 flake supplied piWorker before workspace-portal.nix
accepted it. Its implicit lock evaluation is the likely source of the Pi lock
node addition identified by P7; pre-command status had no flake.lock change,
but no stronger process-level provenance is claimed. P7/lead were notified;
P5 did not explicitly update, restore or stage that graph. Cached exact shell
then formatted successfully and avoids current-flake evaluation. Continue that
until P7 reports coherence. Initial report calling the failed formatter
formatted was corrected promptly.

Watcher policy: selected package
`/nix/store/9hr3ppqzzwb12x51vwjasw8hq0ka7dab-dev-workspace-0.2.0`, catalog
`f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d`, separate
fresh Luna/low operation utility, danger-full-access/never, outside roster.

## Integration handoffs and holds

P3 confirmed exact UUID/32hex support and Accepted receipt fields: original
ClientUserMessageID, native accepted user-entry TurnID, no steering/queue,
nil error after durable witness/receipt. P5 does not edit its shim or framing.
Architect1 confirmed Lookup belongs under central read/recovery admission,
permitting held/busy original outcome reads without load/resume/replay. P5
exposes the frozen native Lookup port and adds no authority-bypassing wrapper.

Impl1 and impl0 received concrete callback/check/docs handoffs. Central-owner
message `82f23a9d-2b81-4b44-a231-92a4320e5096` delivered successfully after
exact-ID retries through transient shared session mutation refusals. Impl2
confirmed original-reference Lookup uses read/recovery admission. Its now
released P2-C source/fake PublishMemberReady owns transition/runtime EX then
team admission; callers enter with none of those locks, outside WithDelivery
and after releasing delivery/init ownership. P5 calls no publication API, so
this integration constraint changes no final P5 source/prose hash. No peer accepted new work
from these current-package clarifications.

Four required live gates remain: P2 member materialization/publication and
existing-record variants; P3 authenticated callback/native witness; distinct
utility authority/launch receipt/settlement; central registrations and P4 applied
model policy. TEAM-I codec proposal is not implementation authority. Installed
team/utility readiness is not claimed. Lead owns whole-deliverable final review
and any later cross-process checks, integrations or deployments.

## Documentation and history

`docs/pi-teams.md` is the authoritative developer/operator explanation of this
source boundary, policy invariants, errors/outcomes, recovery and remaining
live gates. Session-specific check facts remain here. P7 has the entry-link and
Node check request; no edit to overlapping guides. Lead main-agent writing pass
completed before commit: docs use component names instead of private package
labels; the reporting description uses a straight apostrophe. Hash comparison
confirmed only docs/pi-teams.md and reporting.mjs changed; all checked Go files
are unchanged. Post-pass Node syntax and all 3 factory tests pass. Prose SHA256:
`5bb37b72e421d195d8ed937f871d40ada2a246c6e2f3cf0d09f7dd2564945179`;
reporting module SHA256:
`43a04494914654542542ec7a2eb5e37afc5f6e46d801ccc66ee78cebbe7fafce`. No persistence migrations or
rewritten applied/deployed history. No P5 source has been released/deployed or
externally consumed. Full combined branch review remains lead-owned.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>

## Completion report

The independent source slice is ready for lead acceptance at the exact commit
above. Go15 top-level new tests plus all six existing package suites pass;
Node3 factory tests and post-prose syntax pass. All evidence applies to unchanged
P5 Go source and the final prose hashes. No migrations or obsolete transitional
implementation were introduced. The parent includes the committed P3 core and
P4; production native callback/Bind integration remains owner work. Final
combined independent review and later released cross-process verification
remain pending. No feature publication, merge, deployed lineage, physical
machine ownership or live readiness claimed by this package.

Capacity: P5 reported for acceptance; H0/P5 follow-up/review fixes retained.
Available for a lead-allocated continuation after acceptance; no TEAM-I/new
package accepted or queued by this completion report.
