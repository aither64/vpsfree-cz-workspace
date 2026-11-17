# Package R: stable kernel catalog update

Current local and published D3 OS head: `f33f5fd10b53232b5670862f832f4ec5ea835e84`
on staging base `42baba6117bebcde3d04555a71377381df197925`. Affected D3 review
passed; lead released feature publication. Default integration remains lead-owned.
The user canceled the unpublished README-removal preparation; original link and
reviewed two-commit history are restored. Its provenance is retained below.
The final review/remediation/publication receipt below supersedes earlier P/R
head references while preserving their exact historical evidence.

Owner: implementer0. Design: [design.md](design.md).
Base repository head: `435d83468d7a3089eeb45f171d0ab244748f43b4` (amended P).
Overall branch base: `a7d71a54a15496976cb0fccebb8a1b589f24f5e2`.
No catalog mutation before final K source/accounting/publication evidence.

## Input graph

`flake.lock` SHA256:
`114ab5e7079d489770694809739e25a2062ac43965994fa846fba9acd311cb90`.
No flake input update is part of R. Full locked graph and edges at preparation:

```json
{
  "nodes": {
    "home-manager": {
      "inputs": {
        "nixpkgs": [
          "impermanence",
          "nixpkgs"
        ]
      },
      "locked": {
        "lastModified": 1768598210,
        "narHash": "sha256-kkgA32s/f4jaa4UG+2f8C225Qvclxnqs76mf8zvTVPg=",
        "owner": "nix-community",
        "repo": "home-manager",
        "rev": "c47b2cc64a629f8e075de52e4742de688f930dc6",
        "type": "github"
      },
      "original": {
        "owner": "nix-community",
        "repo": "home-manager",
        "type": "github"
      }
    },
    "impermanence": {
      "inputs": {
        "home-manager": "home-manager",
        "nixpkgs": "nixpkgs"
      },
      "locked": {
        "lastModified": 1792739756,
        "narHash": "sha256-s0TeXWG5Ci75Y/Hzon0Z7NrN/fG773Rc54/z6oPFszQ=",
        "owner": "nix-community",
        "repo": "impermanence",
        "rev": "fa627f4c8b8e92f58f58a73d99ee4e1304e64eb2",
        "type": "github"
      },
      "original": {
        "owner": "nix-community",
        "repo": "impermanence",
        "type": "github"
      }
    },
    "netlinkrb": {
      "flake": false,
      "locked": {
        "lastModified": 1562850306,
        "narHash": "sha256-0bXTWUdUDr2XP+bEIfIbxXap8Niva/IoPXTxFeXXImg=",
        "owner": "vpsfreecz",
        "repo": "netlinkrb",
        "rev": "d9de53d843d2586ffa5b7b404887fa801c697ddf",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "netlinkrb",
        "type": "github"
      }
    },
    "nixpkgs": {
      "locked": {
        "lastModified": 1768564909,
        "narHash": "sha256-Kell/SpJYVkHWMvnhqJz/8DqQg2b6PguxVWOuadbHCc=",
        "owner": "nixos",
        "repo": "nixpkgs",
        "rev": "e4bae1bd10c9c57b2cf517953ab70060a828ee6f",
        "type": "github"
      },
      "original": {
        "owner": "nixos",
        "ref": "nixos-unstable",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgsUnstable": {
      "locked": {
        "lastModified": 1794537146,
        "narHash": "sha256-Wpz/7x/YWnDIBu7yj6ixe8j6fIMsidd9Y+o1PqPF3iM=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "d5cc6833999746cffdfe0598f7bc801a57b887a9",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-unstable",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgs_2": {
      "locked": {
        "lastModified": 1794756927,
        "narHash": "sha256-IfuPcOpwC+bYvBdtUhA9hHhY7xV7k9T5LeOTZFiJB4o=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "b349185bb79c7cf7ad8ea8c097931730bf473c71",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-26.05",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "root": {
      "inputs": {
        "impermanence": "impermanence",
        "netlinkrb": "netlinkrb",
        "nixpkgs": "nixpkgs_2",
        "nixpkgsUnstable": "nixpkgsUnstable",
        "ruby-lxc": "ruby-lxc"
      }
    },
    "ruby-lxc": {
      "flake": false,
      "locked": {
        "lastModified": 1780499941,
        "narHash": "sha256-guAdOSP9MyCL3BQ1LGXAhcCoXgEU1fUE69d2ATMqUGE=",
        "owner": "vpsfreecz",
        "repo": "ruby-lxc",
        "rev": "004bf35eb90d41ba60b347b5b1e73d868a4f95d9",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "ref": "2026-06-03-nixos-26-05-port",
        "repo": "ruby-lxc",
        "type": "github"
      }
    }
  },
  "root": "root",
  "version": 7
}
```

## Final Linux source and initial archive receipt

K delivered complete preservation/accounting evidence in [linux-port.md](linux-port.md):
final Linux `3bba27296b6f4f4a2b1568d65cea6037368f229b`, upstream
`b869a5313cbfe7102873d3de318ddb68675146d0`, all 50 range-diff rows unchanged,
no conflicts/adaptations/omissions/extras. SSH publication and fresh remote proof
confirmed the dated feature branch at the final head; no maintenance/default refs
promoted. Lead accepted the source gate before R's archive acquisition.

