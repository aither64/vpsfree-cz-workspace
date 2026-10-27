# Refreshed verification selection

The commands below this note describe the original old-base campaign. Preserve
its evidence with its exact heads/pin. Current new-base verification is prepared
in [verify-refresh.sh](verify-refresh.sh), following the exact pinned appendix in
[design.md](design.md). It accepts the final reviewed/remediated head as an
argument and requires a clean checkout. This substantive refresh needs new
package, Chromium+Firefox, admission/HTTP and private native recovery evidence.
R5 final fold/direct history inventory precedes launch; no stale old result is
claimed as verification of the refresh.

---

# Post-review verification

Prepared, not executed. Run `verify-local.sh` only after final review findings
are resolved/accepted. Tested source starts at final review head
`45deeeacf119eb733852a5df21abd6e030262e26`; original reviewed head and
remediation ranges are retained in the review packets. Bind any further head
change before run.

A fresh managed `gpt-6-luna`/low verification watcher launches the related local
batch, retaining the command handle and per-step complete logs/exit files.
Pinned catalog `840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa`,
full-access execution, native utility
`dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12`.

The exact prepared shell script is `verify-local.sh` in this directory:

1. Evaluate all repository flake checks without building.
2. Build the exact CI fast selection from `.github/workflows/check.yml`, excluding
   its four separately scheduled host/archive/creation VM checks.
3. Run `TestQuestionBrowser`'s composer-handoff and paging live scripts with the
   locked nixpkgs Playwright 1.59.1 and Chromium, against disposable TLS fixture
   state. These use real portal templates/assets/uploads with mocked Codex/API.
4. Run pinned codex-web `TestPinnedCodexRecoveryRemainsColdUntilActivation` with
   the repository's selected native binary and private daemon/home/provider.

No selected-package activation, live session/cluster mutation or host restart.
Unexpected local Linux kernel build is an escalation: cancel the exact owned
verification batch and report; don't bypass cache expectations. Quiet logs are
not a timeout. Preserve raw failure logs; parent/implementers diagnose and decide
reruns. No retry/source edit/deployment/acceptance by watcher.

The native regression proves cold activation/recovery/queued FIFO; it does not
prove consumption order of multiple steers before model processing or execution
order across external writers. Browser tests establish ordered HTTP dispatch.
No protocol change is proposed to expand that contract.

After successful local evidence, publish SSH feature branch only and inspect its
exact-head CI workflow. Integration needs explicit repository/target direction.
Archive/recovery VM remains a future pre-deployment gate per repository README.
