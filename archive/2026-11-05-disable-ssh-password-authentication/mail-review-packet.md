# Alpine member notice: final review

## Narrow review remediation: final head 858b188

Published final head now `858b18811c9363fe6c2fd875b224a813d8e360d4`, replacing
reviewed mail head e652e5b, same base/unchanged SSH parent. Reviewer F2 Important
requested allow_empty for empty chains; F3 Blocking requested actual nested
dataset_in_pool: :pool preload. Implementer made exactly these two source hunks,
folded into mail commit. Lead inspected complete old/new diff, no new design,
scope or copy changes. Corrected fixture models actual empty gate and rejects
nonexistent associations; three focused cases pass (~1s), including old variants
failing and zero-recipient preview/execute successful/noqueue, original nonempty
preview/execute behavior. Ruby syntax, final whitespace and clean tree pass.
New task 5 files/306 lines. Step9 direct requested-fix verification applies;
original independent review continues to whole-branch conclusion.

Final head `e652e5b5cf24553ec71c9f4807ae9d99ac534121`.
Full base `2fdc9f2889ac419136cd0cde0e0955c015ae7107`.
Repository/worktree: `worktrees/2026-11-05-disable-ssh-password-authentication/vpsfree-maintenance-tasks`.
Target master, no integration approval. All intended source/docs/templates committed,
clean tree, quick checks pass. High risk: security communication/recipient selection,
persisted mail preparation and irreversible sends. General, architecture/repetition,
scope/proportionality and risk/compatibility lanes apply. Reviewer0 retained
read_only, gpt-6.1-sol/xhigh, thread 01a1ac18-8de0-7551-9d54-4498d1ffd8cd,
verified live roster; no overrides/fallback/nested reviewer.

## Scope and latest user decisions

Another dated task modeled after existing mail scripts. Only active users owning
currently active/running Alpine VPS matching confirmed mitigation evidence.
Original log: 50 records, 43 changed, six failed Include, zero unchanged, one
incomplete. User then checked all six failures: only30231 had password auth enabled,
user fixed it, confirmed backup exists, and said to treat it as the others.
Final candidate evidence =43 explicit changed records plus manually fixed30231
when its failed dozer record is present. Other five failures excluded entirely.
Current available+running status/Alpine/active owner+VPS/pool matching applies to all,
including30231. No current recipient count known; no live DB operation authorized.
Incomplete, unchanged, unlogged, stopped, non-Alpine, invalid/missing status and
inactive-owner VPS are excluded. One email per user, CS/EN plus English fallback.
No general override/parser/mail framework or persisted send dedup.

Prepare only; no email sending or real DB execution. Runtime log is external,
never copied/embedded into Git. An exact small operator-confirmed ID constant is
intended; no raw uploaded log or derived recipient manifest is committed.
Default mode follows existing Custom-chain rollback preview; only literal execute
can queue. Parse all evidence and render all messages before any mail_custom call.
Preview prints recipients and actual subject/body, then raises before transaction
commit. An operator can later choose execute; duplicate sends on rerun documented.

## Copy and sources

Lead wrote and directly applied vpsfree-user-facing-writing/humanizers to latest
mail-cs.erb/mail-en.erb in tracking. Repository copies must match those exact files.
Vars user:/changed_vpses:, including operator-confirmed30231+backup. Simple conditional
PasswordAuthentication-disabled statement; no failed-VPS discussion. User requested
precautionary framing: VPS may have had no vulnerable account; no compromise claim.
Explain exact '*' password field/no usable password, another account with a real
password, enabled SSH password authentication and OpenSSH without PAM. Do not claim
unknown package cause or blanket safe defaults. Recommend system/OpenSSH update,
sshd restart and log inspection; public-key upload PLUS deployment to an existing
running VPS and console access, with localized KB links. Original backup path and
restoration implication included. See mail-writing-evidence.md for primary sources.

## Complete branch history and final diff

- 2e7c9add2958e614a77e96236e92c55c8b22ad5c:
  2026-11-05-disable-ssh-password-authentication: add Alpine workaround
- e652e5b5cf24553ec71c9f4807ae9d99ac534121:
  2026-11-05-mail-alpine-users-sshhole: prepare SSH security notice

Full diff: git diff BASE..HEAD (8 files/451 added lines).
New task diff: git diff 2e7c9ad..HEAD (5 files/305 added lines: Ruby entry117,
parser47, CS49, EN50, README42). Single separate coherent mail commit includes its
supporting templates/docs. Prior SSH directory and commit remain unchanged; user
provided node execution transcript, without exact deployed-revision proof. Do not
rewrite it. Reuse existing SSH-content final review in review.md, but independently
conclude on complete branch history and new task. No obsolete branch iterations,
fixups, transitional paths, migrations or repeated dependency/input/generated streams
remain. No new schemas/APIs/daemon/module changes. Prior old c4eb218 is review provenance
only, outside final branch series. No live DB/mail run or release of new task.

## Verification

- Ruby syntax for both source files passes; full diff whitespace passes.
- Six grouped isolated mocked checks pass (~3.9 seconds); harness mail_mock_checks.py.
- External attachment parsed read-only WITHOUT vpsadmin initialization: 50 records,
  correct outcomes; script in mock empty DB proves44 candidates.
- Selection tests active/inactive users/VPS; running/stopped/missing/unavailable
  status; Alpine/non-Alpine; pool mismatch; logged/unlogged/unchanged/incomplete;
  other failures excluded; manual30231 requires exact failed dozer evidence and all
  current filters; multiple VPS one email; CS/EN/fallback.
- Rendering tests manual-only and combined change/backup statement, no failure prose,
  latest template bytes; preview rollback/no queued mail; explicit execute mocked
  preparation only; parser ambiguity and invalid args before API init; render failure
  before mail preparation; noisy success and repeated/conflicting evidence.
- Synthetic rendered preview: mail-mock-preview.txt. No live DB or mail execution.
- No repository hooks/environment/global build/CI workflows declared.

Read applicable repository/workspace instructions and mandatory-review skill plus
all four references. Review directly, read-only; report through report_to_lead for
lead persistence. Inspect actual query/chain contracts in canonical vpsadmin at
b4ef8535a629ee8c9cd753afecdb05e0895d0eea as needed; architect evidence/design.md
names source paths. Require explicit whole-branch history/migration/repeated-stream
conclusion. Scope first: this is a one-off task, preserve necessary safety without
optional frameworks. Advisory review does not authorize sending/integration.
