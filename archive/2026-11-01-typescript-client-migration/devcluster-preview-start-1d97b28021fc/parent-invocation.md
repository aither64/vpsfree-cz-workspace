# Parent launch and independent observation

Prepared only; the capture has not run. Final WebUI HEAD is unresolved.
Parent must first accept W's committed review and final five Nix packages.

Run from /home/aither/workspace/ai/vpsfree.cz with the verified session environment
and accepted tool PATH. Substitute the actual accepted 40-character final HEAD:

    /nix/store/jy00n3jp5xj8s40n1fbldmkcr5n7avxc-python3-3.13.15/bin/python3.13 /home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/devcluster-preview-start-1d97b28021fc/capture-start.py FINAL_WEBUI_HEAD

The capture runs only:

    /home/aither/bin/vpsadmin-devcluster start 2026-11-01-typescript-client-migration --topology single --network bridge

It verifies session binding and clean exact WebUI/API sources before start.
It inherits parent environment and sets umask077. Keep normal current workspace
PATH (the vpsadmin-devcluster wrapper selects its own pinned dependencies).
No --force, retry, timeout, stop, reset or automatic cancellation is implemented.
Raw stdout/stderr is start.log (0600); it may contain development credentials.
The native provider runner.log inherits umask077. Never quote credential lines.

Independent Luna watcher: OBSERVE ONLY this operation. Do not launch the script
or any cluster action, probe another cluster, inspect unrelated resources, retry,
diagnose, accept, signal, or clean up. Watch start-state.json and start-exit.json
in this private directory; read bounded start.log progress only when needed.
start-state.json contains exact command/source/CWD, PID/start ticks/PGID/SID,
boot ID and capture PID; these establish identity independently of a parent's
tool handle. Match /proc/PID/stat start ticks and host boot ID when no exit
receipt exists. Native exit must come from complete start-exit.json. An absent
exit receipt plus vanished/mismatched native identity is INCOMPLETE, not a pass
or a reason to relaunch. In-progress JSON is not terminal evidence.

Notify parent promptly if actual Linux kernel compilation appears (not merely a
kernel substitution/download); parent alone manages cancellation of this exact
operation. Silence is not a timeout. Do not print full logs or credentials.
Report native exit, elapsed time, exact source identity, safe phase/error summary
and artifact paths. Exit0 proves only the standard start returned successfully;
the created runner is intentionally allowed to remain active. Parent routes
native-ready/exit evidence to i6 for bounded post-start acceptance. No duplicate
monitoring by i6 while this watcher owns observation.

Post-start i6 acceptance waits for parent evidence. Standard exact-session
status --json is filtered to nonsecret state/labels. Standard services SSH may
inspect the activated system, frontend/BFF package roots and safe build metadata;
no provider repair or DB/API mutation. Compare those packages/served files to
final immutable Git five-package results and honest path-source provenance.
Use cluster-CA-validated safe TLS /healthz, /build-info.json, /config.json and
logged-out session/login redirect/deep route. Credentials stay in private portal
account fields. Any actual login uses the ordinary documented OAuth flow; no
manual seed or credential creation. Report usable URL only after actual health
and authentication-path evidence, with remaining proof limitations explicit.
