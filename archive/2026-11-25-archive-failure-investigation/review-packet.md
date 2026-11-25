# Final archive fix review packet

Status: final review invoked after committed changes and passing quick checks.
User request: investigate the failed workspace archive, find its root cause and
fix it; aitherdev may be deployed using vpsfree-cz-configuration.

## Outcome and acceptance

The failed ordinary archive exhausted the same 30-second admission deadline by
repeating native monitor safety proof after CLI readiness had already returned
validated quiescent proof. Consume that result only in that admitted callback.
Preserve missing-field fallback, blocked/quiesceable observer owner/join/readiness
paths, cancellation, receipt/target/generation fences and fresh executor checks.
No cache, global timeout increase, schema/backend redesign, actual archive retry,
peer mutation or lifecycle cleanup. All reproduction uses isolated fixtures.

Read [plan.md](plan.md), [state.md](state.md), architect-owned [design.md](design.md),
C's complete [core-evidence.md](core-evidence.md), B's exact
[deployment-preflight.md](deployment-preflight.md), and D's
[deployment-evidence.md](deployment-evidence.md). Evidence owners assembled the
exact series, changed files, checks/inputs and documentation inventory in those
existing records; this packet binds that material to the final review.

## Exact repositories and series

Owned worktree root:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-archive-failure-investigation/`.
All branches are `2026-11-25-archive-failure-investigation`; target master.

| Repository / canonical SSH origin | Base | Final head |
| --- | --- | --- |
| dev-workspace / git@github.com:aither64/dev-workspace.git | 65544340f94ebb112872743738f84c1a7022b06a | f6d60bf87002fb1896599f35f0284743c16d7e6f |
| workspace / git@github.com:aither64/vpsfree-cz-workspace.git | d43347c1fd4f9ff9dfdf5c19f6cccb9531bbd639 | 18275679109c2adda4084af1ea7474e21be98b4e |
| vpsfree-cz-configuration / git@github.com:vpsfreecz/vpsfree-cz-configuration.git | d5055ec0b2ea22de976f6703208f5526c3e185ca | 6f6cb452e17ca663114a07013a0402ef85a7fee3 |

Runtime complete series is 9bf34aa1963e3ba226ec678237cee3dacb2e7a25,
91cafd4c0c50ffb7208498a605707c4c3b1b1174,
f6d60bf87002fb1896599f35f0284743c16d7e6f. First two commits are unchanged
installed originals, with prior independent final full655..91c history/no-migration
conclusion in ordinary parent's review.md:1992, cited by design/core evidence.
Preserve that existing review rather than repeating unchanged Pi implementation
work. Review new C affected behavior and explicitly conclude on the complete final
series/diff/history/migrations. Full runtime diff includes the installed parent;
incremental C is91c..f6 (3 files,+126/-1). Inspect both at appropriate scope.

C old655..e50 vs new91c..f6 has equal range-diff, byte-identical binary patches,
patch ID ea289e0482d2c0a6289b45abc29526862c1fbbe5, and independently reconstructed
final tree0ab8c211365bedcd18ddc8fd5074db72b54df562. No obsolete C history remains.
Workspace/config each contain one final consolidated runtime selection stream to
f6, no intermediate pin commits. Read complete base-to-head lists and final diffs
from the owned repositories. No migrations in any stream; no new schema version
merged/released/deployed/consumed. Installed parent originals remain supported.

## Checks, contracts and documentation

C evidence owns exact final focused checks, source NAR/lock/module identities,
final package and session-archive-lifecycle derivations. Longer checks remain
unrun until review. D owns cross-lock/site and full semantic graph checks,
Nixfmt/hooks, contract tests4runs/19assertions, effective host derivation findings
and generated-pin provenance. No hooks bypassed. Main-agent user-facing prose
pass completed before core commit. Final quick status is a required invocation
precondition and will be recorded below.

Documentation inventory is in core-evidence.md: maintained archive recovery guide
(reference/operations for runtime operators), nearby proof-lifetime comment,
README existing entry point; individual lineage/check/rollout records stay in
this session. No warnings, supported recovery paths or old anchors removed.
Config contains no rollout receipt. Independently conclude placement/preservation
under the general lane; do not merely say docs checked.

Generic dev-workspace owns readiness/portal/executor; CLI and browser consume its
existing typed monitor result. No wire or persistent format changes. Workspace
nested runtime override and configuration devWorkspace channel select matchingf6,
with installed extensionbf12/codex-web2547 and complete graph preserved. The local
operator is trusted; ordinary identity/races/recovery and remote clients remain
in scope. Parent claim6097deba is owned by another session, so activation is fenced;
this review grants neither integration nor deployment/lifecycle authority.

## Reviewer and requested lanes

Overall risk HIGH: pre-destructive lifecycle readiness and cross-package deployment.
Use retained independent reviewer0, gpt-6.1-sol/xhigh, read-only, with saved settings
unchanged and no nested reviewers. Mandatory-change-review skill applies.
Lanes: general, architecture/repetition, scope/proportionality, risk/compatibility;
read every lane reference fully. Inspect all intended committed changes after
quick checks, before longer integration tests. Generated pin content is mechanical
but still part of full-series/consolidation/compatibility conclusions.

Return findings ordered Blocking/Important/Advisory with exact locations, or say
no findings. Explicitly conclude complete branch history, obsolete approaches,
repeated-update consolidation, migration lineage/no migrations and documentation
placement/preservation. Distinguish existing baseline review reuse, observed
checks and remaining test/deployment gaps. Do not edit source, run long tests,
merge, deploy, contact peers or perform lifecycle actions. Save review.md and
report promptly through report_to_lead.

## Invocation preconditions satisfied

C final committed quick batch passed exit0 (web22.039s, monitor1.290s), fresh
Luna/low watcher01a2132b-e28d-7c22-83aa-59596c42c314 accounted for completed owned
session54312/no surviving work. Full updated evidence linked above. D reports
clean/published final heads, hooks/Nixfmt and cross-lock/site/semantic graph checks
passed, deployment-contract4runs/19assertions passed. Lead sampled final core
source and final workspace/config commits: only intended core3files, workspace
flake.nix/lock and configflake.lock. All intended changes are committed.

D's effective host comparison is parent config9bdb to final6f6cb: complete differing
dependency traversal (5 paired derivations) terminates at confctl source/input
metadata only. See /tmp/archive-failure-d-host-derivation-delta.json. Parent system
drv810hcsq90pyl6d47jvf9j6g0fidjwj5z and finalfggpznza8b0p7cssamc1rw65vp3bapc4 have
identical service/module/kernel/native payloads. Lead provisionally selects
profile-only rollout subject to reviewing this boundary and verifying actual
parent effects/release; do not claim older live109d equals parent candidate.
Final composed app drv/nix/store/m9pdsbnrrlwkyhp87d3cic5am7c10rbs-dev-workspace-0.2.0.drv,
output/nix/store/apjaqip0xj9cy297z2wmb8hmfqn2c8x1-dev-workspace-0.2.0, not yet built.

CI exact current candidate run45636961676/workflow354263807/attempt1 was observed
in_progress. Runtime monitor tool rejected caller ownership; no registration or
native substitute was created. Lead uses bounded read-only CI fallback while
active. No long local integration check/build/activation started before review.

D final evidence/rollout and full graph artifact are complete at unchanged heads; lead accepted delivery. Parent count corrected to34files (+4217/-232), full candidate37; no source/input change or extra check.
