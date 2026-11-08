# avting.cz BIND log evidence, 2026-11-05–08

Owner: implementer0, LOGS investigation package. Read-only production log access;
no application edits, commits, tests/builds, `rndc` commands or reloads performed.
The `rndc` operations below are historical events read from the logs.

## Finding

Both secondaries successfully acquired serial **2026110501 on November 5 at
17:38:36 +01:00**. The November 6 ns3 failures are real attempts to contact
`2a03:3b40:fe:2ef::1` and `37.205.14.125`, but they do not establish that the
served zone became stale or unavailable. The November 8 manual retransfer fetched
the **same serial**, with the same logged 48-record/3669-byte transfer size as
ns4's November 5 incoming transfer. It fetched from `37.205.11.85`; ns4's
simultaneous outgoing AXFR to `37.205.15.45` identifies the other secondary as
the source of that retransfer.

There are **no zone-specific lines on either host between November 6
06:36:35.805854 and November 8 15:42:21.309863**. In particular, no logged
successful transfer or up-to-date NOTIFY arrives in that interval to supersede
the failure in an event-driven status system. This supports the stale-last-event
explanation supplied by implementer1's source investigation. It does not prove
what happened during silent SOA refreshes, or prove the deployed application's
revision/behavior.

The duplicated IPv6 UI failures match **one BIND attempt**, with two distinct
failure messages for the same transfer handle. They are not duplicated raw
log lines. Parser/database confirmation belongs to the STATUS package.

## Source, time and collection boundaries

- SSH target: `root@log.int.prg.vpsfree.cz`; `hostname` returns `log`.
  Default `aither@…` authentication failed; the root connection succeeded.
- Authoritative source files:
  `/var/log/remote/cz.vpsfree/containers/ns3/log` and
  `/var/log/remote/cz.vpsfree/containers/ns4/log` on that host.
- Every cited event has an explicit **`+01:00`** offset in its retained timestamp.
  November 6 06:36:33 is 05:36:33 UTC; November 8 15:42:21 is 14:42:21 UTC.
  The UI times supplied in the request match the retained wall-clock times;
  the UI timezone setting was not independently read.
- Central server `date --iso-8601=seconds` returned
  `2026-11-08T15:54:45+01:00`; `/etc/localtime` resolves to
  `/nix/store/mkbbamycmw838fwxk21jz0nw3mhnmk16-tzdata-2026c/share/zoneinfo/Europe/Amsterdam`.
  Source-host timezone configuration and clock synchronization were not inspected.
- The current files begin at ns3 `2026-11-01T00:00:01.575111+01:00` and ns4
  `2026-11-01T00:00:07.021897+01:00`. Boundary capture on November 8 ended at
  ns3 `15:57:05.837448+01:00` and ns4 `15:56:40.232829+01:00`.
  Monthly files through `log-20261101` exist but were not scanned: the incident
  window is entirely in the current files.
- November 5 00h through November 8 15h has **88 hourly buckets per host,
  with at least one `named` message in each**. There is no whole-hour host or
  BIND collection gap evident. This is not proof against selective loss,
  suppression, forwarding problems or shorter gaps.
- The first zone extract contains 68 matches across both current November files,
  including November 1 context. It was obtained before the boundary capture.
  The files remain live; these are bounded extracts, not atomic snapshots.

## Incident chronology

All times below are November 2026, **UTC+01:00**. `ns3:N` / `ns4:N` refers to
the original file's line number in the captured extract.

