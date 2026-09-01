# 2026-09-01-security-advisory-lists

## Goal

Keep security advisories compact on the vpsAdmin and vpsf-status index pages,
provide a direct route to the complete advisory list, and make vpsAdmin drafts
easy for administrators to find among published advisories.

## Affected repositories

- `vpsadmin`: limit the index-page list to five published advisories, add a
  full-list link, and sort drafts and published advisories together by their
  effective date.
- `vpsf-status`: limit the index-page list to three advisories, add a full-list
  link, and remove the misleading partial advisory list from the public JSON
  response.
- `vpsfree-kb-contracts`: pin and check the exact vpsAdmin feature revision for
  the WebUI documentation contract.
- `vpsfree-cz-configuration`: update the `vpsadmin` and `vpsf-status` channels
  to the tested feature revisions.

## Approach

### vpsAdmin

- Preserve the existing 30-day filter and five-item limit on the WebUI index.
- Add an in-section `View all` link to the dedicated advisory page.
- Keep draft visibility restricted to administrators through the existing API
  authorization scope.
- Order the dedicated list by an effective date: `published_at` for published
  reports and stable `created_at` for drafts. Apply the same rule in both
  newest-first and oldest-first orders with deterministic tie breakers.
- Apply the same effective-date tuple to `from_id` cursor boundaries so
  pagination cannot skip or repeat advisories whose IDs and dates differ.
- Cover the link and mixed draft/published ordering in API and browser tests.

### vpsf-status

- Change the fetched and rendered recent-advisory limit from ten to three.
- Defensively truncate an overlong API response so the index never renders
  more than three advisories.
- Add a localized link to the full vpsAdmin advisory list:
  `View all security advisories` / `Zobrazit všechna bezpečnostní upozornění`.
- Remove `security_advisories` and its nested types from the public JSON
  response. Keep the runtime advisory model used by the HTML page.
- Change integration coverage to validate advisory rendering through HTML
  instead of the removed JSON field.

### Documentation contract and configuration

- Pin the exact committed and pushed vpsAdmin feature revision in every
  contract location, update the lock file through Nix, and run the contract
  check. The current contract has no advisory bindings, so no KB page or
  screenshot candidate is expected unless the check reveals one.
- Push both application branches before pinning their revisions.
- Update configuration inputs only through `confctl inputs channel set
  --commit`, preserving its generated commit messages.
- Do not deploy systems or publish KB content as part of this initiative.

## Compatibility and deployment

- The vpsAdmin API response schema and database schema are unchanged. Old and
  new WebUI/API versions can run together; ordering changes only affect list
  presentation.
- No persisted state or on-disk format changes are introduced.
- Removing `security_advisories` from vpsf-status JSON is an intentional public
  API break. The previous field exposed only a bounded recent subset and was
  not a reliable complete advisory feed. HTML remains the supported compact
  presentation and links to the authoritative vpsAdmin list.
- The vpsf-status runtime state remains compatible during rolling updates;
  only response serialization and the recent fetch limit change.
- Configuration pins can be applied independently. Updating vpsAdmin first or
  vpsf-status first is safe because the applications communicate through the
  unchanged vpsAdmin advisory API.
- Rollback consists of reverting each application/configuration pin. No data
  written by the new versions requires conversion before rollback.
- No coordinated vpsAdminOS node update is required.

## Testing plan

- vpsAdmin API resource specs for administrator mixed-state ordering and
  public draft exclusion.
- vpsAdmin WebUI localization checks, PHPUnit suite as relevant, and the
  `webui#security-advisories` browser test.
- vpsf-status unit and route tests, localization generation/health checks,
  `go test ./...`, and the `status-page` integration test.
- vpsfree-kb-contracts `nix develop -c bin/check` against the exact vpsAdmin
  feature revision.
- Configuration evaluation/build checks for the affected vpsAdmin services
  and `cz.vpsfree/machines/prg/apu` as supported by local repository tooling.
- Mandatory fresh-agent change review after commits and quick checks, before
  the long browser/integration/build tests.
- Push feature branches and monitor their GitHub Actions workflows. Investigate
  any failure before accepting a rerun.
