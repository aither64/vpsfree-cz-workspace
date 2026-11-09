# 2026-11-08-documentation-governance-review

## Goal

I'd like you to evaluate if it would be worth it to add a specialized team member responsible for writing documentation. I have a problem with that the docs being added is sometimes being put into disrupting places... like random notes in README about some new featureor usage. For example in vpsAdminOS readme sections "Automated flake updates" and "Explicit ZFS Full Suite" add just noise... it should of course be documented somewhere, but not in entry point as README. Or this in vpsfree-cz-configuration README:

```
vpsAdmin configuration

See API configuration and abuse notice processing.
Mail operations

See mx2 relay verification and deployment prerequisites for the isolated SMTP check and queue recovery constraints.
Aitherdev operations

See disk cleanup and retention for Nix profile/test retention, coordination collection, and rollout/recovery.
```

I also dislike where end-result documentation is being mixed with operational/deployment procedures, this can be seen in vpsfree-cz-configuration. While operations and deployment runbooks are useful, they should be clearly organized. These things are temporary and get out of date and useless and still they pollute the end-result/lasting documentation.

So I'd like to improve rules for writing docs, improve the review process to catch these issues as well and I wonder if having a dedicated team member (new doc role) would be helpful. Please investigate and suggest a solution.

## Affected repositories

Read-only investigation: this workspace's documentation/team procedures;
`dev-workspace` documentation skill; `vpsfree-dev-workspace` review/writing
skills; `vpsadminos` and `vpsfree-cz-configuration` default-branch docs.
The original proposal was read-only; implementation now registers feature
branches in all five repositories listed above (including workspace).

## Approach

The retained Full-team architect investigates the named examples, traces the
applicable authoring/review guidance, and proposes the smallest effective
change. Evidence is bounded to relevant entry points, linked pages, skills and
role support. The lead accepts findings and presents the recommendation.

## Decisions

- Initial scope was investigation and suggestion. The user subsequently
  authorized governance/review edits and targeted documentation moves; adding or
  reconfiguring members remains excluded.
- User additionally requested an explicit directory/file convention separating
  end-result documentation, operations, upgrade guidance and rollout records.
- Distinguish durable system explanations, reusable operational procedures,
  supported upgrade paths and individual rollout evidence.
- Evaluate a specialized role by its unique contribution and coordination cost;
  adding a role must not replace implementers' factual responsibility or final
  independent review.

## Compatibility and deployment

No runtime, schemas, protocols, configuration inputs or deployments change.
The proposed organization must preserve supported upgrades, safety constraints,
recovery contracts and discoverability when separating mixed documents.
No merge, deployment or lifecycle action is authorized or planned.

## Documentation

Readers: the workspace owner deciding documentation policy and team structure.
Findings and proposed packages belong in this session's `design.md`; current
status belongs in `state.md`. The subsequent implementation delivers policy at canonical generic/site sources,
local workspace mappings/editor conventions and the two targeted documentation
cleanups; no installed package selection is changed.

## Testing plan

Read source guidance and named examples at recorded revisions; verify claims
and recommended destinations against the actual layout. No builds or runtime
tests were useful for the original proposal. Implementation quick checks,
independent final review and pinned documentation builds apply under the
authorized implementation scope. Routine investigation/findings/session records
alone do not trigger automatic substantive-change review.

## Investigation outcome

D1 accepted: see [design.md](design.md) for exact evidence, directory convention,
README contract, example mapping, seven review questions and proposed P1–P4
follow-ups. Recommend routing/review improvements first and an optional existing-
implementer editor pilot; no default new member or extra mandatory review stage.

## Implementation authorization, 2026-11-09

User: "ok, implement it", referring to the proposed documentation structure,
review contract and targeted example cleanup. Implement P1–P3 on feature branches
and record optional existing-implementer editorial packages as a pilot convention.
No new role/catalog/runtime mechanism, package activation, deployment, integration
or lifecycle operation is included. Generic and site skills change at canonical
sources; installed package adoption remains a separate delivery decision.

Work packages are split by disjoint repository ownership in state.md. Architect
updates the settled implementation brief, implementers own diagnosis through
checks/commits/evidence, and reviewer0 independently reviews the complete final
series. The lead applies the user-facing writing skill directly before commits
where appropriate. Preserve existing useful layout equivalents, recovery and
upgrade semantics and old anchors. No production operation is executed.

## Merge and activation approval, 2026-11-09

User: "okay, so proceed with activation & merge", after explanation that all
five source branches need merge and packaged skills need a workspace application
user-profile rollout on aitherdev, not a full NixOS deployment. Targets:
dev-workspace/master, vpsfree-dev-workspace/master, workspace/master,
vpsadminos/staging and vpsfree-cz-configuration/master. Prepare necessary exact
composition pins, preserving unrelated current source/pins and host/profile
compatibility; verify D3 design and final changed-source review before long
package checks. A demonstrated system-deployment requirement must be surfaced
rather than silently added. No lifecycle or team reconfiguration approval.

## Delivered and activated

All five exact final heads are integrated; profile generation229 installs the
reviewed composed application with updated authoring/review skills. Independent
review, source/graph compatibility, required package/check outputs and installed
health/current-thread/native/system evidence passed. Typed aitherdev reservation
released and verified. Full rollout/source/store/lineage evidence in rollout.md;
current summary state.md. No full system deployment, new member, lifecycle action
or remaining operator step. Preserve branches/session for follow-up.
