# vpsAdmin HaveAPI 0.30.1 upgrade

## Goal and scope

Update every HaveAPI server/client dependency in vpsadmin to 0.30.1. Configure
API documentation examples for the Go SDK and the Git-published Rust vpsAdmin
SDK (the Rust crate is not published on crates.io).
Carry forward the vpsadmin-webui work from 2026-10-19-haveapi-async-client into
this session's own branch, replacing the custom client with the published async
TypeScript npm client. Update KB manuals:vps:api with Python, Rust and
TypeScript clients, preserving supported existing clients.

## Affected repositories

- vpsadmin: Ruby dependencies, lockfiles, generated Nix dependency metadata,
  documentation configuration, and targeted verification.
- vpsadmin-webui: authorized takeover provenance and published-client migration;
  architect confirms the repository's registration and local PR requirements.
- Knowledge base: local bilingual candidates and guarded review manifests;
  assess vpsfree-kb-contracts ownership before adding repository scope.
- haveapi and generated-client repositories: read-only release/API references
  unless investigation establishes a separately approved need to edit them.

## Approach and owners

The retained Full-team architect (architect0) owns investigation and design.md,
including package boundaries and acceptance checks before implementation.
The lead assigns complete packages to ready retained implementers, serializes
Git operations and overlapping edits, and owns session records and final
member-facing writing. reviewer0 performs independent final review after all
intended substantive changes are committed and quick checks pass.

## Compatibility and deployment

Inventory server/client protocol assumptions, authentication, asynchronous
completion, error handling and mixed-version behavior. Preserve persisted
state and supported API behavior; no database migration is intended. Record
any migration discovered and its deployment/consumption provenance. Carry prior
WebUI source without changing the old session. Prefer incremental deployment;
record ordering and rollback constraints in design and owning project docs.
No production deployment or default-branch integration is currently requested.

## Documentation

Developers need dependency and client adapter rationale in owning project docs;
members need accurate install/import links and supported examples in the API KB
article. Lead applies the user-facing-writing skill after facts settle. Prepare
complete local candidates and exact staged review before requesting production
publication approval. Temporary rollout and review evidence stays here.

## Acceptance and verification

- All vpsadmin HaveAPI runtime pins and resolved metadata use 0.30.1.
- Go/Rust documentation examples use correct published client profiles.
- WebUI uses the published async npm client and preserves login, session,
  errors, action completion, list/pagination and existing UI behavior.
- KB names Python, Rust and TypeScript clients with verified package links and
  usable examples, retaining language mapping and markup.
- Repository hooks and targeted quick checks pass; commit complete deliverables,
  inventory complete history/diff/migrations, then independent final review.
- Run longer applicable checks only after review with a fresh Luna/low watcher;
  publish feature branches and repository-required PRs without merging.
- Production KB promotion requires user approval of the exact staged bundle.

## Decisions

The user's takeover direction authorizes carrying forward the prior WebUI work.
The user additionally permits reusing existing vpsadmin-webui PRs; prefer
matching PRs and record exact source/head ownership and history provenance.
Do not alter unrelated old-session repositories or lifecycle/records.
Do not archive or stop this session as part of completing the task.
