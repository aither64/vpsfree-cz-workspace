# HaveAPI history consolidation

Base: `c14e7d3158b91c134c2817b489cd29772fc09f82`. Original independent-review head: `c50c07111baa68e4e321952511acc6da2a9ddce7`.
Corrected pre-consolidation HEAD: `54e233e27360c9533ee64320babd533ac553e348`. Final HEAD: `874e8f2fd8c94a4bc34008936e13b856b82cdd2b`.

| Final commit | Purpose |
| --- | --- |
| `0717da05eb2a6dec60e2fce2a57d97b5bb556653` | clients/rust: add embedded protocol runtime |
| `e93e51ac9edaef7e7cf5ff57e42ee6a292d6c10c` | clients/rust: generate clients from saved API schemas |
| `874e8f2fd8c94a4bc34008936e13b856b82cdd2b` | clients/rust: add protocol acceptance fixtures |

The runtime commit is unchanged. R1 `0149c4dd44a5bd10e866b94679e2372bcc76349d` is folded into the
generator commit; its delta from original generator `615293a1c313511723062283afab815c3e863a7d`
has the same stable patch ID `4c64aae1de089b44e89c9d1254ba017bc7acb798` as R1.
R2 `54e233e27360c9533ee64320babd533ac553e348` is folded into the integration commit. The integration
subject was shortened to satisfy the hook's 60-character limit; its body
is unchanged. No source edits or conflict resolutions were needed.

Exact tree equality: old and final trees are both
`2590b086ebbdb2c8b6ebb2283059051b1e5bfb01`. `git diff --exit-code 54e233e27360c9533ee64320babd533ac553e348 874e8f2fd8c94a4bc34008936e13b856b82cdd2b`
passed. The final series has exactly three commits; the index and worktree
are clean. There are no migrations or retained corrective commits.

Both rewritten logical commits explicitly ran `git commit --amend -F`
with their prepared message files and mandatory root Nix hooks.
HaveapiI18n, RuboCop, SingleLineSubject, TrailingPeriod and TextWidth all
passed. No hook bypass or hook configuration change occurred. No tests,
build, push, default-branch integration or publication ran during this
history-only operation. Earlier quick-check evidence applies to the same
source tree; this is not a new independent review.

- [Original reviewed three commits versus final three](haveapi-history-reviewed.range-diff.txt)
- [Corrected five commits versus final three](haveapi-history-remediation.range-diff.txt)

The lead accepts the direct R1/R2 remediations under the narrow-fix policy.
The client owner must regenerate and bind provenance to the final HaveAPI
HEAD before longer verification.
