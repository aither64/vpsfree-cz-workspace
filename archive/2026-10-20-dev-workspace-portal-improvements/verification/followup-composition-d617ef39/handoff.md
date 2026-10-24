# Final F1 composition closure

Lead accepted the bounded B history fix under mandatory-review step9 after the
completed four-lane HIGH-risk review. No new product, schema or API boundary is
introduced by this downstream closure. No long package/browser check, activation,
merge, claim, lifecycle or live notification action ran here. Machine ownership
remains with the lead.

## Final published sources

| Repository | Base | Final head | Groups |
| --- | --- | --- | --- |
| A | `57972192e30fe52ab33b867c8fe4d171f59a7fd5` | `6e32a9043ee6367d92bfaf8d3ebdf48036e275f9` | 6 |
| B | `968646471b1190c16a8cf60ff50736cd0525fa3f` | `d617ef3968280e9955da85e2d7464a47030e7087` | 15 |
| C | `5276ad798d3dcf2c714f2336b0a50636bab900ae` | `48215f8c24f29358af338ac153d4ece88e1f4da2` | 4 |
| Configuration | `38e7c837893695999e588a73f5d2a0088b8257b1` | `9ab2909175b7248b5800237edd016b523d10d011` | 2 |

`final-identities.json` and `*-remote.txt` bind clean local trees and exact SSH
feature/default refs. Defaults are unchanged. `complete-series.json` lists all27
commits in order. B's [F1 handoff](../followup-history-f1/handoff.md) retains its
complete series/diff/reconstruction,104 focused Node passes, Go1.459s and negative
control. The lead inspected and accepted that narrow correction; no B source was
changed here. A remains unchanged from its prior final receipt.

## Mechanical pin proof

`mechanical-proof.json`, `C-pin-only.patch`, `configuration-pin-only.patch` and
both range-diffs establish exact source-only equivalence to reviewed C755/configcc95:

- C only changes `flake.nix` and `flake.lock`. The sole runtime pin commit is
  amended. All three source/policy commit IDs remain identical:
  `7117fe80`, `82f1f1cf`, `e1763e0b`.
- Configuration only changes `flake.lock`. Its source-policy commit
  `3cc8b745` is identical. Normal `confctl inputs channel set --commit
  dev-workspace devWorkspace d617ef3968280e9955da85e2d7464a47030e7087`
  generated the replacement sole channel stream, with the full968->d617 changelog
  preserved. Normal Nixfmt and commit hooks passed, with only the permitted
  generated72-column warnings; no bypass or manual lock edit.
- Only `dev-workspace` in the C lock and `devWorkspace` in configuration differ
  from reviewed locks. Input edges, follows and all other nodes are identical.
  Shared A6e, extension767dfd5, siblings and nativeCodex0.163.0 remain selected.
  There is no separate A channel: it is the unchanged transitive runtime input.
- Disposable-index reconstruction of each reviewed tree plus its bounded pin
  delta equals the final tree exactly. No extra interim pin commit remains.

Reviewed B133/C755/configcc95 refs are preserved. Original deployed A852/Bf8/C530/
config450 refs and all old review/check/deployment receipts remain intact, as do
[the prior final command packet](../notification-policy-final/handoff.md), its
checkpoint receipts and the failed0ba/061 CI diagnosis. Nothing was relabeled as
new validation. A852 remains a literal ancestor; Bf8/C530/config450 remain deployed
nonancestors with reviewed lineage evidence, not literal integration. Source
refresh does not establish integration or user acceptance.

There are **no migrations**, including none merged/released/deployed/externally
consumed. Existing schema1/IDBv1/catalog6 and session/claim/journal/submission formats
retain the prior review conclusions. No source policy, saved role, model, effort,
access, roster, durable notification control or installed package was changed.

## Focused verification only

`graph.log`: final C/config deployment checker PASS at exact Bd617.
`pin-quick.log`: actual pinned Go module plus positive/negative pin contracts PASS.
`source-pin-proof.json`: all ten shared source/assets match exact A Git and module
cache; all five Go/Nix dependency files are byte-identical to reviewed B133.
The old Nix source output remains collected, so it was not falsely compared or
rebuilt. Final package realization remains required.
All B/C/config whole-range whitespace checks pass. C instruction/catalog/policy
source is identical, so prior source checks are reused without another test run.
Only source generation, focused pin/graph checks, source hashing/reconstruction
and package derivation evaluation ran here. Development-shell prerequisites were
substituted; no application package was built.

## Prepared final commands, not executed

`post-review-composed.sh`, `post-review-display-prepare.sh`,
`post-review-root-dependencies.sh`, `post-review-chromium.sh`,
`post-review-notifications.sh`, `post-review-firefox50.sh`, `metadata.py` and
`registration.py` are final copies. Old commands remain unchanged. All shell
syntax and Python compilation pass; `command-sha256.json` binds exact bytes.
`prepared-command-delta.patch` shows the composed launcher update. Final asset
receipt: app53/store4/browser6, shared mounted21/sync3/uploads7.

Prepared package argv, for the parent's fresh Luna/low utility:

```sh
timeout 3600 bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/followup-composition-d617ef39/post-review-composed.sh
```

Expected composed derivation: `/nix/store/72lyzcfqwb5sf05b3j7yndpaymjxwgx9-dev-workspace-0.2.0.drv`.
Expected package output: `/nix/store/pvbdrx2n6x4zccpzg9qspfni28c564n3-dev-workspace-0.2.0`.

The launcher guards exact clean A/B/C/config and selected predecessorhzf9. It roots
both drv and output before assertions for every stage: composed package,
agent-team-policy, Bgeneric-source, Adefault and Ageneric-source. It retains all
input/derivation/output receipts, validates catalog/default/family/capacity8,
unchanged model/effort/native policy, shipped A Go bytes and current runtime guides,
same nativeCodex executable and corrected reporting-only registration argv with
PATH=/empty/disposable state. No duplicate Bdefault or unrelated host VM suite.
Root lifetime continues through activation or explicit cleanup.

Other prepared argv, each in this packet:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/followup-composition-d617ef39/post-review-display-prepare.sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/followup-composition-d617ef39/post-review-root-dependencies.sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/followup-composition-d617ef39/post-review-chromium.sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/followup-composition-d617ef39/post-review-notifications.sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/followup-composition-d617ef39/post-review-firefox50.sh
```

Browser source guards select exact Bd617; pinned PW1.59.1/Chromium147 and native
Firefox155/Gecko0.36 identities remain unchanged. Display realization, real browser
and native50-tab visibility/discard/restore acceptance remain unverified until the
parent launches them. This package preparation makes no incident-wide cure claim.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
