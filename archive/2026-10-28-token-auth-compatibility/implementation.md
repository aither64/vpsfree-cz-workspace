# HaveAPI implementation package

Owner: implementer0. Scope: narrow Go token-auth documentation compatibility
fix and regressions, followed by the dependent 0.31 backport and separate patch
metadata. Lead owns integration, independent review coordination and publication.

Current result: lead confirmed source and release-branch integration after
independent review. Final release source is
`819bba5110e089465535ecd71ca2eb37a7d39caa`. Bounded observation confirms the
tagged release build passed and its artifact is available; protected `release`
approval is pending. The related release-branch build-only run passed. Lead
retains all Git and protected publication/approval coordination.

## Preparation

- `dev-session current` and both environment markers match
  `2026-10-28-token-auth-compatibility` in
  `/home/aither/workspace/ai/vpsfree.cz`.
- Initial substantive workspace plan/state/portal commit confirmed by lead:
  `4cb9ebb37`.
- Assigned HaveAPI worktree is clean on
  `2026-10-28-token-auth-compatibility` at initial base
  `2fc2b8f86c71a6062434bb60a24e174b20c1a520`. Existing portal registration
  names the same branch/base. Remote: `git@github.com:vpsfreecz/haveapi.git`.
- Read workspace and HaveAPI instructions, routed development/release guidance,
  relevant Go profile documentation, and the documentation/monitoring skills.
- Inspected `.overcommit.yml`, both `.git-hooks/pre_commit` custom hooks and the
  active Overcommit hook entry points. Top-level Nix dependency preparation
  passed in 215 seconds under a fresh catalog-matched Luna/low utility watcher:
  `nix develop -c bash -c 'bundle check && BUNDLE_GEMFILE="$PWD/servers/ruby/Gemfile" bundle install && make doc'`.
  Log: `environment-prepare.log`.
- Installed Overcommit and signed the inspected configuration/custom hooks in
  the top-level Nix shell. No hooks were bypassed.
- Architect-owned `design.md` read; lead accepted the brief before source edits.

## Diagnosis and verification targets

`Documentation#render_auth` compares token transport values strictly while the
automatic server profile uses `StructuralSchema.copy`, whose JSON round trip
turns Symbol scalar names into Strings. The existing Go mounted-profile check
already crosses that boundary without a listener/compiler and can carry the
regression alongside focused adapter specs.

The fix adds one local, protected String/Symbol comparator for the token header
and query-name checks. Both values must have a supported type and identical
string values; provider/descriptor presence remains mandatory. Basic/OAuth2,
shared copying, token configuration, runtime authentication and generated SDKs
are unchanged. Tests cover four supported type combinations, independent
header/query drift, unsupported nil/boolean/numeric coercion, missing saved/live
providers and missing auth descriptor. The existing mounted fixture now enables
a real default token provider; the check asserts saved String/live Symbol values
and emitted environment-token code after automatic mount finalization.

The nearby source comment and regression checks explain the local invariant.
A separate technical document would repeat that explanation; none was added.
No schema, migration, persisted state, protocol or deployment change exists.

## Focused evidence

Commands ran in top-level `nix develop` with
`HAVEAPI_RELEASE_TOOLS_ONLY=1` after preparation:

```sh
BUNDLE_GEMFILE="$PWD/servers/ruby/Gemfile" bundle exec ruby \
  -Iclients/ruby/lib -Iclients/go/lib -S rspec \
  clients/go/spec/unit/documentation_spec.rb
(cd servers/ruby && bundle exec ruby \
  -I../../clients/ruby/lib -I../../clients/go/lib \
  ../../clients/go/spec/documentation_profile_check.rb)
bundle exec rubocop clients/go/lib/haveapi/go_client/documentation.rb \
  clients/go/spec/unit/documentation_spec.rb \
  clients/go/spec/documentation_profile_check.rb \
  clients/go/spec/support/documentation_profile_fixture.rb
git diff --check
```

- Before the source fix: 77 examples, 8 failures; mixed String/Symbol names
  were rejected and equal unsupported scalars were accepted. Mounted check
  failed with the reported SDK mismatch after proving the JSON/live boundary.
  Logs: `go-unit-red.log`, `go-profile-red.log`.
- After the fix: 77 examples, 0 failures; mounted check passed all existing
  current/legacy/profile/authorization assertions plus the token regression.
  Log: `go-quick-green.log`.
- Initial lint found one argument alignment issue, corrected without logical
  changes. Final lint: four files, zero offenses; diff whitespace check passed.
  Log: `go-lint-green.log`.
- Final commit hooks: HaveapiI18n, RuboCop and all commit-message checks passed.
  No warnings on the final commit. The first unpublished commit was amended
  only to wrap its body to Overcommit's 72-column preference; source trees
  compare identical with `git diff --exit-code`.
- An initial push outside Nix was refused by Overcommit's environment-dependent
  configuration signature. The remote branch was absent afterward. Repeating
  the push inside the required top-level Nix shell passed without resigning or
  bypassing hooks. Git operations with these hooks must use the same Nix shell.

