---
lifecycle: archived
---

# HaveAPI and vpsAdmin TypeScript releases

## Current outcome

**Requested releases are published and verified.** HaveAPI 0.31.0 covers every
maintained component. SDK 0.1.0 was published by the user; SDK 0.1.1 was published
through the protected GitHub Actions trusted-publisher workflow. Public bytes,
integrities and SDK provenance match the reviewed sources and retained artifacts.
No operation, repository claim or machine reservation remains held.

The session stays active/open: HaveAPI's release head is **ready, awaiting merge
approval** into master. Release authorization did not grant that separate
integration. SDK/main and PHP/master contain their exact final feature heads.
No archival, deletion, stopping, cleanup or branch removal is authorized.

## Phase checklist

- [x] Exact session binding, retained team/settings/access and initial tracking commit.
- [x] User-confirmed pending haveapi-typescript-client RubyGems publisher.
- [x] All maintained HaveAPI components versioned, reviewed, fully checked and published as 0.31.0.
- [x] HaveAPI fixture failure understood, fixed and future-minor regression verified.
- [x] Approved PHP-first synchronization, short-claim integration, remote proof and claim release.
- [x] Every HaveAPI registry, GitHub Release asset and Packagist source verified.
- [x] MIT SDK 0.1.0 reviewed/checked, manually published by user and integrity verified.
- [x] SDK trusted-publisher instructions and documented GitHub protections configured/reviewed.
- [x] SDK 0.1.1 metadata and publish-path correction reviewed, checked and integrated into main.
- [x] Exact failed SDK tag recovery approved, original identities preserved and replacement verified.
- [x] SDK 0.1.1 protected OIDC publication, public tarball/SRI and signed provenance verified.
- [ ] Separate HaveAPI/master integration approval; no release work remains.

## Exact final source and remote evidence

Fresh SSH readback at the final checkpoint established:

| Repository | Reviewed base | Final head and remote status |
| --- | --- | --- |
| haveapi | `4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c` | Release branch haveapi-0.31 and peeled v0.31.0: `c9124da141adc258fbbaf67d4ec19ee3f8580849`; master remains base |
| vpsadmin-typescript-client | Historical `149c72f11acef67224a47ed77711a3abb805fbd4`; path-fix base `4689d00ca4acf0cc26a3507fc3c238b687b53475` | main, session feature branch and peeled v0.1.1: `60a1b5d1b911c610bd993d93ae2b28d1932a0ccc` |
| haveapi-client-php | `a02dd2506209f54ea782fbd949243207bf9f93bc` | master and peeled v0.31.0: `eafc2a9b77990dd5c927f0d412d14801261223cc` |

Canonical origins are `git@github.com:vpsfreecz/<repository>.git`. Worktrees are
under `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-prepare-client-releases/`.
All final comparisons were captured. SDK/PHP clean detached integration targets
remain retained alongside their feature worktrees. No infrastructure deployment
occurred. Published source boundaries remain exact ancestors, not reconstructed
or falsely described as merged.

## HaveAPI 0.31.0 publication

