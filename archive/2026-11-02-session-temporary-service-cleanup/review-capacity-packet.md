# Capacity retry and native fixture final review packet

Final committed source and focused quick checks are complete. This packet is for
independent source/history review, not native, publication or deployment readiness.
Authoritative implementation/test/source receipt:
[capacity-managed-turn-final-receipt.json](capacity-managed-turn-final-receipt.json).

## User outcome and boundaries

Original scope remains registered temporary-service cleanup and Resources/Team
navigation, excluding all existing unregistered services. User authorized
implementation and aitherdev deployment through configuration, with no default
integration or real-session lifecycle authorization.

The later user reported `Selected model is at capacity. Please try a different
model.` and clarified: "Turn continues, capacity error is reported, I expect it
to be retried no matter what. What's the catch?" Exact evidence in
[capacity-retry-diagnosis.md](capacity-retry-diagnosis.md) establishes native
serverOverloaded and enabled capacity policy; accepted-contributor retirement
had already consumed the long turn. The requirement is that accepted input
volume must not disable an otherwise eligible turn's retry. Preserve actual
model/effort/mode/policy, managed provider/instructions/context, explicit
cancellation, recovery holds, native UUID reconciliation and quota semantics.
No model fallback, original prompt replay, reason UI or new retry policy.

## Repositories, source and history

- Runtime: git@github.com:aither64/dev-workspace.git, target master.
  Worktree: worktrees/2026-11-02-session-temporary-service-cleanup/dev-workspace.
  Full base: c2182254d29c4175c3e9fe4267e5a92dd1da6b79.
  Reviewed published predecessor: ee3f1fdd0d3585a8f4fa9b952169d692e9fa3d5f.
  Fixture-corrected local base: 5b4b711748343f4ffe88b96c50d88a9f98eeb04d,
  tree4b299131feba1f8f64ac2dba675d40d542bb98ae.
- Original three service commits: UI19dd03b79a2997098934afafbe70c63b978c1ca7,
  coref7add7cea8a836810d32688ef2d1cf4cc011af19, dependent5b4b7117.
  Fourth capacity commit/final head:18432f0c8f86dec7405257f5dc244762d7a788ed,
  tree013acdd68b79865ce5f72672e0c2049d529e6464. Capacity delta24files1279+/154-;
  complete branch71files5503+/281-. Final source
  /nix/store/9pxkf5h3wrmhsfl4lx4ahjd04mc3khgb-source,
  NARsha256-4EjB9p7pb85lZtZr+RqIJOpkgnAMEjSQRtZLFR3cnjI=;
  active ordinary root capacity-managed-turn-review-source. All676 committed
  files/modes compared with store and clean worktree; manifest and metadata are
  bound by final receipt. Runtime lockfa808c04.../full9nodegraph unchanged.
- B's one-file CLI fixture fix52ed98c9 was folded into the owning dependent
  commit with exact tree equality; UI/core range-diffs are '='. PublishedEE3 and
  52ed refs remain outside final ancestry. See
  [cli-fixture-confirmation.md](cli-fixture-confirmation.md).
- Existing workspace B7/config59d and their source/artifact receipts remain
  historical EE3 inputs. They do not certify the capacity feature or new final
  runtime. New downstream pins/certification follow actual final native success.

Inventory the complete final base-to-head series and final diff. Explicitly
conclude whether obsolete/fixup/transitional history or repeated input streams
remain. No runtime dependency update is intended; native ascending item reads
use the already-pinned codex-web Request interface. Existing three-commit source
reviews remain in review-final.md, review-final-history.md, review-revive-ui.md
and review-native-job.md; preserve the original reports.

## Changed behavior and compatibility

The native fixture uses a real terminal and correct yes/exact-slug answers for
delete/retry/stop. It checks the intended shutdown refusal, preserved files,
ordinary thread_retired removal journal and services_pending prelude with the
same operation ID/force. Product confirmation/cleanup order is unchanged.

Capacity proof uses one compact current-turn authority and SHA256 native input
prefix, with shared binding/context. Accepted snapshots leave the existing
64-entry budget only through exact native matching and atomic prefix/source
save. Native history checking is incremental, including restart verification,
without a total-page/input cutoff. Cached hints do not grant execution authority.
Unaccepted, uncertain and Pending tuples stay protected.

An already durably handled current turn may retire only accepted-bound,
nonexecuted, unprotected snapshots without acquiring compact authority/rearming.
Fresh ordinary latest-turn observation also permits obsolete executed caches to
retire when not protected; failed/empty observations or old receipts cannot
authorize it. Both caller changes must save atomically before dependent work.

