# E0 inactive release-source checkpoint

Current checkpoint: corrected blog feature `3aec4d6b4858b2ed50e21bdb99d36f707fc9ceeb`
and configuration feature `7bab9781d0a5eb1aed5914f0aed99f6d7d491632` are published.
Immutable artifact/system and final V3 usability evidence were accepted by the
lead. Default branches remain unchanged. Exact feature CI belongs to implementer2;
no integration, activation or session cleanup is authorized. See the final
publication section below; initial E0 identities remain historical evidence.

Prepared by implementer0. This is source/fixture evidence, not deployment,
activation readiness, independent review approval or default-branch integration.
No production request, SSH, credential provisioning, service operation, machine
claim, activation/dry-activation or push was performed for E0.

## Exact source identities

- Blog E0 base: `b6b76192c61802c37fbc6cfdc0133c0bec1b3f07`.
- Blog E0 commit: `c4cf0220e313600f568524fc040cd13159669df3`.
  Eight files: build workflow, `bin/package-release`, `bin/check-release`,
  `docs/deployment.md` and the accepted AGENTS/README/authoring/skill factual
  reconciliation. No `bin/build`, flake, C0, corpus or translation changes.
- Blog's protected initialized base remains
  `0354dac281978867ea8c1553b092ce19bccb5ccd`. Its complete series at the immutable
  E0 checkpoint is listed below. Lead-assigned V2/history consolidation happens
  afterward; its owner supplies final old/new equivalence and final branch head.
- Configuration fresh default: `5941cdb3dda259e91c6a988a7dbf08c84700b326`.
- Refreshed DNS feature: `b4a7f22a46c16be453052a37ac98fc4c39401a9f`.
- Configuration E0 commit: `7bab9781d0a5eb1aed5914f0aed99f6d7d491632`.
  Six files: default-off module/import, configuration-owned helper, two fixture
  checks and `docs/operations/blog-static.md`. Configuration worktree/index were
  clean after commit. Blog index was yielded immediately after its E0 commit;
  V2's three dirty files were preserved.

Blog series at `c4cf0220`:

```text
d7b90f09e1edd6fb2b032057205c91d6df5c94ee Import the captured Czech WordPress corpus and public assets
818202f7b48e8031acb49641360b2402bc4e679b Preserve the original Flat design around the imported archive
e9c286b2f403603907265ac28f4bd38b3ae00227 Align authoring instructions with the imported blog
e8aed2ef787217e8085d782e38a760cd51ddbd90 Translate 63 archived articles into English drafts
c3786b74af9ee9382af4cc44428e7e77965753ea content: draft 62 English archive translations
b6b76192c61802c37fbc6cfdc0133c0bec1b3f07 Prepare opt-in native discussions for production articles
c4cf0220e313600f568524fc040cd13159669df3 Prepare checked immutable blog release artifacts
```

Configuration series above its fresh default is exactly the refreshed DNS
feature followed by E0. [Configuration refresh evidence](configuration-refresh.md)
retains old `85b38f1c..133a94b6`, new `5941cdb3..b4a7f22a`, protected old source
ref and matching record-payload digest. This is semantic equivalence: the removed
SOA predecessor changed from `2026093000` to `2026110200`; feature serial
`2026110600` is strictly newer. The exact A/TTL/public-CNAME boundary is unchanged.
No literal patch equivalence or reuse of old DNS builds is claimed.

## Checks and source boundaries

- Tiny offline producer fixture: `nix develop -c bin/check-release`, passed.
  Covers clean exact source identity, dirty/null rejection, undeclared payload
  and deterministic tar/receipt bytes. Dirty author previews remain supported.
- Workflow YAML parsed with Ruby YAML; read-only contents permissions and seven
  steps verified. Feature/PR jobs cannot publish eligible main artifacts.
- Target: `python3 tests/blog-static-release.py`, six tests passed. Covers mocked
  trusted API acquisition, missing/expired exact artifact, wrong identity,
  unsafe/duplicate/link/device archive entries, hash mismatch, admission refusal,
  stale head including the final switch boundary, concurrent receipt exclusion,
  interruption reconciliation, retained immutable CSS and explicit rollback.
- Nix module fixture passed using the repository's pinned `nixpkgsStable`:
  effective disabled state is identical to the existing hardened WordPress
  configuration; original vhost root/listen are preserved. Separate candidate
  roots/feed/PHP denial/unknown-host rejection and refused scheduler are checked.
  Exact executed command, from the configuration worktree:

  ```sh
  nix eval --impure --json --expr 'import ./tests/blog-static-module.nix { nixpkgs = (builtins.getFlake (toString ./.)).inputs.nixpkgsStable; }'
  ```
- Protected-source comparison against fresh configuration default found no
  changes to WordPress, existing health checks, proxy, forum, public DNS, flake
  inputs or locks. The sole DNS diff is the retained N feature above.
- Configuration Nix files formatted with the declared Nix formatter. Normal
  Overcommit pre-commit and commit-message hooks passed. Commit-message width
  produced nonblocking 72-column warnings; all lines satisfy the workspace's
  80-column maximum. No hook bypass. Documentation local links/examples and
  owned staged whitespace checks passed; lead accepted all final prose.

Upstream action refs verified before use:

| Action | Tag | Pinned commit |
| --- | --- | --- |
| actions/checkout | v7.0.1 | `3d3c42e5aac5ba805825da76410c181273ba90b1` |
| cachix/install-nix-action | v31.11.3 | `75c75c31ebece974e48ebc36b4ad125bd97bd97b` |
| actions/upload-artifact | v7.0.2 | `cf430e030ddbb5b0abf93d22962f4752f3646cd9` |

The workflow requests 90-day retention, subject to repository policy. The target
must retain exact archives/current/previous releases/receipts independently;
expired current-SHA artifacts require an exact-source rebuild, never an older
fallback. No production build is introduced.

## Remaining gates

