# 2026-08-14-kb-updates

## Goal

Modernize the requested Czech vpsFree KB articles, provide reciprocal English
pages, preserve renamed URLs with localized move stubs, retire obsolete pages,
and prepare the exact result for review in the staging KB. Keep production
unchanged until the user explicitly approves promotion.

## Affected repositories

- `vpsfree-kb-contracts`: canonical Czech/English Guix and GRE articles,
  runtime tests, article registry, and WebUI navigation/screenshot
  source-page bindings and generated SSH host-key captures.
- Top-level coordination workspace: fetched KB sources, generated candidates,
  release manifests, and initiative tracking.

The remaining articles stay wiki-owned and are represented only in the local
release candidates.

## Approach

1. Fetch a fresh, checksummed Czech and English production snapshot, including
   expected-new canonical page IDs.
2. Rewrite SSH, firewall, Docker, Snap, WireGuard, Guix, and NixOS Mailserver
   as reciprocal Czech/English pages. Use informal singular Czech.
3. Keep the old Docker, Snap, and Mailserver IDs as localized move stubs.
4. Retire the generic Nginx, obsolete NixOS Nginx/getting-started, OpenShift,
   and OpenWrt WireGuard pages from staging.
5. Manage Guix and GRE in `vpsfree-kb-contracts`; test current Guix
   reconfiguration and deployment plus transient and persistent GRE tunnels.
6. Update homepage links, reciprocal language mappings, navigation annotations,
   existing SSH screenshot source bindings, and add localized host-key
   fingerprint captures.
7. Build schema-3 candidates and localized release manifests, stage the exact
   pages and deletions, verify the staging result, and leave staging claimed for
   user review.

## Compatibility and deployment

- Renamed URLs remain valid through move stubs; no DokuWiki redirect plugin is
  assumed.
- No API, protocol, database, persisted-state, or machine configuration format
  changes are involved.
- Guix and GRE test/article additions are backward compatible with the existing
  contract registry. Existing Docker and Snap runtime coverage remains in
  vpsAdminOS and is not duplicated; the current Ubuntu Snap image test is used
  as validation evidence.
- The contract branch must be fast-forwarded to `master` before staging so
  managed-source links and hashes resolve. Production remains untouched and
  rollback is simply not promoting the staged manifest.
- Staging is global and serialized by `VPSFREE_DEV_SESSION_SLUG`; retain its
  ownership until the user finishes review.

## Testing plan

- Run repository static checks and article-contract tests in the pinned Nix
  development shell.
- Validate generated all-page candidates, source hashes, managed markers,
  reciprocal translations, annotations, release manifests, and staging state.
- After quick checks and committed changes, run the mandatory standalone change
  review and resolve significant findings.
- Regenerate and visually review the Czech and English SSH host-key captures.
- Run `kb/guix#reconfigure` and `kb/gre#tunnel` sequentially through the
  vpsAdminOS test runner, then run the existing current Ubuntu Snap image test.
- Push the feature branch, inspect GitHub Actions, fast-forward `master`, then
  stage and verify both localized manifests plus explicit retired-page deletes.

## Review follow-up

The staged review keeps the accepted firewall page and revises the remaining
feedback as follows:

- streamline SSH, add localized vpsAdmin address and host-key screenshots, and
  make remote-console recovery explicitly reassuring;
- remove the confusing Snap `/lib/modules` prohibition while explaining that
  the historical snapd requirement is fixed and current templates prepare the
  directory;
- shorten NixOS Mailserver to an introduction, upstream setup/release links,
  and MXToolbox-based external checks;
- restore the original `guix deploy` use case as a current, tested
  configuration that imports the maintained vpsAdminOS module;
- manage and test a bilingual GRE article, including corrected transient and
  Debian ifupdown configurations;
- add the English GRE and descriptive Postfix links to the English index.

