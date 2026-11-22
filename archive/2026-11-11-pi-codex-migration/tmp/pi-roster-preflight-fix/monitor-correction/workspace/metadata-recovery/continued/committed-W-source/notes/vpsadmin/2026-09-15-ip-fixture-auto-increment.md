# IP fixture addresses cannot rely on maximum ID modulo a pool size

API Specs engine run35000486221 failed during IncidentReport fixture setup:
`create_ip_address!` generated an IP that already existed, before task execution.
MariaDB auto-increment sequences advance across rolled-back examples while
rows disappear. Two newly created fixture rows can therefore share the address
computed from the previous maximum ID modulo200.

The bounded correction in vpsAdmin46acba869 skips occupied default candidates
while preserving explicit addresses and the helper interface. A deterministic
regression reproduced the failure before the fix; the fixture, incident task
and campaign model specs passed48/0 with the original CI seed55211 afterwards.
The existing engine workflow pattern covers the new spec exactly once.

Related initiative: `work/2026-09-09-ip-release-mechanism/state.md`.
