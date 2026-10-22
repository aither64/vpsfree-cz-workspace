# Remaining dependency verification: checks 06–08

Prepared only; the lead launches a fresh retained-policy Luna/low utility after
accepting this handoff. Use full access and approval policy never explicitly.
Read the dev-session-monitor skill, workspace verification procedure, HaveAPI
AGENTS.md and doc/agent-instructions/development.md before execution.

Session: `2026-10-19-dynamic-python-api-client`.
Workspace: `/home/aither/workspace/ai/vpsfree.cz`.
Expected head: `a8ea3132e7efe601aaa8965afe648459b3dab5c5`.
Expected tree: `9a596258d912ca2075c36ded30d11b3984c656ae`.
Claim: `342cd062-0205-45c7-b636-20d958b8fa75`, held revision 2 when prepared.
The retained affected review accepted this exact head and complete four-commit
history with no findings and no migrations.

Execute exactly once, without editing the runner:

```sh
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-dynamic-python-api-client/run-dependency-final-three.py
```

Working directory:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-dynamic-python-api-client/haveapi`.

Runner SHA256:
`3090273be54d282df47317e2cf60325d7ca8e916c29ba8e67d762db8c936d21f`.

The prior continuation passed Go fixture setup, Ruby client (47 examples), Go
client (9 examples), and generic Python/Rack (59 tests). Its guard stopped
before check 06 because its workspace CLI package generation was superseded.
Checks 06–08 did not run. Earlier documentation and server RSpec checks also
passed. Preserve all original logs/status; repeat none of those checks.

This runner invokes the current stable `/home/aither/bin/dev-session` entrypoint
afresh for identity and claim guards, outside the project Ruby environment. It
does not pin an older selected-package executable, change runtime environment
selection, or retry a superseded invocation. A failed guard stops the batch.
Record and report genuine source, identity, claim or lock drift to the lead.

The only check commands, each through the ordinary declared Nix shell, are:

1. `06-python-package`: `nix develop .#client-python --command bash -euo pipefail -c 'cd clients/python; uv run --locked python utils/package_smoke.py'`
2. `07-release-check`: `nix develop . --command bash -euo pipefail -c 'make release-check'`
3. `08-release-test`: `nix develop . --command bash -euo pipefail -c 'make release-test'`

The runner preserves the prior frozen lock hashes, uses `BUNDLE_FROZEN=true` and
`PYTHONDONTWRITEBYTECODE=1`, and checks exact head/tree/cleanliness, hook signature
verification, identity and held claim before each check and after the batch.
It records the stable CLI entrypoint and its initial wrapper hash. Ordinary
Nix environments remain authoritative; no additional setup or dependency update
is authorized. Package smoke builds temporary wheel/sdist artifacts and removes
its own temporary directory; it performs no registry publication. Release check
and regression targets do not authorize a release.

New output directory:
`verification/dependency-refresh/postreview-final-three/` beneath the session.
Each check has a separate `.log` and `.status.json`; `batch.status.json` reports
the overall state. Existing batch/check evidence refuses overwrite. Own the
command/tool handle and observe these logs/status only. No parallel observer,
nested agent, retry, diagnosis, source/Git/trust edit, push, merge, version, tag,
registry operation or lifecycle action.

There is no timeout for quiet processes. Stop the owned process tree for an
unexpected local Linux kernel build; otherwise cancel only on explicit lead
instruction. On failure, preserve logs and report exact failed/unrun checks and
any known remaining owned processes/listeners. Parent exit alone does not prove
fixture children are gone. Do not terminate ambiguous or unrelated processes.

Save a compact `result.md` inside the new output directory, with tested head,
commands, exit status, elapsed time, check counts, log paths and remaining owned
operations. This result artifact is allowed; no tracking/source edits. Return
raw evidence to the lead without acceptance or publication decisions.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-dynamic-python-api-client/
