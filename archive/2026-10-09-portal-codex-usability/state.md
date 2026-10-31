---
lifecycle: complete
---

# 2026-10-09-portal-codex-usability

## Status

Integrated and deployed. User approval in this conversation on 2026-10-09:
"ok, merge it", following the completed four-repository delivery. Scope is
codex-web/master, dev-workspace/master, workspace/master and
vpsfree-cz-configuration/master. Approval covers the reviewed final changes;
any required clean rebase will be checked for patch equivalence.

Clipboard numbering is implemented,
reviewed, tested and deployed to aitherdev at the recorded final heads. Every
pasted filename is numbered from one per original filename/session and continues
across messages/removal/reload. Both composers, original-file recovery and native
text paste pass. Live served app29/provider upload6 bytes match source, account
still reports three available resets, and native Codex MainPID1204139 stayed
running. No implementation, review, verification or deployment blocker remains.

- [x] Filename numbering implementation and quick checks
- [x] Filename numbering independent review
- [x] Filename numbering verification
- [x] Filename numbering redeployment and smoke
- [x] Default-branch integration (exact final heads proved merged remotely)
- [x] Temporary integration worktrees removed
- [x] Post-merge CI observation stopped on explicit user instruction

Previous delivery:

Ready, awaiting merge approval. New session clipboard attachments are fixed and
deployed to aitherdev. Initial request now uses the existing binary paste handler;
native text paste and draft recovery retain their behavior. Browser/package
checks, exact-head CI, final independent review, guarded deployment and read-only
smoke checks pass. All three actual resets remain available and native Codex
MainPID 1204139 was preserved. No implementation or deployment blocker remains.

This initiative was created by this conversation with
`dev-session start portal-codex-usability --no-codex --no-attach --json`.
It has no retained team; the lead owns design and application edits.

- [x] Planning and read-only investigation
- [x] Visual follow-up implementation and documentation
- [x] Follow-up quick checks and committed branch inventory
- [x] Follow-up independent review
- [x] Follow-up verification and publication
- [x] Follow-up aitherdev host and user-profile deployment
- [x] New-session paste implementation and quick checks
- [x] New-session paste independent review
- [x] New-session paste verification and redeployment
- [x] Integration (subsequently authorized and completed)

## Next actions

No implementation, deployment or integration work remains. The user explicitly
instructed "no waiting for CI after merge"; local CI observation is stopped and
remote workflows are left running. Keep this session and all feature branches.
No archive, deletion or published-history rewrite is authorized. The user has
requested suggestions for improving history review after redundant pins entered
master; record the review failure below and present concrete rule changes.

## Documentation

Provider reference and portal README/guide updated. See [design.md](design.md)
and [creation-paste-review-packet.md](creation-paste-review-packet.md).

## Repositories

All feature branches are `2026-10-09-portal-codex-usability`, published over SSH
and retained. Default-branch integration is complete at these exact heads.

| Project | Base | Current head |
| --- | --- | --- |
| codex-web | 3d07cf60 | 7dab76305dc0084735095d6dbdaef607585d9bca |
| dev-workspace | c51ba3c0 | 66262519d497073d9bb0dccc2252cdec4528f389 |
| workspace | 21624498 (registered 4ac9ef3e) | 07b393609417e921d5b1c2cfec7b3d89abc473ab |
| vpsfree-cz-configuration | ae670dc0 | 1f3569902a4a6b02633019cd172eade5afe90005 |

Canonical worktrees are `worktrees/2026-10-09-portal-codex-usability/<project>`.
Unconsumed corrections and repeated dependency updates are folded into owning
commits. Previously deployed commits remain as delivery provenance. No obsolete
unconsumed history or migrations. See [review.md](review.md),
[visual-review-packet.md](visual-review-packet.md) and [rollout.md](rollout.md).

## Verification

New-session clipboard correction at the current heads:

- Quick syntax/whitespace checks and focused Go checks pass (0.245 seconds).
  Configuration hooks pass. Composition passes at runtime fbf3493d.
- Independent same-reviewer final review passes all four lanes. The complete
  14-commit history is coherent; no obsolete unconsumed history or migrations.
- Fresh Luna/low utility owns the affected browser cases, runtime evaluation,
  generic-source check, full composed workspace checks/package, aitherdev build
  and exact current CI 37963716009. Browser cases and the full composed package
  checks/build and host build pass. Exact CI 37963716009 succeeds at c650a4c7.
  Full batch passed in about 14minutes, exit 0. Current evidence:
  /tmp/portal-creation-paste-retry.log
  and /tmp/portal-creation-paste-retry.exit (zero).


