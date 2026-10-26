# API performance hosted verification runbook

**Ready, awaiting explicit HaveAPI master integration approval.** The lead
accepted the single user-authorized additional quick40196045698 after C's full
independent audit and separate-run comparison, plus the architect's independent
YES recommendation. Weekly40187949233 was accepted separately. The
[lead acceptance](api-performance-acceptance.md) and
[final observation](api-performance-hosted/38ecca75edaf797d048fb36c6a50ea7e05eb50a9/final-hosted-observation.md)
record completed verification at unchanged candidate
`38ecca75edaf797d048fb36c6a50ea7e05eb50a9`, tree
`c6cf3c6809ab52b3b2fba57c117139c7bcff6a37`.

The accepted quick compares candidate38 to the original baseline399, not b85.
All12 cases pass: SQLite includes meets8/9 on both clocks with one unresolved
reverse pair and0regression agreements; the other11 cases meet9/9. The
[separate repeat record](api-performance-hosted/38ecca75edaf797d048fb36c6a50ea7e05eb50a9/repeat-quick-user-authorized/status.md),
[C repeat audit](phase2-c-repeat-quick-analysis.md) and
[comparison](phase2-c-repeat-quick-comparison.json) retain the evidence. Original
push40187916872 stays historically failed/inconclusive7/9/exit2, with all raw
records unchanged. No pooling, reclassification, waiver, causal claim, standing
retry or universal repeatability guarantee follows. Future inconclusive still
blocks.

Weekly40187949233 independently passes all32 cases against fixed reference b85.
Whole performance jobs247s quick and1278s weekly include setup/upload and fit
unchanged600s/1800s caps. All9ordinary workflows pass; release did not trigger.
[Original quick audit](phase2-c-hosted-quick-analysis.md),
[weekly audit](phase2-c-hosted-weekly-analysis.md) and the
[current checkpoint](api-performance-hosted/38ecca75edaf797d048fb36c6a50ea7e05eb50a9/hosted-verification-status.md)
retain the original11 terminal runs and separately accepted additional quick.
Not all original checks are green. All three C audits validate outputs, counts,
source/input/lock graphs, budgets and clock arithmetic, including explicit
reconstruction of the omitted hidden `inputs/.ruby-version` copy from exact
Git-verified archives.

Agreed verification is complete; all utility operations are finished and slots
released. Review/narrow-fix lineage, final ordinary checks and the lead's complete
eight-commit inventory/diff/source-clean checks remain valid. No further campaign
is required. Integration, deployment and lifecycle completion remain unapproved;
the session stays open. Earlier checkpoints and prepared commands below are
historical and confer no action authorization.

Historical one-shot diagnostic: both7f performance push/manualquick runs completed
success; oldae60weekly cancellation is confirmed. [Exact three-run evidence](api-performance-hosted/7f926021834a64e64d3ec65561cfe07337989d17/bounded-diagnostic-status/report.md).
At that checkpoint no metrics were accepted. C subsequently completed the
minimal test-only correction; final38 server RSpec passes all three Ruby versions.
No7f weekly dispatch was made; final38 weekly completed under its own authorization.

Historical7f execution checkpoint:
[7f926021834a64e64d3ec65561cfe07337989d17 checkpoint](api-performance-hosted/7f926021834a64e64d3ec65561cfe07337989d17/hosted-verification-status.md).
Exact leased feature publication succeeded; Git window released. The one snapshot
initially showed server RSpec failure, seven passes, two pending and release
skipped by trigger. Manual quick40187122638 later completed successfully. Old
ae60 weekly cancellation was subsequently confirmed terminal; all evidence is
retained. These earlier states do not replace final38 results and audits.

Historical ae60 follow-up: C diagnosed and corrected the direct run-to-comparator
source-proof issue with a composition regression. No ae60 numeric result was
accepted. [Successor preparation](api-performance-hosted-successor-plan.md)
retains the publication and superseded-run plan; actual successor receipts are
linked above. No new action is authorized by these prepared instructions.

Initial preparation by implementer3 performed no push, fetch, dispatch, CI
polling, test or installation. The lead subsequently accepted final review and
both narrow fixes and authorized publication at frozen whole-branch head
`ae60e0fdbc892d248c1cd4bff9a52ee74a0cfc43`. Publication and the one bounded
Actions snapshot are complete; manual quick completed with a blocking comparator
error, its full evidence is retained, and weekly dispatch was accepted after
quick completion. [Executed checkpoint, exact run IDs and watcher plan](api-performance-hosted/ae60e0fdbc892d248c1cd4bff9a52ee74a0cfc43/hosted-verification-status.md)
contains actual evidence. No watcher or polling loop was launched. The commands
below remain the prepared procedure; execution claims come from that checkpoint.
D's earlier `e98e704e926961bc6d8e4a12ee15c77c1380e7a8` unit is not the final
whole-branch head.