The follow-up uses the same branch and worktree group. Contract commits already
merged at `d85cadc` are immutable; new focused commits are appended and master
is fast-forwarded again after review and tests. The original managed-page
reconciliation base remains `5bf06beccdd29c333f04bb044a7610cee5ccda3d`
because none of the first staged managed pages has been promoted to production.

## Second review follow-up

The second staged review keeps the accepted article structure and makes these
additional changes:

- remove remaining historical-workaround prose from Docker, Snap, GRE, and
  WireGuard, and establish the same current-state rule for future KB work;
- streamline SSH root-login wording and explain recovery through the remote
  console's start-menu shell without referring to a local password;
- manage the bilingual firewall article, lead with simple dual-stack iptables
  and nftables configurations, and retain UFW, firewalld, and NixOS as tested
  alternatives;
- use `/32` examples from the vpsFree playground range in GRE and WireGuard,
  while substituting documentation addresses only inside isolated GRE tests;
- describe GRE as a trusted vpsFree-internal-network tool, and refine the Guix
  wording and NixOS cross-reference without changing its tested deployment.

All five firewall paths are runtime-tested on suitable current guests. The
follow-up remains documentation- and test-only: it changes no live API,
protocol, database, persisted state, or deployed machine configuration.
Contract changes are appended as focused commits after `ccd7942`; production
remains unchanged until a separately approved promotion.

## Third review follow-up

The third staged review keeps the accepted release and makes these additional
usability changes:

- annotate the raw iptables and nftables examples and state the resulting
  policy explicitly in every firewall alternative;
- keep `DEBIAN_FRONTEND=noninteractive` in test harnesses only, never in the
  reader-facing firewall or KVM commands, and enforce that distinction in the
  managed-article contract checker;
- simplify the GRE trusted-network wording and correct the Snap feature-change
  workflow to match vpsAdmin's visible form and automatic VPS restart;
- replace `informace:novacci` and `information:new_members` with reciprocal,
  beginner-oriented first-day checklists linking SSH, console recovery, VPS
  management, backups, networking, and optional advanced topics while reusing
  the existing localized screenshots.

The compatibility and deployment assessment is unchanged: the update touches
documentation and documentation tests only. It changes no persisted state,
API, protocol, database, or live machine configuration. The complete release
will be rebuilt from current production, reviewed at a committed exact head,
tested in the affected firewall and KVM runtime paths, and staged without a
production promotion.

## Runtime workflow follow-up

After the exact-head matrix workflow completes, replace its per-page GitHub
Actions matrix and discovery helper with one self-hosted job. Run the complete
repository test inventory once with `--jobs auto` so the test runner owns
parallel scheduling and enforces memory, shared-memory, and CPU limits across
that invocation. The runner records machine counts as metadata but does not
enforce a separate VM-count ceiling; concurrent runner processes also do not
share one resource pool. Retain contract checks, failure artifacts, result
evaluation, summaries, and cleanup. Do not run a separate discovery or preview
command: the one unfiltered `test` invocation runs the complete repository
  inventory. Keep the `kb-runtime`
  tags and `kbPage` labels as page-contract metadata and useful local
selectors, not as a mechanism for reconstructing the full CI suite.

This workflow-only change has no member-facing, persisted-state, API, protocol,
database, deployment-order, or rollback compatibility impact. It is rolled
back by reverting its focused commit. Verify the latest imported action refs,
run actionlint and the full quick suite, obtain a fresh standalone review, then
push and validate the new one-job workflow before integrating and rebuilding
the exact-head KB manifests.

If the unified run reproduces the pre-existing KVM delegated-IPv6 source flake,
make the synthetic guest's static networking deterministic instead of accepting
a blind rerun. Disable RA/SLAAC before bringing up its interface and bind the
default IPv6 route to the configured source. Review that fixture change as a
separate commit, run the focused `kb/kvm#networking` path, and only then rerun
the complete one-job workflow.

## New-member rendering follow-up

