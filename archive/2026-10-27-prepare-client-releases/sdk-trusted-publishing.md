# SDK 0.1.1 GitHub trusted-publishing prerequisites

Owner: implementer0. **GitHub prerequisites configured and verified; ready for
combined independent review before release.** Applies only to prerequisites for
`vpsfreecz/vpsadmin-typescript-client`; source/Git belongs to implementer1 and
integration/tag/publication to the lead. No credentials or npm account settings
are read or changed. Version 0.1.0 and its artifacts remain untouched.

## Authority and baseline

The user requested release 0.1.1 to exercise trusted publishing. Lead assigned
routine setup; architect0 recorded exact API requests in `design.md` under the
SDK trusted-publication milestone. Read the brief, repository
`docs/releasing.md`, `docs/development.md`, pinned flake and release workflow.
No repository AGENTS.md is present. Session binding and saved member access
were verified without SDK Git operations.

Fresh read-only baseline: zero environments, zero repository Actions variables,
no repository rulesets. GitHub reviewer `aither64` is user ID `4717906`.
No existing settings need replacement. Record safe readbacks after writes.

## Approved exact requests

1. PUT `/repos/vpsfreecz/vpsadmin-typescript-client/environments/release`:

   ```json
   {"wait_timer":0,"prevent_self_review":false,"reviewers":[{"type":"User","id":4717906}],"deployment_branch_policy":{"protected_branches":false,"custom_branch_policies":true}}
   ```

2. After checking for duplicates, POST the environment's
   `/deployment-branch-policies` with `{"name":"v*","type":"tag"}`.
3. After protected-gate readback, POST repository `/actions/variables` with
   `{"name":"NPM_RELEASE_ENABLED","value":"true"}`.

Use `gh api --input` JSON files through the SDK pinned Nix tools. On an uncertain
write, reconcile the exact resource before retry; preserve concurrent changes.

## Readback and remaining boundaries

Environment and tag-deployment gate are verified. Created `release` environment
ID `25494232596`, required-reviewers rule ID `70321400` with User `aither64`
ID `4717906` and `prevent_self_review: false`; the zero wait timer has no active
wait rule. Custom branch-policy protection rule ID `70321402` and deployment
settings are `protected_branches: false`, `custom_branch_policies: true`.
The deployment-policy list was empty before creation; it now contains exactly
policy ID `64571929`, name `v*`, type **tag**. No branch entry was added.

The enable variable was absent on a fresh read after gate verification, then
created at 2026-10-27T18:26:38Z. GET confirms name `NPM_RELEASE_ENABLED` and value
exactly string `true`. GitHub current caller is `aither64`/`4717906`, and the
repository collaborator-permission endpoint confirms `admin`/role `admin`.
This caller matches the required reviewer with self-review allowed; no pending
SDK deployment exists yet to query per-job `current_user_can_approve`, and no
approval was attempted.

Environment protection is separate from release-tag creation permission.
Lead approved architect design of the smallest conventional active creation-only
v* tag ruleset with repository-admin bypass, satisfying `docs/releasing.md`
step 5. Read the completed brief before mutation, rechecked the empty ruleset
list and caller admin permission, then created and independently read back the
single ruleset below. No concurrent settings were replaced and no retries were
needed.

### Tag creation request and exact safe readback

POST `/repos/vpsfreecz/vpsadmin-typescript-client/rulesets` with this JSON:

```json
{
  "name": "Release tag creation",
  "target": "tag",
  "enforcement": "active",
  "bypass_actors": [
    {"actor_id": 5, "actor_type": "RepositoryRole", "bypass_mode": "always"}
  ],
  "conditions": {
    "ref_name": {"include": ["refs/tags/v*"], "exclude": []}
  },
  "rules": [{"type": "creation"}]
}
```

Created ruleset ID **25982494**. GET by exact ID matches every field above and
reports `current_user_can_bypass: "always"`; the repository ruleset list contains
only this ID. There are no update/deletion/signing/status rules, other bypass
actors or exclusions. The architect verified built-in role ID 5 is admin against
[GitHub's reference](https://github.com/github/awesome-copilot/blob/main/skills/repo-standardizer/SKILL.md)
and [GitHub Docs' own ruleset](https://github.com/github/docs/blob/main/.github/rulesets/docs/main-branch-protection.json),
and verified creation/actor/condition fields against the current official REST
schema. The actual API accepted the exact request and read it back unchanged.

### Final configuration verification

At **2026-10-27T18:28:38Z**, fresh GETs and in-memory assertions verified:

| Resource | Exact result |
| --- | --- |
| Environment | `release`, ID `25494232596` |
| Required reviewer | Rule `70321400`, sole User `aither64` / `4717906` |
| Self-review / timer | `prevent_self_review: false`; wait timer zero |
| Deployment protection | `protected_branches: false`, `custom_branch_policies: true` |
| Deployment policy | Sole entry `64571929`, name `v*`, type `tag` |
| Repository variable | `NPM_RELEASE_ENABLED`, exact string `true` |
| Creation ruleset | Sole ID `25982494`, exact JSON above, active |
| Caller eligibility | Authenticated required reviewer has admin role and ruleset bypass `always` |

The authenticated reviewer's identity plus allowed self-review establishes the
configured approval path. No 0.1.1 pending deployment exists yet to query its
per-job approval eligibility. No source Git commands, source edits, workflow
changes, main/tag pushes, npm publication or protected-environment approval ran
under this package. No 0.1.0 package or artifact was changed.

The npm account publisher must match organization `vpsfreecz`, repository
`vpsadmin-typescript-client`, workflow `release.yml`, environment `release`, with
direct-publish permission. That private account state is not established by
GitHub readbacks. The authorized 0.1.1 workflow will test OIDC acceptance.

## Baseline and restoration information

Baseline is empty: these are newly created resources. To restore it, a separately
authorized operator would first reconcile pending releases and verify each
resource still matches this receipt, then remove only ruleset ID `25982494`,
variable `NPM_RELEASE_ENABLED`, tag deployment policy ID `64571929` and environment
`release` / ID `25494232596`. Use their exact resource-specific DELETE endpoints;
never bulk-remove policy or overwrite concurrent changes. No restoration/deletion
is executed or authorized by this receipt.

The npm account fields and actual OIDC publication acceptance remain unverified;
the intended 0.1.1 workflow tests them. Lead owns final combined source/config
review, source integration approval, checks, tagging and protected publication.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-prepare-client-releases/
