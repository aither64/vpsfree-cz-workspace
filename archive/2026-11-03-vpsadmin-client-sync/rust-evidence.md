# Rust client synchronization evidence

Read-only investigation by implementer1, 2026-11-03. Session identity and both
environment markers match `2026-11-03-vpsadmin-client-sync` and the workspace.
No application/rule edits, worktrees, commits, releases, integration, builds or
regeneration were performed. Only the assigned Rust default ref was fetched.

## Exact inputs

| Repository | Default ref | Commit | Freshness |
| --- | --- | --- | --- |
| vpsadmin-rust-client | origin/main | `3ec8c045dcefcca85b60ffccd38259cda29eeb60` | SSH fetch and subsequent ls-remote agree |
| vpsadmin | origin/master | `942c6eaed41331f823d8e0f670ed239e2b308440` | Architect-owned fresh fetch; local ref verified |
| haveapi | origin/master | `f29c1e4675bc1f79641faa619b8c68ecec923c71` | Architect-owned fresh fetch; local ref verified |

Rust origin is `git@github.com:vpsfreecz/vpsadmin-rust-client.git`. Its upstream
HEAD selects main. Fetch command from the workspace root:

```sh
git --git-dir=repos/vpsadmin-rust-client.git fetch --no-tags --no-prune origin \
  refs/heads/main:refs/remotes/origin/main
```

Repository instructions and entry points read: Rust `AGENTS.md`, `README.md`,
`docs/development.md`; vpsAdmin `AGENTS.md`, `README.md`, `docs/README.md`,
`docs/api-schema-export.md`. All inspection used canonical bare repositories.

## Verdict: refresh needed against current API source

API commit `8225229aa0e3306f8b1723c5583969a33c64571c` is an ancestor of the
observed vpsAdmin default and adds contracts missing from the Rust default:

- `api/lib/vpsadmin/api/resources/security_advisory.rb:415` defines `Retract`
  (`POST {security_advisory_id}/retract`); line 440 defines `Delete`.
  Rust `src/generated/resources/security_advisory/mod.rs` exposes only create,
  index, publish, rebuild_affected_vps, show and update. No retract/delete
  modules exist for this resource. The saved schema has the same six actions.
- API `security_advisory.rb:63` defines optional `expected_state` in the
  precondition used by advisory update and the new lifecycle actions;
  line 485 defines it for nested node-status mutations. API
  `security_advisory_cve.rb:22` defines it for CVE create/update/delete.
  `git grep expected_state` across generated `security_advisory`,
  `security_advisory_cve` and `security_advisory__node_status` finds no matches.
  For example, Rust `security_advisory/update.rs:4` has an Input with
  `expected_content_revision` but no `expected_state` field or setter.
  Saved schema CVE create/update/delete inputs also omit `expected_state`.

This proves incomplete source-contract coverage, including unavailable typed
state guards. It does not claim existing requests universally fail, or establish
whether the new source contracts are deployed in production.

## Provenance and generation path

`schema/provenance.json` records an unauthenticated production OPTIONS capture
from `https://api.vpsfree.cz/v7.0/`, captured `2026-10-30T11:20:12Z`, profile
`public-live-api-7.0`. It records no vpsAdmin source revision. Coverage is 152
resources, 524 actions (519 API and 5 authentication), 8720 parameters; plugin
completeness is explicitly unknown. The capture used HaveAPI revision
`f0465630595b4fd120561337b3d1d7fa96cbe221` through its Go component.

Generation is separately pinned to HaveAPI
`1ef9b204ba45bb261d3334be5c555cc1856b713b`, generator/shared-schema version
0.32.2, Ruby 3.3.10 and Bundler 4.0.23. `generator.toml` pins edition 2024,
MSRV 1.95 and `rustfmt 1.9.0`; the recorded nixpkgs revision is
`fe13242281a67641c0102cdb1087f0ebe586c7df`.

`tools/regenerate` requires an owned, clean HaveAPI checkout at that exact
revision via `HAVEAPI_SOURCE`, the retained `schema/generator.Gemfile.lock`,
and the prepared frozen bundle. In the pinned `nix develop` environment it
invokes `clients/rust/bin/haveapi-rust-client generate` with:

```text
--schema schema/api-7.0.json --api-version 7.0
--config generator.toml --output src/generated [--check]
```

The script verifies source revision/cleanliness, dependency locks, loaded source
identities and copied runtime digest. It generates offline from the saved
snapshot, replaces only `src/generated`, and preserves handwritten package
files. `--check` reports generated drift without writing. Generated files must
not be patched manually. Exact setup is in `docs/development.md`.

Bounded object inspection confirmed the saved schema SHA-256
`70f89335e15263fd7177f29a00fab04b5ff1923c6922dfd318b07c3ae922fb8d`
agrees with provenance, inventory and generated manifest, and the retained Ruby
lock digest agrees with provenance. This is narrower than executing all checks.

## Existing enforcement and smallest recommendation

`AGENTS.md` enforces generated ownership and pinned regeneration.
`.github/workflows/ci.yml` runs on branch pushes, pull requests, dispatch and
workflow calls. It checks formatting/provenance, async/blocking tests, docs and
packaging, Rust 1.95, and deterministic regeneration with the **recorded**
HaveAPI revision and schema. There is no hook framework, scheduled upstream
freshness trigger, or comparison with current vpsAdmin source in this workflow.
`tools/check-provenance` checks stored snapshot/identity consistency;
`tools/regenerate --check` checks saved-input generation. Neither proves API
source freshness. `release.yml` publishes only by separate manual dispatch.

Use the existing regeneration workflow and make API-contract completion require
a client refresh or an explicit no-change conclusion tied to the API source
revision. The existing vpsAdmin `tools/export-api-schema` supplies a source-based
full-fixture schema and source/input provenance. Moving Rust to that input
requires an explicit profile/provenance refresh: it differs from today's public
production capture, so their raw digests are not directly comparable. Preserve
the chosen profile, source revision, schema digest and generator pin, then reuse
`tools/regenerate --check`. Keep package publication separate from source sync.
No new orchestration subsystem is needed. Architect owns the final cross-client
recommendation and exporter assessment.

## Limits and handoff

No byte-for-byte regeneration, compilation, live API capture, runtime acceptance,
CI-run inspection or complete schema comparison was performed. CI behavior above
comes from workflow source, not an observed successful run. The mismatch verdict
is established by representative source/snapshot/generated-contract evidence.
No permanent project-documentation edit is useful during this proposal-only
assignment. Lead owns consolidated state and next decisions.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-vpsadmin-client-sync/>