Independent final review and any longer exact-head configuration build remain
pending; no long system build was run before review. No live Actions run,
artifact download, Nginx service, target activation or runtime admission test is
claimed. Required operator facts remain workflow ID, protected branch policy,
artifact read credential/visibility, outbound download route and retained backup.
The timer is default-off and enabling it fails evaluation; production pull,
activation and rollback CLI paths refuse `machine-admission-unavailable`.
Pure fixture callbacks are not a production coordinator bridge.

Legacy query/alias serving, English public DNS/TLS, forum runtime setup and the
actual proxy transition still require their own approved/verified work. No
formal writer freeze is planned; perform the requested brief pre-switch change
check and refresh capture only if needed. No deployed head, system/profile store
path, machine claim or integration evidence exists for E0 because none was
executed. No migrations, input-pin streams or default-history rewrites were added.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-multilingual-blog-migration/)

## Refreshed exact-head DNS parsing

```json
{
  "configuration_head": "7bab9781d0a5eb1aed5914f0aed99f6d7d491632",
  "source_path": "configs/internal-dns/zone.vpsfree.cz.",
  "source_sha256": "f0287f6c9d8950e286155451d15d6724b0018a1967327272ee4da2c705b54087",
  "tool": "/nix/store/2q7r6d5awv41lb810xdczlc8ym4disla-bind-9.20.29/bin/named-checkzone",
  "checks": [
    {
      "fqdn": "ns1.int.prg.vpsfree.cz",
      "exit": 0,
      "serial": 2026110600,
      "materialized_sha256": "38dd3358f8bb79f2a7a6262eb802301929a9be63fbdce7395e77029d23ce5c07",
      "answers": [
        {
          "owner": "blog.vpsfree.cz.",
          "ttl": "3600",
          "class": "IN",
          "type": "CNAME",
          "answer": "proxy.vpsfree.cz."
        },
        {
          "owner": "blog.int.vpsfree.cz.",
          "ttl": "3600",
          "class": "IN",
          "type": "A",
          "answer": "172.16.8.4"
        }
      ]
    },
    {
      "fqdn": "ns1.int.brq.vpsfree.cz",
      "exit": 0,
      "serial": 2026110600,
      "materialized_sha256": "27a7e602e95e703c28dd8d6eb4d17d70714501d34936cabed3149fbcc68f4e9d",
      "answers": [
        {
          "owner": "blog.vpsfree.cz.",
          "ttl": "3600",
          "class": "IN",
          "type": "CNAME",
          "answer": "proxy.vpsfree.cz."
        },
        {
          "owner": "blog.int.vpsfree.cz.",
          "ttl": "3600",
          "class": "IN",
          "type": "A",
          "answer": "172.16.8.4"
        }
      ]
    }
  ],
  "scope": "Two offline materializations only; no live DNS/network/build/activation."
}
```

These results verify the refreshed E0 zone source, not the old DNS build or deployed state.

## Post-review disabled-system build

Watcher-owned command: `nix develop -c confctl build --yes cz.vpsfree/containers/int.blog`.

```json
{
  "auto_rollback_program": "/nix/store/yl9vnin9wlv04cip0sqpkisk80xmccwh-auto-rollback.rb",
  "build_log": "/home/aither/workspace/ai/vpsfree.cz/work/2026-11-06-multilingual-blog-migration/final-blog-system-build.log",
  "build_log_sha256": "b8bab825283c4e518f412a01c0e9924086d73450d96867a8cc41b4184718714f",
  "command_exit": 0,
  "completion_evidence": "Confctl logged Built generations and exact generation; receipt/symlinks/toplevel/input paths and derivation output exist and agree. No rerun.",
  "deployment": "None; no active system/profile path or deployed head is claimed.",
  "derivation": "/nix/store/nzccrw68i25yqvx9zq8b71mfaiz0sd6r-nixos-system-blog-26.05.20261026.718f670.drv",
  "effective_inputs": {
    "nixpkgs": {
      "input": "nixpkgsStable",
      "lastModified": 1793015021,
      "narHash": "sha256-Ee5BWo8sh3pGt70QUdRajnaginqFmWvrtdBc4gJzhks=",
      "narSize": 206804072,
      "path": "/nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source",
      "rev": "718f670e845328e9c2cecdd832835712b2cbd065",
      "shortRev": "718f670e",
      "url": "https://github.com/NixOS/nixpkgs"
    },
    "vpsadminos": {
      "input": "vpsadminosOsStaging",
      "lastModified": 1793720150,
      "narHash": "sha256-LXZP7Ghcr+1obFUD+LjlJRO63qRo/GZtSve5AX5MZ7c=",
      "narSize": 338218032,
      "path": "/nix/store/cgk63vdx1wjl4ybd53abkd5aqyzc7sfa-source",
      "rev": "dd188397abe37d0bc33f4c5dfb3605206ce5e326",
      "shortRev": "dd188397",
      "url": "https://github.com/vpsfreecz/vpsadminos"
    }
  },
  "generation_json": "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/vpsfree-cz-configuration/.confctl/generations/cz.vpsfree:containers:int.blog/2026-11-07--00-29-17/generation.json",
  "generation_sha256": "829923f159788d7b46a6a90e9abf3f0f8e13bf144b5e3fc94086f5775bcac96f",
  "lock_git_blob": "11219f0dcb5a4be6a6a2d813086461988953d2e8",
  "lock_nodes": 64,
  "lock_sha256": "9ed71bd9511c7b4e16e0fd9f4de483e0fe4cf54d2556e715392d28e6e60eacd8",
  "outer_shell_exit": 127,
  "outer_shell_issue": "/etc/bash_logout:4: __ETC_BASHLOGOUT_SOURCED: unbound variable",
  "selector": "cz.vpsfree/containers/int.blog",
  "source_clean_observed": true,
  "source_git_materialization": "/nix/store/ai3m6c2zl40ci93c40n9swv1asm306h7-source",
  "source_narHash": "sha256-oyj2ibCzzi+AaFozbgj5XkxyZlgZy+0yewIhPXuZhhI=",
  "source_proof_limit": "Exact Git snapshot materialized/read after build; generation JSON itself has no configuration revision field. Build source binding uses watcher exact-head/clean checks and unchanged source.",
  "source_sha": "7bab9781d0a5eb1aed5914f0aed99f6d7d491632",
  "toplevel": "/nix/store/pa6j6jvzf8ic3z7bqvzskdgmk2b7mk0z-nixos-system-blog-26.05.20261026.718f670"
}
```

