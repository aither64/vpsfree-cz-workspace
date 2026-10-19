# NixOS container flake update: DNS and TLS findings

Investigated 2026-10-14. This is an investigation record, not a production
change or a claim to have reproduced the original Nix TLS failure.

## Conclusion

The vpsAdminOS NixOS compatibility module supplies static nameservers. Upstream
NixOS 26.05 writes `domain` into resolvconf's static input whenever both
`networking.nameservers` and `networking.domain` are set. That explains why
the container can acquire the domain directive while another NixOS machine
using DHCP nameservers does not. The upstream option documentation says the
domain is not configured for DNS resolution, which disagrees with this path.

The module does not define domain/search paths or override NSS lookup behavior.
The osctld resolver writer emits nameservers and `options edns0`, not a domain.
There is no evidence here of a container host network or TLS defect.

Follow-up clarification: vpsAdminOS does not implicitly choose a domain for
the NixOS guest. Searches of the compatibility modules, NixOS image builders,
image configuration and osctld distribution configuration found no assignment
to `networking.domain` or `networking.search`. The first reporter explicitly
set `networking.domain` themselves. Static nameservers supplied by the
compatibility module expose upstream NixOS's handling of that user-supplied
value; this is not evidence of a vpsAdminOS defect.

Confctl does provide a domain default when its machine metadata specifies one:
[host.nix](https://github.com/vpsfreecz/confctl/blob/cc40679d267165aecfa569128438bb55fe910268/nix/modules/confctl/host.nix#L10-L12)
sets `networking.domain = lib.mkDefault host.fullDomain`. Its
[machine options](https://github.com/vpsfreecz/confctl/blob/cc40679d267165aecfa569128438bb55fe910268/nix/modules/cluster/default.nix#L358-L371)
derive `fullDomain` from an optional location plus the configured domain.
That is consistent with the requesting operator's domain settings, although
their individual machine configuration was not inspected. The forum contains
no evidence that these users use confctl. Confctl reference inspected:
`cc40679d267165aecfa569128438bb55fe910268`, local `origin/master`.

`domain` is a legacy one-entry search list. The reported second domain has
wildcard AAAA answers, while `api.github.com` currently has no AAAA answer.
An IPv6-only lookup can therefore fall back to
`api.github.com.panpanika.eu`. A TLS connection to a wildcard destination with
SNI `api.github.com` can be rejected by that destination. The first post's
Cloudflare addresses are consistent with that explanation, but its actual
domain is anonymized, so its DNS and TLS endpoint cannot be checked.

`getent hosts` tries IPv6 first using `gethostbyname2(AF_INET6)` and only tries
IPv4 if that call fails. A wildcard AAAA result makes it succeed before the
correct IPv4 address is considered. This result alone does not show what
Nix or curl connects to: normal `getaddrinfo(AF_UNSPEC)` can use the valid A
answer for the original name without performing search fallback.

## Source evidence

- [Discussion, posts 1–3](https://discourse.vpsfree.cz/t/nixos-flake-update-ssl-connect-error/370):
  Nix fails with curl code 35/handshake failure, ordinary curl succeeds,
  removing `networking.domain` reportedly fixes it, and the third post reports
  a suffixed AAAA result despite `networking.search = []`.
- vpsAdminOS reference `1150e37b1cc997b1728f2fda806a3433ef55b798`, fetched
  `origin/staging` during the investigation:
  [static nameservers](https://github.com/vpsfreecz/vpsadminos/blob/1150e37b1cc997b1728f2fda806a3433ef55b798/os/lib/nixos-container/stable/vpsadminos-26.05.nix#L24-L32)
  and
  [guest-owned resolver configuration](https://github.com/vpsfreecz/vpsadminos/blob/1150e37b1cc997b1728f2fda806a3433ef55b798/os/lib/nixos-container/stable/vpsadminos-26.05.nix#L118-L122).
- [osctld resolver writer](https://github.com/vpsfreecz/vpsadminos/blob/1150e37b1cc997b1728f2fda806a3433ef55b798/osctld/lib/osctld/dist_config/configurator.rb#L97-L117)
  and its NixOS distribution subclass do not add a domain directive.
- NixOS `nixos-26.05` resolved to
  `7993f34ee47e28a3d607a525aadc6c94b73be728` during inspection:
  [documented domain semantics](https://github.com/NixOS/nixpkgs/blob/7993f34ee47e28a3d607a525aadc6c94b73be728/nixos/modules/tasks/network-interfaces.nix#L709-L733)
  and
  [conditional static domain generation](https://github.com/NixOS/nixpkgs/blob/7993f34ee47e28a3d607a525aadc6c94b73be728/nixos/modules/tasks/network-interfaces.nix#L1856-L1867).
- [resolv.conf manual](https://man7.org/linux/man-pages/man5/resolv.conf.5.html):
  domain/search, default `ndots:1`, and process-local `LOCALDOMAIN` override.
  Increasing dots above that threshold changes initial query ordering; the
  default still permits fallback after an unsuccessful absolute lookup.
- [glibc getent source](https://github.com/bminor/glibc/blob/master/nss/getent.c):
  `hosts_keys` uses IPv6-first `gethostbyname2`; `ahosts_keys` uses
  `getaddrinfo(AF_UNSPEC)`. Inspected current upstream source.
- [Openresolv parser](https://github.com/NetworkConfiguration/openresolv/blob/master/resolvconf.in)
  and [libc writer](https://github.com/NetworkConfiguration/openresolv/blob/master/libc.in)
  convert a domain into a search entry and omit a redundant `search` line when
  it equals the domain. Thus an empty NixOS search option does not prevent
  implicit search from `domain`.

## Bounded local checks

No live resolver file was edited. Glibc's process-local `LOCALDOMAIN` override
was used with the local host's existing recursive DNS servers.

| Check | Observed result |
| --- | --- |
| `dig api.github.com A` | `140.82.121.5` |
| `dig api.github.com AAAA` | `NOERROR`, zero answers |
| `dig api.github.com.panpanika.eu A` | `37.205.14.125` |
| `dig api.github.com.panpanika.eu AAAA` | `2a03:3b40:fe:8d::` |
| `dig probe-20261014.panpanika.eu AAAA` | Same IPv6 address; consistent with wildcard DNS |
| `LOCALDOMAIN=panpanika.eu getent hosts api.github.com` | Suffixed wildcard IPv6 address |
| `LOCALDOMAIN=panpanika.eu getent ahosts api.github.com` | Original GitHub IPv4 address |
| `LOCALDOMAIN=panpanika.eu getent ahostsv6 api.github.com` | Suffixed wildcard IPv6 address |
| Python `getaddrinfo`, AF_UNSPEC / AF_INET / AF_INET6 under same override | GitHub IPv4 / GitHub IPv4 / wildcard IPv6 |
| `LOCALDOMAIN=panpanika.eu getent hosts api.github.com.` | GitHub IPv4; terminal dot prevents search fallback |
| `LOCALDOMAIN=. getent hosts api.github.com` | GitHub IPv4; root-only search avoids the wildcard suffix |
| Normal and `-4` curl under same override | HTTP 200, remote IP `140.82.121.5` |
| `-6` curl under same override | Connection failure, not a reproduced TLS failure |
| Nix `store prefetch-file` under same override, API rate_limit and original nixpkgs commits endpoint | Both succeeded within one second |

Local versions: glibc 2.42, Nix 2.34.8, curl 8.22.0, OpenSSL 3.6.5.
The local Nix and curl binaries use the same libcurl store output and no
c-ares library was present in their `ldd` outputs. This does not establish
the affected user's library versions or resolver backend.

## Limits and practical advice

The original Nix-only error was not reproduced. Removing the domain reportedly
changes the outcome, and the wildcard DNS explains the suffixed IPv6 result,
but attributing Nix's actual connection requires its effective settings and
runtime. Possibilities to inspect include address-family selection, resolver
implementation/version, `ndots`, root versus user environment/binary, and
differences in DNS/NSS/cache state. These are diagnostic possibilities, not
established causes.

Useful comparisons on the affected VPS are `getent ahosts api.github.com`,
`getent ahostsv4 api.github.com`, `getent ahostsv6 api.github.com`, the complete
`/etc/resolv.conf` and `hosts:` NSS line, verbose curl's connected IP, and Nix
and curl versions (including the Nix binary selected under sudo).

A normal domain/search entry is not sufficient to cause the problem. Without
wildcard DNS, the suffixed AAAA lookup normally fails and IPv4 lookup can find
the genuine GitHub address. The actual resolver backend and supported address
families also affect the result.

If retaining `networking.domain` for the system FQDN is desirable, an explicit
safe search list avoids searching a wildcarded public domain. With ordinary
NixOS openresolv management, `networking.search = [ "." ];` produces a later
`search .` line that overrides the one-entry domain search. This configuration
recommendation is source-supported; no NixOS rebuild or deployment was done.
It deliberately disables local suffix expansion, so assess short-name needs.
Removing an unintended wildcard or using a dedicated internal search domain
is another way to avoid these answers. Merely setting `networking.search = []`
or retaining default `ndots:1` does not prevent the IPv6 fallback demonstrated
above.

No owning-project docs or code were changed: the deliverable is investigation
findings with an unresolved environment-specific Nix detail. Independent final
review does not apply to findings/tracking alone. No merge or deployment is
proposed, and the session remains open.
