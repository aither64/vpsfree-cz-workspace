# Post-merge CI feedback

Terminal feedback captured: core **109 tests/323 scripts PASS**,
images/RSpec/RuboCop PASS; generic workflow **FAILED** with the same nine
fixture-preparation failures proven by raw logs. One job-status API inconsistency
is retained below. **No owned operation remains.** Lead reports approved ordinary SSH integration
completed and repository claim released before this feedback package.

- Exact integrated source: `54b4313404cea35b58ebb9df951ae75e27c44971`.
- Tree: `5c03648e084e907957b37263846bc5763abdac1f`.
- Target/default: `staging`; automatic `push` events after November4 11:36 UTC.
- Scope: existing generic/image/RSpec/RuboCop runs as actually triggered.
  No dispatch, rerun, cancellation, local test, source/settings change or claim.
- Session binding verified by `dev-session current` from this tracking directory;
  both session environment variables absent, matching trusted thread binding.
- Retained implementer2: `gpt-6.1-sol/xhigh/workspace_write`, full access.
- Fresh operation utility: `/root/post_merge_ci`, fork none, explicit
  `gpt-6-luna/low`, installed full-access execution (danger-full-access/never).
  Catalog `495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`;
  catalog-supplying installed CLI package `/nix/store/myjy32qh6bd4avgym1awx180y29nvwz9-dev-workspace-0.2.0`;
  matching native `utilities/verification_watcher-low.toml` identity
  `dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`.

Utility initially used workspace-root current instead of the intended tracking
directory and mistyped the native package path. It stopped before session-file
or CI access. Parent supplied the independently verified exact directory/path;
same operation preflight then succeeded using the executable-derived path.
No observer/run was launched by that gap.

## Actual automatic batch

[Discovery JSON](post-merge-ci-discovery.json) binds these existing push runs to
staging/head54. No workflow was dispatched by this package.

| Workflow | Run ID | Actual result |
| --- | --- | --- |
| CI | 41822392601 | workflow FAILED; core109 PASS/323 scripts; nine raw fixture failures; one job-status API discrepancy |
| Changed container images | 41822392604 | completed success; four selected/executed/passed |
| RuboCop | 41822392684 | completed success |
| RSpec | 41822392741 | completed success |

Full JSON independently verifies all four exact54/staging/push identities.
RuboCop [final JSON](post-merge-ci-41822392684-final.json), job126548483585,
and RSpec [final JSON](post-merge-ci-41822392741-final.json), job126548484137,
are completed SUCCESS. Parent independently reconciled the
[new RSpec raw log](post-merge-ci-job-126548484137-logs.txt):13 unique component
PASS rows at3463–3476 and13 native example-count summaries total **3297 examples,
zero failures**. Counts are209,136,197,47,84,168,41,117,1553,119,184,34,408;
the final408 belongs only to test-runner. This is fresh staging-run evidence,
not reuse of the prior run's total.

Utility launched exact30s/exit-status native watches; parent independently
verified actual commands/PIDs:

| Run | Native handle | Shell | gh watch | tee |
| --- | --- | --- | --- | --- |
| generic41822392601 | 75277 | 402731 | 402745 | 402747 |
| images41822392604 | 76237 | 402737 | 402752 | 402753 |

Full `post-merge-ci-<run>-watch.log` files retained. This is one fresh utility
for the related batch, no duplicate observer. Generic's complete original native
reply and both shell numeric exits are preserved; image's original full-reply
limit is recorded below. Exact observer cleanup was independently verified.
Parent remains active through final managed delivery.

### Completed core, independently reconciled

One authorized current [completed-core snapshot](post-merge-ci-core-126551401008-completed.json)
and [full raw core log](post-merge-ci-core-126551401008.log) supersede the old
in-progress snapshots. Core126551401008 completed SUCCESS **14:43:45 UTC**;
job11:43:34–14:43:45 (3h00m11s), Run tests11:43:40–14:43:38 (2h59m58s).
Build126548484677 had already passed. Native bounds were job360min/step350min;
completion preceded17:43:34/17:33:40 UTC limits.

