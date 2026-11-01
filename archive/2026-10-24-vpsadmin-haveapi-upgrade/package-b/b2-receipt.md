# B2: Rust registry documentation adoption

2026-10-25. Bounded follow-up to Package B; final commit/hook proof follows below.
Session/environment identity matched the trusted binding before source access.
The lead owns current session state and the same-reviewer affected-lane packet.

## Scope and acceptance

Remove the Rust Git source from the API 7.0 profile and leave only
`crate_name: 'vpsadmin-client'`, without `crate_version`. Existing Go identity,
HaveAPI 0.30.1 requirements, authorization/locale/action coverage and performance
facts remain intact. The API does not choose or query a registry version.
HaveAPI's actual upstream init renderers now emit:

```text
// cargo add vpsadmin-client
// cargo add vpsadmin-client --features blocking
```

The new `:documentation_profile` tag selects the real API mount check and a
small init-render example. The latter uses the mounted Rust profile, a minimal
in-memory HaveAPI context and the actual async/blocking renderer classes. It
checks exact first-line hints, imports, execution modes and absence of Git,
revision or fabricated SDK version requirements. It does not render a full HTTP
version page. The existing full-page admin/member/anonymous and locale/action
example is retained, with its install expectations changed to registry hints.
`services-up` likewise retains tabs/actions while checking registry hints and
rejecting the former source identity. No VM run is claimed.

Four changed paths relative to old B head:
`api/lib/vpsadmin/api.rb`,
`api/spec/lib/vpsadmin/api/documentation_clients_spec.rb`,
`docs/api-client-examples.md`, `tests/suite/services-up.nix`.
The lead directly applied the required writing skill to the final current-doc
paragraph and accepted it without edits before commit. The original docs index
link remains part of the owning profile commit.

## Release evidence and limits

The architect's immutable release evidence remains in
`rust-crates-2026-10-25/{crates-io.json,comparison.json,release-comparison.json}`.
Non-yanked registry release 0.1.0 has checksum
`2099d96e698e23912879cc15a32097c920f0db96976c2bee671a5ce2239777d0` and source
`b6f84679d33ff041388535dcf4dc060aeb0d1b9d`. All 689 packaged Rust source/example
files plus LICENSE (690 identical files in the raw comparison) match former source
`ff876abe17e3301da62c1b6afbda055ec89db9d2`. API 7.0, Rust >=1.95, edition 2024,
async/blocking imports and feature contract remain unchanged. However, the
packaged Cargo.lock has 17 package-version replacements among 159 packages:
there is no claim of identical dependency graphs or compilation-result reuse.
No SDK compiler or dependency-resolution run was performed for B2.

The packaged `Cargo.toml.orig` separately matches the former source manifest.
The raw comparison is preserved unchanged; the independent review clarified
that its 690-file total includes LICENSE alongside the 689 Rust files.

The old full-page sample observations remain historical evidence at their
recorded old revision: 174 panels, 168 code results, six explicit Go limitations,
all 17 action sample identities, and zero missing SDK symbols in the static
checker. This bounded installation-source revision does not transfer a new
full-page or compiled-program pass to the changed head.

R1 remains blocking: exact published HaveAPI 0.30.1's anonymous documentation
request CPU amplification, measured previously at 50–139 seconds per page.
The user owns its remedy outside this package. No provider edit/version change,
cache, snapshot override, performance investigation or full HTML rerun occurred.
This revision does not establish overall readiness or clear R1.

## Quick verification

`nix develop .#api --command bash -c 'bundle exec rspec
spec/lib/vpsadmin/api/documentation_clients_spec.rb --tag documentation_profile'`
passed: **2 examples, 0 failures**, seed 8971, examples 18.05s and load 17.52s.
The same command batch checked syntax of both changed Ruby files and scoped
RuboCop: **2 files, no offenses**. See `b2-quick.log`.

`nix-instantiate --parse tests/suite/services-up.nix` passed. A lightweight Nix
evaluation of the actual `services-up` definition with a test-framework stub
extracted its interpolated `testScript` without building/booting guests. It
confirmed both registry hints and the source rejection, and the root Nix Ruby
interpreter checked the resulting Ruby syntax. Evidence:
`b2-services-up-script.{json,rb}`. This is assertion evaluation/syntax evidence,
not a packaged API or VM integration pass. Diff whitespace passed.

No changes to spec placement or CI topic patterns. No new database migration,
schema, wire protocol, SDK generated content or runtime dependency. Mixed API
workers may show Git versus registry install hints. Server rollback restores
this config/docs/assertion delta; consumer rollback uses its retained Cargo
manifest/lock. No deployment, publication, merge or lifecycle action.

## History consolidation

Old reviewed range: `b82eeca50cd4dd7bd76728685c7de8aad66e7ba5` through
`21872fe6ad373e52f66f193ee432f4885376e5a5` (A `ff44d95ebe9794341185ba5c78250e130dde80fd`
and B `21872fe6ad373e52f66f193ee432f4885376e5a5`). The old head remains reachable
at local feature ref
`2026-10-24-vpsadmin-haveapi-upgrade-before-rust-registry`; no refs are deleted.
`b2-old-commit.txt`, `b2-old-refs.txt` and the original Package B comparison
artifacts preserve old author/date/source and exact reviewed range.
`b2-source-delta.diff` records the four-path B2 edit before consolidation.

This unmerged/unpublished profile commit is amended coherently to avoid keeping
superseded source-pin instructions in the active series. No fetch/rebase/default
refresh occurred. Dependency commit A is unchanged. Original B author/date are
retained. There were no migrations or deployed/released/externally consumed
migration boundaries in either range. No supported consumer requires the
superseded server profile Git pin; old evidence is historical, not discarded.

## Final committed B2 head and review input

New exact head: `57a53e700132d43589f4e6bcf519f1c7ec3fd2ed`. Complete active series from
`b82eeca50cd4dd7bd76728685c7de8aad66e7ba5` is unchanged A
`ff44d95ebe9794341185ba5c78250e130dde80fd` followed by amended B
`57a53e700132d43589f4e6bcf519f1c7ec3fd2ed`. Original author Jakub Skokan
<jakub.skokan@havefun.cz> and author date 2026-10-24T22:19:22+02:00 retained.
The commit message describes the final registry-based profile contract.

Normal root-shell plain Git amend exited 0. Nixfmt, MigrationSpecs,
VpsadminWebuiI18n, RuboCop, VpsadminApiI18n and every commit-message hook passed
with no warnings. See `b2-commit.log`. Worktree and index are clean; no owned
operation remains running. No hook bypass or outer bundle-exec preflight.

`b2-range-diff.txt` compares complete old and new ranges; A is unchanged and the
B difference is exactly the four-path installation contract/check/docs delta.
`b2-final-history.txt`, `b2-final.diff`, `b2-final-files.txt` retain the complete
active history, diff and file inventory. No obsolete active Git-source pin or
follow-up commit remains. Both ranges contain **no migrations**, schema changes
or migration deployment/consumption boundaries. Historic full-page evidence and
timings remain under their original immutable paths and exact old revision.

These are inputs for `rust-registry-review.md` and the retained independent
reviewer's affected-lane follow-up, not merge/deployment readiness. R1 remains
blocking, the user owns the external performance remedy, and no old full HTML/VM
or compiler check was rerun or claimed.
