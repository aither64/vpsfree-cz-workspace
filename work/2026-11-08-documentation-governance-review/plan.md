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
No feature repositories or branches registered for this proposal.

## Approach

The retained Full-team architect investigates the named examples, traces the
applicable authoring/review guidance, and proposes the smallest effective
change. Evidence is bounded to relevant entry points, linked pages, skills and
role support. The lead accepts findings and presents the recommendation.

## Decisions

- Scope is investigation and suggestion, without applying governance edits,
  moving project documentation, or adding/reconfiguring team members.
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
status belongs in `state.md`. Applied policy and repository documentation are
possible follow-up work, not deliverables of this investigation.

## Testing plan

Read source guidance and named examples at recorded revisions; verify claims
and recommended destinations against the actual layout. No builds or runtime
tests are useful for a proposal. Routine investigation/findings/session records
do not trigger automatic substantive-change review.
