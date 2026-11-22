# Pi runtime on Aitherdev

The optional Pi host prerequisite and workspace application are selected separately.
The configuration's `dev-workspace` channel, role `devWorkspace`, must select the
same reviewed runtime as the workspace's nested `vpsfree-dev-workspace/dev-workspace`
input. Keep the existing native Codex package, provider and session identities.
Resolve effective per-machine inputs and package outputs before changing a channel;
root lock names and reported revision labels alone do not prove that identity.

## Host and workspace configuration

`services.dev-workspaces.piRuntime` uses the stable `aither` UID 1000 and state
root `/home/aither/.local/state/dev-workspaces/pi-runtime-host`. It installs the
non-autostart `workspace-pi-session@` template, immutable helper and session entry,
and sudo permission for that exact helper. The wrappers set both
`NIX_SSL_CERT_FILE` and `SSL_CERT_FILE` to
`/etc/ssl/certs/ca-certificates.crt` in their sanitized environment.

The `workspace-portal@vpsfree-cz` drop-in sets only
`DEV_WORKSPACES_PI_HOST_STATE_ROOT` and `DEV_WORKSPACES_PI_AUTH_DIR`; it does not
replace `ExecStart`. The latter names the owner-selected canonical Pi auth
directory. Configuration does not create or copy credentials. The workspace's
private Codex home and other workspaces keep their own configuration. A provider
catalog and login alone do not configure a custom Pi endpoint; the selected
application must include its reviewed model and endpoint composition.

## Installation and trial

Use the repository's declared shell and channel tools for the accepted exact
runtime. After final review, build the Aitherdev system through
`confctl build cz.vpsfree/machines/aitherdev` and build the matching workspace
application separately. Follow the installed coordination guide for the exact
machine reservation, dry activation and system switch, then select the workspace
application through ordinary `workspace-host switch`. An application build does not
install the host helper or activate either configuration.

Verify host/helper/sudo/entry identity and a newly initialized Manager, the actual
worker's PID/start and both CA variables, portal health, and existing Codex
settings and native identity before the separately authorized Pi UI trial. Preserve
original Accepted receipts and native history across reconnects and follow-ups.
An Unknown outcome does not authorize another send, click or session creation.

## Recovery and ownership

Keep retained package generations and the original recovery records. Pi state may
require a reader that older non-Pi packages do not provide; recover forward with a
compatible corrected package and the original operation. Do not assume that
selecting an old system or application safely rolls back Pi state. An unmerged
deployed trial retains its machine reservation until effects are settled,
deployment is verified, and the full deployed lineage is integrated into approved
remote defaults. Session lifecycle actions remain separately authorized.

The generic [Pi host contract](https://github.com/aither64/dev-workspace/blob/master/docs/pi-runtime-host.md)
owns helper, namespace, lock, invocation and recovery semantics. Exact trial
revisions, build results and activation evidence belong in session records.
