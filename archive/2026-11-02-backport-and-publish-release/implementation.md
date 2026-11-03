# HaveAPI 0.32.2 implementation evidence

Owner: implementer0. Accepted brief: [design.md](design.md).

## Current final result after blocking review correction

Clean frozen head: `1ef9b204ba45bb261d3334be5c555cc1856b713b`, same target base
`9efeadf91d894e01d1d4f4a3e3fc64c6309785c7`. All twelve original source backport hashes are
unchanged. Local documentation correction is now `591a1b6083763e8e7b03edcffd58b4651558056f`;
separate version commit is `1ef9b204ba45bb261d3334be5c555cc1856b713b`.
Focused translated-client sample equality: **1 example, 0 failures**. Refreshed
final-head quick checks all passed; no push/merge/tag/publication or full CI run.
Lead completed independent review, all eleven feature checks, target integration
and annotated tagging. Read-only diagnosis below identifies the automatic target
release run's Nix-cache transfer failure; the tagged build passed that boundary
and remains the lead's monitored publication candidate. No publication approval
or retry was performed by this implementer.
Historical initial completion evidence is retained below and under `.dca492c6`
artifact suffixes; current `final-history.txt`, `final-diffstat.txt`, `final.patch`
and `quick-checks.{json,log}` identify the corrected final head.

## Identity and baseline

