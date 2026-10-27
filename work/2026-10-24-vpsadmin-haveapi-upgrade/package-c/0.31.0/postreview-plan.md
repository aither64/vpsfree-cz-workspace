# C4 released postreview plan

Lead accepted reviewer0's exact5a..baf four-lane final review without findings.
Run only in registered successor `worktrees/<session>/vpsadmin-webui-031`,
head `baf00acc31d34ab37720643c5833b4476a341f3b`, tree
`2e7b4cb5eba6bc96f34f834c49fc097d5fdd987b`. Original LIVEf10/PR74/PR63,
cluster and all old refs remain untouched. No quick/review repeat.

A0 owns the sole utility slot: visible parent-monitor fallback, no competing
watcher or wait for capacity. Each command has one owned handle, full separate
log/exit/elapsed. Command affinity62-63, nice10, Nix maxjobs1/cores2, browser
2workers/0retries. Available memory/disk and exact source/hash/clean state must
pass before each batch. Expected5-15min tests/build,5-15min package realization,
1-4min bounded browser; these are estimates, not cancellation deadlines.
On actual failure stop, retain evidence and diagnose before any retry. Stop an
unexpected actual owned kernel build; modules/initrd evaluation alone is not one.
No foreign signals, runtime/profile/host/collector/policy changes.

1. Existing locked `nix develop -c bash -ec`:
   `npm ci --prefix bff --no-audit --no-fund` (BFF dependencies are absent in new
   successor; lock/source unchanged), then `npm run ci:tests && npm run build`.
   No root npm reinstall. Require build-info exactbaf/dirtyfalse and BFF mode.
2. Ordinary `nix build --out-link <records>/nix-result --json --print-build-logs`
   selects `.#frontend .#bff .#checks.x86_64-linux.provenance
   .#checks.x86_64-linux.source-contents .#checks.x86_64-linux.package-contents`.
   Normal output roots retained; source/toolchain roots already exist. Capture
   complete flake locks, drv/output/NAR/reference/recursive input identities.
   Require matching frontend/BFF metadata exactbaf/dirtyfalse; contents check
   binds package boundary. No NixOS VM/system/whole-platform campaign.
3. Bounded browser proof is useful because the actual dependency bundle changed:
   only `authenticated_home_smoke.spec.ts` (2cases) and
   `session_expiry_redirect.spec.ts` (1case), both chromium/mobile-chrome:
   exactly6cases,2workers,0retries. Covers real bundled XHR/auth headers,
   configured no-description path, expiry→public isolation. Existing rooted
   standard FHS/Playwright1.61/Chromium1228/ffmpeg1011, no runtime/browser swap
   or policy flags. Verify current root/closure/binary identities before use;
   list exactly6 first, then native Playwright server at free loopback52847,
   CI1/no reused server, same90s test/15s expect/120s server timeouts, retained
   failure artifacts and separate JSON. No live OAuth or member mutations.
   Reconcile owned Vite/browser/port and roots/closure/source after run.

Stop after these pass and reconcile; preserve old60/62 and specific2preexisting
mobile expansion failures as historical residual, without a clean62claim. No
new layout tests/fixes or full API/VM campaign. Ordinary own NEW branch publication
released conditionally by lead after allpasses: freshfetch canonicalmain5a,
absent/exact ownref, cleanhead/hooks/SSH and comparison capture; explicit one-ref
no-force push only dev/vpsadmin-haveapi-031, remote/default/protectedhead proof,
bounded exact-head CI discovery. Protected PR74 rewrite/defaultmerge/livecluster
redeploy remain separate lead/E3 actions, never implied by this batch.
