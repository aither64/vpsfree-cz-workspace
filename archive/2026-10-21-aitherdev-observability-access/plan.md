# Aitherdev observability access

## Goal and authorization

User requested implementation of the accepted plan on 2026-10-21. Scope is
vpsfree-cz-configuration feature development, checks, review and feature publication.
No default-branch integration, production provisioning or deployment authorized.
User confirmed the machine key is manually in log root authorized_keys and owns
removing it after acceptance. Do not edit that file.

## Accepted design

Architect0 updates design.md before implementation. SSH uses the existing machine
key, no source-IP restriction, unprivileged log-reader shell, root-managed key,
no sudo/forwarding/PTY/tunnels/rc. Dedicated group reads root-owned remote/messages
logs and archives with persistent rsyslog/logrotate creation permissions. Reconcile
historical metadata only during an authorized rollout; preserve existing readers.

Metrics uses codex-aitherdev Basic auth with a random 32-byte secret (hex64),
bcrypt cost8, both mon1/mon2 /codex/api/v1 prefixes, exact query/discovery/diagnostic
endpoint+method allowlist and default denial. No source-IP bypass, raw9090 grant,
private routing/DNS changes or aitherdev system deployment. Runtime verifier is
/var/lib/nginx-auth/prometheus-codex.htpasswd, root:nginx0640 parent0750; client is
/home/aither/.config/vpsfree-observability/prometheus.curlrc, aither0600 parent0700.
Provision outside builds; no plaintext secrets in Git/Nix/argv/env/output. Document
curl -q --config use, atomic rotation and revocation; no custom client wrapper.
Apply shared 2r/s burst5, max4 concurrent, 64KiB body, connect5s/read30s limits.

## Backlog and ownership

| Owner | Expected result | Acceptance | Dependencies/checks |
| --- | --- | --- | --- |
| architect0 | Reconciled accepted design and brief | Replaces obsolete IP auth/root discovery | Before source edits |
| implementer0 | Logger account, persistent read permissions, ops docs, fixtures | Reads current/new/rotated logs; protected modifications/escalation denied | Architect brief; pinned shell/hooks; coordinate shared Git |
| implementer1 | Proxy query auth/policy/limits, provisioning docs, fixtures | Both backends; exact allowlist; absent/wrong auth denied; human auth retained | Architect brief; pinned shell/hooks; owns shared test registration |
| reviewer0 | Independent final review | All four lanes; whole history and no-migrations conclusion | All changes committed and quick checks pass |
| lead | Acceptance, records, publication and verification coordination | Evidence-backed branch readiness; no deployment claims | Reports; fresh utility watcher for long verification |

## Compatibility and recovery

No schema, TSDB/log format, protocol migration or fleet update. Preserve ingestion,
exporters, human admins, human monitor UI and Grafana. Group/ACL changes persist
across Nix rollback: save metadata before historical reconciliation. New routes
fail closed until credential provisioning. Revoke by removing the dedicated auth
entry and/or log key. Never restore root access automatically or delete logs/data.
Credential access is Unix-user-wide, not isolated per Codex session. Shell can
write home/tmp but cannot modify protected logs/configuration.

## Documentation and verification

Reusable operator documentation belongs in configuration docs/operations, linked
from the existing entrypoint. Exact revisions, review and results stay in state.md.
Quick evaluation/syntax and repository hooks precede final committed-deliverable
review. After final review, disposable behavior fixtures verify file denial,
creation/rotation, both backend routes, auth rotation and path/method rejection.
Long fixtures/builds/CI use a fresh Luna/low utility watcher. Build affected logger
and proxy configurations; no production destructive probes or activation.


## 2026-11-02 requested refresh

Rebase the registered configuration feature branch onto fresh remote default;
verify deployment docs are included and specific to vpsFree.cz. Architect0 owns
bounded doc gap/design brief, implementer0 owns rebase/docs/checks/commits and
publication. Preserve root-key removal and deployment as user-owned operations.
Accept old/new range-diff proof, quick checks, relevant independent final review
and changed-input verification. No new source behavior intended; do not broaden
this into a feature redesign or recreate test/provisioning infrastructure.


## 2026-11-02 operator simplicity correction

User asks clear concise log permission and Prometheus password setup commands,
and challenges excessive inline Python. Architect0 owns bounded reassessment;
one implementer will simplify existing pages, preserving runtime contracts.
Prefer interactive htpasswd and private local curl config over cross-host
provisioning automation. No production operations or feature redesign. Necessary
checks are snippet syntax and disposable provisioning behavior; docs-only changes
do not justify repeating unchanged VM/host builds. Independent final review of
committed operation guidance remains required.


## 2026-11-10 rebase and deployment planning

Prepare the current-default rebase and a concrete plan using newly available root
SSH to proxy.prg and existing logger access. Keep proxy outage to nginx reload or
brief restart; no longer outage. Read-only live preflight and local artifact/check
preparation are in scope. Activation, credential writes and historical permission
changes wait for execution approval of the prepared plan. Default integration
needs its own explicit approval. Assess whole candidate-vs-live system changes,
not only feature patch, and abort activation for unplanned unrelated disruption.

Updated documentation rules: repeatable service setup/recovery in existing config
operations guides; actual rollout revisions, closures, deployed generation and
results in this session. Preserve concise conventional htpasswd/curl setup. Do
not introduce a new provisioning framework or repeat old discarded complexity.


Nov10 user clarification: to the question about other non-root readers needing
current world-readable log access, user answered "No other readers that I know of".
Proceed with the selected log-readers group policy when execution is authorized;
new unexpected owners/groups/ACLs still require inventory review. Existing
exporter/FIFO access stays separate. This resolves the known-reader prerequisite,
not the distinct request to approve deployment execution.


## Execution and workspace usage guide authorization

User approved: "ok, deploy it and then once it is verified, the work can be merged."
Proceed with logger/proxy deployment, permission reconciliation, private credential
provisioning, live verification and then vpsfree-cz-configuration/master integration.
Keep the stated proxy outage bound; root-key removal remains user-owned.

User added workspace instructions for log reading and metrics queries, if absent,
and explicitly selected aither64/vpsfree-cz-workspace. Preserve config runbooks as
the provisioning/recovery authority. Put only short operational usage and discovery
links in the workspace, using an owned workspace feature worktree. No credentials
in docs. Workspace integration approval is assessed for that concrete deliverable;
do not silently add unrelated repositories to the configuration merge approval.
