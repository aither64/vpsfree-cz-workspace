# Final composed deployment: read-only verification brief

Read-only continuity preparation; fresh local pre-switch metadata is saved in
`backend-successor/rollout-b3a6eb2f/implementer3-pre-switch-baseline.json`.
No endpoint checks, native RPCs, builds or activation ran for this brief.
Root owns the final operation release and acceptance. Keep the session
open and machine claim held; this brief contains no release or lifecycle action.

## Inputs required before execution

Accepted source/output bindings now come from
`backend-successor/rollout-b3a6eb2f/deployment-release.json` and
`backend-successor/composed-b3a6eb2f/{result,system-build-receipt}.json`, with their
retained full input/output graphs. Exact heads are A
`11ec57d2203fc735696fe75a837d47da55a5c6af`, B
`b3a6eb2fc0b41cf0cb965bf4c39991815d9df734`, W
`b1f0a0f758eabcab1ad281995177a06fb18d5a8c`, C
`bec5556f6c60414e482550dd735321ebe3c3703b`.

Prepared expected values, **not selected/deployed observations**:

- `FINAL_PROFILE=/nix/store/l9sc1ksacdkm7iij99ggyg87bqsp9n15-dev-workspace-0.2.0`.
- `FINAL_PROFILE_DRV=/nix/store/48n33d9ds4kssi4in9ijjaplr691bjaa-dev-workspace-0.2.0.drv`.
- `FINAL_SYSTEM=/nix/store/qs98vm7qhwz0fdn115yvkpw9a1md7h96-nixos-system-aitherdev-26.05.20261021.da6dc0e`.
- `FINAL_SYSTEM_DRV=/nix/store/mxa67hrjy8nfnhfip2n8q2qk9hsxn6l1-nixos-system-aitherdev-26.05.20261021.da6dc0e.drv`.
- Generation `2026-10-24--20-55-19`; W source
  `/nix/store/ka50bkd0b175d61xynjyx7shnz9np15x-source`, B source
  `/nix/store/igy5j2nx7n4andbi1ibfwd06jb93i5z6-source`.

Activation remains unauthorized in this release. Wait for root's successful
activation receipts and separate verification release. Native/tmux must survive
unchanged; ordinary router/portal/coordinator refresh is permitted. A changed
native executable is a release dependency conflict, not permission to restart.
Retain the release's existing preflight for exact old-target effects; this
continuity package does not repeat or reconcile them.

Old **observed predecessor**, not final expected output:

- Profile `/nix/store/1zkafvr6ns84wdmdh7qrmhx77c90wpxw-dev-workspace-0.2.0`.
- System/live system profile
  `/nix/store/hsi2mzws6j1wa153wf45i23ak7dvx50y-nixos-system-aitherdev-26.05.20261021.da6dc0e`.
- Native PID `3387667`, InvocationID `84b92a0a1c5a4fffa9a0c7beaf0693f1`, start
  ticks `1162579375`, UIDs `1000`, GIDs `100`, NRestarts `0`, executable
  `/nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0/libexec/codex/bin/codex`.
- App socket link `/run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock`:
  device/inode `77/121544`; target
  `/tmp/codex-daemon-1000/bced879de15a05f23836072b53ea2860aa13a982415f07bf83ab93a6ee8c9ea6`,
  socket device/inode `64769/18745722`; both ctime ns `1792318082724922848`.

These observations come from `incident2-prepared-plan/postactivation-continuity.json`
and `incident-network-permission/config-read-ws-once.receipt.json`; they were not
re-probed in this preparation. The latter also proves the same peer
`3387667/1000/100` around the consumed policy reload. Do not rerun that helper.

## Commands and expectations after root release

Use existing commands with caller deadlines: five seconds for local metadata,
ten seconds for each health GET, fifteen seconds per native metadata read. Save
exit/deadline categories and stop on a mismatch; no automatic retries. The command
forms below are prepared instructions, not executed results.

1. Recheck `dev-session current` and both bound environment variables. Read
   `dev-session coordination claim-status 2026-10-22-codex-thread-retries --as-is --id 201af6c8-08a2-48e6-be3e-b69ce916eee1 --json`
   before and after verification. Require owner
   `7cbe38cb-30c7-452d-8015-3907552c550d`, state `held`, exact resource
   `machine:vpsfree:aitherdev`.
2. `readlink -e` `/home/aither/.local/state/dev-workspaces/profile`, `/home/aither/bin/dev-session`,
   `/home/aither/bin/workspace-host`, `"$FINAL_PROFILE/bin/workspace-portal"`,
   `/run/current-system` and `/nix/var/nix/profiles/system`. Require the selected
   profile/commands to resolve through `FINAL_PROFILE`, both system links to
   `FINAL_SYSTEM`. `/home/aither/bin/workspace-portal` is absent; use the profile
   binary. `nix-store --query --deriver "$FINAL_PROFILE"` and the same query
   for `"$FINAL_SYSTEM"` must match the released derivers. Compare released graph
   and output receipts, rather than treating path selection alone as source proof.
   Hash `"$FINAL_PROFILE/share/workspace-portal/runtime-contract.json"` and
   `"$FINAL_PROFILE/share/dev-workspace/package.json"` against that final receipt.
