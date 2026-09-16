# General review

## Findings

### Advisory G1: Include the abandoned-mode recovery command

`dev-workspace` commit `a65583d45b707eb23feb7d490ba177e8360dfb8d`,
`docs/dev-sessions.md:485–488`, gives
`dev-session archive <slug> --as-is` as the recovery command for automatic
archives generally. The empty-session retention tier archives in `abandoned`
mode (`libexec/workspace-auto-archive.rb`, `auto_archive_scan_session`), while
the documented command defaults to `complete`. A user following it for that
tier receives the intentional journal-mode mismatch refusal from
`DevSession::Runner#archive` instead of finishing recovery.

Mention that empty-session automatic archives require the same command with
`--abandoned`. Existing journal checks preserve safety; this is a recovery
documentation omission.

No Blocking or Important findings.

## Scope and evidence

Reviewed the packet, plan/state, applicable repository instructions, runtime
commit series, consumer pins, surrounding archive/retry and portal lifecycle
code, regression tests, and session-guide documentation:

- Runtime: `eb658d49e6b8182d5fc07ab98bc897c58490baa9` →
  `a65583d45b707eb23feb7d490ba177e8360dfb8d`.
- Organization extension: `17da396e7fea5d4e31d4af1382da00fe4d140e17` →
  `1a0bc7db6c968bde9cb9ecbd737d8b1b6f28de44`.
- Workspace: `f8d6217a8a6e83bd317a7bef166aa650806ca553` →
  `3610be86615b8710b2e1bfe8a53b9771bad15fdf`.

The runtime commits have distinct purposes, and each consumer has one matching
pin update. The retirement override restores the previous timeout through the
existing `ensure` path. Stage wrapping preserves the underlying Go error. The
new banner requires matching operation and conversation identities and does not
replace a running lifecycle result. No persisted-format or protocol change was
introduced.

Independent verification: `git diff --check` passed; the two focused Ruby
retirement deadline/retry tests passed in `nix develop` (2 runs, 50 assertions,
zero failures/errors). Existing quick Go/browser-contract results were inspected
through the packet and test source.

Residual verification: real Chromium/Firefox execution, packaged tests,
isolated automatic-archive acceptance, source-session recovery, and deployed
package verification remain for the coordinator after review, as planned.