| Time | Host and original lines | Observation |
| --- | --- | --- |
| Nov 1 21:18:19 / 21:18:26 | ns3:21239; ns4:53728 | Each loads serial `2026102901` after the earlier startup/reload context. |
| Nov 5 03:00:13.783–.785 | ns3:90440–90441; ns4:265241–265242 | Both receive requests from `2a03:3b40:fe:2ef::1` and `37.205.14.125` with `TSIG 2943-avting.cz: tsig verify failure (BADKEY)`. This is earlier and distinct from the later unreachable episode. It does not remain a universal blocker: ns3 subsequently succeeds with the named TSIG. |
| Nov 5 16:56–17:00, 17:23 | Both, control extract | Successful global reloads; see reload table below. |
| Nov 5 17:38:36.891732–.895170 | ns3:105824–105828 | ns3 starts a transfer, connects to `2a03:3b40:fe:2ef::1#53` with TSIG `2943-avting.cz`, transfers serial `2026110501`, logs success, then completion: 3 messages, 48 records, 4027 bytes. |
| Nov 5 17:38:36.897655–.909634 | ns4:279131–279139 | NOTIFY from `37.205.15.45` announces serial `2026110501`; ns4 connects to that address and transfers that serial successfully: 1 message, 48 records, 3669 bytes, `expire option 1814400`. |
| Nov 5 17:38:36.906836–.907293 | ns3:105832–105834 | ns3 serves `37.205.11.85` an AXFR-style IXFR at serial `2026110501`; the previous IXFR serial `2026102901` was unavailable in its journal. This outgoing transfer matches ns4's incoming transfer above. |
| Nov 5 17:38:36.912234 | ns3:105837 | NOTIFY from `37.205.11.85`: `zone is up to date`. This positive event precedes the later failures. |
| Nov 6 06:36:28.972079 | ns3:118442 | `refresh: retry limit for primary 2a03:3b40:fe:2ef::1#53 exceeded (source ::#0)`. |
| Nov 6 06:36:28.972306 | ns3:118443 | `zone avting.cz/IN: Transfer started.` |
| Nov 6 06:36:33.054695 | ns3:118444 | Handle `0x766445e93000`, IPv6 primary: `failed to connect: host unreachable`. |
| Nov 6 06:36:33.054917 | ns3:118445 | **Same handle and primary**, 222 μs later: `Transfer status: host unreachable`. This pair explains the two same-second IPv6 UI entries if each form is persisted separately. |
| Nov 6 06:36:33.054984 | ns3:118446 | Same attempt completes: 0 messages, 0 records, 0 bytes, 4.082 seconds, serial 0. This is not a successful serial-0 zone update. |
| Nov 6 06:36:35.805854 | ns3:118447 | `refresh: failure trying primary 37.205.14.125#53 (source 0.0.0.0#0): host unreachable`. This is a refresh failure, not a separately logged completed IPv4 AXFR. |
| Nov 6 06:36:35.805854–Nov 8 15:42:21.309863 | Both | **No `avting.cz` log matches.** No positive transfer/no-change NOTIFY, expiration, removal or zone-load message in this interval. |
| Nov 7 00:40–00:41 and 19:03–19:04 | Both | Six successful global reloads on each host, with no `avting.cz`-specific message. |
| Nov 8 15:42:21.309863 | ns3:175464 | Historical manual control command `retransfer avting.cz.` received. |
| Nov 8 15:42:21.313935–.322958 | ns3:175465–175469 | Connects to `37.205.11.85#53`, transfers **2026110501**, status success; 1 message, 48 records, 3669 bytes, `expire option 1813063`. No new TSIG label appears on this transfer. |
| Nov 8 15:42:21.319927–.320329 | ns4:356145–356146 | ns4 serves AXFR serial **2026110501** to client `37.205.15.45`, 1 message, 48 records, 3669 bytes. Both ends corroborate the manual ns3-to-ns4 transfer. |
| Nov 8 15:42:21.325716 | ns4:356150 | NOTIFY from `37.205.15.45`: `zone is up to date`. No new incoming ns4 transfer is needed/logged. |

Both hosts also log refused IPv6 NOTIFYs from the other secondary as
`non-primary` (Nov 1/5, and ns4 Nov 8). The accompanying IPv4 NOTIFYs are
accepted. These are separate from the external-primary unreachable errors and
did not prevent the demonstrated IPv4 secondary-to-secondary transfers.

## Reload evidence and limits

| Period | ns3 command time(s) | ns4 command time(s) | Count per host |
| --- | --- | --- | --- |
| Nov 5 burst | 16:56:41.713211–17:00:30.435230 | 16:56:44.302064–17:00:33.159473 | 25 |
| Nov 5 later | 17:23:18.650561 | 17:23:21.318213 | 1 |
| Nov 7 early | 00:40:40.540784, 00:40:54.603892, 00:41:04.720968 | 00:40:43.568506, 00:40:56.897797, 00:41:07.191748 | 3 |
| Nov 7 evening | 19:03:49.882513, 19:03:56.948604, 19:04:04.030745 | 19:03:52.184729, 19:03:59.448425, 19:04:06.712583 | 3 |

All **32 reloads per host** have corresponding `reloading configuration
succeeded`, `reloading zones succeeded` and `running` messages. All reference
`/nix/store/rlvbc4x3ym67pzkgj0jq8v2zik9wibz6-named.conf`. The unchanged main
configuration pathname does **not** prove unchanged generated includes or
per-zone primary configuration. No reload/control failure or restart appears
in this extracted control chronology; relevant `named` PIDs remain ns3
`2601390` and ns4 `2602016`.

