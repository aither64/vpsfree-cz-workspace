# Archive VM hydration timeout diagnosis

Session evidence only. Implementer2 prepared this disposable overlay at the
lead's direction; it has not been built or run. The release repository remains
clean at `0fd31c1fa8858ef15d516e58c883f8dea9aa727e`. No runtime, timeout,
dependency, consumer pin or lifecycle behavior was changed.

## Observations

- Failed local derivation:
  `/nix/store/mvignikbxl14y861bckf3k87k8c87825-vm-test-run-dev-workspace-session-archive-lifecycle.drv`.
  Complete logs: [failed derivation](../failed-derivation.log) and
  [full invocation](../flake-check.log).
- The first browser call in “preflight lead repair survives portal restart
  before agent shutdown” timed out at the initial GET `/operation` hydration
  wait, before clicking Archive. There was no operation GET response in the
  retained list, no archive POST, no repair turn and no archive journal.
  Lifecycle-success cache invalidation therefore had not run.
- Initial page and asset response headers were 200, including conversation
  modules, reset credits and codex providers. No page error was recorded.
  An attention read succeeded; initial attention, notification and coordination
  reads were aborted. Attention/coordination scripts run independently of
  app.js; app.js does not await their promises.
- app.js awaits optional module imports before installing lifecycle controls
  and issuing its initial operation read. The existing trace records headers,
  but not request starts, body completion, pending requests or request times.
  It cannot prove that the last imported module finished downloading/evaluating,
  or distinguish a missing operation request from one still awaiting response.
- The browser command spans approximately guest uptime 161.5–240.8 seconds for
  a 30-second Playwright response budget. Concurrent local flake checks ran
  multiple VMs. This supports resource contention as a possibility; it does
  not establish the cause or certify that no intermittent product issue exists.
- Independent CI run [40398791893](https://github.com/aither64/dev-workspace/actions/runs/40398791893)
  passed fast, archive and creation checks at the exact same feature head.
  [Retained job evidence](../github-success.json). This is independent passing
  evidence, not an explanation of the local timeout or a repaired-rerun claim.

## Remaining uncertainty and next step

No product bug has been identified. The unresolved alternatives are late asset
download/evaluation under local VM load, an intermittent initialization stall,
and an outstanding operation request. The original trace cannot distinguish
them. Do not change production
modules, increase the timeout, refresh pins, or repeat the whole flake suite on
this evidence alone.

The copied browser driver records bounded request start/header/finish/failure
events with elapsed times, outstanding requests, console errors, document
readiness/visibility and completed resource/navigation timings on failure.
The Nix VM scenario and synthetic model are byte-identical to the original
immutable source; the application package and host module are the same exact
inputs. Node syntax and Nix expression parsing passed. The overlay is disposable
and is not a product documentation or source deliverable.

If the lead authorizes a targeted reproduction, a fresh verification watcher
can launch just this archive VM, without concurrent timed benchmarks:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/work/2026-10-26-workspace-cpu-investigation/package-checks/final/archive-hydration-diagnostic
nix build --no-link --print-build-logs --impure --file ./reproduce.nix
```

Stop after this targeted result. If failure recurs, use pending/finished asset
times to distinguish download delay from subsequent initialization, preserving
the failure before any further retry. A successful result supplies a targeted
pass only; it does not retrospectively explain the original stall.
