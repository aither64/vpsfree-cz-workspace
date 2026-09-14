# Focused integration harness correction review

Owned session /home/aither/workspace/ai/vpsfree.cz/work/2026-09-14-kernel-history-fix.
Worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-kernel-history-fix/vpsadmin.
Read AGENTS.md and mandatory-change-review skill, general lane, gpt-5.6-sol xhigh.
No nested reviewers, code edits or external/lifecycle mutations.

All four required implementation lanes and final downstream pin general/risk
reviews completed. See review-reconciliation.md. The code, schema, RSpec tests,
repair contract and operational boundary are unchanged by this correction.

The actual local supervisor/runtime-ingestion scenario at pushed head
2a312616b0bf10465c33bbca97c79b31b22e8ec8 failed in its first two examples before
publishing any report. Both old legacy and new synthetic examples used `sv stop
nodectld` with test-runner timeout30, but sv itself timed out at 7.61 seconds.
Logs: /tmp/kh-sup.fC9MOb/os-test-supervisor__runtime-ingestion-737ba09b/node-shell.log
and test-runner.log. Other nine examples passed. The nodectld wrapper permits
60 seconds before escalating its child shutdown; its later ESRCH is existing
out-of-scope behavior, not changed here.

Correction: both stop/start commands use sv -w90, with runner timeout120. Move
stop into the existing begin/ensure blocks so even a failed stop attempts to
restore the reporter. This changes only tests/suite/supervisor/runtime-ingestion.nix.
No kernel or production daemon change, no real patch unload. Kept the correction
with the owning repair/integration commit by amend. Quick Nix parse, Nixfmt and
git diff --check passed; commit hooks run before final head below is appended.

Review only this small committed delta from old head 2a312616... to the new head
below. General lane rerun selected for a test harness correctness fix; other
lanes are unaffected because no design/contract/operational boundary changed.
New long local integration run follows this review. Downstream pins will move
to the exact final tested revision through confctl/canonical KB workflow,
consolidating each single pin commit and preserving all other locked inputs.

Report Blocking/Important/Advisory findings or no findings with remaining limits
to review-integration-waits.md in this tracking directory.

Committed head: b851ea971ed1cdcec2548395ec1ea493e8344cb6.
All hooks passed. `git diff old new -- api libnodectld nodectld webui nixos packages`
is empty; the sole delta is the 5 insertions/5 deletions in the integration file.