`dev-session current` returned `2026-11-02-backport-and-publish-release`; both
DEV_SESSION variables match that slug and `/home/aither/workspace/ai/vpsfree.cz`.
Live roster confirms implementer0 `workspace_write`, Sol/xhigh, catalog
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`.
Initial tracking commit is `2e5bc7f`.

Fresh `git --git-dir=repos/haveapi.git fetch origin` succeeded. Source master:
`f29c1e4675bc1f79641faa619b8c68ecec923c71`; target haveapi-0.32:
`9efeadf91d894e01d1d4f4a3e3fc64c6309785c7`. Owned feature branch:
`2026-11-02-backport-and-publish-release`; worktree:
`worktrees/2026-11-02-backport-and-publish-release/haveapi`.
Lead corrected portal target to `haveapi-0.32` after initial registration.

## Preparation

`dev-session worktree add ... --base origin/haveapi-0.32 --no-fetch` created the
correct branch/worktree but returned failure from the existing Overcommit
post-checkout hook: configuration signature changed. Verified actual worktree
HEAD and branch before further action; no source commit had occurred.
Preparing declared root Nix bundle through a fresh Luna/low utility, then
installing/verifying/signing Overcommit before source commits.

No push, tag, integration or publication is assigned to this implementer.

Root preparation passed: fresh Luna/low utility ran `nix develop -c true` at
base, exit 0 in 63s; log `root-bundle-preparation.log`. Installed and signed
Overcommit using the root Nix bundle; canonical `hooks/pre-commit` is executable.
`overcommit --list` confirms configured I18n, RuboCop, PHP, Python and JS hooks.
Worktree registration retry succeeded without recreating the worktree.

Source commits use `git cherry-pick -x --no-commit SHA`, then copy MERGE_MSG to
a temporary file and `git commit --author=<original> --date=<original> -F FILE`.
This preserves original author/date and provenance while running pre-commit
hooks (ordinary automatic cherry-pick commits need not run those hooks).
First source commit: `661f571b91606ee33c3e6f4bdc7539fd518c48a4` ->
`3d94938ce2b9b6391db54bb7ec7885c43aaa7c02`; no conflicts; I18n/RuboCop passed.
Overcommit text-width warnings are advisory defaults below the workspace's
80-character limit; original source messages are retained.

Before the next source/Python hook, a fresh standalone Luna/low utility launches
`HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c make release-deps`; actual banner
confirms danger-full-access/never. Revision is first backport above; command/log:
`release-deps-preparation.log`, watcher `release-deps-watcher.log` and result.

Found narrowly stale generated-client installation hint in source
`doc/en/client-examples.md:99`: 0.30.2 despite generator README and retained
smoke requiring exact runtime 0.32.0. Context explicitly calls the generated
createClient API and says this is the generator-supported runtime. Reported
evidence to lead before any edit; no broad documentation audit planned.

## Initial deliverable before review

Initial reviewed head: `dca492c680b8d52f1e4c8b51e89cb7a97fc83c38` (superseded below).
Target base: `9efeadf91d894e01d1d4f4a3e3fc64c6309785c7`.
Branch: `2026-11-02-backport-and-publish-release`; target: `haveapi-0.32`.
Source is frozen for the lead-assigned independent review; implementation/fix
ownership remains with implementer0. No push, test suite, CI, integration,
tagging, publication, deployment or session lifecycle action was performed.

All twelve accepted source commits applied without textual or semantic
conflicts, preserving original author/date and `-x` provenance. All normal
pre-commit hooks passed. [Complete mapping](source-backport-mapping.md) records
source/backport hashes and identical stable patch IDs for all twelve pairs.
[Range comparison](source-range-diff.txt) shows only added provenance trailers.
Before the local correction/version commit, the complete tree differed from
source master only in the 17 existing release-version metadata files.

The two additional focused commits are:

- `83fc752dc92589d9e968b3d1bb42391404671ba0`: approved one-line generated-client
  runtime installation correction in `doc/en/client-examples.md` (0.30.2 to
  exact supported 0.32.0). Source context names `createClient` and explicitly
  claims the generator-supported runtime; generator README and retained smoke
  require 0.32.0. Lead approved this bounded correction and applied writing
  policy to the explicit version pin. No other documentation audit or fix.
- `dca492c680b8d52f1e4c8b51e89cb7a97fc83c38`: focused 0.32.2 metadata and
  changelog commit. `HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c make version
  VERSION=0.32.2` passed. The independent generator runtime remains 0.32.0.
  Lead authored/style-reviewed the factual release-note candidate and accepted
  the final prepended 32-line CHANGELOG section before this commit.

Metadata staging returned an ignored-directory warning for the already tracked
`clients/js/dist/haveapi-client.js` after staging all 18 intended files.
Inspected index and worktree effects: only the expected metadata/changelog
paths were staged, including the existing browser-bundle version string.
Then invoked ordinary `git commit -F /tmp/haveapi-release-message.txt` on that
verified index. No ignored build output or library lock was added, no hooks
were bypassed, and no force-add was needed.

## Dependency and history inventory

`make release-deps` completed through a fresh standalone exact Luna/low utility,
exit 0 in 129 seconds; actual banner verified danger-full-access/never. See
[watcher result](release-deps-watcher-result.md), `release-deps-preparation.log`
and `.status`. No environment repair or retry was needed.

Saved all ten prepared lock texts/hashes before and after versioning in
`dependency-locks-before-version.json` and `dependency-locks-after-version.json`.
Six are byte-identical. Rust/TypeScript locks change only local HaveAPI package
versions/requirements, npm changes only its two local version identities plus
specified formatting, and uv changes only its editable local package version.
Parsed npm object equality after reverting the two local identities, exact
allowed Ruby-lock substitutions and exact uv-local substitution establish that
all external dependency records are unchanged. These locks remain ignored.

Complete base-to-head series: [final-history.txt](final-history.txt), 14 commits.
Final tree: [diffstat](final-diffstat.txt) and full binary/full-index `final.patch`.
Total: 150 files changed, 7,551 insertions and 1,111 deletions, including locale
catalogs, article moves/Czech articles and source tests already in source master.
The twelve source commits (including upstream follow-ups) are retained because
already integrated source history and the release procedure require exact
backport provenance. No newly introduced repair or superseded approach remains.
One coordinated metadata stream selects 0.32.2; no repeated dependency/channel
pin updates or intermediate generated-artifact update stream were introduced.

**No migrations.** The complete changed-path inventory contains no database
migration or seed. Changes introduce no persisted schema/on-disk state or node
protocol transition, as verified against the accepted design and final diff.
No migration version was merged, released, deployed or externally consumed by
this branch. The branch has no deployment or externally consumed state boundary.
Prior 0.32.1 metadata belongs to the already released base and was not rewritten.

## Initial quick checks at dca492c6

All commands below ran at final head in the top-level repository Nix shell via
`HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c python3 /tmp/haveapi-quick-checks.py`.
The temporary runner only sequences existing commands and records their actual
exit status/duration. It creates no source changes or new test harness.
Initial output retained as `quick-checks.log.dca492c6`; initial exact evidence:
[quick-checks.json.dca492c6](quick-checks.json.dca492c6).

| Command | Seconds | Exit |
| --- | ---: | ---: |
| `git diff --check 9efeadf91d894e01d1d4f4a3e3fc64c6309785c7 HEAD` | 0.072 | 0 |
| `bundle exec rake i18n:health` | 0.709 | 0 |
| `ruby utils/release/cli.rb check-clean` | 0.405 | 0 |
| `make release-check` | 0.974 | 0 |
| `make check-format` | 15.331 | 0 |
| `bash -n utils/copydoc.sh utils/release/build.sh` | 0.01 | 0 |
| `node --check clients/typescript/spec/documentation/wire.mjs` | 0.103 | 0 |
| `node --check clients/typescript/spec/typescript/actual_runtime_wire.mjs` | 0.104 | 0 |
| `node --check clients/typescript/spec/typescript/runtime_spy.mjs` | 0.099 | 0 |
| `node --check servers/ruby/lib/haveapi/public/js/documentation.js` | 0.089 | 0 |
| `node --check servers/ruby/spec/client_examples/assets/documentation_test.cjs` | 0.103 | 0 |

Metadata commit also passed PythonChecks, HaveapiI18n, PhpCsFixer, JsFormat and
RuboCop hooks. All commit messages retain the <=80-column workspace contract;
Overcommit's stricter default 72-column text checks gave advisory warnings only.
Final `git status --porcelain` is empty after verification. No long integration
checks have run; the lead owns the required exact-head workflow after review.

## Documentation and compatibility handoff

Checked/retained owning project explanations include
`doc/agent-instructions/{development,releases,documentation,localization}.md`,
`doc/en/{client-examples,performance,documentation-ui}.md` and the TypeScript
generator README. Source backports carry the localized articles, renderer
extension contract and TypeScript describe/receipt compatibility guidance.
CHANGELOG describes the generation boundary and supported runtime explicitly.
Session-specific source mapping, commands and publication status stay here.
No extra project documentation was needed beyond the accepted backports and
one-line runtime correction.

Users with existing generated clients retain their matching runtime pairs;
new generator output requires exact runtime 0.32.0, reserves root `describe`
and emitted helper/type names, validates explicit help selectors/placeholders,
and raises local `ClientInputError` as a `TypeError` subtype before dispatch.
Transport failures and raw envelopes stay intact. No fleet ordering or data
rollback is required; package rollback preserves prior client/runtime pairs.
Publication is not yet performed, and exact artifacts/full checks remain pending
with the lead. Partial-publication recovery retains the existing release
procedure and original artifacts; this implementation adds no recovery helper.

Stable session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-backport-and-publish-release/

## Disposable integration checkout preparation

Prepared only on the lead's subsequent assignment, without a repository claim,
merge, push, tag or feature-source change. Read workspace Git/coordination
procedure and the selected package's `workspace-host coordination guide`.
Selected package:
`/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0`;
coordination catalog:
`sha256:b17a5618c6ce3988022bd02962d4dad95d735568fc4b2717ce462364e41eab6d`.

Fresh `ls-remote` and `fetch origin haveapi-0.32` confirmed unchanged target
`9efeadf91d894e01d1d4f4a3e3fc64c6309785c7`; master still
`f29c1e4675bc1f79641faa619b8c68ecec923c71`. Created detached clean checkout:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-backport-and-publish-release/haveapi-integration`
from `origin/haveapi-0.32` using ordinary `git worktree add --detach` inside the
prepared feature Nix shell. No manifest or lead state was edited.

