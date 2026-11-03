# Managed CI verification result

**Complete evidence package; core suite and all four image cases passed.
Generic workflow failed on nine pre-existing livepatch fixture jobs.**
Those nine remain failed/not-passed. No distinct failure was found in the
retained exact-head job logs. Lead owns check acceptance and integration.

- Source: `1a637e9eac4311adba2b08d60dfa7a17d07bcb52`.
- Tree: `49b8a7879e6b363349ae70808c4cdecc996e578e`.
- Owner: retained `implementer2`, thread
  `01a1a25e-a39b-7ad3-b5a3-d9afa94f9175`,
  saved `gpt-6.1-sol/xhigh/workspace_write`, unchanged.
- Both native watches exited: image exit 0, generic exit 1. An independent
  exact-command process check found no remaining watcher for either run.
- No application edits, commits, merges, deployments, CI retries/cancellations,
  team changes or session lifecycle actions were performed.

## Final CI results

| Workflow | Exact run | Result | Evidence |
| --- | --- | --- | --- |
| Generic CI | [41695511680](https://github.com/vpsfreecz/vpsadminos/actions/runs/41695511680) | failure: OS/core suite passed; nine fixture jobs failed | [final JSON](ci-managed-41695511680-final.json) |
| Changed images | [41695651867](https://github.com/vpsfreecz/vpsadminos/actions/runs/41695651867) | success: all three jobs passed | [final JSON](ci-managed-41695651867-final.json) |

Both final JSON files were independently read and asserted to match the exact
source above. Initial snapshots are `ci-managed-<run>-initial.json`.
Complete native observation logs are [generic](ci-managed-generic-watch.log)
and [image](ci-managed-image-watch.log).

Core suite job [126191147285](https://github.com/vpsfreecz/vpsadminos/actions/runs/41695511680/job/126191147285)
completed successfully, 2026-11-03 20:42:40–23:23:12 UTC.
[Complete job log](ci-managed-job-126191147285.log), lines 249–250, records
exact source/tree; lines 5385–5386 record:

```text
Run 317 test scripts of 109 tests in 7957.44 seconds
109 tests successful
```

This is an actual successful core-suite completion, not a timeout or reuse of
the baseline's 108-pass/one-failure result. Final JSON has two successful
generic jobs (OS/cache and suite) and nine failed fixture jobs.

## Four image cases selected, executed and passed

Detection job `126191399031` passed.
[Detection log](ci-managed-job-126191399031.log), lines 597–600 and 613,
lists exactly the four changed recipes and
`Detected images: centos-10-stream,centos-9-stream,rocky-10,rocky-9`.

Image job [126192300407](https://github.com/vpsfreecz/vpsadminos/actions/runs/41695651867/job/126192300407)
completed successfully, 2026-11-03 22:33:01–23:05:22 UTC.
[Complete job log](ci-managed-job-126192300407.log) records checkout at
109/122, selector at 148/173–176, actual case starts at 183/185/187/194,
successes at 192/195/196/200 and final totals at 201–202.

| Image | Selected | Executed | CI result | Duration |
| --- | --- | --- | --- | --- |
| `centos-9-stream` | yes | yes | passed | 982.18 s |
| `centos-10-stream` | yes | yes | passed | 993.49 s |
| `rocky-9` | yes | yes | passed | 858.68 s |
| `rocky-10` | yes | yes | passed | 972.43 s |

Runner summary: `Run 4 test scripts of 4 tests in 1831.14 seconds`;
`4 tests successful`. Native CI used normal 24 GiB memory/shared-memory
requirements. [Earlier local verification](verified-image-tests-result.md)
separately passed all four at the same head using the scoped 8 GiB module.
Successful jobs do not require a failure-only log artifact; full job logs
are retained.

## Failed livepatch fixtures and artifact limits

All nine failed-job logs were independently checked for the exact checkout
head, the identical fixture derivation below and subsequent missing test log.
The utility's initial terminal message miscounted eight; authoritative final
JSON and downloaded artifact inventory establish **nine**.

| Failed job | Configuration | Raw log |
| --- | --- | --- |
| `126191147517` | amd-low-memory-v5 | [log](ci-job-126191147517.log) |
| `126191147559` | amd-scale-aged-v6 | [log](ci-job-126191147559.log) |
| `126191147584` | amd | [log](ci-job-126191147584.log) |
| `126191147641` | amd-fresh | [log](ci-job-126191147641.log) |
| `126191147643` | amd-low-memory-v6 | [log](ci-managed-job-126191147643.log) |
| `126191147653` | intel | [log](ci-managed-job-126191147653.log) |
| `126191147695` | intel-representative-v5 | [log](ci-managed-job-126191147695.log) |
| `126191147777` | amd-scale-aged-v5 | [log](ci-managed-job-126191147777.log) |
| `126191147819` | intel-representative-v6 | [log](ci-job-126191147819.log) |

```text
/nix/store/vg23dzka1i0dw28fy3kl4wssyms484yx-livepatch_7-exact-candidate.ko.drv
```

[Existing baseline diagnosis](ci-failure-diagnosis.md) establishes the same
platform failing recipe/declared-input identity at baseline `dd188397`,
including AMD/AMD-low-memory-v5 and retained Intel evidence. All current
configurations have the same failure signature before test-runner execution.
The later `test.log ... not found` is a consequence. These are failed checks,
not passing lifecycle tests. Lead already accepted the documented pre-existing
fixture disposition for this feature; this package does not grant a waiver.

[Artifact metadata](ci-managed-41695511680-artifacts.json) lists nine relevant
failure artifacts, 375 bytes each. All nine were downloaded under
`ci-managed-artifacts/os-test-logs-41695511680-1-livepatch-<configuration>/`.
Each contains exactly a 64-byte expected hash
`573e8d1e05433be7c4eab361bb733e92977496f6437b43a4af1e5d21d2452d9d`
and an empty candidate-path file. There is no actual candidate hash/module or
test log. The precise checksum/readability failure remains unobserved.
No kernel build, checksum change, fixture repair or CI retry was attempted.

## Ownership, launch and managed delivery

`dev-session current` in the tracking directory matched this session; both
environment identity variables were absent, accepted via the trusted developer
binding to `/home/aither/workspace/ai/vpsfree.cz`. Live roster confirmed the
owner's exact thread/settings and package `full_access`.

Pinned catalog:
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`,
selected package
`/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0`.
Fresh operation utility `/root/ci_managed_observe` used
`gpt-6-luna/low`, full access (`danger-full-access`, approval `never`),
native config
`share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml`,
identity `dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`.
It stayed outside the roster and never used a member reporting identity.

Predecessor `/root/ci_wait` was explicitly released by the lead after both
observers exited 130; CI jobs were unchanged. A replacement setup attempt
`/root/ci_managed_watch` failed before launching watches. Parent reconciled
no running observers and corrected shell construction. The fresh successful
utility used separate native handles: generic `33773`/PID `2868129`,
image `74195`/PID `2876309`, each `gh run watch <run> --repo
vpsfreecz/vpsadminos --interval 30 --exit-status`. Parent and lead verified
process readiness. One premature utility final with live handles was handled
by resuming that same ongoing operation, without restarting observers/CI.

Only actual status/conclusions establish completion. Pending `*` markers
and names of later steps were explicitly corrected as insufficient evidence;
the in-progress API checkpoint is retained separately. Active-job log 404s
were not classified as test failures. Terminal logs used native job API
`--allow-escape-sequences`; no helper/harness or runtime changes were added.

Authenticated `report_to_lead` receipts from this retained member:

| Message | Receipt turn | Steered |
| --- | --- | --- |
| Readiness `de35f0f2-1c26-4c6d-b9c3-a716d91b4d12` | `01a1a31e-3d7a-7412-8ff5-00269633d3fe` | true |
| Readiness receipt `9541c337-027e-4dd3-b76d-09890cba54ac` | same turn | true |
| Setup escalation `790ead25-6068-4caa-9968-39e4755d14f7` | same turn | true |
| Ownership `e9fbc2d6-c851-4fc2-823f-2aa5d29e3b6b` | same turn | true |
| Image selection `b0a4c1fa-b02c-4868-ad2f-7a1943ed6f15` | same turn | true |
| Image passed `465f3de5-62b3-415a-9eb5-4b95b972472a` | `01a1a3aa-9f30-7892-9c83-f65e3890722a` | false |

Lead acknowledged image report delivery and independently verified the result.
It confirmed the report started this new lead turn, operationally observing
idle continuation. Earlier architect source-contract evidence alone did not
prove this. Utilities' passive final text was never used as a managed callback.

## Lead next action

Resume original user-approved staging integration after independently checking
current session/head/remote state, whole history, hooks and the documented
baseline failure disposition. Lead owns acceptance and the short approved merge
claim; this member neither merges nor grants integration approval. No new user
confirmation is needed for the standing approved repository/target scope.
Session remains open. Final managed report receipt is appended below.

Final authenticated message `c1e2be66-9fd0-4ab0-bfd1-b05f46052845` returned:

```json
{"turnId":"01a1a3bd-b39d-7263-ba7e-1b8aeb45ea90","clientUserMessageId":"c1e2be66-9fd0-4ab0-bfd1-b05f46052845","steered":false}
```

Utility results and managed report delivery have been handled. All raw evidence
and this report remain in the current tracking directory for the lead's fresh
integration checks; this package owner has no running verification process.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-redhat-image-releases/)
