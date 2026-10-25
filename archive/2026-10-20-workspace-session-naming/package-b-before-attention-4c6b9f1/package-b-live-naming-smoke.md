# Post-deployment selected-provider naming smoke

Prepared for the lead's authorized post-activation verification under machine
ownership. **Not executed against the live backend.** The overlay was compiled
without running its test against exact A `4300c40b6406` (pass, 0.048s).
No source or product API change is required.

Use the final reviewed dev-workspace checkout matching the deployed candidate.
The current package B head is `4c6b9f177d5b205b21b45880c6ac1bc3c403eef6`.
If review fixes change it, use that exact final source/pin and repeat the cheap
overlay compilation before activation.

Run during a brief quiet window for new automatic-name requests. Ordinary
conversations may continue. Do not stop/restart either daemon or issue archive,
delete, session-create or session-cleanup commands for this probe. A busy naming
backend fails before inference; wait for existing naming to finish and retry.
Keep MCP/provider configuration unchanged through the call, as required by the
existing ephemeral utility contract.

## Post-deployment prerequisites

Use registered service identity `vpsfree-cz` (units
`workspace-portal@vpsfree-cz.service` and `workspace-codex@vpsfree-cz.service`).
The workspace filesystem remains `/home/aither/workspace/ai/vpsfree.cz`.
The portal executable, package flag and selected user profile must all agree
with the deployed candidate, and the ordinary daemon must be running.

Naming starts eagerly and asynchronously at portal startup. It performs its
version/provider prerequisites before launching one private native child; it is
not activated lazily by a session request. Portal HTTP health alone does not
prove this child is ready. Run discovery after startup settles. If it still
finds no owned child, inspect only the portal's naming prerequisite/exit status;
do not create a preparation, guess another socket or restart a service for this
probe. A child can exit after startup and has no automatic restart here.

The corrected read-only predeployment discovery found the existing owned child
and socket, recorded in `package-b-predeploy-discovery.json`. The old discovery
missed it because it enumerated only the main thread. That snapshot is current
runtime identity evidence, not final-candidate naming or activation acceptance.
Stale `naming-*` directories are not ownership evidence and are never adopted.

## Identity and invocation

`package-b-discover-live-naming.py vpsfree-cz` reads the running portal's own
flags and descendants, collecting children from every `/proc/<pid>/task/*/children`
entry. Go can launch a child from a non-main OS thread; scanning only the main
task misses it. Descendants are deduplicated before ownership checks. It requires
the portal package to equal the selected user profile, the child executable to
equal that package's native Codex binary,
and exactly one portal-owned private naming socket under `naming-*/app.sock`.
It checks private cwd, local-only marker and the package's startup catalog
argument. It reads the currently active provider through existing read-only
`workspace-host provider status`. Its JSON contains selected identity fields,
PID continuity and binary/catalog SHA-256 values; it emits no argv, environment
or credentials.

From the dev-workspace worktree, as the ordinary application user:

```sh
python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-workspace-session-naming/package-b-discover-live-naming.py vpsfree-cz > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-workspace-session-naming/package-b-live-backend-before.json

NAMING_SMOKE_BACKEND=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-workspace-session-naming/package-b-live-backend-before.json \
  timeout 60s nix develop --command go -C portal test -mod=readonly \
  -overlay=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-workspace-session-naming/package-b-live-naming-overlay.json \
  ./internal/web -run '^TestDeployedSessionNamingSmoke$' -count=1 -v -timeout=40s

python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-workspace-session-naming/package-b-discover-live-naming.py vpsfree-cz > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-workspace-session-naming/package-b-live-backend-after.json

python3 - <<'PY'
import json
from pathlib import Path
root=Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-workspace-session-naming')
before=json.loads((root/'package-b-live-backend-before.json').read_text())
after=json.loads((root/'package-b-live-backend-after.json').read_text())
assert before == after, 'profile, backend, provider or ordinary daemon identity changed'
print('Selected profile, naming backend and ordinary daemon remained unchanged')
PY
```

The lead/watcher should retain the Go output with these two JSON snapshots in
the rollout evidence. Discovery only reads live identities; run it after the
selected package and portal are healthy. A missing identity or provider is a
failed prerequisite, not permission to guess a socket or restart a service.

## What this proves

The overlay calls the existing production `namePreparation`,
`modelSessionNameWithRetry` and `modelSessionName` code using the deployed
portal-owned naming child and the currently selected provider. The production
client accessor controls retries. The real client's preflight additionally
checks the immutable catalog and startup `sessionFlags` origin, supported model
and isolation restrictions before inference.

It uses one original 30-second context, requires no pre-existing loaded naming
threads, and asks the actual provider to name this fixed request:

> Disable PHP session upload progress across the managed configuration and
> prepare deployment instructions.

Success requires outcome `model`, a valid generated name containing `php` and
one of `session`, `upload` or `progress`, under the shared deadline. The actual
name, elapsed time and provider are logged; assess the name's subject relevance
rather than requiring one stochastic exact phrase. Loaded naming threads must
be empty afterward. The client closes only its own connections.

The probe creates only temporary scratch state through the existing helper,
not a preparation receipt or registered session. Go testing removes that
scratch state normally. Native diagnostic logging retains its existing policy;
the fixed request contains no private user input. No persistent test-session
lifecycle cleanup is needed.

This is live naming/profile/backend evidence. The separately executed packaged
VM covers request admission, browser retry/manual controls, reservation and
session creation; it remains a distinct acceptance gate.
