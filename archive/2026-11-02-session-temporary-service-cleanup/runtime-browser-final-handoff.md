# Final runtime publication after browser harness correction

Published feature `3d76f527a6b88e9d32c202f729a1a0d673b341f2`, accepted exact tree `b9f7154cabbd95624dc447d87b855f2b01b33247`,
base/master `c2182254d29c4175c3e9fe4267e5a92dd1da6b79`. Runtime lane returned clean with no running operation.
Final source `/nix/store/qkv85x0hzq5kiv93s97wwqmdjsz7ndmz-source`, NAR `sha256-nW2yN5CRj/4hlx1PvK0vCUn7Tkejc8ZiEKqfPO0ygU0=`.

Complete three-commit series:

- `16e4b98212292446cec28724ac9a62ccfcbdfb56 portal: group session resources and show retained counts`
- `d9ec31a05074b5f0774fc9cd9114fc74e3691c29 sessions: retire registered temporary services before file cleanup`
- `3d76f527a6b88e9d32c202f729a1a0d673b341f2 portal: expose registered services and protect lifecycle handoff`

The only new correction is the accepted harness-only c850 fix folded into UI.
Core/dependent patches are exactly equal by range-diff. Final tree equals accepted
c850. No product, API, schema, ownership or migration change; no new state
consumption boundary. Old published e29 and c850 recovery refs are retained,
along with old312/d137/original history and all prior CI/pin receipts. Intermediate
unpublished pins remain historical and will be replaced/consolidated per stream.

Full runtime input graph and flake/lock are unchanged. Exact filtered Ruby source
`/nix/store/032kq2fwxbidrsaavf38vwskkrckd3v6-dev-workspace-ruby-source`, NAR `sha256-YofCVP7YhwSMX2ynV8e/hD0vh4y1dPARm0uXvr2cxgQ=`, all3 exported derivation/output
identities and recursive receipt `d5ff3b20d01f39941cbbc7301d7fb43b27297dade73e7fa87a3048af03028898` match A's
successful affected-shard proof (390tests/5281assertions/11configuredskips).
No full4shard/VM claim follows. Accepted127browser tests+10syntax command inputs
are preserved after rebase; no redundant build/test suite was launched.

Publication used SSH exact lease against observed e29; fresh remote feature is
final3d76 and master remains c218. No superseded active runs existed, so no run
was cancelled. Current Check41518664500 was in progress when captured:
https://github.com/aither64/dev-workspace/actions/runs/41518664500 . Lead owns the
fresh watcher; B does not await CI. No default merge, PR, deployment, claim or
session lifecycle action occurred.

[Complete source/input/derivation/browser/CI receipt](runtime-browser-final-receipt.json),
[complete final diff](runtime-browser-final-base-to-head.diff),
[old e29 range-diff](runtime-browser-final-range-diff.txt),
[pre-c850 range-diff](runtime-browser-final-fixup-range-diff.txt),
[exact source metadata](runtime-browser-final-metadata.json),
[recursive derivations](runtime-browser-final-recursive-derivations.json),
[browser correction inspection evidence](browser-ci-remediation.md).

Workspace/configuration pins proceed separately under lead's granted package;
workspace publication remains held for same-reviewer final history/graph conclusion.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
