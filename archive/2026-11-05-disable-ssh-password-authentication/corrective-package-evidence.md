# Coupled corrective package: final review packet

All intended source/docs/checks committed and published; no node, database or
mail operation, deployment or default-branch integration was performed.

## Exact scope and history

Repository `vpsfree-maintenance-tasks`, canonical SSH origin
`git@github.com:vpsfreecz/vpsfree-maintenance-tasks.git`; registered branch
`2026-11-05-disable-ssh-password-authentication`, clean worktree at
`worktrees/2026-11-05-disable-ssh-password-authentication/vpsfree-maintenance-tasks`.

Complete final range: `2fdc9f2889ac419136cd0cde0e0955c015ae7107..abe485966b7b974365c1f1488a9be9d8e1fafb8c`:

1. `2e7c9add2958e614a77e96236e92c55c8b22ad5c` — original SSH workaround, EXACT operator-run recovery reference retained.
2. `33ef61ff6def3018d3554b734f7b01d14d11c804` — native policy/no-op guard, fixed read-only backup report, real-parser tests/docs.
3. `abe485966b7b974365c1f1488a9be9d8e1fafb8c` — one final mail task introducing positive original-backup eligibility directly.

[Full branch final diff](corrective-full-branch.diff),
[correction relative to original SSH](corrective-final.diff),
[history comparison](corrective-history-range-diff.txt).
No migrations, schemas, dependency/input pin updates or repeated generated streams.

Original mail head `73165032bec0e2eb89e577b6ee3f799cf6449dd9` and its follow-up
consumer commit were published feature history only. They were never
run/deployed/released here; no external consumer is recorded. Lead explicitly
directed consolidation because publication alone was no supported boundary.
The obsolete old-log-only mail rule is removed from final commit history. This
supersedes the earlier provisional direction to preserve that mail commit.
Retaining the original SSH commit is required by operator-run recovery, not
merely its publication. Independent review must assess this rationale and the
whole three-commit history, with explicit no-migrations/no-repeated-stream conclusions.

Before rewriting, ordinary push effects were reconciled and exact remote feature
`24625cd142a05005d80b76e80ee4f9c5af36b087` saved as the force lease. Local backup ref
`2026-11-05-disable-ssh-password-authentication-before-history-consolidation-24625cd` retains that complete old graph and all old mail commits.
The construction ref `2026-11-05-disable-ssh-password-authentication-consolidated`
is retained at the new head. No refs were deleted. Original tested range was
`2fdc9f2889ac419136cd0cde0e0955c015ae7107..24625cd142a05005d80b76e80ee4f9c5af36b087`; final range is above.

Tested pre-consolidation tree and final tree both equal
`cff6abfcf1fc61892b091d70b91fc49ca8b78ff7`. Every task source blob and actual file SHA-256
matches. Producer SSH subtree is also unchanged. Rebuilt history contains no
source behavior changes. Fresh fetch found remote master unchanged at the base;
exact-lease feature push and fresh remote proof confirm final `abe485966b7b974365c1f1488a9be9d8e1fafb8c`.
Worktree is back on the registered feature branch and matches origin; portal
registration still names that same branch. No master mutation or merge claim.

## Requested outcome and bounded contract

The guest shares one classifier for live config and original backup: native
`sshd -T -f`, case-insensitive dump keyword, and the first PasswordAuthentication
value per Match block. Consistent no/absent values prove disabled; consistent
yes/absent values prove enabled; mixed/unrecognized/parser-failed cases are
unknown. Global/default yes plus native Match-all no is preserved. No Match
predicate/overlap engine or recursive Include rewriting.

Disabled: existing unchanged terminal, exact bytes/core metadata preserved, no
backup creation or service restart. Unknown: visible failure, no mutation.
Enabled: existing candidate validation, metadata/original backup, changed-only
restart and recovery. Accepted empty-default Include boundary remains; populated,
unusable or other Includes refuse. Copy matching host wrapper and guest payload
together; mixed historical script pairs are not supported.

Read-only host `--report-backup` passes fixed `report-backup` guest argument and
emits exactly version/node/pool/ID/policy/hash TSV rows for all running Alpine
targets. It only classifies the exact first backup, hashes readable bytes and
detects changes across reads. Unknown rows remain complete and make exit nonzero;
stdout contains rows, diagnostics stderr. No config, backup or service action.

