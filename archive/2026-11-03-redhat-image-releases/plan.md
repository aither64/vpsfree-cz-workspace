# 2026-11-03-redhat-image-releases

## Goal

update redhat-family image releases in vpsadminos. when verified, you can merge it.

## Affected repositories

- vpsadminos: four Red Hat-family release RPM updates plus the approved
  source-identity plumbing and null-safe channel fixes needed for verification.

## Approach

1. Architect inventories exact upstream release RPMs and writes design.md.
2. Implementers update independent image directories; serialize Git operations.
3. Commit one logical update per changed image after quick checks and hooks.
4. Independently review the complete branch and history, then run each changed
   image's image-scripts/test integration test through a verification watcher.
5. Publish and fast-forward merge vpsadminos staging after successful verification.

## Decisions

- User request authorizes integration into vpsadminos's default staging after
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

## Approved verification fix

User approved the proposed durable correction and continuation after diagnosis.
Preserve snapshot-bound revision and dirty metadata through source resolution and
test framework; reuse existing flake version rules when constructing test OS.
Honor unknown revision in channel generation. Avoid live external Git metadata,
fabricated identity, new registries or parallel review/verification systems.

Assess exported framework consumers, existing override semantics and legacy
callers. Preserve source-selection rules including supported untracked files;
record exact design in design.md before framework edits. Meaningful regression
checks cover clean/dirty ordinary and linked checkouts, capture stability,
Git-free sources, and known/unknown channel revision. No production deployment,
schema migration, or running-node update is part of this change. Keep the four
release commits separate and add focused framework/channel logical commits.
The original four-line review remains evidence for that range; the expanded
completed deliverable requires updated independent final review before long
integration tests. Longer checks use a fresh operation utility, at most one at a
time. Repository documentation for source provenance may now be useful and belongs
with the owning framework, reconciled before review.

## Delivered outcome

Completed at reviewed/tested source54b4313404cea35b58ebb9df951ae75e27c44971,
integrated into remote staging by ordinary SSH fast-forward under short released
ownership. Later default2951a632 contains final54; it is not claimed tested here.
All4 requested changed image cases, actual post-push109core tests/323scripts,
RSpec3297 and RuboCop passed. Nine unchanged lifecycle fixture failures and
provider job-status/observer-receipt limits are retained in post-merge-ci-result.md;
no in-scope delivery or verification action remains. Source provenance explanation
was added to owning docs/os/test-framework-integration.md and reviewed with code.
No migrations, runtime API/protocol changes, production deployment, KB publication
or coordinated node update. Source refs/session remain open; no archival requested.
