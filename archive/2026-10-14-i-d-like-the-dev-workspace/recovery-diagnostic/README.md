# Recovery diagnostic preparation

Tracking-only evidence bundle owned by implementer0 for the accepted fixture-only
brief in [recovery-check-investigation.md](../recovery-check-investigation.md).
The source investigation is complete; the root cause is still unproved. This
bundle has not been run as a VM by the member. Lead inspection and one fresh
Luna/low watcher run remain separate steps.

Product `b8a6be26a75347dcc9ec0fd1330dff886e47c93f`, workspace pin `e6aaa9c7`
and configuration pin `c4fb5da4` remain unchanged. No source commit, product
change, deployment, live-host operation, lifecycle action or queue mutation is
part of preparation or the diagnostic command below.

## Exact source and package identity

The wrapper's locked `runtime` input is the original full Git revision from
the canonical local bare repository. Its dependency lock graph is the original
runtime graph, with follows paths prefixed by `runtime`. Static checks compare
every original locked/original dependency entry and input edge. The original
fixture and lock copies also match the source recorded in the original product
derivation:
`/nix/store/fpqzq6vs24m668g5fnddmhc0110vw248-source`.

The wrapper uses `runtime.nixosModules.host`, imports `runtime.inputs.nixpkgs`,
and takes `runtime.packages.x86_64-linux.dev-workspace` directly. The copied
fixture receives the original `runtime` as `self`. No diagnostic directory is
used as product source, and no `mkPackage` call is introduced.

Mandatory identities, recorded by the failed original flake evaluation:

| Item | Exact identity |
| --- | --- |
| Product output | `/nix/store/54cv3sm4z10nal6hi4p214vds9cmjddd-dev-workspace-0.2.0` |
| Product derivation | `/nix/store/77wgdsbc9ra6b23dd7w8kq3zk480zfyc-dev-workspace-0.2.0.drv` |
| Original recovery check | `/nix/store/62lvkrl2f6k82shyb6n4rii4myfmpy5k-vm-test-run-dev-workspace-session-recovery-boot.drv` |
| Runtime nixpkgs revision | `a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4` |
| Ruby interpreter | `/nix/store/nin40kn7prvsn7pmbl7k576hhwcpp9x1-ruby-3.4.9/bin/ruby` |

`evaluated-provenance.json` preserves the lead's initial successful evaluation.
`evaluated-provenance-final.json` identifies the inspected final diagnostic
derivation and observer. The wrapper asserts revision and product output before
exposing its one named diagnostic check. The runner also requires product and
original-check derivation equality and exact equality with the final evaluated
provenance. A mismatch stops before a VM build/run.

Each diagnostic input file is copied individually with `builtins.path`. Adding
logs or result files alongside the wrapper therefore does not change the probe,
collector or fixture input paths. This affects only diagnostic provenance; the
original product's source and derivation remain exact.

## Fixture changes

`fixture.patch` is the complete original-to-copied-fixture diff. The original
node configuration, synthetic provider, native package/services, registration,
and first foreign-cgroup scenario remain. The same UUID requests `pool`; the
same foreign `sleep` is injected into the native cgroup, waiting plus blockers
is required, that process is removed, and `applied`, active `pool` and all
original service checks remain required. Later deliberate failure and reboot
scenarios are excluded. Resource defaults and readiness/ownership timeouts are
unchanged. No session, browser subscription, delay or provider retry is added.

The probe and metadata collector are explicitly included in the VM closure.
After original setup and before the first request, the only new service setting
is `Environment=RUBYOPT=-r<probe>` in the fixture user's
`workspace-codex-provider@fixture.service.d/diagnostic.conf`, followed by that
user manager's daemon-reload. ExecStart, Restart, RestartSec and KillMode retain
their original values. No portal/shared-daemon or manager-wide instrumentation
is installed.

The observer requires argv exactly `run-provider-worker fixture`, host mode
`workspace-host` and UID 1000. It removes only its own require option from child
RUBYOPT; unrelated options remain. Each worker process emits a fixed active
marker. `TracePoint(:raise)` only records active original-package apply/recover
stacks; nested recovery takes precedence and waiting-loop exceptions are
ignored. Original exceptions continue to their existing rescues.

