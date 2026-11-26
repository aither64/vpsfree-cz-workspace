# I2 vpsAdmin source and PHP backup cleanup evidence

## Integration target hook readiness: passed in declared shell

Root's default push outside the declared shell was refused without a remote
update. Bounded inspection of the existing clean integration target confirmed
head 99207a8dcd92f5907c52dbc99af52b30aa7ecac1, tree
3f3cd9a11eec7d8694bc6c1777adf708239a56c3. Committed .overcommit.yml and all four
custom hooks match their trusted source; no local configuration override exists.
Ambient Ruby loads Overcommit 0.71.0, which looks for the legacy Git-config
signature key. The declared Nix shell loads repository Overcommit 0.76.0, which
uses the retained signature-history store. Its existing configuration signature
is present and verified with verification enabled. No signing, reinstall or trust
bypass is required or was performed.

Bundle check and the installed pre-push entry passed inside the normal target
Nix shell with the exact HEAD99207-to-master9e98 ref tuple and canonical origin
arguments. This was git hook run pre-push with prepared stdin, not git push; no
network/default update, source/history mutation or passed-spec repeat occurred.
No PrePush task is enabled in the owning configuration. Diagnosis native 11937
and readiness native 57852 both joined exit0. Logs are
/tmp/i2-integration-hook-diagnosis.log and
/tmp/i2-integration-prepush-readiness.log. Source/index and target remain clean.

Root's normal push command, after its fresh claim/target checks, is:

    # cwd: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-backup-disable-design/vpsadmin-integration
    nix develop .#vpsadmin --command git push origin HEAD:refs/heads/master

The verified Ruby is
/nix/store/fk9isw27bmbdkwrchszx1mnv3qgw2kbf-ruby-3.4.12/bin/ruby; Overcommit 0.76.0
resolves through the prepared owning .gems symlink. Root retains the fresh
claim/no-op FF/push/remote-proof driver. I2 has no active operation and retains
fix ownership; source/history, passed checks and prior receipts are unchanged.

## Endpoint coverage correction: committed and published

The required exact-head API Specs run 45887308287, attempt 1, failed job
140141109113 (full/foundation) with one failure among 1626 examples and four
unrelated pending examples. The sole failure was endpoint_coverage_spec.rb[1:1:1]:
Missing scopes: dataset#disable_backups. Its existing request spec already tests
authorization, options and ordinary receipts, but covered_endpoints.yml omitted
the new scope. The coverage check/manifests are unchanged from upstream base;
this was a feature inventory omission, not a runner or upstream baseline failure.
Native result/environment artifacts and the job log were inspected before any
correction or retry. Verified result ZIP 15149968462 SHA256 is
aae1b342f1a145399beaa28422abff7bed65380379c2661151105e2b1fe8aca4. Exact CI
Ruby/Bundler/RSpec and effective lock identity remain in the preserved receipt.

The entire 5725a099-to-final delta is one added dataset#disable_backups line in
api/spec/api/covered_endpoints.yml; every other tree entry is equal. Root and
architect accepted this small fix boundary before implementation. Full-plugin
endpoint coverage plus the existing action request spec pass: **12 examples,
zero failures/pending**, 111.380 seconds, native handle 93570/exit0. No full
foundation/suite, VM, browser, live action or old CI retry was launched.

Final frozen/published head is **99207a8dcd92f5907c52dbc99af52b30aa7ecac1**, tree
**3f3cd9a11eec7d8694bc6c1777adf708239a56c3**, on unchanged fresh base
9e98d254277114535715353edfd5ddd77fab235e. Four logical commits remain:

| Purpose | Final commit |
| --- | --- |
| API including coverage inventory | 4dfdf09e360107ce4db0a737991bb03607944a64 |
| PHP feature | 1ae664c6287cec399d63188f7c3c4f80fcbd46d3 |
| Storage fixtures | 2e8f87484d37322fca97c34b1238f45c86a4de00 |
| Separate Incidents menu deletion | 99207a8dcd92f5907c52dbc99af52b30aa7ecac1 |

The YAML line was folded into its owning API commit. All other patches have
range-diff equality, and the full final tree equals the checked pre-fold tree.
Old 5725 and the checked fixup are retained by refs ending
pre-endpoint-inventory-5725 and endpoint-inventory-before-fold. No migrations,
obsolete fixups or repeated dependency streams entered the final branch. The
feature diff is 33 files, 2198 insertions / 84 deletions. Menu raw patch SHA256
3852cbc02b096bce46c757fd0b414cc57cdaa0fd2397e85715e380a034ead67d and fixture
patch ID 3afcd907d568eaf98de00c49c2d1521dd95dfbea remain unchanged. Raw correction
patch SHA256 is b96640b6dad31b66db8bed3e8b598e9e909abebf7eecab5b27dfd4e4af31cdae.

Normal pre-commit and commit-message hooks passed without bypass. The temporary
fixup message had two preferred-72-column advisories, within repository 80-column
limits; folding retained the original API message. Commit/fold native 32675
joined exit0. Fresh SSH fetch verified unchanged master and lease head 5725;
publication with that explicit lease succeeded, native 28299/exit0. Fresh remote
feature equals 99207a8d, master remains 9e98d254. Source/index are clean and the
exclusive source/index/history window was returned to root. The prepared clean
integration target and declared hook environment from the previous packet remain
available; root owns final freshness/comparison/claim/fast-forward/default push.

Exact new-head initial CI, all attempt 1:

| Workflow | Workflow ID | Run ID |
| --- | --- | --- |
| API Specs | 234996228 | 45890220538 |
| libnodectld Specs | 247475646 | 45890220531 |
| Webui PHPUnit | 283542743 | 45890220513 |
| CI | 228803702 | 45890220654 |
| RuboCop | 229534945 | 45890220577 |
| i18n health | 307073542 | 45890220510 |

Root owns observation; these initial reads are pending/in progress. Only two
superseded active same-branch runs were selected for cancellation. CI 45887308301
accepted cancellation; API 45887308287 completed cancellation before the manual
request, which returned already-completed. Both were independently read as
completed/cancelled on old 5725. No current-head or other-branch run was cancelled,
and the failed old attempt was not rerun. Passing node/PHP evidence is retained;
full CI and original parked VM suites are outside the user's wait scope.

The API declarations, models, schema, configuration, fixture support, plugins,
exporter/tools, packages and flake inputs are byte-identical to 5725. The complete
range only alters test inventory, so no declared contract change or new schema
acquisition is required for this correction. I3 received the exact final head,
whole delta and input-tree correspondence directly. Its actual 5725 export stays
immutable and is not relabelled; I3 owns global final-schema/client freshness.
The whole API tree changes only because it contains the test manifest. Existing
feature guides and all KB-impact/capture limits remain unchanged; no new prose,
translation, documentation contract or runtime behavior was authored.

[Single failure/correction receipt](captures/api-foundation-45887308287-attempt1/receipt.json)
binds the original failure, native artifacts/environment, checked fix, full series,
input equivalence, hooks, publication, CI IDs and terminal effects. Its directory
is ignored/untracked and private (0700/files0600). Root retains narrow-fix review
acceptance and integration; I2 retains fixes with no active operation. No source,
CI, runtime or evidence expansion follows this consolidation. Session remains
open; the cluster remains released and untouched.

## vpsAdmin integration preparation: frozen, published, window returned

User authorized all initiative merges and the configuration vpsadmin channel update;
root retains comparison capture, repository claims, fast-forward/default pushes and
configuration coordination. I2 completed the one integration-preparation/rebase
package. No merge or runtime action was performed here. The source/Git window was
returned with all owned handles joined; only this evidence consolidation followed.

Fresh SSH master is 9e98d254277114535715353edfd5ddd77fab235e, eleven commits after
reviewed base 81e930b25fa3252d7e849aff4819e663cec37b07. They add typed/localized
system configuration, incident ordering and packaged gem updates. The accepted old
head 3a647f64da783e85ff38c570d6c8f75ab993670e remains at preserved ref
2026-11-25-backup-disable-design-pre-integration-3a647f64. Original live/reviewed
refs and all evidence below remain historical, unchanged.

Final frozen/published head is **5725a0996fb60767511bfc86482acefdec9eb9d9**, tree
**1ab250e6875ff737b74e7b9cf02ca5eda7bd5b64**, on fresh base 9e98d254. Complete series:

| Logical commit | Reviewed old | Final |
| --- | --- | --- |
| API | 8485ffe9f5f81d3b426814a467de1c52a594ca0a | 6809b562b4d87f1107dc9f4790fc92a35c1e423c |
| PHP feature | 696efd350054ff183f92bf01ffdb7e790b0c06a8 | c423a329c20d16ca64a649e10efe6d04fe7d5bf0 |
| Storage fixtures | ac4be5ed380236a16f96e527d55a84c00425c7fc | 5de3f6675ad579c40f9614f75ccf3272da842f2a |
| Separate Incidents menu removal | 3a647f64da783e85ff38c570d6c8f75ab993670e | 5725a0996fb60767511bfc86482acefdec9eb9d9 |

All four entries are equal in git range-diff; log /tmp/i2-integration-range-diff.txt.
The sole conflict was generated Czech MO. PO/POT, API locales and docs index merged
automatically; the repository locales-generate script compiled the merged PO. A
separate git merge-tree composition of old accepted feature with fresh baseline,
then compiling its independently merged PO and replacing only MO in a temporary
index, reconstructs the exact final full tree above. No handwritten conflict,
new feature contract or scope change was introduced. Root owns affected review or
certified-equivalence acceptance; I2 does not substitute self-review for that gate.

