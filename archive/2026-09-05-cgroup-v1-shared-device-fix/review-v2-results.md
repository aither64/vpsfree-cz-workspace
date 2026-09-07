# Mandatory review: cgroup v2 regression follow-up

Reviewed vpsadminos series: `ec7dc42da33cd963fe63d8dde281b0e88fe790c2` through
`19e7601e1932c25f3b6542d667c6d3f5aea7a20b`; new follow-up starts after
`9fb79eb68ba4f7b9d9a9c6e2e985556a10aa725e`.
Packet: `review-v2-packet.md`.

Overall initiative risk: high (device authorization/isolation and production
revision selection); follow-up implementation is test-only.

Four fresh standalone reviewers used `gpt-5.6-sol` at `xhigh`, without nested
reviewers. General, architecture/repetition, scope/proportionality, and
risk/compatibility all reported no Blocking, Important, or Advisory findings.
No remediations or reruns were required.

Accepted residuals and pending verification:

- VM tests must verify kernel-backed BPF transitions, Alpine shell TUN open
  behavior, and explicit permission-denial text.
- Ordered examples intentionally share state, matching v1; an early failure
  can prevent execution of the later recursive-removal scenario.
- The existing configuration pin must later select the exact validated feature
  revision through a consolidated generated lockfile-only update.
- Development-shell `.bin/` and `.bundle/` artifacts were created in the
  configuration worktree during review. The packet was corrected to state
  tracked cleanliness, and these artifacts will be removed before handoff.

## Reruns on amended head 5e31378ae

The initial VM failure and correction are documented in the packet's rerun
section and in state.md. Fresh general and risk/compatibility reviewers again
used gpt-5.6-sol at xhigh. Both reported no findings on
`5e31378ae42f253b4878940e3462f6e40b214fb4` and correction `19e7601e..5e31378ae`.
The correction is supported by v2 group traversal and observed effective
kernel denials. Architecture/scope were not rerun because no interface,
abstraction, runtime behavior, or scope changed.

Accepted residual: the test verifies immediate running-container effective
policy. It deliberately does not assert descendant program identities after
parent removal or cover later parent re-expansion, restart, or reconfiguration.
The amended VM run must still reach the final parent/attachment/health checks,
which the first run did not reach after its overly strict assertion failed.
