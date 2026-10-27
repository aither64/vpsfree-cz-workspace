# C4 postreview results: accepted and own branch published

Latest evidence: the released one-pair desktop expiry comparison passed at both
exact f10 and baf, using isolated complete original sources/locks and the same
rooted FHS/browser at CPU60–63/nice5. Original unchanged assertions all passed;
source/lock/runtime/process/port afterchecks passed. See the
[paired receipt](expiry-paired/receipt.md). Both prior failed six-case runs below
remain preserved. The paired passes do not prove their exact cause or a
preexisting defect; no combined clean six-case result is claimed. Publication
was held pending lead disposition at that checkpoint. Lead has now accepted the
scoped current-correctness evidence and released ordinary publication. The new
own branch is published at exact baf; independent remote proof, comparison,
retained artifact identities/roots and bounded CI discovery are in the
[final publication receipt](publication/receipt.md). CI discovery found no run
for this own-branch push; no CI success or combined browser pass is claimed.

Exact reviewed head `baf00acc31d34ab37720643c5833b4476a341f3b`, tree
`2e7b4cb5eba6bc96f34f834c49fc097d5fdd987b`, base5a2d2bdc.
Independent all-four-lane final review accepted by lead with no findings.
Source remains clean; no postreview source/test/fixture change or review rerun.

Required batch1 PASS0/774s:228 script,57 BFF,303 unit files/1899 cases,
normal production build. [Full log](batch1-tests-build.log),
[exit](batch1-tests-build.exit), [normal metadata](normal-build-info.json).
Exactbaf/dirtyfalse metadata verified. BFF dependencies were absent in successor;
ordinary npmci used unchanged BFF lock. Root installation was not repeated.

Batch2 PASS0/77s: normal frontend/BFF/provenance/source/package-content outputs.
[Results](batch2-nix-results.json), [log](batch2-nix.log),
[drv/output identities](nix-output-identities.json),
[complete recursive graph](nix-recursive-input-graph.json),
[full flake locks](final-flake-metadata.json),
[NAR/references](nix-output-nar-info.json), [owned roots](nix-root-map.json).
Frontend `/nix/store/729jjifw96nb2hvh902563jfh7mjma00-vpsadmin-webui-frontend-1.0.0`,
NAR `sha256-fcxN91fpQaDJP4vZdtNWnlwjs32AQKo5TgXcwf7ULwQ=`.
BFF `/nix/store/l93gg2jcx91ir8qrrbv8x1zl5f4q7izh-vpsadmin-webui-bff-0.1.0`,
NAR `sha256-zonVCNBbQpuKId85O8Nbs3CL/b20FH4jH2dbWXvSoWY=`.
Metadata equal, exactbaf/dirtyfalse/sourceenvironment. Contents check370assets,
source guard15files; no kernel build/VM/cluster action. Preparatory plain-path
getFlake evaluation producedunknown/dirty, caught before any realization;
ordinaryGit-backed selectors then verifiedexactbaf/false. Rejectedpreflight
identities retained separately, not used as build or package proof.

## Bounded browser verification

Only2existing files×2projects=6cases: authenticated_home_smoke (2cases) and
session_expiry_redirect(1case), chromium/mobile-chrome,2workers0retries.
Native list provedexact6 before execution; no full62 or baselinecampaign.
Same retained standardFHS185pathclosure, Node24.21/PW1.61/Chromium1228/ffmpeg1011,
byte hashes and before/afterNAR/reference equality; no policyflags/runtime swap.
A0holdssoleutilityslot, explicitparentfallback; everyhandle completed/reconciled.

Original run atCPU62-63/nice10 FAILED1/73s,3pass3fail. DesktopdashboardLoading
and both expiryURLassertions hit15sexpectdeadline. [Originallog](batch3-browser.log),
[JSON](browser-results.json), [artifacts](browser-artifacts),
[traceboundary](browser-trace-boundary-summary.json), [afterchecks](browser-afterchecks.json).
Trace shows slowcoldVite imports, promptactualcurrent-user responses and public
lazyLoading after hardredirect. This is evidence, not a preexisting disposition.

Lead authorized one environment-only correction: prioracceptedCPU60-63/nice5,
allsource/runtime/fixtures/assertions/timeouts/workers/retries otherwise identical,
no prewarm/framework. Freshpreflight passed, completeSAME6run FAILED1/39.3s,
5pass1fail: desktop+mobileauth/no-description andmobileexpiryPASS;
solefailuredesktop expiry stillLoading atfinalURLassertion.
[Correctedlog](browser-corrected.log), [JSON](browser-corrected-results.json),
[artifacts](browser-corrected-artifacts), [trace](browser-corrected-trace-summary.json),
[afterchecks](browser-corrected-afterchecks.json). Both failedruns remain distinct.

Remaining desktop trace: users/current40137ms at12.615s, hardredirect to
/?session=expired12.711s; reloadedmain27ms14.376s; Overviewmodule64ms19.661s,
secondcurrent40141ms19.680s; public_stats20034ms20.657s nearassertiondeadline.
Screenshotpublicshell/mainLoading. OverviewPageeffect removesexpiredquery after
lazycomponentmount. No pageerror, expectedoptionalconfig404/401only. Runtime
bundle0.30.2/0.31.0byte-equal afteronlyversionstringreplacement independently
verified, application/fixtures equal f10. Loading/resource hypothesis remains
plausible, not accepted as green/preexisting. At that checkpoint no further run
or edit was assigned; the subsequently released paired result is linked above.

Source/hash/closure afterchecks pass, noownedVite/browser remains,52847no
listener and reusablebindPASS. ImmediateexclusivebindinitiallyEADDRINUSEafter
closure, followed by no-listener/reusablebind proof; no signals sent.

Publication was held until lead accepted the paired passes above; the final
publication receipt records the released own-branch push. PR74/PR63/default/
livef10 remain untouched. Old60/62/twoacceptedmobileexpansionresiduals
remain historical, not a disposition of these new failures. Lead/architect owns
the disposition; existing requiredtest/build/Nixpasses are retained.
Lateruserauthorizedclusterredeploy/reset belongs tolead/E3; noCnativeaction.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
