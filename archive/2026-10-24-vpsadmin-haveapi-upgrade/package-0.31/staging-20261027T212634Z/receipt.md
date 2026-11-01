# KB staging attempt — 2026-10-27

## Current result: staged and verified

Lead superseded the initial no-reset restriction solely for our owned,
pending-null stale mirror. Fresh authoritative ownership/pending and exact four
reviewed hashes passed. Public `kb-stage reset --yes` completed exit 0 in
51.876 seconds at 21:33:05 UTC; it mirrored 114 CS + 77 EN pages, 226 media and
warmed 65 language pairs. The original failed attempt and retained bytes below
remain intact. No private-state edit or individual-page bypass occurred.

One fresh retained-catalog observer watched independent reset files only:
Luna/low, full-access/never, thread `01a17f47-6997-7f00-af4f-c19c1a9171ee`,
native utility `dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12`.
Its actual process policy was verified; observer launcher and exact parent reset
handle both completed exit 0. No utility launched/retried the mutation.

Fresh source guards, candidate hashes, public authentication and ACL checks
passed after reset. The sequential CS stage/verify and EN stage/verify commands
all exited 0, completed by 21:34:17 UTC. Native verification and bounded public
HTML reads confirmed rendered headings, Python/TypeScript/install code,
generated SDK distinction, corrected README factory pointer, reciprocal language
links and exact localized revision summaries. No browser/screenshot or broad
link campaign was needed.

| Page | Staged revision | Exact content SHA-256 |
| --- | ---: | --- |
| [CS article](http://kb-cs.aitherdev.int.vpsfree.cz/navody/vps/api) | 1793136820 | `f7c86a960d674a92f9d9da87e7fc9516f323b851c795aa119c7c70e142c8ff48` |
| [EN article](http://kb-en.aitherdev.int.vpsfree.cz/manuals/vps/api) | 1793136839 | `03e26d721d92ddb5d3158fb39e9964bc68a36568aaf462ecb170926dadf26480` |

[CS history](http://kb-cs.aitherdev.int.vpsfree.cz/doku.php?id=navody%3Avps%3Aapi&do=revisions)
shows: **Doplnění klientů pro Python, Rust a TypeScript včetně generických klientů 0.31.0 a závislostí generovaného SDK**.

[EN history](http://kb-en.aitherdev.int.vpsfree.cz/doku.php?id=manuals%3Avps%3Aapi&do=revisions)
shows: **Add Python, Rust and TypeScript clients, generic client version 0.31.0 and generated SDK dependencies**.

Final authoritative state at 21:34:17 UTC: owner
`2026-10-24-vpsadmin-haveapi-upgrade`, container up, pending English manifest
`kb-release-en.yml`, SHA-256
`3d9f5b61436b0c5b76a06cec89f33a09b1fd2a0211e8954177c912693f414b97`.
Only one pending manifest is retained by the public tool; both staged page sets
remain available. Staging ownership/pages are retained for user review.

Evidence: [reset result](owned-reset-result.json),
[reset observer result](reset-observer-final.txt),
[after-reset command exits](after-reset-commands.json),
[fresh production guards](production-guards-after-reset.json),
[CS verify](after-reset-cs-verify.log), [EN verify](after-reset-en-verify.log),
[rendered content/revisions](rendered-and-staged.json),
[final ownership/pending status](status-final.json).
Candidates/manifests/prose are unchanged: generic 0.31.0 and generated SDK
0.1.1/runtime 0.30.2 remain explicit. No 0.31.1 availability query, production
write/promotion, staging stop/release, cluster operation, Git/index mutation or
session lifecycle action occurred. Internal DNS/network access is required;
these are development staging URLs, not production publication.

## Historical first attempt: stale mirror refusal

**Blocked before page writes by stale retained staging content.** The reviewed
D4-A1 candidate/manifests hashes match the current table in `../kb-checks.md`.
No article/prose/file regeneration occurred. No 0.31.1 package query was made;
the intended release remains generic 0.31.0 and SDK 0.1.1/runtime 0.30.2.

Exact session/current was verified; ambient markers were absent and both bound
markers were exported for the public commands. Current routed KB/lifecycle
guides and selected tool help/source were read. E2 owns the watcher, so the
sequential bounded attempt used visible parent fallback without a new utility.

Fresh staging status at 21:28:58 UTC was owner=null, pending=null. Public
`kb-stage start` exited 0; staging is now owned by
`2026-10-24-vpsadmin-haveapi-upgrade` (claimed 21:28:59 UTC), container up.
Public `kb-page whoami` succeeded and ACL was 255 on both exact target pages.
Fresh production page-info/content/page-info checks match original guarded
revisions and hashes in [production guards](production-guards.json).

Public EN stage exited 1 at 21:29:22 UTC:
`staging is not a clean production mirror at manuals:vps:api`.
The selected canonical tool fails in its staging-baseline check before any
page/media write. It set the ordinary managed ref to master and invalidated an
already-null pending record; it did not publish a new pending bundle.
There was no retry, CS stage or successful release verification.

Read-only reconciliation found both retained pages differ from production and
candidate; copies remain local evidence:

| Page | Retained staging revision | Retained SHA-256 |
| --- | ---: | --- |
| EN `manuals:vps:api` | 1789385312 | `3be3d97ff87ec2b59953eb305c6f1baa695db56c9e9ffdc4b92bdac28b082ed6` |
| CS `navody:vps:api` | 1789385242 | `90380a19157a568577bce1850b736e2285ed576c4ae0c365c18e7cf82da37da6` |

Exact [retained baseline](retained-baseline.json), [command exits](commands.json),
[stage failure](en-stage.log), and [post-failure owner/status](status-after-failure.json)
are preserved. No owned staging reset was authorized in this release, so none
was run. No foreign ownership action, discard, stop/release, individual-page
overwrite, production promotion, cluster operation or workaround occurred.

Staging stays owned/up with pending=null. The reviewed pages have **not** been
staged; rendered headings/code/reciprocal links and localized revision summaries
are not accepted by this failed attempt. Lead disposition of the stale baseline
is required before continuing through the canonical path.