Final feature diff remains 32 files, 2197 insertions / 84 deletions. There are
**no migrations**, superseded implementation/fixup commits, repeated dependency or
pin streams. The menu stays its separate one-line deletion; raw patch SHA256 is
3852cbc02b096bce46c757fd0b414cc57cdaa0fd2397e85715e380a034ead67d, identical to the
reviewed patch. Fixture patch ID remains 3afcd907d568eaf98de00c49c2d1521dd95dfbea.
Previously deployed commits are retained provenance, not claimed literal ancestors
of the rebased final branch or already merged.

Focused current-input PHP batch passes **12 tests / 143 assertions** in 3.584s
(PHP 8.4.28, PHPUnit 13.4.8), plus three PHP syntax checks. The tested PHP renderer,
page dispatcher, regression and menu bytes are identical at the final head. Final
gettext freshness/health, compiled locale and whitespace checks pass. Normal
staged pre-commit hooks all pass: API/WebUI i18n, PHP formatter, Nixfmt and migration
coverage; log /tmp/i2-integration-staged-hooks.log. No hooks were bypassed. API
53+3 and node46 remain earlier accepted feature evidence; updated upstream packaged
gems mean this packet does not relabel those as a fresh exact-final dependency run.
Final API/libnodectld specs CI supplies current-head verification.

Local setup initially lacked API gems and WebUI vendor. Declared Nix/API and locked
composer preparation succeeded before the final pass; neither setup error was a
failed correctness assertion. The first manual overcommit --run selected all
tracked files. I2 stopped that owned batch after the missing-bundle error, joined
handle 53277/exit143 and verified process group 9598 empty with no unstaged source
change. The subsequent ordinary staged hook invocation passed. The owned PHPUnit
cache was moved intact to /tmp/i2-integration-phpunit-cache-run1. No reset, clean,
stash or unrelated source alteration occurred. Logs remain /tmp/i2-integration-*;
the final source/checks, dependency identities and initial CI are linked below.

The feature did not previously exist on origin. SSH publication with an explicit
empty/absence lease succeeded, and fresh remote feature equality was verified;
master remained 9e98d254. No superseded current-branch CI run existed to cancel.
Exact initial CI at final head, all attempt 1:

| Workflow | Workflow ID | Run ID |
| --- | --- | --- |
| API Specs (topic parallel) | 234996228 | 45887308287 |
| libnodectld Specs | 247475646 | 45887308305 |
| Webui PHPUnit | 283542743 | 45887308318 |
| CI | 228803702 | 45887308301 |
| RuboCop | 229534945 | 45887308303 |
| i18n health | 307073542 | 45887308297 |

These were queued/in progress at the bounded read; root owns observation. User
explicitly excluded waiting for full CI; relevant specs are the wait gate. No
unchanged storage/PHP VM, browser/live check or cluster recreation was run.

Clean disposable target is
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-backup-disable-design/vpsadmin-integration,
detached at 9e98d254. Common Overcommit hooks are active; ignored root/API .gems
symlinks use the prepared owner bundles and bundle check passed. Root's normal
merge environment is nix develop .#vpsadmin at this target. No repository claim
was acquired by I2. Native handle 85986 completed publication/target preparation
with exit0; every other owned handle is terminal/joined. Both source/index and
target are clean. Root owns the fresh target/remote check before integration.

[Final source/input/CI packet](i2-integration-final-inputs.json) binds exact API tree
64c1026d505d678c303054d7d7687467cc5eb6ee, resource tree
597b95cf8850dd49fb310941685d432b84788d03 and unchanged exporter tree
5d291b4cc5c6c3c59bcef42fa0399a15bfe88b62. Export profile, all seven fixture inputs,
tracked exporter/config/flake and API Gemfile identities are recorded. I3 owns the
new exact-final export and client synchronization for upstream SystemConfig
choices/value_nullable; historical eb8/cbe3 acquisition remains immutable. This
packet is not global schema/client freshness certification.

Documentation routing is unchanged: storage behavior/recovery remains in
[the storage guide](../../worktrees/2026-11-25-backup-disable-design/vpsadmin/docs/storage/disable-backups.md),
PHP form/ordinary action/defaults remain in
[the PHP guide](../../worktrees/2026-11-25-backup-disable-design/vpsadmin/docs/webui-backup-cleanup.md),
and this record owns temporary revisions/checks/integration preparation. The two
feature guides are byte-identical to accepted 3a647f64; merged docs index retains
both feature and upstream system-configuration links. No new prose or translation
was authored. Previous KB impact assessment remains bounded; exact published-pin,
external contract and capture certification are still unperformed, with no KB
writes. Earlier live GET/hash proof remains its recorded source/default proof,
not an actual mutation-response or new rebased runtime deployment proof.

Remaining dependencies are root's affected review/equivalence decision, relevant
specs outcomes and I3's final-source schema/client work, then root-owned comparison,
claim, fast-forward/default push and configuration update. I2 retains fixes with
no active operation. Current user data and released cluster are untouched; session
stays open. Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-backup-disable-design/

## Ordinary PHP action flow and unified defaults: accepted and parked

Lead accepted the final four-lane review with no findings at
`3a647f64da783e85ff38c570d6c8f75ab993670e`, then accepted the first bounded
deployed GET/hash/default proof after reading its preserved receipt and inspecting
the English image. I2 is **parked with fix ownership retained**. No further source,
live, runtime or verification action follows this evidence consolidation.

Safe outputs are preserved byte-for-byte in this session for portal Files:

- [Actual-live English defaults image](captures/php-ordinary-3a647f64/actual-live-en-defaults.png),
  SHA256 `5f86d6fbf70d13b4e4282c3c3ffbef0426f92233286a18d3f33a78d934779e0b`.
- [Safe final receipt](captures/php-ordinary-3a647f64/receipt.json),
  SHA256 `242c1e1eddc66e57e5f37a4ba97b703c1610ce3dc3c68a4e33f207728d672565`.

Destinations are ignored/untracked, directory 0700/files 0600; no uploaded input,
credential or session export was copied. Original safe output/log remain under
`/tmp/backup-ui-ordinary-3a647f64/`. Node syntax check passed; the first and only
native proof handle 46368 exited 0, browser closed normally and synchronous guest
reads joined at `2026-11-26T09:37:20.036Z`. Zero blocked mutation attempts and zero
account-language writes were recorded. No cleanup/plan submission, dataset replay,
repair, payload reread or runtime change occurred.

The exact committed, host and served guest bytes match, each served file resolving
through the live source tree to its `/mnt/vpsadmin/webui` counterpart:

| File | SHA256 |
| --- | --- |
| `public/index.php` | `319ea199749164e2b7f2dc61cd5807d7e47a9d5f3171fa4823fce0d47e37f7ef` |
| `forms/dataset.forms.php` | `b50d991fb13c54e1a4bf7606cfdccb7e345e8b07e76b1919758759d546fc7391` |
| `pages/page_dataset.php` | `e06f48b0d18f6f0245905a276c582fb2bca50fd13106b0de18f34d7e0a9a1ec2` |
| Czech `vpsAdmin.po` | `2d67dea890973936672709fc4d7212b8ea1a94a46a0060a2c42357697becd63e` |
| Czech `vpsAdmin.mo` | `a84428114f89816621e35c68f66fb210c878d3b22b3afce46f4f89469f36c117` |

Actual editor and direct GETs with recursion omitted, `0` or `1` all returned
HTTP 200 with recursion unchecked, preservation checked and required Confirm
unchecked. Normal form/page content, exact concise paragraph, complete rows,
plan explanation/inline placement, admin/member gates and retained menu/navigation
passed. The current editor showed zero plan memberships: current user state was
accepted without any old plan/snapshot count expectation. The one English image
was inspected and shows readable aligned controls/defaults. No alternate locale
or broader viewport matrix was attempted. GET/hash evidence proves served binding
and defaults only; the 12-test actual-client route batch below remains the POST
behavior evidence. No live mutation response is claimed. All intentional services
and current user data remain running/intact.

The lead released one package from accepted/deployed source
`825fd1fa8b5628bc01d053b6d2b48a6878b1a53b`, following the sufficient
`design.md#conventional-php-post-submit-presentation` and
`#unified-cleanup-defaults-correction` briefs. The user's subsequent real cleanup
submission changed current data; earlier fixture counts/captures below are
historical. I2 made no live request, action replay, fixture repair or data-state
assumption during this correction. The uploaded input screenshot stayed outside
Git.

The false-unknown cause was established from pinned HaveAPI 0.32.2 and the real
PHP client: undeclared action output defaults to object layout, so the accepted
result is `ResourceInstance`. The retired helper called nonexistent `getMeta()`
on it, caught resource-method lookup failure and displayed unknown before poll.
The old test wrongly declared hash output. Correcting only that fixture reproduced
the defect: **one focused test / one failure**, expected complete versus unknown,
in `/tmp/i2-ordinary-red.log`. No live response body or log was read to make this
diagnosis; malformed Poll fields were not inferred from the screenshot.

The ordinary dispatch now lives in the existing `page_dataset.php` action case,
matching snapshot-create/rollback/expansion patterns. One API call queues the exact
lead-approved EN/CS in-progress notification and redirects to a sanitized local
return or dataset editor. The normal notification perex, page content and existing
transaction sidebar are used. `ActionFailed` uses ordinary `perex_format_errors`
and the dataset editor; other exceptions follow the existing error path without
false success/redirect or replay. Custom receipt parsing, poll/result maps, custom
status/log blocks and empty task-only rendering were removed. No adapter, task
tracker, shared helper or backend/API change was introduced.

Every fresh GET starts recursion false, preservation true and Confirm unchecked,
including recursive query hints. Valid explicit POST booleans remain independent
and authoritative. Administrator/action capability gating, required confirmation,
consumed dataset-bound single-use CSRF and one mutation are retained. The concise
paragraph/labels and plan-removal explanation are unchanged. The sole new UI copy
is the lead-approved in-progress notification; three obsolete custom status keys
were removed and the old completion translation was replaced conventionally.