Session and saved roster are verified; member model/effort/access are unchanged.
The branch is `2026-10-24-context-copy-performance-tests`, repository
`vpsfreecz/haveapi`, canonical remote `git@github.com:vpsfreecz/haveapi.git`.
Fixed accepted performance reference remains exactly
`b85ec364057f536940d689b09e612512ffffaf82`.

## Responsibilities and boundaries

The lead owns final branch/history review, commit/index windows, publication
coordination and any approval-bound Git refresh. Implementer3 owns diagnosis
of hosted workflow failures after publication and exact evidence interpretation.
A fresh operation-scoped watcher owns each authorized long CI wait. Resolve
the retained catalog's verification utility (`gpt-6-luna`, low), native config
and full-access policy again at launch; do not reuse an old watcher. The
utility slot is exclusive across the team, so ask the lead for its window.

Watchers observe explicit frozen run IDs/head only, retain logs/status and return
without diagnosis, retries, edits or dispatch. D then inspects failures and
assigns a cause before requesting source changes or reruns. Preserve original
failed attempts and artifacts. A timeout/inconclusive result blocks; do not
retry-until-green, relax budgets or update the fixed reference.

No release publication, PR creation/comment, repository permission/protection
change, default-branch integration, deployment or lifecycle action is authorized
by this runbook. Feature publication uses SSH; CI observation uses the existing
authenticated GitHub CLI without printing credentials. If gh is unavailable,
the lead selects the repository's prepared environment; do not install now.

## Freeze and publish after review

From the HaveAPI worktree, only in the lead-granted Git window:

```bash
repo=vpsfreecz/haveapi
branch=2026-10-24-context-copy-performance-tests
reviewed_head=REPLACE_WITH_FINAL_REVIEWED_FULL_SHA
fixed_reference=b85ec364057f536940d689b09e612512ffffaf82
test "$(git rev-parse HEAD)" = "$reviewed_head"
test "$(git branch --show-current)" = "$branch"
test -z "$(git status --porcelain)"
git merge-base --is-ancestor "$fixed_reference" "$reviewed_head"
# Lead performs any required upstream freshness/review checks first.
git push origin "HEAD:refs/heads/$branch"
git ls-remote --exit-code origin "refs/heads/$branch"
```

Record exact local/remote head equality and the reviewed base/range. A later
head change requires a new binding/check/review decision, refreshed publication
and new exact-head CI evidence. Never merge into default just to make a workflow
dispatchable. Do not hold a repository merge claim for publication or CI.

Use a new evidence directory under
`work/2026-10-24-context-copy-performance-tests/api-performance-hosted/<reviewed-head>/`.
Retain `published-head.txt`, `remote-feature-ref.txt`, final review/range links
and a copy/hash of the published workflow and budget input. Preserve old phase-1
CI records at b85; they do not verify the new performance workflow.

## Exact-head push inventory

Once publication is authorized and completed, enumerate once and give the
resulting run IDs to a fresh watcher. This command is prepared, not executed:

```bash
gh run list --repo "$repo" --branch "$branch" --commit "$reviewed_head" \
  --event push --limit 100 \
  --json databaseId,workflowName,event,headSha,headBranch,status,conclusion,url,createdAt,updatedAt \
  > "$evidence/push/runs-initial.json"
```

Create the `$evidence/push` directory first; `$evidence` is the new frozen-head
directory above. Reject run entries for another head/branch/event, not merely
the latest branch result. If the expected new workflow does not appear, D
investigates workflow parsing/event/registration before any rerun. A new workflow
may lack a normal run listing on YAML validation failure; retain the GitHub
checks/run error on the exact commit rather than calling its absence success.

Inventory the ten established workflows and the new performance workflow:

