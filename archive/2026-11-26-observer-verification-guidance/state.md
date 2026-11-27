---
lifecycle: archived
---

# Observer verification guidance

## Current status

**Delivered and verified.** A subsequent workspace deployment already installed
the exact reviewed observer guidance. No additional build or activation is
needed. Session stays open; no lifecycle action or live member reconfiguration
was performed.

- Installed package: `/nix/store/6j7rpx2j176blr46602kzzpb8ycm1mwp-dev-workspace-0.2.0`.
- Installed derivation:
  `/nix/store/ifpsi7200wia0v0dcr091kgamq4w62wd-dev-workspace-0.2.0.drv`.
- All seven observer presets contain the exact reviewed 4087-byte prompt;
  text SHA256 `6057ebc7639a99651ae5ca4b70d85f8761537cdf3bfa43beedfc020ee793d011`.
- Installed catalog digest:
  `4ae58b06cf34c345d952f2ce0288a78d739c5ee06584292062220a217e7f7922`.
- Existing observer0 retains its saved 4021-byte prompt. New selections use the
  deployed default; no retained settings/instructions were silently refreshed.

## Phase checklist

- [x] Design and implementation
- [x] Change-specific quick checks, with unrelated baseline failure recorded
- [x] Independent final source review, no findings
- [x] Approved workspace/master integration and remote proof
- [x] Installed delivery verified from the subsequent deployment
- [x] Health and continuity acceptance; no further work or resources held

## Ownership and acceptance

| Package | Owner | Status | Evidence |
| --- | --- | --- | --- |
| Observer design and bounded refresh design | architect0, Astra/xhigh | Accepted | [design.md](design.md) |
| Prompt/guide, checks, commit/publication | implementer0, Sol/xhigh | Accepted | [review-packet.md](review-packet.md) |
| Independent final source review | reviewer0, Sol/xhigh | Accepted, no findings | [final-review.md](final-review.md) |
| Deployment preparation and installed verification | implementer0, Sol/xhigh | Accepted; no remaining gap | [rollout.md](rollout.md) |
| Integration, freshness, ownership and final delivery acceptance | lead | Done | Fresh ancestry and claim receipts below/in rollout |

Bound session identity verified through `dev-session current` from the tracking
directory. Both shell markers were absent on the resumed turns; trusted exact
thread/workspace binding remains authoritative. Retained roster/access/settings
were verified; no members were added or reconfigured.

## Implemented behavior and source review

The observer now challenges costly serial verification and disproportionate
verification infrastructure, asks the lead to reassess design and verification
strategy, and recommends bounded shared-cause diagnosis plus related-fix batching
and faster faithful checks. Required review, final acceptance and advisory-only
observer authority remain preserved.

Only `config/agent-teams.nix` observer strings and the existing related
`docs/agent-teams.md` prose changed in the original feature. Independent general
review was LOW risk, retained reviewer0 `gpt-6.1-sol`/xhigh, native thread
`01a21790-4f7b-7a72-8c69-6244aa08321d`, without fallback/overrides. No Blocking,
Important or Advisory findings. Complete one-commit feature history has no
obsolete approaches, repeated update streams or migrations.

Quick source catalog/comparison/size and whitespace checks passed. The existing
focused instruction suite was 10 runs/220 assertions/one failure/zero errors:
unchanged AGENTS.md exceeded its 16384-byte budget at 16550 bytes. An exact-base
reproduction established the same failure and identical test/core blobs. Nine
tests passed; full-suite success was never claimed. The proven baseline failure
was accepted for this bounded change; no assertions or hooks were bypassed.

## Integration and source equivalence

- Canonical workspace remote: `git@github.com:aither64/vpsfree-cz-workspace.git`,
  target `refs/heads/master`.
- Feature branch `2026-11-26-observer-verification-guidance`, exact final head
  `844ac4dbf768ebced1d27d208f4d5ebaf8b82deb`, reviewed over
  `bbfaf615b7c1406fc028a486330efda9fb35cb04`.