<details><summary>Complete pinned root source lock graph (64 nodes)</summary>

```json
{
  "nodes": {
    "bun2nix": {
      "inputs": {
        "flake-parts": [
          "devWorkspace",
          "llm-agents",
          "flake-parts"
        ],
        "nixpkgs": [
          "devWorkspace",
          "llm-agents",
          "nixpkgs"
        ],
        "systems": [
          "devWorkspace",
          "llm-agents",
          "systems"
        ],
        "treefmt-nix": [
          "devWorkspace",
          "llm-agents",
          "treefmt-nix"
        ]
      },
      "locked": {
        "lastModified": 1790001035,
        "narHash": "sha256-1/SLBjSYBzDdDhvLQ83wrzBakyS/xNGgtxHGNuveOEQ=",
        "owner": "Mic92",
        "repo": "bun2nix",
        "rev": "07a5bfc8ac36c5370199343fa620b69f63186e33",
        "type": "github"
      },
      "original": {
        "owner": "Mic92",
        "ref": "llm-agents",
        "repo": "bun2nix",
        "type": "github"
      }
    },
    "bun2nix_2": {
      "inputs": {
        "flake-parts": [
          "llm-agents",
          "flake-parts"
        ],
        "nixpkgs": [
          "llm-agents",
          "nixpkgs"
        ],
        "systems": [
          "llm-agents",
          "systems"
        ],
        "treefmt-nix": [
          "llm-agents",
          "treefmt-nix"
        ]
      },
      "locked": {
        "lastModified": 1790001035,
        "narHash": "sha256-1/SLBjSYBzDdDhvLQ83wrzBakyS/xNGgtxHGNuveOEQ=",
        "owner": "Mic92",
        "repo": "bun2nix",
        "rev": "07a5bfc8ac36c5370199343fa620b69f63186e33",
        "type": "github"
      },
      "original": {
        "owner": "Mic92",
        "ref": "llm-agents",
        "repo": "bun2nix",
        "type": "github"
      }
    },
    "codex-web": {
      "flake": false,
      "locked": {
        "lastModified": 1793398646,
        "narHash": "sha256-Hhh2EYZxKiM1fDfPGxDazhs/ElyOF4q6mMvK5JOUOu0=",
        "owner": "aither64",
        "repo": "codex-web",
        "rev": "d3a29bee90ef00a08816920408c596152339a637",
        "type": "github"
      },
      "original": {
        "owner": "aither64",
        "repo": "codex-web",
        "rev": "d3a29bee90ef00a08816920408c596152339a637",
        "type": "github"
      }
    },
    "confctl": {
      "inputs": {
        "nixpkgs": [
          "confctl",
          "vpsadminos",
          "nixpkgs"
        ],
        "vpsadminos": "vpsadminos"
      },
      "locked": {
        "lastModified": 1784400083,
        "narHash": "sha256-gh1tmTv8aAO1OA3HX2NEYnRALMK2i666Lxey8hxD0QM=",
        "owner": "vpsfreecz",
        "repo": "confctl",
        "rev": "7bee58a52372b95c2198ce3f2a719807a3c2c66b",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "confctl",
        "type": "github"
      }
    },
    "devWorkspace": {
      "inputs": {
        "codex-web": "codex-web",
        "llm-agents": "llm-agents",
        "nixpkgs": "nixpkgs_4"
      },
      "locked": {
        "lastModified": 1793782995,
        "narHash": "sha256-pDaBIdK6uFgVq0Gw7arQLjvIjKsGrKg33IFmwmxnOoo=",
        "owner": "aither64",
        "repo": "dev-workspace",
        "rev": "3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7",
        "type": "github"
      },
      "original": {
        "owner": "aither64",
        "repo": "dev-workspace",
        "type": "github"
      }
    },
    "flake-parts": {
      "inputs": {
        "nixpkgs-lib": [
          "devWorkspace",
          "llm-agents",
          "nixpkgs"
        ]
      },
      "locked": {
        "lastModified": 1790898470,
        "narHash": "sha256-zTwuwezD0w3hpga6a6P8emidzAZFyWqlNeRBlpWOOl8=",
        "owner": "hercules-ci",
        "repo": "flake-parts",
        "rev": "024633cd702b10285db5cb19b40ad48d2399ba60",
        "type": "github"
      },
      "original": {
        "owner": "hercules-ci",
        "repo": "flake-parts",
        "type": "github"
      }
    },
    "flake-parts_2": {
      "inputs": {
        "nixpkgs-lib": [
          "llm-agents",
          "nixpkgs"
        ]
      },
      "locked": {
        "lastModified": 1790898470,
        "narHash": "sha256-zTwuwezD0w3hpga6a6P8emidzAZFyWqlNeRBlpWOOl8=",
        "owner": "hercules-ci",
        "repo": "flake-parts",
        "rev": "024633cd702b10285db5cb19b40ad48d2399ba60",
        "type": "github"
      },
      "original": {
        "owner": "hercules-ci",
        "repo": "flake-parts",
        "type": "github"
      }
    },
    "home-manager": {
      "inputs": {
        "nixpkgs": [
          "confctl",
          "vpsadminos",
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
    "home-manager_2": {
      "inputs": {
        "nixpkgs": [
          "nixpkgsStable"
        ]
      },
      "locked": {
        "lastModified": 1780361225,
        "narHash": "sha256-wnV9ttf4fPWNonBIQmvlrSlNpQYgx5HgWWd007mwIFA=",
        "owner": "nix-community",
        "repo": "home-manager",
        "rev": "e28654b71096e08c019d4861ca26acb646f583d8",
        "type": "github"
      },
      "original": {
        "owner": "nix-community",
        "ref": "release-26.05",
        "repo": "home-manager",
        "type": "github"
      }
    },
    "home-manager_3": {
      "inputs": {
        "nixpkgs": [
          "vpsadminosOsStaging",
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
    "home-manager_4": {
      "inputs": {
        "nixpkgs": [
          "vpsadminosProduction",
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
    "home-manager_5": {
      "inputs": {
        "nixpkgs": [
          "vpsadminosStaging",
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
    "home-manager_6": {
      "inputs": {
        "nixpkgs": [
          "vpsfStatus",
          "vpsadmin",
          "vpsadminos",
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
        "lastModified": 1769548169,
        "narHash": "sha256-03+JxvzmfwRu+5JafM0DLbxgHttOQZkUtDWBmeUkN8Y=",
        "owner": "nix-community",
        "repo": "impermanence",
        "rev": "7b1d382faf603b6d264f58627330f9faa5cba149",
        "type": "github"
      },
      "original": {
        "owner": "nix-community",
        "repo": "impermanence",
        "type": "github"
      }
    },
    "impermanence_2": {
      "inputs": {
        "home-manager": "home-manager_3",
        "nixpkgs": "nixpkgs_6"
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
    "impermanence_3": {
      "inputs": {
        "home-manager": "home-manager_4",
        "nixpkgs": "nixpkgs_7"
      },
      "locked": {
        "lastModified": 1769548169,
        "narHash": "sha256-03+JxvzmfwRu+5JafM0DLbxgHttOQZkUtDWBmeUkN8Y=",
        "owner": "nix-community",
        "repo": "impermanence",
        "rev": "7b1d382faf603b6d264f58627330f9faa5cba149",
        "type": "github"
      },
      "original": {
        "owner": "nix-community",
        "repo": "impermanence",
        "type": "github"
      }
    },
    "impermanence_4": {
      "inputs": {
        "home-manager": "home-manager_5",
        "nixpkgs": "nixpkgs_8"
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
    "impermanence_5": {
      "inputs": {
        "home-manager": "home-manager_6",
        "nixpkgs": "nixpkgs_9"
      },
      "locked": {
        "lastModified": 1769548169,
        "narHash": "sha256-03+JxvzmfwRu+5JafM0DLbxgHttOQZkUtDWBmeUkN8Y=",
        "owner": "nix-community",
        "repo": "impermanence",
        "rev": "7b1d382faf603b6d264f58627330f9faa5cba149",
        "type": "github"
      },
      "original": {
        "owner": "nix-community",
        "repo": "impermanence",
        "type": "github"
      }
    },
    "llm-agents": {
      "inputs": {
        "bun2nix": "bun2nix",
        "flake-parts": "flake-parts",
        "nixpkgs": "nixpkgs_3",
        "systems": "systems",
        "treefmt-nix": "treefmt-nix"
      },
      "locked": {
        "lastModified": 1793167323,
        "narHash": "sha256-JxeqQKUhBn5kj6xfE4nIrxw/q3jFJyT+TKc8mLsnuhc=",
        "owner": "numtide",
        "repo": "llm-agents.nix",
        "rev": "91ff550fe42d4dd51dcf8b6bad87a0134fe7f314",
        "type": "github"
      },
      "original": {
        "owner": "numtide",
        "repo": "llm-agents.nix",
        "rev": "91ff550fe42d4dd51dcf8b6bad87a0134fe7f314",
        "type": "github"
      }
    },
    "llm-agents_2": {
      "inputs": {
        "bun2nix": "bun2nix_2",
        "flake-parts": "flake-parts_2",
        "nixpkgs": "nixpkgs_5",
        "systems": "systems_2",
        "treefmt-nix": "treefmt-nix_2"
      },
      "locked": {
        "lastModified": 1793167323,
        "narHash": "sha256-JxeqQKUhBn5kj6xfE4nIrxw/q3jFJyT+TKc8mLsnuhc=",
        "owner": "numtide",
        "repo": "llm-agents.nix",
        "rev": "91ff550fe42d4dd51dcf8b6bad87a0134fe7f314",
        "type": "github"
      },
      "original": {
        "owner": "numtide",
        "repo": "llm-agents.nix",
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
    "netlinkrb_2": {
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
    "netlinkrb_3": {
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
    "netlinkrb_4": {
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
    "netlinkrb_5": {
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
    "nixpkgsProduction": {
      "locked": {
        "lastModified": 1793015021,
        "narHash": "sha256-Ee5BWo8sh3pGt70QUdRajnaginqFmWvrtdBc4gJzhks=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "718f670e845328e9c2cecdd832835712b2cbd065",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-26.05",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgsStable": {
      "locked": {
        "lastModified": 1793015021,
        "narHash": "sha256-Ee5BWo8sh3pGt70QUdRajnaginqFmWvrtdBc4gJzhks=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "718f670e845328e9c2cecdd832835712b2cbd065",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-26.05",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgsStaging": {
      "locked": {
        "lastModified": 1793015021,
        "narHash": "sha256-Ee5BWo8sh3pGt70QUdRajnaginqFmWvrtdBc4gJzhks=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "718f670e845328e9c2cecdd832835712b2cbd065",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-26.05",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgsUnstable": {
      "locked": {
        "lastModified": 1781074563,
        "narHash": "sha256-md8WlXOlfnIeHeOScMTTHFyf2d6iaTwPl2apR5EQ3P4=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "9ae611a455b90cf061d8f332b977e387bda8e1ca",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-unstable",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgsUnstable_2": {
      "locked": {
        "lastModified": 1793110635,
        "narHash": "sha256-dhoW6VgFWlaodSY5jrBn+CF2FLmaUvDVgM7+C7T2+NM=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "31ecbaca1bdefa45dffc409f0250bd8039ea0010",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-unstable",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgsUnstable_3": {
      "locked": {
        "lastModified": 1786106723,
        "narHash": "sha256-zDSUbpoeo/9ZmD2+wXnzxoo1+uhL8vxc0b8yuYMKYq0=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "f13ff45afd1bb73e640eaa08a7066dbed07e3238",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-unstable",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgs_10": {
      "locked": {
        "lastModified": 1786089803,
        "narHash": "sha256-ZuvZfVW2tB5tXYEcpcfhVXB3N4OhdZLOqOviy4OD4b4=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "ee48b147c18c7de1e6ec97dc74792be42724bed1",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-26.05",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgs_2": {
      "locked": {
        "lastModified": 1780902259,
        "narHash": "sha256-q8yYEC5f1mFlQO9RGna4LTc9QrcvWunX6FYp83munkQ=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "bd0ff2d3eac24699c3664d5966b9ef36f388e2ca",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-26.05",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgs_3": {
      "locked": {
        "lastModified": 1792116957,
        "narHash": "sha256-EjZqHKObBfIOeHZnMRVV87HB3pPq/WBkmRJWyFxmZu8=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "f20cd90e28fe0403873f473b29e42662cd86e8c4",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixpkgs-unstable",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgs_4": {
      "locked": {
        "lastModified": 1788405554,
        "narHash": "sha256-r2f1oUwixlgq9zOdYLqJLfS/lWBT60/IITjhTKI59JU=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixos-26.05",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgs_5": {
      "locked": {
        "lastModified": 1792116957,
        "narHash": "sha256-EjZqHKObBfIOeHZnMRVV87HB3pPq/WBkmRJWyFxmZu8=",
        "owner": "NixOS",
        "repo": "nixpkgs",
        "rev": "f20cd90e28fe0403873f473b29e42662cd86e8c4",
        "type": "github"
      },
      "original": {
        "owner": "NixOS",
        "ref": "nixpkgs-unstable",
        "repo": "nixpkgs",
        "type": "github"
      }
    },
    "nixpkgs_6": {
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
    "nixpkgs_7": {
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
    "nixpkgs_8": {
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
    "nixpkgs_9": {
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
    "root": {
      "inputs": {
        "confctl": "confctl",
        "devWorkspace": "devWorkspace",
        "home-manager": "home-manager_2",
        "llm-agents": "llm-agents_2",
        "nixpkgs": [
          "nixpkgsStable"
        ],
        "nixpkgsProduction": "nixpkgsProduction",
        "nixpkgsStable": "nixpkgsStable",
        "nixpkgsStaging": "nixpkgsStaging",
        "nixpkgsUnstable": "nixpkgsUnstable_2",
        "vpsadminProduction": "vpsadminProduction",
        "vpsadminServices": "vpsadminServices",
        "vpsadminStaging": "vpsadminStaging",
        "vpsadminWebui": "vpsadminWebui",
        "vpsadminosOsStaging": "vpsadminosOsStaging",
        "vpsadminosProduction": "vpsadminosProduction",
        "vpsadminosStaging": "vpsadminosStaging",
        "vpsfStatus": "vpsfStatus",
        "vpsfreeNotificationTemplates": "vpsfreeNotificationTemplates",
        "vpsfreeWeb": "vpsfreeWeb"
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
    },
    "ruby-lxc_2": {
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
    },
    "ruby-lxc_3": {
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
    },
    "ruby-lxc_4": {
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
    },
    "ruby-lxc_5": {
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
    },
    "systems": {
      "locked": {
        "lastModified": 1791244623,
        "narHash": "sha256-uuanbkFk8a313Zfrxdcz8Us/yQtaxNnKJtX8v0ZPpd8=",
        "owner": "nix-systems",
        "repo": "default",
        "rev": "d36eeed142f88b5a636f2e3856a53c61654cf29b",
        "type": "github"
      },
      "original": {
        "owner": "nix-systems",
        "repo": "default",
        "type": "github"
      }
    },
    "systems_2": {
      "locked": {
        "lastModified": 1791244623,
        "narHash": "sha256-uuanbkFk8a313Zfrxdcz8Us/yQtaxNnKJtX8v0ZPpd8=",
        "owner": "nix-systems",
        "repo": "default",
        "rev": "d36eeed142f88b5a636f2e3856a53c61654cf29b",
        "type": "github"
      },
      "original": {
        "owner": "nix-systems",
        "repo": "default",
        "type": "github"
      }
    },
    "treefmt-nix": {
      "inputs": {
        "nixpkgs": [
          "devWorkspace",
          "llm-agents",
          "nixpkgs"
        ]
      },
      "locked": {
        "lastModified": 1791885023,
        "narHash": "sha256-C3alQ2MEt0zVrUSho5NUDo3jmhbff72++bfwoqT9Omo=",
        "owner": "numtide",
        "repo": "treefmt-nix",
        "rev": "0d6d739a833ba9a9c93034862e4a7b061a062a1c",
        "type": "github"
      },
      "original": {
        "owner": "numtide",
        "repo": "treefmt-nix",
        "type": "github"
      }
    },
    "treefmt-nix_2": {
      "inputs": {
        "nixpkgs": [
          "llm-agents",
          "nixpkgs"
        ]
      },
      "locked": {
        "lastModified": 1791885023,
        "narHash": "sha256-C3alQ2MEt0zVrUSho5NUDo3jmhbff72++bfwoqT9Omo=",
        "owner": "numtide",
        "repo": "treefmt-nix",
        "rev": "0d6d739a833ba9a9c93034862e4a7b061a062a1c",
        "type": "github"
      },
      "original": {
        "owner": "numtide",
        "repo": "treefmt-nix",
        "type": "github"
      }
    },
    "vpsadmin": {
      "inputs": {
        "nixpkgs": [
          "vpsfStatus",
          "vpsadmin",
          "vpsadminos",
          "nixpkgs"
        ],
        "vpsadminos": "vpsadminos_2"
      },
      "locked": {
        "lastModified": 1785850721,
        "narHash": "sha256-5MfntVa4kDeE1MjIAIMDlGk3X7fJ6BzS7GWW0mCEwuk=",
        "owner": "vpsfreecz",
        "repo": "vpsadmin",
        "rev": "3f9b68adb97b7f43df929a85fc172d9d11e15211",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsadmin",
        "type": "github"
      }
    },
    "vpsadminProduction": {
      "inputs": {
        "nixpkgs": [
          "nixpkgsProduction"
        ],
        "vpsadminos": [
          "vpsadminosProduction"
        ]
      },
      "locked": {
        "lastModified": 1792321599,
        "narHash": "sha256-U0py4ENShmTqcwZDUn11GABUnE0BhVnTM1EXylJmcMc=",
        "owner": "vpsfreecz",
        "repo": "vpsadmin",
        "rev": "ff730be468e366ee346dc6d02dc0fe57c3f8677c",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsadmin",
        "type": "github"
      }
    },
    "vpsadminServices": {
      "inputs": {
        "nixpkgs": [
          "nixpkgsStable"
        ],
        "vpsadminos": [
          "vpsadminosStaging"
        ]
      },
      "locked": {
        "lastModified": 1793802784,
        "narHash": "sha256-J7a/I+juHiy63uDAWxANp/THIX6+Zo7r4l0zaiicSeo=",
        "owner": "vpsfreecz",
        "repo": "vpsadmin",
        "rev": "b83b26e1ba1c8e869ae3ffbcb5801ed071c3844e",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsadmin",
        "type": "github"
      }
    },
    "vpsadminStaging": {
      "inputs": {
        "nixpkgs": [
          "nixpkgsStaging"
        ],
        "vpsadminos": [
          "vpsadminosStaging"
        ]
      },
      "locked": {
        "lastModified": 1792321599,
        "narHash": "sha256-U0py4ENShmTqcwZDUn11GABUnE0BhVnTM1EXylJmcMc=",
        "owner": "vpsfreecz",
        "repo": "vpsadmin",
        "rev": "ff730be468e366ee346dc6d02dc0fe57c3f8677c",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsadmin",
        "type": "github"
      }
    },
    "vpsadminWebui": {
      "inputs": {
        "nixpkgs": [
          "nixpkgsStable"
        ],
        "vpsadmin": [
          "vpsadminServices"
        ]
      },
      "locked": {
        "lastModified": 1793750160,
        "narHash": "sha256-bItN12Wrd6I/PoJOvTOJh1BVq3f9tGVQ+Q/uMQKeRtA=",
        "owner": "vpsfreecz",
        "repo": "vpsadmin-webui",
        "rev": "babe51421bd1df61a548e7b2f047053df14ff3eb",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsadmin-webui",
        "type": "github"
      }
    },
    "vpsadminos": {
      "inputs": {
        "impermanence": "impermanence",
        "netlinkrb": "netlinkrb",
        "nixpkgs": "nixpkgs_2",
        "nixpkgsUnstable": "nixpkgsUnstable",
        "ruby-lxc": "ruby-lxc"
      },
      "locked": {
        "lastModified": 1781261055,
        "narHash": "sha256-Y7FLO10JwU3bo0j6dRHboubKAP8VRxxnaiD2NshG+Kc=",
        "owner": "vpsfreecz",
        "repo": "vpsadminos",
        "rev": "6f9b2c755143197bd9c3452e1c0121b22e978c4d",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsadminos",
        "type": "github"
      }
    },
    "vpsadminosOsStaging": {
      "inputs": {
        "impermanence": "impermanence_2",
        "netlinkrb": "netlinkrb_2",
        "nixpkgs": [
          "nixpkgsStable"
        ],
        "nixpkgsUnstable": [
          "nixpkgsUnstable"
        ],
        "ruby-lxc": "ruby-lxc_2"
      },
      "locked": {
        "lastModified": 1793720150,
        "narHash": "sha256-LXZP7Ghcr+1obFUD+LjlJRO63qRo/GZtSve5AX5MZ7c=",
        "owner": "vpsfreecz",
        "repo": "vpsadminos",
        "rev": "dd188397abe37d0bc33f4c5dfb3605206ce5e326",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsadminos",
        "type": "github"
      }
    },
    "vpsadminosProduction": {
      "inputs": {
        "impermanence": "impermanence_3",
        "netlinkrb": "netlinkrb_3",
        "nixpkgs": [
          "nixpkgsProduction"
        ],
        "nixpkgsUnstable": [
          "nixpkgsUnstable"
        ],
        "ruby-lxc": "ruby-lxc_3"
      },
      "locked": {
        "lastModified": 1792347366,
        "narHash": "sha256-jyXAH3nUkocJj+KQKINbJ0UnDCmuln4EvYRw/1KtXFE=",
        "owner": "vpsfreecz",
        "repo": "vpsadminos",
        "rev": "2abbe3cc1c102a4b39022d3f73ef4a432ad4d616",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsadminos",
        "type": "github"
      }
    },
    "vpsadminosStaging": {
      "inputs": {
        "impermanence": "impermanence_4",
        "netlinkrb": "netlinkrb_4",
        "nixpkgs": [
          "nixpkgsStaging"
        ],
        "nixpkgsUnstable": [
          "nixpkgsUnstable"
        ],
        "ruby-lxc": "ruby-lxc_4"
      },
      "locked": {
        "lastModified": 1793720150,
        "narHash": "sha256-LXZP7Ghcr+1obFUD+LjlJRO63qRo/GZtSve5AX5MZ7c=",
        "owner": "vpsfreecz",
        "repo": "vpsadminos",
        "rev": "dd188397abe37d0bc33f4c5dfb3605206ce5e326",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsadminos",
        "type": "github"
      }
    },
    "vpsadminos_2": {
      "inputs": {
        "impermanence": "impermanence_5",
        "netlinkrb": "netlinkrb_5",
        "nixpkgs": "nixpkgs_10",
        "nixpkgsUnstable": "nixpkgsUnstable_3",
        "ruby-lxc": "ruby-lxc_5"
      },
      "locked": {
        "lastModified": 1786260915,
        "narHash": "sha256-Xd+DyVC+Gkv6+1oSsxb8VfE3DtVCHx90vmKvuFuhYbY=",
        "owner": "vpsfreecz",
        "repo": "vpsadminos",
        "rev": "837baf04054c6ee0e71d288b8870ac42a6990c38",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "ref": "staging",
        "repo": "vpsadminos",
        "type": "github"
      }
    },
    "vpsfStatus": {
      "inputs": {
        "nixpkgs": [
          "nixpkgsStable"
        ],
        "vpsadmin": "vpsadmin",
        "vpsadminos": [
          "vpsfStatus",
          "vpsadmin",
          "vpsadminos"
        ]
      },
      "locked": {
        "lastModified": 1788260265,
        "narHash": "sha256-4iun0P87K5kKG2vYi6Beio/1iWlHmNYFjD8Hlg2qGgk=",
        "owner": "vpsfreecz",
        "repo": "vpsf-status",
        "rev": "587cd65bb02e6dddea7f6b6409e42a15f36ab4fb",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsf-status",
        "type": "github"
      }
    },
    "vpsfreeNotificationTemplates": {
      "inputs": {
        "vpsadmin": [
          "vpsadminServices"
        ]
      },
      "locked": {
        "lastModified": 1790168321,
        "narHash": "sha256-tVRZNlK2iOcorDkw5bK/10e911ILS7VY5uMExH91NQ4=",
        "owner": "vpsfreecz",
        "repo": "vpsfree-notification-templates",
        "rev": "2cfd218d9152888feea4109f064459078ea9f76e",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "vpsfree-notification-templates",
        "type": "github"
      }
    },
    "vpsfreeWeb": {
      "flake": false,
      "locked": {
        "lastModified": 1791740386,
        "narHash": "sha256-/3QHdhSzFlEc7YqWZDjnVxIeS4n1OdImicvgUZjBGew=",
        "owner": "vpsfreecz",
        "repo": "web",
        "rev": "307635a96bc3532af51ff5d08206d920704eee00",
        "type": "github"
      },
      "original": {
        "owner": "vpsfreecz",
        "repo": "web",
        "type": "github"
      }
    }
  },
  "root": "root",
  "version": 7
}
```

