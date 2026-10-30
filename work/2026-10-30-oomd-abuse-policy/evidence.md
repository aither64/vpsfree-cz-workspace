# OOM policy log evidence — 2026-10-30

Read-only investigation authorized by the user through the lead. No database,
node configuration, deployment or live mutations. No owner identities queried.

Current user decision: "no, let's keep the original thresholds for now."
The selected proposal is **5 incidents/rolling 7 days for warning and
10/rolling 30 days for stop**. The 3/8 alternative was declined for now.
VPS 28376 remains below the selected monthly stop limit; its evidence and all
threshold comparisons are retained. No additional log queries or scans were made.

## Source, scan and coverage

Access: `ssh -o BatchMode=yes root@log.int.prg.vpsfree.cz`, resolved from
`notes/vpsfree-cz-configuration/2026-09-14-central-node-log-investigation.md` and
checked against configuration `cluster/cz.vpsfree/containers/prg/int.log/config.nix`.
This host worked; no missing access prerequisite remained.

Read all 32 files: `/var/log/remote/localhost/log-20260930`,
`log-20261001` through `log-20261030`, and current `log`. Rotation suffix is
rotation date, not occurrence date. Remote Perl streamed each file once, retaining
only action/failure fields and per-host/day coverage totals. Input was about
5.04 GB logical (~1 GB allocated); runtime about 2.5 minutes (~35 MB/s logical).
The scan completed with exit 0. No remote files were written. A contemplated
full node-log scan (~195 GB logical) was not launched.

The collected span is 2026-09-28 22:00:06 UTC through
2026-10-30 14:33:26 UTC. Twelve daemon source hosts each appear on all 32 local
calendar dates: node1/2.stg; node19–25.prg; node5/6.brq; backuper2.prg. This
proves daily source presence, not gap-free delivery or full fleet coverage.
The node-log directory has 26 node directories, which is not an inventory of
currently running VPS or of enabled/current OOM daemons.

Fixed analysis cutoff: **2026-10-30 14:30:00 UTC**. Trailing 30 days begin
2026-09-30 14:30 UTC and trailing 7 days begin 2026-10-23 14:30 UTC. Lower bounds
excluded, upper bounds included; UTC comparisons account for the DST transition.
The log timestamp is the action-start syslog timestamp, a proxy for the daemon's
`Time.now` captured immediately after that log message. Exact database
`detected_at`/delivery status was not queried.

## Counting method and confidence

- 4,293,477 `osctl-oomd` lines across the full scan are mostly samples/debugging.
  Only exact `[killer] (restart|stop) pool:numeric_vps` lines count as attempts.
- Full scan: 170 attempts, 6 explicit `osctl ct ... failed` messages, no broadcast
  failures observed. Trailing 30 days: 164 attempts, the same 6 failures (3.7%).
  Each failure matches the preceding action on the same node/pool/VPS/action;
  completion/failure delays range from 95 to 361 seconds for these six.
- Excluding failures leaves **158 inferred-success candidates**, all restarts,
  across 48 VPS. No stop attempts were observed. No duplicate
  `(node,pool,VPS,action,integer-second)` keys were found in these candidates.
  Absence of an error does not prove success, broadcast or API persistence.
- Targeted second command, completed exit 0:
  `grep -m 20 'osctl-oomd action' /var/log/remote/cz.vpsfree/nodes/prg/node23/log`
  over the same read-only SSH connection returned 7 confirmations. All match
  attempts today, with action-start-to-confirmation delays of 26–560 seconds.
  The source broadcasts only after successful `osctl`, so these 7 are confirmed
  successes; this is a targeted sample, not a random success-rate estimate.
- Of today's 8 candidate attempts on node23, VPS 28376 at 12:26:19 UTC has no
  confirmation in the collected sample. It may be pending, missing or failed;
  do not claim it succeeded. Removing it yields 157 candidates, changes that
  VPS from 9→8 monthly and 5→4 weekly. Under the selected 5/10 limits, weekly
  crossings change 4→3 and the five monthly candidates are unchanged. Under the
  declined 3/8 alternative, all eight weekly and seven monthly candidates remain.
  Other unobserved loss or uncertainty remains possible outside this selectively
  confirmed sample.

## Distribution and candidate thresholds

Trailing month count histogram (candidate count → number of VPS):
`1→26, 2→6, 3→6, 6→3, 9→2, 10→1, 11→1, 12→1, 14→1, 19→1`.
Trailing week: 51 candidates across 21 VPS;
`1→10, 2→3, 3→2, 4→2, 5→3, 6→1`.

| Weekly limit | At cutoff: of 21 weekly eventing VPS | Reached in any observed rolling week: of 48 monthly eventing VPS |
| --- | ---: | ---: |
| 3 | 8 (38.1%) | 12 (25.0%) |
| 4 | 6 (28.6%) | 9 (18.8%) |
| 5 | 4 (19.0%) | 7 (14.6%) |
| 6 | 1 (4.8%) | 5 (10.4%) |

