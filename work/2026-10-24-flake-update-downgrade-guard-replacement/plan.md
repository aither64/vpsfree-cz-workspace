# 2026-10-24-flake-update-downgrade-guard-replacement

## Goal

i'd like you to update all automated updated of flake inputs using github workflows to make sure that the update cannot actually cause a downgrade. for example, I sometimes set nixpkgs input to a revision that is not yet propagated into a channel, in order to deploy a fix. the automated workflows mustn't replace this revision with an older revision that doesn't yet contain the fix. not sure how to implement this, but I guess we should somehow check that the new revision is not behind the current revision. maybe this would be useful to have in confctl itself. suggest a solution.

## Affected repositories

Investigation scope: all canonical workspace projects with automated GitHub
flake-input updates, the coordination workspace, and confctl as a possible
shared implementation owner. Architect will inventory exact affected projects.

Identified implementation scope: confctl, haveapi,
terraform-provider-vpsadmin, vpsadminos, vpsf-status, vpsfree-irc-bot,
vpsfree-cz-configuration and vpsadminos-org-configuration. Exact inspected refs,
workflow paths and scope limitations are in [design.md](design.md).

## Approach

Prepare an evidence-backed solution proposal before application changes. Inspect
the actual updater workflows and confctl's current update path. Prefer proving
that the proposed locked commit contains the currently locked commit; commit
dates and revision counts do not establish ancestry.

Architect owns investigation and `design.md`; lead owns scope, acceptance and
user communication. Implementation members remain available for subsequent
execution packages. No source changes, workflow execution, integration or
deployment is part of this proposal phase.

## Decisions

- User authorized implementation: "great, implement it". This covers the guard,
  all seven consumer workflows and required confctl pin bootstrap, feature
  publication, checks and mandatory review. It does not authorize default-branch
  integration or machine deployment.

- Treat the user's final request, "suggest a solution", as a request for a
  concrete design and rollout recommendation first.
- Distinguish a known non-forward candidate from an inability to prove ancestry.
- Assess the full changed lock graph and stale automation branches, rather than
  checking only the intended top-level input.

## Compatibility and deployment

Design must preserve intentional manual pins, fail safely on divergent/unknown
history, and explain intentional branch switches and rollbacks. Investigate
tool-version bootstrap and ordering before recommending workflow adoption.

## Documentation

Readers: repository maintainers and operators managing manual advance pins.
Proposal and repository evidence belong in this session's `design.md`. Lasting
CLI behavior and repeatable operations would belong in confctl documentation
with implementation, and workflow usage belongs with each consumer.

## Testing plan

Proposal acceptance: complete local-ref workflow inventory; source-backed
confctl fit; defined outcomes for equal/ahead/behind/diverged/unknown revisions,
unsupported sources, transitive updates and moving target branches; bounded
implementation packages with dependency order and meaningful test cases.
No application checks or builds needed during read-only investigation.
