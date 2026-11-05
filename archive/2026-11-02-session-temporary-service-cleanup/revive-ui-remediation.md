# Completed archive history and fresh revival confirmation

Local final head `7302f4dc961ded7c768733e25ec39e3c603e093b`, tree `934f92ba1bc27675161f315ae0a8835ff1d7d8f3` is complete, quick-green,
clean and **unpublished**. Runtime Git lane returned. Await lead's direct inspection
and the same reviewer's affected general/risk review before any native/CI run.
No push, pin update, build, copy, claim, deployment, default integration or session
lifecycle action occurred in this remediation.

## Causal evidence and limits

Observed native CI3d76 archive evidence (A owns lifecycle causal inventory):

- Same archived receipt61fa2869... passed statecomplete/currentTarget.archived
  assertions at job-archive.log5585–5588, then archive location/branch/recovery
  hashes passed. Fresh revive reached submit phase; the dialog had been visible,
  same-page navigation occurred and the submit became hidden. No revivePOST,
  no pageerror and onlyGETs were captured at5606–5628.
- The raw operation/details callback bodies are NOT logged in that run. The
  empty pending state follows archived-page controls and template conditions;
  it is not a saved details JSON observation.
- journalExpected=true on the historical completed receipt is SOURCE-NECESSARY:
  the journal retry applies progress options (operation_state.go329), retry
  preserves those Options (server.go3122), successful runLifecycleJob copies
  started and changes terminal state/phase/timestamps (server.go3238), and the
  public projection does not clear Options. A verified this retained contract.
- The native registered-service scenarios are the NEXT subtest and were NOT
  reached. Nativecreation success is independently scoped3d76 evidence only.

The actual shipped UI connects those facts:

1. openLifecycleConfirmation(revive) reads that completed archive receipt and
   calls showLifecycle for any non-idle history.
2. Old showLifecycle assigned pendingLifecycle=archive from journalExpected,
   despite the receipt already being complete.
3. A normal details read confirms no pending journal and archived location.
   reconcileCompletedArchive sees the synthetic pending flag and reloads.
4. Navigation removes the fresh revival dialog before submission.

A deterministic regression mounts the SHIPPED target-state, lifecycle display,
confirmation, revive-submit and details/read-ownership handlers. Before the fix
it produces exactly an unwanted reload; the genuinely pending archive completion
control already passes. This proves the mechanism without using a later green
native retry as causal proof. All involved old lifecycle functions were byte-
identical to pre-featurec218. The mechanism therefore predates this feature;
the exact native callback ordering was not directly captured. The receipt
contract remains unchanged.

## Narrow correction

One condition in showLifecycle prevents completed history from assigning a new
pending flag. It leaves existing pending state intact, keeps history displayed,
preserves receipt journalExpected/options and ordinary journal/retry semantics,
and retains genuine active archive completion/reload. No receipt, Ruby, Go,
public endpoint, schema, ownership or new state/reconciliation framework changed.
No product prose changed. Additional reusable docs were not useful for this UI
contract restoration; evidence and diagnosis belong in this session receipt.

The two shipped-handler controls prove fresh revival remains open through details
and its explicit submit reaches revive with the confirmed target; history still
displays Archive complete and journalExpected remains true. A genuinely pending
archive still reloads exactly once when details confirm completion.

The EXISTING native helper now records only whitelisted operation state/phase/
journalExpected, details.pendingLifecycle and target lifecycle/location/archived,
plus8main-frame path/timestamps and final body.dataset values. It retains at most
16state observations and the existing1500ms failure diagnostic budget. No
credentials, URLs with query strings or raw private response bodies are logged.
The historical missing-callback limitation remains explicit; no new harness or
native rerun was introduced.

## Checks and local history

- Red baseline:2tests,1failure with actual['reload']; real pending controlpasses.
- Fixed causal controls:2/2pass; native helper syntax passes.
- Exact package Node selection, unchanged order and separate processes, prepared
  with the already-realized declared reviewAssets:10syntax checks and129tests
  (readcycle19, attention75, coordination14, resources2, providers19), zero
  failures/skips,16.691seconds. The2new regressions explain127→129.
- Focused full BrowserAsset/OperationsNavigation prefixes: passed0.103s.
- Exact lifecycle asset interactions/deletion assertions: passed0.094s.
- Committed hashes match successful test inputs; complete range whitespace and
  source/index cleanliness pass. No fullWeb/cluster/session/Ruby or long check.

Normal Nix-shell/tempfile/hooks commit created owning-UI fixup
`be0f0b691b9cd426def9ba7aaa1668d4926e26e9`, retained at
`2026-11-02-session-temporary-service-cleanup-pre-revive-ui-consolidation`.
Published3d76 remains at explicit `...-published-3d76f527`; older312/e29/d137 refs
and receipts remain retained. The fixup was folded LOCAL ONLY, preserving exact
fixup tree and three logical commits from basec218:

- `19dd03b79a2997098934afafbe70c63b978c1ca7 portal: group session resources and show retained counts`
- `565e28973a106369bc18ee7f3487c359cf9adc16 sessions: retire registered temporary services before file cleanup`
- `7302f4dc961ded7c768733e25ec39e3c603e093b portal: expose registered services and protect lifecycle handoff`

Range-diff shows only the accepted UI behavior/test/diagnostics correction; core
and dependent patches are `=`. No obsolete fixup remains in final history.
Correction3files81insertions/6deletions; complete branch49files4148insertions/
127deletions. No DB migrations or changed persisted/public contract, release,
deployment or supported state-consumption boundary. Runtime lock/full9node input
graph unchanged. New source `/nix/store/9fsjqqji9kyflc74nrhxz4fwxb2xv2x5-source`, NAR `sha256-bILeNLuxVReQbq2RvL2wvgOr5NMmlLTd+8p1mG43gz0=`.

The changed native helper belongs to the filtered Ruby input: previous generic
Nix/shard receipts are historical and cannot certify this new exact input.
Previously built site artifact09qh and published workspace2c/config46 pins still
bind3d76 and are held. Driver was never evaluated/built/run. Artifact receipt:
[site-artifact-prep.md](site-artifact-prep.md).

## Review packet

- [Complete final series/source/graph/quick receipt](revive-ui-final-receipt.json)
- [Correction diff](revive-ui-correction.diff)
- [Complete base-to-head diff](revive-ui-final-base-to-head.diff)
- [Published3d76 → final range-diff](revive-ui-range-diff.txt)
- [Retained fixup → final range-diff](revive-ui-fixup-range-diff.txt)
- [Causal red baseline](revive-ui-baseline.log)
- [Fixed causal controls](revive-ui-regression.log)
- [Exact Node commands/tested hashes](revive-ui-package-js-result.json)
- [Node output](revive-ui-package-js.log)
- [Go asset/navigation output](revive-ui-go-assets.log)
- [Go lifecycle-asset output](revive-ui-go-lifecycle-assets.log)
- [Exact source metadata](revive-ui-final-metadata.json)

Lead owns reviewer assignment and later exact committed native archive proof.
Both UI causality and observed native evidence retain their separate scopes.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
