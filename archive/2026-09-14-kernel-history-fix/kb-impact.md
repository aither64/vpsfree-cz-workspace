# Kernel history documentation impact

The canonical KB check passed at contract head
`8789cc1f5aeb3b19cbff13f741d6dd9960f14567`, pinning tested vpsAdmin
`c38839d5be62e9d40d055b23a84844e2037ba4db`. No prose changes or capture
regeneration are needed.

The fix changes stored observation bounds rendered by the existing node history
UI. It changes no WebUI source, route, label, layout, semantic ID, or meaning of
the documented controls. The contract's node.kernel-history,
node.kernel-boot-evidence and related bindings remain valid. The selected WebUI integration scenario passed. Its rendering source and both
feature patches are unchanged by the final rebase over the upstream DDNS fix. The recovery checkpoint is private and adds no
visible evidence resource or field.

`nix develop -c bin/check` validates 45 controls, 36 paths, 35 capture concepts,
3 semantic selectors, 94 bindings, 9 exceptions, 4 pages/8 variants, 12 page tests
and 21 executable samples. All checker suites pass (60 runs, 194 assertions),
and all 120 PNG variants validate. No semantic fingerprint drift was reported.

Only the five canonical revision files changed. Existing vpsAdminOS and nixpkgs
pins were preserved with the recorded Nix override after updating vpsAdmin.
No production KB fetch, page write, staging, or publication was needed for this
result. Both preceding K610cb7bf GitHub workflows passed: Check34877456478 and
Managed page runtime34877456477 (12 scripts,4 tests,2337.54s). After the final
rebase, bin/check passed again in both feature and fresh integration worktrees.
K8789cc1f is merged into master and pins Vc38839d5, also merged. New master runs
are Check34950343075 and Managed page runtime34950343064; they remain pending.
