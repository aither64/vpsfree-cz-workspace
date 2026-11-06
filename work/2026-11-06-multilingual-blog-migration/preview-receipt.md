# Reviewed synthetic VPN preview

Running and locally verified at 2026-11-06 21:50 UTC. Final clean source head:
`0354dac281978867ea8c1553b092ce19bccb5ccd`. No source push, default initialization,
production serving/topic changes or firewall edits occurred.

## Access and registered service

- Czech: <http://aitherdev.int.vpsfree.cz:4567/>.
- English: <http://aitherdev.int.vpsfree.cz:4567/en/>.
- Paired synthetic articles:
  <http://aitherdev.int.vpsfree.cz:4567/synteticky-priklad_1/> and
  <http://aitherdev.int.vpsfree.cz:4567/synthetic-example_1/>.
- IP fallback: <http://172.16.106.40:4567/>. Article language links use the
  advertised hostname, so VPN DNS must resolve it correctly.
- Registry ID `6d35d71b-dca8-43dc-9b68-5f4f0b37af7d`; service
  `blog-vpn-preview`, ID `70dd830c-701f-48ba-9116-341eae1edd67`.
- Exact working directory:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog`.
- Registered through `dev-session service run` with command
  `/run/current-system/sw/bin/nix develop -c bin/preview --vpn --fixtures`.
  Native Hugo then receives the exact bind, port and explicit advertised
  `--baseURL`. Only isolated synthetic drafts are selected.
- `ss -ltnp 'sport = :4567'` showed exactly one listener,
  `172.16.106.40:4567`, Hugo PID `3179234`; no wildcard or second language port.
- Service list reports this service running. Original loopback service
  `b0930238-6cc2-4cc0-b511-e1d36c306067` remains running and untouched.
  Initial faulty VPN service `7b1eef5f-3bc4-47b9-8dfd-170e43541a6b` was stopped
  with the lead's explicit bounded repair authorization and is verified retired.
  No session lifecycle action was taken.

## Runtime and artifact checks

`nix develop -c bin/check --vpn` passed at the final clean head. It covers the
existing production/loopback render contracts, fixture route uniqueness, paired
links, real draft selection, isolation/reproducibility and live VPN pages/feeds.

Additional HTTP checks used `curl --noproxy '*' --resolve
aitherdev.int.vpsfree.cz:4567:172.16.106.40`, avoiding the host's local loopback
alias. Both homes, both paired articles, `/feed/` and `/en/feed/` returned 200
without `Location` redirects. Feeds had `application/rss+xml`, parseable RSS and
correct advertised self URLs. HTML had advertised host canonicals and paired
links, no localhost URLs, no script/iframe or Discourse embed, and noindex/nofollow.
Configured internal DNS servers independently resolve the hostname to
`172.16.106.40`; local `/etc/hosts` instead resolves it to `127.0.0.2`.

Final `nix build .#site --no-link --print-out-paths` passed in seconds:

- Artifact: `/nix/store/24k031sa1wzacz1jid198af9vlflgbsg-vpsfree-blog-0`.
- Derivation: `/nix/store/q9aa39sacmg9pahn9pl9qxkc9fpbsf66-vpsfree-blog-0.drv`.
- Source: `/nix/store/8pbnhn68d6n2qmr5830kzw23dlklyjyj-source`.
- Source NAR: `sha256-Q5n+NHSzap6H2U50ZFCVnlH9wC0Ha/BIq48Tq4AL4Xc=`.
- `metadata.json` names final source revision
  `0354dac281978867ea8c1553b092ce19bccb5ccd`; all 12 served-file SHA-256 hashes
  were verified, with separate `cs/` and `en/` production document roots.
- Metadata SHA-256:
  `39ce53dd93f6b5533855a05d8c2bec5663bf315833673eef8d5461c4199852c9`.
- Complete external source/input graph is `flake.lock`: one Nixpkgs node,
  revision `f3a73bcf5d1c5b75a66cf35a48957e30d41d647a`, NAR
  `sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=`. This fixes Hugo
  `0.167.0` and Python. Lock SHA-256:
  `865a3c07a35f43f024ce7c01614be82cb795707edac8e27092bdbba42519cd75`.

The VPN preview serves native Hugo output from the reviewed source; it is not
the production artifact's two-host layout. English homepage/feed use `/en/`;
explicit English article paths remain at the shared origin root. No archive or
production RSS item compatibility is claimed. This proves local listener/HTTP
behavior; no independent external VPN-client path was available to test.

## Review and consolidated history

Reviewer0 accepted the complete empty-tree-to-`20b307e` branch with no findings.
Live launch then exposed Hugo server's implicit localhost base-URL override,
which static rendering did not reproduce. Lead inspected and accepted the narrow
two-file correction at `6a6dd25860415145bd6d6466228be83b81331bf9`: explicit
`--baseURL` in VPN mode plus live advertised-link assertions. Scope and supported
interfaces are unchanged; lead retained initial review under the narrow-fix rule.

The unpublished fix was folded into owning P history before final build/launch:

| Logical commit | Reviewed old | Final |
| --- | --- | --- |
| B0 scaffold | `04b6ecc6dd286a4932910c1a8da12a5d28be1df8` | unchanged |
| P VPN preview | `81b937c62faf6adcb50480bd2d38bab35677ce76` | `e0d37977bc19c8ad9d650658292b6e026212cfcd` |
| D0 authoring docs | `20b307e2b9197c99f185f3633915ba03ad9105a3` | `0354dac281978867ea8c1553b092ce19bccb5ccd` |

`git range-diff 04b6ecc..6a6dd258 04b6ecc..0354dac` marks D0 patch-equivalent
(`=`), P changed only by the approved two-file correction, and the standalone fix
removed into P. `git diff 6a6dd258 0354dac` is empty, proving the consolidation
preserved the corrected final tree. Three logical commits remain; no migrations,
obsolete source streams, published-history rewrite or real content were added.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/>.
