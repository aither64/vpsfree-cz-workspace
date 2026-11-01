# Selected-package idle-proof recovery review

Request bounded final review of the new committed rollout.md operational delta
from shared master 8d15118c9 to the current head. Same final reviewer and saved
Sol/xhigh settings; high risk, general/architecture/scope/risk lanes. Please read
all lane references and relevant workspace lifecycle/deployment procedures.
No application repository heads, package bytes, pins or native schemas changed.
Review report may be written to selected-recovery-review-result.md. No source
edits, live mutation, new subagents, full rebuild or retry.

Live failure: the ordinary switch selected candidate d0wikyzpr7, then nested
_activate repeated quiescence with the new private-home environment while the
old daemon still served shared-home rollouts. The exact archived retained team
proof failed with "Codex thread path is outside this authority's archive".
Old native PID156049 remains, portal is stopped, pending package/native state and
claim remain intact. No hookEntered, publication intent, copy or exchange exists.
The stock CLI has since reopened (PID307640) and its managed daemon; no force-stop
is authorized. Recovery must still wait for that CLI to exit normally.

Design addition is in design.md. One-time migration-host.rb loads the exact
selected installed Host implementation and prepends two narrow boundaries:
- dev_session_invocation: for quiesce --package-transition before publication,
  validate exact workspace, selected candidate, old launch marker, live native
  executable and home; pass source home to existing full execution/archive proof.
- system_env!: route only exact candidate/bin/workspace-host _activate through
  the same adapter, preserving its activation environment and ordinary state
  machine. All other calls pass through. After publication private home applies.

The Python runner selects this adapter only with the candidate already selected.
All lock, claim, journal, partition/inotify/fingerprint behavior is retained.
On retry current error is cleared while prior failure is retained in lastFailure;
switch.log remains append-only. The adapter is not installed in any project.
User explicitly authorized a one-installation migration; no generic migration
API/shared-home mode or lifecycle bypass is added.

Quick checks: 6 installed-host adapter fixtures/21 assertions pass (0.05sec),
16 partition/recovery fixtures pass; Ruby syntax and diff whitespace pass.
The user-installed Minitest6 masked Ruby's bundled mock helper; run the new
fixture with GEM_HOME/GEM_PATH pointing at the exact Ruby3.4.9 bundled gems and
MT_NO_PLUGINS=1. This avoids plugins loading both versions and yielding zero tests.
The live source-native/home/launch check passed read-only. The exact formerly
failing native require-execution-idle request now passes with source-home context;
no thread resumed or message sent.

Please assess the real nested package transition boundary and whether the
adapter preserves proof/forward recovery. Prior reviews stand for unchanged
partition source and all final application branches. No new SQL migrations or
repeated pin streams. Original operational source has now been executed to
selected-package/no-publication state and must retain this recovery lineage;
shared master history cannot be rewritten. After review, refresh only changed
private files from fenced source and restart the exact failed systemd unit.
