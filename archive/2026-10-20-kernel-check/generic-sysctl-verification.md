# Generic runit sysctl service: final verification packet

Exact head `846bb469505789ba0b2a405fa5905ba6d8253006` was integrated into
remote `staging` at 2026-10-22T17:19:40Z after final review, normal hooks,
SSH publication and explicit user acceptance of the six product failures and
aged-v6 warning as merge exceptions. Claim release was verified at 17:19:57Z.
[Integration receipt](generic-sysctl-integration.md).

Original CI [39767770407](https://github.com/vpsfreecz/vpsadminos/actions/runs/39767770407)
is now terminal **failure**, attempt 1: all 11 jobs completed, eight succeeded
and three failed. It ran 11:03:56Z–2026-10-23T01:14:16Z, wall 14h10m20s
including allocation waits. Failed jobs: product suite 119793311317 (124 tests
passed, six failed), aged-v6 119793311395 (scheduler hotplug warning), and
aged-v5 119793311416 (RCU stalls). The later v5 failure was reported separately
after merge; it is outside the earlier exception. Final `amd-fresh` and `amd`
jobs passed. [First errors, all six product names and causal limits](generic-sysctl-ci-failure.md).

The final all-four-lane independent review and quick checks passed. The selected
focused VM passed all eight examples with exact exit 0 at 11:14:33Z. Its native
config/head binding and prior failure chronology remain below. The product CI's
`system/sysctl` also passed. These results do not make the broad CI green.

Terminal metadata was captured at 01:14:27Z in
`generic-sysctl-ci-39767770407-terminal-{run,jobs,artifacts}.json`; full logs and
native artifacts for all three failed jobs are retained. The sole watch ended
01:14:20Z with exit 1; its CLI and parent tool returned exit 0. The local
[no-active-observer receipt](generic-sysctl-ci-39767770407-no-active-observer.json)
confirms no matching watch remains. Monitoring is complete. Earlier local watch
exit 130 receipts record cadence control, not CI conclusions.

Branches, worktrees and session remain retained/open. No deployment, pin update,
production runtime write, retry, revert or lifecycle action occurred. Further
root-cause/test-value investigation is separately assigned; this packet does
not claim delivery to that session's lead.

## Exact complete source series

Repository/worktree: `worktrees/2026-10-20-kernel-check/vpsadminos`, branch
`2026-10-20-kernel-check`, target `staging`. Fresh explicit SSH fetch of
`refs/heads/staging:refs/remotes/origin/staging` retained base
`55c5046514d06fe9398a022c1622bdaae5228841`.

Complete base-to-head series:

1. `8528262315b0794a8f50917cf33c53a07fd14030` — panic policy v3, unchanged.
2. `846bb469505789ba0b2a405fa5905ba6d8253006` — generic sysctl service v3,
   all implementation, fixture and documentation in one coherent logical owner.

Head tree: `df9bd828d843225df749b7a05ed9529bf17425c9`; parent is exact panic
owner `852826`. Native comparison captured. Relative to published generic v2
`895870606179f0c1170ad92a5fdc49eb2d6d1bbf`, only two files change (six
insertions/four deletions): canonical literal-source conversion/comment, and
known-numeric invalid-value failure injection/log assertions. Panic source,
registration and docs are byte-identical to v2.

No merges, migrations, persisted schema/API/protocol changes, dependency/pin
updates, repeated update streams, obsolete stages or fixup commits remain in
this shipping range. Previous generic v1/v2 feature publication and CI use are
retained in evidence and exact local refs
`refs/backup/2026-10-22-kernel-check-generic-sysctl-v1` and
`refs/backup/2026-10-22-kernel-check-generic-sysctl-v2`. None was merged,
released, deployed or known externally consumed beyond development/CI. V3 was
published with an exact lease against v2; remote feature/head and unchanged
staging/base are recorded in [publication proof](generic-sysctl-v3-published-refs.txt)
and [the normal-hook push log](generic-sysctl-v3-publish.log).
[Range comparison](generic-sysctl-v3-range-diff.txt).

## Behavior and corrections

`os/modules/config/sysctl.nix`, registered in `os/modules/os-modules.nix`, adds
a logged ordinary one-shot in default/rescue and preserves stage 1. Enabled
final etc entries are selected by effective `sysctl.conf`/direct
`sysctl.d/*.conf` targets. Sorted target/source pairs drive restart triggers
and SHA256 identity. Source interpolation now matches the pinned etc renderer,
copying literal local paths into content-dependent store snapshots. This fixes
same-path edits that previously changed installed etc without scheduling apply.
No new string-path policy, renderer, parser, wrapper, switcher or control hook.

Checked nonwaiting once precedes setup/application; failures explicitly exit
before the existing one-shot footer. Successful procps `sysctl -w --system`
atomically publishes current identity at `/run/service/sysctl/applied`;
`/service/sysctl/check` rejects old identity even with legacy done. The existing
service environment carries identity to avoid etc/check-presence recursion.

The fixture in `tests/suite/system/sysctl.nix` (registered in `tests/all-tests.nix`)
has eight RSpec examples using benign settings. V2 separated boot/readiness
from the service-check budget. V3 uses `kernel.printk_ratelimit=invalid` for
actual numeric write failure, replacing an unknown key procps intentionally
ignores under `--system`. There is no product error-masking/parser change.
Feature/retry/rollback guidance remains in `docs/os/configuration.md`; the
nearby source comment explains the new conversion. Current brief:
[approved service and literal correction](design.md#literal-source-content-tracking-correction).

## Quick verification

- [Literal regression](generic-sysctl-literal-check.log): on old `895870606`, same-path
  7→9 changes actual renderer store path while identity/triggers/run/check stay
  unchanged; on fixed source, canonical trigger equals renderer snapshot for
  both contents and all identity/trigger/run/check paths change. Small before/
  after JSON command outputs are retained. No host syscall writes.
- [Ten ordinary text/store graphs](generic-sysctl-v3-ordinary-inputs.log): exact
  prior identities/triggers/generated run/check/service/panic outputs retained.
  This also binds reuse of original
  [module selection checks](generic-sysctl-module-check.log) and
  [isolated native runsv checks](generic-sysctl-isolated.log); ordinary generated
  scripts remain byte-identical. Their success/failure/stale/once/marker/control
  behavior passed with isolated sysctl mocks, never host sysctl.
- [V3 format/parse/whitespace](generic-sysctl-v3-quick.log) and
  [normal commit hooks](generic-sysctl-v3-commit.log) pass in declared Nix shell.
  Advisory 72-column warnings only; message lines meet the 80-column repository rule.
  Commit includes validation prose and chronological v1/v2/v3 history.
- [Fixture checks](generic-sysctl-i0-invalid-value-quick.log): Nix formatting,
  parsing, full graph/Ruby render and syntax pass. Source proof:
  [procps IgnoreError and pinned kernel EINVAL propagation](generic-sysctl-failure-injection.md).
- Checked module SHA256:
  `c085e16e42cd6f376dfed4a9dbf3f2779812809fab5899671bd9a6fd3632dc59`;
  fixture SHA256:
  `974690e33b6ec9428c7a6f8c74b4006dc975bc20df37e137a75a3c6493fb1be7`.

## Verification status

[First 88486 attempt](generic-sysctl-focused-failure.md) expired before guest
readiness; OS/cache gate succeeded 12:07:28 CEST before command 12:09:47. The
895 baseline then booted, passed six examples and failed the two unknown-key
failure-injection expectations. Native result is unexpected_failure; actual
outer exit receipt was lost after watcher CLI interruption and is not claimed.
Full895 log/native artifacts are retained with the
`generic-sysctl-focused-vm-895870606` prefix. Neither attempt validates v3.

The recovered old native utility `01a16333-01c8-7451-afe4-b8c8c406a16b`
(Luna/low, explicit danger-full-access/never verified from native turn context)
finished with all command handles accounted and no active old operation.
After v3 publication, exact895 CI `39764186292` was cancelled and reached
terminal status; [bounded control evidence](generic-sysctl-v2-stale-control.json)
and [terminal metadata](generic-sysctl-v2-stale-final.json) are retained.
No completed failed CI job existed at that control snapshot. No duplicate
CI observer/test was launched.
Initial preferred-account reconnect errors recovered before focused launch;
stopping its CLI then caused the avoidable exit-receipt gap. No further
verification retry occurred at that revision.

All four final reviewer0 lanes (saved Sol/xhigh) accepted the exact
55c504→846bb range: general, architecture/repetition, scope/proportionality,
risk/compatibility. The complete two-owner history, both corrections and
no-migrations/no-repeated-stream conclusions were accepted. Lead reconciled
the final report before publication or the new focused run. See
[the review record](generic-sysctl-final-review.md).

Fresh retained watcher `01a1634c-0553-7530-ba30-b19cfc2307d0` owned one related
batch: `./test-runner.sh test system/sysctl` once, plus existing exact-head CI
`39767770407`. Actual native turn context confirms `gpt-6-luna`, `low`,
`danger-full-access`, approval `never`, and the exact feature worktree. Retained
catalog digest is `ffaf9deb97720995ad1d662badae7645eba1fede5068eef529c9024efa7e7376`.
Old ownership was fully accounted before this fresh launch.

The durable wrapper PID `2229812` started at 2026-10-22T11:08:31Z; test-runner
entered `system/sysctl` at 11:08:40Z. It ended at 11:14:33Z with exact selected
exit 0, native `expected_success` and all eight examples passed. Wrapper elapsed
time was 362 seconds; runner reported 353.17 seconds. Full log and durable
start/PID/exit/end receipts use prefix `generic-sysctl-focused-vm-846bb4695`.
[Watcher events](generic-sysctl-v3-watcher-events.jsonl)
retain progress and native identity. Connection interruptions recovered without
stopping or relaunching the active command. The watcher retained the exact CI
after focused completion through its final failure, independently of the focused result. No new full OS/cache
wait was imposed: demonstrated identical local kernel/initrd and ordinary-script
equality discharge that uncertainty. Stop unexpected local kernel-image builds;
no blind retry. No second v3 attempt was run.

At 11:12:57Z the current selected log recorded examples 1–3/8 passing. The
earlier `unexpected_failure` and firmware-only observation read retained895
files in the reused native directory, including prior 12:46 CEST diagnostic
timestamps. They are not a current846bb failure or transient recovery. The
durable selected `.exit` and current log are terminal authorities; copied
native config/result/logs were reconciled to this attempt's timestamps and
tested head before acceptance.

The [terminal binding receipt](generic-sysctl-focused-vm-846bb4695-receipt.json)
records the copied native artifacts, config, SHA256 values, timestamps and
kernel/initrd/toplevel paths. The runner's immutable source snapshot is
`/nix/store/1dvy794aa5kqdk6mbq65phhv2z72a67v-test-runner-repository-source/source`.
All six changed paths match both exact committed846bb content and the clean
worktree. Actual config
`/nix/store/2mv081blizpykng7fcdi4j8k6s4isx4g-os-test-system-sysctl.json`
contains the corrected boot wait and numeric invalid-value injection, one
attempt, and the expected cached kernel/initrd. Its native symlink timestamp
is 11:10:08Z; terminal `expected_success` was written at 11:14:33Z. The copied
`machine-failure-diagnostics.log` remains explicitly labeled historical895
(10:47:33Z), not current evidence of failure.

The focused result covers boot/service application, unchanged-input overrides,
stale identity and dry/boot actions, effective-target/precedence, content and
target changes, removal/null, partial failure without automatic retry, and
explicit successful/failed same-generation retries. Literal-path content
tracking is additionally covered by the quick graph regression above. Broad
automatic CI was retained by the same watcher through terminal failure; its
final conclusion and no-active receipt are recorded above. No broad CI success is claimed.

Accepted limits: switch exit/down status alone is not completion proof;
same-config pre-start checks can be stale. Observe actual attempt completion,
invoke custom check and read back values. Partial writes are not transactional;
unmanaged edits alone do not schedule apply. Removal/null/service removal or
rollback to an older OS does not reset prior live values. Control failure
cannot certify once mode/no retries and diagnoses any stale-status limit. No
coordinated fleet update or persistent migration; stamp is ephemeral under `/run`.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-kernel-check/
