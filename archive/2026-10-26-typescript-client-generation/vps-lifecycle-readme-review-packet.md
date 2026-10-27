# Final VPS lifecycle README review

User explicitly requested coherent start-to-finish guides across Go/Rust/TS including VPS create/destroy/start/stop/restart, minimum creation inputs/server defaults plus optional CPU/memory/diskspace/IP configuration. Accepted plan/design is TOP lifecycle appendix in design.md. Read current plan/state, workspace/repository AGENTS, mandatory-change-review SKILL and general-review reference. GENERAL ONLY: substantive documentation changes, no runtime/auth/permissions/interface changes. Saved independent reviewer0 Sol/xhigh/read_only; no overrides/fallback/nested review.

Acceptance: complete read-only connect/list50 retained; choose location+compatibletemplate (reader-selectedIDs, never guessedrealIDs/firstrowautomatic); ONE minimal OR configured create, then returnedID check/completion prerequisite -> inspect/hostnameonlyrename -> independentpoweralternatives -> delete last. Member minimum hostname+location+os_template despite savedschema onlyhostname required. Server choosesowner=currentmember/node/pool, start=true, environmentresources/IPdefault1each/private0. Configuredcpu2(capacity),memory2048MiB,diskspace10240MiB,ipv4=1/ipv6=1allocationcounts (mayberoutedprefix, notliteralIP/fixedprefix). Limits/quota/locationIPv6 support. GracefulStop/Restart omitforce. MemberDelete is soft/scheduled/defersdiskdestruction; nolazy=false/adminoptions. No framework/polling, receiptisnotcompletion beforedependency. Idiomaticerrors/options/nullhandling/auth and existing URLs preserved.

All intended deliverables committed and clean, all38 exact finalfences compile withactualSDKs/noexecution/API. Lead completed directprosepass. Wholebranch1/1/3history review, obsoleteapproach/repeatedstream/migration explicit conclusions required. Prior finaldocumentation report is vps-client-readme-review.md and closure disposition; prior functional TS reviews remain authoritative for unchanged source. This is new final docs review, not early/advisory. No test/build/checkexecution/network/API/source/record mutations required; inspect committed docs/interfaces/source statically, return fullreport tolead.

## vpsadmin-go-client

Worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-26-typescript-client-generation/vpsadmin-go-client`. Fullrange `1d9240f3d27b5831baf3694baab5fe06294875d8..51b86a59dc378eab1d84249094e27c80bdaf4d08`; tree `909ab596fe3de686de98609da2dd7f9c1da3b961`. Old reviewed/published range `1d9240f3d27b5831baf3694baab5fe06294875d8..bb1bc9622fff5a95b9c922c5b419949235a0305f` retained unchanged.

```text
51b86a59dc378eab1d84249094e27c80bdaf4d08 Document the VPS lifecycle with the Go client
```

Owning documentation amendment diff `bb1bc9622fff5a95b9c922c5b419949235a0305f..51b86a59dc378eab1d84249094e27c80bdaf4d08` (ONLY README):

```text
README.md | 197 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++---
 1 file changed, 189 insertions(+), 8 deletions(-)
```

Base-to-head owned documentation paths: README.md.

## vpsadmin-rust-client

Worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-26-typescript-client-generation/vpsadmin-rust-client`. Fullrange `ff876abe17e3301da62c1b6afbda055ec89db9d2..020f4ddb229d7892c76cf10e89ee7a792fddf9ad`; tree `d5b37e0338f6be05717da663d57fd5b3e7ed1531`. Old reviewed/published range `ff876abe17e3301da62c1b6afbda055ec89db9d2..2aad8d47c68d53ce1cb7e8669e083f96dc868a8c` retained unchanged.

```text
020f4ddb229d7892c76cf10e89ee7a792fddf9ad docs: guide the VPS lifecycle in README
```

Owning documentation amendment diff `2aad8d47c68d53ce1cb7e8669e083f96dc868a8c..020f4ddb229d7892c76cf10e89ee7a792fddf9ad` (ONLY README):

```text
README.md | 131 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++----
 1 file changed, 123 insertions(+), 8 deletions(-)
```

Base-to-head owned documentation paths: README.md.

## vpsadmin-typescript-client

Worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-26-typescript-client-generation/vpsadmin-typescript-client`. Fullrange `6c67b3c6e10e4096f6717345026371a89691f62a..a8966789bd24914daebd9fc0e33a51f76480c4ba`; tree `71ed0c6a7481311d7d851161d7b99929b16a87ba`. Old reviewed/published range `6c67b3c6e10e4096f6717345026371a89691f62a..e116b3e87ce73386b64d8291cffa1f24bb38b718` retained unchanged.

```text
34fefcec9ea382a58a019b4acc9e400df4b9abda Generate the vpsAdmin TypeScript client for API 7.0
2dab582881c4af8d8b3f932d9f2308e133d8d925 Prepare validated npm archives and guarded trusted publication
a8966789bd24914daebd9fc0e33a51f76480c4ba Document the VPS lifecycle and SDK maintenance workflow
```

Owning documentation amendment diff `e116b3e87ce73386b64d8291cffa1f24bb38b718..a8966789bd24914daebd9fc0e33a51f76480c4ba` (ONLY README):

```text
README.md | 161 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++----
 1 file changed, 153 insertions(+), 8 deletions(-)
```

Base-to-head owned documentation paths: README.md and docs/development.md added in original docs milestone; all earlier two source/release commits unchanged.

## Verification and history disposition

All three branches retain their original parent/base and amend only the owning documentation commit; no fixups/obsolete update/pin stream. TS initial34fefcec and release2dab582 unchanged, docs/development.md byteidenticalto e116. All other tracked mode/blob/path entries unchanged (TS702outsideREADME). CompletepriorfunctionalTSreview retained; inventory full3series explicitly, no need repeat sourceaudit. No migrations/persisted/wire/API/schema/runtime change, no merged/released/deployed/externalstateboundary. All previousreviewedSHAs preserved as immutableevidence. No defaultintegration/release/registry/deploy/lifecycle approval.

Quick checks before review:
- Go14 exactfences compilePASS declarednix-shellGo1.26.8/localreplace/readonlymod/GOPROXYoff/-buildvcs=false(noexecution), within60s. README SHA32605cae076dbc671e7c1b66e3cab0bde8488df6c6c0bb9322fbdb3a51148145. /tmp/2026-10-26-typescript-client-generation-go-readme-check/compile-lifecycle.log and script; oldcompletequickstart/auth/errors/devbyteequal.
- Rust12 exactfences compilePASS offline locked cargo check, retainedtarget1.13s/deadcodewarnings only, within60s, fullasync/blockingread-onlyfencesunchanged. README SHAcaea173315c96943c71ae7da49e0d4eb729be43b41ba6a92ea44915768d60dbc. /tmp/2026-10-27-typescript-client-generation-rust-lifecycle-readme-consumer/{check.log,check.status,fence-proof.json,commit-receipt.json}.
- TS12 exactfences compilePASS once7.383s in60s bound, two minimal/configuredconsumerscoverallfencesverbatim, onlydocumentedselectedIDtypedcontexts. ActualpublicSDKdist/runtime0.30.2/TS6.0.3/Node24types, strictNodeNextES2022noEmit/exactOptional/noUnchecked/verbatim. README SHA53586f944ab49e9ce01ce50ddb11fef46b1628c2a6ca1d4b0f81a044c564f674; developmenta8405a20846b29b73eb58ff6f90b5739bf1d626e1b60ae2ed307e3145c08386dunchanged. /tmp/2026-10-26-typescript-client-generation-lifecycle-ts-proof.json pluscompile.log/status.
- Allstaticlinks/pathscope/whitespacepassed, noAPI/exampleexecution/install/build/archive/regeneration/fullsuite. OrdinarydeclaredNix/temp-Famends/hooks/no bypass (norepodeclaredhookframework).

No newfeaturesafety/pollingframeworkrequested. Existinginstructionsforbackgroundcompletionmustremainaccurate; noimplicitcompletion/rawTSwaitForCompletion. Reviewrequestedfinalguidecoherenceandactualcallsemantics/prose, no arbitraryhardeningexpansion. Futurefeaturepublication+exactCIisleadworkafterreview. Report findingsfirst,severity,evidence and explicit completehistory/repeatedstream/no-migrationsconclusions; no sourcewrites.
