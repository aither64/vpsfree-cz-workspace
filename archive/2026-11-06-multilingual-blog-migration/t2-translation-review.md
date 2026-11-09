# T2 English translation batch evidence

Owner: `implementer2`. Lead accepted the completed batch on 2026-11-06.
This records completed source work and agent checks; human editorial review and
publication remain pending. C0 owns subsequent aggregate checks and the index.

## Exact source and committed scope

- Repository: `vpsfreecz/blog`, local branch
  `2026-11-06-multilingual-blog-migration`.
- Parent: `e8aed2ef787217e8085d782e38a760cd51ddbd90`.
- Accepted T2 commit: `c3786b74af9ee9382af4cc44428e7e77965753ea`,
  `content: draft 62 English archive translations`.
- The earlier reported `c3786b751ffacb2109d9db19de9849bfd0577146` was a
  transcription error, explicitly corrected and discarded. Verification used
  the actual accepted commit; the lead independently checked it with Git.
- Exact scope: 62 new `content/posts/<id>/index.en.html` files, 2,220 inserted
  lines, translating 21,468 source words. No Czech/shared data/template edits.
- Source snapshot: `20261106T211556Z`. Complete public source manifest:
  `data/migration/source-manifest.json`, SHA-256
  `e3c56173acbc2dd018da1d7ce5cd8b73d52e5ef83847a0353b17b107e5a36ab4`.
- No migrations, input updates, superseded T2 commits or history rewrite.
  No push, default initialization/integration, production action or service
  change was performed by T2.

Assigned IDs, matching `translation-batches.json`'s `implementer2` batch:

```text
wp-24 wp-37 wp-51 wp-61 wp-74 wp-82 wp-84 wp-100 wp-112 wp-114
wp-119 wp-137 wp-139 wp-151 wp-210 wp-215 wp-244 wp-249 wp-253 wp-269
wp-275 wp-279 wp-291 wp-308 wp-326 wp-343 wp-378 wp-387 wp-406 wp-433
wp-443 wp-450 wp-455 wp-460 wp-465 wp-470 wp-474 wp-490 wp-500 wp-521
wp-529 wp-536 wp-552 wp-580 wp-588 wp-601 wp-610 wp-615 wp-625 wp-629
wp-636 wp-651 wp-653 wp-681 wp-695 wp-709 wp-717 wp-792 wp-805 wp-807
wp-811 wp-815
```

## Exact inventory digest

Final SHA-256:
`ff6ebefe2f8377ca62796917283ededb2caa54ec29e64a5d2ad9de81665d4ce3`.

The digest covers a JSON array of 62 objects containing `path` and `sha256`.
Paths are repository-relative `content/posts/<id>/index.en.html`, sorted in
ASCII order. Each hash covers the file's raw bytes. Encode using Python
`json.dumps(rows, ensure_ascii=False, sort_keys=True, separators=(',', ':'))`
followed by exactly one LF, then hash those UTF-8 bytes. The committed files
are the durable inventory source; `/tmp/blog-t2-inventory.json` was the local
working copy. Every staged blob, committed blob and final owned working file
matched this digest's individual hashes. The commit's changed-path list was
exactly these 62 paths. The index was empty when yielded to the lead.

## Completed checks and limits

Every full Czech source and public author mapping was read. Each full English
body was translated and compared for semantic omissions, chronology, first-person
claims and source-era technical meaning. The lead read all 62 full English bodies
and accepted the contextual wording, including the requested corrections to
`wp-815`, `wp-465` and `wp-500`.

Final local batch checks passed for all 62:

- Actual complete Czech-file SHA-256 equals the manifest's `cs_file_sha256`
  and English `translation_source_sha256`; the raw body hash was not substituted.
- Original `date`, `lastmod`, taxonomy slugs, `translationKey`, `article_id`
  and source provenance remain unchanged. Every English file has `draft=true`
  and `translation_status="draft"`, with no human reviewer or review timestamp.
