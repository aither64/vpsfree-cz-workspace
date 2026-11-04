# 2026-11-04-container-image-build-pipeline

## Goal

I'd like to redesign how container image building for vpsAdminOS works. Currently, the images are built in a VM on build.vpsfree.cz (managed by vpsfree-cz-configuration). While this works and failures are logged, it is hard to discover. I'd like to build the images e.g. using github actions, so that it'd be visible and automated. The question is how to make it work. As it is, the images are built one by one, tests are run and if they pass, the images are placed into a local directory, which is the repository. When that is done, the directory is rsynced to images.int.vpsadminos.org, managed by vpsadminos-org-configuration. This is the public repository.

The end result should be that the public repository remains where it is, but the builds will run elsewhere. In theory, we could run them on self-hosted runners. The issue is that we need vpsAdminOS for the build... so if we were to use github-hosted runners, we'd have to run a VM inside them.

Look over the code to see how it works end-to-end and suggest how we could improve it. You can notice that vpsAdminOS integration tests also run image builds and their tests, but their results are dropped... as a consequence, tests of the commit that adds a new container image always fails, because it's not available in the repository yet... I have to do that manually by deploying build.vpsfree.cz and running vpsadminos-build-vpsadminos-repository-vpsadminos.

## Affected repositories

- `vpsadminos`: image builders, repository tools, integration tests and Actions.
- `vpsfree-cz-configuration`: current build VM, timers and publication.
- `vpsadminos-org-configuration`: public repository hosting and ingestion.

## Approach

Investigation and proposal only. Trace exact source revisions through build,
verification, export, indexing, transfer and consumption. The retained architect
owns design synthesis; three implementers own bounded independent evidence
packages. No application edits, builds, deployments or feature integration.

## Decisions

- Keep the public image repository at its existing host and URLs.
- Compare self-hosted vpsAdminOS execution with GitHub-hosted VM execution.
- Explain and remove the proposed dependency on public publication before
  integration tests can validate newly added images.
- Preserve evidence versus inference and name feasibility checks still needed.

## Compatibility and deployment

Assess repository formats/URLs, old consumers, mixed source revisions,
publication ordering, failed/overlapping runs, runner trust and credentials, and
rollback to the current builder. No database/API migration or fleet-wide update
is assumed; verify this in the investigation. Any future deployment and merges
require their separate authorization.

## Documentation

Readers are maintainers deciding the pipeline architecture. Preserve the
investigation and proposed design in this session, with exact repository heads
and source references; do not publish speculative behavior in project docs.

## Testing plan

Read-only source validation for this request. No expensive runtime checks are
needed to suggest a design; clearly mark VM capacity, networking and workflow
experiments that a future implementation must prove. Investigation/planning
records alone do not trigger mandatory final change review.