| File | Display name | Evidence expected for this head |
| --- | --- | --- |
| `rubocop.yml` | RuboCop | Ruby style job results |
| `servers-ruby-rspec.yml` | servers/ruby RSpec | Ruby 3.2/3.3/3.4 and documentation-assets results |
| `clients-ruby-rspec.yml` | clients/ruby RSpec | Triggered jobs or exact changed-path nontrigger evidence |
| `clients-go-rspec.yml` | clients/go RSpec | Triggered jobs or exact changed-path nontrigger evidence |
| `clients-php-phpunit.yml` | clients/php PHPUnit | Triggered jobs or exact changed-path nontrigger evidence |
| `clients-js-tests.yml` | clients/js tests | Triggered jobs or exact changed-path nontrigger evidence |
| `clients-python-tests.yml` | clients/python | Triggered jobs or exact changed-path nontrigger evidence |
| `clients-rust.yml` | clients/rust | Unit/style/runtime/generated acceptance if triggered |
| `i18n-health.yml` | i18n health | Localization health results if triggered |
| `release.yml` | release | Branch build/test/artifact validation; protected publish skipped |
| `servers-ruby-performance.yml` | servers/ruby performance | Compare endpoint performance AND stable Performance gate |

`_ruby-rspec.yml` is a reusable workflow, not an additional push workflow.
`update-nixpkgs.yml` is a scheduled/manual mutation workflow and is excluded;
do not dispatch it. Existing path filters can legitimately omit unrelated client
runs. Record that with the exact reviewed diff and filter instead of inventing
a result. Phase-2 server/Makefile/workflow changes must trigger the new
performance workflow; a no-work outcome for this feature is unexpected and
requires diagnosis.

For each exact run ID, a watcher may use:

```bash
gh run watch "$run_id" --repo "$repo" --exit-status
gh run view "$run_id" --repo "$repo" \
  --json databaseId,workflowName,event,headSha,headBranch,status,conclusion,url,jobs \
  > "$evidence/push/run-$run_id-final.json"
gh run view "$run_id" --repo "$repo" --log \
  > "$evidence/push/run-$run_id.log"
```

The watcher retains each command's exit independently; a subsequent successful
`run view` must not overwrite a failed `run watch` exit. Use one fresh watcher
for a related fixed run-ID batch when practical. It must return promptly on
failure, retain evidence and release the utility slot before D diagnosis. Do
not launch a second polling loop beside it or guess a generic timeout.

## Performance artifact acceptance

After the watcher completes, D downloads the exact performance run's unique
artifact, not artifacts from a branch's latest run:

```bash
gh api --method GET "repos/$repo/actions/runs/$performance_run_id/artifacts" \
  > "$evidence/push/performance-artifacts.json"
gh run download "$performance_run_id" --repo "$repo" \
  --name "performance-$performance_run_id-$run_attempt" \
  --dir "$evidence/push/performance-artifact"
```

Read the exact `run_attempt` from that run's authoritative data; preserve all
attempt identities. Artifact metadata must bind the selected run/head and
30-day requested retention, including expiry. Retain/download failure evidence
instead of treating missing artifacts as a pass. A killed job may prevent its
upload step from completing; this is an evidence gap to report.

Inspect without changing classifications:

- Both workflow jobs succeeded. `Performance gate` was created and required
  explicit `compared`, not skipped/missing output or an irrelevant-change pass.
- `selection.json` binds push event, exact published candidate, quick profile,
  whole-feature merge-base and captured exact default SHA. Reference remains
  b85. Validate available ancestry and original event data.
- `runner.exit` is 0 and `results/report.json` is schema1/status pass with exact
  baseline/candidate/profile. Every expected case/dimension is present and
  passed; missing/inconclusive/provenance/response errors block.
- Source archives/tree hashes, selection, compatible manifests, retained resolved
  locks, Nix shell/input graph, actual loaded source/runtime/ABI/gem graph and
  worker process receipts match the published head and neutral harness.
- Raw samples, canonical/raw response fingerprints and complete operation/query/
  authorization records support the reported result. Preserve noise, pilot cap,
  alternating order, timing/allocation results and hard10min job duration. Do
  not infer production latency or a wider environment guarantee.

Keep all artifacts plus their SHA-256 manifest, run/job/step JSON, logs, URLs,
timestamps, full head, commands and exits. Failure ownership: D investigates
workflow/event/setup/artifact issues; coordinate runner/comparator faults to C,
endpoint contracts to A and SQLite/query contracts to B, preserving file/Git
windows and requesting design review for consequential changes.

## Historical prepared manual quick and weekly dispatches

These are separate external mutations requiring the lead's post-review launch
direction. Do not dispatch now. For both, use the same published reviewed
candidate and exact b85 reference; do not use a moving default or D-only head.
Capture pre-dispatch exact-head run IDs once to disambiguate newly created runs.
These were the original prepared manual inputs. The later single user-authorized
quick40196045698 explicitly used the original push baseline399, as bound in its
separate authorization/dispatch receipt; it did not change the weekly reference
or grant further dispatch permission.

