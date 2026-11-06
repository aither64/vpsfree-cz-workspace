# Corrective SSH/no-op and mail-evidence review

## Final committed inventory and check results

Final head: abe485966b7b974365c1f1488a9be9d8e1fafb8c.
Complete series from base2fdc9f2889ac419136cd0cde0e0955c015ae7107:

1. 2e7c9add2958e614a77e96236e92c55c8b22ad5c — original SSH task retained exactly
   as operational recovery reference (user ran earlier task; exact deployed SHA
   not established). This is a supported operation boundary, not gratuitous history.
2. 33ef61ff6def3018d3554b734f7b01d14d11c804 — preserve disabled configs and
   produce read-only original-backup report with native-policy regression checks.
3. abe485966b7b974365c1f1488a9be9d8e1fafb8c — final mail task with verified
   original-enabled evidence required from its first introduction.

Unapplied/unrun old mail7316503 was consolidated with corrective consumer24625cd;
its intermediate old-log-only behavior is absent from final series. Prior snapshot
24625cd and old ranges retained in local backup ref/evidence. Exact final tree
equals tested pre-consolidation24625cd (lead independently git-diff proved empty),
same source/test/doc inputs; only commit ordering/messages/parents changed. Full
diff is git diff BASE..HEAD: ten files/893 insertions. No migrations or repeated
dependency/generated streams. Whole-branch consolidation conclusion required.

All intended source/docs committed, clean tree and full whitespace pass. Checks:
6 permanent real OpenSSH10.5p1-backed groups (7.85s), task-local
test_password_authentication.py. Temporary HostKey/config, no daemon/listener;
disabled-byte/core-metadata preservation, no backup/restart, native duplicate and
Match-all behavior, unknown/parse failure no mutation, enabled/recovery, report
hash/read-only/missing/bad/symlink/concurrent-byte/transport/TSV cases. 11 updated
report-gated mail mock groups (7.49s), session harness: enabled inclusion;
disabled/unknown/missing/malformed/conflicting/identity-mismatched exclusion;
manual30231/current filters/one-per-owner, default rollback/execute gate and real
empty-chain/association contracts retained. Shell/Ruby syntax and staged/final
whitespace pass. No actual node report, live DB, node mutation or mail run.
Templates byte-unchanged from prior approved final wording.

Same reviewer0 live identity verified, read_only/gpt-6.1-sol/xhigh, no overrides.
All four lanes for this correction. Read actual final source and complete series;
reuse unchanged member copy with identity proof. No nested review or live actions.

User found the original SSH task rewrote already-disabled configurations because
it always prepended no, removed prior directives and compared bytes. This also
made historical changed logs unsuitable for affected-only mail. User explicitly
requested correcting BOTH node script and mail recipient selection from originals.

Existing published head before correction: 73165032bec0e2eb89e577b6ee3f799cf6449dd9.
Full base: 2fdc9f2889ac419136cd0cde0e0955c015ae7107.
Worktree: worktrees/2026-11-05-disable-ssh-password-authentication/vpsfree-maintenance-tasks.
Final correction head/series/diff/check evidence: pending implementation.
Retain prior SSH2e7c9ad and mail7316503 commits; user executed an earlier task
revision without exact deployed-SHA evidence. No rebase/rewrite of those references.
Correction commits must have one logical purpose and retain original backup contract.

Accepted design: Corrective package section in design.md. One bounded shared guest
classifier uses native sshd -T, case-insensitive output, plus conservative first
PasswordAuthentication-per-Match proof. Uniform no => disabled; uniform yes =>
enabled; mixed/unsupported => unknown. No full Match predicate engine. Native
Match all no works; unknown means no writes/backup/service action. Disabled must
preserve bytes/metadata and backup/service state regardless of formatting/location,
global duplicate precedence or valid all-Match-no forms. Native parsing errors
must not become enabled. Existing Include unsupported boundary retained.

Read-only original-backup report reuses classifier, not current-file fallback.
Fixed TSV version/node/pool/ID/policy/hash report, no credentials/raw configs;
missing/unreadable/unstable/ambiguous originals unknown. Original input/report stays
outside Git; no live node/DB/mail run. Mail now requires report input before API
initialization and positive enabled original evidence for old changed IDs, with
node/pool/current active+running Alpine binding. Disabled/missing/unknown excludes.
Preserve exact operator-confirmed manual30231 exception and existing source-log
failed-dozer evidence/current filters. Other five failures remain excluded.
No current recipient count claimed. Real report collection/live preview remain
operator steps, not performed during development.

No member-facing copy changes requested; templates must remain byte-unchanged.
One implementer owns source/checks/docs/commits; no generalized parser/mail framework,
deployment, API/schema/module changes, migrations or dependency streams.

Verification must include real OpenSSH parser fixtures on temporary configs/keys,
no daemon/listener, plus no-op/backup/restart/recovery control flow and fixed report
wire/input validation/eligibility checks. Original mock-only tests missed semantics;
do not accept a test merely mirroring the candidate rewrite. Cases in design.md.

High risk: SSH policy, persisted guest configs, source evidence/recipient selection,
irreversible mail. Same retained reviewer0 gpt-6.1-sol/xhigh/read_only after fresh
roster verification; all four mandatory-review lanes. Review complete branch series,
final diff and migration/update inventory; reuse unaffected prior material with
identity proof, independently assess corrective behavior. Read mandatory-change-review
and lane references, no nested agents, report to lead for persistence. Scope first,
no optional hardening. Explicit history/no-migrations/no-stream conclusion required.
