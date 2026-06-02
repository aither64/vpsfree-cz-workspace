# Security Advisories

## Goal

Implement security advisories as vpsAdmin core functionality, focused on
kernel and shared-host vulnerabilities where vpsFree.cz is responsible for
assessment, mitigation, and patching. Users must be able to see which
published advisories affect their VPSes and what status applies.

## Affected Repositories

- `vpsadmin`: core API models/resources, database migrations, transaction
  chains, web UI pages, index-page recent advisories, tests, and the optional
  outage-report cross-link.
- `vpsadmin-go-client`: regenerate the Go client after the vpsAdmin API gains
  advisory resources.
- `vpsf-status`: show recent security advisories in the public status service
  and expose them through additive JSON fields.
- `vpsfree-irc-bot`: announce new security advisories and advisory updates,
  similar to outage reports.
- `vpsfree-mail-templates`: add localized production mail templates for
  advisory announcements and updates.
- `vpsfree-cz-configuration`: deploy updated inputs and enable/configure the
  status and IRC integrations, including internal DNS for dev-cluster
  auxiliary services.
- `dev-clusters/vpsadmin`: local workspace dev-cluster wiring for vpsf-status
  and Adminer.

## Product Shape

- Add a first-class `Security advisory` section to vpsAdmin core, not a plugin.
- Each advisory has one or more CVE identifiers and an optional well-known
  vulnerability name.
- Published advisory summaries are public, so status.vpsfree.cz and the IRC bot
  can report them without tenant-specific data.
- A logged-in user can see the advisory status of their own VPSes. Admins can
  see all node, user, and VPS impact data.
- Emails are supported but disabled by default for both initial publication and
  later updates.
- Advisories can receive updates in the same operational style as outage
  reports.
- Outage reports can link to security advisories when mitigation or patching
  requires a maintenance, restart, reset, or other outage.

## vpsAdmin Data Model

All advisory ownership lives in vpsAdmin core. The outage-report link is the
only part that belongs to the existing `outage_reports` plugin, because the
plugin owns the `outages` table.

- `SecurityAdvisory`
  - `state`: `draft`, `published`, `retracted`.
  - `name`: optional well-known vulnerability name.
  - `published_at`, `retracted_at`, normal timestamps.
  - `affected_user_count`, `affected_vps_count`, and
    `affected_node_count` are derived from snapshot rows.
- `SecurityAdvisoryCve`
  - one row per CVE, with validation for `CVE-YYYY-NNNN...`.
  - unique per advisory.
  - exposed as a top-level API resource, not as a subresource and not as a
    flattened comma-separated field on advisory API output.
  - web UI forms still accept/edit a comma-separated CVE text field as an
    operator convenience, then reconcile rows through the CVE API.
- `SecurityAdvisoryTranslation`
  - localized summary/description/response text, following existing vpsAdmin
    translation patterns.
  - `summary` is the public headline shown in lists, status output, IRC
    announcements, and emails.
- `SecurityAdvisoryNodeStatus`
  - belongs to an advisory and a node.
  - `state`: `unknown`, `not_affected`, `vulnerable`, `mitigated`.
  - `vulnerable_until`: nullable timestamp. Set when vulnerability exposure is
    known to have ended on that node.
  - `mitigated_since`: nullable timestamp. Set when the node is known to be
    mitigated.
  - `note`: optional operator-facing/public note, depending on visibility.
- `SecurityAdvisoryVps`
  - current-impact snapshot rows tying a published advisory to VPSes that
    should see it.
  - stores user, VPS, environment, location, node, node status,
    `vulnerable_until`, and `mitigated_since` at publish/rebuild time.
- `SecurityAdvisoryUser`
  - aggregate rows used for filtering, permissions, and email recipients.
- `SecurityAdvisoryUpdate`
  - update records with translated body, optional state changes, and optional
    mail send.
- `OutageSecurityAdvisory`
  - join table inside `outage_reports`, linking outages to core advisories.

The node `state` is intentionally separate from the nullable timestamps. This
avoids ambiguity: `not_affected` with nil timestamps means the node was never
vulnerable, while `vulnerable` with nil timestamps means it is still vulnerable
or not yet known to be patched.

Publishing is blocked until every active vpsAdmin node has a status and no
active node remains `unknown` or `vulnerable`. A `mitigated` node must have both
`vulnerable_until` and `mitigated_since`.

## API And Behavior

- Public users can list/show published and retracted advisories. Draft
  advisories are admin-only.
- Public advisory responses include summary fields, state, timestamps, public
  update text, and public node statuses for published/retracted advisories.
  CVEs are fetched independently through `security_advisory_cve#index/show`.
- Tenant-specific VPS/user impact rows are visible only to admins and the
  owning user.
- Admin resources allow creating advisories, assigning CVEs, setting node
  statuses, publishing, retracting, posting updates, rebuilding
  affected VPS/user rows, and optionally sending emails.
