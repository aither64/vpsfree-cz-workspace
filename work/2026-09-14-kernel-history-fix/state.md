---
lifecycle: active
---

# Kernel history timestamp fix

## Ownership and authorized delivery

`dev-session current` and `DEV_SESSION_SLUG` both matched
`2026-09-14-kernel-history-fix`, including the continuation ownership check.
This is the only owned session. The node1 livepatch-unload investigation was
read as reference only; none of that session's files, branches, or state changed.

Implement, commit, review, test and push feature branches; prepare rollout and
repair instructions. No production deployment or history repair, node update or
reboot, default-branch merge, archive/delete/stop, or delayed session cleanup is
authorized or performed. Leave this initiative active and open for follow-up.

## Repositories and final revisions

All branches use `2026-09-14-kernel-history-fix`. Worktrees are under
`worktrees/2026-09-14-kernel-history-fix/<project>`.

| Project | Upstream base | Final head | Push status |
| --- | --- | --- | --- |
| vpsadmin | 791ab3aa89e2f613979da6090b89785c78245db5 | 337c9257f5e11f36afe81eba4951e267b83e2fc7 | Pushed over SSH |
| vpsfree-cz-configuration | 249bed1ee28e69a907edd09ea97a1144dbcdefeb | 09b3370c2d628bcc7ab5eb7bbdf19edbcf8be347 | Pushed over SSH |
| vpsfree-kb-contracts | 919577d0c770e47b623c591f8bf0cce4e8d30666 | 61aaf95d3dc0968728131a2cf4d4740dae6e9250 | Pushed over SSH |

All three upstreams were fetched before final validation; C/K were fetched again
before their final pushes and remained unchanged. Every
feature descends from its recorded base. No rebase change was needed. V has two
logical commits; C/K each have one consolidated pin commit. Old unmerged repair
and pin revisions were amended/replaced rather than stacked as fixup commits.

Final C/K pushes used explicit leases against their superseded unmerged heads.
All three remote feature refs were verified against the final local heads. C/K
pin exact tested V337c9257. C retains untracked .bin/.bundle development caches;
tracked trees are clean. Final comparisons were captured for all three heads.

## Implementation

Recorder commit `7b4aec6bb9b948ab3d1bdf90a886b99a4ebd4ff5` adds nullable internal
`node_kernel_events.last_confirmed_at` and the shared StableState helper. Current
and supplied previous reports can prove the old stable state. Updates are
monotonic under the node lock/transaction, ignore volatile verification metadata,
and preserve original bounds, updated_at, immutable evidence and public revisions.
Removal/release bounds use the confirmation; application-specific preceding
non-effective evidence and conservative legacy/boot handling remain intact.

Repair commit `337c9257f5e11f36afe81eba4951e267b83e2fc7` adds the public dry-run-first
Rake task, a fixed-candidate batched repair, command validation, operator docs and
synthetic integration coverage. It requires an eligible single node, retained
intact immutable same-boot proof of the immediate public baseline, and strict
lower < proof < upper ordering. Internal snapshots may support proof; mutable
current evidence, raw logs and uname-only samples cannot. Stored content digests
are verified and proposals revalidated under the node lock before each write.
Repairs alter only the lower bound and normal updated_at, invalidating revisions.
Reruns without new evidence are idempotent; insufficient proof leaves bounds intact.

No public field, protocol, WebUI wording/layout, or node software change.
Migration 20260914120000 adds a nullable datetime without default/backfill. Core
schema was regenerated against a core-only disposable database; existing column
reordering is generated, with only the new column as a semantic change.

The final API tree is `8f030d0a27b4ba84a317871f41a728a55c24b8ab`, identical to
focused-tested feaa1524. The last change only replaces a timing-dependent copied
integration report with a complete standalone synthetic report.

## Local verification

Use repository Nix environments. The .#api shell already enters api/. Git hooks
need the root Nix shell, where Overcommit is available. No hooks were bypassed.

- Combined recorder/repair/StableState/supervisor specs: 106 examples, 0 failures.
  Command: nix develop .#api -c bundle exec rspec
  spec/models/operations/node/record_kernel_evidence_spec.rb
  spec/models/operations/node/repair_kernel_history_bounds_spec.rb
  spec/lib/vpsadmin/api/kernel_evidence/stable_state_spec.rb
  spec/supervisor/node/status_spec.rb. Log focused-final-corrected.log.