Parent verified actual suiteci/whole-suite/tagci at log246–350, exact
source54b4313404cea35b58ebb9df951ae75e27c44971/tree5c03648e084e907957b37263846bc5763abdac1f
at250–251. Initial list has323 unique selected scripts in109 unique tests;
native execution line682 agrees. Exactly109 unique successful test names equal
the selected test set. Final5393–5394: **323 scripts/109 tests,8037.71s,
109 successful**. Reconciled categories:109 expected successes,0 expected
failures,0 unexpected failures,0 unexpected successes. Coverage is verified
from native selection/execution/results, not inferred solely from job success.

`kernel/vpsadminos#misc-attrs` passed93.27s (4850); combined group passed1609.93s
(5339). Prior ESRCH did not recur here; no underlying race fix is claimed.
Successful core skipped failure-only artifact upload; evaluation/summarisation/
native cleanup passed. Earlier failed premerge runs retain their original
FAILED dispositions; this fresh core result does not relabel those runs.

**Correction:** our14:47 checkpoint saying core active was stale. It used older
watch output despite actual14:43 completion. Current authoritative completed
snapshot/raw evidence above correct that gap; no duplicate watcher or rerun.

### Terminal generic workflow and fixture evidence

[Revalidated native run JSON](post-merge-ci-41822392601-final-run-revalidated.json)
asserts run41822392601, attempt1, exact54/staging/push, **completed/failure**,
updated_at **16:25:20 UTC**. [Final job-list response](post-merge-ci-41822392601-final-jobs-revalidated.json)
records build/core SUCCESS, eight lifecycle jobs completed/failure and
amd-fresh126551401604 still in_progress. An initial terminal snapshot instead
still showed four AMD jobs queued; subsequent bounded reads resolved three.
[Targeted final amd-fresh response](post-merge-ci-job-126551401604-final-revalidated.json)
still has in_progress/no conclusion despite its complete failure log/artifact
and the completed workflow. These native responses are preserved unchanged.
No further observer/API loop was started to force agreement; the remaining
metadata discrepancy is an evidence limit, not a manufactured final job state.

All **nine** full raw lifecycle logs independently prove the accepted setup
failure: same `vg23dzka1i0dw28fy3kl4wssyms484yx-livepatch_7-exact-candidate.ko.drv`,
same `kmm41zgxg3ai8r84jqm2mk02r4py6cdv-livepatch_7-exact-candidate.ko` output,
builderexit1, then missing test.log/evaluation exit1 before lifecycle assertions.
AMD execution appears in actual logs16:19–16:21 UTC; the earlier queue state
was historical. No new failure signature was found. All nine fixture failures
remain explicitly FAILED/pre-existing, including amd-fresh's log-proven failure;
its inconsistent job-status field is not silently overwritten.

| Lifecycle case | Job ID | Raw log suffix | Native artifact ID |
| --- | --- | --- | --- |
| intel | 126551401259 | logs.zip (text) | 13318291347 |
| intel-representative-v5 | 126551401270 | logs.zip (text) | 13316624202 |
| intel-representative-v6 | 126551401277 | logs.zip (text) | 13317918952 |
| amd | 126551401115 | logs.txt | 13342197186 |
| amd-scale-aged-v5 | 126551401307 | logs.txt | 13342885086 |
| amd-low-memory-v5 | 126551401316 | logs.txt | 13341664355 |
| amd-low-memory-v6 | 126551401365 | logs.txt | 13340724938 |
| amd-scale-aged-v6 | 126551401442 | logs.txt | 13341813775 |
| amd-fresh | 126551401604 | logs.txt | 13341614576 |

Raw logs are `post-merge-ci-job-<jobid>-<suffix>`.
[Artifact metadata](post-merge-ci-41822392601-artifacts.json) binds all nine
original375-byte ZIPs to this run/head; files are `post-merge-ci-artifact-<id>.zip`.
[Independent ZIP verification](post-merge-ci-failure-artifact-verification.json)
records each SHA256 matching its API digest and exact entries: empty corrected
path plus64-byte expected hash
`573e8d1e05433be7c4eab361bb733e92977496f6437b43a4af1e5d21d2452d9d`.
The underlying checksum/read cause remains unknown; no kernel/hash repair was
attempted. The unrelated successful production-livepatch artifact was not downloaded.