Focused checks pass: **12 tests / 143 assertions**, 3.382 seconds, PHP 8.4.28 /
PHPUnit 13.4.8. Log `/tmp/i2-ordinary-quick.log`, JUnit
`/tmp/i2-ordinary-phpunit.xml`. The actual object-layout fixture returns the real
`ResourceInstance`. Existing subprocess redirect-test style exercises the actual
SDK/wire and real CSRF, with only dispatch/UI boundaries stubbed: acceptance once
and no poll; standard notification/redirect; actual `show_notification` perex;
ordinary rejection/editor dispatch; transport/response exceptions without success
or replay; duplicate/reconfirmation guards; strict independent options; all three
fresh GET hints false. Retired custom-screen/poll assertions were replaced.
Three affected PHP syntax checks, PHP CS Fixer, gettext freshness/health,
JavaScript syntax and whitespace passed. Final check log:
`/tmp/i2-ordinary-final-check.log`. No broad suite, storage VM or API/client export
was run. Existing unrelated gettext embedded-URL advisories remain unchanged.

Final source is `3a647f64da783e85ff38c570d6c8f75ab993670e`, tree
`af442b1706e06338e4f9e2e3e4c7127ffe5ab01c`. The complete series on base
`81e930b25fa3252d7e849aff4819e663cec37b07` is:

1. `8485ffe9f5f81d3b426814a467de1c52a594ca0a` — API, unchanged.
2. `696efd350054ff183f92bf01ffdb7e790b0c06a8` — owning PHP feature, ordinary
   post-submit/default correction folded in.
3. `ac4be5ed380236a16f96e527d55a84c00425c7fc` — unchanged fixture patch replay.
4. `3a647f64da783e85ff38c570d6c8f75ab993670e` — separate unchanged menu patch.

The old deployed source is retained at
`2026-11-25-backup-disable-design-pre-ordinary-php`; exact checked correction
`01b9393b7c6c638fa3fe651209b7945b44955eb3` remains at
`2026-11-25-backup-disable-design-ordinary-before-fold`. Its entire tree equals
the final tree. Prepared/committed/final 825-to-final patches share SHA256
`34672a7cb47ef5f3cb9a3bf33935702e952fea9a60ed7fd1c64b701aa98a0c63`:
`/tmp/i2-ordinary-{prepared,committed,final}.patch`.
`/tmp/i2-ordinary-range-diff.txt` records old/new complete series.
API subtree `c2a3ccfa11789536b5ee0ba1f8a254d06e753e87` is unchanged. Fixture
patch ID remains `3afcd907d568eaf98de00c49c2d1521dd95dfbea`. The reviewed separate
menu raw patch remains byte-identical, SHA256
`3852cbc02b096bce46c757fd0b414cc57cdaa0fd2397e85715e380a034ead67d`.
No migrations, dependency/generated-pin streams or obsolete fixup commits remain.
This is preserved component/patch provenance, not a claim that old deployed 825
is an ancestor of the rewritten feature or that integration has occurred.

The correction delta is eight owned paths, 267 insertions / 331 deletions:
renderer, dataset action dispatch, existing PHPUnit/Playwright regression files,
POT/Czech PO/MO and `docs/webui-backup-cleanup.md`. Full base-to-head diff is
32 files, 2197 insertions / 84 deletions. No menu source content, API, SDK,
dependency, infrastructure or runtime file changed in this correction.
Normal correction and final owning-PHP amend hooks passed; final message has no
warnings. Logs `/tmp/i2-ordinary-commit.log`, `/tmp/i2-ordinary-fold.log`.
Native handles 70153/1250 exited 0, unit subprocesses joined, index/worktree are
clean, and I2 explicitly returned the source/Git window. No hook bypass,
reset/clean/stash, push or merge occurred.

Documentation remains the developer/operator behavior reference at
`docs/webui-backup-cleanup.md`, linked by the existing docs index. It now describes
ordinary asynchronous acceptance/defaults and preserves partial-failure,
deployment, backup-first and storage-guide/recovery facts. No authoritative API
contract was duplicated. UI copy is exactly lead-provided; no new warning or task
vocabulary was authored. Cached KB impact remains bounded to the earlier member
controls/menu fingerprint assessment: this is administrator-only action/default
presentation, not a new documented navigation control. Exact published pins,
external contract and capture certification remain pending; no KB writes occurred.

Affected independent final review and the separately released served-file/GET/
default proof are accepted as recorded above. GET/hash proof cannot certify an
actual mutation response; offline real-client route regression supplies that
evidence here. Any destructive live test needs a separately approved disposable
scope and is not included. Dataset 1 must never be replayed or reset. Current
runtime/data are preserved; only the explicitly released read-only proof ran.
I2 retains fixes; the original PHP VM/KB limits and historical image coverage remain
parked.

The postreview proof was prepared and then **executed once after release** at
`/tmp/backup-ui-ordinary-3a647f64/check.cjs`, adapted from the existing live check.
It binds exactly public index, dataset renderer, new dataset dispatch and Czech
PO/MO to committed/host/served bytes; reads the actual editor plan list or empty
state; checks omitted/0/1 direct GET defaults, regular content, role/menu behavior;
and may save one current English form image. Old plan/snapshot count assertions
were removed. It uses the known Node/Chromium/Playwright/CA/protected auth sources,
with output `receipt.json`/`run.log` beneath that private root. Expected execution
was 1–3 minutes, stopping on the first actual failure and joining browser/contexts
and synchronous guest handles. No cleanup/plan/account-language write, dataset 1
replay, fixture repair, alternate-language matrix or runtime refresh is included.
Review-pass release preceded launch; the terminal result and effects are above.

## Concise PHP cleanup form: reviewed and combined live proof passed

Lead accepted the final package and inspected both images/receipt. I2 is
**parked with fix ownership retained**; no further checks or source work run.
The already-inspected outputs are preserved byte-for-byte beneath this session
for portal Files:

- [Actual-live English desktop image](captures/php-final-825fd1fa/actual-live-en-desktop.png),
  SHA256 `1fb087af768d9a7859cd3aa25307222bf15cc0a8fb63165cad71278ccf18efd7`.
- [Actual-live English narrow image](captures/php-final-825fd1fa/actual-live-en-narrow.png),
  SHA256 `aeb940af384cfe0b91a9e667167958ed124e8b47cef071c2521410244bed78cc`.
- [Safe final receipt](captures/php-final-825fd1fa/receipt.json),
  SHA256 `0e548b30c3b59d642a896aeeff13127592bc9882e96c3175608c250e0b6f08d2`.

All three destinations were verified ignored and untracked before/after copying;
directory mode is 0700 and file modes are 0600. No uploaded input, credentials,
auth/session export or other private input was copied. No source/commit/live
read/login occurred for preservation. Intentional runtime/data remain running;
the original PHP VM and KB limits remain parked.

Lead accepted reviewer0's final four-lane review with no findings at
`825fd1fa8b5628bc01d053b6d2b48a6878b1a53b`, then released the combined read-only
PHP/menu proof. Native handle 9421 exited 0 and closed its browser normally at
`2026-11-25T22:08:34.514Z`; the bounded synchronous guest reads also joined.

Actual committed blobs, host bytes and served guest bytes match, with every
served file resolving through `/run/vpsadmin-live-webui` to `/mnt/vpsadmin/webui`:

| File | SHA256 |
| --- | --- |
| `public/index.php` | `319ea199749164e2b7f2dc61cd5807d7e47a9d5f3171fa4823fce0d47e37f7ef` |
| `forms/dataset.forms.php` | `692dfe1c769b0aed3c8508165333390575c83b0aef581f257272956f7a2fe759` |
| Czech `vpsAdmin.po` | `38895f80bb3dbf25985ee6628959d3f796ed0cfb894b0d1d9cfb94add8cf17c5` |
| Czech `vpsAdmin.mo` | `8aa15e0ed39a6af1c9e4aa10787de10edc54afe1ae94d929b4ad48e78e81190d` |

Real admin/member checks passed: editor HTTP 200; exact single concise paragraph
in a full-width cell; complete two-column rows; required unchecked Confirm;
independent recursion default false and preservation default true; scoped CSRF
and dataset 1 action; removed extra help/preview absent; plan explanation inside
Backup plans and cleanup immediately below; existing VPS shortcut prechecked
recursion; member form absent/direct access denied. Incidents is absent from the
main menu for admin/member, with the tested other navigation retained. One plan
and all three source snapshot UI rows remain. The one-backup-snapshot count is
still I1's settled proof, not a fresh storage certification.

Private sanitized receipt/log:
`/tmp/backup-ui-concise-825fd1fa/receipt.json` and `run.log`. Both actual-live
English images were inspected:
`/tmp/backup-ui-concise-825fd1fa/actual-live-en-desktop.png` (1280px viewport) and
`actual-live-en-narrow.png` (390px viewport). The text and checkbox rows are
readable and aligned. The legacy PHP page remains fixed width at the narrow
viewport; these full-form crops do not certify responsive fit. Czech live images
were not attempted because the normal language switch persists `User.language`.
No existing source-rendered locale capture harness was reused. Czech coverage is
the approved source/catalog checks and exact served catalog bytes, without a
runtime image claim. No account language was changed and no fixture captures are
being presented as actual-live images.

There were zero blocked mutation attempts, no cleanup/plan submission or account
write, and no source/Git commit, reload, VM, payload reread or fixture action.
Only normal authenticated sessions and read-only requests were used. Credentials
remained private in process; no trace/HAR/session export or uploaded input entered
Git. All owned handles joined; cluster/services/VPS/plan/snapshots remain running
and intact. The bounded package is complete for lead acceptance with the language,
narrow-layout, full-VM and KB limits stated above/below. No further checks run.