- Ordered HTML structure, machine attributes, comments and original `more-*`
  anchors match. Human-readable alt/title translations are allowed; URLs,
  media targets and other machine attributes are preserved.
- Ordered `href`, `src`, `srcset` and `poster` values match, and complete
  protected `<pre>`/`<code>` spans match raw source bytes.
- Numeric values match after English decimal/percent formatting. The approved
  `wp-500` prose word `twice` is explicitly equivalent to source `2x`.
- Newly introduced unprotected EOF blank lines were removed. Each owned file
  ends with one LF; protected code was not normalized.

Before commit, a global source check covered all 125 Czech/English pairs:
complete source-file/manifest/translation hashes, draft state, absence of human
reviewer/date, matching IDs and explicit root-relative English routes passed.
There were no English route collisions across the 125 files then present.
This was source validation, not a Hugo build, rendered-page check or final
aggregate acceptance. C0 owns aggregate checks; no extra shared build was run
for this evidence. Temporary check helpers were outside the repository.

The ordinary commit ran through `nix develop -c git commit -F` with no hook
bypass. Repository instructions declared no hook framework, and no framework
configuration was found. No whole-worktree cleanliness claim was made; other
owners' work was preserved.

## Raw-byte whitespace classification

All **31 `<pre>` blocks and 50 `<code>` spans** were compared as complete
ordered byte strings using `read_bytes()` and byte-pattern extraction, without
text-mode newline conversion. All matched the Czech source; no protected-code
repair was necessary.

Of those protected spans, **25 `<pre>` blocks contain source-identical CRLF**.
The staged diff check reported **154 trailing-whitespace locations**, all inside
those exact source-identical blocks. Every diagnostic was mapped to its staged
file/line and checked against the raw protected source span. There were no other
diagnostics or remaining EOF findings.

| Article | Protected CRLF blocks | Diff-check line diagnostics |
| --- | --- | --- |
| `wp-308` | 9 | 87 |
| `wp-521` | 3 | 14 |
| `wp-610` | 7 | 16 |
| `wp-615` | 2 | 11 |
| `wp-807` | 4 | 26 |
| Total | 25 | 154 |

These are inherited A1 source-fidelity exceptions, not new prose whitespace.
The code bytes remain unchanged. `/tmp/blog-t2-diff-check.txt` held the local
diagnostics; this record retains the classification and counts.

## Preserved source quirks and editorial boundary

- `wp-24`: `ZPS` remains in the quoted source thread title.
- `wp-84`: the source spelling `PostgresSQL` remains.
- `wp-139`: the statement says five mount states while the list has six entries;
  both remain as written in the source.
- `wp-490`: the protected release-note URL remains
  `http://https;//projects.vpsfree.cz/vpsadmin-doc/releases/v2.7.0/`.
- `wp-521`: the historical PTR explanation and one-record claim remain;
  translation did not turn into a technical update.
- `wp-210`: Czech long-scale `79 kvadriliard` is English short-scale
  `79 octillion`, preserving the value.
- Original relative Czech URLs remain for V1's output handling. Source-era
  security/version claims, plans, opinions, uncertainty and authored asides were
  preserved. Existing English titles/UI strings and code remain intact.
- Meaningful Czech alt/title prose was translated; empty or identifier-only
  media labels were retained without inventing descriptions.

Agent fidelity/style checks and the lead's contextual wording acceptance do not
constitute human editorial review. All 62 translations remain drafts, excluded
from production publication under the agreed contract. Final independent change
review waits for C0/E0 source completion and aggregate evidence; human editorial
approval is a separate later gate. Implementer2 retains ownership of T2 findings.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/>.

## T9 contextual repetition audit — accepted proposals and execution

Base inspected: `3aec4d6b4858b2ed50e21bdb99d36f707fc9ceeb`. All 62 assigned IDs listed above were read in full English prose with the complete Czech prose context, including captions, lists and tables. No article edits, staging, commits, builds or services were performed before the main writing acceptance. The initial proposals below are retained; the final accepted refinements and execution follow. Protected code blocks were outside this prose audit and remain byte-protected.