3. For `workspace-router.service`, `workspace-coordinator.service`,
   `workspace-portal@vpsfree-cz.service`, `workspace-codex@vpsfree-cz.service` and
   `workspace-tmux@vpsfree-cz.service`, use:

   ```sh
   systemctl --user show "$UNIT" --property=Id,ActiveState,SubState,MainPID,InvocationID,NRestarts,ExecMainStartTimestampMonotonic,ExecMainStatus,FragmentPath,DropInPaths
   ```

   Require active/running, status 0 and only the root-approved restart changes.
   Resolve each fragment and `/proc/PID/exe`; compare unit and executable hashes
   with the final package graph. Router/portal must use the final portal binary.
   Ruby wrapper processes require their approved interpreter plus resolved unit
   launcher chain, not an assumption that `/proc/PID/exe` is the package itself.
   Preserve native and tmux PID/start/socket identities. Read only start ticks,
   UID/GID and executable metadata from `/proc`; no environment dump.
4. Prove persistent and live native FD limits independently:

   ```sh
   systemctl --user show workspace-codex@vpsfree-cz.service --property=LimitNOFILE,LimitNOFILESoft,FragmentPath,DropInPaths
   rg '^LimitNOFILE=' "$FINAL_PROFILE/share/systemd/user/workspace-codex@.service"
   rg '^Max open files[[:space:]]' /proc/3387667/limits
   ```

   Require packaged `LimitNOFILE=524288`, effective loaded hard/soft `524288`,
   and process hard/soft `524288`. Recheck PID/Invocation/start/exe and both socket
   link/target identities around these reads. The original live relief alone
   does not prove persistence; a new unit file alone does not prove live limits.
   No daemon reload, prlimit write or restart belongs to verification.
5. Reuse the existing local health forms:

   ```sh
   curl --fail --silent --show-error --max-time 10 --unix-socket /run/user/1000/dev-workspaces/vpsfree-cz/portal.sock http://localhost/healthz
   curl --fail --silent --show-error --max-time 10 --unix-socket /run/dev-workspaces/router.sock -H 'Host: vpsfree-cz.workspace.aitherdev.int.vpsfree.cz' http://localhost/healthz
   ```

   Require HTTP success and exactly `{"ok":true}`. These prove local handler and
   routing health, not authenticated browser/TLS acceptance or provider access.
   Naming has no separate health RPC here: inspect the approved new portal's
   child-process identities and its temporary `naming-*/app.sock` socket metadata.
   Match child executable to the final packaged native, parent to the final portal,
   cwd to that owned naming directory, and resolved catalog path/hash to
   `FINAL_PROFILE/share/workspace-portal/codex-models.json`. Project only the
   `--listen` and `model_catalog_json` argument paths if needed; never retain full
   command lines, provider arguments, environment or token-file contents. Child
   presence proves naming infrastructure only, not successful generated naming.
6. Preserve our exact root `01a162d6-1523-7633-88eb-804ced8a5e19` and roster34's
   six ready members: compare only address/thread/project/state/model/effort/access
   fields from `dev-session team list 2026-10-22-codex-thread-retries --as-is` with
   the fresh pre-switch projection. Do not save role instructions. Owner0/root
   supplies the equivalent ready metadata projection for replacement
   `2026-10-24-flake-update-downgrade-guard-replacement`, root
   `01a16da6-0939-78f3-98a1-9894df368ec8`, request
   `911b102e-c607-4a76-bbd9-20b35eced722`, receipt
   `f2445d7c103956f54a1129df9dc3d78bea9300ff8ddba15f409930973d6ab453`, attempt 1.
   Compare its four exact ready member identities with
   `incident-emfile-625e1f52/replacement-ready-final.json`; do not recreate it.
   For each root/member explicitly released for a native metadata check, reuse:

   ```sh
   "$FINAL_PROFILE/bin/workspace-portal" thread activity --socket /run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock --workspace /home/aither/workspace/ai/vpsfree.cz --user-state-root /home/aither/.local/state/dev-workspaces --thread-id "$RETAINED_THREAD_ID" --cwd "$RETAINED_CWD"
   ```

   This command uses `thread/read` with `excludeTurns:true` and emits only
   threadId/cwd/updatedAt. Require exact retained ID/cwd and a valid timestamp;
   ordinary concurrent activity may advance it. It performs no activation/send.
   Do not substitute `thread observe`, history/turn endpoints, session pages or
   creation-status GETs: observation reads history; creation status can reconcile
   and save receipts and includes initial request text.

## Receipt boundary

Use the existing deployment continuity receipt pattern, not a new framework.
Retain UTC, release/source/input/output hashes, expected versus observed paths,
scoped claim identity, unit/process/socket tuples, effective/live limits,
allowlisted root/member/replacement identity comparisons, naming infrastructure
metadata, health booleans and command exit/deadline categories. Keep configuration,
credentials, provider arguments, prompts/history and raw RPC/errors out. One compact
receipt plus hashes of existing final composed/activation evidence is sufficient.

`incident2-prepared-plan/check-live-continuity.py` is a source pattern only: it is
hardcoded to old releases/baselines and writes an old receipt; do not execute it
unchanged. No verification result in this brief proves provider reachability,
original incident cause, recovered old turns, successful naming or user acceptance.
Keep the machine/session open. Source owners and final operations remain under
lead control. The pre-switch loaded native unit may still report soft limit1024
while the unchanged live process has both limits524288; postactivation must prove
the new loaded soft/hard values independently.

Source anchors: `portal/internal/web/server.go:918`,
`portal/cmd/workspace-portal/naming_runtime.go:29`,
`portal/internal/workspacecodex/client.go:672`,
`portal/cmd/workspace-portal/main.go:809`,
`nix/systemd/workspace-codex@.service:7`, and
`docs/workspace-portal.md` live package-switch contract. No product files changed.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
