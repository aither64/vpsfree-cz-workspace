## Preserve the second moved default: runtime 960dd and downstream selectors

Status: COMPLETE preservation and execution brief for lead disposition. The
user already authorized rebasing while preserving existing changes. Owner1 owns
runtime/configuration composition; owner0 owns the workspace baseline and later
consumer pin. Lead releases their bounded operations from this written brief.
There is no new user approval gate. This subsection supersedes launching the
historical gw45 rebuild or the tool-only corrected-quick successor: first compose
the final source, then bind and verify that source. Existing receipts and roots
remain intact. Architect performed source/evidence inspection and this design
update only; no rebase, test, evaluation, build or native execution is claimed.

### Immutable inputs and compatibility conclusion

Use `runtime-moved-defaults/20261025T223325Z/assessment.md` (SHA256
`ba26d639aed6aec1a2440904d6003070a7d59bfea90a48783bea218c860a7926`) and its
718-file `packet-sha256.json` (SHA256
`f78a444ffcecfa682bdf7405cae709396456cec818bf28a464b41d8a2e586ea5`). The
parent verified all packet entries. Its pre-SSH snapshots preserve both raw
indexes, complete owned histories/bundles, all 605 runtime files, all 472 config
files and prior evidence. Post-inventory HEAD/index/bytes/modes still match.
Owner0's `default-refresh/20261025T223228Z-readonly/` inventory SHA256
`e22bd20cf7acd66ff6ae62ffa3b57c1fa405b55590d5d96812def22562593158` and manifest
`b03570465fbfac61e5b9a799528eb5f8a078828f55dbc6d19ef0d8f8bcbdd29e` bind the
unchanged client and the workspace selector. References below are exact Git
objects, not moving remote aliases.

| Repository | Preserved current input | Fresh canonical default / disposition |
| --- | --- | --- |
| codex-web | `02533a152223416f159bac2578e88bcbe653f247`, tree `8080b79d073c258611b165a0a5b01fdbcb3aea4c`, clean and published | Default remains `8b60554bc10c2a6bcbf9732a8b77ad959c317036`; no source rebase or new client publication |
| dev-workspace | Base `b974f2f3f83792a494610d1ea03f3d69e97bc1a4`, head `f8a282af7ceae26625366b0659ae3c43fe5d80a5`, plus exactly seven saved dirty paths | Rebase the ten feature commits onto `960dd816b7e56cbdd4af0da15bf0b26257775151`, then restore the seven files |
| configuration | Clean zero-suffix `6428e280f06bffabef829a1335b36bac6cad5b9d` | Advance to `270d348a29a832e552a798ba8bb467152a2d36d6`; later select the final published runtime through its existing channel |
| workspace feature | Clean zero-suffix `9c4c97cd1d49232cb930ff5037ae124295f04f0f` | Advance to `3e72f394a73c33be71fcdc1313d05cc74abb802f`; later update only the existing nested runtime selection |

Runtime incoming commits are `2a58cf4937d035dd8688aaae92d9e997c3efdb63`,
`b75a6a1065449743b6a3c2f859b44bc32fefdc40`,
`78077b0e47bb21571c99ca70b854b6ccca2f7682`,
`4fc8ba11412d22f853764a5f3d5546b540a1f9e3`, and
`960dd816b7e56cbdd4af0da15bf0b26257775151`. They change 19 paths, with four
complete-feature overlaps and zero seven-file overlaps. Preserve these effects:

- Registration alone may wait for shared portal readers after a nonblocking
  shared-lock probe. An active exclusive writer still refuses; validation and
  mutation remain under the original exclusive lock/inode. Do not generalize
  the wait to other session actions or change occupied-name/PLAN admission.
- Archive Retry compares `kind`, `receiptId`, `state`, `phase`, `code`, `options`
  and `currentTarget` across the asynchronous journal/details read. Equivalent
  diagnostic/timestamp refreshes may proceed; changed authority or canceled
  reads must stop the retry. Keep the ordinary request and receipt identities.
- `NewContext` passes startup cancellation through retention, preparation
  reconciliation and compaction; `New` remains the Background-context adapter.
  A stopped initializing service must leave transition admission promptly.
  Operational workers keep their independent context: `Close` parks archive
  preparation before cancelling those workers. Cancellation must not turn
  accepted attachments into failed ownership records or bypass admission.
- Cold resume translates only typed `SessionBusyError` to existing temporary
  recovery/exit 75 and backoff. Preserve permanent identity/lifecycle/malformed
  refusals, lock admission, same retained thread and untouched state while busy.
- The native worktree fixture now establishes ordinary manifest scope before
  starting. Preserve production refusal of manifestless retained state.

No incoming SQL/migration, schema version, serialized record, module, flake
graph, catalog, raw-native selection or package-expression change is present.
This is nevertheless substantive cancellation/lock/browser behavior, so source
composition is not a package-equivalence claim. Retain archive-preparation
schema 1, parking/recovery, SQLite readers, original four UI fixes, full naming
takeover, capacity continuation, private cleanup proof and the client025 marker
fixture. Prompted naming remains raw 0.164/d2af with tools potentially available,
30 seconds including queue/cleanup, two slots/two calls, strict output checks and
manual recovery. Strict reusable utility support remains 0.163. No native patch.

