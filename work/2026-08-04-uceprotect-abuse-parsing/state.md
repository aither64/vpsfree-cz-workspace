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

Investigation complete. The supplied message is accepted by the current
UCEPROTECT parser. Production evidence shows that it was not returned by the
IMAP retrieval loop, so there was no parser attempt to log. No production or
project-repository change was made.

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

## Open questions

- Obtain the original raw `.eml` including envelope/outer headers such as
  `Delivered-To`, `Received`, spam-filter headers, and the actual recipient.
- Inspect RT outbound delivery and MX/IMAP delivery/folder logs for ticket
  93961 between 06:56 and 07:04. These systems are legacy/external to the
  configuration inventory and are not present in centralized logs available to
  this session.
- Check whether the configured IMAP account has server-side folders other than
  `INBOX` and `Junk` (for example `Spam`) and whether another client consumes
  that account.

## Cleanup

- Removed both project worktrees, including the configuration shell's
  disposable dependency/cache content and untracked `.bin/` and `.bundle/`.
- Retained both unchanged initiative branches as required by workspace policy.
