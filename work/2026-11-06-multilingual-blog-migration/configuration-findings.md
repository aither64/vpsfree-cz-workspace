# Blog and Discourse configuration discovery

Bounded read-only investigation by implementer0, 2026-11-06. This describes
locally retained configuration, not verified deployed state. No fetch, branch,
configuration edit, build, deployment, machine connection or secret-file read.

## Revision evidence

Only `repos/vpsfree-cz-configuration.git` was inspected. Its symbolic `HEAD` is
`refs/heads/master` at `86e19685313270d88e4db30038c056ce4b807abd`.
`refs/remotes/origin/HEAD` points to `refs/remotes/origin/master`, retained at
`85b38f1cd07d6b3a0fde3eefd32258f747e757e5`. All findings below use that retained
remote default. Fresh remote default and runtime revisions remain unknown.
Of the inspected service/proxy/web/module/input paths, the local/default-head
comparison differed only in `flake.lock`; package inputs must remain tied to the
stated inspected revision. Repository `AGENTS.md` and `README.md` were read.

## Main touchpoints

Paths are relative to the configuration repository at the retained default above.

| Path | Inspected configuration |
| --- | --- |
| `cluster/cz.vpsfree/containers/int.blog/wordpress.nix` | Nginx WordPress backend; MariaDB Unix socket; persistent uploads `/var/lib/wordpress/blog.vpsfree.cz/uploads`; fonts beneath uploads; immutable code and disabled in-app file modifications. HTTP/80 accepts only the metadata-resolved Prague proxy IPv4; TLS and ACME stay at the proxy. Trusted client header is `X-Real-IP` from that exact proxy. |
| `cluster/cz.vpsfree/containers/int.blog/packages/default.nix` | WordPress **7.1.2** and Czech core translation; Akismet 5.7, Disable Gutenberg 3.3.2, Open Graph plugin 3.4.0; local Flat theme version 6.6.6 plus nixpkgs Twenty Twenty-Five. Plugins/translations are fixed-hash downloads; local theme and policy are packaged with the code. |
| `cluster/cz.vpsfree/containers/int.blog/module.nix` | Target `cz.vpsfree/containers/int.blog`, container 29942, internal IPv4 `172.16.8.4`; channels `nixos-stable` and `os-staging`. Health checks require nginx, MySQL, WordPress PHP-FPM/init, and a local HTTP request with blog Host and forwarded HTTPS headers. Static conversion must replace the WordPress-specific checks. |
| `cluster/cz.vpsfree/containers/prg/proxy/config.nix` | `blog.vpsfree.cz` virtual host, lines 287–291: ACME, forced HTTPS, all paths proxied to metadata-resolved blog backend on port 80. Retaining the existing backend leaves this public routing usable. |
| `cluster/cz.vpsfree/containers/discourse/config.nix` | Separate `services.discourse` service at `discourse.vpsfree.cz`, own ACME, PostgreSQL **15**, GitHub/vpsAdmin OAuth, custom OAuth signup-policy plugin, inbound and outbound mail. Discourse package version is inherited from nixpkgs and was not resolved. No blog embedding/comment integration was found here. |
| `cluster/cz.vpsfree/containers/discourse/module.nix` | Target `cz.vpsfree/containers/discourse`, container 24920, IPv4 `37.205.13.116`, same channel names; health checks require Discourse, Postfix and PostgreSQL. |

The blog `config.nix` imports `wordpress.nix` and sets `system.stateVersion =
"26.05"`; Discourse sets `"23.05"`. These are compatibility state versions,
not application-version evidence. `flake.nix` selects `nixos-26.05` for
`nixpkgsStable`; its retained lock revision is
`718f670e845328e9c2cecdd832835712b2cbd065`.

## Existing build and source conventions

`flake.nix:21` declares the non-flake `vpsfreeWeb` input from
`github:vpsfreecz/web`; `flake.lock` pins it to
`307635a96bc3532af51ff5d08206d920704eee00`.
`modules/services/vpsfree-web.nix` uses that input, a `pkgs.runCommand` copy,
and the source's Nix build to create an immutable web output, then points nginx
at `${web}/${language}/`. Its PHP/SSI handling and language-specific directory
layout are specific to the main website; they need not become a static-blog
interface. `configs/webs/default.nix` consumes the module for Czech/English web
hosts and development roots. The README specifies pinned `nix develop` and
`confctl build <machine>`; input changes use `confctl inputs`, not hand-edited
locks. No public blog source repository or Hugo/Zola/Jekyll integration was
found in the bounded inspected Nix/input references. This is not proof that no
external repository exists.

`cluster/cz.vpsfree/containers/int.vpsfbot/config.nix:157` configures the IRC
bot to poll `https://blog.vpsfree.cz/feed/`; preserve that endpoint or verify an
explicit redirect and feed-compatibility plan.

## Proposed integration constraints for architect consideration

These are design inputs, not an approved implementation or executed rollout.

1. Build a pinned immutable static artifact from the selected source in Nix,
   point a backend nginx vhost at its output, and retain proxy-only networking
   and public HTTPS routing where practical. The source repo and generator
   contract still need selection; the existing main-web input is an example,
   not evidence that it owns the blog.
2. Validate exported articles, legacy URLs, media and `/feed/` before cutover.
   WordPress database/uploads are mutable source state; static generation does
   not itself migrate or preserve them. Establish a consistent export and a
   content-write cutoff before publication.
3. Prepare and verify the static artifact first, then change backend serving
   and health checks together. Only change public proxy configuration if the
   chosen hosting target changes. Discourse needs no change for static hosting
   alone; any comment/embed/API settings require a separate concrete brief and
   runtime-aware verification.
4. Retain the old system generation and original database/uploads unchanged
   through the rollback window. Reverting nginx/code is insufficient if those
   data were removed or modified incompatibly. Avoid coupling this cutover to
   Discourse or PostgreSQL upgrades. Runtime backups, database schema state,
   category/embed settings and actual versions were not inspected.

No project source or coordination plan/state/index was edited; this findings
file is the sole owned output and is uncommitted. Lead owns acceptance and any
tracking updates; architect0 owns design decisions.
