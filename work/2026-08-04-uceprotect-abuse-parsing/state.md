# 2026-08-04-uceprotect-abuse-parsing

## Repositories

- `vpsadmin`
  - branch: `2026-08-04-uceprotect-abuse-parsing`
  - base/head: `1907e1990518548a421cf094893d0fa42ec904e2`
  - worktree during investigation:
    `worktrees/2026-08-04-uceprotect-abuse-parsing/vpsadmin`
  - source changes: none
- `vpsfree-cz-configuration`
  - branch: `2026-08-04-uceprotect-abuse-parsing`
  - base/head: `653dfc94ffb7da9d7b1f926986078c1a328436c8`
  - worktree during investigation:
    `worktrees/2026-08-04-uceprotect-abuse-parsing/vpsfree-cz-configuration`
  - source changes: none

## Status

Root cause identified with high confidence, pending direct confirmation of the
machine-generated classifier signal from the RT log or ticket's stored original
headers. The supplied message is
accepted by the current UCEPROTECT parser, but RT did not give Postfix an
envelope recipient for the parser mailbox. RT 4.4.6's default handling of
machine-generated mail explains the selective omission: such mail is sent only
to privileged RT users, while an unprivileged service-mailbox watcher is
filtered out. No production or project-repository change was made.

## Commands run

- Verified the active development session and inspected shared-workspace
  status.
- Created dedicated worktrees for `vpsadmin` and
  `vpsfree-cz-configuration` from current upstream `master`.
- Read both repository-local `AGENTS.md` files.
- Inspected the mail task, handler framework, MasterDC parser, parser routing,
  NixOS timer, production machine configuration, fixtures, specs, and history.
- Ran the focused MasterDC and routing specs in the configuration Nix shell.
  The first run failed because the test Gemfile does not declare Ruby 3.4's
  separately packaged `csv` gem. Re-ran with the already available Nix-store
  `csv` library on `RUBYLIB`; 7 examples passed. The reusable issue was already
  documented by another session in
  `notes/vpsfree-cz-configuration/2026-07-10-rspec-ruby34-csv.md`.
- Reproduced ticket 93961 in memory with the IP only in the Czech prose body;
  the router reported `processed: true` and produced one incident for
  `185.8.165.59` at the supplied message time.
- Attempted read-only `confctl ssh` access to `int.api1`; the current identity
  is not authorized. Used the accessible centralized log host instead.
- Correlated production `api1` mail runs around 2026-08-03 06:56:49 and
  searched its August log for ticket 93961, case 819217, the IP, UCEPROTECT,
  parser warnings, and processed/ignored messages.
- Searched current centralized logs across hosts for the exact ticket, case,
  and IP identifiers. Stopped the broad search after it reached unrelated
  high-volume router logs; no RT or mail-server log source is forwarded there.
- Inspected the full delivery headers of the personal RT notification. They
  prove delivery only to `jakub.skokan@havefun.cz`; the upstream Postfix queue
  ID is `52CE3FF23B` and the RT-host Postfix queue ID is `3DBED141DF`.
- Used the operator's read-only grep result from `prasiatko-mail`: queue
  `52CE3FF23B` has no delivery for the parser mailbox.
- Downloaded the official RT 4.4.6 release tarball, verified its published
  SHA-256 checksum, and traced the exact incoming-mail classifier and outgoing
  recipient filter.
- Searched all retained `api1` logs for initial MasterDC notifications. The
  retained history contains later human replies to MasterDC tickets, but no
  successfully processed initial MasterDC notification.

## Results

- `configs/vpsadmin/api/abuse_notice_parser/master_dc.rb` recognizes every
  subject containing `UCEPROTECT Monitoring Report`. If no CSV or subject IP
  exists, it extracts Czech `IP adresy 185.8.165.59` from the message body and
  uses the message date.
- The exact August shape succeeds locally even though, unlike the existing
  April fixture, its subject does not contain the IP.
- A parser mismatch cannot explain the absence of logs. An unidentified
  message would warn and then be logged as ignored; a missing assignment would
  warn `MasterDC UCEPROTECT: IP ... not found`; a successful parse would log a
  processed message. An exception would fail the systemd service.
- RT created ticket 93961 at 06:56:49. The `api1` mail timer ran successfully
  at 06:53:16 and 07:03:53, then continued approximately every 10 minutes.
  The 07:03 run completed normally in 3.1 seconds with no retrieved message and
  no parser output.
- Across the current August `api1` log, the only mail-task messages on the
  morning of August 3 were ticket 93964 at 08:28 (processed) and its comment at
  08:39 (ignored). This proves the timer, mailbox login, retrieval loop, and
  logging path were operating.
- Neither ticket 93961, case 819217, nor the UCEPROTECT subject appears in the
  `api1` log. Centralized logs contain later WebUI searches for
  `185.8.165.59`, but no evidence that the message reached vpsAdmin.
- The mail task polls only `INBOX` and `Junk`, fetches up to 10 oldest messages,
  and logs every returned message after dispatch. The evidence is therefore
  consistent with an upstream ingestion issue: RT did not send/deliver this
  notification to the configured mailbox, filtering filed it in another IMAP
  folder, or another client removed it before the next poll.
- The available central logger has no RT, MX, or IMAP server log source, so it
  cannot distinguish those three upstream cases.
- The supplied headers and the `prasiatko-mail` queue result now distinguish
  those cases: this was not an IMAP or downstream filtering failure. RT never
  submitted the parser mailbox as a recipient.
- RT 4.4.6 classifies incoming mail as machine-generated when it has, among
  other signals, `Precedence: bulk` or a non-`no` `Auto-Submitted` value. It
  stores `RT-DetectedAutoGenerated: true` on the transaction.
- RT 4.4.6 defaults `RedistributeAutoGeneratedMessages` to `privileged`.
  During notification, that setting removes every recipient whose RT user is
  not privileged and logs the exact reason. This matches a privileged human
  AdminCc receiving ticket 93961 while the service mailbox does not appear in
  Postfix at all.
- The upstream message came from MasterDC's RT 6.0.3. RT-generated mail uses
  `Precedence: bulk` by default, making this classification the expected path
  unless MasterDC overrides it. The original stored transaction header can
  confirm which classifier signal was present.
- The April prose-parser change for ticket 91270 used a synthetic fixture.
  Retained production logs contain only a later human reply to ticket 91270,
  not its initial MasterDC notification. The parser fix was correct but did
  not exercise or fix RT's earlier recipient filtering.
- The operator confirmed that the RT user for the parser mailbox is
  unprivileged. Under the current
  `RedistributeAutoGeneratedMessages = privileged` behavior, RT 4.4.6 has no
  narrower per-recipient eligibility check: this user is necessarily removed
  from machine-generated notification recipients.

## Open questions

- Inspect ticket 93961's stored original message for
  `RT-DetectedAutoGenerated`, `Precedence`, and `Auto-Submitted`, or grep the
  RT log for the outgoing message ID and the recipient-filter explanation.
- Choose an RT-side correction. The narrowest likely operational change is to
  make the dedicated service-mailbox RT user eligible for notifications;
  globally redistributing all machine-generated messages has a broader mail
  loop and bounce-amplification impact.

## Cleanup

- Removed both project worktrees, including the configuration shell's
  disposable dependency/cache content and untracked `.bin/` and `.bundle/`.
- Retained both unchanged initiative branches as required by workspace policy.
