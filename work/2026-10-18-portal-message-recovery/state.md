---
lifecycle: active
---

# 2026-10-18-portal-message-recovery

## Current status

Phase: enabling native coordination after explicit permission.
Implementation, quick checks and independent final review are complete. Source
Go and browser checks, runtime package check, composed workspace build, exact
aitherdev build and final-head CI passed. Nothing has been deployed or integrated.

The user replied “yes” on 2026-10-19 to the exact request to stop only this
initiative's shell runtime and enable native coordination. The normal stop
command, with exact-slug interactive confirmation, removed that runtime and
its authority. Its trailing recovery call then failed because the threadless
session's empty thread ID cannot form a recovery identity. dev-session list
confirms TMUX none. Do not repeat stop; normal native startup is next.
Aitherdev was last observed reserved by 2026-10-18-provider-switch-redesign;
use the coordinator queue when eligible, without polling or releasing its owner.

## Phase checklist

- [x] Investigate behavior and settle user choices.
- [x] Implement, document and complete quick checks.
- [x] Commit the complete deliverable and run independent final review.
- [x] Finish package/host builds and final-head CI.
- [ ] Enable native coordination (shell stop authorized and complete).
- [ ] Deploy and verify aitherdev.
- [ ] Integrate exact final heads and complete handoff.

## Next action

With shell-stop permission received, consolidate current tracking under the
ownership-handoff exception and use normal native startup with the existing
coordination-owner-goal.txt. The external conversation retains implementation
and operational responsibility; the native owner is idle. Prepare approved
coordinated system activation followed by user-profile activation. Verify both
identities, portal behavior and Codex/tmux continuity before authorized merges.
Do not archive, delete or close this initiative.

## Exact branches and worktrees

All branches use 2026-10-18-portal-message-recovery, with worktrees below
worktrees/2026-10-18-portal-message-recovery/.

| Repository | Final published head | Comparison base |
| --- | --- | --- |
| dev-workspace | d3de362f5d8fa86bbf0c4865b0766eb614cf4e2b | 705301228f726bcc9c5e0b516abc03f6f6c995cf |
| workspace | 5ab415afbe766a16267b7ebd5c0646eecfb310e3 | 19eeeb9214eb515a0d6f919f91d8bd6665d9056e |
| vpsfree-cz-configuration | e9dddabf713ab6ee4b4ef24b969ebd68932346dd | 30a20d0ea78afb9854be0845b68a1974ec069b2d |

The initial workspace registration base predates its final pre-review rebase.
verified-branch-inventory.json and *-verified.diff contain the complete current
series and final diffs. Four focused source commits and one final pin per
consumer remain; no obsolete approaches, repeated pin streams or migrations.
Repeat the immediate pre-merge history/baseline check and comparison capture.
All project worktrees are clean. Preserve unrelated shared checkout/index edits.

## Review and verification

- Independent final reviewer /root/portal_final_review, native thread
  01a150d1-1971-72c0-b395-bb55e7da063b, gpt-6-astra/xhigh. All four lanes;
  installed default fallback because this shell-only initiative has no roster.
  Native settings are verified in reviewer-native-policy.json. Risk includes
  persisted browser metadata, mixed-version display and ordered deployment.
- review-report.md records no Blocking findings. Important timestamp DOM
  invalidation was fixed directly and regression-tested; Advisory configuration
  predecessor wording was corrected in the final generated pin commit.
  review-remediation.md records the direct narrow fix under review skill step 9.
  No accepted contract or scope expansion requires another review turn.
- Quick syntax and focused Go/browser contracts passed. Full Go suite passed
  in 73.87 seconds at 421142e3, whose production code matches final d3de362.
  Only browser-fixture synchronization/storage changed afterward.
- Existing paging browser regression passed in 18.58 seconds, including retained
  anchor identity. New complete recovery/display regression passed in Chromium
  and Firefox at final d3de362 (19.24-second Go test, 27.08-second operation).
  Evidence: source-shorttmp-verification.json and source-browser-firefox-verification.json.
