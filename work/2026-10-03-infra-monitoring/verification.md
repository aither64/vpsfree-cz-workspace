# Final verification and readiness

Final feature head: `f725dd3f407b0e5b82c9f9c1ad7720bbc7b14b68`.
Final tree: `8978bc46c53107705a7dc587c0f036ff6d88a219`.
Branch: `2026-10-03-infra-monitoring`, published over SSH to the same origin ref.
The project checkout/index are clean and origin/master remains base b66c929b.
Public capture-comparison recorded this exact base/head for the portal.

## Checks and review

| Evidence | Result |
| --- | --- |
| Real `confctl.machines.*.metaConfig.machineType` evaluation | Passed |
| Declared Overcommit Nixfmt/RuboCop and executable hooks | Passed; active on both final commits |
| Bash syntax, full diff whitespace and accepted source invariants | Passed |
| infra-monitoring-config + infra-monitoring-rules | Exit 0, 8 seconds |
| vps-autostart-prometheus-rules + process-count-prometheus-rules | Exit 0, 7 seconds |
| Mandatory whole-branch review, all four lanes | No Blocking/Important; Advisory R1 fixed |
| R1 focused infra-monitoring-config | Exit 0, 5.636 seconds, exact final tree |
| Final history/patch comparison | Two commits; only R1 fixture differs from reviewed tree; CPU patch identical |

Initial focused evaluation failed because synthetic services lacked `monitor`;
fixture metadata was corrected before commits and the actual checks then passed.
Review R1 found a vacuous filesystem warning equality case on an excluded mount;
the corrected test uses selected `/` at 20% and 19% on separate instances.
Lead inspected and verified this narrow correction under review steps 9–10;
no production/docs/CPU/pin changed and no reviewer rerun was required.

The four original checks ran on tree 406b654f. The final tree changes only the
filesystem fixture, rechecked through the complete config derivation. Unchanged
CPU and adjacent regressions retain their passing evidence. No unnecessary
repeat of unchanged checks was performed.

Details: [implementation](implementation-result.md), [review](review.md),
[history](branch-inventory.md), [focused result](quick-checks-2-result.json),
[R1 result](r1-check-result.json). Full logs remain locally under this session.

## Full central configuration builds

Fresh catalog-policy watcher /root/central_builds_watcher used gpt-6-luna/low
and owned both sequential local builds in the pinned Nix shell, after review.
Read-only inventory first confirmed exactly the intended replicas. Commands:

```sh
nix develop --no-write-lock-file --command confctl build --yes 'cz.vpsfree/containers/prg/int.mon[12]'
nix develop --no-write-lock-file --command confctl build --yes 'cz.vpsfree/containers/prg/int.alerts[12]'
```

| Machines | Exit | Elapsed | Built generation |
| --- | --- | --- | --- |
| mon1, mon2 | 0 | 107 seconds | 2026-10-03--17-18-19 |
| alerts1, alerts2 | 0 | 139 seconds | 2026-10-03--17-19-58 |

[Structured build result](central-builds-result.json) records exact revision/tree,
selectors and confctl log paths. Full output is central-builds.log. No unexpected
local kernel compilation occurred and no verification operation remains running.
These are local build generations, not deployed generations.

## CI and remaining operational limits

SSH feature push succeeded; remote-tracking ref matches the final head. The
repository has only a schedule/dispatch-driven daily-update workflow. Scoped
`gh run list` for the final branch/SHA returned no Actions runs (exit 0).

Ready, awaiting explicit integration direction for vpsfree-cz-configuration/master.
No default integration, production deployment, consumer-pin update or live test
notification was performed. Offline amtool covers routing, not actual delivery,
SMS activation times, repeat timers or inhibition execution. Existing routing
structures were inspected and preserved; full configs built successfully.

For a later approved rollout, update both alerters before either monitor, then
update both monitors promptly. New labels change series/alert identity and can
reset pending/rate windows; mixed monitors can still emit old unlabeled SMS-
eligible alerts. The accepted /run SMS exception does not make tmpfs expand.
Lasting policy/compatibility/rollback explanation is in
[project monitoring docs](../../worktrees/2026-10-03-infra-monitoring/vpsfree-cz-configuration/docs/services/monitoring.md).
Prepared rollout details remain in [design](design.md). No migrations.
