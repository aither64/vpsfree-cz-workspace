# Milestone 5 final browser acceptance

Required browser coverage completed across preserved runs on the same final
source and unchanged HTTP invocation. No product fix was needed. The first two
runs remain failed records for proven ignored-harness errors; successful cases
were retained rather than rerun solely to obtain one green aggregate.

- HaveAPI head: `35c1fb964735639c0873aacf078e18569f05f9bc`
- Tree: `756b61de87833d8ded478b5d7785618671b4ddcb`
- Source SHA-256: `ce9e3e5b491efe094238fdadedd5cd8031f6eb2c0f8ab2601faca50913669831`
- HTTP invocation: `96c6da502cc84f3d93e18c9695f01aaa`; Ruby2094702/DB2095702.
- Fresh server receipt: [milestone5-final-receipt.json](../preview/milestone5-final-receipt.json).
  Each run matched stable/clean loaded-current health, PID and all five local
  0.31.0 gem paths. Final read-only head/tree/status check still matched and clean.
- Browser: Chromium156.0.8078.4, existing Playwright1.64.1/Node24 runner;
  tools `/nix/store/cj7x035wxyc41msqbn9nmg3qblhh3pav-api-documentation-browser-tools`.

## Completed coverage

| Case | Evidence | Actual case time |
| --- | --- | --- |
| Current-source unrouted cold/warm/cross-navigation cache | run1 | 11.000s |
| Actual nested search/native display parity +409/native fallback | run1 | 23.731s |
| 390 touch UI/copy/detail/shell/local scrolling | run1 | 24.945s |
| 768 touch UI | run2 | 23.419s |
| 1024 touch UI | run2 | 24.307s |
| 1440 keyboard UI | run2 | 21.936s |
| Synthetic long API/account geometry at all four widths | run2 | 4.315–4.564s each |
| Ordinary no-JS GET search | run2 | 7.483s |
|503/malformed/wrong-key/executable response failures | run2 per-case diagnostics | all four passed |
| Shared display fixtures +controlled persisted/current bootstrap | run2 completed assertions before final safe-text case | passed |
| Focused literal hostile-label text, no media/script adoption or requests | run3 | 3.757s |

Actual UI checks: one aligned full resource identity; literal `...`; concrete
host identity; root person entry; versions/internals hierarchy without duplicate
main lists; native theme/account disclosure focus/Escape/outside/touch; real
rendered metadata for CLI/curl/HTTP single-level controls, saved thorough restored
for a capable client, and stable example position. Native HTTP copy returned true
at every width and copied exactly307 bytes from the visible current panel, with
nonempty document selection/focus/window+sidebar scroll/preferences retained.
Copy targets were44×44px and stayed clear of code. Guide/limitation exclusions,
code readability/local touch scrolling, semantic validator columns/local touch
and keyboard scrolling, and document-width bounds passed at every viewport.
The actual discovered nested path was `cluster_resource_package.item`.

Parent inspected all24 responsive/geometry screenshots plus failure and final
safety images. No material product usability defect was found. Long identities
wrap, with controls remaining reachable. Phone/tablet versions/internals images
show the open navigation; desktop images include main content. Copy images retain
the deliberate test selection and, at390, local horizontal pan. These are not
untouched initial-state screenshots.

## Current-source cache diagnostics

Unrouted context only: zero page-load bulk requests; one keyed server request,
then one cross-navigation disk-cache hit with zero encoded network bytes.
Payload883,877 bytes:152 resources/524 actions/6,358 parameters. Cold input to
results3435.8ms; warm51.5–59.9ms including driver overhead. These are diagnostics,
not calibrated performance measurements. Cache-Control was private/86400/
immutable; Vary contained Accept-Language, Cookie and Authorization. No routed
fault fixture supplied cache evidence. Historical9f receipts keep their scope.

## Preserved failures and corrections

Run1 stopped at synthetic Account outside dismissal: the long popup covered the
form-label centre, so the intended outside tap actually hit an inert button inside.
The failure image proves the occlusion. A hit-tested noninteractive(8,8) viewport
point corrected only the harness; the menu then passed all widths in run2.

Run2 stopped at literal hostile-label text: fixture resource0 is bulk, but the
harness queried widget, excluding the mutated resource. The failure screenshot
and fixture prove that mismatch. Run3 queried the actual fixture target bulk and
passed without requests/executable nodes. The original failed logs/scripts and
results remain intact. The earlier run3 bootstrap wrong-key flaw is closed by
four successful fresh-keyed fault cases plus separately successful current
bootstrap assertions. No old failure was silently relabelled as passed.

Script durations:65.701s +116.968s +4.757s =187.426s total actual browser-script
execution, including failed harness cases. Watcher startup, diagnosis and manual
image review are separate. Every operation used named15s UI/body/event/close or
45s navigation bounds; no unbounded409 body read or silence cancellation occurred.

## Limits and disposition

Anonymous HTTP does not prove authenticated cookie identity or HTTPS Clipboard
API. Account/long-name images are explicitly synthetic DOM geometry with inert
buttons; backend identity checks and peer HTTPS/OAuth acceptance are separate.
No sign-in/out, credentials, OAuth/TLS/private fixture/peer access was attempted.
Native BFCache was not claimed: earlier9f native unavailability remains historical;
this batch proved controlled persisted/current handler behavior only.

Fresh Luna/low native CLI watchers used retained catalog3ff7a212… and explicit
actual danger-full-access/approval-never headers. Threads: watcher1
01a1834d-bff8-72d3-9e16-e3c82f297f5d; watcher3
01a18353-22a3-7731-9179-5a3b7b5f132a; watcher4
01a18357-7551-7f10-af71-27d3780789e1. Watcher2 stopped before browser launch on
self-description versus launch-header confusion; its record is retained. No
model/settings substitution occurred; subsequent policy uses actual CLI headers.

All watcher command handles returned. Watchers reaped their descendants and the
parent process inspection found no remaining matching runner/watcher/Chromium.
Browser SOURCE HOLD RELEASED; utility capacity free. Preview/DB remain serving.
No application/dependency/Git/hook/service/lifecycle mutation was performed.

## Artifacts

- [run1 result](milestone5-final-35c1fb96-run1/result.json) / [log](milestone5-final-35c1fb96-run1.log)
- [run2 result](milestone5-final-35c1fb96-run2/result.json) / [log](milestone5-final-35c1fb96-run2.log)
- [focused run3 result](milestone5-final-35c1fb96-run3/result.json) / [log](milestone5-final-35c1fb96-run3.log)
- Screens: run1 contains versions/internals/resource/copy/validator390;
  run2 contains those at768/1024/1440 and synthetic-account390/768/1024/1440;
  run3 contains inert-text-safety.png. Each source run retains its failure image.
- Runnable source snapshots and all four watcher logs/results remain in browser/.

[Live HTTP preview](http://172.16.106.40:4567/v7.0/) ·
[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/)
