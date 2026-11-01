# C bounded browser runtime recovery plan

Prepared only; no setup build, package installation or corrected browser execution
has begun. Lead requested a concrete plan before corrected execution. Source
f10d3d48c4f21cc39187c3667ffffd9952404c11 remains clean and unchanged; passing
unit/normal frontend/Nix package checks remain valid. Failed batch3 evidence is
preserved, with all62cases classified as pre-application launch failures.

## Guidance and rejected routes

Read current repository AGENTS, flake, scripts/playwright.mjs,
scripts/e2e-harness.mjs, scripts/playwright-cli.mjs, playwright.config.ts,
docs/design/DEVELOPMENT.md, docs/spec/CI_AND_TESTING_WORKFLOWS.md and native
smoke CI. The normal route is installed pinned Playwright with managed browsers.
The declared --container convenience mode selects system Chromium, disables
artifacts by default and relaxes URLBlocklist policy; it is not a same-browser
NixOS runtime. No system Chromium exists in PATH. Do not use it here.
Locked nixpkgs' packaged Playwright browser is1217/147.0.7727.15, while actual
pinned1.61.0 requires1228/149.0.7827.55; do not substitute that packaged browser.

## Proposed environment only

Session-local playwright-fhs.nix uses locked nixpkgs
5e2305d577ca00acbba631b05cb1094d172b29f3 from the immutable reviewed WebUI flake.
It uses standard buildFHSEnv (bubblewrap),64-bit only, native Node24 and browser
libraries following that nixpkgs' Chromium/headless runtime dependencies.
Glibc supplies /lib64/ld-linux-x86-64.so.2 inside the process namespace, resolving
the observed stub-ld failure. Browser files are neither patched nor copied.
Include fontconfig/DejaVu and native graphical/runtime libraries; no browser
package, host nix-ld or system configuration. Existing /etc/chromium and
/etc/opt/chrome policy directories are bound read-only if present, rather than
masked/modified; both are currently absent. No extra Chromium/security flags.

Expression SHA256 f4b059bcea99fea56c2ad62943427bf2ce82c62b188ba52da1ee3aeb4e866b21.
Evaluated candidate drv:
/nix/store/yv2k1knikln9b4fk6jprv6h80473w60m-package-c-playwright-fhs.drv
Expected output:
/nix/store/yrvkph1ivq0gf80p5b4rvjf9lfz4iakw-package-c-playwright-fhs
Only evaluation performed; no realization. fhs-candidate-identity.json records it.
Original cached headless executable SHA256:
670ba079b75107746ba41abad131180a31a7c7219aa1bd4061fb471f4535d541.
Installed browsers.json records1228/149.0.7827.55, ffmpeg1011; full identity in
browser-original-runtime-identity.json. Require those bytes and package pins
unchanged immediately before/after execution.

## Exact conditional execution proposed to lead

Continue authorized parent-monitor fallback while A holds the single watcher.
Use separate named handles/logs/status/time, CPUs60–63/nice5, Nix1job/2cores,
waits<=60s. Recheck current head/tree/all recorded hashes, clean index/worktree,
capacity>=8GiB available and free local52847. Never touch foreign processes.

First realize only this environment, no source build repeat:

```sh
nix build --file /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-vpsadmin-haveapi-upgrade/package-c/0.30.2/playwright-fhs.nix \
  --max-jobs 1 --cores 2 --no-link --json \
  > /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-vpsadmin-haveapi-upgrade/package-c/0.30.2/fhs-build-results.json
```

Capture complete recursive wrapper derivation/closure and NAR/output identities.
Require expected drv/output, pinned input and no kernel build; unexpected kernel
build stops/escalates only this owned setup command. No arbitrary build timeout.
Inside that wrapper run the prepared smoke probe, preserving native status:

```sh
/nix/store/yrvkph1ivq0gf80p5b4rvjf9lfz4iakw-package-c-playwright-fhs/bin/package-c-playwright-fhs /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-vpsadmin-haveapi-upgrade/package-c/0.30.2/fhs-runtime-probe.sh
```

This only asks native Node/unchanged cached Chromium/ffmpeg for their versions;
no app tests, browser flags, server or live account. If setup/probe fails, retain
evidence and diagnose/report before proceeding. No automatic second attempt.

Only after successful setup/probe, run the prepared exact command file:

```sh
/nix/store/yrvkph1ivq0gf80p5b4rvjf9lfz4iakw-package-c-playwright-fhs/bin/package-c-playwright-fhs /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-vpsadmin-haveapi-upgrade/package-c/0.30.2/browser-fhs-command.sh
```

browser-fhs-command.sh retains the accepted nix develop/Node/repository runner,
all nine explicit existing fixtures, chromium+mobile-chrome,2workers,0retries,
CI1,52847and local native Vite lifetime. It clears inherited system-browser,
artifact-suppression and policy-relaxation options and explicitly retains
artifacts. Outputs change only to browser-fhs-results.json/browser-fhs-artifacts
so failed original batch3 evidence cannot be overwritten. Full command is in
that candidate file; no fixtures/production source/config edits.

Reconcile every native handle, Vite/browser descendant and local listener before
reporting completion. Classify actual app failures separately from setup. Stop
and report failures before rerun or source changes. Preserve full logs, hashes,
counts and limits; no live OAuth/member calls, publication, PR mutation, deploy,
merge or session lifecycle action. No overall browser pass before actual results.