Canonical ancestry and the two new downstream defaults prove merged source and
selection of runtime960dd with NAR
`sha256-yQnkYdToCk8gzhLRVl+psiRthpI77ndaJL38PoIL+BQ=`. The separate current
CLI inspection proves only its documented command path. Full deployed graph,
activation and machine provenance are not inferred. Preserve every new default
behavior even where deployment provenance is unavailable; do not inspect
foreign records to fill that gap. No downgrade/state-reader support follows
from the absence of a new migration; existing forward recovery remains required.

### Owner1 composition and the four conflict boundaries

1. Before mutation, recheck exact f8a HEAD, empty staged delta, raw index and
   all saved bytes/modes against the packet. Account for any untracked paths;
   unexpected changes stop this route. Verify the retained refs/bundles and
   immutable snapshot before temporarily removing any owned working delta.
2. Restore **only** these seven tracked working paths from f8a, leaving the
   index and every unrelated path alone: `flake.nix`, `flake.lock`,
   `portal/go.mod`, `portal/go.sum`, `nix/workspace-portal.nix`,
   `portal/internal/web/creation_contention_test.go`, and
   `portal/internal/web/session_namer_test.go`. Use the ordinary path-scoped
   working-tree restore, never repository-wide reset/clean/stash. The snapshots
   are the authoritative saved bytes; this is temporary removal for rebase,
   not abandonment. Verify the expected clean tracked state before continuing.
3. Rebase the exact b974..f8a ten-commit suffix onto exact960dd in the owned
   runtime worktree, with autostash disabled. Do not replay upstream's five
   commits as new feature commits. Resolve only the four boundaries below;
   any unexpected conflict, changed preserved input or behavior returns to the
   lead before further resolution. Preserve the paused state/evidence on failure.
4. Restore the seven saved working files with their exact bytes and modes,
   after proving their pre-restoration rebased blobs still equal f8a's blobs.
   This proof prevents a saved full-file copy from hiding an unexpected upstream
   edit. Match `seven-owned-paths.json` SHA256
   `7688be6582190673c254ed34b13bcde804ec86d4f0c50ca93bb1f92c10d7f1ff` for every
   file. Both fixture fixes and all five final025 dependency inputs must survive.
5. Record old/new ranges, all ten commit mappings, patch IDs/range-diff and
   exact manual-resolution hunks. Reconstruct the intended combined tree from
   preserved f8a plus incoming patches and the explicit conflict resolution in
   an isolated index, then compare to the rebase; compare the restored seven
   separately. All 15 incoming nonoverlap paths must equal960dd byte/mode-wise.
   All paths outside the declared incoming/restored/resolution sets must retain
   f8a bytes/modes. Do not label the diagnostics adaptation patch-identical.

The exact conflict resolutions are:

| File | Required composition |
| --- | --- |
| `test/archive_lifecycle_browser.cjs` | Keep our bounded, sanitized structured failure diagnostics and timeout. Add `#lifecycle-operation-retry` to their existing `document.querySelectorAll` control selector so Retry appears in the bounded id/tag/hidden/open/disabled projection. Do not restore incoming's old `outerHTML` block or expose response bodies. This is the concrete shared hunk. |
| `portal/internal/web/static/app.js` | Retain the incoming `lifecycleRetryState` and semantic snapshot comparison unchanged alongside the feature's separate composer/unread/queue/switch behavior. No consolidation of archive Retry with message or capacity retry owners. |
| `portal/internal/web/preparation_test.go` | Preserve both existing reconciliation calls' new `server.operationContext` argument and our 30-second/no-fallback/attachment-only naming assertions. Do not substitute startup cancellation into operational work. |
| `docs/workspace-portal.md` | Combine new startup/Close ordering and exit75 recovery paragraphs with the feature's browser, naming and diagnostic contracts. Retain forward-only package recovery; no old naming fallback or isolation promise. |

After the final tree is proved, fold the five final025 input edits into the
existing logical runtime naming/native update (currently6df324a5), rather than
publish another intermediate pin stream. Fold the diagnostics resolution into
its owning feature unit. Keep the two fixture corrections as one focused test
unit or fold them into their owning naming unit with a recorded mapping. Retain
old refs/bundles and original source529/source801 import evidence; no source
import became a new literal ancestor merely because runtime default moved.
Do not duplicate those source deltas. Final whole-history review includes the
new mappings and single final dependency stream. No source further changes
after final binding without a new delta and affected checks.

### Independent consumer package

Owner1 may advance its clean zero-suffix configuration feature to exact270d;
owner0 may advance its clean zero-suffix workspace feature to exact3e72 after
lead release. These are baseline-only fast-forwards, with before/after cleanliness
and ancestry evidence. Preserve obsolete published feature refs as evidence;
do not replay old063/508/7c3/5eb/d0 selectors. Shared workspace masteref1 and its
archive-tracking-only suffix stay untouched; no foreign record content is needed.

