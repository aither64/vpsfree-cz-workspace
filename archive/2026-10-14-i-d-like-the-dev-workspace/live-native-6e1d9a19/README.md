# Post-activation live notification acceptance

**UNRUN — static preparation only.**

Prepared only for runtime `6e1d9a191724d376cad2a71f234f0e4d1c01f36f` at the fixed
HTTPS portal origin and this session's Settings page. No live request, SSH
credential read, display launch or browser operation was performed during
preparation. The predecessor `live-native-bb9e6291/`, all earlier live bundles and
`live-notification-check.cjs` remain unchanged. This new directory adapts the
approved bb9 headed-browser harness and owned-Xvfb runner.

## Actual run command, after authorized activation

Run only after the lead's authorized activation succeeds, using a fresh
dev-session-monitor watcher or its visible fallback:

```sh
LIVE_PROFILE_PREPARED=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/profile-prepared-6e1d9a19.json bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/live-native-6e1d9a19/run.sh
```

`LIVE_PROFILE_PREPARED` must name the actual final activation's trusted profile
preparation record under this tracking directory. At preparation time, the
default `profile-prepared.json` still covers the earlier e414ed3 runtime. The
harness deliberately refuses it. The command above names a new, not-yet-supplied
`profile-prepared-6e1d9a19.json`; the lead must supply a genuine final preparation
record after authorized activation, or point the environment variable at that
record under this tracking directory. Do not edit the stale proof or its
coverage, or disable checks to make a run proceed.

The runner uses the existing cached runtime environment, pinned browser bundle
and rooted Xvfb executable from `xvfb-path.txt`. It verifies the harness manifest,
refuses an existing `run/`, and starts one exact-owned Xvfb process through
`-displayfd`, with TCP disabled. Its retained child handle is the only display
process stopped/reaped afterward. No shared display or global trust is changed.

## Revision and identity checks

The supplied profile preparation must bind `dev-workspace` coverage to exact
6e1d9a19 and its candidate package must equal the selected remote profile's
resolved path. That path is read through the existing trusted root SSH connection using
only `readlink -f`. Before Enable, the authenticated browser also verifies the
served notification client, worker and shared store asset SHA-256 values against
the committed 6e1d9a19 bytes in `expected.json`. The fixed page path and rendered
session slug must match this conversation's session.

The trusted preparation record, selected package and served assets are checked
immediately before Enable, before Test and after the zero-tab window. A mismatch
refuses new test work or records a revision change; only scoped cleanup may continue. This is package/source
binding through the trusted preparation record and served bytes, not a new
server revision endpoint. A changed selected revision requires new matching preparation and proof.
Do not change this bundle's expected value in place.

The client, worker and shared store were independently read from committed
Git objects at bb9e6291 and 6e1d9a19 and compared byte-for-byte. All three are
identical; their SHA-256 values remain the same. `asset-comparison.json` records
each source path, public route and digest. `provenance.json` binds runtime
`6e1d9a191724d376cad2a71f234f0e4d1c01f36f`, workspace
`0a9d232e74209da2c2f53358e5f2807f34074055` and configuration
`45fa9962df83b9bec65523ae6ee7d19b63bb03ea`. These published source identities
are provenance, not activation proof. The genuine final preparation record is
still required. VM/CI, composition, activation and execution remain lead-owned.

## Credentials and native delivery

Only the eventual Node process reads Basic credentials into memory, using the
existing trusted `root@172.16.106.40` commands for the username and password.
They are passed as origin-scoped Playwright HTTP credentials, never in URLs,
environment variables, command arguments, logs or artifacts. SSH diagnostics
and raw exception messages are not printed. Host-key checks remain enabled.
TLS allowances apply only to the new disposable browser contexts/processes.

Chromium and Firefox each get a fresh persistent disposable profile and run
headed. Firefox uses its normal enabled push-service preferences. The harness
grants notification permission only in that context, then explicitly clicks
the shipped Enable and Send test buttons. Native subscription, server transport,
worker and `showNotification` remain unchanged; no mocks or prototype overrides
are installed. It does not change session mutes or use a fixture endpoint.

After the shipped ten-second queued message, every portal tab closes and
`about:blank` remains active for eighteen seconds. Reopening reads only a safe
settings result and counts: test-kind records in the worker's IndexedDB and real
browser notification records. Registration IDs stay within the browser query;
no private server store, endpoint, subscription key, ID, payload or transcript
is returned. IndexedDB inspection aborts a new-database upgrade rather than
creating an empty schema ahead of the application.

Provider acceptance, worker receipt and browser notification records are
separate fields. A zero Firefox browser-record count does not erase positive
worker receipt. Linux/Xvfb cannot establish physical or macOS display. This
harness does not exercise a real notification click; click/auth contracts are
separate evidence. A zero process status means diagnostics completed, not that delivery succeeded.

## Scoped cleanup and evidence

After any Enable attempt, cleanup uses only this fresh profile's shipped
Disable action. Success requires its fully Disabled result and an independent
`getSubscription()` absence check. It closes only this profile's notifications,
then closes its browser. A confirmed-clean profile is removed. If cleanup or
browser closure is uncertain, the private mode-0700 temporary profile is retained
for explicit recovery, with a mode-0600 `run/recovery-profiles.json` containing
only the browser name and local profile directory. Do not upload retained
profiles or expose their contents. No automatic retry is performed.

`run/results.json` contains sanitized per-browser evidence.
`run/browser-check.log/status` records the exact Node result, while `run/status`
and `run/runner-summary.json` also cover owned display cleanup. Owned Xvfb output
and timestamps remain beside them. No session, host, reservation or lifecycle
mutation is performed by the harness.

## Static preparation checks

From this directory in the cached runtime environment:

```sh
bash -n run.sh
node --check live-check.cjs
python3 -c 'import ast; ast.parse(open("run_live.py").read())'
sha256sum --quiet -c harness-sha256.txt
```

These do not execute the live JavaScript or contact SSH/HTTPS. Preparation also
checks the local Xvfb executable and asset hashes without launching anything.
See `preparation-checks.log/status`, `preparation-summary.json`, `provenance.json`,
`asset-comparison.json`, `preserved-prior-bundle.sha256` and `adaptation.patch`.
`inventory.md` lists the exact preparation scope and limitations. Source, prior
probes and the old live script remain unchanged. Earlier disposable native
provider results belong to their own runs. This directory has no `run/`, browser
profile, delivery result or final preparation proof; no live acceptance has run.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>
