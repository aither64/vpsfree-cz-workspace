# Hotplug source-only commit packet

Review remediation pending: recorder source and its documentation now have the
selected shutdown correction prepared outside Git. The hashes/checks below
describe original reviewed `9bea27c9`, not corrected-source validation. See
[current source/check packet](review-shutdown-fix.md): selected native syntax and
all41 actual-helper mocked cases pass, with the old false-complete path
reproduced. Packaged build and logical-owner folding remain separately
unselected. Frozen runtime inputs use the old binary and remain held.

Both logical units are committed and on the feature branch:
health `81235fe742c5e8382997a1cb0b09f983f22a0456`, recorder/docs
`9bea27c93beb22d08c3be2eb481bce4ef57300a6`. Normal hooks pass. The single selected
feature FF from4de50f completed under authorization
`dc02e400-ee25-4a49-8192-36d96ef9e6e1`; stage2 window was explicitly released
through lead report `d905e800-32a7-4e99-bc4b-12ae1c1f1461`. All7647 peer paths and
six owned bytes/modes are preserved, index empty. Exact authoritative completion
proof is `commit-stage2-result.json` and `commit-stage2-final-effects.json`.
Retained isolated source/backups remain. No push, default merge, build, runtime
or cleanup occurred. Whole-branch final review stays with the lead.
Neither commit establishes the warning's cause or runtime BPF admission.

1. `tests/suite/kernel/livepatch-6.12.95/qualification.rb`: label the two hotplug
   phases and check the existing cumulative kernel-health baseline after each
   CPU/progress check. Predecessor warnings fail before replacement. Keep all
   existing later health, transition, migration and removal requirements.
2. `tests/suite/kernel/livepatch-6.12.95/hotplug-recorder.{nix,c,bpf.c,h}`:
   standalone experimental exact-binary diagnostic utility, not called by
   ordinary qualification. Its Nix function requires the caller's authenticated
   `vmlinuxHeader`. Native loading is guarded by original GNU build ID and fixed
   CPU127/predicate offset; file/ring/deadline/loss limits refuse incomplete data.

`livepatch-6.12.95-common.nix` is unchanged. Opt-in first-hotplug orchestration
has not been implemented and remains outside these units. All `repair/hotplug/`
fixtures, guard/operation scripts, extracted header and receipts are session-only;
do not stage them into the product. There is no kernel/configuration pin change,
SDK rebuild, protocol/schema migration, production service or automatic test
registration in this boundary.

Current exact source SHA-256 values:

| Owned shipping path under `tests/suite/kernel/livepatch-6.12.95/` | SHA-256 |
| --- | --- |
| `qualification.rb` | `fabdb90594721190ada783d6927f8bb7c9f592559fe595d60af3943432c026d7` |
| `hotplug-recorder.c` | `fdbf4429808966f5bd1bfe9b6e3674a8daceb8cb8868be1291f499cb3edfae4f` |
| `hotplug-recorder.bpf.c` | `86ac6ec888871749104d694f56400222c4d1bf6c2804e8109237daf0768b9370` |
| `hotplug-recorder.h` | `8ec5f644bfd1c011454d2da4513909d6d316583c44374e4f07cb3312a09a282d` |
| `hotplug-recorder.nix` | `baee3b6c8d77af5df159f00dd0f348cdef09273c3611f67bed3a8597c3942741` |

Fresh declared-environment checks: Ruby3.4.9 `-c` reports Syntax OK; direct
prepared-env RuboCop inspects one file with no offenses (existing renamed-cop
configuration warning only); Nixfmt1.5.0 `--check` passes. Both hotplug callers
supply their phase. Normal Overcommit hooks remain mandatory during the lead's
Git window; these checks do not bypass or replace them.

The same four recorder sources and frozen generated header
`82ac9ea144b1f92f35b8cc2eb947ce672cfca6d06a60fe9e925a40ff30e51484`
were built successfully in the selected build2: drv
`v9f0794pzylhgc7r9lj7afw37b6l8wgy-livepatch-first-hotplug-recorder-1.drv`,
output `q4isqny2rdrj41ivcj400sd3p4fpnjmi-livepatch-first-hotplug-recorder-1`.
Native C/BPF compilation and help/rejected-argument CLI checks passed; binary
SHA-256 is `098fa4cacfee98cc6427b721c9a349da08833864ac42adfe663db0c44e8980a5`,
BPF object SHA-256 is `4aab6cc08451097034be7fae91857b6b324e8352701afe206d61c5b3b29cbb8b`.
No compiler rebuild or VM is needed merely to commit this unchanged boundary.

Runtime attachment, verifier admission, observed count changes and zero-loss
recording remain unproven. They are execution gates before relying on the tool,
first-hotplug wiring or aging, not prerequisites to finishing these two bounded
source units. Any admission-discovered source repair belongs in the recorder's
logical owner and receives the applicable focused checks/review; do not claim
promised orchestration exists. Actual warning attribution and a proven kernel
repair remain open work, not acceptance supplied by a tool build.

Owner3 owns project test documentation. It should distinguish early cumulative
health checkpoints from experimental recorder admission and state that the
ordinary workload/aging/quarantine/ABI/recovery contracts are retained. This lane
has not edited those shared docs. Whole-branch independent final review remains
with the lead after all intended sources/docs are committed and quick checks pass.
No integration or deployment approval is present.

## Isolated stage1 partial checkpoint (historical)

This checkpoint predates the successful continuation and final stage2 above.

Lead selected stage1 only at exact4de50f0046052d377780a3be3a9aeec37ad86f6e. Plan/messages were recorded first in `commit-stage1-plan.json` and `commit-messages/{health,recorder}.message.txt`. Entire20line docs stay with recorder: the first health paragraph gives context for ordinary qualification already implemented by the parent. No shared FF is selected.

Health commit81235fe742c5e8382997a1cb0b09f983f22a0456, treef2c5065769c36058fe6605993e39f598d9f721ff, contains only qualification.rb and passed normal pre-commit/commit-msg plus fresh Ruby syntax/RuboCop. The recorder+docs remain exactly staged in the retained clean-origin detached `vpsadminos-hotplug-commit`; the guard stopped its read-only staged diff before commit. No recorder commit exists yet.

`commit-stage1-reconciliation.json` proves shared4de50f/indexbyteexact and empty, all7647 tracked/untracked/ignored peer paths unchanged in bytes/type/mode, all6 originals backed up, and no remaining native groups or accessible canonical isolated references. Protected foreign descriptors were not claimed inspected. Owned allocation upper349188096B is below1GiB; freshfree134589825024B exceeds40GiB. The stop was caused by treating a4636897280B global df drop as owned growth. The initial nonexistent absolute Git precondition failure is retained separately; corrected existing Git2.54.0 runs require no installation.

Current stage1 window explicitly released through lead reporta05951cd-3543-49e9-923e-f219daf868de. Preserve both isolated tree/index and all shared bytes. Narrow continuation will count owned allocation independently from shared df, retaining1GiB/8MiB/40GiB/55s and cumulative600s bounds; lead must select it before further Git mutation. No rebuild, runtime, shared FF or checkout cleanup occurred.
