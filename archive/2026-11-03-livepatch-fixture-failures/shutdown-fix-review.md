# Production shutdown correction: final committed independent review

## Findings and disposition

**No new Blocking, Important or Advisory findings.**

The correction at **645927e22809a29c67ffd59c072e553e05e2a72b** passes this affected committed review for proceeding to the separately controlled publication and single focused runtime acceptance described in the packet. This is not whole-head qualification, a historical VM root-cause conclusion, deployment approval or merge readiness. The unavailable whole-osctld unit suite, real packaged shutdown, temporary message directive and final exact-head CI remain explicit limits/gates below.

Complete reviewed range: **2951a632c4254a44747a8da326e3dde897eaa0e2..645927e22809a29c67ffd59c072e553e05e2a72b**. New substantive inspection: **e1751c917f216897292ab0b893727a6e5553a540..645927e22809a29c67ffd59c072e553e05e2a72b**, all four committed osctld files and necessary consumers. General, architecture/repetition, scope/proportionality and risk/compatibility lanes; overall risk **HIGH**, because production host shutdown, resource ownership, abort and recovery change.

## Scope and proportionality

The added production scope has explicit user approval, recorded as “Fix here as a separate commit (Recommended)” in response to call_7ccafe3d4e8749109837706d8a32a8c7. It is separate from the original normal-module livepatch qualification. Neither architect acceptance nor an internal plan is being used to infer that authorization.

The actual delta is **four files, +714/-53**, comprising **+143/-53 production code and 571 added spec lines**. It stays in Daemon and Self::Shutdown, with their existing spec files. No global Manipulable, pool import/export implementation, CLI, runit, runner, kernel, input/pin, public option or persisted format change accompanies it.

A daemon-local mutex/CV and one captured completion record are proportionate to the demonstrated stale-snapshot defect and required complete-operation semantics. Dropping a removed pool from a retry list cannot establish completion: actual Pool::Export removes its DB entry before SendReceive.deploy and its post-export hook. Serializing queued requests by rerunning each also permits a duplicate to reset an accepted abort. Joining the active outcome resolves those concrete cases without a scheduler or general framework. Tests exercise finite ownership, completion, error and abort boundaries.

Records identify delivered milestones: source interleaving reproduction, accepted design, final targeted controls, frozen four-file handoff and separate hooked commit. They do not establish a continuous comparable working-time clock, so I do not infer a stall or speed claim from elapsed session time.

## Correctness, architecture and current consumers

### Admission and complete outcome

- **osctld/lib/osctld/daemon.rb:91,254-319** initializes per-instance synchronization and admits one active owner under its guard before executing the command body. Resource work runs outside the guard. A joiner retains the particular operation record and waits in a predicate loop; a later operation cannot replace its result/error.
- **osctld/lib/osctld/commands/self/shutdown.rb:7-24** places admission before the first pool snapshot, rather than only around export or confirmation.
- Success is published only after the owner block returns, including every call_cmd! export and the command's ensure cleanup. **Pool::Export:151-159** establishes the relevant ordering: DB removal, SendReceive.deploy, post_export, then return. Absence from DB cannot produce premature joined success.
- Owner exception and confirmation failure are published to joiners. Admission/broadcast survives ordinary exceptions and interruption; incomplete nonlocal exits cannot be published as successful completion. The next explicit request may start after the prior record is done.

### Abort, markers and restart

- **daemon.rb:292-309,325-371** coordinates abort, confirmation and publication through the same short guard. Resource wait/export work does not hold that mutex, so independent abort remains available.
- Joining does not invoke begin_shutdown or clear the abort flag. Abort accepted during the active operation prevents confirmation and final publication removes a marker that the unchanged CLI may recreate before submitting a duplicate. A later request after completion is deliberately fresh.
- Ordering is explicit: abort obtaining the guard during the operation prevents success; abort obtaining it after completed confirmation removes the marker without retroactively changing the captured outcome.
- Ordinary failure leaves pending restart intent. No rollback of already stopped/exported resources is newly promised.

I traced current consumers by repository search: Daemon#setup serves clients before import and may resume Self::Shutdown after import (**daemon.rb:154-174**); command clients use the same Self::Shutdown entry; Self::AbortShutdown calls the independent abort method; indirect Pool::Export reads the abort state; osctl shutdown writes its pre-request marker and retains existing protocol/fallback handling (**osctl/lib/osctl/cli/self.rb:79-137**); halt and runit stage3 still invoke ordinary osctl shutdown.

No production caller of begin_shutdown/confirm_shutdown bypasses the new command admission. Joined clients can receive zero intermediate updates, which the existing Generic::ClientHandler protocol permits. Wall/message options are used by the admitted owner; duplicates join that operation.

### Resource lifetime and errors