| Monthly limit | At cutoff: of 48 monthly eventing VPS |
| --- | ---: |
| 8 | 7 (14.6%) |
| 10 | 5 (10.4%) |
| 12 | 3 (6.3%) |
| 15 | 1 (2.1%) |

The any-week calculation examines windows ending at observed events using only
events inside the sampled 30 days. Early windows can omit events before that
period. It is distinct from the current-week count and not a simulation of
actual warnings/stops. Enforcement would change subsequent user behavior and
event counts. Fleet denominator and database completeness are unknown.

| VPS | 7d | 30d | Max observed rolling 24h | Distinct UTC dates in 30d |
| --- | ---: | ---: | ---: | ---: |
| 27741 | 5 | 19 | 3 | 14 |
| 28655 | 5 | 14 | 1 | 14 |
| 4135 | 6 | 12 | 3 | 10 |
| 27837 | 3 | 11 | 3 | 8 |
| 29528 | 4 | 10 | 4 | 8 |
| 28376 | 5 | 9 | 4 | 6 |
| 29988 | 0 | 9 | 7 | 4 |
| 21234 | 2 | 6 | 2 | 6 |
| 27838 | 4 | 6 | 4 | 4 |
| 24913 | 0 | 6 | 4 | 3 |

The initial recommendation used 5/7 and 10/30 to select the most persistent
cases, whose top five monthly counts span 8–14 dates. That calibration missed
the user's known case: VPS 28376 was joint sixth by monthly count, and the
proposal's five-row table omitted it. At 5/10 it does not meet the monthly stop
limit; whether it meets the weekly warning depends on the unresolved action.
At 3/8 it meets both limits with either 5/9 or the more conservative 4/8 counts.

The 3/8 alternative covers 8/21 weekly eventing VPS (38.1%) and 7/48 monthly
eventing VPS (14.6%), unchanged by excluding that unresolved action. It would
give earlier warning and include two additional monthly candidates, including
VPS 29988: nine in a rolling week, seven in 24h, but none this week. The user
declined this broader coverage for now, retaining 5/10 with the known VPS 28376
limitation. No separate burst rule is proposed. Historical counts alone must
not cause stops, and all inferred-success limitations still apply.

The shortest candidate inter-action interval is 19.4 seconds. Three rapid
VPS 28376 restarts on Oct30 are separately confirmed; proximity is not proof
of duplication. Do not collapse actions into arbitrary time buckets.

## Reset semantics and provenance limits

`osctl-oomd/lib/osctl/oomd/killer.rb` increments restart/stop hit scores on hits,
decrements them on misses, and resets only the score for the completed action.
Scores live in daemon memory and are pruned; they are not monthly counters.
The node source configuration enables verbose OOM logging; sampled lines show
8 restart hits / 40 stop hits. This analysis does not establish running source
revision/configuration for every historical node, nor daemon uptime, VPS owner
transfers, manual starts/stops, database ingestion or email delivery. No existing
monthly policy action was inferred from the absence of daemon stop logs.

Sanitized disposable artifacts remain untracked under `evidence/`:
`oomd-actions.tsv`, `node23-confirmed.tsv`, `distribution.json`. Do not stage raw
artifacts. This Markdown preserves conclusions if those files are removed later.
Local analysis used Python datetime parsing, failure matching on source identity,
window filtering, per-VPS grouping and rolling maxima; no production writes.

## Verified email guidance links

Read-only `kb-page get` on 2026-10-30 verified these existing public pages:

- Czech: [Vše o členských poplatcích](https://kb.vpsfree.cz/informace/platby#z_ceho_se_sklada_clensky_poplatek),
  page `informace:platby`, section `Z čeho se skládá členský poplatek`.
- English: [Everything About Membership Fees](https://kb.vpsfree.org/information/membership_fees#what_the_membership_fee_is_composed_of),
  page `information:membership_fees`, section `What the Membership Fee is Composed of`.

Both describe increasing VPS RAM/disk through increased membership fees and
contacting support. The Czech `<page>information:membership_fees</page>` tag
confirms the language pairing; public HTTP verified the Czech canonical URL
and section anchor. These are membership-fee pages with expansion guidance,
not a separately discovered expansion article.

Existing [Czech OOM guidance](https://kb.vpsfree.cz/navody/vps/incidenty#oomd) and
[English OOM guidance](https://kb.vpsfree.org/manuals/vps/incidents#oomd) were also
read through `kb-page get`. Both describe memory pressure affecting other VPS
and the whole node, and recommend fitting worker counts (web server/Apache/PHP)
to available memory. No KB writes were performed; final email prose is lead-owned.
