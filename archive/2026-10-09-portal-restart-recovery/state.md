---
lifecycle: complete
---

# 2026-10-09-portal-restart-recovery

## Status

Current phase: complete; all four repositories merged and pushed, with post-merge
CI and temporary integration-worktree cleanup passed.
The duplicate-artifact
follow-up is implemented, reviewed, checked and deployed on aitherdev without
reboot. The affected session page, retained conversation and repeated artifact
download all return HTTP 200. Both declarations remain in the unchanged manifest;
the catalog shows one link using the first label. No blockers or remaining
implementation/deployment work.

All user services are enabled/active, lingering is on, healthz passes and HTTPS
requires authentication. Host boot ID, native Codex PID and tmux PID are unchanged.
Selected profile is /nix/store/s2zxa731kh87li7syxi3qzjzw3wcp9zd-dev-workspace-0.2.0.

Current final heads: runtime a756b2c6, provider c9878454, composition be09a886,
configuration 6e4947b5 (patch-equivalent integration rebase; deployed configuration
remains 875420e0). Every exact final feature head is contained in its remote
master; retained feature refs still match those heads. Workspace master has since
advanced to 1025d8c3, a verified descendant of be09a886. No work remains; the
session stays open for follow-up. Current review:
[duplicate-artifacts-review.md](duplicate-artifacts-review.md).
Executed rollout: [duplicate-artifacts-rollout.md](duplicate-artifacts-rollout.md).
Original review and executed rollout remain in [review.md](review.md) and
[rollout.md](rollout.md).

Dedicated shell-only initiative created for this
conversation, with no native lead/team roster; main agent owns design and code.
Independent review uses the installed default review-role fallback. Long
verification uses the installed utility watcher. Shared master and unrelated
working-tree/index changes are preserved.

## Phase checklist

- [x] Investigate current portal/runtime and native queue/goal behavior.
- [x] Confirm automatic restoration and explicit activation preferences.
- [x] Create initiative and record initial plan/design.
- [x] Implement recovery and cold activation.
- [x] Pass quick checks and commit complete deliverable.
- [x] Independent whole-branch review and remediation.
- [x] Longer native/runtime/Nix verification and CI.
- [x] Deploy configuration and application without host reboot.
- [x] Follow-up duplicate handling implementation and quick checks.
- [x] Follow-up independent whole-branch review.
- [x] Follow-up packaged/browser/configuration/CI checks.
- [x] Follow-up no-reboot deployment and unchanged-manifest verification.
- [x] Ready for use and explicit merge approval received.
- [x] Approved fast-forward integration and exact remote proofs.
- [x] Post-merge CI and temporary integration-worktree cleanup.

## Next actions

No remaining action or blocker. Preserve the forward package, retained branches
and original initiative worktrees. The completed session remains open; no
archive/delete, session stop or aitherdev reboot is authorized.

## Documentation

Technical and verification brief: [design.md](design.md).
Approved scope and compatibility: [plan.md](plan.md).
Original deployment evidence: [rollout.md](rollout.md). Follow-up deployment
preparation/evidence: [duplicate-artifacts-rollout.md](duplicate-artifacts-rollout.md).

## Repositories

Expected: dev-workspace, codex-web, workspace, vpsfree-cz-configuration.
All use branch 2026-10-09-portal-restart-recovery and corresponding worktrees.

Current final published heads:

- dev-workspace: a756b2c6a3ec30efaf5fd25dccf1717c21a8efa8.
- codex-web: c9878454f07da244c103b8a79340b92b6d5bf052.
- workspace: be09a8866026fe1464814a50dd693e96e3d8ca80.
- vpsfree-cz-configuration: 6e4947b52abe103c582bfab2d0b37a8f17a7c02d.

## Commands run

`dev-session current` found no owned initiative and no environment binding.
Created `dev-session start portal-restart-recovery --no-codex --no-attach --json`.
Verified newly created literal environment identity through `current`.
`team list --as-is` confirms no native lead thread; no roster is invented.
Fetched workspace origin; shared master and origin/master were identical.

## Original recovery branches and verification history

The original rollout used the following published heads, superseded by the
follow-up heads listed above where changed:

