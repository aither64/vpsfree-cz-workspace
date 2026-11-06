# Implementation evidence and revised review packet

Same sole package submitted to lead for acceptance and affected-lane review.
No production execution, deployment, merge or lifecycle action occurred.

## Revisions, complete history and scope

- Repository: `vpsfree-maintenance-tasks`; worktree:
  `worktrees/2026-11-05-disable-ssh-password-authentication/vpsfree-maintenance-tasks`.
- Branch: `2026-11-05-disable-ssh-password-authentication`.
- Original reviewed range: `2fdc9f2889ac419136cd0cde0e0955c015ae7107..c4eb218a2fb2084a44a544c61399517b70cd562f`.
- Revised complete range: `2fdc9f2889ac419136cd0cde0e0955c015ae7107..2e7c9add2958e614a77e96236e92c55c8b22ad5c`.
- Current series is one amended commit: `2e7c9add2958e614a77e96236e92c55c8b22ad5c`,
  `2026-11-05-disable-ssh-password-authentication: add Alpine workaround`.
- [Final diff](implementation.diff); [old/new range comparison](implementation-range-diff.txt).
  This is a substantive requested correction, not a patch-equivalent rebase.
  No obsolete approach or fixup commit remains in current branch history.
- Fresh fetch found master unchanged at base, so no rebase was required.
  Feature-only exact-lease force push succeeded, replacing only the old head.
  No repository CI workflows exist, so no superseded runs to cancel.
- No migrations, dependency/pin changes or repeated generated-update streams.
  Neither old nor new task was deployed, released or externally consumed here.
- One commit bundles the wrapper, directly supporting companion payload and
  operator README. Three task-local files, 146 added lines; no unrelated edits.

## Requested result and narrow revision

Run `./2026-11-05-disable-ssh-password-authentication/disable_ssh_password_authentication.sh`
as root on a node, copying both scripts together. Wrapper enumerates running
Alpine guests and calls pool-qualified `ct runscript ID ABSOLUTE_PAYLOAD` with
stdin closed. Companion `disable_ssh_password_authentication_in_container.sh`
validates and sets main-file `PasswordAuthentication no`, preserves original
before mutation, and restarts only if changed. Failure is visible and processing
continues. A failed restart restores immediate preceding contents in a separate
inode, attempts one recovery restart, and returns failure.

Important review finding F1: Alpine ships active default
`Include /etc/ssh/sshd_config.d/*.conf`; blanket refusal skipped ordinary guests.
Accepted correction permits only that two-token form when the glob has no
matches and its directory is absent or usable. Keyword case/whitespace variants
are accepted; allowed lines are preserved. Any matching path (including dangling
symlink or literal star), unusable directory, or other active Include form fails
without mutation. Adding snippets later requires reassessment. No recursive
parser or snippet rewrite. Architect's revised [brief](design.md) and lead
accepted this boundary. Later USER steering required the runscript/file split.

Original backup remains
`/etc/ssh/sshd_config.before-2026-11-05-disable-password-authentication`;
it is never overwritten by reruns. README records invocation, changed-only
restart, include coverage, partial failures and deliberate manual restore.
Stock sshd/OpenRC paths and no concurrent config writer are assumed. Key,
keyboard-interactive and PAM settings are unchanged; password-requiring
AuthenticationMethods may prevent login. No API/schema/protocol/module change
or fleet-wide update ordering; guests are independent.

## Verification and gaps

- `bash -n` wrapper and `sh -n` companion: PASS.
- `python3 work/2026-11-05-disable-ssh-password-authentication/mock_checks.py`:
  all 7 grouped standard-library unittest cases PASS, 9.8 seconds.
- Previous 5 groups retained: exact selection/filtering/pool qualification, same
  ID across pools, empty/failed enumeration; transform variants/Match overrides;
  idempotence; first backup byte/mode equality and no overwrite on later runs;
  validation/backup/unusable backup failures; unsupported Include/missing/symlink
  refusal and later-guest continuation; restart failure, recovery and later-run
  rollback to immediate prior contents. Live/backup inode inequality plus later
  in-place live mutation prove original remains intact; documented cp restore passes.
- Revised osctl mock verifies exact runscript argv and absolute actual companion
  path from a different CWD, copies/remaps/runs the real file, checks closed stdin,
  forwards its status and removes its temporary executable.
- Two focused new groups: absent/empty/nonconf-only default directory succeeds,
  allowed Include line bytes survive and rerun does not restart; populated,
  dangling, literal-star and directory matches, regular-file/dangling-directory
  include paths refuse without config mutation, backup or service restart.
- Staged and final `git diff --check`: PASS. Working tree clean. No declared
  hook framework or active hooks; none bypassed.
- Fixture corrections only: original mock assumed absent `/bin/ln` on Nix
  (replaced by os.link); revised mock initially retained mode-0500 copied payload
  between calls (now removes it as osctld does). Full reruns then passed.
- No real Alpine/BusyBox/OpenRC/node execution; validation/service actions mocked.
  No long integration build applies. Fresh review required for runscript change.

Overall high risk (authentication, guest files and restart/recovery). Lead owns
fresh reviewer0 eligibility/invocation with saved gpt-6.1-sol/xhigh and affected
lanes, final packet/acceptance and state. Preserve initial review conclusions and
review this exact revised range/history; no migrations or repeated update streams.
Repository index/commit window released after publication; implementer0 retains
sole-package follow-up ownership, has accepted no new package.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-05-disable-ssh-password-authentication/)
