# September 12 rebase and development deployment

All four retained branches are clean and pushed on the freshly fetched default
branches. The development cluster is running and ready on the bridge network.
The session, branches and worktrees remain open.

| Component | Revision |
| --- | --- |
| vpsAdmin | `a2e6d8037c737c61c15bfd845c1b3c57d894f310` |
| Notification templates | `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11` |
| KB contract | `6d8ab17db3ce8ffc41216feeb90bff8468b4d39d` |
| Configuration | `8928b2aba9230202e805aa5489dc9f7369650ac7` |
| Development-cluster OS | `15802517e2d92dda4ddc07ebac3d1d7ea087b430` |

All 41 recovery patches compare equal after rebase. The API tree changes only
packaged JWT from 3.2.0 to 3.3.0; the deployed package confirms 3.3.0. The
previous feature review and production deployment barrier still apply.

All seven configuration builds pass: both APIs, both WebUIs, the authentication
proxy, and both monitoring hosts. All declared hooks, 87 configuration specs,
strict MkDocs and the complete KB check pass. API and WebUI source and their
development bundles are unchanged from the preceding successful validation.

The repaired provider started services, both DNS guests and node1. The services
VM reports clean vpsAdmin `a2e6d803` / 4.2.1. API/recovery services, both DNS
bind/nodectld pairs, node osctld/nodectld and the active tank pool pass health
checks. This deployment did not compile a kernel locally.

The previous cluster database and disks were already absent before September
11. This startup retains the session's configuration and socket identity and
initializes VM disks under the same slug. It restores the established acceptance
TOTP, shared email and default WebUI OAuth client. Only test-user1 has MFA.

Live acceptance passes: neutral submission, grouped email with one eligible
link, TOTP, password change, ordinary sign-in confirmation, sessionless audit
history with client metadata, and captured security notice. There is one recovery
history event, no pending submission and no usable recovery authority. Core
schema `20260831220000` and the upstream payment index are present.

[KB Check](https://github.com/vpsfreecz/vpsfree-kb-contracts/actions/runs/34715979633)
and [KB runtime](https://github.com/vpsfreecz/vpsfree-kb-contracts/actions/runs/34715979634)
pass, including all four runtime suites / 12 scripts and the inherited Guix fix.
The five fast vpsAdmin workflows and
[API topics](https://github.com/vpsfreecz/vpsadmin/actions/runs/34715749822) pass.
[Full integration](https://github.com/vpsfreecz/vpsadmin/actions/runs/34715749842)
is still running; no failure is reported at the latest check. The user chose
to check its result later and waived waiting before this handoff. Only the
local status watcher was stopped; the GitHub workflow remains running.

The preceding intermittent local metrics-token HTTP 500 was not reproduced by
its diagnostic rerun or subsequent CI. Its root cause remains unknown; details
are retained in state.md.

Production deployment, integration into default branches and KB publication
remain outside this request. The development cluster is left running.
