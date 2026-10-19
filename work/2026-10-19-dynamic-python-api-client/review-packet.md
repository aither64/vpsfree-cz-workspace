# Final review packet

Complete intended deliverable committed, final quick checks pass, no long
integration tests launched. This is a final complete-branch review request.

## Outcome and ownership

Implement a generic dynamic Python HaveAPI protocol 2 client, synchronous and
asynchronous, with vpsAdmin interoperability, uv packaging, enforced code checks,
documentation/examples and PyPI trusted-publishing integration. Python 3.11+.
No server protocol/application changes or default-branch integration authorized.

Owner: HaveAPI `clients/python`. No existing Python consumer/pin to migrate;
vpsAdmin is the representative external API consumer target. Existing clients
must retain behavior and shared release compatibility.

References: [plan.md](plan.md), [design.md](design.md),
[verification-plan.md](verification-plan.md), [state.md](state.md).

## Repositories and final inventory

- HaveAPI worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-dynamic-python-api-client/haveapi`.
- Base: `c58704a08451a231fdf6c6123437133422af46dc`.
- Head: `05e6236c7a9570d51f4330183141ff3ac290e9b1`.
- Tree: `28e19ad0a6b4e5f4615ac63422ce7167555edbd6`.
- Base matches freshly fetched origin/master; no upstream rebase needed.
- Full seven-commit series:
  1. `509fc4d2a7d5d4ccb41f111a82c13a013197248e`: package/tooling/docs/generic harness.
  2. `0a9f48b77d411d7c44d41e873fcb91e5c8b49671`: immutable protocol core/tests.
  3. `4347d1b051561ed7488bdc7632c9502c21ae1f38`: response/paging/operations/tests.
  4. `93c7616c13215f372a50485760ca839a0fbac04b`: sync/async facade/auth/tests.
  5. `b052c7d788b8ff39531a23cb9aff5edc99280564`: guarded actual vpsAdmin bridge.
  6. `a5f20a635195cbfc05fc2a7dd51bed482c7393d4`: examples/public fixture.
  7. `05e6236c7a9570d51f4330183141ff3ac290e9b1`: shared release/PyPI integration.
- Final diff: 60 files, +9583/-17. Lead inspected complete series/stat and
  confirmed clean worktree/index, diff --check clean. Reviewer must inspect full
  diff directly: `git diff c58704a..05e6236`.
- vpsAdmin reference only, no source changes:
  `fb2f51222503a45f2e5a42af505f719e44279ed0`.
- No migrations/schema changes; none merged/released/deployed/externally consumed.
  This new Python package has no released or externally consumed feature version.
- Packaging followup 53d1756 folded into original a83b7f9 as 509fc4d; no obsolete
  scaffolding/export/fixup commits retained. Runtime dependency and uv.lock
  creation form one final package stream. Root enforcement extends that stream
  for new release helpers in release commit; no repeated pin-update streams or
  changed root Nix input/flake.lock. Message-only temporary amendments discarded
  from final series; no supported consumer boundary requires intermediate heads.
- Packaging source, checks, docs and generic harness are bundled as the one new
  component's development/distribution contract; core, runtime features, facade,
  actual-API integration, examples/fixture and shared release remain separately
  reviewable. Assess proportionality and split independently.
- Safe unpublished
  rebase retained backup `2026-10-19-dynamic-python-api-client-before-consolidation`
  at 841ee6b/tree 2353ea6f024e45bb87678c81aa7fe8de6c50fb83. Historical hook
  configurations are inspected/signed and hooks remain enabled. Consolidation
  exposed Ruff import classification depending on which modules exist in an
  intermediate commit; lead approved explicit isort `known-first-party` for
  `haveapi_client`. Final-vs-backup diff verified solely that three-line config
  addition. Six unaffected streams stable-patch-ID equivalent to preconsolidation.

## Review selection and risk

Risk: **high**, due to authentication/credential handling, dynamic untrusted
discovery, public protocol contracts and registry publication workflow changes.
All four lanes apply: general, architecture/repetition, scope/proportionality,
risk/compatibility. Read the mandatory-change-review skill and every selected
reference. Retained reviewer0 verified ready/read-only/independent with saved
model `gpt-6.1-sol`, effort `xhigh`, thread
`01a155f8-f45b-72c3-97c3-a6149b4b489d`. No overrides/fallback.

## Acceptance and boundaries

- Shared protocol core and wire behavior; thin synchronous/asynchronous HTTPX
  execution. No hidden property/network I/O or `asyncio.run` library wrapper.
- Dynamic exact resource/action lookup plus ergonomic shortcuts, all declared
  input/output layouts, nested paths/base mounts and immutable request binding.
- Correct error envelopes/metadata/coercion, omission/null distinction,
  continuation-based token auth and authorized rediscovery/stale-proxy behavior.
- Basic/existing token/bearer, explicit renewal/revocation. Browser OAuth,
  WebAuthn interaction and automatic refresh are non-goals; no persistent cache.
- Explicit pagination strategies and bounded operation waiting/cancel semantics.
- uv/uv_build self-contained distributions with shared version, typed stable
  interfaces and honest dynamic typing limits; Ruff/mypy/tests/hooks/CI.
- Extend shared protected build-once release with PyPI OIDC and hash recovery;
  no registry configuration change or actual publication claimed.
- Current-source generic server integration and real vpsAdmin/released HaveAPI
  integration are longer checks after final review. Their absence before review
  is intentional; inspect test quality and launch readiness.
- No node VM/lifecycle operation coverage claimed by API-only compatibility.
- No server schema/state migration/deployment order or coordinated node upgrade.

## Evidence, documentation and dependencies

Prepared documentation paths: `clients/python/{README,CONTRIBUTING}.md`, root
README client link, `doc/agent-instructions/{development,releases}.md`.
Lead applied direct writing pass, corrected false vpsAdmin resource nesting and
recorded sync wait deadline limits. Reconcile final text with actual integration
evidence before final handoff.

Final-head quick evidence:

- `nix develop .#client-python -c clients/python/utils/check.sh`: locked sync,
  Ruff 36 files formatting/lint including root release Python, strict mypy 18
  sources, 187 unit tests pass in 1.14s.
