# Instruction restoration

Current outcome: all six initiative instruction amendments are removed and the
feature refs are published. Productedb90d2fe2190d88d8b9d2d21bd0def79eedc898
contains only selector/persistence owners; workspacec0d19e269fe5d34d4680c0988711061eb0faf959
and extension767dfd587e346168e1443e65ccdb67ce748f3fe3 are clean empty feature
ranges equal fetched defaults. All three SSH pushes passed exact prior-head
leases. No default branch or retained backup ref was changed by publication.

The following records preserve the earlier restoration checkpoints.

The user directed reverting this initiative's instruction amendments and later
authorized the implementation plan. All six owned paths are restored byte-for-byte
to the parent of their instruction-only owner; unrelated functional content is
preserved. `inventory.json`, `proof.json`, original patches/messages and declared
rebase logs bind the exact revisions and restored blobs.

- Product20b803f -> f2b1960d: AGENTS.md and patch-series policy restored.
- Workspaceabacb121 ->5a2119d4: commit instructions restored.
- Extension9d2ae656 ->c697acc7: general/scope/risk review references restored.

Every prior tip remains at the exact dated backup ref
`backup/2026-10-15-config-imports-before-instruction-restore` in its repository.
The dedicated feature branches remain; no default branch was changed. Workspace
and extension now have no instruction feature diff. At that restoration checkpoint remote feature refs remained
unchanged until final publication. Product guide/implementation refinements and
logical patch message reconciliation are separate pending work.

Two initial pre-rebase attempts refused a stale Overcommit signature and moved
no branch. Signing in the declared Nix environment followed by ambient Git was
insufficient. Signing and rebasing together in the same declared environment
succeeded, with all hooks enabled; no separate hook-version diagnosis is claimed.
`*-declared-restore.status` and `restoration.status` are0. Original refusals remain
in their logs. No hook bypass, repository-wide reset/clean/stash or lifecycle
operation was used.

The restored empty feature branches were subsequently fast-forward-rebased to
fetched defaults before final review: workspacec0d19e269fe5d34d4680c0988711061eb0faf959,
extension767dfd587e346168e1443e65ccdb67ce748f3fe3. Both are clean and have zero
feature diff against their respective fetched master. The six restored
instruction blobs were unchanged by these upstream refreshes. Exact restored
pre-refresh refs remain at backup/2026-10-15-config-imports-restored-before-refresh;
refresh-proof.json and per-project logs/status0 bind the operation. Remote
feature publication is still pending; no default branch was mutated.

Before publication, fetch confirms all three recorded defaults unchanged.
Product final comparison capture succeeds at7fd09b9b1..edb90d2fe. Normal companion
capture refuses because each restored range is empty; explicit exactbase=head
retry confirms the portal rejects identical endpoints. No fabricated nonempty
comparison was substituted. Direct clean Git/default equality is authoritative.
This is a portal representation limit, not a source/history gap.
