# One shared typed evidence collection

Authorized by lead after architect catalog acceptance and actual all111 declaration
validation. Read `/home/aither/.codex/skills/dev-session-monitor/SKILL.md` completely.
Watcher model/effort: retained catalog verification_watcher gpt-6-luna/low.
Native execution policy: danger-full-access, approvals never. No sandbox roots.
Catalog ffaf9deb97720995ad1d662badae7645eba1fede5068eef529c9024efa7e7376.

Verify `dev-session current` matches `2026-10-19-vpsadmin-kernel-cves`, with env
markers both absent or exactly matching this slug and `/home/aither/workspace/ai/vpsfree.cz`.
Working directory:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories`
Revision 69027fd51efc5c7eb0a4711947b4f9d08190940e plus all60 validated untracked
source dossiers. Collection catalog is frozen:67 options,7 sysctl names, Jan1 history.
No code edits, retries, diagnosis, commits, deployment or advisory writes.

Run exactly once, preserving exit status:

```sh
umask 077
mkdir -p .state
chmod 700 .state
nix develop --command bin/security-advisory collect > .state/evidence-collect.stdout.log 2> .state/evidence-collect.stderr.log
```

Collector writes ignored `.state/evidence.json`; stdout also contains raw private
Node evidence, so never print log content or copy raw material into session files.
Keep complete output restricted there. Record exit status and times in ignored
`.state/evidence-collect-result.json`; return only exit status, elapsed time,
snapshot existence/byte count/SHA256/mode and log paths. Do not print credentials,
API response bodies, Node/event records or raw stdout/stderr. For failure, return
sanitized error category only and let parent inspect restricted details.

No generic timeout; quiet collection is not failure. Do not relaunch, kill or
retry silently. Escalate unexpected build (especially kernel), auth failure,
collection failure or other concrete operation issue; parent decides remedy.
No cancellation authorized merely for duration/silence. Own execution handle
until final report. No nested agents. Leave session open.
