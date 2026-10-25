# A forward refresh, 2026-10-24

Published final A: `6e469863a69c7d35941ca2e15de9514223b58f4f`, one owning
commit above freshly fetched deployed baseline
`11ec57d2203fc735696fe75a837d47da55a5c6af`. Canonical SSH remote proof and
explicit old4300 lease succeeded. Source and refs are frozen after publication.

No manual source edits or new policy/API were needed. Range-diff reports old4300
and new6e469 as equal. An independently computed three-way merge tree exactly
matches the final tree, preserving all upstream cancellation isolation, failed-turn
continuation, prepared-send/context and retry UI behavior. Four ephemeral Go files
are byte-identical to the reviewed candidate. Six owned paths remain; the two
overlap files retain both additions. Main approved the unchanged reference prose.

Focused Nix Go selection from the design (Ephemeral, CanceledWrite,
AlreadyCanceledWrite, ContinueFailedTurn and Continuation) passed in3.589s.
Protocol coverage and diff checks passed. Commit used temporary message and Nix
Git; no hook framework/active hooks or bypass. No long/native/integration checks
were run on this refreshed head, and old PASS/build receipts are not reused as
new-head proof. Lead owns affected-lane review and fresh verification watchers.

`source.json` binds the immutable final source/NAR/catalog, independently hashed.
The Luna catalog is byte-identical to installed11ec, with unchanged SHA256
049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1. Native,
provider and model policy are unchanged. B owner received exact final A; no
provisional pin is needed. C remains gated on exact final refreshed B.

`inventory.json`, `history.txt`, `baseline-history.txt`, `forward-diff.patch`,
`old-to-new-source.diff`, `range-diff.txt` and `replay-proof.json` provide exact
new/old ranges, complete history and source preservation. There are no A migrations.
Original reviewed/native/package/build receipts, manifest and recoverable old
source bundle are under `original-candidate/`; no original file or Nix root was
removed. Old published B e515 consumed A4300 for verification/building, but this
initiative activated neither old candidate. Those artifacts are stale deployment
inputs. The selected deployed11ec/b3a6 lineage is preserved, not replaced by an
old candidate. No default ref, unrelated feature ref or other-session worktree
was changed. No claims, copies, activation, PRs, merges or lifecycle action.

Current CI40127462113 was in progress when sampled, not awaited; old4300 CI
completed successfully and no superseded active run required cancellation.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/>.
