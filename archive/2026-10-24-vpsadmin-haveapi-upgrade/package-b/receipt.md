# Package B: Go and Rust documentation profiles

Current follow-up: the Rust installation profile was consolidated to crates.io
on 2026-10-25. See [B2 receipt](b2-receipt.md) for current exact head, scope,
checks and range comparison. The original sections below retain evidence at
21872fe6 and its former Git source; they are not current installation guidance.

Status: source and focused checks complete; committed as
`21872fe6ad373e52f66f193ee432f4885376e5a5`.
Documentation performance acceptance is blocked by released HaveAPI 0.30.1's
per-request copying cost. No push, independent final review, long integration,
SDK compilation, deployment or integration has been performed by this package.

## Scope and source

- Session identity verified with `dev-session current`, exact environment and
  trusted binding `2026-10-24-vpsadmin-haveapi-upgrade` in workspace
  `/home/aither/workspace/ai/vpsfree.cz`.
- vpsAdmin base: `b82eeca50cd4dd7bd76728685c7de8aad66e7ba5`.
- Package A preserved at `ff44d95ebe9794341185ba5c78250e130dde80fd`.
- Five B files: `api/lib/vpsadmin/api.rb`,
  `api/spec/lib/vpsadmin/api/documentation_clients_spec.rb`, `docs/README.md`,
  `docs/api-client-examples.md`, `tests/suite/services-up.nix`.
- Inline profiles target API 7.0 only. Go uses
  `github.com/vpsfreecz/vpsadmin-go-client/client` without an invented SDK
  version. Rust uses `vpsadmin-client` from HTTPS Git at the full immutable
  revision `ff876abe17e3301da62c1b6afbda055ec89db9d2`, for async and blocking
  examples. Generator gems are exact released HaveAPI 0.30.1 from package A.
- No SDK repository edits, snapshot override, new renderer, application cache,
  server route, authentication or data change. No database migrations, schema
  changes or migration consumption boundaries. No deployment occurred.

## SDK parity evidence

Fresh read-only SSH checks confirmed Go master
`1d9240f3d27b5831baf3694baab5fe06294875d8` and Rust default main
`ff876abe17e3301da62c1b6afbda055ec89db9d2`. Exact immutable source exports are
retained under `reference/{go,rust}` for offline comparison only.

`reference/rust/schema/api-7.0.json` is the SDK's sanitized unauthenticated
2026-10-19 API 7.0 capture: 3,649,376 bytes, SHA256
`70f89335e15263fd7177f29a00fab04b5ff1923c6922dfd318b07c3ae922fb8d`.
Its original provenance records HaveAPI generator 0.30.0 and 524 actions;
`v0.30.0..v0.30.1` does not change Rust IR/naming or copied runtime.

The current server has 23 core resource files absent from the Go SDK. This is a
generic SDK coverage limitation, not proof that a displayed sample is invalid.
All 17 actually rendered action sample identities were audited, across
administrator/English, member/Czech and anonymous/English pages. The unchanged
upstream renderers produced 174 Go/Rust panel results:

- 168 complete programs: 52 Go, 58 Rust async and 58 Rust blocking.
- Six explicit limitations: Go token authentication and Go `Vps.Index`, once
  per role. The token panel reports a mismatched authentication contract;
  `Vps.Index` reports a response field unavailable in the model. No code is
  fabricated for these panels. Rust emits code for every captured panel.
- `check_symbols.py` found zero missing generated action members, input setters,
  accessed output fields, path placeholders or authentication methods against
  the exact external source revisions. Complete emitted source was also
  inspected directly for package/import identity, origin/version usage and
  representative setter types. This static inspection is not compilation or
  runtime proof.

Final capture and audit: `rendered-instrumented/{results.json,symbol-audit.json}`,
complete programs beside them, and `symbol-audit.log`. The application has no
instrumentation: `audit_rendered_spec.rb` is session-only observation around
unchanged return values.

## Focused checks and performance diagnosis

The first focused run was started inline as a presumed quick spec. It proved
mounting, visibility and emitted public programs, but multiple full pages made
it unexpectedly slow. A fresh policy Luna/low watcher observed the existing
owned process, which was interrupted once using SIGINT. RSpec finished its
current example and ordinary cleanup: 3 examples, 0 failures in 5m20s, exit 1
because interrupted. No owned Ruby/MariaDB process remained. See
`focused-first.log`. This incomplete run is not the passing receipt.

The final focused check reduced six overlapping full GETs to the three required
role/locale requests and bounded assertions to avoid huge HTML failure diffs.
A fresh catalog-pinned Luna/low watcher launched `run-profile-checks.sh`, using
`nix develop .#api` and the ready bundle. Retained policy catalog SHA256:
`840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa`;
full-access native watcher configuration was verified. Result: exit 0,
2 examples, 0 failures, 5m08s, seed 64746. See `instrumented.log` and
`instrumented.exit`.

