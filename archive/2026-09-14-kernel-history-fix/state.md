---
lifecycle: complete
---

# Current status: merged on 2026-09-15

User authorized default-branch integration. All four branches are merged by
fast-forward over SSH; feature branches and canonical worktrees remain retained.

| Project | Integration base | Merged head |
| --- | --- | --- |
| vpsadmin | f7a17d6e512f0b11e2c908813eb2e780261e20ae | c38839d5be62e9d40d055b23a84844e2037ba4db |
| vpsfree-maintenance-tasks | 6eea682ede8d8e2634b2d41e5b11cf0f02231bc6 | 2fdc9f2889ac419136cd0cde0e0955c015ae7107 |
| vpsfree-cz-configuration | b0bb82d13159ce0da15375acf0483ab58572824a | b792c50e3baa17a73989dda1129cb17ba0e63587 |
| vpsfree-kb-contracts | 919577d0c770e47b623c591f8bf0cce4e8d30666 | 8789cc1f5aeb3b19cbff13f741d6dd9960f14567 |

Exact V pin: c38839d5be62e9d40d055b23a84844e2037ba4db. C changes only
vpsadminServices, with confctl's generated message unchanged. All11 consumers
built as2026-09-15--10-59-39. Final rebase preserves both reviewed feature patches;
142 focused combined examples pass. Canonical KB check passes with no prose or
capture changes. Prior full V CI135scripts/118tests and K runtime12scripts/4tests
passed. New CI triggered by merges is running; see verification.md and the
postmerge-*-ci.json metadata. Do not claim those pending runs have completed.

Prepared rollout/repair commands use final heads and exact build generation.
No production deployment, repair, node upgrade/reboot or lifecycle action took
place. Leave this session open and active. The unused extension worktree is
unchanged and outside this merge. All four temporary target worktrees were removed with normal non-force git
worktree removal. Canonical feature worktrees and all branches remain retained.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-14-kernel-history-fix/

# Historical tracking (superseded status retained below)

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

## Follow-up implementation in progress

Ownership reverified: dev-session current and DEV_SESSION_SLUG both equal this
session. User approved the recovery checkpoint and all-node maintenance task.
Review model corrected by user to gpt-6-astra; retain xhigh and all four lanes.
The earlier V337/C09b/K61a heads and their green CI are the previous delivery,
not validation of this follow-up. Production remains untouched.

Registered vpsfree-maintenance-tasks at
worktrees/2026-09-14-kernel-history-fix/vpsfree-maintenance-tasks on the matching
feature branch, starting from origin/master 6eea682. Existing V/C/K worktrees
remain owned by this session. Fetched vpsadmin upstream; rebase initially refused
by Overcommit configuration signature. Inspect and re-sign the unchanged hook
configuration in the repository Nix shell before retrying.

Upstream V advanced to 014fbc784; rebased feature commits are d8bd6ece3 and
597c26953. Resolved the schema conflict retaining upstream password tables;
subsequent core schema regeneration normalizes table ordering.

The user briefly requested updating persistent review-model instructions.
Created and registered vpsfree-dev-workspace at a08a40e on this session's branch
and verified the two-line skill edit. The user then took that instruction update
into another session. Reverted only those two uncommitted edits; the worktree
and retained branch remain clean at their upstream base. No installed skill,
runtime package, or lifecycle state was changed. This session still uses the
user's gpt-6-astra/xhigh review override.

Follow-up quick verification: 130 focused DB-backed examples passed, including
101 recorder/comparator/supervisor cases and 29 relocated maintenance cases.
The maintenance subprocess test passed all-node preview, subset apply, all-node
apply and idempotent rerun on disposable MariaDB data. Two additive migration
specs passed. The original new migration collided with upstream's daily-report
20260914120000, so ours is now 20260914180000; the checkpoint migration is
20260914190000. Neither prior feature migration had been deployed. Regenerated
core schema with VPSADMIN_PLUGINS=none after renumbering.

All 10 touched API Ruby files passed lint. The initial maintenance lint invocation
used RuboCop defaults outside V's directory and reported irrelevant default
metrics/style limits. Rerun explicitly with V's .rubocop.yml, fix actual layout
and fixture issues, and retain the command in final verification. User-facing
writing skill applied directly to task CLI help/README and rollout revisions.
Long integration and new mandatory review have not started yet.

