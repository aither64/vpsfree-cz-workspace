# vpsAdminOS integration preparation

Later user steering explicitly accepts the observed six product failures and
AMD-scale-aged-v6 warning as nonblocking for this merge, without claiming CI
success. [Fresh exception-aware tuple](generic-sysctl-premerge-accepted-exceptions.md)
supersedes the initial all-green condition below. Actual integration awaits
lead's critical-section release; current CI continues under its sole watcher.

User direction, relayed by lead: “keep checking it periodically, like every
10 minutes, and merge when it is done.” Scope is `vpsadminos` → `staging`,
conditional on successful exact-head CI and lead's final freshness gate. A
terminal failed/cancelled run does not release integration. No merge, claim,
deployment, pin update or session lifecycle action has occurred.

## Prepared tuple and checkout

At 2026-10-22T14:00:14Z, fresh SSH refs were:

- Target `staging`: `55c5046514d06fe9398a022c1622bdaae5228841`.
- Published feature: `846bb469505789ba0b2a405fa5905ba6d8253006`.
- Feature tree: `df9bd828d843225df749b7a05ed9529bf17425c9`.

Feature source is unchanged and clean; no rebase is needed at this target.
The clean disposable target checkout is
`worktrees/2026-10-20-kernel-check/vpsadminos-staging-integration`, detached at
exact55c504. The normal `nix develop` environment is prepared there: Ruby3.4.9,
Overcommit0.73.0, installed executable ordinary hooks and successful actual
post-merge hook invocation. Hook bypass variables are inactive. Preparation
log: [environment and hooks](generic-sysctl-premerge-environment.log).

## Complete reviewed range

The entire range has exactly two logical owners, unchanged from final review:

1. `8528262315b0794a8f50917cf33c53a07fd14030`: paired crashdump panic policy.
2. `846bb469505789ba0b2a405fa5905ba6d8253006`: generic sysctl service v3,
   including its implementation, fixture, documentation and caused fixes.

Final diff: six files, +399/-1. No merge commits, migrations, dependency/pin
updates, repeated streams, obsolete stages or fixup residue. Published earlier
iterations were used only for development/CI, not known merged, released or
deployed; their native failures and dated backup refs remain preserved. The
exact v3 backup ref is
`refs/backup/2026-10-22-kernel-check-generic-sysctl-v3`. No backup was deleted.

[Full commit history](generic-sysctl-premerge-history.txt),
[final patch](generic-sysctl-premerge-final.patch), and
[refs/backups/diff digest](generic-sysctl-premerge-refs.txt) bind this inventory.
Patch SHA256: `ee6a55c44aada17410cb6ea8edba274bad3294a47bfcb13be3a13bfd93295d56`.
Native repository comparison was refreshed at exact55c504→846bb.

[Final independent review](generic-sysctl-final-review.md) accepted all four
lanes and complete history. [Verification packet](generic-sysctl-verification.md)
records passing quick checks/hooks and focused VM8/8, exact selected exit0.
Its frozen source/config/head binding is retained. No additional test was run
for this preparation.

## Remaining gate and ownership

Existing exact846bb CI is run
[39767770407](https://github.com/vpsfreecz/vpsadminos/actions/runs/39767770407).
Same native watcher `01a1634c-0553-7530-ba30-b19cfc2307d0` now owns one
`gh run watch --interval600 --exit-status`. Its original three-second local
watch was intentionally interrupted with exit130 to change cadence; that is
control evidence, not a CI conclusion. The original logs are unchanged.
The replacement started13:57:26Z with separate `-600s` log/start/end/exit
receipts. Same actual Luna/low, danger-full-access/never policy is verified.
No workflow, retry, second observer or CI cancellation was launched.

On first CI failure, preserve evidence and report for diagnosis before any
rerun. On CI success, provide the exact terminal head/jobs/conclusion to lead
for the final freshness gate. Only then may the actual critical section be
launched: acquire the single repository claim, freshly recheck target/head and
clean checkout, ordinary fast-forward/hooks, non-force SSH push and exact remote
proof, then promptly release. If target moves or hooks need intervention,
return to preparation outside the claim. No claim is held while waiting.
Feature branches and this session remain retained/open.
