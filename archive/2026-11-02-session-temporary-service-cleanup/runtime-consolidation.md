# Runtime consolidation and source publication receipt

Session: `2026-11-02-session-temporary-service-cleanup`; owner implementer1.
Final feature head `312d2e2a8994c136f96938d2f2a71ae8e2f16f33`; tree `c121d46242fb9d5af8eea3e974248c46a27f7fbf`. Remote feature ref was verified
at that exact head after an ordinary SSH push. Remote master remained `c2182254d29c4175c3e9fe4267e5a92dd1da6b79`.
Runtime index and checkout are clean. No repository claim, target integration,
deployment or lifecycle action occurred. Runtime Git lane is returned to lead.

## Review and source equivalence

Independent final review: [review-final.md](review-final.md), retained reviewer0
Sol/xhigh, all four lanes. The lead accepted the exact requested R1/R2/R3
corrections by direct narrow-fix inspection at accepted source tree `c121d46242fb9d5af8eea3e974248c46a27f7fbf`
before publication. This is recorded authority to proceed under the review
skill's narrow-fix rule; it does not supply default integration approval.

Initial reviewed range: `c2182254d29c4175c3e9fe4267e5a92dd1da6b79..85760a7a673f3ec072c7c16dc88006e89214d448`.
Accepted remediation range: `85760a7a..6daf7856d812450a2fda896a2e1afaffe6ccdc4c`: eight files, 274 insertions,
26 deletions, covering only the three findings. Final consolidation preserves
that accepted tree exactly (`git diff --exit-code 6daf7856d812450a2fda896a2e1afaffe6ccdc4c 312d2e2a8994c136f96938d2f2a71ae8e2f16f33` passed).
No source edits or baseline change occurred during consolidation. Core and
dependent messages were refreshed through temporary files/normal Git hooks to
state the first-conversation guard and all-registration compatibility rule.

The initial-review-to-corrected-series range comparison is retained in
[runtime-consolidation-range-diff.txt](runtime-consolidation-range-diff.txt).
Its changes are the inspected review remedies and commit-message corrections;
it is not a claim of patch equality with the pre-remediation review head.

## Full final series

```text
e5c26680a8c91cb7db31dab695453be054475e1c portal: group session resources and show retained counts
39e3b67c4ecdd8e499a9fc3b484d5ee3c44afb16 sessions: retire registered temporary services before file cleanup
312d2e2a8994c136f96938d2f2a71ae8e2f16f33 portal: expose registered services and protect lifecycle handoff
```

All three fixups were folded into their distinct owning unpublished commits.
No obsolete implementation or fixup commit remains in the final feature range.
The old six-commit series is retained locally by branch
`2026-11-02-session-temporary-service-cleanup-pre-consolidation`, at `6daf7856d812450a2fda896a2e1afaffe6ccdc4c`.
No old feature head was published, deployed, released or integrated.

| Old unpublished commit | Disposition |
| --- | --- |
| `fac02494b5b41d0d4a6f299f083e67f4ea3a799e` | UI original; folded with R3 into e5c26680 |
| `08a0df822b4a01cef25207ba663df861b2b4006d` | core original; folded with R1/R2 into 39e3b67c |
| `85760a7a673f3ec072c7c16dc88006e89214d448` | dependent original; folded with R1 into 312d2e2a |
| `399136d8d6db71b140b2df3d859a7cbe31840abd` | core R1/R2 fixup; folded into 39e3b67c |
| `2d9089d1e94802038c03f9861c14447d4ac48115` | UI R3 fixup; folded into e5c26680 |
| `6daf7856d812450a2fda896a2e1afaffe6ccdc4c` | dependent R1 fixup and accepted remediation head; folded into 312d2e2a |

There are no database migrations. Local service schema 1 is new and was never
externally consumed at an intermediate feature revision. No transitional
migration remains. Existing ordinary archive/removal/revival journal schemas
and recovery policies remain preserved. R1 retains capabilities for any
registration; R2 refuses root-changing first conversation creation before
mutation; R3 updates the existing navigation regression.

