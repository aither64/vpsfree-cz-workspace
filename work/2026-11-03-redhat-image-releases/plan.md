# 2026-11-03-redhat-image-releases

## Goal

update redhat-family image releases in vpsadminos. when verified, you can merge it.

## Affected repositories

- vpsadminos: Red Hat-family image scripts only, including obsolete stable
  Fedora images if absent from live upstream mirrors as required by the skill.

## Approach

1. Architect inventories exact upstream release RPMs and writes design.md.
2. Implementers update independent image directories; serialize Git operations.
3. Commit one logical update per changed image after quick checks and hooks.
4. Independently review the complete branch and history, then run each changed
   image's image-scripts/test integration test through a verification watcher.
5. Publish and fast-forward merge vpsadminos master after successful verification.

## Decisions

- User request authorizes integration into vpsadminos's default master after
  verification: "when verified, you can merge it."
- Retain the existing team and its saved settings; lead coordinates records and
  integration. No production deployment is requested.

## Compatibility and deployment

- Release RPM updates affect newly built images, not running containers or host
  state. Preserve each family's repository URL layout and shared release values.
- No schema, protocol, API or coordinated node update is expected. Confirm this
  against the actual diff. Recovery is reverting the relevant image commit.

## Documentation

- Readers: image maintainers and operators verifying this update. Keep exact
  release discovery, branch, review and test evidence in this session's records.
- Existing skill owns reusable release-update instructions; no product prose or
  separate repository documentation is expected for version-only edits.

## Testing plan

- Quick: shell syntax and relevant repository hooks, exact upstream RPM listing
  comparison, release-line consistency and final diff inspection.
- Final independent review precedes longer tests. Run the documented test for
  every changed image; investigate any failures and stop unexpected kernel builds
  unless the runner has not yet published the expected derivation.
- Record exact source revisions, commands, results and CI status before merge.
