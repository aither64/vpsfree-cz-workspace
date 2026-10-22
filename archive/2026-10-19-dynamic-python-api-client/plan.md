# 2026-10-19-dynamic-python-api-client

## Goal

I'd like to create a haveapi client in python. it should work dynamically against any haveapi-based api. see clients in other languages for inspiration. use idiomatic python. test it. packaging by uv. use only maintained dependencies, like some http client if needed. maintain code standards: does python have code formatter? commit hooks and github workflows to enforce rules. we could provide both sync and async versions. readme and examples can be made against vpsadmin API (it has to work against this API), like other haveapi clients do it. we'll publish the python client in the appropriate registry (pypi?) using trusted publishing if possible.

suggest a solution.

## Affected repositories

- `haveapi`: Python client at `clients/python`, shared tooling and release
  workflow integration; implementation/review corrections in feature worktree.
- `vpsadmin`: read-only reference checkout and disposable actual API integration
  using existing spec helpers/MariaDB; no server source changes planned.
- Workspace: session tracking, design/review and verification evidence only.

## Approach

The user accepted the proposal and explicitly requested implementation. The
architect owns `design.md` and internal contracts; the lead owns scope,
acceptance inspection, tracking and user-facing writing. Retained implementers
own the application packages through tests, commits and review fixes.

Implement a shared protocol core with synchronous and asynchronous HTTPX
transports, dynamic resource/action discovery, Python-native interfaces, uv
packaging, Ruff, typing, pytest, commit hooks, GitHub Actions and PyPI trusted
publishing. Confirm protocol details against existing clients rather than
assuming this API behaves like a generic REST service.

## Decisions

- Implementation authorized by “sounds good, proceed with implementation”.
  Build the client, tooling, tests, docs and trusted-publishing integration;
  actual package publication and default-branch integration are separate gates.
- User added implementer2 and implementer3; preserve saved settings and allocate
  independent packages without overlapping source ownership.
- Preserve the retained Full-team roster and saved member settings.
- Use the same public behavior and protocol implementation for sync and async;
  shared ClientState owns pure continuation security decisions.
- Architect findings: protocol 2.0, authentication-dependent OPTIONS discovery,
  continuation-based token MFA and forced password reset must be represented.
  Do not infer universal pagination ordering from `from_id`/`limit` metadata.
- Proposed package location: `haveapi/clients/python`; distribution name
  `haveapi-client`, import `haveapi_client`. Availability/ownership must be established
  before release; a current PyPI JSON 404 is not proof of registrability.
- Follow HaveAPI's existing shared VERSION and `vX.Y.Z` release tags, subject to
  its repository instructions, rather than introducing independent Python tags.
- Final review corrects legacy-client assumptions against actual server:
  DELETE uses JSON, GET permits only lossless Rack bracket shapes and rejects
  unsupported structures/types before I/O. Exact boundary in `design.md`.

## Compatibility and deployment

The new client must discover arbitrary HaveAPI-based APIs and work with
vpsAdmin. Do not require server, database, protocol, Terraform, generated client
or node changes. Document version/authentication behavior and mixed server
versions in the design. No persistent credential cache by default; no schema
migration or deployment ordering expected. Installing/downgrading an independent
Python package should not alter server state. Actual publishing is a later
operation after package ownership and release configuration are established.

## Documentation

Readers: Python application authors, HaveAPI maintainers and release operators.
Design/review evidence belongs in this session. Lasting client usage, vpsAdmin
sync/async examples, contributor checks and release instructions live under the
client directory, with shared release setup/recovery in repository guidance.

## Testing plan

Use shared sync/async contract tests, mocked HTTP tests,
real HaveAPI server integration, and vpsAdmin compatibility acceptance.
Network-dependent production tests should not be required for ordinary CI;
write operations belong on isolated fixtures/development APIs. Formatter,
lint, typing, tests and package install/build checks should be enforced locally
and in GitHub workflows. Run independent final review on implementation after
commits and quick checks, before long integration tests; routine proposal work
does not trigger that review.

## Approved dependency follow-up — 2026-10-20

Update certifi to 2026.10.19 and Ruff to 0.17.1; refresh nixpkgs using
utils/update-nixpkgs.sh to align native Ruff. Preserve lock revision and other
Python versions, runtime behavior and merged history. Separate generated Nix
and Python dependency commits. Check flake, Python quality/unit, package smoke
and generic integration; independently assess final history and monitor CI.
Publish only; merging and releasing require separate direction.

Dependency follow-up outcome: all four reviewed follow-up commits merged into
HaveAPI/master at a8ea3132e7efe601aaa8965afe648459b3dab5c5 after the user explicitly
directed "merge it after verification". Local checks and all six exact-head
feature/master CI workflows passed. No release was made; session remains open.
