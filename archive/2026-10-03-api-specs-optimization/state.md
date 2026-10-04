---
lifecycle: complete
---

# API specs workflow optimization

## Current status

Merged into vpsadmin/master at6cda3e3667b1a4610d040f20566954f5c714c823.
Approved static 13-topic
implementation is coded, locally checked, independently reviewed, pushed and
verified by one complete baseline plus two complete candidate CI runs. All tests
and modes preserved. Default branch now contains the verified workflow. Production was not deployed.
Session remains open; feature refs/worktree retained. Automatic post-merge CI
is running; see integration.json for exact run IDs and captured status.

## Phase checklist

- [x] Historical investigation and independent proposal review.
- [x] Accepted static plan; verified same-session team/worktree; focused design.
- [x] Two functional commits, quick checks and all mandatory hooks.
- [x] Independent whole-branch review: all four lanes, no findings, no migrations.
- [x] Baseline +2 candidate CI;81jobs successful; exact example/outcome/dependency parity.
- [x] <=25-minute max-job target twice; measured queue/setup/wall/runner evidence.
- [x] Documentation, portal, exact base/head comparison and handoff reconciled.
- [x] Required checks inventoried: master unprotected, no matching protection rule or active rules.
- [x] Current master compatibility checked: unrelated WebUI update, conflict-free combined tree.
- [x] Explicit vpsadmin/master approval, patch-equivalent rebase, scoped hooks and atomic fast-forward push.
- [x] Exact remote master/feature heads confirmed; temporary integration worktree removed.
- [ ] Automatic post-merge CI completion (merge itself is complete).

## Branch, ownership and history

vpsAdmin canonical repos/vpsadmin.git; SSH git@github.com:vpsfreecz/vpsadmin.git.
Owned branch2026-10-03-api-specs-optimization and worktree
worktrees/2026-10-03-api-specs-optimization/vpsadmin.
Base/origin master:f9beb46e5206864bca9d37672e1419cf03661467, re-fetched unchanged
at final handoff. Complete functional series:

1. 0412a349edf31c0f2d516a189c27493a75b65366 — diagnostics/nativeJSON/environment
and stronger both-mode aggregate, original13 topics; controlled baseline.
2. 13b0e78f0932f280d77bef409fc6dc90237a5ca6 — approved static 13-domain rebalance
plus AGENTS/testing placement guidance; exact pushed/tested final head.

Final diff only .github/workflows/api-specs.yml, AGENTS.md and
docs/agent-instructions/testing.md. Source/index clean. Independent whole-history
conclusion: two legitimate retained functional commits, no obsolete approach,
fixup or unsupported transitional/compatibility path. No migrations, hence no
migration merge/release/deployment/external-use provenance obligations.
Exact base/head comparison saved with dev-session worktree capture-comparison.

User “Implement the plan” on2026-10-04 authorizes implementation/benchmark, not
master integration, production deployment or session closure. Weighted sharding
explicitly rejected. Retained identities/settings: architect0 Astra/xhigh/write,
implementer0 Sol/xhigh/write, reviewer0 Sol/xhigh/read_only; no overrides/fallback.
Architect owned focused design and session comparator; implementer all source
edits/quick fixtures/commit preparation; lead setup/normal hook commits/records/
CI evidence/acceptance. No unauthorized default-branch or external-settings edit.

## Results

See [CI verification](ci-verification.md), [timing data](benchmark-summary.json)
and [exact native parity](example-parity.json).

| Run / attempt1 | Wall minutes | Slowest test job | Runner minutes |
| --- | ---: | ---: | ---: |
| Baseline 37182100859 | 41.03 | 40.85 | 296.97 |
| Candidate1 37184185919 | 23.85 | 21.13 | 303.93 |
| Candidate2 37185470628 | 29.77 | 19.73 | 303.70 |

All 81 jobs passed with no retries/cancellations. Both candidates meet25-minute
max-job target. Wall improved41.9% / 27.5%; second critical DNS job waited9.88 min.
Native4,646 examples per mode/run, full 8 pending/core 404 pending, all identities/
paths/statuses/reasons identical. Same effective Ruby 3.4.11/Bundler 2.6.9/
RSpec 3.13.6 and lock fingerprints within each mode across all 3 runs. Source/test/
plugin/dependency inputs unchanged.415 eligible files exact once each mode/run.
No test reductions or new skips. Runner use about2.3% higher; queue/CPU variability
remain limits to extrapolating two runs as typical future duration.

## Verification and independent review

Both committed snapshots passed actual parsed-workflow selector/structure checks,
36 gate fixtures each (1valid+35negative), Actionlint1.7.12 with ShellCheck0.11.0,
YAML/Bash and whitespace. Six native formatter/environment/exit-status fixtures
pass; session comparator20 synthetic cases pass. Candidate workflow differs from
baseline only in matrix patterns/expected names; five unchanged domains verbatim.
Local reproduction selects actual committed patterns. Full logs/fixtures remain
local /tmp/api-specs-optimization-*; raw CI metadata/artifacts in ci-evidence/.

Mandatory retained reviewer0 gpt-6.1-sol/xhigh/read_only, all four lanes, medium bounded
CI-interface risk, full source series/final diff inspected independently.
No findings. Reviewer independently verified415-file partitions, scope, native
formatter and gate, check compatibility and explicit history/no-migration
conclusions. [Packet](implementation-review-packet.md), [review](implementation-review.md).
No source changes after review; CI completes its stated residual verification.

## Setup and environment constraints resolved

