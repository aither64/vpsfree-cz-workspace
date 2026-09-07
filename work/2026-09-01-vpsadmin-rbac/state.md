---
lifecycle: active
---

# 2026-09-01-vpsadmin-rbac

## Repositories

- `vpsadmin`
  - Existing read-only source used for the exploration:
    `worktrees/2026-06-15-vpsadmin-events/vpsadmin`
  - Branch: `2026-06-15-vpsadmin-events`
  - Head: `131ef638075a652cdfaecdbe163f137f7716056f`
  - The head matched `origin/2026-06-15-vpsadmin-events` and the worktree was
    clean when the architecture source was inspected.
  - At the time of inspection, the branch was 55 commits behind and 127 commits
    ahead of fetched `origin/master`.
  - No RBAC feature branch or worktree has been created because this initiative
    is currently an architecture exploration only.
  - A final status check later observed unrelated concurrent modifications and
    unresolved conflicts in this existing events worktree. This initiative did
    not create or alter them and stopped using the worktree.
- `haveapi`
  - Existing read-only source used for the exploration:
    `worktrees/2026-06-15-vpsadmin-events/haveapi`
  - Branch: `2026-06-15-vpsadmin-events`
  - Head: `d4941f2b9098751a75f94c9cdf4988384215fb5d`
  - The head matches `origin/2026-06-15-vpsadmin-events` and the worktree is
    clean.
  - At the time of inspection, the branch was 4 commits behind and 5 commits
    ahead of fetched `origin/master` at
    `0138a2a8497604ba6db98453a9f02cda2892a83e`.
  - A small Ruby-server framework change is now a definite design dependency;
    vpsAdmin-specific RBAC semantics remain in vpsAdmin.
- Possible later consumers and deployment repositories are listed in
  `plan.md`; none were modified.
- The shared coordination checkout already had an unrelated modification to
  `AGENTS.md` and other unrelated untracked paths. They were left untouched.
  Only this initiative's tracking files were edited.

## Status

- Verified that both `VPSFREE_DEV_SESSION_SLUG` and
  `bin/dev-session current` identify `2026-09-01-vpsadmin-rbac`.
- Read the top-level workspace instructions and the vpsAdmin and HaveAPI
  repository-local `AGENTS.md` files.
- Fetched the vpsAdmin SSH origin and compared the events branch with current
  upstream `master`.
- Inspected the present user, session, token-scope, authorization, ownership,
  transaction, event-policy, routing, and WebUI context-switching models.
- Inspected HaveAPI's authorization and action-execution paths.
- Compared the requirements with primary guidance for NIST RBAC, Active
  Directory security groups and delegated ACLs, Azure RBAC, OWASP
  authorization, and Zanzibar-style relationship authorization.
- Wrote a proposed architecture, compatibility bridge, rollout plan, test
  strategy, and open decisions in `plan.md`.
- Refined the plan after user review to make HaveAPI changes explicit, show the
  concrete schema, remove numeric user levels completely in the target, and
  define a release-blocking no-privilege-expansion invariant.
- No code, schema, API, WebUI, generated client, deployment configuration, or
  production state has been changed. Nothing has been committed or pushed.

## Commands run

- Session and workspace checks: `bin/dev-session current`, environment and Git
  status inspection.
- Repository inspection: `git fetch`, `git status`, `git rev-parse`,
  `git rev-list`, `git log`, and targeted `git diff` comparisons.
- Source discovery and reading: `rg`, `rg --files`, `find`, `sed`, `wc`, and
  `cat` against vpsAdmin and HaveAPI.
- Internet research was limited to primary or authoritative NIST, Microsoft,
  OWASP, and Google publications linked from `plan.md`.

## Results

- The existing `User` model combines at least four concepts that delegated
  access needs to separate: login principal, resource-owning account, quota and
  billing subject, and platform privilege level.
- The current numeric user levels combine coarse ordinary-account classes with
  platform-wide support/admin authority; they are not tenant-scoped RBAC
  roles. Existing HaveAPI session scopes attenuate a token; they do not grant
  resource access.