- Top Nix shell `make release-check release-test`: shared 0.29.0 metadata, 34
  RSpec examples pass in 1.18s and six offline Python artifact tests in 0.026s.
- RuboCop seven owned Ruby files clean; shim/bridge Ruby syntax and shell syntax
  clean. All commits passed normal hooks; signatures enabled after rebase.
- Generic integration ten cases collected only; no server fixture executed.
  vpsAdmin five scenarios collected only, DB preflight rejection checked.
  Actual generic/vpsAdmin HTTP suites and package smoke remain post-review.

Runtime deps: HTTPX and directly used AnyIO. Tooling: Ruff 0.16.10 matches native
locked Nixpkgs; uv_build minimum 0.13.0 allows pinned uv native backend on NixOS,
with generic PEP 517 frontends permitted newer compatible backend. Both choices
documented in contributor guidance. Development/runtime versions do not promise
all package-index combinations; final locks and CI matrix are review inputs.

Published runtime ranges are HTTPX >=0.28.1,<1 and AnyIO >=4.15,<5; inspect
pyproject/uv.lock for complete dev pins and Python 3.11–3.15 CI matrix. Actual
PyPI ownership/protected environment setup not performed. Release uses retained
wheel/sdist and exact hashes, no rebuild after approval. Public vpsAdmin subset
fixture provenance records source URL, capture
time, pruning rule and original/derived hashes; contains no authenticated data.

Implementation ownership: impl0 core/response/paging/operations, impl1
package/tooling/generic harness/release, impl2 facade/auth/vpsAdmin bridge,
impl3 bounded examples/public description fixture. Lead applies user-facing
writing before docs commit and accepts evidence; architect owns design.
