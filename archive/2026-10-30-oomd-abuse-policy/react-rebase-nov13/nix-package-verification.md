# Exact-source Nix package verification

Final clean source bbd820a65536564756484f6dd037f10224901b35,
tree90de7b671745233b8da012aa9d2b13d2e1b25332, after independent review and R1
lead closure. No application/source/lock/toolchain edits were made.

One standard native batch passed exit0 in 55.001s:

```sh
nix build --no-link --print-build-logs --json .#frontend .#bff .#checks.x86_64-linux.provenance .#checks.x86_64-linux.package-contents
```

Dry-run0 planned five bounded builds and nine substituted support paths
(863.2KiB unpacked); the frontend fixed-output npm cache was built, the BFF cache
and provenance check reused. No kernel/toolchain compilation or material
allocation expansion occurred. Managed utility capacity was authoritatively full;
visible active-parent fallback retained the turn through native67911 terminal0,
with all operation-owned subprocesses joined. No competing watcher was launched.

The six optional WASI packages without resolved URLs still produced warnings,
but the exact frozen x86_64 frontend install/build and installed-content check
passed. The actual frontend cache NAR hash equals the locked Q1g hash; BFF pifj
cache hash is unchanged. The ordinary Nix npm hooks installed frozen dependencies inside the build sandbox.
No separate worktree npm ci, local BFF npm install, unit/browser
rerun, CI polling, server, guest or image operation occurred. Local dist and
bff/node_modules remain absent.

## Output and provenance evidence

- Frontend: /nix/store/x6zkacrqqqgkyrd54cilmc67w5jqn36z-vpsadmin-webui-frontend-1.0.0
  (drv42aiw45dqk03pf8hlqj44p5pqm6alana).
- BFF: /nix/store/8azqqn8s5c4j693k25h8i3bhr7bsrr5w-vpsadmin-webui-bff-0.1.0
  (drvxdxiygy2dhiaxc0fsmqxl3q4r0ywwpjx).
- Provenance: /nix/store/p3vlsh9drr8mjjvahb4h4sy3r915n6sn-vpsadmin-webui-provenance
  (drvny33jynq7m66q5w6q4rxq4q5bqbigvxn).
- Installed contents: /nix/store/13a47s0cpg498sx8s9qfb3xxg7smra96-vpsadmin-webui-package-contents
  (drvw29mrn62fsk4ml435i3160cdyp9rbsh6).

Actual frontend build-info.json and BFF share metadata are equal: schema1,
fullbbd820a65536564756484f6dd037f10224901b35, shortbbd820a65536,
dirty:false, source:environment. Package contents verifies382publicassets and
matching full provenance, allowed public/runtime files, dependencies and wrapper.
Source-contents chg6pj remains the exact previously passed derivation and was not
rebuilt just to record it. Frontend's declared internal source audit also passed.

[nix-package-verification.json](nix-package-verification.json) contains complete
output paths, all NAR/metadata hashes, derivations, source identities, measured
allocated bytes and before/after disks. [Raw derivations](nix-package-derivations.json)
retain exact native inputs; [input summary](nix-package-input-summary.json) binds
cleaned source /nix/store/0a21iz636vjifl54dvpxyxnjwzs1ih5x-source, both npm cache
paths/hashes and frontend VITE_BUILD_SHA/dirtyfalse. Native command/result,
full logs/exits and elapsed files are adjacent.

The known frontend/BFF/cache allocated path sizes are6,516,736/6,123,520/
231,968,768 bytes (244,609,024B summed), plus small support/metadata. The reused
BFF cache is2,879,488B. Root available space increased from256,897,589,248 to
267,717,087,232B during concurrent host activity; no net physical recovery is
attributed to this build.

BFF direct Nix references include slimNode24.21, fullNode24.21 and Bash. The
unchanged BFF graph and installed wrapper passed the declared checks. Runtime
closure minimization was not audited, and no shell/full-Node absence is claimed.
No attempt to alter that independent packaging behavior was made.

Operational notes: the executor's default shell failed before any native
preflight started; explicit current /run/current-system/sw/bin/bash worked.
A summary reader initially expected old derivation JSON shape; native Nix command
itself passed0, complete schema2 raw output remained, and the reader was corrected
without repeating a package check. Ignored transient eval-cache busy messages
and Nix/npm/Vite deprecation/chunk warnings remain in raw/native receipts.

This completes the declared package proof for the existing development SDK
input. It does not publish a registry SDK, deploy either output or authorize
integration. Published registry artifact replacement before WebUI merge remains
mandatory. CI observation remains exclusively with lead.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
