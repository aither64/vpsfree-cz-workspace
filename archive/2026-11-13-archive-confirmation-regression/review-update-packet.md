# Narrow final review update

Original independent review.md remains authoritative for unchanged provider behavior. All intended changes are again committed, quick-checked, clean and SSH-published. Same saved reviewer0 Sol/xhigh/read_only; no fallback/override. Please review only the new test correction, changed histories/pin graphs and refreshed configuration baseline/host implications, reusing unchanged original lane conclusions. Include explicit final whole-branch/no obsolete history/repeated pins/no-migrations conclusions. Relevant concerns: general/history, proportionality of test timing and risk/compatibility of refreshed deployment graph; no request to repeat unaffected implementation review.

## Final complete ranges

All worktrees remain under worktrees/2026-11-13-archive-confirmation-regression/{dev-workspace,workspace,vpsfree-cz-configuration}; branch unchanged.

| Repository | Final base | Final head | Complete series |
| --- | --- | --- | --- |
| dev-workspace | 458c7857b942fb592607c83af7b5287a6c93ea96 | 9241a342a6ef4ca69148594e98cce7ddcfb459a6 | Original e96284d1 functional commit unchanged, then separate 9241a342 test-only correction |
| workspace | aa9333916fdc1062755a88e1b8298b845ec2ccc4 | 5cde17b6ea854264f3cc8ecd8430f62c3d758688 | One consolidated final runtime pin |
| configuration | 5447fac5342404678d2f72094995ce43e41d7602 | 111973876df886739be5abe330f58ff6062bf03a | One regenerated channel pin; complete 458c7857→9241 changelog preserved |

## Test correction and evidence

Old automatic CI fast job failed TestMaintenanceCancellationContinuationTimeoutRetriesOriginalIdentity during WebSocket initialization before deliberately unanswered resume was reached. Owner verified this test byte-identical at base/current and reproduced an unmodified focused pass0.781s; parallel packaged CI had insufficient setup budget. New commit changes only the first attempt's300ms child cap to3s plus rationale. Server read budget remains5s, parent10s, and every reached/DeadlineExceeded/parentalive/stable submitting identity/dedup/retry-settlement assertion remains. No production maintenance change/client seam/retry loop. Exact test plus three related deadline/allowance checks PASS3.572s. Separate commit preserves independent logical purpose. Inspect actual diff and failure reasoning independently; no assertion weakening should be accepted merely to obtain green CI.

Old CI43700542294 ended cancelled after supersession (fastfailed, archivepassed, creationstillrunning at cancellation). Final9241 automatic CI43703969384 attempt1 is runtime-observed separately. No local long build/test occurred: prior registered native watcher only polled its registration. It was canceled and resolved through owner/native evidence that argv never launched; no process/phase artifacts. Parent fallback will launch first real build after this update passes, with explicit process receipt/phase logs. Do not interpret its lack of results as a product check failure.

## Config baseline refresh and mechanical pin history

Original reviewed config11ef63c5..9f7679; clean rebase5447fac..2ac8f287 preserved patch ID650a3de9858e13ad91c7c980c705e5ee1cb6d835 and range-diff1=1. New default5447fac contains exactly three already-merged upstream commits: staging and production vpsAdminOS pins to7554720e640c763639a1ed207b1621143b483025, plus node RTNL watchdog consolidation. No aitherdev subtree/shared machine module/profile/environment or its selected nixos-stable/home-manager/llm-agents dependency changes were found. Exact new system output still requires build/evaluation; no host activation is assumed.

Final H regenerates one pin per repo to9241; no intermediate e962 pin remains. Strict full-graph reconstruction against each final base passes: only intended runtime identity changes, every other node/edge/follows preserved, upstream changes retained. Both locks select9241 with narHash `sha256-Be50ECDhDhL/Q0yAlkAIa2GrWVZgdZ8oIW1sZJaP6D4=`. Final lock hashes: workspace96ced7da8029c53ef17413d6fa244fbdb43f115b7b92689e72acd7be8be280a6; configuratione162ed9b2375487a460b6ee7b393b0f6a0595c6472113bf6734b785be9fabd1b. Extension/native/codex-web/llm-agents unchanged. Parity PASS0.09s, semantic graphs, Nix parse/whitespace, channel/selector inventory and normal configuration hooks pass. Generated history retained without width reformat. No migrations/deployed/merged/released feature heads.

Evidence: implementation.md and h-evidence.md (current final sections; historical old ranges retained). Original review.md/A1 decision unchanged; no product prose added. User integration approval remains for named defaults after verification; clean equivalent config rebase and mechanical pin advance stay within same scope. Independent conclusion on all final histories/graphs and supported verification reuse is required before readiness. Return report text via report_to_lead; lead saves review-update.md. No test/build/target/private-data/lifecycle actions or edits.
