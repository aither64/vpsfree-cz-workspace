# Proposed parent activation command and observation contract

E4 preparation after accepted 0.31.1 source mapping. **This rebound template has not been executed.** Parent owns startup release and execution.
This adds a reviewable session-local wrapper around the exact public native
start. It changes no provider, OS, application source, canonical ref or host
configuration. Existing roots and stopped state remain intact.

Selected identities accepted by lead for this prepared command: runtime
`/nix/store/pq2jwjcv4hbyiwzcam50x6j9fv008qiq-dev-workspace-0.2.0`, provider
`/nix/store/vh650zaiazv3n8z12yf12pfbc951xwb9-vpsfree-dev-workspace-tools-0.1.0`.
Prior accepted fa7zlb/7vrkd bytes and hashes are retained in
`history/fa7zlb-accepted-activation/`; only identity constants were rebound.

Lead accepted the architect's clarification: a foreign `vpsfree:aitherdev`
physical-deployment/profile hold does not itself block this ordinary owned
QEMU startup. No guest claim, transfer or foreign release is appropriate. Any
actual collision, native refusal, changed input/generation or required host
configuration/profile action returns to lead. Earlier C residuals remain historical evidence. The final 0.31.1 source/checks
and effects handoffs were accepted separately.

## Gates before executing

Lead accepted the final A/C gates and canonical source mapping; before execution,
recheck exact session/generation, clean 9697/e468 heads, native OS f4e55a13, complete
accepted 20-node graph, schema/policy, config/tuple/pending state, available memory/CPU,
no overlapping legacy guests, and fixed-IP/native ownership observations.
The wrapper adds bounded identity/limit checks; it does not replace this fresh
lead preflight or independently accept a changed input graph.

No evaluation, build, network probe, scope or watcher was launched to prepare
this proposal. Only installed systemd documentation, native source and
read-only local resource settings were inspected before the latest no-probe
instruction. The wrapper has received static syntax and filter checks only.

## Exact parent-launched command after release

Run from the bound workspace in the parent, with an ordinary retained command
handle. Use a fresh attempt name for one intentional execution. Do not pipe
native output to tee or use an unattended mutation utility.

```bash
cd /home/aither/workspace/ai/vpsfree.cz
export DEV_SESSION_SLUG=2026-10-24-vpsadmin-haveapi-upgrade
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
export NIX_CONFIG="${NIX_CONFIG-}"$'\nmax-jobs = 1\ncores = 2\n'
e_attempt="$(date -u +%Y%m%dT%H%M%SZ)"
e_scope="vpsadmin-haveapi-upgrade-e-${e_attempt}.scope"
e_dir="/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-vpsadmin-haveapi-upgrade/devcluster/activation/${e_attempt}"
systemd-run --user --scope --unit="$e_scope" --expand-environment=no \
  --property=MemoryAccounting=yes --property=CPUAccounting=yes \
  --property=MemoryMax=32G --property=MemorySwapMax=0 \
  --property=CPUQuota=1200% --property=OOMPolicy=continue \
  python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-vpsadmin-haveapi-upgrade/devcluster/activation-driver.py \
    --execute-after-lead-release --scope "$e_scope" --attempt-dir "$e_dir"
```

This calls only
`vpsadmin-devcluster start 2026-10-24-vpsadmin-haveapi-upgrade --topology single --network bridge`.
It uses no `--existing`, `--force`, reset, private helper or automatic retry.
The execution flag prevents accidental ordinary invocation; it is not an
authorization source. Lead's release and fresh preflight remain necessary.

`systemd.scope(5)` says a scope has no main process and lives while any process
remains. Native `nohup setsid` changes process/session identity, not cgroup
membership. Thus the scope can retain the 32 GiB resident-memory ceiling,
zero swap allowance and 12-CPU scheduling quota over the driver, detached
runner and QEMU descendants after native startup returns. These properties
are checked from cgroup v2 before the native command. Actual descendant
membership must still be proved after boot and again after the parent returns.
No runtime deadline, timeout, scope teardown, stop, cleanup or trap is installed.
Do not stop the scope when handing off: doing so would terminate the guests.
An OOM or other abnormal scope state requires reconciliation, not a retry.

## Output and independent observation

[activation-driver.py](activation-driver.py) discards native stdout entirely:
successful native startup prints account values there. It streams stderr in
memory with bounded records and only emits structured store-path build/copy
events; all other native text is withheld. Exceptions never echo captured
content. No raw native log/config/status/URL output is copied into tracking.
The native provider's own private runner log retains its native location.