The sufficient brief at `design.md#inline-cleanup-form-and-concise-copy-correction`
and lead-approved exact EN/CS copy supersede the earlier UI scope/help display.
I2 confirmed capacity and owned the released PHP source/index window. Final head
is `825fd1fa8b5628bc01d053b6d2b48a6878b1a53b`, tree
`8901b8c1a01506f2ec44d699fa3453ac7ed1ad06`, on base
`81e930b25fa3252d7e849aff4819e663cec37b07`:

1. API `8485ffe9f5f81d3b426814a467de1c52a594ca0a`, unchanged.
2. PHP `d93c85bc55fe4be92446bbe52f51b401d31f0b56`, with this same-feature
   correction folded into its owning commit.
3. Fixtures `672727b97e4eba6d868715b13c81a49e91168176`, unchanged patch replay.
4. Menu `825fd1fa8b5628bc01d053b6d2b48a6878b1a53b`, the user-required separate
   logical commit, unchanged patch replay.

Previous reviewed source `cc922af324751b212d87178c9fa06b4238b2ca91` remains at
`2026-11-25-backup-disable-design-pre-concise-php`; checked correction
`4edf1b19bc19c97e7a49b57acd460d9795935be4` remains at
`2026-11-25-backup-disable-design-concise-before-fold`. The final entire tree
equals that checked correction tree. Prepared, committed and final binary delta
from cc922af3 have the same SHA256:
`0b7bb7a4f1e47c3ea0daaf8cb357266e0656545c830b766b4017a40559d5e5e2`.
Artifacts: `/tmp/i2-concise-{prepared,committed,final}.patch` and
`/tmp/i2-concise-range-diff.txt`. Replayed menu patch SHA256
`3852cbc02b096bce46c757fd0b414cc57cdaa0fd2397e85715e380a034ead67d`
exactly equals the independently reviewed cc922af3 patch. Fixture patch ID remains
`3afcd907d568eaf98de00c49c2d1521dd95dfbea`; API subtree remains
`c2a3ccfa11789536b5ee0ba1f8a254d06e753e87`. There are no migrations, repeated
dependency updates or obsolete UI fixup commits in the final series. Existing
deployed/checked refs and evidence are preserved; this is no integration claim.

The correction changes seven owned paths, 55 insertions / 190 deletions:
`webui/forms/dataset.forms.php`, existing focused PHPUnit/Playwright files,
POT/Czech PO/MO and `docs/webui-backup-cleanup.md`. It uses one exact approved
paragraph in a standard full-width `colspan=2` cell, followed by complete two-cell
rows for Include subdatasets, Back up existing snapshots first, required Confirm
and the existing submit button. Confirm is unchecked, recursion defaults false,
preservation defaults true, and the existing recursive shortcut may precheck
recursion. The actual form stays immediately below Backup plans, including the
planless case; the separate plan-removal explanation stays inside Backup plans.

Dataset identity/scope text, descendant preview/list/read helper, separate
retention/manual-snapshot paragraph, backup-first help/no-new-snapshot/opt-out
warnings and long acknowledgement text were removed at the user's explicit
request. They were not moved to tooltips or other UI. The now-obsolete preview
tests and their fake pagination data were removed with the preview. The focused
markup test instead verifies exactly one paragraph, its exact text/full-width
cell, every complete row width, absent removed help and the existing scoped POST.
Independent options, default safety, unconfirmed/duplicate POST behavior,
admin/capability gates, CSRF, one ordinary action receipt and failure/unknown
handling are retained and covered. Seven unused feature catalog entries were
removed; unrelated common translations remain unchanged. The short labels and
exact new EN/CS paragraph are lead-approved, including common Confirm/Potvrdit.

Quick checks pass: **17 PHPUnit tests / 98 assertions**, 3.372 seconds, no PHPUnit
warnings, PHP 8.4.28 / PHPUnit 13.4.8; both PHP syntax checks; PHP CS Fixer dry-run;
gettext catalog freshness/health; JavaScript syntax with the known existing Node
24 executable; whitespace check. Logs `/tmp/i2-concise-final-check.log`, JUnit
`/tmp/i2-concise-phpunit-final.xml`. Initial new DOM parsing exposed the shared
checkbox helper's pre-existing duplicate `id=input` warning. The test now uses
the adjacent tests' established libxml internal-error capture/restore while
retaining real paragraph/row assertions. Diagnosis is recorded in
`/tmp/i2-concise-markup-diagnosis.log`; no global helper/style work was added.

Required pre-commit and message hooks passed for correction and final PHP amend.
Temporary fixup message had only 72-column advisories within the 80-column rule;
final message has no warnings. Logs `/tmp/i2-concise-commit.log` and
`/tmp/i2-concise-fold.log`. The diagnostic PHPUnit invocation created only an
untracked `.phpunit.cache`; the clean-status guard caught it before rebase. That
owned cache was preserved at `/tmp/i2-concise-phpunit-diagnostic-cache`, without
reset/clean/stash. Final source/index are clean; commit/rebase handles 4248/49002
exited 0 and all effects joined. The exclusive source/Git window was returned.

The owning developer/operator guide retains its docs-index entry and safety,
receipt, failure and storage-guide facts; its form description now matches the
three short controls. UI copy removals are deliberate and supersede earlier
display-copy warnings. Cached KB impact assessment remains bounded: the menu
patch/fingerprints and member-facing plan explanation are unchanged; this
correction removes administrator-only form prose. Exact published feature pins,
full external contract and captures remain uncertified. No KB source/staging or
production write, API/client export, backend/React/infra edit, broad suite,
browser/login/guest read, reload or fixture mutation occurred.

Independent final review and the combined read-only PHP/menu proof are complete
as recorded above. Exact final served-file binding and English desktop/narrow
captures passed; the Czech live-capture limitation is explicit. Earlier long-copy
screenshots below are historical and do not certify this concise rendering.
The mounted PHP exposure is understood; cluster, services, VPS, plan and snapshots
remain running/intact. I2 retains review-fix/proof ownership; the original full
PHP VM batch remains parked.

## Separate PHP main-menu Incidents removal: committed for focused review

User requested removal of Incidents from the PHP main menu in a separate commit.
I2 confirmed capacity and retained settings/access, then received the lead's
bounded brief and exclusive source/index/commit window. Base is accepted
`ebb78bc958668f77c0965df40e84728d0b03142e`, tree
`a7530571d1d207db099aa30ea3100ba3d0fa017f`. New head is
`cc922af324751b212d87178c9fa06b4238b2ca91`, tree
`25e94538ede7701139883c56d11aa54051e5e081`.

The entire delta is one deleted `admin_incidents_menu()` call in
`webui/public/index.php`. The helper, incident pages/actions/routes/sidebar,
authorization checks, translations and every other menu declaration remain
unchanged. The call was admin-only; its removal leaves the main-menu entry absent
for all roles. No new copy was authored; the lead approved the faithful deletion.
No product documentation change is useful for this isolated navigation deletion;
incident route documentation remains applicable.

Syntax, PHP CS Fixer dry-run and whitespace checks passed. The existing focused
`testAuthenticatedHeaderRetainsLanguageSessionJumpNavigationAndSidebarControls`
passed **1 test / 8 assertions**, 0.302 seconds, with PHP 8.4.28 / PHPUnit 13.4.8.
It verifies retained header/navigation controls; production menu absence is the
one-line source delta and awaits the postreview live check. No new test that
mirrors the deletion or broad suite was added/run. Log `/tmp/i2-menu-quick.log`,
JUnit `/tmp/i2-menu-phpunit.xml`. All normal pre-commit and commit-message hooks
passed without warnings; `/tmp/i2-menu-commit.log`. Commit used the repository
Nix environment and `git commit -F /tmp/i2-menu-commit-message.txt`.

Cached KB contract `873758fd6aec0c03f50a94600e0ceab97946f255` has no
`admin.incidents.menu` or `page=incidents` control/binding. Its one-line source
context check finds that this deletion restores adjacent `backups.menu` to
recorded fingerprint
`ae9b0e75d94bafb85fc24b06c4797b5c0acf87fe90bfcc1cbce3c12ce5692243`
(before: `86ede1e5cef9c41d4e9318300c74d00ce66c03e22936fd45ab7803d79f093b27`).
`vps.menu` remains at recorded
`780cff337602656a3feac47e2f02c3f929ad98e9b7bb5018fbd0bd021676d41e`.
Bounded evidence: `/tmp/i2-menu-kb-impact.json`. There is no identified cached
admin-menu documentation control to retire, so no contract branch or KB write
was made. Exact published feature pins, full external contract and capture
certification were not run or claimed; existing KB coverage limits remain.

The complete series on `81e930b25fa3252d7e849aff4819e663cec37b07` is the accepted
API `8485ffe9f5f81d3b426814a467de1c52a594ca0a`, PHP
`c4ae9e020914f949beef594ec14b6e0d1143edd6`, fixtures
`ebb78bc958668f77c0965df40e84728d0b03142e`, then the separate menu commit
`cc922af324751b212d87178c9fa06b4238b2ca91`. The accepted lineage is unchanged;
no obsolete fixup history, repeated update stream or migrations were added.
No API/client/React/infra source or verification was repeated for this head change.
Final delta `/tmp/i2-menu-final.patch` has SHA256
`3852cbc02b096bce46c757fd0b414cc57cdaa0fd2397e85715e380a034ead67d`.
Committed index.php object is `c470bfaa6161d86935b115aca53607740d3ebf40`, SHA256
`319ea199749164e2b7f2dc61cd5807d7e47a9d5f3171fa4823fce0d47e37f7ef`.