Visual follow-up at the current heads:

- Independent review: all four lanes pass without findings; the complete
  11-commit history is coherent, with no obsolete unconsumed history or migrations.
- Browser: revised presentation, settings and usability cases pass in 63 seconds.
  Mocked account data and reset RPCs cover layout, reset safety, native text
  paste and binary attachments. Lead inspected the desktop and phone captures.
- Runtime package checks, composed workspace checks/build and the aitherdev
  build pass. Exact runtime CI run 37956710362 succeeds at 577d5b72.
  Full evidence: /tmp/portal-visual-checks.log; wrapper exit status zero.
- Composition passes at runtime 577d5b72; the extension and provider stay fixed.
- Host generation 2026-10-09--18-40-23 built and dry-activated successfully.
  Guarded host and profile activation both exited zero; both host health checks
  pass. The deployed app, stylesheet and reset controller byte-match the final
  source; session HTML selects app.js?v=27 and style.css?v=6.
- Read-only live account check reports credits, three available resets, three
  detail rows and three expiration dates. No reset POST was sent. Codex remains
  active at MainPID 1204139; the restarted portal is active at MainPID 3194295.
  Configured-local-CA TLS check returns the expected unauthenticated HTTP401.
  Exact stores and operation evidence are in [rollout.md](rollout.md).

Initial delivery evidence retained for unchanged behavior:

- Quick: 59 provider Node tests and five mocked reset-controller tests pass.
  Focused Go account/client/cache and shipped browser API contracts pass.
- Protocol: selected native Codex 0.160.0 experimental schemas pass the full
  corpus; optional account/reset RPC supported.
- Review: all four Important findings fixed; same independent reviewer passes
  the focused lock design. Eight coherent commits and no migrations.
- Browser: all seven cases pass across full and focused runs. Chromium and
  Firefox cover presentation/restoration; native two-page reset locks, shared
  storage, same-key recovery, text paste and binary/mixed attachments pass.
- Provider package: Nix flake checks and exact-head CI 37943560998 pass.
- Runtime CI: exact final head675504f6 passes run37945562244 (fast job;
  unchanged host VM job is skipped on feature branches).
- Runtime/workspace package and host build pass in 1,757 seconds. Full log
  /tmp/portal-usability-package-checks.log. Host generation
  2026-10-09--17-06-31; kernels fetched from cache, no local kernel build.
- Composition: check passes at runtime 675504f6; extension source preserved.
- Deployment: exact host generation 2026-10-09--17-06-31 dry-activated and
  switched, then the composed workspace user profile switched successfully.
  Live portal/provider assets match the final sources. Read-only account checks
  report credits, three available resets and three expiration/detail rows.
  Codex MainPID 1204139 and native version 0.160.0 were preserved. Public TLS
  with the configured local CA returns the expected unauthenticated HTTP401.
  No live reset use. Exact deployed store paths are in [rollout.md](rollout.md).

Detailed review and failed-check diagnosis: [review.md](review.md).
Executed transition evidence: [rollout.md](rollout.md).
Complete cleaned branch series: [final-inventory.md](final-inventory.md).

## Cleanup

Preserve unrelated shared workspace changes. Retain branches and this session.
All four source worktrees are clean and their published feature refs match the
recorded final heads. Workspace master integration also published its existing coordination
ancestors as part of the authorized fast-forward; no shared history was rewritten. Initial delivery checkpoint c31fd962 is the day's consolidated local tracking
commit. Visual follow-up records remain current in the working tree under the
tracking cadence. No feature content is integrated by coordination commits.

## Browser verification correction

First long batch: provider Nix checks pass; settings, lifecycle, history paging
and repository browser cases pass. Three fixtures failed: question warning
still used the old ten-second grace; archival metadata assertions targeted the
old values container despite metadata already living under Technical details
in the base revision; asynchronous reset confirmations raced listener handling.
Fixtures now use current timing/selectors and await dialog handling. The
focused reruns pass; the final presentation fix opens the existing Workspace menu. Complete log /tmp/portal-usability-full-verification.log.

CI cancellation of superseded run 37943731262 was refused with GitHub API403
because the token lacks cancellation permission; no other runs were targeted.
Read-only native account check confirms credits and all three banked resets.
No live reset redemption was performed.

## New-session browser fixture diagnosis

