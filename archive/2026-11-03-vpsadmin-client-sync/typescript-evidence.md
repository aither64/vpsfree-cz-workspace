# TypeScript client synchronization evidence

Investigation by implementer2, 2026-11-03. **The current TypeScript default
branch needs a schema refresh and regeneration to cover current vpsAdmin API
contracts.** Direct source/schema mismatches establish this; byte-for-byte
regeneration was not attempted.

## Identity and revisions

`dev-session current` and both environment markers matched
`2026-11-03-vpsadmin-client-sync` in `/home/aither/workspace/ai/vpsfree.cz`.
Initial tracking commit `34f13f05b` exists. Required workspace procedures and
the client README/development/releasing guides were read. The client default
tree contains no `AGENTS.md`; vpsAdmin's `AGENTS.md`, documentation index and
security-advisory guide were read before comparing its source.

| Repository | Ref | SHA and freshness |
| --- | --- | --- |
| vpsadmin-typescript-client | `origin/main` | `d354491537f8b654b4d2c33a705cad84474f95d6`; upstream HEAD confirmed by `ls-remote --symref`, then fetched by implementer2 |
| vpsadmin | `origin/master` | `942c6eaed41331f823d8e0f670ed239e2b308440`; architect0 fetched, locally confirmed |
| haveapi | `origin/master` | `f29c1e4675bc1f79641faa619b8c68ecec923c71`; architect0 fetched, locally confirmed |

Existing client origin is
`git@github.com:vpsfreecz/vpsadmin-typescript-client.git`. The sole fetch was:

```sh
git --git-dir=repos/vpsadmin-typescript-client.git fetch --no-tags --no-prune \
  origin refs/heads/main:refs/remotes/origin/main
```

## Recorded inputs and generation

At the client SHA above:

- `schema/provenance.json` records vpsAdmin source
  `5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5`, mounted-source acquisition,
  profile `vpsadmin-full-fixture`, API `7.0`, protocol `2.0`, 151 application
  resources and 519 actions. Plugins: monitoring, newslog, outage_reports,
  payments, requests and webui. Its exporter graph records HaveAPI gems
  `0.32.2`.
- `tools/generator.json` pins HaveAPI source
  `1ef9b204ba45bb261d3334be5c555cc1856b713b`, generator source SHA256
  `c21f17af40295bdd633f846ef9099bfb3d7a3c52aa1b581a802b5c42d7b426e7`
  and shared Ruby-client identity `0.32.2`. A newer HaveAPI default SHA alone
  does not establish generator-output drift.
- Saved schema SHA256 is
  `476f0086726a443a6ef8ad9a9d499bd3feff6eb6c5b0b652dcc999192d638794`;
  provenance SHA256 is
  `d51cfb24217fb381f66c1a0eb46168c637fea7ec988beb7e54b2d9a679ad81b6`.
  Both hashes were recomputed from committed blobs and match the generator pin.
- `src/generated/.haveapi-generated.json` records generator `0.32.2`, the same
  schema/source hashes, 675 owned files, application coverage 151/519 and
  separate excluded authentication coverage 1 resource/5 actions.
- `package.json` is package `0.3.0`, with `haveapi-client` peer/dev dependency
  `0.32.0`; this runtime package identity is distinct from the generator and
  exporter's `0.32.2`.

Documented existing path, not executed here: export candidates from a clean,
committed vpsAdmin checkout using its controlled `tools/export-api-schema
--prepare`, then `tools/export-api-schema --api-version 7.0 --output
/tmp/vpsadmin-schema-review`. Review and update the client schema, provenance,
exporter lock and generator pins. In the client's pinned Nix environment:

```sh
./tools/regenerate --haveapi-source /path/to/exact-haveapi-checkout
./tools/regenerate --haveapi-source /path/to/exact-haveapi-checkout --check
```

