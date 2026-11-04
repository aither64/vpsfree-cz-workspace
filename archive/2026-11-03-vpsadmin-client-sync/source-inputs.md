# Phase 1 shared API source input

Ready for client regeneration, 2026-11-03. The raw export is unchanged. This is
source-fixture evidence, not proof of a deployed API or its runtime permissions.

## Source and saved artifacts

Architect0 refreshed the API default and approved these exact inputs:

- vpsAdmin: `942c6eaed41331f823d8e0f670ed239e2b308440`, from
  `git@github.com:vpsfreecz/vpsadmin.git` master.
- HaveAPI generator source: `1ef9b204ba45bb261d3334be5c555cc1856b713b`, the
  existing 0.32.2 release pin. Current master is
  `f29c1e4675bc1f79641faa619b8c68ecec923c71`; the architect found no generator or
  shared-schema implementation difference, only eight version/gemspec declarations.
- Source worktrees: `worktrees/2026-11-03-vpsadmin-client-sync/{vpsadmin,haveapi}`
  relative to the workspace. Both remain clean at the above exact commits.
  Their registrations retain those initial bases. The nonancestor HaveAPI pin is
  a source dependency; exact-final-head completion handling remains with the lead.

The shared directory is [source-inputs/api-7.0](source-inputs/api-7.0/).
Preserve its three files byte for byte:

| Artifact | SHA-256 |
| --- | --- |
| [schema.json](source-inputs/api-7.0/schema.json) | `d6ec617653913c56e92398a6032aa350118597a0e3f45c599bc92b6071ea0a26` |
| [provenance.json](source-inputs/api-7.0/provenance.json) | `c85815abd315f53a5ef05f324abe377760293786a13a25b7a127ec804c50e0c1` |
| [tooling.Gemfile.lock](source-inputs/api-7.0/tooling.Gemfile.lock) | `62a0e7f65e0755296ea50e3f5efa590f51e8615571a078cf45243f6ca8555f1c` |

The independent [repeat export](source-inputs/api-7.0-repeat/) matches all three
files exactly. No provenance normalization was needed, including database fields.

## Contract and provenance

The envelope is format 1, API 7.0, protocol 2.0, mount `/`, profile
`vpsadmin-full-fixture`, with synthetic source URL `https://schema.invalid/v7.0/`.
The exporter used English and all six bundled plugins: monitoring, newslog,
outage_reports, payments, requests and webui. Each plugin reports version 4.2.1;
its full tracked-source digest and applied migration inventory are preserved in
`provenance.json`.

Inventory: 151 resources, 521 actions, 8,760 parameters. The scope inventory digest
is `a8d34345461583b9c489067ef72829a62add2cd119e815c9e318ad459602590a`.
The source receipt includes the seven fixture/configuration input hashes, exact
API commit, complete loaded-gem inventory and exporter Gemfile/lock hashes.
Exporter code is `tools/export-api-schema` and `tools/api-schema-export/` from
that unchanged API commit. Tooling used Ruby 3.4.9, Bundler 4.0.23 and MariaDB
11.4.12. The isolated exporter HaveAPI and client-generator gems are 0.32.2;
their archive SHA-256 digests are retained in the provenance. This does not change
any packaged runtime dependency.

Quick assertions passed for the envelope, source revision, locale, complete plugin
profile, schema digest and repeated artifacts. `security_advisory.retract` and
`security_advisory.delete` are present. Optional string `expected_state`, with
draft/published/retracted choices, is present on all seven compared mutation inputs:
advisory Update, advisory CVE Create/Update/Delete and advisory node-status
Create/Update/Delete. Retract and advisory Delete also retain this parameter and
the content-revision precondition.

Parent checks recomputed all seven fixture/configuration hashes and all six
complete plugin-source hashes against the unchanged checkout, plus the exporter
Gemfile and saved tooling lock hashes; all match the retained provenance.

The fixture OAuth URLs, including `http://api.test`, remain unchanged. Rust and
TypeScript consume the raw schema. The lead/architect approved a finite Go-only
derived-input projection retaining its shipped revoke URL; implementer0 owns that
projection, hashes, provenance and tests. The raw shared input remains authoritative
evidence of the API source fixture.

## Execution and setup evidence

A fresh operation utility used `gpt-6-luna`/low with pinned catalog digest
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`, native
identity `dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`, full-access
sandbox policy and approval `never`. It completed the batch in 204 seconds,
exit 0. No operation remains running and its single utility slot was released.

From the vpsAdmin worktree, the batch entered `nix develop .#vpsadmin`, prepared
the existing isolated exporter bundle using `tools/export-api-schema --prepare`,
and ran the existing `safety_spec.rb` and `snapshot_spec.rb` with RSpec's
`--options /dev/null`: 14 examples, zero failures. These database-free checks used
the isolated exporter bundle, which derives the normal API Gemfile and pins
HaveAPI 0.32.2, avoiding a redundant second API dependency installation. Then:

```sh
tools/export-api-schema --api-version 7.0 --output /home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-vpsadmin-client-sync/source-inputs/api-7.0
tools/export-api-schema --api-version 7.0 --output /home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-vpsadmin-client-sync/source-inputs/api-7.0-repeat
```

Each invocation used its own fresh temporary MariaDB fixture. Exporter safety
checks excluded inherited database/Bundler overrides and local configuration;
no production API, database, cluster or server was accessed.

Worktree creation initially reported stale Overcommit configuration signatures
after creating and registering both clean source trees. The utility signed the
reviewed configurations without bypassing hooks. No creation retry, source edit,
commit, publication or merge was needed. Client owners retain their own ignored
component locks and isolated bundles; shared HaveAPI tracked source and root
`.bundle/config` remain immutable.

Full run evidence: [export-batch.log](source-inputs/logs/export-batch.log) and
[export-batch.exit](source-inputs/export-batch.exit). Raw JSON, locks and logs are
disposable session artifacts; clients must retain their required input copies and
provenance in their own deliverables. The original Markdown receipt remains useful
after those artifacts are retired under the workspace retention procedure.