- Isolated migration spec with --options /dev/null: 1 example, 0 failures.
  Core schema load, migrate and dump passed with VPSADMIN_PLUGINS=none.
- Repair public-entrypoint spec: 26 examples pass. Exact synthetic payload
  preflight passes parser, persistence, transitions, a new supervisor instance,
  and actual public Rake repair in a disposable DB (2 examples, 0 failures).
- Touched Ruby lint, Nixfmt, Ruby syntax and commit hooks pass.
- CI selector: 16 runs, 55 assertions pass. Migration/spec coverage and the exact
  workflow Bash topic expansion pass: all 404 non-migration specs covered once.
- Final supervisor/runtime-ingestion: all 11 examples pass at V337c9257,
  935.48 seconds total, synthetic example 123.27 seconds. Finished 13:03:20.
  Main log integration-supervisor-standalone.log; disposable state
  /tmp/kh-sup4.tPXKYf. Includes real supervisor service restart and packaged
  bundle exec rake preview/apply/idempotence on disposable history.
- Local webui#admin-cluster passed: browser flow 459.01 seconds, total 1483.19.
  Rendering code is unchanged since this run. Log integration-webui-retry.log,
  disposable state /tmp/kh-ui.7CHLdB. No real patch unload or kernel build.
- Final canonical KB bin/check passes: 45 controls, 36 paths, 35 capture concepts,
  3 semantic selectors, 94 bindings/9 exceptions, 4 pages/8 variants, 12 tests,
  21 executable samples, 60 checker runs/194 assertions, 120 PNG variants.
  No semantic fingerprint drift, prose change, or capture regeneration needed.