Reused the existing root gem environment by entering the feature's top-level
Nix shell and running Git with `-C` (or changing to the disposable checkout
inside that same shell). Root Gemfile, flake.nix, flake.lock, .overcommit.yml and
.git-hooks are byte-identical between target base and candidate; no source or
dependency copying/symlinks were needed. `HAVEAPI_RELEASE_TOOLS_ONLY=1` skips
redundant dependency installation; it does not disable Git hooks.

From that exact environment in the target, verified executable post-merge hook,
loaded Overcommit `0.74.0`, and invoked the actual `hooks/post-merge 0` entrypoint:
exit 0, trust/signatures accepted. `overcommit --list` confirms this repository
has no enabled post-merge actions; all standard configured post-merge actions
are disabled by the retained repository configuration. The hook framework
still executes and verifies trust. Target `git status --porcelain` is empty,
HEAD is the exact base, and feature head remains clean at `dca492c6...`.

After final review/CI and explicit held repository claim, the lead's ordinary
merge command, **run with CWD at the prepared feature worktree**, is:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c git \
  -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-backport-and-publish-release/haveapi-integration \
  merge --ff-only 1ef9b204ba45bb261d3334be5c555cc1856b713b
```

This is a prepared command, not executed. Lead must first recheck current remote
target, exact final feature head and target cleanliness inside the short claim,
then inspect post-merge hook results, push HEAD to `refs/heads/haveapi-0.32` over
SSH, verify remote and release the exact claim before CI/records. A moved target
or any hook intervention returns to preparation outside ownership after stopped
commands and reconciled effects. This preparation acquires no repository or
machine reservation and grants no cleanup/session lifecycle authorization.

## Blocking review remediation: English/Czech sample parity

Reviewer identified that the approved installation-pin correction changed only
English. The Czech command at `doc/cs/client-examples.md:95` still selected
0.30.2, violating the existing shared-page noncomment sample equality contract.
Lead directed this exact one-value change and accepted the matching explicit
0.32.0 machine pin under the writing policy. No translated prose changed.

Rewrote only the last two unpublished local commits with interactive rebase
from unchanged source-backport head
`e0f961715a39f5b778c1abe753ec1bcc56327e84`. Both commits were amended using
normal Git hooks and temporary-file commit messages. The documentation commit
now changes the matching command in both languages; version metadata stayed
separate and patch-identical. All twelve source commit objects are unchanged.

Old reviewed range:
`9efeadf91d894e01d1d4f4a3e3fc64c6309785c7..dca492c680b8d52f1e4c8b51e89cb7a97fc83c38`.
New final range:
`9efeadf91d894e01d1d4f4a3e3fc64c6309785c7..1ef9b204ba45bb261d3334be5c555cc1856b713b`.
[Range diff](review-fix-range-diff.txt) shows the single Czech correction in the
local documentation commit and an `=` metadata commit. The old/new complete
final trees differ only by that one runtime token:
[exact narrow diff](review-fix-narrow.diff). This is the directly verified
requested correction, not a claim that the whole trees are identical.
No migrations or new compatibility/dependency boundary was introduced.

The first temporary rebase editor counted commented Git help as commands and
refused before changing history. A subsequent amend attempt lacked its expected
temporary message and failed without a commit. Inspected actual HEAD, index and
worktree: original head and clean state were intact. Corrected the editor to
count only command lines, then completed the intended two-commit rewrite with
normal hooks. No reset, cleanup, bypass or source-scope expansion occurred.

At the new final head, in the declared top-level Nix environment:

| Command | Seconds | Exit |
| --- | ---: | ---: |
| `make doc` | 0.533 | 0 |
| `bundle exec rspec spec/documentation/shared_pages_spec.rb --example translates client-examples while preserving its English anchors and noncomment samples` | 2.287 | 0 |

The focused RSpec command ran from `servers/ruby`; output confirms exactly
**1 example, 0 failures**. Logs/status/durations:
`review-fix-translation.log` and [review-fix-translation.json](review-fix-translation.json).
`make doc` created only ignored packaged documentation. Loading the prepared
server bundle refreshed its ignored local server/client identities from .1 to
.2 in `servers/ruby/Gemfile.lock`; exact allowed substitutions prove all
external dependency records stayed unchanged. Other after-version locks are
unchanged.

Repeated final quick checks at `1ef9b204ba45bb261d3334be5c555cc1856b713b`:

| Command | Seconds | Exit |
| --- | ---: | ---: |
| `git diff --check 9efeadf91d894e01d1d4f4a3e3fc64c6309785c7 HEAD` | 0.068 | 0 |
| `bundle exec rake i18n:health` | 0.767 | 0 |
| `ruby utils/release/cli.rb check-clean` | 0.395 | 0 |
| `make release-check` | 0.721 | 0 |
| `make check-format` | 14.881 | 0 |
| `bash -n utils/copydoc.sh utils/release/build.sh` | 0.012 | 0 |
| `node --check clients/typescript/spec/documentation/wire.mjs` | 0.11 | 0 |
| `node --check clients/typescript/spec/typescript/actual_runtime_wire.mjs` | 0.106 | 0 |
| `node --check clients/typescript/spec/typescript/runtime_spy.mjs` | 0.108 | 0 |
| `node --check servers/ruby/lib/haveapi/public/js/documentation.js` | 0.1 | 0 |
| `node --check servers/ruby/spec/client_examples/assets/documentation_test.cjs` | 0.101 | 0 |

[Current quick evidence](quick-checks.json) and `quick-checks.log` supersede the
initial checks only for final-head identity; initial receipts remain retained.
No full integration suite or CI was launched. The disposable integration
checkout remains detached, clean and unchanged at exact target base
`9efeadf91d894e01d1d4f4a3e3fc64c6309785c7`. Its already verified hook inputs
are identical on the corrected candidate; the prepared merge command above now
names the corrected final head. It remains unexecuted.

## Target release CI failure diagnosis (immutable tagged source)

Lead assigned read-only diagnosis after integrating the exact final head and
pushing annotated `v0.32.2`. No source edits, reruns, commits, pushes, tags,
publication approval or claims were performed during diagnosis.

Failed build-only target run:
https://github.com/vpsfreecz/haveapi/actions/runs/41528866548

Run metadata verifies exact source `1ef9b204ba45bb261d3334be5c555cc1856b713b`,
branch `haveapi-0.32`, first push run created 2026-11-02 21:29:54Z and finished
failed at 21:30:55Z. Build job `125563604995` failed in step 4,
**Check source and release metadata**. The Ruby metadata checker did not execute:
`nix develop` failed while realizing the development shell. Tests, package
build, artifact discovery/upload/verification and summary were all skipped;
publication job was skipped. GitHub artifacts API reports **zero artifacts**.

### Exact cause and scope

At 21:30:24Z many `cache.nixos.org` downloads reported connection reset,
broken pipe and OpenSSL EOF/SSL_ERROR_SYSCALL. Specifically, downloading
`/nix/store/fsrw69w5mx838p7xydbdvywhwl6wnbjw-tzdata-2026e` from
`https://cache.nixos.org/nar/1h75anlsky77wbxvz2hprwdma567qw9651bvjn36sqffjm85k7vj.nar.zst`
was interrupted with curl error 55; Nix retried from offset **203920**. That
resumed transfer returned **HTTP 416** at 21:30:24.978Z. The missing tzdata
substitute made dependent gh/Go/Python/Git outputs unavailable and failed
`/nix/store/vqzb10q9hry5xycqk75kf4gjcqy9hpwx-haveapi-env.drv`; process exit 1.
This is a runner-to-cache download/transfer failure before HaveAPI code ran.
Logs do not identify whether the cache/CDN or runner connection caused resets;
no source-code or release-metadata defect is evidenced. No local Linux kernel
build or package upload occurred.