Fresh standalone native watcher `/root/kernel_archive`, selected installed package
`/nix/store/ydvk4ljk3z3lynyrz2prcyibmpp2yzbj-dev-workspace-0.2.0`, schema-6
catalog `7659519e2fbe326ba88f3f4e4b07169f291b61a907be06e5b9e374d27fced37e`,
`gpt-6-luna`/low, full_access, native utility
`dw_32fc0df129055f50f5e6054c8d971d33430112edeba8b88d`. Policy was read
and verified against the selected `workspace-host` path before launch.

Command `nix store prefetch-file --json
https://github.com/vpsfreecz/linux/archive/3bba27296b6f4f4a2b1568d65cea6037368f229b.tar.gz`
passed exit 0 after about 50 seconds; tool session 45845 joined, no surviving
operation-owned work. This hashed raw archive bytes without unpacking.
Stdout `/tmp/stable-kernel-archive-prefetch.json`, stderr
`/tmp/stable-kernel-archive-prefetch.log`.

- Hash: `sha256-tXgl0RdF3YigscvXI/tD5QHbujUV+6bVW+KIyESG93U=`
- Store: `/nix/store/y9smdxxh7z7df58hzybqpyrx11rmjrvq-3bba27296b6f4f4a2b1568d65cea6037368f229b.tar.gz`

Added one final new 6.12.118 catalog pin and changed stable only. Retained the
6.12.117/all older entries and unstable. The predecessor has no per-version
config/features overrides; effective common Linux `bridge_stp_helper` remains,
the 6.12.109-specific NFS patch does not apply. Preserved ZFS source
`481845fca6ae3f61ca2262c1a5693a58ae364650`, hash
`sha256-/zeZH5EJYa0zaNcbMUoeHp6UnHNAMUrjgok/VgWI88A=`, and
`zfs235-free-account.patch` for built-in/external packaging. Actual evaluated
identities and source realization are checked next.

## Catalog/package verification and source realization

`nix eval --json --impure --file /tmp/stable-kernel-catalog-check.nix` exited 0.
Native evaluation used `lib.vpsadminosSystem` with normal QEMU modules and explicit
stable/unstable, retained `.117` and external-ZFS module profiles. Python semantic
comparison against the pre-edit catalog confirmed every old entry exactly equal,
only new `.118` added, stable changed to `.118`, unstable remains `6.18.49`, and
new entry's non-revision/hash fields exactly equal predecessor. All profiles retain
`bridge-stp-helper`; both new built-in/external ZFS paths retain the predecessor
source and `zfs235-free-account.patch`. No `.109`-only patch leaks to the target.

Evaluated package identities (path-import evaluation; actual committed Git-flake
CI identity is recorded separately below):

