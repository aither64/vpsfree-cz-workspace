# vpsAdmin generated client synchronization

## Goal and scope

Check whether the Go, Rust and TypeScript generated clients match current
vpsAdmin API default-branch contracts. Suggest rules that keep client default
branches current without requiring package releases. This turn is investigation
and a proposal; no application or rule changes, releases, merges or deployments.

## Affected repositories

Inspect vpsadmin, haveapi, vpsadmin-go-client and the upstream Rust/TypeScript
client repositories identified from their source documentation. Workspace rules
are a possible future enforcement home, not an authorized implementation now.

## Approach and owners

Architect0 owns investigation, exact default refs, generation provenance and a
concise design/proposal in design.md. Independent evidence packages may go to
saved same-session implementers. The lead owns scope, acceptance and tracking.
Use canonical bare repositories and fresh upstream refs; do not inspect peer
sessions. Distinguish proven contract drift from timestamp/version differences.

## Acceptance and checks

Report a per-language regeneration verdict with concrete source evidence or a
precise verification limit. Explain reproducible generation, where a rule belongs,
how it is checked and how cross-repository integration avoids circular gates.
Prefer existing tooling. Run only bounded read-only checks; any long or uncertain
build needs the verification watcher procedure before launch.

## Compatibility and deployment

Assess public schema versus runtime behavior, source versus production API,
generator versions and mixed API/client versions. Proposal must keep release
metadata and publication separate from generated-source synchronization.
No persisted data, migrations, configuration or deployment changes are planned.

## Documentation

Readers are the user and future maintainers. Keep findings and proposed decisions
in this session; lasting project procedures can be implemented after selection.
