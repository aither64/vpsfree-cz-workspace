# C postreview verification

## Latest status: current f10 verification

Unit/script/BFF, normal production build and Nix package/source/provenance/
contents checks passed. Exact normal artifacts restored and persistently rooted.
Fresh rooted browser batch:60/62 passed (desktop31/31,mobile29/31); two mobile
transaction-expand clicks timed out with pointer interception. Exact-base
comparison reproduces both boundaries. Architect recommended and lead accepted
this specific preexisting interaction residual as nonblocking for scoped HaveAPI
upgrade acceptance and development testing, subject to remaining gates. This is
not a clean-browser claim; exact CSS cause remains unproven. All operations
reconciled and roots retained; no active C runner.
See browser-full-rooted-failures.md, browser-full-rooted-reconciliation.json
and nix-retained-restoration-receipt.json. No app/Git/cluster/publication changes.


Latest execution is the current f10 parent-monitored release below. Earlier
757 execution and its failed result remain preserved as historical evidence.

## Historical initial 757 execution

Explicit lead release after reviewer0 final all-lanes acceptance and B3 consumer
performance reconciliation. C holds the exclusive session utility slot until
batches1->2->3 are finished/reconciled or an escalation is handed back. No other
session verification batch starts meanwhile. No code/Git/source guard changes,
PR update/publication, integration/deployment or lifecycle operation authorized.

Exact test identity: HEAD757f7fd8c2d5d3a4d1f6ee464acd29a5a2502176,
tree0aa1152064b123562dceb311fc56efa50fd7fc05; planned-input-identity.json
binds manifest/lock/flake/provenance hashes. Rechecked exact session/env, clean
worktree/index, installed0.30.2 and all file hashes before batch1. No local env/
private config or provenance override exists. Logs/status/time from each fresh
pinned Luna/low utility stay beside this receipt. No automatic retries.

Batch1 running: normal npm ci:tests then normal production frontend build,
launched by fresh utility c0302_full_tests_build. Exact command in accepted plan
and batch1-watch-brief.md; full output batch1.log, status batch1.exit and elapsed
batch1.elapsed. No concurrent Nix prefetch/build or browser process launched.

Batch1 failed/reconciled exit1 in33.776s: 227/228scriptcases passed; stale
GET/rawdescription assertion failed. BFF/rootunits/build were not reached.
No Nix/browser batch launched. Lead assigned test-only correction; C released
utilityslot toA0 and has no owned liveprocess. Currenthead nowf10d3d48 after
bounded scriptassertion fix, fullreceipt inoptions-test-fix.md. Five targetedcases,
scopedlint/format passed inline; no batch1retry. Await lead directverification
and freshslot release. Plannedinputs updated to newhead/tree andscript hash;
prior fullhead/source evidence retained. No runtime/dependency/migrationchange.

## Current f10 parent-monitored release

Lead directly accepted the narrow test-only OPTIONS correction and then
explicitly released C batches1→2→3 under the monitor skill's visible parent
fallback, because A0 holds the single verification watcher. No extra watcher
or model substitute launched. Parent retains every operation handle and uses
bounded output/waits; full logs/status/time are written beside this receipt.

Exact head `f10d3d48c4f21cc39187c3667ffffd9952404c11`, tree
`e1084bb80dd07140719034ab908a6f62daff855b`, base
`5a2d2bdc3ad7a827038f877d75959916528db844`. All planned file hashes
matched before execution; tracked/index state clean, installed HaveAPI0.30.2.
C commands use CPU affinity60–63, nice5, NIX_BUILD_CORES2.

Batch1-resume PASS, exit0,317.854s: `nix develop -c bash -c
'npm run ci:tests && npm run build'`. Script228/228 and BFF57/57 passed;
Vitest303/303files and1899/1899cases passed (248.33s). Normal production
frontend build passed in23.01s; existing chunk-size warning only. Full log
`batch1-resume.log`, command/status/time in matching files; owned handle74647
completed. `normal-build-info.json` proves fullf10, dirty:false, source:git.
Original prior757 failure/log/exit remain intact; this rerun follows its assigned,
diagnosed and lead-accepted test-only correction.

Batch2 launched after a fresh clean-head/hash check and capacity inspection
(~53GiB available, load~15 across64CPUs). `batch2-preflight.json` and
`tested-flake.lock` preserve inputs. Parent handle11987 owns the accepted
frontend/BFF/provenance/source/package-contents batch with --max-jobs1/--cores2;
full log `batch2.log`. Current cleaned source, recursive derivations and actual
outputs are pending completion; old757 source remains historical only.
Batch3 has not launched. No source/Git, push/PR, deploy/merge or lifecycle action.

## Reconciled postreview results at f10