```bash
for profile in quick weekly; do
  # Run each profile only in its separately authorized launch/window.
  mkdir "$evidence/manual-$profile"
  gh run list --repo "$repo" --branch "$branch" --commit "$reviewed_head" \
    --event workflow_dispatch --limit 100 \
    --json databaseId,workflowName,event,headSha,headBranch,status,conclusion,url,createdAt \
    > "$evidence/manual-$profile/runs-before.json"
  date --utc +%FT%TZ > "$evidence/manual-$profile/dispatch-started-at.txt"
  set +e
  gh workflow run servers-ruby-performance.yml --repo "$repo" --ref "$branch" \
    -f candidate_sha="$reviewed_head" -f baseline_sha="$fixed_reference" \
    -f profile="$profile" \
    > "$evidence/manual-$profile/dispatch.stdout" \
    2> "$evidence/manual-$profile/dispatch.stderr"
  dispatch_status=$?
  set -e
  printf '%s\n' "$dispatch_status" > "$evidence/manual-$profile/dispatch.exit"
  if test "$dispatch_status" -ne 0; then
    # Preserve refusal; stop this dispatch path, do not retry or enable via merge.
    break
  fi
done
```

The loop illustrates both exact input sets, not standing authorization to submit
two runs at once. The lead may select only one and must keep the one utility
window rule. After an accepted dispatch, identify the newly created exact
workflow/event/head/branch run from the before/after ID set and creation time;
then give that specific ID to a fresh watcher. Do not assume latest-run order
when quick and weekly use the same workflow/head. D verifies profile and source
pair in the downloaded artifact. Quick hard10min, weekly hard30min; both block
on errors/inconclusive and preserve artifacts30days.

GitHub may refuse manual dispatch because this workflow is absent from the
remote default branch. Preserve the API/CLI refusal and exit as evidence. Do not
merge, rename branches, change workflow policy, add an automatic weekly branch
job, escalate permissions or dispatch another event as a workaround. Under the
lead's separate authorization, run the same weekly endpoint command locally
through a fresh watcher against reviewed candidate/b85 with exact source and
input receipts. That verifies the workload but leaves hosted manual/scheduled
weekly execution unverified until authorized integration and actual execution.

## Keep execution claims separate

| Mode | Local evidence already available | Hosted claim permitted only after |
| --- | --- | --- |
| Feature-push quick | Resolver/new-branch/whole-feature and aggregate unit/subprocess coverage | Exact published push run/artifact passes |
| Explicit manual quick | Manual pair and schema/exit coverage | Accepted exact-input manual run/artifact passes |
| PR quick | Head-vs-synthetic merge/base resolver coverage | A separately authorized real PR event run/artifact passes |
| Default push | Multi-commit before/after resolver coverage | An authorized real default push run/artifact passes |
| Weekly workload | Fixed-reference/ancestry/profile resolver coverage; later local weekly receipt if authorized | Actual hosted weekly profile passes |
| Sunday scheduled event | Cron/source policy checked locally | Actual Sunday03UTC default event run/artifact passes |

Do not claim PR/default/scheduled execution from a passing feature push, manual
dispatch or local replay. Do not create those events solely to fill this table
without explicit direction. Report each as passed, failed, refused, locally
verified only or unexecuted, with exact evidence and remaining limitation.

## C/D reconciliation checkpoint

C's `endpoints.rb` source currently confirms the agreed run/compare flags,
schema1 and exit0pass/1regression/2inconclusive/3error, archive tracked-blob proof,
generated-doc allowance, neutral candidate-checkout harness and profile-specific
root/server/(weekly Rust) locks. D consumes that interface without another CLI.

The reported error-provenance discrepancy is resolved by C's update, confirmed
by read-only inspection of `endpoints.rb`'s rescue path: error reports retain
`baseline_sha`, `candidate_sha` and `profile` when available, plus the available
`harness_sha256`. C confirmed this interface directly after its weekly worker
freeze release. Supplied source identities are preserved; missing arguments do
not acquire fabricated identities. D's normal invocation supplies both SHAs and
profile, so its existing report/exit/source validation remains compatible.

Keep D's absent-field checks for malformed or incomplete calls. Exit3 blocks
and preserves `runner.exit`, original report and stderr; missing or mismatched
provenance also blocks and can add a wrapper diagnostic. The accepted CLI,
schema1 and exit0/1/2/3 contract is unchanged. C's source also contains read-only
`run --help` and `compare --help` handling. No D source edit or test was performed
for this reconciliation. C's final checks/commit and subsequent narrow fixes
are included in the lead-accepted reviewed whole-branch head recorded above.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-context-copy-performance-tests/
