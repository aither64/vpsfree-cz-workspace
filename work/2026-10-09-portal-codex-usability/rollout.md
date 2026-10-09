# Aitherdev rollout

Deployed and verified on 2026-10-09. The user authorized deployment via
vpsfree-cz-configuration. Default-branch integration remains unapproved.
All three actual resets remain available; checks used no live redemption POST.

## Exact sources

- codex-web: `860d515d0aa5d2f7ad68893db41f0969c78e00a7`
- dev-workspace: `675504f638d21578e87a94f460cc9cbf9e0df395`
- workspace: `5448392af308b64cd28af4c0c665d68cf81e18a7`
- vpsfree-cz-configuration: `081ac7cc6098f79b004f7ff349e71c85257b518f`

Extension source remains 0ff827df13e82dfab4b536ff29979280f264e8f5.
Host/profile composition check passes at runtime 675504f6.

## Predecessor and transition

Previous profile: /nix/store/a6c63h1ik2y4ghgn7gz53wn418mlq9qc-dev-workspace-0.2.0.
Previous host: /nix/store/cd5wdjz1v9fji8c2hjlbd1wdgczhh05z-nixos-system-aitherdev-26.05.20261006.b253099.
Native Codex 0.160.0 is retained by the compatible live-switch policy. The
portal/router restart and browsers reconnect; persistent formats do not change.
Forward-only recovery retries the same switch or selects a newer fixed package.
Do not force an older package or clear unrelated lifecycle/cluster state.

## Executed sequence

1. Packaged/provider/browser/runtime/workspace checks and aitherdev build.
2. Exact aitherdev confctl dry-activate, inspect changes.
3. Exact aitherdev confctl switch; verify host services.
4. workspace-host switch --source the initiative workspace worktree.
5. Verify selected profile, native Codex identity, portal assets and read-only
   live limits/credit count. No live redemption POST.

All five steps passed. The host switch used the exact built generation with
`--dry-activate-first --enable-auto-rollback`; both host health checks passed.
The stable `/home/aither/bin/workspace-host switch --source` command selected
the initiative workspace worktree and passed protocol/semantic compatibility
checks. The package transition used its existing forward-only recovery policy.

Selected profile:
`/nix/store/0krn8v92j23j0xdkia8l43iphsh4iwkk-dev-workspace-0.2.0`.
Selected host:
`/nix/store/pzhs0yvpcpsmami7gvrvdv1hx3yb47gx-nixos-system-aitherdev-26.05.20261008.7c8764b`.
Selected native Codex remains
`/nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0/bin/codex`.
Codex MainPID 1204139 did not change; the restarted portal is active at
MainPID 2002921.

Byte comparisons of the served app, reset controller, refresh, upload, sync
and conversation modules match the final source files. The session page serves
app.js?v=26. Read-only live limits report credits, `canReset: true`, three
available resets, three detail rows and three expiration dates. Reset IDs,
account scope and balances are omitted from this record. No reset POST was sent.
The public session URL verifies TLS with the configured public CA and returns
the expected HTTP401 without credentials. Private portal GETs return HTTP200.
The ordinary system CA bundle does not trust the private CA; see the existing
[local-CA note](../../notes/dev-workspace/2026-10-02-local-ca-portal-checks.md).

## Evidence

Read-only account check before deployment: selected App Server reports credits,
three banked resets and three detail rows. No redemption request was sent.
The installed old portal only reports windows, confirming the data was lost
in its earlier account presentation.

Initial independent review and focused lock rerun pass after four Important
findings were resolved. Provider CI run 37943560998 passed at 860d515d.
Provider packaged checks and all seven real-browser cases pass, including
native text paste and binary/mixed clipboard attachments.


Runtime exact-head CI37945562244 passed at 675504f6. Superseded current-day
runs finished; cancellation attempts were denied by token permissions and
no unrelated run was targeted.

All runtime fast package checks and composed workspace checks/build passed in
1,757 seconds. Host generation 2026-10-09--17-06-31 built successfully; 509
derivations, kernel and modules fetched from cache. No local kernel build.
Parent launched portal-codex-usability-dry.service with exact source guards and
atomic exit evidence under /tmp/portal-usability-deploy-evidence/dry/.
Dry activation exited zero. Parent then launched
portal-codex-usability-activate.service; host-switch, profile-switch and overall
exit statuses are zero. Activation completed in about 82 seconds. Complete
local deployment evidence is under /tmp/portal-usability-deploy-evidence/;
each mode has its own log, stage and atomic exit.status. Fresh Luna/low watchers
observed the parent-launched operations without deploying or retrying.
