# Schema input preparation

Both the TypeScript full-fixture candidate and the public Go/Rust snapshot are
accepted for SDK-owner input copying. This record describes input preparation,
not a release or compatibility certification. All original source worktrees and
the reused HaveAPI component lock remained clean/unchanged.

## Full fixture for TypeScript

- Canonical repository: `git@github.com:vpsfreecz/vpsadmin.git`, fetched over SSH.
- Source/default: `bcfa95eb136c50d25024f53a6b1af557d1173d56` (`origin/master`).
- Clean registered source worktree: `worktrees/2026-10-30-haveapi-client-releases/vpsadmin`.
- Branch: `2026-10-30-haveapi-client-releases`; no application or dependency edits.
- Accepted candidate: `schema-candidates/typescript-fixture-a/`.
- Independent repeat: `schema-candidates/typescript-fixture-b/`.
- API 7.0, protocol 2.0, mount `/`, profile `vpsadmin-full-fixture`, English.
- Synthetic source `https://schema.invalid/v7.0/`; no deployed API/DB contacted.
- All six plugins: monitoring, newslog, outage_reports, payments, requests, webui.
- Inventory: 151 application resources, 519 actions, 8720 parameters.
- Scopes SHA256: `2e575a597445cf4b4277596c5f7f990b04f75a56dca2a0a3ce80d5c7a2abe177`.

| Frozen file | SHA256 | Bytes |
| --- | --- | ---: |
| `schema.json` | `476f0086726a443a6ef8ad9a9d499bd3feff6eb6c5b0b652dcc999192d638794` | 3649167 |
| `provenance.json` | `7b477c6156c82ab483d686e1e0305ea2a40b82e0e24d50dc7653228b19556927` | 21207 |
| `tooling.Gemfile.lock` | `b1d32a5ff5fb7e922c56ac6efadfa765ac4b2043cae90a54f0a71124b9b90019` | 18403 |

Both exports produced byte-identical copies of all three files; there were no
volatile provenance differences. All seven fixture/config input hashes match
the selected checkout. Plugin source/migration inventories match the existing
TypeScript inputs. The new canonical schema is byte-identical to the existing
TypeScript schema at `60a1b5d1b911c610bd993d93ae2b28d1932a0ccc`. Provenance changes
are the vpsAdmin source revision and resolved csv, io-console, mime-types-data,
rack, rotp and rubocop versions/hashes, plus the dependency-lock hash. These
metadata changes do not establish meaningful generated changes or justify a
client release. Four literal HTTP URLs were checked without userinfo, query or
fragment; exporter sanitization specs cover credentials and protected defaults.

Tooling remained the documented exporter override: HaveAPI and haveapi-client
0.30.2, Ruby 3.4.9, Bundler 4.0.23, MariaDB 11.4.12. The deployed API Gemfile
was unchanged. Exact gem identities and input graphs are in provenance and lock.

## Commands and checks

From the selected clean source root, one monitored batch ran:

```sh
nix develop .#vpsadmin
tools/export-api-schema --prepare
BUNDLE_GEMFILE="$PWD/api/Gemfile" BUNDLE_PATH="$PWD/api/.gems" \
  NIX_ENFORCE_PURITY=0 bundle install
BUNDLE_GEMFILE="$PWD/api/Gemfile" BUNDLE_PATH="$PWD/api/.gems" \
  bundle exec rspec --options /dev/null \
  tools/api-schema-export/safety_spec.rb tools/api-schema-export/snapshot_spec.rb
tools/export-api-schema --api-version 7.0 --output /absolute/candidate/typescript-fixture-a
tools/export-api-schema --api-version 7.0 --output /absolute/candidate/typescript-fixture-b
```

Actual commands are retained in ignored `schema-candidates/prepare-export.sh`.
The fresh policy watcher used Luna/low, danger-full-access and approval never,
matching catalog `495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`.
Result: exit 0, approximately 3m35s; 14 examples, zero failures; both independent
database exports passed; no running operation remains. See
`schema-candidates/logs/prepare-export.log`, `prepare-export.exit-status`, and
`prepare-export-result.txt`. Parent verified artifact equality, source/input
hashes, profile/plugin inventory and clean worktree after completion.

The first worktree add created the checkout but its post-checkout Overcommit
hook refused a stale configuration signature. Inspection confirmed clean HEAD
and the expected hook configuration. Retrying the ordinary add adopted the
existing clean checkout and registered it; no hook bypass or signing occurred.

