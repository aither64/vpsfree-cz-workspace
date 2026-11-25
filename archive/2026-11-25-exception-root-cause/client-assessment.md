# Current-source generated-client assessment

Package C owner: implementer1. All comparisons use the same final clean committed
API head and raw export below. Go and Rust require a separate bounded mechanical
synchronization: their older saved inputs omit two admin incident resources.
TypeScript needs no generated change: all 691 owned files match exactly. No client source, saved input, version,
lock or branch head has been changed by this assessment.

## API input and reproducibility

Source repository: `git@github.com:vpsfreecz/vpsadmin.git`, head
`da7724abdc080e59820cc4f0812ce1a41b3fc5df`. Implementer0 owns its clean-source and
independent fresh-database export proof in [B-export-receipt.md](B-export-receipt.md).
Its export/check batch passed: 14 safety/snapshot examples, zero failures, and
byte-identical schema, provenance and tooling lock across two independent fresh
fixture databases. This package did not duplicate API checks or exports.

Authoritative raw export: `/tmp/exception-root-cause-schema-1`. An unchanged copy
is retained under ignored `client-artifacts/raw-export/`; copies were checked
byte-for-byte. These exact raw artifacts were used for every comparison:

| Artifact | SHA-256 |
| --- | --- |
| `schema.json` | `7e2a529787c06944f1ad0cdf3369edd8b4650d79826f3bbda9101af2dfb67628` |
| `provenance.json` | `59194958ead214f70ff7835a0fec5e6d3280cfca6d31ddd2a97e3276e96186e8` |
| `tooling.Gemfile.lock` | `64c1663d2fd040dd5bf0e92aa7a5b2a1b187c5d464ba9b2cc5154aaf16729b69` |

Profile: schema format 1, API 7.0, protocol 2.0, `vpsadmin-full-fixture`, locale
`en`, mounted-source acquisition, mount `/`, synthetic source URL
`https://schema.invalid/v7.0/`. Six plugins: monitoring, newslog, outage_reports,
payments, requests, webui. Exported application inventory: 156 resources,
529 actions, 9031 parameters. Exact plugin source/migration and complete fixture,
configuration and dependency identities remain in raw provenance.

Profile digest: `26340ba241ddea3c2e65846b5eddb3d050802fc5d625768df5ca844667a1a899`.
This hashes canonical two-space sorted-key JSON plus one newline of the six
schema envelope identity fields (`schema_format`, `api_version`,
`protocol_version`, `profile`, `mount_path`, `source_url`) plus `locale` and the
complete `plugins` value from raw provenance. `client-artifacts/input-identity.json`
retains that exact profile object and artifact hashes.

Exporter tools: Ruby 3.4.12, Bundler 4.1.1, HaveAPI 0.32.2, ActiveRecord 8.1.4.1,
mysql2 0.5.7, MariaDB 11.4.13. Tooling Gemfile SHA-256:
`87df3509b79a68dcf55f4f344017c619a8fcf0dbb9e70e576a2d2d39891a8ef2`.
The exporter graph is separate from the retained per-client generator graphs.

## Assessed clients and ownership

Canonical SSH remotes were fetched on 2026-11-25 before worktree creation.

| Client | Exact assessed head | Default | Complete comparison scope |
| --- | --- | --- | --- |
| Go | `5934903568862a95b688479f0b13e11e4a36692f` | `master` | `client/*.go`, excluding handwritten `*_test.go` |
| Rust | `15db0ffd95ccd34247de9f839c906d860afb1b69` | `main` | recursive `src/generated/**`, including copied runtime/ownership manifest |
| TypeScript | `b619eb8324bfe80c7b225f698fb83efe97639c83` | `main` | recursive `src/generated/**`, including ownership manifest |

Registered owned worktrees are under
`worktrees/2026-11-25-exception-root-cause/<client>` on branch
`2026-11-25-exception-root-cause`. The separate
`haveapi-client-assessment` worktree uses branch
`2026-11-25-exception-root-cause-client-assessment`. All source worktrees started
clean; handwritten files and Go module metadata were preserved. Fresh candidates
were generated only under ignored `client-artifacts/`.

