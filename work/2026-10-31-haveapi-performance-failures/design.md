# HaveAPI performance failure investigation

Investigation only, 2026-10-31. No application/workflow changes, CI reruns,
test campaigns, integration or deployment were performed.

## Finding and evidence

Current GitHub `master` is `0e7166a0f8f15827bfac051666a53bf449e999ec`.
The failure at this SHA is a deterministic event-selection error on creation of
`haveapi-0.32`; no performance measurement failed. Confidence: high, based on
the retained event/error, source and existing regression specification.

| Run | Event and result | Evidence |
| --- | --- | --- |
| [41056909892](https://github.com/vpsfreecz/haveapi/actions/runs/41056909892), 2026-10-30 12:38 UTC | New `haveapi-0.32` branch at current master; failed before benchmark setup | [Comparison job 124066632586](https://github.com/vpsfreecz/haveapi/actions/runs/41056909892/job/124066632586), step `Resolve immutable sources and relevant paths` |
| [41056402034](https://github.com/vpsfreecz/haveapi/actions/runs/41056402034), 2026-10-30 12:34 UTC | Preceding master push at the identical SHA; genuine quick comparison pass | [Comparison job 124064915437](https://github.com/vpsfreecz/haveapi/actions/runs/41056402034/job/124064915437); all 14 workloads passed wall, CPU and allocations; all-client contract: 214 examples, 0 failures |

Failed artifact `performance-41056909892-1` (artifact ID `12977416903`):

```text
event.ref     = refs/heads/haveapi-0.32
event.created = true
event.before  = 0000000000000000000000000000000000000000
event.after   = 0e7166a0f8f15827bfac051666a53bf449e999ec
resolver.stderr:
HaveAPI::PerformanceCI::Error: Baseline and candidate must differ
```

There is no `selection.json`, runner exit or measured result in that artifact.
The [Performance gate job](https://github.com/vpsfreecz/haveapi/actions/runs/41056909892/job/124066791056)
then fails because its prerequisite failed; it is not a second performance defect.

The passing master's retained `report.json` has `status: pass`, not
`inconclusive`, comparing baseline `7edb003dd5d5a058b3308510bb8a5f60387ad654`
with the current master SHA. This proves the recorded quick comparison, not a
weekly fixed-reference campaign or production latency. Its all-client contract
includes all 15 registered renderer variants. Current workflow definitions have
one performance workflow; client coverage is a step within it. An exact-SHA API
query found no other failed workflow at this SHA, including client workflows.
Branch-only queries omit the failing release-branch run. The inspected evidence
does not establish an unresolved intermittent performance regression.

## Cause and smallest proposed correction

At the investigated SHA, [`utils/performance_ci.rb:94`](https://github.com/vpsfreecz/haveapi/blob/0e7166a0f8f15827bfac051666a53bf449e999ec/utils/performance_ci.rb#L94)
selects `merge_base(candidate, captured_default)` for zero-before pushes. A branch
created at master has no new source delta, so that baseline equals the candidate.
Line 125 rejects equality before computing relevance. The
[`event_baseline_spec.rb:92`](https://github.com/vpsfreecz/haveapi/blob/0e7166a0f8f15827bfac051666a53bf449e999ec/servers/ruby/spec/performance/event_baseline_spec.rb#L92)
example explicitly requires this rejection, so the behavior is a policy edge case,
not random runner noise.

Recommend allowing **only validated quick zero-before branch pushes whose
captured-default merge-base equals their candidate** to produce an explicit
no-work selection: `relevant: false`, empty changed paths and an explanatory
reason, retaining the candidate/default/baseline SHAs and normal event evidence.
This also covers a branch created at an older commit already contained in the
captured default. It must not silently substitute `HEAD^` or another baseline.

The [existing workflow no-work path](https://github.com/vpsfreecz/haveapi/blob/0e7166a0f8f15827bfac051666a53bf449e999ec/.github/workflows/servers-ruby-performance.yml#L131)
already skips benchmark execution and emits `outcome=no-work`. Keep the campaign
runner's distinct-source requirement and the aggregate's explicit-outcome gate.
No threshold increase, automatic retry, baseline change or workflow rewrite is
needed. A no-work outcome must not be described as a measured performance pass.

## Prospective implementation boundary and acceptance

One bounded implementer package is sufficient if implementation is requested:

- `utils/performance_ci.rb`: narrow resolver exception; preserve validation and
  existing output schema. No changes to the campaign/comparator or runtime code.
- `servers/ruby/spec/performance/event_baseline_spec.rb`: replace the matching
  rejection expectation and cover the exception plus its rejection boundaries.
- `doc/performance.md`: document this exception to the current equal-endpoint
  rule and the retained evidence/no-work meaning.

No independently useful second package or downstream dependency was identified.
Acceptance checks for that future package:

1. A real-Git fixture reproducing zero-before creation at default resolves to
   explicit no-work; a candidate already ancestral to default behaves likewise.
   A new branch with relevant changes still selects a distinct baseline and runs.
2. Equal manual pairs and nonzero-before pushes still fail. Missing/unavailable
   commits/default/merge-base, deleted/tag events, invalid ancestry and unproven
   maintenance lineage still fail. Preserve the existing zero-before contract
   independently of the event's `created` boolean.
3. Weekly/fixed-reference selection and all campaign distinct-source guards stay
   unchanged. The existing aggregate accepts successful `no-work` and rejects
   missing outcomes or failed prerequisites.
4. Quick checks in the repository Nix environment: focused event-baseline specs
   and affected Ruby style checks. Broader `make test-performance` and hosted
   no-work/ordinary-push verification follow the normal review/verification
   procedure if implemented; no long timing campaign is required to diagnose
   this resolver-only failure. Any long check uses the required watcher.

Compatibility: only CI selection behavior changes. Preserve selection schema 1
and retained evidence fields. No persisted application data, migrations, API,
client, protocol, package version or Nix configuration change. No coordinated
deployment or mixed-version requirement. Reverting a future resolver change
restores the old rejection without data conversion; historical red runs remain
historical evidence.

## Already-fixed historical failure

The preceding master failure [40529570313](https://github.com/vpsfreecz/haveapi/actions/runs/40529570313)
at `18b45aeddd0c28c8ddf6c5ea81f9611d6e3a7875` failed in
[job 122278356313](https://github.com/vpsfreecz/haveapi/actions/runs/40529570313/job/122278356313)
with `HaveAPI::Performance::ContractError: Response identity differs between
operations/revisions`. Its retained report is an error, not a timing regression.
Commit [`4d36efcf`](https://github.com/vpsfreecz/haveapi/commit/4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c),
already ancestral to current master, changed this policy to stability within each
revision, with cross-revision response differences retained as diagnostics.
The subsequent master [run 40547615707](https://github.com/vpsfreecz/haveapi/actions/runs/40547615707)
succeeded. That historical cause is separate from the current branch-creation
error; no additional historical excavation is needed for the recommendation.

Raw downloaded evidence is disposable under
`/tmp/haveapi-performance-failures-{41056909892,41056402034,40529570313}`.
Durable conclusions and exact GitHub references are above. Lead owns state and
portal updates; this is the architect's sole assigned edit.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-31-haveapi-performance-failures/)