No database migrations. Existing production retry schema1 is an intentional
supported predecessor. A strict dual1/2 reader upgrades valid records only on
ordinary admitted save; immutable Snapshot/Pending/UUID/charge formats remain.
Keep turnRetryStateSchema:1 for predecessor-host admission, add
turnRetryManagedTurnProof:1, and require both for any retained retry JSON through
existing package/candidate guards. Old strict readers cannot manage schema2;
recovery is forward with a compatible package. No bulk rewrite/new inventory or
state deletion. Previously consumed failures stay consumed. New local service
schema1 and ordinary lifecycle journals/receipts retain their accepted contracts.

Design/clarifications: [design.md](design.md), compact-current-turn section,
already-handled exception, obsolete-executed-proof retention and system-first
feasibility note. Host system activation precedes ordinary app selection; source
tracing found no new-capability ordering deadlock or need for a bridge/bootstrap.

## Verification and documentation

Final focused commands and scopes are in the final receipt: turnretry6.960s,
workspacecodex166.553s, session4.094s pass; affected retry-web43.415s pass;
host12/238pass0.641s; shipped Go harnesses TestComposerHandoffRetainsOriginalIntent
and TestShippedBrowserClientMatchesSessionAPI pass0.673s/1.238s (actual browser JS
and composer retry module). Lead independently compared tested tree
95b4e7f8afd55d67ccce2a4615e71ae1d15cfc18 to final commit: only one added active
observation line in the new web test; all core code/test inputs unchanged. The
affected web selection was rerun after that fixture correction.

Batch01/02 failures and incorrect standalone integration-script invocation remain
retained, not hidden as an overall batch pass. Three core failures were obsolete
snapshot assumptions/invalid unbound synthetic fixture; corrected tests check
managedTurn plus actual Backend.Prove and original UUID/send limits. Web failure
was missing active observation in its new fixture; production code unchanged by
these corrections. Two Playwright consumers remain postreview integration scope.

Earlier development evidence is scoped to its actual draft/input hashes:

- Actual 74-input production-wrapper baseline red and corrected green.
- Pure-state220 inputs with120,000-byte common instructions/35,000-byte context.
- Reader component261pages, one-page batches, restart at130, corruption/cursor controls;
  this uses synthetic native DTOs and does not certify the real native API.
- One-off205-input large wrapper passed214.979s with56,000-byte role instructions
  and40,000-byte context; receipt capacity-managed-turn-205large-receipt.json.
  Permanent cases are reduced to205small +65large with separate pure-state coverage.
- 12 host cases with 238 assertions passed in 0.715s; predecessor Go/Ruby reader/host
  checks are in capacity-managed-turn-predecessor-receipt.json.
- B fixture parse/evaluated-Python/type/lint, harmless real-PTY wrapper probes,
  and existing confirmation4/21 checks; no VM acceptance implied.

Multi-turn cache/protection/save-failure and handled/warmsettings regressions pass
within the full state/core batches, including200successive Controller turns.
Long integration/native checks run only after final committed review.
Earlier EE3 CI41533913313 passed fast/package/creation and failed the now-corrected
native fixture confirmation; neither that run nor old app/system/driver outputs
certifies the changed source. No fresh native cleanup/installed usability claim.

Owning product documentation: runtime docs/turn-retry-recovery.md. Lead applied
vpsfree-user-facing-writing and pinned English guidance to settled facts before
commit, including exact atomic-save recovery wording. Operational plans/results
stay in this session; no new documentation bundle or historical backfill.

## Required review assignment

High risk: persisted retry authority and automatic continuation, native protocol,
host package compatibility/forward recovery. Assign retained reviewer0 unchanged
Sol/xhigh/read_only/purpose review/ready after fresh roster verification, with
general, architecture/repetition, scope/proportionality and risk/compatibility
lanes. Reviewer must read mandatory-change-review and all four lane references,
perform review directly with no nested reviewers, and record whole-history and
migration conclusions. Scope/proportionality must distinguish the explicit retry
follow-up from the original cleanup feature. Inspect actual consumers: portal,
CLI, retained-team delivery/scheduler and host candidate preparation/activation;
downstream workspace/config source selection remains a later mechanical stream.

No deployment/copy/claim/default integration/real-session lifecycle action has
occurred. No publication or long-test permission follows review acceptance.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
