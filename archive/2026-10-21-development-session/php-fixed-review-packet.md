# Final review: fixed PHP, workaround revert, Foto shutdown

Completed substantive deliverable, all intended changes committed, quick checks
pass. FINAL review now, all four lanes. No builds (user will build), no live
probes/deploy/CLI or nested reviewers. Explicit user configuration/master merge
authorization exists after review: "merge it when done".

## Outcome and constraints

User selected latest release-26.05 source containing NixOS/nixpkgs PR576865,
without waiting for channel. Exact observed source head/PR merge:
8c259fc0dd1f3ccc1aaf4f9156ab16b7328b5a4f. nixos-26.05 channel headcd4ea8d
lacks fixes. Pin through native confctl, original ref policy unchanged.
User then required temporary Foto disablement (PHP5.6 partial workaround
insufficient), exact revert of original workaround commit, separate Foto commit.
Final result: ten configured FPM/session runtimes8.4.27, no workaround globally,
Foto hostname503 with no FPM/legacy package/root/locations; accounts/data preserved.
Vendor fixed floors8.2.35/8.3.36/8.4.27/8.5.12, compare within minor branch.

## Session, repo and current design

Session2026-10-21-development-session, workspace/home/aither/workspace/ai/vpsfree.cz.
Worktree/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-21-development-session/vpsfree-cz-configuration.
Read repo AGENTS.md and relevant workspace routes. design.md current section is
canonical for Foto shutdown; php-fixed-version-design.md retains source/advisory
provenance with superseded Foto-only mitigation marker. plan/state track scope.
Implementer0 source/Git, implementer1 independent evaluation. Reviewer0 eligible
retained read_only gpt-6.1-sol/xhigh, no overrides/fallback. Overall risk HIGH:
security update/mitigation removal/host behavior and deployment. All lanes:
general, architecture/repetition, scope/proportionality, risk/compatibility.
Read canonical mandatory-change-review skill and all four references.

## Complete unmerged history and final diff

BASE37a338b25192d9271ee211110800c2dc6a094a57 (fresh origin/master).
HEAD38e7c837893695999e588a73f5d2a0088b8257b1 (remote feature exact verified).
Complete THREE commits:
1.823ffe9cd1bbbf6dd708f756211d4d0d55913bc6 inputs: set nixpkgsStable to 8c259fc0
2.01213695503ab85ee273263a17751c2a68389f43 Revert "php: disable session upload progress in FPM pools"
3.38e7c837893695999e588a73f5d2a0088b8257b1 web: temporarily disable foto.vpsfree.cz

Final diff php-fixed-final.diff: five paths,6insertions/60deletions. One native
pin stream, only stable lock rev/hash/timestamp; no unrelated/transitive/ref-policy
changes. Exact revert diff independently checked by implementer against inverse
of merged38687a; earlier merged history preserved. Foto separate per user.
Earlier unmerged local/feature-published6cf8c9 and55ed38c functional iterations
consolidated out of final ancestry. No obsolete history or repeated updates left.
NO migrations, schema changes or state conversions; thus no migration merge/
release/deployment/external-use provenance. No new commits deployed or released.
Reviewer must independently conclude history/streams/migration lineage.

## Quick checks and independent evidence

All intended commits normal precommitNixfmt/commit-msg hooks pass. Format/parse
checks on final Nix source and complete-range git diff--check pass; worktree clean.
Generated native pin message preserved; no manual lock edit or hook bypass.
Fresh upstream check still base37a; no rebase after final source check.
No push CI (only scheduled/manual daily-update), no workflow wait.

php-fixed-runtime-coverage.md and php-fixed-runtime-evidence.json independently
prove actual confctl-composed ten FPM+session packages8.4.27, source/hash/derivation
provenance, no workaround, noFoto pool/systemd service/cleanup, nginxserver503
rootnull/locationsempty, accounts preserved. NoIFD evaluation/no builds.
Evaluation at old candidate55ed38c tree8a42d008d0949147945bf7504777c0c368170d81
is bound to FINAL head38e7c837 by identical exact tree; lead and both implementers
verified. php-fixed-final-tree-binding.json records proof; snapshot provenance
and evaluator source seam are documented. Earlier dirty projections superseded.

## Compatibility/documents/limits

New generation couples patched PHP with removal; deploy complete final series,
not revert alone. Foto unavailable until safe runtime upgrade; restoring old
config reopens vulnerable PHP. No data/user cleanup, migrations/API/protocol
change. Broader stable package delta affects other stable consumers too.
User owns builds/activation; do not claim system build/runtime success.
Source comment explains Foto unavailability; session design/source references
hold rationale/rollout evidence. No new project report/framework needed.

## Requested report

Concise findings by severity/lane or explicit none, complete final history and
migration/repeated-stream conclusions, accepted build/runtime limits. Direct
review only, no edits/nested agents/long tests. User asks speed; focus material
correctness/security/scope and exact requested commit split. Lead persists report
if reviewer policy read_only. Merge only after this report accepted.
