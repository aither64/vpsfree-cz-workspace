**Important — General / risk:** the permanent fix still runs the first retained-source hook before preparing its dependencies. In `5dd5f0c9`, [prepare_merge](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-13-workspace-coordination/dev-workspace/libexec/workspace-coordination-execution.rb:282) calls `retain_commit` before `prepare_merge_hooks`. [retain_commit](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-13-workspace-coordination/dev-workspace/libexec/workspace-coordination-execution.rb:193) creates a worktree, which invokes `post-checkout`. The actual configuration hook requires Bundler/Overcommit immediately.

For a fresh source under the ordinary runtime environment, this can fail before the new shell initialization runs. A retry finds the already-created directory and skips that checkout hook. This is a remaining gap in the requested fix; the new tests call hook preparation directly and miss it. Include fresh retained-source creation in the preparation sequence and add a focused regression with a real `post-checkout` dependency and no inherited bundle.

No Blocking findings. **The permanent runtime correction is not fully accepted until this Important finding is fixed or explicitly dispositioned.**

**I accept the exact operator push recovery** in [recover-bootstrap-push-2026-10-14](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-13-workspace-coordination/workspace/bin/recover-bootstrap-push-2026-10-14:44), independently of that runtime finding:

- Job: `ec09fd84-f48c-4ea6-92fe-a2392f08e7a2`
- Attempt: `bb975e20-0b90-42c3-a09a-a6476353823c`
- Owner: `55e83d75-cb96-417a-9308-11d3caf22dcd`
- Repository/target: `vpsfree-cz-configuration`, `refs/heads/master`
- Approved head: `9a481ba1c69a0f22a7e84e3353d676911df2271e`
- Expected remote baseline: `8bf9da9c3be811b3e5666ccd4177c9c63e537171`

Read-only inspection confirms the original request and snapshot digests, unchanged evidence hashes, actual merge approval, `reconciling`/`push_intent` state, clean retained checkout at the approved head, and held `deployed_review` reservation. The selected package remains `m12`; its coordination implementation matches reviewed `a10af6c4`.

The recovery holds the original worker and repository locks, reruns the actual post-merge hook, performs a normal exact-SHA push, and leaves settlement to ordinary reconciliation. An already-published head returns without replaying the merge. Changed baselines refuse; uncertainty retains the original claim. Execution must retain the declared bundle, supervised exclusion and selected package, and pass every guard. I made no live remote probe; the script performs that validation.

All four lanes were assessed directly:

| Lane | Conclusion |
|---|---|
| General | Important cold-source preparation gap above. Exact recovery guards and retry ordering are sound for this retained attempt. |
| Architecture/repetition | Generic environment preparation belongs in the runtime. The dated recovery is appropriately confined to one existing operation and reuses installed validation and reconciliation. |
| Scope/proportionality | No new scheduler privilege, ownership transfer, replacement job or recovery framework. The bounded maintenance addition is proportionate. |
| Risk/compatibility | Allowlisted capture, marker validation, PATH restoration and retained transport address the demonstrated failure. Existing artifact/worker formats remain readable. Recovery requires no package switch. |

Complete histories and final diffs match the previous inventory plus the declared additions:

| Repository | Complete series |
|---|---|
| dev-workspace, base `fea04c6d` | `2727495f` → `0264c6b4` → `ef4ec58d` → `a10af6c4` → `5dd5f0c9` |
| Extension, base `505ffc45` | `01faecf6` → `c697acc7` |
| Workspace, base `90005ea3` | `4ae8cea7` → `2c212466` → `aadaa171` → `b78dc0a4` → `6239414c` |
| Configuration, base `8bf9da9c` | `abc0dae8` → `9a481ba1` |

Reviewed new heads are `5dd5f0c9e5c3679de3b5b5899eb7ef76c02db869` and `6239414c4026102be503640e64e32850fdae26e2`. Feature worktrees are clean. No obsolete unmerged approach or redundant pin stream remains; consumed helper predecessors retain their immutable operational history. **No migrations.** No new dependency selection or installed API/schema change appears in this delta.

Recorded verification passes **3 tests/14 assertions**, the supplementary coordinator suite **44/282**, and retained-target dependency checks. Their recorded hashes match. Pure Engine loading resolves `RbConfig` without workspace-host. These results do not cover the Important ordering gap.

Recovery acceptance does not authorize foreign tracking publication, package activation, finish/release, reboot or lifecycle closure. After recovery, ordinary reconciliation must prove success for the original job. No agents, mutations, live RPCs or long checks were run by this reviewer.