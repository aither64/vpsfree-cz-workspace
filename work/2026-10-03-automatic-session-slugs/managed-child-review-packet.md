# Related managed naming-child verification review

Review committed runtime d161e98ad034bc00f1f8c54879508acec6ba2232 after
compile-only quick verification. All four High-risk lanes apply: general,
architecture/repetition, scope/proportionality, risk/compatibility. Same retained
independent reviewer0, saved gpt-6.1-sol/xhigh/read_only; no override or fallback.
This is related verification review, not final package/branch readiness.

## Outcome and frozen scope

User requested automatic initial-prompt naming with optional custom slug and
explicitly kept model naming, file/network tools disabled and immediate question
rejection. The fixed gpt-5.5/low/full-catalog helper and portal-owned standard
child were reviewed at c8a9/1219. Report static-profile-review.md found no
Blocking/Important. The one Advisory reference correction amended provider to
1be5ba65da7d2e2876804cb809b1fe398bdd50a7; its code/test trees are equivalent.

New runtime source: ONLY portal/cmd/workspace-portal/naming_runtime_integration_test.go,
tag naming_runtime_integration. SHA-256 23666283f927707e23f778fe4223b6c52d325b63bd62f10d832a47562d49edfe.
Prepared initiative artifact: work/<slug>/managed-child-smoke.nix, SHA-256
fd69c7fa6f509d3c2088ff4672b9ee7da7a6e2d6713bb22db3ea12e3a4baaa49. Read its exact frozen contents and full
managed-child-smoke-brief.md, design.md managed-child supplement and
managed-child-report.md. The wrapper is a per-initiative prepared VM recipe,
not an exported product module/check or a generic test framework. Coordination
records follow normal daily/handoff cadence; before actual VM execution its
exact reviewed artifact must be retained in the consolidated checkpoint/store.

The tagged fixture has five managed cases plus owning-function HTTP failure:
one native child/two simultaneous POSTs plus third completion, missing home,
captured child loss, user-unit MainPID TERM, MainPID KILL/cgroup cleanup; owned
listener closure through actual production factory/web.New/servePortalHTTP.
No SessionNamer/fake AppServer positive, product test flag, ptrace, registration
receipt fabrication, host unit/slice or live credentials. CLI stubs prevent real
session initialization. Real candidate/team resources, private profile/lock/state,
real ordinary native plus observed UDS proxy, original full catalog and synthetic
builtin OpenAI HTTP fallback. Review process UID/PID/start-time/group/cgroup
ownership, cleanup on partial setup/failure, observation synchronization,
finite bounds and whether each assertion can prove its stated result.

VM runs a real UID1000 user manager. A UID-scoped inet firewall is installed
before developer native processes, blocks/counts a reserved canary, allows other
loopback, denies remaining IPv4/IPv6. Completed owned negative DialContext
control precedes one fixed baseline; no reset or unrelated packet attribution.
This avoids the known host-user-unit network-namespace inheritance gap. Only
recorded fixture units/groups are faulted/stopped; failure remains failure after
emergency cleanup. Leave canonical adjacent registration.json absent per current
web.New path contract. Actual GET form provides date/team/digest; no invented
preparations. No source binary/version/hash or required VM prerequisite skips.

The VM recipe requires explicit runtimeSource/packageRoot/fixtureBinary/manifestFile
immutable inputs. Manifest/source/package hashes are trusted coordinator
provenance, not arbitrary-builder attestation. Exact future package/fixture and
manifest do not exist yet. Do not interpret the old assembled package or current
compile-only binary as final candidate proof. The HTTP-failure test covers
production-function native integration, not externally faulted packaged CLI HTTP.
Positive slot observation is paired with existing owning semaphore unit test.

## Commits, consumers, compatibility

Current complete committed inventory/diffs: branch-inventory.md and linked
final/incoming artifacts; managed-child-fixture.diff is only the new unit.
Heads: provider1be5ba65da7d2e2876804cb809b1fe398bdd50a7 from base4c170393;
runtime d161e98ad034bc00f1f8c54879508acec6ba2232 from base924c0ec;
extension2e3733ad from base8f8d8ec; workspace725db671 from current mastera51fa51e.
Exact full bases and lists are in the inventory. New test unit is independently
reviewable/revertible explicit release verification; it changes no production
behavior and is never selected by normal tests. Owning child/helper production
support stays in one utility unit, mechanical pins remain separate. Preserved
consumed runtime4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4 and extension399c33023a568a8d7a21e4e4df52829628720a28;
no migrations or schema/policy/receipt/journal/host/cluster change. Assess complete
history disposition explicitly without a final-readiness claim.

Current runtime committed provider pin remains oldd371; new API validation uses
ONE explicit temporary task-local modfile replacement. No silent committed
replace, package-source stand-in or build-ready claim. Publication/pins/vendorHash,
complete exact candidate package/CI/resources and deployment remain pending.
Production docs were reconciled in static-profile review; this verification
addition needs no public behavior change. Its concrete inputs/cases/commands and
limitations belong in session artifacts, per dev-session-documentation placement.

## Quick evidence and strict remaining gates

Parent owning cached Nix profile/Go1.26.7, TMPDIR=/tmp/GOWORK=off,
-mod=readonly -modfile=/tmp/automatic-session-slugs-static-profile-runtime.mod,
-tags=naming_runtime_integration -c ./cmd/workspace-portal passed; no tests ran.
Nix --parse wrapper passed. Log /tmp/automatic-session-slugs-managed-fixture-compile.log.
Prior provider95/pure99/runtime26 focused source cases remain qualified at their
recorded code-equivalent revisions; normal behavior was not modified by this unit.

One new provider-native run at1be5ba65 failed once22s: catalog-precedence/dynamic
negative passed,38 phase records stable2->2/no unavailable, no tool mismatch,
then unexplained shell/memory equality failures and28 SQLite log marker diagnostics.
See static-profile-native-observation.md. Architect proposed a bounded quiescent
persistence baseline; implementer0 is NOW editing only provider native fixture
under separate task01a10515-e795-78a1-bd19-8246d298675b. DO NOT review that dirty
future provider fixture in this assignment; use committed1be for helper context.
It needs its own committed quick verification/affected review before a native run.

Required logging choice remains unanswered. No SQLite/marker/seed/tool/counter
waiver. Actual managed/native execution and unchanged real-provider valid MODEL
within ten seconds remain unexecuted gates. No deployment, default merge,
archive/delete/stop or lifecycle completion authorized by review.

## Review instructions

Read mandatory-change-review skill and all four references, applicable workspace
routes/repository AGENTS and documentation guidance. Inspect this committed test,
prepared frozen VM recipe, exact production counterparts and native source only
as needed. Trusted local operator boundary applies; don't add compromised-local-
operator defenses. Return severity-ordered lane/file/commit findings, exact proof
limits and history/migration conclusion. Do not run tests/VM/native/model/network,
edit docs/code/records, modify refs/pins, diagnose unrelated delta, delegate or
activate. Report through report_to_lead/final; parent saves report. Same session URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-automatic-session-slugs/