Mail interface: `mail_alpine_users_sshhole.rb LOGFILE BACKUP_REPORT [execute]`.
Strict report grammar/enum/identity/hash and duplicate conflict checks precede
API initialization/chain preparation. Old log-changed VPSes need enabled report
policy and current node/pool identity matching; disabled/unknown/missing/mismatched
proof excludes them. Exact manually fixed dozer/30231 remains the user-confirmed
fix+backup exception, requiring failed-log evidence and all current eligibility
checks; other failures excluded. One email/active owner, current active/running
valid-status Alpine only, same localized member templates and preview rollback.
No blanket eligibility from the old 43 changed records remains. No actual report
or current recipient count was generated here.

## Checks and input identities

- [Verification/input receipt](corrective-verification-inputs.json) binds tested
  head `24625cd142a05005d80b76e80ee4f9c5af36b087`, final tree/source blobs/SHA-256, fixture checksum and tool paths.
  It records tool identities after consolidation for reproduction; this package
  made no source, package or environment changes between testing and reconstruction.
- `python3 2026-11-05-disable-ssh-password-authentication/test_password_authentication.py`:
  6 grouped tests PASS, 7.85s. Real OpenSSH 10.5p1, temporary host key/configs,
  native -T and representative -C; no daemon/listener. Committed task-local tests.
- Preservation cases: no away from first line; whitespace/case/quoted bool;
  first global no then ignored yes; duplicate no; Match first no then ignored yes;
  global/default yes plus Match all no. Assert bytes/core metadata unchanged,
  no backup/restart, existing backup retained. Mixed Match enabling and parser
  failure refuse untouched; ordinary explicit/default yes mutates correctly.
- Validation failure and restart recovery/inode independence retained. Read-only
  reports cover enabled/disabled/mixed, exact hashes, missing/directory/symlink
  backup unknown, concurrently changed backup unknown, host rows for every target
  including guest inspection failure, no service action.
- `python3 work/2026-11-05-disable-ssh-password-authentication/mail_mock_checks.py`:
  11 grouped tests PASS, 7.49s. Positive enabled inclusion, disabled/unknown/missing
  exclusion, node/pool mismatches, malformed/conflicting rows before API,
  identical duplicate coalescing, manual exception regardless report policy,
  all current filters/one mail per owner, CS/EN/fallback, preview rollback,
  empty-chain gate, invalid association rejection and render failure pre-preparation.
- History-only final checks: host Bash/guest sh syntax and three Ruby syntax
  checks PASS; full-branch whitespace PASS; clean tree. Earlier full checks reuse
  the exact unchanged sources/fixtures; no redundant full test repeat.
- No declared hook framework or active hooks bypassed. Commit messages used temp
  files. No private raw logs/reports or derived actual recipient lists in Git.

## Documentation, compatibility and review

Both task READMEs now describe classification/refusal, report collection and
concatenation outside Git, positive mail evidence, identity/unknown bounds,
preview/execute and recovery. Member templates are unchanged from the last
accepted lead-authored wording. The new mail input is intentionally required;
old log-only invocations fail before queueing. Current status/report cannot prove
historical ownership. Report hashes identify observed bytes, with operator-owned
collection/provenance; no signing framework or guessed node map.

No schema/API/daemon or fleet configuration change. Operational order: update
matching SSH scripts, collect/review external backup reports from relevant nodes,
then preview mail with both inputs. Queued/sent mail is not reversible and repeat
execute can duplicate mail; no sending here. Live Alpine/BusyBox/OpenRC, osctl and
production DB behavior remain unexecuted gaps; real OpenSSH parser is local,
transport/services/ORM/mail are mocked. Unknown proof fails safely.

High risk: SSH auth policy, node-local file/restart handling, operational TSV
contract and member mail side effects. Lead assigned retained reviewer0 with
saved gpt-6.1-sol/xhigh, all four lanes: general, architecture/repetition,
scope/proportionality, risk/compatibility. Review exact final range and retained
recovery boundary independently. Lead owns acceptance, state and integration
approval. No lifecycle action is requested; session stays open.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-05-disable-ssh-password-authentication/)