Records contain fixed labels, PID/sequence/monotonic elapsed time, direction,
allowlisted exception class or `OtherError`, numeric errno, and at most six
frames from the exact original provider/host Ruby files. Paths become fixed
`provider`/`host` labels and method names use a finite allowlist. The observer
never reads exception messages, arbitrary locals, argv, URLs, token files,
snapshots or RPC payloads. It performs no filesystem/process probes inside the
callback and makes no subprocess calls or product method changes.

All observer output is at most 64 lines per worker PID and 768 bytes per line,
including active/truncation/disabled markers. A direction/class/raise-site plus
provider-caller signature emits at most twice; the provider caller preserves
different helper steps. There is at most one truncation marker per process.
Internal observation failure disables the probe with a fixed marker if stderr
can still be written, and never replaces the original exception.

Unexpected terminal `failed`/`canceled` returns success from the polling shell
to Python, where the original expectation fails immediately. Waiting, applying
and recovery-required retain the original polling/deadline behavior. On failure
or timeout, collection reads at most 64 KiB total of journal output for only
the fixture worker/native units since scenario start, the six selected systemd
fields, and an allowlisted metadata/count projection. The snapshot and terminal
files must have fixed fixture paths, private regular-file/UID bounds and
matching schema/root/socket identities. Their contents are never dumped.
Collection errors cannot replace the assertion failure. Disposable VM cleanup
belongs to the original test driver.

Coverage is collected after the original assertions, with no pre-request timing
fence. On success only observer-prefixed journal records are retrieved; failure
coverage is derived from the same capped failure journal. The driver and safe
result summary distinguish `observed-no-raises`, `observed-with-raises`,
`missing-active-inconclusive` and `observed-partial-inconclusive`. Missing active
markers, disabled observation or truncation never certify complete observation.
Selected MainPID/NRestarts plus active PID markers allow the lead to assess
restart coverage. An infrastructure failure without the driver summary is
`not-collected-inconclusive`.

## Preparation checks

Exact member command (quick, no Nix daemon or VM):

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/recovery-diagnostic/quick-checks.sh
```

`quick-checks.log` records declared Ruby 3.4.9 syntax and synthetic subprocess
checks, shell syntax, locked-input/node/setup/scenario invariants, and static
Python compilation. Synthetic checks cover forward/nested recovery, errno,
original exception object propagation to its rescue, exact argv/mode guard,
waiting exclusion, unrelated RUBYOPT retention, per-signature/provider-caller
and process/line/frame caps, opaque unknown classes, secret-canary omission,
stderr failure isolation and fresh-process active markers. The UID rejection
case varies only the expected UID literal in the isolated synthetic observer;
this unprivileged member does not change its real UID or the VM's guard.

The lead acquired `flake.lock` and evaluated provenance using the declared Nix
environment. No member daemon bypass, product substitution or test run was
used. `INPUTS.sha256` fixes the complete preparation inputs; preserved original
log hashes are in `preserved-evidence.sha256`.

## One diagnostic run, lead watcher only

After direct inspection of this bundle, the lead assigns a fresh Luna/low
watcher to execute exactly:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/recovery-diagnostic/run-diagnostic.sh
```

The runner refuses an existing `run/`, verifies the input manifest and exact
evaluated identities, then invokes only:

```sh
nix build --no-link --no-write-lock-file --print-build-logs \
  'path:/home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/recovery-diagnostic#checks.x86_64-linux.session-recovery-diagnostic'
```

It preserves `run/provenance.json`, `run/check.log`, `run/status` and sanitized
`run/result.json`. It does not retry or run the original full flake. The watcher
must retain the skill's cancellation/escalation rules, including an unexpected
local kernel build. This command is prepared, not executed by implementer0.

A failed scenario with covered original raises can locate the failing boundary;
class/callsite alone may still leave a helper/protocol cause unproved. Terminal
failure without coverage is inconclusive. `applied` is a non-reproduction,
including when observation is complete. TracePoint overhead can change timing.
No diagnostic outcome makes the original failed suite pass or independently
proves the root cause. Any proposed remedy goes back through the lead.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>
