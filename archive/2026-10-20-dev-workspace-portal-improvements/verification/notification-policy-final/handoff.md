# Final notification, runtime-policy and composition handoff

Source preparation is complete and clean; independent final review and longer
verification remain lead-owned. No merge, activation, claim, roster, notification
send/subscription, lifecycle or live settings operation was performed.

## Exact final identities

| Repository | Base | Head | Groups |
| --- | --- | --- | --- |
| A codex-web | `57972192e30fe52ab33b867c8fe4d171f59a7fd5` | `6e32a9043ee6367d92bfaf8d3ebdf48036e275f9` | 6 |
| B dev-workspace | `968646471b1190c16a8cf60ff50736cd0525fa3f` | `133d23f5d341808559b08a533409e748d6a400aa` | 15 |
| C workspace | `5276ad798d3dcf2c714f2336b0a50636bab900ae` | `7550f0183eaab80873666bb4c886a499609e8817` | 4 |
| Configuration | `38e7c837893695999e588a73f5d2a0088b8257b1` | `cc95d60fbccdff97a3df0fd7973f6b3b6b4f4a68` | 2 |

All four SSH feature heads match; defaults remain unchanged. Detailed remote and
cleanliness proof is in `final-source-identities.json` and `*-remote-final.txt`.
A is unchanged from its [own final packet](../a-followup-6e32a90/handoff.md).
Extension remains `767dfd587e346168e1443e65ccdb67ce748f3fe3`, native Codex0.163.0.
Both composed locks select exact final B and transitive A; only runtime and
codex-web nodes differ from their policy-source checkpoints. All other nodes,
input edges/follows, extension and siblings are byte-identical. The configuration
has only dev-workspace/devWorkspace as the owning channel: shared A is transitive,
not an extra direct channel or interim pin. `lock-invariants.json` records it.

## Completed behavior

Notifications use the existing browser registration ID as a transport-only epoch.
The existing IDBv1 store retains one protected gate; bounded transaction-commit CAS
and Web Locks fence stale actions and destructive side effects. Disable commits
off before cleanup; fresh Enable is future-only and cannot adopt an old endpoint.
Continuous idempotent registration keeps its epoch and pending outbox.

The actual controlling worker and server must advertise support. Managed workers
drop off/missing/mismatched epochs before every fallback/Test branch and recheck
after status/sound awaits. Current enabled deliveries retain neutral fallbacks.
Storage failure fails closed. The durable gate survives tabs/reload/worker restart;
a context that has seen it refuses an unexpected missing record. Explicitly
clearing this site's browser data resets its locally retained delivery state.
Legacy no-gate behavior is retained only until the first explicit updated action.
Old workers cannot supply the guarantee; forward recovery keeps notifications off
until capable code is installed. Server send revalidation and completion guards
never resurrect removed work. No team reporting transport or attention identity
change was made. All visible prose received the lead's direct pass.

Runtime policy separately requires integration of deployed feature lineage, actual
user acceptance of environment/result and explicit machine-specific release for
every deployed physical machine. Generated normal/retained lead/member guidance,
site/workspace procedures and tests retain short merge claims and saved settings.
The cooperative release API is unchanged and does not enforce these human gates.

## Verification and exact correction

- 71/71 deterministic notification fixtures PASS7.721s (`attention-final.log`),
  including epoch/fallback/Test, status/sound, CAS/pruning/reload/absence,
  off/on/provider old epoch, capability, continuous registration and two-tab
  permission/register/Disable races; cleanup-storage failure stays retryable.
- Final Go notifications/attention PASS0.543s (`go-notifications-final.log`).
  Generated lead/member policy focused checks PASS0.019s each (`go-final.log`).
- Browser client/store/worker and real-browser fixture syntax pass. The new
  negative browser assertions await the actual worker decision; no browser ran.