SDK owners copy accepted inputs; this package does not alter their repositories.
No production changes, migrations, tags, publication or integration occurred.
The public snapshot binds the frozen HaveAPI 0.32 candidate and must be
rechecked against its final released source identity before SDK publication.

## Public snapshot for Go and Rust

- Frozen HaveAPI source: `f0465630595b4fd120561337b3d1d7fa96cbe221`, clean before
  and after capture. No fetch, source change, bundle installation or resolution.
- Existing source: `worktrees/2026-10-30-haveapi-client-releases/haveapi`.
- Accepted snapshot: `schema-candidates/public-api7/api-7.0.json`.
- One unauthenticated OPTIONS acquisition of `https://api.vpsfree.cz/v7.0/`,
  2026-10-30 11:20:08–11:20:12 UTC. No API mutation or raw response retained.
- Format 1, API 7.0, protocol 2.0, mount `/`, profile `public-live-api-7.0`.
- Inventory: 151 application resources/519 actions, plus one authentication
  resource/five actions; 152 resources/524 actions in total. Application scopes
  hash is the same `2e575a597445cf4b4277596c5f7f990b04f75a56dca2a0a3ce80d5c7a2abe177`.
- Snapshot SHA256: `70f89335e15263fd7177f29a00fab04b5ff1923c6922dfd318b07c3ae922fb8d`,
  3649376 bytes. It matches the previously recorded Rust snapshot exactly.
- Resolved Go component lock: `public-api7/generator.Gemfile.lock`, SHA256
  `bb4b5eab29bef661b4b3b5cd64a26852eee795105d0a1d872a37623ffb70450d`.
- Shared schema identity: `haveapi-client` 0.32.0, source SHA256
  `e12f7989a028bb529f4a78a510af8e09411bbeb5eec9c782feb1fbf20862533c`.
- Ruby 3.4.11 at
  `/nix/store/jnjll1yxfq02bdcw5pjf9gl86wh8gfhq-ruby-3.4.11/bin/ruby`,
  Bundler 4.0.23. `public-api7/tooling.json` records actual loaded gem paths and
  versions. `public-api7/provenance.json` additionally binds cached gem hashes,
  Gemfile/VERSION/lock identities, source commit/tree/full file graph, acquisition
  time, sanitization and inventory. `haveapi-source-tree.txt` retains the graph.

The capture uses the exact source CLI and its prepared component bundle:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop
BUNDLE_GEMFILE="$PWD/clients/go/Gemfile" BUNDLE_FROZEN=true BUNDLE_IGNORE_CONFIG=1 \
  bundle exec ruby clients/go/bin/haveapi-go-client fetch \
  https://api.vpsfree.cz/v7.0/ --api-version 7.0 --profile public-live-api-7.0 \
  --output /absolute/candidate/public-api7/api-7.0.json
```

Tools-only mode skips the Nix shell's dependency installation; frozen Bundler
prohibits lock resolution. The batch checked original clean HEAD and exact
component-lock equality before/after. A fresh Luna/low utility with verified
full-access/approval-never launch ran the batch: exit 0, approximately four
seconds, no running operation. Logs/results: `logs/public-capture-retry1.log`
and `logs/public-capture-retry1-result.txt` under `schema-candidates/`. The empty
command log contains no protected-default removal diagnostics. The parent
checked profile, version, nested inventory and four literal HTTP URLs without
userinfo/query/fragment, then loaded the saved bytes through the exact source
`HaveAPI::Schema::Snapshot.load` and confirmed its canonical byte round trip.

The first candidate-only launcher had a nested shell quoting error and exited
before network access. Its effects were inspected; corrected separate helpers
passed `bash -n` before the fresh watcher executed the actual capture. The first
failure and both final results remain in the ignored logs. No repeated API
capture occurred.

Go and Rust owners must consume these same accepted snapshot bytes, retaining
the read-only tooling lock/identity evidence. The full-fixture and public
descriptions differ despite matching action inventory; retain each established
profile. No generated-code equivalence or release decision follows from the
unchanged schema alone. Rebind to the final released HaveAPI commit/identities
before SDK publication; if generator/shared sources change, owners rerun the
affected generation/checks under the revised brief.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-haveapi-client-releases/
