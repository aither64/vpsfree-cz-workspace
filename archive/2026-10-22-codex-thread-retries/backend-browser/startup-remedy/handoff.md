# Browser fixture startup correction

Frozen B `e914c52a91d94192acd8368e77871b5a451196bd`, tree `0144e3dab9938553c09469b11e19c2fd9f967da0`, clean and SSH-published using exact c79 lease. Only `portal/internal/web/retry_backend_browser_test.go` differs from c79: the existing managed-client assignment now precedes `addPolicyMember`. `newTestServer` configures UserStateRoot but no Codex client; `addPolicyMember` calls real `teamService`, which refuses nil Codex. This explains the observed setup failure before Node on every variant. No additional authority tuple or product change is needed.

First14 commits exact; browser15 amended; separate service16 has exact prior patch. All581 other blobs/modes equal, including CJS assertions, shared/manual helpers, fork fixture, service, product, A5743/sole9ccb pin, docs and AGENTS. Complete16 series, full diff, c79 delta and old/new range diff accompany scope-proof.json. No migrations or repeated pin updates. Existing review conclusions are retained; lead owns narrow correction disposition and browser release.

Gofmt/diff and repository-Nix web compile-only passed 18.458s (web0.048s, no tests). Final tree equals the checked candidate. CJS remains byte-identical, so its previously passed syntax result retains exact input identity. Source metadata and all582 blob/mode checks plus independent NAR match final HEAD and complete committed input graph.

Original c79 dedicated tag, verified bundle, all33 packet artifacts and actual combined run remain intact (43 files rehashed). Browser actual exit1 before Node/no manifests remains failed evidence. Fork actual all21 PASS/31.243s/exit0 on c79 is retained and will not be repeated. No claim of package/native/browser success or deployment readiness.

`browser-command.py` is PREPARED ONLY for one lead-selected watcher: final-head/tree/session/clean and full Nix PATH/GCC guards, browser only360s JSON,5 test names/all32 manifest cases, zero skip/fail/missing, raw stdout/stderr/actual exit/elapsed and post-source receipt. Unique output `browser-attempt-2` remains absent at preparation. No owner browser/fork/pressure/native/package build/CI/live/integration/lifecycle operation.

No lasting docs or visible-copy update is useful: this corrects private disposable constructor initialization only; recovery and product contracts are unchanged. Lead maintains shared state.md and final W/C repin direction.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
