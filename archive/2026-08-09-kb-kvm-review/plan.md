# 2026-08-09-kb-kvm-review

## Goal

Replace the historical Czech and English KVM KB articles with a current,
test-backed Debian/libvirt guide. Make the recommendations about platform
features, ZFS datasets and properties, QEMU image formats, and the retained NFS
installer-ISO workaround precise and maintainable.

## Affected repositories and services

- The coordination workspace tooling: let KB candidate plans distinguish
  guarded updates of existing media from creation of new media.
- `vpsadminos`: reference its pinned external test framework without changing
  the shared framework's repository-source behavior.
- `vpsadmin-kb-captures`: add the durable runtime test suite, documentation
  contract, reusable command samples, and CI integration.
- `kb.vpsfree.cz` and `kb.vpsfree.org`: prepare and stage complete candidates
  for `navody:vps:kvm` and `manuals:vps:kvm` at their real page IDs.
- Obsolete, unlinked pages `navody:vps:kvm-openrc` and
  `navody:vps:vpsadminos:libvirt` are deletion candidates after a complete
  backlink scan.
- `vpsadmin` and `vpsadminos` remain pinned dependencies and sources of the
  cluster topology, platform behavior, and integration-test framework.

## Approach

1. Extend `vpsadmin-kb-captures` as an external consumer of the pinned
   vpsAdminOS test framework while preserving its operator-run capture app.
2. Factor the existing vpsAdmin cluster topology so the capture workflow and
   KVM documentation tests use the same platform setup.
3. Provision current `Debian (latest)` VPSes through vpsAdmin without explicit
   KVM/TUN overrides, then test platform defaults, libvirt on the system
   connection, a default-property subdataset mounted as a libvirt directory
   pool, production-shaped guest networking, and the narrowly scoped NFS
   read-only installer-ISO workaround.
4. Store executable documentation commands in the capture repository and map
   article claims and snippets to maintained tests in a runtime contract.
5. Run static checks on every change and the tagged KVM-in-a-VPS suite on a
   recurring, manual, and relevant-change CI schedule.
6. Rewrite both language variants together. Use Debian/libvirt as the only
   complete walkthrough, retain no historical Alpine/OpenRC instructions, and
   document NAT and routed guest networks without bridging the VPS veth.
7. Keep the existing feature screenshot, generate a dedicated dataset
   screenshot with a 20 GiB root dataset and a 100 GiB `vm-images` subdataset,
   build all-page KB candidates, check backlinks, stage the exact release
   manifest, and stop for explicit production approval.
8. Wrap the external runner inside the capture flake and pass the flake's
   existing immutable, Git-filtered `self` source through
   `TEST_RUNNER_REPO_ROOT`. Expose the wrapper as both the app and package so
   ignored `.devcluster` VM disks never reach the runner's path-flake snapshot,
   without changing source semantics for other vpsAdminOS test-framework users.

## Documentation decisions

- vpsAdminOS runs VPSes as containers, so KVM guests use the physical node's
  hardware virtualization directly; this is not nested virtualization.
- KVM and TUN/TAP are enabled by default. The guide says only which features
  are required and retains the feature screenshot.
- A separate subdataset is recommended so VM-image properties can be changed
  later without affecting the VPS root dataset. Mount it at
  `/srv/libvirt/images` and register that path as a persistent libvirt
  directory pool.
- Leave ZFS properties at platform defaults unless a measured workload justifies
  tuning. Compression stays enabled and `recordsize=128K` is described as the
  default maximum block size, not a fixed allocation unit.
- Prefer raw images on ZFS. Mention qcow2 only for its additional image-format
  features and let libvirt create all volumes.
- Rely on Debian package installation to enable and start libvirt; do not add a
  redundant `systemctl enable` command or a disposable smoke domain.
- Keep NFS advice only for a reproduced lock failure while accessing a
  single-client, read-only installer ISO. Prefer a local ISO and never apply
  `nolock` to writable or shared VM storage.
- The outer VPS veth is a routed layer-3 link and must not be attached to a
  libvirt bridge.
- For public addresses assigned to the VPS, define an explicit dual-stack
  libvirt network with private IPv4 and ULA IPv6 guest addresses, NAT44 and
  NAT66, and persistent TCP/UDP port forwards through a network hook. Explain
  the XML and essential firewall operations before presenting the complete
  automation. Keep this network on a subnet distinct from libvirt's active
  `default` network and call out that interconnected private networks need
  independently generated ULA prefixes.
- To assign the public IPv4 `/32` to a domain, ask support to assign the VPS a
  private IPv4 `/32`, route the public address to the VPS through that private
  address in vpsAdmin, and route it onward over a private libvirt transit
  network without DNAT or SNAT. The routed public address is not configured on
  an interface inside the VPS.
