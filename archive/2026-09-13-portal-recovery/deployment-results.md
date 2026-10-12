# Deployment validation

Final package pins are in final-revisions.json. Deployment contract passes at
runtime 8f75ece30462b184065f21867508af5e14365c4a. All branches are feature
branches; no default branch integration is authorized.

Before deployment, live user package is
/nix/store/cgllc6zfnab06ah8w17izn4hmj80mhia-dev-workspace-0.2.0 (generation 35).
Live system is
/nix/store/jvi5n2bbp0li9w2xikh5kgwqnnzgy7g7-nixos-system-aitherdev-26.05.20260911.21a67dc
(confctl generation 2026-09-13--11-33-55). Recheck immediately before activation.
Codex remains pinned to 0.154.0. No state format or host module implementation
changes, and no migration is needed for rollback.

Provider nix flake check passed. Workspace deployment-contract flake tests
passed (3 runs, 14 assertions). Application package built:
/nix/store/71bnn9hribjb5p3hj655xyzq33wki98l-dev-workspace-0.2.0.
Packaged Go suite passed; Ruby suites passed 297 runs/2989 assertions and
73 runs/438 assertions (12 and 3 declared environment-dependent skips).
Aitherdev system built:
/nix/store/z2p1f0l5w1fbqm4k17ibn27yzwmyd82g-nixos-system-aitherdev-26.05.20260911.21a67dc,
confctl generation 2026-09-13--18-06-32. Dry activation passed. No kernel build.
Both browsers passed all 9 acceptance checks. All current-head CI passed.
User-profile switch selected generation 36 and the package above. Confctl switch
selected the built system generation, and both deployment health checks passed.
Portal, router and nginx are active. Codex retained MainPID 1090021 at version
0.154.0. Live checks verify 200 for authenticated pages/assets/thread, 401 without
authentication, named ready/heartbeat through nginx, and all five repository
totals. Live totals also exactly match local Git counts and net diffstats.
No rollback was needed; previous generations remain available. Branches remain
unmerged and the initiative remains active.
