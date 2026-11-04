# Active-session overview and evidence boundary

Lead inspection, 2026-10-31. Read-only observation; no peer session resources
were used as this session's work area.

The global portal endpoint `/api/index-status?progress=1`, read over the selected
workspace portal socket, returned an authoritative snapshot generated at
2026-10-31T14:06:13.612273614Z. It listed **116 unarchived sessions**, including
this investigation. Unarchived does not mean currently executing, and update
timestamps do not establish active model work.

Non-sensitive examples from the global overview:

| Session | Registered repositories |
| --- | ---: |
| 2026-10-24-vpsadmin-haveapi-upgrade | 23 |
| 2026-10-30-linux-cve-review | 1 |
| 2026-10-30-oomd-abuse-policy | 4 |
| 2026-10-30-reboot-recovery-fix | 4 |
| 2026-10-31-vpsadminos-archive-fix | 0 |

Counts show different coordination scope; they do not establish actual task
complexity, time spent or avoidable serialization. Zero registered repositories
does not mean no useful investigation.

The endpoint provides membership, timestamps, repository/cluster counts and
availability indicators. It exposes no lead/member working-time totals,
phase timings, runnable backlog or wait-for-lead measurements. Detailed clocks
are available through per-session endpoints, but this conversation's isolation
rules prohibit peer rosters, transcripts, worktrees and private session files.
No such endpoints or files were inspected; no peer leads were contacted.

Consequently this investigation can establish architecture and transport
constraints, but cannot independently quantify the user's reported imbalance
or identify its cause in these particular sessions. A follow-up measurement
pilot should run within each participating session's own authority and return
only approved aggregate evidence.

Source provenance and duration caveats are in
[measurement-findings.md](measurement-findings.md); transport evidence is in
[transport-findings.md](transport-findings.md). The proposed operating model is
in [design.md](design.md). No existing team was reconfigured.
