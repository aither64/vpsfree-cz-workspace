# Native provider fixture for b8a6be26a753

Prepared only from exact committed runtime
`b8a6be26a75347dcc9ec0fd1330dff886e47c93f`. The registered source is clean and
frozen. Wait for lead verification before actual execution. If the source head
changes, prepare another exact-head fixture. All older probes, including
`final-native`, remain unchanged evidence.

## Preparation checks

The static check environment is the cached declared runtime environment, with
GOMODCACHE=/tmp/session-webpush-mod, GOCACHE=/tmp/session-attention-go-build,
GOFLAGS=-mod=readonly and GOPROXY=off. From this directory's `source/`:

```sh
bash -n ../run.sh
node --check portal/internal/web/notifications_browser_test.cjs
python3 -c 'import ast; ast.parse(open("../run_native.py").read())'
sha256sum --quiet -c ../source-sha256.txt
gofmt -l portal/internal/web/notifications_browser_test.go
cd portal
go test -mod=readonly ./internal/web -run '^$'
```

The executable named by the existing tracking `xvfb-path.txt` is restored and
executable at preparation time. Presence was checked without launching it.
`preparation-checks.log/status`, `runtime-prerequisite.status` and
`preparation-summary.json` record the actual result. No Go tests are selected;
no TLS fixture, Xvfb or browser starts during these checks.

## Actual execution command, lead-owned

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/push-provider-probe/native-b8a6be26a753/run.sh
```

Use a fresh dev-session-monitor watcher or its visible fallback after lead
verification. The runner uses the existing cached tools, pinned browser bundle
and restored `xvfb-path.txt`. It verifies the source manifest and refuses an
existing `run/`. The retained Python child handle owns one dynamically allocated
Xvfb display through `-displayfd`, with TCP disabled, and reaps only that process.
Each engine uses a fresh disposable profile.

The Go diagnostic fixture and Xvfb runner are unchanged from the approved native
adaptation. Only the CJS source revision differs from `final-native`; its finite
diagnostic hostname list already matches the product's Mozilla/FCM/jmt17 hosts.
Exactly the two notification browser fixture files differ from the committed
archive. The actual shipped registration/deletion APIs, independent cleanup,
encrypted transport, guarded client, worker and `showNotification` remain
unmodified. Firefox retains its normal enabled push preferences; both engines
run headed. No endpoint is rewritten and no transport validation is bypassed.

The fixture starts only a sender ticker for the explicit Test action, never
activity reconciliation. After its ten-second delay is queued, all portal tabs
close while `about:blank` stays active; eighteen seconds later the harness
reopens and inspects generic provider status, real worker IndexedDB receipts and
real browser notification records. Those outcomes remain separate from OS and
macOS display, which this Linux virtual display does not establish.

Read `run/results.json`, `run/go-test.log`, `run/go-test.status`, `run/status`
and `run/runner-summary.json`. Owned Xvfb output and timestamps also remain
under `run/`. Exit zero means diagnostic completion, not delivery success.
Only public hostnames and bounded sanitized outcomes/counts are emitted, never
capability paths, queries, subscription keys, IDs or payloads. Cleanup uses the
committed shipped Disable action for its isolated registration/subscription,
then closes the owned browser and removes its fresh profile. No real session,
host, reservation or lifecycle action is involved.

`provenance.json` records exact source/archive identity and earlier artifact/run
checksums. `adaptation.patch` compares the fixture against this commit;
`native-increment.patch` shows the source-revision-only CJS change from the
prior prepared fixture. `source-sha256.txt` pins the complete source copy.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>
