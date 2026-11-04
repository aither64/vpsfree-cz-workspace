# Profile browser-run server recovery

The orphaned test-server effects are reconciled. One SIGTERM was sent to
process group 691400 at 2026-11-01T23:37:19.547434+00:00. npm 691400, Vite 691415 and esbuild 691486
then disappeared. Workers 691592/691593 were already absent. No port 5187
listener or member of that process group remained after teardown.

Before signaling, exact PID start ticks, parentage, session/process-group
membership, source CWD, ordinary command identities and listener ownership
were verified and saved. The group contained only the three listed processes.
The npm parent had been adopted by user-systemd 1588. No matching same-source
Playwright runner or worker remained. The only other source-CWD process was
an older idle shell 1416176, with no children; it was left untouched.

The ordinary POSIX group SIGTERM follows the same group-signaling mechanism
supported by Playwright's graceful web-server shutdown. Repository configuration
sets no gracefulShutdown option. No private teardown helper was invoked.

Evidence:

- [Before snapshot](w-profile-owned-server-recovery-before.json)
- [Signal action](w-profile-owned-server-recovery-action.json)
- [After snapshot](w-profile-owned-server-recovery-after.json)
- Existing run log: `webui-browser-core-profile-fixed.log`

Verification result remains: focus **2 passed (20.8s)**; full A **INCOMPLETE**.
The core log starts 124 tests and has no terminal result. No rerun, source edit,
Git mutation, install, DB/API interaction, escalation or session lifecycle action
was performed. The lead owns any later verification launch and state summary.