</details>

The declared root graph is complete; the generation selects the two effective machine inputs recorded above. This build verifies the disabled candidate system, not enabled static hosting or installed machine admission.

## Superseded unrooted blog artifact attempt

The watcher successfully built reviewed `aeed3a018d895b797e1b8d9b2863dd20c0dec8e0` with `nix build --no-link --print-out-paths .#site` (command exit0). Initial metadata read identified artifact `/nix/store/cn6fxvcjidfvh3hyx4q1hqxixixsqyld-vpsfree-blog-0`, derivation `/nix/store/0m4andba5pv1aq6370h2208481nc82qw-vpsfree-blog-0.drv`, source `/nix/store/l8mawc1jgn90n8v74wgvzfsh1pd5pwpx-source`, source NAR `sha256-qCFMNOKvIRpmLMFH8a6k2cDTIZb5viyvma1CPXJQKhQ=`, Hugo0.167.0 and the 2-node Nixpkgs lock at `f3a73bcf5d1c5b75a66cf35a48957e30d41d647a` / `sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=`. Metadata declared1655served files.

Before the full digest/route pass, that artifact, source and derivation disappeared from the store. No cleanup was run by the implementer; an unrooted-output retention issue is possible but not proven. Full artifact verification is **incomplete**, with no content defect inferred. Publication paused. The first rooted-watcher preflight stopped before a build because of PATH, per lead report; no successful replacement artifact is claimed. A subsequent VPN runtime finding requires a corrected final blog head and new rooted build; old artifact interpretation remains superseded. Do not use these paths as retained current artifacts or eligible GitHub artifact proof.