- **shutdown.rb:13-15,79-92,95-163** keeps acquisition lists from the first successful hold, masks interruption across acquisition-plus-recording, and cleans up before publishing the outcome.
- Cleanup visits containers then pools in reverse acquisition order and checks holder identity. Already released or differently owned objects are skipped; there is no foreign-thread unlock or global lock rewrite.
- Actual Manipulable permits same-thread nested export without changing/releasing the outer hold. The new ensure releases that hold when the shutdown operation ends, even if its setup/client thread stays alive.
- Cleanup attempts all recorded resources/lists and preserves the initiating error if cleanup also fails. A cleanup-only failure prevents successful confirmation. Interrupted owners reach cleanup/publication rather than stranding joiners.
- The guard owns admission/marker state, not manipulation locks or export/hook work. I found no newly introduced reverse resource/guard dependency in the inspected consumers.

The completion record belongs in Daemon; cleanup belongs in the shutdown command that acquires the resources. No new mirrored policy, speculative extension point or repeated production rule needs another abstraction. The small duplicated marker-privilege test wrappers do not justify shared test machinery.

## Verification evidence and adequacy of the unit gap

I inspected the tests and raw receipts without rerunning a suite:

- **heavy_system_spec.rb:192-539** uses a fixture pool with real Manipulable, real DB::List snapshots/removal, Base dispatch and actual nested Pool::Export. External pool work, empty ancillary registries and external hook/deploy effects are isolated; queue barriers control interleavings.
- Controls cover setup/client owner order both ways and duplicate clients; admission before snapshots; no joined completion through post-removal deploy/post_export tails; shared tail failures; import-wait/partial-acquisition abort; late duplicate after abort; recreated CLI marker; final-tail abort; cleanup with a still-live owner thread; partial pool/container acquisition errors; released/foreign-held containers; original versus cleanup-only errors.
- **daemon_spec.rb:34-245** covers marker modes/restart inputs, marker creation/confirmation errors, captured success/failure across a later operation, completion/abort guard ordering, original Interrupt publication and incomplete nonlocal exit. Unchanged manipulable controls exercise same-thread re-entry and second-thread exclusion.
- Final declared three-file invocation: **45 examples / 0 failures**, seed11860, 1.4s RSpec / 2.831s total. This ran against the frozen four source hashes subsequently committed as645927; I independently compared working files and committed blobs with all four hashes. It is not a separate postcommit suite execution.
- Recreated-marker focus: **1/1**. Declared root RuboCop1.75.8: **four files / no offenses**. Normal Nixfmt/RuboCop/commit-message hooks passed in package-a-shutdown-commit-hooks.log; no bypass. My read-only complete-range whitespace check passed.

The target uses the osctld Gemfile, patched Ruby3.4.11, locked NETLINK/RUBYLXC source bindings and recorded local native extension. I verified the local development lock SHA **3169e57f8aae4f66ed5c291140feb74ab724577b2d4b6872f375fedb535e9820**. This is ignored development state, not a committed package lock; it must not be described as a tracked old/new Git blob.

The broader all-osctld invocation is **unavailable before examples**, not green. After the recorded native LXC correction, stderr identifies repository_spec -> existing repository.rb require of filelock. The one matching-provider load-only dry-run advances to utmp_reader_spec -> existing utmp_reader.rb require of bindata. RSpec's absent did_you_mean diagnostic is secondary. The requires, gemspec dependencies and Gemfile are unchanged from e175; I checked them directly. No assertion result follows from either failed load.

**Gap assessment:** targeted coverage is adequate for this pre-runtime committed review and the next focused VM acceptance. It exercises changed synchronization/ownership and actual export-tail ordering directly. More cache/provider repair before that check would expand the work without replacing missing packaged/guest proof. The whole suite remains unverified, including suite-wide fixture interactions; neither45 examples nor a load-only attempt establishes it. Real Pool/container effects, daemon startup, wire clients and graceful host shutdown still require runtime verification. Those gates are not waived.

I read A's actual645927 ten-field IFD-disabled identity receipt and independently compared its JSON with the retained2951 receipt: exact equality. This supports only unchanged module/sites/resolver/boot/SDK/compiler/config artifact scope. Module/sites hashes remain **7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f** / **093cf255a38db5275b62370da8bac1297781e48e2ae3245c1c5b5e1ceeb23ed1**. It does not qualify changed packaged osctld or the guest closure. Prior D81/207 and A99 host checks retain only their unchanged loaded source/bundle/native input scope; I did not rerun or relabel them.

## Compatibility, safety and documentation

No public command name, request/response field, CLI option, marker pathname, on-disk format or migration changes. Pending/confirmed marker convention and process-restart resume remain. Older clients retain final success/error semantics; zero progress updates for joiners fit the protocol. The in-memory gate is per daemon and disappears on restart. No coordinated fleet update is required.

Abort still permits partly disabled/stopped/exported pools, without restoring prior resource state. Existing **osctl/man/man8/osctl.8.md:3242-3273** explains this and manual export/import recovery. Code rollback can read the same marker/state but restores the old race risk. Restarting/upgrading a live daemon during active shutdown is not proposed or authorized as recovery.

Near-owner comments explain captured outcomes, masked admission/publication, command-owned hold lifetime and recreated-marker handling. Together with contract tests they adequately document this bounded internal change. Existing user-facing messages and man-page behavior remain applicable. Individual incident evidence, CI sequence and temporary age choices correctly remain in session records.