- codex-web: c9878454f07da244c103b8a79340b92b6d5bf052, base 7dab76305dc0084735095d6dbdaef607585d9bca.
- dev-workspace: 97ea4c56f4984c5d8e574735e09a205c6a648f59, base 66262519d497073d9bb0dccc2252cdec4528f389.
- workspace: 4f4060ab3425c8eecc4614c261f28ee359b611e0, rebased onto shared master b73995877adf9e70ad36eef68df06e514c9f6faf.
- configuration: f715299ccd019a3f282dfbd969231223f3479e3b, base 1f3569902a4a6b02633019cd172eade5afe90005.

Workspace/configuration select the final 97ea4c56 runtime and the deployment
contract passes. Each update stream remains one functional/generated commit.

Quick checks passed: Go compile for all portal packages; focused recovery,
queue retry, exact activation, cold goal and stopped-session checks; shipped
browser API contract; Ruby cold resume (30 assertions) and package rollback
policy (6 assertions); JavaScript/Ruby syntax; protocol request coverage;
deployment pin contract; diff whitespace. Tooling came from repository Nix
inputs; focused Go used CGO_ENABLED=0 because the ambient shell lacks gcc.
Packaged verification will use the normal Nix toolchain. Nixfmt finds an existing
flake.nix formatting baseline failure (confirmed on the original base too);
only its same-width revision URL changed. Configuration hooks were installed,
signed and passed on the generated pin commit.

The first published library revision missed one activation corpus entry.
Local coverage and CI 37989847634 identified the same count mismatch. The fix
was folded into the library commit; runtime pins and checksums were consolidated.
No superseded update commits remain. Cancellation of superseded runtime CI
37990061537 was attempted and denied HTTP 403 by the GitHub token. Final-head
verification will not rely on that run.

No database migrations. Before this rollout, new private schema-1 recovery
records and the existing schema-3 submission-ledger path import were not deployed,
released or merged. They are now deployed only at the final runtime revision;
no intermediate revision was consumed.
Existing manifest, lifecycle journal, roster and native rollout schemas remain.
Ledger import supports the deployed socket-adjacent path; older writers must
be excluded and package policy prevents normal rollback once durable state exists.

Review: high risk (persistent state, protocol, host lifecycle and rollback).
All four lanes apply. No native roster exists, so fallback uses installed default
lead_reviewed/reviewer, gpt-6-astra/xhigh, read-only fresh context, catalog digest
437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd.
Packet: [review-packet.md](review-packet.md).

Remediation quick checks pass: implicit normal/observer watch reconnect holds;
known queue and delegated-send proofs, unchanged strict retirement proof;
CLI assignment through observation/lifecycle without browser acknowledgement;
Continue decision retirement and later stop/socket cycles; held deletion
completion; helper exit-75 retry classification; finished-creation visibility;
Ruby cold resume including temporary transport failure (44 assertions).

Runtime CI 37990197018 failed only TestCreatingAuthorityNeverGrantsControls
because unfinished creation exposed the composer. The readiness predicate fixes
both cases locally. Full failure evidence is retained transiently in
ci-runtime-initial.log. Final library CI 37990102747 passed its then-current head.

