# vpsAdmin Rust client 0.1.0: first-publication packet

Preparation only, package `3e7e6f8e-029d-4836-be53-d63bc4bf1ebd`. The user authorized
regeneration/publication; lead must accept this concrete configuration packet and
its review route before effects. Owner3 alone edits/Gits the SDK. No default
integration, settings/secret write, dispatch, tag, upload, token read, cleanup or
lifecycle action has run. No utility slot was used.

## Actual metadata: bounded pass and authorized addendum

[observations.json](observations.json) retains exact official URL, status,
timestamp, allowed headers and filtered nonsecret JSON for the initial three
GETs at 2026-10-24 17:42:42–43 UTC. The separately authorized organization
metadata GET is in [organization-bootstrap-secret.json](organization-bootstrap-secret.json).

- Repository environment list: HTTP 200, total_count 0, empty list. `release` is
  absent. No redundant exact environment or environment-secret GET was made.
- Repository Actions secrets metadata: HTTP 200, complete empty list.
  `CARGO_PUBLISH_BOOTSTRAP_TOKEN` is absent at repository scope. Only this
  permitted name/boolean and metadata counts were retained; no other secret
  names or any values were output. Organization/inherited secret availability
  remains unknown, as qualified below. An existing secret name would not
  establish a usable token.
- Current authenticated actor: HTTP 200, `aither64`, user ID 4717906.
  The retained SDK repository response at 17:32 reports admin/push permissions;
  its exact digest/limitations are in
  [retained-repository-permissions.json](retained-repository-permissions.json).
  No write capability was exercised. A later 403 must stop; it is not permission
  to broaden settings or substitute credentials.

The one organization-secret GET at 17:46:32 UTC returned HTTP 403: GitHub
requires organization-admin or Actions-secrets fine-grained permission. This
does not distinguish absence from restricted visibility. No selected-repository
GET, retry or access repair followed. **Bootstrap credential availability is
UNKNOWN overall.** The scoped repository absence is not a request for a new
token; lead must resolve inherited availability through an authorized owner
before deciding whether a new environment secret is needed. No credential
values were requested or read.

Architect's crate/tag/Release 404 observations are retained in its design, not
repeated by this packet. They are not proof of crate-name ownership or upload
permission. Recheck the actual crate immediately before approved bootstrap using
the maintained workflow; no live token/account probe is appropriate here.

## Prepared configuration, for lead/reviewer acceptance

[release-environment.json](release-environment.json) contains:

- reviewer User 4717906 (`aither64`), bound to fresh current actor and retained
  repository admin permission evidence;
- prevent_self_review=false, consistent with the maintained single-maintainer
  workflow and lead approval of its own reviewed release;
- wait_timer=0, no unrelated custom protection rules;
- can_admins_bypass=true explicitly retains GitHub's ordinary new-environment
  admin policy. This packet does not silently harden or broaden an existing
  environment. Lead/reviewer should assess the explicit bypass default;
- protected_branches=false/custom_branch_policies=true, so deployment eligibility
  comes from the separate version-tag policy, not main ancestry.

[version-tag-policy.json](version-tag-policy.json) is exactly
`{"name":"v*","type":"tag"}`. No branch deployment policy, wildcard repository
permission change, publisher binding, auth fallback or default integration is
proposed. These policy objects must be reviewed together; creating an environment
without completing/readback of its tag restriction is not release readiness.

## Minimal accepted-effect sequence (not executed)

Run from a qualified declared operational gh environment only after lead accepts
the packet/review and confirms current repository/actor. `PACKET` below is the
absolute path to this directory. No secret value is an argument or payload here.

1. Fresh GET `repos/vpsfreecz/vpsadmin-rust-client/environments/release`:

```sh
gh api --method GET repos/vpsfreecz/vpsadmin-rust-client/environments/release
```

   If HTTP 200, compare its complete existing protection/admin/deployment settings and **do
   not blindly PUT this new-environment payload**. If403 or ambiguous404, stop
   and reconcile access. Only an authenticated absent-environment result supported
   by a complete authorized environment list permits new-environment creation. The
   initial complete list establishes absence at its observation time, not an
   unconditional future overwrite grant.
2. Create the missing environment with the reviewed JSON; retain its actual
   ID/settings response:

```sh
gh api --method PUT repos/vpsfreecz/vpsadmin-rust-client/environments/release --input "$PACKET/release-environment.json"
```

3. GET the environment's deployment policies:

```sh
gh api --method GET repos/vpsfreecz/vpsadmin-rust-client/environments/release/deployment-branch-policies
```

   Reuse an exact existing v*/tag policy; do not duplicate it. Unexpected policies require reconciliation,
   not deletion. If there is no policy, add this one reviewed object:

```sh
gh api --method POST repos/vpsfreecz/vpsadmin-rust-client/environments/release/deployment-branch-policies --input "$PACKET/version-tag-policy.json"
```