Native handle 60045 exited 0, index/worktree are clean, all I2 effects joined,
and the exclusive source/Git window was returned. No push/merge, browser/login,
guest read, refresh, start/stop or fixture operation occurred. Existing PHP live
mount exposure remains understood; cluster/services/data are preserved.
This is a low-risk navigation-only delta for lead-owned focused independent
review. After accepted review, the prepared smallest read-only proof is: bind
the committed/host/served `public/index.php`, log in through the known protected
sources, assert no `#nav` incident anchor/landmark for admin/member while retained
menu routes remain, and optionally GET the existing admin incident route/sidebar.
No form submission, new environment, broad suite or fixture write is needed.
No such live check has launched. I2 retains review fixes and postreview proof.

## Inline layout correction: reviewed and live proof passed

Lead accepted reviewer0's final four-lane review at
`ebb78bc958668f77c0965df40e84728d0b03142e` with no findings, then released the
focused nondestructive proof. That proof passed once, using the existing
persistent cluster and the known Node 24 / Chromium 152 / Playwright environment.
Native handle 32009 exited 0, all synchronous guest-read handles joined, and the
browser closed normally at `2026-11-25T19:50:03.457Z`.

The committed host blobs, current host files and actual served webui guest files
are byte-identical. Each guest file resolves beneath `/mnt/vpsadmin/webui` through
the existing `/run/vpsadmin-live-webui` source tree:

| Served file | SHA256 |
| --- | --- |
| `forms/dataset.forms.php` | `feb5c5471a8ee3199e826da528dd7fa96031987e2f0b93ceb771ff0afa238182` |
| `lang/locale/cs_CZ.utf8/LC_MESSAGES/vpsAdmin.po` | `e91e721b32ebe025feffee2200b8d275ddb7e9ae3b1a9dc39ed259036d3635a2` |
| `lang/locale/cs_CZ.utf8/LC_MESSAGES/vpsAdmin.mo` | `dda4b86bd4898fc19b66d88008943db559e972dbf61f1fb216aca00eb94b424c` |

Real admin/member checks passed: editor HTTP 200; one plan and its exact
explanation inside Backup plans; no cleanup anchor; cleanup form immediately
after Backup plans; independent editable recursion default false and preservation
default true; required destructive confirmation unchecked with native
value-missing validity; scoped CSRF; dataset scope, all-plan-memberships,
categorical full-transfer and opt-out text; existing VPS shortcut prechecked
recursion; member cleanup absent and direct access denied. All three source
snapshot UI rows remain. The backup-snapshot count of one remains I1's settled
fixture proof, not a new UI certification. The one cropped English screenshot
was visually inspected and shows readable placement, explanation and controls.
Czech served catalog bytes were bound, without an extra language/screenshot run.

Safe private receipt and screenshot:
`/tmp/backup-ui-layout-ebb78bc9/receipt.json`,
`/tmp/backup-ui-layout-ebb78bc9/admin-inline-cleanup.png`; safe command output:
`/tmp/backup-ui-layout-ebb78bc9/run.log`. There were zero blocked mutation
attempts and no cleanup or plan-deletion submission. Credentials stayed private
in process; no trace/HAR/session export was made. No source/Git/KB changes,
environment installation, refresh, restart, second VM or fixture writes were
performed. The cluster boot source remains 140f; this proof binds the changed
served PHP/locales to final ebb source without claiming a service/kernel rebuild.
The cluster, services, VPS, three source snapshots, one backup snapshot and plan
are retained. The package is complete for lead acceptance; the full PHP VM suite
and KB capture workflow retain their existing coverage limits.

The lead's bounded correction brief starts from reviewed/live source
`140f0769e222dd2aa51e64d08f11cd5e8dae397b`, tree
`a872181147d22917e37f2a5023af7c30557fd7ea`. I2 confirmed capacity and retained
Sol/xhigh/workspace_write, then owned the exclusive source/index/commit window.
Architect0 settled the static scope preview and dataset-bound single-use CSRF;
lead finalized all added EN/CS wording and passed the guide prose.

Final source is `ebb78bc958668f77c0965df40e84728d0b03142e`, tree
`a7530571d1d207db099aa30ea3100ba3d0fa017f`. The complete series on base
`81e930b25fa3252d7e849aff4819e663cec37b07` is:

1. `8485ffe9f5f81d3b426814a467de1c52a594ca0a` — API, unchanged.
2. `c4ae9e020914f949beef594ec14b6e0d1143edd6` — owning PHP change with this
   correction folded in.
3. `ebb78bc958668f77c0965df40e84728d0b03142e` — unchanged fixture patch replay.

Pre-layout source remains at feature ref
`2026-11-25-backup-disable-design-pre-layout`. The quick-checked correction
`328d1dad4d9486f6938a69b56eae5f3072ee29ec` remains at
`2026-11-25-backup-disable-design-layout-before-fold`. Its entire tree equals the
final tree. The prepared and final 140f-to-final binary patches have identical
SHA256 `ee4a73698fac43172087867f56773e9ec229805e628a53422bcf40d72b07db7e`:
`/tmp/i2-layout-prepared.patch` and `/tmp/i2-layout-final.patch`.
`/tmp/i2-layout-range-diff.txt` records the old/new three-commit comparison.
The fixture patch ID is unchanged:
`3afcd907d568eaf98de00c49c2d1521dd95dfbea`. API subtree
`c2a3ccfa11789536b5ee0ba1f8a254d06e753e87` is unchanged. There are no migrations,
repeated dependency updates, obsolete layout fixup commits or D2 paths in the
final series. This UI-only delta requires no schema/client/export rerun.

The delta is seven owned files, 228 insertions / 88 deletions:
`webui/forms/dataset.forms.php`,
`webui/tests/Regression/DatasetDisableBackupsTest.php`,
`tests/playwright/webui/specs/storage-backup-export.spec.cjs`,
`webui/lang/locale/vpsAdmin.pot`, Czech `vpsAdmin.po`/`vpsAdmin.mo`, and
`docs/webui-backup-cleanup.md`. It moves the exact plan-removal sentence inside
Backup plans, replaces the dataset-editor perex link with the existing cleanup
form directly below it, and displays optional descendants beside an independent
recursion checkbox. Recursion defaults false; preservation defaults true. An
explicit required destructive confirmation defaults unchecked. The explanation
names all selected datasets' backup-plan memberships and states that re-enabling
backups will require a full transfer. Existing retained-backup/manual-snapshot
facts, preservation help, admin/capability gates, one API submission and ordinary
receipt/failure behavior remain. The existing VPS recursive shortcut prechecks
the same editable recursion checkbox. There is no JavaScript, new abstraction,
duplicate renderer, backend, client or React change.

Quick verification:

- Focused real-client/form PHPUnit: **19 tests / 245 assertions**, exit 0,
  3.176 seconds. It covers actual form containment/order, defaults and required
  unchecked confirmation, independent submitted options, no mutation for GET or
  unconfirmed POST, invalid options/cross-dataset CSRF, duplicate prevention,
  full 151-row nonmonotonic scope and withholding the form on scope-read failure.
  Log `/tmp/i2-layout-quick.log`; JUnit `/tmp/i2-layout-phpunit.xml`.
- Both changed PHP files pass syntax. PHP CS Fixer final dry-run, gettext catalog
  freshness/health, JavaScript syntax and whitespace checks pass. Logs:
  `/tmp/i2-layout-format.log`, `/tmp/i2-layout-final-check.log`. The first combined
  formatting command stopped because the root shell has no Node; the known
  existing Node 24 executable passed the focused syntax check, and remaining
  checks completed. No dependency was installed for that correction.
- Required pre-commit and commit-message hooks passed for the correction and
  final owning-PHP amend. Correction-message 72-column advisories stayed within
  the required 80 columns; the final message has no warnings. Logs:
  `/tmp/i2-layout-commit.log`, `/tmp/i2-layout-fold.log`.

Documentation routing: the developer/operator behavior reference remains
`docs/webui-backup-cleanup.md`, linked by the existing docs index; only its first
two paragraphs changed. Safety/failure/recovery facts and storage-guide link
remain. EN/CS product strings use lead-approved copy and existing labels, with
normal generated catalogs. The canonical KB workflow was read. Moving member
plan help can affect dataset-editor captures even when semantic fingerprints
stay equal; final feature-pin/capture impact review remains lead-coordinated.
No KB source, staging or production writes occurred.

Risk remains high because this is a destructive-action form and editable scope.
The focused independent review should cover general, architecture/repetition,
scope/proportionality and risk/compatibility concerns; unchanged production
reviews remain applicable outside this delta. Older open confirmation forms use
the old CSRF scope and must be reloaded; no compatibility replay path is added.
The development provider live-symlinks these existing PHP/locale paths, so source
edits were visible without a build or refresh. No runtime driver, destructive
POST or fixture write was executed. Commit/rebase handles 12203/83866 exited 0;
index/worktree are clean and the source/Git window was explicitly released.
Independent review and the focused nondestructive host/guest binding and
rendered-form proof are complete as recorded above. Cluster/data/services remain
running; the full PHP VM suite is still parked on lead resources.

## Accepted bounded live PHP human-review check

The lead accepted the live read-only check on backend source
`140f0769e222dd2aa51e64d08f11cd5e8dae397b`. The existing persistent cluster and
settled I1 fixture were used; no additional VM, server, installation or broad
suite was launched. Final browser command 73557 exited 0, finishing at
`2026-11-25T18:21:40.049Z`, and closed its browser normally.