The final staging review found that DokuWiki splits lists when screenshots or
wrapped continuation lines interrupt them. Rewrite the reciprocal new-member
pages as a linear onboarding flow headed `Informace pro nové členy` and
`Information for new members`: log in with the credentials from the welcome
email, check membership and payment, find the VPS, choose password or SSH-key
access, recover through the console, and continue into basic or advanced
guides. Use standalone subsections around screenshots, keep any remaining list
item on one physical source line, and remove the monthly-traffic screenshot
while retaining its guide link.

Recapture the localized member and VPS lists with the full horizontal vpsAdmin
menu above the page title and table. Preserve their existing capture and media
IDs, add semantic contract paths for login and the Members menu, refresh the
candidate-aware navigation inventory, and include all four updated media
variants in the complete guarded release. Also remove unsupported Red Hat
Enterprise Linux from the reciprocal Docker installation lists and order the
remaining template distributions alphabetically.

This follow-up remains documentation- and capture-only. It has no persisted
state, API, protocol, database, runtime, deployment-order, or mixed-version
compatibility impact. No managed article command changes, so no managed VM
runtime suite is required. After focused commits and quick validation, obtain a
fresh mandatory review, rebuild the full exact-head candidates and manifests,
and restage both languages without promoting production.

## Humanized bilingual writing follow-up

Pin the reviewed English and Czech Humanizer skills in the coordination
workspace and add a concise vpsFree wrapper. Require the wrapper in both the
workspace and `vpsfree-kb-contracts` authoring instructions. The task-owning
agent applies it directly after factual work; a fresh subagent reviews the
result. There is no automated Humanizer or AI-text checker because stylistic
quality is not a deterministic property.

Apply the English and Czech profiles independently to all 29 changed pages in
the exact staged release. Preserve DokuWiki structure, semantic tags, links,
media targets, technical claims, and tested commands. Give Czech pages Czech
explanatory comments in scripts and configuration blocks and English pages
English comments. Represent these as localized display fixtures in the article
contract, require their non-comment lines and directives to remain equivalent,
and execute the shared command stream only once.

Keep the Czech onboarding title `Informace pro nové členy`, remove its final
introductory reassurance, simplify the repeated login wording, and explain in
the membership section that a new member can test the VPS for one week before
paying. Add the same trial information naturally to the English counterpart.

This remains documentation, authoring-policy, and test-contract work. It changes
no API, protocol, database, persisted state, runtime behavior, or deployment
ordering. After focused commits and quick checks, run the mandatory standalone
review, the complete 12-script runtime inventory in one parallel test-runner
call, rebuild both manifests, reset and restage the owned review KB, verify all
29 pages and intended retirements, and leave production untouched.

## Locale-specific Humanizer packaging follow-up

Rename the imported skills to `humanizer-en` and `humanizer-cs`, using the ISO
639-1 Czech language code and no compatibility aliases. Keep only the prompt,
license, and OpenAI UI metadata needed at runtime; record upstream revisions,
upstream hashes, local hashes, and deliberate deviations in the stable
`vpsfree-user-facing-writing` wrapper.

Correct the Czech adaptation by preserving the original English MIT copyright
notice, keeping vague attribution unless the user authorizes a content change,
and replacing its unsupported one-dash quota with functional Czech typography.
Retain valid en dashes for ranges, relations, pauses, contrasts, and
parenthetical boundaries.

This is workspace authoring-policy packaging only. The contract repository
continues to invoke the stable wrapper, so it needs no matching rename. Existing
KB candidates, staged pages, runtime evidence, and production state do not
change. Validate the three skill packages, recorded hashes, file types and
modes, stale references, fresh-context English/Czech behavior, and the focused
commit series before an independent mandatory review and push.

## Per-page release summaries follow-up

Replace the single release-wide DokuWiki summary with a bilingual changes file
that gives every page write or deletion its own informative summary. Generate
schema-4 release manifests from that file, show and verify the exact summaries
in staging revision history, and reuse them unchanged during production
promotion. Keep schemas 1–3 and the legacy `--summary` interface compatible for
already prepared artifacts, but require schema 4 in the documented workflow for
new releases.

