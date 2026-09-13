# File links: deployed validation

The portal on aitherdev now opens absolute workspace file links in a read-only
source viewer. Previously copied absolute website paths redirect to the same
viewer. The referenced line is scrolled into view and highlighted; line numbers
update the link and support normal browser back, reload and new tabs.

Active repository files show current worktree content, including uncommitted
edits. Archived sessions use the exact recorded final commit. Curated artifacts
use the existing session artifact catalog. Links refer to the current source, so
a later edit can change what appears at the same line number.

## Live examples

Both original URLs returned 404 before deployment. They now redirect with HTTP
302, and the file API returns HTTP 200 with text identical to the current local
file. Firefox confirmed syntax highlighting and the selected line:

- [Proxy module, line 10](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/files/2026-08-18-vpsadmin-password-reset?path=cluster%2Fcz.vpsfree%2Fcontainers%2Fprg%2Fproxy%2Fmodule.nix&repository=f7e4ad2503a24e7ccdccd7895eec0012#L10)
- [Frontend module, line 95](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/files/2026-08-18-vpsadmin-password-reset?path=cluster%2Fcz.vpsfree%2Fvpsadmin%2Fcommon%2Ffrontend.nix&repository=f7e4ad2503a24e7ccdccd7895eec0012#L95)

## Validation

- General, architecture, risk and scope reviews completed using sol/xhigh.
  All findings addressed; dispositions are in review-reconciliation.md.
- Focused Go and mounted Node browser contracts passed.
- Generic `nix flake check --print-build-logs` passed, including host VM checks.
- Full workspace package build passed, including its Go and Ruby suites.
- Firefox fixture passed at 1440x1000 and 390x844: line reveal, syntax coloring,
  no horizontal page overflow, navigation, copy link, invalid/missing line
  notices, rapid hash changes, literal HTML source, curated artifacts and
  archived content after removing the worktree. A retained page also loaded
  successfully with the pre-feature editor bundle used during rollback.
- Authenticated live checks passed for both original examples, session page,
  health and declared artifact reads. Unauthenticated reads return 401;
  artifact traversal is rejected with 400.
- [Generic CI](https://github.com/aither64/dev-workspace/actions/runs/34772498526)
  passed at f41d4220dd1d5ade08ba3bb28f964e9570a11ed9.
- [Organization CI](https://github.com/vpsfreecz/dev-workspace/actions/runs/34772521732)
  passed its flake and development-cluster checks at
  9f3142248f6e40d602115aa0fad66701595ef232.

## Deployment

The user package and the host module use the same final generic revision,
f41d4220dd1d5ade08ba3bb28f964e9570a11ed9. The deployment contract checker,
aitherdev configuration build, dry activation and activation passed.

- Workspace package: /nix/store/gzhi8hrjb7j2pbzlxs0bcv4abqkg2r7q-dev-workspace-0.2.0
- User profile: 37
- Confctl generation: 2026-09-13--19-47-18
- Active system: /nix/store/6zn634xr6m6rn0vvxiv4fvrzzrk3mk7l-nixos-system-aitherdev-26.05.20260911.21a67dc

Both deployment health checks passed. Router, portal, nginx and Codex are active;
Codex retained PID 1090021 through the update. No state migration or local kernel
build was needed. All four feature branches are merged into their remote master branches and
retained. Worktrees are removed, and the development session remains open for
follow-up. See integration.md for the subsequent merge checks and workflow links.