First follow-up batch stopped at the new index upload control assertion; no
later checks ran. The question-browser harness replaced config.BaseURL after
Server.New but kept trustedOrigins initialized to workspace.example.test.
Creation /api/upload-drafts POSTs therefore failed exact-origin validation,
while the already configured conversation/upload handlers accepted the TLS
fixture URL. This had been hidden because prior portal mutations were mocked.
Set the fixture's trustedOrigins to its actual TLS origin before serving. The
application wiring and public boundaries are unchanged. Treat this as a narrow
fixture remediation under review step9; inspect directly, run focused checks
and consolidate the unconsumed correction into its owning commit/pins.
Evidence: /tmp/portal-creation-paste-checks.log (exit 1, browser stage).

The narrow test-origin remediation was inspected directly under mandatory-review
step9; application bytes are unchanged from reviewed fbf3493d. Focused Go checks
pass (0.238 seconds). Unconsumed source and pin corrections are consolidated; final
heads remain a 14-commit series. Config generated changelog was corrected to
reflect its net deployed-predecessor 577d5b72 -> c650a4c7 update after consolidation;
generated Git history remains. Composition passes at c650a4c7.
Cancellation of superseded CI 37962866775 was attempted and denied HTTP403 due
to token permissions. Exact current CI is37963716009; no unrelated run targeted.

New-session verification completed successfully. Usability/creation browser case
passes in7.69 seconds; independent creation-settings fixture passes in3.95 seconds. Package
Go checks and Ruby suites pass:401 runs/5408 assertions,12 runs/50 assertions,
126 runs/988 assertions, with expected skips and no failures/errors. Workspace
checks pass; candidate profile is81y60n11hr869w4d73jld43r3x3y1l6p. Exact host
generation 2026-10-09--19-22-15 built; no local kernel build. Dry activation was
parent-launched with source guards; fresh Luna/low watcher observes it.

New-session deployment and read-only smoke pass. Exact host generation
2026-10-09--19-22-15 dry-activated and switched; workspace user profile switched
with both health checks passing. Profile 81y60n11hr869w4d73jld43r3x3y1l6p and
host lz94vc6b11c6n17bbd9rnafszswkmvya match the built outputs. Served app/style/reset
assets byte-match final source; index/session HTML selects app.js?v=28. Live
read-only account data reports credits and three resets/details/expiration rows.
No reset redemption or live test-session POST was performed. Codex stays active
at MainPID 1204139 and version 0.160.0; portal active at MainPID 3496724. Configured
local-CA TLS check returns expected unauthenticated HTTP401. See rollout.md for
exact stores and operation evidence. All four source worktrees are clean and
published final refs match. No further tracking-only checkpoint this day.

## Numbered paste verification preparation

Provider Node suite64 passes; revised upload suite39 passes. Runtime focused Go
checks pass0.105s; browser syntax/whitespace and confctl hooks pass. Composition
checker passes runtime66262519. Metadata build first refused a Go/flake pin
mismatch; aligned pins and fresh utility hash build computed the adopted hash.
No final integration started before review. Full18-commit inventory and all final
diffs are in numbered-paste-review-packet.md/final-inventory.md. Retained native
reviewer identity and saved Astra/xhigh verified; independent review pending.
Workspace three prior pins rebased patch-equivalently onto shared21624498.

Numbered paste final independent review passes all four lanes with no findings.
Retained reviewer verified all final diffs byte for byte and the full18-commit
series, including patch-equivalent workspace rebase; no obsolete unconsumed
history or migrations. Provider exact-head CI37970617731 succeeds; runtime
CI37971136991 is in progress at66262519. No superseded active runs remain.
Fresh Luna/low owns /tmp/portal-numbered-paste-checks.sh final check batch.

Verification milestone: provider packaged checks and the representative real
browser usability fixture pass at reviewed heads. Browser covers both inputs,
repeated image.png with distinct bytes, original text paste/undo, numbering after
reload, upload readiness and frozen creation recovery. Fresh utility remains
responsible for runtime evaluation/generic source, composed package/checks, host
build and exact-head CI. No deployment has started.

Workspace flake checks pass. The composed package build is running its declared
Ruby session tests; aitherdev build and final CI confirmation follow in the same
owned utility batch. No unexpected local kernel build reported.

Final batch passes exit0 in about15minutes: provider packaged checks, real
browser fixture, runtime evaluation/generic source, composed workspace checks
and package, aitherdev build, runtimeCI37971136991 and providerCI37970617731.
Full evidence: /tmp/portal-numbered-paste-checks.log, .exit=0, .stage=completed.
Package /nix/store/za0yzb4j1ahkdgnbciix3plfzsyhcwrr-dev-workspace-0.2.0.
Host generation2026-10-09--20-31-44; no local kernel build. Next guarded dry
activation, host/profile switch and read-only smoke; fresh utilities observe.

