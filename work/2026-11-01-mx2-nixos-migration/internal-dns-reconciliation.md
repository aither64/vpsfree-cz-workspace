# Internal mail DNS source reconciliation

User direction, relayed by lead: “you can fixup the internal zone if the mail
records do not correspond to the public DNS -- the public DNS is correct, the
internal is probably stale”. This authorizes source reconciliation. No live DNS
reload, deployment or default-branch integration was performed.

Implementer1 verified the exact session identity and retained `workspace_write`,
`gpt-6.1-sol` / `xhigh` settings. Exclusive source/Git ownership was assigned for
this bounded package; implementer0 resumes ownership after the commit report.

## Result and provenance

- Worktree: `worktrees/2026-11-01-mx2-nixos-migration/vpsfree-cz-configuration`.
- Branch: `2026-11-01-mx2-nixos-migration`.
- Parent: `e4c1ac0c5ae7426fb019b79ba936b30ce63e6e6c`.
- DNS commit: `655851e595c57efbedb45588f0cca28509f00907`,
  `internal-dns: align mail records with public DNS`.
- Only source path: `configs/internal-dns/zone.vpsfree.cz.`;
  9 insertions, 4 deletions. Post-commit worktree/index clean, branch ahead one
  commit of its existing published feature. No rebase, ref rewrite, push or
  default integration in this package; original refs remain intact.

Added the missing apex MX pair and `prasiatko-mail` A/AAAA records. Replaced
the single lists MX with the public primary/backup pair. Corrected `mx2` AAAA
from `2a00:cb40:2::1:95` to `2a03:3b40:100::1:95`, and `mx1` AAAA from
`2a01:430:17:1::33` to `2a03:3b40:fe:1c3::1`. The latter is the existing
`mail` alias target and a directly confirmed public mail-host mismatch; the
alias itself is preserved. SOA serial advances from `2026093000` to
`2026110200`, following the repository's date-plus-counter convention.

No internal `vpsfree.org` zone exists. The shared module serves only
`vpsfree.cz`, `vpsadminos.org` and `snajpadev.int`; it recursively resolves
other zones. The earlier configured-resolver observation already returned the
public `vpsfree.org` MX pair, so no additional zone was introduced.

## User-authoritative public DNS evidence

Requeried 2026-11-02 15:44:32 UTC using public recursive resolver
`1.1.1.1`, UDP53. All replies were NOERROR. Commands used:

```text
dig @1.1.1.1 +noall +comments +answer +stats +nocookie +time=3 +tries=1 MX DOMAIN
dig @1.1.1.1 +noall +comments +answer +stats +nocookie +time=3 +tries=1 TYPE HOST
```

`DOMAIN` was each of the three rows below; `TYPE` was A/AAAA for each exchanger
and for the existing mail alias target `mx1`. Observed TTLs are retained here;
the internal zone keeps its established default one-hour TTL.

| Owner | Type | Public value(s) | Observed TTL |
| --- | --- | --- | --- |
| `vpsfree.cz` | MX | 10 `prasiatko-mail.vpsfree.cz.`, 15 `mx2.vpsfree.cz.` | 3600 |
| `lists.vpsfree.cz` | MX | 10 `prasiatko-mail.vpsfree.cz.`, 15 `mx2.vpsfree.cz.` | 3600 |
| `vpsfree.org` | MX | 10 `prasiatko-mail.vpsfree.cz.`, 15 `mx2.vpsfree.cz.` | 1800 |
| `prasiatko-mail.vpsfree.cz` | A | `37.205.15.53` | 3600 |
| `prasiatko-mail.vpsfree.cz` | AAAA | `2a03:3b40:fe:1c3::1` | 3600 |
| `mx2.vpsfree.cz` | A | `37.205.11.114` | 3600 |
| `mx2.vpsfree.cz` | AAAA | `2a03:3b40:100::1:95` | 3600 |
| `mx1.vpsfree.cz` | A | `37.205.15.53` | 3600 |
| `mx1.vpsfree.cz` | AAAA | `2a03:3b40:fe:1c3::1` | 3600 |

## Quick checks and consumer inventory

Checks ran in `nix develop --no-write-lock-file --command ...` without
refreshing inputs. BIND tools report version 9.20.29. For each consumer's
`@fqdn@` substitution, both original and changed zones passed:

```text
named-checkzone vpsfree.cz. TEMP_ZONE
named-compilezone -q -s full -o TEMP_CANONICAL vpsfree.cz. TEMP_ZONE
```

The inline verification driver compared BIND-canonical RRsets against the exact
parent blob. Exactly six intended RRsets plus the SOA changed: apex/list MX,
primary A/AAAA, mx1/mx2 AAAA. All other RRsets were equal, including existing
mx1/mx2 A records and `mail CNAME mx1.vpsfree.cz.`. Each variant had
482 original and 485 final RRsets; the expected mail values match the public
observations. This also checks expanded `$GENERATE` records without changing
their source. Disposable parser inputs/output were removed by their temporary
directory owner. `git diff --check` passed before and after the commit.

`confctl ls` confirmed all four exact consumers below. Each imports
`configs/internal-dns`; the FQDN controls only the SOA server substitution.

| Exact confctl name | FQDN |
| --- | --- |
| `cz.vpsfree/containers/brq/int.ns1` | `ns1.int.brq.vpsfree.cz` |
| `cz.vpsfree/containers/prg/int.ns1` | `ns1.int.prg.vpsfree.cz` |
| `cz.vpsfree/containers/prg/int.mon1` | `mon1.int.prg.vpsfree.cz` |
| `cz.vpsfree/containers/prg/int.mon2` | `mon2.int.prg.vpsfree.cz` |

Installed executable pre-commit/commit-msg hooks were verified as Overcommit.
The focused commit used a temporary message file and the repository environment.
Nixfmt pre-commit and all commit-msg hooks passed. TextWidth warned about two
body lines over 72 columns; all lines satisfy the repository's 80-column limit.
Only the assigned zone was staged.

## Deferred joint review and targeted builds

No long build ran in this package. Lead owns joint final review with the main
SMTP-test package and fresh watcher-run builds afterward. Exact targeted build
commands from the repository root are:

```sh
nix develop --no-write-lock-file --command confctl build cz.vpsfree/containers/brq/int.ns1
nix develop --no-write-lock-file --command confctl build cz.vpsfree/containers/prg/int.ns1
nix develop --no-write-lock-file --command confctl build cz.vpsfree/containers/prg/int.mon1
nix develop --no-write-lock-file --command confctl build cz.vpsfree/containers/prg/int.mon2
```

Source correction does not change the currently running internal DNS or resolve
the access/SMTP policy limits in [primary-baseline.md](primary-baseline.md).
It changes no mail queue/state format. Once separately approved and deployed,
internal clients will use the public mail destinations and current IPv6
addresses. A source rollback after any deployment must use a fresh higher SOA
serial so caches/secondaries accept it; no deployment or rollback was attempted.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-mx2-nixos-migration/
