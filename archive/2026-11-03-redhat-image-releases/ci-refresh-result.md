# Refreshed CI evidence: collection complete; integration held

**Generic core failed: 102 tests passed, seven unexpectedly failed
(eight scripts). Image, RSpec and RuboCop passed.** Nine additional lifecycle
jobs failed on the independently established pre-existing fixture signature.
Lead holds integration; architect0 owns attribution/diagnosis. No retry or
source fix was performed by this package owner.

- Exact head: `54b4313404cea35b58ebb9df951ae75e27c44971`.
- Tree: `5c03648e084e907957b37263846bc5763abdac1f`.
- Reviewed base: `742eb30cb1a8b6766c85e915d26b0400e38244b1`, target `staging`.
- Owner: retained implementer2, thread `01a1a25e-a39b-7ad3-b5a3-d9afa94f9175`,
  saved `gpt-6.1-sol/xhigh/workspace_write`, unchanged.
- All owned observers/download/extraction commands ended; independent process
  check found no watcher for either refreshed run. No Git/config writer,
  repository/machine claim, deployment or session lifecycle action is held.

[Refresh mapping/review/checks](refresh-result.md) retains six byte-identical
old/new patches and no-migration history conclusion. [Old CI evidence](ci-managed-result.md)
remains at `1a637e9e`; no old result is reused here.

## Exact-head outcomes