```json
{
  "ciDrv": "/nix/store/jiv7xaxxw3x9x26fmy97a21ic7wc7mpp-vpsadminos-system-vpsadminos-26.05pre-git.drv",
  "external": {
    "linux": {
      "drv": "/nix/store/61h04f41dsq8sgxj87kiyx5s2hr97chm-linux-6.12.118.drv",
      "kernelPatches": [
        {
          "name": "bridge-stp-helper",
          "patch": "/nix/store/ak757c8kik76ip5xm8xkkxs9fkwr5iz7-source/pkgs/os-specific/linux/kernel/bridge-stp-helper.patch"
        }
      ],
      "source": "/nix/store/y9smdxxh7z7df58hzybqpyrx11rmjrvq-3bba27296b6f4f4a2b1568d65cea6037368f229b.tar.gz",
      "sourceDrv": "/nix/store/ppllxmkasqg8mws4rryw1a20b0kcz3r9-3bba27296b6f4f4a2b1568d65cea6037368f229b.tar.gz.drv",
      "version": "6.12.118"
    },
    "selected": "6.12.118",
    "zfsBuiltin": false,
    "zfsBuiltinPackage": {
      "drv": "/nix/store/x4468m97719ik8lpjfjmck2gki0znrf8-zfs-builtin-2.3-vpsadminos-6.12.118.drv",
      "patches": [
        "/nix/store/lhwdnxqjw9xvi5qbqqbfb74dbcjnibmg-source/os/packages/zfs/zfs235-free-account.patch"
      ],
      "source": "/nix/store/gfbfdram71x5imp44590b04pc0wch182-source"
    },
    "zfsExternal": {
      "drv": "/nix/store/1fwpcyi837hv9nam8zfzzx3s33dz3gvq-zfs-kernel-2.3-vpsadminos-6.12.118.drv",
      "patches": [
        "/nix/store/lhwdnxqjw9xvi5qbqqbfb74dbcjnibmg-source/os/packages/zfs/zfs235-free-account.patch"
      ],
      "source": "/nix/store/gfbfdram71x5imp44590b04pc0wch182-source"
    },
    "zfsUser": {
      "drv": "/nix/store/vpvdy6pbvk68j5kl9djr2za8pj9w71zz-zfs-user-2.3-vpsadminos.drv",
      "source": "/nix/store/gfbfdram71x5imp44590b04pc0wch182-source"
    }
  },
  "retained": {
    "linux": {
      "drv": "/nix/store/splppa8hrdg2s5njq2rn8990zr43l6lr-linux-6.12.117.drv",
      "kernelPatches": [
        {
          "name": "bridge-stp-helper",
          "patch": "/nix/store/ak757c8kik76ip5xm8xkkxs9fkwr5iz7-source/pkgs/os-specific/linux/kernel/bridge-stp-helper.patch"
        }
      ],
      "source": "/nix/store/irq31a9wf081gvvss97k54x9r4p2wja8-764acbb0ca8c4b60ee5b98f89406b152e992b1d6.tar.gz",
      "sourceDrv": "/nix/store/rwrjm8v5y3fh52d89sb5i1iyraxpiyh8-764acbb0ca8c4b60ee5b98f89406b152e992b1d6.tar.gz.drv",
      "version": "6.12.117"
    },
    "selected": "6.12.117",
    "zfsBuiltin": true,
    "zfsBuiltinPackage": {
      "drv": "/nix/store/jkfkimmhbfiffrr62y8dhaj00d2nvwg5-zfs-builtin-2.3-vpsadminos-6.12.117.drv",
      "patches": [
        "/nix/store/lhwdnxqjw9xvi5qbqqbfb74dbcjnibmg-source/os/packages/zfs/zfs235-free-account.patch"
      ],
      "source": "/nix/store/gfbfdram71x5imp44590b04pc0wch182-source"
    },
    "zfsExternal": null,
    "zfsUser": {
      "drv": "/nix/store/vpvdy6pbvk68j5kl9djr2za8pj9w71zz-zfs-user-2.3-vpsadminos.drv",
      "source": "/nix/store/gfbfdram71x5imp44590b04pc0wch182-source"
    }
  },
  "stable": {
    "linux": {
      "drv": "/nix/store/3slqrmfmm3jqz8x99rcvi2qr10y3w1dq-linux-6.12.118.drv",
      "kernelPatches": [
        {
          "name": "bridge-stp-helper",
          "patch": "/nix/store/ak757c8kik76ip5xm8xkkxs9fkwr5iz7-source/pkgs/os-specific/linux/kernel/bridge-stp-helper.patch"
        }
      ],
      "source": "/nix/store/y9smdxxh7z7df58hzybqpyrx11rmjrvq-3bba27296b6f4f4a2b1568d65cea6037368f229b.tar.gz",
      "sourceDrv": "/nix/store/ppllxmkasqg8mws4rryw1a20b0kcz3r9-3bba27296b6f4f4a2b1568d65cea6037368f229b.tar.gz.drv",
      "version": "6.12.118"
    },
    "selected": "6.12.118",
    "zfsBuiltin": true,
    "zfsBuiltinPackage": {
      "drv": "/nix/store/x4468m97719ik8lpjfjmck2gki0znrf8-zfs-builtin-2.3-vpsadminos-6.12.118.drv",
      "patches": [
        "/nix/store/lhwdnxqjw9xvi5qbqqbfb74dbcjnibmg-source/os/packages/zfs/zfs235-free-account.patch"
      ],
      "source": "/nix/store/gfbfdram71x5imp44590b04pc0wch182-source"
    },
    "zfsExternal": null,
    "zfsUser": {
      "drv": "/nix/store/vpvdy6pbvk68j5kl9djr2za8pj9w71zz-zfs-user-2.3-vpsadminos.drv",
      "source": "/nix/store/gfbfdram71x5imp44590b04pc0wch182-source"
    }
  },
  "unstable": {
    "linux": {
      "drv": "/nix/store/jc8n7yv848b9xay2bwc7g0c166mnln56-linux-6.18.49.drv",
      "kernelPatches": [
        {
          "name": "bridge-stp-helper",
          "patch": "/nix/store/ak757c8kik76ip5xm8xkkxs9fkwr5iz7-source/pkgs/os-specific/linux/kernel/bridge-stp-helper.patch"
        }
      ],
      "source": "/nix/store/00851ybgngm3ajyaksp34w67pvkzq3y5-a770f5086fc500ca258852aea1cb3e209a342d2b.tar.gz",
      "sourceDrv": "/nix/store/34igcjs8z6nwiv9q689df009zl170wc4-a770f5086fc500ca258852aea1cb3e209a342d2b.tar.gz.drv",
      "version": "6.18.49"
    },
    "selected": "6.18.49",
    "zfsBuiltin": true,
    "zfsBuiltinPackage": {
      "drv": "/nix/store/sg3lcyhmkm19vzlbdqcvpyh23i88fn0x-zfs-builtin-2.3-vpsadminos-6.18.49.drv",
      "patches": [],
      "source": "/nix/store/zwxj43rfcbl0vamyw42a24g5rsyv80g9-source"
    },
    "zfsExternal": null,
    "zfsUser": {
      "drv": "/nix/store/ciz8rfxmxa5883ldx14cvck3kcrflyiv-zfs-user-2.3-vpsadminos.drv",
      "source": "/nix/store/zwxj43rfcbl0vamyw42a24g5rsyv80g9-source"
    }
  },
  "versions": [
    "6.12.109",
    "6.12.110",
    "6.12.113",
    "6.12.117",
    "6.12.118",
    "6.12.48",
    "6.12.95",
    "6.18.44",
    "6.18.49"
  ]
}
```

`nix build --no-link --print-out-paths --impure --file
/tmp/stable-kernel-source.nix` exited 0 and returned the exact prefetched archive
store output. `nix-store -q --outputs` of the actual source derivation also matches.
No compilation, second archive fetch or product build occurred. Source-only tool
session 50117 completed. Actual source derivation definition:

```json
{
  "derivations": {
    "ppllxmkasqg8mws4rryw1a20b0kcz3r9-3bba27296b6f4f4a2b1568d65cea6037368f229b.tar.gz.drv": {
      "args": [
        "-e",
        "/nix/store/l622p70vy8k5sh7y5wizi5f2mic6ynpg-source-stdenv.sh",
        "/nix/store/vvlgjnnch92k53af32iwim3d7jdxai3y-builder.sh"
      ],
      "builder": "/nix/store/8favl12dxjfxwzgqq5jh53k2kjn19nn9-bash-5.3p9/bin/bash",
      "env": {
        "out": "/nix/store/y9smdxxh7z7df58hzybqpyrx11rmjrvq-3bba27296b6f4f4a2b1568d65cea6037368f229b.tar.gz"
      },
      "inputs": {
        "drvs": {
          "h0nmpgmb92b8hv2m3zbc146da8jkfph1-mirrors-list.drv": {
            "dynamicOutputs": {},
            "outputs": [
              "out"
            ]
          },
          "i4p56k7aqh6747lymkg6drbqir363i2d-bash-5.3p9.drv": {
            "dynamicOutputs": {},
            "outputs": [
              "out"
            ]
          },
          "m92iyrzzp6li72p1q3hq9lrc5xl5h7ld-curl-8.23.0.drv": {
            "dynamicOutputs": {},
            "outputs": [
              "dev"
            ]
          },
          "zmsngr5aqfxfy7awpjrwv1wnligdc2i5-stdenv-linux.drv": {
            "dynamicOutputs": {},
            "outputs": [
              "out"
            ]
          }
        },
        "srcs": [
          "l622p70vy8k5sh7y5wizi5f2mic6ynpg-source-stdenv.sh",
          "vvlgjnnch92k53af32iwim3d7jdxai3y-builder.sh"
        ]
      },
      "name": "3bba27296b6f4f4a2b1568d65cea6037368f229b.tar.gz",
      "outputs": {
        "out": {
          "hash": "sha256-tXgl0RdF3YigscvXI/tD5QHbujUV+6bVW+KIyESG93U=",
          "method": "flat"
        }
      },
      "structuredAttrs": {
        "SSL_CERT_FILE": "/no-cert-file.crt",
        "buildInputs": [],
        "builder": "/nix/store/8favl12dxjfxwzgqq5jh53k2kjn19nn9-bash-5.3p9/bin/bash",
        "cmakeFlags": [],
        "configureFlags": [],
        "curlOpts": "",
        "curlOptsList": [
          "--no-retry-all-errors",
          "--retry",
          "3",
          "--retry-delay",
          "30",
          "--connect-timeout",
          "30",
          "--max-time",
          "600",
          "--retry-max-time",
          "1800"
        ],
        "depsBuildBuild": [],
        "depsBuildBuildPropagated": [],
        "depsBuildTarget": [],
        "depsBuildTargetPropagated": [],
        "depsHostHost": [],
        "depsHostHostPropagated": [],
        "depsTargetTarget": [],
        "depsTargetTargetPropagated": [],
        "doCheck": false,
        "doInstallCheck": false,
        "downloadToTemp": false,
        "env": {
          "SSL_CERT_FILE": "/no-cert-file.crt"
        },
        "executable": false,
        "hash": "sha256-tXgl0RdF3YigscvXI/tD5QHbujUV+6bVW+KIyESG93U=",
        "impureEnvVars": [
          "http_proxy",
          "https_proxy",
          "ftp_proxy",
          "all_proxy",
          "no_proxy",
          "HTTP_PROXY",
          "HTTPS_PROXY",
          "FTP_PROXY",
          "ALL_PROXY",
          "NO_PROXY",
          "NIX_SSL_CERT_FILE",
          "NIX_CURL_FLAGS",
          "NIX_HASHED_MIRRORS",
          "NIX_CONNECT_TIMEOUT",
          "NIX_MIRRORS_alsa",
          "NIX_MIRRORS_apache",
          "NIX_MIRRORS_bioc",
          "NIX_MIRRORS_bitlbee",
          "NIX_MIRRORS_centos",
          "NIX_MIRRORS_cpan",
          "NIX_MIRRORS_cran",
          "NIX_MIRRORS_debian",
          "NIX_MIRRORS_dub",
          "NIX_MIRRORS_fedora",
          "NIX_MIRRORS_gcc",
          "NIX_MIRRORS_gentoo",
          "NIX_MIRRORS_gnome",
          "NIX_MIRRORS_gnu",
          "NIX_MIRRORS_gnupg",
          "NIX_MIRRORS_hackage",
          "NIX_MIRRORS_hashedMirrors",
          "NIX_MIRRORS_ibiblioPubLinux",
          "NIX_MIRRORS_imagemagick",
          "NIX_MIRRORS_kde",
          "NIX_MIRRORS_kernel",
          "NIX_MIRRORS_luarocks",
          "NIX_MIRRORS_maven",
          "NIX_MIRRORS_mozilla",
          "NIX_MIRRORS_mysql",
          "NIX_MIRRORS_openbsd",
          "NIX_MIRRORS_opensuse",
          "NIX_MIRRORS_osdn",
          "NIX_MIRRORS_postgresql",
          "NIX_MIRRORS_pypi",
          "NIX_MIRRORS_qt",
          "NIX_MIRRORS_sageupstream",
          "NIX_MIRRORS_samba",
          "NIX_MIRRORS_savannah",
          "NIX_MIRRORS_sourceforge",
          "NIX_MIRRORS_steamrt",
          "NIX_MIRRORS_tcsh",
          "NIX_MIRRORS_testpypi",
          "NIX_MIRRORS_texhistoric",
          "NIX_MIRRORS_ubuntu",
          "NIX_MIRRORS_xfce",
          "NIX_MIRRORS_xorg"
        ],
        "mesonFlags": [],
        "mirrorsFile": "/nix/store/xjlyyg078dgwkigz6v8fidh01axpfmy0-mirrors-list",
        "name": "3bba27296b6f4f4a2b1568d65cea6037368f229b.tar.gz",
        "nativeBuildInputs": [
          "/nix/store/5pnrrxh0hfdrr86qk860qdkq2sp1sghj-curl-8.23.0-dev"
        ],
        "nixpkgsVersion": "26.05",
        "outputChecks": {
          "out": {}
        },
        "outputHash": "sha256-tXgl0RdF3YigscvXI/tD5QHbujUV+6bVW+KIyESG93U=",
        "outputHashMode": "flat",
        "outputs": [
          "out"
        ],
        "patches": [],
        "postFetch": "",
        "preferHashedMirrors": false,
        "preferLocalBuild": true,
        "propagatedBuildInputs": [],
        "propagatedNativeBuildInputs": [],
        "showURLs": false,
        "stdenv": "/nix/store/y2x4lg1q7cxywr1ikxiwxshckgh4q7z4-stdenv-linux",
        "strictDeps": false,
        "system": "x86_64-linux",
        "urls": [
          "https://github.com/vpsfreecz/linux/archive/3bba27296b6f4f4a2b1568d65cea6037368f229b.tar.gz"
        ]
      },
      "system": "x86_64-linux",
      "version": 4
    }
  },
  "version": 4
}
```

