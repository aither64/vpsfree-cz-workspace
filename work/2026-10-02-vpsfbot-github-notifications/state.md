---
lifecycle: active
---

# GitHub IRC notifications

## Current phase

Final implementation, quick checks and expanded independent whole-branch review
pass with no findings. Exact final heads are clean and published; comparisons
recaptured. Final VM, archive hash, scoped build and RSpec CI passed. Broader
integration CI remains queued; final_verification_watcher retains monitoring
ownership. No merge or deployment is authorized.

## Phase checklist

- [x] Analyze repository names, routing and automation identities.
- [x] User selects original-author filtering and exactly six repository additions.
- [x] Architect records accepted design before application edits.
- [x] Implement notification policy, configuration, docs and isolated VM fixture.
- [x] Quick checks/hooks and initial whole-branch review pass.
- [x] Initial VM executes expected wire behavior; archive failure investigated.
- [x] Design and implement reproduced HTML asset race fix and deterministic regression.
- [x] Final source/pin commits and quick checks/hooks pass.
- [x] Expanded independent whole-branch review, all four affected lanes, no findings.
- [x] Final publication, GitHub archive hash and signed-webhook VM pass.
- [x] Exact final scoped configuration build and RSpec CI pass.
- [ ] Broader GitHub integration CI37031196330 remains queued for a runner.
- [ ] Ready, awaiting explicit merge approval for both repositories/master.
- [ ] Production rollout/live delivery checks: not authorized.

## Complete final branch inventory

Both worktrees are under `worktrees/2026-10-02-vpsfbot-github-notifications/`,
on branch `2026-10-02-vpsfbot-github-notifications`, registered in portal.yml.

| Repository | Base | Current committed head |
| --- | --- | --- |
| vpsfree-irc-bot | 88906fd54b0fc8cf613fc2cec2fb930d8196d05a | e9c60b0b95d3cc0dad6f012d8127c2bc078cfa7d |
| vpsfree-cz-configuration | 028d70b233c5b100fea7f7aa0b945fb8b6d3ec4d | b164a3b786cb82878f00f8ebd2a7825ee5254c15 |

Bot chronological series: cf21b243 (author-filter feature) then e9c60b0b
(independent existing logger-race correction). Configuration: cf2840c1
(functional routes/policy) then b164a3b7 (fixed pin). Local committed NAR hash:
`sha256-jONz5RyWIzH2/h9oALb31Ms1pQlbwP3MNRUe1vwzp5A=`. Both exact final
heads published, upstream default branches refetched and unchanged. No obsolete
sender-only approach, fixup history or unused transitional path. Supported
legacy renderer retained. No migrations/schema/seed/persisted-format changes.
Nine already-upstream commits from old bot pin565c4b4e to base affect only
workflow/flake.lock/advisory fixture, with runtime/dependencies unchanged.
[Expanded review packet and exact diffs](review-expanded-packet.md).

## Ownership and review

architect0 retained Astra/xhigh workspace_write: designs completed before edits.
implementer0 retained Sol/xhigh workspace_write: all application edits/checks.
reviewer0 retained Sol/xhigh read_only: initial review passed without findings;
expanded complete final review passed all four lanes at high risk, without
overrides/fallback. Lead owns scope, records, prose and result reconciliation.
Long operations use fresh Luna/low operation-lifetime utility watchers from
catalog digest4676433c6831fbaca91da8ffde84891aff6ce065a17c74c2f367f1acf1d15b17.
[Expanded review](review-expanded.md), [initial review](review.md),
[accepted design](design.md).

## Verification and discovered reliability issue

Final quick checks: logger focused4/0, full RSpec112/0, RuboCop62 files clean,
Nixfmt/fixture parse/extracted Ruby/diff checks and real mandatory hooks pass.
The controlled real-file regression fails against old logger code with EACCES
and passes fixed code. Asset installation is synchronized through copying and
chmod; updates/modes and exception release remain tested. Logger code comment
owns durable rationale. Notification policy/docs/routes are unchanged by fix.

At previous cf21b243/config2b84893e, public archive hash, scoped build and RSpec
CI passed. VM reached all expected filtered/unfiltered IRC markers but failed
second-channel archive barrier. Reproduction proves existing concurrent asset
copy failure; original VM JOIN cause remains inferred because old journal tail
omitted startup. New fixture captures full boot unit journal on failure.
First earlier VM run also exposed unsupported after(:each), folded into feature.
Initial config build EOF corrected using documented `confctl build --yes`.
No unexpected local kernel compilation. [Detailed verification](verification.md).
Old integration CI37025858914 confirmed cancelled after superseding push.
Current exact-head runs: Integration Tests37031196330 and RSpec37031196334.

## Accepted behavior and runtime limits

Only #vpsfree ignores github-actions[bot]. Nonempty pushes filter original
commit authors, retain unknown authors/order, suppress all-ignored events and
show at most ten retained commits. Other events/originally empty eligible pushes
filter sender. Absent/empty policy retains legacy behavior. Exactly six approved
#vpsadminos routes added; template rename already correct and historical captures
repo now vpsfree-kb-contracts. [Repository inventory](repository-inventory.md).

Private overrides, deployed revision, hook subscriptions/deliveries and live
IRC/Matrix relay unknown; hook metadata API403. Build success cannot establish
production delivery. Later activate package/policy together; rollback is state
compatible. Old bot restores logger race and automation noise. Startup lock is
process-local, retaining one writing process per archive root assumption.
Restart can lose existing in-memory queued events. No fleet/schema update.

## Final runtime milestone

Final signed-webhook VM passed at e9c60b0b, exit0, harness169.98s. All wire and
both-channel HTML/YAML archive assertions passed unchanged. Published GitHub
archive/hash matches the final pin, exit0. Logs final-webhook.log/.status and
final-archive.log/.status. Exact b164a3b7 build passed, exit0, generation
2026-10-02--18-08-42; final-config-build.log/.status. Exact-head RSpec
CI37031196334 passed. Integration CI37031196330 remains queued under watcher
ownership; no generic timeout, cancellation or rerun. No deployment/live
delivery claim.

## Next action and coordination

Watcher continues exact integration CI; lead reconciles its result and any
failure through the retained team before final branch readiness. Explicit user
direction is still required to merge both repositories into master and deploy.
No production
replay, activation, merge, branch removal or session lifecycle action.
Initial tracking commit1ff5d9fa; current records follow consolidated cadence.
Environment/hook failures and pinned-tool workaround are in verification.md and
[reusable setup note](../../notes/cross-project/2026-10-02-nix-dev-env-restricted-member.md).
Shared master/index unrelated edits preserved. Session remains active and open.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-vpsfbot-github-notifications/)
