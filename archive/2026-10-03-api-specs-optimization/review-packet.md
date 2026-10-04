# Review packet: API specs investigation and proposal

Scope: documentation-only read-only investigation requested by user. No
vpsAdmin application, spec, workflow or default branch changes. No new CI runs,
no deployment and no integration approval requested.

## Outcome and acceptance

Explain usual api-specs duration with actual completed run metadata; recommend
coverage-preserving faster parallel execution, distinguishing measured data
from estimated improvements and preserving both full/core plugin modes.

## Evidence and instructions

- Bound session: 2026-10-03-api-specs-optimization; workspace
  /home/aither/workspace/ai/vpsfree.cz. Verify dev-session current and env markers.
- Workspace AGENTS.md and docs/agent-instructions/{sessions,documentation,git,
  verification,commits,lifecycle}.md apply. Read full applicable guidance.
- Canonical read-only vpsAdmin reference: repos/vpsadmin.git origin/master
  148ef0eaed0459c825f1ba94b8dad2b9f3311b2f. Read local AGENTS.md and
  docs/agent-instructions/testing.md using git show before evaluating CI design.
- Session files: plan.md, state.md, investigation.md, design.md,
  timing-summary.json; raw metadata/logs are adjacent local evidence.
- Workspace initial tracking commit: 8bd7c4e7. Consolidated proposal checkpoint
  supplied in assignment. These are coordination commits on shared master,
  not an unmerged feature branch. No project base-to-head changes, migrations,
  pins, production states, superseded application approaches, or feature refs.

## Review selection

Mandatory-change-review skill at
/home/aither/.codex/skills/mandatory-change-review/SKILL.md; general lane only,
reference references/general-review.md. Documentation-only low risk; proposed
future implementation is not validated by this review. reviewer0 is retained,
ready, independent, read_only, gpt-6.1-sol/xhigh. No settings override/fallback.

## Verification completed

GitHub API sampled latest50 workflow runs and20 master runs. Fourteen successful
runs with job/step data (8 master Sep13–17,6 feature Sep25–Oct2); one failed run
excluded. Recomputed creation-to-final-job wall duration and job/step medians;
confirmed upstream master SHA via GitHub and canonical fetch. Checked docs and
JSON structure before checkpoint. No full suite/build needed for this proposal.

Check sample representativeness, arithmetic, distinctions between wall/job/step
and queue delay, alignment with source, coverage/isolated-state assumptions,
static partition and weighted-shard recommendations, and uncertainty labels.
Do not take estimates as measured future speed or assert a known organization
concurrency plan. No application documentation update needed until implementation;
unaccepted proposals belong in session records.

Reviewer must remain read-only and perform review directly without subagents.
Return findings, residual limits and review conclusion via team assign lead;
lead records your report. No lifecycle actions or CI launches.