There are no repeated dependency/channel/input/generated streams in this runtime
range. `flake.nix` and `flake.lock` are byte-identical to the baseline. Future
workspace/configuration pin streams remain unmodified and will each get one
final generated update plus the retained reviewer's explicit history/graph
conclusion before readiness.

## Final quick verification

At exact final committed head/tree above, repository Nix shell
`nix develop --no-update-lock-file -c bash -e -c ...` ran once:

- `go -C portal test -mod=readonly ./internal/cluster ./internal/session`:
  passed (1.193 s / 3.732 s).
- `go -C portal test -mod=readonly ./internal/web -run
  "^Test(Service|Resource|InitialLifecycleReceipt|OperationsNavigationDoesNotReadOrEmbedStatus)"
  -count=1`: passed (0.447 s), including service handoff and exact Operations test.
- `ruby -Itest test/workspace_host/session_services_test.rb`: 5 tests,
  93 assertions passed.
- `node --check` on app.js and coordination.js: passed.
- `node --test` on resources_browser_test.cjs and coordination_browser_test.cjs:
  16 tests passed.
- Full-range whitespace and clean-index/checkout checks: passed.

Complete output: [runtime-consolidated-smoke.log](runtime-consolidated-smoke.log).
A's 34-test/484-assertion R1/R2 component result is retained for its unchanged
source/input scope; see [review-r1-r2-remediation.md](review-r1-r2-remediation.md).
Tree equality alone is not used to claim unperformed Nix derivation/build results.
No local long VM/browser/package check or build was launched by this package.

## Publication and CI

Ordinary SSH push published only
`refs/heads/2026-11-02-session-temporary-service-cleanup` at `312d2e2a8994c136f96938d2f2a71ae8e2f16f33`.
`git ls-remote` freshly proved both the feature head and unchanged master.
No PR, force push, current-head cancellation or default merge occurred.

The post-review source push queued GitHub **Check** run
[41503878011](https://github.com/aither64/dev-workspace/actions/runs/41503878011)
at the exact published head. Status when observed: queued; no conclusion yet.
B did not await/monitor its long work. Lead coordinates the fresh watcher and
subsequent one-time mechanical deployment pins.

## Complete source/input graph

Nix metadata identifies the immutable source store path below; `nix hash path`
confirmed its NAR hash. No application/system/profile build or activation was
performed, so there is no deployed profile/store result in this receipt.
All locked nodes, input routes, follows edges and original selectors are included:

```json
{
  "repository": "git@github.com:aither64/dev-workspace.git",
  "target": "master",
  "branch": "2026-11-02-session-temporary-service-cleanup",
  "base": "c2182254d29c4175c3e9fe4267e5a92dd1da6b79",
  "head": "312d2e2a8994c136f96938d2f2a71ae8e2f16f33",
  "tree": "c121d46242fb9d5af8eea3e974248c46a27f7fbf",
  "nixSource": "/nix/store/pph8bza3rjfga93a7l0v9929wsykri96-source",
  "sourceNarHash": "sha256-rGcsolzKwEqs7T09CF7QLU4hOvGD7JSI4nj+eeJOMmk=",
  "flakeNixSha256": "124305e752c69b6c0fbe9a635793c7dee38beaf3f0503b53d02445d6c04bedc9",
  "flakeLockSha256": "fa808c04beeaf2ea5d6dfb4b76b1bd6ff1a166e298771de3756a646a5294a955",
  "inputLock": {
    "nodes": {
      "bun2nix": {
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
      "flake-parts": {
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
      "llm-agents": {
        "inputs": {
          "bun2nix": "bun2nix",
          "flake-parts": "flake-parts",
          "nixpkgs": "nixpkgs",
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
      "nixpkgs": {
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
      "nixpkgs_2": {
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
      "root": {
        "inputs": {
          "codex-web": "codex-web",
          "llm-agents": "llm-agents",
          "nixpkgs": "nixpkgs_2"
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
      "treefmt-nix": {
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
      }
    },
    "root": "root",
    "version": 7
  }
}
```

Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
