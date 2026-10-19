# 2026-10-19-dynamic-python-api-client

## Goal

I'd like to create a haveapi client in python. it should work dynamically against any haveapi-based api. see clients in other languages for inspiration. use idiomatic python. test it. packaging by uv. use only maintained dependencies, like some http client if needed. maintain code standards: does python have code formatter? commit hooks and github workflows to enforce rules. we could provide both sync and async versions. readme and examples can be made against vpsadmin API (it has to work against this API), like other haveapi clients do it. we'll publish the python client in the appropriate registry (pypi?) using trusted publishing if possible.

suggest a solution.

## Affected repositories

- `haveapi`: proposed home for a Python client beside the existing language
  clients, subject to architect inspection. Read-only investigation this turn.
- `vpsadmin`: protocol and example compatibility reference only; no server
  changes planned.
- Workspace: session tracking and proposed design only.

## Approach

Prepare a grounded solution proposal before application implementation. The
architect owns existing-client investigation and `design.md`; the lead owns
scope, acceptance inspection, tracking and the user-facing recommendation.
Implementation, release and integration are later phases.

Evaluate a shared protocol core with synchronous and asynchronous HTTPX
transports, dynamic resource/action discovery, Python-native interfaces, uv
packaging, Ruff, typing, pytest, commit hooks, GitHub Actions and PyPI trusted
publishing. Confirm protocol details against existing clients rather than
assuming this API behaves like a generic REST service.

## Decisions

- Current requested deliverable is a solution suggestion; no application edits
  or publication in this turn.
- Preserve the retained Full-team roster and saved member settings.
- Use the same public behavior and protocol implementation for sync and async.
  Final interfaces and packaging choices remain proposals until investigation.
- Architect findings: protocol 2.0, authentication-dependent OPTIONS discovery,
  continuation-based token MFA and forced password reset must be represented.
  Do not infer universal pagination ordering from `from_id`/`limit` metadata.
- Proposed package location: `haveapi/clients/python`; distribution name
  `haveapi-client`, import `haveapi`. Availability/ownership must be established
  before release; a current PyPI JSON 404 is not proof of registrability.
- Follow HaveAPI's existing shared VERSION and `vX.Y.Z` release tags, subject to
  its repository instructions, rather than introducing independent Python tags.

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
Current proposal belongs in this session's `design.md`. Later lasting client
usage, vpsAdmin sync/async examples, contributor checks and release instructions
belong under the owning client's directory and its README.

## Testing plan

The proposal must identify shared sync/async contract tests, mocked HTTP tests,
real HaveAPI server integration, and vpsAdmin compatibility acceptance.
Network-dependent production tests should not be required for ordinary CI;
write operations belong on isolated fixtures/development APIs. Formatter,
lint, typing, tests and package install/build checks should be enforced locally
and in GitHub workflows. Run independent final review on implementation after
commits and quick checks, before long integration tests; routine proposal work
does not trigger that review.
