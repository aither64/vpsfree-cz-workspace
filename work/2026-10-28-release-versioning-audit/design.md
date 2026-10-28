# HaveAPI release versioning: findings and proposed correction

Status: investigation complete; all implementation below is **proposed and
unimplemented**. Scope is HaveAPI only. No project checkout, branch, commit,
tag, release, push, merge or deployment was created or changed. The only Git
mutation was the authorized fetch of upstream master and tags into the canonical
bare clone. Architect owns this brief; lead owns acceptance and session records.

## Evidence at 2026-10-28

`dev-session current`, both environment identity values and the trusted thread
binding agreed on `2026-10-28-release-versioning-audit` in
`/home/aither/workspace/ai/vpsfree.cz`. The live roster confirmed architect0's
design role and write access. Inspection used `repos/haveapi.git` and its canonical
`git@github.com:vpsfreecz/haveapi.git` remote; no other session was inspected.

After serialized fetch, `git ls-remote origin` confirmed:

| Ref | Commit (peeled for annotated tags) |
| --- | --- |
| `master` | `2f5156262baaf137800c17a9321e617c2b5df1d5` |
| `haveapi-0.31` | `819bba5110e089465535ecd71ca2eb37a7d39caa` |
| `v0.31.0` | `c9124da141adc258fbbaf67d4ec19ee3f8580849` |
| `v0.31.1` | `d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42` |
| `v0.31.2` | `819bba5110e089465535ecd71ca2eb37a7d39caa` |

The annotated tag objects are respectively
`d300dfa8715cca35c29bce312333ece886b5e74e`,
`4d665d6bc1a2f6a62710219150afd2175c312347`, and
`815c033be8cfca22822d0b2f80c022e959c5d0c4`.

None of those three release commits is an ancestor of master. Their common
merge base with master is `4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c`.
In contrast, the minor release tags `v0.27.0`, `v0.28.0`, `v0.29.0`, and
`v0.30.0` are ancestors of master. Master's last VERSION change is
`b64fb25bea8d8222fb3263b99956c0b61438a859` (Version 0.30.0, October 22).

Master's root `VERSION` and all maintained component identities are `0.30.0`;
the same fields at `v0.31.2` are `0.31.2`:

- Ruby constants: `servers/ruby/lib/haveapi/version.rb`,
  `clients/ruby/lib/haveapi/client/version.rb`,
  `clients/go/lib/haveapi/go_client/version.rb`,
  `clients/rust/lib/haveapi/rust_client/version.rb`, and
  `clients/typescript/lib/haveapi/typescript_client/version.rb`.
  Their gemspecs derive package versions from these constants.
- JavaScript: `clients/js/package.json`, `clients/js/src/haveapi/client.ts`,
  and the tracked `clients/js/dist/haveapi-client.js` version assignment.
- PHP: `clients/php/composer.json` and `clients/php/src/Client.php`.
- Python: `clients/python/pyproject.toml`.
- Four dependent gemspecs require `haveapi-client ~> 0.30.0` on master versus
  `~> 0.31.2` in the release. The ActiveRecord example's HaveAPI constraint also
  differs. Unmaintained Elixir components and protocol version `2.0` are separate
  identities and must not be updated as part of this repair.

`git diff --stat origin/master v0.31.2` identifies exactly 19 differing files:
17 version/constraint paths, `CHANGELOG.md`, and
`servers/ruby/spec/performance/release_lineage_spec.rb`. Master lacks changelog
entries for `0.30.1`, `0.30.2`, `0.31.0`, `0.31.1`, and `0.31.2`.
`git cherry -v origin/master v0.31.2` marks the four nonrelease patch commits
`f47aacc1`, `baa736f2`, `4dd137d6`, and `5a016f08` as patch-equivalent to master
commits. There is no additional application behavior diff in this comparison.
This proves content equivalence for those changes, not literal merge ancestry.

The release-only test fix is
`c9124da141adc258fbbaf67d4ec19ee3f8580849`, which isolates synthetic 0.30
maintenance fixtures from the checkout's current version. On master,
`release_lineage_spec.rb:79` calls `Release.version(original)` before making
synthetic fixtures; `servers/ruby/benchmarks/performance_compare.rb:105` accepts
only `0.30.N` for that specific historical maintenance contract. Therefore a
version-only bump exposes a test-fixture failure. This conclusion is from source
inspection; no test suite was executed. The production maintenance guard must
remain narrow; the already-released test adaptation addresses the fixture issue.

