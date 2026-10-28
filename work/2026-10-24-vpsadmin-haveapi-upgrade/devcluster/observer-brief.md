# Package E startup observer — fresh operation only

PREPARED, NOT LAUNCHED. Start only after lead assigns the exact parent-launched
attempt directory and scope; no earlier utility or conversation is reused.

Policy: retained catalog digest
`840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa`,
`utilities.verification_watcher`: `gpt-6-luna`, `low`, operation lifetime,
max_concurrent=1. Matching native utility:
`dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12`, configuration
`/nix/store/fqajxhsmaqg44pl8x2xshgn8q0bl7wr2-dev-workspace-0.2.0/share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml`.
The currently selected pq2jwjc catalog separately supplies full_access execution.
Both native TOML and explicit CLI policy are danger-full-access / approval never.

The observer receives only the following bounded prompt, completed with the
assigned directory/scope. It is not a team member or an activation executor.

> You are the fresh verification watcher for one already parent-launched Package
> E startup operation. Read `/home/aither/.codex/skills/dev-session-monitor/SKILL.md`.
> Workspace `/home/aither/workspace/ai/vpsfree.cz`, bound session
> `2026-10-24-vpsadmin-haveapi-upgrade`; verify current/env before observation.
> Parent owns the mutation driver. Do not start/resume/retry a build, driver,
> cluster or any mutation. Do not delegate, edit sources/tracking/config, install,
> signal, stop, reset, release, clean, approve, diagnose or inspect foreign records.
>
> Observe only the assigned attempt's sanitized `events.jsonl`, `identity.json`,
> `result.json` and the prepared driver's `--observe-only` command for that exact
> directory/scope. Never use its execution flag. Follow
> `devcluster/activation-command.md`'s observation contract. Keep reads bounded
> and normally wait 30 seconds between progress observations. Do not dump raw
> native stdout/stderr/logs/config/status/URLs, process arguments or credentials.
> The prepared read-only command provides allowed status/cgroup/tuple and bounded
> private-log kernel-path evidence; do not bypass it to inspect raw runner logs.
> In event payloads, `scope` is the unit-name identity; counters are under
> `scope_accounting` and must not be confused with that string.
>
> Report immediately on HALT_REQUIRED events, nonzero native result, OOM events,
> cgroup/tuple/source mismatch, escaping guests or uncertain completion. No signal
> or cancellation is authorized for the observer. If startup remains in flight,
> notify the parent and retain observation until parent responds or the exact
> operation completes. Quiet output alone supplies no deadline or failure.
>
> Complete observation when the native result is recorded and reconciled, or
> parent explicitly ends this observation. Success requires native exit 0,
> ready=true, active exact scope with 32GiB/12CPU limits, exact native runner
> tuple in that scope and all four expected QEMU guests resident there. Capture
> actual evidence and limitations; do not infer application/login/applied-root
> acceptance from these fields. Parent/implementer3 owns later runtime proof.
>
> Return a compact result: passed/failed/incomplete; exact attempt/scope/client
> PID, native exit and elapsed time; allowed readiness/tuple/cgroup/resource
> evidence; artifact paths; any escalation or still-running operation. Save only
> sanitized observer artifacts under the assigned attempt. Never stop the scope
> or guests at completion. No lifecycle action is authorized.

## Launch command template, only after assignment

The assigned `E_ATTEMPT_DIR` and `E_SCOPE` are nonsecret identifiers. The caller
must substitute them from the parent's actual identity file. This is a fresh
standalone `codex exec`, without resume/fork or another watcher. The native
utility's exact developer instructions are loaded as one structured argument;
retained model/effort and current execution policy are explicit.

```bash
python3 - "$E_ATTEMPT_DIR" "$E_SCOPE" <<'PY'
import json, os, shutil, subprocess, sys, tomllib
from pathlib import Path
root = Path('/home/aither/workspace/ai/vpsfree.cz')
slug = '2026-10-24-vpsadmin-haveapi-upgrade'
attempt, scope = Path(sys.argv[1]), sys.argv[2]
assert attempt.parent.resolve() == (root / 'work' / slug / 'devcluster/activation').resolve()
identity = json.loads((attempt / 'identity.json').read_text())
assert identity['scope'] == scope
assert os.environ.get('DEV_SESSION_SLUG') == slug
assert os.environ.get('DEV_SESSION_WORKSPACE') == str(root)
retained = Path('/nix/store/fqajxhsmaqg44pl8x2xshgn8q0bl7wr2-dev-workspace-0.2.0')
current = Path('/nix/store/pq2jwjcv4hbyiwzcam50x6j9fv008qiq-dev-workspace-0.2.0')
assert Path(shutil.which('dev-session')).resolve() == current / 'bin/dev-session'
catalog = json.loads((retained / 'share/dev-workspace/agent-teams.json').read_text())
assert catalog['catalog_digest'] == '840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa'
policy = catalog['utilities']['verification_watcher']
assert (policy['model'], policy['effort'], policy['max_concurrent']) == ('gpt-6-luna', 'low', 1)
selected = json.loads((current / 'share/dev-workspace/agent-teams.json').read_text())
assert selected['execution_access'] == 'full_access'
entry = next(v for v in catalog['native_agent_configs']['utilities'] if v['utility'] == 'verification_watcher')
native = tomllib.loads((retained / entry['path']).read_text())
assert native['name'] == 'dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12'
assert native['sandbox_mode'] == 'danger-full-access' and native['approval_policy'] == 'never'
brief = (root / 'work' / slug / 'devcluster/observer-brief.md').read_text().split('## Launch command template')[0]
brief += '\nAssigned exact attempt: ' + str(attempt) + '\nAssigned exact scope: ' + scope + '\n'
brief += 'Read-only observation command: python3 ' + str(root / 'work' / slug / 'devcluster/activation-driver.py') + ' --observe-only --scope ' + scope + ' --attempt-dir ' + str(attempt) + '\n'
args = ['codex', '--ask-for-approval', 'never', '--sandbox', 'danger-full-access',
        '-c', 'developer_instructions=' + json.dumps(native['developer_instructions']),
        'exec', '--model', policy['model'], '-c', 'model_reasoning_effort=' + json.dumps(policy['effort']),
        '--json', '-C', str(root), '-o', str(attempt / 'observer-final.txt'), '-']
os.umask(0o077)
with (attempt / 'observer-events.jsonl').open('x') as events:
    result = subprocess.run(args, input=brief, text=True, stdout=events, stderr=events, cwd=root)
sys.exit(result.returncode)
PY
```

Retain the launcher handle and observe its final artifact independently. Do not
run this template during preparation or before checking the sole watcher slot.
