# 2026-07-10-kb-czech-fixes

## Goal

Bring the Czech knowledge base in line with the localized vpsAdmin interface,
replace all 59 unique vpsAdmin screenshots used by the affected pages, and make
both capture and review workflows repeatable. Publish the reviewed Czech
release, then create complete English screenshot parity and stage the English
reference migration for review. Review happens on full staging KB instances at
the real page and media IDs.

## Affected components

- Coordination workspace: KB lifecycle/release tooling, candidate sources,
  checksummed release bundle, instructions, plan, and state.
- `vpsadmin-kb-captures`: standalone deterministic screenshot inventory and
  capture implementation.
- `vpsfree-cz-configuration`: internal DNS records, reverse proxy, and an
  on-demand declarative `kb-staging` NixOS container on aitherdev.
- `vpsadmin` at `af3b885a82955dbeb06a102948c35a82bf74acc4`:
  read-only authority for Czech UI terminology and captured behavior.
- Production and staging Czech/English DokuWiki instances. No production
  writes are part of implementation or infrastructure validation.

## Design

### Screenshot inventory

The capture repository is independent of the coordination workspace at
runtime. It pins its own vpsAdmin development cluster, owns deterministic
fixtures, and maps every PNG to a scenario/checkpoint. Repository paths put the
language first:

```text
screenshots/<language>/<topic>/<view>.png
```

DokuWiki IDs follow the same language-first convention:

```text
<language>:screenshots:vpsadmin:<topic>:<view>.png
```

Names are semantic and contain neither display order nor version counters.
Git versions capture files and DokuWiki versions published media. A future UI
can use a new capture driver and scenario set while preserving stable asset
IDs where the documented concept is unchanged.

The `screenshots` topology mirrors the public production shape without copying
production identifiers: Production/Praha runs on `node1`,
Playground/Playground on `node2`, and Praha storage/Praha Storage on
`backuper1`. Brno and Staging remain display-only. Public environment,
location, cluster-resource, and package labels and values are fixture data;
domains and IDs are stable local values. The documentation account receives
the four standard packages. Its fixtures include VPSes `vps` and
`playground-vps`, a `data` subdataset mounted at `/srv/data`, and a `nas`
dataset on the primary pool.

Both documentation VPSes and the captured VPS-creation wizard select the exact
`Debian (latest)` template. Console readiness and normalization require a real
Debian console banner, so an accidental fallback to the first or an Alpine
template fails capture instead of silently producing the wrong documentation.

All Czech assets are recaptured. Content-aware cropping measures visible text,
complete table borders, controls, media, and terminals instead of full-width
layout containers. It retains full heading line heights and adds symmetric
eight-pixel margins. The pinned capture shell provides Liberation Mono for the
CLI monitor and WebUI console. The WebUI console includes its complete heading
and on-screen keyboard, and the rescue screenshot uses the semantic name
`vps-console-boot.png` and includes the rescue controls in the WebUI sidebar.
TOTP documentation replaces the real QR and secret with a deterministic,
non-scannable placeholder before capture.

The two historical password-form images `informace:details2.png` and
`navody:vps:root_passwd.png` map to the single canonical
`vps-management/set-root-password.png` asset. Capture schema 4 records the
former as a legacy alias and both source pages use the same generated PNG. The
incorrect `vps-action-menu.png` capture has no remaining KB use and is removed.

The final fixture follow-up uses the production location domains `prg`, `brq`,
`pgnd`, `prg`, and `stg`. Its exposed screenshot nodes are `node1.prg`,
`node1.pgnd`, and `backuper1.prg`; the Playground machine keeps the internal
orchestration key `node2`. Seed and peer mappings use node IDs, machine keys,
or complete domain names so the repeated exposed name `node1` is unambiguous.
The Web Console crop targets the complete outer iframe together with its H1,
avoiding nested-frame scrolling and retaining the full heading and iframe
border without changing crop behavior for other screenshots.

### Staging infrastructure

`vpsfree-cz-configuration` declares one stopped-by-default NixOS container on
aitherdev:

- container: `kb-staging`, `autoStart = false`;
- private addresses: host `192.168.123.1`, container `192.168.123.2`;
- Czech: `http://kb-cs.aitherdev.int.vpsfree.cz`;
- English: `http://kb-en.aitherdev.int.vpsfree.cz`;
- internal DNS CNAMEs point at aitherdev;
- the existing aitherdev nginx is the only VPN-facing endpoint and proxies to
  the container;
- production-compatible DokuWiki, template, syntax plugins, ACLs, and shared
  media are used;
- production OAuth, OAuth secrets, and analytics are excluded;
- generated local `authplain` API users are used only for staging.
- a root-owned `kb-staging-containerctl` helper accepts only `start`, `stop`,
  and `clear` for the fixed container; aither has passwordless sudo access to
  those three exact helper invocations, not to `nixos-container` generally.

The internal sites intentionally use HTTP, consistent with other aitherdev
services. They are reachable only through internal DNS/VPN firewall rules.
Disposable staging credentials therefore never reach production and can be
regenerated by removing their local files. Production OAuth is not exposed to
an HTTP callback.

Only the user/operator can deploy this configuration from a build machine.
This initiative prepares the configuration and builds the complete aitherdev
system closure; it does not deploy the machine or DNS.