`nix develop --command nixfmt --check os/packages/linux/available-kernels.nix`
exited 0 after its declared shell dependency realization completed. This one
shell preparation copied cached dependencies and built Python tkinter/matplotlib/
pytest/markdown/rich/remarshal and nixfmt-tree/bundix/shell derivations; no Linux
compilation. Existing command session 33499 joined. The environment was reused
for normal changed-file commit hooks; no broad RuboCop scan or tooling change.

## Commits and history

Ordinary temp-message-file `git commit -F` inside declared Nix environment exited
0 with pre-commit Nixfmt and commit-msg hooks passing. One advisory >72-column
body-line warning, within required 80-column limit. Clean worktree after commit.

Complete current branch sequence from initial base
`a7d71a54a15496976cb0fccebb8a1b589f24f5e2`:

1. `435d83468d7a3089eeb45f171d0ab244748f43b4` — reusable process, including
   demonstrated conditional replay correction folded into its original owner.
2. `5a59f3059ca6ada368deeeeca6dba5034468be93` — one final stable catalog update.

Final diff: seven paths, +324/-1; R itself only
`os/packages/linux/available-kernels.nix`, +10/-1. No intermediate pins, migrations,
schema changes, compatibility guards, abandoned approaches, fixup/WIP residue or
obsolete transition commits. Existing old catalog identities remain intact; no
released/deployed migration provenance applies. Global independent final review
and long product checks remain lead-owned; no OS push before final review.

## Exact committed head and target freshness

`git fetch --no-tags origin staging` over configured SSH origin exited 0;
`origin/staging` is still `a7d71a54a15496976cb0fccebb8a1b589f24f5e2`.
`git merge-base --is-ancestor origin/staging HEAD` exited 0. No rebase needed.
`git diff --check origin/staging..HEAD` exited 0; worktree/index clean.
`dev-session worktree capture-comparison ... vpsadminos --as-is` captured that
exact base and final head `5a59f3059ca6ada368deeeeca6dba5034468be93`.

`nix eval --json .#lib.kernelVersions` includes `.118` and all retained keys.
`nix eval --raw .#ci-toplevel-kernel-6_12_118.drvPath` on committed Git flake:
`/nix/store/smzzgsm45k9qiir8sv7wwfrn8z4f4174-vpsadminos-system-vpsadminos-26.05.git.5a59f30.drv`.
This is the exact final source CI closure derivation, evaluated without building.
Flake lock checksum remains unchanged. Actual committed Git-flake role/source
identity evaluation exited 0 (session 90412 joined):

```json
{
  "retained": {
    "linuxDrv": "/nix/store/splppa8hrdg2s5njq2rn8990zr43l6lr-linux-6.12.117.drv",
    "src": "/nix/store/irq31a9wf081gvvss97k54x9r4p2wja8-764acbb0ca8c4b60ee5b98f89406b152e992b1d6.tar.gz",
    "version": "6.12.117",
    "zfsSource": "/nix/store/gfbfdram71x5imp44590b04pc0wch182-source"
  },
  "stable": {
    "linuxDrv": "/nix/store/3slqrmfmm3jqz8x99rcvi2qr10y3w1dq-linux-6.12.118.drv",
    "src": "/nix/store/y9smdxxh7z7df58hzybqpyrx11rmjrvq-3bba27296b6f4f4a2b1568d65cea6037368f229b.tar.gz",
    "version": "6.12.118",
    "zfsSource": "/nix/store/gfbfdram71x5imp44590b04pc0wch182-source"
  },
  "unstable": {
    "linuxDrv": "/nix/store/jc8n7yv848b9xay2bwc7g0c166mnln56-linux-6.18.49.drv",
    "src": "/nix/store/00851ybgngm3ajyaksp34w67pvkzq3y5-a770f5086fc500ca258852aea1cb3e209a342d2b.tar.gz",
    "version": "6.18.49",
    "zfsSource": "/nix/store/zwxj43rfcbl0vamyw42a24g5rsyv80g9-source"
  }
}
```