4. Read back with GET of `environments/release` and its
   `deployment-branch-policies`; prove reviewer 4717906, self-review policy,
   wait/admin settings and only intended v*/tag eligibility. Verify the API
   actually acknowledges the requested admin policy; a silently ignored field is
   not proof. Preserve responses.
   No rollback/delete is implied if partial configuration fails: report exact
   effects and stop for lead recovery.
5. Resolve the inherited-secret uncertainty through an authorized owner. Only
   if a suitable bootstrap secret is unavailable, use the conditional owner
   instructions below. A later authorized name-only metadata GET may establish
   target presence at its actual scope; it cannot establish token usability.
   Never request, print or verify a secret value. Workflow authentication/upload
   establishes actual usability; no unrelated secret metadata is retained.

GitHub references: [environment API](https://docs.github.com/en/rest/deployments/environments#create-or-update-an-environment)
and [tag policy API](https://docs.github.com/en/rest/deployments/branch-policies#create-a-deployment-branch-policy).
No configured environment exists yet, so its future environment ID is UNSET.

## Bootstrap secret: conditional owner instructions

These are prepared instructions, not a request to create a duplicate credential.
First resolve the organization-secret visibility limit. If a usable credential
is already inherited and the accepted workflow/owner policy permits that scope,
no duplicate is needed. Otherwise, after lead routes the owner-only prerequisite,
an intended first crate owner uses [crates.io API tokens](https://crates.io/settings/tokens)
from their authenticated account to create a token with the **minimum available
first-publication scope** and shortest practical expiry for this one release.
Restrict it to vpsadmin-client if the current UI supports scoping a not-yet-created
crate. Do not invent a selectable crate scope or grant ownership/yank/account
administration merely to publish. The account/name availability and the exact
UI scope are not inspected by this packet. If the service cannot issue an
appropriate minimal first-publication token, report the concrete refusal to lead.

Enter it directly as the `release` environment secret named
`CARGO_PUBLISH_BOOTSTRAP_TOKEN` at the repository's
[environments settings](https://github.com/vpsfreecz/vpsadmin-rust-client/settings/environments),
selecting release → Environment secrets → Add secret. Never send it in chat,
notes, commands, receipts or a repository file. Do not perform local cargo login.
Repository secret absence is observed, but the maintained contract's intended
placement is environment scope so it is protected by release approval.

Source `.github/workflows/release.yml` supports explicit authentication=bootstrap
and stops if the crate exists, lookup fails or token is absent. It passes the
bootstrap credential only to native cargo publish --locked; it never falls back
from OIDC. No new authentication mechanism is needed. After successful first
upload and owner binding, later OIDC registration and bootstrap-token retirement
are separate explicit owner actions; neither is performed by this packet.

## Candidate/approval boundary

The default branch already carries the manual workflow; owner3's reviewed
feature tag is a supported dispatch ref. Main integration is not required or
authorized. Final feature head, immutable annotated tag object, run/attempt,
run-bound Cargo.lock artifact/digest and candidate/actual publish archive hashes
remain UNSET. Owner3's current source/workflow transfer changes still require
committed final review and the maintained verification matrix.

After those gates and actual readiness, the lead's reviewable dispatch is:

```sh
gh workflow run release.yml --repo vpsfreecz/vpsadmin-rust-client --ref v0.1.0 -f authentication=bootstrap
```

This is **not executed or newly granted** by this packet. The future protected
approval commands are:

```sh
gh api --method GET "repos/vpsfreecz/vpsadmin-rust-client/actions/runs/$RUN_ID/pending_deployments"
gh api --method POST "repos/vpsfreecz/vpsadmin-rust-client/actions/runs/$RUN_ID/pending_deployments" --input "$REVIEWED_APPROVAL_JSON"
```

`RUN_ID` must be the actual accepted run/attempt. The reviewed JSON must contain
its verified numeric release environment ID in `environment_ids`, `state` set
to `approved`, and a source/artifact-bound comment. No approval payload with an
invented environment ID is prepared. Match current actor eligibility, exact
source/tag, successful mandatory verification and run-bound lock/artifact
evidence before approval; never approve an old or missing artifact.

The source workflow inspected here places the protected boundary on the whole
publish job. Owner3 is implementing the accepted candidate/native-publish
retention contract. Final review must state which package evidence is available
before approval versus generated after job admission and before credentials.
This packet does not claim a pre-approval candidate artifact currently exists
or replace that design decision. Candidate, actual publish and public archive
hashes remain required at their proper stages.

Preserve original .crate and actual native-publish output even on failure; compare
candidate/actual/public archive checksums under the design. On uncertain upload,
verify the public version/hash before any retry. No reupload, yank, tag movement
or automatic choice of another version. docs.rs indexing is a separate outcome.
A registry permission/token failure does not block ongoing source preparation.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/)
