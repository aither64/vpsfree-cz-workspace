---
lifecycle: complete
---

# Codex 0.163.0 upgrade

## Current status

The Codex 0.163.0 upgrade is complete. All four exact final feature heads are
integrated into their remote master branches. Aitherdev's reservation is
released at revision 7, and all 18 notifications are delivered. The user explicitly
instructed "merge it and release aitherdev" for codex-web, dev-workspace,
vpsfree-cz-configuration and workspace to refs/heads/master, followed by ordinary
coordinator completion. Session, worktrees, branches and recovery roots remain.
See [final integration and release](integration-completion.json).

Aitherdev's system/profile links select lr6b9x40 at configuration aed7d507.
The workspace profile is a335n75h and its actual managed native assembly is
jrsm1rzx. Both report Codex 0.163.0; the running native SHA-256 is
5e538cfe7c25daf382afe195c08b2ffd24415b0cdd7f5456ec0cf1d277c3d1a5.
Exact paths and accepted receipts are in [postactivation-acceptance.json](postactivation-acceptance.json).

- [x] Implement/publish layered skills, package/catalog/protocol updates and matching pins.
- [x] Quick checks, skill validation, whole-branch independent review and CI.
- [x] Native isolation, naming VM, persisted-state compatibility and exact builds.
- [x] Coordinated system then workspace profile rollout and two bounded profile fixes.
- [x] Real provider check, deployed profile safety, portal/terminal/thread acceptance.
- [x] Preserve recovery roots, reconcile pending marker, settle jobs and notifications.
- [x] Integrate all four exact final feature heads under recorded user approval.
- [x] Finish the coordinator reservation after exact integration/live proofs and explicit completion.

## Integrated final branches

All use 2026-10-16-update-codex and are clean, published and integrated. Original
reviewed/deployed ranges remain frozen in [final-heads-login-fixed.json](final-heads-login-fixed.json);
final integration and replacement proofs are in [integration-completion.json](integration-completion.json).

| Repository | Final head | Commits |
| --- | --- | --- |
| codex-web | a0561fad8decb794117f8959fa2dd629547c5ba7 | 2 |
| dev-workspace | 3c57e2eab56c94fec5f456d8067def8717a0d418 | 2 |
| vpsfree-cz-configuration | aed7d5071e24793d7bd811af11ccfa80e6f049d6 | 5 |
| workspace | 6bebd5ee14af006aedc4eff827b005a428682d78 | 2 |

Worktrees are under worktrees/2026-10-16-update-codex/. No application migrations.
Repeated dependency streams were consolidated. The two separate profile fixes
remove invalid schema fields and preserve shared login respectively; independent
whole-branch review accepted that split.

## Verification and review

Exact schemas and all 55 utility restrictions passed. Browser contracts (64),
Go, Ruby/Nix package suites, native namespace/hostile-dispatch suites for both
GPT-5.5 and Luna, and managed naming NixOS VM passed. Real Luna/low naming after
deployment returned a valid title in 3444 ms. Synthetic threads from 0.160.0 and
0.162.1 passed new read/resume/turn/fork and older-reader-after-upgrade checks.
Final codex-web CI and runtime CI 38920925512 passed. No local kernel/Rust build.

Independent Astra/xhigh review covered all four lanes and complete histories:
[original report](review-report.md), [native fixture follow-up](followup-review-report.md),
[strict-profile follow-up](deepseek-review-report.md) and
[final authentication follow-up](deepseek-login-review-report.md). All findings
resolved; no pending review requests. Final authentication report supersedes the
earlier conclusion about forced API login. Reviewer identities/replacement
reasons are retained with the reports; no persistent team was configured.

Final live checks prove the system/workspace/native identities, healthy services,
five browser assets, byte-identical installed skills, active codex-lb provider,
owned tmux panes and same retained thread/cwd with eight saved turns. HTTPS verifies
against the configured public workspace CA and requires authentication (401).
The ambient curl trust store lacks that private CA; no TLS bypass was used.

## DeepSeek profile correction and local login recovery

Strict execution exposed two obsolete profile fields, then an unrelated forced
OpenAI API-login restriction. Native enforcement deleted the local ChatGPT
credential before selecting DeepSeek authentication. Parent restored it privately
from two identical retained operator backups; local login status passes. This
check should have been isolated first. No tokens were revoked or credential
values printed/committed. Remote ChatGPT refresh was not exercised.

