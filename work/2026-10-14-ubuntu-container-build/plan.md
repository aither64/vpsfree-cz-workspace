# Ubuntu 26.10 container image

## Goal and scope

Add Ubuntu 26.10 image build scripts and its container image repository
configuration to vpsadminos. Follow the current Ubuntu release conventions;
do not change unrelated distributions or deploy/publish production images.

## Affected repositories and ownership

- vpsadminos: dated feature branch/worktree under this initiative.
- Workspace: session coordination records only, on shared master.
- Retained Full-team mode: architect0 (Astra/xhigh) owns design,
  implementer0 (Sol/xhigh, workspace_write) owns application edits,
  reviewer0 (Sol/xhigh, read_only) performs independent final review.
- The user explicitly selected the existing session on 2026-10-16.

## Approach

Inspect nearby Ubuntu release definitions, repository discovery and image tests.
The architect records the design/verification brief in design.md. Create and
register the dedicated vpsadminos worktree after this initial planning commit.
Have the implementer add the minimum release-specific definitions, run quick
checks and commit with mandatory hooks. Inventory and independently review the
whole branch before the targeted long image build test. Publish the feature
branch over SSH and inspect its CI. Integration into master requires separate
explicit user direction.

## Compatibility and deployment

This is an additive image release. Preserve old image identifiers, defaults,
repository formats, APIs, on-disk state and existing image scripts. Check the
Ubuntu builder/debootstrap support and cgroup/kernel requirements against the
new release. No schema changes or migrations are intended. No coordinated
node update or production configuration change is planned. Existing image
builds remain available; rollback removes the new definitions without altering
existing containers. Record any discovered exception before implementation.

## Documentation

Readers are image maintainers and operators. Read image-scripts/README.md and
docs/container-images/{creating,repositories}.md. Keep release-specific details
in the definitions and test evidence in state.md; update project documentation
only when the supported workflow or a lasting constraint changes.

## Verification and acceptance

The new image must resolve as Ubuntu 26.10 with the correct upstream codename
and sources, use existing builder/variant conventions, and have the requested
repository entry. Check shell syntax, Nix syntax/evaluation and project hooks.
Independent review covers final diff, entire commit history, no-migration
provenance and compatibility. After review, run the exact targeted image test
with a fresh catalog-policy Luna/low watcher; stop and investigate unexpected
local kernel builds. Inspect branch CI and record any limitations honestly.
