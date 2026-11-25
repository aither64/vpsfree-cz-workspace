# React exact-head CI observation handoff

Owner after this inventory: lead. Implementer2 has stopped CI polling and has not launched a CI watcher.
Use the installed dev-session-monitor skill and a fresh catalog Luna/low utility under its execution policy; no existing backend/KB/Rust observer is to be joined, duplicated or replaced.

Repository vpsfreecz/vpsadmin-webui; branch dev/oomd-abuse-policy; head bbd820a65536564756484f6dd037f10224901b35; base88ac13b89d6421c914cd57e18153de1fee6fc7b7; all run attempts1.

| Workflow | Workflow ID | Run ID | Event | Attempt |
| --- | --- | --- | --- | --- |
| Playwright smoke | 369520616 | 43536102691 | pull_request | 1 |
| Playwright broad smoke | 369520614 | 43536102644 | pull_request | 1 |
| CI | 369520612 | 43536102707 | pull_request | 1 |
| Playwright broad smoke | 369520614 | 43536097719 | push | 1 |

Required source-selected gates and initial native job state:

- Run43536102691/attempt1/job132265357956: PR smoke E2E (mobile-chrome); in_progress/pending.
- Run43536102691/attempt1/job132265358315: PR smoke E2E (chromium); in_progress/pending.
- Run43536102691/attempt1/job132265358342: PR smoke E2E (mobile-webkit); in_progress/pending.
- Run43536102644/attempt1/job132265357770: Broad smoke E2E (chromium); in_progress/pending.
- Run43536102644/attempt1/job132265358047: Broad smoke E2E (mobile-chrome); in_progress/pending.
- Run43536102707/attempt1/job132265357915: Required nonbrowser checks; in_progress/pending.
- Run43536102707/attempt1/job132265358126: Production build; completed/success.
- Run43536102707/attempt1/job132265358413: Chromium script regression; completed/success.
- Run43536097719/attempt1/job132265341856: Broad smoke E2E (chromium); in_progress/pending.
- Run43536097719/attempt1/job132265342179: Broad smoke E2E (mobile-chrome); in_progress/pending.

CI369520612 runs root npm ci, critical production audit, BFF production install/high audit, ci:quick and ci:tests; separate production build and Chromium script regression. Smoke369520616 runs desktop/mobile Chrome/mobile WebKit; broad369520614 runs desktop/mobile Chrome. Nightly369520615 was not dispatched and is outside this batch.

Bounded observation only: retain authoritative terminal conclusions for these exact runs/attempts/head; retrieve failed-job logs/artifact metadata promptly on actual failure, report raw evidence to lead for implementer2 diagnosis. Do not edit, diagnose, rerun, manually dispatch, install locally, build/browser locally, merge, deploy, release, alter lifecycle or cancel current-head runs. No superseded nonterminal same-branch run existed in this inventory, so none was canceled. Both current broad runs are automatic event duplication, not agent-initiated repetitions.

Use exact native API argv for each run (repeat status reads only as necessary for observation, never a moving branch latest):

`["gh", "api", "repos/vpsfreecz/vpsadmin-webui/actions/runs/43536102691/attempts/1"]`
`["gh", "api", "repos/vpsfreecz/vpsadmin-webui/actions/runs/43536102644/attempts/1"]`
`["gh", "api", "repos/vpsfreecz/vpsadmin-webui/actions/runs/43536102707/attempts/1"]`
`["gh", "api", "repos/vpsfreecz/vpsadmin-webui/actions/runs/43536097719/attempts/1"]`

All observed jobs report head_sha equal to the final source. Record actual checkout/build commit from available logs when certifying source; pull_request checkout can use the synthetic merge ref, so preserve its source/base/tree evidence separately. Do not infer real backend behavior from intercepted browser fixtures or old screenshots. CI cancellation is not command interruption permission. Return result, provider conclusion, exact IDs/attempts/head, elapsed, log/artifact paths and any unknown/still-running effects per monitor skill.

Initial raw inventory/jobs are stored beside this brief; no local full suite was repeated. Implementer2 owns concrete source/check failures when the lead delivers them.