Primary publication checks returned HTTP 200:

- [RubyGems exact haveapi 0.31.2 metadata](https://rubygems.org/api/v2/rubygems/haveapi/versions/0.31.2.json)
  reports version `0.31.2`, created `2026-10-28T09:17:26.825Z`, gem SHA-256
  `f1c3869bea92a3902c0e52d22f036906db5d1ca964303db587c506c6d49f04a0`.
- [GitHub release v0.31.2](https://github.com/vpsfreecz/haveapi/releases/tag/v0.31.2),
  checked through its public API, is published, neither draft nor prerelease,
  at `2026-10-28T09:20:14Z`. Its listed assets include the five gems, npm/browser
  outputs, PHP archive, Python wheel/sdist, notes and manifest. Its API field
  `target_commitish: master` does not establish ancestry; the peeled Git tag
  above is authoritative. This sample confirms publication, not an independent
  checksum audit of every destination.

## Root cause and limits of attribution

The 0.31 release metadata commit
`3bbb98e76e286d64707c368fe1c2cc4d03f35eed` was added after branching from master
and remains release-only. The later release metadata and fixture fix also remain
absent from master. This is branch metadata synchronization failure, not a
runtime cache or one forgotten component constant.

Under the user's clarified policy, leaving patch version bumps on release
branches is intentional. The defect is master's missing **major/minor** advance
to `0.31.0`, alongside the missing notes and generally applicable test fix.

The current procedure, `doc/agent-instructions/releases.md`, says to create
`haveapi-X.Y` from master, then run `make version`, update the changelog and tag
on the release branch. It calls master the development version but defines no
minimum version or synchronization step. The existing `Makefile` version target
updates only its checkout. `Artifacts#check` in `utils/release/artifacts.rb:79`
checks local component agreement, dependency constraints and a local changelog
entry. `Artifacts#check_tag` at line 151 checks tag identity, the remote tag,
newest release branch and tag ancestry on that branch; it never checks master.
`.github/workflows/release.yml` invokes this validation for tagged builds, and
`utils/release/cli.rb:34` invokes it again before publication stages. Consequently
the documented and automated path permits a successful release while master
remains consistently stale.

Git proves what did and did not propagate. It does not prove whether a maintainer
forgot a step, deliberately kept master behind, or followed an instruction from
an unavailable conversation. No historical operator motive is asserted.

## Proposed implementation package and boundaries

One small HaveAPI package, owned by one implementer after authorization, is
sufficient. Its prerequisites are a fresh master/release comparison and lead
acceptance of the version policy below. No other repository needs an edit.

1. **Immediate catch-up:** use the existing `make version` flow to synchronize
   master's maintained identities and constraints to `0.31.0`, the latest
   released major/minor line with patch zero. `haveapi-0.31` retains `0.31.2`.
   Preserve a higher master major/minor line if it advances before implementation,
   still with patch zero. Carry over the missing release changelog entries and
   port the release-only maintenance-fixture adaptation into
   `servers/ruby/spec/performance/release_lineage_spec.rb`, preserving subsequent
   master changes. These paths are the 19-file difference identified above;
   prepare local ignored locks through the existing dependency workflow.
   Do not invent a next release number or add a prerelease suffix: the current
   release parser accepts only numeric `X.Y.Z`.
2. **Define the future policy** in `doc/agent-instructions/releases.md`: master
   records the latest major/minor version as `X.Y.0`. Prepare and integrate each
   intended major/minor bump on master before cutting `haveapi-X.Y`. Subsequent
   patch bumps stay on that release branch; do not propagate their package
   versions or patch-specific internal dependency constraints to master.
   Applicable release notes and general source/test fixes still propagate, while
   retaining master's synchronized `X.Y.0` identities and constraints. A higher
   master major/minor line remains valid for a supported branch's patch release.
   Master synchronization/integration still requires separate authorization.
3. **Minimal guard:** extend the existing `Artifacts#check_tag` in
   `utils/release/artifacts.rb`, with cases in
   `utils/release/spec/release_spec.rb`, to validate a freshly fetched
   `origin/master:VERSION`: require the existing numeric `X.Y.Z` grammar,
   `master.patch == 0`, and numeric tuple comparison
   `(master.major, master.minor) >= (candidate.major, candidate.minor)`.
   Thus master `0.31.0` permits candidate `0.31.2`; a full-version floor would be
   incorrect. Missing/malformed master evidence fails visibly. The workflow
   already checks out full history independently for build and publication;
   document and verify ref freshness and the local preflight requirement.
4. **Master checks:** tag validation alone cannot enforce patch zero on every
   master push. Reuse the existing quick metadata validation (`Artifacts#check`)
   for the local master checkout and master build-only CI, passing explicit
   master context through `utils/release/cli.rb` and the existing release workflow
   where CI uses a detached checkout. Add `VERSION` to that workflow's path
   filters so a standalone VERSION edit triggers validation. Scope the zero-patch
   assertion to master; release-branch checks must allow nonzero patches.
   Existing consistency checks continue to require all maintained identities and
   constraints to match their checkout's VERSION. This is proposed validation,
   not an assertion that current CI already enforces the policy.

No new subsystem or automatic master write is needed. Preserve the existing
tag/source/newest-release-branch checks. Do not require the release tag to be an
ancestor of master: release branches and cherry-picked fixes intentionally have
distinct ancestry. Version comparisons and a GitHub Release's `target_commitish`
are not proofs of application-content integration.

## Compatibility, deployment and recovery

The proposed change affects package identity, internal dependency constraints,
release validation, release documentation and a test fixture. It adds no schema,
on-disk format, protocol, API or generated-configuration migration. Existing
published consumers remain unchanged. Source-built consumers may observe the
corrected version in package resolution, CLI output or generated documentation;
keep coordinated component versions together. No fleet-wide coordinated update
is required and no deployment is necessary to repair repository metadata.

Published tags and accepted package bytes are immutable. **The new guard applies
to future tagged tooling.** Existing 0.31 release recovery continues to use its
original tagged helpers, saved artifacts and manifest; do not retag, rebuild or
republish accepted 0.31 packages to add the guard. The selected release procedure
already requires original tooling/artifacts for recovery. Source corrections can
be reverted through ordinary reviewed commits; they do not roll back registry
publications. Any later publication needs separate approval and the normal
protected environment. Integration also requires separate approval.

## Acceptance criteria and verification brief

Investigation checks completed: fresh SSH ref/tag inspection, ancestry checks,
full master-to-tag path diff, patch-equivalence classification, source inspection
of version/release checks, and the two primary publication samples. No runtime
test or build was needed or run for this findings-only assignment.

For an authorized implementation, quick checks in the documented top-level Nix
shell should establish:

- All maintained identities and internal constraints agree with the selected
  master VERSION, initially `0.31.0`, with patch zero; release-branch versions
  remain unchanged. Release notes are retained and no unrelated source paths
  change. Prepare dependencies with `make release-deps`, then use
  `make release-check` and source-only `ruby utils/release/cli.rb check-clean`
  after committing. Generated files follow the repository's existing workflow.
- Focused release specs accept master `0.31.0` with candidate `0.31.2` and an
  explicitly higher master major/minor with patch zero. Reject an older master
  major/minor, nonzero master patch, and absent/malformed metadata. Compare
  integer major/minor tuples, including multi-digit and major-boundary cases;
  candidate patch does not raise master's required version. Preserve existing
  tag/source/release-branch rejection cases. Mock remote reads or use disposable
  test repositories; never push real tags.
- Focused quick-validation cases reject a nonzero patch in master context,
  including detached master CI, while accepting it for release branches. Confirm
  a VERSION-only master change selects the existing build-only workflow.
- Focused `servers/ruby/spec/performance/release_lineage_spec.rb` passes with
  the new master version and a synthetic later-minor template while the original
  production 0.30 maintenance guard still rejects unsupported inputs.

After intended changes are committed and quick checks pass, perform the required
independent final review. Then run existing `make release-test`, relevant server
checks and build-only release CI as warranted by the changed package identities;
delegate long or uncertain checks under the monitoring procedure. None of these
checks authorizes publication. The investigation itself triggers no independent
final change review.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-release-versioning-audit/
