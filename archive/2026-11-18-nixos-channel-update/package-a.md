# Package A: vpsFree.cz stable channel

Owner: implementer0. Scope: `vpsfree-cz-configuration` only; no deployment,
default-branch integration or PR. Architect0 owns the design and lead owns
acceptance and integration.

## Preparation

- Bound session and both environment variables verified as
  `2026-11-18-nixos-channel-update`, workspace
  `/home/aither/workspace/ai/vpsfree.cz`; live roster grants implementer0
  `workspace_write`. Capacity confirmed to lead before package execution.
- Initial plan/state commit verified:
  `d918b4539a432f4f39fd340f902fb333e195cae2`.
- Freshly fetched default/base:
  `e3910c79e85edc94ee3e715bf93887413bfed827` (`origin/master`).
- Registered branch: `2026-11-18-nixos-channel-update`.
- Worktree: `worktrees/2026-11-18-nixos-channel-update/vpsfree-cz-configuration`.
- Canonical remote: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`.
- `nixos-stable.nixpkgs` maps to `nixpkgsStable`; initial URL is
  `github:NixOS/nixpkgs/nixos-26.05`.
- Checkout registration created the worktree and recorded its exact base, but
  the ambient Overcommit checkout hook reported missing Ruby gems. Repository
  `nix develop` installed its documented local gems; `bundle check` passed and
  `bundle exec overcommit --install` installed hooks. All final rebase/commit
  operations ran inside that shell. No hook bypass was used.

## Boundary and documentation

The initial branch-switch interpretation was superseded by the user's explicit
one-time-update correction. Lead released the corrected bounded brief and
architect0 amended `design.md`. Two unpublished branch-switch commits were
removed by an owned narrow rebase; neither was integrated, deployed or published.
The final change preserves the original tracking branch.

Other inputs, functional configuration and existing hooks are outside the edit
scope. Individual revisions, evaluation evidence and deployment selectors belong
in this session record. Repository README and AGENTS.md explicitly cover confctl
channel updates and say routine channel bumps need no separate project
documentation commit. No reusable procedure or local behavior changed. Topic/class/placement: this
one-time pin, its tests and target list are individual operations evidence for
operators and reviewers; this file is their authoritative home, with the
existing README/AGENTS channel instructions unchanged.

## Committed change and quick checks

- Exact base: `e3910c79e85edc94ee3e715bf93887413bfed827`.
- Exact head: `828c390c7e1857f11522933977afd852634b85f8`.
- Full series: one generated commit, `inputs: set nixpkgsStable to 4077fb98`.
- Full changed-file inventory: `flake.lock`, 3 insertions and 3 deletions.
- Command, from the original base flake and lock inside `nix develop`:
  `confctl inputs channel set --commit --no-changelog nixos-stable nixpkgs 4077fb98f09d5bd847f848ae4f214a4c5b9f0a9d`.
- Generated message retained unchanged. Pinned confctl's Setter saves/restores
  the selected root input's complete `original` attributes and generates the
  lock through Nix; no manual lock edit occurred.
- Hooks: pre-commit Nixfmt and commit-msg SingleLineSubject, TextWidth,
  TrailingPeriod all passed. `git diff --check` passed; worktree clean.
- Semantic old/new lock assertion passed: same root mapping, same node set and
  follows edges; only root-resolved `nixpkgsStable.locked` revision, content hash
  and timestamp differ. Every sibling node remains identical.
- `flake.nix` is byte-identical to base. Complete selected `original` remains
  `{ owner = NixOS; repo = nixpkgs; ref = nixos-26.05; type = github; }`.
- Locked revision: `4077fb98f09d5bd847f848ae4f214a4c5b9f0a9d`, NAR hash
  `sha256-zX+62p0XLF5AbMgzy8JgNBH6cTJSiDovTOSk2NBc0GQ=`.
- GitHub compare of PR #589970 merge
  `1e6cf0d7cf5f5354d1bfd7105813dddb527851d4` to that exact lock: `ahead`,
  ahead_by 6, behind_by 0; merge-base equals the PR merge. Locked source's
  `pkgs/servers/http/nginx/stable.nix` declares 1.30.7 and
  `sha256-JWW1yDcFDpWPcPsPc8SOK8pFQq00n9NW9G+wxyYQvG4=`; `mainline.nix`
  declares 1.31.9 and `sha256-oRxe7uLiV/RHjw5kn4SwBAeH0nfS0+UjOVKqa23LgK0=`.
- Whole-branch inventory: no migrations, module changes, transitional paths,
  superseded pin updates or obsolete commits remain. Nothing from this package
  has been released or deployed. Independent history assessment belongs to lead.
- Git/index/rebase/hook window explicitly released to lead for merge preparation
  after quick checks. Lead reports both exact heads merged and remote-proven, repository claims
  released. Publication/integration evidence is lead-owned; package head unchanged.

## Evaluated inventory

Managed metadata evaluation found 110 entries, 103 managed and 51 managed machines
whose resolved `nixpkgs` role is `nixpkgsStable`. Seven unmanaged org.vpsadminos
reference entries are not deploy targets in this repository.

The session-local probe copies pinned confctl
`ff5e017780a35fb97b549db2a51b570193867c3b`'s evaluator and inserts exactly one
output exposing its existing `evalConfigFor`. All original evaluator text,
modules, specialArgs, source inputs and channels are preserved; the relocated
unused `moduleOptions` import is not forced. Raw probe/results live in
`package-a-raw/` and are disposable. The installed utility package is
`/nix/store/zdr7y043hi6y4sbfbsixsrlgbvd530nk-dev-workspace-0.2.0`; its validated
agent catalog SHA-256 is
`780db421a46b2a3bb6128dcc60b706de0753bd2a564c2e5f3c310344f3fce0bb`,
verification watcher `gpt-6-luna`/low, utility native identity
`dw_32fc0df129055f50f5e6054c8d971d33430112edeba8b88d`, full-access/never.
Fresh children `/root/a_inventory_watch` (interrupted first probe) and
`/root/a_targets_watch` (successful narrowed probe) owned separate operations. Source
is final configuration head `828c390c7e1857f11522933977afd852634b85f8` and
locked input `4077fb98f09d5bd847f848ae4f214a4c5b9f0a9d`. The final targeted
enable/package/source inventory passed in about 82 seconds
(exit 0, empty stderr); all watcher sessions are quiescent. No activation ran.

Final selectors and package provenance are below. The first all-assertions
evaluation was intentionally interrupted and supplies no passing evidence; the
selected normal proxy system derivation passed as recorded below.

Verification refinement: the first all-consumer package/assertion evaluation
exceeded three minutes and used `outPath` fields that Nix serializes as a path,
losing nested metadata. It was stopped at its exact owned process; watcher
reported exit 1 (`interrupted by the user`) and no surviving sessions. This is
not a configuration failure or passing assertion evidence. Its log showed two
small web-package import-from-derivation builds, not a system/kernel build.
The corrected probe shares one original evaluator and selects nginx enablement
and package/source identities only, uses `outputPath` fields, and ran in a new
fresh watcher. The separate selected toplevel evaluation uses the repository's
unmodified exported confctl output.

Selected final system evaluation passed (exit 0, approximately six seconds):
`timeout 45s nix eval --raw --no-write-lock-file --no-update-lock-file .#confctl.toplevel.m_cz_vpsfree_containers_prg_proxy_e8bbb836.drvPath`
returned
`/nix/store/zznyfszfz739xbxs8q25dxh1iyshpy88-nixos-system-proxy-26.05.20261118.4077fb9.drv`.
This evaluates the normal exported system derivation and its assertions without
realizing it. No full system build, VM test or deployment was run.


