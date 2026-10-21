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
