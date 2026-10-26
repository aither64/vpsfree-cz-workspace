# Prepared post-review campaigns

Prepared only. Neither command has executed; final independent review and the
lead's approval of the exact command remain required before a fresh policy
watcher owns each operation. Serialize the profiles through the one utility slot.

Candidate is exactly `ae60e0fdbc892d248c1cd4bff9a52ee74a0cfc43`, tree
`e83aff21574490a79282f58fc5cbe28bb2d8170b`, in the clean registered HaveAPI
worktree. [Preparation receipt](phase2-c-postreview-preparation.json) binds all
runner/comparator/budget/fixture/wrapper/workflow and prepared dependency inputs,
source graph, exact event data, command arrays, output paths and script hashes.
The manifest SHA256 is
`56f1d023fba0c5c50a9ab31d79107d67f270c44c624dea545c1b109a82bfb6d1`.

From the workspace root, the prepared entry points are:

```sh
bash work/2026-10-24-context-copy-performance-tests/phase2-c-postreview-quick.sh
bash work/2026-10-24-context-copy-performance-tests/phase2-c-postreview-weekly.sh
```

Each invokes [one supervisor](phase2-c-postreview-campaign.py), SHA256
`11614b603bd065ec846caadc46dfa66cdf954daf7cba3ae56241d220e759cacb`.
Python compilation and Bash syntax checks, including the embedded Nix command,
passed without executing the campaign. The supervisor refuses changed inputs,
wrong/dirty candidate checkout or existing output/source directories.

| Profile | Exact baseline | Local deadline | New evidence directory |
| --- | --- | --- | --- |
| quick | `39909094649b1d14a23f00615775ca7136acf4fd` | 600 seconds | `phase2-postreview-quick-ae60e0fd/` |
| weekly | `b85ec364057f536940d689b09e612512ffffaf82` | 1,800 seconds | `phase2-postreview-weekly-ae60e0fd/` |

Quick uses an explicitly labelled synthetic local feature-push event whose
captured default is the exact 3990909 baseline, reproducing whole-feature
selection. Weekly uses manual exact candidate/fixed-reference selection. Both
run D's actual `utils/performance_ci.rb resolve` then `run`; there is no direct
runner shortcut. The wrapper exports both exact sources, retains archives/trees,
matches dependency inputs, copies common locks, generates documentation and
captures the complete Nix shell/input graph before running the unchanged paired
policy. Both invoke the same prepared unbundled gem graph with preloads scrubbed,
locale C.UTF-8, timezone UTC, test Rack environment and JIT disabled.

The deadline starts before local preflight, Nix and wrapper preparation. The
actual command owns a new process group/session. At the profile deadline only,
the supervisor records members and sends TERM; after at most ten seconds of
shutdown grace it sends KILL if needed, then verifies remaining group state.
Deadline expiry is blocking exit 124, regardless of any partial runner outcome.
There is no retry, timeout budget extension or cancellation on quiet output.
Final evidence records the original process return code, signals/timestamps,
remaining descendants, exact whole-script elapsed time, unchanged inputs,
execution scripts/events/manifest and final clean source head/status. Grace
exists only to stop/reconcile an already failed timed-out operation; it cannot
turn the result into a pass.

The eventual watcher brief must explicitly authorize cancellation only at that
profile deadline and retain ownership if effects remain uncertain. It must use
the pinned Luna/low fresh-operation policy with danger-full-access/never, capture
the supervisor's exact exit and report without diagnosis, retry or edits.

After each run, C inspects raw/canonical output parity, every operation/query/
authorization result, all AA/AB samples and both timing classifications. No
missing report, preparation failure, inconclusive result or timeout is a pass.
The weekly runtime model remains tight and unproven; the measured profile and
hosted job limit are acceptance items. A review finding or final-head/input
change invalidates these exact prepared commands and requires a new receipt.

## Process observation safety

The read-only host probe found no unreadable stats or command lines at that
instant; earlier retained evidence had ten inaccessible processes. The supervisor
therefore treats observation errors as explicit uncertainty, including in its
finally path. It never counts unreadable processes as drained. Atomic operation
receipts record the spawned PID, UID, PGID, session and boot start ticks before
observation and final hash/Git collection. Signals require a positive matching
live member of that original session, with leader start-time protection against
PID reuse. Known foreign/reused membership withholds group signals.

An incomplete final observation records operation_running:null unless a live
member/root is positively known, ownership_retained:true and blocking exit3.
The watcher must report that receipt and retain ownership for parent diagnosis;
it must not claim slot release or schedule cleanup. Deadline-expired, completely
drained operations remain exit124. Any final hash/Git exception is recorded
without discarding the already durable ownership receipt.

[Safety checks](phase2-c-supervisor-safety-check.json) cover synthetic stat and
cmdline PermissionError, missing ownership/foreign UID/reused PID signal refusal,
positive-owned signalling through a mocked syscall only, empty-but-incomplete
non-drainage, and the actual finalization path with observer plus final-evidence
errors and a mocked child. That path exits3 with both receipts intact and
ownership retained. No child, campaign, real signal or source mutation occurred.

The original reviewed-head preparation is retained separately as
phase2-c-postreview-preparation-reviewed-head.json. This successor preparation
binds the narrow reviewed fixes and final clean source; no campaign has run.
