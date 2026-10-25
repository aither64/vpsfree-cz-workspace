# Verification utility assignment

You are a fresh operation-only verification watcher. Read
/home/aither/.codex/skills/dev-session-monitor/SKILL.md, then run only the
assigned local verification and observe listed CI. Do not edit application
source/tracking, diagnose failures, retry, publish, deploy, integrate or delegate.

Session 2026-10-22-haveapi-release in workspace
/home/aither/workspace/ai/vpsfree.cz; verify dev-session current before using
session-owned paths. Trusted parent session binding matches. Read HaveAPI
AGENTS/development/release guidance before running. The installed and retained
catalog digest is 840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa.
Utility policy gpt-6-luna/low, operation lifetime, full_access/never; matching
native utility config is
/nix/store/4cn1hh88xdpql5jp9pyrnf5fvnqsc829-dev-workspace-0.2.0/share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml.
Confirm launch full-access/never as inherited runtime policy before treating ready.

Current exact reviewed/pushed source:
08345b2d5ede025972a3daec8b4a373efb51d711, tree
3bd9df27413a1794bad5d8db27faca551cc3f79a. Working directory:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi.
Independent final review completed no findings before this operation. No source
or Git owner active. New API-example work is planning-only; no source edits.

Run exact command from that directory:

bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/verify-release.sh

Capture complete combined output to
/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/release-verification.log
and preserve exact exit status in release-verification.exit in same directory.
The script validates exact head/clean tracked tree/empty dist, enters declared
Nix shell, installs release deps, builds all release artifacts with Rust smoke,
runs full component tests, Clippy, npm/Python smoke and final manifest verify.
Stop on first local failure, collect bounded evidence, no retry/diagnosis.
No generic quiet timeout. Do not run registry publication helpers or read tokens.
Cancel only if unexpected local Linux kernel build starts, preserving evidence;
otherwise notify parent on escalation and retain unfinished operation ownership.

In parallel, observe these already-running exact-head GitHub Actions IDs in
vpsfreecz/haveapi; do not relaunch or rerun:
39805593028,39805592764,39805592862,39805592873,39805592810,
39805592842,39805592693,39805592701,39805592751,39805592804.
Use gh through existing environment or suitable Nix shell if absent. Verify
headSha before accepting conclusions. Save compact final statuses/failure logs
as release-ci-status.json/release-ci-failures.log in session directory. Do not
cancel runs absent parent direction. If CI fails, retain failure evidence and
notify parent promptly without waiting for unrelated local check completion.

Report result passed/failed/incomplete, exit status/CI conclusions, exact tested
head, command and elapsed time, log paths/bounded failure excerpts and every
still-running operation. No acceptance decisions. Return to parent automatically
when batch complete. Logs/results allowed; no session source/tracking edits.
