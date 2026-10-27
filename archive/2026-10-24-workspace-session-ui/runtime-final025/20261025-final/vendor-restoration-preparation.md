# Exact vendor input restoration: prepared, not executed

The current recipe is `run-vendor-proof-restoration.py` with
`vendor-restoration-ready-v2.json` and `vendor-restoration-inputs-v2.sha256`.
The unexecuted v1 preparation receipts are retained; v2 adds an explicit
cache-presence check before any frozen-source fetch. Do not use the old ready
receipt with the changed runner. No restoration, continuation, test, output
build, Git write or original-evidence change ran during preparation.

Run once from the owned runtime worktree:

```sh
env DEV_SESSION_SLUG=2026-10-24-workspace-session-ui DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz /nix/store/5a0h3d6488628sh6w1ccqk8dizvmp8ji-python3-3.13.15-env/bin/python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/runtime-final025/20261025-final/run-vendor-proof-restoration.py
```

The parent owns execution through a fresh policy-selected utility. First inspect
the entire runner and current ready/manifest/guards. Both new root/result
directories must remain absent until that invocation. Actual commands, stdout,
stderr and exits are written once beneath `vendor-restoration-results-v1/`;
`restoration.exit` is this repair invocation's actual outcome. Any failure stops
without retry or cleanup, preserving partial roots/store additions and receipts.

The 653 guards bind all605 current runtime file bytes, the original ten present
guards, nine declared input derivations, two source scripts, interpreter/tools,
original runner/logs/exit/deriver/retained JSON, missing-input inventory and
accepted137-file publication manifest. The manifest proves600 unrelated runtime
source bytes/modes equal f8a, exact HEAD and five owned changes; execution checks
that boundary again. Source restoration checks the complete605/137 file sets,
bytes and executable modes. No original historical evaluation argv is claimed.

Each of the eight frozen source NARs has a read-only calculated address. The
preview found seven existing addressed sources and missing cfjj; presence alone
is not content acceptance. At execution each present source is independently
NAR-checked and rooted without invoking fetchTree. A missing source alone permits
its exact frozen revision/NAR fetch. Client025 uses the local canonical bare Git
object and must reproduce cfjj exactly. No moving-ref lookup or lock write is
allowed. All Nix calls disable IFD, substitution, remote builders and flake
configuration/registry adoption. The evaluator selects only the unchanged final
goModules declaration; it does not realize a derivation output or rebuild.

New roots are `vendor-restoration-roots-v1/{continuation-python,source-codex-web,
source-bun2nix,source-flake-parts,source-llm-agents,source-nixpkgs,source-nixpkgs_2,
source-systems,source-treefmt-nix,final-go-modules-drv,runtime-source}`. Every
non-derivation root helper first requires a present valid store path and refuses
.drv input. The final derivation root is created atomically by nix-instantiate.
It must resolve to exact2r, rawSHA17254/full original v4 JSON, source995/outputlg6/
recursive Fx and unchanged input references/closure. All roots' symlink targets
and Nix registrations are checked. Existing vendor-final-root is untouched.

AST and all nine Nix-expression parse checks passed; none evaluated a repair
expression. The source address preview executed only read-only hash-to-address
calculation and lstat of eight selected paths. Original runner exit1/logs/guards
remain intact; no continuation receipts were created. Repair PASS would restore
identity bindings, while retained original build return0 remains inferred from
its command/log/set-e control flow. The parent must inspect actual restoration
receipts before releasing the separate evidence-only continuation. Native,
application/system build, final review, publication and live gates remain held.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
