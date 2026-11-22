# User migration can leave absolute instance-unit links behind

During the `2026-09-09-workspace-components` aitherdev cutover, moving
`~/.local/state/vpsfree-workspaces` to `~/.local/state/dev-workspaces` left
systemd user-unit symlinks pointing at the old profile path. Template instance
links such as `workspace-codex@vpsfree-cz.service` also still pointed directly
at the old store package, so merely relinking the generic templates was not
enough.

The symptom was `203/EXEC` for Codex and tmux followed by a missing App Server
socket during profile activation. Verify every old link target exactly, disable
the affected instances, remove only the verified stale links, run
`systemctl --user daemon-reload`, and enable the instances again from the new
profile. The recreated links pointed at the selected `dev-workspace` package;
Codex, tmux and portal then started and both sockets appeared.

Related initiative: `work/2026-09-09-workspace-components/`.