[Preparation and final receipt](haveapi-preparation.md) contains all commands,
resolved-lock identities, failures, recovery and exact registry hashes. Corrected
run [40554625752](https://github.com/vpsfreecz/haveapi/actions/runs/40554625752)
build/publish succeeded at c9124da1; all 19 other current-head workflows passed.
GitHub Release425817748 was published 2026-10-27T18:13:31Z.

Verified five Ruby gems (name/version/platform ruby/SHA256), npm name/version/SRI,
both Python files/SHA256, PHP master/tag, Packagist0.31.0 source+dist eafc2a9,
and every public Release asset's actual bytes. Original artifact12756023295 and
all 12 public assets retain manifest SHA256
`6e31e4c59e4629adeff0fd8f00e86935b644b6018c3d53361450b07a1b102a49`, binding source,
run, all11payloads and10dependency-lock texts. Tools-only verification passed.

All maintained destinations released: haveapi, haveapi-client, Go/Rust/TypeScript
generator gems; npm client/browser bundle; Python; PHP/Composer. Elixir is
unmaintained/excluded. First trusted TS gem upload succeeded; private RubyGems
pending-to-normal publisher state is not publicly exposed, so no account-state
claim is made beyond successful publication and exact gem verification.

The first tagged build failed7lineage examples before artifacts/upload. Fixtures
incorrectly normalized the checkout's new0.31 version before constructing0.30
inputs. Production0.30 guard was preserved; isolated synthetic sources and a
0.32-template regression fixed recurrence. Focused18examples/hooks/RuboCop and
post-review160-example deterministic suite passed. Original failed annotated
object73eb7726a245804b8aa3abdff9181772f827d2d9/source3bbb98e7 remains at
`refs/recovery/2026-10-27-prepare-client-releases/v0.31.0-failed`. User explicitly
corrected an interim0.31.1 choice to fix/retry0.31.0; exact-old-object lease
replaced only that failed tag. Final tagobject d300dfa8715cca35c29bce312333ece886b5e74e
peels reviewed c9124da1. No0.31.1 mutation occurred.

## SDK 0.1.0 and 0.1.1 publication

[SDK 0.1.0 receipt/instructions](manual-publication.md): user selected MIT/0.1.0,
published at2026-10-27T17:40:04.673Z; original artifact12755255825 and public
integrity match exact source38a25ad88d0bf3018670184620cf69cdb71e92e7.

[SDK 0.1.1 final record](sdk-0.1.1.md): corrected run
[40566122638](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/40566122638)
and publish122408377105 succeeded. npm public time2026-10-27T19:18:54.829Z,
latest0.1.1. Public tarball is byte-identical to corrected tagartifact12762393553:
SHA256 `9d262825d1dffb695eaace8029e3e7eb03a44338131602822907632945f566e8`;
SHA512 `sha512-G7YlKCe4jX/ikmDYUT4SdZM2hf8Qvi1mQYNVetdNtHYYm4fzfLhBhcQEZYgDs7shVaAA5Bk6NCwcezqRPAWohA==`.

npm identifies GitHub Actions trustedPublisher github/config
3bb51631-4704-43ac-9e90-622e84fcc9c5. Publication statement and SLSAv1 subject
pkg:npm/vpsadmin-typescript-client@0.1.1 bind exact archive SHA512. Provenance and
verified DSSE signature/certificate bind workflow release.yml, tagv0.1.1,
source60a1b5d, run40566122638/attempt1 and environmentrelease. Public
[Sigstore entry](https://search.sigstore.dev/?logIndex=3523718588) matches npm's
provenance payload/certificate. This establishes actual direct OIDC acceptance;
no manual token, fallback, upload retry, repack or rebuild was used.

First0.1.1 attempt failed before OIDC/upload because npm treated unprefixed
`release/package.tgz` as GitHub shorthand. The workflow now uses
`./release/*.tgz` with a concise rationale. Actual pinnednpm11.19 command dry-run
against the original archive passed in isolated auth/config state;6release tests,
affected review and fullCI passed. Original failed tagobject
cb914823d2e74e9565e56a1af770b0d129fd0876/source4689d00 and artifact12761282299 remain
unaltered under recovery receipts/ref. Duplicate old run40562213605 was rejected
at its protected gate before any publish step; no current-head duplicate occurred.
User explicitly approved fix60a1 integration and replacing only failedv0.1.1;
exact-old-object lease produced final tagf4cb49ab54214d043d34716d30a43f14224d6ce2,
peeling60a1. Old4689 and new60a1 receipts retain their actual distinct source/tag
bindings despite byte-identical payload. See [effects reconciliation](sdk-0.1.1-recovery-reconciliation.md).

[GitHub setup receipt](sdk-trusted-publishing.md): releaseenv25494232596,
required revieweraither64/User4717906, self-review allowed, sole v* tagdeployment
policy64571929; NPM_RELEASE_ENABLED=true; sole active creation-only tagruleset
25982494 with repository-admin bypass. Exact settings/baseline/restoration limits
are recorded. Actual protected publication confirmed this setup and npm identity.

## Reviews, approvals and short claims

- [Initial review](final-review.md), [fixture review](fixture-review.md),
  [PHP history review](php-review.md), [SDK 0.1.1 source/config review](sdk-0.1.1-review.md),
  [SDK path-fix review](sdk-path-review.md): no Blocking/Important/Advisory findings.
  Same retained reviewer0, thread01a17e59-3823-76f0-9764-5525072525a2,
  gpt-6.1-sol/xhigh/read_only; no overrides/fallback. Explicit complete-series,
  consolidation and no-migrations conclusions retained. Actual published38a and
  integrated4689 boundaries justify retaining their history.
- User **"Approve PHP sync and finish release"** covered PHP eafc2a9/master/tag
  and PHP-before-other-registries ordering. [PHP preparation/receipt](php-preparation.md)
  and [ordering](php-publication-order.md) preserve details. Claim
  18deacb8-41f8-41c8-915f-d03ef92c8645 released/readback18:07:40Z after ff/atomic
  push/exact proof, before protected approval deployment7366320231.
- User **"Approve SDK main integration and release"** covered4689/main/tag0.1.1.
  Claim8c94ceb8-c796-4480-afb4-1304406dff5a released/readback18:40:05Z before CI/tag.
- User **"Approve fix and retry 0.1.1"** covered60a1/main plus exactfailedtag
  replacement and trustedretry. Claim8f6f47a4-e8f5-44b7-af0d-61fb4854fca9 held only
  fresh target/feature/remote checks, ordinary ff/push and exactremote proof;
  released/readback19:06:16Z before tag/CI. Final protected deployment7367860943
  approved only after tagged artifact acceptance. No claim remains held.

No repository claim was held during checks, review, approval waits or CI.
No machine was reserved/deployed. Latest selected package guide
`/nix/store/yi4hlb3s8lmm8w2bv34z35yhy6fmqk29-dev-workspace-0.2.0`, catalog
4b78710cec4cda72b150007131b36b252d54311fdfd438412d587f08e65c4a12 was read/refreshed;
changes from earlier guide were package/catalog headers only. Watchers used
pinned Luna/low policy; one temporary tool-unavailability used the documented
visible parent fallback, without model substitution or duplicate test batches.

## Handoff and retention

Release work is done. Only separate HaveAPI/master integration remains unapproved;
leave lifecycle active and the session open. Preserve every feature/tag/recovery
ref, original accepted artifact and receipts. Initial tracking commit433b3b61f
preceded code/external mutation; this consolidated final handoff records the
completed milestones without committing raw logs/builds. Preserve unrelated
shared-workspace changes. No archival, deletion, stopping or cleanup is implied.

Reusable lessons: [maintenance fixture version independence](../../notes/haveapi/2026-10-27-release-fixture-version-independence.md),
[npm local archive path](../../notes/vpsadmin-typescript-client/2026-10-27-npm-relative-tarball-path.md).

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-prepare-client-releases/
