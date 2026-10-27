# Final vendor dependency failure: read-only diagnosis

Prepared by implementer2 for architect0 and lead. This is diagnosis evidence; cache restoration and retry have not run.

The forced final target rebuild failed before its own build phases. Eight of the nine selected dependency outputs are valid locally; only the selected Git output is absent/invalid. All nine input drv files are valid, demonstrating why drv presence is insufficient. The existing fixed output remains valid and is not a fresh vendor pass.

## Exact selected dependencies

Every path below is absolute. `allDeclaredOutputs` in `receipt.json` also preserves unselected output names/paths. Only the selectors below belong to target xcl.

| Input derivation | Selected name | Declared selected output | Current local status |
| --- | --- | --- | --- |
| `/nix/store/324jiy1aizlwmqhfvj8w7cxbkybwj6lw-git-minimal-2.54.0.drv` | `out` | `/nix/store/g14fri80i39za36cqhi5pxrprnwp0kaj-git-minimal-2.54.0` | invalid / absent |
| `/nix/store/773919n1zvj8z1v6yr53j218gs5pgz1l-bash-5.3p9.drv` | `out` | `/nix/store/rzl7zd3zx56vl7m55x1l49sr4xx2bb7y-bash-5.3p9` | valid / exists |
| `/nix/store/8q2z94mf32mv0j8wxlsshm805xlfysi9-workspace-repository-review-assets-1.0.0.drv` | `out` | `/nix/store/hllcfkaav40y98j1v7vl3gkikgpd0w75-workspace-repository-review-assets-1.0.0` | valid / exists |
| `/nix/store/i3c2bk0rsdk4ifyz6cvihwq643n36zrx-nss-cacert-3.126.drv` | `out` | `/nix/store/206m56yfhycp91zp3y6ry3ddirqflnxs-nss-cacert-3.126` | valid / exists |
| `/nix/store/p4m7f8xxk3c5wv00z01av8078aqjbayw-jq-1.8.2.drv` | `bin` | `/nix/store/vkjzswzi7r1ayxa0xr920bjrzmi04x7v-jq-1.8.2-bin` | valid / exists |
| `/nix/store/v7lwwcrmm66pmwhs7zyn2cv7y5gqh0sq-stdenv-linux.drv` | `out` | `/nix/store/843sqza79ns6k8n7sykxwmy04s741jzn-stdenv-linux` | valid / exists |
| `/nix/store/vqn9gw6ja6jwypif4hpcy9ygjnzzbg94-bash-interactive-5.3p9.drv` | `out` | `/nix/store/pkf547jp8a92k4wmxikkyby58w10pysr-bash-interactive-5.3p9` | valid / exists |
| `/nix/store/xgkymsj1lx0fr3dqrbmx4ljg237y0f16-go-1.26.6.drv` | `out` | `/nix/store/3yh8g6m3balbhzxsx77jlyyx443bxqii-go-1.26.6` | valid / exists |
| `/nix/store/xshd860gif707cn5krzl14260ash8c02-make-shell-wrapper-hook.drv` | `out` | `/nix/store/bnpp6hwrlvcdyijh5fpqyn13m11sy8rp-make-shell-wrapper-hook` | valid / exists |

The runtime-requisite union of the eight valid selected outputs contains 73 exact store paths. The bounded query and validity check exited0; every path exists. These are runtime closures of those outputs, not the complete build-time dependency graph. Missing Git has no locally observable valid runtime closure. No broad closure/global store discovery was performed.

## Source and target identity

Target: `/nix/store/xcl55br6w0piydf9dap79pwmp1jgjpzk-dev-workspace-0.2.0-go-modules.drv`, raw SHA256 `ffef7e12d5e119a74b8271dc019a4c5d69a35281216402690857f0a7c8d30ba5`. The frozen v4 JSON selects exactly three direct source inputs:

- `/nix/store/alhmfv9zw2j0p12hifm83vpxw4imzn23-source`: valid/exists; actual current NAR `sha256-U0nvYqqpbToyaBuT7otTMedVCBpPtxDI87CuMtc4OY8=`.
- `/nix/store/l622p70vy8k5sh7y5wizi5f2mic6ynpg-source-stdenv.sh`: valid/exists; actual current NAR `sha256-XtbkqLpGD+LK0h01ReriTG6AVfz98JBx+BNFGm+eVM0=`.
- `/nix/store/shkw4qm9qcw5sc5n1k5jznc83ny02r39-default-builder.sh`: valid/exists; actual current NAR `sha256-g4iylkzyVczW3+hTZHknt6RNO9WDF1+TK5lVxU2GYjk=`.

