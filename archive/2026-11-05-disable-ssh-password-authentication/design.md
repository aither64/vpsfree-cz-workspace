# Disable SSH password authentication on running Alpine containers

Architect: architect0. Implementation owner: implementer0. Lead accepted this
bounded brief for release. Accepted review correction allows only the ordinary
default Include with no matching snippets; later user steering requires
`ct runscript` and a separate guest payload. No deployment is included.

## Package and scope

One implementation package owns only
`vpsfree-maintenance-tasks/2026-11-05-disable-ssh-password-authentication/`:
executable host wrapper `disable_ssh_password_authentication.sh`, POSIX shell
guest payload `disable_ssh_password_authentication_in_container.sh`, and a short
`README.md`.
Small mocked checks may live there if useful; no new framework is needed.
The lead owns tracking, acceptance, independent review and publication.
Architect0 owns this design only; direct technical clarification is available
between architect0 and implementer0. No other package or file dependency remains.

Run manually as root on a vpsAdminOS node. Use a Bash host wrapper and a POSIX
shell payload inside each running Alpine container. Enumerate with
`osctl ct ls -H -o pool,id --distribution alpine --state running`.
Check enumeration exit status before iterating. Keep pool and ID together and
invoke `osctl --pool "$pool" ct runscript "$id" "$payload" </dev/null`.
Resolve the absolute companion payload path from the wrapper's `BASH_SOURCE`
directory, so invocation is independent of the current directory. Require the
payload to be readable before iterating; it starts with `#!/bin/sh` and stays in
the same task directory. Copy both scripts to the node. The CLI resolves the
host file's real path; osctld copies it to a temporary executable in the guest,
attaches to the running container, executes the shebang script, propagates its
exit status and removes that temporary copy. No `-r` or `-n` flags are used.
Do not start stopped containers. Process sequentially, identify each result by
pool/ID, continue after per-container failures and return nonzero if any failed.
An empty successful list is a successful no-op.

## Configuration and recovery invariants

- Target `/etc/ssh/sshd_config` only. Require an existing regular non-symlink
  file and available `sshd` and Alpine `rc-service` before editing.
- Generate a temporary candidate beside the original. Put one global
  `PasswordAuthentication no` first, then preserve the original content except
  active PasswordAuthentication directives, which are removed throughout the
  main file, including every Match block. Match keywords case-insensitively,
  with leading whitespace and whitespace or `=` separators supported. Leave
  comments and unrelated settings alone. The transformation must be idempotent.
- This small task does not recursively rewrite Include files. Permit only the
  ordinary two-token `Include /etc/ssh/sshd_config.d/*.conf` directive when its
  glob has no matches. Allow leading/trailing whitespace, whitespace between the
  tokens and case variation in the keyword; keep the path case-sensitive and
  literal. Preserve permitted lines unchanged, including repeated occurrences.
  Other active forms (additional patterns, quoting, `=` or trailing comments)
  remain unsupported without mutation; do not add a general parser.
  Check the literal default glob inside the guest. Every match is unsupported,
  including a dangling symlink, directory or literal `*.conf` entry: testing
  both existence and symlink status distinguishes no expansion from such names.
  Accept an absent snippet directory, or a readable/searchable directory with
  no matches; an unusable directory path is not evidence of emptiness. Report all
  unsupported cases with nonzero per-container status and no mutation. Included
  Match rules can override the global setting, so refusing populated includes
  is a deliberate coverage limit, not a claim of protection. The allowed Include
  remains live: adding snippets later can change policy and needs reassessment.
- If candidate bytes equal the original, report unchanged and do not back up,
  replace or restart. Otherwise validate the candidate with `sshd -t -f` before
  modifying the live file. A failed validation leaves it untouched.
- Before the first live modification, preserve the original as
  `/etc/ssh/sshd_config.before-2026-11-05-disable-password-authentication` using
  metadata-preserving copy. Never overwrite an existing backup on reruns;
  reject an unusable backup path. A failed backup prevents live modification.
