# 2026-10-07-prepare-confctl-release-changelog

## Goal

I'd like to release confctl v3.0.0, so please prepare the change log and release commit, then wait for my approval. We will also push it to rubygems when done. This will be the last version with support for software pins, that must be mentioned in the change log.

## Affected repositories

- `confctl`: prepare a release branch from current `origin/master` in
  `worktrees/2026-10-07-prepare-confctl-release-changelog/confctl`.
- Coordination workspace: this session's tracking and review evidence only.

## Approach

Inspect all changes since v2.2.3 and their current documentation. Refresh all
locked dependencies within the existing manifest constraints using Ruby 3.3,
then regenerate the Bundix-managed gemset. Add a repository release skill and
AGENTS.md route. Commit dependency refresh and release instructions before the
final v3.0.0 changelog/version commit, which must be the branch tip.
Run quick release checks and the retained reviewer's independent final review,
then package and verify the gem locally. Wait for user approval before release
integration, tagging, or RubyGems publication.

## Decisions

- Per the user's clarification, say that software pins remain supported in
  v3.0.0 and will be removed in v4. Link the existing flake migration guide.
- Lead owns investigation and edits. Retained `reviewer0` remains read-only and
  uses its saved Astra/xhigh settings for final review.
- User additionally requests refreshing Gemfile.lock dependencies, regenerating
  gemset.nix through Bundix, keeping the release commit last, and recording the
  future release procedure as a skill.
- No code features, configuration pin changes, PR, default
  branch integration, release tag, or RubyGems upload in this preparation step.
- Publish the development branch under the normal workspace Git procedure.

## Compatibility and deployment

Document existing changes since v2.2.3, including runtime requirements and any
configuration upgrade requirements. Dependency updates must retain the declared
Ruby >= 3.3.0 and gem constraints; resolve on Ruby 3.3 and verify with that runtime
as well as the normal development environment and Nix package. The release edits change no
persisted state, database schema, protocol, or deployment behavior. Software
pins remain supported in v3.0.0. Configuration consumers are not updated here.
After approval, integrate into confctl master, tag the approved release and
publish the exact verified gem. RubyGems publication is deferred and cannot be
treated as reversible; a publication problem must be investigated before retry.

## Documentation

Public audience: confctl operators upgrading from v2.2.3 and maintainers preparing
future versions. Keep the release skill in `skills/confctl-release/SKILL.md`
and link it from repository AGENTS.md. Keep release guidance
in `confctl/CHANGELOG.md`, following existing format. Keep this release's exact
revisions, artifact verification, review and prepared publication steps in this
session. Read README and relevant input/build/deployment guides for accuracy.

## Testing plan

Quick checks: diff whitespace, version and gemspec consistency, changelog
coverage, Ruby syntax, and declared Git hooks. After final committed review,
use a fresh utility watcher for the repository's RSpec/RuboCop checks and gem
build; inspect the package contents and CLI version. No infrastructure deploy
or long cluster integration test is needed for release text and metadata.