All three pin HaveAPI `1ef9b204ba45bb261d3334be5c555cc1856b713b` (0.32.2).
The complete Go generator/shared-source file hash map was independently checked
against `schema/generator.json` at the exact Go head. The canonical compact
sorted map plus newline hashes to
`73519c97ec02a7a57de4761c941db44945ce3e0233f389346ec4ef5ff0b9c486`.
The Go runtime is emitted from `clients/go/template/**` at that same source pin;
its template hashes are included in that checked map. No separate Go runtime
package is substituted.

| Client | Generator/runtime and dependency identities | Observed tools and formatter |
| --- | --- | --- |
| Go | retained generator lock SHA-256 `f75dfbefc8ced373a643517b9a416ac8886695b9ac74e2cf8bd2eabd0be1afc5`; exact full source hash map above | HaveAPI `.#client-go` shell; Ruby 3.4.11, Bundler 4.0.23, Go/gofmt 1.26.10 |
| Rust | generator source `7f941d42626a967296ae1c8e897ef7c9b249858f564e98a3d41824fbf10d15a1`; shared-schema source `d704e6c155f9f2ec82bdf627857bdc23aa08a1d2133806df1f8ed5beb2d8c439`; copied runtime `9c50b8167a8b82118ba42372633e3b004276ba49fbdfed75d4979a913feea739`; retained generator lock `061f5e4e0f3cb48d529a7914eb087cabda9889d4200a1af9d0d70af7908b5459` | client pinned Nix shell; Ruby 3.3.10, Bundler 4.0.23; `rustfmt 1.9.0`, edition 2024 |
| TypeScript | generator source `c21f17af40295bdd633f846ef9099bfb3d7a3c52aa1b581a802b5c42d7b426e7`; shared source identical to Rust; exact JS runtime `haveapi-client` 0.32.0 from retained npm lock | client pinned Nix shell; Node 24.21.0, npm 11.19.0, Ruby 3.4.11, TypeScript 6.0.3, Prettier 3.9.10 |

Rust `generator.toml` SHA-256:
`039f5e861b2cde5ba60666e62cbd75ca820b7b6584fd81dc848d639cefa94811`;
it selects crate `vpsadmin-client` 0.2.0, MIT, edition 2024, MSRV 1.95 and
`rustfmt 1.9.0`. Rust `flake.lock` SHA-256:
`922570e28119697ac47ab550f951e5badb9915f41bfaab6b9015d3a942c06254`.
TypeScript `package-lock.json` SHA-256:
`8b147b63067709354e55295c5bdbe208d9cc550e5d866ac273e574f92e866304`;
its runtime artifact integrity is
`sha512-ldZcLcQEV2hSEznKdrNGnpjwJLsyu5QyhHxf5DzrfBC12+L7ZVCKqC4Hz4KmjTG8B8HLXXgbOXF6503yXBQQYA==`.
TypeScript/HaveAPI `flake.lock` SHA-256:
`187d63f65b46f5cfa3ac830a5d0c182693cd0ca7ab8e486c3876fcf4b4f6d4f4`.
Packaged Prettier configuration SHA-256:
`ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356`.
Full identities, including runtime template hashes and executable store paths,
are retained in `client-artifacts/generator-identities.json` and preparation logs.

## Commands, transformations and results

Dependency preparation used each repository's documented Nix environment,
retained generator locks and npm graph. `client-artifacts/prepare.sh` passed
with exit 0 in about 90 seconds. Component logs are
`prepare-{go,rust,typescript}.log`; the requested outer preparation log was not
created. Source/pin/lock checks passed. No integration suite was run.

