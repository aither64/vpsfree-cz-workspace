# Post-review verification watcher

This brief is prepared, not launched. Start only after the lead records final
review acceptance and the exact checked head. Use a fresh utility operation,
not a retained team member or previous watcher.

Read `/home/aither/.codex/skills/dev-session-monitor/SKILL.md`. Role: run only
the assigned verification command, retain logs/exit status, no source changes,
diagnosis, retries, acceptance decisions, deployment or nested agents.

Policy source:
`/nix/store/ad0s75irvrbj6pz6qk1zf7v9sy4l1qyp-dev-workspace-0.2.0/share/dev-workspace/agent-teams.json`

- Matching retained catalog digest:
  `ffaf9deb97720995ad1d662badae7645eba1fede5068eef529c9024efa7e7376`.
- `utilities.verification_watcher`: model gpt-6-luna, effort low, fresh operation,
  max concurrent one. Package execution_access full_access.
- Matching native utility config:
  `share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml`,
  name `dw_91978c240a6a43c2168b5be643cb58668a0bdf42d703ed0e`.
- Read/verify TOML: danger-full-access, never approvals. A standalone CLI must
  explicitly set both; native execution must verify corresponding policy.

Working directory: `/home/aither/workspace/ai/vpsfree.cz`.
Bound session: `2026-10-19-dynamic-python-api-client`. Verify dev-session current
matches before session-owned log writes; present DEV_SESSION markers must match.

Exact operation: lead supplies `HAVEAPI_REVIEWED_HEAD` and runs
`bash work/2026-10-19-dynamic-python-api-client/run-verification.sh` with that
environment. Never infer the head from a moving branch. Script checks clean
HaveAPI checkout and exact read-only vpsAdmin reference revision before work.
No registry publication or deployment command is included.

Keep driver stdout/stderr at
`work/2026-10-19-dynamic-python-api-client/verification/driver.log`, preserve
exact exit status in driver.status and each script-owned log. Report tested
head, elapsed time, result and bounded failure excerpt. Do not dump credential
or token-bearing manifests/envelopes. Normal fixture tokens remain private.

The batch starts current-source generic Ruby HaveAPI, builds and installs wheel/
sdist outside the repository, runs offline release checks, then serves actual
vpsAdmin with ephemeral MariaDB under its guarded bridge. The native harnesses
own loopback listeners/children/database cleanup. No node/VM/kernel build expected.
On unexpected kernel build, stop that owned operation and escalate immediately.
On failure retain evidence and return without retry; silence is not failure.
No arbitrary wall-clock deadline. If cancellation is requested by the lead,
terminate only this owned command/process tree using its normal signal cleanup;
never stop the development session or another operation. Session lifecycle
actions are not authorized.