Fourteen affected IDs are proposed below. All teasers remain unchanged and useful alone; each revised body develops the teaser. Intentional interview/anniversary rhetoric, useful technical repetition, source-era claims, uncertainty and existing source quirks remain. These are agent editorial proposals, not human translation review.


### wp-24

Reason: The teaser and body repeat the daily rsync schedule, and the body states it twice. Retain the automatic schedule, snapshot ordering and lack of individual settings.

Unchanged teaser: We currently back up once a day using rsync. But we are preparing a move to ZFS snapshots, which will open up many possibilities.

Old: VPSes are currently backed up once a day using rsync, followed by a snapshot to preserve the state after rsync finishes. It is not currently possible to configure backups individually for each VPS. Everything runs automatically once a day.

Proposed: After rsync finishes, a snapshot preserves the resulting state. Backups run automatically once a day; individual schedules cannot currently be configured for each VPS.

Revised opening in context: After rsync finishes, a snapshot preserves the resulting state. Backups run automatically once a day; individual schedules cannot currently be configured for each VPS. You can then access backups through the control panel or directly from your VPS in /vpsadmin_backuper and its .zfs/snapshot/ subdirectory. Read more in our knowledge base.


### wp-82

Reason: The teaser has already stated both educational and publicity purposes. The body can add regular attendance, then name conferences; neither purpose is removed from the full article.

Unchanged teaser: Conference talks are our contribution to education, but they also help people find us. Sometimes with a surprisingly long delay.

Old: We try to speak regularly at interesting conferences, both to contribute to education and to be visible so that the public knows we exist at all.

Proposed: We try to speak regularly at interesting conferences.

Revised opening in context: We try to speak regularly at interesting conferences.


### wp-119

Reason: Avoid repeating the entire attendance/largest-event claim immediately after the teaser. Keep the linked event, returning stand and member staffing.

Unchanged teaser: Just as last year, we cannot miss the biggest Czech Linux event. We are going to LinuxDays.

Old: As last year, we are going to LinuxDays, the biggest Czech Linux conference. We plan to have a stand again, staffed in turn by our members.

Proposed: At LinuxDays, we plan to have a stand again, staffed in turn by our members.

Revised opening in context: At LinuxDays, we plan to have a stand again, staffed in turn by our members. You can talk to them about vpsFree.cz and their experience running Linux servers and various services.


### wp-275

Reason: The teaser already asks and explains the exact application-form question. Start the body with continued growth, then develop the 408/308 application analysis.

Unchanged teaser: How did you hear about us? We ask every new member that question on the application form. Personal recommendations lead the way.

Old: We are still growing quickly, and we ask every new member how they heard about us when they apply.

Proposed: We are still growing quickly.

Revised opening in context: We are still growing quickly. I took the 408 applications from the past year and selected those with a meaningful answer to this question. That reduced the number to 308. Here are the results:


### wp-308

Reason: The teaser already describes mounting an API as files/directories. Keep the body's narrower HaveAPI compatibility requirement and all surrounding FUSE/API links.

Unchanged teaser: FUSE lets you mount almost anything as a filesystem. With HaveAPI-fs, you can mount your API and work with it as files and directories.

Old: It lets you mount any API using HaveAPI and work with it through directories and files.

Proposed: Any API using HaveAPI is supported.

Revised opening in context: haveapi-fs is a virtual filesystem built on FUSE. Any API using HaveAPI is supported. Of course, it also works with our api.vpsfree.cz (documentation).


### wp-387

Reason: The four-year threshold occurs twice in adjacent sentences. State it once, preserving the count, cautious conclusion and following exact 4-5/5-6/6+ list.

Unchanged teaser: A few days ago, we passed 1000 members. It was predictable, and it means we have not done anything fundamentally wrong.

Old: We looked at how many members have been with us for more than four years. It seems we have very loyal members: more than two hundred have stayed for over four years:

Proposed: We looked at members who have stayed for more than four years. There are over two hundred of them, so it seems we have very loyal members:

Context: the unchanged preceding graph follows the opening 1,000-member announcement; the unchanged following list is 4-5 years: 90 members; 5-6 years: 53; 6+ years: 74.


### wp-470

Reason: The teaser already introduces long-running blocking actions. Begin the body with what clients can do, retaining version, both links, console example and every action example.

Unchanged teaser: The new HaveAPI release mainly adds support for long-running blocking actions.

Old: HaveAPI version 0.7 adds support for so-called blocking actions: actions that take longer to execute. In our API, these include creating a VPS, reinstalling, starting/stopping/restarting, cloning, swapping and so on. Clients can now monitor the progress of these actions or block until they finish, as the console client does, for example.

Proposed: HaveAPI version 0.7 lets clients monitor the progress of blocking actions or block until they finish, as the console client does, for example. In our API, these include creating a VPS, reinstalling, starting/stopping/restarting, cloning, swapping and so on.

Revised opening in context: HaveAPI version 0.7 lets clients monitor the progress of blocking actions or block until they finish, as the console client does, for example. In our API, these include creating a VPS, reinstalling, starting/stopping/restarting, cloning, swapping and so on.


### wp-500

Reason: The teaser and body repeat integration and recipient selection; the body then repeats selection again. Retain version/release link, email channel, affected-only delivery and no need to remember the node. The following outage-list paragraph stays intact.

Unchanged teaser: vpsAdmin 2.8.0 integrates outage reporting, so it always knows who an outage affects and where to send notifications.

Old: vpsAdmin v2.8.0 integrates outage reporting. vpsAdmin now knows exactly who an outage affects and can notify the relevant members by email. You no longer need to remember which node hosts your VPS. If an outage affects you, you will be notified; otherwise, you will not.

Proposed: With vpsAdmin v2.8.0, you no longer need to remember which node hosts your VPS: only members affected by an outage receive email notifications.

Revised opening in context: With vpsAdmin v2.8.0, you no longer need to remember which node hosts your VPS: only members affected by an outage receive email notifications.


### wp-536

Reason: The first body sentence repeats the teaser. Develop its scope instead: retain version/link, source of observations and distinction from user-service monitoring; checks and notification-only behavior follow unchanged.

Unchanged teaser: We have released a new vpsAdmin, mainly adding simple monitoring for your VPS.

Old: The new vpsAdmin v2.9 mainly brings simple VPS monitoring. It is not a monitoring system for watching your own services. It only uses the information vpsAdmin collects from VPSes and nodes.

Proposed: In vpsAdmin v2.9, monitoring uses only the information collected from VPSes and nodes; it does not check your own services.

Revised opening in context: In vpsAdmin v2.9, monitoring uses only the information collected from VPSes and nodes; it does not check your own services. It currently checks free dataset space, CPU usage against the rules and the amount of transferred data. Monitoring only sends notifications; it takes no action itself.


### wp-601

Reason: The availability announcement is already in the teaser. Move straight to authentication-device choices, retaining the acronym, linked TOTP description and all program/setup/security instructions.

Unchanged teaser: To protect our members, we are introducing two-factor authentication in vpsAdmin using TOTP.

Old: You can now set up two-factor authentication (2FA) using TOTP in vpsAdmin. For example, you can authenticate with a phone running

Proposed: For two-factor authentication (2FA) using TOTP, you can use a phone running

Revised opening in context: For two-factor authentication (2FA) using TOTP, you can use a phone running Google Authenticator, FreeOTP or any program implementing TOTP. To set it up, scan the QR code with the application or enter the secret key. The application can then display the current login password at any time; it changes every 30 seconds.


### wp-695

Reason: Avoid repeating the teaser's whole new-root issuance clause. Add the exact date and root identity/history; all historical support claims and the linked announcement remain.

