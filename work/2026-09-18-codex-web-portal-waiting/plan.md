# codex-web licensing, portal waiting state, and Ruby test structure

## Goal

Relicense codex-web to Apache-2.0, replace its internal-facing README with
user documentation while preserving the technical material in `docs/`, show a
compact waiting-state indicator on the dev-workspace Codex menu, split the two
large Ruby test files into feature-focused suites, and deploy the result on
aitherdev without waiting for CI.

## Affected repositories

- `codex-web`: license, README, and new user and API documentation.
- `dev-workspace`: waiting indicator, browser contracts, Ruby test layout, and
  the codex-web dependency pin.
- `vpsfree-dev-workspace`: pin the reviewed generic runtime.
- workspace: pin the reviewed extension and retain the initiative records.
- `vpsfree-cz-configuration`: pin the matching generic runtime for aitherdev.

## Approach and decisions

- Use Apache License 2.0's unmodified text for codex-web. Preserve existing
  project copyright attribution and third-party notices.
- Make the README a practical entry point: purpose, capabilities, trusted
  deployment model, standalone quick start, embedding overview, links to the
  detailed API guides, development checks, and license. Move, rather than
  remove, the existing technical contracts into topic-specific Markdown pages.
- Show an amber overlay dot on the existing Codex rail icon when the portal's
  current synchronized state proves an interactive session is idle or has a
  blocking request. Do not add server state, an endpoint, or polling. Do not
  show a dot for nonblocking requests, missing activity data, connection
  failures, archived sessions, or read-only views.
- Keep the existing Ruby entry points as small loaders. Move fixtures and test
  doubles into support modules and test cases into feature-specific classes in
  `test/dev_session/` and `test/workspace_host/`; retain every scenario and
  direct `ruby test/{dev_session,workspace_host}_test.rb` compatibility.
- Use `gpt-5.6-terra` for implementation and mandatory review as directed by
  the user. The long-check monitoring helper remains its separately prescribed
  watcher role. Do not wait for CI.

## Compatibility and deployment

The changes do not alter Codex App Server requests, HTTP/browser APIs,
persisted session data, manifests, lifecycle journals, or database schemas.
New portal JavaScript degrades to no indicator until existing snapshots arrive.
Older package generations ignore the styling and continue to read all prior
state. Roll back the user profile with `workspace-host rollback`; no data
migration or coordinated node update is needed.

The dependency order is codex-web, generic dev-workspace, vpsFree extension,
workspace package, then the aitherdev host-module input. The configuration
feature branch is deployed but remains unmerged without a separate integration
direction.

## Documentation and verification

Codex-web owns its reusable user and API documentation. This plan and state
own model selection, exact dependency revisions, review evidence, deployment
steps, and rollback results. The test reorganization needs no member-facing
documentation, but its compatibility entry points will be documented in the
test support layout.

Capture the pre-refactor Ruby run/assertion counts; after the move, require
matching counts from the old entry commands and run every focused group. Add
browser coverage for waiting, blocking prompts, nonblocking prompts, resumed
work, unavailable state, and compact Repositories navigation. Run quick checks
before Terra mandatory review, then long package/build/deployment checks using
the prescribed monitor. Verify the deployed portal and service health; do not
await GitHub Actions.
