# HaveAPI post-verification history consolidation

Final HEAD: `2ac6da81fa313b9df129a9fa8843358d0ef90492`. Base: `c14e7d3158b91c134c2817b489cd29772fc09f82`.

- Runtime `0717da05eb2a6dec60e2fce2a57d97b5bb556653` is unchanged.
- Generator/tooling `e21d8a929ad8579e47ebaf1bf6c97c5340a664b3` folds target-ignore `40af2a2e2ffeff33cfe6af0e5ef6c325b894109d`
  into previous generator `e93e51ac9edaef7e7cf5ff57e42ee6a292d6c10c`.
- Integration `2ac6da81fa313b9df129a9fa8843358d0ef90492` folds accepted fixture correction `80da2a09d34d18d52e777733e396f68c385ba2de`
  into previous integration `874e8f2fd8c94a4bc34008936e13b856b82cdd2b`.

Pre-consolidation corrected HEAD `40af2a2e2ffeff33cfe6af0e5ef6c325b894109d` and final HEAD have identical
tree `452864f73b77694d83e49ce45d9639f4732dca68`; `git diff --exit-code` passed. Exactly three logical feature
commits remain. The worktree and index are clean. No conflict/source edit
occurred during consolidation. The generator delta matches the ignore
commit's stable patch ID `fb4f18b669ddcdddf6d5c1a78b376c4f4cfb7f4f`.

Both rewritten logical commits explicitly ran `git commit --amend -F` with
mandatory root Nix hooks. HaveapiI18n, RuboCop, SingleLineSubject, TrailingPeriod
and TextWidth passed without hook bypass or configuration changes. This
history operation ran no application build/test, push, default integration
or publication. No migrations or separate corrective commits remain.

The range-diff from the previous post-review three-commit head shows only
the narrow runtime target ignore and accepted integration fixture changes.
Original independent review references and R1/R2 mapping remain in
[the first consolidation record](haveapi-history-consolidation.md).

- [Previous accepted three commits versus final three](haveapi-verification-reviewed.range-diff.txt)
- [Corrected five commits versus final three](haveapi-verification-remediation.range-diff.txt)

Freeze this source for the next watcher. The actual client remains owned
by implementer3; final provenance refresh must bind this source HEAD.