Published client `02533a152223416f159bac2578e88bcbe653f247`: `/nix/store/cfjj8pdplzk3vw154wk1ab9cc10kx9mk-source`, valid/exists; current actual NAR `sha256-f5AjJntJvsRGb8ocU6yGQOW+FYhK0TGoYzS3w4gSVbs=`. Both runtime and client current NARs match the retained stage07/08 values and accepted source certificate.

Existing output `/nix/store/lg6qgishdvazi9xz6giji5zhhjb4zzsg-dev-workspace-0.2.0-go-modules` is valid/exists. Stage09 already lists xcl among three valid producer registrations, before this failed rebuild; registration therefore cannot certify target execution. No new vendor SRI/content proof or PASS was produced.

## Actual failed execution

Retained outer7837: settled CLI0, runner1; 11 actual stages, first 10 exit 0. Target `forced-final-rebuild`: exit1, 25.461134472861886 seconds. Exact argv from actual stage receipt:

```json
[
  "nix",
  "build",
  "--no-link",
  "--rebuild",
  "--print-build-logs",
  "/nix/store/xcl55br6w0piydf9dap79pwmp1jgjpzk-dev-workspace-0.2.0-go-modules.drv^*",
  "--option",
  "allow-import-from-derivation",
  "false",
  "--option",
  "substitute",
  "false",
  "--option",
  "builders",
  "",
  "--option",
  "accept-flake-config",
  "false",
  "--option",
  "flake-registry",
  ""
]
```

The option overrides bind `allow-import-from-derivation=false`, `substitute=false`, empty builders, `accept-flake-config=false`, empty flake registry. No max-jobs0 override was present. Global substitution disabling also affected missing dependency outputs; existing outputs were reused but missing Git caused its build-time graph to be pursued from source. The missing-bootstrap builder message is not a cache availability observation under these settings.

The retained stderr contains 121 `building` lines and 65 `Cannot build` entries. It first reports stage0 builder exit1 at lines240–288, then propagated dependency refusals; Git fails at540–544 and target at545–548. It has no target `building xcl` or target phase lines. No final `go mod vendor` phase occurred.

One exact declared path through derivations named in that failure log is:

- `/nix/store/xcl55br6w0piydf9dap79pwmp1jgjpzk-dev-workspace-0.2.0-go-modules.drv` → `/nix/store/324jiy1aizlwmqhfvj8w7cxbkybwj6lw-git-minimal-2.54.0.drv` selects `out` = `/nix/store/g14fri80i39za36cqhi5pxrprnwp0kaj-git-minimal-2.54.0`.
- `/nix/store/324jiy1aizlwmqhfvj8w7cxbkybwj6lw-git-minimal-2.54.0.drv` → `/nix/store/5z8sj1169xaps07s9yw780fvznwn8yqy-pkg-config-wrapper-0.29.2.drv` selects `out` = `/nix/store/cizqnkc40i7k401f8cl2260ksi9nnph4-pkg-config-wrapper-0.29.2`.
- `/nix/store/5z8sj1169xaps07s9yw780fvznwn8yqy-pkg-config-wrapper-0.29.2.drv` → `/nix/store/906f0r5yx85527y5bwqfd89mn8zksidw-stdenv-linux.drv` selects `out` = `/nix/store/mhmv0p4sqvfxsyxx58y6qx9zqfzyas1w-stdenv-linux`.
- `/nix/store/906f0r5yx85527y5bwqfd89mn8zksidw-stdenv-linux.drv` → `/nix/store/pz3m6g7iabylyazm40p363y8795vybf9-mescc-tools-1.9.1.drv` selects `out` = `/nix/store/53zd871rgpcvi7qmqkffxhzaiq0is7k4-mescc-tools-1.9.1`.
- `/nix/store/pz3m6g7iabylyazm40p363y8795vybf9-mescc-tools-1.9.1.drv` → `/nix/store/2kbbzfsz1hzd21yj0h989s3z40cgrp58-stage0-posix-1.9.1-source.drv` selects `out` = `/nix/store/4f7nm8dblrdy74gmsl62b25rjrh4jcz3-stage0-posix-1.9.1-source`.