The VM boot check installs actual private user-profile units and verifies user
lingering, unit dependencies and socket startup before and after a disposable VM
reboot. It is assigned to the existing host CI lane. Imported action refs were
checked against official latest releases and remain unchanged:
[checkout v7.0.1](https://github.com/actions/checkout/releases/tag/v7.0.1),
[install-nix-action v31.11.1](https://github.com/cachix/install-nix-action/releases/tag/v31.11.1).

The all-lane rerun resolved six initial findings and confirmed coherent complete
history, consolidated pin streams and no database/transitional migrations. It
identified an additional Blocking hot-to-cold retry receipt bypass and remaining
Important transport classification gaps. Both requested narrow fixes are now
verified directly: accepted/submitting sends cannot reserve another queue entry;
portal and team retries reconcile prior receipts before loading; loaded discovery,
materialization and final identity rechecks preserve temporary transport errors.
Focused tests cover accepted/unknown outcomes and six proof boundaries versus
native refusals. Canonical Ruby cold recovery still passes 3 runs/44 assertions.
No new API/design beyond the assessed contracts requires another lane rerun.

Library final CI 37994414751 passed at e2d08464. Runtime CI 37992708941 passed
its previous reviewed b313879b head (host lane skipped); current-head runtime
CI 37994541207 is pending. Nixfmt's workspace flake baseline also fails at its
unchanged base; revision substitutions preserve its existing layout. Final
deployment pin contract passes at runtime 423ded60.

First long native run stopped before exercising recovery: the fixture supplied
a bootstrap marker without its thread ID, and lacked the required project
origin. The fixture now creates exact private projects and includes/verifies
the original marker across restart. This is a narrow fixture correction, with
no runtime contract change. No later batch check ran after that failure.

The second native run found the fixture's five-second unload wait was shorter
than native's default 60-second delay. Its private config now sets delay zero;
operator configuration remains unchanged. Native test c9878454 passed in 14.14s
with exact bootstrap history proof, surviving normal/observer watches, dormant
queues/goal, explicit activation/FIFO and held member isolation. Logs remain
transient under /tmp. Package/browser/VM/configuration checks have not run yet.

Final validated fixture pins are consolidated, with library CI 37995107833
passed and runtime CI 37995206264 at 3ab62594 in progress. Superseded runtime
37994541207 cancellation was attempted and refused with GitHub HTTP 403; it
will not serve as final evidence. Configuration's sole generated update remains
66262519 -> 3ab62594, with hooks passing and no superseded pin commits. Final
deployment pin contract passes. Longer packaged/VM/browser/build batch now runs
under a fresh Luna/low utility.

The existing host idempotency/activation VM completed its script successfully
in 208s. The watcher's first milestone report overstated all three check
conclusions: Nix still owns the first package/VM batch; the composed package has
not started. Package and new boot-test conclusions remain pending. No unexpected
local kernel build was observed. Aitherdev remains running.

The first packaged batch then failed in the new boot fixture before registration:
its workspace omitted the required repos/work/worktrees directories. The fixture
now creates the complete layout; Nix parse, formatting and diff checks pass. This
is a direct fixture setup correction, with no application or supported boundary
change; main inspected it under the narrow-fix review rule. Pins are consolidated
and the deployment contract passes at d4d39bf4. The old 3ab62594 runtime CI
37995206264 and superseded 423ded60 CI 37994541207 both completed successfully;
no stale run still needs cancellation. A fresh utility owns the remaining batch
and current d4d39bf4 CI 37996689493. Nothing has been deployed yet.

The d4d39bf4 batch passed packaged Go and all Ruby checks, then failed when the
private VM tried to retain the Codex GC root. The shared store made the package
visible, but the VM Nix database did not register its closure, so nix-store tried
an unavailable external substituter. Pinned NixOS qemu-vm source confirms
virtualisation.additionalPaths registers closures on boot. The fixture now adds
devWorkspace there while still installing the application from the user profile.
Nix parse/format checks pass. A fresh utility runs this corrected fixture against
the already-built d4d39bf4 application; final source is ad7d341e. This setup-only
fix leaves application code/contracts unchanged. CI 37996689493 passed; final
ad7d341e CI 37998220703 is in progress. Shared master advanced separately to
b7399587 with unrelated tracking only; reconcile the workspace feature after the
fixture check, preserving all unrelated changes.

The focused ad7d341e fixture confirmed the closure fix and protocol compatibility,
then activation refused the test's hand-made direct profile symlink. The supported
profile contract requires a Nix generation link. The fixture now installs its
already-built package with nix-env --profile --set. Syntax/formatting pass; a
fresh utility verifies fixture 1837a658 against the same d4d39bf4 application.
All changes since d4d39bf4 are confined to this VM setup. No application code,
public interface, deployment or package-transition policy changed.

Fixture 1837a658 passed first-boot registration and every unit/socket check,
then the driver's reboot shut down QEMU because machine.start defaults to
allow_reboot=False. The pinned driver implementation explicitly requires True
for reconnecting after reboot. Fixture 97ea4c56 enables that private-VM flag and
waits for both sockets, avoiding active-unit/readiness races. Formatting/parse
checks pass; a fresh utility verifies it against the unchanged built application.
These are bounded fixture corrections under the narrow-fix review rule.
Cancellation of superseded ad7d341e CI 37998220703 was attempted and denied
HTTP 403. Its result will not substitute for final-head CI evidence.

The final pins are published at the heads above. Configuration hooks pass and
its generated changelog describes only 66262519 -> 97ea4c56. Workspace rebased
cleanly onto b7399587; range-diff proves its reviewed functional patch unchanged
before the final revision substitution. The new shared commit contains only
unrelated tracking. No repeated pins or new migration lineage were introduced.
Composition evaluation confirms the unchanged live native Codex package
a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0; no native restart is needed.
Final runtime CI is 37999200234. Cancellation of superseded 1837a658 run
37998694264 was attempted and refused HTTP 403; final evidence will use only
97ea4c56. The corrected private reboot fixture remains running.

The focused 97ea4c56 fixture passed in 4m40s (reboot subtest 54.31s), installing
the prebuilt d4d39bf4 application through a valid Nix profile. All first/second
boot units were active/enabled, dependencies matched, boot ID changed and both
sockets returned. No owned VM remained afterward. A fresh utility now owns the
final-source batch: generic package plus standard final-head boot check, composed
application, browser fixture, aitherdev configuration build and exact CI. The
independent package builds share one Nix command so Nix can parallelize them.
Final-head standard check conclusions remain pending; deployment is not started.

The final combined Nix build exited successfully and produced the composed
application path artifact. Generic and composed package checks passed; the
standard 97ea4c56 boot VM passed in 281.07s, including its actual reboot and
lingering/socket assertions. The enclosing batch has advanced to the browser
fixture. Configuration build and exact final CI still remain before deployment.

## Open questions

None affecting accepted product behavior. Implementation evidence may refine
the cold activation and package-transition mechanics in design.md.

## Cleanup

Retain feature branches and original initiative worktrees. The newly created
temporary integration targets were removed after their master pushes. Default
branch integration was authorized and completed; post-merge CI passed. No
archive, delete, session stop or aitherdev reboot was requested.

The final browser suite passed all seven subtests in 158.72s, and
portal/internal/web returned PASS. The batch advanced to the aitherdev
configuration build; final runtime CI follows that build.

The entire final packaged/browser/configuration-build script exited 0. Both
VM checks, generic/composed packages, browser recovery fixture and aitherdev
configuration BUILD ONLY passed. The watcher now observes exact runtime CI
37999200234 at 97ea4c56. No deployment has begun.

The first final CI observation inferred aither64/vpsfree-cz-workspace from
the watcher CWD, so GitHub returned 404 for the runtime run. This was a lookup
error, not a failing workflow. A fresh utility now observes the same existing
37999200234 with explicit --repo aither64/dev-workspace and verifies its
97ea4c56 head. No workflow is rerun.

Exact final runtime CI [37999200234](https://github.com/aither64/dev-workspace/actions/runs/37999200234)
completed successfully at 97ea4c56. All local long checks and final library CI
37995107833 passed. Configuration/profile deployment is now the current phase.

Final generic/composed Ruby results: session 404 runs/5452 assertions/0 failures/
0 errors/12 skips; auto-archive 12 runs/50 assertions/0 failures/0 errors; host
127 runs/994 assertions/0 failures/0 errors/3 skips. Host idempotency VM passed
in 223.12s; standard recovery boot VM passed in 281.07s. Browser suite passed
all seven test files in 158.72s. Aitherdev build generation was
2026-10-10--00-53-47.

The authorized configuration deployment at f715299c exited 0 after 1m43s.
Confctl reported SystemState=running and active firewall, with 2 health checks
passed/0 failed. It used --dry-activate-first --no-reboot. Application user-profile
switch is next; full post-deployment health verification remains pending.

## Final deployment result

Configuration f715299c deployed with dry activation and --no-reboot, exit 0;
confctl health checks passed 2/2. Selected system:
/nix/store/kxscawff631f111i9blaiwbjpvv9h9g6-nixos-system-aitherdev-26.05.20261008.7c8764b.
Stable workspace-host switch selected the composed application at 4f4060ab,
exit 0. Selected package:
/nix/store/wgbyyyivgza0i1y4wpk8d0hn8c0pd8fj-dev-workspace-0.2.0.

Post-deployment checks passed: sessionRecoveryPolicy=1, livePackageSwitchPolicy=1,
all four user services active/enabled, lingering=yes, Unix healthz {"ok":true},
owned session page HTTP 200 and TLS portal expected unauthenticated HTTP 401.
Native Codex remains PID 1204139; tmux remains PID 435397. Portal/router refreshed
to 1415774/1415614. Boot ID remains 0104034e-3a15-4772-aa62-aac7ee4ff6ef.
No occupied-host/native restart was performed. Private VM reboot and separate
native fixtures provide restart coverage; accepted integrated-test limits remain
in review.md. Normal downgrade is refused; recover with a compatible forward
package. No default branch was integrated.

Stable portal URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-09-portal-restart-recovery/.

Final handoff sanity check: all four feature worktrees are clean, each local
head equals its published origin feature head, all final diffs pass whitespace
checks and the shared index is empty. Workspace master remains b7399587 and
the verified initiative identity is unchanged. No feature branch integration
or lifecycle mutation was performed.

## Follow-up: duplicate artifact manifest investigation

User requested investigation and a proposed solution for the portal error on
2026-10-05-network-ipv4-left-counter. Read-only inspection confirmed the same
artifact path twice at manifest lines 77/518, introduced together by workspace
b7399587 before deployment. Both Go and Ruby reject duplicate paths; that contract
predates this rollout. Retained native thread metadata is present. No native
runtime status/history proof or mutation was attempted.

A private copy reproduces validation exit 1; removing only the later two-line
artifact declaration gives exit 0 with the deployed binary. The live manifest is
unchanged, in keeping with investigation/proposal scope. Suggested next action:
apply that minimal metadata repair in the affected session's owned scope and
reload its page; no restart or runtime change is necessary. Durable findings:
[duplicate artifact validation](../../notes/dev-workspace/2026-10-10-duplicate-portal-artifact-validation.md).

Follow-up phase: investigation complete; proposed repair verified in isolation,
not applied. Original recovery implementation remains deployed, with branches
ready and awaiting merge approval.

Follow-up implementation started with verified retained initiative identity.
No native lead/team roster exists; main owns edits and design. Fetched affected
remotes; default heads are unchanged, workspace master/origin b7399587. Feature
worktrees are clean. Deployed runtime 97ea4c56 will be preserved, not amended.

Follow-up implementation and quick checks passed at runtimea756b2c6. Go session
suite and live-server duplicate regression passed, all packages compile, Ruby
canonical fixture/readiness/save checks passed 4 runs/58 assertions. The initial
HTML-label counting assertion and direct Ruby subfile entry-point setup failures
were corrected and verified. No raw manifest or native state changed. Pins are
consolidated at compositionbe09a886/config875420e0; pin contract and configuration
hooks pass. Final independent review is the current phase, before long checks.
Packet: [duplicate review](duplicate-artifacts-review-packet.md); prepared rollout:
[duplicate rollout](duplicate-artifacts-rollout.md).

Follow-up final whole-branch review completed with no findings in all four lanes.
Exact reviewed heads are a756b2c6/c9878454/be09a886/875420e0; retained deployed
source, consolidated pins and no migrations were independently confirmed. The
long-check launch failed before any checks ran (exit 126): the temporary script
was non-executable. Invocation is corrected to bash /tmp/portal-duplicate-checks.sh;
the failed-launch evidence is retained separately. No source change or CI rerun
is required. A fresh operation watcher owns the corrected batch.

The corrected follow-up batch passed (exit 0, 1,048s). Generic/composed package
suites and unchanged original duplicate fixture validation passed. Browser suite
passed all seven checks in 160.20s; localhost TLS diagnostic lines did not fail
the suite. Aitherdev configuration build generation 2026-10-10--09-13-27 passed.
Exact runtime CI [38032042779](https://github.com/aither64/dev-workspace/actions/runs/38032042779)
passed at a756b2c6 (fast success, host skipped; unchanged original VM evidence
remains applicable). Current phase is deployment; the baseline still matches
the captured boot/profile/native/tmux/affected-manifest values.

Follow-up configuration deployment at 875420e0 exited 0, activated generation
2026-10-10--09-13-27, and passed 2/2 host checks. Stable application profile switch
at be09a886 is running; live unchanged-manifest/conversation/health proof follows.

## Follow-up final deployment result

Application profile switch at be09a886 exited 0, generation 104. Actual package
/nix/store/s2zxa731kh87li7syxi3qzjzw3wcp9zd-dev-workspace-0.2.0; actual system
/nix/store/dmzm997gh7smblm2c1dlrcfsqwbr1mjq-nixos-system-aitherdev-26.05.20261008.7c8764b.
All post-switch checks passed: recovery/live-switch policies 1, four services
active/enabled, lingering=yes, healthz ok, owned and affected pages HTTP 200,
affected thread API HTTP 200 with exact retained root, one duplicate artifact
catalog link retaining first label, artifact download HTTP 200, TLS unauthenticated
401. Manifest SHA-256 remains
ac058185886e7ea9ce5ba0bfdb7c512578927ed8c78abc3b962e81d170f8c50f.
Boot ID remains 0104034e-3a15-4772-aa62-aac7ee4ff6ef; native Codex/tmux PIDs remain
1204139/435397. Portal/router refreshed to 3094612/3094571. No conversation
Send/Continue or foreign tracking edit occurred. No default branch was integrated.
Ready for use; retained feature branches await explicit merge approval.

Final handoff sanity: verified retained initiative identity and stable URL. All
four feature worktrees are clean and equal their published exact reviewed heads;
complete series remain runtime 2 commits, provider/composition/configuration 1
each. Complete diffs pass whitespace checks; review confirms consolidated pin
streams and no migrations. Shared master remains b7399587 with empty index.
Tracking remains current in the working tree under the normal checkpoint cadence;
no additional tracking commit or lifecycle mutation was needed.

## Integration approval

User explicitly directed "merge it" after the completed deployment/readiness
handoff. This approves integration of this initiative's complete reviewed
deliverable into codex-web/master, dev-workspace/master, workspace/master and
vpsfree-cz-configuration/master. It does not authorize archive, branch deletion,
session stop, host reboot or additional deployment. Fetch and check the complete
series/final diffs against the final review before each fast-forward integration.

Fresh fetch found configuration master b3eec80f (one upstream llm-agents update).
Configuration rebased cleanly from 875420e0 to 6e4947b5; range-diff reports the
single owned commit identical. Pin contract still selects a756b2c6 and unchanged
extension/provider. Feature push used an explicit lease on old 875420e0. No new
design/scope or review lane rerun is needed; merge approval remains applicable.
Other default branches and exact reviewed heads are unchanged. Whole-branch
review still applies: runtime 2 functional commits, provider/composition/config
1 owned commit each, consolidated pins, no obsolete paths or migrations.

Fresh detached integration targets are under worktrees/2026-10-09-portal-restart-
recovery/integration-targets for the three independent repositories. Configuration
worktree creation returned 78 after creating the checkout because its checkout
hook lacked Bundler dependencies in the ambient shell. Rerunning the exact
post-checkout hook through the repository Nix shell passed; no hook was bypassed.
Target configuration build follows before that master is pushed. Runtime/provider/
workspace source heads remain identical to their passing reviewed/deployed heads.

All four approved master integrations fast-forwarded and pushed successfully.
Fresh ls-remote proves each remote master and retained feature ref equals its
final exact head; [merge-proof.json](merge-proof.json) records them. No feature
refs or normal initiative worktrees were removed. Configuration's fresh target
build passed at 6e4947b5 in 154.57s, generation 2026-10-10--13-02-15, without
deployment or local kernel compilation. Provider master CI
[38047024103](https://github.com/aither64/codex-web/actions/runs/38047024103)
passed at c9878454. Runtime master CI
[38047082380](https://github.com/aither64/dev-workspace/actions/runs/38047082380)
is running at a756b2c6; workspace/configuration have no push CI.

Removed all three newly created, verified-clean detached integration targets
using ordinary git worktree remove. Original initiative worktrees and local/
remote feature refs remain. No archive/delete, reboot, profile switch or native
restart accompanied integration. Runtime master CI is the sole remaining check.

## Integration completion

Runtime master CI
[38047082380](https://github.com/aither64/dev-workspace/actions/runs/38047082380)
passed at exact final head a756b2c6: fast 12m01s, host 7m11s, overall 12m03s.
Together with the successful provider master CI and fresh configuration build,
all post-merge checks are complete. All four original feature worktrees are
clean and their retained local/remote feature refs equal the final heads.
Workspace shared master and remote master subsequently advanced to
1025d8c346a961c9f219ebb490a84c9d28f07b37; ancestry confirms they contain exact
feature head be09a886. The shared index is empty and unrelated files remain
untouched. The timestamped merge-proof.json preserves the original successful
remote integration proof.

Every registered final feature head is merged into its remote default branch;
no review, CI, deployment, approval or temporary-worktree cleanup remains.
Lifecycle is complete. The session and original feature worktrees remain open
and retained. No additional deployment, archive, deletion, session stop or
host reboot was performed during integration.
