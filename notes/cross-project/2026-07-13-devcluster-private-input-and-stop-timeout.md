# Dev cluster private input and stop timeout

Related initiative:
`work/2026-07-13-security-advisory-automation`

## Private flake input

The vpsAdmin development cluster uses the private
`vpsfreecz/vpsfree-sms-gateway` branch `2026-06-15-vpsadmin-events`. Nix's
unauthenticated GitHub archive fetch returned 404 although SSH access and the
branch were valid.

Create an initiative-local `vpsfree-sms-gateway` worktree at the standard
`worktrees/<slug>/vpsfree-sms-gateway` path. The devcluster tooling detects it
and overrides the private flake input with the local path; do not edit the
shared development-cluster flake for this case.

Verification: the cluster evaluated and built with the input shown as a local
`path:` source and reached `ready: yes` on the bridge network.

## Stop timeout

Stopping the running `2026-07-02-haveapi-i18n` cluster did not complete its
graceful shutdown before the tool timeout. The devcluster command then killed
the runner and removed its GC root, returned success, and a subsequent
`devcluster status` reported it stopped. Confirm status after this fallback;
do not assume a timed-out graceful phase means the stop command failed.
