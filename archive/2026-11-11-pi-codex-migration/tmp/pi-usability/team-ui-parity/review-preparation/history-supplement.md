# History preparation supplement

This supplement binds the completed mechanical history work to the existing [combined review packet](../combined-review-packet.md). That packet owns scope, acceptance criteria, documentation routing and independent-review instructions. Lead owns acceptance and review invocation. No application edit, new pin, test/build, push/CI, live operation or default integration occurred in this package.

## Frozen source and complete review ranges

| Repository | Final head | Final tree | Final parent | Complete review range |
| --- | --- | --- | --- | --- |
| R | `5e48e114f5cbc45e2cb9816315b6ad928805832d` | `48f8f77b927752b7cf7d5d9fc00381ae498bc374` | `7e168c699cd07572d483fb7d8fc3d3886cc352fc` | `9241a342a6ef4ca69148594e98cce7ddcfb459a6..5e48e114f5cbc45e2cb9816315b6ad928805832d`, 106 commits |
| W | `e1136f2b95189622ee2e2dafd9627617dbd8f9d8` | `1bcc0364a7a4d6d39be97c164551172a83f9aeba` | `002e21a886c94f14ab9bdf06d749e4de7715a5e7` | `9610ea74a70d4b9b9d0f2d9296ea4908c0d4725b..e1136f2b95189622ee2e2dafd9627617dbd8f9d8`, 11 commits |

Complete ordered lists and binary diffs: [R commits](R-merge-base-commits.txt), [R diff](R-merge-base.patch), [W commits](W-merge-base-commits.txt), [W diff](W-merge-base.patch). [Export bindings](export-bindings.json) records sizes and SHA256. H remains provenance only at `d598f3e65340c859b4f540283029a129b7c9f8e1`, tree `b78701a89b26499880f84d4f82cbc260b01f32fa`.

## Preservation and equivalence

R prehead `09608843edffc38523c5c46356cb9d51939ef875` is retained at `refs/heads/retained/pi-parity-pre-review-r-09608843`. Its final tree and complete origin/master-to-head binary patch are exactly preserved: 4,130,267 bytes, SHA256 `50796fb73a9e6f54bcede7bb94e97e8328f9d49a000e69ec3a1aeb4b12a5f635`. The unreleased three-path `81510ac37c8f3f3fc091a4d31029af35ebff7b02` correction was folded into owning Team `f1bb4c1b472661f6d76e246f252b8fc46f7df3db`, now `340b279d49dee33d9885026672a731a155fde3a5`. Rules56eca70a and observer8ea81d0 stay literal unchanged. The three messaging commits remain separate, patch-equal successors. [R mapping/proof](R-history-result.json) and [range-diff](R-range-diff.txt) retain exact identities.

W prehead `2f1d73eb75fe4de01a6b695d41365da51895b16d`, tree `32360013b597a2adf04d59c781dc5ffd08b6a14d`, is retained at `refs/heads/retained/pi-parity-pre-review-w-2f1d73eb`. Five feature commits were rebased conflict-free from d918b453 to exact shared master `fcbed7990960a914eae2241a39dce9ef989bccc0`. All five range-diff entries and individual binary patches are equal. The proper-base feature patch SHA256 stays `ce54b468ac79e700aa7c6b4f80dd4f24244fe3d0cb950db01c72d32dd5ae6512`. [W mapping/proof](W-history-result.json), [range-diff](W-range-diff.txt) and [baseline context](W-baseline-context.json) distinguish the five feature commits from the complete 11-commit review range. The inherited baseline delta contains only 20 session-tracking paths; shared master was untouched. Its complete review diff is 499,604 bytes, SHA256 `de502a08c74a11c293c05a7e65d6d001cf7d8cd77dfd3163c62a3d06a1590790`.

Both normal rebases exited0 and joined, without hook bypass. Both worktrees were clean/index empty at their positive whole-source releases, reported before packet formatting. [R operation](R-consolidation-result.json) and [W operation](W-rebase-result.json) retain the commands and results. No active effects remain from this package. These are recorded release-time facts; no later source audit is implied.

## Existing evidence, migration lineage and streams

[Existing evidence bindings](existing-evidence-bindings.json) links original Team, timestamp, observer, messaging and F packages with their original hashes and source scopes. Team checks remain at original f1bb inputs; the three-path legacy correction has its own original evidence. All 15 messaging quick input hashes equal the final committed blobs. History equality maps that evidence; it does not execute new tests or qualify new outputs. Original failures remain preserved. `TestPinnedSDKPolicyInspectDuringSharedBashChild` is prepared/compiled but **UNRUN** at this handoff; synthetic controls remain synthetic.

Whole R is **not migration-free**. Reuse `review-final-schema12.md` full59/60/74/81 and F conclusions at lines3394,3417,3658,3692–3716,3729–3749 and3762–3786, plus the combined packet's retained inventory. The inherited preparation/input3/draft5, Pi2/Codex1 replay, runtime/authority/communication/creation/domain/observer/lifecycle/livePolicy/maintenance/snapshot/shared-topology boundaries, native3, Add roster3 and Fork destination creation5/roster4 remain supported lineage. Team adds explicit removal-on-write roster5, including historical nil/zero removals. No SQL or bulk conversion is introduced. Old-reader refusals, frozen launch equality, retained roots/forward recovery and AcceptedUnknown/no-resend remain required.

[Deployed-boundary references](deployed-boundary-references.json) binds existing8fe delivery and activation receipts. R `8fe50341b83c7f55b4c48a9042531063fb741656` remains a literal unchanged ancestor. Rebased W is patch-equivalent to its prior consumed history; it is not literal deployed ancestry. H is unchanged provenance. W/H continue to select deployed8fe; later matching pins are outside this package.

| Stream or purpose | Disposition retained for final reviewer |
| --- | --- |
| R C-selection dependency | Owning `7ae2fe8353c2a1f7784c31a09d285fdca933b17c` consolidates C1993f16 across flake, Go/checksum and vendor fields. |
| R Pi SDK introduction and packaging | Separate functional purposes at938d6d4e and3bf58ab7; host launcher/native endpoint work remains separate. Team/messaging adds no dependency update. |
| W runtime selection | One owning commit306a8cf8; prior deployed/consumed refs remain retained. No new pin here. |
| W other functional purposes | Catalog/composition b0ef5cb1, model expansion002e21a8 and two interface-rule commits e47cb5f8/e1136f2b remain separate: five logical commits total. |
| R current branch-only follow-up | Only815 was folded into Team. Rules, observer and three messaging purposes remain separate; earlier consumed/deployed lineage was not rewritten. |

Prior whole-branch reviews recorded no obsolete transition solely for an abandoned design. This assembly adds no independent certification of that conclusion. The final reviewer must assess all106 R and11 W commits, repeated streams, migration provenance and retained boundaries; any obsolete branch-only transition or redundant pin found requires an explicit disposition. None beyond the authorized815 fold was newly established in this bounded package.

The combined packet is lead-maintained and may change after the earlier evidence-bindings snapshot; `handoff.json` records its snapshot at this handoff without replacing earlier hashes. No additional product documentation was needed for this history/evidence-only work. This supplement supplies the state-update pointer for lead and does not write shared state or invoke review.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
