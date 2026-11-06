# Mail task package: exact review evidence

Second package submitted for lead acceptance/independent review, no live DB or
email execution. Earlier accepted/deployed SSH task content and commit preserved.

## Revisions and inventory

Repository `vpsfree-maintenance-tasks`, canonical SSH origin
`git@github.com:vpsfreecz/vpsfree-maintenance-tasks.git`; same session branch and
worktree `worktrees/2026-11-05-disable-ssh-password-authentication/vpsfree-maintenance-tasks`.

- Package base: `2e7c9add2958e614a77e96236e92c55c8b22ad5c`.
- Final package head: `73165032bec0e2eb89e577b6ee3f799cf6449dd9`.
- Complete package series is one commit: `73165032bec0e2eb89e577b6ee3f799cf6449dd9`,
  `2026-11-05-mail-alpine-users-sshhole: prepare SSH security notice`.
- Complete branch range `2fdc9f2889ac419136cd0cde0e0955c015ae7107..73165032bec0e2eb89e577b6ee3f799cf6449dd9` has two commits:
  `2e7c9add2958e614a77e96236e92c55c8b22ad5c` (previously accepted/deployed SSH task), then this mail commit.
  The mail commit adds only its new directory; no amendment/rewrite of deployed
  task history. No obsolete/fixup commit or repeated dependency update stream.
- No migrations, schema changes, dependency pins or generated updates. Mail task
  has not been run/deployed/released here; no externally consumed migrations.
- Fresh fetch: master remains `2fdc9f2889ac419136cd0cde0e0955c015ae7107`; no rebase needed. Ordinary feature
  push succeeded; remote proof reported to lead. No repository CI workflows.
- Five files/298 added lines in `2026-11-05-mail-alpine-users-sshhole/`:
  executable `mail_alpine_users_sshhole.rb` (118), `run_log.rb` (47),
  exact lead `mail-cs.erb` (45)/`mail-en.erb` (46), `README.md` (42).
  One logical behavior includes its isolated parser, final templates and operator notes.
- [Package final diff](mail-implementation.diff); full branch diff remains
  directly inspectable with `git diff 2fdc9f2889ac419136cd0cde0e0955c015ae7107..73165032bec0e2eb89e577b6ee3f799cf6449dd9`.

## Final contract and provenance

Invocation from task directory: `./mail_alpine_users_sshhole.rb /path/to/run.log`.
Only trailing literal `execute` permits queueing; default renders recipients,
internal classifications and subject/body, prepares the conventional Custom
chain and raises before return to roll back. No recipients is a clear no-op.
All evidence and rendering are validated before any mail_custom preparation.

Active users/current active Alpine VPSes, with valid latest running status, are
intersected with explicit changed log entries plus exact operator-confirmed
manual fix/backup VPS 30231 requiring its failed `dozer/30231` record. All five
other failures, unchanged, incomplete, unlogged, pool mismatches and current
ineligible objects are excluded. ID plus current pool is available binding;
log cannot establish complete historical node/ownership mapping. No paid,
environment or mailer preference filters were added. Exactly one email/user.

The fixed manual exception and backup existence were explicitly confirmed by
the user through lead. This supersedes earlier all-failed eligibility and the
briefly proposed split-template variables; final implementation directly uses
`user:`/`changed_vpses:` only. Member copy has no failed-VPS prose. Latest lead
CS/EN templates copied exactly, bytes checked before commit; lead performed
required writing/humanizer and factual checks. Backup/key deployment/console
instructions are in those final templates. No private input path or log contents
are embedded in source/Git; sole manual ID is the expressly requested constant.

## Verification

- Both Ruby files: `ruby -c`, PASS.
- Real external attachment read with isolated parser only: 50 unique records,
  43 changed, 6 failed, 1 incomplete, 0 unchanged; no vpsadmin initialization.
- Full task with actual external log plus mocked empty DB: 44 candidate IDs,
  zero recipients/queued mail. This is not a claim of 44 actual recipients.
- `python3 work/2026-11-05-disable-ssh-password-authentication/mail_mock_checks.py`:
  prior six grouped standard-library tests PASS at `e652e5b5cf24553ec71c9f4807ae9d99ac534121`,
  3.9 seconds; final-head focused checks below, no permanent framework.
- Coverage: active/inactive owners and VPSes; current Alpine/running/status,
  missing/invalid status; logged/unlogged/unchanged/incomplete/five other failures;
  pool mismatch; exact manual record/current filters; one email/user;
  script-only/manual-only/mixed lists and backup wording; no failed member text;
  CS/EN/missing/unsupported-language fallback and localized access links.
- Parser: noisy explicit success, identical duplicates, conflicting pools/results,
  mismatching failure identity; ambiguity and invalid/unreadable arguments abort
  before API initialization. Render failure aborts before any preparation.
- Mock preview rolls back with empty queue; explicit execute only prepares mock
  records. [Synthetic rendered preview](mail-mock-preview.txt) records output and
  rollback/queue state; fixture IDs/logins are synthetic, not actual recipients.
- Staged/final whitespace checks PASS; committed tree clean; no declared hook
  framework/active hooks bypassed. Final template byte equality PASS.
- No live DB, mail, node or production connection; no integration build needed.
  Mock transaction proves control flow, not independent production DB behavior;
  architect supplied source evidence for ordinary Custom transaction rollback.

## Narrow review remediations F2/F3