Evidence retained:

- `failed-release-41528866548-logs.zip`: full GitHub run logs, 41,425 bytes;
  SHA-256 `5ac8dda0cf7265e1d749f40a13cfa1300e93dfd48e22b1aa34724e5352d49cd7`.
- `failed-release-41528866548.log`: entire failing-step text;
  `failed-release-41528866548-excerpt.txt`: exact relevant lines.
- [failed run/job state](failed-release-41528866548.json) and
  [zero-artifact state](failed-release-41528866548-artifacts.json).

Same-source feature release run
https://github.com/vpsfreecz/haveapi/actions/runs/41527342376
passed. Its existing unexpired artifact `13180298796`,
`release-41527342376`, is retained untouched; archive digest
`sha256:83ab290d63979948514d1d111a3a218d8dce0d5720025220d42546e4eb2d3330`,
size 1,317,331 bytes. Exact run and artifact API receipts are
`feature-release-41527342376.json` and
`feature-release-artifact-13180298796.json`.

The single diagnostic snapshot of tagged run
https://github.com/vpsfreecz/haveapi/actions/runs/41529223599
shows the same source already passed metadata, publication setup and artifact
discovery, and reached **Test and build maintained packages**. Thus the tagged
run has passed the exact shell-realization boundary that failed on the target
run. Snapshot: `tagged-release-41529223599-initial.json`. This is diagnostic
stage evidence, not a completed tagged-run result or publication approval.
No second watcher or ongoing CI monitor was launched by this implementer.

