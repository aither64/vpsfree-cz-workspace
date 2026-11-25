# Exact-head automatic CI: native job failure

Run [39600028637](https://github.com/vpsfreecz/vpsadminos/actions/runs/39600028637), head `b81c43ff6865a033268072f55cd94ad763d0630b`, attempt 1. Native job `119228578900` failed after 3h36m46s. The run subsequently completed with failure at 2026-10-22 01:11:10 UTC: all other ten jobs (OS build plus nine livepatch jobs) passed. No rerun, new test, source change or cancellation was performed for this failure.

The native runner completed 337 scripts in 129 tests: 124 tests passed, five unexpectedly failed. Each first failure is `RSpec::Expectations::ExpectationNotMetError` at `assert_retained` in `tests/suite/upgrade/common.nix:1534`: the impermanent guest's reported `boot_dataset` changed from its saved clone to `tank/ct/niximpermanent` after successful userspace activation.

| Test | Saved dataset suffix | Kernel throughout | Container init PID throughout | Shell lines: switch / post-switch dataset |
| --- | --- | --- | --- | --- |
| upgrade/from-6.12-guests | 685182 | 6.12.95.6 | 6138 | 2823 / 3209 |
| upgrade/from-6.12-guests-v1 | b78356 | 6.12.95.6 | 6290 | 2769 / 3155 |
| upgrade/from-6.12-inherited-guests | e53faa | 6.12.95.6 | 7301 | 4063 / 4558 |
| upgrade/from-6.18-guests | e901ed | 6.18.49 | 8939 | 5343 / 5752 |
| upgrade/from-6.18-guests-v1 | 433e6e | 6.18.49 | 6883 | 3529 / 3928 |

Expected dataset is `tank/ct/niximpermanent.impermanence-<suffix>`. Actual is `tank/ct/niximpermanent` in every case. All five containers remain reported running. The 6.18 v2 case additionally times out in teardown `poweroff -f`; that occurs after the dataset assertion and is not its first error.

## Relevance to the panic policy

The five actual shell traces show `switch-to-configuration test` succeeded, then the same kernel release, boot ID, and `/run/booted-system` as before activation. They then reach the dataset assertion; init PID and its previously asserted process birth identity remain unchanged. `common.nix:308` deliberately boots the pinned predecessor, and `:1679` onward enforces unchanged kernel/boot identity before `assert_retained`.

The new source changes only the option description and `boot.kernelParams` under the existing `mkIf cfg.enable` (`os/modules/misc/crashdump.nix:156,419`). The flag is consumed at kernel boot, with no added runtime sysctl. These failures never boot the current generation, so they never parse its new `nmi_watchdog=panic` argument. This is direct execution-path evidence excluding that argument as the cause of these five first errors, independent of the size of the diff. No hardlockup or kernel panic report appears in these five console logs.

The option defaults false. These guest switches contain no crashdump-service operation. Those observations are supporting context, not an attestation of each realized crashdump boolean or `/proc/cmdline`; the actual unchanged boot identity is the stronger exclusion. No new evaluation was run to fill that unnecessary gap.

## What is and is not established

High confidence: the observed first failure is inherited impermanence run-state recovery/reporting across userspace activation, with the new boot argument not executed. The API export (`osctld/lib/osctld/container.rb:853`) obtains `boot_dataset` from `run_conf.dataset`, falling back to the configured base dataset without `run_conf`; `container/run_configuration.rb:341` also defaults a missing dataset key to the configured base. This explains the observed form but does not distinguish a lost runtime file, missing key, or replacement run configuration.

The precise runtime-loader root cause and whether the actual mounted ephemeral root remains correct are unresolved. The artifact uploads logs/text, not the relevant pre/post runtime `config.yml` bytes; do not infer data loss, benign behavior, or baseline reproduction from this API mismatch. There was no baseline comparison run. Smallest useful follow-up is read-only inspection of the inherited run-configuration loading/preservation path and any retained runtime metadata; a later isolated diagnostic would need the pre/post runtime file and actual mount source, not a blind CI rerun. No panic-policy edit is justified by the evidence so far. The broader CI is failed and cannot be called green.

## Preserved evidence

- [First failed-job log](os-hardlockup-ci-first-failed-job.log), full 5,700+ lines. Final summary at lines 5509–5520; artifact upload receipt at 5574–5578.
- [Native artifact ZIP](os-hardlockup-ci-native-logs.zip), all 950 members, 4,720,560 bytes. SHA256 `85eadc310707dc36ffc4f1c662214172a1abf857fed9aef317d0176a7dab30fa` matches the uploader's digest. Artifact ID `12359659166`.
- [Artifact metadata](os-hardlockup-ci-first-failure-artifacts.json).
- Extracted five cases under `os-hardlockup-ci-native-logs/`; each `test-runner.log:3` records the first assertion error and its `machine-shell.log` contains before/after observations. Original ZIP is retained intact.
- [First locally observed failed job state](os-hardlockup-ci-first-failure.txt).
- [Existing watcher output](os-hardlockup-ci-new-watch.log), retained through terminal completion.

The first log-download attempt refused terminal escape sequences; the explicit `gh api --allow-escape-sequences` retry downloaded the unchanged completed job log to a local file. This retried evidence retrieval only, not CI execution.

Final CI metadata is [os-hardlockup-ci-new-result.json](os-hardlockup-ci-new-result.json); all 11 jobs are terminal. The full [all-job log](os-hardlockup-ci-new-jobs.log) independently confirms the five-case final native summary at lines 7155–7162. No diagnostic or CI retry was performed after this bounded triage.
