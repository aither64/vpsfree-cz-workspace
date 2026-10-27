# Environment-explicit successor, static preparation only

This replaces the unexecuted update portion of v1 after outer32148 refused
`Environment drift: LANG` in0.336s. Its summary/actual effects show exit1 before
SSH or Nix; no scoped-lock-update started receipt exists. The entire old packet,
accepted prepare, failed operation, parent disposition and original expectations
remain unchanged. `reused-evidence.json` binds all93 retained old files. No failed
directory is reused or altered.

The current workspace remains ef3227b6/treeb86da3d2 on3e72, with only the prepared
nested URL changed to c31. Its lock still selects44; index and all620 source
expectations are unchanged. `inputs.json`, `guard.py`, commit message and every
snapshot are byte-identical copies of v1. The historical `inputs.json.package`
field still identifies that original baseline packet; new destinations come only
from the successor script's own location. No tool/source/protected-file hash was
refreshed. Actual5dg/c31 NAR
`sha256-30kKzkA7kulWE3eBXlaMgG1ym+9lLuU3jdsfMOT5erA=` and the complete nine-node
graph remain the original accepted inputs, not values learned from a utility
environment.

## Explicit environment and future commands

Use only the literal argv/cwd in `ready.json`, through `launch.py`. This is new
static preparation, with no new execution authorization. Update and consolidation
require new parent release records naming the successor manifest and accepted
final vendor receipt. The old v1 release cannot authorize this new manifest.

The launcher first verifies its frozen package, caller session/envpair and every
original forbidden override. Any forbidden variable present in the caller fails
before normalization or a child command. It then constructs a child environment
from an explicit allowlist. Every nonnull bound value is set to the exact original
value, including PATH, LANG=en_US.UTF-8 and LC_ALL=C.UTF-8. Declared null values
are absent. The only optional caller values forwarded unchanged are SSH_AUTH_SOCK,
SSH_AGENT_PID and XDG_RUNTIME_DIR; their values are not logged. The verified session
pair and the original nonprompting Git/optional-lock/Python-bytecode overrides
are set explicitly. Other ambient variables are excluded. There is no broad
environment copy, live expectation import or silent clearing of forbidden inputs.
The original strict environment guard remains unchanged.

The launcher execs the pinned Python directly, preserving the operation's actual
exit and standard streams. `guard` invokes only the read-only URL-phase guard.
`update` invokes the successor runner. The sole Nix command is unchanged:

```text
/run/current-system/sw/bin/nix flake update vpsfree-dev-workspace/dev-workspace
```

The new runner has no prepare action. It verifies and reuses the actual accepted
v1 prepare summary, exact preserved ef ref/thin bundle and parentb893 assessment.
It never repeats fetch, ref creation, bundle creation or URL preparation. Update
still performs the original required fresh SSH gates around the sole Nix command;
all original source/index/tool/node/edge/follows/semantic and finite command guards
remain unchanged. Its new exclusive-create destination is
`workspace-consumer-c31-preparation-v2/effects-v2/update`. `runner-from-v1.diff`
contains the complete runner change. The launcher is a separate new file.

Consolidation remains a separately released phase. It requires actual SUCCESS
from **this successor's effects-v2/update**, matching newly generated file bytes,
normal hooks and same-base one-commit consolidation. It cannot consume the failed
v1 update. Its receipts go to new effects-v2/consolidate. Publication is held.

## Boundaries and reconciliation

This package grants no execution. Parent inspection/release and a fresh retained
Luna/low max1 utility remain required for the uncertain update. CLI/event output
does not substitute for actual effects-v2 stage logs/exits, summary, semantic
proof and file snapshots. No parallel observations or edits while it runs.

Bounds remain local guards30s, SSH90s, Nix update600s, normal commit120s and owned
command TERM/KILL joins5s each. New directories/logs are exclusive-create. No
retry, rollback, deletion, cleanup, new prepare, pin publication, checker, build,
test, eval, native/provider/VM, default/claim/deploy or lifecycle action is released.
Any failure retains its actual effects for parent reconciliation; the old failed
operation and accepted preparation are not modified.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