No global reload is logged on November 6. On November 8 the only captured BIND
control command is ns3's manual zone retransfer. November 7's reloads do not
produce an `avting.cz` transfer/no-change event, so the logs cannot establish
which reload removed an external primary or what an equal-serial SOA check did.
No historical configuration content or primary-change audit was inspected.

Ns3 context ties sample reloads to nodectld transactions: Nov 5 17:23:18
`chain=13002152,trans=74371377`; Nov 7 00:40:40
`chain=13005730,trans=74401069`; Nov 7 19:03:49
`chain=13009102,trans=74429908`. These are correlation references only, not
proof that any particular transaction changed this zone's primary list.

## What can and cannot be concluded

- **High confidence:** the Nov 5 success, Nov 6 unreachable attempts, one IPv6
  transfer handle producing two error forms, and Nov 8 same-serial retransfer
  from the other secondary. These have direct timestamped log evidence.
- **High confidence within retained files:** no subsequent zone-specific
  positive event before manual retransfer, despite BIND messages throughout
  the hourly coverage window; global reloads succeed without emitting such
  an event for this zone.
- **Supported explanation, source correlation required:** a stored last failure
  can remain visible while data stays at the current serial if routine
  equal-serial refresh emits no event consumed by the application. The logs
  alone do not inspect application state or prove successful silent refresh.
- **Not established:** continuous authoritative availability, exact zone-content
  equality, historical SOA refresh schedule/expiration, the external primary's
  authoritative data after November 5, precise IP-detach/disown times,
  per-zone generated configuration history, or the deployed parser revision.
  Equal serial and equal transfer size do not independently prove equal content.
- Earlier BADKEY messages require their own context if pursued; they precede a
  confirmed successful TSIG transfer and must not be presented as the cause of
  the November 6 host-unreachable result.

No additional production probe is needed for this bounded chronology. Further
source/status/IP-lifecycle synthesis belongs to architect0 and the other
assigned packages. Broad scans stopped once chronology and collection limits
were established.

## Commands and disposable artifacts

Session identity was verified with `dev-session current` and matching
`DEV_SESSION_SLUG` / `DEV_SESSION_WORKSPACE`; the live same-session roster was
read before investigation. Every SSH command used
`ssh -o BatchMode=yes -o ConnectTimeout=15 root@log.int.prg.vpsfree.cz`.

Exact remote commands for the incident evidence:

```sh
hostname
date --iso-8601=seconds
readlink -f /etc/localtime
ls -lah /var/log/remote/cz.vpsfree/containers/ns3 /var/log/remote/cz.vpsfree/containers/ns4
grep -nHF avting.cz /var/log/remote/cz.vpsfree/containers/ns3/log /var/log/remote/cz.vpsfree/containers/ns4/log
grep -nHE '^2026-11-0[5-8].*named.*(control channel|reload|reconfig|running|stopping|exiting|loading|configuration|starting BIND)' /var/log/remote/cz.vpsfree/containers/ns3/log /var/log/remote/cz.vpsfree/containers/ns4/log
awk 'substr($0,1,10)>="2026-11-05" && substr($0,1,10)<="2026-11-08" {k=FILENAME " " substr($0,1,13); total[k]++; if($0 ~ / named\[/) named[k]++} END {for(k in total) print k,total[k],named[k]+0}' /var/log/remote/cz.vpsfree/containers/ns3/log /var/log/remote/cz.vpsfree/containers/ns4/log
stat -c "%n %s bytes mtime=%y" /var/log/remote/cz.vpsfree/containers/ns3/log /var/log/remote/cz.vpsfree/containers/ns4/log
head -n 1 /var/log/remote/cz.vpsfree/containers/ns3/log /var/log/remote/cz.vpsfree/containers/ns4/log
tail -n 1 /var/log/remote/cz.vpsfree/containers/ns3/log /var/log/remote/cz.vpsfree/containers/ns4/log
sed -n '105630,105670p;118435,118455p;140290,140330p;157260,157310p;175455,175475p' /var/log/remote/cz.vpsfree/containers/ns3/log
```

Remote `rg` was attempted first but is not installed (`bash: rg: command not
found`); the successful extract uses `grep`. No package was installed.

Raw, untracked, disposable outputs are separate under `raw-log-evidence/`:
`avting-current.log` (68 lines), `named-control-nov5-8.log` (321 lines),
`hourly-coverage.log` (176 rows), `boundaries.log`, and `ns3-context.log`.
Original file line numbers are retained by the grep extracts. Hour buckets
were checked locally with Python against the complete 88-hour expected set;
no missing bucket was found on either host. These are evidence analyses,
not application tests. No feature revision or migration was changed.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-08-dns-transfer-ip-lifecycle/
