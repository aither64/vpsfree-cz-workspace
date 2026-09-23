# Final review remediation

This is a follow-up to `review-final-integration-packet.md` for the same
independent Sol/xhigh reviewer. The first review found one Blocking General
pin-history issue, Important Risk HTTP sender spoofing, and Important
General/Architecture unmanaged preset races. The previously accepted
missing-thread classification Advisory is unchanged. Rerun only General,
Architecture, and Risk. Scope was not expanded; there is no reason to rerun
the Scope lane.

Current committed heads:

| Project | Prior reviewed head | New head |
| --- | --- | --- |
| codex-web | `d542e767310d9d7b32460691a54829371b88e3b2` | unchanged |
| generic dev-workspace | `2f3c8b80a52ee932b21236df07e7fca164402439` | `ec8cb4211111d9734bfef5e4fe5c1f06c8372934` |
| vpsFree extension | `1cea22427b809f5774631abc8f40400337e7b688` | `ecd56fb91e79265de17c050a12ee5fefa139ef47` |
| workspace | `361925dd52ddbf791550dd921c6b836d74ba2304` | `5826554ea134e92f0fda056ad253a336414f4312` |

Generic commits `8f5bff1` and `ec8cb42` separate the HTTP sender fix
from atomic unmanaged preset reservation. The HTTP Team API now rejects an
explicit non-lead `from` and passes only `lead` to `Service.Assign`; the
local CLI and member-bound report path are unchanged. The fallback preset
reserves all addresses in one locked roster update before starting any
thread, then resumes creating members. The follow-up review found that an old
creating prefix can also be a concurrent manual Add, so only a complete exact
reservation is retried. Shorter and all-ready prefixes fail closed; an
operator can retry the retained member and add missing roles explicitly. Solo
remains an unpersisted no-op with a serialized empty-roster check. No schema
or public wire shape changed. The generic portal guide records the HTTP
sender boundary.

Each downstream repository now has one feature commit and one final pin
commit. The old intermediate pins were consolidated by interactive rebase;
before and after tree hashes matched in both repositories. The extension
feature ref was force-pushed with an exact lease after `nix flake check
--no-build` passed. The workspace feature remains local and is based on
shared `master` `3132359b`.

The retained reviewer confirmed the original three findings at intermediate
heads `e4ce1ad`/`eaa4bbc`/`dcef1b4`. Its sole new Important finding was the
ambiguous shorter prefix; `ec8cb42` removes that recovery path and adds
focused rejection tests. This only deletes the rejected behavior, so the
mandatory review workflow does not require another reviewer rerun. Extension
and workspace final pin commits were amended to the exact current heads.

Quick verification: focused generic Go tests for HTTP sender, concurrent
reservation, partial retry, old-prefix recovery, Solo locking and manual
prefix rejection passed. The concurrent test passed 20 repeated runs. Focused
tests also pass for rejecting an old or manual creating prefix without adding
roles.
Extension and workspace `nix flake check --no-build` passed at the new heads;
diff whitespace checks passed. Long packaged checks, final-head CI, aitherdev
switch and live browser checks remain post-review.
