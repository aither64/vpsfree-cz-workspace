# Merged one-time nginx fix update

Both remote master branches contain exact final reviewed heads:

- vpsfree-cz-configuration: `828c390c7e1857f11522933977afd852634b85f8`.
- vpsadminos-org-configuration: `72c18d811086dac8e16ec8c7ee6bf8e32ce62123`.

Each changes only three generated locked fields, preserving flake.nix and normal
nixos-26.05 tracking. Selected one-time nixpkgs revision is
`4077fb98f09d5bd847f848ae4f214a4c5b9f0a9d`, containing PR #589970.
Quick checks and independent complete-history assessment pass. No obsolete
streams or migrations. No deployment was executed.

## Deployment commands

Run from each repository's checkout of updated master. Pinned confctl builds
selected generations first, then serializes copy, activation and health checks
with --one-by-one. Listed pattern order is not a deployment-order guarantee.
Patterns were checked with Ruby File.fnmatch? FNM_EXTGLOB against evaluated
inventory: exactly 17 A targets and four B targets, no additional match.

vpsfree-cz-configuration:

```sh
nix develop -c confctl deploy --one-by-one 'cz.vpsfree/{containers/{discourse,int.blog,int.kb,int.munin,int.utils,int.vpsfbot,int.web,prg/proxy},machines/{aitherdev,brq/apu,build,em1,prg/apu},vpsadmin/{int.vpsadmin-webui1,int.webui-dev,int.webui1,int.webui2}}' switch
```

vpsadminos-org-configuration:

```sh
nix develop -c confctl deploy --one-by-one 'org.vpsadminos/{int.images,int.iso,int.www,proxy}' switch
```

All selected active nginx packages evaluate to stable 1.30.7 with fixed upstream
source, including Discourse custom package and images/ISO fancyindex variants.
The other evaluated changed-channel consumers have nginx disabled. vpsAdminOS
nodes using unchanged staging/production inputs are outside this deployment list.

These results describe desired configurations. No fleet build, running-version
inspection, activation or runtime rollback check is claimed. Whole nixpkgs input
advances other packages as well; normal build/activation checks still apply.

## Evidence

- [Design](design.md), [review](review.md), [current state](state.md).
- [vpsFree package and exact selectors/FQDNs](package-a.md).
- [vpsAdminOS.org package and exact selectors/FQDNs](package-b.md).

Both repository claims were released and verified after exact remote proof.
All verification commands/utilities quiescent. Feature refs and session retained;
no lifecycle action requested/performed.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-18-nixos-channel-update/)

## Confctl follow-up implementation

User accepted D4 proposal and requested formal design then implementation. D5
brief is in design.md; one owner implemented complete source/tests/docs package.
Feature commit d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49, base
ff5e017780a35fb97b549db2a51b570193867c3b, published at
refs/heads/2026-11-18-nixos-channel-update in vpsfreecz/confctl. One coherent
14file commit, no migrations/dependency/pin/workflow changes. Clean worktree;
exact remote head equality and comparison recorded. No confctl integration yet.

Expected behind upstream is successful no-update; independent inputs advance,
whole rejected candidates discarded; one final validated lock installed/committed.
Strict check-update and hard rejection/evidence errors retain failures. Skip
messages include retained and candidate revisions. No new flag required.

Independent all-lane review no findings, focused128examples pass, full245examples
zero failures/two existing packaged-CLI pending, full lint110files no offenses,
required hooks/man generation pass. Ruby matrix3.3/3.4/4.0 and RuboCop CI pass;
self-hosted integration run44372697108 passed19:09:36UTC (four tests successful).
All CI is green at exact reviewed head.

Evidence: [C implementation](package-c.md), [review](confctl-review.md),
[review packet](confctl-review-packet.md), [semantics/design](forward-only.md).
Confctl default integration requires separate approval; original direction named
only configuration repos. Updating their confctl dependency is a later adoption
step; both currently keep old ff5e017 and old daily-update behavior. No version
release, configuration adoption or machine deployment performed for C.

Confctl implementation is ready for merge approval into master. No source changes
remain; updating configuration confctl pins is a separate adoption step.

## Confctl merge outcome

User explicitly approved merge. Exact reviewed/tested d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49
fast-forward merged and pushed to confctl/master; fresh remote equality proved.
Claim92a761f8-fc14-4ff5-939f-5ecabe702f6f released and resulting state verified.
No new patch/rebase or source changes; prior all-green CI remains exact-head proof.
Earlier awaiting-approval passages above are historical checkpoints, superseded
by this outcome. Configuration confctl pins still ff5e017 until separate adoption.

## Final adoption outcome

User approved continuation. Both configuration/master branches now pin reviewed
confctld8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49:

- vpsfree-cz-configuration finalbf19f6aacae7f57c8bd06746ff10481b242baf2f.
- vpsadminos-org-configuration finalfadb89a3f828bc98ea75aa5fcd8de953390c15e2.

Fresh remote equality proved after normal ff-only integration, separate claims
released/verified. This supersedes earlier not-yet-adopted checkpoints. Generated
lock-only updates preserve entire nginx4077fb98 identity and nixos-26.05 original,
all sibling/nested/follows values. Both updated tools/channel mappings smoke pass;
independent new+cumulative history assessment no findings. Exact provider review/
full checks/all-green CI reused. No system activation needed for tool adoption:
next scheduled daily workflow loads the corrected --forward-only semantics.

Original21 nginx targets and --one-by-one deployment commands above remain valid.
No deployment executed; no session lifecycle action. Evidence:
[adoption review](adoption-review.md), [A2](package-a2.md), [B2](package-b2.md).