## Published source and review handoff

Base: `2fc2b8f86c71a6062434bb60a24e174b20c1a520` (fresh `origin/master`).
Final feature head: `2f5156262baaf137800c17a9321e617c2b5df1d5`.
Remote SSH `ls-remote` confirms that exact head on
`refs/heads/2026-10-28-token-auth-compatibility`. Worktree is clean.

Complete base-to-head history: one commit,
`clients/go: match String and Symbol token transport names`.
Diff: four scoped Ruby files, 73 additions and one deletion. No obsolete
approach, transitional compatibility path, dependency update or migration.
No migrations were merged, released, deployed or externally consumed.
Temporary unpushed head `26dbf899ef13cb721d2a050b92caa2f0ad643373` has the exact
same tree; only message wrapping differs. Reviewer must bind the final report
to published `2f5156262baaf137800c17a9321e617c2b5df1d5`.

Independent review and broader verification were pending at the source handoff.
Lead subsequently confirmed master integration; the dependent release package
is recorded below. Source implementer performed no shared-branch integration.

Post-review recommendation: reuse pushed-head CI instead of duplicating the
Go suite or performance campaign. Current run IDs for the exact final head:

- `40658113520`: RuboCop.
- `40658113525`: servers/ruby performance (includes current-client contract).
- `40658113568`: clients/go RSpec (Ruby 3.2/3.3/3.4, full Go unit/integration).
- `40658113538`: i18n health, already successful at handoff.

One fresh watcher can observe these exact runs after independent review and run
this additional server-side adapter/profile batch once:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -c '
  cd servers/ruby && bundle exec rspec \
    spec/client_examples/go_spec.rb \
    spec/client_examples/profiles_spec.rb \
    spec/client_examples/profile_mount_spec.rb
'
```

Use `gh run watch RUN_ID --repo vpsfreecz/haveapi --exit-status` for each retained
run, without relaunches. No full local suite, compiler acceptance harness or
extra performance campaign is needed if these required CI runs succeed. Parent
lead diagnoses any failure before retry. Backport/release metadata remains a
separate milestone after master integration.

Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-token-auth-compatibility/

## 0.31 backport and patch preparation

Lead confirmed master integration at
`2f5156262baaf137800c17a9321e617c2b5df1d5` before assigning this milestone.
Fresh SSH refs confirm `haveapi-0.31` is
`d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42`, equal to peeled `v0.31.1`,
with no `v0.31.2` tag. New checkout and registration:
`worktrees/2026-10-28-token-auth-compatibility/haveapi-0-31`, feature branch
`2026-10-28-token-auth-compatibility-0.31`, exact initial base above.
Lead set registration `default_branch: haveapi-0.31`; clean checkout verified.
Read release checkout AGENTS and routed development/releases procedures, and
inspected its Overcommit configuration/custom hooks.

Runtime setup lesson: run `dev-session` outside HaveAPI's Nix shell. The runtime
wraps Ruby 3.4.9, while HaveAPI's shell supplies Ruby 3.4.11 and its native gems;
inheriting component `GEM_HOME` makes runtime JSON loading fail before mutation
with a GLIBC/native-extension mismatch. Normal runtime invocation avoids this.
Hooked project Git operations run inside the project's top-level Nix shell.
The runtime refuses dots in worktree names, so use `haveapi-0-31` for the local
name while retaining `haveapi-0.31` as target and `.0.31` in the feature branch.
Creation's post-checkout hook reported the known signature mismatch after the
checkout and registration succeeded; preserve them and sign inspected hooks
inside Nix rather than recreating the worktree.

A fresh Luna/low watcher completed this top-level Nix preparation at the exact
release base in approximately 154 seconds:

```sh
nix develop -c bash -c \
  'make release-deps && make doc && ruby utils/release/cli.rb check-inputs'