Batch2 PASS, exit0,96.127s. Ordinary Nix frontend, BFF, provenance,
source-contents and package-contents all built. Source15required files and
package370public assets passed. Both build-info receipts identify exactf10 and
dirty:false (source:environment). Six existing optional unresolved URL warnings
did not prevent the actual normal registry package build. No kernel build.
Full `final-nix-identity.json` binds outputs, derivations, source/output NAR
identities, fingerprint, both build-info files and all1796recursive derivations.
`tested-flake.lock` retains all11input nodes. Nix metadata normalizes node names;
its recursively expanded locked/original/flake/input graph equals the committed
lock exactly (canonical SHA256 recorded). JSON derivation output is version4;
a read-only extractor was corrected for that wrapper, without rerunning a build.

Current cleaned package source:
`/nix/store/5bswsak9xx2i15rwzvwii22r508wgb1j-source`
(NAR sha256-zu62gZ2IVqupFvRWzRip6gZ/v/f0+TpuOSMDe3rZycc=).
Flake source `/nix/store/q11zzv4i4b73ksl9dd1c9bbbn22pfjcz-source`.
Frontend `.drv`:
`/nix/store/yjkvw1mc6hwnajzfqbdm7l2xd81h24hg-vpsadmin-webui-frontend-1.0.0.drv`;
output `/nix/store/zmjxhvsch25qx37slbvi62d1xn3abvah-vpsadmin-webui-frontend-1.0.0`.
BFF `.drv`:
`/nix/store/45yi4fv5ffgr4qi4v9s9kg9q5qzl23ra-vpsadmin-webui-bff-0.1.0.drv`;
output `/nix/store/6ayfyxgx8rpgxayf0sz268jxic90297l-vpsadmin-webui-bff-0.1.0`.

Batch3 FAILED at environment setup, exit1,53.163s; no retry. The exact nine-file
selection produced62cases,31Chromium desktop and31mobile Chrome. Every case
failed at browserType.launch before any application assertion: NixOS stub-ld
cannot start the generic Linux cached Chromium headless-shell1228, browser
process exit127. `browser-results.json`, `batch3.log`, full command/status/time
and62error-context files preserve the evidence. Vite started successfully;
no live API/OAuth/member workflow ran. Browser workflows remain UNVERIFIED.
See `browser-runtime-blocker.md` for the narrow recovery referral.

All three parent operation handles74647/11987/85178 completed and were consumed.
Owned child PIDs are absent, local Vite has exited and52847has no listener.
A plain bind initially encountered TIME_WAIT; ss showed no listener and a
SO_REUSEADDR bind confirmed release, without killing anything. See
`postreview-reconciliation.json`. No watcher was launched; A0 continues to own
the sole session watcher slot. C has no active build/browser operation or held
verification capacity. Final preflight confirms clean exactf10/two commits,
all planned file hashes and retained review refs unchanged. No source/Git or
publication/deployment/lifecycle mutation during this verification.

Remaining gate: authorize/prepare a compatible local browser runtime, then run
only the same nine existing desktop/mobile fixtures with retained failed evidence.
No repeats of passing quick/unit/build/Nix checks are indicated for unchanged
inputs. No migration/schema/persisted/wire change or deployed consumer boundary.
Own branch publication and protected PR74 rewrite remain separately gated.

## Accepted same-browser FHS recovery execution

Lead accepted the concrete environment-only plan and released conditional setup,
version/hash probe, then the unchanged browser boundary. Standard buildFHSEnv
from locked nixpkgs5e2305d5 supplies the ELF runtime only; no app/fixture/Git,
host configuration, browser version or security policy/flag change. Original
62prelaunch contexts remain historical. Parent-monitor fallback and resource
caps retained while A0 owns the sole watcher.

FHS setup PASS exit0,17.762s; expected drv/output realized exactly. Version
probe PASS exit0,0.591s: Node24.21.0, Chromium149.0.7827.55/revision1228 and
ffmpeg1011. Original browser/ffmpeg hashes and all source/input hashes matched.
See final-fhs-identity.json, fhs-recursive-derivations.json (complete graph),
fhs-closure-nar-info.json and setup/probe logs/status/time. Fresh free-port and
capacity preflight passed; no unexpected kernel build.

Corrected batch3-fhs launched under parent handle62295, same nine files/two
projects/two workers/no retries. Separate browser-fhs-results.json and
browser-fhs-artifacts preserve original failed outputs. Browser launch now
succeeds and initial desktop app assertions pass; final outcome pending.

### FHS run result and confirmed GC interruption

Batch3-fhs exit1,195.975s:31/31desktop app cases passed;31mobile cases
failed at launch ENOENT before app assertions. No app assertion failed.
Read-only host journal confirms pressure GC began09:21:42UTC, deleted the
exact unrooted FHS drv/output/rootfs09:22:07UTC while the batch was active.
Seven of185closure paths disappeared. Cached browser bytes remain unchanged.
See fhs-gc-journal.log, fhs-postrun-missing-paths.json and
batch3-fhs-reconciliation.json. Parent handle62295completed; owned PID absent,
Vite exited,52847has no listener. No rerun/global GC/service/source action.

The proposed correction retains the same wrapper with a normal session-local
GC root, then repeats version/hash probes and only the unverified mobile cases.
Concrete plan browser-fhs-gc-correction-plan.md sent to lead before execution.
Desktop proof remains valid; overall browser acceptance remains incomplete.