- Give the routed-address VPS its normal public IPv6 `/64`, then use another
  `/64` already available to the user, route it through an address in the
  primary prefix, and place that delegated `/64` directly on the libvirt
  bridge. If the user already has a larger routed prefix such as `/48`, select
  a dedicated `/64` from it. Do not route individual `/128`s from the VPS's
  primary `/64` for this design.
- Compare the dual-stack NAT and routed-address topologies, including their
  operational advantages and disadvantages. The setup scripts are run when a
  network is created or its addresses change; libvirt autostart, network hooks,
  and persistent sysctls handle reboots.

## Compatibility and deployment

The capture-repository changes add tests, contracts, media, and a local runner
wrapper only; they do not alter vpsAdmin or deployed vpsAdminOS APIs, schemas,
protocols, persisted state, node configuration, or shared test-framework
behavior. The wrapper reuses the immutable Git-flake source already selected
by `nix run`, so tracked dirty changes remain available and ignored/untracked
runtime state remains outside the Nix store. The external suite consumes the
revisions pinned by the capture repository and must continue to work when
those pins are advanced. The workspace candidate-builder extension is backward compatible:
media entries remain create-only by default, while an explicit update requires
the SHA-256 of the existing production object and carries it into the release
manifest.

KB publication is independently approval-gated. Candidates are staged only if
production still matches the recorded source revisions. Promotion updates both
languages together and deletes obsolete pages only when the backlink scan is
clean. Rolling deployment and rollback are therefore limited to DokuWiki
revision history; no coordinated node update is required.

## Testing plan

- Run the repository's existing static checks and runtime-contract unit tests.
- Build both the capture test-runner package and app, verify that the wrapper
  exports an immutable store source containing no `.devcluster` or disk-image
  paths, and list all tagged tests through the normal `test-runner.sh` entry
  point while retaining the prior vpsAdminOS pin.
- Exercise the five RSpec-style scripts independently and through the
  `kb-runtime` tag:
  - `kb/kvm#platform-defaults` verifies default features and devices
  - `kb/kvm#libvirt` installs Debian packages without a manual service-enable
    step and verifies the system connection and KVM capabilities without
    creating a domain
  - `kb/kvm#storage` creates and mounts the recommended subdataset through
    vpsAdmin, preserves inherited ZFS defaults, configures the documented
    libvirt pool, and creates a volume through libvirt while retaining logical
    headroom
  - `kb/kvm#networking` boots deterministic Nix-built KVM appliances and
    verifies dual-stack public-VPS NAT with IPv4/IPv6 HTTP, SSH, outbound
    access, and additional UDP forwards; public IPv4 routed through the VPS's
    private address; and a delegated IPv6 `/64` routed through the VPS's
    primary `/64`, including inbound and outbound paths
  - `kb/kvm#nfs-locking`
- Confirm the suite provisions through vpsAdmin, uses the exact Debian image
  label, exercises the documented command samples, and implements route-via
  using the same vpsAdmin/osctld path as production.
- Run the mandatory fresh-context change review after quick verification and
  commits, before the long integration suite.
- Fetch the complete Czech and English KB corpus, validate navigation and
  annotations, scan backlinks to deletion candidates, stage the manifest, and
  verify staged pages and media before requesting production approval.

## Generic managed-article follow-up

The repository will become `vpsfree-kb-contracts` and will own an explicit
subset of source-controlled KB articles together with their screenshots,
samples, contracts, and runtime tests. The KVM guide is the first registered
article; this does not make the repository authoritative for the complete KB.

- Replace the KVM-specific runtime manifest and checker with a generic article
  registry validated against the external test framework's `testsMeta` output.
  Every article test script carries the common `kb-runtime` tag and an
  article-specific `kbArticle` label. CI derives one runtime job per article
  from the registry.
- Add a visible localized maintenance note to every managed page, linking its
  canonical source and automated test and directing contributors away from
  direct wiki edits. Update both KB authoring guides with the managed-page
  exception.
- Extend candidate construction with managed-article replacement and a
  three-way reconciliation among the fetched wiki page, the explicit Git base
  commit, and the current canonical source. Wiki-only changes are never
  overwritten: release preparation stops until they are explicitly adopted or
  merged into Git and pass the contract and tests.
- Require the explicit base to be a full commit OID. Managed sources and the
  registry must match the contract repository's committed HEAD, and registered
  pages cannot use legacy release-time replacements or sample expansion. Bind
  the base, contract HEAD, registry digest, and canonical page digests into the
  candidate index and generated schema-3 release manifests.
- Rename the GitHub repository and active references. Keep the existing
  capture provenance identifier and flake outputs compatible. Since unrelated
  sessions still have linked worktrees using the old local bare path, expose
  the new project name through a temporary ignored symlink and defer moving the
  bare directory until those worktrees are gone.
