# Internal blog DNS: prepared rollout receipt

Prepared by `implementer2` for package NB on 2026-11-06. Both exact system
builds passed. **Prepared, not deployed.** No machine/repository claim, SSH,
activation or default integration was performed by N/NB. User integration and
DNS activation approval remain outstanding. Lead owns those gates and execution.

## Reviewed source and targets

- Repository: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`;
  target default branch `master`.
- Feature: `2026-11-06-multilingual-blog-migration`.
- Reviewed base: `85b38f1cd07d6b3a0fde3eefd32258f747e757e5`.
- Reviewed and built final head: `133a94b62b3c2161c126fa347cab61ae1b819001`.
  Final worktree check after both builds was clean at this exact head.
- Source tree: `3fe62c7e8caeb47e89f6c7f14afe3cd52ac90ee5`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/vpsfree-cz-configuration`.
- Only source change: `configs/internal-dns/zone.vpsfree.cz.` adds
  `blog.int IN A 172.16.8.4`, inheriting TTL 3600, and advances SOA from
  `2026093000` to `2026110600`. Zone blob:
  `611e7e5cbbf7b922491c53c945e920800f1ac9d0`.
- Existing `blog.vpsfree.cz` CNAME remains unchanged. Container configuration
  identifies `blog.int.vpsfree.cz` at `172.16.8.4`; this is configured address
  evidence, not an independent live container identity check.
- Lead accepted N; reviewer0's independent final review of the complete one-commit
  range passed without findings. No migrations, obsolete intermediate commits,
  repeated pin streams or history rewrite. Published feature head was verified
  after N's push; no default integration is claimed.

| Exact confctl target | Host / machine alias | IPv4 | VPS | Prepared generation |
| --- | --- | --- | --- | --- |
| `cz.vpsfree/containers/prg/int.ns1` | `ns1.int.prg.vpsfree.cz` | `172.16.9.90` | 21850 | `2026-11-06--22-23-03` |
| `cz.vpsfree/containers/brq/int.ns1` | `ns1.int.brq.vpsfree.cz` | `172.19.9.90` | 21851 | `2026-11-06--22-24-04` |

These are independent BIND masters using `configs/internal-dns/default.nix`;
both require activation. That module materializes the shared zone with each
host's `@fqdn@`. This package changes no serving/proxy/TLS/Discourse/public
`.org` configuration.

## Complete source and input graph identity

The complete graph, including all 64 lock nodes and follows edges, is the
[committed flake.lock at the reviewed head](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/133a94b62b3c2161c126fa347cab61ae1b819001/flake.lock),
also present unchanged in the worktree. `flake.lock` Git blob:
`11219f0dcb5a4be6a6a2d813086461988953d2e8`; file SHA-256:
`9ed71bd9511c7b4e16e0fd9f4de483e0fe4cf54d2556e715392d28e6e60eacd8`.
`flake.nix` Git blob: `0dec4d0b2a649f2a47def3e29d0e6bad52070181`.
Use this complete graph with the source tree/head, not only the effective role
summary below, to reproduce the candidate.

Both target receipts agree on these effective inputs:

| Role / channel / root input | Exact revision | Source store path |
| --- | --- | --- |
| `nixpkgs` / `nixos-stable` / `nixpkgsStable` | `718f670e845328e9c2cecdd832835712b2cbd065` | `/nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source` |
| `vpsadminos` / `os-staging` / `vpsadminosOsStaging` | `dd188397abe37d0bc33f4c5dfb3605206ce5e326` | `/nix/store/cgk63vdx1wjl4ybd53abkd5aqyzc7sfa-source` |

Their locked NAR hashes are respectively
`sha256-Ee5BWo8sh3pGt70QUdRajnaginqFmWvrtdBc4gJzhks=` and
`sha256-LXZP7Ghcr+1obFUD+LjlJRO63qRo/GZtSve5AX5MZ7c=`.
Pinned confctl is `7bee58a52372b95c2198ce3f2a719807a3c2c66b`, NAR hash
`sha256-gh1tmTv8aAO1OA3HX2NEYnRALMK2i666Lxey8hxD0QM=`, executable
`/nix/store/j5wxvlxdnsh2gyc6wbjx8xxfllqp4zmv-confctl/bin/confctl`.

## Completed checks and build receipts

N's quick checks passed: materialized `named-checkzone` for both host FQDNs,
canonical zone dump showing the exact A record and unchanged public CNAME,
`git diff --check`, and actual Overcommit pre-commit/commit-message hooks.
No push CI is configured; the branch's workflow query returned no runs.

Lead's fresh Luna/low `dns_build_watcher` executed these commands from the
configuration worktree, with exit 0 for each; lead reported no operation running:

```sh
nix develop -c confctl build --yes cz.vpsfree/containers/prg/int.ns1
nix develop -c confctl build --yes cz.vpsfree/containers/brq/int.ns1
```

Prague took 77 seconds; Brno took 62 seconds. Logs:
[Prague](dns-build/prg-int-ns1.log), [Brno](dns-build/brq-int-ns1.log).
Generation timestamps are local CET (`+01:00`), as recorded in their JSON.

Authoritative local receipts relative to the worktree:

- `.confctl/generations/cz.vpsfree:containers:prg:int.ns1/2026-11-06--22-23-03/generation.json`,
  SHA-256 `36fe02cdeb9c5e404871902416439f4de725650c7db42be10e8e7d58d90eff43`.
- `.confctl/generations/cz.vpsfree:containers:brq:int.ns1/2026-11-06--22-24-04/generation.json`,
  SHA-256 `27ade1218098864e8cfa5c468e64211892259700203ed7fcc0f698cdbe4960a2`.

Exact Prague toplevel:
`/nix/store/51kr42zaswnw6zcxr6gkvk4rpa4d4a26-nixos-system-ns1-26.05.20261026.718f670`.

Exact Brno toplevel:
`/nix/store/gv95bq1xgzvixdq9xszp8p12y0fsmd0w-nixos-system-ns1-26.05.20261026.718f670`.

Both use auto-rollback helper:
`/nix/store/yl9vnin9wlv04cip0sqpkisk80xmccwh-auto-rollback.rb`.

Receipt `toplevel`, `auto_rollback`, `nixpkgs.input` and `vpsadminos.input`
symlinks were read after completion; all equal the JSON paths and all targets
exist. These are prepared store outputs, not deployed system/profile paths.
Ordinary build output stays in ignored `.confctl`; the source and lock remained
unchanged. No rebuild or additional integration test was run for this receipt.

## Proposed activation and recovery, not executed

After explicit approval, the lead must read current selected-package coordination
guidance, acquire the exact machine reservations and inspect live current
system/profile paths, previous recoverable generations, BIND state and SOA
serials. A built candidate does not establish the deployed baseline: stop for
unexpected system differences or a live/source serial at or above `2026110600`.
Any required source refresh returns to preparation/review outside machine claims.
Prepare closure copies before the activation window using ordinary confctl
`deploy --copy-only --generation GENERATION` for each exact target.

Proposed commands select the built generations explicitly; run from the same
worktree only under that later authorization and current machine ownership:

```sh
nix develop -c confctl deploy --yes --generation 2026-11-06--22-23-03 cz.vpsfree/containers/prg/int.ns1 dry-activate
nix develop -c confctl deploy --yes --generation 2026-11-06--22-24-04 cz.vpsfree/containers/brq/int.ns1 dry-activate
nix develop -c confctl deploy --yes --enable-auto-rollback --generation 2026-11-06--22-23-03 cz.vpsfree/containers/prg/int.ns1 switch
nix develop -c confctl deploy --yes --enable-auto-rollback --generation 2026-11-06--22-24-04 cz.vpsfree/containers/brq/int.ns1 switch
```

Verify the first switched master before proceeding to the second. Preserve
ordinary confctl health checks. Query both authoritative addresses directly:

```sh
dig +norecurse @172.16.9.90 blog.int.vpsfree.cz. A
dig +norecurse @172.16.9.90 vpsfree.cz. SOA
dig +norecurse @172.19.9.90 blog.int.vpsfree.cz. A
dig +norecurse @172.19.9.90 vpsfree.cz. SOA
```

Require authoritative (`aa`) NOERROR A answers `172.16.8.4`, TTL 3600, and SOA
serial `2026110600`; check unchanged `blog.vpsfree.cz` CNAME and existing
`health-checks/internal-dns.nix` apex/node/management queries on both masters.
Recursive clients may retain previous negative answers for up to one hour.
Record resulting exact deployed system/profile paths and observed effects here.

Before activation, capture usable previous generation paths and recovery
prerequisites. Preserve confctl auto-rollback. Removing the new DNS record after
publication requires a new serial greater than every published serial;
re-activating the old zone with its lower serial is not sufficient DNS recovery.
Build and check that correction, activate both masters under ownership and
verify the intended answers and serials again. This package has no database or
on-disk schema migration.

Integration is a separate approval: perform the fresh target/history check,
fast-forward merge/hooks, SSH push and remote ancestry proof inside the short
repository merge claim, then release it before records or other work. Before
machine release, reconcile all command effects and record authoritative ownership,
successful deployed effects and fresh remote proof that the complete deployed
lineage is integrated. No merge/activation/release evidence exists yet.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/>.