- Both final consumers select d3de362; final composed deployment contract passed.
  build-source-heads.json binds current build inputs. build-verification.json
  records per-command results; build-watcher-final.txt will record completion.
- Completed build watcher: native 01a150e6-90e6-7370-a06f-c6871d934954,
  gpt-6-luna/low, full access/never verified. Parent exec session 83982 completed.
  Runtime package passed (330.36s), workspace passed (325.99s). The aitherdev
  command exited 1 before building: Continue? [y/N] received EOF. Inspected
  build-aitherdev.log and confctl build --help; the documented --yes option
  corrects unattended invocation. No code change or build-test failure occurred.
  Fresh watcher 01a150f2-9187-7b80-b9b4-237e8195726a (parent exec 92889 completed),
  gpt-6-luna/low, full access/never verified in
  aitherdev-build-watcher-native-policy.json, completed run-aitherdev-build.py.
  Exact configuration e9dddabf passed in 113.58s, exit 0, without local kernel
  compilation. Evidence: build-aitherdev-noninteractive-verification.json and
  aitherdev-build-watcher-final.txt. No verification operation remains running.
- Final source CI run 39167591341 passed at d3de362. Native watcher
  01a150f1-90f6-7560-88cf-eae3b57f9862, gpt-6-luna/low, full access/never verified
  in ci-watcher-native-policy.json. ci-current-status.json records job results;
  ci-current-result.json records matching head and success. No current CI
  operation remains. Catalog permits one verification watcher at a time.
- Superseded CI cancellation returned HTTP 403; token cannot cancel Actions.
  Do not repeat or cancel current-head/foreign runs. Earlier-head successes do
  not substitute for final-head CI.

Host isolation failures and browser-fixture failure evidence remain retained.
Set DEV_WORKSPACES_CODEX_PROVIDERS to an absent owned path; unsetting it still
loads the host catalog. Set TMPDIR=/tmp inside the Nix shell to keep existing
recovery-test Unix sockets below the pathname limit. Reusable note:
notes/dev-workspace/2026-10-18-source-test-host-isolation.md.

## Authorization, deployment and compatibility

The user's initial direction authorizes aitherdev deployment using configuration
and merging after verification. The earlier explicit scope selection covers
master in dev-workspace, workspace and vpsfree-cz-configuration after successful
deployment verification. Deployment and those conditional merges need no renewed
approval. The separate shell-stop permission was granted by the user’s “yes” on 2026-10-19.

No server submission-ledger, journal/schema, queue, Codex-version or protocol
change. Dismissal adds optional sessionStorage metadata; timestamp retention is
page memory and the cold-loading API field is additive. No database migrations.
System activation precedes the user-profile application; retain machine ownership
through verification and integration. Profile recovery is forward-only through
the original admitted candidate or reviewed successor. Preserve uncertain attempts.

Selected package last verified:
/nix/store/a5dcgj4hxcf6q87agjnpp20ls9jn004d-dev-workspace-0.2.0.
Catalog digest ffaf9deb97720995ad1d662badae7645eba1fede5068eef529c9024efa7e7376.
An older waiting command correctly refused as superseded after another authorized
package switch; subsequent commands use the stable selected entry point.

## Documentation and handoff

Feature semantics: dev-workspace/docs/workspace-portal.md. Repeatable deployment
and recovery: configuration/docs/operations/workspace-coordination-aitherdev.md.
Exact rollout and prepared/executed distinction: rollout.md. Historical development
and failed-attempt narrative: progress-history.md. Original review artifacts and
logs remain available. The portal manifest includes the verified final inventory and verification summary.

Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-18-portal-message-recovery/

The earlier accidental shell-only 2026-10-18-portal-recovery-displays initiative
and its runtime/records remain intact; no cleanup is authorized.
