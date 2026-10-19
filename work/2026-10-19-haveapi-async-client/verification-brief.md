# Post-review verification brief (not yet launched)

Session: 2026-10-19-haveapi-async-client. Review packet: review-packet.md.
Run only after final review findings are addressed. Each operation uses a fresh
pinned verification watcher (Luna/low, full_access), retaining exact exit/logs.
No diagnoses, retries, source edits or deployment by watcher. Escalate unexpected
kernel builds; no generic timeout based on silence. Any failure returns to lead
and owning implementer. No real API credentials or production mutations.

Expected committed candidates:

- HaveAPI dc94157808966c12418b4009085fec237a869789.
- React fbf2a7f70f145a1bb87f659e68c84df0245448c3.

Check exact heads first; revise this brief if review remediation changes them.

## HaveAPI full JS/server contract

Working directory: session HaveAPI worktree. Exact command:

```sh
nix develop -c bash -c '
set -e
export BUNDLE_GEMFILE="$PWD/servers/ruby/Gemfile"
bundle install
cd clients/js
npm test
'
```

This includes full JS suites, CallbackAdapter and AsyncAdapter shared Ruby-server
contracts, and typed-input tests. Helper owns local test-server lifecycle.
The top-level Nix environment supplies Ruby as well as Node. No other-language
full regression suite is selected for this client-only change.

## React full unit/build and packed browser fit

Working directory: session vpsadmin-webui-async worktree. Full normal checks:

```sh
nix develop -c bash -c 'npm test && npm run build'
```

Then actual package proof, with exact committed source and retained runtime root:

```sh
nix develop -c env PLAYWRIGHT_BROWSERS_PATH=/tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/playwright-browsers npm run test:haveapi-package -- --package /tmp/2026-10-19-haveapi-async-client-implementer0-review.CFkmQj/remediation/package/haveapi-client-0.29.0.tgz --webui-ref fbf2a7f70f145a1bb87f659e68c84df0245448c3 --haveapi-ref dc94157808966c12418b4009085fec237a869789
```

Expected tar SHA256:
de55212e85ceb2bceac77e249272e20e1062afa8aa733df42e02eae981c094b8.
Exact source/package/browser preparation is in haveapi-review-inventory.md and
evidence/haveapi/package-receipt.json + browser-environment.json.

The proof isolates npm ci/candidate installation in a committed-ref snapshot,
checks actual package declarations/Vite output, and runs four adapter Chromium
cases plus raw-UMD callback+async XHR smoke in Chromium/Firefox/WebKit.
Record actual runtime versions and browser results; unavailable engines are
incomplete coverage rather than skips/pass. HTTP fixtures are synthetic; this
is not deployment, live OAuth or actual infrastructure completion evidence.

Keep logs/result.json/traces and report still-running operations. Source owners
own any resulting fixes. Re-check tracked tree/index after generated builds.
