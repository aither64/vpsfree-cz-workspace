# confctl v3.0.0 release preparation

## Scope, interfaces and files

Expanded user scope: refresh Gemfile.lock dependencies and regenerate gemset.nix
with Bundix. Add `skills/confctl-release/SKILL.md` and repository AGENTS.md
routing for future releases. Keep the dependency refresh and release procedure
commits before the final release commit. Rewrite only this unmerged branch;
preserve remote lease evidence and the original release patch in session records.

Prepare release text and version metadata on the session's confctl feature
branch. Summarize the released v2.2.3 to current master changes in
`CHANGELOG.md`; update `lib/confctl/version.rb` and the local package version in
`Gemfile.lock`, and the confctl path-gem entry in `gemset.nix`. The gemspec
consumes the version constant. Follow the
existing dated changelog and `Version 3.0.0` release commit convention.

## Invariants and implementation boundaries

- v3.0.0 continues supporting legacy software pins; their removal is planned
  for v4, per the user's clarified release decision.
- Every factual release note must match existing master code or documentation.
- The runtime requirement is Ruby >= 3.3.0, already declared by master.
- No feature implementation, consumer configuration update, migration execution
  or deployment. Dependency updates stay within declared manifest constraints
  and Ruby >= 3.3.0; resolve on Ruby 3.3. Regenerate gemset with Bundix.
- Changelog, source version, Bundler path dependency and Nix gemset version agree.
- Final history: dependency update, release instructions, then one release unit
  for changelog/version identifiers. Final branch tip is `Version 3.0.0`.
- Generated manpages and `pkg/` outputs remain ignored local artifacts.

## Compatibility

Document flakes as the new default for `confctl init`, with `--swpins` retaining
the legacy workflow. Link the existing swpins-to-flakes migration guide and
input-management guide. Call out the raised Ruby requirement and operators'
upgrade choice. Existing generation metadata remains readable; this preparation
does not change its format. The dependency refresh updates installed vpsAdmin
and HaveAPI clients; inspect their requirements and the existing confctl caller
contracts. No database/schema migration, API server, Terraform provider or
protocol implementation is changed in this branch. The existing swpins-to-flakes
helper is already in master and changes a configuration repository only when
explicitly invoked. No coordinated fleet update is required by release edits.

## Deployment and recovery

Wait for user approval after review and local package verification. The pending
release consists of integrating this branch into confctl master, creating and
pushing v3.0.0, and publishing the verified gem to RubyGems. Do not invoke the
Bundler release task during preparation because it tags and pushes. Retain the
exact local artifact and checksum for approval. Before publication recovery is
editing the feature branch and rebuilding. A published gem version cannot be
overwritten; investigate partial release results before taking further action.

## Acceptance criteria

- Complete, concise changelog covering material operator-visible changes since
  v2.2.3; software pin removal-in-v4 notice appears near the start.
- Version metadata identifies v3.0.0 consistently in source, lock and gem.
- Nix's path-gem metadata also identifies confctl as v3.0.0.
- Release commit is clean and independently reviewed as a whole branch.
- RSpec, RuboCop and applicable format checks pass in the project environment.
- Built gem includes release text, runtime files and generated manpages, and
  excludes worktree metadata, local dependencies, caches and release evidence.
- No release integration, tag or RubyGems upload before approval.

## Verification brief

Quick: factual changelog comparison, `git diff --check`, Ruby syntax, gemspec
version/runtime requirement and declared Overcommit checks. Revised final review
uses general, architecture/repetition, scope/proportionality and
risk/compatibility lanes at high risk because dependencies and publication
instructions are included. It explicitly covers complete branch history and
absence of schema migrations.
Longer checks after final review: `bundle exec rspec`, `bundle exec rubocop`,
`nixfmt --check` on tracked Nix files, `bundle exec rake md2man:man build` and
package inventory/CLI smoke checks. Use fresh utility watchers for uncertain
duration runs. Infrastructure integration tests add little evidence for this
release-only diff and are outside the selected checks.

Expanded verification: check refreshed dependencies on Ruby 3.3; evaluate and
build the actual flake confctl package and verify its bundled path-gem version.
Validate the release skill with skill-creator's quick validator. Run independent
final review again on the completed revised series because dependency changes
and reusable publication instructions expand the reviewed scope. Release
instructions cover approval boundaries, exact artifact/source provenance,
Bundix generation, release-last ordering and partial publication recovery.
