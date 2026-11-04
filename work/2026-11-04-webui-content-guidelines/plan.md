# WebUI process and content-guidance investigation

## Goal and scope

Evaluate vpsadmin-webui instructions, development workflow and design/content
rules against the user’s concerns: routine healthy-state banners, excessive
explanatory text and weak information hierarchy. Recommend improvements,
additions and removals with concrete source evidence. Investigation only;
no application/rule changes, deployment, PR, publication or integration.

## Affected repositories

- vpsadmin-webui: read-only inspection of canonical bare repository and its
  verified default revision; no feature branch or worktree required.
- Coordination workspace: this session’s tracking and findings only.
- Linked policy sources may be read where needed to establish applicable rules.

## Approach and owners

- Lead: scope, source/claim acceptance, tracking, final recommendations.
- architect0 (ready, workspace_write, retained Astra/xhigh): own substantive
  investigation and investigation/design brief; identify independent evidence
  packages for saved implementation members if useful.
- Saved implementers: read-only evidence packages only when independent scope
  is established; no product implementation is requested.

## Acceptance criteria

Identify existing rules and their actual authority; distinguish missing policy
from ignored policy. Give representative file/line examples of noise and
necessary information. Evaluate workflow quality and proportionality. Prioritize
keep/simplify/remove/add recommendations, include exceptions for useful action
feedback, uncertainty, operational risk and accessibility. State source and
runtime-inspection limitations.

## Compatibility and deployment

No schema, API, client, protocol, persistent state or configuration changes.
No deployment or rollback required. Future content changes must preserve useful
state, accessibility, permission boundaries and safety-critical explanations.

## Documentation and checks

Audience: user deciding future product/process direction. Findings and evidence
belong in this session; proposed rules are recommendations rather than adopted
project policy. Read applicable procedures; verify citations at pinned revision,
compare prescribed checks with manifests/CI where relevant. No application
build/test runs justified by this read-only investigation. Routine investigation
and findings do not trigger automatic final change review.
