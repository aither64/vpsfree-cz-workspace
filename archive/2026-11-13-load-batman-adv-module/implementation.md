# Package I: default batman_adv loading

Ready for lead acceptance and independent final review. Implementer0 owns this
evidence and the single source change. Design: [design.md](design.md), accepted
by the lead under the bounded-small-edit brief. No design deviations.

- Repository/worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-load-batman-adv-module/vpsadminos`.
- Branch: `2026-11-13-load-batman-adv-module`; target: `origin/staging`.
- Base: `eedc1254d309cac861cb0f7af080ee8de8296506`.
- Final head: `6d5f63697d2f87c817329d6731b7dd0bedd0b6e0`.
- Change: `os/modules/config/kernel.nix`, one insertion: `"batman_adv"`
  between `autofs4` and `blowfish_common` in the existing default list.
- Worktree/index clean after commit. Source and Git/index/commit window finished.
- Committed 2026-11-13 09:23:51 UTC. No push, deployment or merge performed.

## Bounded checks

All checks passed against the source now committed at the final head. No module
was loaded into the development host; no kernel or OS build was launched.

| Check | Result |
| --- | --- |
| `nix develop --command nixfmt --check os/modules/config/kernel.nix` | Passed; also repeated immediately before commit in the same repository shell. |
| `nix-instantiate --parse os/modules/config/kernel.nix` | Passed; repeated in the repository shell before commit. |
| `git diff --check` and committed base-to-head `git diff --check` | Passed. |
| Default QEMU system evaluation before/after, with IFD disabled | Passed: exactly one `batman_adv` addition, no other list changes; autoload remains false; kernel/config/nixpkgs/kmod paths unchanged. |
| Cached config and `modinfo` | BATMAN_ADV=m; dependency metadata available, as detailed below. |
| Selected cached kmod `modprobe --show-depends` | Passed with empty host configuration; every returned module file exists. |
| Normal hooked `git commit -F /tmp/2026-11-13-load-batman-adv-module-commit.txt` under `nix develop` | Nixfmt pre-commit and all commit-msg hooks passed. TextWidth issued advisory >72-column warnings; maximum line width 76 complies with the repository's 80-column limit. No hooks bypassed. |

Evaluation command (run at the base, then after the one-entry edit; JSON compared
to establish the exact list difference and unchanged fields):

```sh
nix eval --json --option allow-import-from-derivation false --impure --expr '
  let
    f = builtins.getFlake (toString ./.);
    s = f.lib.vpsadminosSystem {
      system = "x86_64-linux";
      modules = [ ./os/configs/qemu.nix ];
    };
  in {
    modules = s.config.boot.kernelModules;
    autoload = s.config.boot.kernel.moduleAutoload.enable;
    version = s.config.boot.kernelPackage.version;
    kernel = s.config.boot.kernelPackage.outPath;
    config = toString s.config.boot.kernelPackage.configfile;
    nixpkgs = toString f.inputs.nixpkgs.outPath;
    kmod = f.inputs.nixpkgs.legacyPackages.x86_64-linux.kmod.outPath;
  }'
```

## Compiled module and dependency evidence

Evaluated stable kernel: `6.12.117`. Exact existing cached paths:

- Kernel/module root: `/nix/store/8mixm0g0z8iabkgm0np6zyjmrhdndxyf-linux-6.12.117`.
- Compiled config: `/nix/store/lr07axmngs2fgb2h610m6pm9myqshz1j-linux-config-6.12.117`.
- Selected kmod: `/nix/store/plshlafrnmfk1rsx9cinsg3jisdzzh0s-kmod-31`.
- nixpkgs: `/nix/store/7sa2x9c9566lfxkaxs36n3z4yayl5cy4-source`.
- Unchanged complete input graph: repository `flake.lock` blob
  `22ef14b9fb541321a3e5f8ad883f7b9838cbfc81` at both base and head.

The compiled config contains `CONFIG_BATMAN_ADV=m`, `CONFIG_BATMAN_ADV_BLA=y`,
`CONFIG_CRC16=m`, `CONFIG_LIBCRC32C=m`, `CONFIG_CRYPTO_CRC32C=m` and
`CONFIG_CRYPTO_CRC32C_INTEL=m`. `modinfo` names the file
`kernel/net/batman-adv/batman-adv.ko.xz` as `batman_adv` and reports direct
dependencies `bridge,crc16,libcrc32c`. `bridge` depends on `llc,stp`; `stp`
depends on `llc`. `libcrc32c` has the compiled soft dependency `pre: crc32c`.

Using the selected kmod binary (not just the ambient host tool):

```sh
/nix/store/plshlafrnmfk1rsx9cinsg3jisdzzh0s-kmod-31/bin/modprobe \
  -C /dev/null \
  -d /nix/store/8mixm0g0z8iabkgm0np6zyjmrhdndxyf-linux-6.12.117 \
  -S 6.12.117 --show-depends batman_adv
