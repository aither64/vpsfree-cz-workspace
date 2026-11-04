# Optional local client cycle: proposed post-review command

Not executed. Requires the lead's operation release after affected committed
review and the current unique CI watcher has finished. Use one fresh Luna/low
watcher and the existing operation-local durable state/log/exit capture, with
status independent of watcher lifetime. This adds no helper or test harness.
Expected 3–8 minutes; stop at the first unexpected nonzero or input mismatch,
retain evidence and reconcile owned server effects before any retry.

Inputs:

- WebUI: `6c755ea2ba78c7ba8b27fe9e9731985903d67ce1`.
- Local client: `e16663a9e7ed1bbd7e25337b824283f635f47395`, clean tracked
  checkout verified read-only. Its existing TypeScript tool, runtime and built
  entrypoint are present; no build/install/pack has been performed by W.
- Already-realized Node24.21.0/npm11.19.0, Git2.54.0 and Python3.13.15 paths
  are in `w-local-client-commit-receipt.json`. Do not retry the failed Nix shell
  or repair inputs to run this operation.

Use the actual current local client rather than the unchanged99ee archive. A
client `npm ci`, explicit build and pack are necessary new execution steps in
this proposal, not previously completed preparation. They need the operation
release. No regeneration, committed artifact or dependency update is involved.

## Native preparation and override

Run from an ordinary Bash shell with the verified Node/npm/Git directories first
in PATH. The private session directory below must not already exist. These
commands are a reviewable batch, not a new script to install in a repository.

```sh
client_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/vpsadmin-typescript-client
webui_root=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/vpsadmin-webui
cycle_root=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/optional-local-client-6c755ea2-e16663a9
test ! -e "$cycle_root"
mkdir -p "$cycle_root/pack" "$cycle_root/webui"
cd "$client_root"
test "$(git rev-parse HEAD)" = e16663a9e7ed1bbd7e25337b824283f635f47395
test -z "$(git status --porcelain=v1)"
git rev-parse HEAD > "$cycle_root/client-revision.txt"
git status --short > "$cycle_root/client-dirty.txt"
rg --files --hidden --no-ignore dist | LC_ALL=C sort | xargs sha256sum > "$cycle_root/dist-before.sha256"
npm ci --ignore-scripts --no-audit --no-fund
npm run build
rg --files --hidden --no-ignore dist | LC_ALL=C sort | xargs sha256sum > "$cycle_root/dist-after.sha256"
cmp "$cycle_root/dist-before.sha256" "$cycle_root/dist-after.sha256"
git diff --exit-code
npm pack --ignore-scripts --pack-destination "$cycle_root/pack"
client_archive="$cycle_root/pack/vpsadmin-typescript-client-0.3.0.tgz"
test -f "$client_archive"
sha256sum "$client_archive" > "$cycle_root/local-archive.sha256"
git -C "$webui_root" archive 6c755ea2ba78c7ba8b27fe9e9731985903d67ce1 | tar -x -C "$cycle_root/webui"
cd "$cycle_root/webui"
sha256sum package.json package-lock.json packages/vpsadmin-typescript-client-provenance.json vendor/vpsadmin-typescript-client-0.3.0-99ee06654ef9.tgz > "$cycle_root/protected-before.sha256"
npm ci
rg --files --hidden --no-ignore node_modules/vpsadmin-typescript-client | LC_ALL=C sort | xargs sha256sum > "$cycle_root/installed-canonical.sha256"
npm install --no-save --package-lock=false --ignore-scripts "$client_archive"
```

The exact pack filename above follows the inspected current manifest0.3.0. If
its input changes, stop; do not choose a wildcard or a new version automatically.
Record the new archive digest and source/dirtiness separately from the retained
337414-byte99ee archive. The new README is part of this packed snapshot. Equal
`dist` digests do not imply equal archive bytes or generator revision changes.
Canonical WebUI `node_modules` remains untouched because all consumer installs
happen in the disposable Gitless snapshot. Such a snapshot is development input
with a recorded source revision, not clean release-provenance evidence.

## Consumer and forced-Vite legs

In the snapshot, run the exact entrypoint/actual peer snippet from
`docs/design/HAVEAPI_CLIENT.md` (it already passed on the existing committed
installation), recording output. Then:

```sh
npm run typecheck
npm exec -- vitest run src/lib/api/sdk.test.ts src/lib/api/sdk.wire.test.ts
setsid npm run dev -- --force --host 127.0.0.1 --port 5188 --strictPort > "$cycle_root/vite-override.log" 2>&1 &
vite_pid=$!
```

Before any request, save this owned new-session PID, `/proc` start ticks,
PPID/PGID/SID/CWD/exe and descendant Vite/listener identity. Confirm port5188
belongs to that group; if it was already occupied or ownership is ambiguous,
stop and report rather than signal another process. Observe readiness through
the owned log and a bounded local GET of `/src/lib/api/sdk.ts`, then follow its
actual optimized `vpsadmin-typescript-client` import URL and require HTTP200.
This proves forced dependency resolution; no UI/browser or backend request is
needed. Keep these nonsecret responses/logs with the operation receipt.

Stop only that recorded exclusive group with ordinary `kill -TERM -- -$vite_pid`,
wait for its native exit (0 or143 as applicable), and prove the root/descendants,
group and listener absent. On any failure, preserve its real status and perform
only the same already-owned native server teardown; never mark pass before
absence is proven. No background cleanup or broad process matching.

## Restore and second forced-Vite leg

```sh
npm ci
rg --files --hidden --no-ignore node_modules/vpsadmin-typescript-client | LC_ALL=C sort | xargs sha256sum > "$cycle_root/installed-restored.sha256"
cmp "$cycle_root/installed-canonical.sha256" "$cycle_root/installed-restored.sha256"
sha256sum package.json package-lock.json packages/vpsadmin-typescript-client-provenance.json vendor/vpsadmin-typescript-client-0.3.0-99ee06654ef9.tgz > "$cycle_root/protected-after.sha256"
cmp "$cycle_root/protected-before.sha256" "$cycle_root/protected-after.sha256"
```

Repeat only the documented entrypoint/peer snippet and the forced-Vite resolution
leg with a new owned PID and `vite-restored.log`, then the same native teardown
and exact absence proof. Record actual runtime0.32.0 and resolved entrypoint at
both stages. Do not repeat typechecking or the focused tests on restored inputs
unless restoration mismatches. Verify canonical source Git/index state stayed
clean and pinned files unchanged. Retain the disposable directory and receipts
for review; no deletion or session lifecycle action is part of this operation.
