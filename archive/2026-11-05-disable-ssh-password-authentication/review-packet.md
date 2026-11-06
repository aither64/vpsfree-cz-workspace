# Urgent Alpine SSH maintenance script review

## Revised committed head for affected-lane review

Final head now `2e7c9add2958e614a77e96236e92c55c8b22ad5c`, same base
`2fdc9f2889ac419136cd0cde0e0955c015ae7107`. Initial review below was of
`c4eb218a2fb2084a44a544c61399517b70cd562f`; preserve its report in review.md.
This is one consolidated final commit, three files/146 added lines, clean tree,
no migrations, obsolete branch iterations or dependency/generated update streams.

Changes since reviewed head: F1 narrow fix allows the exact ordinary default
Include only when its glob matches nothing; otherwise refusal remains. User
then required `osctl ct runscript`: wrapper resolves absolute companion payload
beside itself and invokes pool-qualified runscript with closed stdin. Mutation
code moved into a POSIX shebang companion script. README updated for both files
and supported Include boundary. No deployment/external consumption.

Quick checks: wrapper Bash/companion sh syntax, final whitespace, all seven
grouped disposable mocked cases pass (~9.8 seconds). Prior backup/restart/error
coverage retained. New coverage proves actual companion path/file execution
from another working directory, pool/ID selection, closed stdin; absent/empty
default Include succeeds; populated/dangling/literal-star/directory matches and
unusable directory fail without mutation; reruns avoid restart. Exact command
semantics independently verified by architect in canonical osctl/osctld source
49636f9. No real-node/BusyBox/OpenRC run. See implementation-evidence.md and
updated mock_checks.py.

Same reviewer: general, architecture and risk lanes affected by runscript and
the Include correction. Scope remains the same bounded task; reuse original
scope assessment unless changed code presents a scope issue. Review revised
whole base-to-head series/history and no-migration conclusion. No nested review.

## Original packet (retained for reviewed-range provenance)

Requested: node-local script in vpsfree-maintenance-tasks using `osctl ct ls`
to enumerate running Alpine containers, set `/etc/ssh/sshd_config` to
`PasswordAuthentication no`, restart sshd only if changed, and store the original
before modification (user follow-up).

Session: `2026-11-05-disable-ssh-password-authentication`.
Repository/worktree: `worktrees/2026-11-05-disable-ssh-password-authentication/vpsfree-maintenance-tasks`.
Base: `2fdc9f2889ac419136cd0cde0e0955c015ae7107` (`origin/master`).
Final head: `c4eb218a2fb2084a44a544c61399517b70cd562f`.
Complete series: one commit, `c4eb218` —
`2026-11-05-disable-ssh-password-authentication: add Alpine workaround`.
Final diff: `git diff 2fdc9f2889ac419136cd0cde0e0955c015ae7107..c4eb218a2fb2084a44a544c61399517b70cd562f`.
Two new files: dated task script (81 lines) and README (40 lines). No obsolete
approaches remain in history; no migrations or repeated update streams.
All source/docs committed; working tree clean. `git diff --check` passes.

Quick-check evidence from implementer0: host Bash and embedded POSIX sh syntax
pass; `python3 work/2026-11-05-disable-ssh-password-authentication/mock_checks.py`
passes five grouped cases. Disposable test source is alongside this packet.
Coverage: filters/pool qualification; same ID in two pools; enumeration/no matches;
commented/absent/mixed-case/duplicate/Match rules; idempotence; first backup and
later preservation; file mode; validation and backup failure; Include/missing/
symlink refusal; continued processing; restart failure restoring immediate state,
recovery restart and independent inode protecting the original backup. No live
Alpine node/BusyBox run; sshd/OpenRC mocked. No repository CI workflows exist.
The early fixture assumed /bin/ln on the Nix host; its ln mock now uses os.link.
The backup rollback alias issue was fixed before this sole commit.

Scope: one dated task directory, standalone script and operator README. One
coherent operational behavior; its documentation/checks belong with that behavior.
No production execution, default-branch integration, package changes, recursive
Include rewriting, keyboard-interactive changes, or fleet configuration updates.
Active Include is an explicit failure rather than a false mitigation claim.

Design: [design.md](design.md). Plan/state carry the user scope and phase record.
No migrations, dependency or generated update streams are planned; verify this
against the complete final series. No deployed/released/external consumers of
this new task. Preserve original first-change backup on reruns and metadata;
failed validation/backup must not mutate the live file. Restart failure must be
reported and recovery attempted. No host/guest protocol change.

High risk: SSH authentication policy, node-local guest operations, persisted
configuration and recovery. Reviewer: retained `reviewer0`, gpt-6.1-sol/xhigh,
read-only, no overrides. Lanes: general, architecture/repetition,
scope/proportionality, risk/compatibility. Read the mandatory-change-review skill
and all four references, perform review directly, and explicitly conclude on
whole-branch history, migration lineage and repeated update streams.

Review the actual user scope first; favor a conventional bounded script and
required correctness within the supported boundary. Report concrete findings,
severities, evidence and residual test gaps. Source-based/mocked checks do not
constitute a live-node execution test.