`tools/regenerate` verifies the exact HaveAPI HEAD, tracked/untracked source
cleanliness, Ruby/Node toolchain, source identity, VERSION and saved input/tooling
hashes. `tools/generator-source.rb` loads schema code from `clients/ruby/lib` and
the generator from `clients/typescript/lib`, then invokes
`clients/typescript/bin/haveapi-typescript-client`. Generation reads the saved
schema offline and owns only `src/generated/`; `--check` compares without
writing. Source URL `https://schema.invalid/v7.0/` is a context marker.

## Proven contract mismatches

The recorded vpsAdmin source is an ancestor of current `origin/master`, three
commits behind it. Commit
`8225229aa0e3306f8b1723c5583969a33c64571c` is after that source and an ancestor
of current master; all three ancestry checks returned success.

| Current API source contract | Saved TypeScript contract |
| --- | --- |
| `api/lib/vpsadmin/api/resources/security_advisory.rb:415` defines Retract, `POST /security_advisories/:id/retract`; `:440` defines Delete | `src/generated/resources/security_advisory/resource.ts` exposes only create/index/publish/rebuild_affected_vps/show/update and their aliases; no retract/delete action files exist |
| `security_advisory.rb:58` adds optional `expected_state` through `revision_precondition`, used by Update; `:480` defines the nested node precondition | `src/generated/resources/security_advisory/actions/update.ts` and nested `resources/node_status/actions/{create,update,delete}.ts` lack `expected_state` in input types and descriptors |
| `api/lib/vpsadmin/api/resources/security_advisory_cve.rb:17` defines the state precondition for CVE mutations | `src/generated/resources/security_advisory_cve/actions/{create,update,delete}.ts` lack `expected_state` |

All seven saved action schemas were also parsed directly from
`schema/schema.json`: `expected_content_revision` is present and `expected_state`
is absent. Saved advisory action keys are
`create,index,publish,rebuild_affected_vps,show,update`.

This matters beyond a missing TypeScript declaration:
`src/generated/runtime.ts:167` (`encodeFields`) rejects unknown input keys
before dispatch, so callers cannot pass the new guard through the existing
facade even with a type assertion. Current vpsAdmin's
`docs/security-advisories.md` requires draft synchronization consumers to send
`expected_state: draft` and capability-check all six sync mutation actions.
Refreshing the facade does not itself implement that application policy.

## Existing checks and smallest recommendation

Only `.github/workflows/release.yml` exists. Branch pushes, PRs and manual runs
check out the exact HaveAPI generator revision from `tools/generator.json`, run
offline regeneration `--check`, build/typecheck/consumer and unit checks, and
validate an npm archive. Publication is a separate tag-only protected job.
There is no scheduled/API-triggered comparison to current vpsAdmin source and
no vpsAdmin checkout/export in this workflow. Existing checks establish saved
input/output consistency, not API-default freshness.

Reuse this tooling. Refresh the full-fixture snapshot and regenerate the client
as an ordinary reviewed source update, without a package-version bump or
publication requirement. Add a short API-change completion rule in vpsAdmin's
own instructions linking to the existing export guide and each client's
regeneration guide; mirror the saved-input versus current-API distinction in
the client development guide. Keep the current client CI consistency check.
If an automatic freshness check is selected later, reuse the controlled exporter
and compare semantic schema content before demanding a refresh; a changed source
SHA alone can reflect unrelated changes. Avoid circular cross-repository merge
gates: API integration can precede the client refresh, with explicit owned
follow-up and a recorded API source SHA. No new orchestration subsystem is needed.

## Limits and handoff

No schema export, byte-for-byte regeneration, build, test, workflow execution,
package publication, code/rule edit, clone, worktree, commit or integration was
performed. No production API or registry was queried. The inspected workflow
configuration is evidence of declared checks, not a fresh CI result. This is
representative drift evidence, not an exhaustive API diff or a claim about
production deployment. Lead owns state/portal reconciliation and the architect
owns the cross-client recommendation.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-vpsadmin-client-sync/)
