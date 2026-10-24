# Recovery display: silent index loading candidate

Immutable candidate only. Base B is
`965aadc51dfb4a7d838a401b20ecafa38c8a70db`; intended source boundary is only
`portal/internal/web/recovery_display_browser_test.cjs`. Nothing was applied to B,
its index or refs. No syntax check, test, probe, browser, build or CI wait ran.

The accepted design and shipped membership group intentionally keep routine
index loading silent. The single obsolete expected loading sentence becomes
an empty-text assertion plus a hidden assertion. The existing `runFor(1)` stays
on its line; `runFor(749)`, applied snapshot/read synchronization, stale warning
29999/30000 timing, healthy-snapshot clearing, immediate HTTP403 and every earlier
receipt/timestamp/storage/saved-ID/attachment/transcript/reload check are
byte-unchanged. No time budget, product, documentation, mock, cache or pin change.

`candidate-manifest.json` binds the exact base and candidate file hashes and patch
hash. Construction checks require one exact replacement and prove that undoing
only it reconstructs the whole original file byte for byte. This is construction
evidence, not verification. Keep prior candidate directories and the failed965
receipts under `../../browser-corrected-965aadc5/watcher/` unchanged.

After the parent's explicit serialized source/Git transfer, validate the base
file hash from the manifest, then apply only this patch in B:

```sh
git apply /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/browser-failures-imp3/recovery-loading-candidate/recovery-loading.patch
nix develop --no-update-lock-file -c node --check portal/internal/web/recovery_display_browser_test.cjs
git diff --check
```

Fold into the owning membership group (`7d9392e6` lineage) if practical, preserving
other owners' changes and prior refs. The parent owns final narrow inspection,
tracking and runtime acceptance. No new contract or migration is proposed.

After the correction is committed, the parent's fresh Luna utility can run the
actual two-engine fixture with the same pinned PW1.59.1/Chromium1217/Firefox1511,
`PORTAL_BROWSER_TEST=1`, absent-provider environment and review-assets overlay:

```sh
nix develop --no-update-lock-file -c go -C portal test -mod=readonly \
  -overlay /tmp/portal-followup-browser-assets-overlay.json ./internal/web \
  -run '^TestQuestionBrowser$/^recovery_display_browser_test[.]cjs$' \
  -count=1 -timeout=5m -v
```

A fresh launcher must guard the committed successor head and clean tree; the old
exact965 launcher remains immutable. The parent may include this in a converged
full-suite run instead. HTTP403 display, final page-error assertion and complete
two-engine recovery acceptance remain unverified after the retained stop.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