- Final instruction tests9runs166assertions PASS0.046s; deployment contract tests
  4runs19assertions PASS1.203s; actual final C/config graph checker PASS
  (`c-final-quick.log`). AGENTS15882bytes,502headroom; size assertion unchanged.
- Configuration declared shell, Nixfmt and ordinary commit hooks passed; generated
  changelog kept exactly, including nonfatal72-column warnings. No hook bypass.
- Existing A/B dependency source quick receipts remain in the original handoff;
  no pin/dependency bytes changed since0ba except downstream exact runtime pins.
  Final positive/negative pin contract and corrected fixture pass
  (`ci-fixture-final-pin-quick.log`, Go0.051s).

Old0ba CI39641137157 and checkpoint061 CI39645834660 both failed solely at
`TestAutomaticArchivalPageIsSeparateFromIndex`, expecting app.js?v=39 while the
actual template usesv52. Full failed logs are retained, not discarded/rerun.
The exact one-line fixture correction is `ci-fixture-only.patch`, folded into
the owning lifecycle group before final review. Effective diff061->133 contains
only that test line; product code is identical. Both obsolete runs had completed
before the final push, so no superseded queued/running job needed cancellation.
No blind rerun, full suite or CI wait occurred.

## Full series, reconstruction and retained lineage

Whole-range patches, file inventories, stats and range-diffs are `B-*`, `C-*`,
`configuration-*`. `final-history-proof.json` binds exact old/new ranges, stable
patch-ID mappings, bounded deltas and reconstructed final tree equality.
The B061->133 mapping changes only the lifecycle fixture patch ID; all other
14patchIDs match. C's two source groups and policy patch are unchanged;
configuration's policy patch is unchanged. Each old pin is replaced by the one
final stream; temporary fixture fixup is absent. No obsolete update chain remains.

Original [0ba handoff](../followup-combined-6e32a904/handoff.md), prerewrite eeb
reconstruction, original source proof and checks remain untouched. Original
policy-source checkpoint and deployed old/new baseline rebases remain in
[policy-source-followup](../policy-source-followup/handoff.md).
Checkpoint061/eb736/7d52 full receipts are retained under
`checkpoints/pre-ci-asset-fix`, with exact safety refs in the owning repositories.

Deployed A852 remains an ancestor; deployed Bf8/C530/config450 are not literal
ancestors after accepted consolidation/rebase. Their exact safety refs, receipts
and reviewed equivalence provenance remain intact; do not call them literally
merged. New behavior requires reviewed deployment and renewed acceptance.
There are **no migrations**: server state schema1, IDBv1, global attention identity,
claim/journal/session formats remain unchanged. The reserved gate is additive
local data, not a database upgrade. No migration was merged, released, deployed
or externally consumed. Older workers cannot honor the new gate; this is an
explicit mixed-asset limitation, not an unused compatibility path.

### Complete final B series

| Commit | Purpose |
| --- | --- |
| `4a2fadd106d5eb9a7dcd92fb7ab28fb8cbd94458` | deps: update shared conversation presentation helpers |
| `db1e91ebd008f479cc1021b25e9756c588c5949a` | team: project full-team names from actual implementer counts |
| `b006196781869aec5d267b790ef0a839e4aa57dd` | portal: add authorized file downloads and source copy actions |
| `54169426248448119fd257ffbf3d652b1f3b5172` | portal: keep large artifact catalogs compact and stable |
| `7d9392e6643e8d856688ee1dc08ba86146f41ddc` | portal: publish session membership before optional enrichment |
| `5a764b28d654c9b00538f333fd550067da7a121d` | portal: retain member settings through sequential additions |
| `0ce92e8619f6b1ae9afbe8b6016ba8949c89036c` | portal: present team messages and decorated Markdown |
| `cee4cca19ad2fcf98ffb1317aff7876d784e26b5` | portal: show delivery recovery beside the composer |
| `1f162c38138b35bfe9b75b2b7a1af2f18f34e513` | portal: browse eligible session files in a lazy tree |
| `bd46c6ebe326ef2a68bebb9225b7d828224a44aa` | portal: retire paused read cycles and recover on tab resume |
| `d2210fa96c86705241a68b397f0a81cca5c83706` | coordination: derive claims from registered repository identities |
| `a6df26e55a1b6a6dd32da76b56bae4a6b71c288a` | portal: measure read stages without logging session content |
| `b4709c17cebb1fea281fc18accf4363b3bfbbae3` | test: prepare ordinary Firefox acceptance across fifty native tabs |
| `cb12f4c4f80cde1156eadc5176cb90b8bb369c95` | notifications: drop deliveries from disabled browser epochs |
| `133d23f5d341808559b08a533409e748d6a400aa` | coordination: retain deployed machines through explicit user release |