## Final nginx deployment subset

The corrected `targets.nix` probe passed at exact final head/input above; its
`targets.json` contains all 51 resolved input consumers and actual nginx package
metadata. Automated evidence assertions found **17 enabled nginx targets**, all
version **1.30.7**, each with the complete source identity equal to upstream
`nginxStable.src` (source derivation, output, URL, hash and mode). No independently
sourced nginx exists in this evaluated subset. The old exact input's source
package definitions declare stable 1.30.6/mainline 1.31.8; the local module graph
is unchanged. These are desired-configuration results, not an inspection of
currently deployed generations.

| Exact confctl selector | Host alias / FQDN |
| --- | --- |
| `cz.vpsfree/containers/discourse` | `discourse.vpsfree.cz` |
| `cz.vpsfree/containers/int.blog` | `blog.int.vpsfree.cz` |
| `cz.vpsfree/containers/int.kb` | `kb.int.vpsfree.cz` |
| `cz.vpsfree/containers/int.munin` | `munin.int.vpsfree.cz` |
| `cz.vpsfree/containers/int.utils` | `utils.int.vpsfree.cz` |
| `cz.vpsfree/containers/int.vpsfbot` | `vpsfbot.int.vpsfree.cz` |
| `cz.vpsfree/containers/int.web` | `web.int.vpsfree.cz` |
| `cz.vpsfree/containers/prg/proxy` | `proxy.prg.vpsfree.cz` |
| `cz.vpsfree/machines/aitherdev` | `aitherdev.int.vpsfree.cz` |
| `cz.vpsfree/machines/brq/apu` | `apu.int.brq.vpsfree.cz` |
| `cz.vpsfree/machines/build` | `build.vpsfree.cz` |
| `cz.vpsfree/machines/em1` | `em1.vpsfree.cz` |
| `cz.vpsfree/machines/prg/apu` | `apu.int.prg.vpsfree.cz` |
| `cz.vpsfree/vpsadmin/int.vpsadmin-webui1` | `vpsadmin-webui1.int.vpsfree.cz` |
| `cz.vpsfree/vpsadmin/int.webui-dev` | `webui-dev.int.vpsfree.cz` |
| `cz.vpsfree/vpsadmin/int.webui1` | `webui1.int.vpsfree.cz` |
| `cz.vpsfree/vpsadmin/int.webui2` | `webui2.int.vpsfree.cz` |

