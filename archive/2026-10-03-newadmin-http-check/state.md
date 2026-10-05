---
lifecycle: complete
---

# 2026-10-03-newadmin-http-check

## Status

Merged into the remote default branch, `master`, at
`7e32833aca1cb65902b50f61eb76dd1022691591`. Integration was fast-forward-only,
with no rebase, source change or merge commit. The remote default and retained
feature refs both match the independently reviewed and built final revision.
Production rollout is owned by the user and remains unexecuted by the agent.
The session remains open and active.

The frontend probe now accepts compact and formatted schema-1 metadata while
requiring a full lowercase 40-character commit hash. All nine dedicated
Newadmin alerts are warning; shared infrastructure and other HTTP-site
severities retain their existing policy.

## Phase checklist

- [x] Verify exact session identity and inspect the retained roster.
- [x] Confirm the frontend metadata formatting cause and separate BFF/status behavior.
- [x] Set up implementation/review members and register the feature worktree.
- [x] Implement probe correction, dedicated warning policy, tests and documentation.
- [x] Pass quick checks and required hooks; commit the intended two changes.
- [x] Pass independent whole-branch review across all four lanes, with no findings.
- [x] Build both exact monitoring hosts and prepare rollout/recovery instructions.
- [x] Publish the feature branch and capture its exact comparison.
- [x] Integrate the exact reviewed feature head into remote default branch master.
- [ ] Operator deploys both monitors and verifies loaded production probes/rules.

## Next action and risks

The user will deploy the integrated configuration. Use [rollout.md](rollout.md)
for the prepared both-monitor rollout, live verification and recovery steps.
No implementation or integration blockers remain. Deployment evidence can be
added after the operator reports results; no agent activation is assigned.

The running monitors have not been activated with this branch. Until both are
updated, an old monitor can still emit the false body-match failure and critical
Newadmin alerts. Severity changes also change alert identity; allow old alert
instances to resolve after rollout. Production exporter results, loaded rule
labels and notification behavior remain unverified. These metadata/health
probes do not certify interactive login or all WebUI behavior.

## Repository and branch