`gh run list --repo vpsfreecz/vpsadminos --branch
2026-11-17-stable-kernel-update --limit 5 --json
databaseId,headSha,status,conclusion,workflowName,url` exited 0 with `[]`.
No OS topic push has started. Lead moved publication to after final review
because os/** feature pushes trigger long CI product checks. No long compile,
VM test, integration or deployment performed by R.

R reported for lead acceptance with capacity confirmed for follow-up findings.
Exclusive source/index/commit window released. Final independent review and long
checks remain outstanding; this report does not declare whole-branch readiness
or lifecycle completion. Session stays open.

## Final review advisory A1, history reconciliation and publication

Reviewer reported no Blocking/Important source/process/catalog finding. Lead
requested the one Advisory A1: explicitly export `GIT_NO_LAZY_FETCH=1` throughout
owned partial-clone inspection/replay/continuation instead of a preflight-only
command prefix. Applied lead's direct writing instruction without changing the
missing-content deliberate-acquisition boundary or other commands.

Old reviewed range:
`a7d71a54a15496976cb0fccebb8a1b589f24f5e2..5a59f3059ca6ada368deeeeca6dba5034468be93`.
New final range:
`a7d71a54a15496976cb0fccebb8a1b589f24f5e2..ba7e99b5e3d435826bd387e64f1c1a6ec173169c`.
Final two logical commits:

1. `18f820a1df8fc473a496f13f7e1d32ca75151bf1` — process with A1 folded into P.
2. `ba7e99b5e3d435826bd387e64f1c1a6ec173169c` — unchanged single catalog update.

Native range-diff proves P differs only in A1 and catalog R is `=`. Direct final
tree diff old/new is exactly `docs/os/kernel-updates.md` +11/-4; exit-zero
`git diff --exit-code OLD NEW -- . ':!docs/os/kernel-updates.md'` establishes
equality outside that clarification. No source/pin/lock/migration changes or
new transitional commits. Retained exact local backup ref:
`refs/heads/backup/2026-11-17-stable-kernel-update/os-before-lazy-fetch-doc-fix`
at old reviewed head.

Pre-rebase initially refused configuration trust before mutating history. The
owned patch was saved and restored around the retry; the follow-on environment
command was interrupted/joined before any amend. Ambient Ruby 3.4.11 is
incompatible with native gems prepared for declared Ruby 3.4.12. Evaluated the
declared devShell's nativeBuildInputs and reused their existing exact tool paths
(Ruby 3.4.12, Nixfmt 1.5.0, MkDocs 1.6.1) with project GEM_HOME and default gem
paths; no global tool/dependency change. Ordinary `overcommit --sign` and rebase
then passed. No hook bypass. This also avoided another broad shell realization.

Focused checks: skill quick_validate exit0; make doc exit0 (1.09 seconds, same two
existing nav notices); relative links and all shell blocks checked; staged/full
diff checks exit0; ordinary amend pre-commit/commit-msg hooks all pass without
warnings. Successful rebase/edit/amend/replay sequence was fail-fast. The exact
requested change was independently assessed and accepted by lead under the
mandatory-review narrow-fix rule; no full rerun required.

Current stable identity re-evaluated after final commit:

```json
{
  "linuxDrv": "/nix/store/3slqrmfmm3jqz8x99rcvi2qr10y3w1dq-linux-6.12.118.drv",
  "selected": "6.12.118",
  "source": "/nix/store/y9smdxxh7z7df58hzybqpyrx11rmjrvq-3bba27296b6f4f4a2b1568d65cea6037368f229b.tar.gz"
}
```

`nix eval --raw .#ci-toplevel.drvPath` and
`nix eval --raw .#ci-toplevel-kernel-6_12_118.drvPath` both returned exactly:
`/nix/store/1xz2kh8yvxaijd57mwkdk2wb0d1mgif8-vpsadminos-system-vpsadminos-26.05.git.ba7e99b.drv`.
String equality assertion exited 0; no build. Existing raw source/hash,
selectors/retained-entry/package-layer evidence remains applicable because the
only changed tree content is the process clarification. Lock checksum unchanged.

Lead accepted A1 and explicitly released feature publication. Fresh SSH fetch
confirmed `origin/staging` still at the initial base; ancestry check passed. Final
comparison capture binds that base to `ba7e99b5e3d435826bd387e64f1c1a6ec173169c`.
Initial ambient-environment push was refused locally for configuration trust and
made no remote change. Reusing declared tools with ordinary trust signing, fresh
staging check and push succeeded exit0. Fresh SSH ls-remote returned exact final
head on `refs/heads/2026-11-17-stable-kernel-update`. No force push, PR, default
integration or deployment. Source worktree/index clean.

One bounded CI query after push returned the following exact-head runs; lead owns
runtime monitoring. R did not wait for CI or start a watcher/local product build:

```json
{"conclusion":null,"head_sha":"ba7e99b5e3d435826bd387e64f1c1a6ec173169c","html_url":"https://github.com/vpsfreecz/vpsadminos/actions/runs/44120817659","id":44120817659,"name":"CI (ci)","run_attempt":1,"status":"in_progress","workflow_id":162100852}
{"conclusion":null,"head_sha":"ba7e99b5e3d435826bd387e64f1c1a6ec173169c","html_url":"https://github.com/vpsfreecz/vpsadminos/actions/runs/44120817623","id":44120817623,"name":"Livepatch documentation","run_attempt":1,"status":"in_progress","workflow_id":418457005}
{"conclusion":null,"head_sha":"ba7e99b5e3d435826bd387e64f1c1a6ec173169c","html_url":"https://github.com/vpsfreecz/vpsadminos/actions/runs/44120818064","id":44120818064,"name":"Livepatch qualification","run_attempt":1,"status":"queued","workflow_id":418457006}
```

Main CI: workflow `162100852`, run `44120817659`, attempt `1`, exact final head,
in progress at query. All tool sessions/commands from remediation/publication
completed, no surviving utility or uncertain effects. Exclusive OS publish window
released after receipt; implementer0 retains R finding ownership/capacity.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-17-stable-kernel-update/

## User-directed README scope reduction

User rejected feature-specific additions to the top-level README. Lead assigned
only removal of our kernel update link, retaining existing topic/MkDocs/skill/
AGENTS navigation and delegating policy suggestions elsewhere. Removed exactly
that line and folded it into P via an owned interactive edit/amend/replay with
`rebase.updateRefs=false` and normal declared-environment hooks. No other source
change, new navigation section, workspace rule change or follow-up pin.

Old published/reviewed range:
`a7d71a54a15496976cb0fccebb8a1b589f24f5e2..ba7e99b5e3d435826bd387e64f1c1a6ec173169c`.
New prepared range:
`a7d71a54a15496976cb0fccebb8a1b589f24f5e2..94e9e13d7ce27a76b304cdd0acddc4a9ef0e3584`.
Exactly two commits:

1. `0d2bded4f290ecf087c3bdf9cf8b9a7695f43a81` — process without the rejected
   top-level README link.
2. `94e9e13d7ce27a76b304cdd0acddc4a9ef0e3584` — same final catalog patch.

Native range-diff shows only the removed README hunk in P, catalog `=`. Direct
`git diff --exit-code` confirms README byte-identical to initial branch base
and all paths except README identical to old published final tree. Backup ref
`refs/heads/backup/2026-11-17-stable-kernel-update/os-before-readme-link-removal`
preserves exact old published head. Full resulting diff: six paths +330/-1; no
migration/source/catalog/flake change beyond prior accepted work.

Focused checks all exit0: make doc (1.07s, same two pre-existing nav notices),
quick_validate.py, relative links, shell example syntax, staged/full diff checks,
ordinary pre-commit Nixfmt and commit-msg hooks. Worktree/index clean; lock checksum
unchanged. Comparison capture refreshed for initial base -> prepared final head.
Final committed target CI drv evaluation:
`/nix/store/qn0fgqp8r8fkarzxl02pyyh24mjnz3wb-vpsadminos-system-vpsadminos-26.05.git.94e9e13.drv`.
Existing kernel/source/selector/package evidence reused under exact tree equality
outside README. No remote push, CI cancellation or observation started by this
remediation; lead owns narrow assessment and subsequent publication sequencing.

## User reversal: original published history restored

User clarified: "apologies! i misread the code comparison. it can stay as it is".
Lead canceled the unpublished README-removal preparation and directed restoring
the original published head. Confirmed clean current topic at exact removal
head `94e9e13d7ce27a76b304cdd0acddc4a9ef0e3584` with no intended commits above
it; retained it in exact local backup ref
`refs/heads/backup/2026-11-17-stable-kernel-update/os-canceled-readme-removal`.
Zero-commit native rebase with `--no-update-refs --onto` restored the original
branch tip without a reset, stash, clean, deletion or added revert/fix commit.
Ordinary declared hook environment used; no bypass.

Local HEAD and fresh SSH remote topic both match exactly
`ba7e99b5e3d435826bd387e64f1c1a6ec173169c`. Clean worktree/index. Restored two
commits are `18f820a1df8fc473a496f13f7e1d32ca75151bf1` (process, original
README link included) then `ba7e99b5e3d435826bd387e64f1c1a6ec173169c` (catalog).
Comparison recaptured from `a7d71a54a15496976cb0fccebb8a1b589f24f5e2` to exact
restored head. First comparison call inherited project Ruby GEM_HOME and hit
workspace-host's Ruby ABI mismatch; retried it from a clean tool shell, exit0.
No source change, push, force-push, CI cancellation, retest, runtime identity
change, new watcher, default integration or deployment. Original reviewed source/
CI identity/evidence remains current; lead owns existing CI observation.

## D3-OS: Linux version-branch publication instructions

Owner: implementer0. Accepted D3 brief is appended to design.md; user approved
branch-only `vpsadminos-<upstream-version>` with no automatic downstream tags.
Changed only kernel-routing paragraph in AGENTS.md, process page and skill. A
candidate dated publication may supply archive bytes before review/builds; final
version-branch publication follows existing exact-head review/validation gates.
Same-head existing version branch is satisfied; different head is preserved and
inspected, never force-updated just to finish. Existing conditional -2/-3 convention
is available only for intentional later same-upstream revisions after ref checks.
No Linux default/series merge or generic alias update, exact immutable OS SHA/raw
hash pin retained; upstream tag reads remain valid. Direct lead writing pass
applied before commit. Existing replay/range/conflict/selector/recovery contracts
were preserved. No README/nav/catalog/flake/Linux source change.

Pre-D3 prepared range:
`42baba6117bebcde3d04555a71377381df197925..ba6837de511ef9364fa4126e24c91de0251f33ad`.
D3 final prepared range:
`42baba6117bebcde3d04555a71377381df197925..f33f5fd10b53232b5670862f832f4ec5ea835e84`.
Exactly two commits: `2352449568afa3b2f5bd500dba3fbed1c1163e0b` (updated P),
`f33f5fd10b53232b5670862f832f4ec5ea835e84` (catalog).
Native range-diff shows only D3 prose in P; catalog `=`. Direct tree diff equality
outside three assigned files passed; D3 delta +45/-14. No migrations/repair or
intermediate pin commits. Backup ref
`refs/heads/backup/2026-11-17-stable-kernel-update/os-before-version-branch-instructions`
retains pre-D3 head; reviewed/tested old ranges remain in prior receipts.

Focused checks exit0: skill quick_validate.py, links/all shell syntax, make doc
(0.90 seconds, same pre-existing nav notices), staged/full diff checks, ordinary
pre-commit/commit-msg hooks. Required pre-rebase trust refreshed in declared tool
environment outside any claim; no bypass. Clean source; comparison captured
new base -> D3 head. Prepared merge-target remains untouched/clean at 42baba.

Fresh SSH `git ls-remote` independently returned exact named Linux branch:
`3bba27296b6f4f4a2b1568d65cea6037368f229b refs/heads/vpsadminos-6.12.118`.
Full publication receipt is in linux-port.md; no Linux mutation by D3-OS.
Lock SHA256 remains `114ab5e7079d489770694809739e25a2062ac43965994fa846fba9acd311cb90`.
Final stable/kernel/ZFS native identity re-evaluation:

```json
{
  "linuxDrv": "/nix/store/3slqrmfmm3jqz8x99rcvi2qr10y3w1dq-linux-6.12.118.drv",
  "selected": "6.12.118",
  "src": "/nix/store/y9smdxxh7z7df58hzybqpyrx11rmjrvq-3bba27296b6f4f4a2b1568d65cea6037368f229b.tar.gz",
  "srcDrv": "/nix/store/ppllxmkasqg8mws4rryw1a20b0kcz3r9-3bba27296b6f4f4a2b1568d65cea6037368f229b.tar.gz.drv",
  "zfsDrv": "/nix/store/x4468m97719ik8lpjfjmck2gki0znrf8-zfs-builtin-2.3-vpsadminos-6.12.118.drv",
  "zfsSrc": "/nix/store/gfbfdram71x5imp44590b04pc0wch182-source"
}
```

Source/kernel/ZFS drv identities match accepted CI receipts. D3 changes instructions
only; old exact OS closure evidence remains scoped to ba7e99b, with mechanical
exporter-baseline refresh provenance recorded in verification.md. Affected final
documentation review is lead-owned and pending. No force-push/merge/claim, local
product test, deployment or lifecycle operation. D3-OS reported for acceptance
with source-window released and capacity confirmed.

Final D3 Git-flake target CI derivation (evaluation only):
`/nix/store/6a560v0f442rchkda1024cvsjnliswdn-vpsadminos-system-vpsadminos-26.05.git.f33f5fd.drv`.
All D3-OS commands joined; no surviving or uncertain effects.

## Final reviewed feature publication

Affected D3 independent review passed without findings. Lead authorized feature
publication of final `f33f5fd10b53232b5670862f832f4ec5ea835e84`, preserving normal
hooks and an exact lease against prior published
`ba7e99b5e3d435826bd387e64f1c1a6ec173169c`.
Fresh SSH fetch confirms staging still
`42baba6117bebcde3d04555a71377381df197925`; ancestor/cleanliness/head checks passed.
`git push --force-with-lease=refs/heads/2026-11-17-stable-kernel-update:ba7e99b5e3d435826bd387e64f1c1a6ec173169c
origin HEAD:refs/heads/2026-11-17-stable-kernel-update` exited 0 with ordinary hooks.
Fresh SSH ls-remote returns exact final head on the topic ref. No default mutation,
claim, target-worktree edit, test, build, deployment or lifecycle action.

One bounded post-push branch-run query found current-head attempt-1 runs queued:
main CI workflow `162100852` run `44166848013`, and docs workflow `418457005`
run `44166848023`. Old ba7e99b main/docs runs are completed success; old
qualification completed failure remains separately diagnosed. No superseded
queued/running/waiting/requested/pending runs exist, so no cancellation was sent.
No current-head or other-branch run canceled, no CI wait/observer started by
implementer0. Lead owns imminent default integration and CI observation.
Publication command and metadata read joined; all effects clear.
