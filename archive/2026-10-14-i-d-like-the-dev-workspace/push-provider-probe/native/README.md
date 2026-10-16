# Headed native provider probe

Prepared only; implementer0 has not launched Xvfb or a browser. The first probe
and registration-diagnostic sources and run artifacts remain unchanged. This
third disposable source copy again comes from runtime commit
`e414ed31806d2b91620d5e5fad8b5b5ee56e07ac`; only its notification Go/CJS browser
fixture files differ. The registered application source and branch are frozen.

## Why this run differs

The diagnostic run established that Chromium created a local subscription with
valid key shape and null expiry, but its hostname failed the product allowlist.
The register API returned 400 `unsupported_endpoint`, with zero stored
registrations. The hostname was not recorded, so a native provider mismatch is
not yet established. Firefox registered the worker, then native
`getSubscription` rejected with `AbortError` before a register API request.

The installed Firefox `playwright.cfg` explicitly sets
`dom.push.serverURL` to an empty string and `dom.push.connection.enabled` to
false. This probe overrides them with the native push-service URL and true,
respectively. Both engines run headed on one disposable Xvfb display. Chromium
retains the previous background-networking/certificate arguments. The native
subscription hostname is now recorded to establish its exact allowlist fit;
paths, query strings, capabilities and keys remain excluded.

These changes address demonstrated fixture conditions. There is no product
change, synthetic subscription, provider transport replacement or weakened
endpoint validation.

## Exact lead watcher command

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/push-provider-probe/native/run.sh
```

Use a fresh dev-session-monitor watcher or its visible fallback. Do not run a
blind retry. The runner reads the lead-prepared absolute executable from
`work/2026-10-14-i-d-like-the-dev-workspace/xvfb-path.txt`, uses the cached declared
environment and pinned browser bundle, verifies the copied source manifest and
refuses to overwrite `run/`.

`run_native.py` starts one Xvfb child using `-displayfd` and `-nolisten tcp`,
waits up to fifteen seconds for display allocation and passes that display only
to its Go/browser child. It never selects a shared display. The Xvfb PID is
recorded locally; cleanup signals and reaps only that retained child handle,
with a five-second termination grace before killing the same child if needed.
No process-name search or broad kill is used. The browser test has its existing
operation bounds; X startup does not time out a quiet provider operation.

Read `run/results.json` for browser/provider evidence, `run/go-test.log` and
`run/go-test.status` for the exact Go result, and `run/status` plus
`run/runner-summary.json` for runner/display cleanup. `run/xvfb.log` contains
only the owned display's output. Exit zero records completed diagnostics; it
does not imply provider or worker success. A failed setup remains incomplete.

The Go fixture, sender-only ticker, explicit shipped Enable/Test actions,
ten-second delivery delay, eighteen-second zero-portal-tab window, actual
worker/IndexedDB/getNotifications evidence and shipped Disable cleanup are
unchanged from the diagnostic adaptation. Browser profiles and private fixture
state remain disposable. No real session, host, machine reservation or lifecycle
operation is performed.

## Evidence limits and artifacts

Only the public endpoint hostname is newly permitted in output, filtered as a
bounded DNS name. All other diagnostic values remain fixed categories, booleans
and counts. Existing registration response classification remains bounded and
never prints raw bodies. No subscription key, registration ID, full endpoint or
payload is emitted. Firefox's public push-service preference is configuration,
not a subscription endpoint.

This is a headed Linux test on a virtual display. It cannot establish macOS or
physical OS notification display. Provider acceptance, actual worker receipt and
browser notification records must still be assessed separately. Report any
native provider mismatch or confirmed product issue to the lead before changing
the frozen application.

`adaptation.patch` compares against the committed fixture;
`native-increment.patch` compares against the prior diagnostic adaptation.
`provenance.json`, `source-sha256.txt`, `preparation-summary.json` and
`preparation-checks.log/status` identify the copied source, preserved earlier
evidence and static preparation checks. Preparation selects no Go tests and
starts neither Xvfb nor browsers.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>