All named checks passed: real administrator and member login, one attached plan,
plan-removal explanation, dataset 1 confirmation scope, checked `backup_first`,
unchecked destructive confirmation, scoped CSRF field, three source-snapshot UI
rows and recursive shortcut. The member cleanup entry was hidden and its direct
confirmation GET denied; the member plan explanation remained visible. The
administrator confirmation screenshot was visually inspected: scope,
consequences, preservation help and default controls were readable. I1's verified
one backup snapshot is fixture evidence, not a separate UI certification.

The apparent missing confirmation form was a scratch-browser navigation race.
An awaited confirmation GET returned HTTP 200 with exactly one form and no
exception/fatal; awaiting navigation and form attachment resolved the check.
No PHP fix or restart was needed. A separate broader browser-spec locator finding
remains: perex messages sit under `#content`, outside `#content-in`. It does not
block human review and was not edited in this package.

Private local evidence is `/tmp/backup-ui-review-php-59df3707/receipt.json`,
`confirmation-get-receipt.json` and `admin-cleanup-confirmation.png`. No
credentials, tokens, browser session exports, traces or HAR files were retained.
There were zero blocked mutation attempts; cleanup and plan deletion were never
submitted. The cluster, services, VPS, snapshots and plan remain intact. No
application, Git/index or KB source changes were made. The full three-case PHP VM
suite below remains parked on lead-owned resources; this bounded live check does
not replace its unexecuted coverage.

## Parked full browser VM preparation at final eb8 source

I2 confirmed capacity within the same retained PHP/browser package and verified
its session identity, workspace_write access and unchanged settings. Operational
preparation alone was refreshed for final
`eb8d111b6e0c318336b818aabeacc3d575ac3279`, tree
`84a4bded3a29dc0789723574212638fcf38b8935`. No application, Git/index or KB source
edits, repeated source checks, Nix evaluation/build/cache/selection, browser/VM,
new utility or resource overlap occurred. Execution remains **HELD** on explicit
I1 effects-quiescent/shared-runner release and the lead's root-utility handoff.

Current compact operational packet:
[i2-browser-eb8-input-packet.json](i2-browser-eb8-input-packet.json), SHA256
`c31c201d535118597e022a2943f64e619e9b5f6cf6699a24255255b53daa2c4b`.
The original packet below remains byte-identical, SHA256 `5818041d…1cbe7e`.
The refresh references I1's verified current input proof
`i1-storage-eb8-input-packet.json`, SHA256
`7ccb10a81108daf87bebeaffd0b9ce4217f1abb9411806d07cd0c8f1e8a40f59`, for actual
runner source `/nix/store/84pb87f43h7kll3i689fa021ki4mgc8i-source`, NAR
`sha256-Q73Ls8Ypyp4xaKR4AzPLs7o4Y90YNwha5LJ03kdjqEY=`, node/Nix/kernel inputs
and prior component proof. It does not claim I1's active cache/VM work passed.
I3's `i3-chain-scope-schema-no-change.json` binds the same final API and unchanged
schema `cbe3a7ca90d7f1c94e2b769058b1c32a570e36fd92f55cf48a4302d4e50dc05d`.

Known quick Git reads prove the complete WebUI tree
`08531dc117491676ac9de4452ea95127017bc79a` is identical at accepted R1 fix
`7cdec07ab9bbf7c403ccae142930e71898154759`, accepted consolidated e303 and final
eb8. `tests/suite/webui.nix` and the entire `tests/playwright/webui` tree also
match those heads exactly. The packet records these object identities, so PHP
checks and four-fingerprint/member-capture impact conclusions remain applicable;
no full inventory, build or KB rewrite was repeated.

The selector and all three existing cases remain `webui#storage-backup-export`,
including nondestructive cleanup confirmation only. Eventual watcher argv uses
absolute source/runner paths, jobs 1, fresh state
`/tmp/backup-disable-php-browser-eb8d111b-run1`, separate log/cache/selection/native
exit receipts and declared native test status paths. That root and receipts were
absent at preparation. Expected cost remains the original unmeasured 20–45 minute
warm-image estimate plus required builds/substitution. The exact ordinary runner
exit, all three terminal outcomes and complete effect quiescence are the stopping
condition. No quiet/total timeout, automatic replay or expanded suite is allowed.
A fresh installed-policy watcher and refreshed resource admission are required
only after the current I1 utility/runner effects handoff; separate roots do not
authorize overlap. No extra user approval gate is introduced.

## Historical e303 post-review verification packet: prepared, not launched

Lead accepted resolution of both Important findings and the final review/history
gate. Final clean source is `e303d336c538a75938eba08e646fbd9501afe124`, full tree
`eaa2b1a7bf030b91815e90ff0159a1c5cfc045b9`. Its consolidated tree equivalence
was accepted by lead. Existing passing PHP source checks remain in force;
no broad repeat was run for preparation.

Exact related browser packet:
[i2-browser-verification-packet.json](i2-browser-verification-packet.json), SHA256
`5818041d2cfe52ac311ae4a040ed21201e01d6d625cdf936aa19edc2ac1cbe7e`.
It includes full source/store/NAR identity, complete locked input graph and edges,
relevant file hashes, declared runner path/version, cache/selection/test argv,
expected duration, stop/escalation rules, artifact paths and effects accounting.
Root nixpkgs follows vpsadminos/nixpkgs, lock node `nixpkgs_2`
(`94c3211b0ee8ba969a3f12eb4aff8ba0f72971dd`); the other lock node named
`nixpkgs` is not the root package set. The packet preserves both nodes/graph.

Only `webui#storage-backup-export` is selected, using the declared test-runner
with jobs 1, fresh owned state, no prebuild, and state root
`/tmp/backup-disable-php-browser-e303d336-run1`. Its three existing Playwright
cases cover member storage regressions, role gates/plan explanation, and the
administrator's scoped default-on English/Czech confirmation. The browser case
leaves destructive cleanup unsubmitted; one-call execution and data guarantees
remain the focused PHP/API/storage evidence, not an implied browser result.

I1 owns the shared storage runner/output/fixture window first, using a different
root. No browser, dry-run, selection or VM command has been launched by I2. A
fresh lead-arranged watcher must exist before those phases. A distinct output
root does not authorize concurrent launch. Planning estimate is 20–45 minutes
with warm images plus cold builds/substitution, with no total/quiet timeout.
The normal runner's native limits and failure behavior remain unchanged.
Terminal receipt must account for runner/Nix/QEMU/socket effects before I2's
window is released; idle chat or elapsed time cannot establish quiescence.

### Read-only KB source assessment at final source

Using cached contract revision `c064b4fe87d66486c5eb8f43cb278a464d8574ab` and its
one-line source-context rule, the four affected landmarks are unchanged from
prefeature `81e930b25fa3252d7e849aff4819e663cec37b07` and match the contract's
recorded fingerprints exactly:

| Control | Source-context SHA256 |
| --- | --- |
| backups.vps | 586c20762234e476b6fc5dae4dc2b6d39027d2212f6de0bc825412f8cb8bb880 |
| datasets.edit | b397af2ef43e89a6aec228526ce116d78698435f2ed5838e4eabda949d803659 |
| datasets.create | 111aa84621734d1ef6401e3fba95d96635d32d3deab6edff8245604356caf940 |
| datasets.mount | 643be6db2f657fb18dab241ee8970adc6bf2a501d246e70a2e47055008d3b5f5 |

No semantic ID/label/route change or new member-control scope was found. New
cleanup controls are administrator-only; current affected member captures show
the existing list/navigation subjects. Relevant pages/capture concepts remain
the earlier inventory below. This targeted read-only comparison is not a full
published-feature pin/contract/capture certification. Exact pin/full checks and
reported page/capture review follow coordinated source publication. No contract
source, KB staging/production content or screenshots were changed.

## Review finding: complete recursive confirmation scope

The narrow scope correction was committed as focused fixup
`7cdec07ab9bbf7c403ccae142930e71898154759`, parent/review head
`50aa37aede8926965598f4f8fb0782dce377afb6`. Reviewer0 identified name/ID cursor
mismatch in recursive confirmation. Lead granted I2 the exclusive shared
source/index/commit window for this narrow correction; it was explicitly returned
after successful commit and effect verification. No I2 command remains active.

Bounded source inspection confirmed `Dataset.Index` orders by full_name while
HaveAPI's default pagination filters IDs greater than from_id. The installed
HaveAPI 0.32.2 Paginable input has no default limit; its ActiveRecord adapter
omits SQL LIMIT when no limit is supplied. Therefore the smallest supported fix
is one complete `list(['dataset' => id])` request. No API/schema/client change,
new pagination mechanism or visible error text was needed. Existing read errors
occur before a confirmation form is offered.

The new real-client/form regression models a name-ordered root plus 150 children
with descending child IDs. Before the fix it failed on missing
`root/100 (#1051)` after 101 assertions. After the fix it asserts all 151 scope
name/ID rows are rendered and only one list read occurs. Focused complete PHP
file: **16 tests / 222 assertions**, exit 0, 2.641 seconds. Logs:
`/tmp/i2-review-scope-before.log` and `/tmp/i2-review-scope-after.log`.
Both affected PHP files pass syntax and formatter dry-run checks; whitespace
check passes. Locales and UI prose were untouched; existing broader passing
evidence was reused without a full/long/browser rerun.

Only `webui/forms/dataset.forms.php` and
`webui/tests/Regression/DatasetDisableBackupsTest.php` changed: 30 insertions,
11 deletions. Required pre-commit and message hooks all passed without warnings
or bypass. Commit command session 81178 exited 0. Committed patch is byte-identical
to the prepared/quick-checked patch, SHA256
`63fdcab3d41aca46f91d53b536d9992a562bc32f0c1c63164cba76137d092e9f`, saved at
`/tmp/i2-review-scope-committed.patch`. Verified clean index/worktree before
explicit window release. No rewrite, push or deployment occurred. Fixup subject
targets PHP commit `bd36c4f241ed34da4ce726b702988e3e151d2549`; later consolidation
and review closure remain lead/I1 coordination.