- `User#level` cannot be replaced only at `User#role`: raw levels also gate
  system configuration, monitoring data, console validity, administrator
  recipient selection, DokuWiki integration, and parts of the public User API.
  The target removes the numeric level and replaces each meaning explicitly.
- HaveAPI's existing `pre_authorize` hook is early and its `restrict` primitive
  supplies only equality filters. The clean design adds generic deny-only,
  validated-input, post-prepare, relation-scope, and record-authorization
  primitives to the Ruby server. HaveAPI does not learn vpsAdmin permission
  names or database roles.
- vPSAdmin authorization is distributed across roughly 526 action authorization
  blocks. A safe rollout therefore needs a declarative policy inventory,
  coverage checks, query scoping, and shadow evaluation before enforcement.
- The events initiative is a good prerequisite. It already separates the event
  subject from the actor and reserves `rbac`/`rbac_route` routing vocabulary.
  Its Event API is delivery history, however, and must not be treated as a
  complete security audit log.
- Recommended model:
  - create one `AccessDomain` for every existing top-level `User` account;
  - make users login principals that join domains through memberships;
  - use domain-local groups for **who**, roles for **what**, and scoped role
    bindings for **where**;
  - keep current resource `user_id` ownership, quotas, billing, and node-facing
    behavior attached to an immutable legacy account row during the compatible
    rollout, while adding `access_domain_id` to converted resources;
  - attribute actions and events to the actual sub-user principal;
  - maintain a separate append-only security audit stream for membership,
    group, role, and grant changes.
- The proposal deliberately excludes explicit deny rules, group nesting,
  cross-domain trusts, and arbitrary ACL entries from the first version. These
  features add substantial evaluation and escalation complexity without being
  required for the initial delegation use cases.
- Activation of real delegated sessions is not safe while old API or worker
  processes can still handle requests. Additive migrations and shadow policy
  evaluation are mixed-version safe; enforcement needs a coordinated vpsAdmin
  service update and feature gate. No coordinated vpsAdminOS node update is
  expected because legacy ownership remains stable.
- Before delegation, effective access is the intersection of legacy and
  candidate decisions at action, query, object, input, and output levels. Any
  candidate allow paired with a legacy denial is a release-blocking security
  mismatch. Unconverted actions remain owner-only and never run a sub-user as
  the legacy account principal.

## Verification

- Checked the tracking documents for trailing whitespace, unfinished-work
  markers, heading structure, and balanced fenced blocks.
- Rechecked the HaveAPI source worktree as clean after the read-only
  investigation.
- No application tests were run because there are no code or schema changes.
- Mandatory change review is not applicable to an architecture-only tracking
  update; it will be required after each coherent implementation slice is
  committed and its quick checks pass.

## Open questions

The detailed decision list is in `plan.md`. The highest-impact product choices
to settle before implementation are:

1. Whether a person may belong to multiple domains in the first public version,
   even though the schema should support it from the start.
2. Which built-in roles and permission keys form the first supported contract.
3. Whether custom roles ship with the pilot or follow the built-in-role rollout.
4. Which scopes are included initially: domain and individual VPS are the
   recommended minimum.
5. Which event categories are ordinary operational history versus sensitive
   domain security history.
6. Whether domains need shared routes or only personal routes plus an explicit
   catch-all receiver initially.
7. Whether API tokens can be issued directly to groups/service principals in
   the first release or remain tied to human memberships.
8. Whether production levels 1/2/3 encode non-authorization business
   distinctions that must survive as explicit account entitlements.

## Cleanup

- No new project worktree, branch, build output, database, or temporary artifact
  was created.
- This initiative did not modify the existing events or HaveAPI worktrees.
  The events worktree was later observed dirty from concurrent activity as
  recorded above; the HaveAPI worktree remains clean.
- `work/2026-09-01-vpsadmin-rbac/plan.md` and this state file remain as the
  durable handoff for the exploration.