Unchanged teaser: From January next year, Let's Encrypt will issue certificates based on a new root. Test whether your Android device already supports it.

Old: From 11 January 2021, Let's Encrypt will issue certificates based on a new root. It has existed since 2015, and most devices already have the necessary updates and include the new ISRG Root X1.

Proposed: Let's Encrypt will make the switch on 11 January 2021. The new root has existed since 2015, and most devices already have the necessary updates and include ISRG Root X1.

Revised opening in context: Let's Encrypt will make the switch on 11 January 2021. The new root has existed since 2015, and most devices already have the necessary updates and include ISRG Root X1.


### wp-792

Reason: The teaser already establishes the two-year interval and distribution statistics. Move directly into comparison while keeping the previous-statistics URL and every later figure/table byte.

Unchanged teaser: After two years, we bring you our regular statistics from our virtual servers, specifically the distribution breakdown.

Old: It has been two years again since we last published statistics on the distributions our members use. It is time to look at the current data and compare it with the previous figures.

Proposed: It is time to compare the current distribution data with our previous figures.

Revised opening in context: It is time to compare the current distribution data with our previous figures.


### wp-807

Reason: The teaser already gives the 2022 start and kernel/userspace split. Keep gradual work, prior-post link, ongoing kernel status and every integration detail that follows, without announcing the same start/split twice.

Unchanged teaser: Since the beginning of 2022, we have been working on the move to cgroups v2. It requires changes to the Linux kernel as well as userspace integration. That is why the devcgprog utility came about.

Old: In my previous post, I wrote about the planned move to cgroups v2. We have been working on it gradually since the beginning of 2022. It requires changes to our kernel, still in progress, and userspace integration:

Proposed: As I wrote in my previous post, we are gradually working on the planned move to cgroups v2. Kernel changes are still in progress, alongside userspace integration:

Revised opening in context: As I wrote in my previous post, we are gradually working on the planned move to cgroups v2. Kernel changes are still in progress, alongside userspace integration: controller delegation, different ways of configuring and reading parameters, and finally integration with vpsAdmin. For me, the devices controller has probably been the toughest part so far. I will describe what it is for and how it works, for anyone interested.


### wp-811

Reason: The teaser already says disk exhaustion is common. Start the body with the warning threshold and its limits; retain all application/login/ZFS effects and expansion/recovery numbers.

Unchanged teaser: A virtual server running out of disk space is quite a common occurrence here. To protect applications and filesystems, we have decided to automate the response.

Old: Someone regularly runs out of disk space inside a VPS. vpsAdmin sends warnings from 90% usage, but even that does not always prevent it.

Proposed: Even though vpsAdmin sends warnings from 90% usage, VPSes still run out of disk space.

Revised opening in context: Even though vpsAdmin sends warnings from 90% usage, VPSes still run out of disk space. A full disk stops applications that use it from working and can also make it impossible to log in to the VPS and free up space manually.


### T9 final main acceptance, checks and committed result

The lead read all 14 proposals with full English prose and Czech openings and
accepted them before edits, with two exact refinements:

- `wp-24`: "After rsync finishes, a snapshot preserves the resulting state.
  Backups run automatically once a day and cannot currently be configured for
  individual VPSes." This replaces the narrower proposed schedule limitation.
- `wp-387`: the first body paragraph also changes from "Last week, we passed
  1000 members, and more have already applied, so growth continues at its steady
  pace." to "More members have already applied since last week's milestone, so
  growth continues at its steady pace." The actual apostrophe is ASCII. The
  accepted loyalty paragraph change above also applies.

All remaining 12 proposals were accepted exactly. All 62 assigned IDs above were
inspected; the 48 not named as affected remain byte-identical to the inspected
baseline. Fifteen exact prose replacements were applied across 14 files using
`read_bytes()`/`write_bytes()`, without decoding and re-encoding whole source files
or changing line endings. All standalone teasers remain byte-identical. No title,
frontmatter, date, ID, source hash, draft/review state, raw tag/comment sequence,
HTML attribute, link/media target, more anchor, protected code or Czech source
changed.

