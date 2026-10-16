# Firefox display assessment, 2026-10-15

Investigation only. Bound current/environment identity and retained roster rev17
match this session and architect0's saved design/workspace-write role. Source
inspected: `4ed9af55127743b7564cb4dd01d10c9f7fee5120`. Lead reports that runtime,
workspace `750ab33c` and configuration `c90e56d5` are deployed with both ordered
jobs applied and independently checked identities; this investigation did not
repeat those host checks. Existing [design](design.md#deployed-firefox-delivery-feedback-2026-10-15)
and its physical-display acceptance limit remain unchanged.

## What the sealed run establishes

Evidence: [results.json](live-native-4ed9af55/run/results.json) and
[runner-summary.json](live-native-4ed9af55/run/runner-summary.json). The run used
headed Linux browsers under Xvfb, real provider delivery, matching served assets
and zero portal tabs during the wait. Exit 0 means diagnostics completed.

| Observed stage | Chromium 147.0.7727.15 | Firefox 148.0.2 |
| --- | --- | --- |
| Test queue accepted; valid descriptor | Yes | Yes |
| Last provider result | Accepted, uncorrelated | Accepted, uncorrelated |
| Exact Test worker outcome | Received, correlated | Received, correlated |
| Display API outcome | Resolved | Rejected, category `UnknownError` |
| Worker notification-record result | Present | Unavailable after rejection |
| Separate matching browser-record read | One present | Zero, absent |
| Physical OS appearance / click | Unverified | Unverified |

The correlated worker receipt establishes arrival of the particular queued Test;
the registration-wide provider result alone would not. Firefox therefore failed
at the display-call boundary in this run, after real delivery. Its worker did
not claim a successful display followed by disappearance. Both shipped Disable
actions confirmed server cleanup and local absence; the runner records browser
closure, profile removal and Xvfb reaping. No cleanup is requested here.

## Source interpretation and remaining uncertainty

`portal/internal/web/static/notification-worker.js:29-55` separates the awaited
`showNotification` call from bounded diagnostic storage and old-Test cleanup.
Its catch records rejection; the later matching-record lookup runs only after
resolution. The call uses a fixed title/body, a fresh event-specific tag,
`renotify: false` and cloneable route/identity/revision data. No invalid option
combination or application exception is demonstrated by the sealed evidence.

The Test branch bypasses session trust/focus/acknowledgement processing. Session
ack closes only session tags, and old-Test cleanup targets older entries of the
same registration. These mechanisms do not explain this recorded display-call
rejection. `session-attention-store.js:44` maps every exception name outside six
allowlisted categories to `UnknownError`; that value is not proof that Firefox
raised a native exception with that exact name or a particular backend error.

The evidence proves browser-side rejection of the application's call, not its
underlying cause and not a platform-only defect. Browser implementation,
notification-backend/environment failure and an unobserved compatibility issue
remain distinguishable possibilities, not findings. Granted web permission does
not prove a usable OS notification backend. Xvfb supplies a virtual display; it
does not establish the user's desktop notification environment. The packet has
no backend diagnostics establishing a missing Linux service or policy. Neither
that Linux rejection nor Chromium's success explains or exonerates the original
Firefox/macOS report. No source change or Linux retry is justified by this
packet alone.

## Smallest useful next evidence, for the lead to arrange

Use the existing deployed controls on the user's actual Firefox/macOS profile.
Confirm the updated page's worker-readiness status first; follow its close-tabs
and reopen guidance if an update is waiting, without resetting subscriptions.
Record Firefox/macOS versions, then send one explicit Test. For the requested
background condition, close portal tabs while leaving Firefox running and
minimized/unfocused. Reopen the same origin/profile after the ten-second send
delay to read the saved result; let its bounded expiry/grace check finish if
still pending. Retain the final Test text/error category, worker-update status,
separately labelled last provider result, actual banner/notification-center
appearance, and click result if an entry exists. Do not collect IDs, endpoints,
keys, private-state dumps or arbitrary console output.

- No matching receipt: investigate delivery/worker/update or local evidence
  availability; provider acceptance alone cannot choose among them.
- Matching receipt with rejection: the user's failure is also at the display
  API boundary. Preserve the safe category; `UnknownError` still needs further
  local evidence, not an assumption about macOS settings.
- Resolved API with no visible entry: distinguish matching browser record from
  physical appearance and investigate the browser/OS presentation boundary.
- Visible entry and working click: acceptance for that exact browser case;
  session input/done acceptance remains a separate existing requirement.

If rejection persists on macOS, the smallest subsequent discriminating control
would be one separately arranged local `showNotification` call using the same
active registration and minimal fixed options, recording only resolution or a
safe exception-name category and appearance. It would bypass transport and
custom Test options, never count as push acceptance, and need no new server API.
That control is conditional and not executed or assigned here. The immediate
next step needs no code: obtain the shipped correlated result on the actual
affected platform before choosing further instrumentation or a remedy.

Only this tracking note was written. No source/design edit, test, browser,
provider, network, host, deployment, queue or lifecycle operation was performed;
all sealed evidence and the active session remain preserved.