Original reviewed mail range: `2e7c9add2958e614a77e96236e92c55c8b22ad5c..e652e5b5cf24553ec71c9f4807ae9d99ac534121`.
Final amended mail range: `2e7c9add2958e614a77e96236e92c55c8b22ad5c..858b18811c9363fe6c2fd875b224a813d8e360d4`; deployed SSH parent unchanged.
[Exact remediation diff](mail-remediation.diff), [range comparison](mail-range-diff.txt).
Only add `allow_empty` DSL after label and replace invalid direct `:pool`
preload with `dataset_in_pool: :pool`. No template/filter/parser changes.

Read canonical vpsAdmin `b4ef8535a629ee8c9cd753afecdb05e0895d0eea`:
`api/models/transaction_chain.rb` fire2 empty gate/destroy and allow_empty DSL;
`api/models/vps.rb` pool helper and belongs_to dataset_in_pool;
`api/models/dataset_in_pool.rb` belongs_to pool. Original mock omitted the empty
gate and accepted all includes, concealing these runtime defects. Corrected it
to model the real empty gate and reject nonexistent associations.

Final-head `ruby -c` PASS; three focused unittest methods PASS in 1.0 second:
`test_empty_chain_gate_and_successful_no_recipient_noop`,
`test_nonexistent_pool_association_is_rejected`,
`test_preview_rolls_back_and_execute_only_prepares`.
Nonempty log/no eligible DB rows succeeds in default/execute with empty chain
destroyed and no queue; fixture without allow_empty fails as real gate does;
fixture restoring invalid direct :pool preload raises before preparing mail.
Nonempty preview still rolls back and explicit execute only queues mock mail.
Earlier six-group parser/filter/template evidence retained for unchanged logic.
Synthetic preview refreshed at final head with corrected mock.

## Subsequent user copy corrections

Previously accepted mail range: `2e7c9add2958e614a77e96236e92c55c8b22ad5c..858b18811c9363fe6c2fd875b224a813d8e360d4`.
New committed range for affected copy-lane review: `2e7c9add2958e614a77e96236e92c55c8b22ad5c..8b90ad54f6c5450a207da89eb1d344582c372e84`.
[Copy-only diff](mail-copy.diff), [range comparison](mail-copy-range-diff.txt).
Only CS/EN templates changed. Recipient logic, parser, no-op/preload fixes,
README and deployed SSH parent/content are unchanged. Final task is 5 files,
298 lines, in one amended mail commit.

Exact latest lead-authored templates remove the existing-compromise sentence
and support-reply paragraphs, clarify the stored-password-hash condition, and
remove redundant outer nonempty guards while preserving loops. Recipient
selection already guarantees a nonempty confirmed-change list. Lead supplied
wording/factual verification; implementer copied exact bytes without redrafting.
Lead trimmed trailing spaces and wrapped prose before final copy.

Focused ERB/render checks at this head:
`test_preview_rolls_back_and_execute_only_prepares` and
`test_mixed_script_and_manual_single_email`, both PASS in 0.45 seconds.
Latest lead template byte equality PASS; unstaged/staged/final whitespace PASS.
Synthetic rendered preview refreshed at final head. Prior logic/mock evidence
remains applicable to unchanged Ruby/filter/parser sources; no live DB or sends.
Fresh fetch found master unchanged, no rebase; exact-lease feature-only force
push replaces only the prior mail head. Remote proof is reported to lead.

## Final user-requested tone adjustment

Previously accepted range `2e7c9add2958e614a77e96236e92c55c8b22ad5c..8b90ad54f6c5450a207da89eb1d344582c372e84`; latest range
`2e7c9add2958e614a77e96236e92c55c8b22ad5c..73165032bec0e2eb89e577b6ee3f799cf6449dd9`. [Exact tone-only diff](mail-tone.diff).
Copied latest lead templates byte for byte: CS recommends updating rather than
using the urgent imperative; English has the corresponding recommendation.
Only those CS/EN prose lines changed. No facts, filters, interface, source logic,
README or SSH-parent changes. Parent remains `2e7c9add2958e614a77e96236e92c55c8b22ad5c`.

Focused preview/render and mixed script/manual ERB tests PASS (2 tests, 0.46s),
exact lead template equality PASS, staged/final whitespace PASS, tree clean.
Fresh fetched master remains `2fdc9f2889ac419136cd0cde0e0955c015ae7107`, ancestor
of feature; no rebase required. Amended only mail commit, using exact feature
lease. Remote proof recorded in lead report. Prior final review retained under
user-requested narrow-fix direct verification; no reviewer rerun was requested.
No mail, live DB or merge execution.

## Review, limits and next dependency

High risk: security notice selection, member communications and mail queue
side effects. Proposed lanes: general, architecture/repetition,
scope/proportionality and risk/compatibility. Lead freshly verifies retained
reviewer0 gpt-6.1-sol/xhigh eligibility and assigns review; require whole-branch
history/no-migrations/no-repeated-stream conclusion, preserving prior SSH review.
Plan/state and architect-owned mail brief are alongside this evidence.

Uses current vpsAdmin models/Custom mail transactions; no schema/API/daemon
change or update ordering. Preview rolls back; repeat execute can send duplicates,
and sent mail is not undone by reverting source. Operator owns live preview and
sending after review. Implementation/index window released following publication;
implementer0 retains narrow-fix ownership and accepts no new package yet.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-05-disable-ssh-password-authentication/)