## Pre-finding consolidated source verification

Pre-finding consolidated source was clean at
`50aa37aede8926965598f4f8fb0782dce377afb6`. I1 consolidated the unpublished
D2/correction history to API `cbb8def6056301558ed17c8b4818a9653ae5d35e`, PHP
`bd36c4f241ed34da4ce726b702988e3e151d2549`, and fixtures
`50aa37aede8926965598f4f8fb0782dce377afb6`, on initiative base
`81e930b25fa3252d7e849aff4819e663cec37b07`.

I2 independently compared all ten owned paths from the prior tested/fixup head
`f634d35d6e7d63c62f0b987bc497cb82116bc591` to current final source: diff empty.
The complete WebUI subtree is identical at both heads,
`33001bd809e87eb1756e44b7617ecfbb101ad2a8`. No tests were repeated for this
read-only history check. Current PHP commit is 10 files, 702 insertions / 31
deletions. No I2 command remains active; no push, browser run or lifecycle action
occurred. Whole-branch review was pending at this historical checkpoint; the
current cleared gate and post-review verification phase are recorded above.

The accepted D3 design/plan and current lead-owned ui-copy.md supersede the D2
behavior retained below as historical evidence. Identity/retained workspace_write
were reverified at correction release. I2 keeps PHP/tests/docs and follow-up
ownership; no next package accepted. Independent final review and long browser/KB
work remain pending under lead coordination.

## Current implementation and removed scope

- One ordinary DisableBackups POST with exactly `recursive` and `backup_first`.
  The real HaveAPI PHP client regression uses the ordinary empty-hash output,
  success `response.dataset == {}` and `_meta.action_state_id`. It verifies one
  mutation, no action-specific fields, exact route/parameters/input namespace
  and one bounded 15-second poll. I1's final three actual wire cases passed with
  this shape; the PHP fixture correction required no production adapter change.
- The existing scoped CSRF mechanism uses a consumed single-use token to prevent
  repeated POSTs. No separate operation/session receipt map, continuation option,
  public phase/output adapter, preserved/Continue/status POST form, or special
  retry protocol remains. Existing transaction detail links observe pending work;
  they never invoke the cleanup mutation. Architect0 confirmed this is sufficient.
- Completion requires known successful task completion and fresh dataset/plan
  reads. Pending text says accepted work continues after page exit. Failed tasks
  show possible partial changes; unknown submissions/reads link to ordinary task
  reconciliation and never automatically resubmit.
- Admin/capability/no-plan access, default-on checkbox, all-source scope, loss
  warning, no-new-snapshot fact and nondestructive plan-removal explanation remain.
  Ordinary-transfer preservation failure explicitly prevents cleanup in the
  final lead-owned help text. No compatibility shim for unpublished D2.
- Removed nine inactive D2-added message IDs from source/POT/PO, plus one
  intermediate uncommitted help entry; unrelated historical catalog entries were
  preserved. MO regenerated. Fifteen current shared EN/CS strings are mapped.
- Current correction diff: 8 owned files, 172 insertions / 452 deletions (net
  removal 280 lines). Files: PHP dataset form/helper, its regression test,
  POT/CS PO/MO, PHP guide/docs index and existing browser spec comment. Backup/VPS
  entry and dataset page route from the original package remain unchanged.

## Current D3 checks and prose

- Full PHP suite: **176 tests / 1438 assertions**, exit 0, 29.452 seconds;
  `/tmp/i2-d3-phpunit-final.log` and `/tmp/i2-d3-phpunit-final.xml`.
  It preceded the final help-copy-only change. Final focused suite after that
  change: **15 tests / 69 assertions**, exit 0, 2.604 seconds;
  `/tmp/i2-d3-focused-final.log`. Unchanged full-suite coverage is retained.
- After I1 confirmed the ordinary empty dataset wrapper, the affected PHP fixture
  was corrected and its focused suite passed **15 tests / 70 assertions**,
  exit 0, 2.577 seconds (`/tmp/i2-d3-wire-focused.log`). Formatter dry run and
  whitespace checks also pass. No unchanged full-suite rerun was made.
- Three runtime PHP syntax checks pass; formatter dry run passes on changed
  PHP/helper tests (`/tmp/i2-d3-lint.log`). Current gettext generation/health pass
  (`/tmp/i2-d3-locales-health.log`), using repository Nix environments.
- Existing browser script `node --check` passes using repo-pinned nixpkgs.
  Browser execution remains deferred. Whitespace check passes. No new runtime
  path/test registration or selector change; original UI path selection applies.
- Full-suite warning/deprecation are the same diagnosed unchanged
  SecurityAdvisoryLocalization fixture and pagination signature noted below.
  Current I2 cases have no warnings. Initial quick test caught a stale mock output
  layout/field left by a mechanical rewrite; fixed before the passing batches.
- Lead's D3 guide wording pass is applied, including the `backup_first` coverage
  condition and no automatic opt-out. Existing API identifiers, routes, paths and
  deployment/recovery facts are preserved. No prose blocker remains.

Guide: `vpsadmin/docs/webui-backup-cleanup.md`, linked from docs index, describes
ordinary receipts, duplicate submit protection, partial failure, server-side
continuation after browser exit and existing task-detail recovery. Storage/API
guarantees remain I1's linked `docs/storage/disable-backups.md`. KB affected member
landmarks/pages/captures remain the prior assessment below; no production/staging
or contract-repository write has occurred. Exact committed/published pin/check
follows the lead's post-review checkpoint.

I1 consolidated the unpublished D2/correction series, with exact old/new heads
and I2's independent reconstructed UI comparison retained above. No I2 migrations,
pins, client generation or deployed/public consumers. I2 retains PHP review/KB-fix
ownership. Lead owns acceptance, final packet and review launch. Export and final
review provenance must reconcile the latest review/consolidated head above,
rather than the superseded API correction SHA below.

## D3 commit and window release

I1 granted a short window after corrected API
`5526c99f7f675977f7b0e4da5b060791bbd09c06` committed with required hooks. Index
was empty. I2 staged exactly its eight correction paths and used the required
Nix environment and message file, with the subject
`fixup! webui: add admin backup cleanup confirmation`.

Every pre-commit hook and commit-message hook passed. TextWidth emitted advisory
72-column body warnings; lines satisfy the mandatory 80-column limit. Commit
command session 1182 exited 0, with no unfinished effect. No hooks were bypassed.
The committed patch matches the prepared/quick-checked patch exactly: SHA256
`4448460460463456aa46bd6fc6a68a724eac42ca6554c1e565cd9b13be98e23a`.

Verified parent/head above, empty index and only these I1-owned working changes:
`tests/suite/storage/backup-multiple-destinations-remote.nix`,
`tests/suite/storage/backup-remote-interrupted-send.nix`, and
`tests/suite/storage/remote-common.nix`. Their before/after diff is byte-identical,
SHA256 `7fc064fd694fac072598e47c2b61deae87d00b7fc8077757358515dc591b92bc`.
I2 explicitly returned the window before writing this receipt. Prepared and
committed patches are `/tmp/i2-d3-owned-final.patch` and
`/tmp/i2-d3-committed.patch`; no source edits occurred during hook handling.

Current pre-consolidation series from initiative base
`81e930b25fa3252d7e849aff4819e663cec37b07`: original API
`46a4a1c0bd33c9f2c318086d475b1e289a50c678`, original UI
`1fad9eee08f971d2417c0e26f0f96f731452ff55`, API correction
`5526c99f7f675977f7b0e4da5b060791bbd09c06`, UI correction
`f634d35d6e7d63c62f0b987bc497cb82116bc591`. These superseded unpublished
approaches must be consolidated by I1 before final whole-branch review. This
receipt certifies I2's current package and preserved effects, not final export,
integration or deployment readiness.

## Historical D2 package evidence

Owner: implementer1, retained workspace_write / Sol xhigh. Identity verified with
`dev-session current` from this session's tracking directory; both environment
identity variables absent. Source edits began after I0's ready signal.

Current status: implementation, quick checks and required-hook commit complete;
ready for lead package acceptance and independent review. I2 commit is
`1fad9eee08f971d2417c0e26f0f96f731452ff55`, parent I1 API commit
`46a4a1c0bd33c9f2c318086d475b1e289a50c678`. Git/source window returned to I0
with verified clean index and working tree. I0 still owns two existing remote
VM fixture extensions; this is not final whole-branch source/export readiness.
No pushes, long browser tests, deployment, integration or lifecycle actions.

## Source and history

- Repository: `git@github.com:vpsfreecz/vpsadmin.git`, target `master`.
- Worktree: `worktrees/2026-11-25-backup-disable-design/vpsadmin`.
- Branch: `2026-11-25-backup-disable-design`.
- Initiative base: `81e930b25fa3252d7e849aff4819e663cec37b07`.
- I2 parent: `46a4a1c0bd33c9f2c318086d475b1e289a50c678`.
- I2 head: `1fad9eee08f971d2417c0e26f0f96f731452ff55`
  (`webui: add admin backup cleanup confirmation`).
- I2 diff: 10 files, 982 insertions, 31 deletions. Complete committed patch is
  byte-identical to the quick-checked prepared patch: SHA256
  `6d4081395fef4a973e7a24cb0e1ffe51051d31bae20a796e869849a484eaca5f`.
- Current complete initiative series at I2 handoff: API
  `46a4a1c0bd33c9f2c318086d475b1e289a50c678`, then UI
  `1fad9eee08f971d2417c0e26f0f96f731452ff55`. I0's remaining fixture work may
  advance this series before lead assembles the final review packet.