All targets except Discourse select package derivation
`/nix/store/lz5pkqfpx64qfb6xvq6pz3dyckp9hzay-nginx-1.30.7.drv`, output
`/nix/store/v5yfyvpd7z7lbzh86bpbh5cjp10qad4m-nginx-1.30.7`.
Discourse's module-derived package selects
`/nix/store/z9jxi85m4ri964vh58jyvi4418bsyh0a-nginx-1.30.7.drv`, output
`/nix/store/6l286wl3iglr3hnhhj39pjq2d9n9lcg9-nginx-1.30.7`.
Both use source derivation
`/nix/store/d6kgcj285iifmlnk9w1vq4gz3g4lsyl4-nginx-1.30.7.tar.gz.drv`, source
`/nix/store/z255nq6zrhzqaikkjsp9hbks8v9v55hd-nginx-1.30.7.tar.gz`, URL
`https://nginx.org/download/nginx-1.30.7.tar.gz`, flat SHA-256
`sha256-JWW1yDcFDpWPcPsPc8SOK8pFQq00n9NW9G+wxyYQvG4=`.
The locked nginx NixOS module's `ExecStart` uses
`${cfg.package}/bin/nginx -c ...`; source inspection found no local nginx
ExecStart or package override redirecting execution. No separate mainline
consumer was found.

Prepared command, from this repository root (not executed):

```sh
nix develop -c confctl deploy --one-by-one '{cz.vpsfree/containers/discourse,cz.vpsfree/containers/int.blog,cz.vpsfree/containers/int.kb,cz.vpsfree/containers/int.munin,cz.vpsfree/containers/int.utils,cz.vpsfree/containers/int.vpsfbot,cz.vpsfree/containers/int.web,cz.vpsfree/containers/prg/proxy,cz.vpsfree/machines/aitherdev,cz.vpsfree/machines/brq/apu,cz.vpsfree/machines/build,cz.vpsfree/machines/em1,cz.vpsfree/machines/prg/apu,cz.vpsfree/vpsadmin/int.vpsadmin-webui1,cz.vpsfree/vpsadmin/int.webui-dev,cz.vpsfree/vpsadmin/int.webui1,cz.vpsfree/vpsadmin/int.webui2}' switch
```

This builds selected systems first, then switches one at a time. Brace selector
order is not a guaranteed deployment order. Deployment authorization and machine
ownership are separate from this prepared command.

## Other consumers and exclusions

The following 34 managed stable-input consumers evaluate nginx disabled, so they
are not targets for this nginx fix (they still receive the wider input update):

```text
cz.vpsfree/containers/brq/int.ns1
cz.vpsfree/containers/brq/ns1
cz.vpsfree/containers/brq/ns2
cz.vpsfree/containers/int.paste
cz.vpsfree/containers/int.rubygems
cz.vpsfree/containers/mx2
cz.vpsfree/containers/ns0
cz.vpsfree/containers/ns1
cz.vpsfree/containers/ns2
cz.vpsfree/containers/ns3
cz.vpsfree/containers/ns4
cz.vpsfree/containers/prg/int.alerts1
cz.vpsfree/containers/prg/int.alerts2
cz.vpsfree/containers/prg/int.grafana
cz.vpsfree/containers/prg/int.log
cz.vpsfree/containers/prg/int.mon1
cz.vpsfree/containers/prg/int.mon2
cz.vpsfree/containers/prg/int.ns1
cz.vpsfree/containers/prg/ns1
cz.vpsfree/containers/prg/ns2
cz.vpsfree/containers/prg/tor-relay
cz.vpsfree/machines/brq/apu#nixos-live
cz.vpsfree/machines/build#nixos-live
cz.vpsfree/machines/nixos-live
cz.vpsfree/machines/prg/apu#nixos-live
cz.vpsfree/machines/prg/int.vpn
cz.vpsfree/vpsadmin/int.api1
cz.vpsfree/vpsadmin/int.api2
cz.vpsfree/vpsadmin/int.db
cz.vpsfree/vpsadmin/int.rabbitmq1
cz.vpsfree/vpsadmin/int.rabbitmq2
cz.vpsfree/vpsadmin/int.rabbitmq3
cz.vpsfree/vpsadmin/int.redis1
cz.vpsfree/vpsadmin/int.vpsadmin1
```

The other 52 managed entries are vpsAdminOS nodes using unchanged staging (8) or
production (44) nixpkgs roles, outside this one-time stable input update. Seven
unmanaged org.vpsadminos reference entries are excluded: int.cache,
int.gh-runner1, int.gh-runner2, int.images, int.iso, int.www and proxy. Package B
owns that repository's deployment report, so this list does not duplicate it.

Gaps: no fleet build, VM test, full-fleet assertions, activation, remote runtime
inspection or rollback certification. Targeted package/source inventory and one
normal exported system derivation are proven. No further checks are needed by
the accepted bounded brief. No migration or application interface change exists.

Package A is ready for lead acceptance. Exact final source head remains
`828c390c7e1857f11522933977afd852634b85f8`; no further application or Git mutation
is pending. Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-18-nixos-channel-update/
