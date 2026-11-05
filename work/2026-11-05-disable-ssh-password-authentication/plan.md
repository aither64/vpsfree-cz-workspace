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

Quick shell syntax and mocked enumeration/configuration/restart checks, then
independent committed-deliverable review. Do not run the script on this host.