- Preserve ownership and permissions when installing the candidate. Prefer a
  same-directory rename after copying metadata. Retain an immediate pre-change
  copy for recovery on a later run; the persistent first backup is not necessarily
  the immediately preceding configuration.
- Restart with `rc-service sshd restart` only after the live bytes changed and
  validation passed. On restart failure, restore the immediate pre-change file
  and attempt service recovery once, report failure even if recovery succeeds,
  and retain the persistent original backup. Do not promise atomicity across
  process termination, filesystem failure or concurrent configuration writers.

README: invocation on a node, running-Alpine restriction, changed-only restart,
backup path, nonzero/partial-failure meaning, empty-default Include support and
unsupported populated/other Include/custom service
configuration, and manual recovery by restoring the backup, validating with
`sshd -t`, then restarting sshd. Restoration re-enables the original password
policy and must be a conscious operator action. No production execution here.

## Compatibility and acceptance

Use ordinary Alpine BusyBox tools, OpenSSH and OpenRC; no added guest packages.
This changes only SSH password authentication policy. Do not change
keyboard-interactive authentication, PAM, packages or host configuration.
Key authentication settings remain untouched; existing AuthenticationMethods
requirements may make logins unavailable when they require passwords.
There are no database, API, protocol, schema or configuration-module changes.
Each container is independent; no fleet-wide coordinated upgrade is required.
The original configuration remains available for rollback. Containers without
sshd/configuration and containers that stop during execution must be clearly
reported without creating configuration or claiming mitigation.

Acceptance: correct pool-qualified target selection; all active main-file
PasswordAuthentication rules removed and an explicit global no present; original
saved before first mutation and preserved on reruns; valid changed files restart
once; unchanged files do not restart; errors remain visible and do not stop work
on subsequent selected containers.

## Quick checks and delivery evidence

Use Bash syntax checking for the wrapper and POSIX shell checking for the guest
payload. Run small,
safe mocked osctl/service/sshd checks, never the live host paths. Cover: running
Alpine filter and same IDs in distinct pools; no matches and enumeration failure;
commented/absent, mixed-case, duplicate and Match-scoped directives; unchanged
second run; first backup byte equality and preservation after a later change;
validation/backup failure without mutation or restart; restart failure with
restoration; empty default Include succeeds and is preserved, populated default
Include (including a dangling symlink) and other Include forms are refused;
one guest failure followed by another guest succeeding. Mock `ct runscript`
must receive the correct pool/ID and absolute companion path, read and execute
the actual guest payload, preserve its failure status, and work from another
current directory. Record commands/results and known gaps. No long build
or live deployment check is needed for this task; independent final review follows
committed deliverable and successful quick checks.

Implementer reports exact base/head, changed files, checks, gaps and history
provenance (no migrations) to lead. Base supplied by lead is `2fdc9f2`.

## Evidence

