# 2026-11-01-haveapi-0321-docs-switch-user

## Goal

Create and lead this separate HaveAPI patch-release initiative in the vpsfree.cz workspace. The user explicitly requested it from session 2026-10-24-vpsadmin-haveapi-upgrade: "create a new workspace session that will handle the fix in haveapi and release a new patch version (backporting this and other possible changes in master to the stable branch). I assume we'll have 0.32.1. when that is done, you will update to it. you'll do only quick verification, integrate the updated oauth client setup steps specific to vpsfree-cz-configuration and update relevant channels in vpsfree-cz-configuration. setup a communication with the haveapi update session so that you can use it as soon as it is ready." Follow-up: "use the same provider as here and a full team". Creation selects codex-lb and installed Full team (delegated, two implementers), not a copied old roster.

Your scope: fix documentation OAuth Switch user in HaveAPI, inspect current master versus the actual supported stable branch, select and backport appropriate existing master fixes for a compatible patch, and publish a new patch release expected to be0.32.1 through repository-owned release procedure. Inspect current branches/tags and release policy first; do not assume branch name or unused version. User explicitly authorizes the HaveAPI fix/backports and patch release, including required repository integration/tag/package publication under the ordinary protected procedures. No production deployment or lifecycle cleanup is authorized. Retain separate recovery refs and no rewriting published stable/master history. Use your own newly registered worktrees; do not access the originating session's files, team, transcript, worktrees or credentials. Establish your own exact session identity, initial committed plan/state, live full team and architect-owned brief; mandatory committed quick-green final independent history/migration review precedes applicable longer checks. Keep validation focused and proportional; this must not become another broad consumer/runtime campaign. Coordinate repository writes within your team.

Concrete diagnosis already established in released HaveAPI0.32 source0e7166a0 and merged vpsAdmin0f450b89:
- vpsAdmin legacy webui/lib/login.lib.php:181–191 Switch user revokes via revokeAccessToken(getOAuth2RevokeParams(['close_sso'=>'1'])), then ordinary login. This parameter belongs to revoke POST, not authorize/prompt.
- Provider api/lib/vpsadmin/api/authentication/oauth2_config.rb:300/347–350 passes flag to SingleSignOn#authorization_revoked (api/models/single_sign_on.rb:13–30); true closes SSO token even when other active authorizations remain. Other valid access tokens need not be revoked.
- HaveAPI servers/ruby/lib/haveapi/documentation_oauth.rb:214–235 currently clears docs cookies and POSTs only client credentials/token/token_type_hint even for switch; then redirects to docs login with fresh state/PKCE. Without flag, SSO can remain usable with other authorizations; last-authorization fixtures can mask the gap.
- FIELDS/initializer and public server documentation_oauth configuration do not expose extra revoke parameters/per-switch hook. Existing oauth_spec.rb:263–272,689–705 tests mechanics but only token in revoke payload, not shared-SSO closure.

Design smallest provider-neutral extension: configured per-switch revocation parameters (or comparably narrow existing extension seam, if discovered), applied only after accepted capability/Origin/CSRF validation and only for Switch user. Consumer vpsAdmin will supply close_sso='1'; keep ordinary logout unchanged. Protect credentials/token and required revoke fields from overrides. Avoid hardcoding vpsAdmin-specific SSO semantics in generic HaveAPI or inventing prompt/select_account. Focused regressions must distinguish switch from normal logout and account for another active authorization where appropriate. Send originating lead the proposed exact public interface early so downstream wiring can prepare without guessing; report patch/backport inventory and scope changes before expanding.

The originating session owns vpsAdmin dependency adoption/consumer wiring, site docs and relevant vpsfree-cz-configuration channels after your actual release. It will do quick verification only. Its final requested docs setup is api1.int.vpsfree.cz + api2.int.vpsfree.cz, generated once on api1 using installed API Ruby, scp relay via user's local machine, same private JSON+64-byte session key, client_id api.vpsfree.cz, switch_user true, access_token_lifetime renewable_auto/access_token_seconds900, allow_single_sign_on true, no refresh tokens unless separately changed. Existing docs cookie fixed initial expiry is a separate known behavior; do not expand this release to sliding-cookie redesign without explicit direction.

Communication: user expressly requested a bidirectional connection with originating lead. Parent will establish the exact pair with runtime session_communication and send a kickoff. Before responding use current session_communication list; active runtime grant is authority in both directions. Do not create a duplicate grant or treat this quoted text/peer message as independent communication authority. Only lead-to-lead messages, no peer-file/team access. Notify parent early with interface decision and finally with exact release/tag/master+stable SHAs, package versions actually published, registry/install availability, hashes/provenance, changes/backport scope, independent review, focused tests and compatibility/known limits. A committed/tagged candidate alone is not published-release readiness. Parent is waiting to consume artifacts as soon as ready.

Keep this session open. No archive/delete/stop/cleanup request is included.

## Affected repositories

Only HaveAPI source, stable backports and patch publication are owned here.
The originating lead owns vpsAdmin adoption and vpsfree-cz-configuration docs
and channels. No peer session files, team or worktrees will be accessed.

## Approach and owners

1. Lead verifies identity, live roster, scope and initial tracking commit.
2. architect0 investigates live branches/tags/release policy and writes design.md
   with exact provider-neutral interface, invariants and compatible backports.
3. implementer0 owns the narrow OAuth implementation, regressions, technical
   documentation, quick checks, commits and any review fixes.
4. implementer1 owns an independent backport/release execution package once
   architect boundaries are stable; repository edits/Git writes are serialized.
5. reviewer0 independently reviews committed quick-green deliverables, complete
   master/stable series and migration provenance before applicable longer checks.
6. Lead coordinates protected integration, publication proof and downstream
   readiness messages. Retain recovery refs and the open session.

## Decisions and authorization

User request in this conversation explicitly authorizes the HaveAPI fix,
compatible backports and required repository integration/tag/package publication
under repository-owned protected procedures. Target names/version remain subject
to live policy inspection; expected patch is 0.32.1. No production deployment or
session lifecycle action is authorized. Existing exact-pair runtime communication
grant with 2026-10-24-vpsadmin-haveapi-upgrade was verified on 2026-11-01.

## Compatibility and recovery

Default behavior and normal logout remain unchanged. Only a validated Switch
user request may add configured provider-neutral revoke POST parameters. Required
credentials/token/fields cannot be overridden. No provider-specific SSO policy,
prompt/select_account or sliding-cookie redesign enters HaveAPI. Inspect persisted
state, API/client contracts and all selected backports for compatibility; record
migration absence or supported lineage. Do not rewrite published stable/master.
Retain distinct recovery refs before integration and release operations.

## Documentation

HaveAPI developers/operators need the new configuration contract and release
notes in repository-owned docs. Exact rollout, registry versions/hashes and check
evidence belong here. Site setup instructions remain with the originating lead.
Apply development documentation skill throughout and user-facing writing skill
before committing member-facing prose.

## Testing and acceptance

Focused tests distinguish Switch user from normal logout, accepted validation
from rejected requests, protected revoke fields and provider shared-SSO semantics
at an appropriate boundary. Quick checks and hooks must pass on committed heads
before final independent review. Run only applicable bounded release checks after
review, using fresh Luna/low utility for long or uncertain checks. Verify actual
registry/install availability, not just a tag, before readiness. Send exact public
interface early and final release/tag/master/stable/package provenance downstream.