### Shortest safe recovery and retry conditions

Let the existing tagged run continue under the lead's fresh monitor; no source
change or retry is presently indicated for it. A green tagged build must retain
and verify that run's original artifacts before protected publication review.
Preserve the annotated tag, original source and all accepted artifacts.

If the lead needs to clear the failed build-only target run, one authorized
**Re-run failed jobs** of original run `41528866548` is supported after diagnosis
because it failed before any artifact upload or publication and the same-source
tagged run has demonstrated successful shell realization. A fresh hosted runner
can redownload the unchanged closure. This is not permission to blindly repeat:
if the same transfer failure recurs, retain the new attempt's errors and diagnose
the cache/network path before another attempt. Do not change Nix pins, add
fallback source builds or create retry infrastructure for this isolated failure.
Lead owns any actual rerun; none was initiated here.

`utils/release/workflow.rb` binds artifact discovery to its own GITHUB_RUN_ID.
The existing feature artifact is independent evidence and must not be substituted
into the tagged run. The existing helper permits an early build retry when no
prior upload succeeded; after a successful upload, reruns must reuse the exact
original run artifact and refuse missing/expired bytes. If the tagged build
fails before upload due solely to a diagnosed transfer issue, retry that original
run only after the lead's decision. If it has uploaded artifacts, preserve/reuse
them. Any source defect requiring code changes follows the immutable-tag release
procedure: no edits or retagging of 0.32.2; lead decides the subsequent patch
release with appropriate authorization. No such source defect was found here.

Fresh SSH remote evidence `diagnosis-release-remote-refs.txt` confirms target head
`1ef9b204ba45bb261d3334be5c555cc1856b713b`, annotated tag object
`7f8f656ca7655bafaf2cf5e7095573806085a442` and its peel to that same final head.
The implementation worktree remains clean at the immutable source.
