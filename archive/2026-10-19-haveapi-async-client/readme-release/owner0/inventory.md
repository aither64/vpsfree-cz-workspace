# Release-check correction: owner0 inventory

Committed source: `3a79c8ec0863de22823ab5f2031a6e845f612afb`.
Tree: `f7027fd44116e32c1d5cacb39950874925bc95fe`.
Parent: `f94e65e35166a0bf8048a27c9d57c7d36957d65b`.
Both author and committer: Jakub Skokan <jakub.skokan@havefun.cz>.

Exact four owned paths: Makefile, utils/release/artifacts.rb,
utils/release/spec/release_spec.rb and utils/release/npm-consumer.ts.
Delta: 221 additions, 11 deletions. [Code diff](code.diff).

The version target updates both lock root versions. The disposable-copy regression
checks all nested dependency identities and their complete byte suffix unchanged,
accepts the new shared metadata, then rejects a deliberately stale lock root.
No actual VERSION, package.json, package-lock, client source, emitted runtime or
emitted declarations changed in this commit. release-deps now uses npm ci.

Archive inspection retains identity, bundle/version and PHP/Ruby checks, adding
exact main/types paths, nonempty declaration files and required README, both
async guides and LICENSE.txt. The installed smoke tests CJS package-name loading,
CallbackClient/Client identity, version and both client constructors. It compiles
a package-name consumer with pinned TypeScript and checks every resolved input
against the isolated installed declarations, consumer and compiler standard libs.
The quick negative tests use the real compiler to reject missing transitive
and outside-package declarations; npm install alone is stubbed in these fixtures.
Actual smoke uses ordinary npm install --ignore-scripts --no-audit --no-fund of
the retained archive, in a fresh private npm consumer, with NODE_PATH unset.
Publisher, workflow, manifest, artifact reuse and approval contracts are unchanged.

## Quick verification and hooks

Normal top-level nix develop, final exit 0:

- Ruby syntax: both changed Ruby files PASS.
- Scoped RuboCop: 2 files, no offenses.
- make release-test: 49 examples, 0 failures, 8.6 seconds.
- make release-check: metadata valid 0.29.0.
- git diff --check PASS.
- Normal pre-commit HaveapiI18n and RuboCop OK; commit-msg passed with
  nonblocking >72-column TextWidth warnings (all message lines <=80).
  Ambient missing Ruby native-extension warnings were also present.

Raw evidence directory:
`/tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/release-update/`.
Final checks: quick-final.log + quick-final.exit (0).
Normal commit: commit.log + commit.exit (0); staged-paths.txt is exact scope.
Initial quicks passed 49 tests but lint found style offenses; quick-1.log and
quick-2.log retain that diagnosis/correction history.

Index was empty after commit. Only owner1's three expected docs remained
unstaged; Git slot released immediately to owner1. Their later documentation
commit is a separate final review input, not part of this source receipt.

## Complete branch and compatibility

[Ordered complete seven-commit series](series.txt) from base
`c58704a08451a231fdf6c6123437133422af46dc` through the exact source head above.
Complete final diff is reproducible with git diff of these exact refs.
The prior six reviewed commits and historical package identities are preserved.
There are no migrations, database/state changes, new pins or repeated dependency
updates in this release correction. The generated JS/declaration update stream
is unchanged from f94; prior complete-history conclusions remain attributed to
the original reviews, with final expanded branch review still pending.
The WebUI exact f94 archive remains an unchanged historical dependency.

## Postreview proof, prepared only

After owner1 docs commit and final independent review, one fresh utility may
build/pack the exact final clean source using the existing locked client tools,
retain the final npm tar plus identical standalone JS in an owned absolute OUT,
and call the actual Artifacts.smoke_npm helper. No full release build, server,
WebUI or registry operation is needed. Runtime/declaration bytes are expected to
match f94; README archive bytes will change and must be reconciled honestly.
No pack or real installed-tar smoke has run for this correction yet.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-haveapi-async-client/
