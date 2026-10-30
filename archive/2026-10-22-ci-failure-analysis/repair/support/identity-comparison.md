# First-switch diagnostic identity boundary

Batch3 passed without realization/VM, 2026-10-22 19:26:36–19:27:57 UTC.
Authoritative files report support41s, original35s, recursive graph4s, all exit0.
The lead's initial message transposed the two query durations; the receipt files
are authoritative. The corrected CLI path context resolved batch2's refusal.

## Three distinct targets

| Evaluation | Target output | Target osctld output |
| --- | --- | --- |
| Preserved incident receipt | `gnf7wyg9p1yjvgfihm1d4056xy08mwmp-vpsadminos-system-vpsadminos-26.05.git.846bb46` | `5ya177sxjk8w3i9l1xrrl011nkjfg6ja-ruby3.4-osctld-26.05.0` |
| Recomputed unmodified original fixture | `ja0vpvv9g1p3vymwd23a9lzfzjb14rzx-vpsadminos-system-vpsadminos-26.05pre-git` | `63mrvm06mq7nbc1n59ph3daqm2hnqk0d-ruby3.4-osctld-26.05.0` |
| Selected first-switch diagnostic | `3nl6c9yx07skwfid44dd95xbzm8wvcr3-vpsadminos-system-vpsadminos-26.05.git.846bb46` | `63mrvm06mq7nbc1n59ph3daqm2hnqk0d-ruby3.4-osctld-26.05.0` |

Every basename in this document is beneath `/nix/store/`. Recomputed original
is not the original incident binary graph. Incident target/gem derivations and
the original source transport output are unavailable locally; the previously
checked public-cache entries returned404. No further historical recovery is
needed for this bounded experiment. Their difference remains explicitly unknown.

## Exact comparison of the two reproducible graphs

Inputs: [support graph](native-input-derivations.json), SHA256
`5b6467774b7799dba5ecc165089a4a47680e8bda8df993f7e99e07cd11ad831a`,
and [recomputed original graph](preflight-batch3-original-input-derivations.json),
SHA256 `398e49a6a4a7ba05ce93ea05fe94b2851d90ccb9f859030526191a679ee8e114`.
Each has5794 nodes.5779 have identical keys and complete JSON objects, not only
equal names. The15 replacements below account for every differing node.

| Support drv prefix / role | Original drv prefix | Difference |
| --- | --- | --- |
| `0fz8if5x` local-cmds | `65qyx1cb` | Target boot log version string |
| `3g7fnsjz` vpsadminos-version | `a7yd2h3j` | Revision/version substitutions and corresponding unsubstituted-token check |
| `s88f9yna` etc-os-release | `1xksy8nw` | BUILD_ID |
| `vfwgagzz` security-evidence.json | `d9jj4g4q` | revision and version fields only; kernel, source config and sysctls identical |
| `x5lfc8j0` target toplevel | `kd7raqfi` | Label/name and references to changed generated metadata/environment |
| `0pan9w2x` os-version | `sh5gqrxp` | Version utility reference |
| `5kvsvpvg` system-path | `dcllgdg3` | Version utilities in structured package list |
| `dfcigm8q` stage-2-init | `l6q037xk` | system-path/local-cmds references |
| `skz3rcnb` system-crontab | `wqa4yc9s` | system-path PATH references |
| `ldhjn870` crontabs | `q2shiipz` | system-crontab reference |
| `i5kdvf7a` etc | `mf5pb1dy` | Changed metadata/crontab/system-path references |
| `6qdsyp8a` predecessor toplevel | `n38m5k92` | Only extraDependencies target reference and output path |
| `pxm9rylc` closure-info | `hql65k1n` | Retained predecessor root reference |
| `09pfjczv` squashfs | `59dr7nbz` | closure-info reference |
| `3k70877r` native test JSON | `v536gp96` | Diagnostic name/tags, bounded recorder/stop script and propagated machine/target paths |

Replacing paired drv/output references in each complete node leaves only the
five explicit metadata/label rows and native test JSON with differing values.
All source inputs for the14 non-JSON pairs are identical. This comparison
includes structured attributes and full input references, not just env text.