- Final C build passes all 11 cz.vpsfree/vpsadmin/* consumers, generation
  2026-09-14--13-07-10. Command: nix develop -c confctl build --yes
  'cz.vpsfree/vpsadmin/*'. Log tested-consumer-build.log. Direct buildPlan
  evaluation confirms all 11 use vpsadminServices at exact V337c9257;
  channel-pin-verification.json contains the filtered result.
- All 11 prepared rollout shell blocks pass bash -n. None was executed.

## Reviews and direct remediations

Overall risk is high: persisted history/schema, future repair writes and a
multi-writer rollout. All reviewers used gpt-5.6-sol at xhigh.

Initial general, architecture, scope and compatibility lanes completed. Required
findings fixed: a comment inside a literal CI pattern block became a path;
provider-level StableState specs were missing; normalized child snapshot drift
required stored-digest verification. Focused checks passed after each fix.
The advisory three-state boot abstraction was declined: conservative bootstrap
and positive-proof identity intentionally differ; tests document that boundary.

Downstream general/compatibility reviews required explicit per-host runtime-mask
checks through each activation/migration, and a clear boundary between an online
preview and later apply. The prepared runbook retains the requested CLI: for
approval of exact proposed repairs, pause both writers/other history maintenance,
review a saved preview, repeat and cmp-check it, then apply while still paused.
No new preview-manifest protocol was introduced. Exact C HEAD/pin assertions and
choice of a known stable node for confirmation checks were added.

Bounded fresh general reviews checked test waits and the public Rake correction,
with no remaining findings. A previous exact-pin review found no consistency
issues but marked its heads intermediate after the final fixture dependency was
found. Final review_delivery_pin checked V337c9257/C09b3370c/K61aaf95 and rollout
with no Blocking, Important or Advisory findings. Report: review-final-pin.md.
The earlier intermediate report is retained separately.
All detailed findings, decisions and reviewed heads are in review-reconciliation.md.
The task owner applied the user-facing writing skill directly to CLI help,
repository operator docs and rollout instructions.

## Investigated integration and tooling failures

- Long state paths exceeded the Unix socket path limit before examples. Use short
  real mktemp state directories; original failed state/logs remain untracked.
- Default sv seven-second waits rejected stops before publication. The wrapper
  permits 60 seconds; explicit sv -w 90 and runner timeout 120 cover it, with stop inside
  ensure protection. Subsequent legacy examples passed.
- Synthetic version length 26 exceeded the DB limit 25; reproduced ValueTooLong and
  changed it to a 19-character value. Exact payload preflight passed afterward.
- Tasks.run/classify singularized NodeKernelHistoryBounds to a missing Bound
  class. Internal class/key now ends in BoundsRepair; public task unchanged.
  Added public Rake preview/apply/idempotence coverage and packaged VM invocation.
- After a legacy report, waiting for the reporter process did not guarantee a
  new current evidence snapshot. Copying nil yielded {}. The final standalone
  synthetic report removes that dependency; full VM scenario now passes.
- Empty Ruby single quotes terminated a Nix indented string; equivalent double
  quotes pass Nixfmt and Ruby syntax checks.
- Standalone local rake -T without a DB failed during API initialization;
  DB-backed Rake tests and the seeded packaged VM cover the actual entrypoint.
- A mistaken supervisor spec path produced a pre-example LoadError; corrected
  path and complete 106-example run pass.
- K nix flake update tried replacing transitive vpsAdminOS/nixpkgs pins. Preserve
  them with nix flake lock --override-input vpsadmin/vpsadminos
  github:vpsfreecz/vpsadminos/6bdf458fd9105379860234ff33d352e55844f08f. Only the
  vpsadmin lock entry changes at the final head.
- Confctl logger chunks long JSON; parsing one line of buildPlan failed. Evaluate
  directly to a temporary JSON file and filter it. All final assertions pass.
- Running GitHub job logs were unavailable through the logs API; runner SSH was
  denied for normal/root accounts. No access changes attempted. Monitor GitHub
  status and inspect completed logs/artifacts. Do not retry SSH.

Reusable lessons are in this initiative's dated notes under notes/vpsadmin/,
notes/vpsfree-kb-contracts/ and notes/vpsfree-cz-configuration/.

## GitHub Actions

Final V337c9257 runs:
- CI 34836306209: passed; 135 scripts across 118 tests in 17951.35 seconds,
  all 118 successful. Completed logs inspected; no unexpected results.
- API Specs 34836306199: passed, all 26 topic jobs and final coverage check.
- RuboCop 34836306248: passed.
- i18n 34836306232: passed.
Migration 34827227517 and libnodectld 34827227454 passed on unchanged relevant
source. Initial implementation API 34827227593 passed all 26 topics.
Final K Check 34837590578 and Managed page runtime 34837590575 both passed
at pushed K61aaf95. Runtime logs confirm 12 scripts across 4 tests passed in
2378.07 seconds. C has no branch workflows; all 11 consumer builds passed.

Superseded running CI was cancelled only after each correction push. GitHub also
cancelled old API runs by concurrency. Inspected cancelled CI logs/artifacts:
2a run 34827227475 retained 18 expected-success results (last periodic count 15),
b851 run 34831012297 retained 19, feaa run 34833489308 retained 9; no reported
unexpected failures before cancellation. These are partial results, not full
suite passes. Never cancel runs on the current head or unrelated branches.
Investigate any final CI failure before rerunning.

## Prepared operation, remaining work, and open session

rollout.md asserts exact final C HEAD and V pin. Its prepared commands pause and
runtime-mask both API supervisors for API1 activation, additive migration as the
database account from the new package, and API2 activation. Then restart both and verify
confirmations advance while bounds/updated_at stay fixed. Both API hosts have
autoSetup=false, so activation alone does not migrate. No node upgrade/reboot.
Older application code can ignore the nullable column on rollback, with the old
recording behavior returning. Keep the column and evidence-supported repairs.
Node 400 repair preview is separate; production rows were never inspected and
retention may leave no sufficient proof. All operator commands remain unexecuted.

All final-head CI, feature pushes, exact-pin reviews, consumer builds and
comparison captures are complete. The follow-up status timestamp audit is also
complete: 13 database-backed examples pass, including six reproductions of a
separate existing invalid-evidence fallback defect. See status-timestamp-audit.md
and its retained reproduction spec. The affected paths include software,
deployment, sysctl, modules, inferred eBPF inventory, and the livepatch-application
preceding-report special case. That defect remains unfixed; this question
did not change the delivered project heads or extend the kernel-only repair.
The consolidated handoff checkpoint retains the curated artifacts and notes.
Workspace initial tracking commit was 6160147. The initiative stays active with
unmerged feature branches; the new recovery finding remains an open follow-up.
Shared master and unrelated changes must be preserved. Raw logs, VM state,
preflight payloads and downloaded CI artifacts remain untracked.

Portal manifest points to useful review, rollout and validation artifacts.
Obtain its URL again at handoff:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-14-kernel-history-fix/

Keep all worktrees, branches and this session open. No archival, deletion,
private lifecycle helper or delayed cleanup is authorized.