Source-only checks passed through the pinned environment:
`nix develop -c python3 /tmp/t9-implementer2-check.py`. The transient helper binds
all 62 final files to the exact baseline plus the accepted substitutions; it
checks complete raw frontmatter/teasers/markup, 31 pre blocks and 50 code spans
against both the baseline and exact Czech bytes, all 125 fresh manifest/source/
translation hashes and draft states, stable article/translation IDs, and absence
of invented human-review fields. The complete 125-file Czech inventory and its
raw hashes are unchanged, with no Czech diff from inspected base to this commit.
URLs/media/attributes are covered by equality of ordered complete raw tags.

Numeric sequence equality is deliberately **not** claimed. Approved removal of
repeated visible digit tokens is exactly one `1000` in `wp-387` and one `2022` in
`wp-807`; both facts remain verbatim in the unchanged teaser. Repeated prose
references such as the four-year threshold (`wp-387`), two-year interval
(`wp-792`) and daily schedule (`wp-24`) likewise retain their distinct facts.
All other visible numeric tokens retain their sequence. Numeric checks exclude
HTML attributes/URLs, which are independently byte-identical; the first helper
attempt incorrectly counted URL digits when a date phrase moved in `wp-695`.
That helper was corrected without any further article change.

The lead released the exclusive index window after T9-3 yielded. The index was
empty at admission, and staging/committing included exactly these 14 paths:

```text
content/posts/wp-119/index.en.html
content/posts/wp-24/index.en.html
content/posts/wp-275/index.en.html
content/posts/wp-308/index.en.html
content/posts/wp-387/index.en.html
content/posts/wp-470/index.en.html
content/posts/wp-500/index.en.html
content/posts/wp-536/index.en.html
content/posts/wp-601/index.en.html
content/posts/wp-695/index.en.html
content/posts/wp-792/index.en.html
content/posts/wp-807/index.en.html
content/posts/wp-811/index.en.html
content/posts/wp-82/index.en.html
```

- Parent: `d6c673c9e6addc8cf4f32f10cd653d8a632f0ddb` (accepted T9-3).
- Commit: `f0337fb7eae8797efca9254cd7208949cb0f77e4`,
  `content: avoid repeated English article openings`.
- Tree: `b80d2261d92efe01c51946f97fec5cd45b32b0fe`.
- Diff: 14 files, 15 additions/15 deletions; no other application scope.
- Staged and committed 14-file inventory SHA-256:
  `0dfb62339bca4d9c8a8b9edd6922175f126d702f8fd6975dd6390f4264c8c947`.
- Final complete owned 62-file inventory SHA-256:
  `2bcbb18b608c05cc2d7866fe1723c6d46f9ddf59b533f946151847dc2d71de5f`.

Both inventories use the earlier documented sorted canonical JSON path/raw-file-
SHA-256 method, with compact separators, sorted keys, UTF-8 and one LF. Each
committed blob matched its staged/working hash; the committed path list exactly
matched the 14-file inventory. Normal `nix develop -c git commit -F` exited 0.
The repository declares no hook framework; its hook config files, core.hooksPath
and active non-sample hooks were checked and absent. No hook bypass occurred.

`git diff --cached --check` and the exact parent-to-commit `git diff --check`
both passed with **zero diagnostics**. This claim is only for the T9 14-file
change; it does not erase the historical source-identical whitespace exceptions
recorded above or imply a blanket branch whitespace pass. Raw CRLF code bytes
remain unchanged. The index was empty after the commit and yielded immediately
to the lead; no whole-worktree cleanliness claim is needed for unrelated owners.

This package ran no build, browser/service operation, push/rebase/default update,
production action or independent-review invocation. No migrations, pins, content
schema or rendering contracts changed. The lead owns combined final quick checks,
independent review and any later publication. All translations remain drafts
pending **human** review; main-agent wording acceptance is not human approval.
