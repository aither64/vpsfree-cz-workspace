# Package A: source backport handoff

Owner: implementer0. Architect-owned package A and lead's GO accepted before
source work. Status: complete, with all nine pure backports committed locally
and focused checks passed. Clean checkout/index available for the lead's
serialized transfer to implementer1. No push, versioning, publication or
release/default integration.

## Exact source and result

- Repository: `git@github.com:vpsfreecz/haveapi.git`.
- Checkout: `worktrees/2026-10-25-haveapi-backport-release/haveapi`.
- Branch: `2026-10-25-haveapi-backport-release`; intended target: `haveapi-0.30`.
- Maintenance baseline: `1c3c98f0d77e0b23c8da1a8937f25c5799864a3b` (v0.30.1).
- Master snapshot: `38ecca75edaf797d048fb36c6a50ea7e05eb50a9`.
- Common source ancestor: `b64fb25bea8d8222fb3263b99956c0b61438a859`.
- Package A head: `b9b971b929edc75ef2f11fb6e541c1e0b52c99e1`.

Each new commit was applied in the specified order with ordinary
`git cherry-pick -x` inside the declared top-level Nix shell. All nine completed
without conflicts, source adaptations or hook bypasses. No duplicate source
commits were replayed. Existing release metadata remains byte-identical to the
maintenance baseline; source-only release metadata validation reports 0.30.1.

## Complete source mapping

Every master-side commit since the common ancestor has one existing or new
maintenance counterpart with the same stable Git patch ID. Each counterpart has
the exact upstream provenance trailer. The nine new commits are the complete
baseline-to-package-A series; the other thirteen already existed in v0.30.1.

| Master source | Maintenance counterpart | Disposition |
| --- | --- | --- |
| `cbf6a3f0b34f15e2bb4224872b46c423d7d02313` | `587a04d0f88705724f88686002bde99a2a0b03cb` | Existing |
| `431d7ffed098c7403d3d0555b3b93c4a3ab8b3e3` | `40471f2ed2fc394d941dd8b15cc7377187c8812c` | Existing |
| `01a30a39cdfc0d81e2eca62dcce912c165d891fa` | `e3648859bb0d1520993c092efc75ec9146a98081` | Existing |
| `412511176d7f54a96d48bc0995b202f335d1be4f` | `73df386699a03adb307f1c612763e944f48e0c9b` | Existing |
| `c424c579a314593e25cfe661374caafb9ab78a4c` | `e406ae4c4f683398dd0f6bcc74d3d898bbc93163` | Existing |
| `090a188cb4ef3477324718627f4ae3415d1c0975` | `8270b519a2ea1d60735634d34cc1a451a3e904b4` | Existing |
| `4dc0f7e11c494d1a0dc852dabcc312411699fcab` | `682a9869f7b3cfb90e25b330dc6d138d36e27b46` | Existing |
| `6cb3c3e80b827b665e00da3de588d97eb9d00ec3` | `a252adbc94bce918c2605e503c3582853ec0a483` | Existing |
| `f08d3f63cd1d4e4dc6731bad81ec6f34d6228921` | `d7bfed7778aac9d34384d82669b45d39a9330cb7` | Existing |
| `dc52a7a52d0991b597f44cd5bd8901eec92259f9` | `9c5de16776a964dadf1b886b5d22f3b7183a3414` | Existing |
| `67fcd34ba506264a5c7ee2e8e18a88d221c6f469` | `8591394e13144431b27ecb366aae2b7b77a94e2c` | Existing |
| `7ac977a26080d45d44b6608aafad2cadd2ec7f81` | `2ffaa682f9461f696c098cba5dd457e2010e6138` | Existing |
| `1103a3a14b1dc6dec17fc4859df80220a54f111d` | `173184597412411bf0c06479cfed5ec36d3a6d05` | Existing |
| `39909094649b1d14a23f00615775ca7136acf4fd` | `17272733cd27429e1ad6ea2eac0da6050816635c` | New 1/9 |
| `5003ded2a47db6b1637a3fef2fdd40474ea7de06` | `4c12fc84e7827b97cc8c1faf8a083325c18991ea` | New 2/9 |
| `82a7f8880663dfa9d8ad6cd67e981a5842dedf9c` | `5f038aba93c341bab37a687db254cc4849fd61fa` | New 3/9 |
| `de799b595d04e880d092b3e5ef47bce2f4587130` | `48ae0d5541b97bb9bae10924b85dc13e0a6146e1` | New 4/9 |
| `b85ec364057f536940d689b09e612512ffffaf82` | `8b7abc097db49893da9cc8fa4395648901fec71d` | New 5/9; package B lineage |
| `610da4e3212e66fac026eb94eedb55abf6d3c66a` | `89389777edac5a67f9f8d57e5d042c060c30c1ec` | New 6/9 |
| `4e05ca8dc4f6b938814b354996025b0aad91d9c7` | `559c162316cbb23db0d84e969da029ea82354ab9` | New 7/9 |
| `e98e704e926961bc6d8e4a12ee15c77c1380e7a8` | `6a4d0ada1ccb2133a34c638db6c48aacb2e16c36` | New 8/9 |
| `38ecca75edaf797d048fb36c6a50ea7e05eb50a9` | `b9b971b929edc75ef2f11fb6e541c1e0b52c99e1` | New 9/9 |

