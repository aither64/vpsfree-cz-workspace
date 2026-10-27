# Final release preparation review

User requests coordinated release of every maintained HaveAPI component as
0.31.0 and preparation/instructions for manual vpsadmin-typescript-client
publication. User explicitly chose MIT and SDK 0.1.0; pending RubyGems TS publisher
is user-confirmed saved. No default-branch integration is approved. No optional
new generator behavior, dependency upgrade, regeneration or workflow redesign.

## Review assignment

Mandatory final review, lanes **general, scope/proportionality, risk/compatibility**.
Overall risk high: persistent multi-registry publication and PHP mirror default
synchronization, plus first public npm release/license. No implementation logic or
workflow changed; architecture lane unnecessary for these metadata/docs edits.
Retained independent reviewer0: gpt-6.1-sol/xhigh, read_only; no overrides.
Read mandatory-change-review skill and each selected reference in full. Inspect
actual complete series/diffs and repository instructions directly. No nested
agents. Report findings and explicit whole-history/migration/update-stream
conclusions to lead; save final-review.md in this session. Do not edit source.

## Exact completed committed ranges

HaveAPI worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-prepare-client-releases/haveapi
Canonical: git@github.com:vpsfreecz/haveapi.git, release branch haveapi-0.31,
remote default master. Base 4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c.
Head 3bbb98e76e286d64707c368fe1c2cc4d03f35eed.
Complete series (one commit): 3bbb98e7 release: prepare HaveAPI 0.31.0.
18 files +94/-17: prescribed coordinated make version output plus changelog.
Tracked JS bundle changes only its prescribed version line. Ignored library
locks not staged; all external dependency records preserved. Historical 0.30.1
and 0.30.2 changelog entries restored exactly from published v0.30.2; new 0.31
claims based on released-tree comparison because cherry-picked fixes overcount
in commit-list comparison. Existing release guides already describe five-gem and
all-component packaging; no lasting guide update needed. See haveapi-preparation.md.

SDK worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-prepare-client-releases/vpsadmin-typescript-client
Canonical: git@github.com:vpsfreecz/vpsadmin-typescript-client.git, branch
2026-10-27-prepare-client-releases, default main.
Base 149c72f11acef67224a47ed77711a3abb805fbd4.
Head 38a25ad88d0bf3018670184620cf69cdb71e92e7.
Complete series (one commit): 38a25ad8 Prepare the first public npm release as 0.1.0.
7 files +81/-18: package/root lock version/public/MIT, standard LICENSE,
README installation/license, docs/development/releasing current state/manual
first upload. Only tools/generator.json change is tooling package-lock digest.
No checker/files-list/workflow changes. Main-agent editorial pass applied.
Runtime peer/dev remains exact haveapi-client 0.30.2; generator revision remains
18b45aeddd0c28c8ddf6c5ea81f9611d6e3a7875, API 7.0/protocol 2.0 snapshot and generated
sources unchanged. Check package provenance/lock binding and preserved inputs.

Both series have one logical release commit, no superseded approaches or repeated
dependency/channel/generated update streams. No migrations in either range;
none merged/released/deployed/externally consumed. No infrastructure rollout.
Assess these conclusions independently, including no obsolete history.

## Acceptance and documentation

All maintained HaveAPI components version 0.31.0: five gems (server, Ruby client,
Go/Rust/TS generators), npm/browser, Python, PHP/Composer. Elixir excluded by
project procedure. Correct shared Ruby dependencies and all-destination workflow
remain essential. SDK artifact public 0.1.0/MIT and exact existing runtime/schema
contracts, with retained immutable archive and clear manual user commands.

Session plan.md/state.md/design.md contain scope, ownership and setup inspection.
Read docs/releasing.md in SDK and doc/agent-instructions/releases.md in HaveAPI.
manual-publication.md is the operation receipt/instruction draft; immutable
artifact evidence will fill remaining fields after review, with no source edits.
Owning project release instructions are committed. Do not treat planned actions
as executed. No registry credentials in records.

## Quick verification and available evidence

HaveAPI: top Nix make release-deps passed 177s; make version and release-check
passed, all required Overcommit checks passed; make release-test passed 24s,
213 Ruby examples/0 failures and six Python tests OK. Clean/diff-check passed.
Logs and ten before-version local locks under this session; see preparation.md.
Full HaveAPI long batch has not started; feature push held pending review.

SDK: pinned Nix npm ci passed; metadata/lock/external dependency/pin identity
assertions and unchanged src/schema/workflow/toolchain assertions passed;
all six test/release.test.mjs cases passed; diff-check and clean checkout passed.
No repository AGENTS or hook framework declared. Source docs committed.

SDK feature push completed just before lead hold-push correction arrived and
triggered canonical Actions batch 40550139596, SUCCESS at exact head. This
sequencing deviation is recorded; no duplicate full run. Tests: offline
regeneration, build, typechecks, ten tests and recursive archive consumer checks.
Immutable Actions artifact 12755255825 downloaded into sdk-0.1.0/, containing
original tarball and receipt. Archive ZIP digest matches GitHub metadata.
Inspect actual payload/receipt as useful, without re-running full tests.

## Publication boundaries and recovery

HaveAPI setup API-verified: release enabled, environment required reviewer
(aither64), v* tag policy, PHP secret NAME present. Other registry account-level
publisher settings uninspected; recent successful 0.30.2 is supporting history.
User-created pending TS publisher uses vpsfreecz/haveapi release.yml, release env.
PHP mirror master at a02dd2506209f54ea782fbd949243207bf9f93bc, equal v0.30.2 and
Packagist source; no intervening untagged commits. Its master sync requires named
integration approval before protected publication. No tag/publish yet.
SDK NPM_RELEASE_ENABLED absent; keep disabled. User uploads exact retained tarball
with npm login and npm publish FILE --ignore-scripts --access public --registry
https://registry.npmjs.org; no --provenance on local manual publication.
Compare registry dist.integrity to retained receipt; uncertain success requires
reconciliation, never blind retry, overwrite, repack or moved tags.

Review scope/proportionality first; do not expand this release into a generator,
workflow or operational-framework project. Important/Blocking findings need
concrete evidence and the smallest correction within this boundary.