The cause of this *reproducible* metadata difference is explicit in846bb
`flake.nix:171–213`: direct immutable GitHub flake evaluation supplies self.rev;
the unmodified fixture's `getFlake (toString ../../..)` evaluates a local store
path without that revision metadata. `.vpsadminos-git-rev` is not the system
version source. Its marker alone was insufficient, motivating the approved
diagnostic-only exact target override. Both evaluations now use the identical
osctld recipe `lchcx9yc6fik7xm7vlbz331y5b0ynwy3-ruby3.4-osctld-26.05.0.drv`,
including inputs, source and postPatch; this does not establish equivalence to
the missing incident `5ya...` recipe. Whole-repository source packaging at
`os/overlays/osctl.nix:8` and `os/packages/ruby-source-gem-config.nix:30` makes
source-bundle identity relevant, but its exact incident difference is unknown.

The original and support native machines are otherwise identical after their
propagated toplevel/squashfs paths: one8192MiB guest,4CPU cores in1socket, one10G
managed file disk, user network, one test shell; equal kernel/initrd/QEMU and
all other machine fields. Boot kernel remains `ii8f7mj2a82cjvx0f84pjpz31lncpnxv-linux-6.12.95/bzImage`
and initrd `3jcr32gn651ppxk7hqpj1ic53v1q04c0-initrd/initrd`. Target configuration
describes6.12.113 but activation does not replace the boot kernel. Both
predecessor graphs use unchanged old osctld `41f5fkvymy4pcln8gvd134mggp61fsr1`;
their toplevel changes only because it retains the selected activation closure.
There is no target test-shell/transport recipe change between these two graphs.

## Selected boundary and preparation

Recommend selecting the support graph as an explicitly newly packaged846bb
target, with the immutable3cc31e39 predecessor writer/kernel and frozen
846bb archive plus four support-only overlays. No writer274e826 or reader repair
is included. Source/lock/overlay proofs remain in [baseline source](baseline-source.md)
and [diff](baseline-support.diff). This can establish actual stale saved YAML,
GC ownership and live root/process/marker facts across first import in this
declared execution. It cannot prove incident-exact binaries/images, exclude an
additional incident contributor, or exonerate generic service interactions.

Selected rooted drv:
`/nix/store/3k70877r1v12vgd90ml599ya02wxs5zj-os-test-upgrade-from-6.12-guests-first-switch.json.drv`.
Native root: `/tmp/ci-failure-analysis-2026-10-22/support/gcroots/config.drv`.
Expected output: `/nix/store/hd3by52cz1wrza2k28av89iflad1j4ly-os-test-upgrade-from-6.12-guests-first-switch.json`,
whose SHA256 must be `ad0f136d98a6e0e59ddf3c38facc1acf0846cc2e0bde0fd10295487b2ff86adf`.
The second `gcroots/original-config.drv` remains rooted for this comparison.
Neither root was removed; no cleanup or lifecycle action was taken.

Lead accepted the boundary and selected bounded local preparation. The current
executable procedure is [run-local-preparation.py](run-local-preparation.py),
documented in [brief](brief.md), with kernel substitution first, plan allowlists,
deadline, resource/output guards and actual measurements. It remains unexecuted
by implementer3. The realization primitive inside that procedure is:

```sh
nix-store --realise /nix/store/3k70877r1v12vgd90ml599ya02wxs5zj-os-test-upgrade-from-6.12-guests-first-switch.json.drv --add-root /tmp/ci-failure-analysis-2026-10-22/support/gcroots/config.json --indirect --max-jobs 2 --cores 4 --builders '' --option fallback false --option allow-import-from-derivation false --option max-build-log-size 16777216
```

Before it, refresh `nix-store --realise <same-drv> --dry-run`, keep the exact
logs, and refuse new local-build derivations outside the previously inspected
216 in [preflight-build-drvs.txt](preflight-build-drvs.txt). These216 contain no
Linux/ZFS source compilation; module/empty-directory assemblies are expected.
If shared GC changed the needed build set, report rather than silently building
a kernel. Lead's watcher owns any realization and may stop its exact command on
unexpected source compilation or reserve-floor breach. Realizing this JSON
builds/substitutes referenced closures and the squashfs, but starts no runner/VM.
It avoids reevaluating mutable checkout/flake paths. Host launcher preparation is
separate: the snapshot's `test-runner.sh` can still build its flake runner before
execution, so do not call the VM launch fully prepared solely from this JSON.

24GiB remains the accepted provisional total incremental budget including the
future10GiB managed disk. Recheck free-minus24GiB above40GiB before preparation;
record before/after free and physical owned du. After successful realization,
hash the output JSON, read actual `57g5dsl6kczrp504h512l2igyzxx1q2r-closure-info/total-nar-size`,
measure squashfs apparent/allocated bytes and full output closure physical du,
and confirm every kernel/target/gem identity before any VM. The source snapshot
and both roots remain owned/retained until dependent work ends; no global GC.