The final profile removes all three settings and retains DeepSeek's required
DEEPSEEK_API_KEY, endpoint, model, effort and catalog. Synthetic before/after
execution proves credential preservation. A real isolated-home strict canary
returned CODEX_UPDATE_OK in 2.47 seconds with no copied login or shared-auth change.
Actual deployed-profile loading then preserved exact shared-auth bytes and stopped
at empty prompt before another request. See [provider evidence](deepseek-canary.json),
[synthetic preservation](deepseek-login-preservation.json),
[local recovery](local-login-recovery.json), and [live acceptance](live-acceptance.json).

## Deployment, recovery and ownership

All four deployment jobs and all four merge jobs succeeded. Reservation
0c72d37a-dcdd-44bc-bd4a-bc9f9a462505 is released (revision 7) for owner
c7fbd286-e060-419b-b538-6675336ab1ce on vpsfree:aitherdev. The coordinator freshly
verified exact remote integration, the independently reviewed patch_equivalent
workspace lineage, unchanged system/profile identities, and settled jobs/deliveries.
See [finish request](release-finish-request.json), [release receipt](release-result.json)
and [final status](release-status.json).

The pending Codex marker cleared through ordinary scheduled reconciliation.
Previous system/workspace generations and native roots remain retained; all owned
verification runners ended and the disposable state probe was cleaned. Preserve
journals, snapshots, logs and roots; no GC, archive, delete or session stop.
Detailed execution and rollback constraints are in [rollout.md](rollout.md),
[retention proof](postactivation-retention.json) and [history.md](history.md).
Original and intermediate release evidence remains frozen and checksummed.

## Repeatable skills and documentation

Invoke installed $update-codex. It routes workspace -> configuration's
update-aitherdev-codex -> runtime's update-dev-workspace-codex -> codex-web's
update-codex-web. The workspace/runtime/library skills are installed through the
profile; the host skill is repository-owned. Each repository owns its procedure.
Project package/operations guides and AGENTS routes are committed with the skills.
Accepted intent/design remain in plan.md and design.md; reusable failures and
fixes are in notes/dev-workspace/2026-10-16-codex-upgrade-verification.md.

## Next action

No remaining work or blockers. Use installed $update-codex for the next upgrade.
Keep the session and retained feature/recovery refs open; no archive, delete,
reboot or session stop was requested.

Session native anchor: 01a1450c-fb0c-7050-9438-501a9678a3c6. Portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-16-update-codex/

## Integration recovery

User instruction: "merge it and release aitherdev". All four repositories target
refs/heads/master. codex-web, dev-workspace and configuration merged unchanged
through individual coordinator jobs 0b3ceba8, 538d592c and c7d28e63. Workspace
was rebased from a158608e onto shared tracking master 7e923371 as 6bebd5ee; the
feature diff is byte-identical and both range-diff entries are equal. The final
comparison was captured and the refreshed feature published with an exact lease.

Automatic run 1ff62d7b stopped before any job submission: the installed pin
recipe's 256 KiB subprocess bound rejected the 10,836-path tracking archive
difference. Its journal and scratch sources are retained as failed preparation
evidence. Do not resume that original run; recovery uses ordinary exact-snapshot
commands. The retained Astra/xhigh reviewer accepted the exact workspace rebase for
normal patch_equivalent deployed lineage with no findings; see
[rebase review](workspace-rebase-review-report.md). No coordinator ledger or driver
journal was edited. Quick diff and deployment alignment checks passed; changed
workspace check derivations required fresh checks after review.

## Final integration verification

Retained reviewer 01a14598-96f1-7e92-9212-eb4912342792 (gpt-6-astra/xhigh,
read-only) accepted the workspace rebase under general/risk lanes with no
findings. Both original ordered patches/messages and the complete feature diff
are unchanged, no obsolete history or repeated update stream remains, and there
are no migrations. The installed deployment remains compatible; no redeployment
was required solely for the tracking/source-identity refresh.

Fresh `nix flake check --print-build-logs --no-update-lock-file` passed for
workspace 6bebd5ee in 299.4 seconds, including composed package verification.
Exact check derivations are retained in workspace-integration-derivations.json.
Codex-web master CI 38938901856 and runtime master CI 38938931839 passed;
configuration/workspace had no applicable runs. Parent monitored the workspace
checks while the single permitted utility watcher was occupied with runtime CI.
All owned commands/watchers have ended.

The large-tracking refresh limitation and successful ordinary-command recovery
are recorded in notes/dev-workspace/2026-10-16-integration-large-tracking-baseline.md.
Project skills and operations docs remain unchanged from their accepted final
implementation; this phase added integration/release evidence and an investigation
note only. Original acceptance/release artifacts remain frozen.
