# Guarded draft execution release

Status: RELEASED to retained implementer1 after independent review, source
freeze, full RSpec212/0 and RuboCop29/0 passed. Exclusive project Git and remote
draft-write slot; no other owner may edit source or mutate Git.

Source: `d23040cd3f3e8e33677dafdeb8e59cc83466e17b`.
Approval: exact60 IDs in approved-cves.json; unpublished drafts only.
Procedure: implementer1/draft-sync/README.md with exact approved order.
Evidence: frozen SHA256
`61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274`.

Acceptance gates already complete: normal-hook source commits, final independent
whole-branch review, narrow requested fixes verified directly, clean logical
history and final mechanical dossier/evaluation digest check. The initial full run found three stale-cohort spec failures. The bounded
correction and independent affected-lane review are complete. Full rerun passed
at d23040cd:212RSpecexamples/0failures,29lintedfiles/nooffenses. Lead verified
exactHEAD, cleanworktree/index and frozen snapshot hash before release.

On release, implementer1 owns exclusive project Git and remote draft writes.
Use the existing guarded CLI in one persistent Nix shell. Inspect one CVE's
dry-run, apply, exact remote draft readback and submission baseline; commit that
one baseline through normal hooks before the next write. Keep the source tree
and snapshot fixed. Report every five completed checkpoints and immediately on
any failure/uncertainty. No blind retry, adoption, replacement API or parallel
writer. No collect/evaluate/ready/publish/email/deploy/merge/lifecycle action.

Honest unresolved states stay unchanged. Four CVEs block publication; this does
not prevent their accurate unpublished drafts. Do not rewrite consumed source
commit lineage or submission recovery commits after external writes begin.

After exact60 draft/checkpoint completion, return the Git slot, sanitized ledger,
readback counts and final head. Branch publication and CI receive a separate
bounded lead brief. Leave the session active and open.