- Project: `vpsfree-cz-configuration`.
- Canonical bare repository: `/home/aither/workspace/ai/vpsfree.cz/repos/vpsfree-cz-configuration.git`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-03-newadmin-http-check/vpsfree-cz-configuration`.
- Branch: `2026-10-03-newadmin-http-check`.
- Reviewed base: `657cc0a8e087f8c4bed7fe8d7176cb9f06a6e2da`.
- Remote default branch after integration: `7e32833aca1cb65902b50f61eb76dd1022691591`.
- Commit 1: `fae43505f2b52f849627b571265b7d7906447dcf`, probe correction.
- Commit 2/final head: `7e32833aca1cb65902b50f61eb76dd1022691591`, warning policy with tests/docs.
- Worktree clean. Final head descends from the base; the comparison is captured.
- Feature and default branch published over canonical SSH. `git ls-remote`
  confirms both remote refs at the exact final head; master advanced by fast-forward.
- No migrations, dependency/pin changes, obsolete functional history or unused
  compatibility paths. Both commits introduce final behavior and are independently reversible.

## Verification and review

See [implementation-result.md](implementation-result.md) for exact quick-check
commands, [review.md](review.md) for the preserved independent conclusion and
[verification.md](verification.md) for the consolidated verification evidence.

- Fifteen Go regexp fixtures passed using the evaluated source patterns.
- Promtool 3.12.0 validated 36 rules and passed all 17 scenarios.
- Actual rule-test name/count/warning assertions passed through pure evaluation.
- Generated base/final rules differ only in seven dedicated severity values;
  expressions, durations, frequencies, annotations, groups and every other rule are identical.
- Both final commits passed required formatting and commit hooks without warnings or bypass.
- Retained reviewer0 reviewed all four adaptive lanes at the exact final head:
  no Blocking, Important or Advisory findings. Explicit whole-history and empty
  migration-lineage conclusions passed before host builds.
- Mon1: `nix develop --command confctl build --yes cz.vpsfree/containers/prg/int.mon1`,
  exit 0 in 58.8 seconds; generation `2026-10-03--20-47-18`.
- Mon2: `nix develop --command confctl build --yes cz.vpsfree/containers/prg/int.mon2`,
  exit 0 in 58 seconds; generation `2026-10-03--20-51-51`.
- Each build was owned by a fresh GPT-6 Luna/low utility watcher. Neither generation was activated.
- No feature-push CI is configured: `gh run list` returned no branch runs; the
  repository workflow is scheduled/manual dependency updating. No workflow was triggered.

## Diagnosis evidence

Public read-only checks on 2026-10-03 at approximately 18:00–18:03 UTC returned
HTTP 200, application/json and formatted schema-1 metadata at `/build-info.json`.
Both original compact-body patterns failed; both whitespace-tolerant replacements
matched, with schema 10 rejected. `/healthz` returned HTTP 200 with `ok`.
The status site's redirect to `/?lang=en` succeeded when followed and is
separate from the frontend regex failure.

`modules/clusterconf/monitor/default.nix` passes body patterns directly to
blackbox exporter's required raw-body regex list. Upstream blackbox exporter
0.28.0 `matchRegularExpressions` and its configuration documentation were
checked. Cached WebUI source emits formatted JSON, consistent with the live
response; the exact publicly pinned WebUI source revision was not inspected.
The live exporter itself was not queried during diagnosis.

## Documentation

The owning configuration guide, `docs/operations/newadmin-webui.md`, now records
the lasting dedicated-warning policy and explicit decision needed to promote
it to critical. The existing mkdocs index makes that guide discoverable.
The individual rollout and recovery checklist is [rollout.md](rollout.md),
marked prepared, not executed. No member-facing KB or interactive UI changed.

## Authorization and team

The user requested warning-only Newadmin alerts, selected the dedicated-alert
scope and authorized implementation with “Implement the plan”. Shared VPS
infrastructure remains outside that severity change. The original implementation
request did not authorize integration; the later explicit merge direction is
recorded below. Deployment belongs to the user. No session lifecycle or cleanup
action was requested.

Initial tracking commit `b9c2ef2b` preceded team setup and project-code commits.
A differing team preset was refused; supported team-add operations preserved
the saved solo lead and added catalog implementer0 and reviewer0. Their saved
GPT-6.1 Sol/xhigh settings and implementation workspace-write/review read-only
access were verified. The lead owned coordination; implementer0 owned application
edits and reviewer0 owned independent review. The bounded design is in plan.md
and the implementation assignment is [implementation-brief.md](implementation-brief.md).

The utility watcher policy came from installed catalog digest
`4676433c6831fbaca91da8ffde84891aff6ce065a17c74c2f367f1acf1d15b17`.
Session identity was rechecked at the final checkpoint: current slug and both
environment markers match the exact trusted workspace binding.

## Recovered setup and verification issues

The first worktree registration failed in its checkout hook because the local
Ruby bundle was absent. A fresh watcher prepared `nix develop --command true`
(exit 0, 41 seconds), then supported registration retry succeeded without hook
bypass. The implementation sandbox's daemon-socket restriction was resolved
with a private cached declared-shell environment and already installed pinned
Nix/Prometheus tools; no source ownership or access policy changed.

The first mon1 build stopped at confirmation EOF before building; the documented
`confctl build --yes` option resolved it. The next mon2 invocation failed in an
unavailable external timing wrapper before starting its build. A fresh mon2-only
watcher used built-in timing and passed. No source changes or repeated mon1
build were needed. Detailed evidence and reusable lessons are linked from
verification.md and the workspace notes.

## Retained ownership

No development cluster was created. Feature refs, worktree and session remain
open and owned by this active initiative. Temporary fixtures, caches and the
private shell snapshot are outside portal artifacts. Unrelated shared-workspace
files and index changes were preserved. No archive, cleanup or session-stop
operation was performed or scheduled.

## Default-branch integration authorization

The user explicitly directed: “ok, merge into the default branch. I will deploy
it myself.” This authorizes only `vpsfree-cz-configuration` integration into its
verified default branch, `master`. Production deployment is owned by the user
and is not assigned to the agent. No session lifecycle or cleanup action was
requested.

Fresh upstream fetch still resolves master to
`657cc0a8e087f8c4bed7fe8d7176cb9f06a6e2da`, the reviewed base. The exact final
feature head remains `7e32833aca1cb65902b50f61eb76dd1022691591`. No rebase or
patch change is required. Integration target worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-03-newadmin-http-check/integration-targets/vpsfree-cz-configuration`.

Completed `git merge --ff-only refs/heads/2026-10-03-newadmin-http-check` from
that isolated target, followed by `git push origin HEAD:refs/heads/master` over
canonical SSH. Master advanced from the reviewed base to the exact final head;
no rewrite or new commit was introduced. Target worktree was clean and its
base-to-head diff check passed. Existing validation applies to the unchanged
final revision, so no source checks or host builds were repeated.

Post-push `git ls-remote` confirms both remote master and feature heads equal
`7e32833aca1cb65902b50f61eb76dd1022691591`. The local target HEAD and origin/master
match as well. GitHub's latest master workflow metadata contains only completed
Daily update runs at older revisions, with no integration-head run. No workflow
was triggered or awaited. Feature refs and both owned worktrees are retained;
no cleanup or lifecycle transition was performed.
