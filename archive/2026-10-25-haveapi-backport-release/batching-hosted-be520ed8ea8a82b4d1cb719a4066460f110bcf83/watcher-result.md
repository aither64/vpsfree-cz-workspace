**Result: incomplete.** The watcher command ran once, exited `1`, and observed all 12 exact-head runs to terminal status. Eleven succeeded; performance run `40221259354` was cancelled. The script reported that performance classification still requires parent assessment.

- **Watcher duration:** 2,742.146 seconds (45m 42s), from 18:28:14Z to 19:13:56Z.
- **Quick profile, run `40221256782`:** 14 cases; raw acceptance says pass, all cases passed and were wall/CPU adequate. Job duration was 597/600 seconds, with a 3-second margin.
- **Weekly profile, run `40221259354`:** captured samples contain 34 cases, but the run ended cancelled and has no final `report.json`; final adequacy and classification are unavailable in the captured evidence.
- **Source/runtime:** both profiles identify candidate `be520ed8ea8a82b4d1cb719a4066460f110bcf83`. The quick baseline is `1741a25e1df45f06f9966942d5c34a97967ebb3e`; the weekly baseline is `b85ec364057f536940d689b09e612512ffffaf82`. Captured runtime: Ruby 3.4.11 and JSON 2.21.2.

Logs and raw evidence:

- [Watcher command log](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-25-haveapi-backport-release/batching-hosted-be520ed8ea8a82b4d1cb719a4066460f110bcf83/watcher-command.log)
- [Watcher result](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-25-haveapi-backport-release/batching-hosted-be520ed8ea8a82b4d1cb719a4066460f110bcf83/watcher-result.json)
- [Quick acceptance summary](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-25-haveapi-backport-release/batching-hosted-be520ed8ea8a82b4d1cb719a4066460f110bcf83/quick-acceptance.json)
- [Quick raw performance artifacts](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-25-haveapi-backport-release/batching-hosted-be520ed8ea8a82b4d1cb719a4066460f110bcf83/40221256782-artifacts)
- [Weekly raw performance artifacts](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-25-haveapi-backport-release/batching-hosted-be520ed8ea8a82b4d1cb719a4066460f110bcf83/40221259354-artifacts)