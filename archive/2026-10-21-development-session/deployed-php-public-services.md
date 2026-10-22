# Public-service built PHP artifact inspection

Checked at 2026-10-21T08:23:59.438433+00:00. Owner: implementer0.

## Result: actual build contents unavailable locally

The exact-head generated FPM artifacts are absent from this local Nix store.
No built-content PASS is claimed. Earlier effective configuration evaluation
does not substitute for reading realized files. No source/Git mutation, build,
deployment, service restart, HTTP/PHP execution, or remote write was performed.

Session identity and both environment values match
`2026-10-21-development-session` and `/home/aither/workspace/ai/vpsfree.cz`.

## Exact-head artifact inventory

Existing evidence binds revision `38687a8438a6e75b20a1924fb65d060a05217b06`
and snapshot `/nix/store/2q5ar7wpdivcz06vvibqc8bc7k6rvnm2-source`.
Each expected `-c`/`-y` path below was checked with `Path.is_file()`.
All ten returned false; their contents and scan-chain cannot be asserted.

| Machine / pool | Generated pool INI (`-c`) | Generated FPM configuration (`-y`) |
| --- | --- | --- |
| `cz.vpsfree/containers/int.blog` / `wordpress-blog.vpsfree.cz` | `/nix/store/2a3mdrhn3ddxs8gwv5g34xzrx3lk8spf-php.ini` — absent | `/nix/store/l7h7fa3bxncfipdngk23ffgdx8mbmh15-phpfpm-wordpress-blog.vpsfree.cz.conf` — absent |
| `cz.vpsfree/containers/int.kb` / `dokuwiki-kb.vpsfree.cz` | `/nix/store/lxi2pq1mbs7pm8rinzdk9jfxp5dbi1ay-php.ini` — absent | `/nix/store/gcs9vaq41iri3g9ifjl86ll90aq7ldvd-phpfpm-dokuwiki-kb.vpsfree.cz.conf` — absent |
| `cz.vpsfree/containers/int.kb` / `dokuwiki-kb.vpsfree.org` | `/nix/store/jc9az920r46391pz2far8s4nv61y20my-php.ini` — absent | `/nix/store/794cvch0k2fhd5016gnpwzwvr2i731mq-phpfpm-dokuwiki-kb.vpsfree.org.conf` — absent |
| `cz.vpsfree/containers/int.utils` / `adminer` | `/nix/store/33w2i4xqvkdizplh3zs9l7mkh6c3xd3p-php.ini` — absent | `/nix/store/mc22y89ix6ayb916whf8is4533y24x8b-phpfpm-adminer.conf` — absent |
| `cz.vpsfree/containers/int.web` / `foto` | Omitted by earlier no-IFD projection | Omitted by earlier no-IFD projection |
| `cz.vpsfree/containers/int.web` / `vpsfree` | `/nix/store/a0128c16spzsgnxgcmf1z21fq44ghsx9-php.ini` — absent | `/nix/store/ygq41cc1nzl874sxsnnsp2rszzsznjpv-phpfpm-vpsfree.conf` — absent |

Foto: local `/nix/store/*-phpfpm-foto.conf` and
`/nix/store/*-unit-phpfpm-foto.service` searches returned no realized candidates.
A bounded offline/read-only/no-IFD attempt to resolve its exact ExecStart
refused because the helper-generated evaluator store path was not valid.
Nothing was built or fetched by that attempt.

## SSH and runtime limitations

Pinned `nix develop -c confctl ls --output name,host.target,host.fqdn`
confirmed the four targets: blog `172.16.8.4`, kb `kb.int.vpsfree.cz`,
utils `utils.int.vpsfree.cz`, web `web.int.vpsfree.cz`.
The repository IPs for the last three are `172.16.9.179`, `172.16.9.156`,
and `172.16.9.28`. Initial bounded root SSH reads to all four IPs failed
at host-key verification before any remote artifact output. No host-key
checking or known-hosts state was changed; further SSH investigation stopped
when the lead selected local built-file inspection.

No `/run/current-system`, loaded unit, running master, wrapper scan directory,
generated FPM include, or runtime value was verified for these four hosts.
The concrete missing evidence is access to the realized outputs selected by
the user deployment. Reading those outputs is required before a built-content
or deployed-service claim can be made.