`git cherry -v HEAD 38ecca75edaf797d048fb36c6a50ea7e05eb50a9` now
reports all 22 source commits with `-`. Independent stable patch-ID comparison
also passed for every pair. The nine-commit `git range-diff` reports only the
added provenance trailers in the commit messages, with no code differences.

The package A commits preserve separately integrated upstream functional units.
There are no local superseded approaches or follow-up fixes to consolidate.
Final whole-branch history assessment remains with the independent reviewer
after packages B and C.

## Tree comparison and migration conclusion

The final master-to-package-A diff contains exactly the sixteen paths changed by
the existing v0.30.1 metadata commit: CHANGELOG, VERSION, component version
constants, internal HaveAPI dependency constraints, JS/PHP/Python package
versions and the example HaveAPI constraint. Comparing these paths with the
maintenance baseline is empty. All other tracked files have identical mode and
blob identity to the master snapshot, including the fixed performance budget
and reference declarations. `flake.lock` is unchanged.

**No database migrations or persisted-state changes.** New SQLite schemas and
seed operations exist only in disposable test fixtures. The package has no
network protocol or public generated-client contract change and requires no
deployment ordering or state conversion on rollback to 0.30.1.

Package B still owns the accepted release-lineage adaptation; the pure backport
intentionally retains master's reference/ancestry and own-version comparisons
until that separate reviewed work is applied. Package A alone is not a release
candidate ready for branch CI or publication.

## Imported workflow action verification

On 2026-10-25 queried each official SSH upstream with `git ls-remote --tags` and
compared stable numeric release tags and the imported aliases. All imports in
the two backported workflows use the latest stable release or its matching
major alias; no version edit was needed.

| Official upstream | Latest stable verified | Exact tag/major-alias commit |
| --- | --- | --- |
| [actions/checkout](https://github.com/actions/checkout) | `v7.0.1`; `v7` matches | `3d3c42e5aac5ba805825da76410c181273ba90b1` |
| [actions/cache](https://github.com/actions/cache) | `v6.1.0`; `v6` matches restore/save | `55cc8345863c7cc4c66a329aec7e433d2d1c52a9` |
| [actions/upload-artifact](https://github.com/actions/upload-artifact) | `v7.0.2` | `cf430e030ddbb5b0abf93d22962f4752f3646cd9` |
| [cachix/install-nix-action](https://github.com/cachix/install-nix-action) | `31.11.3` | `75c75c31ebece974e48ebc36b4ad125bd97bd97b` |

## Checks and documentation

Known quick checks passed in the top-level Nix environment:

- `bash -n utils/update-nixpkgs.sh`.
- `ruby utils/release/cli.rb check-clean`: release metadata valid, 0.30.1.
- RuboCop over all 22 changed Ruby files: no offenses.
- All 22 stable patch-ID/provenance mappings; all metadata paths unchanged.

The fresh `package_a_quick_checks` Luna/low utility completed the related
environment preparation and focused-check batch in `package-a-quick-checks.sh`:
server/Rust bundles, `make doc`, three affected server documentation/context
spec files, deterministic `spec/performance`, Rust generator unit specs, then
the normal Overcommit diff check. Exit 0 in 140 seconds at the exact package A
head; no operation remains running. Results:

- Server focused context/documentation and deterministic performance specs:
  105 examples, 0 failures, seed 60317.
- Rust generator unit specs: 147 examples, 0 failures, seed 21379.
- Overcommit: HaveapiI18n and RuboCop passed; all applicable pre-commit hooks
  passed on the complete base-to-head diff.
- Final `git diff --check` and scripted assertions for exact head, clean
  checkout/index, nine new commits, all 22 patch-equivalent upstream commits,
  the exact sixteen metadata-only master differences, unchanged maintenance
  metadata and unchanged flake lock passed.

Full output: `package-a-quick-checks.log`. Compact status:
`package-a-quick-checks.result`. Expected negative-case error JSON and temporary
packaging-fixture warnings occur inside successful assertions; the suite has no
failures.

Existing hook setup evidence is in [hook-preparation.md](hook-preparation.md).
Git's ordinary cherry-pick path was used without disabling any hooks; the
explicit Overcommit diff run verifies every configured pre-commit check on the
complete backported diff.

Project documentation backports explain context ownership, selected-subtree
normalization, benchmark usage, fixed performance gates and flake ancestry
behavior. Reviewed their placement in the existing development guide,
`doc/client-examples.md`, `doc/performance.md` and the Rust adapter guide;
their bytes match the master snapshot. Temporary package/release evidence stays
in this session. No additional prose changes were needed for the pure backport.

## Ownership transfer

Package A source/index/Git work is finished; implementer0 will make no further
checkout mutations while the lead transfers ownership to implementer1. The
prepared local server/Rust bundles and ignored locks remain available for the
next package. No long timing campaign, all-component integration suite or branch
CI has run. Package B/C, final independent review, longer checks, branch
publication and authorized release coordination remain with their assigned
owners. No machine reservations. Please reconcile this accepted report into the
lead-owned state record under the existing tracking cadence.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-haveapi-backport-release/>