[Complete native run-log ZIP](post-merge-ci-41822392601-raw-run-logs.zip)
retains94 entries/288278 bytes, SHA256
`334e1ae8c40eeaece814196bd54d75f1c9e680d83d715256cd05a21b7dd7e63e`.
Core successful failure-only upload was skipped; no nonexistent core failure
artifact is claimed. All raw case evidence and original premerge receipts remain.

Generic watch75277 exited1 naturally. Its wrapper
[completion](post-merge-ci-41822392601-native-completion.json) and **complete
original stored native reply** [raw JSON](post-merge-ci-41822392601-native-reply.json)
agree: chunk23c34a, exit_code1, wall_time_seconds26.131192509,
original_token_count1208, full4668-character output, no session_id. The utility
initially thought this object lost after compaction; parent requested the exact
public store key, and the authentic final object was recovered without
re-polling or rewatching. Both parent and utility verified all original observer
PIDs absent: generic402731/402745/402747 and image402737/402752/402753.
Utility ended its bounded receipt reconciliation. **No owned operation remains**;
no CI workflow was dispatched, retried or cancelled, and no session lifecycle action.

### Historical queue checkpoint (superseded)

At15:33 UTC parent independently read one authoritative
[all-jobs snapshot](post-merge-ci-41822392601-remaining-jobs.json):11 jobs,
five completed, **zero in progress, six queued**. All six AMD jobs have
runner_id0, empty runner_name and steps[], with no completion:
126551401115/307/316/365/442/604. All bind run41822392601/head54. The separately
[sampled base AMD job](post-merge-ci-amd-126551401115-current.json) agrees.

**Correction:** the earlier one-AMD-running interpretation of the watch `*`
marker was incorrect. That marker alone proves only nonterminal status.
Each queued job's populated started_at11:43:33 equals created_at and is not an
execution start. No remaining job or step has been admitted to time against
native job360min/step350min bounds. Queue has no runtime ETA; no deadline is
derived from those placeholder timestamps. This is a runner-assignment queue
dependency, not a test failure or proven stall.

This was the15:33 checkpoint; the terminal native workflow/raw execution evidence
above supersedes its queue state. No runtime ETA was assigned to that wait.

Three completed Intel lifecycle jobs126551401259/270/277 FAILED before tests.
Parent independently inspected all three raw logs
`post-merge-ci-job-<id>-logs.zip` (verbatim text despite suffix):
`/nix/store/vg23dzka1i0dw28fy3kl4wssyms484yx-livepatch_7-exact-candidate.ko.drv`,
output`/nix/store/kmm41zgxg3ai8r84jqm2mk02r4py6cdv-livepatch_7-exact-candidate.ko`,
builderexit1 then missing test.log. This matches the accepted pre-existing
fixture signature; the new jobs remain explicitly FAILED. The remaining AMD
fixture failures are retained in the terminal evidence above.

Images build126548484031/detector126548866844/test126552086702 all SUCCESS.
Test job ran11:45:06–12:10:36 UTC,25m30s. Parent independently asserted
[terminal full JSON](post-merge-ci-41822392604-final.json): exact54/staging/push,
completed success. Parent independently read
[raw detector log](post-merge-ci-job-126548866844-logs.txt): line590 compares
base742eb30 to54; lines594–597 list four changed build.sh paths; line610 selects
exactly **centos-10-stream,centos-9-stream,rocky-10,rocky-9**. No upstream extras
are selected in this staging run.

[Actual image-job raw log](post-merge-ci-job-126552086702-logs.txt) lines169–173
select all four; resource reservations179–189 prove native24 GiB RAM/shared
memory and4 CPUs per case, with ordinary resource waiting for the fourth case.
Lines188–197 prove exactly all four executed/passed; summary4 scripts/four tests,
1410.21s, four tests successful. No extra upstream cases were executed here.

| Image case | Result | Seconds |
| --- | --- | ---: |
| centos-10-stream | PASS | 789.11 |
| centos-9-stream | PASS | 647.28 |
| rocky-10 | PASS | 767.26 |
| rocky-9 | PASS | 762.91 |

