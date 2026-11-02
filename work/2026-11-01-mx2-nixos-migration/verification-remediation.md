# Narrow final-review remediation

Reviewed predecessor: `f3789413a53bcd12e2352940a0ec3e88009c5d9f`.
Current head: `53d1310dd1be1c35ea83317a620ce9f6a7fae227`.
Current tree: `281b8e3184758d6fdb68e41532de6a8b034cf903`.
Base remains `c040c14cdbacc07998700b524996a89306188d7f`, freshly fetched unchanged.

Read [the complete independent review](verification-review.md); its original
range and conclusions are unchanged. Lead assigned the exact R1/R2 corrections
and accepted direct focused verification under mandatory-change-review step 9.
There is no new design, production policy, fixture topology or scope extension.

## Changes and focused verification

Only `tests/mx2.py` changes from the reviewed predecessor: 16 additions and six
deletions. See [complete source/range delta](verification-remediation-diff.md).

- Important R1: DNS-resolvable unrelated-domain and arbitrary-subdomain RCPT
  denial now runs over both existing IPv4 and IPv6 source/target pairs. Each
  requires a 5xx response at RCPT and an empty queue. Existing malformed and
  unknown-domain cases remain separate. Production/fixture trust is unchanged.
- Advisory R2: after locating the deferred queue ID and verifying queued
  sender/content, the test now checks that the queued recipient is exactly
  `temporary@vpsfree.cz` and its `delay_reason` contains
  `450 4.2.0 fixture temporary rejection`, before removing the primary map entry.
  DNS/connect failures cannot satisfy this assertion.

Focused checks passed: Python compilation, pyflakes-F on the standard NixOS
generated-driver machine hints, `git diff --check`, direct source inspection,
and normal commit hooks. No hook bypass; advisory 72-column message warnings only.
The fix is folded into its owning tests commit, leaving three logical commits:
host `36ae652962d0217dd5b22965cd44fd711790d77a`, DNS
`91595bef8847063d76246b292293a687362af420`, tests/docs current head above.
Both earlier commits are byte-for-byte unchanged. Source ref 40411d67 and
reviewed-import ref e4c1ac0c remain exact. No migrations or input streams added.

## Exact final evaluation and fidelity

Both derivation evaluations passed at the exact new committed head:

| Item | Derivation | Expected output |
| --- | --- | --- |
| Isolated check | `/nix/store/4xlkdsfhvjgm07za5gdyyn0ialfc6np4-vm-test-run-mx2.drv` | `/nix/store/fd5wgwclsmlpkxwailkbwnyx68m08j8d-vm-test-run-mx2` |
| Production MX | `/nix/store/40sp2bas7rr2609lccpw3iq3b9kdyc7d-nixos-system-mx2-26.05.20261026.718f670.drv` | `/nix/store/rq91giv8lrlgsj26h7dv7cv9c5sr5w5l-nixos-system-mx2-26.05.20261026.718f670` |

The new production root's selected main.cf, transport, Postgrey and TCP25
firewall derivations and generated texts were independently re-read and equal
the reviewed predecessor's exact selected identities. This is derivation/input
evidence, beyond tree equality. Test fixture/module source and all seven timing
overrides are unchanged; their actual production/fixture values remain in
[implementation evidence](verification-implementation.md). Disposable supporting
data is `verification-remediation-generated.json`.

The unchanged complete lock graph remains blob
`ec3d5aea9a7e55e69778e3ae4136cf2b3bb84e86`, SHA-256
`505f6c89e18972827beecc29a0c7c85e1df2576ed4074205501167a3dd6f326a`, recoverable
from the exact final head. No new test/system realization, VM or long check has
been started. Original review identities and earlier build evidence are not
rewritten or claimed as runtime validation of this candidate.

## Publication and next action

Published only the owned feature branch with the exact reviewed-predecessor
`--force-with-lease`; refreshed native comparison to this new head. Fresh remote
checks prove feature head `53d1310dd1be1c35ea83317a620ce9f6a7fae227` and unchanged
master/base above. CI returned no branch runs, so no superseded run needed
cancellation. Worktree is clean; both preserved refs remain exact. Lead accepts
the focused diff and launches fresh policy utilities for approved long checks. No default merge,
production operation, real mail, deployment or session lifecycle action.
