# 2026-11-05-disable-ssh-password-authentication

## Goal

I need an immediate script in vpsfree-maintenance-tasks that will update /etc/ssh/sshd_config on all vpsAdminOS containers on a node and disable password authentication (PasswordAuthentication no). If the change was made, restart sshd service. Use `osctl ct ls` to get running alpine containers. I need this quickly in order to workaround this issue https://sshhole.com/

## Affected repositories

- `vpsfree-maintenance-tasks`: one dated, node-local maintenance script and
  concise operator instructions. No configuration deployment or integration.

## Approach

Use the retained architect for bounded command/configuration investigation and
one implementer for the complete script package. Enumerate running Alpine
containers using `osctl ct ls`, set `PasswordAuthentication no`, and restart
sshd only when the configuration changes. Keep the script conventional and
small for immediate operational use.

## Decisions

- Corrective user request: ignore VPS whose configurations already disable
  password authentication. Preserve those files byte for byte, without backup
  or restart. Use a separate correction commit to preserve previously executed
  SSH task history. Keep the existing log insufficient for historical mail
  classification; do not infer prior enabled policy from a file rewrite.
- User clarified both tasks must be corrected: require original-backup evidence
  when choosing mail recipients. Prepare a read-only node reporting step and
  guarded mail input; missing/ambiguous evidence must not produce a recipient.
  Preserve the separate explicit user confirmation for manually fixed 30231.

- User addition: store the original `sshd_config` before modifying it. Preserve
  that original backup on repeat runs.
- User steering: execute the guest payload with `osctl ct runscript`.
- Follow-up: add a separate dated mail task, modeled after existing mail tasks.
  Email only active users with current running Alpine VPS explicitly recorded
  as changed or failed to mitigate in the supplied run log. Exclude unchanged-only
  and unlogged VPS. Keep the uploaded log outside version control. Prepare only;
  do not send mail in this session.
- Mail additions: key upload/deployment and remote console with localized KB
  links; original backup path; update system/OpenSSH and inspect logs. Latest
  copy steering: keep PasswordAuthentication statement simple and omit failed
  VPS from member-facing text, while retaining them for recipient eligibility.

## Compatibility and deployment

Only running Alpine containers on the invoking node are in scope. Password
logins will stop working; key authentication is the intended remaining access.
No database, protocol, API, or host configuration changes. Preserve existing
configuration where practical and document restoration. Preparing this script
does not execute it on a node.

## Documentation

Readers are node operators. Put invocation, behavior and recovery alongside
the script; keep investigation/review evidence here.

## Testing plan

Final mail eligibility correction: user checked all six failures; only VPS
30231 had password authentication enabled, and user fixed it and confirmed its
backup. Treat 30231 like script-confirmed changes; exclude other five failures.
Candidate evidence is 43 script changes plus 30231 before current DB filters.

Quick shell syntax and mocked enumeration/configuration/restart checks, then
independent committed-deliverable review. Do not run the script on this host.