Only after final runtime review/publication select that exact runtime in both
consumers: configuration's existing confctl devWorkspace channel and workspace's
existing `vpsfree-dev-workspace/dev-workspace` nested input. Keep all unrelated
nodes, follows, extension767, root nixpkgsd58, configuration root EA/HM/retention
and source filtering. Account explicitly for the final runtime's authorized
025/EA transitive changes; do not copy a whole old lock or invent a top-level
runtime input. Match both effective runtime selections and run the existing
deployment consistency check. Fresh source drift before publication is assessed
from a new exact range rather than silently pinning an older baseline.

### Final source proof, checks and review sequence

Historical outer83971/gw45/gg30 source proof, old forced rebuild, failures and
tool-drift receipts remain valid for their recorded inputs. They cannot certify
this new runtime source. The unrun corrected quick packet must not execute or
receive replacement expected hashes. Prepare new source/derivation/root and
quick packets after composition, recording the exact baseline, full source
inventory (not a hard-coded 605 count), final input graph and source delta.
Rebind current installed wrapper/alias identities using the preceding section's
pre-invocation and final checks; no globally refreshed guard list or old-wrapper
generation bypass. Unexpected unrelated drift stops acceptance.

The module set, published025 source, checksums and vendorHash are unchanged.
Keep Fx only with actual source/output/content proof. Evaluate and root the new
requested goModules derivation through the existing declared recipe, then run
the already-required **one final-source forced dependency rebuild** under the
lead's watcher release. Do not build gw45 first or repeat fake-hash discovery.
Record actual stage exits and bind requested derivation, raw hash, source,
valid-producer membership, output SRI, 22 modules and the 52 vendored file
comparison. Use standard owned add-root receipts and exact symlinks; no broad
root query, manual store metadata changes, old-root removal or output deletion.
Any identity/content mismatch is a new concrete failure, not an automatic retry.

Quick verification uses the declared pinned environment, absent private provider
catalog, disposable sockets/state and unchanged no-native opt-ins. Carry forward
the corrected packet's unrun stages and coverage assertions into a new packet;
run the corrected Go web selection under077 and unsafe-state case separately
under022. Retain naming/capacity/retirement, archive readiness, PLAN/source locks,
browser unit contracts, fixture diagnostics and syntax checks. Add these affected
baseline checks using the existing tests, with explicit root/subcase coverage:

- Go web: `TestWorktreeRegistrationDistinguishesPortalReadersFromWriters`,
  `TestStartupContextLeavesWorkerShutdownToClose`,
  `TestStartupCancellationPreservesAcceptedAttachments`, and
  `TestSessionPreparationPublishedAdmissionConfirmationDispatchesOnce`.
- Go command: `TestServeStopsWhileStartupWaitsForPackageTransition`, exercising
  its actual owned subprocess and transition inode. Its helper test's skip is
  not independent coverage. Preserve the existing naming-child/compile checks.
- Ruby ordinary readiness: existing
  `test_cold_resume_retries_lock_contention_without_changing_retained_identity`
  plus retained permanent-refusal coverage. The native tmux test remains a later
  native check; do not turn its scoped manifest setup into a quick live action.
- Syntax/contract checks cover the combined archive diagnostics and app.js.
  Actual equivalent-refresh/replacement-receipt Chromium and Firefox cases in
  `archive_failure_browser_test.cjs` run after committed final review, alongside
  the already-required affected creation/naming/archive acceptance.

Known bounded non-native checks may run inline; uncertain or longer verification
uses the existing fresh watcher policy. Do not broaden or repeat successful
unaffected suites solely because a commit ID changed. Conversely, old runtime
checks do not prove the new startup/worker lifetime or retry authority behavior.
Bind each reuse to its real source/tool/input scope and report unrun stages.

After quick passes and all intended commits, the same retained reviewer receives
the final runtime whole range/history, explicit overlap resolution, test fixes,
source/derivation and consumer graph. General, architecture, scope and risk lanes
are affected by substantive startup cancellation, worker separation, archive
semantic identity and lock/recovery behavior; no pre-completion source review is
requested. Existing client025 review remains scoped to unchanged client source.
Raw d2af native, catalogs/schema and earlier8e stages00–05 may transfer only where
the existing exact scenario/runner/native/control/persistence input proof still
holds; this does not create a blanket025 or new-runtime native PASS. Corrected
client stage06 still requires real thread/message/receipt/FIFO/cold-read/resume/
fork/restart/offline-old-reader acceptance. Fail rather than infer downgrade
support. No client/provider/native repetition is added solely by these defaults.

Sequence: compose/prove final tree and coherent025 inputs; prepare new binding
and final dependency proof plus quick checks; commit/consolidate and affected
review; publish final runtime; prepare matched consumers and run postreview
native/affected runtime acceptance; build exact final outputs and verify the
deployment graph before activation. Consumer preparation may precede completed
stage06 after the lead's release; acceptance is still required before use.
Keep original mandatory packaged creation/archive and recovery gates. These
operations do not authorize default integration, machine/session lifecycle
changes or any production/foreign-state fixture. No installed package is changed
by this design. Lead retains rollout and readiness decisions.