```

`release-deps.log` ends with `Prepared release inputs valid: 0.31.1`.
Installed and signed inspected hooks inside Nix, with no bypass. Applied
`git cherry-pick --no-commit -x 2f5156262baaf137800c17a9321e617c2b5df1d5`,
copied Git's generated backport message to a temporary file, and committed
with `git commit -F` after focused checks so the ordinary hooks ran.
Source commit: `5a016f080bf39c184f71f6b15f904fc165448d6f`; message retains
the exact master cherry-pick trailer. Lead's `range-diff` acceptance confirms
identical source patch apart from that required trailer.

Backport source checks passed: 77 unit examples, mounted standalone regression,
four-file RuboCop and diff whitespace check; all commit hooks passed.
Log: `backport-quick-commit.log`. Used the same focused commands recorded above
from the release worktree. No source differences from the reviewed master fix.

Immediately before versioning, SSH refs again confirmed unchanged `d49cfa3f`
target and absent `v0.31.2`. Ran `make version VERSION=0.31.2` and
`make release-check` in top-level Nix. Both native metadata and prepared-input
checks passed for 0.31.2 (`release-version-check.log`).

Metadata commit: `819bba5110e089465535ecd71ca2eb37a7d39caa`,
`release: prepare HaveAPI 0.31.2`. Its 18 paths contain the approved seven-line
changelog addition and 17 generated version-only changes, including the tracked
JavaScript bundle's version. Every generated path was compared with the prior
commit: its only change is `0.31.1` to `0.31.2`. The changelog heading and text
were supplied and accepted by the lead under main-agent writing skills.

Ten prepared lock texts were retained before versioning under
`/tmp/token-auth-031-locks-before`. Compared complete lock contents after
versioning, allowing only this checkout's HaveAPI package identities to change:
npm root/package version fields, the editable Python package version, and Ruby
HaveAPI local version/dependency lines. All external dependencies and other
content match. `release-lock-comparison.log` records each final lock SHA-256.
Library locks remain ignored/local; none were added to Git.

Metadata quick checks passed: changed Ruby metadata lint (ten files), real
mounted check under version 0.31.2 and diff whitespace. Log:
`release-metadata-quick.log`. Metadata commit hooks passed HaveapiI18n,
PythonChecks, PhpCsFixer, RuboCop and all message checks, without warnings.
Log: `release-metadata-commit.log`. No further local test batch was run.

Final base/head series for independent review:

1. Base `d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42`.
2. Backport `5a016f080bf39c184f71f6b15f904fc165448d6f`.
3. Metadata/final head `819bba5110e089465535ecd71ca2eb37a7d39caa`.

Full diff: 22 files, 97 additions and 18 deletions. Exactly one source backport
and one conventional shared-version/changelog commit; no obsolete history,
dependency update stream, migrations or new behavior in the metadata commit.
No migration was merged, released, deployed or externally consumed.
Fresh fetch before publication still found the recorded target base. Feature
branch `2026-10-28-token-auth-compatibility-0.31` was pushed over SSH from the
top-level Nix shell. SSH `ls-remote` verified exact
`819bba5110e089465535ecd71ca2eb37a7d39caa` on that feature ref.
Worktree is clean. No shared release-branch merge, tag or package publication
was performed by implementer0.

Long all-component tests/builds remain deferred until final review. The existing
tagged release workflow runs `make release-deps`, i18n health,
`make release-test`, `make release`, `make test`, npm smoke and Python package
smoke before protected publication. Reuse that workflow after lead review and
integration instead of duplicating the all-component build locally. No local
hook failure, source-check failure or unresolved command remains.

CI inventory at release-package handoff, all bound to final `819bba51`:

| Workflow | Run ID | Observed status |
| --- | --- | --- |
| servers/ruby RSpec | 40660354857 | success |
| clients/rust | 40660354816 | in progress |
| servers/ruby performance | 40660354784 | in progress |
| i18n health | 40660354972 | success |
| release (branch push, build only) | 40660354757 | in progress |
| clients/ruby RSpec | 40660354922 | success |
| clients/php PHPUnit | 40660354891 | success |
| RuboCop | 40660354762 | success |
| clients/python | 40660354745 | success |
| clients/js tests | 40660354871 | success |
| clients/go RSpec | 40660354899 | success |

No CI watcher was launched by implementer0 at the feature-package handoff; lead coordinated
post-review observation and avoids duplicate builds. The branch push already
started the repository's build-only release workflow automatically.

## Integrated tagged release build observation

Lead assigned observation after integration: tagged run `40661462796`,
tag `v0.31.2`, and release-branch build-only run `40661462440`, both exact
head `819bba5110e089465535ecd71ca2eb37a7d39caa` in `vpsfreecz/haveapi`.
Session identity reverified. One fresh Luna/low utility uses pinned catalog
`3ff7a2129ed39b4d6774466e53060bbff33d2cd2d893aa168c87cb3d64bd6b41`,
native utility `dw_261a10738ad06c003118fa86a9c9a7ce71a28ba2529d3b2b`,
full-access/never-approval execution policy. This is observation only.

Stop condition: tagged build succeeds, its artifact is available and protected
`release` deployment is pending; observe the related build-only run in the
same batch. Poll job/pending-deployment status approximately every 20–30 seconds.
Expected duration about seven minutes; after 15 minutes escalate phase/status
and retain monitoring ownership. No retries, cancellation, relaunch, Git edits,
publication or approval are authorized. On failed build retain failed logs and
report. Lead inspects artifacts and coordinates protected approval afterward.

Observation completed at the requested boundary after approximately eight
minutes; both runs matched the exact assigned head. Tagged run `40661462796`
completed `Validate, test and build` job `122725246582` with success. Artifact
ID `12804711465`, name `release-40661462796`, is available and not expired.
The authoritative pending-deployments API reports protected environment
`release`, ID `24722193856`; publish job `122728549971` is waiting. Build-only
run `40661462440` completed successfully at the same head, with its publication
job skipped. Full status/job/artifact/pending-environment snapshots are in
`tagged-release-watch.log`.

Watcher stopped without approval, publication, retries, relaunches, cancellation
or Git edits. No monitoring operation remains running. This proves the build
checkpoint only; tagged release publication is pending lead artifact inspection
and protected approval.
