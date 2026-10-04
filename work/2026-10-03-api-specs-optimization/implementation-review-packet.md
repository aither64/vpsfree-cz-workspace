# Implementation whole-branch review packet

Session: 2026-10-03-api-specs-optimization. User authorized implementation of
static domain rebalancing; explicitly rejected dynamic weighted shards because
new feature/test placement should stay straightforward. No integration or
session lifecycle action is authorized. Read current plan/state/design and
implementation-plan; older review.md is proposal evidence only.

## Scope and acceptance

vpsAdmin branch/worktree `2026-10-03-api-specs-optimization`,
`worktrees/2026-10-03-api-specs-optimization/vpsadmin`.
Base: f9beb46e5206864bca9d37672e1419cf03661467 (fresh origin/master).
Final head and complete series are appended after candidate commit.

Two independently useful commits: instrument original thirteen topics with
native RSpec JSON/environment evidence and stronger both-mode coverage gate;
then apply static thirteen-topic partition plus developer placement guidance.
First head is retained as same-code baseline. These are functional changes,
not superseded designs/fixups. No migration changes, versions or merge/release/
deployment/external-use provenance exists. No transitional runtime paths.

Require all existing full/core tests and filters, isolated process/database per
job, 26 test jobs, current 60-minute timeouts, stable aggregate check. Native
JSON alongside readable output; mode-qualified seven-day artifacts; aggregate
requires successful matrices plus exact thirteen-manifest partition per mode.
No test moves, changed assertions/skips/auth work/schema/dependency inputs,
custom formatter/selector or timing-assignment framework. Long verification
must establish exact example ID/outcome/pending parity and matching effective
dependency fingerprints against baseline and two candidate runs; <=25-minute
candidate max test-job target remains unvalidated before those runs.

## Verification and documentation

Actual parsed-workflow selector/gate fixtures:
`/tmp/api-specs-optimization-check-workflow.py`, logs
`/tmp/api-specs-optimization-{baseline,candidate}-checks.log`.
Original/instrumented/candidate file sets derive eligible git paths (415 today,
never implementation hardcoded); both modes exact once. Actual gate success
and 35 rejection fixtures per snapshot; missing/empty/extra/duplicate/wrong-mode/
nested manifests, wrong expected names, unsuccessful matrix results.
Six actual formatter/metadata command fixtures pass success/failure/empty for
full/core; readable output, native JSON and nonzero exit status preserved.
`/tmp/api-specs-optimization-formatter-checks.log`.
Session-only comparator `compare-results.py --self-test`: twenty cases pass,
including shared-example definition paths, scoped identities/pending drift and
within/cross-run dependency mismatch. This is evidence tooling, not a shipped
application framework; current tracking/prototype records remain working copies
under the workspace tracking cadence.
Actionlint 1.7.12 with ShellCheck 0.11.0; YAML/shell structural validation;
normal mandatory Overcommit hooks. Final candidate results appended below.
Lead runs prepared normal commits from unrestricted declared Nix shell because
member sandbox denies hook database sockets; implementer owns source edits.
No bypass. First commit all hooks passed, harmless 72-column warning within
required 80-column max.

Lasting guidance changed in vpsAdmin AGENTS.md and
`docs/agent-instructions/testing.md`; session-specific benchmark/check mapping
and recovery remain in design/state. Docs entry point inspected.

## Risk and review ownership

Medium: bounded CI orchestration and compatible/reversible code, with changed
check/artifact interfaces. Lanes: general, architecture/repetition,
scope/proportionality, risk/compatibility. Retained eligible reviewer0,
gpt-6.1-sol/xhigh/read_only; exact saved settings, no override/fallback.
Read mandatory-change-review SKILL.md plus all selected references and all
applicable repository/workspace procedures. Perform review directly, no nested
reviewers. Give explicit whole-series obsolete-history and migration conclusions.

Workflow owns its static selection and gate; full/core share the matrix anchor.
Known consumers found by source search: workflow file-manifest aggregate and
AGENTS/testing guidance. No other tracked artifact consumer found. CI context
names are externally consumed by branch checks: five unchanged domains, network
retains name but narrowed coverage, other old topics map to new groups. Stable
`API specs - topic coverage` preserved. Classic protection lookup403, rulesets
empty: required contexts are unresolved rather than absent. No protection
changes or master adoption authorized. No production runtime, API/client,
protocol, persistent format, schema, Nix/deployment ordering change or VM test
required by this workflow-only scope. No dependency pin changes.

Long verification uses dev-session-monitor visible parent fallback: native
utility selection absent in exposed tool schema; do not claim native watcher.
No CI launched before review. Residual order/queue/runner-capacity risks need
controlled runs; review is not benchmark acceptance or merge approval.

## Final committed inventory and quick verification

Head: `13b0e78f0932f280d77bef409fc6dc90237a5ca6`.
Complete base-to-head series, oldest first:

1. `0412a349edf31c0f2d516a189c27493a75b65366` — ci: retain API spec evidence and validate both modes.
2. `13b0e78f0932f280d77bef409fc6dc90237a5ca6` — ci: rebalance API specs into thirteen static domains.

Final diff: `.github/workflows/api-specs.yml`, `AGENTS.md`,
`docs/agent-instructions/testing.md` only. No obsolete application approach,
follow-up fixup, unused runtime compatibility path or migrations identified by
lead inventory; independent explicit conclusion required. Baseline diagnostics
and static partition are both retained behavior, legitimate two-commit split.
API/plugin/package code, gemfiles/pins and Ruby-series input diff is empty
between baseline and candidate. Working tree/index clean after final commit.
Fresh canonical fetch still has origin/master at the recorded base.

Candidate exact patterns match design/docs; unchanged five domains verbatim.
Parsed workflows equal after removing matrix include and EXPECTED_TOPICS only.
Both snapshot selector/gate/lint checks pass; six formatter and twenty comparator
fixtures pass. Final normal lead Nix commit passed all pre-commit/commit-msg
hooks, no warnings. Logs `/tmp/api-specs-optimization-commit{1,2}-lead.log`.
Review whole branch directly, not just these reported checks.
