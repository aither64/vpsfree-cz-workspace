# HaveAPI 0.32.2 downstream release

## Goal and authorization

Consume HaveAPI 0.32.2 after registry publication, update and merge vpsAdmin,
regenerate Go, Rust and TypeScript clients, and merge/minor-release/publish each
client with code changes. Finally update and merge the configuration vpsadmin
channel. User request in this conversation explicitly authorizes these merges
and client publications. No machine deployment is requested. Do not wait for
long CI. Leave this session open.

## Affected repositories

- vpsadmin (master), consuming published HaveAPI 0.32.2.
- vpsadmin-go-client (master), vpsadmin-rust-client (main),
  vpsadmin-ts-client (main), exact repository identities to confirm in design.
- vpsfree-cz-configuration (master), vpsadmin channel only.
- HaveAPI upstream publication belongs to the cooperating release session.

## Approach and owners

Architect0 owns investigation and design.md, including generation inputs,
release conventions and independent execution packages. Implementers own code,
generation, quick checks, commits and fixes. Lead owns coordination, independent
review assignments, approval records and acceptance. Preserve saved settings.

Order: upstream publication evidence; vpsAdmin dependency update and verification;
client regeneration against the updated API; conditional client releases;
configuration channel update after upstream integration/publications. Prepare
independent packages only once generation contracts are settled.

## Compatibility and recovery

Assess generated public contracts and runtime pairs. The publishing lead reports
no DB/protocol migration or coordinated machine update in HaveAPI 0.32.2.
Preserve existing supported runtime pairs. Release tags/publications are durable;
verify exact artifacts and versions before publishing. Revert dependency/channel
pins for source rollback; no production activation is in scope.

## Documentation and checks

Readers are release operators and future maintainers. Keep rollout revisions,
registry evidence and decisions in session records; update owning project docs
only if workflow or supported behavior needs explanation. Follow repository Nix
environments/hooks. Commit intended deliverables and pass quick checks before
independent final history/migration review; mechanical content exemptions do not
remove history review. Do not await long CI. Record exact final heads and remote
integration/publication evidence before completion.

## Cross-session communication

User explicitly directed coordination with 2026-11-02-backport-and-publish-release
in the initial task message. Runtime grant c61cca2368b7b2cd5e144bc85b118e6c
permits deliberate lead messages only. Never access peer files or worktrees.