## Numbered paste deployed evidence

Generation2026-10-09--20-31-44 dry activation passed (invocation
117b83600e4043babf20735986229f75; exit0). Guarded activation passed (invocation
3a118da9ebf94075a51e199c9b3ca2af; host-switch/profile-switch/exit all0); host
health2/2 pass and compatible live profile switch selected the built package.
Evidence: /tmp/portal-numbered-paste-deploy-evidence/{dry,activate}/.
Live app.js/style.css/reset-credits.js and provider uploads.js/conversation.js
byte-match source. Index/session HTML selects app29. Actual portal executable is
/nix/store/za0yzb4j1ahkdgnbciix3plfzsyhcwrr-dev-workspace-0.2.0/bin/workspace-portal,
MainPID3762055. Codex MainPID1204139/version0.160.0 preserved; codex/current
resolves to the existing native a29lfsrd package. Live account reports credits,
three available resets/detail rows/expiration dates. No reset POST was sent.
Public configured-local-CA TLS GET returns expected unauthenticated401.
A trailing optional readlink diagnostic used an incorrect guessed profile path
and returned1 after the successful smoke script; corrected using the actual
codex/current link and running portal executable, which both pass. Functional
smoke itself exited0. All four source worktrees remain clean and their published
refs match. No new same-day tracking checkpoint, merge, archive or cleanup.

## Master integration and review correction

Approval: user "ok, merge it" in this conversation on 2026-10-09, covering
codex-web/master, dev-workspace/master, workspace/master and
vpsfree-cz-configuration/master. Fresh remote targets were ancestors of the
reviewed heads; no rebase or patch change was needed. Comparisons were captured
for every repository before integration. All four fast-forward merges and
ordinary SSH pushes succeeded; fresh fetches prove the exact local/remote
feature heads are merged, with both feature refs retained. Exact before/after
refs: [integration.json](integration.json). Shared checkout remains master,
its index remains untouched, unrelated changes are preserved, and the three
clean temporary target worktrees were removed.

Target-check quick verification: provider uploads39/39 pass; focused portal Go
passes0.107s; whitespace and composed deployment checks pass. Configuration's
post-checkout hook initially failed outside its declared Nix environment (exit78)
after creating the checkout. Its merge/hooks and push passed inside Nix, without
bypasses. Existing lesson: notes/vpsfree-cz-configuration/2026-10-06-worktree-checkout-hooks.md.
Two incorrectly scoped shell commands were stopped/corrected; the composition
check was also initially run before the configuration merge completed and
reported the then-mismatched pins. Corrected target check passes at66262519.
These did not change source, deployed state or reviewed revisions.

Post-merge CI: provider run37978158995 passed. Runtime run37978162925 had its
host job pass and fast job still running when observation was stopped on the
user's explicit "no waiting for CI after merge" instruction. Fresh Luna/low
utility /root/master_merge_ci_watch stopped its local gh watcher (exit130),
leaving remote CI untouched. Logs: /tmp/portal-codex-master-ci-watch/.
There is no remaining authorized CI wait. Existing tested deployment is unchanged.

User correctly identified four redundant devWorkspace channel update commits
081ac7cc,04ee1fe6,557c97a7,1f356990 entering configuration master. One update from
basec51ba3c0 to final66262519 would have produced the same final lockfile. The
lead's inventory labeled deployed feature revisions as consumed provenance;
the independent reviewer accepted that rationale rather than challenging the
redundant pin sequence. Development deployment alone did not require retaining
these commits. The prior "no obsolete unconsumed history" conclusion was too
narrow. The existing general-review Commit Series rule already explicitly
requires repeated flake/dependency updates in one stream to be consolidated;
this was failure to enforce an existing rule, not absence of a rule. Workspace likewise retained four successive runtime-pin updates.

Proposed rule clarifications and enforcement: distinguish deployed runtime/schema
compatibility from commit-history retention; require one final pin update per channel/role unless
an independently shipped boundary requires multiple commits; make generated
updates part of whole-branch history review even when their content is exempt
from standalone review; require reviewer disposition of every superseded pin
with a concrete reason for retention; treat redundant unmerged pins as an
Important finding before merging. Keep rollout SHA provenance in rollout
records. No review-rule edits or published-master rewrite have been performed.
