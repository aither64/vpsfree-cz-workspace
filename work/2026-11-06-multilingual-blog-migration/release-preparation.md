# P18 production rollout plan

Local preparation is complete and ready for your staged rollout. Both final
feature heads are published; source review, native builds, the exact blog
artifact, scoped nginx checks, isolated fixed-CLI integration and applicable CI
are accepted. You perform integration, deployments, credential provisioning and
live GitHub/forum setup. The team has made no production change. Keep WordPress
public until the private static site and recovery checks pass.

| Prepared input | Exact source and current evidence |
| --- | --- |
| Blog | `82a1ee3c90990e56cfde0da28ababed8f0444441`, tree `d23e142cee504f6284ed0bbc4b028be6b8935e8c`; includes E18/B18, D19 `5032d82` and A18 documentation. All 125 English articles have your review approval. |
| Configuration | `1e840b8056bbc700ca3e9cd832f0d9301da52652`, tree `6f6d2020345f731370698be3ed2ff7fe25ac637e`; includes H18 `937fd371`, corrected A18 publication and the direct `/feed/` fix. Default enable flags remain off. |
| Completed checks | H18 mode/540-alias projection checks; corrected A18 21 pure release cases, 19 webhook cases and six actual UID/capability namespace cases; normal hooks; D19 source/regex/document checks. Earlier module evaluations cover unchanged settings, not a newly built corrected system. These prove their recorded source, not deployed behavior. |
| Review and artifact | A18 affected review at `15ad7646` remains valid for unchanged scope; the two-file feed fix at `1e840b80` passed its focused generated fixture and lead inspection. Exact blog `82a1ee3` artifact/input graph and all 2397 served hashes are accepted, with 125 articles/indexed pages and ten feed entries per language; accepted `7fa57c80` visual proof is reused for later documentation-only changes. |
| Runtime evidence | Exact `1e840b80` native two-node builds and full input/output proofs are accepted ([native proof](h18-refresh-config-build-proof.json)). Nginx proof combines 558 valid unchanged observations (540 aliases plus 18 cases) with 14 new passing feed/mode cases; both feeds return 200/RSS ([HTTP proof](h18-nginx-runtime/final-proof.json)). The original feed500 and fix history remain below. These are compiled-default and adapted loopback checks, not live deployment proof. |
| Functional integration | A18I is accepted: 28 observations passed in 6.522 seconds at exact `1e840b80`, using registered fixture `8df97376-df93-4247-a811-69811e3fd122`, real private NSS/fixed CLI/HTTPS adapter and unchanged compiled policy ([result](a18-fixed-cli-rehearsal/final-output/result.json), [source/NAR proof](a18-fixed-cli-rehearsal/realization-proof.json)). Pause/defer/resume, rollback, duplicate and generation/policy checks passed; final state is paused. |
| Feature publication and CI | Both exact heads above were published by ordinary SSH fast-forward, with remote blog `main`/HEAD at `0354dac281978867ea8c1553b092ce19bccb5ccd` and configuration `master`/HEAD at `5941cdb3dda259e91c6a988a7dbf08c84700b326` unchanged ([blog proof](b18-publication-proof.json), [configuration proof](h18-config-publication-result.json)). [Build blog run 42411255497](https://github.com/vpsfreecz/blog/actions/runs/42411255497), attempt 1, passed checks and the Nix build at exact `82a1ee3c`; protected-main packaging/upload were skipped, with zero artifacts. Configuration has no applicable feature-push CI; no workflow was dispatched. |
| User-run rollout checks | Real host systemd.path/LoadCredential/NixOS switching, live credentials/GitHub delivery, enabled deployment/TLS and the forum pilot remain your later checks. The isolated test uses synthetic DNS/CA/API and a recorded fixed-systemctl trigger. Feature CI supplies no protected-main eligible artifact; step 3 establishes that release evidence. |
| English host | DNS already points to `proxy.vpsfree.cz` on public/internal resolvers and all three authorities. The HTTPS check in E18DNS found a certificate-name mismatch. H18 supplies the missing TLS/vhost options; no DNS installation is needed. |


Accepted local outputs, with full input/NAR/derivation receipts linked above:

- Blog artifact: `/nix/store/zd9ip2lyjpc52pwhn4rpihd3kz2rrfhx-vpsfree-blog-0` ([artifact proof](b18-artifact-proof.json)).
- Blog system: `/nix/store/04fyz2bcfb2xx5hv0rzna6kmkhha699k-nixos-system-blog-26.05.20261026.718f670`.
- Proxy system: `/nix/store/a2b5d14vj9rkzlm8sv2j5v0kcf9vplc8-nixos-system-proxy-26.05.20261026.718f670`.
- Integration source package: `/nix/store/n0869rky0g7pm7azw94gjlypa4ssb9bg-blog-publication-source`, NAR `sha256-Va+ewaBQortvfqv/osefwI4Ks0PLgS83ORRqgWzyzDw=`; its compiled policy and result digest are bound in the linked A18I proofs.

The tested legacy redirect set covers 540 captured aliases. Recorded historical
daily-archive and pagination output coverage remains 0/124 and 35/41 respectively,
unchanged from the earlier artifact. Manifest inventory is not proof that those
additional routes are generated; the B18 receipt preserves this coverage limit.

The [configuration operations guide][operations] owns the publication commands
and hosting contract; the [blog release guide][release] owns Actions/artifact
behavior; the [discussion guide][discussions] owns the exact forum setup and
pilot. Historical receipts below remain evidence for their named revisions.
Operator opt-in edits produce new configuration revisions/generations that must
be built and recorded; do not call their enabled outputs identical to the
default-off build.

## 1. Verify the prepared source and prepare recovery

Use the published heads and accepted evidence above. Before integration or
deployment, compare your checkout and fresh remote defaults with those heads;
review and revalidate any later changes. You choose when to integrate the
reviewed blog into protected `main`; the feature branch alone cannot produce an
eligible release artifact.
Configuration integration is separate, and an enabled configuration can be
deployed from its reviewed feature revision. No default-branch action is implied
by this plan.

Retain the current system generations and complete input graphs for
`cz.vpsfree/containers/int.blog` and `cz.vpsfree/containers/prg/proxy`. Back up
and verify recovery of the WordPress database,
`/var/lib/wordpress/blog.vpsfree.cz`, uploads/fonts, secret-key state and
existing owners. Keep the original public route and a runnable old generation.
The migration snapshot is not an atomic final cutover backup. Store private
backups and credentials outside Git and this record. Do not delete data, change
ownership recursively or prune generations/releases.

## 2. Supply operator settings and deploy coexistence

Verify the GitHub repository ID for `vpsfreecz/blog` and workflow ID/path for
`.github/workflows/build.yml` (**Build blog**) through GitHub's
repository/workflow API. Confirm protected `main`, the repository's allowed
90-day artifact retention, and a credential that can read
repository/branch/run/artifact facts and download artifacts. It needs no push,
dispatch or administration write authority. Verify outbound HTTPS from the blog
target to GitHub API and artifact storage.

Provision separate root-owned mode 0600 runtime files using your existing secret
provisioning method: an exact nonempty HMAC secret without trailing newline, and
the read-only GitHub token. Use absolute file strings outside the Nix store, not
Nix path values. Only paths and verified IDs go into configuration; no secret
contents, signatures or signed download URLs go into commands or records. The
units pass each secret only to its intended user through `LoadCredential`.

Add these options to the existing machine configuration files; replace the ID
and path descriptions with verified values:

| File / option | Initial coexistence value |
| --- | --- |
| `cluster/cz.vpsfree/containers/int.blog/config.nix`: `services.vpsfree-static-blog.enable` | `true` |
| Same: `services.vpsfree-static-blog.publication.enable` | `false` for stage-only delivery first |
| Same: `services.vpsfree-static-blog.publication.repositoryId`, `.workflowId`, `.tokenFile` | Verified repository/workflow IDs and absolute read-token file; prepare these for step 4 |
| Same: `services.vpsfree-blog-webhook.enable` | `true` |
| Same: `services.vpsfree-blog-webhook.repositoryId`, `.workflowId`, `.secretFile`, `.tokenFile` | Same verified IDs/read-token file, plus distinct HMAC file |
| Same: `services.vpsfree-static-blog.pull.enable` | Leave `false`; polling is unsupported |
| `cluster/cz.vpsfree/containers/prg/proxy/config.nix`: `services.vpsfree-blog-proxy.enableEnglish` | `true` |
| Same: `services.vpsfree-blog-proxy.serveStatic` | `false`; CZ remains WordPress, EN returns 503 |

Build from the configuration checkout, then deploy the backend before the proxy:

```sh
nix develop --no-write-lock-file --no-update-lock-file -c confctl build --yes '{cz.vpsfree/containers/int.blog,cz.vpsfree/containers/prg/proxy}'
nix develop --no-write-lock-file --no-update-lock-file -c confctl deploy cz.vpsfree/containers/int.blog switch
nix develop --no-write-lock-file --no-update-lock-file -c confctl deploy cz.vpsfree/containers/prg/proxy switch
```

Before each deployment, confirm confctl selected the exact generation just built
for that machine. Record its source, inputs and system path. If publication
state already exists from an earlier attempt, run `blog-static-release
maintenance-enter` as root on the blog target before a system switch; do not
bypass the native check. A first installation with no publication state needs no
fabricated control files.

Verify existing WP/PHP/database/cron health, public Czech WP content and
unchanged accounts/data. Private 8080 accepts only the metadata-resolved proxy
IPv4; the receiver is loopback 8091. The Czech exact route
`https://blog.vpsfree.cz/_hooks/github/build` goes through proxy HTTPS → blog
port 80 → loopback 8091 with fixed `Host: blog.vpsfree.cz`. It remains there
after cutover. No inbound GitHub SSH, public ports 8080/8091 or English webhook
endpoint is needed. Verify the English certificate normally, without `-k`, and
its prelaunch 503. Stop on a failed build, health check, certificate or
unexpected public-route change.

## 3. Test the real Actions artifact and stage-only webhook

After you integrate the intended source into protected `main`, its push run must
pass `bin/check`, `bin/check-release`, `nix build .#site` and upload
`blog-<SHA>`. An existing manual workflow run on that same protected-main SHA is
also eligible. Feature/PR runs test the build but skip release packaging/upload.
Do not relax eligibility or run an older main revision as proof of this
candidate.

Record the exact source/run/attempt/workflow/artifact identities and retention.
In repository webhook settings configure JSON, SSL verification, the matching
HMAC secret, the exact Czech URL above, and only **Workflow runs** events. A
valid signed ping returns 200 without work. A completed successful eligible run
returns 202 promptly after durable enqueue. The worker independently verifies
current protected main and the artifact before staging; payload hints cannot
choose an older release.

With publication disabled, verify the staged immutable archive/tree/receipt
under `/var/lib/blog`, the exact SHA/run and `activated=false`. Payload files,
archives and new directories are flushed before a completed stage receipt;
reused stages and retained CSS receive the required durability barrier before
pointer selection. A flush failure aborts eligibility or the switch. No current
pointer should be created on this first rollout; public WordPress remains
unchanged. Check safe outcomes in `/var/lib/blog-webhook/status.json`, without
dumping credentials.

Test duplicate redelivery and a controlled failure/retry while WordPress is
public. GitHub does not automatically retry failed webhook deliveries. After
diagnosis, redeliver the delivery in GitHub or, as root on the blog target, run:

```sh
systemctl start blog-webhook-work.service
```

Recover start-limited units through the normal operator procedure if necessary.
Missing/expired current artifacts require an authorized rebuild of that exact
SHA; the helper never falls back to an older build. Retain downloaded archives
and receipts in backups because GitHub retention expires. Stop before
publication if signature, identity, validation, acknowledgment or stage-only
behavior is wrong.

## 4. Enable publication and verify the private site

Set only `services.vpsfree-static-blog.publication.enable = true` in the
prepared backend configuration. Its IDs and read-token path must match the
webhook. Build and deploy that backend revision with the same commands scoped to
`cz.vpsfree/containers/int.blog`. Public proxy mode stays `serveStatic=false`.
Before a switch with prior publication state, enter maintenance. For the first
transition from stage-only with no current/control state, the native check
permits the switch and the newly installed control state defaults paused.

As root on the blog target, verify the selected system/policy, then run:

```sh
blog-static-release status
blog-static-release maintenance-exit
systemctl start blog-static-pull.service
blog-static-release status
```

Resume permits private content publication and wakes deferred webhook work. The
explicit pull is a one-time current-main acquire/validate/activate operation,
not a timer. The fixed service runs as `blog-release` and receives its token
through systemd credentials. Direct `prepare`, `pull` and `activate` commands
reject root and any other NSS account; use the fixed service for operator
publication. If resume already published the same release, repeat work is
idempotent. Confirm the current release key, receipt digest, source SHA and
selected system. A successful command does not switch public proxy routing.

From the proxy target, check the private language roots with their intended
Host:

```sh
curl --fail --show-error --max-time 10 -H 'Host: blog.vpsfree.cz' http://172.16.8.4:8080/
curl --fail --show-error --max-time 10 -H 'Host: blog.vpsfree.org' http://172.16.8.4:8080/
```

Compare to the final artifact: 125 articles per language, ten full-content feed
entries per language, original Czech GUIDs/dates, media/comment anchors,
separate search indexes and shared discussion identities. Verify direct RSS at
`/feed/`, representative aliases and query/fragment destinations, unknown
Host/PHP rejection and private rendered pages. Local H18 evidence covers all 540
exact redirects; public/private live spot checks confirm the deployed wiring.
Literal unknown or extra legacy identity keys return 404; percent-encoded key
aliases are outside the captured alias contract and must not infer an article.
Analytics is CS 4 / EN 10; previews stay tracker-free. The Discourse embed
remains false.

Exercise the rollback procedure in step 7 with two intended retained releases
when available. With only one release, record that no previous static release
exists; retain verified WordPress routing recovery and the local
transaction/crash tests. Do not fabricate an older eligible artifact. Stop on
mismatched bytes/routes, receipt corruption, stale-head refusal that has not
been diagnosed, or failed private serving. Keep public traffic on WordPress
while resolving it.

## 5. Prepare Discourse and make the public switch

Before exposing embeds, follow the [discussion setup guide][discussions] on the
actual installed forum. Configured source is Discourse 2026.9.1; verify the
installed version and live overrides. Inspect RSS polling at
`/admin/plugins/rss_polling`, existing exact source/topic mappings and category
subscriptions. Select one creator for this blog. Preserve matching
topics/replies; resolve unmapped discussions before allowing their import,
without fuzzy-title matching or duplicate topics.

At `/admin/customize/embedding`, choose a real public category and existing
import author, verifying their identity and member read/reply permissions.
Initially allow one exact pilot Czech source path. Add the English host with
reject-all path regex `\A(?!)\z`: it permits English framing through the pinned
CSP host behavior while authorizing no English source import. Keep
`embed_any_origin=false` and CSP framing protection on. Both translations retain
the same immutable HTTPS Czech URL.

Use `.entry-content` extraction. Retain the guide's exact HTML/truncation
settings, `embed_unlisted=false` and `import_embed_unlisted=true`: native
imports remain unlisted until a regular reply. This is not silent or private.
Check notifications, mailing-list subscriptions and forum-to-IRC/webhooks; do
not seed or crawl 125 topics. Keep the blog's global embed false until the final
static-page pilot passes.

Immediately before cutover, compare current WordPress posts/comments with the
capture. Refresh changed source, translations and affected artifact/checks if
needed; otherwise use the captured content. No writer freeze is planned, so this
remains a bounded delta check, not an atomic snapshot guarantee. Refresh
recovery backups.

When the private site, recovery and English certificate pass, deliberately set
`services.vpsfree-blog-proxy.serveStatic = true` in the proxy configuration.
Build and deploy only that proxy with the commands from step 2 using its
selector. Both public language roots now use port 8080; the exact Czech webhook
still uses port 80, and WordPress stays running. Verify both HTTPS roots,
representative legacy/feed/media paths, language switches and search. Record the
selected proxy generation and content receipt. A public failure uses the route
rollback in step 7.

## 6. Pilot discussions, then enable them

The [guide's bounded pilot][discussions] uses the forum-generated native snippet
in temporary DOM changes on the final Czech and English article tabs while the
source boolean stays false. Use the same Czech embed URL in both tabs. This can
create a topic and notifications; you perform it deliberately, not as a
read-only appearance check. Verify one shared topic under concurrent first
visits, final article-only extraction, anonymous reading, ordinary top-level
login/reply, English CSP/referrer behavior and cross-site cookie restrictions.
Reloading removes the temporary DOM changes; forum topics/replies remain.

After the pilot and existing mappings pass, apply the guide's anchored future
root-slug path rule on the Czech host. Keep the English reject-all rule. Enable
`[params.discourse] enabled = true` through a reviewed blog commit and
protected-main release. Preview/server/draft guards remain unchanged. No
per-article forum action, forum credential in CI or forum upgrade is needed for
subsequent posts. If installed behavior differs, keep the embed off and resolve
that precise discrepancy first.

Once publication is enabled and resumed, successful trusted-main builds trigger
webhook acquisition and automatic content publication. No further system deploy,
polling or workspace session is needed for ordinary articles. Retain
protected-main review policy and monitor failed delivery/acquisition outcomes;
automatic publication does not mean automatic retry of a failed GitHub delivery.

## 7. Maintenance and recovery

Before future backend system switches or rollback to an older generation, run as
root on the blog target:

```sh
blog-static-release maintenance-enter
blog-static-release status
```

Pause and pointer mutation share one stable lock. Root writes only its control
state. For content inspection, reconciliation and rollback, it uses a fixed
child that irreversibly drops to the `blog-release` UID/GID and configured
groups, with no saved root identity or capabilities. The child inherits the held
lock instead of reacquiring it. Queue writes use that same service identity
after the content lock is released; root then starts only the fixed worker.
Pause persists before returning, so an in-flight download cannot switch
afterward. Deploy and verify the intended system, then explicitly run
`blog-static-release maintenance-exit` to resume. Changed policy/system identity
stays paused until that step. Never bypass the pre-switch check, replace the
root control files or set the current symlink by hand. Paused webhook work is
retained without a polling loop and resumes without dropping newer pending work.
Corrupt or unknown receipts/pointers require diagnosis; keep publication paused
and use the retained public fallback.

For a static-content failure, choose an exact validated retained release key and
read the current receipt digest from `status`. As root, substitute those values:

```sh
blog-static-release rollback --release '<retained-release-key>' --expected-current '<current-receipt-sha256>'
blog-static-release status
```

Rollback persists pause before retained-target validation and stays paused after
success. Queued newer work cannot immediately undo it. This restores both
language roots and search together, without reverting the system or forum.
Resume only when current protected main is again the content you intend to
publish. No previous release means no static rollback target; use WordPress
recovery instead.

For public cutover recovery, set `serveStatic=false`, build and deploy the
proxy: Czech returns to retained WP port 80 and English returns 503. Keep
English TLS and the webhook route. If a backend system rollback is necessary,
enter maintenance first and select the recorded old confctl generation with its
supported `deploy --generation <generation> <machine> switch` interface; verify
the old services and leave content publication paused until a compatible policy
is restored.

Disabling the blog embed or narrowing the forum source-path rule stops new
imports; it must not delete topics, mappings or replies. Preserve direct
discussion links. WordPress cannot automatically consume new Git articles or
Discourse replies, so record them for reconciliation. Do not remove
WordPress/PHP/database data, prune releases or retire old generations during
this rollout.

## Evidence to record as each gate completes

Keep this one record current: final reviewed source heads; complete build input
and system paths for both enabled targets; previous generations/backups;
verified GitHub IDs/branch policy and delivery/run/attempt/artifact/receipt
identities; private and public checks; forum installed
version/category/author/pilot topic and notification results; current/previous
content receipts and tested recovery. Record credential paths only. Until those
facts are recorded, source preparation is complete but the corresponding
production step remains unverified. The superseded unpublished `9ea9fbd9` /
`3fb7d25` commits remain under recovery refs; their substantive fixes are
recorded below, without claiming patch equivalence or deployed lineage.

Command provenance: configuration pins confctl
`7bee58a52372b95c2198ce3f2a719807a3c2c66b`; its `lib/confctl/cli/app.rb`
declares `build --yes`, `deploy [machine-pattern [switch-action]]` and
`--generation`, while `lib/confctl/pattern.rb` enables brace patterns with
`FNM_EXTGLOB`. These commands were checked against that local pinned source, not
executed during plan preparation.

[operations]: ../../worktrees/2026-11-06-multilingual-blog-migration/vpsfree-cz-configuration/docs/operations/blog-static.md
[release]: ../../worktrees/2026-11-06-multilingual-blog-migration/blog/docs/deployment.md
[discussions]: ../../worktrees/2026-11-06-multilingual-blog-migration/blog/docs/discussions.md
---

# E0 inactive release-source checkpoint

Current independent BLOG checkpoint: feature `6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344`
(tree `c28f761c78714715a2c22e455782fa325188f12e`) is published and exact
[Build blog run42398048773](https://github.com/vpsfreecz/blog/actions/runs/42398048773)
passed. Lead accepted final T16 review, rooted1802-file/source-input proof and
actual8HTML privacy evidence. Production trackers use CS4/EN10 only on guarded
base-layout pages; preview/server output omits them. No tracker request was made.
Fresh SSH proof leaves main/HEAD at0354dac; protected-main package/upload steps
were skipped, artifact_count0. Config/workspace refs remain untouched. All refs,
results, previews and session remain open; no integration or activation is implied.
Current B16 artifact/publication/CI details are appended below.

Prior independent W15 BLOG checkpoint: feature `92ed3dca3120ffa3acae1b6efda6dfa974fb9dce`
(tree `cd8e3e7de8434fefd391e7ccf7706b74801fe019`) is published and exact
[Build blog run42390960159](https://github.com/vpsfreecz/blog/actions/runs/42390960159)
passed. Lead accepted final blog review/history, rooted1802-file/source-input proof
and focused U13 actual UI evidence. Fresh SSH proof leaves main/HEAD at0354dac;
protected-main package/upload steps were skipped, artifact_count0. H15/N15
configuration work remains independent and was not published or certified by
this operation. All refs/results/previews/session remain open. No integration,
activation, human English approval or cleanup is implied. Current independent
BLOG artifact/publication/CI details follow below.

Prior B12 checkpoint: blog feature `b5e3ebe54d9c42ab89142a1bcc50192e580fff10`
(tree `4e5248b97e53b7d34b9bf1a1ccf10d3ace54854d`) is published and exact
[Build blog run42373985435](https://github.com/vpsfreecz/blog/actions/runs/42373985435)
passed. Lead accepted mandatory review, rooted B12 artifact/input proof and focused
U12 runtime evidence. All1802 served-file hashes pass;141 Pagefind files, adapter
and native inputs are identical to accepted b29. Main-only package/upload steps
were skipped, with zero artifacts. Fresh SSH proof leaves main/HEAD at0354dac;
configuration7bab and workspace refs are unchanged. All roots/previews/session
remain retained. No merge, deployment, human English approval or cleanup is implied.
Current B12 details follow at the end of this existing receipt.

Prior R10 checkpoint: blog feature `b29f21bfa084d3b99e83d07ca8feb0b57afcfa6d`
(tree `15e46f8e619f60c82c07a612ec8360a4a1f286a6`) is published and exact
[Build blog run42370490884](https://github.com/vpsfreecz/blog/actions/runs/42370490884)
passed. Lead accepted mandatory review, R10 rooted artifact/input/Pagefind/search
proof and the final U10 actual runtime/browser packet. Main-only package/upload
steps were skipped, with zero artifacts. Default main remains0354dac; config7bab
and workspace refs are unchanged. No integration, production transition, human
English approval or lifecycle cleanup is implied. Historical checkpoints below
remain retained; current R10 evidence is appended last.

Prior published checkpoint: blog feature `f0337fb7eae8797efca9254cd7208949cb0f77e4`
(tree `b80d2261d92efe01c51946f97fec5cd45b32b0fe`) is published and exact Build blog
run [42360486251](https://github.com/vpsfreecz/blog/actions/runs/42360486251) passed.
R9 rooted artifact and U9 browser evidence were accepted by the lead before
publication. Configuration remains `7bab9781d0a5eb1aed5914f0aed99f6d7d491632`;
default branches are unchanged. Main-only packaging/upload were skipped, with
zero run artifacts. No integration, activation or session cleanup is authorized.
Earlier source/artifact/publication sections remain historical evidence.

Prepared by implementer0. This is source/fixture evidence, not deployment,
activation readiness, independent review approval or default-branch integration.
No production request, SSH, credential provisioning, service operation, machine
claim, activation/dry-activation or push was performed for E0.

## Exact source identities

- Blog E0 base: `b6b76192c61802c37fbc6cfdc0133c0bec1b3f07`.
- Blog E0 commit: `c4cf0220e313600f568524fc040cd13159669df3`.
  Eight files: build workflow, `bin/package-release`, `bin/check-release`,
  `docs/deployment.md` and the accepted AGENTS/README/authoring/skill factual
  reconciliation. No `bin/build`, flake, C0, corpus or translation changes.
- Blog's protected initialized base remains
  `0354dac281978867ea8c1553b092ce19bccb5ccd`. Its complete series at the immutable
  E0 checkpoint is listed below. Lead-assigned V2/history consolidation happens
  afterward; its owner supplies final old/new equivalence and final branch head.
- Configuration fresh default: `5941cdb3dda259e91c6a988a7dbf08c84700b326`.
- Refreshed DNS feature: `b4a7f22a46c16be453052a37ac98fc4c39401a9f`.
- Configuration E0 commit: `7bab9781d0a5eb1aed5914f0aed99f6d7d491632`.
  Six files: default-off module/import, configuration-owned helper, two fixture
  checks and `docs/operations/blog-static.md`. Configuration worktree/index were
  clean after commit. Blog index was yielded immediately after its E0 commit;
  V2's three dirty files were preserved.

Blog series at `c4cf0220`:

```text
d7b90f09e1edd6fb2b032057205c91d6df5c94ee Import the captured Czech WordPress corpus and public assets
818202f7b48e8031acb49641360b2402bc4e679b Preserve the original Flat design around the imported archive
e9c286b2f403603907265ac28f4bd38b3ae00227 Align authoring instructions with the imported blog
e8aed2ef787217e8085d782e38a760cd51ddbd90 Translate 63 archived articles into English drafts
c3786b74af9ee9382af4cc44428e7e77965753ea content: draft 62 English archive translations
b6b76192c61802c37fbc6cfdc0133c0bec1b3f07 Prepare opt-in native discussions for production articles
c4cf0220e313600f568524fc040cd13159669df3 Prepare checked immutable blog release artifacts
```

Configuration series above its fresh default is exactly the refreshed DNS
feature followed by E0. [Configuration refresh evidence](configuration-refresh.md)
retains old `85b38f1c..133a94b6`, new `5941cdb3..b4a7f22a`, protected old source
ref and matching record-payload digest. This is semantic equivalence: the removed
SOA predecessor changed from `2026093000` to `2026110200`; feature serial
`2026110600` is strictly newer. The exact A/TTL/public-CNAME boundary is unchanged.
No literal patch equivalence or reuse of old DNS builds is claimed.

## Checks and source boundaries

- Tiny offline producer fixture: `nix develop -c bin/check-release`, passed.
  Covers clean exact source identity, dirty/null rejection, undeclared payload
  and deterministic tar/receipt bytes. Dirty author previews remain supported.
- Workflow YAML parsed with Ruby YAML; read-only contents permissions and seven
  steps verified. Feature/PR jobs cannot publish eligible main artifacts.
- Target: `python3 tests/blog-static-release.py`, six tests passed. Covers mocked
  trusted API acquisition, missing/expired exact artifact, wrong identity,
  unsafe/duplicate/link/device archive entries, hash mismatch, admission refusal,
  stale head including the final switch boundary, concurrent receipt exclusion,
  interruption reconciliation, retained immutable CSS and explicit rollback.
- Nix module fixture passed using the repository's pinned `nixpkgsStable`:
  effective disabled state is identical to the existing hardened WordPress
  configuration; original vhost root/listen are preserved. Separate candidate
  roots/feed/PHP denial/unknown-host rejection and refused scheduler are checked.
  Exact executed command, from the configuration worktree:

  ```sh
  nix eval --impure --json --expr 'import ./tests/blog-static-module.nix { nixpkgs = (builtins.getFlake (toString ./.)).inputs.nixpkgsStable; }'
  ```
- Protected-source comparison against fresh configuration default found no
  changes to WordPress, existing health checks, proxy, forum, public DNS, flake
  inputs or locks. The sole DNS diff is the retained N feature above.
- Configuration Nix files formatted with the declared Nix formatter. Normal
  Overcommit pre-commit and commit-message hooks passed. Commit-message width
  produced nonblocking 72-column warnings; all lines satisfy the workspace's
  80-column maximum. No hook bypass. Documentation local links/examples and
  owned staged whitespace checks passed; lead accepted all final prose.

Upstream action refs verified before use:

| Action | Tag | Pinned commit |
| --- | --- | --- |
| actions/checkout | v7.0.1 | `3d3c42e5aac5ba805825da76410c181273ba90b1` |
| cachix/install-nix-action | v31.11.3 | `75c75c31ebece974e48ebc36b4ad125bd97bd97b` |
| actions/upload-artifact | v7.0.2 | `cf430e030ddbb5b0abf93d22962f4752f3646cd9` |

The workflow requests 90-day retention, subject to repository policy. The target
must retain exact archives/current/previous releases/receipts independently;
expired current-SHA artifacts require an exact-source rebuild, never an older
fallback. No production build is introduced.

## Remaining gates

Independent final review and any longer exact-head configuration build remain
pending; no long system build was run before review. No live Actions run,
artifact download, Nginx service, target activation or runtime admission test is
claimed. Required operator facts remain workflow ID, protected branch policy,
artifact read credential/visibility, outbound download route and retained backup.
The timer is default-off and enabling it fails evaluation; production pull,
activation and rollback CLI paths refuse `machine-admission-unavailable`.
Pure fixture callbacks are not a production coordinator bridge.

Legacy query/alias serving, English public DNS/TLS, forum runtime setup and the
actual proxy transition still require their own approved/verified work. No
formal writer freeze is planned; perform the requested brief pre-switch change
check and refresh capture only if needed. No deployed head, system/profile store
path, machine claim or integration evidence exists for E0 because none was
executed. No migrations, input-pin streams or default-history rewrites were added.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/)

## Refreshed exact-head DNS parsing

```json
{
  "configuration_head": "7bab9781d0a5eb1aed5914f0aed99f6d7d491632",
  "source_path": "configs/internal-dns/zone.vpsfree.cz.",
  "source_sha256": "f0287f6c9d8950e286155451d15d6724b0018a1967327272ee4da2c705b54087",
  "tool": "/nix/store/2q7r6d5awv41lb810xdczlc8ym4disla-bind-9.20.29/bin/named-checkzone",
  "checks": [
    {
      "fqdn": "ns1.int.prg.vpsfree.cz",
      "exit": 0,
      "serial": 2026110600,
      "materialized_sha256": "38dd3358f8bb79f2a7a6262eb802301929a9be63fbdce7395e77029d23ce5c07",
      "answers": [
        {
          "owner": "blog.vpsfree.cz.",
          "ttl": "3600",
          "class": "IN",
          "type": "CNAME",
          "answer": "proxy.vpsfree.cz."
        },
        {
          "owner": "blog.int.vpsfree.cz.",
          "ttl": "3600",
          "class": "IN",
          "type": "A",
          "answer": "172.16.8.4"
        }
      ]
    },
    {
      "fqdn": "ns1.int.brq.vpsfree.cz",
      "exit": 0,
      "serial": 2026110600,
      "materialized_sha256": "27a7e602e95e703c28dd8d6eb4d17d70714501d34936cabed3149fbcc68f4e9d",
      "answers": [
        {
          "owner": "blog.vpsfree.cz.",
          "ttl": "3600",
          "class": "IN",
          "type": "CNAME",
          "answer": "proxy.vpsfree.cz."
        },
        {
          "owner": "blog.int.vpsfree.cz.",
          "ttl": "3600",
          "class": "IN",
          "type": "A",
          "answer": "172.16.8.4"
        }
      ]
    }
  ],
  "scope": "Two offline materializations only; no live DNS/network/build/activation."
}
```

These results verify the refreshed E0 zone source, not the old DNS build or deployed state.

## Post-review disabled-system build

Watcher-owned command: `nix develop -c confctl build --yes cz.vpsfree/containers/int.blog`.

```json
{
  "auto_rollback_program": "/nix/store/yl9vnin9wlv04cip0sqpkisk80xmccwh-auto-rollback.rb",
  "build_log": "/home/aither/workspace/ai/vpsfree.cz/work/2026-11-06-multilingual-blog-migration/final-blog-system-build.log",
  "build_log_sha256": "b8bab825283c4e518f412a01c0e9924086d73450d96867a8cc41b4184718714f",
  "command_exit": 0,
  "completion_evidence": "Confctl logged Built generations and exact generation; receipt/symlinks/toplevel/input paths and derivation output exist and agree. No rerun.",
  "deployment": "None; no active system/profile path or deployed head is claimed.",
  "derivation": "/nix/store/nzccrw68i25yqvx9zq8b71mfaiz0sd6r-nixos-system-blog-26.05.20261026.718f670.drv",
  "effective_inputs": {
    "nixpkgs": {
      "input": "nixpkgsStable",
      "lastModified": 1793015021,
      "narHash": "sha256-Ee5BWo8sh3pGt70QUdRajnaginqFmWvrtdBc4gJzhks=",
      "narSize": 206804072,
      "path": "/nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source",
      "rev": "718f670e845328e9c2cecdd832835712b2cbd065",
      "shortRev": "718f670e",
      "url": "https://github.com/NixOS/nixpkgs"
    },
    "vpsadminos": {
      "input": "vpsadminosOsStaging",
      "lastModified": 1793720150,
      "narHash": "sha256-LXZP7Ghcr+1obFUD+LjlJRO63qRo/GZtSve5AX5MZ7c=",
      "narSize": 338218032,
      "path": "/nix/store/cgk63vdx1wjl4ybd53abkd5aqyzc7sfa-source",
      "rev": "dd188397abe37d0bc33f4c5dfb3605206ce5e326",
      "shortRev": "dd188397",
      "url": "https://github.com/vpsfreecz/vpsadminos"
    }
  },
  "generation_json": "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/vpsfree-cz-configuration/.confctl/generations/cz.vpsfree:containers:int.blog/2026-11-07--00-29-17/generation.json",
  "generation_sha256": "829923f159788d7b46a6a90e9abf3f0f8e13bf144b5e3fc94086f5775bcac96f",
  "lock_git_blob": "11219f0dcb5a4be6a6a2d813086461988953d2e8",
  "lock_nodes": 64,
  "lock_sha256": "9ed71bd9511c7b4e16e0fd9f4de483e0fe4cf54d2556e715392d28e6e60eacd8",
  "outer_shell_exit": 127,
  "outer_shell_issue": "/etc/bash_logout:4: __ETC_BASHLOGOUT_SOURCED: unbound variable",
  "selector": "cz.vpsfree/containers/int.blog",
  "source_clean_observed": true,
  "source_git_materialization": "/nix/store/ai3m6c2zl40ci93c40n9swv1asm306h7-source",
  "source_narHash": "sha256-oyj2ibCzzi+AaFozbgj5XkxyZlgZy+0yewIhPXuZhhI=",
  "source_proof_limit": "Exact Git snapshot materialized/read after build; generation JSON itself has no configuration revision field. Build source binding uses watcher exact-head/clean checks and unchanged source.",
  "source_sha": "7bab9781d0a5eb1aed5914f0aed99f6d7d491632",
  "toplevel": "/nix/store/pa6j6jvzf8ic3z7bqvzskdgmk2b7mk0z-nixos-system-blog-26.05.20261026.718f670"
}
```

<details><summary>Complete pinned root source lock graph (64 nodes)</summary>

```json
{
  "nodes": {
    "bun2nix": {
      "inputs": {
        "flake-parts": [
          "devWorkspace",
          "llm-agents",
          "flake-parts"
        ],
        "nixpkgs": [
          "devWorkspace",
          "llm-agents",
          "nixpkgs"
        ],
        "systems": [
          "devWorkspace",
          "llm-agents",
          "systems"
        ],
        "treefmt-nix": [
          "devWorkspace",
          "llm-agents",
          "treefmt-nix"
        ]
      },
      "locked": {
        "lastModified": 1790001035,
        "narHash": "sha256-1/SLBjSYBzDdDhvLQ83wrzBakyS/xNGgtxHGNuveOEQ=",
        "owner": "Mic92",
        "repo": "bun2nix",
        "rev": "07a5bfc8ac36c5370199343fa620b69f63186e33",
        "type": "github"
      },
      "original": {
        "owner": "Mic92",
        "ref": "llm-agents",
        "repo": "bun2nix",
        "type": "github"
      }
    },
    "bun2nix_2": {
      "inputs": {
        "flake-parts": [
          "llm-agents",
          "flake-parts"
        ],
        "nixpkgs": [
          "llm-agents",
          "nixpkgs"
        ],
        "systems": [
          "llm-agents",
          "systems"
        ],
        "treefmt-nix": [
          "llm-agents",
          "treefmt-nix"
        ]
      },
      "locked": {
        "lastModified": 1790001035,
        "narHash": "sha256-1/SLBjSYBzDdDhvLQ83wrzBakyS/xNGgtxHGNuveOEQ=",
        "owner": "Mic92",
        "repo": "bun2nix",
        "rev": "07a5bfc8ac36c5370199343fa620b69f63186e33",
        "type": "github"
      },
      "original": {
        "owner": "Mic92",
        "ref": "llm-agents",
        "repo": "bun2nix",
        "type": "github"
      }
    },
    "codex-web": {
      "flake": false,
      "locked": {
        "lastModified": 1793398646,
        "narHash": "sha256-Hhh2EYZxKiM1fDfPGxDazhs/ElyOF4q6mMvK5JOUOu0=",
        "owner": "aither64",
        "repo": "codex-web",
        "rev": "d3a29bee90ef00a08816920408c596152339a637",
        "type": "github"
      },
      "original": {
        "owner": "aither64",
        "repo": "codex-web",
        "rev": "d3a29bee90ef00a08816920408c596152339a637",
        "type": "github"
      }
    },
    "confctl": {
      "inputs": {
        "nixpkgs": [
          "confctl",
          "vpsadminos",
          "nixpkgs"
        ],
        "vpsadminos": "vpsadminos"
      },
      "locked": {
        "lastModified": 1784400083,
        "narHash": "sha256-gh1tmTv8aAO1OA3HX2NEYnRALMK2i666Lxey8hxD0QM=",
        "owner": "vpsfreecz",
        "repo": "confctl",
        "rev": "7bee58a52372b95c2198ce3f2a719807a3c2c66b",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "confctl",
        "type": "github"
      }
    },
    "devWorkspace": {
      "inputs": {
        "codex-web": "codex-web",
        "llm-agents": "llm-agents",
        "nixpkgs": "nixpkgs_4"
      },
      "locked": {
        "lastModified": 1793782995,
        "narHash": "sha256-pDaBIdK6uFgVq0Gw7arQLjvIjKsGrKg33IFmwmxnOoo=",
        "owner": "aither64",
        "repo": "dev-workspace",
        "rev": "3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7",
        "type": "github"
      },
      "original": {
        "owner": "aither64",
        "repo": "dev-workspace",
        "type": "github"
      }
    },
    "flake-parts": {
      "inputs": {
        "nixpkgs-lib": [
          "devWorkspace",
          "llm-agents",
          "nixpkgs"
        ]
      },
      "locked": {
        "lastModified": 1790898470,
        "narHash": "sha256-zTwuwezD0w3hpga6a6P8emidzAZFyWqlNeRBlpWOOl8=",
        "owner": "hercules-ci",
        "repo": "flake-parts",
        "rev": "024633cd702b10285db5cb19b40ad48d2399ba60",
        "type": "github"
      },
      "original": {
        "owner": "hercules-ci",
        "repo": "flake-parts",
        "type": "github"
      }
    },
    "flake-parts_2": {
      "inputs": {
        "nixpkgs-lib": [
          "llm-agents",
          "nixpkgs"
        ]
      },
      "locked": {
        "lastModified": 1790898470,
        "narHash": "sha256-zTwuwezD0w3hpga6a6P8emidzAZFyWqlNeRBlpWOOl8=",
        "owner": "hercules-ci",
        "repo": "flake-parts",
        "rev": "024633cd702b10285db5cb19b40ad48d2399ba60",
        "type": "github"
      },
      "original": {
        "owner": "hercules-ci",
        "repo": "flake-parts",
        "type": "github"
      }
    },
    "home-manager": {
      "inputs": {
        "nixpkgs": [
          "confctl",
          "vpsadminos",
          "impermanence",
          "nixpkgs"
        ]
      },
      "locked": {
        "lastModified": 1768598210,
        "narHash": "sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg=",
        "owner": "nix-community",
        "repo": "home-manager",
        "rev": "c47b2cc64a629f8e075de52e4742de688f930dc6",
        "type": "github"
      },
      "original": {
        "owner": "nix-community",
        "repo": "home-manager",
        "type": "github"
      }
    },
    "home-manager_2": {
      "inputs": {
        "nixpkgs": [
          "nixpkgsStable"
        ]
      },
      "locked": {
        "lastModified": 1780361225,
        "narHash": "sha256-wnV9ttf4fPWNonBIQmvlrSlNpQYgx5HgWWd007mwIFA=",
        "owner": "nix-community",
        "repo": "home-manager",
        "rev": "e28654b71096e08c019d4861ca26acb646f583d8",
        "type": "github"
      },
      "original": {
        "owner": "nix-community",
        "ref": "release-26.05",
        "repo": "home-manager",
        "type": "github"
      }
    },
    "home-manager_3": {
      "inputs": {
        "nixpkgs": [
          "vpsadminosOsStaging",
          "impermanence",
          "nixpkgs"
        ]
      },
      "locked": {
        "lastModified": 1768598210,
        "narHash": "sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg=",
        "owner": "nix-community",
        "repo": "home-manager",
        "rev": "c47b2cc64a629f8e075de52e4742de688f930dc6",
        "type": "github"
      },
      "original": {
        "owner": "nix-community",
        "repo": "home-manager",
        "type": "github"
      }
    },
    "home-manager_4": {
      "inputs": {
        "nixpkgs": [
          "vpsadminosProduction",
          "impermanence",
          "nixpkgs"
        ]
      },
      "locked": {
        "lastModified": 1768598210,
        "narHash": "sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg=",
        "owner": "nix-community",
        "repo": "home-manager",
        "rev": "c47b2cc64a629f8e075de52e4742de688f930dc6",
        "type": "github"
      },
      "original": {
        "owner": "nix-community",
        "repo": "home-manager",
        "type": "github"
      }
    },
    "home-manager_5": {
      "inputs": {
        "nixpkgs": [
          "vpsadminosStaging",
          "impermanence",
          "nixpkgs"
        ]
      },
      "locked": {
        "lastModified": 1768598210,
        "narHash": "sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg=",
        "owner": "nix-community",
        "repo": "home-manager",
        "rev": "c47b2cc64a629f8e075de52e4742de688f930dc6",
        "type": "github"
      },
      "original": {
        "owner": "nix-community",
        "repo": "home-manager",
        "type": "github"
      }
    },
    "home-manager_6": {
      "inputs": {
        "nixpkgs": [
          "vpsfStatus",
          "vpsadmin",
          "vpsadminos",
          "impermanence",
          "nixpkgs"
        ]
      },
      "locked": {
        "lastModified": 1768598210,
        "narHash": "sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg=",
        "owner": "nix-community",
        "repo": "home-manager",
        "rev": "c47b2cc64a629f8e075de52e4742de688f930dc6",
        "type": "github"
      },
      "original": {
        "owner": "nix-community",
        "repo": "home-manager",
        "type": "github"
      }
    },
    "impermanence": {
      "inputs": {
        "home-manager": "home-manager",
        "nixpkgs": "nixpkgs"
      },
      "locked": {
        "lastModified": 1769548169,
        "narHash": "sha256-03+JxvzmfwRu+5JafM0DLbxgHttOQZkUtDWBmeUkN8Y=",
        "owner": "nix-community",
        "repo": "impermanence",
        "rev": "7b1d382faf603b6d264f58627330f9faa5cba149",
        "type": "github"
      },
      "original": {
        "owner": "nix-community",
        "repo": "impermanence",
        "type": "github"
      }
    },
    "impermanence_2": {
      "inputs": {
        "home-manager": "home-manager_3",
        "nixpkgs": "nixpkgs_6"
      },
      "locked": {
        "lastModified": 1792739756,
        "narHash": "sha256-s0TeXWG5Ci75Y/Hzon0Z7NrN/fG773Rc54/z6oPFszQ=",
        "owner": "nix-community",
        "repo": "impermanence",
        "rev": "fa627f4c8b8e92f58f58a73d99ee4e1304e64eb2",
        "type": "github"
      },
      "original": {
        "owner": "nix-community",
        "repo": "impermanence",
        "type": "github"
      }
    },
    "impermanence_3": {
      "inputs": {
        "home-manager": "home-manager_4",
        "nixpkgs": "nixpkgs_7"
      },
      "locked": {
        "lastModified": 1769548169,
        "narHash": "sha256-03+JxvzmfwRu+5JafM0DLbxgHttOQZkUtDWBmeUkN8Y=",
        "owner": "nix-community",
        "repo": "impermanence",
        "rev": "7b1d382faf603b6d264f58627330f9faa5cba149",
        "type": "github"
      },
      "original": {
        "owner": "nix-community",
        "repo": "impermanence",
        "type": "github"
      }
    },
    "impermanence_4": {
      "inputs": {
        "home-manager": "home-manager_5",
        "nixpkgs": "nixpkgs_8"
      },
      "locked": {
        "lastModified": 1792739756,
        "narHash": "sha256-s0TeXWG5Ci75Y/Hzon0Z7NrN/fG773Rc54/z6oPFszQ=",
        "owner": "nix-community",
        "repo": "impermanence",
        "rev": "fa627f4c8b8e92f58f58a73d99ee4e1304e64eb2",
        "type": "github"
      },
      "original": {
        "owner": "nix-community",
        "repo": "impermanence",
        "type": "github"
      }
    },
    "impermanence_5": {
      "inputs": {
        "home-manager": "home-manager_6",
        "nixpkgs": "nixpkgs_9"
      },
      "locked": {
        "lastModified": 1769548169,
        "narHash": "sha256-03+JxvzmfwRu+5JafM0DLbxgHttOQZkUtDWBmeUkN8Y=",
        "owner": "nix-community",
        "repo": "impermanence",
        "rev": "7b1d382faf603b6d264f58627330f9faa5cba149",
        "type": "github"
      },
      "original": {
        "owner": "nix-community",
        "repo": "impermanence",
        "type": "github"
      }
    },
    "llm-agents": {
      "inputs": {
        "bun2nix": "bun2nix",
        "flake-parts": "flake-parts",
        "nixpkgs": "nixpkgs_3",
        "systems": "systems",
        "treefmt-nix": "treefmt-nix"
      },
      "locked": {
        "lastModified": 1793167323,
        "narHash": "sha256-JxeqQKUhBn5kj6xfE4nIrxw/q3jFJyT+TKc8mLsnuhc=",
        "owner": "numtide",
        "repo": "llm-agents.nix",
        "rev": "91ff550fe42d4dd51dcf8b6bad87a0134fe7f314",
        "type": "github"
      },
      "original": {
        "owner": "numtide",
        "repo": "llm-agents.nix",
        "rev": "91ff550fe42d4dd51dcf8b6bad87a0134fe7f314",
        "type": "github"
      }
    },
    "llm-agents_2": {
      "inputs": {
        "bun2nix": "bun2nix_2",
        "flake-parts": "flake-parts_2",
        "nixpkgs": "nixpkgs_5",
        "systems": "systems_2",
        "treefmt-nix": "treefmt-nix_2"
      },
      "locked": {
        "lastModified": 1793167323,
        "narHash": "sha256-JxeqQKUhBn5kj6xfE4nIrxw/q3jFJyT+TKc8mLsnuhc=",
        "owner": "numtide",
        "repo": "llm-agents.nix",
        "rev": "91ff550fe42d4dd51dcf8b6bad87a0134fe7f314",
        "type": "github"
      },
      "original": {
        "owner": "numtide",
        "repo": "llm-agents.nix",
        "type": "github"
      }
    },
    "netlinkrb": {
      "flake": false,
      "locked": {
        "lastModified": 1562850306,
        "narHash": "sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg=",
        "owner": "vpsfreecz",
        "repo": "netlinkrb",
        "rev": "d9de53d843d2586ffa5b7b404887fa801c697ddf",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "netlinkrb",
        "type": "github"
      }
    },
    "netlinkrb_2": {
      "flake": false,
      "locked": {
        "lastModified": 1562850306,
        "narHash": "sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg=",
        "owner": "vpsfreecz",
        "repo": "netlinkrb",
        "rev": "d9de53d843d2586ffa5b7b404887fa801c697ddf",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "netlinkrb",
        "type": "github"
      }
    },
    "netlinkrb_3": {
      "flake": false,
      "locked": {
        "lastModified": 1562850306,
        "narHash": "sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg=",
        "owner": "vpsfreecz",
        "repo": "netlinkrb",
        "rev": "d9de53d843d2586ffa5b7b404887fa801c697ddf",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "netlinkrb",
        "type": "github"
      }
    },
    "netlinkrb_4": {
      "flake": false,
      "locked": {
        "lastModified": 1562850306,
        "narHash": "sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg=",
        "owner": "vpsfreecz",
        "repo": "netlinkrb",
        "rev": "d9de53d843d2586ffa5b7b404887fa801c697ddf",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "netlinkrb",
        "type": "github"
      }
    },
    "netlinkrb_5": {
      "flake": false,
      "locked": {
        "lastModified": 1562850306,
        "narHash": "sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg=",
        "owner": "vpsfreecz",
        "repo": "netlinkrb",
        "rev": "d9de53d843d2586ffa5b7b404887fa801c697ddf",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "netlinkrb",
        "type": "github"
      }
    },
    "nixpkgs": {
      "locked": {
        "lastModified": 1768564909,
        "narHash": "sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc=",
        "owner": "nixos",
        "repo": "nixpkgs",
        "rev": "e4bae1bd10c9c57b2cf517953ab70060a828ee6f",
        "type": "github"
      },
      "original": {
        "owner": "nixos",
        "ref": "nixos-unstable",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgsProduction": {
      "locked": {
        "lastModified": 1793015021,
        "narHash": "sha256-Ee5BWo8sh3pGt70QUdRajnaginqFmWvrtdBc4gJzhks=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "718f670e845328e9c2cecdd832835712b2cbd065",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-26.05",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgsStable": {
      "locked": {
        "lastModified": 1793015021,
        "narHash": "sha256-Ee5BWo8sh3pGt70QUdRajnaginqFmWvrtdBc4gJzhks=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "718f670e845328e9c2cecdd832835712b2cbd065",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-26.05",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgsStaging": {
      "locked": {
        "lastModified": 1793015021,
        "narHash": "sha256-Ee5BWo8sh3pGt70QUdRajnaginqFmWvrtdBc4gJzhks=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "718f670e845328e9c2cecdd832835712b2cbd065",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-26.05",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgsUnstable": {
      "locked": {
        "lastModified": 1781074563,
        "narHash": "sha256-md8WlXOlfnIeHeOScMTTHFyf2d6iaTwPl2apR5EQ3P4=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "9ae611a455b90cf061d8f332b977e387bda8e1ca",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-unstable",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgsUnstable_2": {
      "locked": {
        "lastModified": 1793110635,
        "narHash": "sha256-dhoW6VgFWlaodSY5jrBn+CF2FLmaUvDVgM7+C7T2+NM=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "31ecbaca1bdefa45dffc409f0250bd8039ea0010",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-unstable",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgsUnstable_3": {
      "locked": {
        "lastModified": 1786106723,
        "narHash": "sha256-zDSUbpoeo/9ZmD2+wXnzxoo1+uhL8vxc0b8yuYMKYq0=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "f13ff45afd1bb73e640eaa08a7066dbed07e3238",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-unstable",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgs_10": {
      "locked": {
        "lastModified": 1786089803,
        "narHash": "sha256-ZuvZfVW2tB5tXYEcpcfhVXB3N4OhdZLOqOviy4OD4b4=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "ee48b147c18c7de1e6ec97dc74792be42724bed1",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-26.05",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgs_2": {
      "locked": {
        "lastModified": 1780902259,
        "narHash": "sha256-q8yYEC5f1mFlQO9RGna4LTc9QrcvWunX6FYp83munkQ=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "bd0ff2d3eac24699c3664d5966b9ef36f388e2ca",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-26.05",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgs_3": {
      "locked": {
        "lastModified": 1792116957,
        "narHash": "sha256-EjZqHKObBfIOeHZnMRVV87HB3pPq/WBkmRJWyFxmZu8=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "f20cd90e28fe0403873f473b29e42662cd86e8c4",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixpkgs-unstable",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgs_4": {
      "locked": {
        "lastModified": 1788405554,
        "narHash": "sha256-r2f1oUwixlgq9zOdYLqJLfS/lWBT60/IITjhTKI59JU=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-26.05",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgs_5": {
      "locked": {
        "lastModified": 1792116957,
        "narHash": "sha256-EjZqHKObBfIOeHZnMRVV87HB3pPq/WBkmRJWyFxmZu8=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "f20cd90e28fe0403873f473b29e42662cd86e8c4",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixpkgs-unstable",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgs_6": {
      "locked": {
        "lastModified": 1768564909,
        "narHash": "sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc=",
        "owner": "nixos",
        "repo": "nixpkgs",
        "rev": "e4bae1bd10c9c57b2cf517953ab70060a828ee6f",
        "type": "github"
      },
      "original": {
        "owner": "nixos",
        "ref": "nixos-unstable",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgs_7": {
      "locked": {
        "lastModified": 1768564909,
        "narHash": "sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc=",
        "owner": "nixos",
        "repo": "nixpkgs",
        "rev": "e4bae1bd10c9c57b2cf517953ab70060a828ee6f",
        "type": "github"
      },
      "original": {
        "owner": "nixos",
        "ref": "nixos-unstable",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgs_8": {
      "locked": {
        "lastModified": 1768564909,
        "narHash": "sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc=",
        "owner": "nixos",
        "repo": "nixpkgs",
        "rev": "e4bae1bd10c9c57b2cf517953ab70060a828ee6f",
        "type": "github"
      },
      "original": {
        "owner": "nixos",
        "ref": "nixos-unstable",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgs_9": {
      "locked": {
        "lastModified": 1768564909,
        "narHash": "sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc=",
        "owner": "nixos",
        "repo": "nixpkgs",
        "rev": "e4bae1bd10c9c57b2cf517953ab70060a828ee6f",
        "type": "github"
      },
      "original": {
        "owner": "nixos",
        "ref": "nixos-unstable",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "root": {
      "inputs": {
        "confctl": "confctl",
        "devWorkspace": "devWorkspace",
        "home-manager": "home-manager_2",
        "llm-agents": "llm-agents_2",
        "nixpkgs": [
          "nixpkgsStable"
        ],
        "nixpkgsProduction": "nixpkgsProduction",
        "nixpkgsStable": "nixpkgsStable",
        "nixpkgsStaging": "nixpkgsStaging",
        "nixpkgsUnstable": "nixpkgsUnstable_2",
        "vpsadminProduction": "vpsadminProduction",
        "vpsadminServices": "vpsadminServices",
        "vpsadminStaging": "vpsadminStaging",
        "vpsadminWebui": "vpsadminWebui",
        "vpsadminosOsStaging": "vpsadminosOsStaging",
        "vpsadminosProduction": "vpsadminosProduction",
        "vpsadminosStaging": "vpsadminosStaging",
        "vpsfStatus": "vpsfStatus",
        "vpsfreeNotificationTemplates": "vpsfreeNotificationTemplates",
        "vpsfreeWeb": "vpsfreeWeb"
      }
    },
    "ruby-lxc": {
      "flake": false,
      "locked": {
        "lastModified": 1780499941,
        "narHash": "sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE=",
        "owner": "vpsfreecz",
        "repo": "ruby-lxc",
        "rev": "004bf35eb90d41ba60b347b5b1e73d868a4f95d9",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "ref": "2026-06-03-nixos-26-05-port",
        "repo": "ruby-lxc",
        "type": "github"
      }
    },
    "ruby-lxc_2": {
      "flake": false,
      "locked": {
        "lastModified": 1780499941,
        "narHash": "sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE=",
        "owner": "vpsfreecz",
        "repo": "ruby-lxc",
        "rev": "004bf35eb90d41ba60b347b5b1e73d868a4f95d9",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "ref": "2026-06-03-nixos-26-05-port",
        "repo": "ruby-lxc",
        "type": "github"
      }
    },
    "ruby-lxc_3": {
      "flake": false,
      "locked": {
        "lastModified": 1780499941,
        "narHash": "sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE=",
        "owner": "vpsfreecz",
        "repo": "ruby-lxc",
        "rev": "004bf35eb90d41ba60b347b5b1e73d868a4f95d9",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "ref": "2026-06-03-nixos-26-05-port",
        "repo": "ruby-lxc",
        "type": "github"
      }
    },
    "ruby-lxc_4": {
      "flake": false,
      "locked": {
        "lastModified": 1780499941,
        "narHash": "sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE=",
        "owner": "vpsfreecz",
        "repo": "ruby-lxc",
        "rev": "004bf35eb90d41ba60b347b5b1e73d868a4f95d9",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "ref": "2026-06-03-nixos-26-05-port",
        "repo": "ruby-lxc",
        "type": "github"
      }
    },
    "ruby-lxc_5": {
      "flake": false,
      "locked": {
        "lastModified": 1780499941,
        "narHash": "sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE=",
        "owner": "vpsfreecz",
        "repo": "ruby-lxc",
        "rev": "004bf35eb90d41ba60b347b5b1e73d868a4f95d9",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "ref": "2026-06-03-nixos-26-05-port",
        "repo": "ruby-lxc",
        "type": "github"
      }
    },
    "systems": {
      "locked": {
        "lastModified": 1791244623,
        "narHash": "sha256-uuanbkFk8a313Zfrxdcz8Us/yQtaxNnKJtX8v0ZPpd8=",
        "owner": "nix-systems",
        "repo": "default",
        "rev": "d36eeed142f88b5a636f2e3856a53c61654cf29b",
        "type": "github"
      },
      "original": {
        "owner": "nix-systems",
        "repo": "default",
        "type": "github"
      }
    },
    "systems_2": {
      "locked": {
        "lastModified": 1791244623,
        "narHash": "sha256-uuanbkFk8a313Zfrxdcz8Us/yQtaxNnKJtX8v0ZPpd8=",
        "owner": "nix-systems",
        "repo": "default",
        "rev": "d36eeed142f88b5a636f2e3856a53c61654cf29b",
        "type": "github"
      },
      "original": {
        "owner": "nix-systems",
        "repo": "default",
        "type": "github"
      }
    },
    "treefmt-nix": {
      "inputs": {
        "nixpkgs": [
          "devWorkspace",
          "llm-agents",
          "nixpkgs"
        ]
      },
      "locked": {
        "lastModified": 1791885023,
        "narHash": "sha256-C3alQ2MEt0zVrUSho5NUDo3jmhbff72++bfwoqT9Omo=",
        "owner": "numtide",
        "repo": "treefmt-nix",
        "rev": "0d6d739a833ba9a9c93034862e4a7b061a062a1c",
        "type": "github"
      },
      "original": {
        "owner": "numtide",
        "repo": "treefmt-nix",
        "type": "github"
      }
    },
    "treefmt-nix_2": {
      "inputs": {
        "nixpkgs": [
          "llm-agents",
          "nixpkgs"
        ]
      },
      "locked": {
        "lastModified": 1791885023,
        "narHash": "sha256-C3alQ2MEt0zVrUSho5NUDo3jmhbff72++bfwoqT9Omo=",
        "owner": "numtide",
        "repo": "treefmt-nix",
        "rev": "0d6d739a833ba9a9c93034862e4a7b061a062a1c",
        "type": "github"
      },
      "original": {
        "owner": "numtide",
        "repo": "treefmt-nix",
        "type": "github"
      }
    },
    "vpsadmin": {
      "inputs": {
        "nixpkgs": [
          "vpsfStatus",
          "vpsadmin",
          "vpsadminos",
          "nixpkgs"
        ],
        "vpsadminos": "vpsadminos_2"
      },
      "locked": {
        "lastModified": 1785850721,
        "narHash": "sha256-5MfntVa4kDeE1MjIAIMDlGk3X7fJ6BzS7GWW0mCEwuk=",
        "owner": "vpsfreecz",
        "repo": "vpsadmin",
        "rev": "3f9b68adb97b7f43df929a85fc172d9d11e15211",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsadmin",
        "type": "github"
      }
    },
    "vpsadminProduction": {
      "inputs": {
        "nixpkgs": [
          "nixpkgsProduction"
        ],
        "vpsadminos": [
          "vpsadminosProduction"
        ]
      },
      "locked": {
        "lastModified": 1792321599,
        "narHash": "sha256-U0py4ENShmTqcwZDUn11GABUnE0BhVnTM1EXylJmcMc=",
        "owner": "vpsfreecz",
        "repo": "vpsadmin",
        "rev": "ff730be468e366ee346dc6d02dc0fe57c3f8677c",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsadmin",
        "type": "github"
      }
    },
    "vpsadminServices": {
      "inputs": {
        "nixpkgs": [
          "nixpkgsStable"
        ],
        "vpsadminos": [
          "vpsadminosStaging"
        ]
      },
      "locked": {
        "lastModified": 1793802784,
        "narHash": "sha256-J7a/I+juHiy63uDAWxANp/THIX6+Zo7r4l0zaiicSeo=",
        "owner": "vpsfreecz",
        "repo": "vpsadmin",
        "rev": "b83b26e1ba1c8e869ae3ffbcb5801ed071c3844e",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsadmin",
        "type": "github"
      }
    },
    "vpsadminStaging": {
      "inputs": {
        "nixpkgs": [
          "nixpkgsStaging"
        ],
        "vpsadminos": [
          "vpsadminosStaging"
        ]
      },
      "locked": {
        "lastModified": 1792321599,
        "narHash": "sha256-U0py4ENShmTqcwZDUn11GABUnE0BhVnTM1EXylJmcMc=",
        "owner": "vpsfreecz",
        "repo": "vpsadmin",
        "rev": "ff730be468e366ee346dc6d02dc0fe57c3f8677c",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsadmin",
        "type": "github"
      }
    },
    "vpsadminWebui": {
      "inputs": {
        "nixpkgs": [
          "nixpkgsStable"
        ],
        "vpsadmin": [
          "vpsadminServices"
        ]
      },
      "locked": {
        "lastModified": 1793750160,
        "narHash": "sha256-bItN12Wrd6I/PoJOvTOJh1BVq3f9tGVQ+Q/uMQKeRtA=",
        "owner": "vpsfreecz",
        "repo": "vpsadmin-webui",
        "rev": "babe51421bd1df61a548e7b2f047053df14ff3eb",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsadmin-webui",
        "type": "github"
      }
    },
    "vpsadminos": {
      "inputs": {
        "impermanence": "impermanence",
        "netlinkrb": "netlinkrb",
        "nixpkgs": "nixpkgs_2",
        "nixpkgsUnstable": "nixpkgsUnstable",
        "ruby-lxc": "ruby-lxc"
      },
      "locked": {
        "lastModified": 1781261055,
        "narHash": "sha256-Y7FLO10JwU3bo0j6dRHboubKAP8VRxxnaiD2NshG+Kc=",
        "owner": "vpsfreecz",
        "repo": "vpsadminos",
        "rev": "6f9b2c755143197bd9c3452e1c0121b22e978c4d",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsadminos",
        "type": "github"
      }
    },
    "vpsadminosOsStaging": {
      "inputs": {
        "impermanence": "impermanence_2",
        "netlinkrb": "netlinkrb_2",
        "nixpkgs": [
          "nixpkgsStable"
        ],
        "nixpkgsUnstable": [
          "nixpkgsUnstable"
        ],
        "ruby-lxc": "ruby-lxc_2"
      },
      "locked": {
        "lastModified": 1793720150,
        "narHash": "sha256-LXZP7Ghcr+1obFUD+LjlJRO63qRo/GZtSve5AX5MZ7c=",
        "owner": "vpsfreecz",
        "repo": "vpsadminos",
        "rev": "dd188397abe37d0bc33f4c5dfb3605206ce5e326",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsadminos",
        "type": "github"
      }
    },
    "vpsadminosProduction": {
      "inputs": {
        "impermanence": "impermanence_3",
        "netlinkrb": "netlinkrb_3",
        "nixpkgs": [
          "nixpkgsProduction"
        ],
        "nixpkgsUnstable": [
          "nixpkgsUnstable"
        ],
        "ruby-lxc": "ruby-lxc_3"
      },
      "locked": {
        "lastModified": 1792347366,
        "narHash": "sha256-jyXAH3nUkocJj+KQKINbJ0UnDCmuln4EvYRw/1KtXFE=",
        "owner": "vpsfreecz",
        "repo": "vpsadminos",
        "rev": "2abbe3cc1c102a4b39022d3f73ef4a432ad4d616",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsadminos",
        "type": "github"
      }
    },
    "vpsadminosStaging": {
      "inputs": {
        "impermanence": "impermanence_4",
        "netlinkrb": "netlinkrb_4",
        "nixpkgs": [
          "nixpkgsStaging"
        ],
        "nixpkgsUnstable": [
          "nixpkgsUnstable"
        ],
        "ruby-lxc": "ruby-lxc_4"
      },
      "locked": {
        "lastModified": 1793720150,
        "narHash": "sha256-LXZP7Ghcr+1obFUD+LjlJRO63qRo/GZtSve5AX5MZ7c=",
        "owner": "vpsfreecz",
        "repo": "vpsadminos",
        "rev": "dd188397abe37d0bc33f4c5dfb3605206ce5e326",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsadminos",
        "type": "github"
      }
    },
    "vpsadminos_2": {
      "inputs": {
        "impermanence": "impermanence_5",
        "netlinkrb": "netlinkrb_5",
        "nixpkgs": "nixpkgs_10",
        "nixpkgsUnstable": "nixpkgsUnstable_3",
        "ruby-lxc": "ruby-lxc_5"
      },
      "locked": {
        "lastModified": 1786260915,
        "narHash": "sha256-Xd+DyVC+Gkv6+1oSsxb8VfE3DtVCHx90vmKvuFuhYbY=",
        "owner": "vpsfreecz",
        "repo": "vpsadminos",
        "rev": "837baf04054c6ee0e71d288b8870ac42a6990c38",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "ref": "staging",
        "repo": "vpsadminos",
        "type": "github"
      }
    },
    "vpsfStatus": {
      "inputs": {
        "nixpkgs": [
          "nixpkgsStable"
        ],
        "vpsadmin": "vpsadmin",
        "vpsadminos": [
          "vpsfStatus",
          "vpsadmin",
          "vpsadminos"
        ]
      },
      "locked": {
        "lastModified": 1788260265,
        "narHash": "sha256-4iun0P87K5kKG2vYi6Beio/1iWlHmNYFjD8Hlg2qGgk=",
        "owner": "vpsfreecz",
        "repo": "vpsf-status",
        "rev": "587cd65bb02e6dddea7f6b6409e42a15f36ab4fb",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsf-status",
        "type": "github"
      }
    },
    "vpsfreeNotificationTemplates": {
      "inputs": {
        "vpsadmin": [
          "vpsadminServices"
        ]
      },
      "locked": {
        "lastModified": 1790168321,
        "narHash": "sha256-tVRZNlK2iOcorDkw5bK/10e911ILS7VY5uMExH91NQ4=",
        "owner": "vpsfreecz",
        "repo": "vpsfree-notification-templates",
        "rev": "2cfd218d9152888feea4109f064459078ea9f76e",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsfree-notification-templates",
        "type": "github"
      }
    },
    "vpsfreeWeb": {
      "flake": false,
      "locked": {
        "lastModified": 1791740386,
        "narHash": "sha256-/3QHdhSzFlEc7YqWZDjnVxIeS4n1OdImicvgUZjBGew=",
        "owner": "vpsfreecz",
        "repo": "web",
        "rev": "307635a96bc3532af51ff5d08206d920704eee00",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "web",
        "type": "github"
      }
    }
  },
  "root": "root",
  "version": 7
}
```

</details>

The declared root graph is complete; the generation selects the two effective machine inputs recorded above. This build verifies the disabled candidate system, not enabled static hosting or installed machine admission.

## Superseded unrooted blog artifact attempt

The watcher successfully built reviewed `aeed3a018d895b797e1b8d9b2863dd20c0dec8e0` with `nix build --no-link --print-out-paths .#site` (command exit0). Initial metadata read identified artifact `/nix/store/cn6fxvcjidfvh3hyx4q1hqxixixsqyld-vpsfree-blog-0`, derivation `/nix/store/0m4andba5pv1aq6370h2208481nc82qw-vpsfree-blog-0.drv`, source `/nix/store/l8mawc1jgn90n8v74wgvzfsh1pd5pwpx-source`, source NAR `sha256-qCFMNOKvIRpmLMFH8a6k2cDTIZb5viyvma1CPXJQKhQ=`, Hugo0.167.0 and the 2-node Nixpkgs lock at `f3a73bcf5d1c5b75a66cf35a48957e30d41d647a` / `sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=`. Metadata declared1655served files.

Before the full digest/route pass, that artifact, source and derivation disappeared from the store. No cleanup was run by the implementer; an unrooted-output retention issue is possible but not proven. Full artifact verification is **incomplete**, with no content defect inferred. Publication paused. The first rooted-watcher preflight stopped before a build because of PATH, per lead report; no successful replacement artifact is claimed. A subsequent VPN runtime finding requires a corrected final blog head and new rooted build; old artifact interpretation remains superseded. Do not use these paths as retained current artifacts or eligible GitHub artifact proof.

## Corrected final rooted production artifact

Command: `nix build --out-link result --print-out-paths .#site`, exact clean final source below. The existing ignored `result` link is retained; no cleanup was performed. All assertions below passed by reading the immutable artifact/source only, without a new build or CI packaging.

```json
{
  "artifact_eligibility": "Local Nix artifact only; no GitHub run/artifact identity invented, no activation claim.",
  "artifact_path": "/nix/store/8m7n2r4hpis3wn2593vj0a8iiayljc22-vpsfree-blog-0",
  "both_home_canonicals": true,
  "complete_lock_graph": {
    "nodes": {
      "nixpkgs": {
        "locked": {
          "lastModified": 1792422028,
          "narHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
          "owner": "NixOS",
          "repo": "nixpkgs",
          "rev": "f3a73bcf5d1c5b75a66cf35a48957e30d41d647a",
          "type": "github"
        },
        "original": {
          "owner": "NixOS",
          "ref": "nixos-26.05",
          "repo": "nixpkgs",
          "type": "github"
        }
      },
      "root": {
        "inputs": {
          "nixpkgs": "nixpkgs"
        }
      }
    },
    "root": "root",
    "version": 7
  },
  "cs_article_routes": 125,
  "derivation_path": "/nix/store/1jmg6d2m3yq6xdxzdbiflqrskgwmvhvm-vpsfree-blog-0.drv",
  "en_drafts_verified_and_excluded": 125,
  "en_production_article_count": 0,
  "feed_items": {
    "cs": 10,
    "en": 0
  },
  "full_feed_content_date_guid_parity": true,
  "historical_comment_anchors_verified": 107,
  "inputs": {
    "hugoVersion": "0.167.0",
    "nixpkgsNarHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
    "nixpkgsRevision": "f3a73bcf5d1c5b75a66cf35a48957e30d41d647a",
    "revision": "3aec4d6b4858b2ed50e21bdb99d36f707fc9ceeb",
    "source": "/nix/store/8lwj9092h3n6v7977phwn2c5n1rxl6qc-source",
    "sourceNarHash": "sha256-JuLwVNsVGIE4yt5U5SYXko4vC21znWUydRQ0Au9ojAM="
  },
  "legacy_upload_digest_copies": 1138,
  "lock_sha256": "865a3c07a35f43f024ce7c01614be82cb795707edac8e27092bdbba42519cd75",
  "metadata_path": "/nix/store/8m7n2r4hpis3wn2593vj0a8iiayljc22-vpsfree-blog-0/metadata.json",
  "metadata_sha256": "02b2e117737477025c8c021b4a17ff7761aa4564ff09be380e277294ec3d638f",
  "retained_result_link": "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog/result",
  "retained_result_target": "/nix/store/8m7n2r4hpis3wn2593vj0a8iiayljc22-vpsfree-blog-0",
  "served_files_verified": 1655,
  "source_narHash": "sha256-JuLwVNsVGIE4yt5U5SYXko4vC21znWUydRQ0Au9ojAM=",
  "source_narSize": 52237824,
  "source_path": "/nix/store/8lwj9092h3n6v7977phwn2c5n1rxl6qc-source",
  "source_sha": "3aec4d6b4858b2ed50e21bdb99d36f707fc9ceeb"
}
```

The earlier unrooted aeed3a0 attempt remains incomplete/superseded. Corrected source3aec4d6b has the accepted narrow preview/check fix. Production excludes all125 English drafts; this is distinct from their usable preview. Publication remains paused until the separate V3 real-runtime/browser result is released by the lead.

Additional read-only final-artifact scope: every HTML canonical uses its own production host; no script or production Discourse iframe appears. Effective Nixpkgs source path/NAR also agrees with the complete two-node lock.

```json
{
  "all_html_canonicals_verified": {
    "cs": 430,
    "en": 22
  },
  "nixpkgs_source_narHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
  "nixpkgs_source_path": "/nix/store/kv7b75nbhc93yrs276n0ba9gsiv8cz3b-source",
  "production_scripts_and_discourse_frames": 0
}
```

## Final verified feature publication

The lead released publication after accepted corrected rooted artifact/system proof and final V3 real HTTP/browser usability evidence. The baseline independent review and accepted narrow preview fix remain recorded in final-review/V3 receipts; publication does not grant integration or activation.

```json
{
  "CI": "No workflow run ID surfaced in Git push output; publication-ready sent directly to implementer2 and lead. Implementer2 owns exact corrected-head Build blog discovery/watching. Implementer0 did not monitor CI.",
  "blog": {
    "command_exit": 0,
    "comparison_base": "0354dac281978867ea8c1553b092ce19bccb5ccd",
    "comparison_head": "3aec4d6b4858b2ed50e21bdb99d36f707fc9ceeb",
    "default_before_and_after": "0354dac281978867ea8c1553b092ce19bccb5ccd",
    "default_ref": "refs/heads/main",
    "method": "ordinary fast-forward push of exact SHA",
    "new_feature": "3aec4d6b4858b2ed50e21bdb99d36f707fc9ceeb",
    "old_feature": "0354dac281978867ea8c1553b092ce19bccb5ccd",
    "remote": "git@github.com:vpsfreecz/blog.git",
    "remote_HEAD": "refs/heads/main",
    "retry_count": 0
  },
  "branch": "2026-11-06-multilingual-blog-migration",
  "configuration": {
    "command_exit": 0,
    "comparison_base": "5941cdb3dda259e91c6a988a7dbf08c84700b326",
    "comparison_head": "7bab9781d0a5eb1aed5914f0aed99f6d7d491632",
    "declared_workflow": {
      "cron": "30 4 * * *",
      "events": [
        "workflow_dispatch",
        "schedule"
      ],
      "file": ".github/workflows/daily-update.yml",
      "name": "Daily update",
      "push_trigger": false
    },
    "default_before_and_after": "5941cdb3dda259e91c6a988a7dbf08c84700b326",
    "default_ref": "refs/heads/master",
    "method": "--force-with-lease=refs/heads/2026-11-06-multilingual-blog-migration:133a94b62b3c2161c126fa347cab61ae1b819001",
    "new_feature": "7bab9781d0a5eb1aed5914f0aed99f6d7d491632",
    "old_feature": "133a94b62b3c2161c126fa347cab61ae1b819001",
    "preserved_old_DNS_ref": "refs/heads/2026-11-06-multilingual-blog-migration-dns-reviewed",
    "remote": "git@github.com:vpsfreecz/vpsfree-cz-configuration.git",
    "remote_HEAD": "refs/heads/master"
  },
  "evidence": "Fresh canonical SSH fetch/ls-remote matched approved old refs before pushes. Immediate post-push ls-remote proved exact feature SHAs and unchanged default/HEAD refs. Both explicit base/head portal comparisons captured.",
  "limits": "Features only. No merge, PR, default update, rebase after review, source/pin changes, production request, activation, machine claim, service or lifecycle cleanup.",
  "retention": "All feature/recovery refs, rooted result, registered previews and session remain retained."
}
```

The original blog push remained owned throughout its quiet archive transfer. A measured49.5second interval acknowledged another16,580,180bytes before eventual exit0; no cancellation, retry or silence-based failure was introduced. Configuration used only the exact approved feature lease, preserving the old reviewed source ref; neither default branch was a push target.

## R9 final f0337fb artifact verification

After lead-reported mandatory final review acceptance, a fresh pinned Luna/low utility owned the sole rooted build. Its slot was yielded directly to U9 before this read-only artifact interpretation. Every assertion in the following scope passed against immutable store data. No source/index/service/configuration change, packaging with invented CI IDs or unchanged-system rebuild was performed.

```json
{
  "added_served_paths": [
    "cs/css/site.f3fd02ac6b25f134844db89cdc6923dfe3863bcc5667b3330ed3cd554e0e255f.css",
    "cs/theme/branding/join-us.svg",
    "en/css/site.f3fd02ac6b25f134844db89cdc6923dfe3863bcc5667b3330ed3cd554e0e255f.css",
    "en/theme/branding/join-us.svg"
  ],
  "all_125_cs_complete_file_bytes_unchanged_from_3aec": true,
  "artifact": "/nix/store/x9fa1vr5ljagv91yxmh5hwlycd0ihkzr-vpsfree-blog-0",
  "build_watcher": "/root/r9_build_watcher",
  "canonical_html_pages_verified": {
    "cs": 430,
    "en": 22
  },
  "command": "nix build --out-link result-d9 --print-out-paths .#site",
  "command_exit": 0,
  "complete_2_node_lock_graph": {
    "nodes": {
      "nixpkgs": {
        "locked": {
          "lastModified": 1792422028,
          "narHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
          "owner": "NixOS",
          "repo": "nixpkgs",
          "rev": "f3a73bcf5d1c5b75a66cf35a48957e30d41d647a",
          "type": "github"
        },
        "original": {
          "owner": "NixOS",
          "ref": "nixos-26.05",
          "repo": "nixpkgs",
          "type": "github"
        }
      },
      "root": {
        "inputs": {
          "nixpkgs": "nixpkgs"
        }
      }
    },
    "root": "root",
    "version": 7
  },
  "configuration": "7bab9781 unchanged; no repeated system build.",
  "cs_article_routes": 125,
  "derivation": "/nix/store/y8z3p3j4apfsqjxd378ahxp8an70hi9s-vpsfree-blog-0.drv",
  "elapsed_seconds": 7.009447788936086,
  "eligible_CI_artifact": "Not claimed; local Nix output only, no fabricated run or artifact IDs.",
  "en_drafts_fresh_and_excluded": 125,
  "en_production_article_count": 0,
  "feed_items": {
    "cs": 10,
    "en": 0
  },
  "full_cs_feed_guid_date_content_parity": true,
  "historical_comment_anchors": 107,
  "inputs": {
    "hugoVersion": "0.167.0",
    "nixpkgsNarHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
    "nixpkgsRevision": "f3a73bcf5d1c5b75a66cf35a48957e30d41d647a",
    "revision": "f0337fb7eae8797efca9254cd7208949cb0f77e4",
    "source": "/nix/store/l0bhsk62mndhki3n0pmidsfn5mnpa79x-source",
    "sourceNarHash": "sha256-7ysSUzHR0QGxgX/ZfwUwcrSUSTflHCz6pJ6ws7ZDbzQ="
  },
  "legacy_asset_digest_copies": 1138,
  "lock_sha256": "865a3c07a35f43f024ce7c01614be82cb795707edac8e27092bdbba42519cd75",
  "log": "r9-blog-build.log",
  "log_sha256": "09babee1412e794326fa8c514b5dc93a5eaaffd62ca008954f66ab3b9667a470",
  "metadata_sha256": "347274434654318fd8a6c6c40df5f44c9b6a141d726db781c0eaff7a975b71d2",
  "more_anchors": 125,
  "new_result_root_preserved": "/nix/store/x9fa1vr5ljagv91yxmh5hwlycd0ihkzr-vpsfree-blog-0",
  "nixpkgs_source_narHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
  "nixpkgs_source_path": "/nix/store/kv7b75nbhc93yrs276n0ba9gsiv8cz3b-source",
  "old_result_root_preserved": "/nix/store/8m7n2r4hpis3wn2593vj0a8iiayljc22-vpsfree-blog-0",
  "publication": "Held for separate final UI acceptance and lead second release.",
  "script_and_discourse_iframe_count": 0,
  "served_file_digests_verified": 1657,
  "served_paths_changed_from_3aec": 320,
  "source_clean_pre_post": true,
  "source_narHash": "sha256-7ysSUzHR0QGxgX/ZfwUwcrSUSTflHCz6pJ6ws7ZDbzQ=",
  "source_narSize": 52261984,
  "source_path": "/nix/store/l0bhsk62mndhki3n0pmidsfn5mnpa79x-source",
  "source_sha": "f0337fb7eae8797efca9254cd7208949cb0f77e4",
  "source_tree": "b80d2261d92efe01c51946f97fec5cd45b32b0fe",
  "unchanged_source_manifest_sha256": "e3c56173acbc2dd018da1d7ce5cd8b73d52e5ef83847a0353b17b107e5a36ab4",
  "watcher_policy": {
    "approval": "never",
    "catalog_digest": "a3f49bd3c1429d2d570cde01d509ae2d65a84c03b896c4265d9b9ccb0e317958",
    "effort": "low",
    "model": "gpt-6-luna",
    "native_utility": "dw_e45f9c382e5b2ea9a5313a9410cf2005d2b36626391d8cad",
    "sandbox": "danger-full-access"
  }
}
```

All125 Czech source bundles are byte-identical to the prior3aec snapshot and the original manifest; intended template/CSS/branding changes affect rendered output only. The27 modified English drafts remain drafts and source-fresh; this verification does not replace human language review. Existing `result` and new `result-d9` roots are both retained. Feature publication remains gated on the separate U9 browser acceptance and lead release.

## R9 final feature publication and exact CI

After the lead accepted both the rooted artifact and U9 final11-view usability result, R9 published only the exact blog feature SHA. No source/check modifications, default advances, broad force, rebase or extra repository push occurred. A new pinned Luna/low utility owned the exact new run; it did not reuse the earlier build utility. The authoritative final metadata was interpreted only after the utility finished.

```json
{
  "CI": {
    "conclusion": "success",
    "databaseId": 42360486251,
    "event": "push",
    "headBranch": "2026-11-06-multilingual-blog-migration",
    "headSha": "f0337fb7eae8797efca9254cd7208949cb0f77e4",
    "jobs": [
      {
        "completedAt": "2026-11-07T09:37:39Z",
        "conclusion": "success",
        "databaseId": 128367627432,
        "name": "build",
        "startedAt": "2026-11-07T09:36:59Z",
        "status": "completed",
        "steps": [
          {
            "completedAt": "2026-11-07T09:37:01Z",
            "conclusion": "success",
            "name": "Set up job",
            "number": 1,
            "startedAt": "2026-11-07T09:37:00Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T09:37:03Z",
            "conclusion": "success",
            "name": "Run actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1",
            "number": 2,
            "startedAt": "2026-11-07T09:37:01Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T09:37:06Z",
            "conclusion": "success",
            "name": "Run cachix/install-nix-action@75c75c31ebece974e48ebc36b4ad125bd97bd97b",
            "number": 3,
            "startedAt": "2026-11-07T09:37:03Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T09:37:31Z",
            "conclusion": "success",
            "name": "Run nix develop -c bin/check",
            "number": 4,
            "startedAt": "2026-11-07T09:37:06Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T09:37:32Z",
            "conclusion": "success",
            "name": "Run nix develop -c bin/check-release",
            "number": 5,
            "startedAt": "2026-11-07T09:37:31Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T09:37:36Z",
            "conclusion": "success",
            "name": "Run nix build .#site",
            "number": 6,
            "startedAt": "2026-11-07T09:37:32Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T09:37:36Z",
            "conclusion": "skipped",
            "name": "Package trusted main build",
            "number": 7,
            "startedAt": "2026-11-07T09:37:36Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T09:37:36Z",
            "conclusion": "skipped",
            "name": "Run actions/upload-artifact@cf430e030ddbb5b0abf93d22962f4752f3646cd9",
            "number": 8,
            "startedAt": "2026-11-07T09:37:36Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T09:37:36Z",
            "conclusion": "success",
            "name": "Post Run actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1",
            "number": 16,
            "startedAt": "2026-11-07T09:37:36Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T09:37:36Z",
            "conclusion": "success",
            "name": "Complete job",
            "number": 17,
            "startedAt": "2026-11-07T09:37:36Z",
            "status": "completed"
          }
        ],
        "url": "https://github.com/vpsfreecz/blog/actions/runs/42360486251/job/128367627432"
      }
    ],
    "status": "completed",
    "url": "https://github.com/vpsfreecz/blog/actions/runs/42360486251",
    "workflowName": "Build blog"
  },
  "artifact_count": 0,
  "ci_watcher": {
    "approval": "never",
    "catalog_digest": "a3f49bd3c1429d2d570cde01d509ae2d65a84c03b896c4265d9b9ccb0e317958",
    "command": "gh run watch 42360486251 --repo vpsfreecz/blog --exit-status --interval 15",
    "effort": "low",
    "mode": "fresh standalone Codex exec, no reused build-watcher identity/history",
    "model": "gpt-6-luna",
    "native_identity": "dw_e45f9c382e5b2ea9a5313a9410cf2005d2b36626391d8cad",
    "parent_duplicate_polling": false,
    "retries_cancellations": false,
    "sandbox": "danger-full-access",
    "utility_elapsed_seconds": 46.24749922391493,
    "utility_exit": 0,
    "watch_duration": "under one second; run already terminal when fresh watcher inspected it",
    "watch_exit": 0
  },
  "comparison": {
    "base": "0354dac281978867ea8c1553b092ce19bccb5ccd",
    "command": "dev-session worktree capture-comparison 2026-11-06-multilingual-blog-migration blog --as-is --base 0354dac281978867ea8c1553b092ce19bccb5ccd --head f0337fb7eae8797efca9254cd7208949cb0f77e4",
    "head": "f0337fb7eae8797efca9254cd7208949cb0f77e4"
  },
  "feature_branch": "refs/heads/2026-11-06-multilingual-blog-migration",
  "fresh_remote_proof": "canonical SSH fetch/ls-remote before push matched expected feature/main; immediate post-push ls-remote matched exact f033 feature and unchanged main/HEAD",
  "old_remote_feature": "3aec4d6b4858b2ed50e21bdb99d36f707fc9ceeb",
  "other_repositories": "Configuration feature7bab9781 and workspace feature unchanged; no additional pushes or system build. Existing configuration proof retained.",
  "published_remote_feature": "f0337fb7eae8797efca9254cd7208949cb0f77e4",
  "published_tree": "b80d2261d92efe01c51946f97fec5cd45b32b0fe",
  "push": "normal fast-forward, exact SHA refspec, exit 0, no retry",
  "release_limits": "Feature-only verification. Main packaging/upload skipped and no eligible GitHub deployment artifact exists for this feature run. No integration, production/blog/forum/service/machine/default/PR/lifecycle action. Human English review and transition/admission gates remain.",
  "remote_default_ref": "refs/heads/main",
  "remote_main_and_HEAD_before_after": "0354dac281978867ea8c1553b092ce19bccb5ccd",
  "repository": "git@github.com:vpsfreecz/blog.git",
  "retained_evidence_sha256": {
    "r9-ci-watcher-result.json": "3101cc0bde3ee876cd5e0dcaa1ee5d3ec94e75ca3c4ddeadbc4ee7429e4484aa",
    "r9-feature-ci-artifacts.json": "244563f989470892c537c9a4622920af0d228ee4528f7d00c64a06d6cd95856c",
    "r9-feature-ci-watch.exit": "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa",
    "r9-feature-ci-watch.log": "a2acb0ffe4e3bdabb06dd9fe9561f5be9bf823edf478b834795b54bdc29e4c45",
    "r9-feature-ci.json": "0db2f66b3b16a1eb8ee51d135b24ba74f5e110096e33a46ea578d8f8aa00250c"
  },
  "retention": "Old result, result-d9, all refs, registered previews and session retained."
}
```

Normal checks and build succeeded; trusted protected-main packaging and artifact upload were skipped, and the artifact listing reports0. This is expected feature CI, not a live release or activation result. No process remains from either R9 watcher. All source/input/route/digest proof above belongs to the exact final f033 artifact; unchanged configuration-system evidence was not repeated.

## S10 accepted Pagefind source checkpoint

Source and known-quick evidence only. Lead accepted the exact package and main wording; no new independent review, browser, HTTP service, artifact or publication success is claimed here. The source/index window is yielded for the separate requested D11 work.

```json
{
  "base": "c829fbf4abcd7f7ab47b44386b3d12ec39090b55",
  "boundaries": "No article/translation/data/flake.lock/configuration/workflow/admission changes, production calls, services/restarts, final artifact/long browser/push/default/lifecycle actions. No D11 link work included.",
  "checks": {
    "bash -n bin/build bin/preview": "PASS",
    "corpus/data/flake.lock unchanged and complete U10 CSS prefix retained": "PASS",
    "git diff --check and exact staged owned inventory": "PASS",
    "local documentation links/TOML examples/localizations": "PASS",
    "nix develop -c bin/check": "PASS: real/fixture/production counts, empty root, current route/feed/canonical/draft contracts, deterministic full output, isolated preview pre-generation survives command stub, no watch/clean flags",
    "nix develop -c bin/check-release": "PASS: local Pagefind JS/WASM/entry payload inclusion and hash-tamper rejection"
  },
  "copy": "Main accepted exact CS/EN search/status/error/reload and snapshot copy; required README comma correction applied before commit.",
  "deletions": 30,
  "dependency": {
    "existing_lock_unchanged": true,
    "package": "pkgs.pagefind",
    "recorded_build_input": "pagefindVersion",
    "version": "1.5.2"
  },
  "dependency_setup_evidence": {
    "caveat": "Utility failed to redirect first successful output, mistakenly started second pure version invocation with redirection then interrupted it. No process remains; no parent repeat or false full-log claim.",
    "command": "nix develop -c pagefind --version",
    "reported_result": "pagefind 1.5.2, exit0",
    "retained_report": "s10-pagefind-setup-watcher.md",
    "utility": "fresh pinned gpt-6-luna/low dependency watcher"
  },
  "files": 19,
  "gaps": [
    "Independent final review after D11 source completion",
    "Actual browser native API positive and negative nav/comment query evidence",
    "Desktop/mobile keyboard, loading/empty/error and missing-shard reload behavior",
    "Real native disk HTTP serving and snapshot edit/add/remove coherence",
    "Exact final rooted Nix artifact and any feature publication/CI"
  ],
  "head": "95a3cae2a1185c096968357e558ee15ad5a2a7f8",
  "insertions": 433,
  "ownership": "S10 findings and eventual artifact interpretation remain implementer0; execution capacity free after receipt. Existing build roots/previews/refs/session retained.",
  "package": "S10 Pagefind source only",
  "source_contract": {
    "Czech_stemming": false,
    "VPN": "One origin-root bundle, native cs-cz/en separation; search pages /search/ and /en/search/, explicit article paths unchanged",
    "cache_recovery": "Pinned native loader fetches entry JSON with Date.now query; adapter imports fresh module query per page load, clears failed results and offers reload; no registry/config retention change",
    "dual_root_bundles": "cs/pagefind and en/pagefind, baseUrl /",
    "empty_root": "No Pagefind invocation or bundle; localized empty state without importing absent module",
    "fixture_indexed_articles": {
      "cs-cz": 2,
      "en": 1
    },
    "index_order": "Hugo rendered output -> Pagefind -> complete file/hash metadata",
    "preview": "Fresh isolated prebuild/index then native Hugo disk server --watch=false, no cleanDestinationDir; rerun same flags and reload after edits",
    "production_indexed_articles": {
      "cs-cz": 125,
      "en": 0
    },
    "real_draft_preview_indexed_articles": {
      "cs-cz": 125,
      "en": 125
    },
    "selection": "Positive article file list; title/body markers only; no nav/bylines/comments/discussion"
  },
  "status": "Committed source and quick checks accepted by lead; index yielded; joint final review waits D11.",
  "tree": "3a6516555e072ee0352ea1c700f4615841d09292"
}
```

## R10 reviewed Pagefind/link artifact proof

One fresh pinned Luna/low operation launched the exact rooted build after Gate1 review acceptance. It completed once with exit0, clean exact source before/after, and yielded the utility slot before read-only interpretation. This section binds the completed native package/version directly; the reviewer's earlier offline lookup failure is not used as version evidence.

```json
{
  "CS_feed_exact_original_GUID_date_link_full_content": true,
  "EN_production_article_count": 0,
  "actual_native_pagefind_path": "/nix/store/zwbwi2iqisisr5190lc3nyxb0fpdmzvw-pagefind-extended-1.5.2",
  "actual_native_pagefind_version": "pagefind 1.5.2",
  "artifact": "/nix/store/4slql6rxi0bzmi3ixygxq7y31ckdj6gb-vpsfree-blog-0",
  "canonical_html_pages_verified": {
    "cs": 431,
    "en": 23
  },
  "complete_2_node_lock_graph": {
    "nodes": {
      "nixpkgs": {
        "locked": {
          "lastModified": 1792422028,
          "narHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
          "owner": "NixOS",
          "repo": "nixpkgs",
          "rev": "f3a73bcf5d1c5b75a66cf35a48957e30d41d647a",
          "type": "github"
        },
        "original": {
          "owner": "NixOS",
          "ref": "nixos-26.05",
          "repo": "nixpkgs",
          "type": "github"
        }
      },
      "root": {
        "inputs": {
          "nixpkgs": "nixpkgs"
        }
      }
    },
    "root": "root",
    "version": 7
  },
  "cs_routes_and_byte_identical_sources": 125,
  "csrf_or_private_metadata_in_index": "No extra input selected; indexed files positively restricted to125publicCS article pages; actual nativeAPI negative queries belong to separate runtime/browser evidence.",
  "derivation": "/nix/store/r76d4ynzyaqvnimxjhqzq9xqmmicspfl-vpsfree-blog-0.drv",
  "empty_EN_pagefind_directory_absent": true,
  "english_drafts_fresh_and_excluded": 125,
  "feed_items": {
    "cs": 10,
    "en": 0
  },
  "gates": "Artifact interpretation complete; publication Gate2 still waits lead artifact+actual browser acceptance. No source/service/config-system rebuild or production/default action.",
  "historical_comment_anchors": 107,
  "inputs": {
    "hugoVersion": "0.167.0",
    "nixpkgsNarHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
    "nixpkgsRevision": "f3a73bcf5d1c5b75a66cf35a48957e30d41d647a",
    "pagefindVersion": "1.5.2",
    "revision": "b29f21bfa084d3b99e83d07ca8feb0b57afcfa6d",
    "source": "/nix/store/4r6isvxjd4nzw83jhv6nnwffdj73sqar-source",
    "sourceNarHash": "sha256-GDdMKj0YdD1xjAVftjHTpkaKI8vggozAsCie4sEXwyQ="
  },
  "legacy_upload_digest_copies": 1138,
  "limits": "Local Nix artifact only; no invented eligible GitHub workflow/run/artifact IDs, no human translation review, no activation/admission or deployed-state claim.",
  "lock_sha256": "865a3c07a35f43f024ce7c01614be82cb795707edac8e27092bdbba42519cd75",
  "metadata_sha256": "071fc12281dc6e818b2bfea41907d80e19ccf95fc4825d5f9a246c1c25e4c995",
  "more_anchors": 125,
  "native_build_inputs": {
    "/nix/store/hkd4g75f33sz8jhpgqylimag1m1i1sy2-hugo-0.167.0": {
      "narHash": "sha256-yaz23NvCtALFtXFr8lCCNXRQQ1uzsR58wJ4b62qxZQs=",
      "narSize": 94993968
    },
    "/nix/store/jy00n3jp5xj8s40n1fbldmkcr5n7avxc-python3-3.13.15": {
      "narHash": "sha256-GsNk36VDa0CGPpECb9c+w82JAjB8tzDygqotmpZTIiQ=",
      "narSize": 133706872
    },
    "/nix/store/zwbwi2iqisisr5190lc3nyxb0fpdmzvw-pagefind-extended-1.5.2": {
      "narHash": "sha256-O+IytCNILjU+7Yz9Ur27lCl0fFyp4AhvBK5vhTMng+A=",
      "narSize": 60085288
    }
  },
  "new_root": "result-d10",
  "nixpkgs_source_narHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
  "nixpkgs_source_path": "/nix/store/kv7b75nbhc93yrs276n0ba9gsiv8cz3b-source",
  "old_roots_preserved": [
    "result",
    "result-d9"
  ],
  "only_local_search_page_module_script_count": 2,
  "pagefind_entry": {
    "include_characters": [
      "_",
      "\u203f",
      "\u2040",
      "\u2054",
      "\ufe33",
      "\ufe34",
      "\ufe4d",
      "\ufe4e",
      "\ufe4f",
      "\uff3f"
    ],
    "languages": {
      "cs-cz": {
        "hash": "cs-cz_f490f59540ec4",
        "page_count": 125,
        "wasm": null
      }
    },
    "version": "1.5.2"
  },
  "pagefind_files_hashed": 141,
  "pagefind_version_binding": "Read from completed build metadata + derivation nativeBuildInputs + cached actual binary --version; no offline reviewer claim reused.",
  "pre_post_clean": true,
  "production_index_counts": {
    "cs-cz": 125,
    "en": 0
  },
  "search_pages": {
    "cs": {
      "has_articles": "true",
      "local_hashed_module": "/js/search.95c5f599f96adbc3b7f5b9768d5e44bbd7d62b96ea8f18d2236dd634fc9f115a.js",
      "path": "/search/"
    },
    "en": {
      "has_articles": "false",
      "local_hashed_module": "/js/search.95c5f599f96adbc3b7f5b9768d5e44bbd7d62b96ea8f18d2236dd634fc9f115a.js",
      "path": "/search/"
    }
  },
  "served_files_all_digests_verified": 1802,
  "source_manifest_sha256": "e3c56173acbc2dd018da1d7ce5cd8b73d52e5ef83847a0353b17b107e5a36ab4",
  "source_narHash": "sha256-GDdMKj0YdD1xjAVftjHTpkaKI8vggozAsCie4sEXwyQ=",
  "source_narSize": 52296712,
  "source_path": "/nix/store/4r6isvxjd4nzw83jhv6nnwffdj73sqar-source",
  "source_sha": "b29f21bfa084d3b99e83d07ca8feb0b57afcfa6d",
  "source_tree": "15e46f8e619f60c82c07a612ec8360a4a1f286a6",
  "watcher": {
    "build_result": {
      "command": [
        "/run/current-system/sw/bin/nix",
        "build",
        "--out-link",
        "result-d10",
        "--print-out-paths",
        ".#site"
      ],
      "cwd": "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog",
      "elapsed_seconds": 11.667490112944506,
      "exit_status": 0,
      "log_path": "/home/aither/workspace/ai/vpsfree.cz/work/2026-11-06-multilingual-blog-migration/r10-blog-build.log",
      "output_path": "/nix/store/4slql6rxi0bzmi3ixygxq7y31ckdj6gb-vpsfree-blog-0",
      "result_d10_symlink": "/nix/store/4slql6rxi0bzmi3ixygxq7y31ckdj6gb-vpsfree-blog-0",
      "started_utc": "2026-11-07T11:36:40.248534+00:00"
    },
    "catalog_digest": "a3f49bd3c1429d2d570cde01d509ae2d65a84c03b896c4265d9b9ccb0e317958",
    "effort": "low",
    "fresh_operation": true,
    "identity": "dw_e45f9c382e5b2ea9a5313a9410cf2005d2b36626391d8cad",
    "model": "gpt-6-luna",
    "slot_yielded_to": "implementer1 runtime/browser"
  }
}
```

Every one of1802served files matches its metadata SHA256; all125 Czech source bundles remain byte-identical to the prior manifest/source. The production Czech search entry names exactly125 pages, and English has no bundle while its localized search page uses the explicit empty-root guard. ThePagefind JS/WASM/data files are fully hashed. Actual browser-native query isolation, negative navigation/comment terms, missing-shard recovery, snapshot freshness and localized-link interaction remain with the separately released U10 operation, not inferred by grepping compressed index bytes.

## R10 final feature publication and authoritative CI

The lead released exact feature publication to overlap CI with the remaining runtime verification; this was a coordination sequence, not integration/production approval. Native/API sentinel diagnostics required no source fix. The lead subsequently accepted the complete actual browser packet, and the sole fresh CI utility completed successfully. No duplicate parent polling, build, retry or runtime mutation was performed by R10.

```json
{
  "CI": {
    "conclusion": "success",
    "databaseId": 42370490884,
    "event": "push",
    "headBranch": "2026-11-06-multilingual-blog-migration",
    "headSha": "b29f21bfa084d3b99e83d07ca8feb0b57afcfa6d",
    "jobs": [
      {
        "completedAt": "2026-11-07T12:00:18Z",
        "conclusion": "success",
        "databaseId": 128397434394,
        "name": "build",
        "startedAt": "2026-11-07T11:59:39Z",
        "status": "completed",
        "steps": [
          {
            "completedAt": "2026-11-07T11:59:41Z",
            "conclusion": "success",
            "name": "Set up job",
            "number": 1,
            "startedAt": "2026-11-07T11:59:40Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T11:59:42Z",
            "conclusion": "success",
            "name": "Run actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1",
            "number": 2,
            "startedAt": "2026-11-07T11:59:41Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T11:59:45Z",
            "conclusion": "success",
            "name": "Run cachix/install-nix-action@75c75c31ebece974e48ebc36b4ad125bd97bd97b",
            "number": 3,
            "startedAt": "2026-11-07T11:59:42Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T12:00:12Z",
            "conclusion": "success",
            "name": "Run nix develop -c bin/check",
            "number": 4,
            "startedAt": "2026-11-07T11:59:45Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T12:00:13Z",
            "conclusion": "success",
            "name": "Run nix develop -c bin/check-release",
            "number": 5,
            "startedAt": "2026-11-07T12:00:12Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T12:00:16Z",
            "conclusion": "success",
            "name": "Run nix build .#site",
            "number": 6,
            "startedAt": "2026-11-07T12:00:13Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T12:00:16Z",
            "conclusion": "skipped",
            "name": "Package trusted main build",
            "number": 7,
            "startedAt": "2026-11-07T12:00:16Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T12:00:16Z",
            "conclusion": "skipped",
            "name": "Run actions/upload-artifact@cf430e030ddbb5b0abf93d22962f4752f3646cd9",
            "number": 8,
            "startedAt": "2026-11-07T12:00:16Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T12:00:16Z",
            "conclusion": "success",
            "name": "Post Run actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1",
            "number": 16,
            "startedAt": "2026-11-07T12:00:16Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T12:00:16Z",
            "conclusion": "success",
            "name": "Complete job",
            "number": 17,
            "startedAt": "2026-11-07T12:00:16Z",
            "status": "completed"
          }
        ],
        "url": "https://github.com/vpsfreecz/blog/actions/runs/42370490884/job/128397434394"
      }
    ],
    "status": "completed",
    "url": "https://github.com/vpsfreecz/blog/actions/runs/42370490884",
    "workflowName": "Build blog"
  },
  "artifact_count": 0,
  "artifact_scope": "Rooted local artifact4slql6rxi0bzmi3ixygxq7y31ckdj6gb and1802-digest/source/Pagefind/search/feed/draft proof accepted by lead. Feature CI produced no eligible deployment artifact.",
  "boundaries": "Only authorized blog feature push. Configuration7bab and workspace refs untouched, no system rebuild/source/index/default/merge/PR/production/forum/machine/service/lifecycle action.",
  "comparison": {
    "base": "0354dac281978867ea8c1553b092ce19bccb5ccd",
    "captured": true,
    "head": "b29f21bfa084d3b99e83d07ca8feb0b57afcfa6d"
  },
  "default_main_HEAD_before_after": "0354dac281978867ea8c1553b092ce19bccb5ccd",
  "engine_observation": "Initial u10nomatchzzqx test term returned47 both natively and in UI, highlighting common u; not an adapter race. No unverified segmentation internals, query-parser change or source fix claimed. All-letter test corrected the harness expectation.",
  "evidence_sha256": {
    "r10-ci-watcher-result.json": "1d69457c59662af69a4a87b4ee09354ea73c5ac4329159842315e12393f866f3",
    "r10-feature-ci-artifacts.json": "244563f989470892c537c9a4622920af0d228ee4528f7d00c64a06d6cd95856c",
    "r10-feature-ci-watch.log": "6ab556e2cd7b3bc19e9f8b1d0008ef8765c971b3caa3eb8946f08e06a0590335",
    "r10-feature-ci.json": "2a9b8b6f98ad2067d4252605d3161e246ba2516ab8d30f31c046c0899479a337"
  },
  "feature_branch": "refs/heads/2026-11-06-multilingual-blog-migration",
  "final_source_sha": "b29f21bfa084d3b99e83d07ca8feb0b57afcfa6d",
  "final_source_tree": "15e46f8e619f60c82c07a612ec8360a4a1f286a6",
  "fresh_remote_proof": "Fetch and ls-remote matched expected f033 feature/main0354 before push; immediate postpush ls-remote verified exact b29 and main/HEAD unchanged0354.",
  "new_remote_feature": "b29f21bfa084d3b99e83d07ca8feb0b57afcfa6d",
  "old_remote_feature": "f0337fb7eae8797efca9254cd7208949cb0f77e4",
  "push": "Exact SHA normal fast-forward, exit0, no retry/lease/rebase",
  "remaining_product_gates": "English human review, installed machine admission, trusted-main artifact/recovery facts, forum setup and separately approved production transition remain outside this verification.",
  "remote": "git@github.com:vpsfreecz/blog.git",
  "retention": "result, result-d9, result-d10, all refs, registered real/fixture previews and session retained; no cleanup.",
  "runtime_scope": "Lead accepted owner1 final actual result JSON/screenshots: native CS/EN queries, article-only exclusions, all-letter absent token native/UI0, failure/reload/noJS/more, coherent snapshot A/B same-tab refresh, navigation/localized links and original source continuity. Runtime receipt belongs to owner1.",
  "watcher": {
    "approval": "never",
    "catalog_digest": "a3f49bd3c1429d2d570cde01d509ae2d65a84c03b896c4265d9b9ccb0e317958",
    "command": "gh run watch 42370490884 --repo vpsfreecz/blog --exit-status --interval 15",
    "duplicate_parent_polling": false,
    "effort": "low",
    "model": "gpt-6-luna",
    "native_identity": "dw_e45f9c382e5b2ea9a5313a9410cf2005d2b36626391d8cad",
    "operation": "fresh standalone exact-run watch, separate from rooted-build utility",
    "retries_or_cancellations": false,
    "sandbox": "danger-full-access",
    "slot_coordination": "Owner1 directly confirmed no active browser utility and no further launches before CI utility started. Browser used its explicit parent fallback.",
    "tool_shell_identity_note": "Utility reported both session identity environment variables absent; parent verified current session/environment and provided fixed bound absolute paths. No conflicting identity or other-session path was used.",
    "utility_elapsed_seconds": 36.3268344149692,
    "utility_exit": 0,
    "watch_duration": "Immediate terminal result; run had already completed by utility observation.",
    "watch_exit": 0
  }
}
```

The authoritative final build job completed successfully: normal checks, release checks and Nix build succeeded; protected-main packaging and artifact upload were skipped. Artifact count0 is expected on the feature branch and is not deployment proof. Both R10 operations are complete with no running process. Capacity is available after lead acceptance; search/import/release findings remain with implementer0.

## B12 reviewed correction artifact proof

After the lead accepted the mandatory final review, one fresh pinned Luna/low utility built the exact clean b5 source once. The rooted build exited0 in10.9165 seconds; the utility completed and yielded its slot directly to implementer1. Full immutable verification passed. The first verifier comparison stopped at the existing intentional absolute RSS media URLs; correcting that literal comparison to the documented RSS transform passed, with full feeds independently byte-identical to b29. No build retry or source correction occurred.

```json
{
  "source_sha": "b5e3ebe54d9c42ab89142a1bcc50192e580fff10",
  "source_tree": "4e5248b97e53b7d34b9bf1a1ccf10d3ace54854d",
  "pre_post_clean": true,
  "artifact": "/nix/store/rrv49p2bjp15rj2lnzpf5n5m13xq9xz8-vpsfree-blog-0",
  "derivation": "/nix/store/plzg4s96nr9gg43l2xpp714cm90z2lbq-vpsfree-blog-0.drv",
  "served_files_all_digests_verified": 1802,
  "metadata_sha256": "e72dd6d89f7b02f44891ca857a60ead8f8608fa96c257b649dc2e69163cbca38",
  "inputs": {
    "hugoVersion": "0.167.0",
    "nixpkgsNarHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
    "nixpkgsRevision": "f3a73bcf5d1c5b75a66cf35a48957e30d41d647a",
    "pagefindVersion": "1.5.2",
    "revision": "b5e3ebe54d9c42ab89142a1bcc50192e580fff10",
    "source": "/nix/store/vabbq85kqqjjwkkdknlg362k9a9ga7wd-source",
    "sourceNarHash": "sha256-BRIDZ4AxjFsmGqx7c8rg079++Fa9EGfJCJdlKhVctik="
  },
  "source_input_nar_receipts": {
    "/nix/store/vabbq85kqqjjwkkdknlg362k9a9ga7wd-source": {
      "narHash": "sha256-BRIDZ4AxjFsmGqx7c8rg079++Fa9EGfJCJdlKhVctik=",
      "narSize": 52301232
    },
    "/nix/store/kv7b75nbhc93yrs276n0ba9gsiv8cz3b-source": {
      "narHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
      "narSize": 206774680
    },
    "/nix/store/hkd4g75f33sz8jhpgqylimag1m1i1sy2-hugo-0.167.0": {
      "narHash": "sha256-yaz23NvCtALFtXFr8lCCNXRQQ1uzsR58wJ4b62qxZQs=",
      "narSize": 94993968
    },
    "/nix/store/jy00n3jp5xj8s40n1fbldmkcr5n7avxc-python3-3.13.15": {
      "narHash": "sha256-GsNk36VDa0CGPpECb9c+w82JAjB8tzDygqotmpZTIiQ=",
      "narSize": 133706872
    },
    "/nix/store/zwbwi2iqisisr5190lc3nyxb0fpdmzvw-pagefind-extended-1.5.2": {
      "narHash": "sha256-O+IytCNILjU+7Yz9Ur27lCl0fFyp4AhvBK5vhTMng+A=",
      "narSize": 60085288
    }
  },
  "source_tracked_files_byte_verified": 1007,
  "complete_2_node_lock_graph": {
    "nodes": {
      "nixpkgs": {
        "locked": {
          "lastModified": 1792422028,
          "narHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
          "owner": "NixOS",
          "repo": "nixpkgs",
          "rev": "f3a73bcf5d1c5b75a66cf35a48957e30d41d647a",
          "type": "github"
        },
        "original": {
          "owner": "NixOS",
          "ref": "nixos-26.05",
          "repo": "nixpkgs",
          "type": "github"
        }
      },
      "root": {
        "inputs": {
          "nixpkgs": "nixpkgs"
        }
      }
    },
    "root": "root",
    "version": 7
  },
  "effective_input_graph": {
    "inputs": {
      "nixpkgs": {
        "inputs": {},
        "path": "/nix/store/kv7b75nbhc93yrs276n0ba9gsiv8cz3b-source"
      }
    },
    "path": "/nix/store/vabbq85kqqjjwkkdknlg362k9a9ga7wd-source"
  },
  "lock_sha256": "865a3c07a35f43f024ce7c01614be82cb795707edac8e27092bdbba42519cd75",
  "native_build_inputs": [
    "/nix/store/hkd4g75f33sz8jhpgqylimag1m1i1sy2-hugo-0.167.0",
    "/nix/store/jy00n3jp5xj8s40n1fbldmkcr5n7avxc-python3-3.13.15",
    "/nix/store/zwbwi2iqisisr5190lc3nyxb0fpdmzvw-pagefind-extended-1.5.2"
  ],
  "actual_native_pagefind_version": "pagefind 1.5.2",
  "pagefind_files_byte_identical_to_b29": 141,
  "pagefind_manifest_sha256": "16bf60d466b74f8333766f6015ddaa784977f0d919aeb059e3e141bb4784d8a3",
  "search_adapter_source_sha256": "95c5f599f96adbc3b7f5b9768d5e44bbd7d62b96ea8f18d2236dd634fc9f115a",
  "search_generated_modules_identical_to_b29": {
    "cs/js/search.95c5f599f96adbc3b7f5b9768d5e44bbd7d62b96ea8f18d2236dd634fc9f115a.js": "95c5f599f96adbc3b7f5b9768d5e44bbd7d62b96ea8f18d2236dd634fc9f115a",
    "en/js/search.95c5f599f96adbc3b7f5b9768d5e44bbd7d62b96ea8f18d2236dd634fc9f115a.js": "95c5f599f96adbc3b7f5b9768d5e44bbd7d62b96ea8f18d2236dd634fc9f115a"
  },
  "search_input_native_paths_identical_to_b29": true,
  "pagefind_entry": {
    "version": "1.5.2",
    "languages": {
      "cs-cz": {
        "hash": "cs-cz_f490f59540ec4",
        "wasm": null,
        "page_count": 125
      }
    },
    "include_characters": [
      "_",
      "‿",
      "⁀",
      "⁔",
      "︳",
      "︴",
      "﹍",
      "﹎",
      "﹏",
      "＿"
    ]
  },
  "production_index_counts": {
    "cs-cz": 125,
    "en": 0
  },
  "empty_EN_bundle_absent": true,
  "canonical_html_pages_verified": {
    "cs": 431,
    "en": 23
  },
  "local_search_script_count_with_SRI": 2,
  "cs_routes_byte_identical_sources_and_rendered_article_bodies": 125,
  "source_manifest_sha256": "e3c56173acbc2dd018da1d7ce5cd8b73d52e5ef83847a0353b17b107e5a36ab4",
  "english_drafts_source_fresh_byte_identical_and_excluded": 125,
  "historical_comment_anchors": 107,
  "more_anchors": 125,
  "legacy_upload_digest_copies": 1138,
  "legacy_upload_original_bytes": 50375369,
  "feed_items": {
    "cs": 10,
    "en": 0
  },
  "CS_feed_GUID_date_link_full_body_with_RSS_absolute_media": true,
  "all_feed_bytes_identical_to_b29": true,
  "roots_retained": {
    "result": "/nix/store/8m7n2r4hpis3wn2593vj0a8iiayljc22-vpsfree-blog-0",
    "result-d9": "/nix/store/x9fa1vr5ljagv91yxmh5hwlycd0ihkzr-vpsfree-blog-0",
    "result-d10": "/nix/store/4slql6rxi0bzmi3ixygxq7y31ckdj6gb-vpsfree-blog-0",
    "result-d12": "/nix/store/rrv49p2bjp15rj2lnzpf5n5m13xq9xz8-vpsfree-blog-0"
  },
  "build_result": {
    "state": "completed",
    "command": [
      "/run/current-system/sw/bin/nix",
      "build",
      "--out-link",
      "result-d12",
      "--print-out-paths",
      "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog#site"
    ],
    "cwd": "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog",
    "started_utc": "2026-11-07T12:37:46.921589+00:00",
    "elapsed_seconds": 10.916509615955874,
    "exit_status": 0,
    "log_path": "/home/aither/workspace/ai/vpsfree.cz/work/2026-11-06-multilingual-blog-migration/b12-blog-build.log",
    "pre_identity": {
      "session": {
        "exit": 0,
        "value": "2026-11-06-multilingual-blog-migration"
      },
      "status": {
        "exit": 0,
        "porcelain": ""
      },
      "head": {
        "exit": 0,
        "value": "b5e3ebe54d9c42ab89142a1bcc50192e580fff10"
      },
      "tree": {
        "exit": 0,
        "value": "4e5248b97e53b7d34b9bf1a1ccf10d3ace54854d"
      },
      "env": {
        "DEV_SESSION_ID": null,
        "DEV_WORKSPACE": null
      }
    },
    "post_identity": {
      "session": {
        "exit": 0,
        "value": "2026-11-06-multilingual-blog-migration"
      },
      "status": {
        "exit": 0,
        "porcelain": ""
      },
      "head": {
        "exit": 0,
        "value": "b5e3ebe54d9c42ab89142a1bcc50192e580fff10"
      },
      "tree": {
        "exit": 0,
        "value": "4e5248b97e53b7d34b9bf1a1ccf10d3ace54854d"
      },
      "env": {
        "DEV_SESSION_ID": null,
        "DEV_WORKSPACE": null
      }
    },
    "result_d12": {
      "exists": true,
      "symlink_target": "/nix/store/rrv49p2bjp15rj2lnzpf5n5m13xq9xz8-vpsfree-blog-0",
      "resolved_target": "/nix/store/rrv49p2bjp15rj2lnzpf5n5m13xq9xz8-vpsfree-blog-0"
    },
    "expected": {
      "session": "2026-11-06-multilingual-blog-migration",
      "head": "b5e3ebe54d9c42ab89142a1bcc50192e580fff10",
      "tree": "4e5248b97e53b7d34b9bf1a1ccf10d3ace54854d",
      "clean": true
    }
  },
  "watcher": {
    "identity": "dw_e45f9c382e5b2ea9a5313a9410cf2005d2b36626391d8cad",
    "model": "gpt-6-luna",
    "effort": "low",
    "exit_code": 0,
    "elapsed_seconds": 49.82149590505287,
    "final": "/home/aither/workspace/ai/vpsfree.cz/work/2026-11-06-multilingual-blog-migration/b12-build-watcher-final.md"
  },
  "verifier_correction": "Initial literal article/feed body comparison stopped on existing intentional relative-page vs absolute-feed media URLs. Compared documented RSS media-origin transform, and independently identical full feed bytes against b29. No artifact/source change or build retry.",
  "reuse_scope": "All141Pagefind files, adapter source/generated modules, native paths/NARs and lock identical to accepted b29. Prior full nativeAPI/search/snapshot proof reused; no repeated suite. Changed CSS/KB focused UI belongs to implementer1.",
  "limits": "Local immutable artifact only; no eligible CI release identity invented; feature publication waits lead artifact acceptance; no config rebuild/production/default/runtime/lifecycle change."
}
```

All1802 declared served-file hashes and the complete two-node source/input graph match. All141 Pagefind files, the source/generated search adapter and native inputs are identical to accepted b29, so prior full search/API/snapshot evidence is reused without repeating that suite. All125 CS sources and rendered article bodies,125 fresh EN drafts and production exclusions,107 comment anchors,125 more anchors,1138 upload digest copies and exact10-item full Czech feed identities/dates/content remain verified. Both localized production search pages use local SRI modules; English has its explicit empty state and no bundle.

The lead separately accepted owner1 focused U12 mobile/landscape/CLI/anchor runtime proof at exact b5. Feature publication remains held until lead artifact acceptance. This is a rooted local artifact receipt, not an eligible trusted-main Actions artifact, production deployment, integration, human English review or lifecycle action. Configuration7bab was not rebuilt; all prior roots and previews remain retained.

## B12 feature publication and final CI

The lead accepted the complete immutable B12 artifact and separately accepted focused U12 runtime evidence before releasing publication. Fresh canonical SSH refs and fetch matched expected b29 feature/main0354; both were proven ancestors of exact b5. One normal exact-SHA push exited0, and immediate fresh remote proof confirmed b5 feature with main and symbolic HEAD unchanged0354. The explicit portal comparison was refreshed without changing other repositories.

```json
{
  "remote": "git@github.com:vpsfreecz/blog.git",
  "before": {
    "remote": "git@github.com:vpsfreecz/blog.git",
    "remote_before": {
      "HEAD": "0354dac281978867ea8c1553b092ce19bccb5ccd",
      "refs/heads/2026-11-06-multilingual-blog-migration": "b29f21bfa084d3b99e83d07ca8feb0b57afcfa6d",
      "refs/heads/main": "0354dac281978867ea8c1553b092ce19bccb5ccd"
    },
    "remote_symbolic_HEAD": "refs/heads/main",
    "head": "b5e3ebe54d9c42ab89142a1bcc50192e580fff10",
    "tree": "4e5248b97e53b7d34b9bf1a1ccf10d3ace54854d",
    "clean": true,
    "fetch_exit": 0,
    "main_and_old_feature_are_ancestors": true
  },
  "push": {
    "command": [
      "git",
      "push",
      "git@github.com:vpsfreecz/blog.git",
      "b5e3ebe54d9c42ab89142a1bcc50192e580fff10:refs/heads/2026-11-06-multilingual-blog-migration"
    ],
    "exit": 0,
    "elapsed_seconds": 2.14989935408812,
    "head": "b5e3ebe54d9c42ab89142a1bcc50192e580fff10",
    "remote": "git@github.com:vpsfreecz/blog.git"
  },
  "after": {
    "remote": "git@github.com:vpsfreecz/blog.git",
    "refs": {
      "HEAD": "0354dac281978867ea8c1553b092ce19bccb5ccd",
      "refs/heads/2026-11-06-multilingual-blog-migration": "b5e3ebe54d9c42ab89142a1bcc50192e580fff10",
      "refs/heads/main": "0354dac281978867ea8c1553b092ce19bccb5ccd"
    },
    "symbolic_HEAD": "refs/heads/main",
    "matches_exact_final_and_unchanged_default": true
  },
  "comparison": {
    "base": "0354dac281978867ea8c1553b092ce19bccb5ccd",
    "head": "b5e3ebe54d9c42ab89142a1bcc50192e580fff10",
    "captured": true
  },
  "actual_new_CI_run": {
    "id": 42373985435,
    "url": "https://github.com/vpsfreecz/blog/actions/runs/42373985435",
    "head": "b5e3ebe54d9c42ab89142a1bcc50192e580fff10"
  },
  "CI_state": "Completed: one fresh pinned Luna/low utility observed exact run42373985435 success; final authoritative evidence follows. No parent duplicate CI polling.",
  "runtime": "Lead accepted owner1 focused U12 actual browser packet at exact b5: six mobile flows, desktop views, nine CLI/two moved link attributes. Utility slot yielded and no more browser launches."
}
```

### B12 terminal authoritative CI result

```json
{
  "CI": {
    "conclusion": "success",
    "databaseId": 42373985435,
    "event": "push",
    "headBranch": "2026-11-06-multilingual-blog-migration",
    "headSha": "b5e3ebe54d9c42ab89142a1bcc50192e580fff10",
    "jobs": [
      {
        "completedAt": "2026-11-07T12:47:51Z",
        "conclusion": "success",
        "databaseId": 128407707644,
        "name": "build",
        "startedAt": "2026-11-07T12:46:54Z",
        "status": "completed",
        "steps": [
          {
            "completedAt": "2026-11-07T12:46:56Z",
            "conclusion": "success",
            "name": "Set up job",
            "number": 1,
            "startedAt": "2026-11-07T12:46:55Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T12:46:58Z",
            "conclusion": "success",
            "name": "Run actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1",
            "number": 2,
            "startedAt": "2026-11-07T12:46:56Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T12:47:01Z",
            "conclusion": "success",
            "name": "Run cachix/install-nix-action@75c75c31ebece974e48ebc36b4ad125bd97bd97b",
            "number": 3,
            "startedAt": "2026-11-06T12:46:58Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T12:47:42Z",
            "conclusion": "success",
            "name": "Run nix develop -c bin/check",
            "number": 4,
            "startedAt": "2026-11-07T12:47:01Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T12:47:44Z",
            "conclusion": "success",
            "name": "Run nix develop -c bin/check-release",
            "number": 5,
            "startedAt": "2026-11-07T12:47:42Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T12:47:49Z",
            "conclusion": "success",
            "name": "Run nix build .#site",
            "number": 6,
            "startedAt": "2026-11-07T12:47:44Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T12:47:49Z",
            "conclusion": "skipped",
            "name": "Package trusted main build",
            "number": 7,
            "startedAt": "2026-11-07T12:47:49Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T12:47:49Z",
            "conclusion": "skipped",
            "name": "Run actions/upload-artifact@cf430e030ddbb5b0abf93d22962f4752f3646cd9",
            "number": 8,
            "startedAt": "2026-11-07T12:47:49Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T12:47:49Z",
            "conclusion": "success",
            "name": "Post Run actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1",
            "number": 16,
            "startedAt": "2026-11-07T12:47:49Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T12:47:49Z",
            "conclusion": "success",
            "name": "Complete job",
            "number": 17,
            "startedAt": "2026-11-07T12:47:49Z",
            "status": "completed"
          }
        ],
        "url": "https://github.com/vpsfreecz/blog/actions/runs/42373985435/job/128407707644"
      }
    ],
    "status": "completed",
    "url": "https://github.com/vpsfreecz/blog/actions/runs/42373985435",
    "workflowName": "Build blog"
  },
  "artifact_count": 0,
  "watcher": {
    "identity": "dw_e45f9c382e5b2ea9a5313a9410cf2005d2b36626391d8cad",
    "model": "gpt-6-luna",
    "effort": "low",
    "sandbox": "danger-full-access",
    "approval": "never",
    "catalog_digest": "a3f49bd3c1429d2d570cde01d509ae2d65a84c03b896c4265d9b9ccb0e317958",
    "exit_code": 0,
    "elapsed_seconds": 58.18002730701119,
    "run_id": 42373985435,
    "head": "b5e3ebe54d9c42ab89142a1bcc50192e580fff10",
    "final": "/home/aither/workspace/ai/vpsfree.cz/work/2026-11-06-multilingual-blog-migration/b12-ci-watcher-final.md",
    "launch_preflight_correction": "Parent first wrapper asserted catalog_digest against raw file SHA256 and stopped before any watcher launch/CI operation. Corrected to actual catalog_digest field; no watch/check retry or duplication."
  },
  "watch_command": "gh run watch 42373985435 --repo vpsfreecz/blog --exit-status --interval 15",
  "watch_exit": 0,
  "watch_scope": "One exact new run observed after publication; completed before watch, authoritative final jobs/steps collected once. No parent duplicate polling/retry/cancellation.",
  "clean_exact_final_source": true,
  "evidence_sha256": {
    "b12-artifact-proof.json": "2d52abd6a266ccb43b9a319bf73937b7266ccc3acd71baf1099f07d437c59658",
    "b12-feature-push-result.json": "eaf075281d15485413e449c50c81772330cbeaf58f135fe9e8848fabd3fe5a6b",
    "b12-publication-preflight.json": "b45c8a9a626a0f02ead191a19ff574e4890b837998ee13f596625930cac1e7d5",
    "b12-publication-remote-after.json": "6eba45ea34937e2e1db94f7c0473641873ec022ebe2c2382924d38c4d10eb0d3",
    "b12-feature-ci.json": "41071758fca001052ed9c262094c1c43f4574f0489f71c7b26e3cdb65361f9aa",
    "b12-feature-ci-artifacts.json": "d3ad979d01443a9d7342e7fbe39064b41ebdb340029293f1b099bcfb6c493c42",
    "b12-feature-ci-watch.log": "d3b94eb12c350d46881940acb429780c49419fcf00cda326c5c70bf9484443a6",
    "b12-ci-watcher-result.json": "07f8c8e314b871461855c0365ad87d956c9c052f8b68ce8eb5647c5653c181c3"
  },
  "scope": "Blog feature exactb5 only; configuration7bab/workspace refs unchanged. Default main0354 unchanged. No merge/default/production/forum/machine/service/lifecycle action or cleanup. No source/index changes.",
  "readiness_limits": "Trusted-main packaging/upload skipped, artifact_count0. No eligible Actions deployment artifact, human English review or production transition approval. Installed admission and target activation remain blocked/defaultoff.",
  "retention": "All feature/recovery refs, result/result-d9/result-d10/result-d12 and registered previews/session retained.",
  "runtime": "Owner1 focused U12 exactb5 result accepted by lead. Prior search proof reused only after141Pagefind/adapter/native input identity verified.",
  "capacity": "B12 artifact/publication/CI evidence complete; capacity available following lead acceptance; import/search/E0/N-refresh finding ownership retained."
}
```

The single build job succeeded: normal checks, release checks and Nix build all passed. Trusted-main packaging and artifact upload were skipped; artifact count0 is expected for the feature branch and supplies no deployment eligibility. Exact final source remains clean. The CI utility completed with no running command. The initial parent launch preflight used the semantic catalog digest as a raw-file SHA and stopped before creating any watcher or CI operation; checking the actual catalog_digest field corrected that setup error, with no duplicate watch or CI retry.

## W13 workflow-test explanation and source-retirement documentation

Bounded documentation-only package: blog docs/deployment.md explains existing feature checks, local packager/configuration mock coverage and the remaining real protected-main upload/download/API-validation gate after explicit integration approval. It reconciles the inactive C13 source retirement and system-generation-first WordPress recovery with owner3 confirmation. No workflow, script, dependency, source-content, configuration or deployment changes belong to W13. Main accepted the proposed exact paragraphs with six plain-word substitutions and natural wrapping; all were applied. Owner2 retained the P13 index window until explicit yield at14da1cfc; W13 then committed only its accepted document.

Evidence is reused within its recorded scope: B12 exact-b5 Build blog run42373985435 passed normal checks, release checks and Nix build, while main-only package/upload were skipped with artifact_count0. Existing E0 producer and configuration mocked acquisition/transaction fixtures cover local deterministic/hash/identity and failure handling. None proves real trusted-main artifact upload, retention/download/visibility, protected-main/workflow API facts or installed production admission. No repeated build/test/workflow/dispatch/service/production action was performed for this explanation. C13 new-source final checks remain with owner3; W13 does not reuse the old disabled-system generation as proof of that new candidate. Final W13 doc commit and focused link/whitespace evidence are recorded below after the index yield.


## C13 WordPress source retirement: accepted source and quick checks

Lead accepted the clean configuration feature head
`314f3881366c7315f8c3d64b43ef80a027a52fa0`, tree
`95ff7c958c27d85da6b0bfec1aa798c2a98469ca`, after the separate prerequisite
`36f1f5678d69086d5274d824e7e023c8f353390d`. The prerequisite's parent is
`7bab9781d0a5eb1aed5914f0aed99f6d7d491632`; retirement's parent is the
prerequisite. Configuration index yielded empty; no blog index was used.

The two commits touch 74 distinct paths. The prerequisite changes only
`int.blog/static-blog.nix` (one insertion/deletion). Retirement changes
`int.blog/{config,module}.nix`, adds `legacy-ownership.nix`, updates
`tests/blog-static-module.nix` and `docs/operations/blog-static.md`, and removes
`wordpress.nix` plus 67 exclusively referenced site-package/policy/vendored-theme
files. The large deletion statistic comes from those obsolete source assets,
not persistent uploads/fonts or runtime data. No migrations or repeated input,
channel or generated-update streams; no pins, refs, remote defaults or history
were rewritten. Existing DNS/E0 commits remain in the feature series.

Stronger enabled-composition evaluation discovered an inherited unsupported
`listen` entry's `default = true`, which the old fixture had not forced.
Pinned NixOS `vhost-options.nix:295` defines the flag at virtual-host level;
`nginx/default.nix:421` emits `default_server` from that flag. The separate fix
moves only that flag, preserving IPv4 port 8080, unknown-host return 444 and
admission. The updated fixture forces enabled nginx service/configuration
through activation evaluation and permits the pinned inactive `localhost`
placeholder while asserting disabled nginx has no service.

Quick checks passed against pinned nixpkgs
`/nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source`:

- `nix eval --impure --json --expr 'import ./tests/blog-static-module.nix { nixpkgs = (builtins.getFlake (toString ./.)).inputs.nixpkgsStable; }'`
  checks actual site composition, absent WordPress/PHP/MariaDB/init/cron/wrappers
  and old health checks, retained identities, no legacy-state activation/tmpfiles
  paths, disabled/enabled nginx, roots/feed/PHP denial, proxy-only port 8080,
  no broad 80/8080/3306 openings, disabled pull and refused scheduling.
- Old/new effective identity comparison passed: WordPress `uid = null`, system
  user, nginx group; nginx UID/GID 60, system user; mysql UID/GID 84 with pinned
  `isSystemUser = false`. All have `/var/empty` and `createHome = false`.
  Pinned `update-users-groups.pl:217` preserves an existing UID when unset;
  `createHome = false` avoids its home ownership operation. No numeric live
  WordPress UID was invented. The retired modules have no destructive stop hook.
- Nix formatting, staged/final whitespace checks and ordinary Overcommit
  pre-commit/commit-message hooks passed for both commits. Retirement's message
  had advisory 72-column warnings; every line meets the workspace's 80-column
  limit. No hook bypass. Unaffected mocked release-helper tests were not repeated.

Module-result SHA-256:
`689c72466eb7194143a954704f873da36ebb4c0a77f0a241f3b59b1c80f1b6ab`;
old-identity receipt SHA-256:
`e3787f0396fa961892051f90c7ac753400da35d2e4e0ee799e7a55b7da21374f`;
staged-inventory SHA-256:
`bb03028a25d3a6584eeaf0d3440b695f0472bcda9c2cdcbde9fcf6fc6a98a13a`.
Raw local receipts are disposable `/tmp/c13-{module-check,old-eval}.json` and
`/tmp/c13-staged-raw.txt`; the committed tree and explanation above are durable.

Complete `/var/lib/wordpress/blog.vpsfree.cz` state (including keys/uploads/fonts),
`/var/lib/mysql`, all other persistent files, backups, logs and container storage
remain retention requirements. Source removal adds no deletion, state move,
recursive permission/ownership change, drop, aging or GC rule. All live roots,
services and data are untouched. Actual account IDs, paths, snapshots and live
retention remain a later read-only verification gate. Static/pull defaults remain
off, proxy/DNS/container identity and address unchanged: this candidate serves
neither site and must not be deployed alone. Recovery requires the retained exact
prior system generation/store closure, compatible original MariaDB/accounts/data,
then WordPress verification before proxy restoration; proxy restoration alone is
insufficient. Main accepted the operations wording and requested plain-word edits.

No SSH, live stop, activation, dry-deployment, build, push, integration, cleanup,
forum or lifecycle action occurred. Final joint independent review is pending;
owner3 retains findings and the exact `int.blog` post-review build, which must
wait for lead release. Source/quick acceptance proves no live retention or
production readiness. Session remains open.

### W13 committed source and focused documentation check

```json
{
  "package": "W13 bounded documentation/evidence only",
  "base": "14da1cfc3e7c22380872d0fa1789edea192d0c0a",
  "head": "45d04bc2be31b071cfe4011bab60ddf6d45322f5",
  "tree": "f5fddf0e2c6ce577fe8f11fa6096718b3807078c",
  "changed_files": {
    "docs/deployment.md": {
      "insertions": 45,
      "deletions": 19,
      "sha256": "7e1eb02fcc74e372bc73bec3f66a514d7640ef14b566675c22d6fe9bf1f58ef6"
    }
  },
  "main_writing_acceptance": "Exact proposed paragraphs accepted with six supplied plain-word substitutions; applied all and natural rollback wrapping before commit. C13 facts confirmed directly by owner3.",
  "focused_doc_checks": {
    "git diff --check -- docs/deployment.md": "PASS",
    "local Markdown links and unchanged command fences": "PASS",
    "stale port80 assertion absent and admission refusal retained": "PASS",
    "exact staged inventory": "Only docs/deployment.md",
    "post_commit_source_and_index": "Clean"
  },
  "commit_command": "nix develop -c git commit -F <temporary message file>",
  "commit_exit": 0,
  "hooks": "Repository declares no hook framework; Git default commit hooks absent. No hooks disabled or bypassed.",
  "history": "One documentation commit atop owner2 P13 exact14da1cfc, no rebase or history rewrite; no migrations; article/configuration source untouched by W13.",
  "evidence_reuse": "B12 exactb5 Actions42373985435 success and existing E0 producer/configuration mocked fixture evidence only within prior recorded scope. No new build/test/workflow executed for unchanged scope.",
  "scope_limits": "No workflow/script/new mode/dispatch/dependency/application/config/source-content/index-sharing violation/push/default/production/service/lifecycle changes. Source evidence only: mandatory combined review and exact-final artifact/CI remain with later lead release; old checks do not certify later changed P13/C13 source.",
  "remaining_gates": "Real protected-main exact-source artifact upload/download/retention/visibility and independent API validation only after explicit integration approval; production admission remains unavailable. No current-blog transition authorized.",
  "index": "Explicit owner2 yield received, W13 commit finished, index immediately yielded to lead; no staged entries remain."
}
```


## C14 supersedes C13: WordPress/static coexistence restored

C13 retirement `314f3881366c7315f8c3d64b43ef80a027a52fa0` and its pure build
are **superseded evidence, not current-candidate certification**. Recovery ref
`refs/heads/2026-11-06-multilingual-blog-migration-c13-recovery` retains that
exact head, tree `95ff7c958c27d85da6b0bfec1aa798c2a98469ca`, prior review and
build provenance. No old output or `.confctl` generation was removed.

After verifying clean exclusive ownership, native
`git rebase --onto 36f1f5678d69086d5274d824e7e023c8f353390d 314f3881366c7315f8c3d64b43ef80a027a52fa0`
omitted only the unpublished retirement commit. Result was unchanged `36f1f567`,
tree `b80b55245a44319425cdf4ccaaa4f54e6cfce542`; published `7bab9781` ancestry
and cached remote feature ref were preserved. WordPress/config/module/all 67
site-package files match `7bab9781` exactly, with the ownership-only module and
nginx conditional absent. The sole difference from that base was the retained
valid vhost-default fix. All prior results/generation files and symlinks survived
unchanged; no reset, clean, stash, default rewrite or runtime operation.

New C14 commit `8f122c39f6756860c3f8a6417fa5533561e3c1e8`, parent
`36f1f5678d69086d5274d824e7e023c8f353390d`, tree
`d46442c77217174bc4f34af3068c2a5b11caceaf`, changes only
`tests/blog-static-module.nix` and `docs/operations/blog-static.md`.
Range-diff of `7bab..314f` against `7bab..8f122` proves `36f` unchanged,
`314f` removed and the new coexistence commit added. This intentionally changes
the retirement behavior; no whole-range semantic equivalence is claimed.

Focused module evaluation passed using the same pinned nixpkgs and exact
`nix eval --impure --json --expr 'import ./tests/blog-static-module.nix { nixpkgs = (builtins.getFlake (toString ./.)).inputs.nixpkgsStable; }'`
command. It forces actual nginx unit/activation generation in both states,
proves disabled static equals original hardened WordPress, and enabled static
adds 8080 while preserving active WP80/PHP/MariaDB/init/cron/wrappers, accounts,
persistent paths and health checks. Feed/PHP denial/default444/proxy-only rules
and blocked/unwanted/no-timer pull remain checked. WordPress UID stays null;
nginx remains 60:60 and mysql 84:84 with its pinned false system-user setting.
Quick-result SHA-256:
`f07e5b121eb76b79a891ad4ef4ae0d9333bdc435173c3954ba9b05cbbb6338be`.
Nixfmt, whitespace and ordinary commit hooks passed; only advisory 72-column
message warnings, with all lines within the required 80 columns. Main accepted
actual doc copy, including its two requested wording corrections. Index yielded
empty and source clean at exact final head. No migrations or input-update streams.

No C14 system build, receiver/admission implementation, publication, downstream
artifact release, activation, SSH, claims, data change, cleanup or GC. WordPress
remains the initial public service; `prepare` stages without setting `current`.
Webhook notification is selected future work, not active delivery. Renewed final
review must precede a released exact C14 build; C13's output cannot substitute.
Lead owns acceptance and later operation windows; config findings remain owner3's.

## W15 amended workflow/coexistence/webhook documentation

The user replaced the proposed WordPress retirement with staged coexistence, then selected native GitHub workflow-completion notifications instead of scheduled polling. W15 owns only blog docs/deployment.md and this existing evidence record. The unpublished W13 documentation head45d04bc2be31b071cfe4011bab60ddf6d45322f5 is retained exactly under refs/heads/recovery/2026-11-06-multilingual-blog-migration-w13-45d04bc; its retirement wording is superseded. Its parent14da1cfc3e7c22380872d0fa1789edea192d0c0a and published b5/U13/P13 history remain unchanged. D13 downstream artifact/runtime/publication was held before any blog build or runtime launch and is not reused as proof of revised source.

The W15 draft preserves the feature/local-fixture/protected-main test explanation and replaces obsolete retirement/timer wording with active WordPress80, default-off exact-path webhook ingress through existing proxy/backend80 to loopback8091, HMAC-authenticated durable wake-up and independent HTTPS artifact preparation only. It distinguishes operator-provisioned HMAC/read-token credentials, explicit redelivery or worker retry, unchanged current pointer, unavailable admission and separate later private/public cutover gates. Owner3 confirmed settled D15 route and source facts; H15/N15 source/runtime verification remains with those owners and is not certified here. Exact proposed paragraphs were sent for main-context writing acceptance before any staging/amendment. No workflow/script/build/runtime/network/dispatch/credential/service/production action belongs to W15.

### W15 final amended documentation/history proof

Main accepted the exact D15 proposal with two clarifications: distinguish GitHub inbound-SSH needs from ordinary operator access, and describe credential provisioning as part of coexistence deployment without inventing another prose approval chain. Both were applied before the normal amendment. The actual task authorization remains source/documentation only; no runtime credential, hook registration, build, dispatch, deployment or public switch was performed.

```json
{
  "base": "14da1cfc3e7c22380872d0fa1789edea192d0c0a",
  "old_head": "45d04bc2be31b071cfe4011bab60ddf6d45322f5",
  "new_head": "92ed3dca3120ffa3acae1b6efda6dfa974fb9dce",
  "new_tree": "cd8e3e7de8434fefd391e7ccf7706b74801fe019",
  "recovery_ref": "refs/heads/recovery/2026-11-06-multilingual-blog-migration-w13-45d04bc",
  "recovery_ref_exact_old_head": true,
  "range_diff_old": "14da1cfc3e7c22380872d0fa1789edea192d0c0a..45d04bc2be31b071cfe4011bab60ddf6d45322f5",
  "range_diff_new": "14da1cfc3e7c22380872d0fa1789edea192d0c0a..92ed3dca3120ffa3acae1b6efda6dfa974fb9dce",
  "range_diff_file": "w15-doc-range-diff.txt",
  "range_diff_sha256": "eb2a9cb2ba87ccf45966e7a75ba70f145e57ed68a4fd2bca84e14b2044bb7477",
  "same_logical_commit_count": 1,
  "changed_files": "73\t22\tdocs/deployment.md",
  "clean_working_tree_and_empty_index": true,
  "published_b5_is_ancestor": true,
  "history_conclusion": "One unpublished documentation commit amended in place; C13 retirement/polling prose superseded by coexistence/native-webhook contract. No literal patch equivalence claimed: intentional documentation semantics changed. Original45d preserved exactly; U13/P13/published b5 ancestry unchanged. No migrations, extra fixup commit, rebase or published-history rewrite.",
  "doc_checks": "Whitespace/local link/unchanged command fences PASS; exact owned staged inventory; main two copy clarifications applied.",
  "commit": "nix develop -c git commit --amend -F <temporary message file>, exit0; normal hooks, none declared/installed, none bypassed."
}
```

The existing feature checks, local packager/configuration mock coverage and later protected-main actual upload/download/API proof remain documented. WordPress is retained at80; exact native workflow-run/HMAC/loopback ingress is a default-off configuration contract being implemented separately. Durable notification leads only to independently validated immutable preparation, never current-pointer changes or fenced commands. Explicit failure recovery and unavailable private-activation admission remain visible. These words do not certify H15/N15 code or deployed behavior. The amended blog milestone can proceed to its own independent final review and exact artifact/UI verification under the next lead release, separately from ongoing config implementation. No such verification has been launched. All prior refs/roots/previews/session remain retained. Capacity is available after acceptance; source/import/search/release findings remain owned.

## D15 independent BLOG rooted artifact proof at92ed

The lead accepted final independent BLOG review at exact92ed/treecd8e, including the19-commit history and amended-doc/no-migration conclusion. This milestone is independent of unfinished H15/N15 configuration. After owner2 directly confirmed the utility free, one fresh pinned Luna/low/full-access/never operation launched the exact absolute rooted result-d15 command from the explicit blog worktree. It exited0 in10.31 seconds with exact clean pre/post source and all four old roots unchanged. The utility completed and yielded the successful path/slot directly to owner1 before immutable interpretation. No old45d/result-d13 operation was launched.

```json
{
  "source_sha": "92ed3dca3120ffa3acae1b6efda6dfa974fb9dce",
  "source_tree": "cd8e3e7de8434fefd391e7ccf7706b74801fe019",
  "pre_post_clean": true,
  "artifact": "/nix/store/wmfrxjri1d8mss04l8n4bz05mm3dpngc-vpsfree-blog-0",
  "derivation": "/nix/store/4aryip4c7pnr5hnz18hrkmkpmjm75x7y-vpsfree-blog-0.drv",
  "served_files_all_digests_verified": 1802,
  "metadata_sha256": "d9c73619ff3d58d2a86bf620efc1d58ddef5d8dc35a1bd4c8542d1fe8ed9b003",
  "inputs": {
    "hugoVersion": "0.167.0",
    "nixpkgsNarHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
    "nixpkgsRevision": "f3a73bcf5d1c5b75a66cf35a48957e30d41d647a",
    "pagefindVersion": "1.5.2",
    "revision": "92ed3dca3120ffa3acae1b6efda6dfa974fb9dce",
    "source": "/nix/store/mlaqnlckzzkm9a8a01hazj8fpaz5vln1-source",
    "sourceNarHash": "sha256-u5FLrvuBA6AQQQ/4URdOt3/LIE6oVgH3ixEQ3jTEmJE="
  },
  "source_input_nar_receipts": {
    "/nix/store/mlaqnlckzzkm9a8a01hazj8fpaz5vln1-source": {
      "narHash": "sha256-u5FLrvuBA6AQQQ/4URdOt3/LIE6oVgH3ixEQ3jTEmJE=",
      "narSize": 52332968
    },
    "/nix/store/kv7b75nbhc93yrs276n0ba9gsiv8cz3b-source": {
      "narHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
      "narSize": 206774680
    },
    "/nix/store/hkd4g75f33sz8jhpgqylimag1m1i1sy2-hugo-0.167.0": {
      "narHash": "sha256-yaz23NvCtALFtXFr8lCCNXRQQ1uzsR58wJ4b62qxZQs=",
      "narSize": 94993968
    },
    "/nix/store/jy00n3jp5xj8s40n1fbldmkcr5n7avxc-python3-3.13.15": {
      "narHash": "sha256-GsNk36VDa0CGPpECb9c+w82JAjB8tzDygqotmpZTIiQ=",
      "narSize": 133706872
    },
    "/nix/store/zwbwi2iqisisr5190lc3nyxb0fpdmzvw-pagefind-extended-1.5.2": {
      "narHash": "sha256-O+IytCNILjU+7Yz9Ur27lCl0fFyp4AhvBK5vhTMng+A=",
      "narSize": 60085288
    }
  },
  "source_tracked_files_byte_verified": 1007,
  "complete_2_node_lock_graph": {
    "nodes": {
      "nixpkgs": {
        "locked": {
          "lastModified": 1792422028,
          "narHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
          "owner": "NixOS",
          "repo": "nixpkgs",
          "rev": "f3a73bcf5d1c5b75a66cf35a48957e30d41d647a",
          "type": "github"
        },
        "original": {
          "owner": "NixOS",
          "ref": "nixos-26.05",
          "repo": "nixpkgs",
          "type": "github"
        }
      },
      "root": {
        "inputs": {
          "nixpkgs": "nixpkgs"
        }
      }
    },
    "root": "root",
    "version": 7
  },
  "effective_input_graph": {
    "inputs": {
      "nixpkgs": {
        "inputs": {},
        "path": "/nix/store/kv7b75nbhc93yrs276n0ba9gsiv8cz3b-source"
      }
    },
    "path": "/nix/store/mlaqnlckzzkm9a8a01hazj8fpaz5vln1-source"
  },
  "lock_sha256": "865a3c07a35f43f024ce7c01614be82cb795707edac8e27092bdbba42519cd75",
  "native_build_inputs": [
    "/nix/store/hkd4g75f33sz8jhpgqylimag1m1i1sy2-hugo-0.167.0",
    "/nix/store/jy00n3jp5xj8s40n1fbldmkcr5n7avxc-python3-3.13.15",
    "/nix/store/zwbwi2iqisisr5190lc3nyxb0fpdmzvw-pagefind-extended-1.5.2"
  ],
  "native_paths_and_NARs_identical_to_b5": true,
  "actual_pagefind_version_binding": "Same exact native store path/NAR as b5 actual pagefind1.5.2 verification; metadata1.5.2 and all141 generated files identical. No repeated version/search suite.",
  "pagefind_files_byte_identical_to_b5": 141,
  "pagefind_manifest_sha256": "16bf60d466b74f8333766f6015ddaa784977f0d919aeb059e3e141bb4784d8a3",
  "search_adapter_source_sha256": "95c5f599f96adbc3b7f5b9768d5e44bbd7d62b96ea8f18d2236dd634fc9f115a",
  "search_generated_modules_identical_to_b5": {
    "cs/js/search.95c5f599f96adbc3b7f5b9768d5e44bbd7d62b96ea8f18d2236dd634fc9f115a.js": "95c5f599f96adbc3b7f5b9768d5e44bbd7d62b96ea8f18d2236dd634fc9f115a",
    "en/js/search.95c5f599f96adbc3b7f5b9768d5e44bbd7d62b96ea8f18d2236dd634fc9f115a.js": "95c5f599f96adbc3b7f5b9768d5e44bbd7d62b96ea8f18d2236dd634fc9f115a"
  },
  "pagefind_entry": {
    "version": "1.5.2",
    "languages": {
      "cs-cz": {
        "hash": "cs-cz_f490f59540ec4",
        "wasm": null,
        "page_count": 125
      }
    },
    "include_characters": [
      "_",
      "‿",
      "⁀",
      "⁔",
      "︳",
      "︴",
      "﹍",
      "﹎",
      "﹏",
      "＿"
    ]
  },
  "production_index_counts": {
    "cs-cz": 125,
    "en": 0
  },
  "empty_EN_bundle_absent": true,
  "canonical_html_pages_verified": {
    "cs": 431,
    "en": 23
  },
  "local_search_script_count_with_SRI": 2,
  "cs_routes_byte_identical_sources_and_rendered_article_bodies": 125,
  "all250_ID_language_source_bytes_identical_to_b5": true,
  "ID_language_filehash_map_sha256": "3074c333417392cf9dd3ae4f65d8676e3de283ebf27a20df9948e191187fef52",
  "source_manifest_sha256": "42a9eccfdff8d5e76b986dc243642af867795f5a76947ef2e5cad13cdc600468",
  "old_b5_source_manifest_sha256": "e3c56173acbc2dd018da1d7ce5cd8b73d52e5ef83847a0353b17b107e5a36ab4",
  "source_manifest_semantics_identical_after_only_path_normalization": true,
  "normalized_manifest_sha256": "318183f994f41a510dc0c3421bed2a633a7303a049f92f15e9c30fd622d6c95d",
  "all_generated_manifest_file_digests_verified": 822,
  "source_mapping": "Each old/current manifest cs_file selected by immutable article_id; paired EN via same bundle filename.125 dated current bundle paths/IDs/date prefixes verified; no wp-folder assumption. Raw source-body hash and exact complete CS-file hash remain distinct and preserved.",
  "english_drafts_source_fresh_byte_identical_and_excluded": 125,
  "historical_comment_anchors": 107,
  "more_anchors": 125,
  "legacy_upload_digest_copies": 1138,
  "legacy_upload_original_bytes": 50375369,
  "feed_items": {
    "cs": 10,
    "en": 0
  },
  "CS_feed_GUID_date_link_full_body_with_RSS_absolute_media": true,
  "all_feed_bytes_identical_to_b5": true,
  "CSS_expected_U13_change": {
    "old": {
      "cs/css/site.35cc98931a14500b871be980c60e5dcbe8fa60f72bef798ff0bd0344fa76cec4.css": "35cc98931a14500b871be980c60e5dcbe8fa60f72bef798ff0bd0344fa76cec4",
      "cs/pagefind/pagefind-component-ui.css": "de389c7e5d87d6e2b10d65fb1e36e8989a12a2ad8dd6239b7e070d81fb5d8b0d",
      "cs/pagefind/pagefind-modular-ui.css": "653ab29e4de5629f6ddf5f6fcdf5d2b3eb539a8c07fff8a56b8ce2156a570788",
      "cs/pagefind/pagefind-ui.css": "e113b816110ed07b017613e901addfe635350f2a5b84990aa76c91a74b158084",
      "en/css/site.35cc98931a14500b871be980c60e5dcbe8fa60f72bef798ff0bd0344fa76cec4.css": "35cc98931a14500b871be980c60e5dcbe8fa60f72bef798ff0bd0344fa76cec4"
    },
    "new": {
      "cs/css/site.11ddee4e615cf5585d8d97665e610172c98be07b26966e45e5b6cf4aa258cdb2.css": "11ddee4e615cf5585d8d97665e610172c98be07b26966e45e5b6cf4aa258cdb2",
      "cs/pagefind/pagefind-ui.css": "e113b816110ed07b017613e901addfe635350f2a5b84990aa76c91a74b158084",
      "cs/pagefind/pagefind-component-ui.css": "de389c7e5d87d6e2b10d65fb1e36e8989a12a2ad8dd6239b7e070d81fb5d8b0d",
      "cs/pagefind/pagefind-modular-ui.css": "653ab29e4de5629f6ddf5f6fcdf5d2b3eb539a8c07fff8a56b8ce2156a570788",
      "en/css/site.11ddee4e615cf5585d8d97665e610172c98be07b26966e45e5b6cf4aa258cdb2.css": "11ddee4e615cf5585d8d97665e610172c98be07b26966e45e5b6cf4aa258cdb2"
    }
  },
  "roots_retained": {
    "result": "/nix/store/8m7n2r4hpis3wn2593vj0a8iiayljc22-vpsfree-blog-0",
    "result-d9": "/nix/store/x9fa1vr5ljagv91yxmh5hwlycd0ihkzr-vpsfree-blog-0",
    "result-d10": "/nix/store/4slql6rxi0bzmi3ixygxq7y31ckdj6gb-vpsfree-blog-0",
    "result-d12": "/nix/store/rrv49p2bjp15rj2lnzpf5n5m13xq9xz8-vpsfree-blog-0",
    "result-d15": "/nix/store/wmfrxjri1d8mss04l8n4bz05mm3dpngc-vpsfree-blog-0"
  },
  "build_result": {
    "result": "passed",
    "exit_status": 0,
    "elapsed_seconds": 10.314753907034174,
    "command": [
      "/run/current-system/sw/bin/nix",
      "build",
      "--out-link",
      "result-d15",
      "--print-out-paths",
      "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog#site"
    ],
    "cwd": "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog",
    "start_utc": "2026-11-07T16:16:24.742817+00:00",
    "end_utc": "2026-11-07T16:16:35.057673+00:00",
    "pre_identity": {
      "slug": "2026-11-06-multilingual-blog-migration",
      "workspace": "/home/aither/workspace/ai/vpsfree.cz",
      "head": "92ed3dca3120ffa3acae1b6efda6dfa974fb9dce",
      "tree": "cd8e3e7de8434fefd391e7ccf7706b74801fe019",
      "status_clean": true,
      "old_roots": {
        "result": "/nix/store/8m7n2r4hpis3wn2593vj0a8iiayljc22-vpsfree-blog-0",
        "result-d9": "/nix/store/x9fa1vr5ljagv91yxmh5hwlycd0ihkzr-vpsfree-blog-0",
        "result-d10": "/nix/store/4slql6rxi0bzmi3ixygxq7y31ckdj6gb-vpsfree-blog-0",
        "result-d12": "/nix/store/rrv49p2bjp15rj2lnzpf5n5m13xq9xz8-vpsfree-blog-0"
      }
    },
    "post_identity": {
      "head": "92ed3dca3120ffa3acae1b6efda6dfa974fb9dce",
      "tree": "cd8e3e7de8434fefd391e7ccf7706b74801fe019",
      "status_clean": true,
      "status_porcelain": ""
    },
    "output_path": "/nix/store/wmfrxjri1d8mss04l8n4bz05mm3dpngc-vpsfree-blog-0",
    "result_d15_target": "/nix/store/wmfrxjri1d8mss04l8n4bz05mm3dpngc-vpsfree-blog-0",
    "old_roots_unchanged": true,
    "old_roots_after": {
      "result": "/nix/store/8m7n2r4hpis3wn2593vj0a8iiayljc22-vpsfree-blog-0",
      "result-d9": "/nix/store/x9fa1vr5ljagv91yxmh5hwlycd0ihkzr-vpsfree-blog-0",
      "result-d10": "/nix/store/4slql6rxi0bzmi3ixygxq7y31ckdj6gb-vpsfree-blog-0",
      "result-d12": "/nix/store/rrv49p2bjp15rj2lnzpf5n5m13xq9xz8-vpsfree-blog-0"
    },
    "log": "/home/aither/workspace/ai/vpsfree.cz/work/2026-11-06-multilingual-blog-migration/d15-blog-build.log"
  },
  "watcher": {
    "identity": "dw_e45f9c382e5b2ea9a5313a9410cf2005d2b36626391d8cad",
    "model": "gpt-6-luna",
    "effort": "low",
    "sandbox": "danger-full-access",
    "approval": "never",
    "catalog_digest": "a3f49bd3c1429d2d570cde01d509ae2d65a84c03b896c4265d9b9ccb0e317958",
    "exit_code": 0,
    "elapsed_seconds": 56.73629301204346,
    "head": "92ed3dca3120ffa3acae1b6efda6dfa974fb9dce",
    "final": "/home/aither/workspace/ai/vpsfree.cz/work/2026-11-06-multilingual-blog-migration/d15-build-watcher-final.md"
  },
  "reuse_scope": "141Pagefind files, adapter source/generated modules, native paths/NARs and lock identical to accepted b5; prior full nativeAPI/search/snapshot proof reused. U13 focused UI belongs to owner1; no whole-source-tree equality asserted.",
  "limits": "Independent blog artifact only; no H15/N15 config implementation/runtime or config-system certification, eligible CI release identity, integration or production activation. Blog publication waits lead artifact+UI acceptance; all resources retained."
}
```

All1802 served-file SHA256 values match with no undeclared files. All250 CS/EN bytes are identical to accepted b5 when keyed by immutable article ID/language using each source manifest cs_file path and its paired EN file. The raw manifest SHA changes, but its entire semantics are identical after only dated-path/generated-key normalization; every generated-file hash matches. All141 Pagefind files, adapter bytes, native inputs/NARs and lock are identical to b5; prior full search/API/snapshot evidence is reused without repeating that suite. U13 CSS changes are recorded explicitly rather than claiming whole-tree equality. Routes, source/raw hashes,125ENdraft exclusion,107comment/125more anchors,1138 upload digest copies,10exact full Czech feeds/0English feed,431CS/23EN canonicals and local search/empty-English state all pass.

Owner1 independently reports focused U13 runtime PASS at exact92ed and a free utility slot; the lead owns that packet acceptance. Blog feature publication still waits lead artifact and UI acceptance. This receipt certifies only the independent blog artifact: no H15/N15 implementation, configuration build, webhook delivery, production credential, admission, activation or public transition claim. All refs/roots/previews/session remain retained.

## D15 independent BLOG final feature publication and CI

After artifact and focused UI acceptance, fresh canonical SSH refs/fetch matched expected b5 feature and main/HEAD0354; ancestry and clean exact92ed passed. A single normal exact-SHA fast-forward push exited0 in2.36seconds. Immediate fresh SSH proof confirmed feature92ed with main/HEAD unchanged0354. The explicit0354..92ed comparison was captured. One separate fresh pinned Luna/low utility observed the actual new run and collected final jobs/steps/artifacts once. No parent CI duplication, retry, cancellation or config operation occurred.

```json
{
  "final_blog_head": "92ed3dca3120ffa3acae1b6efda6dfa974fb9dce",
  "final_blog_tree": "cd8e3e7de8434fefd391e7ccf7706b74801fe019",
  "clean_exact_final_source": true,
  "canonical_remote": "git@github.com:vpsfreecz/blog.git",
  "fresh_before": {
    "remote": "git@github.com:vpsfreecz/blog.git",
    "remote_before": {
      "HEAD": "0354dac281978867ea8c1553b092ce19bccb5ccd",
      "refs/heads/2026-11-06-multilingual-blog-migration": "b5e3ebe54d9c42ab89142a1bcc50192e580fff10",
      "refs/heads/main": "0354dac281978867ea8c1553b092ce19bccb5ccd"
    },
    "remote_symbolic_HEAD": "refs/heads/main",
    "head": "92ed3dca3120ffa3acae1b6efda6dfa974fb9dce",
    "tree": "cd8e3e7de8434fefd391e7ccf7706b74801fe019",
    "clean": true,
    "fetch_exit": 0,
    "main_and_old_feature_are_ancestors": true
  },
  "push": {
    "command": [
      "git",
      "push",
      "git@github.com:vpsfreecz/blog.git",
      "92ed3dca3120ffa3acae1b6efda6dfa974fb9dce:refs/heads/2026-11-06-multilingual-blog-migration"
    ],
    "exit": 0,
    "elapsed_seconds": 2.3558943360112607,
    "head": "92ed3dca3120ffa3acae1b6efda6dfa974fb9dce",
    "remote": "git@github.com:vpsfreecz/blog.git"
  },
  "fresh_after": {
    "remote": "git@github.com:vpsfreecz/blog.git",
    "refs": {
      "HEAD": "0354dac281978867ea8c1553b092ce19bccb5ccd",
      "refs/heads/2026-11-06-multilingual-blog-migration": "92ed3dca3120ffa3acae1b6efda6dfa974fb9dce",
      "refs/heads/main": "0354dac281978867ea8c1553b092ce19bccb5ccd"
    },
    "symbolic_HEAD": "refs/heads/main",
    "matches_exact_final_and_unchanged_default": true
  },
  "comparison": {
    "base": "0354dac281978867ea8c1553b092ce19bccb5ccd",
    "head": "92ed3dca3120ffa3acae1b6efda6dfa974fb9dce",
    "captured": true
  },
  "CI": {
    "conclusion": "success",
    "databaseId": 42390960159,
    "event": "push",
    "headBranch": "2026-11-06-multilingual-blog-migration",
    "headSha": "92ed3dca3120ffa3acae1b6efda6dfa974fb9dce",
    "jobs": [
      {
        "completedAt": "2026-11-07T16:23:18Z",
        "conclusion": "success",
        "databaseId": 128458229278,
        "name": "build",
        "startedAt": "2026-11-07T16:22:22Z",
        "status": "completed",
        "steps": [
          {
            "completedAt": "2026-11-07T16:22:24Z",
            "conclusion": "success",
            "name": "Set up job",
            "number": 1,
            "startedAt": "2026-11-07T16:22:23Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T16:22:26Z",
            "conclusion": "success",
            "name": "Run actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1",
            "number": 2,
            "startedAt": "2026-11-07T16:22:24Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T16:22:29Z",
            "conclusion": "success",
            "name": "Run cachix/install-nix-action@75c75c31ebece974e48ebc36b4ad125bd97bd97b",
            "number": 3,
            "startedAt": "2026-11-07T16:22:26Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T16:23:10Z",
            "conclusion": "success",
            "name": "Run nix develop -c bin/check",
            "number": 4,
            "startedAt": "2026-11-07T16:22:29Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T16:23:11Z",
            "conclusion": "success",
            "name": "Run nix develop -c bin/check-release",
            "number": 5,
            "startedAt": "2026-11-07T16:23:10Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T16:23:16Z",
            "conclusion": "success",
            "name": "Run nix build .#site",
            "number": 6,
            "startedAt": "2026-11-07T16:23:11Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T16:23:16Z",
            "conclusion": "skipped",
            "name": "Package trusted main build",
            "number": 7,
            "startedAt": "2026-11-07T16:23:16Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T16:23:16Z",
            "conclusion": "skipped",
            "name": "Run actions/upload-artifact@cf430e030ddbb5b0abf93d22962f4752f3646cd9",
            "number": 8,
            "startedAt": "2026-11-07T16:23:16Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T16:23:17Z",
            "conclusion": "success",
            "name": "Post Run actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1",
            "number": 16,
            "startedAt": "2026-11-07T16:23:16Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T16:23:17Z",
            "conclusion": "success",
            "name": "Complete job",
            "number": 17,
            "startedAt": "2026-11-07T16:23:17Z",
            "status": "completed"
          }
        ],
        "url": "https://github.com/vpsfreecz/blog/actions/runs/42390960159/job/128458229278"
      }
    ],
    "status": "completed",
    "url": "https://github.com/vpsfreecz/blog/actions/runs/42390960159",
    "workflowName": "Build blog"
  },
  "artifact_count": 0,
  "watcher": {
    "identity": "dw_e45f9c382e5b2ea9a5313a9410cf2005d2b36626391d8cad",
    "model": "gpt-6-luna",
    "effort": "low",
    "sandbox": "danger-full-access",
    "approval": "never",
    "catalog_digest": "a3f49bd3c1429d2d570cde01d509ae2d65a84c03b896c4265d9b9ccb0e317958",
    "exit_code": 0,
    "elapsed_seconds": 43.59020903601777,
    "run_id": 42390960159,
    "head": "92ed3dca3120ffa3acae1b6efda6dfa974fb9dce",
    "final": "/home/aither/workspace/ai/vpsfree.cz/work/2026-11-06-multilingual-blog-migration/d15-ci-watcher-final.md"
  },
  "actual_watch": {
    "command": [
      "/nix/store/lmnakv2iy4b8m8saqvwkxywyd76yvypl-gh-2.100.0/bin/gh",
      "run",
      "watch",
      "42390960159",
      "--repo",
      "vpsfreecz/blog",
      "--exit-status",
      "--interval",
      "15"
    ],
    "run_id": 42390960159,
    "exit_status": 0,
    "elapsed_seconds": 0.7757679499918595,
    "log_path": "/home/aither/workspace/ai/vpsfree.cz/work/2026-11-06-multilingual-blog-migration/d15-ci-watch.log",
    "operation_state": "completed"
  },
  "watcher_log_naming": "Watcher saved complete watch output at d15-ci-watch.log rather than requested d15-feature-ci-watch.log; actual path/status retained, no watch rerun.",
  "utility_coordination": "Owner2 directly confirmed slot free before rooted build; yielded to owner1 after successful build; owner1 focused UI completed and slot free; owner2 again explicitly confirmed no H15 utility before CI. Final CI completion/free slot directly reported to owner2.",
  "duplicate_parent_CI_polling_or_retry": false,
  "artifact_runtime": "Lead accepted rootedwmfrx artifact/full1802digests/source+nativegraph/250ID-language/normalizedmanifest/141Pagefind+adapter identity and owner1 focused12forms9.66s exact92ed proof before publication.",
  "recovery_ref": {
    "refs/heads/recovery/2026-11-06-multilingual-blog-migration-w13-45d04bc": "45d04bc2be31b071cfe4011bab60ddf6d45322f5"
  },
  "history": "One W15 documentation amendment atop14da; old45d retained in recovery only. Publishedb5/U13/P13 ancestry preserved. Full19-commit blog history/no obsolete stream/no migrations reviewed by reviewer0 and accepted by lead. No force/rebase/default update or extra fixup.",
  "evidence_sha256": {
    "d15-artifact-proof.json": "91803e526752923d5d698e162beb126262f887f639ad12818dec34305d28647d",
    "d15-feature-push-result.json": "ff818b97160328f76293fc331dfd1c6fa542a11e50e1ac1b9f7c25a0a3b20259",
    "d15-publication-preflight.json": "dc6c8ea142aeff43cfa859dd0c4bfe371f82b7202e243066f08ba788792d1554",
    "d15-publication-remote-after.json": "5edcdb651af8715896f3ab35012cc0052e9c2575ad0e64bd72790fa345d85252",
    "d15-feature-ci.json": "a28385d5ddcbb23ebe1ec244751042ada9192e46ef94ca9e3576b60e9d624f26",
    "d15-feature-ci-artifacts.json": "244563f989470892c537c9a4622920af0d228ee4528f7d00c64a06d6cd95856c",
    "d15-ci-watch.log": "5dfa628e2d41514016c754ad0029432ed927bc04140ef9fdea85e97c613961f4",
    "d15-ci-watch-result.json": "c25a6b9a6ec58b26e655e3952d2b4f49db00e32100359de7076c49b1bca9f55f",
    "d15-ci-watcher-result.json": "d3057d63af2da66c178fd9b9f247a389e4bb8b98aa3013a2be1896ec8e845bcf"
  },
  "scope": "Only independent blog feature publication and verification. No configuration/workspace push, workflow dispatch, integration/default advance, production/forum request, credentials, service/machine/lifecycle operation or cleanup. H15/N15 configuration source/review/build/publication remains separate and unverified by this package.",
  "remaining_gates": "Trusted protected-main real artifact upload/download/retention/API validation after approved integration; actual signed webhook/target immutable staging after separately managed coexistence deployment; supported private activation admission and separate public cutover; human English review. Feature artifact_count0 supplies no deployment eligibility.",
  "retention": "All refs/recovery refs, result/result-d9/result-d10/result-d12/result-d15 roots and current registered previews/session retained.",
  "capacity": "Independent blog delivery complete for lead acceptance; no operation running. Capacity available after acceptance; source/import/search/release finding ownership retained."
}
```

The single build job passed normal checks, release checks and Nix build. Protected-main packaging/upload were skipped and artifact_count0 is expected for this feature branch. Final blog source is clean; both fresh utility operations are completed and no command remains running. This completes the independent blog package without certifying or publishing unfinished H15/N15 configuration. Lead owns final state and acceptance; all retained runtime/resources remain open.


## N15 default-off webhook wiring: source and quick checks

Committed `2aa36562503c8e32f02a308bc70bc9260f5ee120`, parent H15
`d2328a8ad2eeea9aea6eb90968c0bc6f4ae3149c`, tree
`d2ee9e537154e757a6f277cc7fbdd36011ad9a09`; clean source and empty config
index yielded. Five owned paths only: new `int.blog/blog-webhook.nix`, its import
in `int.blog/config.nix`, exact route in `prg/proxy/config.nix`, new
`tests/blog-webhook-module.nix` and existing `docs/operations/blog-static.md`.
No H15 Python file changed; its 14 webhook/seven release test evidence remains
owner2's exact-parent evidence and was not duplicated. Main accepted actual
operations copy and requested precision edits/check command, all applied.

The native interface was agreed directly with H15: copied Python siblings;
fixed `serve`/`work` argv; separate systemd HMAC/token credentials; shared inbox
2770 and stable root/group lock files 0660; atomic hints 0660. Receiver user
cannot access release state, worker is `blog-release` and prepares only. The
path watches pending/processing, not failed/status, with bounded crash triggers
and no polling timer. Explicit static enablement, positive IDs and distinct
absolute non-store credential strings are prerequisites; source defaults are off.
Exact Czech HTTPS hook -> existing blog IPv4:80 -> 127.0.0.1:8091 preserves
ordinary WP80 routing/hardening, body/signature headers, 1 MiB/5s request bounds,
private8080 and activation fence. No additional ingress port or current switch.

Both documented `nix eval --impure --json --expr 'import ./tests/NAME.nix { nixpkgs = (builtins.getFlake (toString ./.)).inputs.nixpkgsStable; }'`
checks passed after H15 committed: NAME `blog-webhook-module` and
`blog-static-module`. They force nginx/service generation for both proxy hops,
default-off parity, exact routing/raw-body/header policies, credential/inbox
isolation, no added ingress/timer and preserved WP services/data/accounts/health.
Result SHA-256 respectively:
`f1e14bb40239f495ebecad0d6d18e8c919016db5a620d820e3cb4b8bf114d147`,
`f07e5b121eb76b79a891ad4ef4ae0d9333bdc435173c3954ba9b05cbbb6338be`.
Ordinary Nixfmt and commit hooks passed without bypass; subject-width advisory
only (within workspace's 80-column limit). Exact staged-inventory SHA-256:
`10ded51d025d90434debdcff7331f3b4511c6fe262c6723663e9cede88afc6d7`.

No input changes: flake.nix SHA-256
`01d6cb4187fee8ca60588905b7e4902339e1948a557b10f2e6ec1a7bd9fa827b`,
flake.lock `9ed71bd9511c7b4e16e0fd9f4de483e0fe4cf54d2556e715392d28e6e60eacd8`;
pinned nixpkgs `/nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source`.
No migrations/repeated update streams; C14 restoration and recovery ref remain.
Required exact builds after final review cover both
`cz.vpsfree/containers/int.blog` and `cz.vpsfree/containers/prg/proxy`.
Registered HTTP integration, runtime credentials, webhook registration and live
proof remain later gates. No build, server, production request, SSH, provisioning,
push, default integration, deployment, activation, machine claim or cleanup
occurred in N15. All previous roots/data/services remain untouched.


## N15 final native builds and H15 HTTP rehearsal

Final reviewed source: `2aa36562503c8e32f02a308bc70bc9260f5ee120`, tree
`d2ee9e537154e757a6f277cc7fbdd36011ad9a09`. One fresh pinned Luna/low
full-access/never utility ran exactly one native related batch from the canonical
configuration worktree:

```sh
nix develop --no-write-lock-file --no-update-lock-file --command confctl --color never build --yes '{cz.vpsfree/containers/int.blog,cz.vpsfree/containers/prg/proxy}'
```

The brace selector was one literal argv element under native `FNM_EXTGLOB`, not
shell expansion. Build exit 0 in 119.056s; utility completed in 135.25s. Source,
tree and flake files stayed exact/clean pre/post. Previous result/generation files
and this configuration's native GC-root symlinks were retained; only native
current-generation links advanced. No kernel cancellation or unfinished build.
The slot/raw paths were yielded directly to owner2 before parent interpretation.
Old C13 `gn9...` output remains obsolete evidence and was not reused.

Both native generations are `2026-11-07--17-38-18` under their respective
`.confctl/generations/cz.vpsfree:containers:{int.blog,prg:proxy}` directories.
Immutable outputs, independently queried from the store:

- **cz.vpsfree/containers/int.blog**: system `/nix/store/3lqbqwphv3497kckbhph5zzbwa6fjnyf-nixos-system-blog-26.05.20261026.718f670`; derivation `/nix/store/l1bcjvw9gbahrbq8lnz4sscaj524ga0z-nixos-system-blog-26.05.20261026.718f670.drv`; NAR `sha256-1gUV0CYT2tTyTBtgkPkU2SIkyO9qY/5dQITgz2GW67I=`.
- **cz.vpsfree/containers/prg/proxy**: system `/nix/store/ri1mhpm8rnwh2fpy1l8p6aillq357ry4-nixos-system-proxy-26.05.20261026.718f670`; derivation `/nix/store/by79zk1jzr6iv9gjr3agva309bdck7cb-nixos-system-proxy-26.05.20261026.718f670.drv`; NAR `sha256-7vpk3CrT//cibKN1bigfyLrhLdSrPJs1deSvSHBNTr0=`.
- **Both autoRollback outputs**: `/nix/store/yl9vnin9wlv04cip0sqpkisk80xmccwh-auto-rollback.rb`; derivation `/nix/store/za41c9rsf8k0qv0ay8svf4kc4y2x0q51-auto-rollback.rb.drv`; NAR `sha256-jxWEsEUoscnyhIg2YmZF781gpn8CbuvYXNa85iSafSQ=`. Built only, never executed.

Root source is `/nix/store/a1w073d2awqa879ywlby97byv3kjcwp4-source`, Git
`2aa36562503c8e32f02a308bc70bc9260f5ee120`, queried/source-metadata NAR
`sha256-iVDy6KtK04dkMbRfdwjTtDDKIgPjlvLavwMZJwi+7ug=`. The complete
64-node graph/follows in offline flake metadata equals immutable committed
`2aa36562503c8e32f02a308bc70bc9260f5ee120:flake.lock` (SHA-256
`9ed71bd9511c7b4e16e0fd9f4de483e0fe4cf54d2556e715392d28e6e60eacd8`).
Full graph, per-node native `inputs`/`inputs_info`, output NARs/derivation input
graphs and compiled assertions are retained in `n15-config-build-proof.json`.
Actual input source NARs were independently matched to the corresponding lock
nodes; both nodes select nixpkgsStable and vpsadminosOsStaging, and proxy also
selects vpsadminServices:

- `nixpkgsStable`: revision `718f670e845328e9c2cecdd832835712b2cbd065`, source `/nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source`, NAR `sha256-Ee5BWo8sh3pGt70QUdRajnaginqFmWvrtdBc4gJzhks=`.
- `vpsadminosOsStaging`: revision `dd188397abe37d0bc33f4c5dfb3605206ce5e326`, source `/nix/store/cgk63vdx1wjl4ybd53abkd5aqyzc7sfa-source`, NAR `sha256-LXZP7Ghcr+1obFUD+LjlJRO63qRo/GZtSve5AX5MZ7c=`.
- `vpsadminServices`: revision `b83b26e1ba1c8e869ae3ffbcb5801ed071c3844e`, source `/nix/store/rrm4q09vliq62dqhv6syxwv6vlrzym6y-source`, NAR `sha256-J7a/I+juHiy63uDAWxANp/THIX6+Zo7r4l0zaiicSeo=`.

Compiled blog configuration retains WP nginx80/PHP/MariaDB/init/cron and timer,
complete WordPress/uploads/fonts/MySQL state paths, and original ownership:
wordpress UID=null/system/nginx group; nginx60:60/system; mysql84:84 with its
pinned false system-user setting; no home creation. Default-off webhook/static
users, units, paths and runtime credentials are absent; no8080/8091 listener or
opening. Compiled firewall retains port80 only from proxy172.16.9.140/32.
Compiled proxy retains ordinary WordPress upstream172.16.8.4:80 and the exact
hook path/Host, 1MiB/5s/buffered unchanged-body/header/no-request-log policy.
Enabled secret isolation and activation refusal remain the scope of the earlier
source fixtures/H15 tests, not an enabled-service deployment claim. Existing WP
initialization/tmpfiles rules were compiled, never executed. Actual machine IDs,
persistent data and deployed coexistence remain later verification gates.

Proof SHA-256: `1cc1e27e3f6b9701444721bfc4a97df5e1c62e0e595738c45d95671b24b10ce4`;
status: `ea012fcb953cd7318a532248052693c7c1bbf9ae915d00f5cd778e2960941d33`;
log: `9ee195d5e6a3ef16683088552ee862cf3c52db0967f62e7e720bc7aff58195df`.
Supporting `n15-config-source-inputs.json`, `n15-config-output-paths.json` and
`n15-config-role-paths.json` contain raw receipts. Read-only readers were adapted
to native Nix derivation JSONv4 and the packaged firewall ExecStart path; cached
evidence was reused and no build was repeated.

### H15 real HTTP rehearsal, same exact source

Owner2's fresh pinned Luna/low utility passed exit0 (0.40s operation,
0.151543s driver), with unchanged exact head/tree and clean source. Parent read
the result/source identity/status and independently recomputed result/driver
hashes. Real `serve` CLI and real `work` main/acquire/validate/prepare/stage paths
were exercised; only GitHub factory/API responses were synthetic. Four actual
HTTP POSTs returned401 for bad HMAC, then202 for valid delivery,202 during blocked
mocked fetch and202 for same-ID redelivery (4.516/13.291/12.229/12.695ms).
New pending work survived an active claim. Mocked current protected-main A was
staged despite delayed B/higher run999; missing-current-artifact failure reported
exact A without older fallback or pending/processing trigger markers. Same-ID
retry staged the identical key/archive with `hint_stale=true`, `activated=false`.

Staged archive SHA-256
`83e2108d76ed058e7b87e373da2428f95652b9df356250c38bae9010f06da710`.
Sentinel `current`=`releases/sentinel`, serving receipt SHA-256
`64e3e50b2aa71e0453c5bc59330c91af29679560a2b55cad2a3fe914517b2d1a` and
served SHA-256 `28d23b5214aec2ce679bb5d130e73297f3de2f22da1aed7788accd51ca37ec83`
were unchanged. Audit guard allowed only five connects to127.0.0.1:18091
(readiness + four requests), with no remote network. Evidence lives under
`h15-http-rehearsal/`; result/run.log SHA-256
`f137d64134f5319d8811ef47845080074c242a5a982c7cd8371d975e5fcf19fe`,
driver `a208cb111f7e16548476a12ec776c20cf887d885d98a11128fe50c2ba3816ec1`.

No check process remains. Registered receiver
`22b5dfd9-f039-47a5-bab2-56c430e3b0dd`, PID648120 at127.0.0.1:18091, remains
running intentionally, as owner2 verified via service authority/ss; no stop or
cleanup was performed. This workspace-UID synthetic scratch rehearsal does not
prove live GitHub, deployed nginx/two-hop routing, production Unix identities,
LoadCredential/systemd.path, admission or live WordPress coexistence. Those
remain explicit later gates. No source change/review rerun follows from this
passing rehearsal. No activation, SSH, production credentials/webhook setup,
push/default integration, machine claim, cleanup or session lifecycle action.
CONFIG feature push remains held for lead acceptance of both proofs.


## Final CONFIG feature publication

Lead accepted final builds and H15 HTTP proof, then explicitly released CONFIG
feature publication only. Fresh canonical SSH fetch plus independent `ls-remote
--symref` matched the required feature `7bab9781d0a5eb1aed5914f0aed99f6d7d491632`
and master/HEAD `5941cdb3dda259e91c6a988a7dbf08c84700b326`; both are ancestors
of clean reviewed `2aa36562503c8e32f02a308bc70bc9260f5ee120`, tree
`d2ee9e537154e757a6f277cc7fbdd36011ad9a09`. No drift or repair occurred.
Supported `dev-session worktree capture-comparison` explicitly captured
`5941cdb3dda259e91c6a988a7dbf08c84700b326..2aa36562503c8e32f02a308bc70bc9260f5ee120`
for the registered configuration repository before publication.

One ordinary exact-SHA push ran in the repository's Nix shell:

```sh
nix develop --command git push --porcelain origin 2aa36562503c8e32f02a308bc70bc9260f5ee120:refs/heads/2026-11-06-multilingual-blog-migration
```

Canonical remote: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`.
Push exited0, reporting fast-forward `7bab9781..2aa36562`; no force, rebase,
default update or hook bypass. Fresh remote verification at
2026-11-07T16:54:38.926771+00:00 proves feature exactly2aa, master and symbolic
HEAD/master still exactly5941. Local head/tree remain exact and source/index
clean. Recovery ref remains exact314f; all prior roots/generations, registered
services and session were left intact. No BLOG/workspace ref was changed.

The only declared workflow, `.github/workflows/daily-update.yml`, has schedule
and workflow_dispatch triggers, with no push trigger. Therefore there is no
applicable feature-push CI; no workflow was dispatched, repeated, monitored or
cancelled and no extra utility was launched. Raw fresh refs/preflight/push/result
are retained under the `n15-config-publication-*` / `n15-config-feature-push*`
prefixes. Publication result SHA-256: `c84a3a69d086c7f0e27f254b75e9af06c682aa7a94eaed91543e1553019d5336`.

Feature delivery is published, awaiting any separately authorized default
integration/operations. No production, deployment, secret/hook provisioning,
content activation, machine claim, cleanup, service stop or lifecycle action.
Capacity free; owner3 retains configuration source/runtime finding ownership.

## O17 read-only Piwik backend discovery: SSH trust blocker

After reading D17 and the selected coordination guide, implementer0 tried the one existing effective route to prasiatko.int.vpsfree.cz (generic user aither, port22, default identities, no jump/host alias). The single command used BatchMode=yes, StrictHostKeyChecking=yes, IdentitiesOnly=yes, ConnectTimeout=10 and ConnectionAttempts=1, with one bounded read-only metadata/source-discovery batch. SSH exited255 in0.063seconds with no stdout: “No RSA host key is known for prasiatko.int.vpsfree.cz and you have requested strict checking. Host key verification failed.” No authentication or remote command succeeded; no OS, service, app-root/version, CLI source or account data was read.

The required next fact is independently trusted host-key material and ordinary known_hosts setup for that exact hostname, plus confirmation of the intended authorized administrative account/route if generic aither is not it. No automatic host-key acceptance, keyscan trust, password prompt, alternative account/key/host, retry or remote mutation was attempted. The installed Matomo/Piwik version and supported login-list/recovery methods remain unknown; cached5.10 does not prove them. Account reading and any recovery still require exact reader/method discovery and later lead release. O17 stops at this concrete trust boundary with no operation running; no build, source/Git/config/service/collector/admin/API write or lifecycle action occurred.

### O17 exact-backend local trust follow-up

The user resolved the UI issue by disabling its uBlock Origin blocking; no DNS/proxy repair or further HTTP/browser investigation is needed. A bounded ssh-keygen -F lookup checked only prasiatko.int.vpsfree.cz and its source-verified backend IP37.205.15.53 in the effective SSH user/global known_hosts files. Neither exact target has a pre-existing key entry, so there is no fingerprint/type to report and the conditional IP SSH attempt was not launched. No trust file, key, account or remote state was changed. Required remaining facts are independently trusted host-key material and the confirmed authorized admin SSH login/route. No account discovery/recovery command is yet supported by installed-source evidence, and no operation remains running.

## B16 production-only Piwik rooted artifact at6dae

Following accepted final independent T16 review at exact6dae/treec28f (complete20-commit history/no obsolete stream/no migrations), one fresh pinned Luna/low/full-access/never utility launched the exact absolute rooted result-t16 build from the original blog worktree. Command exit0 in10.79seconds; exact clean source pre/post and all five older roots unchanged. Successful path and slot were yielded directly to owner1 before offline artifact interpretation. No tracker/backend requests or JavaScript/pixel execution occurred.

```json
{
  "source_sha": "6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344",
  "source_tree": "c28f761c78714715a2c22e455782fa325188f12e",
  "pre_post_clean": true,
  "artifact": "/nix/store/5bs03cb3g49iyl4gb81sd6kma06bcmyk-vpsfree-blog-0",
  "derivation": "/nix/store/b0ilm9m8nlm90wic7dyri3ddqy4b9zaj-vpsfree-blog-0.drv",
  "served_files_all_digests_verified": 1802,
  "metadata_sha256": "e9253b714d9d646ac0bfc60b5d2956e35110527af27997b188932f943fbaf15b",
  "inputs": {
    "hugoVersion": "0.167.0",
    "nixpkgsNarHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
    "nixpkgsRevision": "f3a73bcf5d1c5b75a66cf35a48957e30d41d647a",
    "pagefindVersion": "1.5.2",
    "revision": "6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344",
    "source": "/nix/store/s2r3nknzw11rrivi78h5i1cizs4b3z19-source",
    "sourceNarHash": "sha256-E08Il03vWCjHcsSE+Zif+G3BBjothngQp5+/3fyl/tw="
  },
  "source_input_nar_receipts": {
    "/nix/store/s2r3nknzw11rrivi78h5i1cizs4b3z19-source": {
      "narHash": "sha256-E08Il03vWCjHcsSE+Zif+G3BBjothngQp5+/3fyl/tw=",
      "narSize": 52337728
    },
    "/nix/store/kv7b75nbhc93yrs276n0ba9gsiv8cz3b-source": {
      "narHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
      "narSize": 206774680
    },
    "/nix/store/hkd4g75f33sz8jhpgqylimag1m1i1sy2-hugo-0.167.0": {
      "narHash": "sha256-yaz23NvCtALFtXFr8lCCNXRQQ1uzsR58wJ4b62qxZQs=",
      "narSize": 94993968
    },
    "/nix/store/jy00n3jp5xj8s40n1fbldmkcr5n7avxc-python3-3.13.15": {
      "narHash": "sha256-GsNk36VDa0CGPpECb9c+w82JAjB8tzDygqotmpZTIiQ=",
      "narSize": 133706872
    },
    "/nix/store/zwbwi2iqisisr5190lc3nyxb0fpdmzvw-pagefind-extended-1.5.2": {
      "narHash": "sha256-O+IytCNILjU+7Yz9Ur27lCl0fFyp4AhvBK5vhTMng+A=",
      "narSize": 60085288
    }
  },
  "source_tracked_files_byte_verified": 1008,
  "complete_2_node_lock_graph": {
    "nodes": {
      "nixpkgs": {
        "locked": {
          "lastModified": 1792422028,
          "narHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
          "owner": "NixOS",
          "repo": "nixpkgs",
          "rev": "f3a73bcf5d1c5b75a66cf35a48957e30d41d647a",
          "type": "github"
        },
        "original": {
          "owner": "NixOS",
          "ref": "nixos-26.05",
          "repo": "nixpkgs",
          "type": "github"
        }
      },
      "root": {
        "inputs": {
          "nixpkgs": "nixpkgs"
        }
      }
    },
    "root": "root",
    "version": 7
  },
  "effective_input_graph": {
    "inputs": {
      "nixpkgs": {
        "inputs": {},
        "path": "/nix/store/kv7b75nbhc93yrs276n0ba9gsiv8cz3b-source"
      }
    },
    "path": "/nix/store/s2r3nknzw11rrivi78h5i1cizs4b3z19-source"
  },
  "lock_sha256": "865a3c07a35f43f024ce7c01614be82cb795707edac8e27092bdbba42519cd75",
  "native_build_inputs": [
    "/nix/store/hkd4g75f33sz8jhpgqylimag1m1i1sy2-hugo-0.167.0",
    "/nix/store/jy00n3jp5xj8s40n1fbldmkcr5n7avxc-python3-3.13.15",
    "/nix/store/zwbwi2iqisisr5190lc3nyxb0fpdmzvw-pagefind-extended-1.5.2"
  ],
  "native_paths_and_NARs_identical_to_92ed": true,
  "pagefind_version_binding": "Same exact native store path/NAR verified previously; buildmetadata1.5.2 and141generatedfiles identical. No new version/search suite.",
  "pagefind_files_byte_identical_to_92ed": 141,
  "search_adapter_source_sha256": "95c5f599f96adbc3b7f5b9768d5e44bbd7d62b96ea8f18d2236dd634fc9f115a",
  "search_generated_modules_identical_to_92ed": {
    "cs/js/search.95c5f599f96adbc3b7f5b9768d5e44bbd7d62b96ea8f18d2236dd634fc9f115a.js": "95c5f599f96adbc3b7f5b9768d5e44bbd7d62b96ea8f18d2236dd634fc9f115a",
    "en/js/search.95c5f599f96adbc3b7f5b9768d5e44bbd7d62b96ea8f18d2236dd634fc9f115a.js": "95c5f599f96adbc3b7f5b9768d5e44bbd7d62b96ea8f18d2236dd634fc9f115a"
  },
  "all_nonHTML_served_file_hashes_identical_to_92ed": 1348,
  "CSS_identical_to_92ed": {
    "cs/css/site.11ddee4e615cf5585d8d97665e610172c98be07b26966e45e5b6cf4aa258cdb2.css": "11ddee4e615cf5585d8d97665e610172c98be07b26966e45e5b6cf4aa258cdb2",
    "cs/pagefind/pagefind-ui.css": "e113b816110ed07b017613e901addfe635350f2a5b84990aa76c91a74b158084",
    "cs/pagefind/pagefind-component-ui.css": "de389c7e5d87d6e2b10d65fb1e36e8989a12a2ad8dd6239b7e070d81fb5d8b0d",
    "cs/pagefind/pagefind-modular-ui.css": "653ab29e4de5629f6ddf5f6fcdf5d2b3eb539a8c07fff8a56b8ce2156a570788",
    "en/css/site.11ddee4e615cf5585d8d97665e610172c98be07b26966e45e5b6cf4aa258cdb2.css": "11ddee4e615cf5585d8d97665e610172c98be07b26966e45e5b6cf4aa258cdb2"
  },
  "production_siteIDs_from_source_TOML": {
    "cs": 4,
    "en": 10
  },
  "production_tracker_markup": {
    "cs": {
      "base_layout_pages_with_exact_inline_and_pixel": 302,
      "redirect_HTML_excluded": 129,
      "all_HTML_files": 431
    },
    "en": {
      "base_layout_pages_with_exact_inline_and_pixel": 12,
      "redirect_HTML_excluded": 11,
      "all_HTML_files": 23
    }
  },
  "changed_HTML_files_exactly_inline_plus_noscript_addition": 314,
  "external_tracker_execution_or_requests": 0,
  "RSS_tracking_absent": true,
  "native_preview_exclusion_scope": "Owner1 separately owns released HTML-only preview and production-environment IsServer HTTP proof, no tracker execution. Source guard requires production, not IsServer, positive ID; fixtureIDs0.",
  "pagefind_entry": {
    "version": "1.5.2",
    "languages": {
      "cs-cz": {
        "hash": "cs-cz_f490f59540ec4",
        "wasm": null,
        "page_count": 125
      }
    },
    "include_characters": [
      "_",
      "‿",
      "⁀",
      "⁔",
      "︳",
      "︴",
      "﹍",
      "﹎",
      "﹏",
      "＿"
    ]
  },
  "production_index_counts": {
    "cs-cz": 125,
    "en": 0
  },
  "empty_EN_bundle_absent": true,
  "canonical_html_pages_verified": {
    "cs": 431,
    "en": 23
  },
  "local_search_script_count_with_SRI": 2,
  "cs_routes_byte_identical_sources_and_rendered_article_bodies": 125,
  "all250_ID_language_source_bytes_identical_to_92ed": true,
  "ID_language_filehash_map_sha256": "3074c333417392cf9dd3ae4f65d8676e3de283ebf27a20df9948e191187fef52",
  "source_manifest_sha256": "42a9eccfdff8d5e76b986dc243642af867795f5a76947ef2e5cad13cdc600468",
  "source_manifest_bytes_identical_to_92ed": true,
  "source_mapping": "Manifestcs_file -> dated bundle; pairedEN same directory, keyed immutablearticleID/language. Rawbodyhash and completeCSfilehash distinct and unchanged.",
  "english_drafts_source_fresh_byte_identical_and_excluded": 125,
  "historical_comment_anchors": 107,
  "more_anchors": 125,
  "legacy_upload_digest_copies": 1138,
  "legacy_upload_original_bytes": 50375369,
  "feed_items": {
    "cs": 10,
    "en": 0
  },
  "CS_feed_GUID_date_link_full_body_with_RSS_absolute_media": true,
  "all_feed_bytes_identical_to_92ed": true,
  "roots_retained": {
    "result": "/nix/store/8m7n2r4hpis3wn2593vj0a8iiayljc22-vpsfree-blog-0",
    "result-d9": "/nix/store/x9fa1vr5ljagv91yxmh5hwlycd0ihkzr-vpsfree-blog-0",
    "result-d10": "/nix/store/4slql6rxi0bzmi3ixygxq7y31ckdj6gb-vpsfree-blog-0",
    "result-d12": "/nix/store/rrv49p2bjp15rj2lnzpf5n5m13xq9xz8-vpsfree-blog-0",
    "result-d15": "/nix/store/wmfrxjri1d8mss04l8n4bz05mm3dpngc-vpsfree-blog-0",
    "result-t16": "/nix/store/5bs03cb3g49iyl4gb81sd6kma06bcmyk-vpsfree-blog-0"
  },
  "build_result": {
    "command": [
      "/run/current-system/sw/bin/nix",
      "build",
      "--out-link",
      "result-t16",
      "--print-out-paths",
      "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog#site"
    ],
    "cwd": "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog",
    "pre_identity": {
      "head": "6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344",
      "tree": "c28f761c78714715a2c22e455782fa325188f12e",
      "status": ""
    },
    "start_utc": "2026-11-07T17:42:27.216314+00:00",
    "exit_status": 0,
    "elapsed_seconds": 10.791522291954607,
    "output_path": "/nix/store/hcnhcbglh1559785y1ml75rgq6qd6nv8-blog-source.json.drv",
    "result_root_target": "/nix/store/5bs03cb3g49iyl4gb81sd6kma06bcmyk-vpsfree-blog-0",
    "post_identity": {
      "head": "6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344",
      "tree": "c28f761c78714715a2c22e455782fa325188f12e",
      "status": ""
    },
    "old_root_targets_before": {
      "result": "/nix/store/8m7n2r4hpis3wn2593vj0a8iiayljc22-vpsfree-blog-0",
      "result-d9": "/nix/store/x9fa1vr5ljagv91yxmh5hwlycd0ihkzr-vpsfree-blog-0",
      "result-d10": "/nix/store/4slql6rxi0bzmi3ixygxq7y31ckdj6gb-vpsfree-blog-0",
      "result-d12": "/nix/store/rrv49p2bjp15rj2lnzpf5n5m13xq9xz8-vpsfree-blog-0",
      "result-d15": "/nix/store/wmfrxjri1d8mss04l8n4bz05mm3dpngc-vpsfree-blog-0"
    },
    "old_root_targets_after": {
      "result": "/nix/store/8m7n2r4hpis3wn2593vj0a8iiayljc22-vpsfree-blog-0",
      "result-d9": "/nix/store/x9fa1vr5ljagv91yxmh5hwlycd0ihkzr-vpsfree-blog-0",
      "result-d10": "/nix/store/4slql6rxi0bzmi3ixygxq7y31ckdj6gb-vpsfree-blog-0",
      "result-d12": "/nix/store/rrv49p2bjp15rj2lnzpf5n5m13xq9xz8-vpsfree-blog-0",
      "result-d15": "/nix/store/wmfrxjri1d8mss04l8n4bz05mm3dpngc-vpsfree-blog-0"
    },
    "old_roots_unchanged": true,
    "log": "/home/aither/workspace/ai/vpsfree.cz/work/2026-11-06-multilingual-blog-migration/b16-blog-build.log"
  },
  "watcher": {
    "identity": "dw_e45f9c382e5b2ea9a5313a9410cf2005d2b36626391d8cad",
    "model": "gpt-6-luna",
    "effort": "low",
    "sandbox": "danger-full-access",
    "approval": "never",
    "catalog_digest": "a3f49bd3c1429d2d570cde01d509ae2d65a84c03b896c4265d9b9ccb0e317958",
    "exit_code": 0,
    "elapsed_seconds": 44.77395842492115,
    "head": "6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344",
    "final": "/home/aither/workspace/ai/vpsfree.cz/work/2026-11-06-multilingual-blog-migration/b16-build-watcher-final.md"
  },
  "reuse_scope": "141Pagefind/CSS/adapter/native/lock/nonHTML and articlebytes identical to accepted92ed; full search/UI/snapshot tests not repeated. Only new inline/pixel markup interpreted offline.",
  "limits": "Blog artifact only; no PiwikJS/pixel executed or tracker/backend contacted, no config-system/SSH/admin/sourcefix/deploy or eligibleCIartifact identity. Publication awaits lead artifact+runtime acceptance."
}
```

Every one of1802 served-file digests matches the declared exact payload. Native/source NARs, complete two-node lock/effective input graph and all250 ID-language source bytes are bound to exact6dae. Production source TOML selects CS4 and EN10. Exactly302CS and12EN nonredirect base-layout pages contain one guarded inline loader and one exact noscript pixel;129CS and11EN redirect documents contain neither. Removing only those exact additions yields byte-identical HTML to accepted92ed. All1348 non-HTML served-file digests are unchanged, including both full feeds,141Pagefind files, CSS and search adapter. The125CS routes/bodies,125freshENdraft exclusions,107comment/125more anchors,1138uploaddigest copies,431CS/23ENcanonicals,10CS exactGUID/date/link/fullbody feed and0ENfeed all pass.

No prior full search/UI/snapshot suite or configuration build was repeated. Runtime preview/VPN/fixtures and production-environment IsServer exclusion is separately assigned to owner1 as HTML-only proof; this artifact check does not execute analytics. Feature publication remains held for lead acceptance of artifact and privacy proof. No source fixes, config/system/SSH/admin/backend/collector action, deployment or lifecycle action occurred. All refs, old/new result roots, previews and session remain retained.

## B16 final BLOG feature publication and exact CI

After lead accepted both immutable artifact and actual privacy runtime proof, fresh canonical SSH refs/fetch matched expected92ed feature and main/HEAD0354. Clean exact6dae and both ancestry links passed. A single normal exact-SHA fast-forward push exited0 in2.02seconds; immediate fresh remote refs confirmed6dae with main/HEAD unchanged0354. The explicit0354..6dae portal comparison was captured. One separate fresh pinned Luna/low utility observed the actual new run and collected authoritative jobs/steps/artifact index once.

```json
{
  "final_blog_head": "6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344",
  "final_blog_tree": "c28f761c78714715a2c22e455782fa325188f12e",
  "clean_exact_final_source": true,
  "canonical_remote": "git@github.com:vpsfreecz/blog.git",
  "fresh_before": {
    "remote": "git@github.com:vpsfreecz/blog.git",
    "remote_before": {
      "HEAD": "0354dac281978867ea8c1553b092ce19bccb5ccd",
      "refs/heads/2026-11-06-multilingual-blog-migration": "92ed3dca3120ffa3acae1b6efda6dfa974fb9dce",
      "refs/heads/main": "0354dac281978867ea8c1553b092ce19bccb5ccd"
    },
    "remote_symbolic_HEAD": "refs/heads/main",
    "head": "6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344",
    "tree": "c28f761c78714715a2c22e455782fa325188f12e",
    "clean": true,
    "fetch_exit": 0,
    "main_and_old_feature_are_ancestors": true
  },
  "push": {
    "command": [
      "git",
      "push",
      "git@github.com:vpsfreecz/blog.git",
      "6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344:refs/heads/2026-11-06-multilingual-blog-migration"
    ],
    "exit": 0,
    "elapsed_seconds": 2.0248245489783585,
    "head": "6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344",
    "remote": "git@github.com:vpsfreecz/blog.git"
  },
  "fresh_after": {
    "remote": "git@github.com:vpsfreecz/blog.git",
    "refs": {
      "HEAD": "0354dac281978867ea8c1553b092ce19bccb5ccd",
      "refs/heads/2026-11-06-multilingual-blog-migration": "6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344",
      "refs/heads/main": "0354dac281978867ea8c1553b092ce19bccb5ccd"
    },
    "symbolic_HEAD": "refs/heads/main",
    "matches_exact_final_and_unchanged_default": true
  },
  "comparison": {
    "base": "0354dac281978867ea8c1553b092ce19bccb5ccd",
    "head": "6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344",
    "captured": true
  },
  "CI": {
    "conclusion": "success",
    "databaseId": 42398048773,
    "event": "push",
    "headBranch": "2026-11-06-multilingual-blog-migration",
    "headSha": "6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344",
    "jobs": [
      {
        "completedAt": "2026-11-07T17:48:23Z",
        "conclusion": "success",
        "databaseId": 128479582616,
        "name": "build",
        "startedAt": "2026-11-07T17:47:41Z",
        "status": "completed",
        "steps": [
          {
            "completedAt": "2026-11-07T17:47:43Z",
            "conclusion": "success",
            "name": "Set up job",
            "number": 1,
            "startedAt": "2026-11-07T17:47:42Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T17:47:45Z",
            "conclusion": "success",
            "name": "Run actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1",
            "number": 2,
            "startedAt": "2026-11-07T17:47:43Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T17:47:48Z",
            "conclusion": "success",
            "name": "Run cachix/install-nix-action@75c75c31ebece974e48ebc36b4ad125bd97bd97b",
            "number": 3,
            "startedAt": "2026-11-07T17:47:45Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T17:48:16Z",
            "conclusion": "success",
            "name": "Run nix develop -c bin/check",
            "number": 4,
            "startedAt": "2026-11-07T17:47:48Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T17:48:17Z",
            "conclusion": "success",
            "name": "Run nix develop -c bin/check-release",
            "number": 5,
            "startedAt": "2026-11-07T17:48:16Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T17:48:20Z",
            "conclusion": "success",
            "name": "Run nix build .#site",
            "number": 6,
            "startedAt": "2026-11-07T17:48:17Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T17:48:20Z",
            "conclusion": "skipped",
            "name": "Package trusted main build",
            "number": 7,
            "startedAt": "2026-11-07T17:48:20Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T17:48:20Z",
            "conclusion": "skipped",
            "name": "Run actions/upload-artifact@cf430e030ddbb5b0abf93d22962f4752f3646cd9",
            "number": 8,
            "startedAt": "2026-11-07T17:48:20Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T17:48:21Z",
            "conclusion": "success",
            "name": "Post Run actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1",
            "number": 16,
            "startedAt": "2026-11-07T17:48:20Z",
            "status": "completed"
          },
          {
            "completedAt": "2026-11-07T17:48:21Z",
            "conclusion": "success",
            "name": "Complete job",
            "number": 17,
            "startedAt": "2026-11-07T17:48:21Z",
            "status": "completed"
          }
        ],
        "url": "https://github.com/vpsfreecz/blog/actions/runs/42398048773/job/128479582616"
      }
    ],
    "status": "completed",
    "url": "https://github.com/vpsfreecz/blog/actions/runs/42398048773",
    "workflowName": "Build blog"
  },
  "artifact_count": 0,
  "watcher": {
    "identity": "dw_e45f9c382e5b2ea9a5313a9410cf2005d2b36626391d8cad",
    "model": "gpt-6-luna",
    "effort": "low",
    "sandbox": "danger-full-access",
    "approval": "never",
    "catalog_digest": "a3f49bd3c1429d2d570cde01d509ae2d65a84c03b896c4265d9b9ccb0e317958",
    "exit_code": 0,
    "elapsed_seconds": 48.60402793704998,
    "run_id": 42398048773,
    "head": "6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344",
    "final": "/home/aither/workspace/ai/vpsfree.cz/work/2026-11-06-multilingual-blog-migration/b16-ci-watcher-final.md"
  },
  "actual_watch": {
    "command": [
      "/nix/store/lmnakv2iy4b8m8saqvwkxywyd76yvypl-gh-2.100.0/bin/gh",
      "run",
      "watch",
      "42398048773",
      "--repo",
      "vpsfreecz/blog",
      "--exit-status",
      "--interval",
      "15"
    ],
    "exit_status": 0,
    "elapsed_seconds": 0.7856026600347832
  },
  "watcher_transcription_correction": "Final watcher prose incorrectly claimed supplied expectedSHA had extra trailinge (41chars). Saved original launch prompt contains correct40char6dae...344, authoritative final run headSha matches that exact expectedSHA, and parent checked this locally. No CI or watch failure; no retry/requery. Raw watcherreport retained unchanged.",
  "watcher_actual_log_path": "b16-ci-watch.log (watcher naming differs from requested b16-feature-ci-watch.log; complete actual log retained, no rerun).",
  "utility_coordination": "Rooted build slot yielded directly owner1; owner1 completed8HTML privacy batch/no active utility; lead released soleCI slot. Both fresh operations completed; no runningprocess.",
  "duplicate_parent_CI_polling_or_retry": false,
  "artifact_runtime_acceptance": "Lead accepted rooted5bs03 artifact1802hash/full2node/sourceNAR/nativegraph, all250ID-language bytes,302CS+12ENexactinline/pixels and140redirectsnone,1348nonHTML/feeds/141Pagefind/CSS/adapter identity; actual8HTML privacy JSON confirms preview+production-modeIsServer omit tracking. No tracker execution or request.",
  "history": "Exact20-commit blog branch inventory/history reviewed and accepted; no obsolete streams/migrations. Published92ed extended normally by oneT16commit. No force/rebase/default change.",
  "evidence_sha256": {
    "b16-artifact-proof.json": "39179645674a4ae3515500822d0d0e3d34dea2a2cf4715b52428e7fb5719d33c",
    "b16-feature-push-result.json": "52e8ad4bac12fa1401dcf8578ca5a824edff18367d3dd92e02a9548fefd3a833",
    "b16-publication-preflight.json": "dc26a37411aa8524cbce0a4abfa15405376ef148aa4beec7b39e1e9770e2da2e",
    "b16-publication-remote-after.json": "5e053a3c08e4370c944837207636d56a0d9bee8fb727ccd89d82a87ee38f3ec7",
    "b16-feature-ci.json": "8567fde74bfe40036eaca491b209ab6c74e191d3b05dc9a7d8414566c7b2c622",
    "b16-feature-ci-artifacts.json": "244563f989470892c537c9a4622920af0d228ee4528f7d00c64a06d6cd95856c",
    "b16-ci-watch.log": "e4f9210e53afffa748c787565d98b26f9f75c45ea3ca4b68695d64761302f9ef",
    "b16-ci-watch-result.json": "f05ec95adcedf68575b56eca21b16eb4b1d746ac139a09db07c23185ea41c955",
    "b16-ci-watcher-result.json": "d1b1b0937da05ac063dac0959a23fd55350430be4817dfc23081975ff655e23b"
  },
  "scope": "Independent BLOG feature only. No configuration/workspace push, workflow dispatch, default integration/advance, production/Piwiktracker/backend/admin request, SSHaccount action, credentials, service/machine/lifecycle operation or cleanup by this package.",
  "remaining_gates": "FeatureCIzeroartifacts is not trusted-main artifact/upload or deployment proof. Actual protected-main upload/download/retention/API validation requires approvedintegration; coexistence/webhook/admission/privateactivation/publiccutover and humanEnglishreview remain separate.",
  "retention": "Allrefs/recoveryrefs, result/result-d9/result-d10/result-d12/result-d15/result-t16, registeredpreviews/productionguard/session retained.",
  "capacity": "B16 source/review/rootedartifact/privacy/publication/CI evidence complete for lead acceptance; capacity available afteracceptance, findingownershipretained."
}
```

The single build job passed normal checks, release checks and Nix build. Protected-main packaging/upload were skipped, with artifact_count0. The final watcher prose transcribed an extra trailing character into its expected SHA; local comparison of its saved original prompt with the authoritative saved run metadata proves both match the exact40-character6dae source. This is a report transcription error, not a source/CI failure; no retry or new API query was performed. Raw evidence remains unchanged. Both utilities completed and no operation remains running. Lead owns final state/acceptance; all resources and recovery refs remain retained.

## E18DNS: existing English DNS and current TLS limit (2026-11-07)

Read-only evidence collected **18:02:47–18:03:10 UTC**; no DNS, configuration,
service or deployment change. Public resolver `1.1.1.1` and workspace resolver
`172.16.9.90` both returned `NOERROR` for CNAME/A/AAAA queries:

| Name / resolution step | Answer |
| --- | --- |
| `blog.vpsfree.org.` | CNAME `proxy.vpsfree.cz.`, TTL 1800 |
| Effective IPv4 | `37.205.14.61` |
| Effective IPv6 | `2a03:3b40:fe:35::1` |

The public resolver returned target A TTL 60 / AAAA TTL 3600; the workspace
resolver returned both target TTLs 3600. `/etc/resolv.conf` selects
`172.16.9.90` first (then `172.19.9.90`, `172.16.106.1`); only the first was
queried. Public NS discovery returned `ns.forpsi.cz`, `ns.forpsi.it`,
`ns.forpsi.net`. Direct nonrecursive CNAME, A and AAAA queries to **each**
authority returned `NOERROR`, the authoritative `aa` flag and the same
`blog.vpsfree.org. 1800 IN CNAME proxy.vpsfree.cz.` (the alias, rather than
independent A/AAAA records). Actual authoritative server addresses were
`81.2.209.185`, `95.110.254.165`, `81.2.194.130`, respectively.
Commands used `dig @RESOLVER blog.vpsfree.org TYPE +time=3 +tries=1`;
authoritative queries also used `+norecurse`. All DNS commands exited 0.

Source comparison at configuration commit
`2aa36562503c8e32f02a308bc70bc9260f5ee120`: public proxy address records match
`configs/public-dns/zone.vpsfree.cz.:114–115`; the internal counterparts match
`configs/internal-dns/zone.vpsfree.cz.:89–90`. The current public proxy has a
Czech blog vhost and WordPress port-80 route in
`cluster/cz.vpsfree/containers/prg/proxy/config.nix:287–312`, with no
`blog.vpsfree.org` vhost. The inactive static candidate separately declares the
English Host in `cluster/cz.vpsfree/containers/int.blog/static-blog.nix:105–106`.
The observed `.org` DNS authority is FORPSI; no `.org` zone edit is proposed.

One normal HTTPS HEAD at **18:03:10 UTC** used
`curl --noproxy '*' --head --connect-timeout 5 --max-time 10 --max-redirs 0 --proto '=https' --silent --show-error https://blog.vpsfree.org/`.
It exited **60**: `SSL: no alternative certificate subject name matches target
hostname 'blog.vpsfree.org'`; reported HTTP code was `000` (no HTTP response
obtained), `ssl_verify_result=1`, elapsed 0.086730 s. Certificate verification
was not bypassed, no redirect was followed and no page assets, JavaScript or
tracker were fetched/executed. The selected peer IP was not exposed in curl's
failure output; this check does not certify both address families or an HTTP
content route.

**Rollout implication:** English DNS already targets the intended current proxy.
Retain that DNS and prepare/verify the English TLS certificate and public vhost/
route under the accepted rollout design before calling the English site usable.
The isolated English backend declaration alone does not provide public TLS or
prove serving readiness. No SSH/admin/account/hook/forum action, source edit,
Git index/ref mutation, build, utility or service operation was performed.


## H18 selectable hosting and finite legacy routes: accepted source

Lead accepted commit937fd3717203d4daf2076d733f97a2236b36cdca, parent
2aa36562503c8e32f02a308bc70bc9260f5ee120, tree
7126940aaf416c44d6e5a0d4c4100a5cf45e197c. Eight owned paths:
prg/proxy/{blog.nix,config.nix}, int.blog/{legacy-routes.nix,config.nix},
data/blog-legacy-routes.json and tests/{blog-proxy-module.nix,
blog-legacy-module.nix,blog-legacy-projection.py}. Diff3082+/32- includes2706
generated JSON lines for the finite540-row projection. All eight owned files
equal committed blobs; index yielded empty directly to A18 owner0. His six dirty
publication/static/webhook/Python/test files were preserved; no whole-tree
clean claim. No owner0 existing fixture, guide or blog source edit by H18.

Proxy enableEnglish/serveStatic both defaultfalse. Default Czech WP80 and exact
hook80 settings remain equivalent (moved hook block checked apart from
indentation). English opt-in supplies ACME/forceSSL with prelaunch503;
serveStatic requires English and routes both article Hosts to existing
blogIPv4:8080 with their correct fixed Host. Hook80 remains unchanged through
cutover; switching static off restores CZWP80/EN503. No DNS/certificate/runtime
or original WP/account/data/health/input change.

Static-gated ordinary nginx maps contain the exact540 kind/source/target rows
from blog manifest SHA256
42a9eccfdff8d5e76b986dc243642af867795f5a76947ef2e5cad13cdc600468.
Projection SHA256
48b90b9aa5317c3334e60fafabd119aa7e16461acf852262c7c4b67dc19e720a.
Case-sensitive anchored request-URI keys select only fixed absolute Czech
destinations; redirect consumes the query and preserves recorded comment
fragments. Direct RSS and exact/?feed=rss2 alias remain. Literal identity/feed
key detection is case-insensitive after exact-map miss: unknown, missing,
duplicate and extra combinations return404. Percent-encoded key aliases such
as%70 are explicitly outside captured identities, receive ordinary static
handling and never infer post8. No decoder, online lookup, PHP/rewrite service
or English legacy identity was introduced.

Focused quick commands passed:
- nix eval --impure --json --expr 'import ./tests/blog-proxy-module.nix { nixpkgs = (builtins.getFlake (toString ./.)).inputs.nixpkgsStable; }'
- nix eval --impure --json --expr 'import ./tests/blog-legacy-module.nix { nixpkgs = (builtins.getFlake (toString ./.)).inputs.nixpkgsStable; }'
- nix develop -c python3 tests/blog-legacy-projection.py --manifest ../blog/data/migration/source-manifest.json --module-result /tmp/h18-legacy-check.json

They force generated nginx/unit/activation for valid modes, reject static without
English, preserve WP80/feed/PHP protections, omit CZ aliases from English, and
check all540 generated map destinations/query/fragment/feed/404/non-inference
cases. Python consumes the actual generated map regex/value output as a unit
check; it is not a real nginx-response certificate. Formatting/whitespace and
ordinary Nixfmt/commit-message hooks passed without bypass. Staged inventory
SHA2561c04b8e99a0aa5ecd45d4983fa07c624fc56b5334e8e350ef931b3580f157a7d.
No broad old/full suite duplicated; owner0 was told to retain the extracted
blog.nix import in his existing webhook fixture's filtered composition.

Whole250CS/EN files and body bytes matched committed blog
7fa57c809d828e945b104f5ab3fa74f76a030a51, corpus digest
d813fcbda67a754b33ffdfbef47b191899d9d6d5adffc06c56557fc02f4e54b6 and body
digest01b432d3932365a36850c9c273de3173a35e9b7bc428374aed07fff1e6ad49be.
Raw local receipts h18-proxy-check.json, h18-legacy-check.json and
h18-preservation.json bind the source results. Shared operations-guide technical
paragraphs were sent to owner0 for his final sequential/main-copy window;
this EOF append preserves the architect's current plan and prior receipts.

No migrations, repeated input-update streams or pin changes. No system build,
server, network/SSH/Discourse/DNS/certificate operation, source push/default
integration/deployment or cleanup. Final combined intended commits and review
must precede exact blog/proxy builds and a bounded registered real nginx
alias/response test. Those later operations remain H18 owner3's finding/runtime
responsibility, not proof supplied by these source fixtures. Capacity free after
this receipt; no next package executing. Architect append window returned.


### H18 final verification preparation only

No build/server/HTTP/utility/reservation is launched. Exact final head/tree stay
unset until intended A18/H18 commits, combined quick checks, independent review
and direct lead launch release. Prepared canonical once-only batch remains
nix develop --no-write-lock-file --no-update-lock-file --command confctl --color
never build --yes with one literal selector
{cz.vpsfree/containers/int.blog,cz.vpsfree/containers/prg/proxy}.
Pre/post will bind exact source/lock, root Git/NAR/full input graph, per-node
inputs_info and both system/rollback outputs, retaining every prior result/
generation/native GC root (only native current links may advance). Default
compiled WP/account/data/service/listener proof does not imply enabled A18
runtime; its enabled source fixtures remain complementary.

After review/release, plan one registered pinned-final-nginx fixture, with only
loopback ports/scratch roots/feed/pid/temp paths and TLS-off/synthetic-backend
adaptations. Recheck planned19680/19681/19880/19881 ports only at launch.
Use actual final generated H18 map/server directives; test all540 exact redirects
without following Location, query stripping/comment fragments/feed, literal
identity404, encoded-key non-inference, CZWP/EN503 and both static Hosts/hook80
modes plus fixed-target/no-open-redirect. Bound it to540 and a small named set.
No remote/DNS/ACME/Discourse/tracker requests. This is adapted local response
proof, not production TLS/firewall/two-node/liveWP/webhook delivery or enabled
publication-authority proof. Parent owns registration; leave service/evidence
open unless an exact later stop is authorized. Max1 fresh pinned utility:
two-node build first, then a new probe utility. No duplicate Python/Nix suites,
source edit, activation, deployment/default/push/cleanup or lifecycle action.
Preparation plan is disposable /tmp/h18-verification-preparation.json; current
record is the durable dependency/limit summary. Architect window returned.

## A18 committed operator publication source and quick evidence

The lead released the sufficient operator-policy design and accepted exact source-facing prose before commits. H18 first config and D19 first blog index windows yielded directly; A18 then committed its owned paths with normal hooks, preserving both predecessors. This section is source/quick evidence only and supplies no runtime, deployment or integration approval.

```json
{
  "configuration": {
    "base": "937fd3717203d4daf2076d733f97a2236b36cdca",
    "head": "9ea9fbd9f9a436f82249c08d9e3efc485fe8bff8",
    "tree": "d160b48cd08b5bce350610120732edd068685540",
    "files": [
      "cluster/cz.vpsfree/containers/int.blog/blog-webhook.nix",
      "cluster/cz.vpsfree/containers/int.blog/static-blog.nix",
      "docs/operations/blog-static.md",
      "tests/blog-static-module.nix",
      "tests/blog-static-release.py",
      "tests/blog-webhook-module.nix",
      "tests/blog-webhook.py",
      "tools/blog-static-release.py",
      "tools/blog-webhook.py"
    ],
    "stat": "9paths1077insertions/200deletions",
    "clean_and_index_yielded": true,
    "normal_hooks": "Nixfmt/precommit and commitmsg passed; only nonblocking72columnwarning, allmessage lines<=80; no bypass"
  },
  "blog": {
    "base": "5032d82ffd43870aa7e0aa6dd332300e4ce2f3b4",
    "head": "3fb7d25b1ca39dcddf3dcc8a22b2e47bcf0e49a2",
    "tree": "743521562f0ef6b1e419011e55888ced23637cea",
    "files": [
      "AGENTS.md",
      "README.md",
      "docs/authoring.md",
      "docs/deployment.md",
      "skills/blog-authoring/SKILL.md"
    ],
    "stat": "5approveddocpaths91insertions/60deletions",
    "clean_and_index_yielded": true,
    "normal_commit": "nix develop -c git commit -F temporarymessage exit0; repository declares no framework, no hooks bypassed",
    "D19_discussion_paragraph_preserved": true
  },
  "quick_checks": {
    "pinned_python": "nix develop -c python3 tests/blog-static-release.py:17PASS/1.533s; tests/blog-webhook.py:19PASS/1.799s",
    "module_batch": [
      {
        "name": "static-module",
        "argv": [
          "/run/current-system/sw/bin/nix",
          "eval",
          "--impure",
          "--json",
          "--expr",
          "import ./tests/blog-static-module.nix { nixpkgs = (builtins.getFlake (toString ./.)).inputs.nixpkgsStable; }"
        ],
        "exit_status": 0,
        "elapsed_seconds": 40.263,
        "log": "/home/aither/workspace/ai/vpsfree.cz/work/2026-11-06-multilingual-blog-migration/a18-static-module.log"
      },
      {
        "name": "webhook-module",
        "argv": [
          "/run/current-system/sw/bin/nix",
          "eval",
          "--impure",
          "--json",
          "--expr",
          "import ./tests/blog-webhook-module.nix { nixpkgs = (builtins.getFlake (toString ./.)).inputs.nixpkgsStable; }"
        ],
        "exit_status": 0,
        "elapsed_seconds": 41.053,
        "log": "/home/aither/workspace/ai/vpsfree.cz/work/2026-11-06-multilingual-blog-migration/a18-webhook-module.log"
      }
    ],
    "all9checked_hashes_equal_final_commit_blobs": {
      "tools/blog-static-release.py": "bce0e4ad2e61648079e4a6ae7eec284d0c5a05217866446dde7016390eb42fc7",
      "tools/blog-webhook.py": "132df79c7bd148390a5a149e4d9fa49b30b24fa19d1f55539c70ca005d07944d",
      "tests/blog-static-release.py": "712170836cb9b6f631e551abb86e75f54cbcc38eed54914fba197d52033d5234",
      "tests/blog-webhook.py": "b8f0322f981b68d0fd9b7bd2f9c2813dd5c0530ae2eab8760e233a91e22abb6d",
      "cluster/cz.vpsfree/containers/int.blog/static-blog.nix": "d89dd3d4cadf2e538e46cf12250e965f06779b55ba1769ab95b0d1435e48ba95",
      "cluster/cz.vpsfree/containers/int.blog/blog-webhook.nix": "c0ccaa0b2d194d285379fbb94e14df4503b49d342c3f0c9968f512bd21f4f5ad",
      "tests/blog-static-module.nix": "6cef14874fff803d6a532c9968c9cc7c54f1e304e4352c6e14b502a0e0ad52ba",
      "tests/blog-webhook-module.nix": "9f57668de245d93dca82be2b2f7b6d08c780134f2a5e02cfebbc801e0ad63051",
      "docs/operations/blog-static.md": "6713729ebf9a87ab41d7037f0c49bdcbcf8fbfefaaaeda977919b880306067e7"
    },
    "other": "Owned Nixfmt, Python AST, actual relative Markdown links, fixed CLI examples and scoped whitespace passed."
  },
  "policy_contract": {
    "options": "services.vpsfree-static-blog.publication.enable=false default; explicitrepositoryId/workflowId/externalreadtoken, webhooksettingsmustmatch; pull.enable periodicpoll unsupported",
    "immutable_policy": "/etc/blog-release-policy.json -> compiled Nixpolicy fixesrepository/workflow/state, includesbothhelpers implementationdigest; helperbinds its starting /run/current-system identity and rejects latergenerationchange",
    "root_control": "/var/lib/blog-control root:blog-release0750, stabletransaction.lock0660; rootrecord0640, absent/unknown/changed defaults paused; publicationservicecanlockbutcannotreplace/unlinklockorwritecontrol",
    "CLI": "prepare staysnonactivating; opted-in resumed pull/webhook independently current-main acquire/validate/stage/switch; activate exactrelease+expected-current+token; rootmaintenance-enter/exit/status; rootrollback exactrelease+expected-current persists pause; fixedcheck-maintenance in native preSwitchChecks includingdisabledcandidate",
    "recovery": "same stable lock for pointer and rootcontrols; durablepending/current/history receipts, exactretained file/archive/schema validation; rollback keeps newerqueue/releases paused; deferred marker unwatched; resume preservesnewpending andwakesfixedworker outsidecontentlock; boot recoversresume-beforewakecrash; queue/contentlocks nevernested"
  },
  "compatibility": "Deliberate authority change from unconditional workspace-session refusal to operator-installed targetcontentpolicy. No workspace/session/machine authority is fabricated. Artifact/stagereceiptschema1 and H15 auth/filters/queue/leastprivilege preserved; rootcontrolschema1 additive. No DB/schema/content migrations, pinchanges, historyrewrite or H18/D19lineage changes. WordPress/proxy/publiccutover remain independent. Older refuse-only helpers cannotpublish; enterpause before oldsystemrollback and retainallarchives/oldgeneration/data. Existingprepare/work stageonly flags remaincompatible and grantnopointerauthority; activating paths enforcefixedroot/policy/IDs.",
  "resolved_check_findings": "Initial fixture patchedSTATE too broadly; corrected testscope. Webhookfixtureold wrapper-name/bootstartup assertions updated to actualcontract. Staticfixture caught missing implementationdigest after indentation-sensitive source edit; correctedsource and finalfreshbatchpassed. Docchecker originallytreated fencedillustrativeimageasreal link; checkedactualrelativelinks. No failedcheck hidden/no runtime bypass.",
  "limits": "Committed source and meaningful quickfixtures only. Mandatory final jointreview, registered HTTP/systemd-style integration, native affectedsystem builds and exactartifact/UI/CI are still later lead-released work. No production/liveGitHub/SSH/secret/hook/forum/credential/deployment/defaultintegration/push/service/lifecycle action; user deploys. No claim of installed runtime policy, admission or readiness from these fixtures.",
  "watcher": {
    "identity": "dw_e45f9c382e5b2ea9a5313a9410cf2005d2b36626391d8cad",
    "model": "gpt-6-luna",
    "effort": "low",
    "sandbox": "danger-full-access",
    "approval": "never",
    "exit": 0,
    "elapsed_seconds": 146.82505574601237
  },
  "resources": "No operationrunning; allpriorrefs/recoveryrefs/results/previews/session retained. B18artifactprep staysparked under originalowner."
}
```

Both final trees and indexes are clean and yielded. All nine module-tested source hashes match exact config commit blobs, including immutable implementation binding. The prior refusal was deliberately replaced by installed operator policy; no test-only injection or path override is exposed by the production CLI. Root maintenance and pointer updates share the stable lock; successful automatic work remains an explicit opt-in plus resume. Main owns final joint review and later verification release. Architect owns P18 plan reconciliation after this append; no new report bundle or system/runtime check was added.

## A18 Important review corrections R1/R2: amended source and focused checks

The earlier A18 quick/source checkpoint at9ea/3fb is superseded by these corrected unpublished successors for final review. The lead accepted the fixed privilege-separation and durability correction contract, and main accepted the narrow command/lock-order/durability prose before normal amendments. No earlier review or stage receipt is treated as proof of the corrected runtime.

```json
{
  "amended_history": {
    "config": {
      "head": "15ad7646c369770fbee584c0e248d05ab9a372bc",
      "tree": "22160d9a56c16ae270b10ef51b4e4403afe8536b",
      "parent": "937fd3717203d4daf2076d733f97a2236b36cdca",
      "old_reviewed_head": "9ea9fbd9f9a436f82249c08d9e3efc485fe8bff8",
      "recovery_ref": "refs/heads/recovery/2026-11-06-multilingual-blog-migration-a18-before-r1-r2-config",
      "old_range": "937fd3717203d4daf2076d733f97a2236b36cdca..9ea9fbd9f9a436f82249c08d9e3efc485fe8bff8",
      "new_range": "937fd3717203d4daf2076d733f97a2236b36cdca..15ad7646c369770fbee584c0e248d05ab9a372bc",
      "range_diff": "a18-r1-r2-config-range-diff.txt",
      "range_diff_sha256": "0c9be5980f7dee6ea50fd6a0192da2e546365b6512dbffa815307c0fe847b32c",
      "changed_fix_paths": [
        "docs/operations/blog-static.md",
        "tests/blog-static-release.py",
        "tests/blog-webhook.py",
        "tools/blog-static-release.py"
      ],
      "clean_and_index_yielded": true
    },
    "blog": {
      "head": "82a1ee3c90990e56cfde0da28ababed8f0444441",
      "tree": "d23e142cee504f6284ed0bbc4b028be6b8935e8c",
      "parent": "5032d82ffd43870aa7e0aa6dd332300e4ce2f3b4",
      "old_reviewed_head": "3fb7d25b1ca39dcddf3dcc8a22b2e47bcf0e49a2",
      "recovery_ref": "refs/heads/recovery/2026-11-06-multilingual-blog-migration-a18-before-r1-r2-blog",
      "old_range": "5032d82ffd43870aa7e0aa6dd332300e4ce2f3b4..3fb7d25b1ca39dcddf3dcc8a22b2e47bcf0e49a2",
      "new_range": "5032d82ffd43870aa7e0aa6dd332300e4ce2f3b4..82a1ee3c90990e56cfde0da28ababed8f0444441",
      "range_diff": "a18-r1-r2-blog-range-diff.txt",
      "range_diff_sha256": "c8a1290388af02636804058363d535cc0337d00a4486b16c1d8040cd39d92438",
      "changed_fix_paths": [
        "docs/deployment.md"
      ],
      "clean_and_index_yielded": true
    },
    "history_conclusion": "Same unpublished owning A18 commits amended in place; rootprivilege+durability semantics intentionally changed, no literal patch equivalence claimed. H18/D19 parents and publishedancestors untouched; no migrations/pin streams/artifact schema changes. Raw oldreviewheads retained for affectedreview."
  },
  "findings": {
    "A18-R1": "Root crosses no service-writable content boundary: fixed NSS blog-release child resets supplementary groups to configured account memberships (including blog-webhook-inbox), irreversibly setresgid/setresuid, clears effective/permitted/inheritable capabilities and forbids privilege regain; bounded JSON pipe only. Parent holds stable root lock and waits; child reuses inherited lock, no reacquire. Root status/content reconciliation/rollback are delegated, queue resume uses same fixed identity outside content lock, and root only starts fixed systemd worker. Content CLIs require actual NSS service UID and reject root before token/policy I/O.",
    "A18-R2": "New payload and archive files are fsynced after final modes; bottom-up tree directories then completed release-parent/root sync precede stage receipt eligibility. Reused old schema1 stages and reconciliation get a barrier; explicit/idempotent activation flushes payload/archive and retained CSS files/directories before pending receipt/pointer. Flush errors abort new eligibility/switch."
  },
  "focused_checks": {
    "pinned_release_suite": "27 total:21PASS,6namespace-onlySKIP;3.107s",
    "pinned_webhook_suite": "19PASS;2.033s",
    "actual_namespace": "6PASS;1.913s tests/2.432s wrapper; no network/server/host-root paths",
    "exact_commands_and_hashes": {
      "head": "9ea9fbd9f9a436f82249c08d9e3efc485fe8bff8",
      "results": [
        {
          "name": "release",
          "command": [
            "/nix/store/5a0h3d6488628sh6w1ccqk8dizvmp8ji-python3-3.13.15-env/bin/python3",
            "tests/blog-static-release.py"
          ],
          "exit": 0,
          "elapsed_seconds": 3.5158733390271664,
          "log": "/home/aither/workspace/ai/vpsfree.cz/work/2026-11-06-multilingual-blog-migration/a18-r1-r2-release.log"
        },
        {
          "name": "webhook",
          "command": [
            "/nix/store/5a0h3d6488628sh6w1ccqk8dizvmp8ji-python3-3.13.15-env/bin/python3",
            "tests/blog-webhook.py"
          ],
          "exit": 0,
          "elapsed_seconds": 2.4016535819973797,
          "log": "/home/aither/workspace/ai/vpsfree.cz/work/2026-11-06-multilingual-blog-migration/a18-r1-r2-webhook.log"
        },
        {
          "name": "privilege",
          "command": [
            "/run/current-system/sw/bin/unshare",
            "--user",
            "--map-auto",
            "--map-root-user",
            "--mount",
            "--propagation",
            "private",
            "--fork",
            "--",
            "/nix/store/5a0h3d6488628sh6w1ccqk8dizvmp8ji-python3-3.13.15-env/bin/python3",
            "-c",
            "import os,subprocess,sys; subprocess.run([sys.argv[1],\"-t\",\"tmpfs\",\"-o\",\"mode=755\",\"tmpfs\",sys.argv[2]],check=True); os.environ[\"TMPDIR\"]=sys.argv[2]; import tempfile; tempfile.tempdir=None; sys.exit(subprocess.run([sys.executable,\"tests/blog-static-release.py\",\"RealPrivilegeBoundary\"]).returncode)",
            "/nix/store/0bmapmnznzaxgx76jhzbznhlwq738g03-util-linux-2.42.3-bin/bin/mount",
            "/tmp/a18-r1-final-ao7mj386"
          ],
          "exit": 0,
          "elapsed_seconds": 2.4317607649136335,
          "log": "/home/aither/workspace/ai/vpsfree.cz/work/2026-11-06-multilingual-blog-migration/a18-r1-r2-privilege-final.log"
        }
      ],
      "pre_sha256": {
        "tools/blog-static-release.py": "5bbe2e4fdbb0a738cc86444d9629eea1be890c51bc6705cf997518b3c4aef1fc",
        "tests/blog-static-release.py": "9de48ff74cf2441d0a5551730a429a57bb0908b96cc5f9c07b98abeb6d462214",
        "tests/blog-webhook.py": "a655a221bac102d9ff9667d1d5196ea8ac9a1fa594ab1e75449d6802ffada875",
        "docs/operations/blog-static.md": "33a325435d2efe9c72115affe9fc17641bec50180fe085392647a8f42d8b7c64"
      },
      "post_sha256": {
        "tools/blog-static-release.py": "5bbe2e4fdbb0a738cc86444d9629eea1be890c51bc6705cf997518b3c4aef1fc",
        "tests/blog-static-release.py": "9de48ff74cf2441d0a5551730a429a57bb0908b96cc5f9c07b98abeb6d462214",
        "tests/blog-webhook.py": "a655a221bac102d9ff9667d1d5196ea8ac9a1fa594ab1e75449d6802ffada875",
        "docs/operations/blog-static.md": "33a325435d2efe9c72115affe9fc17641bec50180fe085392647a8f42d8b7c64"
      },
      "namespace_scope": "Actual subordinate UID/GID+private mount tmpfs, no network/server or host-fixed content paths; synthetic NSS identity selects mapped UID1/GID1+dedicated group2 only. UID/group/capability drop and root-owned outside-sentinel protections execute in kernel; no mocked successful drop.",
      "still_running": false,
      "resolved_namespace_environment_failure": {
        "record": "a18-r1-r2-checks-first.json",
        "log": "a18-r1-r2-privilege.log",
        "cause": "Nixshell TMPDIR parent0700 prevented realdroppedUID1 traversing fixture; use independent scratch mount directlyunder/tmp. No permission/control/source changes or repeatedpassingpurechecks."
      }
    },
    "normal_hooks": "Config Nixfmt/precommit+commitmsg passed, nonblocking72colwarnings only/all<=80; blog normal Nix commit exit0; no hooks bypassed.",
    "docs": "Main exact narrow copy accepted with queue/content-lock clarification applied; affected local links/whitespace pass."
  },
  "privilege_scope": "Actual kernel subordinate-UID/GID+private tmpfs tests, synthetic fixed NSS account selection only. No mocked successful UID/capability drop: observed UID/GID triples1, configured groups1+2, zero effective capabilities, root regain denied; root-owned outside sentinel bytes/modes unchanged through ancestor/final CSS symlinks, concurrent replacement, receipt/reconciliation/status and inbox attacks. Positive queue resume, inherited-lock rollback/maintenance and root CLI rejection passed. This is not host NSS/systemd/LoadCredential or positive production HTTP/CLI rehearsal proof.",
  "resolved_test_setup": "Initial namespace command used absent systemPythonpath, corrected to cached pinnedPython. Queue fixture initially touched0660 underumask resulting0640; corrected fixture to actual production tmpfiles0660. Existing synthetic gzip timestamp became nondeterministic across slower fsync test; fixture mtime0 now stable. First pinned namespace scratch under Nix TMPDIR0700 blocked dropped UID traversal; corrected only runner to explicit /tmp private mount, no permission broadening. Original failed logs/record retained and successful pure suites were not repeated for runner-only correction.",
  "module_evidence": "No Nix module/fixture source or permission wiring changed in R1/R2. Earlier module results retained for unchanged settings only; compiled corrected source/new native system builds remain unverified until later release.",
  "compatibility": "Same unpublished owning commits amended; exact reviewed9ea/3fb recovery refs retained. H18/D19 parents, published ancestors, pins, corpus and artifact/stage schema1 unchanged; no migrations, generic framework or CLI UID/policy/exec override. Service-account-only CLI/root rejection is the accepted compatibility adjustment; operators use fixed credential-backed pull service, root maintenance/rollback. All existing releases/archives/queue work remain retained.",
  "gates": "Source/quick evidence handed to lead for affected independent review. Verification preparation stays PARKED. Owner2 owns separate unexecuted integration-driver preparation; owner0 retains fixes and eventual rootedBLOGartifact/publication. No long builds/HTTP/systemd integration/live GitHub/SSH/secrets/forum/hook/production/default/push/lifecycle actions. User performs deployments.",
  "still_running": false,
  "evidence_sha256": {
    "a18-r1-r2-checks.json": "bde5f32cdadc6eeae6dfe1781936a1933ee3608339a1805286e74defea49e9c4",
    "a18-r1-r2-history.json": "00e4bf94c0df916bef38f40777acbf776a5e28d7b22c9f02ef37738ff49eda37",
    "a18-r1-r2-release.log": "652dd6cc806a5ae536b0369e4aa238c1d88d589515f2b6b8639f2f1019287151",
    "a18-r1-r2-webhook.log": "286e684055b80a8946a66710ab15b95334c011a0402f7f10b9a9307a03004b18",
    "a18-r1-r2-privilege-final.log": "867d307ff43dfea0c698d49ae3f5c2fe5a399cc69b54b758fb4d678f27967db2"
  }
}
```

Both final source trees and indexes are clean/yielded. Checked configuration source hashes equal the amended commit blobs. The raw old/new range evidence intentionally reports substantive fixes rather than literal patch equivalence. Remaining affected review, native builds and isolated integration are lead-owned gates; no such operation has been launched. The append-only window is returned to architect0 for P18 reconciliation.


### H18 final native configuration build at 15ad7646

After final review acceptance, one fresh pinned Luna/low full-access/never utility ran the native two-node batch once in 98.877 seconds (exit 0):

```sh
nix develop --no-write-lock-file --no-update-lock-file --command confctl --color never build --yes '{cz.vpsfree/containers/int.blog,cz.vpsfree/containers/prg/proxy}'
```

Canonical cwd was the session configuration worktree. Exact source, index and flake hashes were unchanged before/after; all prior result links, generations and native GC roots were retained, with only native current-generation links advancing. No kernel build, cancellation, activation, machine claim or cleanup occurred. Raw evidence: `h18-final-config-build{.log,-status.json,-watcher-launch.json,-watcher-native.jsonl,-watcher-final.md}`; immutable interpretation: `h18-final-config-build-proof.json`, root metadata `h18-final-config-source-inputs.json`, output NARs `h18-final-config-output-paths.json`. The utility slot/raw paths were yielded directly to owner0 before interpretation.

```json
{
  "source": {
    "head": "15ad7646c369770fbee584c0e248d05ab9a372bc",
    "tree": "22160d9a56c16ae270b10ef51b4e4403afe8536b",
    "root": "/nix/store/nky94sk29fkb6r9kzmb1szqg4z7mghvl-source",
    "narHash": "sha256-sovRVl6kqDICuSEdcMSzP2z2AZ/UOBdv3L/H2mk6dPY=",
    "lock_nodes": 64,
    "flake_nix_sha256": "01d6cb4187fee8ca60588905b7e4902339e1948a557b10f2e6ec1a7bd9fa827b",
    "flake_lock_sha256": "9ed71bd9511c7b4e16e0fd9f4de483e0fe4cf54d2556e715392d28e6e60eacd8"
  },
  "systems": {
    "cz.vpsfree/containers/int.blog": {
      "generation": "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/vpsfree-cz-configuration/.confctl/generations/cz.vpsfree:containers:int.blog/2026-11-07--20-39-35",
      "outputs": {
        "toplevel": {
          "path": "/nix/store/44pj55dlwlqc32ya9yns6v393zrwa7a7-nixos-system-blog-26.05.20261026.718f670",
          "derivation": "/nix/store/a7nlxy77yz1z6ljg92b3a25p5jlm3gnw-nixos-system-blog-26.05.20261026.718f670.drv",
          "narHash": "sha256-wZPvwCsoJridMWEW79bFvIt1KN9fBSy1TQeabk1a9TU="
        },
        "auto_rollback": {
          "path": "/nix/store/yl9vnin9wlv04cip0sqpkisk80xmccwh-auto-rollback.rb",
          "derivation": "/nix/store/za41c9rsf8k0qv0ay8svf4kc4y2x0q51-auto-rollback.rb.drv",
          "narHash": "sha256-jxWEsEUoscnyhIg2YmZF781gpn8CbuvYXNa85iSafSQ="
        }
      },
      "native_inputs_info": {
        "nixpkgs": {
          "input": "nixpkgsStable",
          "lastModified": 1793015021,
          "rev": "718f670e845328e9c2cecdd832835712b2cbd065",
          "shortRev": "718f670e",
          "url": "https://github.com/NixOS/nixpkgs"
        },
        "vpsadminos": {
          "input": "vpsadminosOsStaging",
          "lastModified": 1793720150,
          "rev": "dd188397abe37d0bc33f4c5dfb3605206ce5e326",
          "shortRev": "dd188397",
          "url": "https://github.com/vpsfreecz/vpsadminos"
        }
      },
      "effective_locked_nar_nodes": 8
    },
    "cz.vpsfree/containers/prg/proxy": {
      "generation": "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/vpsfree-cz-configuration/.confctl/generations/cz.vpsfree:containers:prg:proxy/2026-11-07--20-39-35",
      "outputs": {
        "toplevel": {
          "path": "/nix/store/y8k4chkrs4s50pky7ymc98mfmzqpn2yf-nixos-system-proxy-26.05.20261026.718f670",
          "derivation": "/nix/store/bpx4b8m603x6zw8v7ncjzsgf9cm82vzg-nixos-system-proxy-26.05.20261026.718f670.drv",
          "narHash": "sha256-18ta0NzMi1xsVyu4HfB2dqDQ9CoTtYCiMwFhj5C+/4Y="
        },
        "auto_rollback": {
          "path": "/nix/store/yl9vnin9wlv04cip0sqpkisk80xmccwh-auto-rollback.rb",
          "derivation": "/nix/store/za41c9rsf8k0qv0ay8svf4kc4y2x0q51-auto-rollback.rb.drv",
          "narHash": "sha256-jxWEsEUoscnyhIg2YmZF781gpn8CbuvYXNa85iSafSQ="
        }
      },
      "native_inputs_info": {
        "nixpkgs": {
          "input": "nixpkgsStable",
          "lastModified": 1793015021,
          "rev": "718f670e845328e9c2cecdd832835712b2cbd065",
          "shortRev": "718f670e",
          "url": "https://github.com/NixOS/nixpkgs"
        },
        "vpsadmin": {
          "input": "vpsadminServices",
          "lastModified": 1793802784,
          "rev": "b83b26e1ba1c8e869ae3ffbcb5801ed071c3844e",
          "shortRev": "b83b26e1",
          "url": "https://github.com/vpsfreecz/vpsadmin"
        },
        "vpsadminos": {
          "input": "vpsadminosOsStaging",
          "lastModified": 1793720150,
          "rev": "dd188397abe37d0bc33f4c5dfb3605206ce5e326",
          "shortRev": "dd188397",
          "url": "https://github.com/vpsfreecz/vpsadminos"
        }
      },
      "effective_locked_nar_nodes": 16
    }
  },
  "proof_sha256": "de57cd3374806f364fb95e56e44a0ac3a39f7172f5174c3a8e61984ac373d1fd"
}
```

The compiled defaults retain WordPress80/PHP/MariaDB/initialization/cron, original persistent paths and ownership (WordPress numeric UID remains null; nginx60/mysql84, mysql.isSystemUser=false), original source health definitions and proxy-only port80 firewall. English/static/webhook/publication remain off with no optional accounts, services, credentials or 8080/8091 listeners. The disabled policy, installed corrected Python bytes and native read-only pre-switch guard are bound in the proof; that guard was inspected, never executed. The reader initially looked for the guard inline and was corrected to follow PRE_SWITCH_CHECK; no product failure or rebuild resulted.

This proves immutable compiled defaults, not enabled deployment or live state. Existing enabled-mode fixtures remain separate evidence. Both rollback artifacts and all previous systems are built/retained but never activated here. No schema/content migrations, pin changes or source mutation. The conditional registered loopback nginx probe is next after owner0's successful exact82a artifact and direct utility yield; its result is pending in this entry.


## B18 final rooted blog artifact: exact82a1ee3c

The single fresh pinned Luna/low operation built BLOG
`82a1ee3c90990e56cfde0da28ababed8f0444441` / tree
`d23e142cee504f6284ed0bbc4b028be6b8935e8c` with the absolute original flake and explicit
blog cwd, `nix build --out-link result-b18 --print-out-paths
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog#site`.
Exit0 in17.789s; exact clean pre/post and post-interpretation, all six old roots
unchanged. Native output `result-b18` is
`/nix/store/zd9ip2lyjpc52pwhn4rpihd3kz2rrfhx-vpsfree-blog-0`; derivation
`/nix/store/a2zg8ibvm7mnx9gad09yy1n07hn3bwl0-vpsfree-blog-0.drv`; output NAR
`sha256-6hBjUXMaTfdR4NkU18eU1MctuK0E0FBfT3/Ggo0PXv0=`. Raw successful path and free utility
slot were delivered directly to lead/owner3/owner2 before interpretation; no
build/watcher remains. Owner3 real-nginx precedes owner2 fixed-CLI integration.

[Artifact proof](b18-artifact-proof.json), [build status](b18-build-status.json),
[full build log](b18-build.log) and
[watcher result](b18-build-watcher-final.md) bind all2397 served SHA256 values
and the exact file set,1009 tracked source files, the complete two-node locked
and effective input graphs, source NAR and all three native input paths/NARs.
Source `/nix/store/d5idsicy4a09y31nqalncavlxmc185kk-source` has NAR
`sha256-wzdO7vrZa+RMx7ElfkS5rpNCLvRF+C4a7/rL1pbotko=`. Locked Nixpkgs remains
`f3a73bcf5d1c5b75a66cf35a48957e30d41d647a` /
`sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=`; Hugo0.167.0, Pagefind1.5.2 and Python
native identities equal accepted T16. Metadata SHA256 is
`14aaaf2f9079b4126cb5ac7750454b91daafa177e6754ffdb1ab6bcf71038401`.

Both production roots contain125 articles, Pagefind125 indexed pages and10
full-content feed items with exact original dates, links and per-language GUIDs.
All250 paired immutable-ID/language source body bytes,125 complete Czech files,
dates/paths/source hashes, public data, manifest, pins and1138 legacy media copies
retain T16 continuity. English frontmatter changes are only the accepted
publication/review metadata.125 Czech rendered bodies and the Czech feed are
unchanged;107 historical comment anchors and125 more anchors are present.
All431 Czech HTML routes remain identical. The source manifest also inventories
WordPress daily and pagination paths: rendered coverage remains0/124 daily and
35/41 pagination in both T16 and B18; inventory is not a generated-route claim.

All141 Czech Pagefind files and the search adapter/SRI remain byte-identical;
English now has144 Pagefind files and125 indexed articles. Both roots serve the
local background JPEG
`f8e3a64a8be47585ee528889ff3ee185a6c69a2b54e95ebcd294406b08b3ff97`
through CSS
`ea8191e29a7fd5e2926a5629003b31b778d8c61513f631d2ec7c5ce53a260831`.

Each language has302 base-layout pages with exactly one expected Piwik loader
and exact noscript pixel (CS4/EN10), plus129 alias redirects without tracking.
RSS has no tracking; three synthetic fixture routes remain excluded. Source
guards still require production, not HugoServer, and a positive ID; fixtures
configure0 and Discourse defaults off. No JavaScript/pixel/tracker request was
executed. Accepted7fa visual/runtime evidence is reused because subsequent
changes are documentation only; no render/UI/search suite was repeated.

This receipt proves the immutable blog artifact, not configuration runtime,
live webhook/systemd, deployment, credentials, public cutover or publication.
Feature publication remains held for lead acceptance and a separate release.
All roots, previews, recovery refs and the session remain open.


## A18 final feed mapping correction: exact1e840b80

The enabled-candidate nginx rehearsal at CONFIG
`15ad7646c369770fbee584c0e248d05ab9a372bc` / tree
`22160d9a56c16ae270b10ef51b4e4403afe8536b` exposed a real direct `/feed/`500: the index
phase appended `index.html` to the file alias. Retain
[h18-nginx-runtime/result.json](h18-nginx-runtime/result.json), its error log
and exact generated manifest;540 legacy aliases and preceding negative probes
had passed. The earlier15ad source review and native two-node build remain
evidence for that predecessor, not proof that the enabled feed worked.

Corrected CONFIG `1e840b8056bbc700ca3e9cd832f0d9301da52652` / tree
`6f6d2020345f731370698be3ed2ff7fe25ac637e` amends the same unpublished A18 commit on unchanged
H18 parent `937fd3717203d4daf2076d733f97a2236b36cdca`. Exact15ad remains at
`refs/heads/recovery/2026-11-06-multilingual-blog-migration-a18-before-feed`;
[history/source identity](a18-feed-fix-history.json) and
[old/new range-diff](a18-feed-range-diff.txt) retain provenance. The only delta
to15ad is `int.blog/static-blog.nix` and its existing static-module fixture
(32 insertions,3 deletions): exact `/feed/` now uses
`try_files /feed/index.xml =404` under each fixed language root, with unchanged
RSS type. No public redirect, map/proxy/PHP/unknown-host, policy/helper/privilege,
pin, schema or documentation-contract change.

The affected fixture passed once after correcting its invocation to supply the
required flake attrset for the same pinned Nixpkgs source (initial bare-path
argument failed before evaluation; evidence retained). Final exit0 in37.425s
checks both language roots, no file alias, both internal mappings/RSS type and
exactly two actual generated directives. See
[focused result](a18-feed-checks.json) and
[fixture log](a18-feed-static-module-final.log). Source hashes remained stable.
Normal amendment hooks passed; commit-message72-column warnings were nonblocking,
all lines satisfy80. Worktree/index were clean/empty at yield; no broad Python
or webhook fixture was repeated.

Lead accepted this exact source/quick/narrow-inspection result under the direct
finding-fix rule; no full reviewer rerun was required. Owner3 owns released
final native identity refresh followed by both feeds/remaining nginx modes,
retaining unchanged540-map evidence. Owner2 fixed-CLI integration follows his
direct yield. Their results remain pending in this receipt. BLOG82a/result-b18
and accepted artifact/UI/privacy evidence are unchanged. No runtime, build,
service reload, publication, deployment or cleanup was performed by owner0 for
this correction. Publication/integration gates remain held by lead.


### H18 final feed repair, native refresh and nginx closure

The first real pinned-nginx probe at15ad passed all540 exact aliases (including107 comment fragments),13 malformed literal-query cases,4 ordinary/encoded-query cases and the RSS query alias. Direct `/feed/` then returned500: nginx appended `index.html` to the file alias (`index.xmlindex.html`). The first result, error excerpt, config and hashes remain under `h18-nginx-runtime/{result.json,first-failure-evidence.json,first-failure-error.log,nginx-first-failure.conf}`. Owner0 fixed only both-language feed locations to inherited-root `try_files /feed/index.xml =404`, retaining RSS types; normal-hook same-parent amend1e840 replaces15ad, retained at `recovery/2026-11-06-multilingual-blog-migration-a18-before-feed`. Main accepted the narrow fix/quick37.425s; no full-review or BLOG rebuild was repeated.

One fresh pinned Luna/low full-access/never utility refreshed the exact same canonical two-node native command recorded above, once, exit0 in98.235s. Fresh root Git/NAR/full64-node lock graph, native per-node inputs_info/source NARs/reachable8-and16-node graphs and both system/autoRollback derivations/NARs are independently bound below and in `h18-refresh-config-{build-proof.json,source-inputs.json,output-paths.json}`; raw log/status/watcher evidence uses `h18-refresh-config-build*`. Exact clean source/flake hashes were unchanged before/after, all prior roots/generations including15ad remained, and only native current-generation links advanced.

```json
{
  "config_head": "1e840b8056bbc700ca3e9cd832f0d9301da52652",
  "tree": "6f6d2020345f731370698be3ed2ff7fe25ac637e",
  "source_path": "/nix/store/cvqfqdzbs9xywb14zc33ihhqpjcn5fjg-source",
  "source_nar": "sha256-x1i8Gv7VaomIhZSEIBrg4UWI3VqWpJLkPJjmoaD6G0g=",
  "root_lock_nodes": 64,
  "effective_role_graph_nodes": {
    "cz.vpsfree/containers/int.blog": 8,
    "cz.vpsfree/containers/prg/proxy": 16
  },
  "outputs": {
    "cz.vpsfree/containers/int.blog": {
      "toplevel": {
        "path": "/nix/store/04fyz2bcfb2xx5hv0rzna6kmkhha699k-nixos-system-blog-26.05.20261026.718f670",
        "derivation": "/nix/store/wnd1hy1s1925hk3d55zspz49a5wgq0ym-nixos-system-blog-26.05.20261026.718f670.drv",
        "narHash": "sha256-jdrdHA+QmyUoy7i/aK93CbmnjMTxsyAqDx8fQRwb8PU="
      },
      "auto_rollback": {
        "path": "/nix/store/yl9vnin9wlv04cip0sqpkisk80xmccwh-auto-rollback.rb",
        "derivation": "/nix/store/za41c9rsf8k0qv0ay8svf4kc4y2x0q51-auto-rollback.rb.drv",
        "narHash": "sha256-jxWEsEUoscnyhIg2YmZF781gpn8CbuvYXNa85iSafSQ="
      }
    },
    "cz.vpsfree/containers/prg/proxy": {
      "toplevel": {
        "path": "/nix/store/a2b5d14vj9rkzlm8sv2j5v0kcf9vplc8-nixos-system-proxy-26.05.20261026.718f670",
        "derivation": "/nix/store/35pgpn4a659lx9zvg77i073v83kcihw1-nixos-system-proxy-26.05.20261026.718f670.drv",
        "narHash": "sha256-hpgGSrzdk0jMcBOxpfrsj77yA5bGVNdQxGQCxhPHfoo="
      },
      "auto_rollback": {
        "path": "/nix/store/yl9vnin9wlv04cip0sqpkisk80xmccwh-auto-rollback.rb",
        "derivation": "/nix/store/za41c9rsf8k0qv0ay8svf4kc4y2x0q51-auto-rollback.rb.drv",
        "narHash": "sha256-jxWEsEUoscnyhIg2YmZF781gpn8CbuvYXNa85iSafSQ="
      }
    }
  },
  "build_proof_sha256": "9fb8163ea07d07238f7d4a0374ae11cfea7742f3923c6fd061e99842c2880498",
  "resume_result_sha256": "43b105e608d9a88067acff6c0413e18e4482fe66f0a5d67f97ce80ad0c7204a3",
  "runtime_proof_sha256": "e12e0eab6da6876498fd593bf9df41681dcb44c50233929bdad1c95b22aebb05"
}
```

Compiled defaults preserve hardened WordPress80/PHP/MariaDB/initialization/cron/health/source data paths and account identities (WordPress UID null, nginx60/mysql84 with mysql.isSystemUser=false), proxy-only80 firewall and default-off English/static/webhook/publication. The fresh proof follows the native pre-switch guard and binds actual installed helper/corrected Python bytes and disabled policy; the separately generated enabled text contains exactly two fixed feed directives. No compiled definition was activated. Input pins and publication implementation remain unchanged.

The parent verified service4400a630-af21-4ea5-a424-a8f1a0e7e8cb ownership/cmdline, syntax-checked then natively reloaded only its two feed locations (same master1940932; new worker2049302). First adapted config SHA2561b0f4b390b929f48b766d0693f386526201fec79eccbdbbd18f7bc8ba4e5d131; fixed SHA256336696ab577eacc66584445b234cd04aca8df143bb233fecd4f0c9e9ef43fdb1. Actual generated maps and all text outside those locations are byte-identical (`manifest-fixed.json`), so all558 earlier passed observations are reused for precisely that scope. A fresh probe-only Luna ran only the14 remaining/feed cases, exit0/0.274967s: CS/EN feeds200+RSS, prelaunch CZWP200/EN503, both static Hosts200, exact hook to synthetic80 in both modes, English/trailing hook404, English no Czech aliases, fixed canonical redirect under hostile Host, unknown backend closes without response and PHP404. No redirects were followed; all14 connects were numeric loopback only. Separate `resume-*` and `final-proof.json` retain the new results without overwriting first failure. Raw success/slot was yielded directly to owner2 before interpretation.

This is one registered built-nginx process using generated modules, scratch roots/feed bodies/ports and TLS/ACME-off synthetic WP/hook backends. It proves these adapted HTTP responses, not production TLS/firewall/two-node routing, live WP, service UIDs/systemd credentials, webhook delivery or publication authority. Registered4400 and all earlier services/results/GC roots/recovery refs remain open; final native-root parity also passed after probing. No activation, SSH, credentials, DNS/GitHub/forum requests, push/default integration, migration, pin change or cleanup occurred.

## A18I source realization and initial fixture boundary (2026-11-07)

At configuration `1e840b8056bbc700ca3e9cd832f0d9301da52652`, tree
`6f6d2020345f731370698be3ed2ff7fe25ac637e`, the synthetic-enabled actual-module
`sourcePackage` realized successfully in 32.78 seconds. An earlier watcher stopped
before building because it checked the workspace root rather than the explicit
session/config directories; that prelaunch stop is not a failed source build.
The enabled fixture output is
`/nix/store/n0869rky0g7pm7azw94gjlypa4ssb9bg-blog-publication-source`, NAR
`sha256-Va+ewaBQortvfqv/osefwI4Ks0PLgS83ORRqgWzyzDw=`. Its compiled policy is
`/nix/store/hvvx0gq8792m472mzx2i8hfbfsq5w5a2-blog-release-policy.json`, NAR
`sha256-Qz0NLv+grtlwoDKwiNOdT4sEcyL0kS4En1dg+8mHp58=`, file SHA256
`890106b15af7dd73e0bdc7db65cdee862ceaa7feecabe945361fe9c168a15fc9`.
It explicitly enables the fixture's repository/workflow IDs 42/99; it is not the
disabled production default. Packaged Python bytes equal final source with only
the compiled policy-path substitution. The unchanged implementation digest is
`4aac9abd45818f96323ab2cbe0f32c85f47fe4162821c1a79ec03c65c454780e`; this does not
claim new code coverage from a cached path. Evidence is under
`a18-fixed-cli-rehearsal/realization{.log,-status.json,-proof.json}` and
`source-identity.json`.

Initial registered fixture `61accaea-0bd3-4476-9f58-6e80e223ad94` and the single
stderr diagnostic `3a6608ac-1db7-437e-ac63-a77f8af2e12d` both exited before any
HTTP/control/pointer probe. The diagnostic captured nonroot Python loader exit
127: `libpython3.13.so.1.0: cannot open shared object file: Permission denied`.
These attempts establish no HTTP, publication or rollback success. Both failed
registrations remain retained, with no running process; initial startup and
diagnostic outputs remain separate and unchanged.

One separately authorized no-server/no-application exec/read smoke (0.402 s)
found private `/nix` owned by namespace root with mode 0700, while the host path
is 0755. Root could read the library and exec Python. The irreversibly dropped
child could not exec it. Intermediate dropped stat/status rows were lost when
the smoke's exec error propagated, so those rows are not claimed as evidence.
Lead and architect accepted this as private fixture ancestor DAC caused by the
inherited service umask, not an application defect. See `exec-smoke.log`,
`exec-smoke-status.json`, `exec-smoke-output/exec-smoke-result.json`,
`initial-startup{.log,-result.json,-status.json}` and
`diagnostic-output/result.json` in the same rehearsal directory.

Lead accepted a fixture-only setup umask 022 repair, explicit private ancestor/
NSS modes, restrictive control/inbox/credential modes and actor umask 0007.
One corrected registered attempt is separately released; its result will be
recorded below. At this checkpoint fixed-CLI integration remains **incomplete**.
No host permissions, accounts, application source, compiled policy bytes or
existing services were changed. No live GitHub/forum/tracker request, deployment,
publication, default integration or cleanup occurred. Real host systemd.path,
LoadCredential and NixOS-switch behavior remain user-run limits.

## A18I final fixed-CLI rehearsal accepted

Lead inspected and accepted the final **28-observation pass, 6.521575 seconds**
at configuration `1e840b8056bbc700ca3e9cd832f0d9301da52652` / tree
`6f6d2020345f731370698be3ed2ff7fe25ac637e`. The source and index remained clean.
The actual synthetic-enabled module output, compiled policy and code/NAR binding
are the unchanged `n0869rky0g7pm7azw94gjlypa4ssb9bg-blog-publication-source` and
`hvvx0gq8792m472mzx2i8hfbfsq5w5a2-blog-release-policy.json` documented above.

Final registered fixture `8df97376-df93-4247-a811-69811e3fd122` runs one isolated
user/mount/network process tree with real private NSS, irreversible identity
operations, root controls, nonroot receiver/worker, fixed paths and compiled
policy checks. The actual GitHub class performs HTTPS acquisition/redirects
against synthetic private DNS/CA/API/artifact servers at the fixed expected
origins. It does not inject an API object or replace preparation/switch logic.
The fixed systemctl wake is a recorded synthetic trigger, not host systemd.

The pass includes bad-signature 401 and six durable 202 acknowledgments in
3.87–4.18 ms, including a concurrent arrival while artifact fetch was held.
Maintenance during fetch allowed staging but prevented switching; deferred work
left no watched trigger loop. A newer pending hint survived resume. Independently
current A and B activated, and a duplicate retained exact current-receipt bytes.
Root rollback with the exact expected receipt restored A, stayed paused, and
preserved newer pending work and both archives. A selected-system change refused
the old worker; the new worker remained idle with deferred work, paused status
and unchanged A pointer. Explicit root resume then permitted B publication.
The old compiled helper rejected a changed active policy. Final control is
`{"paused": true, "schema": 1}`; A and B archives remain retained.

Evidence: [final result](a18-fixed-cli-rehearsal/final-output/result.json),
[final status and digests](a18-fixed-cli-rehearsal/final-status.json),
[compiled output proof](a18-fixed-cli-rehearsal/realization-proof.json) and the
small `namespace.py` / `probe.py` drivers in that directory. Final result SHA256
is `f628e6b56a68e509b4d9eac7c78730c6433f5c9a9d72741d9b033c4f861782ee`.

The initial startup failures and one exec/read smoke remain unchanged. Umask 022
fixed private setup directories, but bubblewrap still created implicit `/nix`
as 0700; explicit `--perms 0755 --dir /nix` before the read-only store mount
resolved that fixture DAC boundary. Restrictive control/inbox/credential modes
and actor umask 0007 remained enforced. The subsequent partial runs
`explicit-ancestor-output/result.json` and `completed-flow-output/result.json`
stopped on driver expectations: actual outcomes are `activated` / `unchanged`,
and a new worker with only unwatched deferred work returns `idle`. Corrections
matched the source and added paused/deferred/pointer assertions; they did not
weaken application checks. Those prior results are not counted as full passes.

Fresh pinned Luna/low ran the successful source-only realization. Native watcher
delegation was unavailable during the final registered fixture observation;
the disclosed monitoring-skill parent fallback read bounded result/unit status,
with no parallel observer. No verification operation remains. The accepted
fixture is intentionally active/running (PID 2262351), paused and retained, as
are all earlier registrations and other previews/roots. No cleanup was performed.

This proves the isolated fixed-CLI workflow, not real host systemd.path,
LoadCredential, NixOS switching, deployed Unix accounts, production networking,
live GitHub delivery, WordPress coexistence or forum behavior. Those remain
user-run rollout checks. No application source, pins, repository index/refs,
production host paths, accounts or permissions changed; no deployment/default
integration or feature publication was performed by this verification package.
Lead owns final publication and rollout acceptance; implementer2 retains findings.


### Final CONFIG feature publication at 1e840b80

After final source, native build and bounded runtime acceptance, one ordinary SSH fast-forward push published CONFIG feature `2026-11-06-multilingual-blog-migration` from `2aa36562503c8e32f02a308bc70bc9260f5ee120` to exact `1e840b8056bbc700ca3e9cd832f0d9301da52652` (exit0,14.368s). Canonical origin was `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`; the command used the repository Nix environment and ordinary hooks, with no bypass/force/rebase:

```sh
nix develop --no-write-lock-file --no-update-lock-file --command git push origin 1e840b8056bbc700ca3e9cd832f0d9301da52652:refs/heads/2026-11-06-multilingual-blog-migration
```

Fresh explicit fetch and independent `ls-remote --symref` first matched the expected old feature and master/HEAD; both were proven ancestors of the final head. Immediate fresh remote verification confirmed the feature at exact1e840 above, while remote `master` and `HEAD` remained `5941cdb3dda259e91c6a988a7dbf08c84700b326`, with HEAD still pointing to master. Local pre/post source and index remained clean at tree `6f6d2020345f731370698be3ed2ff7fe25ac637e`. The portal comparison was explicitly captured from5941 to1e840. Raw fetch/preflight/comparison/push/remote/result evidence uses existing session prefix `h18-config-publication-*`.

Workflow source is unchanged since accepted2aa and declares only the daily schedule and manual dispatch: no applicable feature-push CI, no dispatch and no CI wait. Main accepted the fresh publication proof. This publishes the feature only; it does not integrate or deploy it. No source/build/HTTP/service/secret/migration/pin/default-branch or lifecycle action occurred. All refs, recovery refs, prior systems, generations, GC roots and registered services remain retained and open.


## Final BLOG feature publication and exact CI: accepted82a1ee3c

Lead accepted the complete BLOG delivery at
`82a1ee3c90990e56cfde0da28ababed8f0444441` / tree
`d23e142cee504f6284ed0bbc4b028be6b8935e8c` after source review, rooted2397-file artifact
validation, accepted visual/privacy evidence and the separate local runtime
packages. See [publication proof](b18-publication-proof.json) and
[artifact proof](b18-artifact-proof.json) for exact source/input/native/NAR,
paired250-source,125-per-language article/index/feed and media identities.

Fresh canonical SSH preflight/fetch matched feature
`6dae2b146b4ad73df8f4bcf2b8d7fdacd830d344` and main/HEAD
`0354dac281978867ea8c1553b092ce19bccb5ccd`. Both were ancestors of the exact clean final head.
One ordinary exact-SHA fast-forward push to
`git@github.com:vpsfreecz/blog.git`,
`refs/heads/2026-11-06-multilingual-blog-migration`, exited0 in2.678s. Immediate canonical
remote verification returned feature `82a1ee3c90990e56cfde0da28ababed8f0444441` with main and
HEAD unchanged at `0354dac281978867ea8c1553b092ce19bccb5ccd`. No force, rebase, default-branch
or configuration mutation occurred. Native comparison capture explicitly binds
`0354dac281978867ea8c1553b092ce19bccb5ccd..82a1ee3c90990e56cfde0da28ababed8f0444441`. At push completion the local exact
head/tree/index were clean and all result roots and recovery refs were unchanged.
Full Git evidence is [b18-publication-git.log](b18-publication-git.log).

[Build blog run42411255497](https://github.com/vpsfreecz/blog/actions/runs/42411255497), push event/attempt1,
completed successfully at authoritative exact40-character head
`82a1ee3c90990e56cfde0da28ababed8f0444441`. One fresh pinned Luna/low/full-access/never watcher
observed only this run; `--interval` and `15` were separate arguments. The run
was already terminal by watch start (exit0,0.811s); terminal run, jobs/steps and
artifact index were each fetched once, without parent CI polling, rerun or
dispatch. The single job passed `bin/check`, `bin/check-release` and
`nix build .#site`. Protected-main packaging and upload were correctly skipped;
artifact count0. Retain [run](b18-feature-ci-run.json),
[jobs/steps](b18-feature-ci-jobs.json),
[artifact index](b18-feature-ci-artifacts.json) and
[watcher receipt](b18-ci-watcher-final.md).

Feature CI proves checks/build only; it does not supply a protected-main eligible
release artifact, actual signed delivery or deployment evidence. User-run default
integration/rollout and live credentials/services remain separate operations.
Lead accepted final publication/CI delivery; no local source/check work or
utility remains. Owner0 retains findings with capacity free. All refs, recovery
refs, result roots, registered fixtures/previews and the session stay open; no
production, admin, settings, deployment or lifecycle action was performed.