C upstream advanced to 3f213d5e and already pins V014fbc784. Rebasing the old
feature pin conflicted only in vpsadminServices. Dropped that superseded,
unmerged pin commit with rebase --skip; C is clean at current upstream pending
one new confctl-generated final pin. Its original generated message was never
edited. K rebase reports up to date. V API CI topic expansion covers all 403
tracked non-migration specs exactly once; migration specs remain covered by the
existing migration workflow glob. CI selector tests: 16 runs, 55 assertions pass.

Additional quick checks passed: 23 API-resource/standalone-runner examples,
including no checkpoint resource/rows exposed, plus a focused immutable-evidence
check rejecting recovery checkpoints. Maintenance lint passes with the explicit
VpsAdmin RuboCop configuration. All commit hooks passed (only nonblocking
72-column advice; messages satisfy the repository's 80-column limit).

Full-schema verification caught one lost upstream created_at index on
password_change_logs after resolving the rebase's duplicate table blocks.
Replaced schema.rb with the dump from exact upstream 014fbc784 plus both new
migrations, preserving that index. The generated predecessor check is retained
as check-recovery-schema.rb; it requires RACK_ENV=test for disposable DB startup.
Consolidate the obsolete repair-in-API commit into the permanent kernel fix,
leaving a separate valid-evidence recovery commit and the maintenance task commit.
Latest fetches still show V014fbc784 and maintenance6eea682 upstream.

Committed review heads after consolidation:
- V cccf59c060be4c85a7a0809203e6fe24447e16a4 (permanent kernel confirmations),
  then 268f7d09b9e3ca59d2b8f286e6666f72f9f7a9ff (invalid-evidence recovery),
  based on 014fbc78422f3660b295add7a50f35cc7acdf0c8.
- M c77ff3742f623afd23c0be26c0f6ddbc026f1ba4 based on
  6eea682ede8d8e2634b2d41e5b11cf0f02231bc6, all code scoped to the dated task.
Both tracked project trees are clean. All obsolete repair-in-API history was
folded out. General, architecture and scope reviews launched with fresh
standalone gpt-6-astra/xhigh agents; compatibility follows as a slot opens.
Packet: recovery-review-packet.md. High risk for persisted history/schema and
mixed writer deployment. New feature heads are not pushed yet; long integration
is intentionally after all required findings are resolved.

All four recovery review lanes completed with GPT-6 Astra/xhigh. Scope and
compatibility found no additional issues. General caught an invalid synthetic
software SHA; architecture caught the installed Ruby loader bypassing the CLI
and the mistaken history batch default. Fixed all three locally: exact parser
fixture preflight passes, installed-load help/preview/apply/rerun passes, and the
approved default is explicitly 1,000. Maintenance: 29 examples, zero failures;
all six Ruby files lint clean. Full predecessor schema check passes exactly.
See recovery-review-reconciliation.md and four lane reports. These narrow fixes
need no review rerun; downstream exact pins still require their final review.
Latest fetches remain V014fbc784/M6eea682/C3f213d5e. Maintenance final head is
 a80cc098ac15f2a88c5a369836434448af168b1d. V fixture amendment hooks are running.

Final vpsAdmin recovery head 42984def67d405c235e2a34d91820563858ddd89 is
pushed over SSH with an explicit lease against former337c9257. Push initially
hit the ambient Overcommit signature mismatch; the inspected unchanged hook
configuration was signed in the root Nix shell and push succeeded. Maintenance
 a80cc098ac15f2a88c5a369836434448af168b1d is also pushed. All mandatory reviews
and direct remediation checks passed before long integration started.
Local supervisor/runtime-ingestion and webui#admin-cluster run against V42984def6
with isolated short /tmp/kh-recovery-* state paths. New GitHub Actions are
34877084311(API),34877084349(libnodectld),34877084303(migrations),
34877084413(CI),34877084302(i18n),34877084305(PHPUnit),34877084338(RuboCop).
All prior-head workflows were already completed, so none needed cancellation.
Configuration exact pin and canonical KB metadata update are running. Preserve
KB's pre-existing vpsAdminOS6bdf458 and nixpkgs pins after Nix refresh.

All 11 configuration consumers built successfully at Cc8b7a499, generation
2026-09-14--19-51-56. Direct buildPlan checks confirm vpsadminServices and exact
V42984def6 on every consumer. Canonical KB check passed at pushed K610cb7bf:
all contract/annotation/page checks, 60runs194assertions and 120PNGvariants.
Existing OS/nixpkgs pins are unchanged. K workflows34877456478(Check) and
34877456477(Managed page runtime) are pending. Source comparisons captured for
V/M/C/K; maintenance requires recapture after its latest doc amendment.

Final downstream general review caught ineffective runtime masks on NixOS:
/etc main units outrank /run masks. Original checks would safelyhalt but rollout
could not proceed. Reviewers reproduced this with isolated fixtures and proved
runtime ConditionPathExists drop-in+marker prevents start even after replacing
the base unit/reloading. Pinned Nix activation preserves the runtime guard.
Rollout now checks marker, exact loaded drop-in, raw effective Conditions tuple,
and inactive/ConditionResult=no on BOTH hosts around both activations. Commands
select exact built generation. Removal is scoped to the two task guardfiles on
each host after packages/schema are ready; repair and rollback reuse the guard.
No real host service or production state was touched. Fourteen shell blocks
parse with bash-n. M README advice updated and pushed as doc-only amendment,
final head2fdc9f2889ac419136cd0cde0e0955c015ae7107; repair code/tests unchanged.

Final general/compatibility pin reviews complete with no unresolved findings.
Runtime guard finding is resolved and bound to finalM2fdc9f28. All feature
comparisons are captured, including the doc-only M amendment. The new supervisor
VM regression passed (119.94s), covering stable/valid confirmations through
transitions, rejected evidence and supervisor restarts. Remaining VM cases and
long GitHub Actions continue. No rollout/repair action has been executed.

Local supervisor/runtime-ingestion completed successfully: all11 examples,
1067.52s total, new confirmation/recovery/restart example119.94s. Final V
integration CI34877084413 has started; API topic jobs22/26passed as of18:09UTC.
WebUI local flow is running and KB runtime remains queued.

## Authorized default-branch integration (2026-09-15)

User explicitly requested merging into default branches. This supersedes the
original no-merge restriction for the four implementation/pin repositories.
No deployment, production repair, archive/delete/stop or instruction update is
authorized. Verified current session/DEV_SESSION_SLUG match; leave session open.
All final V42984def6 workflows passed, including full integration34877084413 and
API34877084311. K610cb7bf Check and managed runtime also passed. Local WebUI
completed successfully in1358.63s (browser example481.79s); supervisor11examples
passed in1067.52s. Fetch now finds one new V upstream commitf7a17d6e (DDNS check)
and Cb0bb82d1 pins that revision. Rebase V, verify combined code and unchanged
feature delta, regenerate C/K exact pins, capture final comparisons, and merge
with fresh target worktrees and fast-forward-only pushes. M and K bases remain
unchanged; unused extension worktree has no changes and is outside this merge.

Rebased V headc38839d5be62e9d40d055b23a84844e2037ba4db consists of unchanged
feature patches4959e251a andc38839d5b on upstreamf7a17d6e. git range-diff
reports both patches identical; only the three upstream DDNS code/spec paths
differ from fully testedV42984def6. Combined DDNS+recorder/supervisor/maintenance
specs are running from fresh integration worktree sources. Configuration old
pin conflicted with newer upstreamServices pin and was skipped before fresh
confctl generation. Nix cannot enter a shell while flake.lock has conflict
markers; direct git rebase --skip resolved the obsolete pin without editing
generated messages. No default branch has been pushed yet.

Rebased merge validation passed:142 examples,0 failures, covering all130 feature/
maintenance cases plus12 DDNS/lifecycle cases, from fresh target worktrees.
The broad initial resource test was gracefully stopped after132 passing examples
and replaced with that complete focused selection; it is not counted as a full
suite pass. K target-worktree bin/check also passed with no drift. Fresh C target
buildPlan proves all11 consumers use vpsadminServices at exactVc38839d5.

Remote master fast-forwarded in maintenance6eea682->2fdc9f28 and
vpsadminf7a17d6e->c38839d5. V feature also points toc38839d5. No default history
was rewritten. Cb792c50e is the untouched confctl-generated exact-pin commit;
K8789cc1f5aeb3b19cbff13f741d6dd9960f14567 contains only the five revision files.
All final comparisons were captured before their remote integration.
New V master workflows:34950267509(libnodectld),34950267548(API),
34950267566(CI),34950267587(migrations),34950267521(lint),34950267498(i18n).
These post-merge runs are separate from the completed prior-head validation.

All four remote feature refs equal their remote master refs at the final
recorded heads; ancestor checks passed and tracked canonical worktrees are clean.
Only temporary target worktrees are being cleaned, not registered initiative
worktrees. C temporary cleanup initially refused due to generated .bin/.bundle
files; remove those exact task-generated files before normal git worktree removal.

Temporary C .bin/rubocop and .bundle/config were the only untracked files.
Removed those generated files and empty directories, then normal git worktree
remove succeeded. All four temporary target worktrees are gone; no session
lifecycle helper was invoked.