```

This dry run resolves, in order: `crc16`, `crc32c-intel`, `crc32c_generic`,
`libcrc32c`, `llc`, `stp`, `bridge`, `batman-adv`. Every resolved `.ko.xz`
exists in that exact cached kernel root. The CRC32c soft dependency is therefore
resolved by explicit modprobe before libcrc32c loads, without relying on kernel
module autoloading. No extra explicit dependency list is necessary.

The existing `runit.stage1` loop in `os/modules/config/runit.nix` runs modprobe
for each configured module. `os/modules/config/kernel-modules.nix` generates
`/etc/kernel-modules` from the same list and explicitly uses kmod modprobe on
service start/reload. Both mechanisms remain unchanged.

## Compatibility, history and remaining limits

No persisted-state, API, protocol, CLI, schema, Nix-option or migration changes.
No kernel/configuration pin or other input updates, repeated update streams,
superseded implementations, fixup commits or transitional compatibility paths.
The full base-to-head series contains only the coherent change above. No part
of this feature has been merged, released, deployed or externally consumed.

Mixed nodes remain compatible and need no coordinated update. Rollback restores
the old default list. Existing `unloadRemovedModules = false` avoids unloading
an already active module; reboot into the prior generation restores its boot
loading policy. No forced unload or mesh setup is part of this change.

Documentation placement: the changed source list is sufficient lasting behavior
documentation; [design.md](design.md) holds temporary investigation and recovery
rationale; this file holds check evidence for maintainers/reviewers. No separate
product manual is useful for the one-entry change, as accepted by the lead.

No runtime VM boot, exhaustive kernel matrix, full OS build or production test
was run. The bounded acceptance evidence is exact evaluated configuration plus
cached compiled metadata and dependency resolution. Lead owns acceptance,
independent review invocation, any later runtime check, and publication. Capacity:
package I is reported for acceptance; available for review findings or a newly
assigned package after lead acceptance.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-load-batman-adv-module/>.

## Package I2: refresh onto advanced staging

The original evidence above describes the reviewed revision and is retained.
Lead accepted package I and assigned this sole executing refresh package after
the user's explicit integration direction for `vpsadminos/staging`. This package
performs only feature-branch preparation; publication and integration remain
lead-owned. Identity and live same-session roster reverified before work.

| Range | Base | Head |
| --- | --- | --- |
| Original reviewed | `eedc1254d309cac861cb0f7af080ee8de8296506` | `6d5f63697d2f87c817329d6731b7dd0bedd0b6e0` |
| Refreshed | `52a2ac3a4b3155b1991aa6984164eced11c54f87` | `0d3fa0a255fe0c194d1ef89934178b07498431d4` |

Old head retained at exact local backup ref
`refs/backup/2026-11-13-load-batman-adv-module/pre-refresh-6d5f63697`.
Full baseline delta was inspected with `git log`, `git diff --stat` and
`git diff` between the two bases. It consists of one upstream commit,
`52a2ac3a4b3155b1991aa6984164eced11c54f87`, subject
`flake: nixpkgsUnstable 177d05409 -> d4f25a3e5`; only `flake.lock` changes
(3 insertions, 3 deletions). No source, module-loader or procedure changes.

Ran `nix develop --command sh -ec '...; git rebase origin/staging'` with a clean
feature worktree, the repository's hooks active, executable pre-rebase hook,
and no Overcommit disable variables. Rebase completed without conflict or
intervention. No source/input edits were introduced by this package.

Equivalence and quick checks:

- `git range-diff <old-base>..<old-head> <new-base>..<new-head>` reports
  `1: 6d5f63697 = 1: 0d3fa0a25 os: load batman_adv by default`.
- Complete binary output of both base-to-head `git diff` commands is identical.
  Both `git patch-id --stable` values are
  `3a51fe84e5297408f58f33ecdb0a33ab9de4e385`.
- New range still changes only `os/modules/config/kernel.nix`, one insertion;
  the single coherent commit and commit message are preserved. No migrations,
  transitional paths, repeated feature input updates or superseded repairs.
- Re-ran `nixfmt --check`, `nix-instantiate --parse`, and base-to-head
  `git diff --check` under the repository Nix shell: passed.
- Re-ran the exact IFD-disabled default evaluation above. Its full result JSON
  is identical to the original reviewed-head result: exactly one `batman_adv`,
  autoload false, same kernel/version/config/nixpkgs/kmod identities.
- Original compiled dependency evidence is reused only for its exact scope:
  `/nix/store/8mixm0g0z8iabkgm0np6zyjmrhdndxyf-linux-6.12.117`, config
  `/nix/store/lr07axmngs2fgb2h610m6pm9myqshz1j-linux-config-6.12.117`,
  kmod `/nix/store/plshlafrnmfk1rsx9cinsg3jisdzzh0s-kmod-31`, and selected
  stable nixpkgs `/nix/store/7sa2x9c9566lfxkaxs36n3z4yayl5cy4-source`.
  These were freshly evaluated unchanged; no dependency rerun/build is needed.
- Final feature worktree and index are clean. Source/index/rebase window is
  finished. No push, merge claim, merge, deployment, long test, kernel/OS build,
  machine reservation or session lifecycle action was performed.

### Complete source/input identities

Old complete lock graph is Git blob
`22ef14b9fb541321a3e5f8ad883f7b9838cbfc81` at old base and old head. New complete
lock graph is `6acc3885ff55fe18072cbedcf59caac75f6002cc` at new base and new
head. Parsed comparison confirms only `nodes.nixpkgsUnstable.locked` changes;
all node names, other full node records, original selectors, root and follows
relationships are identical. The exact blobs retain all timestamp/selector
metadata as well as the following complete source identities.

| Lock node / upstream | Revision | NAR hash |
| --- | --- | --- |
| `home-manager` / nix-community/home-manager | `c47b2cc64a629f8e075de52e4742de688f930dc6` | `sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg=` |
| `impermanence` / nix-community/impermanence | `fa627f4c8b8e92f58f58a73d99ee4e1304e64eb2` | `sha256-s0TeXWG5Ci75Y/Hzon0Z7NrN/fG773Rc54/z6oPFszQ=` |
| `netlinkrb` / vpsfreecz/netlinkrb | `d9de53d843d2586ffa5b7b404887fa801c697ddf` | `sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg=` |
| `nixpkgs` / nixos/nixpkgs (impermanence input) | `e4bae1bd10c9c57b2cf517953ab70060a828ee6f` | `sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc=` |
| `nixpkgs_2` / NixOS/nixpkgs (selected root stable input) | `ac588ef1c914865dad517b337ea0eb9694a4021c` | `sha256-XuAV2cUwaod3Bt4XFVqiXz3v1w2ex16W6Sv4S7EWres=` |
| `nixpkgsUnstable` / NixOS/nixpkgs, old | `177d0540942fb205af6993b1d5fa0b57799e09f8` | `sha256-SvB8u5qaJAOwZZyZciqTVOg/rBoUs2w0sFTU6ED51AQ=` |
| `nixpkgsUnstable` / NixOS/nixpkgs, new | `d4f25a3e562008648d45bcf2d70bcc7422cad84e` | `sha256-x9sADJvoVG0L6RejZB+/BB4YiGZFBZrfTlhF4uBq1tQ=` |
| `ruby-lxc` / vpsfreecz/ruby-lxc | `004bf35eb90d41ba60b347b5b1e73d868a4f95d9` | `sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE=` |

Graph edges: root `nixpkgs -> nixpkgs_2`, `nixpkgsUnstable -> nixpkgsUnstable`,
`impermanence -> impermanence`, `netlinkrb -> netlinkrb`, `ruby-lxc -> ruby-lxc`.
Impermanence inputs are `home-manager -> home-manager`, `nixpkgs -> nixpkgs`.
Home-manager's `nixpkgs` follows `[impermanence, nixpkgs]`. Other locked source
nodes have no input edges. Netlinkrb and ruby-lxc remain non-flake inputs.

The baseline update is inherited upstream history, not another feature update
stream requiring consolidation. No feature migration was merged, released,
deployed or externally consumed; there are no migrations at either head.
The original head's CI/publication coordination and later superseded-run
cancellation remain with the lead. Compatibility/recovery constraints above
are unchanged. No material deviation or remaining local check gap was found.
I2 is reported for acceptance; capacity available for review findings.