Member sandbox blocked Nix cache/daemon, RubyGems DNS/network and mandatory hook
DB sockets despite valid session/write access. Lead realized declared root/API
Nix environments, executed required shell hooks/dependency setup and normal
prepared commits from unrestricted declared root shell. All mandatory hooks
passed; no bypass, hook/config change or application edit by lead. First commit
had harmless72-column warning within required80limit; second no warnings.
Setup lesson: notes/vpsadmin/2026-10-04-api-specs-realized-shell.md.

Required catalog digest4676433c6831fbaca91da8ffde84891aff6ce065a17c74c2f367f1acf1d15b17
matches roster, native utility gpt-6-luna/low
dw_e866a6b603888eff4fc2fd19d1a7a9fddb2e25ed4f1e8fed. Exposed spawn schema lacks
native configuration selection; dev-session-monitor visible parent fallback
used, with owned handles/exact run IDs, bounded waits/output and regular updates.
No substitute watcher identity, unexpected kernel build or remaining operation.
Imported refs verified against official releases2026-10-04: checkout/upload v7,
download v8, ruby/setup-ruby v1 remain compatible/current.

## Documentation, adoption and next action

Approved [implementation plan](implementation-plan.md), [focused design](design.md).
Lasting static topic placement/artifact/aggregate/local reproduction instructions
are in vpsAdmin AGENTS.md and docs/agent-instructions/testing.md; session owns
benchmark/history/adoption evidence. Historical timings remain in investigation.md
and timing-summary.json; prior review.md is proposal-only. Initial coordination
commits 8bd7c4e7/ad539340 retained. One consolidated implementation/review/CI handoff
checkpoint is prepared under normal cadence; reproducible bulk logs uncommitted.

Required-check inventory resolved by follow-up read-only verification on2026-10-04:
REST master metadata reports protected=false, disabled protection, empty contexts;
GraphQL lookup of the exact master ref returns branchProtectionRule=null.
Active branch rules and rulesets including parents are empty. Detailed protection
endpoint still returns403; that error is not the absence proof. No enforced
required contexts need migration. Design's mapping remains useful if protection
is configured later. No settings or production change.

Fetched master is now f73f9a5e08358474191a4fb982bfc28312b2b7b9: one WebUI
dependency-update commit since the benchmark base. Prospective combined tree
38e09c20ad897694119534af5ad6e05af3a0657a is conflict-free and differs from
verified feature only in webui/composer.lock and webui/php-packages.nix.
All tested API/workflow inputs remain identical; no new suite run is warranted
by that update. Feature remains at verified13b0e78f, not rebased or merged.
Latest candidate's exact27jobs/attempt1 success was rechecked. Snapshot:
[Adoption verification](adoption-verification.json). Recheck target/settings and
perform the required patch-equivalent rebase when integration is authorized.
Next action belongs to user: explicit vpsadmin/master integration direction.
Keep session/refs open; rollback needs no production-data migration.

[Stable session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-api-specs-optimization/).

## Endpoint coverage follow-up

User asked how existing endpoint checks catch future additions. Inspected source
and retained candidate2 native results; no application changes or new test runs.
HaveAPI inventory check is retained in foundation, passes full, intentionally
pending in core.519 manifest entries covered, none pending; unknown/stale scopes
fail. Manifest accounting accepts explicit pending and does not prove actual
behavioral requests. It checks first API version; custom routes use a manual list.
Static file aggregate independently prevents omission of any new eligible tracked
spec. Details: [CI verification](ci-verification.md#existing-endpoint-coverage-checks).
Readiness unchanged: awaiting explicit vpsadmin/master integration direction.

## Integration authorization

2026-10-04 user explicitly instructed: "all right, merge it into the default branch".
Scope is the registered vpsadmin repository, default branch master. This supplies
integration approval under the workspace Git procedure. Lead will rebase the
reviewed feature onto current master, verify patch/input equivalence, run focused
final checks, capture comparison, and fast-forward push from a fresh temporary
target worktree. Production deployment, branch deletion and session closure are
not requested. Original reviewed/tested head13b0e78f remains recorded above.

## Integration result

User approval above applied to vpsadmin/master only. Atomic SSH push succeeded:
master fast-forwarded f73f9a5e0 ->6cda3e366; feature updated with exact lease
against13b0e78f. Rebase produced76bbced556ee8a24468d405b9b9ad09a2d5386dd
and6cda3e3667b1a4610d040f20566954f5c714c823. Range-diff marks both commits
identical. All reviewed API/workflow/dependency input blobs remain byte-identical.
No material edit or new review boundary; existing independent whole-branch review
and controlled three-run benchmark remain applicable. Comparison recaptured at
f73f9a5e0..6cda3e366 before integration.

Rebased workflow Actionlint/ShellCheck, both-mode415-file selectors and36actual
gate fixtures passed. Applicable normal Overcommit hooks all passed using
`nix develop .#vpsadmin -c overcommit --diff origin/master`. Initial broad
`bundle exec overcommit --run` was stopped after unnecessarily selecting all
tracked files; worktree remained clean, no tracked formatter changes. An invalid
single-hook CLI invocation also failed without edits. Root `bundle exec`
contaminated component hook startup with root Bundler state; API setup plus normal
direct Overcommit launch resolved execution. No hooks/configuration bypassed.
Logs remain /tmp/api-specs-optimization-rebased-*.log.

Fresh detached target worktree was fast-forwarded and pushed normally, then
removed with non-force git worktree remove. Feature branch/worktree retained.
All three final refs were confirmed equal after fetch. [Integration evidence](integration.json)
records exact remote heads and automatic post-merge CI IDs; master API run
37215684054 is starting. These newly triggered runs are not yet accepted as
successful. Session remains active/open pending automatic CI; no production
operation, archive/delete or feature-ref cleanup was performed.
