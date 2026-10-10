# Preserve resource-producer failures before formatting

The reduced G14 qualification at K725c325e booted both 2048-MiB guests and
attested their identity and system closures, then failed the services resource
key-set assertion. The private native output contained an empty
`available_inodes=` field despite a successful public SSH command. The root
reported 4164870144 bytes available; this failure did not prove a capacity
shortfall.

The generated command combined `df -i` with `--output=iavail`. GNU df rejects
that combination. A pipeline inside successful `printf` hid the producer's
exit status; `set -e` did not make that expression fail. The repair belongs in
the verifier's generated resource script: select `df --output=iavail` and
capture each memory/df/ZFS producer in a status-preserving assignment before
formatting. Numeric validation and resource thresholds remain required.

Existing parser tests supplied synthetic numeric output and did not execute
the generated shell. The correction at K22e2fb77 executes that actual script
with declared GNU tools
and covers each failing producer and missing/malformed numeric output, rather
than reproducing a corrected command only in a test. Exact hosted verifier33/744
passes in both source branches; no local CI ran. Independent affected review
completed all four lanes with no findings. Source repair and passing hosted
tests do not complete the failed finite qualification or permit replay.

Current evidence and repair status: `work/2026-10-05-network-ipv4-left-counter/`
`finish-virtiofs-runtime-failure-proof1.json`, `design.md:6447`, and `state.md`.
The original private attempt, credentials and native output remain private.

A separate public G14 stop returned zero with complete recorded-process exit,
reservation release and owned socket removal. Its disks and failed attempt remain
retained. This does not complete API/PHP/lease/resume/media qualification.