Successful image workflow had no downloadable artifacts (failure-only upload);
full raw job log and finalJSON retain authoritative evidence. Image native
wrapper completion records exit_status0. Utility saw original native
wait exit_code0/session ended, but its parallel tool display was truncated
and the complete original result object was not retained. That full object
is unavailable; it is not reconstructed from the wrapper JSON. Full stdout
remains in tee log and terminal job/run JSON proves success. No ended handle
was re-polled or new watch launched to manufacture a receipt. Generic's original
reply was recovered as documented above. Parent independently checked all
image and generic observer PIDs absent. No replacement observer was launched.
Unchanged workflow bounds: build180min, detector15min, testjob86400min with
no step override. This configured value supplies no completion ETA.

Earlier active-run files named `post-merge-ci-<run>-final.json` were intermediate
snapshots. Native revalidated final responses above preserve the terminal run
and remaining job-status discrepancy. Same SHA alone establishes no
input/derivation equivalence; this report uses fresh observed results.

Preparation checkpoint authenticated managed receipt:

```json
{"turnId":"01a1a656-bd5d-7d53-b0f8-db38382a1fb3","clientUserMessageId":"e0d91cd5-dd89-4b8a-b959-1bf8c8e79b26","steered":true}
```

Actual managed ownership readiness receipt (initial uncertain response reconciled
by retrying the identical message and same ID):

```json
{"turnId":"01a1a656-bd5d-7d53-b0f8-db38382a1fb3","clientUserMessageId":"528efc8a-b0fa-45d0-9670-b86909b2d980","steered":true}
```

Raw four-image selection managed receipt:

```json
{"turnId":"01a1a656-bd5d-7d53-b0f8-db38382a1fb3","clientUserMessageId":"98ff079c-adac-4633-8444-d64ed1017557","steered":true}
```

Fresh terminal Ruby scope managed receipt:

```json
{"turnId":"01a1a670-d2c9-7520-b00b-328a82d0135d","clientUserMessageId":"fd72f55b-67dc-4e92-8540-5cd40f16b7eb","steered":false}
```

Four-image pass and subsequent native-object limitation receipts:

```json
{"turnId":"01a1a679-f75a-7612-aab5-d8c744ee92e7","clientUserMessageId":"70dbb40e-a5bb-45ad-a9fe-b3490e92bb6e","steered":false}
{"turnId":"01a1a679-f75a-7612-aab5-d8c744ee92e7","clientUserMessageId":"0f395da5-6e9b-416c-9b58-d00c3426bb1b","steered":true}
```

14:47 UTC existing-watch checkpoint managed receipt:

```json
{"turnId":"01a1a708-195d-7620-8306-15f746ade8fc","clientUserMessageId":"4810f01e-04a0-43dd-a5a9-61bdd618e30b","steered":false}
```

Authoritative core109/323 PASS and stale-checkpoint correction receipt:

```json
{"turnId":"01a1a71d-0799-73b3-a37f-c5c58c552ff5","clientUserMessageId":"33bc94d1-ccfb-479c-9ef2-9cf779c54ab4","steered":true}
```

Authoritative six-AMD queued/unassigned correction receipt:

```json
{"turnId":"01a1a732-a1fc-7672-83e0-4ab6f94b40fd","clientUserMessageId":"048a6753-908c-45d7-9154-503b1b9d1c4c","steered":false}
```

Final package authenticated delivery receipt, starting a new lead turn:

```json
{"turnId":"01a1a76c-e179-7f71-bad4-857cbcf48137","clientUserMessageId":"a97c9314-c207-442a-a9e5-6d2a80696783","steered":false}
```

## Earlier evidence retains its scope

[Premerge full CI](ci-refresh-result.md) remains FAILED: core102 passed/seven
failed groups/eight failed scripts. Seven openSUSE script failures were accepted
as FAILED/exact-base; nine separate `vg23dz...` livepatch fixture jobs remain
FAILED/pre-existing. Prior `misc-attrs` LXC namespace-attach ESRCH remains
intermittent/unfixed.

[Focused CI](kernel-group-verification-result.md) passed the full14/native6
group at54 without reproducing ESRCH; this did not establish its cause or fix.
Earlier exact54 image4 Red Hat+4upstream/RSpec3297/RuboCop successes remain
premerge-run evidence. Same SHA alone establishes no new input equivalence.

Implementer2 completed terminal evidence and authenticated managed delivery;
no owned operation remains. Lead owns state/acceptance. No source delivery or integration approval remains
pending; no deployment or session lifecycle action is authorized.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-redhat-image-releases/)