Historical e175 incident remains unclassified beyond its observed phase: ct-passwd body passed, stage3 waited on self_shutdown pool holds, the900s stop deadline expired, and cleanup TERM supplied QEMU exit. The constructed unit interleaving proves a source defect, not that VM's actual holder/restart/export history. No historical shutdown pass, flakiness/resource attribution or claim that this correction necessarily explains the incident follows.

## Complete history, consolidation and migrations

I independently reconstructed the parent chain and whole-range inventory:

1. **8169b8189c29f471b2ecf27a33b6f71dbde5e70e**, parent2951: tests/livepatch: qualify current module probe sites.
2. **e1751c917f216897292ab0b893727a6e5553a540**, parent8169: osvm: record bounded host evidence for boot failures.
3. **645927e22809a29c67ffd59c072e553e05e2a72b**, parente175: osctld: coalesce concurrent shutdown requests.

Range: **three commits, 24 paths, +3637/-237**. Merge base is assigned2951. Both reviewed prefix objects remain ancestors with unchanged raw messages; all **twenty** prefix feature file modes/blobs are identical at645927. Only the four assigned osctld files change. This supports reuse of packaged-dependency-refresh-review.md and the previous OSVM/source-identity/full-source/retention/R1/R2/DS1 reports and reconciliations for the unaffected prefix.

Independent ordered patch IDs:
- 8169: **317857127604b13d7f79a3d294ee39efe97b3379**
- e175: **35e735aa81029cac8e6e960ff15a8a94a2ef0cc7**
- 645927: **19c6fb29f4087b55e2c9aea927a7c115febad579**

The three purposes are independently meaningful and reviewable. Production shutdown fixes an existing baseline defect rather than a caused livepatch repair; the user explicitly requested a separate commit. Observational OSVM logging remains a separate verification dependency. **No obsolete implementation, intentional-red source prototype, fixup/WIP, discarded approach or transitional compatibility path remains in the committed series.**

**No repeated dependency/channel/input/pin/generated-artifact update streams exist in the feature series.** The paired rake-compiler packaged update remains canonical baseline2951, not another feature update. No redundant intermediate update needs retention or consolidation. Seven dated provenance refs remain outside the delivery series and do not justify shipping superseded history.

**No migrations.** No schema/database/on-disk/protocol transition or unapplied intermediate migration is present. No migration was merged, released, deployed or externally consumed. The new shutdown correction has not been deployed or merged; this review makes no production deployment claim for the branch.

HEAD/index/tracked/nonignored-untracked state was clean. Message lines are within80 characters. Source identity/profile inputs outside the four-file delta are unchanged.

One deliberate delivery limitation remains: the third message contains isolated **[skip ci]**. It is not obsolete implementation history, but **must not enter staging**. Current645927 is the controlled focused-test head, not final normal-CI/integration message state. After focused acceptance, retain its tested/reviewed ref, remove only the directive through the authorized message-only path, prove tree/patch/prefix equivalence and use the resulting final SHA for full qualification. This review does not satisfy that outstanding condition.

## Remaining runtime gates and completion

The existing workflow excludes sites capture/lifecycle for nonempty test_pattern (**ci.yml:153,396**) and appends one quoted native selector (**ci.yml:333-338**). Planned ci/tagci/osctl/ct-passwd/prebuild/stop-on-failure dispatch is a focused native check, not native-plus-nine qualification. Verify actual selected head/inputs. Require body completion, real graceful stage3 and QEMU exit before the existing timeout, without cleanup TERM creating apparent success. Inspect a failure; no blind retry or timeout increase is justified.

The committed qualification profile remains **14400s**, byte-identical to e175, SHA **367dd4ce864b36c4807cb974857d7b58e22b18bb51343ad2724757132da12f2f**. The saved300s diagnostic patch is absent. Focused ct-passwd has no aging; any shortened later diagnostic is not four-hour acceptance.

After focused acceptance and skip-directive removal, **full exact-FINAL-head native plus all nine lifecycle rows**, module/sites/boot identity, semantic witnesses, health and recovery proof remain required. Earlier green rows, old-image passes, identity equality and this review cannot qualify new production package/guest inputs. Earlier boot/shutdown failures are not erased or waived; old cgv1 boot cause remains unclassified. Conditional merge permission remains unsatisfied until required accepted verification and ordinary final integration checks complete.

Identity reverified: dev-session current prints the exact bound slug; both environment markers absent; trusted thread-bound developer instruction names this workspace/session/reviewer. Live roster confirms reviewer0/thread01a1a24e-920c-7b82-9fff-7754d1f947ab, review-purpose ready, retained **gpt-6.1-sol/xhigh/read_only**, no override/fallback. Current mandatory-change-review skill and all four full lane references, workspace routing and applicable sessions/documentation/verification/Git/package-workflow guidance including2b5944e8, repository AGENTS and patch-series policy were read.

Read-only source/history/receipt inspection and bounded Git/hash checks only: no source/session write, suite/eval/build/VM/network/CI operation, Git mutation, nested reviewer, service or lifecycle action.

**Review package complete.** Root saves this report as shutdown-fix-review.md and owns reconciliation and separately released publication/CI. No source fix requested. Session remains open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/
