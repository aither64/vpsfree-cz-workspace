# Native CI follow-up, 19 October 2026

Exact published head: `a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1`.
[CI39068521841](https://github.com/vpsfreecz/vpsadminos/actions/runs/39068521841)
finished with a failed native suite. OS build, RSpec, RuboCop and four livepatch
profiles passed. Six livepatch profiles had no steps and were cancelled after24h;
their coverage was not executed. No job was rerun.

## Preparation and original regression

Native job117523492265 ran on gh-runner3.int.vpsadminos.org. Log694 records
102400MiB assigned,101437MiB initially available,8192MiB reserve,93245MiB usable,
8192MiB/job estimate and inherited Nixmaxjobs48, yielding11 preparation jobs.
Logs695–702 show all127 exact configurations prepared from05:55:33Z to06:30:37Z
before runtime began335 scripts; the first VM reservation follows completion.
Runtime retained91.1GiB RAM and72 guest CPUs (48*1.5). Build logs report48
compressor processors. No runtime nix-build/derivation-build line appears;
this is log evidence, not independent process tracing.

All12 original persistence scripts passed, with shared group3662.63seconds and
artifact result expected_success.126 of127 test groups succeeded. This is a
second physical builder in addition to local32/16GiB admission-ceiling checks.
There is no aggregate daemon peak or arbitrary-build OOM guarantee.

## Sole native failure

`native-ci-final-artifacts/os-test-upgrade__from-6.18-guests-7613a053/test-runner.log`
lines2–3: assert_guest_ready(nixold) reported systemctl readiness degraded after
496.31seconds. Lines21–22 and140–144 identify network-setup.service failing to
apply ambient capabilities before UID change: Permission denied,218/CAPABILITIES.
Guest versions were NixOS22.11/systemd251.16 on predecessor kernel6.18.49.
AmbientCapabilities was empty in the captured unit properties; no specific
missing capability or syscall/LSM cause is established.

The guest failed before the upgrade: machine-shell.log2517 creates nixold,
2569 starts it,2594–2600 reports degraded. No switch-to-configuration ran.
Source tests/suite/upgrade/common.nix1074–1114 creates and checks predecessor
guests; switching is later at1667. from-6.18.nix pins predecessor
3cb830e596a7fed900bec49f50c9b6cf51e76bb5. common.nix308–315 preserves predecessor
daemon/LXC/kernel/policy, replacing only test transport. This branch changes
neither the fixture nor capability policy. common.nix396–397 already documents
intermittent predecessor access denial, introduced by bcfc50745 on13September;
these logs do not prove that this is the identical prior issue. Scheduling/timing
sensitivity cannot be fully excluded without comparison.

The later poweroff timeout of900seconds is secondary cleanup, not the original
readiness cause. Guest diagnostics show about4401MiB available of7952MiB. A
captured OOM belongs to an intentional limited-container resource probe
(common.nix815–817), not evidence of runner OOM.

## Disposition

Architect0 completed read-only diagnosis; lead checked the primary failure and
preparation boundary. No resource implementation fix is justified by this
evidence, and readiness assertions must not be weakened. Overall CI remains red.
A separate investigation would need the exact predecessor/systemd capability
syscall/security denial; a bare rerun would not establish its root cause.
No source change, rerun, merge or deployment was performed. Session remains open.

Evidence: native-ci-final-job.log and downloaded native-ci-final-artifacts
(artifact12131444137). Source and evidence line numbers above refer to this head
and the original failed attempt, respectively.
