**Important I1 — General and Risk/compatibility:** the committed scratch helper can respond to a global native request despite its intended read-only role.

[clientOptions](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-04-session-archive-reliability/workspace/bin/repair-legacy-sessions-2026-10-04-threadless/main.go:104) omits `ObserverOnly` (inherited owner `c953ff73397ace99f9c76b1742eeb503076fe4e7`). Pinned codex-web `3d07cf60` immediately rejects unsupported incoming requests. Selected Codex 0.160 broadcasts external ChatGPT-token refresh requests to every initialized connection and accepts the first response/error. The helper could therefore defeat the legitimate token supplier during an unrelated refresh.

I have not established that the prepared server uses externally managed tokens or that this occurred. Main must fix the passive-caller boundary or establish and record a supported-input exclusion. Simply setting `ObserverOnly` needs verification: its existing allowlist rejects discovery APIs this helper requires. No thread-answering or settings-override path was demonstrated; these discovery calls do not subscribe or resume threads.

No Blocking findings. The supervised maintenance window is sufficient for the documented trusted-operator contract **when writers actually remain excluded**. Sampled CWD/tmux checks alone do not establish that exclusion. Keep coordination/log writes outside tracked workspace, retain exclusions across interruption, and freshly verify them on retry. The existing barriers and exact commit-chain checks appropriately refuse drift.

Committed heads reviewed remain:

- R: `ea4c7e979ae534df4e199ede86952aac5f878ced`
- W: `88f42810902e4873ec9d207f949f3a55cb6c4ae7`
- C: `62cd8566ff8e26221192060c174b119b42616ef8`

The complete 3/2/1 history conclusions stand: no obsolete unmerged approaches, redundant pins or transitional migrations; no SQL/database or installed-schema migrations. Existing deployed readers and removal criteria remain supported. Unaffected architecture, scope and documentation conclusions stand.

W helper/test edits appeared during this investigation and were not reviewed as committed remediation. Native repair, builds, browser acceptance and real apply/retry outcomes remain unverified here.

Full addendum sent to Lead. Actual review turn: `01a10dbc-e428-7f23-8ada-3c3eb5e6a943`, Sol/xhigh/read_only.