For Go, `tools/prepare-schema RAW EFFECTIVE` was run twice using the recorded
Python 3.13.17 executable. Both effective outputs were byte-identical. JSON
comparison confirmed exactly one transformation:
`description.authentication.oauth2.revoke_url` from
`http://api.test/_auth/oauth2/revoke` to
`https://auth.vpsfree.cz/_auth/oauth2/revoke`. This preserves the client's
existing endpoint without changing origin-trust behavior. Helper SHA-256:
`92a56fbc9056bda008b6e7c7c47c3f6b95f15e665f6158a593f1c93811f0e019`.
Effective schema SHA-256:
`138d11ce48b6b79db9ca55c3d16f4a1a98b5ba78078720be787bff6c4cf14a16`.
Owner is the Go repository's existing projection; implementer1 executed it.
Rust and TypeScript use the raw export unchanged.

The comparison batch invocation was:

```sh
bash work/2026-11-25-exception-root-cause/client-artifacts/compare-current.sh \
  /tmp/exception-root-cause-schema-1 da7724abdc080e59820cc4f0812ce1a41b3fc5df
```

Its Go generation used the documented command from the owned HaveAPI root,
with `BUNDLE_GEMFILE` selecting `clients/go/Gemfile`, the frozen retained lock,
and the isolated prepared bundle:

```sh
bundle _4.0.23_ exec ruby clients/go/bin/haveapi-go-client generate \
  --schema "$ART/go-effective.json" --api-version 7.0 \
  --output "$ART/go-output" \
  --module github.com/vpsfreecz/vpsadmin-go-client --package client
```

Rust used its existing `tools/regenerate` source-identity checks and Ruby loader
as an external-input assessment adapter: loaded gem roots, generator/shared-schema
and maintained runtime digests were verified before loading the same pinned
`clients/rust/bin/haveapi-rust-client` entry point. Arguments were:

```sh
generate --schema /tmp/exception-root-cause-schema-1/schema.json \
  --api-version 7.0 --config "$RUST_CLIENT/generator.toml" \
  --output "$ART/rust-output"
```

`ART` denotes this session's absolute `client-artifacts` directory;
`RUST_CLIENT` denotes its registered Rust worktree. Exact commands/environment
are retained in `compare-current.sh` and `generate-rust.rb`. Neither adapter
changed generator behavior or client inputs. Go and Rust commands passed.
The batch itself exited 1 at the unrun TypeScript step because a nested Python
path lost quotes in the evidence launcher. This was isolated from both passing
comparisons and corrected by extracting the TypeScript step into a separate
script. Its next attempt passed source/tooling checks but the generator refused
a fresh destination not ending in `src/generated`. No generated output or client
source was changed by either failure. The candidate path was corrected to
`$ART/typescript-output/src/generated` for the remaining TypeScript-only run.

The final TypeScript-only command passed with exit 0 in 17 seconds:

```sh
# From the registered TypeScript client worktree:
nix develop -c bash /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-exception-root-cause/client-artifacts/typescript-current.sh
```

It verified the retained tooling hashes and exact generator/shared-source identity,
then called the existing source loader with both pinned Ruby source include paths:

```sh
PRETTIER="$TS_CLIENT/node_modules/.bin/prettier" ruby \
  -I "$HAVEAPI_SOURCE/clients/ruby/lib" -I "$HAVEAPI_SOURCE/clients/typescript/lib" \
  tools/generator-source.rb generate "$HAVEAPI_SOURCE" generate \
  --schema /tmp/exception-root-cause-schema-1/schema.json --api-version 7.0 \
  --output "$ART/typescript-output/src/generated"
```

`TS_CLIENT` and `HAVEAPI_SOURCE` are the registered TypeScript and owned pinned
HaveAPI worktrees. `compare-typescript-final.log` retains successful source/tool
identity and comparison output. The first batch's `compare-current.log`, per-client
`compare-{go,rust}.log` and the diagnostic `compare-typescript-fixed.log` retain
the earlier outcomes. No completed passing comparison was repeated.

