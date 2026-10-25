# Proposed follow-up commit split

Status: proposed only; no staging or commits. Head/base remains
`b64fb25bea8d8222fb3263b99956c0b61438a859` on
`2026-10-22-haveapi-release-followups`. Index empty; all owners yielded and no
runner, build, test, install or Git mutation is active. Await lead acknowledgement
and exact-path hooked commit grant.

The [JSON inventory](followups-commit-plan.json) lists every full path, partial
file allocation and final SHA-256: **six purposes, 45 unique application paths**.
Proposed order:

1. **R1 Fiddle runtime dependency:** gemspec, component lock, dependency spec,
   both approved `flake.nix` libffi additions, shared artifact inspection/smoke,
   Rust-contract release specs and the Fiddle paragraphs in both release guides.
2. **R1 generated naming lint:** two templates, generator/naming specs,
   focused integration mode and the nested-name/lint section in the Rust guide.
3. **J1 tooling:** npm manifest/lock, helper compiler option, gulp/shared Rollup
   config, maintained JSDoc config/alias helper, helper/doc tests and corresponding
   JS test-guide prose.
4. **J2 graph:** eight owned graph source/spec files, the explicit three-facade
   isolated emit config and graph-specific JS test-guide sentences. The strict
   declaration consumer's temporary tsconfig includes `types: []` and retains
   full strict declaration checking.
5. **P1 registry confirmation:** publisher/query and their specs, existing
   registry-version release-spec changes, recovery/confirmation guide prose
   including the lead's final wrap.
6. **Cumulative JS output:** exactly eight emitted bundle/declaration files,
   including the two new ignored declaration files. No regeneration needed.

## Shared-file allocations

| Path | First purpose | Later purpose |
| --- | --- | --- |
| `utils/release/spec/release_spec.rb` | R1: changed hunks within `Rust generator gem contract` | P1: changed hunks within `existing registry versions` |
| `doc/agent-instructions/releases.md` | R1: three-line retained-gem Fiddle paragraph | P1: partial-failure/recovery changes and final wrap |
| `clients/rust/docs/releasing.md` | R1 dependency: Fiddle paragraph, final lines 30–34 | R1 naming: nested-name/lint-mode section, final lines 62–84 |
| `clients/js/test/README.md` | J1: commands, helpers/loaders, licensing and JSDoc | J2: three graph sentences from `The dependency-graph check` through `Normal builds report warnings without filtering them.` |

J1 authored `clients/js/test/async-resources.tsconfig.json`; its complete diff
belongs to J2's logical graph purpose because retaining all facade emits is
required by the relocation. J1's shared Rollup factory must precede J2's test.
R1 package enforcement and its declaration enter together. P1's unrelated
registry changes need no R1 naming dependency. Partial staging must preserve
the final approved worktree bytes; never rewrite application files to split
history.

## Reconciled evidence and preservation

J1's final receipt and all 19 authored/generated SHA-256 values match current
files. Compatibility **53/0**, async **39/0**, resources **11/0**, source/public/
deep types, graph, ES5 and actual JSDoc page/anchor checks passed. Exactly one
product build: bundle
`df8012e07294e50da26165803ac44e928c9cf7b594ff5d9228ba70379a133938`.
The final J2 fixture correction was test-only; no rebuild followed.

R1 final nine-path yield was received from implementer3 (delivery `8a928f53`);
79 unit examples passed, five Ruby files style-clean, frozen native setup exit 0
in 21.80 seconds. P1: 170 Ruby and six Python tests passed, seven Ruby files
syntax/style-clean, release metadata valid. All owner commands exited.

The lead's sole later release-guide wrapping change is preserved; current guide
SHA-256 is
`0e355749cd3697d061c07295918a45dc98ab0f3304e29a8e3f514cb9bdf7121b`.
R1 doc, lock and gemspec hashes remain exactly at owner yield. No test repeat
was run for inventory or prose wrapping.

Keep `clients/rust/.bundle-user/` and `utils/release/__pycache__/` unstaged.
The released 0.30.0 source, original worktree/dist, refs, artifacts and receipts
remain untouched. No migrations. One npm lock stream, one Fiddle lock stream and
one cumulative JS generated stream; no intermediate generated commit.

After the separately granted commits: export complete b64-to-head history,
final diff, exact map and stream/no-migration evidence for reviewer0. Long
acceptance, feature push, integration, versioning and publication remain outside
this preparation.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