### Complete final C series

| Commit | Purpose |
| --- | --- |
| `7117fe8006112e2b97ac28bc123e80482d702231` | instructions: keep core rules within the discovery limit |
| `82f1f1cf945560c4ae69928398c250fad4a5b870` | teams: default to Full team with implementer-count variants |
| `e1763e0bff920c174a551de48df80ca9eab92e53` | docs: require three gates before deployed machine release |
| `7550f0183eaab80873666bb4c886a499609e8817` | inputs: select responsive portal with protected notifications |

### Complete final configuration series

| Commit | Purpose |
| --- | --- |
| `3cc8b745eec48af6703a91819b3075a28d8ed32d` | docs: apply machine retention to aitherdev deployments |
| `cc95d60fbccdff97a3df0fd7973f6b3b6b4f4a68` | inputs: set devWorkspace to 133d23f5 |

## Prepared longer verification, not executed

All `.sh` files pass `bash -n`; metadata/registration helpers compile. Hashes are
in `command-sha256.json`. Original0ba commands/evidence stay untouched; this packet
contains final guarded copies. Browser cache references match pinned PW1.59.1 /
Chromium147; raw Firefox155+Gecko0.36 remains separate. Xvfb realization and native
discard/compatibility remain unverified until the parent launches the fixtures.

After final review the lead may assign a fresh Luna/low utility:

```sh
timeout 3600 bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/notification-policy-final/post-review-composed.sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/notification-policy-final/post-review-display-prepare.sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/notification-policy-final/post-review-root-dependencies.sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/notification-policy-final/post-review-chromium.sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/notification-policy-final/post-review-notifications.sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/notification-policy-final/post-review-firefox50.sh
```

The composed batch guards exact clean A/B/C/config and selected predecessorhzf9.
It instantiates exact immutable Git revisions and checks expected final workspace
/nix/store/pjhj1qj9pfcbcmfc5r1w2nfrbyv7mym4-dev-workspace-0.2.0.drv//nix/store/vqk9zcdgb84arin0yfzdsarg9n45ww8p-dev-workspace-0.2.0, roots every stage's derivation and output before downstream use,
and preserves derivation/input/output receipts. Stages are composed package,
agent-team-policy, Bgeneric-source, Adefault and Ageneric-source; no unrelated
host VM suites. Package realization covers B's packaged Go/Ruby checks, so a
separate Bdefault build would duplicate that work. Source revisions changed since
the deployed batch; old all-stage receipts remain historical, not proof of this
new composition. The shared source remains exact A6e but its prepared source
checks are explicit, with no claim based on tree equality alone.

Metadata asserts defaults/family/count6/capacity8, unchanged models/efforts,
utilities/native policy, exact shared Go bytes, native executable identity,
unchanged runtime/claim/integration contracts and final runtime guidance/capability.
Registration checks the original corrected reporting-only argv contract against
both selected and candidate, with PATH=/empty and disposable state; required
native child threads0/states[] and exact team-reporting MCP overrides are required.
Roots remain through activation/explicit cleanup. No profile is selected.

The parent owns final review, all long operations, deployment and its continuing
machine claim. No review, source completion or handoff releases that ownership.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
