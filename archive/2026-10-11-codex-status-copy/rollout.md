# Executed deployment and recovery

Deployment succeeded on 2026-10-11, 17:25:38–17:28:01 CEST (2m23s). Accepted plan
authorized development deployment; it did not authorize merge. All three feature
heads remain unmerged. No schema, backend API, protocol or persisted state changed.

## Selection and execution

- Runtime: f145d3b8fa275932ee7837bba33568f29635d36f.
- Workspace: 51683b15ffb751174c4e0b875cfd4d1612f4755c.
- Configuration: 01c8350d0d07b7613c3893e5cd8666bface9c47b.
- Built host generation: 2026-10-11--17-23-39.
- Application profile: /nix/store/amvgyanpyfm37f12k1w9w5azhv4r8naa-dev-workspace-0.2.0.

Parent launched rollout.sh in transient user service
workspace-status-copy-rollout.service, invocation 5148597aaa994b32858c5b2bfabaed75,
initial PID512205. Fresh catalog Luna/low utility /root/monitor_status_copy_rollout
observed the existing exact operation. Atomic rollout.status=0, phase complete,
unit Result=success/ExecMainStatus=0. No operation remains running.

confctl deployed aitherdev with dry-activate-first, no-reboot and auto rollback,
then stable workspace-host switched the application user profile from its feature
worktree. The system pin selects matching module contracts and does not install
the application. Two host health checks passed: systemd running and firewall active.
Codex protocol and local semantic observation contracts passed. No unexpected local
kernel compilation occurred. The subordinate confctl full log was unavailable
at completion; the retained rollout.log records command, generation and health.

Before: /nix/store/mhf6xc33xh0hknhl992i29b52h612brb-nixos-system-aitherdev-26.05.20261008.7c8764b.
After: /nix/store/qi14qdh8wkp1k58nv06jbga6jlgk6ypw-nixos-system-aitherdev-26.05.20261010.6fcc160.
The scheduled upstream stable-nixpkgs update was retained. host-closure-diff.txt
shows the system/source identity and a small gh closure difference, with no kernel,
systemd, SSH or other package-version change. No reboot was requested/performed.

## Live verification

pre-deploy.json captured healthy services immediately before activation;
post-deploy-result.json proves the selected profile, exact served app.js/style.css,
versioned template and health. All four user services remain active/running;
Codex and tmux PIDs were preserved. Native root remains /nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0.
Candidate native executable and complete runtime contract match the predecessor.

GET/HEAD-only browser checks observed three idle member views while implementer0
worked, then the active implementer view at1280px/420px. Compact Working/peer labels,
full details, right-side counters, separator and narrow layout passed. Six peer and
two active work-row images were captured; representative wide/narrow images were
inspected. No prompt, roster or setting was written to the observed session.
See verification.md for the bounded live geometry evidence and controlled tests.

## Retained recovery

Keep clean feature branches and the candidate-package output root. Host recovery
uses the retained system generation under confctl's auto-rollback contract.
Application switches remain forward-only: repeat the same compatible switch or
select a newer reviewed package; do not select an older application generation.
Persisted state and transition contracts are unchanged. No archive, deletion,
session stop or branch removal is authorized by this rollout.
