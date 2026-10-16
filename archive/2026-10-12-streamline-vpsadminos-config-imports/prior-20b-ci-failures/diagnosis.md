# Prior 20b broad CI failures

Original workflow 38645848469 tested product
20b803f349d68b1bb5619058ccc025e16baafd29. Original job logs and downloaded
native/Intel artifacts are retained here, with download status and hashes in
downloads.json. These are diagnosed failures, not rerun results.

Native CI ran 331 scripts in 127 tests and reported three failed scripts.
Intel lifecycle reported only the default NFS cancellation failure. No overall
CI pass is claimed.

- Both default osctl/nfs-cancellation attempts fail the first kernel assertion:
  expected uname 6.12.95.7, actual 6.12.95. Native machine-shell.log line137 and
  failure diagnostics line302, and the corresponding Intel lines, establish
  this directly. The native110 cancellation variant passed its full 65 examples.
  This is the unchanged test's kernel-release expectation, not persistence
  activation or allocation evidence.
- kernel/livepatch-kernel-identity first fails comparison of configured notes
  /nix/store/8gfs2ph5nnh95vc41mwgp773lk19yvn1-livepatch-kernel-notes-6.12.95
  against /sys/kernel/notes at byte17. Later load/wait/unload examples fail
  downstream of that unmet identity prerequisite. Exact kernel mismatch is
  established; these artifacts alone do not identify every binary-build cause.
  The subsequently fetched staging commit48c2dffa08f3e84440bd0d28f8d0a1a33b99ba89
  separately records nonreproducible historical signing/build identity and
  freezes the original outputs. That is upstream corrective context, not a
  verification pass of this feature.
- upgrade/from-6.18-guests-v1 fails after 5610.61s at guest nixold readiness.
  Actual guest logrotate-checkconf.service exits219/CGROUP: permission denied
  attaching to /system.slice/logrotate-checkconf.service. Guest systemd is251
  on kernel6.18.49. The common upgrade fixture pins nixold to the22.11 minimal image
  (tests/suite/upgrade/common.nix:1078); that older raw module is unchanged.
  This is a cgroup failure, distinct from the earlier fixture
  store-owner and EXEC failures. Root cause beyond that recorded failed step
  remains unproved; no service or cgroup workaround has been introduced.

Git comparison4c25fa5f9..f2b1960d shows no feature changes in the three tests,
their kernel boot fixture, or the livepatch service. The persistence refinement
edits only the four modern raw compatibility files and its focused fixtures;
no host, kernel, NFS or cgroup implementation change is included. These facts
separate the failures from a claimed persistence-suite acceptance, but do not
make an unexplained cgroup failure an overall-green CI result.

Do not rerun these jobs blindly. Preserve this evidence when superseded own-head
workflows are cancelled after publication. The revised feature still requires
its own quick checks, committed review and exact-head twelve-case acceptance.
