# Leave scrape margin in the index render freshness alert

Initiative: `archive/2026-09-07-vpsfstatus-index-stale-2/`.

An unchanged status index body uses a 240-second keepalive, checked when probe
and notice updates request rendering. The successful-render metric contains a
completion timestamp. Prometheus scrapes every 60 seconds and alerts when its
observed render age exceeds 300 seconds. The alert group evaluates every 300
seconds and the rule has no `for` period.

The normal interval plus scrape delay already consumes the threshold. A local
timing reproduction with successful renders every 242 seconds and successful
scrapes at 1, 61, 121, 181, 241 and 301 seconds yielded an observed age of 300.5
seconds at evaluation time 300.5, although the actual body was only 58.5 seconds
old. A five-minute rule group can retain that briefly triggered firing state
until the next evaluation. `max_over_time(timestamp[5m])` tolerates metric
absence but does not remove observation delay or guarantee tolerance of a
missed scrape.

Compare render age with attempt age, render duration/failures, `up` and actual
alert times. Give the keepalive, scrape interval and threshold enough margin;
use a suitably frequent rule group if adding a short `for` period. The report
records a proposed monitoring-only remedy; no fix was deployed in this session.

The page's displayed generated time comes from its per-request shell and does
not establish that the cached body was rebuilt. English and Czech caches share
one render-success gauge, so nearby timestamp updates can represent localized
bodies within the same cycle.
