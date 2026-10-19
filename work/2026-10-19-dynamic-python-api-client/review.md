# Independent final review: original deliverable

Review completed 2026-10-20 by retained reviewer0, gpt-6.1-sol/xhigh/read-only,
thread `01a155f8-f45b-72c3-97c3-a6149b4b489d`, no overrides/fallback/nesting.
Lead records this faithful summary of the full report returned through team
messaging; the reviewer did not write files. Full report remains in conversation.

Reviewed base `c58704a08451a231fdf6c6123437133422af46dc`, head
`05e6236c7a9570d51f4330183141ff3ac290e9b1`, tree
`28e19ad0a6b4e5f4615ac63422ce7167555edbd6`. All seven commits and final 60-file
diff inspected. Risk HIGH; general, architecture, scope and risk lanes complete.
Result: **changes required**. No long integration/package/CI tests run.

## Blocking

**R1: preserve final query pair order.** `_transport/__init__.py:86-90`
(93c7616) passes `params=spec.query` into HTTPX, which groups duplicate keys.
Core row-major pairs `rows[][a]=1,rows[][b]=2,rows[][a]=3,rows[][b]=4` become
`a=1,a=3,b=2,b=4` bracket pairs. Installed HTTPX reproduction and Rack 3.2.7
parse show three differently associated rows instead of two. Both facades and
nested Custom object arrays are affected. Preserve validated ordered pairs in
final encoded URL without injection; verify actual HTTPX raw bytes and Rack
results, not just RequestSpec. This does not resolve sparse/empty R4 shapes.

**R2: DELETE requires JSON input/metadata.** `_protocol/request.py:187-202`
(0a9f48b) incorrectly groups DELETE with GET. Current and released v0.29.12
server.rb:721-739 classify non-GET/HEAD/OPTIONS as body methods and ignore DELETE
query action input. Example impact, not executed: vpsAdmin VPS administrator
delete(lazy=False) would lose the option and use default soft deletion. PHP
client agrees with server; legacy Ruby query behavior is an existing client bug.
Use JSON body and real HTTP regression with declared DELETE fields+metadata,
paired facade wire tests, reconcile docs/design.

**R3: shared continuation security policy.** `client.py:150-174` and
`async_client.py:156-180` (93c7616) duplicate described-token requirement, private
field stripping, nonce creation/currentness, override rejection and private token
merge. A future auth fix can land in only one facade. Extract minimal shared
preparation/submission helpers in existing ClientState, retaining sync/await I/O
wrappers. Test shared invalid-next-step/currentness/override policy and retain
paired public tests. No generalized execution framework is requested.

## Important

**R4: define a lossless GET boundary.** `_protocol/request.py:96-108,196-202`
(0a9f48b). Even ordered sparse rows `[{a:1},{b:2}]` parse in Rack as one merged
row; explicit Custom empty list/hash produces no pairs and becomes omission.
This can broaden filters or turn validated required input into missing data.
Represent faithfully or reject locally, preserve expressive JSON paths, document
GET limitations. No invented numeric-index semantics or silent coercion. Inspect
Rack outcomes and rejection before I/O. Architect's proposed whitelist is a
remediation requiring affected public-contract/risk review after commit.

**R5: preserve known no-show resource context.** `response.py:165-168` (4347d1b)
returns `executor.resource(path)` without source bindings despite its comment.
A custom-only job.run invoked with job_id=7 returns object.resource lacking its
ID, so .run() fails locally. Retain safe ordinary-object originating bindings;
do not infer association parents or copy unrelated source context into
`inherit_context=False` associations. Test named/positional bindings and keep
incomplete associations fail-closed.

## Advisory and accepted conclusions

- Reconcile design's unknown/custom-type passthrough wording with literal Custom
  support in input.py; do not invent speculative unknown-type semantics.
- No additional must-fix release/package finding or credential-forwarding bypass
  demonstrated. Application payloads/errors remain potentially sensitive.
- Registry ownership/environment setup/OIDC publishing are unperformed; this is
  source/test review, not end-to-end release proof.
- Shared core parsing/coercion, immutable binding, destination/envelope handling,
  paging/operation/concurrency ownership is sensible except R3 duplication.
- Scope proportional: dynamic client, explicit cursors, finite operations,
  advertised resumable auth, vpsAdmin tests/examples, no runtime vpsAdmin names,
  persistent cache/browser flows/generated types/node features.
- Risk controls: credentials added after mount/origin validation, no redirects
  or injected auth/cookies, auth mutation gate, stale proxies, temporary tokens
  not normal identities. No server format/schema/rollout requirement introduced.
- Explicit association fetches, finite pages/cursor progression, operation
  failure/deadline/cancel semantics coherent except R5. Sync deadline limitation
  documented accurately.
- Packaging self-contained, licensed/typed, maintained HTTPX/AnyIO, locked tools,
  native Ruff parity, Overcommit, typing/CI. Smoke tests prepared not run.
- Release preserves protected official OIDC, retained wheel/sdist/hash identity,
  build-once/recovery, PHP preflight before registry writes and only missing
  original Python uploads. No inferred merge/publication approval.
- Guarded vpsAdmin bridge's DB/source/version preflight, private manifests,
  owned loopback/process cleanup and limited external side-effect stubs are
  appropriate. Actual integration and exact-head CI remain required. API-only
  testing does not prove node/VPS lifecycle.

## Whole-history and migrations

The seven-commit split is dependency ordered and reviewable: package/tooling/docs/
harness, core, responses/paging/operations, facade/auth, vpsAdmin bridge, examples/
public fixture, release/PyPI. Initial component bundle has concrete shared
development/distribution rationale, no unrelated feature bundling.

No obsolete unmerged approach, transitional behavior, unused compatibility shim,
scaffolding/export/fixup remains in the original reviewed series. Reviewer
independently compared backup and final: sole tree delta is approved three-line
Ruff first-party setting. Packaging followup consolidated; no repeated pin or
generated-update streams remain. pyproject/uv.lock introduced once, root
flake.lock unchanged. No supported boundary requires intermediate unpublished
heads. Fold requested fixes into owning unmerged commits before readiness.

**NO MIGRATIONS:** complete range has no migrations/schema transitions/new server
persisted state. No feature version merged/released/deployed/externally consumed,
no pre-existing Python consumers/pins. Released HaveAPI 0.29.12 is a test baseline.

## Verification side effects and disposition

Reviewer reproduced with existing Python venv (PYTHONDONTWRITEBYTECODE=1) and
installed Rack parser, no live API. Entering server-ruby shell unexpectedly
started ignored dependency setup; reviewer immediately terminated its owned
process, reported it, launched no server/integration, source/index clean and
exact head/tree unchanged. No lifecycle operations.

Fix R1/R2/R3 before long integration; fix or explicitly decide R4/R5. Lead chooses
to fix all five and reconcile advisory wording. Exact narrow fixes can be
directly inspected/tested; changed encoding boundary and materially new auth
design require affected-lane rereview by same reviewer after commits/quick pass.
Original-head review is complete but does not establish readiness.