## Corrected final rooted production artifact

Command: `nix build --out-link result --print-out-paths .#site`, exact clean final source below. The existing ignored `result` link is retained; no cleanup was performed. All assertions below passed by reading the immutable artifact/source only, without a new build or CI packaging.

```json
{
  "artifact_eligibility": "Local Nix artifact only; no GitHub run/artifact identity invented, no activation claim.",
  "artifact_path": "/nix/store/8m7n2r4hpis3wn2593vj0a8iiayljc22-vpsfree-blog-0",
  "both_home_canonicals": true,
  "complete_lock_graph": {
    "nodes": {
      "nixpkgs": {
        "locked": {
          "lastModified": 1792422028,
          "narHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
          "owner": "NixOS",
          "repo": "nixpkgs",
          "rev": "f3a73bcf5d1c5b75a66cf35a48957e30d41d647a",
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
          "nixpkgs": "nixpkgs"
        }
      }
    },
    "root": "root",
    "version": 7
  },
  "cs_article_routes": 125,
  "derivation_path": "/nix/store/1jmg6d2m3yq6xdxzdbiflqrskgwmvhvm-vpsfree-blog-0.drv",
  "en_drafts_verified_and_excluded": 125,
  "en_production_article_count": 0,
  "feed_items": {
    "cs": 10,
    "en": 0
  },
  "full_feed_content_date_guid_parity": true,
  "historical_comment_anchors_verified": 107,
  "inputs": {
    "hugoVersion": "0.167.0",
    "nixpkgsNarHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
    "nixpkgsRevision": "f3a73bcf5d1c5b75a66cf35a48957e30d41d647a",
    "revision": "3aec4d6b4858b2ed50e21bdb99d36f707fc9ceeb",
    "source": "/nix/store/8lwj9092h3n6v7977phwn2c5n1rxl6qc-source",
    "sourceNarHash": "sha256-JuLwVNsVGIE4yt5U5SYXko4vC21znWUydRQ0Au9ojAM="
  },
  "legacy_upload_digest_copies": 1138,
  "lock_sha256": "865a3c07a35f43f024ce7c01614be82cb795707edac8e27092bdbba42519cd75",
  "metadata_path": "/nix/store/8m7n2r4hpis3wn2593vj0a8iiayljc22-vpsfree-blog-0/metadata.json",
  "metadata_sha256": "02b2e117737477025c8c021b4a17ff7761aa4564ff09be380e277294ec3d638f",
  "retained_result_link": "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-multilingual-blog-migration/blog/result",
  "retained_result_target": "/nix/store/8m7n2r4hpis3wn2593vj0a8iiayljc22-vpsfree-blog-0",
  "served_files_verified": 1655,
  "source_narHash": "sha256-JuLwVNsVGIE4yt5U5SYXko4vC21znWUydRQ0Au9ojAM=",
  "source_narSize": 52237824,
  "source_path": "/nix/store/8lwj9092h3n6v7977phwn2c5n1rxl6qc-source",
  "source_sha": "3aec4d6b4858b2ed50e21bdb99d36f707fc9ceeb"
}
```

