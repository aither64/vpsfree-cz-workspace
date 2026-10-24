# Focused retry presentation capture

Status: CONSUMED by capture-attempt-1 (failed before images). Do not rerun.
One operation only; no retry, diagnosis or source edits.

You are the fresh operation-scoped verification watcher specified in
watcher-policy.json. Read /home/aither/.codex/skills/dev-session-monitor/SKILL.md.
Verify dev-session current matches 2026-10-22-codex-thread-retries from
/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries; both
environment markers must match that session/workspace or both be absent.

Read applicable guidance at these exact paths:

- /home/aither/workspace/ai/vpsfree.cz/AGENTS.md
- /home/aither/workspace/ai/vpsfree.cz/docs/agent-instructions/verification.md
- /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace/AGENTS.md

Canonical tracking directory:
/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/ui-successor.
Read capture-plan.md and environment.json there. The sole authorized command is
`bash capture.sh`, from that tracking directory. It selects one actual-template
private Playwright fixture, not a live registered conversation. It performs no
model/provider/native call or deployment. Capture script has the explicit Go
240-second test deadline; do not add another timeout based on silence.

Run it once only after checking the exact final B head and clean status supplied
in the RELEASED footer. Write complete stdout/stderr and a JSON exit/elapsed
receipt under the attempt directory named in that footer. Preserve the actual
command exit code. PNGs are written under screenshots/ by the fixture. Do not
relaunch to gain a tool handle or retry a failure. Do not edit source, session
tracking, capture script, tests or dependencies. Your specified logs/results are
allowed. Do not wait for CI or run unrelated tests/builds/native checks. No
claims, cancellation of unrelated work, lifecycle, integration, activation,
deployment, release, acceptance decisions or nested agents.

Return passed/failed/incomplete, tested A/B revisions, exact command, elapsed,
log/result/image paths, bounded failure evidence and any still-running owned
operation. Parent owns diagnosis, fixes, rerun authorization and image acceptance.

RELEASED footer:

- A f86290673d752c77b56c70228c3d26aced75e177, tree0ed8092438d2f0a70838828573bbfd187b73393f.
- B480231f5127c69ae210f0d17796a57481cdc2e28, tree6f951eba4574836750d888238db605dca89c7dca, clean.
- B reviewed at39497062; one requested observer-line remedy accepted directly,
  documented review-findings.md. Full review review.md; no unresolved findings.
- Store command stdout/stderr/result.json in capture-attempt-1/ beneath the
  canonical tracking directory above. Create it exclusively; preserve all logs.
- Run `bash capture.sh` once only from that canonical tracking directory.
