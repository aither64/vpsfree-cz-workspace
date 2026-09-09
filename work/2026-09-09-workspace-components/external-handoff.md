# Independent CLI handoff

The current portal agent runs inside `workspace-codex@vpsfree-cz.service`, as
verified through `/proc/self/cgroup` and `systemctl --user show`. A restart of
that service can terminate the agent and commands it launched. The workspace
tmux server is also managed by a workspace user service.

Normal package activation restarts the router and portals. Codex replacement,
rollback, and some compensation paths restart the Codex services too. Busy
session checks should defer or refuse unsafe transitions, but the process
performing recovery should be independent of these services.

The same working directory is suitable for the independent controller. Start
it from a fresh SSH login to aitherdev, outside the portal's managed terminal:

```sh
tmux -L workspace-maintenance new-session -s component-split
cd ~/workspace/ai/vpsfree.cz
codex
```

Use a new standalone conversation. Do not attach it to the workspace's App
Server through `--remote`, and do not resume the existing managed thread.
Codex documents `--remote` as a connection to a selected App Server endpoint.
[OpenAI App Server documentation](https://learn.chatgpt.com/docs/app-server).

The fresh SSH shell avoids inheriting the managed session's `VPSFREE_*`
environment and service cgroup. Verify `/proc/self/cgroup` from a shell tool
inside the new agent before performing the cutover: it must not belong to
`workspace-codex@vpsfree-cz.service` or `workspace-tmux@vpsfree-cz.service`.
This local controller does not survive host reboot or loss of the host itself.

The following is a suggested opening prompt for the user to paste into that
instance. Pasting it explicitly assigns the existing initiative to the new
controller and overrides automatic managed-session startup for that controller:

> Continue initiative `2026-09-09-workspace-components` from this independent
> Codex CLI. Reuse its existing tracking directory and dated worktree group;
> do not create or attach a managed dev-session for this controller. Read
> `AGENTS.md` and the initiative's `plan.md`, `state.md`, and `assessment.md`.
> The portal conversation is idle and this CLI now owns implementation.
> I will supply the two new repositories' SSH URLs. Implement the agreed
> component split after settling the implementation plan. You may deploy
> aitherdev as needed. Preserve existing sessions and their identities, follow
> the workspace review and testing rules, and leave this initiative open.
> Deployment does not authorize integration into the configuration default
> branch, archival, deletion, or session stop.

The current user has already authorized aitherdev deployments and said they
will create the two repositories. No URLs have been supplied yet. This handoff
does not launch a controller, transfer the managed thread, or perform a service
or session lifecycle action. Avoid concurrent implementation turns in the
portal and standalone CLI after the user assigns ownership.

The assessment and updated tracking are in the shared working tree. The initial
plan/state commit is `58ccb4da27d6e1ef26c330662b2471d559d2c437`. Other sessions
have unrelated changes in the shared checkout; preserve them and keep all
functional development on the required feature branches/worktrees.

Stable portal URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-09-workspace-components/