The earlier unrooted aeed3a0 attempt remains incomplete/superseded. Corrected source3aec4d6b has the accepted narrow preview/check fix. Production excludes all125 English drafts; this is distinct from their usable preview. Publication remains paused until the separate V3 real-runtime/browser result is released by the lead.

Additional read-only final-artifact scope: every HTML canonical uses its own production host; no script or production Discourse iframe appears. Effective Nixpkgs source path/NAR also agrees with the complete two-node lock.

```json
{
  "all_html_canonicals_verified": {
    "cs": 430,
    "en": 22
  },
  "nixpkgs_source_narHash": "sha256-qVt97ILUu2DorFGGEi+mqVuzOF8R18fQLgFkHiLrNfE=",
  "nixpkgs_source_path": "/nix/store/kv7b75nbhc93yrs276n0ba9gsiv8cz3b-source",
  "production_scripts_and_discourse_frames": 0
}
```

## Final verified feature publication

The lead released publication after accepted corrected rooted artifact/system proof and final V3 real HTTP/browser usability evidence. The baseline independent review and accepted narrow preview fix remain recorded in final-review/V3 receipts; publication does not grant integration or activation.

```json
{
  "CI": "No workflow run ID surfaced in Git push output; publication-ready sent directly to implementer2 and lead. Implementer2 owns exact corrected-head Build blog discovery/watching. Implementer0 did not monitor CI.",
  "blog": {
    "command_exit": 0,
    "comparison_base": "0354dac281978867ea8c1553b092ce19bccb5ccd",
    "comparison_head": "3aec4d6b4858b2ed50e21bdb99d36f707fc9ceeb",
    "default_before_and_after": "0354dac281978867ea8c1553b092ce19bccb5ccd",
    "default_ref": "refs/heads/main",
    "method": "ordinary fast-forward push of exact SHA",
    "new_feature": "3aec4d6b4858b2ed50e21bdb99d36f707fc9ceeb",
    "old_feature": "0354dac281978867ea8c1553b092ce19bccb5ccd",
    "remote": "git@github.com:vpsfreecz/blog.git",
    "remote_HEAD": "refs/heads/main",
    "retry_count": 0
  },
  "branch": "2026-11-06-multilingual-blog-migration",
  "configuration": {
    "command_exit": 0,
    "comparison_base": "5941cdb3dda259e91c6a988a7dbf08c84700b326",
    "comparison_head": "7bab9781d0a5eb1aed5914f0aed99f6d7d491632",
    "declared_workflow": {
      "cron": "30 4 * * *",
      "events": [
        "workflow_dispatch",
        "schedule"
      ],
      "file": ".github/workflows/daily-update.yml",
      "name": "Daily update",
      "push_trigger": false
    },
    "default_before_and_after": "5941cdb3dda259e91c6a988a7dbf08c84700b326",
    "default_ref": "refs/heads/master",
    "method": "--force-with-lease=refs/heads/2026-11-06-multilingual-blog-migration:133a94b62b3c2161c126fa347cab61ae1b819001",
    "new_feature": "7bab9781d0a5eb1aed5914f0aed99f6d7d491632",
    "old_feature": "133a94b62b3c2161c126fa347cab61ae1b819001",
    "preserved_old_DNS_ref": "refs/heads/2026-11-06-multilingual-blog-migration-dns-reviewed",
    "remote": "git@github.com:vpsfreecz/vpsfree-cz-configuration.git",
    "remote_HEAD": "refs/heads/master"
  },
  "evidence": "Fresh canonical SSH fetch/ls-remote matched approved old refs before pushes. Immediate post-push ls-remote proved exact feature SHAs and unchanged default/HEAD refs. Both explicit base/head portal comparisons captured.",
  "limits": "Features only. No merge, PR, default update, rebase after review, source/pin changes, production request, activation, machine claim, service or lifecycle cleanup.",
  "retention": "All feature/recovery refs, rooted result, registered previews and session remain retained."
}
```

The original blog push remained owned throughout its quiet archive transfer. A measured49.5second interval acknowledged another16,580,180bytes before eventual exit0; no cancellation, retry or silence-based failure was introduced. Configuration used only the exact approved feature lease, preserving the old reviewed source ref; neither default branch was a push target.