The fresh private attempt directory contains only sanitized `events.jsonl`,
`identity.json` (exact client PID/PGID and scope/cgroup), and `result.json`
(native exit status, withholding count). Files are mode 0600 in a mode-0700
directory. A new watcher, only after lead supplies the free slot, observes
these independent files; it does not launch/resume the mutation driver, edit,
diagnose, retry, signal, stop, or clean anything. Until identity exists, it
observes events or the parent's retained process status. Do not relaunch to
obtain a different tool handle, and do not use a second watcher while A owns it.

Accounting payloads use `scope_accounting` for counters; `scope` remains the
unit-name string in operation identity. This avoids duplicate keyword keys in
the initial and final event assembly. The failed 151600 attempt and its exact
prior driver bytes are retained in `history/pq2jwjc-activation-failure-20261026T151600Z/`.

Once `identity.json` exists, the observer may run this read-only command using
the exact recorded attempt directory and scope, without the execution flag:

```bash
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-vpsadmin-haveapi-upgrade/devcluster/activation-driver.py \
  --observe-only --scope "$e_scope" --attempt-dir "$e_dir"
```

It emits only allowed native status fields, source identity fields, scope
properties, process IDs/executable names/cgroups, runner tuple match, accounting
and any strict kernel-build path from the private log's bounded tail. It does
not dump process arguments, account fields or raw log lines. Normal progress
snapshots occur every 30 seconds. The utility owns bounded observation/waiting;
parent must not duplicate its polling. If that slot is unavailable at release,
use the documented visible parent-monitor fallback, never another utility.

Observation is incomplete until all of these agree:

- Exact native client exit 0 and parent/scope-launcher outcome recorded. Scope
  `ActiveState=active`, ControlGroup matching identity, MemoryMax=34359738368,
  CPUQuotaPerSecUSec=12s, cgroup `memory.max=34359738368`, `cpu.max` quota/period=12.
- Native stopped-to-running transition and ready=true, single/bridge, matching
  source provenance; exact runner PID's native four-flag tuple matches this
  workspace/slug/state/socket, and its cgroup is the accepted scope or child.
- All four expected QEMU guests and relevant helper descendants reside in that
  scope or children. Record actual process/cgroup evidence after startup returns;
  absence of a ready file or scope alone is not proof of complete boot.
- Native applied guest/system/root/seed/refresh proof and intended runtime
  0.31.1, API 7 and 9697/e468 identities agree. The wrapper does not establish
  application readiness, TLS trust or either actual PHP/React login/logout.

Escalate immediately on `HALT_REQUIRED_unexpected_kernel_compile`, ignored
Nix resource limits, nonzero native outcome, unknown command completion,
scope/runner escape, OOM events, readiness/tuple mismatch or changed inputs.
The wrapper reports but never automatically stops guests or retries.
For an unexpected kernel build, the parent must interrupt the exact owned
client build immediately after checking that no runner/guest was launched;
the persisted native PGID identifies that foreground operation. Any signal
requires verifying current ownership/process state first. If guests already
exist or interruption effects are uncertain, reconcile through lead before
any native lifecycle action. Do not signal the scope, use blanket process
matches, Ctrl-C the scope indiscriminately, or stop a foreign process.

## Separate Nix daemon load accounting

Daemon-backed builds are outside the user scope; its 32 GiB / 12 CPU cap is
**not a hard aggregate cap on the Nix daemon or total host activity**. The
command requests one local job with two build cores each, checks the client
settings before native start and reports ignored-setting diagnostics. These
are concurrency hints, not a daemon memory/CPU cgroup limit or a bound on
every build tool's thread count. No global daemon setting is changed.

Each baseline/30-second/final event records host MemAvailable and global
`nix-daemon.service` ControlGroup, MemoryCurrent, MemoryPeak, CPUUsageNSec and
TasksCurrent alongside scope memory/cpu/events. These daemon values include
other sessions; historical peak or baseline subtraction cannot attribute E's
own peak. Lead must schedule enough separate host headroom and avoid overlapping
heavy work, observing the aggregate during activation. A scope counter cannot
be presented as total-build consumption. If daemon pressure cannot fit that
allocation, return to lead instead of setting host policy or concealing it.

The final source/input and live-login verification receipt remains Package E's
later work. No session stop/reset/archive/delete or delayed cleanup is authorized.