- User explicitly directed “merge it”; lead fast-forward merged/pushed and
  verified exact remote equality. Merge claim5c40fa3c-d319-4cd0-9638-b351133e4e2a
  was released and resulting state verified on November26.
- Fresh SSH default read now returns integrated root
  `0d24fd5596e65ae1e918e9441142d1e11bf418ec`; both that root and original
  feature844 are ancestors of the fresh remote default (exit0).
- One **no-build** pure evaluation of immutable integrated root0d24 exactly
  equals the installed derivation ifpsi7200.... This proves an independently
  reproducible integrated source for the current artifact. It does not invent
  the historical Git head used by the other deployment.
- Current application runtimebbe27c6ffb5f367e7be9a4ce45bffdf34185854f and
  unchanged extensionbf12ac71a8a00b1581eed5352f99c1b2daaeff5b/codex-web
  2547d535eefd4154afef4125ea0fb76e5894a8b6 have fresh remote-default ancestry
  proof in rollout. Complete source/input graphs remain linked there.

## Configuration-mediated delivery and resources

User authorized deployment and explicitly required vpsfree-cz-configuration
mediation. November26 preparation used the exact deployed configuration tools
and existing cross-repository checker. After two bounded setup corrections, one
actual application build passed in87.543s; old candidate spsm07ac... was never
activated by this session. No system build, configuration pin edit or new test
infrastructure was introduced.

Machine-only claim4ace1db8-6721-45f6-99fd-06624bd570db queued, then granted after
another deployment changed the live baseline. Lead verified the stale boundary,
made no activation attempt, released the unused claim, and verified released
revision3 at2026-11-27T11:01:44Z before any refresh investigation. No machine,
repository, job or unfinished command effect remains owned.

The intermediate installed recovery-bridge generation lacked the new prompt.
Its transition prerequisite correctly prevented an unrelated stale deployment.
The current6j generation uses ordinary updated guidance and already contains the
feature; no bridge transition is needed for this task. No historical cleanup
claim, private helper, original operation action or peer mutation was performed.
Earlier conditional source-pin/build proposals are superseded by verified
existing delivery; no new source change or merge approval is required.

Current effective clean host configuration:
`a3af000f116bca48dd59b9fd3f0ca46fd433a640`, runtimebbe27c6f.... Both live system
and system profile resolve to
`/nix/store/akwb3y9nqydy9nj4iv5crsk9kycnb6yd-nixos-system-aitherdev-26.05.20261121.94c3211`.
This existing host configuration is not claimed newly deployed/integrated by us.
Its SHA is not an ancestor of fresh config defaultdc1449bd...; our unchanged
registered config branch head1e43e2e18c85cf1fc63f31327d1f8e5eb953eab8 IS an
ancestor. No configuration feature content or integration is part of our change.

## Final health and continuity

Authenticated HTTPS healthz200 and session page200; required five units active
and running. Native Codex binary/socket target and tmux PID1917 remain unchanged;
retained member native IDs/settings/prompt hashes are preserved. Wrapper PID
changed with the intervening deployment and is recorded honestly. No duplicate
optional checks or rebuilds followed these acceptance results.

Final owner receipt: `checks/current-6j7-observer-delivery.json`; reproducible
source proof: `checks/current-6j7-source-derivation.log`. Raw checks remain ignored,
untracked/disposable. Public exact profile/system/source/input evidence and the
historical preparation results are in [rollout.md](rollout.md).

## Next actions and session

No further action is needed for the deployed default guidance. Updating saved
observers would be a separate explicit live-role instruction change. Preserve
feature refs/worktrees and keep this session open.

[Plan](plan.md), [design](design.md), [review packet](review-packet.md),
[independent review](final-review.md), [rollout](rollout.md).

<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-26-observer-verification-guidance/>
