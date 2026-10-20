# Post-review verification brief

Do not launch until independent final review is accepted and required fixes pass
focused verification. Deployment/activation/restarts/default-branch integration
are excluded. Fresh gpt-6-luna/low utility with pinned catalog/native config and
full_access execution; not a roster member. Read dev-session-monitor/SKILL.md.

## Tested revisions

Bot 49a8ff8086b7b325f9f1a8f4825619f8e03245ce; configuration final refreshed
head e30cd3399c5f57fd792afa4147d293307227d9b4 above a2ad6da4 after
mechanical repin and clean patch-equivalent rebase. Lead inspected the
review-requested narrow bootstrap/YAML fix and passing regression checks.
Do not use superseded original bot/config heads for new verification.
Both branches use 2026-10-19-security-advisory-notifications.

## Authorized local checks

1. Bot worktree:
   `./test-runner.sh test vpsadmin-events`
2. Configuration worktree:
   `nix develop -c confctl build --yes 'cz.vpsfree/containers/int.vpsfbot'`

Commands are from the respective implementers and repository guidance. VM test
retains existing networking and individual coverage; summary uses a minute test
interval and two-second polling. Full container build performs no activation.
Preserve exact exit statuses and complete logs under this session. Track the
runner's output/state paths, any owned guests/processes and produced derivation.
No arbitrary quiet-build timeout. Stop an unexpected local Linux kernel build
and report the exact derivation/log evidence per workspace verification policy;
this authorizes cancelling only the owned verification command/process tree.
Do not cancel unrelated tasks, edit, diagnose, retry, deploy or launch nested agents.
Return failure evidence promptly and retain ownership of any still-running run.

## Exact automatic CI

Bot head 49a8ff8 auto-created RSpec 39317498639 and Integration Tests 39317498503.
Old integration 39315420422 was cancelled as superseded; old RSpec 39315420448
completed success. Do not wait on superseded runs.
Use gh through repo Nix shell if necessary; inspect these exact IDs/head, not a
moving branch. No manual workflow dispatch. Collect failed logs/artifact paths
without rerunning; parent routes diagnosis to package owner. Do not infer that a
queued workflow passed. No CI cancellation except superseded runs after a fix
push, verified exact old SHA and same branch; parent will explicitly coordinate.

## Return evidence

Report passed/failed/incomplete, tested exact revisions, commands/run IDs,
elapsed time, full log/status paths, bounded error excerpt and any remaining
owned process/runner. No acceptance decisions. Lead owns results and next steps.