| Workflow | Run | Actual result | Full evidence |
| --- | --- | --- | --- |
| Generic CI | [41741634771](https://github.com/vpsfreecz/vpsadminos/actions/runs/41741634771) | failure: core and nine lifecycle jobs failed; OS/cache passed | [final JSON](ci-refresh-41741634771-final.json) |
| Images | [41741634791](https://github.com/vpsfreecz/vpsadminos/actions/runs/41741634791) | success: all eight cases passed | [final JSON](ci-refresh-41741634791-final.json) |
| RSpec | [41741634539](https://github.com/vpsfreecz/vpsadminos/actions/runs/41741634539) | success: 13 components, 3297 examples, zero failures | [final JSON](ci-refresh-41741634539-final.json), [log](ci-refresh-job-126284298139.log) |
| RuboCop | [41741634674](https://github.com/vpsfreecz/vpsadminos/actions/runs/41741634674) | success | [final JSON](ci-refresh-41741634674-final.json), [log](ci-refresh-job-126284298293.log) |

All final run JSON heads were independently asserted to match the full head
above. RSpec's last 408-example/17.62-second summary is the test-runner subset,
not the whole workflow. Full OS/cache job log:
[126284299199](ci-refresh-job-126284299199.log). All runs were automatic push
runs; no workflow dispatch, retry or cancellation was made.

## Distinct core failures and ready case evidence

Core job `126350677643` failed, 2026-11-04 03:27:14–06:39:57 UTC
(3h12m43s job wall time). [Complete job log](ci-refresh-job-126350677643.log),
lines 248–249, proves exact source/tree; lines 5421–5423 report:

```text
Run 323 test scripts of 109 tests in 8514.96 seconds
102 tests successful
7 tests should have succeeded, but failed
```

Eight failed scripts span seven tests because device-units has two failures.
These are distinct from the accepted pre-runner lifecycle fixture failures;
no regression or root-cause attribution is inferred in this packet.

| Failed script | Observed error | Full case log / line |
| --- | --- | --- |
| `cgroups/mount-v1#opensuse-leap-16.1` | image not found | [log](ci-refresh-artifacts/native-failures/cgroups-mount-v1/test-runner.log), 8 |
| `cgroups/mount-v2#opensuse-leap-16.1` | image not found | [log](ci-refresh-artifacts/native-failures/cgroups-mount-v2/test-runner.log), 14 |
| `dist-config/netif-routed#opensuse-leap-16.1` | image not found | [log](ci-refresh-artifacts/native-failures/dist-netif-routed/test-runner.log), 64 |
| `dist-config/start-stop#opensuse-leap-16.1` | image not found | [log](ci-refresh-artifacts/native-failures/dist-start-stop/test-runner.log), 30 |
| `dist-config/systemd-rundir#opensuse-leap-16.1` | image not found | [log](ci-refresh-artifacts/native-failures/dist-systemd-rundir/test-runner.log), 36 |
| `systemd/device-units#opensuse-leap-16.1` | image not found | [log](ci-refresh-artifacts/native-failures/systemd-device-units/test-runner.log), 14 |
| `systemd/device-units#opensuse-latest` | device-unit command timeout | [log](ci-refresh-artifacts/native-failures/systemd-device-units/test-runner.log), 39 |
| `kernel/vpsadminos#misc-attrs` | lxc-attach pidfd error | [log](ci-refresh-artifacts/native-failures/kernel-vpsadminos/test-runner.log), 3142–3143 |

Six cases print `container image opensuse:leap-16.1 (arch=x86_64,
vendor=default, variant=default) not found in repositories: default`.
The latest device-unit case times out running `osctl ct exec testct-c580
systemctl status sys-devices-virtual-net-eth0.device`, with empty output.
The kernel case's `osctl ct exec kmisc-attrs-zfs-a9d2 chattr +i
/immutable-zfs.file` exits 1 with `__attach_namespaces_pidfd: 711 No such
process - Failed to attach to namespaces via pidfd`.

The raw stdout also includes driver/rspec's intentionally failed/retried
script-attempt fixture; attempt 2 succeeds at 2310 and the whole driver/rspec
test succeeds at 2311. It is not an additional final unexpected failure.

[Final artifact metadata](ci-refresh-41741634771-final-artifacts.json) binds
native artifact `13301471711` to run `41741634771` and exact head.
[Full native ZIP](ci-refresh-artifacts/ci-refresh-artifact-13301471711-native.zip):
3,919,714 bytes, 828 entries, SHA256
`2902ee98e3f9f8a9304855f0d5c2bf94a6a708910803318d7b2f844cc6633ead`.
Selected full case/result/diagnostic/console/shell logs are ready under
`ci-refresh-artifacts/native-failures/`: seven directories, 36 files.
No duplicate current artifact retrieval was performed by architect0.

## Four required image cases passed; upstream extras separate

Detector job `126288221452` [raw log](ci-refresh-job-126288221452.log), line 622,
selected all four Red Hat recipes plus four openSUSE cases. Existing automatic
push run therefore qualified; no duplicate dispatch was needed.

Image job `126288325476` passed, 00:15:39–01:01:08 UTC on November 4
(45m29s job wall time). [Full log](ci-refresh-job-126288325476.log) proves exact
checkout at 109/122, actual starts, 24 GiB memory/shared-memory reservations,
individual successes and final totals at 214–215.

| Required Red Hat case | Selected/executed | Result | Duration |
| --- | --- | --- | --- |
| `centos-9-stream` | yes/yes | passed | 898.14 s |
| `centos-10-stream` | yes/yes | passed | 906.86 s |
| `rocky-9` | yes/yes | passed | 1007.19 s |
| `rocky-10` | yes/yes | passed | 999.78 s |

| Extra upstream case | Result | Duration |
| --- | --- | --- |
| `opensuse-leap-15.6` | passed | 833.02 s |
| `opensuse-leap-16.0` | passed | 974.39 s |
| `opensuse-leap-16.1` | passed | 704.96 s |
| `opensuse-tumbleweed` | passed | 696.63 s |

Runner summary: eight scripts/eight tests in 2594.57 seconds, eight successful.
These native image results do not turn the distinct core failures into passes.

## Nine pre-existing lifecycle failures

The parent independently checked every complete log for exact refreshed
checkout, identical recipe/output, builder exit 1 and subsequent missing
test.log. [Baseline diagnosis](ci-failure-diagnosis.md) remains authoritative
for recipe/input identity and its limits. All nine retain FAILED/pre-existing
disposition; they are not passing lifecycle tests.

| Configuration | Failed job / full raw log |
| --- | --- |
| amd | [126350677696](ci-refresh-job-126350677696.log) |
| amd-fresh | [126350677717](ci-refresh-job-126350677717.log) |
| amd-scale-aged-v5 | [126350677758](ci-refresh-job-126350677758.log) |
| amd-low-memory-v6 | [126350677775](ci-refresh-job-126350677775.log) |
| amd-scale-aged-v6 | [126350677823](ci-refresh-job-126350677823.log) |
| amd-low-memory-v5 | [126350677965](ci-refresh-job-126350677965.log) |
| intel | [126350677750](ci-refresh-job-126350677750.log) |
| intel-representative-v5 | [126350677734](ci-refresh-job-126350677734.log) |
| intel-representative-v6 | [126350677835](ci-refresh-job-126350677835.log) |

```text
/nix/store/vg23dzka1i0dw28fy3kl4wssyms484yx-livepatch_7-exact-candidate.ko.drv
Reason: builder failed with exit code 1.
/nix/store/kmm41zgxg3ai8r84jqm2mk02r4py6cdv-livepatch_7-exact-candidate.ko
```

[Artifact metadata](ci-refresh-41741634771-artifacts.json) and nine ZIPs
`ci-refresh-artifacts/ci-refresh-artifact-<ID>.zip` retain each 375-byte failure
artifact. Every ZIP was independently opened: empty candidate-path file and
64-byte expected digest
`573e8d1e05433be7c4eab361bb733e92977496f6437b43a4af1e5d21d2452d9d`.
No actual candidate bytes/hash or test log exists there. Precise checksum/read
failure remains unknown. The unrelated 42,727,848-byte production artifact was
not downloaded. No kernel/fixture/hash repair was attempted.

## Publication, operation and metadata limits

Session/current/environment binding and live same-session saved settings were
verified. Both identity environment variables were absent, accepted via trusted
thread binding. Fresh SSH refs showed old feature `1a637e9e` and staging
`742eb30`; fetch and clean reviewed head/tree checks preceded this publication
through the prepared Nix shell, hooks enabled/signature verification 1:

```sh
git push --force-with-lease=refs/heads/2026-11-03-redhat-image-releases:1a637e9eac4311adba2b08d60dfa7a17d07bcb52 origin 54b4313404cea35b58ebb9df951ae75e27c44971:refs/heads/2026-11-03-redhat-image-releases
```

Publication exit 0; [log](ci-refresh-publication.log). Fresh SSH proof showed
feature `54b43134`, staging unchanged `742eb30`, clean local index/worktree.
Git/index writer authority was released immediately, before CI observation.

Fresh utility `/root/ci_refresh_watch` used explicit Luna/low, fresh context,
full access (danger-full-access/approval never), unchanged parent settings.
Pinned catalog `495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`;
selected package
`/nix/store/hyjxg06wbz3z7jm62338a3s3s18hn66w-dev-workspace-0.2.0`;
native utility identity
`dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`, config
`share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml`.
It stayed outside the roster and never used member reporting identity.

Initial native handles/PIDs: generic `7050/913471`, image `79291/913599`;
each `gh run watch <exact-run> --repo vpsfreecz/vpsadminos --interval 30
--exit-status`. Complete watch logs:
[generic](ci-refresh-41741634771-watch.log), [image](ci-refresh-41741634791-watch.log).

**Native numeric exits/full completion replies are unavailable for both
consumed handles:** the utility received no recoverable exit field and later
unknown-handle responses. No numeric exit is invented. Authoritative GitHub
run/job conclusions and full raw logs establish the results above; no new
watch or CI rerun was launched merely to reconstruct observer metadata.

Checkpoint-gap correction established actual core Run tests start 03:27:22 UTC.
[Exact workflow](ci-refresh-workflow-ci.yml.txt) gives full push-ci/tag-ci with
prebuild, 350-minute step/360-minute job bounds at 09:17:22/09:27:14 UTC.
The actual failure completed before both. Earlier active-log 404/BlobNotFound
responses are retained in `ci-refresh-core-live-log-*.txt`; they were not test
failures. [Matrix snapshot](ci-refresh-41741634771-matrix-complete-jobs.json)
is immutable; the utility refreshed the separate current-jobs filename after
the earlier 04:10 checkpoint, so its earlier queued states are historical.

## Managed delivery and diagnosis handoff

All lead reports used this retained member's authenticated report_to_lead.

| Message | Receipt turn | Steered |
| --- | --- | --- |
| Publication `1d0ed226-8585-4d69-a98b-2418c5f033ba` | `01a1a3bd-b39d-7263-ba7e-1b8aeb45ea90` | true |
| Ownership `a584d4ea-a31e-461c-980a-3b9e8908e31d` | same turn | true |
| Image `0297bb57-74a4-465b-ad34-bc2c066051cd` | `01a1a414-e41d-7c83-a2b2-67e21a7bdbb0` | false |
| RSpec/RuboCop `1086192b-f1ac-4de8-88a3-627eb0ad1d9b` | `01a1a418-0e5a-72a3-a903-fb1511c1911d` | false |
| Checkpoint `47e35430-8118-4978-b752-aaf5be6f1fa9` | `01a1a4bf-90bd-7412-967e-1576884b7c28` | true |
| Matrix `2c0ad6c3-7421-4269-aaeb-a8ca17de1a7b` | `01a1a4f5-6dca-7460-9a2c-32bf134d4cd5` | false |
| Distinct core failure `eadc75d7-ece0-4992-96c1-45c2680b509c` | `01a1a54c-0180-73e3-bec0-f85e19add5f5` | false |

Lead received the distinct failure, held integration and assigned architect0
bounded attribution against base742 and old1a success. Ready case paths/errors
were shared with architect0 through the managed same-session route, from
implementer2, message `6b9e1910-d854-4204-b5df-f326238a2b45`, receipt turn
`01a1a54c-b51e-7a32-bdb1-52ae8c7c8341`, steered true. Preliminary peer
message `c8919f0b-07b6-46cf-8a80-c7b344e5f3b3` used that same target turn.

No exact-base742 CI evidence was previously collected by this owner; architect0
supplied its own base-run job-log paths and requested a bounded base artifact
only if this utility remained active. It had already ended after current
collection, so availability was reported before any new operation. No baseline
artifact retrieval/new utility was started here. Architect owns diagnosis;
lead owns acceptance, state and any later approved integration. Standing
integration approval is not a claim that these failed checks are accepted.

No Git/config writer, claim or active verification/collection operation remains.
Session stays open. Actual final managed completion receipt:

```json
{"turnId":"01a1a553-5d48-76b2-acf8-19da1d7cd191","clientUserMessageId":"f6b63d4e-2273-4e3b-80de-58170a0c4b9d","steered":false}
```

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-redhat-image-releases/)