Represent page removals as guarded manifest entries instead of out-of-band
commands. A deletion records the expected production revision and content hash,
uses the same localized summary in staging and production, verifies that the
page is absent afterward, and supports safe retries only when the latest
revision summary also matches. Extend cleanup manifests with per-page summaries
while retaining schema-1 compatibility; media deletion remains summary-free.

This changes only release tooling, manifests, tests, and documentation. It does
not alter production or staging content as part of implementation. Old release
manifests remain usable, and schema-4 promotion remains guarded against source
drift, ACL failures, and mismatched staged or partially promoted summaries. Run
quick tests and the mandatory standalone review before a staging-only smoke test
of page writes and deletions. Never promote the smoke-test manifest.

## Branch-safe managed-page links follow-up

Replace full GitHub URLs in `<kb-managed>` with repository-relative article
paths and test-runner patterns such as `kb/firewall#*`. Configure the DokuWiki
plugin with the repository URL and either production `master` or a staging ref
file. A staged managed release writes its exact committed and pushed contract
revision to that file, so feature branches can be reviewed without merging to
master or redeploying aitherdev for every update.

Extend release provenance with the managed test source and checksum. Staging
must fail before writing when the exact commit is unpublished or differs from
the manifest. Production promotion must fail before writing until remote
`master` contains the exact managed article and test files. Keep old full-URL
markers and existing release manifests readable during rollout.

Make the localized managed-page edit notice as prominent as a warning note,
without depending on the note plugin's CSS. Preserve escaping and visible
diagnostics for untrusted or malformed tags. Migrate all eight Firewall, GRE,
Guix and KVM page markers, while leaving their article prose and executable
samples unchanged. Keep the existing one-call, all-tests parallel runtime
workflow.

The user will deploy the prepared aitherdev configuration. After quick checks,
commits, mandatory standalone review and configuration builds, stop and provide
the exact deployment revision. Resume live staging validation only after the
user confirms deployment. Production configuration deployment and KB promotion
remain separately approval-gated.

### Managed warning wording follow-up

Limit the bilingual edit warning to the one relevant fact: automated tests do
not cover changes made only in DokuWiki. Remove the claim that a later
repository release may overwrite such edits, because publication is a
deliberate operation rather than an accidental background update.

Keep the warning title, accessibility attributes, prominent presentation,
source and test links, selector, and editing-guide link unchanged. Update the
plugin's focused regression expectations and pin that plugin revision in both
staging and production configurations. The already staged KB page content and
contract revision do not change.

The deployed aitherdev generation still contains the prior wording, so the user
must deploy the new configuration revision before live staging verification.
The change has no persisted-state, API, protocol, database, or mixed-version
impact. Rollback is the previous plugin pin. Production configuration and KB
publication remain separately approval-gated.

## Managed-page terminology follow-up

Rename the canonical managed-page registry from `contract/articles.yml` to
`contract/pages.yml` and migrate its schema from 1 to 2. The schema uses a
top-level `pages` mapping, `variants` for the Czech and English sources, and
page terminology throughout runtime labels and generated provenance. New test
metadata uses `kbPage`; new candidate and release metadata uses `page_key` for
the stable registry key and `id` for a language-specific DokuWiki page ID.

The DokuWiki `<page>` tag is the shared identifier that connects translations.
Both variants must use the same value, derived from the English KB page ID.
Correct every managed English source, not only Guix, and enforce the invariant
in the page-contract checker and authoring instructions.

Replacement-plan schema 5 uses `managed_pages`, and release-manifest schema 5
emits the new terminology. The release loader continues to accept existing
schema-4 manifests so the current staged bundle and rollback evidence remain
readable, but new managed-page artifacts use schema 5 only. The change affects
documentation tooling and metadata, not commands in the managed pages or live
VPS behavior. Run quick suites, a standalone mandatory review, and then the
single complete 12-script runtime workflow. Rebuild and restage both localized
manifests at the new exact contract revision; production remains unchanged.