Both generator profiles mount, nonconfigured API versions have none, public
initialization/auth/action tabs use real generated source and correct package
hints, and member fields/admin samples remain filtered after an administrator
request. Member Czech locale survives the added tabs without translation errors.
Only RSpec's description metadata was then changed to `VpsAdmin::API` to satisfy
DescribeClass lint; test bodies and application source were unchanged.

Per-request timings, after mount/setup and before HTML unescaping/matchers:

| Role/locale | GET wall | Process CPU | Context derivations | Context time | Renderer calls | Renderer time |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| admin/en | 102.376s | 102.275s | 639 | 88.757s | 294 | 16.075s |
| member/cs | 49.716s | 49.668s | 484 | 42.536s | 224 | 6.041s |
| anonymous/en | 139.036s | 138.846s | 639 | 122.885s | 294 | 20.749s |

Context and renderer timings overlap and must not be summed. CGI unescaping
cost 0.003–0.005s. Repeated deep copies of the authorized description dominate;
this is request cost, not only startup model construction. Saved SDK snapshots
do not remove it. The architect's decision B1 and lead direction retain exact
0.30.1 with candid evidence; no speculative local patch, filtering or cache is
authorized. This package cannot claim overall documentation usability acceptance.

Ruby syntax and final scoped RuboCop pass (`lint.log`, `lint-final.log`), and
`git diff --check` passes. New spec path matches existing platform-config
`spec/lib/**/*_spec.rb` in full/core topic matrices; no selector edits required.
The modified `services-up` test is a prepared packaged-API integration assertion,
not executed evidence. All long integrations and external SDK compilation wait
for committed-deliverable independent final review.

## Documentation and rollback

`docs/api-client-examples.md`, linked from `docs/README.md`, records profile
identity, startup failure behavior, compatibility audit expectations, current
slow-page contract and coupled configuration/gem rollback. No wire or persistent
state changes; mixed API workers may show different tabs. The lead directly applied the
writing skill to the complete final prose, including the added performance
paragraph, and accepted it without text edits before commit.

## Hook invocation diagnosis

A manual preflight mistakenly used `bundle exec overcommit --run`; that selects
all repository files and carries root Bundler execution state into the API i18n
subprocess. It failed to materialize root lint dependencies from the API gem
path, despite the ready API bundle passing its own checks. The owned preflight
was cancelled with SIGINT, ended with exit 65, and both Overcommit/RuboCop
children were confirmed absent. Staged B paths remained intact with no unstaged
changes. No preflight result was accepted and no hooks were bypassed. The normal
commit is run through the root Nix shell as plain `git commit -F`, matching A's
successful environment and the standard hook entrypoint. See `hooks.log` for
the failed preflight and `commit.log` for normal-hook evidence.

## Final complete branch inventory

The complete base-to-head series is one dependency stream plus one focused
profile adaptation commit. No obsolete intermediate pin, alternate renderer,
compatibility workaround, generated SDK or migration remains:

1. `ff44d95ebe9794341185ba5c78250e130dde80fd` — Package A released dependencies,
   generated metadata/browser distributions and required native environment.
2. `21872fe6ad373e52f66f193ee432f4885376e5a5` — Package B profile configuration, focused spec, developer docs
   and packaged documentation assertions.

The complete history, final diff and affected paths are retained in
`final-history.txt`, `final.diff`, `final-files.txt`. There are no database
migrations in either commit, therefore none merged/released/deployed/consumed by
this branch. Exact HaveAPI pin stream is consolidated in A only; B adds no
dependency updates. A's reviewed provenance is linked in `../package-a/receipt.md`.

Normal commit exit 0; all declared pre-commit hooks passed (Nixfmt,
MigrationSpecs, VpsadminWebuiI18n, RuboCop, VpsadminApiI18n). Commit-msg hooks
passed with one advisory >72-column warning; every line is within the required
80-column limit. `commit.log` retains the exact result. The worktree/index are
clean and no owned operation remains running. No push/merge/deployment.

Ready for the lead's independent final committed-deliverable review, with
performance acceptance explicitly blocked and long integration/compile proof
still pending review. Do not call this overall ready for production use.

Count correction: the first lead report incorrectly summed the per-role table
as 194 panels/188 programs. The authoritative `results.json` and
`symbol-audit.json` consistently record **174 panels/168 programs/6 limitations**
(52 Go + 58 Rust async + 58 Rust blocking). All 17 action sample identities are
still present. This arithmetic correction does not change code, symbol findings,
role coverage, timings or test outcomes.