- Useful filters should mirror outage-report ergonomics where possible:
  `recent_since`, `state`, `cve`, `affected`, `user`, `vps`, and `node`.
- v1 remains operator-controlled. It does not infer vulnerable nodes from
  kernel version strings automatically; operators enter node statuses and
  rebuild affected rows explicitly.

## UI

- Add a security-advisory index and detail page in the vpsAdmin web UI.
- Add an admin form for advisory metadata, CVEs, translations, node statuses,
  publication, updates, and email sending.
- Show recent security advisories on the vpsAdmin index page near recent outage
  reports, but as a separate section.
- On a VPS detail page or advisory detail page, let users see whether the VPS
  is affected, mitigated, not affected, or still vulnerable.
- Outage detail pages show linked security advisories; advisory detail pages
  show linked outage reports.
- Outage-report links only reveal published/retracted advisories to non-admins.
  Draft advisory links remain hidden until the advisory is published.

## Integrations

- `vpsadmin-go-client`
  - regenerate from the updated vpsAdmin API; do not hand-edit generated code.
- `vpsf-status`
  - fetch recent advisories through the generated client.
  - fetch CVE rows separately through `security_advisory_cve#index`.
  - render recent advisories as their own status section.
  - render outage reports and the no-issues banner above security advisories.
  - do not show affected-node counts in the public advisory list.
  - expose advisory CVEs as an array of objects in JSON. The advisory feature
    is unreleased, so the previous draft flattened-CVE JSON shape does not
    need compatibility.
  - preserve stale advisory data but mark advisory status failed when the
    advisory fetch fails.
- `vpsfree-irc-bot`
  - add a `security_advisories` module/config block parallel to
    `outage_reports`.
  - announce new published advisories and advisory updates.
  - fetch CVE rows independently and omit affected-node counts from messages.
  - link to the vpsAdmin advisory detail page.
- `vpsfree-mail-templates`
  - add templates for initial advisory announcement and advisory update.
  - include CVEs, advisory name, current VPS impact summary, and canonical link.
- `vpsfree-cz-configuration`
  - update input pins after code lands and generated clients are released.
  - configure status and IRC bot advisory support.
  - add `adminer.aitherdev.int.vpsfree.cz` to the internal dev-cluster DNS
    zone.
  - ensure mail templates are deployed before any production email sends.
- `dev-clusters/vpsadmin`
  - include vpsf-status in the services VM when the matching worktree exists.
  - expose Adminer at `https://adminer.aitherdev.int.vpsfree.cz/` with
    dev-cluster basic auth and documented vpsAdmin database login details.

## Compatibility And Deployment

- vpsAdmin changes are additive database migrations and new API resources.
  Security advisories are unreleased, so changing the draft advisory CVE API
  from flattened fields to `SecurityAdvisoryCve` rows has no production
  compatibility impact.
- Existing outage reports continue to work. The cross-link table lives in the
  outage plugin and only adds optional associations.
- Existing released API clients continue to work because no released resources
  are renamed or removed.
- Existing outage JSON fields in `vpsf-status` are preserved. Security-advisory
  JSON is still unreleased and uses the new CVE object-array shape.
- `vpsfree-irc-bot` config is additive and disabled unless configured.
- No vpsAdminOS/node coordinated rollout is required for v1 because node status
  is manually recorded in vpsAdmin.
- Safe deployment order:
  1. deploy vpsAdmin migrations/code and mail template definitions;
  2. regenerate and release `vpsadmin-go-client`;
  3. update `vpsf-status` to depend on the released generated client and deploy
     status code;
  4. deploy `vpsfree-irc-bot` code;
  5. deploy production mail templates;
  6. enable integrations and update pins in `vpsfree-cz-configuration`;
  7. publish the first advisory only after templates and UI are deployed.
- Rollback should be safe as long as no old service is required to understand
  advisory data. New tables can remain unused if older code is restored.

## Testing Plan

- vpsAdmin API/model specs for advisory CRUD, state visibility, CVE validation,
  node status semantics, affected user/VPS rebuilds, and mail-default behavior.
- vpsAdmin web UI tests or focused integration checks for index, detail, admin
  forms, and user-visible affected VPS status.
- Update vpsAdmin API spec generation/CI selection files for new resources and
  web UI paths.
- `vpsadmin-go-client`: regenerate with `haveapi-go-client`, review generated
  diff, run `go test ./...`.
- `vpsf-status`: run `go fmt ./...` and `go test ./...`; verify additive JSON
  output and rendered template behavior.
- `vpsfree-irc-bot`: add specs for advisory announcements/updates and run the
  repository test task.
- `vpsfree-mail-templates`: run template tests/install task against a local or
  staging vpsAdmin API as documented by the repository.
- `vpsfree-cz-configuration`: validate changed inputs/configuration with the
  appropriate `confctl` build/dry-run workflow.
