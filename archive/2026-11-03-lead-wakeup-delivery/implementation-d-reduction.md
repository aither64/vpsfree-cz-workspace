# D: bounded maintenance reduction

Frozen source on R `9cf1c7694b3918fcef1b088669ee6241605f071f` / tree `2c71c9b4c15da00f0353c1d31d3b2b8f70ad23b9`. Main owns the index, commit and affected independent review.

The patch removes the isolated Operations maintenance API/UI/browser contract and separate switch timing/decision classification. It changes 19 paths, +20/-1146. The operation UUID is generated once during preparation and reused for operation/startup/recovery. Admission, Stop, queues, terminal restoration and automatic cooperative pause/resume remain. No schema migration or input/pin change.

Evidence: `/tmp/lead-wakeup-maintenance-D-reduction-6k84w047/final-D-source.json` (SHA256 `8aa2703223b61b9a135de43b5b7a011eede7d378d56a80a80979f477cfff17cc`). Exact diff: `/tmp/lead-wakeup-maintenance-D-reduction-6k84w047/source.diff` (SHA256 `49573bac14281e4c729571d192ecb31d5d05196f1aae87b82c91d9b57ae6a3e6`). Per-path baseline/final hashes and actual command/log/exit receipts are in the packet.

Passed in repository Nix: Ruby focused 27 tests/377 assertions; Go web focused 1.760s; tagged compile-only 0.047s (no tests executed); Ruby/Nix/embedded-Python syntax, Go format and whitespace; prepared-operation UUID/startup/recovery control 1 test/16 assertions. Auxiliary UUID-control failures are retained and explained in the packet; application source stayed unchanged.

Main accepted the three changed documentation drafts as written. `docs/workspace-portal.md` needed no change. The native setup smoke has only the released asset URL substitution; all other native fixture bytes and the retained prompt/monitor tests are preserved exactly.

No native, VM, browser, model, full suite, build, CI, Git mutation, publication or live action ran. Prior native failures remain unresolved and historical evidence retained. No automatic follow-up; D capacity returned. Next: main source inspection/commit and affected independent review, followed only by separately authorized acceptance.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/)