Repository README and existing Arch/Fedora maintenance scripts establish dated
task directories and shell payload conventions. Canonical vpsAdminOS source
at `49636f902704ce6019a7a8ae47ec0b3ca6902f68`,
`osctl/lib/osctl/cli/app.rb` and `container.rb`, exposes distribution/state
filters, pool/id output, global pool selection, and runscript host-file resolution
and exit-status forwarding. `osctl/man/man8/osctl.8.md` documents
`ct runscript [options] ctid script|- [arguments...]`; omitting `-r` does not start
stopped containers. `osctld/lib/osctld/commands/container/runscript.rb` explicitly
rejects stopped containers without that flag, and
`osctld/lib/osctld/container_control/commands/runscript.rb` copies the host file
into the container, sets mode 0500, executes it and removes the temporary copy.
This is source evidence, not a live-node execution check.
[OpenSSH sshd_config manual](https://man.openbsd.org/sshd_config) documents
case-insensitive keywords, first-value precedence and Match/Include behavior.
No advisory interpretation is needed to implement the user-requested setting.

Bounded Alpine image-default follow-up: at the same vpsAdminOS revision,
`image-scripts/images/alpine/config.sh` installs `openssh`, and
`image-scripts/include/alpine.sh:165-169` rewrites PasswordAuthentication and
PermitRootLogin to yes in the package-provided sshd_config. The image scripts do
not insert/remove Include or provide a complete sshd_config. Repository evidence
alone cannot establish whether deployed Alpine package defaults contain an
active Include. Subsequent review supplied the official
[Alpine 3.22 OpenSSH patch](https://raw.githubusercontent.com/alpinelinux/aports/3.22-stable/main/openssh/include-config-dir.patch),
independently read for this correction: it adds the active default
`Include /etc/ssh/sshd_config.d/*.conf` line. This invalidates blanket Include
refusal as a useful ordinary-Alpine boundary and motivates the narrow empty-glob
exception above. No deployed sample was inspected. The empty-glob exception
does not require interpreting or modifying any included configuration.

## Mail task: sufficient implementation brief

Architect0 owns this section; implementer0 owns the entire new directory
`2026-11-05-mail-alpine-users-sshhole/` in vpsfree-maintenance-tasks: one Ruby
Custom task, the two lead-provided templates (if kept separate), README and
small focused mocked checks. The earlier SSH task stays unchanged. Lead owns
acceptance and final member-facing wording; use the latest session
`mail-cs.erb` and `mail-en.erb` exactly. No live DB run or email send is authorized.
Relevant contracts are settled; the package is ready for lead release.

### Runtime interface and eligibility

Use the repository's `vpsadmin-api-ruby` shebang, require `vpsadmin`, initialize
plugins with `VpsAdmin::API.default`, and redefine
`TransactionChains::Maintenance::Custom`. Suggested entry point:
`mail_alpine_users_sshhole.rb LOGFILE [execute]`. The required log is an external
runtime path, not embedded content or a tracked derived recipient/status list.
Reject unreadable/missing input and invalid arguments before firing the chain.

Select active users and their active VPSes with joins on `:os_template` and
`:vps_current_status`, where distribution is `alpine` and
`vps_current_statuses: { status: true, is_running: true }`. This is the latest
reported status, not a fresh node probe; absent/invalid status is excluded.
Intersect that set with explicit `changed` outcomes from the log, plus exact
operator-confirmed manually fixed VPS ID `30231`. Represent that sole exception
with a simple fixed ID constant; it must match an explicit failed record in the
supplied log (`dozer/30231`), not create eligibility for an unlogged ID. The user
confirmed that VPS 30231 also has the original configuration backup, so it joins
the ordinary confirmed-change list and backup statement. All other failed IDs
are excluded: user inspection established they do not need this mail. There are
44 candidate IDs before current active/running/Alpine/pool filtering, not 44
proven recipients. Do not add configurable overrides or a general exception
framework. Do not select unlogged, unchanged-only or incomplete-only VPSes/users. No new
paid-account, environment or mailer-enabled filter was requested: use only
active user state and this VPS intersection. Group by user and prepare exactly
one email per user, ordered deterministically. Do not add a persistent dedup
system; document that executing again can queue duplicate emails.

Bind numeric log IDs to `Vps.id`, and compare log pool with `vps.pool.name`.
`Pool#name` is the filesystem's first path component and is what VPS creation
passes as `pool_name`. Pool mismatch is excluded and printed for operator review.
The supplied transcript has only one node prompt and cannot establish complete
node grouping; never propagate that prompt over the rest of the concatenated
log or infer nodes from blank lines. Global vpsAdmin ID plus current pool is the
available binding. Report this evidence limit in preview/README; migrated or
reused IDs cannot be proved historically from this log. Do not invent node data.

### Bounded log classification

Read the supplied text as sequential records starting at an anchored `POOL/ID`
line, with positive decimal ID. Recognize the script's complete success terminal
line `changed; sshd restarted; original backup: ...`, anchored `unchanged`, or
an anchored `failed: POOL/ID` matching the current record. Parse only this task's
output conventions; ignore service chatter, prompts and blank separators.
An entry without a terminal result is `incomplete`, never changed or failed.
Both a success and failure result in one record, a mismatching failure identity,
or duplicated numeric IDs with conflicting outcomes/pools are ambiguous: abort
before queuing mail. Identical repeated evidence may be coalesced. A failed
record wins only by an explicit failure terminal, not by generic warning text.
Print counts and excluded/incomplete IDs; do not print the raw attachment.

Observed source log outside Git:
`/home/aither/.local/state/dev-workspaces/portal/vpsfree.cz-8a2a555cb2f65b33/uploads/files/20b76d2d-daf2-453e-b6f6-4fb7192c13ba/file.log`.
SHA-256 `d3d950962c601584ff8936aa75e0ee0feabe7eef3d9aa4b9914fea6a42afc560`;
9,440 bytes, 228 lines, 50 records with unique numeric IDs. Inventory: 43 changed,
zero unchanged, six failed and one incomplete. Failed IDs: tank/26427,
tank/24921, tank/26201, dozer/28872, dozer/23988, dozer/30231. All six explicitly
say populated Include is unsupported and sshd_config was not changed.
`tank/7668` has no terminal result and is excluded. Several successful records
contain OpenRC cgroup mkdir warnings; their explicit success terminal still
establishes script-reported success. This log proves reported outcomes, not
current effective SSH policy or mail-recipient counts. No live database checked.

### Template and preview contract

Lead templates use `user:` and `changed_vpses:` containing VPS objects supporting
id, hostname and node.domain_name. `changed_vpses` is the union of currently
eligible script-confirmed changes and operator-confirmed manual change 30231.
The user's latest confirmation establishes the same backup path for 30231.
This supersedes the briefly proposed `updated_vpses`/`backed_up_vpses` split;
retain the simple single list and common backup statement. Other failures remain
internal classifications/operator output only, with no eligibility and no
member-facing failure prose. Changed-only paragraphs and backup path must remain
conditional on nonempty `changed_vpses`. Key-upload/deployment and
remote-console guidance and localized KB links are supplied by the lead.
Use Czech for `cs`, English for `en`, and English for absent/unsupported language.
Follow conventional `mail_custom` with user, role `:admin`, and sender/reply-to
`podpora@vpsfree.cz`; use lead-supplied subjects and text unchanged.

Default mode previews recipients, VPS classifications, selected language and
rendered subject/body, then deliberately raises before the Custom chain returns,
following existing maintenance tasks. `TransactionChain.fire` wraps linking in
a database transaction; mail_custom creates mail records and queues send
transactions, so this preview exception rolls back preparation. Only literal
`execute` permits commit/queueing. Do not rescue that preview exception into
success inside the transaction. Parse and validate all evidence before any
mail_custom call. Invalid args, parse ambiguity or render failure cannot queue
partial mail. Zero eligible users is a clear no-op, not a send attempt.

### Acceptance, checks and recovery

Quick Ruby syntax and isolated mocks only. Exercise the actual supplied log
read-only for counts above without vpsadmin initialization, plus synthetic
changed/failed/unchanged/incomplete, noisy success, conflicting duplicate and
pool-mismatch cases. Mock active/inactive owners, Alpine/non-Alpine,
running/stopped/missing status, logged/unlogged VPSes and multiple qualifying
VPSes per owner. Verify one email/user, no unchanged-only or other-failed-only
recipient, English fallback, preview rollback/no queue and explicit execute
preparation only. Verify exact manual ID 30231 is included with backup wording
only when present as failed log evidence and still passes the same current
active/running/Alpine/pool checks; other five failed IDs stay excluded. Use latest
lead templates with `user:`/`changed_vpses:`, including mixed script/manual
owner coverage and no failure prose. No live mail or DB
check is needed for development; lead invokes final independent review.

No schema, API, daemon, node configuration or existing SSH script changes.
Uses current vpsAdmin model and existing mail transaction behavior; no deployment
ordering requirement. Preview rolls back; queued/sent mail is not reversible by
reverting this task. User controls actual execution after reviewing output.
Evidence: three existing tasks (2025-09-27 Arch/systemd mail, 2026-04-09 cgroups
mail, 2023-08-26 cgroups-init mail) and canonical vpsAdmin
`b4ef8535a629ee8c9cd753afecdb05e0895d0eea`: `api/models/vps.rb`,
`vps_current_status.rb`, `pool.rb`, `transaction_chain.rb`, and supervisor
`node/vps_status.rb`. Implementer returns exact base/head, files, quick-check
results and no-migration provenance; lead handles tracking and publication.

## Corrective package: preserve disabled configs and verify original mail evidence

This accepted user correction supersedes byte-canonicalization as a reason to
change a guest and supersedes old-log-only automatic mail eligibility. Owner is
implementer0 for the existing SSH and mail task directories, their README files
and focused checks. Architect0 owns this brief. Preserve the deployed/published
SSH commit and current mail head `7316503`; add focused corrective commits after
that head, never amend or rewrite the earlier deployed change. No node, database
or mail execution is authorized. SSH/report implementation can start from this
settled brief; mail consumes the fixed interface below in the same package.

### One bounded, read-only policy classifier

Reuse one shell function inside the guest payload for current configuration and
the exact original backup. Its result is `enabled`, `disabled` or `unknown` for
the PasswordAuthentication policy, not a claim about exploitability or all other
authentication methods. Run native `sshd -T -f FILE` and inspect its
PasswordAuthentication output case-insensitively; command failure, missing or
unexpected output means unknown. Do not infer policy from file byte differences.
Retain the current Include support boundary; unsupported/populated/unusable
includes mean unknown, without writes. A missing/nonregular/symlink backup is
unknown. Use the native tool for syntax/default/duplicate precedence, not a
second complete sshd parser.

For supported ordinary directive spelling, scan only Match boundaries and the
first explicit PasswordAuthentication value in each Match block. Recognize
case-insensitive keywords, whitespace/equals separators and ordinary quoted
boolean tokens, or fail closed on unrecognized relevant syntax. Global
duplicates are resolved by native sshd. Later duplicates in the same Match
block do not replace its first value. No connection predicates are evaluated.

- Native result `no` and every Match block's first explicit value `no` or absent
  proves `disabled`.
- Native result `yes` and every Match block's first explicit value `yes` or
  absent proves `enabled`.
- Mixed/unsupported/uncertain cases are `unknown`; never rewrite them merely
  because they might enable passwords. This deliberately refuses some safe or
  unsafe conditional configurations instead of building a predicate engine.

Local real OpenSSH evidence: disposable host key and configs, no daemon/listener.
`sshd -T` and `-T -C user=root,host=localhost,addr=127.0.0.1` both returned no for
global yes + Match all no, default + Match all no, and global no then duplicate
global yes. Global no + Match User root yes returned no without -C but yes with
-C. Thus a dump alone is insufficient for conditional rules; Match all no is
handled without rewriting under the rule above. The
[OpenSSH manual](https://man.openbsd.org/sshd_config#Match) and
[parser source](https://raw.githubusercontent.com/openssh/openssh-portable/V_10_3_P1/servconf.c)
confirm first-applicable Match precedence. This bounded proof deliberately
avoids deciding overlap or reachability between different conditions.

### Mutation behavior

Classify before candidate creation, backup creation or service action. Disabled:
emit the existing `unchanged` terminal and preserve all bytes, metadata, backup
state and service state. Enabled: use the existing validated candidate, original
backup and restart/recovery path. Unknown: explicit failure/nonzero with no
mutation, no new backup and no restart. In particular a Match-only no is not
proof that global/default password auth is disabled, and an apparent Match yes
is not proof of reachability. Keep existing pool-qualified runscript transport.

### Fixed original-backup report and mail input

Add one fixed read-only host mode, `--report-backup`, passing `report-backup` as
the companion payload argument to `ct runscript`. It reads only
`/etc/ssh/sshd_config.before-2026-11-05-disable-password-authentication` and
classifies it with the same function. No copying, chmod, configuration edit,
backup creation or service action in this mode. Unknown modes fail. Diagnostics
go to stderr; the guest emits only `POLICY<TAB>SHA256_OR_DASH`. Hash readable
backup bytes with SHA-256; use `-` if bytes cannot be read. Detect changed backup
bytes across classification/hash reads and report unknown. Do not classify the
current config as a substitute for a missing backup.

The host emits one machine-readable TSV line per enumerated running Alpine VPS:
`ssh-password-backup-v1<TAB>NODE_FQDN<TAB>POOL<TAB>ID<TAB>POLICY<TAB>SHA256_OR_DASH`.
Derive NODE_FQDN once with `hostname -f`; failure is fatal. Fields must not
contain tabs/newlines. Invocation is read-only; report unknown for failed guest
inspection with `-` hash when no reliable result is available. Emit rows for
all enumerated targets; nonzero summary exit signals any unknown/inspection
failure, but retains complete rows for operator review. Enumeration failure is
fatal. No extra summary or service chatter on stdout. Operator captures stdout
to an external report file and reviews stderr; concatenate such report files
from the relevant nodes outside Git. No raw log/report copies in tracked files.

Mail invocation becomes `mail_alpine_users_sshhole.rb LOGFILE BACKUP_REPORT
[execute]`. Validate fixed TSV version/field count, positive IDs, policy enum,
node/pool identity and SHA-256 format (`-` only for unknown). Reject malformed
or conflicting evidence before firing the chain. Identical duplicate rows may
coalesce; conflicting node/pool/status/hash for one numeric ID aborts. Current
DB node.domain_name and pool.name must match the report and original log pool.
The original log has no full historical node map; report+current binding is the
available proof, not invented historical node information.

Old log `changed` IDs qualify only with matching backup report `enabled`.
`disabled`, unknown, missing and identity-mismatched reports exclude automatic
mail eligibility and are listed for the operator. Preserve the explicit manual
30231 exception: the user confirmed both its manual fix and original backup;
it still requires its failed original-log evidence plus all existing current
active/running/Alpine/pool checks, without requiring an enabled backup report.
Other failed IDs remain excluded. Templates remain lead-owned
`user:`/`changed_vpses:` and contain no failure prose. The old 43 changed entries
prove file rewrite/restart only, not previously enabled password policy. No
current recipient number can be inferred before the external report exists.

### Focused acceptance and evidence

Use real `sshd -T` (temporary HostKey) plus `-C` for representative conditional
fixtures; no daemon. Required preservation fixtures: no away from first line,
whitespace/case variation, first global no followed by duplicate yes, duplicate
no, all-Match values no with native no, and global/default yes + Match all no.
For each assert unchanged bytes, no backup creation and no restart. Conditional
global-no/Match-yes and unproved mixed cases must fail without mutation. Ordinary
global/default yes without disabling conditions must still modify/backup/restart.
Retain validation/recovery checks. Real parser failure is unknown, never enabled.

Report checks prove read-only behavior, exact rows and hashes, missing/invalid
backup unknown, guest failures, node/pool identity and mixed report outcomes.
Mail mocks cover changed+enabled inclusion; changed+disabled/unknown/missing
exclusion; mismatch/conflict rejection; exact manual30231 preservation;
one mail per eligible owner and preview rollback. Reuse the classifier rather
than duplicating policy parsing. README explains report collection before mail
preview, provenance bounds, unknown exclusions and no-send development scope.
No schema/migration change. Review the full retained base-to-final-head series;
do not claim the earlier operation affected password-enabled VPS exclusively.
