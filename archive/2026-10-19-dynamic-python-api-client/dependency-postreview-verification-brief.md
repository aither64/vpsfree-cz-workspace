# Dependency refresh post-review verification

Prepared by implementer1; **not executed by the owner**. The lead accepted the
retained review of exact head `18331877660ed0f736a25b29914756da89df0df9`
(general, architecture and risk: no findings; three-commit history accepted,
no migrations) and will authorize a fresh policy utility to execute this batch.
The original [owner receipt](dependency-refresh-owner.md) is unchanged.

Command:

```sh
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-dynamic-python-api-client/run-dependency-postreview.py
```

Working directory:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-dynamic-python-api-client/haveapi`.
Script SHA256:
`587dce502956284e37fad814632ac199d565f1045460a695f0f573c3e2accc0d`.
Only Python syntax compilation was performed during preparation.

## Command sequence

Every command runs through `nix develop <selector> --command bash -euo pipefail
-c <command>` in the repository root, using the existing declared shell and
ordinary gem home. Existing component locks remain frozen. Child processes
inherit `PYTHONDONTWRITEBYTECODE=1`.

| Check/log prefix | Shell selector | Command |
| --- | --- | --- |
| `01-doc` | `.` | `make doc` |
| `02-server-rspec` | `.#server-ruby` | `cd servers/ruby; ruby --version; bundle exec rspec` |
| `03-ruby-client-rspec` | `.#client-ruby` | `cd clients/ruby; ruby --version; bundle exec rspec` |
| `04-go-client-rspec` | `.#client-go` | `cd clients/go; ruby --version; bundle exec rspec` |
| `05-python-generic-rack` | `.#client-python` | `cd clients/python; uv run --locked pytest tests/integration/test_ruby_server.py tests/integration/test_rack_wire.py` |
| `06-python-package` | `.#client-python` | `cd clients/python; uv run --locked python utils/package_smoke.py` |
| `07-release-check` | `.` | `make release-check` |
| `08-release-test` | `.` | `make release-test` |

Sources: HaveAPI AGENTS/development instructions, Makefile, `utils/copydoc.sh`,
component RSpec entrypoints, generic harness and `utils/package_smoke.py`.
`make release-check` validates metadata; `make release-test` runs the existing
Ruby release specs and Python artifact tests. These targets do not publish.

No repeated flake or quick checks, vpsAdmin rerun, VM, release build, version
change, tag, registry action or source edit is included.

## Guards, evidence and ownership

Before each check, outside every child Nix shell, the runner verifies:

- session identity and held claim `342cd062-0205-45c7-b636-20d958b8fa75`;
- exact head above and tree `320fc303f5ae2af73bc34139a918cccf1ea4b254`;
- clean tracked/index/untracked status and signature verification enabled;
- unchanged root, server, Ruby-client and Go-client Gemfile.lock hashes.

Ruby/Bundler environment variables are cleared only for the outer workspace CLI
and orchestration environment, preventing the packaged workspace Ruby from
loading project native gems. The child development shells set their ordinary
declared environments; there is no native tool override.

Evidence directory: `verification/dependency-refresh/postreview/`. Each row has
its own `<prefix>.log` and atomic `<prefix>.status.json`; overall state is
`batch.status.json`. Status records bind command, cwd, head/tree, claim, runner
PID, child PID, exit code and elapsed time. The first nonzero check stops the
batch. Existing evidence is refused rather than overwritten. No automatic retry
or fallback exists.

The fresh retained-policy Luna/low utility owns the command, native tool handle
and observation. It reports raw pass/failure, revision, elapsed time, evidence
paths, bounded failure excerpt, and any remaining owned processes. It does not
edit source, diagnose, retry, push, approve or publish. Unexpected kernel builds
must stop under workspace policy; silence alone supplies no timeout. Native
harness teardown remains responsible for its disposable servers; the utility
also verifies no owned child remains before handing back.

## Generated artifacts

- `make doc` copies shared Markdown/PNG and renders `json-schema.html` into
  ignored `servers/ruby/doc/` paths.
- The existing server packaging spec builds ignored
  `servers/ruby/pkg/haveapi-0.29.0.gem` and extracts test copies into temporary
  directories.
- Python package smoke uses `haveapi-python-package-*` temporary directories
  for wheel/sdist, extracted standalone source and installation environments;
  its native context manager removes them.
- Release specs use their existing disposable `haveapi-release-spec-*` and
  artifact fixtures. Bytecode generation is disabled so the artifact validator
  does not leave a new root `utils/release/__pycache__`.
- Existing declared gem setup and test caches remain ignored. No cleanup of old
  payloads, recovery refs/stash, source or unrelated files is included.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-dynamic-python-api-client/>
