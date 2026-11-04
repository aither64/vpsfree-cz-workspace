# Go client synchronization evidence

Read-only investigation by implementer0 on 2026-11-03. Session identity and
environment match `2026-11-03-vpsadmin-client-sync` in
`/home/aither/workspace/ai/vpsfree.cz`; initial tracking commit is
`34f13f05b0a9ca73a5cb862e067cc8d371e7f6d2`.

## Verdict and exact revisions

**The Go client default branch is stale against current vpsAdmin API source.**
Concrete missing actions and inputs prove this without regenerating the client.

| Repository | Default ref inspected | Exact SHA | Freshness |
| --- | --- | --- | --- |
| vpsadmin-go-client | origin/master | `134a9e69f9aa6ddec5c94b53744865c6f81ecdd0` | Implementer0 checked SSH remote HEAD and fetched only master |
| vpsadmin | origin/master | `942c6eaed41331f823d8e0f670ed239e2b308440` | Architect0 fetched; implementer0 verified local ref |
| haveapi | origin/master | `f29c1e4675bc1f79641faa619b8c68ecec923c71` | Architect0 fetched; implementer0 verified local ref |

Go origin is `git@github.com:vpsfreecz/vpsadmin-go-client.git`. The authorized
fetch used `-c fetch.prune=false -c fetch.pruneTags=false fetch --no-tags
--no-prune --no-write-fetch-head origin
refs/heads/master:refs/remotes/origin/master`. No project branch or checkout was
created or changed.

## Representative contract drift

API commit `8225229aa0e3306f8b1723c5583969a33c64571c` introduced the compared
contract and is an ancestor of the inspected API master (`merge-base
--is-ancestor` returned 0).

| Current API source | Go client at inspected head |
| --- | --- |
| `api/lib/vpsadmin/api/resources/security_advisory.rb:415` defines Retract; `:440` defines Delete | `client/resource_security_advisory.go:4` has neither accessor; neither corresponding generated action file exists |
| `security_advisory.rb:58` defines revision preconditions including optional string `expected_state`; Update uses them at `:343` | `client/resource_security_advisory_action_update.go:78` has `ExpectedContentRevision` but no `ExpectedState` or request-map entry |
| `api/lib/vpsadmin/api/resources/security_advisory_cve.rb:17` defines the same preconditions, used by Create/Update/Delete | `client/resource_security_advisory_cve_action_{create,update,delete}.go` all lack `expected_state`/`ExpectedState` |
| `security_advisory.rb:480` defines the same preconditions for nested NodeStatus Create/Update/Delete | `client/resource_security_advisory_node_status_action_{create,update,delete}.go` all lack `expected_state`/`ExpectedState` |

The seven existing mutation bindings above still contain
`expected_content_revision`. The missing state precondition is an ordinary
String input, separate from the documented Go limitation that omits Custom
inputs. Current API `docs/security-advisories.md` requires draft synchronization
consumers to send `expected_state: draft` on all six synchronization actions.
The existing typed Go bindings cannot express that precondition. Retraction and
deletion are admin-only actions; missing bindings do not imply API permission
changes. No live API availability or production deployment was checked.

## Recorded provenance and generation

- Client `README.md:402` records an unauthenticated public API 7.0 snapshot from
  2026-10-30 and warns that permissions/plugins determine its surface.
- Client `CHANGELOG.md:3` and regeneration commit
  `8a7483d535ac8caf86d318c89a773afde79c5ee2` record HaveAPI 0.32.0. That commit
  explicitly generated into fresh directories and removed obsolete outputs.
- The client tree commits no saved schema, source-API SHA, exact generator-SHA
  manifest or resolved generator dependency lock. The historical public snapshot
  and generator patch level therefore cannot be reconstructed from this tree
  alone.
- Client `README.md:414` and `AGENTS.md:20` document the legacy command
  `haveapi-go-client https://api.vpsfree.cz ./client`. It contacts production
  discovery and defaults to the server-selected API version. `AGENTS.md:28`
  prohibits hand edits to generated files.
- Current HaveAPI `clients/go/README.md` documents offline generation from a
  saved schema. `clients/go/lib/haveapi/go_client/cli.rb:36` implements
  `generate --schema FILE --api-version 7.0 --output FRESH_DIR --module
  github.com/vpsfreecz/vpsadmin-go-client --package client`. It verifies the
  snapshot API version and requires `go fmt` to succeed.
- At the inspected HaveAPI SHA, both root `VERSION` and
  `clients/go/lib/haveapi/go_client/version.rb` still declare 0.32.0. Ruby
  exporter/framework 0.32.2 provenance must not be described as a proven Go
  generator 0.32.2 revision. Pin the exact source SHA and resolved bundle.
- The Go CLI has no `--check`. `generator.rb:47` writes emitted files without
  deleting stale outputs; a fresh-tree comparison must detect removals too.

## Existing checks and minimal recommendation

The inspected client tree has 687 tracked files, zero `*_test.go` files and no
`.github` workflows, Makefile or synchronization script. Its existing checks are
documented `go test ./...` (primarily compilation) and Go formatting, in its
`shell.nix` environment. No tests or regeneration ran for this evidence task.

Proposed smallest change: require API-contract work to include a client refresh
or an explicit no-generated-change result, using the existing source exporter
and saved-schema generator. Retain the schema/provenance and exact source and
generator revisions with the client; add one ordinary client-repository CI
check that regenerates into a temporary directory, compares the entire owned
generated-file set including removals, and compiles the client. Preserve
handwritten tests and module metadata when reconciling generated output.
Do not make this check depend on production discovery or on moving defaults
across repositories. Package versioning/publication remains separate from
committing and integrating current generated source. Architect0 owns the wider
cross-repository ordering proposal.

This is direct source-contract evidence, **not byte-for-byte regeneration
verification**, a complete API drift inventory, a compile result or proof of
production schema parity. No code/rule edits, commits, release, integration,
deployment, long builds or regeneration were performed. Lead owns the state
summary and evidence link.