### Ownership and reset lifecycle

`bin/kb-stage` serializes the single staging container by the verified active
development-session slug. Ownership and container data survive `stop`. `reset`
first clears all staging DokuWiki state and history, then mirrors the current
production Czech/English pages and their shared media. `release` stops the
container and clears ownership, but refuses to discard a pending review bundle
without an explicit override.

The installed `mlfarm` translation map is populated lazily. Reset and release
tooling therefore renders every English target before its Czech `<page>`
source and verifies that both rendered pages contain both language links. The
27 paired candidate pages must pass this check; the three intentionally
unpaired pages remain unaffected.

### Candidate and publication lifecycle

Candidates retain their real page IDs, translation mappings, relative links,
and final language-first screenshot references. `kb-release.yml` records:

- each page's production source revision and source SHA-256;
- each candidate page path and SHA-256;
- each target media ID, local path, SHA-256, and create/update policy.

`bin/kb-release stage` refuses production drift, requires a clean staging
mirror for all candidate pages, writes media before pages, verifies all staged
bytes, and records the exact pending manifest digest. `verify` can recheck
staging or production. `promote` requires both the same owned/pending manifest
and an explicit production-approval flag, rechecks production drift, writes,
rechecks every source page again immediately before its save, and verifies all
results. DokuWiki has no compare-and-swap page-save API, so a narrow race with
an independent editor remains between that final check and the write;
publication should run in an announced editing window. `bin/kb-page` applies
the same environment boundary:
staging ownership for staging writes, explicit approval for every production
write, including the legacy `drafts:` namespace.

The previously uploaded production draft namespace is obsolete. Remove its 30
pages and 60 media objects only after the staging instances have been deployed,
mirrored, populated, and verified, and only with explicit production-write
approval.

## Compatibility and deployment

- No API, database schema, protocol, or production DokuWiki state format is
  changed.
- The new aitherdev container is stopped by default. Deploying the host
  configuration creates capability but does not start or reset staging.
- Existing production pages and legacy screenshots remain untouched until an
  explicitly approved promotion. New screenshot IDs are create-only.
- Old coordination tooling that used `--approved-non-draft` fails with a clear
  migration message; callers must use `--approved-production`.
- Staging reset intentionally preserves no staging wiki history. Stopping the
  container preserves all current review state.
- Rollback of the host configuration removes the proxy/container declaration;
  it does not affect production KB state. Container state can be retained or
  removed independently by the operator.
- Deployment order: merge/deploy configuration and internal DNS, claim/start
  staging, reset from production, stage and verify the release, review, then
  request approval for production promotion. No coordinated fleet update is
  required.

## Verification

1. Validate capture schema, production-shaped fixture data, exact
   scenario/checkpoint mappings, 59 PNG hashes, 63 references, and
   language-first paths with `nix develop -c bin/check`.
2. Run Ruby syntax and unit tests for authentication, ownership, production
   gates, manifest validation, source-drift checks, and staged verification.
3. Regenerate the screenshot manifest and 30-page/59-media release bundle; fail
   on replacement counts, missing media references, or checksum differences.
4. Format Nix, run repository hooks, and build
   `cz.vpsfree/machines/aitherdev` through `confctl`.
5. Run the mandatory standalone change review after functional commits and
   quick checks, before starting the full three-machine capture cluster.
6. Run the `screenshots` topology, regenerate all 59 Czech captures, inspect
   contact sheets, rebuild the page/media bundle, and restage it at the real
   IDs. Verify all 27 language pairs and every rendered screenshot.
7. Push feature branches. Production promotion remains a separately approved
   operation.
8. For the English follow-up, derive the 14 affected production pages and 54
   old media references from the bilingual schema, preserve all non-media
   source bytes, and package all 59 English captures as create-only media.
   Reset staging after Czech publication, stage the English bundle at its real
   page IDs, verify all API bytes, counterpart links, rendered pages, and media
   responses, then stop for user review without writing English production.

## Publication and English follow-up

- Before Czech publication, remove the obsolete review namespace using an
  explicit checksummed cleanup manifest. The 30 pages exist only on the Czech
  wiki; the 60 media objects are shared by both production wikis and are
  deleted exactly once, then verified absent through both endpoints.
- Promote the already staged Czech manifest in its existing media-first order,
  verify all 30 pages and 59 canonical media objects through the API and a
  browser, and retain legacy production media unchanged.
- Extend the capture inventory to 59 language-neutral concepts with Czech and
  English variants. Generate all 59 English PNGs even when an English article
  does not currently embed a particular concept.
- Build the English release from current production sources. Upload all 59
  `en:screenshots:vpsadmin:*` media objects and change only existing image
  references in English pages; do not rewrite English prose in this phase.
- Stage and verify the English release, then stop for user review. English
  production promotion happens only after that review.
- After both language releases are complete, start a separate initiative for a
  standalone DokuWiki annotation plugin and a semantic vpsAdmin documentation
  contract. That follow-up is not allowed to delay or alter the reviewed
  localization publication.
- Before English approval, normalize every screenshot on
  `manuals:vps:management` to uniform non-floating left placement and restage the
  checksummed bundle. Record a concise English production summary in the
  manifest; production remains gated on the user's subsequent approval.
