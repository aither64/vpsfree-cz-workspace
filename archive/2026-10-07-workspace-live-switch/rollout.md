# Live-switch rollout

This record concerns only this deployment. It is not a reusable procedure.

## Baseline

Observed after another authorized initiative completed a workspace selection:
- system: /nix/store/zw4pi574kh9cmgx2wk8ab8hg9r25ibq6-nixos-system-aitherdev-26.05.20261006.b253099
- selected application: /nix/store/rr9rzzwcmpvhl2s75r21jb4gmnm4jq3j-dev-workspace-0.2.0
- running native: /nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0/bin/codex
- immutable launch package: /nix/store/yc881ddhy7sr4k2f59jfqwjq6b1wr4p3-dev-workspace-0.2.0
- Codex PID 1518065, invocation 799739960bab422391798302a83a40a4
- tmux PID 435397, invocation 23939798ce4d4b9d9af1e5f1d471f314
- portal PID 101132, invocation 6010f3692d9649788ae3b2c07901015e

Launch policy 1, argv [], capacity 0. Launch package has no live-switch policy,
so the first new-runtime switch must perform the authorized idle bootstrap.
Allow existing threads to finish naturally. Preserve retained generations and
never interrupt unrelated sessions or reset their ownership.

## Prepared sequence

1. Resolve committed independent review and execute packaged, exact-native and
   final feature-revision CI checks through fresh policy watchers.
2. Build aitherdev from the owned configuration feature worktree, then run
   confctl deploy --yes --no-interactive --dry-activate-first
   cz.vpsfree/machines/aitherdev switch in its Nix environment.
3. Switch application separately from the owned workspace source with
   workspace-host switch --source PATH. If installed command refuses because
   threads remain busy, use the normal guarded candidate entry to perform the
   bootstrap once they finish. Do not bypass refusals or alter lifecycle state.
4. Record actual selected system/application/native paths, service invocation
   IDs and immutable launch marker. Repeating a compatible application switch
   must keep Codex and tmux invocation IDs and refresh portal/router.
5. Fetch targets, verify final patch equivalence if rebasing, capture exact
   comparisons, integrate all three authorized masters fast-forward-only.
   Keep feature refs, session and owned worktrees available for follow-up.

Recovery remains forward-only: before selection the old package is restored;
after selection retry the selected candidate or a corrected newer package.
Pending records are ordinary runtime state, not manually edited recovery tools.

## Executed host deployment

Final configuration 7e744b49 built generation 2026-10-07--21-28-29. The normal
confctl deploy --yes --no-interactive --dry-activate-first command activated
that generation with switch and passed 2/2 health checks (systemd and firewall).
Exit 0. Before/after captures show Codex, tmux, portal and router retained their
service PIDs and invocation identities across this host-only deployment.

Application bootstrap completed through the normal guarded stable workspace-host
command against workspace 8163ff2e / runtime c51ba3c0 (exit 0). No idle,
identity, lifecycle or ownership checks were bypassed. The approved initial
cutover restarted Codex once and resumed terminal clients. Existing unproven
worktree warnings concern other initiatives; their ownership was not changed.

## Verified compatible switch

The next ordinary switch completed with exit 0 in 18.5 seconds. Actual selection:
- system: /nix/store/cd5wdjz1v9fji8c2hjlbd1wdgczhh05z-nixos-system-aitherdev-26.05.20261006.b253099
- application: /nix/store/a6c63h1ik2y4ghgn7gz53wn418mlq9qc-dev-workspace-0.2.0
- native: /nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0/bin/codex
- Codex PID 1204139, invocation 9907fe2769294bbfb05a020ffca4afc5
- tmux PID 435397, invocation 23939798ce4d4b9d9af1e5f1d471f314

Codex/tmux identities and all 291 terminal pane PIDs were unchanged between
after-bootstrap and after-live captures. Portal/router identities changed.
The complete launch marker hash was unchanged. Its actual launch policy is 1,
argv empty and required capacity 0; the launch package publishes
livePackageSwitchPolicy 1. This proves real profile-switch process continuity.
Busy-turn behavior and request/report recovery were checked separately in the
host tests and isolated native fixture; no full native MCP/terminal UI coverage
is claimed by this host observation.

The public HTTPS probe encountered the ambient curl trust store's missing issuer
certificate. Direct portal Unix-socket /healthz returned {"ok":true}. This was a
probe trust limitation, not evidence of an activation failure.

## Integration

All three approved master targets fast-forwarded to the exact deployed feature
heads and were pushed over SSH. Generic runtime c51ba3c0, workspace 8163ff2e,
configuration 7e744b49. Fresh remote fetches prove the exact heads merged.
Temporary detached integration worktrees were removed normally; feature refs,
initiative worktrees and session remain available. Post-integration master CI
37676621854 includes the host VM lane. The user explicitly directed "no waiting
for CI", so observation was stopped while the workflow continued in GitHub.
No master-CI success is claimed. Final feature CI 37673057916 passed, together
with the packaged checks, exact-native fixture and real deployment evidence.