- Rebuild and stage the KVM pages and the Czech/English authoring guides after
  the repository rename. Production publication remains separately approval
  gated.

The shared candidate-plan schemas 1 through 3 remain supported. Schema 4 adds
managed articles without changing DokuWiki release manifests or production
write safeguards. No vpsAdmin, vpsAdminOS, database, API, protocol, node
configuration, or persisted-state change is introduced.

## Invisible managed-page marker follow-up

Replace the visible source/test note on every repository-managed article with
an invisible `<kb-managed>` marker immediately after the bilingual `<page>`
mapping. The marker carries the canonical GitHub source and test links. The
existing `vpsadmindoc` plugin records those links as page metadata, adds a
localized source link to the right-hand page toolbar, and warns in every
editor-bearing view without blocking emergency edits.

- Keep the page ID as plain text and use the existing
  `TEMPLATE_PAGETOOLS_DISPLAY` hook; do not change the DokuWiki template.
- Validate marker attributes as untrusted input, render valid markers as no
  body content, and render malformed markers with a localized diagnostic.
- Require one correctly positioned marker per registered page and verify its
  source/test URLs against `contract/articles.yml`.
- Update the Czech and English authoring guides to describe the toolbar and
  editor warning instead of a notice below the article title.
- Pin the reviewed plugin revision in the aitherdev staging and production KB
  configurations. Build both closures, but leave machine deployment to the
  operator and retain the separate approval gate for production KB writes.
- Preserve all KVM prose, executable samples, runtime tests, article IDs, and
  release reconciliation guarantees.

## Managed-page editing guidance follow-up

Keep the normal DokuWiki Edit action and clarify that direct edits are possible
but are not verified by the repository test. The managed-page toolbar source
link and every link in the editor notice open in a new tab with
`rel="noopener noreferrer"`.

- Use this exact English notice: “This page is managed in a repository and
  covered by an automated test. Manual edits made directly in the KB are not
  verified. See the source on GitHub, automated test, and Contributing to the
  Knowledge Base.”
- Use the equivalent Czech notice: “Tato stránka je spravována v repozitáři a
  pokryta automatickým testem. Ruční úpravy provedené přímo v KB nejsou
  ověřovány. Viz zdroj na GitHubu, automatický test a Jak přispívat do
  znalostní báze.”
- Link source and test from the validated marker. Generate the editing-guide
  link locally with DokuWiki for `informace:jak_psat` or `information:kb`, so
  staging remains on staging and production remains on production. Do not add
  another toolbar action or marker attribute.
- Align both KB authoring guides with the same non-prohibitive policy while
  retaining the existing drift protection and release reconciliation text.
- The marker and metadata schemas remain unchanged. Old and new plugin versions
  accept the same pages, so rolling deployment and rollback require no page or
  persisted-state migration. Deploy the plugin before publishing the updated
  guidance; production KB writes remain separately approval-gated.

## Czech informal-address follow-up

Make informal singular address (`tykání`) the durable convention for Czech KB
articles. Record it in the coordination workspace and contract-repository
instructions, then convert all direct reader address in the Czech KVM article
from polite plural to singular while preserving technical meaning, commands,
screenshots and the English article.

Refresh the Czech article-section fingerprints and any derived identities for
changed annotated paragraphs. Run the complete static contract checks and
mandatory fresh-context review, then push the development branch and monitor
its existing workflows. Reconcile the managed article from a complete
production fetch and stage a Czech-only guarded release at `navody:vps:kvm`.
Production promotion remains separately approval-gated.

## KVM navigation-contract completeness follow-up

Cover every vpsAdmin operation in the KVM storage workflow with a semantic
navigation annotation. Add an inert dataset Edit landmark to vpsAdmin, bind
Edit, Create dataset, and Mount to both KVM pages and the existing dataset
screenshot, and rewrite the storage paragraph as three explicit annotated
steps. Strengthen independent discovery for this workflow and make a manual
action-by-action annotation audit mandatory in the fresh-context review.

Record the same broader rule in the contract repository and the Czech/English
KB authoring guides: instructions to perform vpsAdmin actions require
`<vpsadmin-nav>` even when they do not name a menu or form. Pin the final
vpsAdmin commit, refresh the complete bilingual capture provenance, rerun the
managed KVM suite, and replace the obsolete staged Czech-only release with
guarded bilingual candidates. No existing production revision summary is
rewritten, and corrected publication remains approval-gated.

## Czech KB change-summary follow-up

Czech production change summaries use informative noun phrases that describe
the resulting changes, rather than infinitive instructions. For example, use
`Aktualizace KVM, doplnění sítě a vysvětlení správy článků v repozitáři`
instead of `Aktualizovat KVM, doplnit síť a vysvětlit správu článků v
repozitáři`. Keep summaries specific and single-line; leave all existing
DokuWiki summaries and the obsolete pending manifest unchanged.
