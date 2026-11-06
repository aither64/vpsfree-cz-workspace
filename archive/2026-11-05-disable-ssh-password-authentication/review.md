# Independent final review

Reviewed range: `2fdc9f2889ac419136cd0cde0e0955c015ae7107..c4eb218a2fb2084a44a544c61399517b70cd562f`.
Reviewer0, thread `01a1ac18-8de0-7551-9d54-4498d1ffd8cd`, retained
gpt-6.1-sol/xhigh, review purpose/read_only, session and bindings verified.
No fallback, overrides or nested reviewers. General, architecture, scope and
risk lanes read and completed. Report delivered through session transport;
lead persisted this report because reviewer remains read-only.

## F1: Important — default Alpine Include skips ordinary containers

Script lines 29–30 unconditionally refuse active Include. Official Alpine
3.20-stable and 3.22-stable package patches add
`Include /etc/ssh/sshd_config.d/*.conf`; APKBUILD applies the patch and creates
the directory. vpsAdminOS image setup rewrites password/root directives without
removing Include. An ordinary guest with no snippets is therefore skipped,
leaving password authentication enabled. Deployed prevalence is unknown.

Primary evidence:

- [Alpine 3.22 patch](https://raw.githubusercontent.com/alpinelinux/aports/3.22-stable/main/openssh/include-config-dir.patch)
- [Alpine 3.20 patch](https://raw.githubusercontent.com/alpinelinux/aports/3.20-stable/main/openssh/include-config-dir.patch)
- [Alpine package definition](https://raw.githubusercontent.com/alpinelinux/aports/3.22-stable/main/openssh/APKBUILD)
- [OpenSSH Match semantics](https://man.openbsd.org/sshd_config#Match)

Recommended narrow fix: permit the standard no-matching-snippets Include case;
retain visible failure for unsupported overrides. Blindly removing the guard
could allow included Match rules to override the global no. A generalized
Include implementation needs affected-lane review; direct narrow remediation
can be inspected and checked under skill step 9.

## Remaining conclusions

No other Blocking or Important findings in supported main-file/no-Include
behavior. Validation precedes mutation, backups preserve metadata and original
contents across reruns, rollback installs a separate inode, unchanged files do
not restart, and guest failures continue with aggregate nonzero status. Pool
targeting and stdin/exit handling match osctl source at
`49636f902704ce6019a7a8ae47ec0b3ca6902f68`. README accurately covers invocation,
restoration and residual authentication risks.

Scope is proportionate: 81-line script and 40-line directly supporting README.
One dated standalone task matches repository conventions, with clear host/guest
boundary and no unnecessary framework or drift-prone policy duplication.
Design accepted 14:31 UTC, committed deliverable 14:36, review dispatch 14:37;
no milestone-based scope concern.

Whole branch independently inspected: one coherent commit, correct task prefix,
merge base equals supplied base, clean worktree. No obsolete approaches, fixups,
transitional compatibility or superseded history remain. No migrations and no
migration lineage to preserve. No dependency/channel/input/generated update
streams or pins, so no consolidation needed. No deployment/release/external
consumption reported.

Reviewer independently passed host Bash syntax, extracted guest sh syntax and
diff whitespace checks; inspected all five mocked groups and implementer
evidence without rerunning write-producing fixtures. No live Alpine, BusyBox,
OpenSSH, OpenRC or production check. No global build/framework applies.
High risk is appropriate for SSH authentication, guest configuration and
restart/recovery. Custom daemon config/options, concurrent writers,
interruption/filesystem failure, keyboard-interactive/PAM remain limitations.
No coordinated component update, schema/API/protocol/module change.

Final readiness awaits F1 resolution. Subsequent user-requested switch to
`osctl ct runscript` will receive affected-lane final review at the revised head.

## Revised-head final review: passed

Exact final range:
`2fdc9f2889ac419136cd0cde0e0955c015ae7107..2e7c9add2958e614a77e96236e92c55c8b22ad5c`.
Same reviewer0 identity/settings freshly verified; retained gpt-6.1-sol/xhigh,
read_only, same thread, no overrides/fallback/nesting. General, architecture and
risk lanes completed; original scope conclusion retained. Compared old reviewed
head c4eb218 to new head, complete final diff/log, updated packet/design/evidence,
repository instructions and mock source. No new Blocking, Important or Advisory
findings. Final review gate satisfied at this exact head; integration separate.

F1 resolved: exact default Include with case/whitespace variants is accepted
only for absent/usable empty snippet directory; line bytes remain. Glob matches
including dangling symlinks/directories/literal stars, unusable directories and
other forms fail before mutation. Populated snippets remain a documented limit;
later snippet additions require reassessment.

User runscript request implemented conventionally: host resolves readable
companion from BASH_SOURCE, passes absolute file with pool/ID and closed stdin.
Reviewer independently checked canonical osctl/osctld source 49636f9: realpath,
temporary guest copy mode 0500, running-guest attachment/shebang execution, status
propagation and cleanup; no -r means stopped guests are not started. Failure
aggregation/continuation preserved. Mutation/backup/recovery body independently
compared exactly unchanged from original review. README matches copying both
scripts, runscript and Include limits, retained backup and manual restore.

Independent wrapper Bash/companion sh syntax, complete diff whitespace and
clean-tree checks passed. Mutation-body comparison passed. Seven mocked groups
and implementer evidence inspected; reviewer did not rerun write-producing
fixtures. No live Alpine/BusyBox/OpenSSH/OpenRC/production test. Documented stock
path, concurrent writer, interruption/filesystem and keyboard-interactive/PAM
limits remain runtime gaps, not new findings.

Whole final branch independently verified: exactly one coherent consolidated
commit 2e7c9ad, correct prefix and exact merge base. Old c4eb218 remains review
provenance only. No obsolete approaches, fixups, transitional compatibility or
superseded history. No migrations or migration lineage. No repeated dependency,
channel, input, generated streams or pins; no consolidation required. Neither
revision reported deployed/released/external consumption. Revision is substantive,
not patch-equivalent. Three task-local files/146 lines are fully explained by
user transport request and narrow F1 correction; no added subsystem needed.
