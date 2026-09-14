# Kernel history documentation impact

The canonical KB check passed at contract head
`61aaf95d3dc0968728131a2cf4d4740dae6e9250`, pinning tested vpsAdmin
`337c9257f5e11f36afe81eba4951e267b83e2fc7`. No prose changes or capture
regeneration are needed.

The fix changes stored observation bounds rendered by the existing node history
UI. It changes no WebUI source, route, label, layout, semantic ID, or meaning of
the documented controls. The contract's node.kernel-history,
node.kernel-boot-evidence and related bindings remain valid. The selected WebUI
integration scenario passed; its rendering code is unchanged at the final pin.

`nix develop -c bin/check` validates 45 controls, 36 paths, 35 capture concepts,
3 semantic selectors, 94 bindings, 9 exceptions, 4 pages/8 variants, 12 page tests
and 21 executable samples. All checker suites pass (60 runs, 194 assertions),
and all 120 PNG variants validate. No semantic fingerprint drift was reported.

Only the five canonical revision files changed. Existing vpsAdminOS and nixpkgs
pins were preserved with the recorded Nix override after updating vpsAdmin.
No production KB fetch, page write, staging, or publication was needed for this
result. The final contract branch's GitHub Check and Managed page runtime
workflows both passed at pushed head 61aaf95d: Check 34837590578 and
Managed page runtime 34837590575. The runtime log confirms all 12 scripts across
4 tests passed in 2378.07 seconds. The final pin review found no issues.