## Current rooted-runtime verification and artifact retention

Lead accepted the GC correction. Same expression/drv/output restored with a
normal persistent registered fhs-gc-root (and duplicate output root named
fhs-drv-gc-root; the latter points to the output, not a derivation). Rooted
setup exit0,30.808s; version probe exit0,0.449s. Full185path closure restored.
Comparison caught one NAR discrepancy before browser tests: generated rootfs
size6219704→6219712 (+8bytes), oldsha256-oDvQ0O60i9Z1vZgjbofeoiAuIm9il+i/bXOw4sUDObc=
→newsha256-Faq97Z93sfvQBWCNJ/EX5jic/sqAG5EaMPXqyh3CjhQ=. All184other
closure paths/NARs/references and complete2122derivation JSON are identical.
Randomized builder/generated schema-cache explanation remains plausible, not
proven; no equivalence claim for that rootfs content. See
fhs-rooted-comparison-mismatch.json and restored rootfs inventory. The earlier
version probe ran after an assertion failure because a compound shell lacked
fail-fast sequencing; no app test followed. Subsequent gates use separate
sequenced operations and checked completion.

Lead directed a fresh BOTH-project62case run on the current actual rooted
closure instead of further static equivalence analysis. Historical31desktop
passes are not combined with a later mobile run. Preflight independently passed
clean exactf10/all source+lock+wrapper/browser hashes, all185current closure
NARs stable, root registration, capacity and freeport. Versions-only current
probe passed exit0,0.231s. The full browser run is active under parent80218,
original9files/2projects/2workers/0retries, separate browser-full-rooted outputs.
No extra watcher, source/Git/config/browser/security-policy or host-GC change.

Independent normal artifact restoration PASS, exit0,69.456s. All5original
package/check .drv/output paths restored exactly; frontend/BFF NAR hashes,
sizes/references match historical values, as do clean/flake source NARs.
Complete1796recursive package derivation JSON is byte-identical. Both packages
report exactf10,dirty:false. New check NARs captured at actual restored paths;
all5outputs plus clean and flake source have registered normal owned GC roots.
See nix-retained-restoration-receipt.json and matching logs/status/JSON.
Retain these roots for later verification/cluster preparation. No cluster action
or artifact deployment/use occurred. The earlier passing Nix proof remains
historical; these matching present rooted outputs now support preparation.

## Final actual rooted-run result and handoff

browser-full-rooted exit1,393.23s: desktop31/31passed, mobile29/31passed;
user/admin transaction-expansion click cases timed out at90s. See detailed
browser-full-rooted-failures.md and checksummed screenshot/video/trace/context
inventory. Full current62case result is retained without combining historical
runs. Current185path runtime closure NAR/hash/size/references is identical
before/after; root registration and cached binary/source/input hashes intact.

All owned native command handles consumed/PIDs absent,Vite/browser exited,
52847free. C execution capacity released to lead; Asolewatcher never changed.
Normal5outputs/sources are present, exact historical NARs matched and roots
registered; no missing artifact may be deployed. Retain roots for later prep;
no cluster operation. Exact cleanf10/tree/two commits/mapping/PR74plan unchanged.
No migration/schema/persisted/wire change, publication, source/Git/host/security
or lifecycle action. Browser gate remains open; no retry/repair authorized yet.

## Final architect/lead residual disposition

Architect reviewed the completed exact-base comparison; lead explicitly ACCEPTED
the two matching mobile expansion failures as a specific preexisting interaction
residual, nonblocking for the scoped HaveAPI upgrade and development testing
subject to remaining gates. Current actual result remains60/62
(desktop31/31,mobile29/31), not a clean browser pass. Exact CSS cause is unproven.

No UI/test/fixture/source fix, force click, additional run/current-archive
experiment or Git rewrite assigned. Exactf10, original failing/full/base evidence,
rooted runtime/package/source identities and retained roots remain unchanged.
Own-branch publication is prepared only; publication/PR74protected rewrite/
integration/deployment/cluster actions remain separate lead/user gates.

## Own branch published, protected alias unchanged

Lead released exactf10 ordinary own-branch publication. Fresh main fetch and
cleanhead/input/SSH/hook/remote boundaries passed; one-refspec NOFORCE push
exit0 in2.634s. Remote refs/heads/dev/vpsadmin-haveapi-upgrade independently
verified atf10d3d48c4f21cc39187c3667ffffd9952404c11. Main/HEAD5a2d2bdc and
PR74alias5dd2333b unchanged; old/localrefs/PR63/currentworktree untouched.
No PR/newPR/default/deployment/cluster/source/test/lifecycle action.
See publication/receipt.json and logs/preflight/exact-head CI observations.
Ordinary ownbranch push triggers no matching workflows; no exacthead
run/check/status exists. No manualdispatch substituted. PR74concrete plan now
reflects completed ownpublication; protected alias rewrite still awaits exact
published-history approval. Current60/62accepted residual and roots preserved.