All native watchers used the installed separate utility policy: package
`/nix/store/1zn1a51qrsin83fszrprdjp45208vsj4-dev-workspace-0.2.0`, catalog
`1184a2cf511b6e77ff7afe12433027abe06e8bb0b897f39cffc26efd443d1a7c`,
`verification_watcher` = GPT-6 Luna/low, utility identity
`dw_c699c3bf36ffc569cca1d7f83580bf68e6fffbb536cfad0d`, effective
`danger-full-access` and approval `never`. Each operation used a fresh watcher;
all command/tool sessions finished. Watches did not edit or diagnose source.

Fresh file inventories compare the union of baseline/candidate paths and exact
SHA-256 bytes, recording additions, changes **and deletions**. Go excludes only
handwritten `*_test.go`; the recursive Rust/TypeScript scope includes hidden
ownership manifests. Complete before/after path-to-hash maps are retained in
`compare-{go,rust,typescript}.json`.

| Client | Result | Baseline → candidate files | Added / changed / removed |
| --- | --- | --- | --- |
| Go | current-source drift; no no-change conclusion | 693 → 697 | 4 / 1 / 0 |
| Rust | current-source drift; no no-change conclusion | 698 → 702 | 4 / 3 / 0 |
| TypeScript | no generated change required | 691 → 691 | 0 / 0 / 0 |

Go additions: `resource_incident_policy_evaluation.go`,
`resource_incident_policy_evaluation_action_index.go`,
`resource_incident_policy_exposure.go`,
`resource_incident_policy_exposure_action_index.go`.
Only existing-file change is `client.go`, registering the two resources.

Rust additions: `resources/incident_policy_evaluation/{index,mod}.rs` and
`resources/incident_policy_exposure/{index,mod}.rs`. Existing changes are
`.haveapi-generated.json`, `mod.rs` (schema digest) and `resources/mod.rs`
(module registrations). Copied runtime and existing incident-report files are
byte-identical. Go's existing incident-report files are also byte-identical.

Both Go/Rust saved raw schemas are from API
`de4df3d63f4d4afb0c27e8b9be2785c15d24811c`. A complete structural comparison
found exactly two added subtrees versus the final export:
`/description/resources/incident_policy_evaluation` and
`/description/resources/incident_policy_exposure`; no other changes/removals.
TypeScript's saved raw schema from API
`74c0af3aef3ec9124ca89ce7669ccd9b99633495` is byte-identical to this final export.
TypeScript's full regeneration also reproduces every owned file including its
ownership manifest, so its no-change conclusion is tied to this final API head,
raw schema/profile digest and pinned generator/runtime/formatter rather than
only a saved-input check. Thus the Go/Rust drift predates the ordering fix and is
already represented by the assessed TypeScript client. `schema-drift.json` retains the complete path list.

## Scope, gaps and next dependency

Package C status: ready for lead acceptance. The required assessment is complete;
the Go/Rust synchronization gap is reported and belongs to the next separately
released package. Capacity is available for that bounded package after C acceptance.

No client/generated files were edited, no commits were made, and no versions,
tags, releases, defaults, deployments or peer worktrees were mutated. Assessment
branches have zero commits above their exact starting heads; there are no new
migrations, transitional history or consolidation obligations in this package.
Long integration suites await final review and any separately released sync
package. No generator/runtime incompatibility was observed in completed runs.

Go/Rust current-source freshness is an explicit gap; it cannot be called
no-change at these heads. Reported to lead before expansion. Architect0 is
preparing A2 limited to mechanical saved-input/provenance and generated-output
alignment, retaining pins and the Go projection, with source-revision-only Go
README alignment. Existing candidates are reusable; no regeneration rerun is
needed when those inputs/pins remain unchanged. Lead owns C acceptance and any
new package release/capacity confirmation. This is not a sync execution assignment.

No project documentation update is useful for this evidence-only package.
Guidance and exact source identities were read and preserved; lead owns
state/portal coordination updates and any tracking commit. Source worktrees
remain available and session lifecycle is unchanged.

Stable session URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-exception-root-cause/