Each edge is taken from raw declared input selections, with raw hashes/output declarations retained in `retained-failure-chain.json`; log ordering alone was not treated as an edge. This is one sufficient route, not an exhaustive build graph inventory. The terminal `/nix/store/4f7nm8dblrdy74gmsl62b25rjrh4jcz3-stage0-posix-1.9.1-source` is currently absent/invalid. The builder executable is a deliberately diagnostic text referring to unavailable bootstrap sources; no attempt to bootstrap them is proposed.

Partial unrelated work remains preserved: `expand-response-params` reaches fixup/strip in lines65–77 and its exact output `/nix/store/10ypd8q9arjlbyx5d8188dyjd06ffji1-expand-response-params` is currently valid. No before-snapshot proves first creation by this attempt. `byacc` reaches buildPhase, but the log has no completed install/fixup or per-derivation exit; no successful completion inferred. Source downloads time out for tinycc/config.guess/config.sub at237–239. No cleanup occurred.

## Cache availability and standard method proposal

Cache availability is **UNKNOWN**. The inspected receipts record no meaningful cache availability/substitution result for missing Git or its runtime closure. No cache request, cached metadata query, evaluation, realization or restore ran during diagnosis. The stage0 diagnostic does not prove cache absence because substitutes were globally disabled.

Installed Nix2.34.9 documentation was read and retained without invoking build commands:

- `nix build --help`, lines149–152: `--rebuild` rebuilds an already-built package and compares existing output paths.
- `nix-store --help --realise`, description: a **non-derivation output-path** argument attempts to substitute that path/closure and fails when no substitute is available; a drv argument can recursively build missing prerequisites.
- Same manual, `--check`: rebuilds the specified derivation and compares its already-existing outputs. `--ignore-unknown` would silently ignore missing non-derivation substitutes and must be absent.
- `man nix.conf`, substitute: false forces source building; fallback=false refuses source fallback after failed binary substitution. Merely disabling fallback does not prevent builds when no substitute exists for a drv request.
- `man nix.conf`, max-jobs:0 disables ordinary local builds but explicitly excludes preferLocalBuild=true derivations. max-jobs0/empty builders alone are insufficient as a universal no-build boundary; the non-derivation output-only request is essential.

Minimal proposal for architect disposition (prepared description only, **not executed**): request only the missing exact non-drv `/nix/store/g14fri80i39za36cqhi5pxrprnwp0kaj-git-minimal-2.54.0` via ordinary `nix-store --realise`, with substitution=true, fallback=false, max-jobs0, empty builders and existing trusted cache policy; no drv arguments, force-realise, ignore-unknown, remote builder or source/toolchain fallback. That restores only the requested output and its necessary runtime closure or fails explicitly if unavailable. Keep selected-output/closure evidence and register fresh explicitly owned retention roots through the standard separately authorized add-root recipe; preserve all 17 historical roots. Retain all nine selected outputs and the already-required sources/target output against GC before the separate final command. Architect owns exact availability/restoration/retention recipe and authorization.

Only after dependency success, retention and all unchanged source/tool/guard checks, run one separately evidenced actual requested xcl rebuild in a fresh results directory. Require target start/own phases, actual exit0, exact producer/output/SRI and 22-module/52-file content proof; dependency restoration or the existing lg6 output is not a pass. Any availability/final identity failure stops without bootstrap/toolchain retry. No source diagnosis or Ruby-loader work is duplicated.

## Scope and preservation

All 2483 frozen input expectations, runner/ready/manifest, accepted605b certificate and original failure/logs remain byte-identical. The 17 declared roots received no mutations; their prior standard root receipts remain preserved. No global/current roots query was issued. Current observations are timestamped snapshots and make no guarantee against later independent GC. No store/root/database mutation, eval/instantiate/realise/build/fetch/substitute/repair/retry/test/Git/native/claim/lifecycle operation ran. The frozen command had already exited; no further background-effect inference is made.

One diagnosis mistake is explicit: an initial validity query used a guessed incorrect bootstrap suffix. That irrelevant result is preserved as `discarded-wrong-bootstrap-path-query.json`, excluded from all conclusions, and corrected using the exact retained log/raw drv identity. It was a read-only existence/DB query.

The lead owns state.md and all broader records. This evidence-only package needs no product source change or standalone mandatory review. Final receipt binds immutable inspected packet inputs; package hash list binds the supporting observations and documentation.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