- No I2 migrations, dependency/pin changes or generated-client changes. One
  intended PHP behavior/test/doc commit, including its generated POT/MO and
  translated PO; no obsolete intermediate I2 commits or repeated update streams.

Owned files: `webui/forms/{dataset,backup}.forms.php`,
`webui/pages/page_dataset.php`, `webui/lang/locale/vpsAdmin.pot`,
`webui/lang/locale/cs_CZ.utf8/LC_MESSAGES/vpsAdmin.{po,mo}`,
`webui/tests/Regression/DatasetDisableBackupsTest.php`,
`tests/playwright/webui/specs/storage-backup-export.spec.cjs`,
`docs/webui-backup-cleanup.md`, and I0-approved `docs/README.md` links.

API/storage/scheduler source, API locales/specs, storage docs and any runtime
configuration changes remain I0's ownership; I2 never stages those paths.

## Behavior and settled clarification

Admin and advertised-action gates protect both entry and every POST. The
plan-management explanation remains available to existing authorized plan users
and older backends. The cleanup entry remains available with no plans. VPS
backups links to the root dataset's recursive confirmation, preserving return
context. Confirmation names the dataset, lists the current intended subtree,
defaults backup-first on and explains opt-out loss, existing-snapshot-only
preservation, full-transfer cost, primary cleanup and normal backup retention.

The PHP session owns immutable scope/options and exact phase receipts. Each
mutation is fenced as unknown and persisted before network submission. Session
serialization protects concurrent tabs. Initial/status POSTs poll only and never
automatically submit cleanup after preservation. Known success displays
**Continue cleanup**, which requires a fresh deliberate scoped CSRF POST. That
POST can submit the sole continuation and poll cleanup. A repeated submission
never starts over or continues twice. Polling errors preserve the known receipt;
unknown mutation outcomes never replay. A lost continuation response cannot
mislabel the preservation receipt as the cleanup receipt.

Architect0 confirmed this explicit continuation boundary after I2 identified
that PHP can outlive browser disconnect. It preserves D2's client-exit contract,
uses existing lead-owned copy and changes no API fields or phases. Lead was
informed. Successful preservation alone never displays cleanup completion.
`retry-needed:` is recognized only as the actual API rejection prefix.

Lead supplied and applied the required writing skill to `ui-copy.md`; I2 uses
its English/Czech strings. Czech recursive scope uses the repository's established
`vnořené datasety` term in place of `poddatasety`, with the same meaning.

## Quick verification

All commands used the repository's Nix environments (Node used the repository's
pinned nixpkgs via `nix shell --inputs-from . nixpkgs#nodejs`). Final PHP suite:

- `nix develop .#webui --command ... vendor/bin/phpunit
  --cache-directory=/tmp/i2-phpunit-cache
  --log-junit=/tmp/i2-phpunit-final.xml`: **180 tests, 1463 assertions**, exit 0,
  29.004 seconds. Includes 19 I2 tests / 93 assertions after the final receipt
  correction. Log: `/tmp/i2-phpunit-final.log`; JUnit XML above.
- PHP syntax for all three changed runtime files: passed.
- `php-cs-fixer fix --dry-run --config=.php-cs-fixer.dist.php
  --path-mode=intersection` on the four owned PHP runtime/test files: passed;
  `/tmp/i2-php-lint.log`.
- `webui/lang/scripts/locales-generate` then `locales-health`: passed with 21
  finalized shared strings; `/tmp/i2-locales-health.log`. Only pre-existing
  xgettext embedded-URL warnings in unrelated files.
- `ruby tests/ci-selection-test.rb`: **16 runs, 55 assertions**, passed;
  `/tmp/i2-ci-selection.log`. Existing selectors already map all changed
  runtime/browser paths to `webui-storage-backup-export` and storage tags.
- `node --check tests/playwright/webui/specs/storage-backup-export.spec.cjs`:
  passed. Browser execution remains deferred until independent final review.
- `git diff --check`: passed.

The full PHP suite reports one pre-existing warning in
`SecurityAdvisoryLocalizationTest::testNodeFormHasOneNoteFieldPerContentLanguage`
(`security_advisory.forms.php:1179`, missing fixture REQUEST_METHOD), and one
pre-existing PHP 8.4 deprecation from `pagination.lib.php:151` (implicit nullable
constructor argument), triggered by nine existing NetworkAvailability tests.
A focused 27-test diagnostic reproduced both in unchanged files; exit 0,
430 assertions, `/tmp/i2-phpunit-existing-warnings.log`. I2 tests have no issues.

Initial focused tests caught incorrect one-argument XTemplate::perex usage and
a missing mock find alias; both corrected before the successful quick batches.
PHP CS Fixer needs explicit `--config=.php-cs-fixer.dist.php` for multiple paths.
Gettext generation exposed a superseded unsupported-backend draft string; source
and catalog now use the current lead copy. No hooks were bypassed.

### Temporary Git window and blocked commit

I0 granted a temporary index/commit window with 23 API/storage paths already
staged. Before I2 staging, the staged patch matched I0's recorded SHA256
`b8fcc4cb5bb4f121a2ad9afe2a88d4b5ec515b96c418b191d533f22a95c98707`
and staged tree `333653374d6ba8519a22bdf094f7e65120816007`.
I2 staged only its ten owned paths and used `git commit --only -F
/tmp/i2-commit-message.txt -- <explicit-owned-paths>` in `nix develop .#vpsadmin`.
Nixfmt, MigrationSpecs, PHP CS Fixer and WebUI i18n passed. VpsadminApiI18n failed:
missing `dataset.disable_backups` / `dataset.preserve_for_disable` transaction
labels and unnormalized en.yml. Those labels are present in I0's actual staged
and working locale files. Path-only hook isolation likely hides tracked locale
changes while leaving new untracked-relative-to-HEAD chain files visible.

HEAD remained `81e930b25fa3252d7e849aff4819e663cec37b07`. After hook completion,
the API staged patch was byte-identical and the working tree had no differences
from the combined index. I2 saved its final owned patch at
`/tmp/i2-final-owned.patch` (SHA256
`6d4081395fef4a973e7a24cb0e1ffe51051d31bae20a796e869849a484eaca5f`), then
unstaged only its ten explicit paths, preserving all working files. The staged
API patch/tree were verified identical to the recorded originals before window
release. The owned-path restore printed an Overcommit missing-signature notice
after index mutation; actual effects were reconciled without retry. Lead and I0
received exact reports. No active command remains, no hook was bypassed and no
API/source repair was attempted by I2.

After I0 committed the API/catalog as
`46a4a1c0bd33c9f2c318086d475b1e289a50c678`, it granted a fresh exclusive
window with an empty index. I2 staged only the same ten owned paths and verified
their staged patch byte-identical to the saved prepared patch. Normal
`nix develop .#vpsadmin --command git commit -F /tmp/i2-commit-message.txt`
succeeded. Every required pre-commit hook passed, including API i18n. Commit
message hooks passed with advisory 72-column body warnings only; all lines meet
the mandatory 80-column limit. No hook bypass or source change was needed.

Verified exact final head/parent and clean worktree/index, then returned the
window promptly to I0 before updating this evidence. The first completion
message transcribed the full I2 SHA incorrectly; an immediate fresh-ID correction
provided the authoritative verified SHA above. No Git mutation used that incorrect
text. I3 received the correct head and the explicit warning to await lead's final
source/export release.

## Documentation and KB impact

| Topic | Reader / class | Authoritative home | Evidence / limit |
| --- | --- | --- | --- |
| PHP confirmation, receipt/session invariants and recovery | PHP maintainers / reference | `vpsadmin/docs/webui-backup-cleanup.md` | Matches helper/form regression coverage; linked from docs index |
| Storage preservation/cleanup contract and deployment order | API/storage maintainers / reference | I0's `vpsadmin/docs/storage/disable-backups.md` | Cross-linked from docs index; owned and verified by I0 |
| Current revisions/check output/delivery | Session participants / execution record | This file and lead-owned state.md | Local quick evidence; no deployment claimed |

Canonical `vpsfree-kb-contracts/docs/webui-change-workflow.md` and repository
guidance read. Existing `datasets.edit`, `backups.menu` and `backups.vps` semantic
IDs/labels/routes/source landmark statements are preserved. The new cleanup link
is administrator-only and is not a documented member control. The additional
plan-removal explanation changes the member dataset editor; no current capture
concept in the cached contract shows that plan editor.

Candidate review scope from current bindings: `datasets.edit.open` → Czech
`navody:vps:kvm`, English `manuals:vps:kvm`, capture `vps-details/datasets`;
`backups.vps.open` → Czech `navody:vps:zalohy`,
`navody:vps:obnova_webu_zo_zalohy`, `navody:vps:exporty`; English
`manuals:vps:backups`, `manuals:vps:exports`,
`manuals:vps:vpsadminos:storage`; capture `backups/vps-backups`. Related screenshot
concepts use member sessions, where the new administrator link is absent.
This is an impact assessment, not a final exact-revision contract certification.

Lead's post-review publication checkpoint must provide the exact committed and
pushed vpsAdmin revision before the external contract pin/check. That workflow
then determines actual drift, page candidates and screenshot regeneration.
No production pages, staging state, contract branch or screenshots were changed.

## Next dependency

Lead accepts this package, I0 finishes its assigned fixture extensions and lead
releases final committed source for I3 schema/client synchronization. Lead owns
the complete whole-branch packet and independent review invocation. I2 retains
PHP follow-up/review-fix ownership and has no new package assignment. Long browser
work needs a fresh watcher after review; intended target is
`./test-runner.sh test 'webui#storage-backup-export'`. Publication remains held
until the lead's post-review checkpoint.

Stable session URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-backup-disable-design/
