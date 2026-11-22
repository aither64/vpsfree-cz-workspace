# P7-C: consume the published neutral conversation dependency

Owner implementer0. Bounded dependency update after P1 acceptance, 2026-11-12.
Only D `flake.nix`, `flake.lock`, `portal/go.mod`, `portal/go.sum` and
`nix/workspace-portal.nix` vendor hash are owned. H0 manifests/check wiring and
maintained host documentation remain a later package; no such edits here.
Lead owns the D index/commit window and final combined acceptance/review.

## Input graph

Consumer repository: `git@github.com:aither64/dev-workspace.git`, feature branch
`2026-11-11-pi-codex-migration`, current session's canonical D worktree. SSH
fetches of D and C preceded updating pins. D remote default remained
`6587c4c1cedabee95bcc52f4667e7d33e3a82859`; the shared feature contains accepted
P0/P2 work, preserved without broad resets/stashes/staging.

| Input | Before | Selected |
| --- | --- | --- |
| codex-web source | `dd90fb4308ba85617ee2a4267cc835aa9a4f11ce` | Published `f9b9b4831b23aab5ddf61316eefdd02edca1cc7c` |
| codex-web Nix narHash | `sha256-JcQLZ4GPc5fOy2r4/iM4nhzqVTPWgZb6sNhJFd2nX+g=` | `sha256-AczegHUF6s7t5mnH8fAVtZSphbzk2zvz/cPuEbhOQWY=` |
| Go module | `v0.0.0-20261108185431-dd90fb4308ba` | `v0.0.0-20261112094020-f9b9b4831b23` |
| Go module sum | `h1:w7r/pzWLCevSAArjYC6bHOHJ/w6CLTeAbfa66BAESeY=` | `h1:q6M2/GYw3lTMgaySoddF0n9LM7nCVqPpHnpjGbhmxzQ=` |
| Module go.mod sum | `h1:z4to20c2m2G4k2YusCQCw3g7z1g63EugO4dmjTgo+dM=` | Identical |
| Vendor hash | `sha256-vVIP1NDnLTXmB7uMp/1hpd6iabbTwW2J+hlqBkAmlA4=` | `sha256-JQZdriJTU+1p/LL4olpexD8kZKyEcK+Xzdml6tacIK8=` |

Scoped `nix flake update codex-web` changed exactly that lock node. All other
lock nodes, including llm-agents `91ff550fe42d4dd51dcf8b6bad87a0134fe7f314`,
remain unchanged. Native Codex selection/package version remains untouched.
The old and new naming catalog are byte-identical: 62,680 bytes, SHA-256
`049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1`.
Go tidy changed only the codex-web requirement and its two checksum lines;
there are no unrelated module/toolchain changes.

## Checks and fresh vendor evidence

The lead-owned environment watcher ran the exact D `nix develop` version probe
once: exit 0 in 0.762 s; Go 1.26.6, Node 24.19.0, jq 1.8.2. Log:
`/tmp/2026-11-11-pi-codex-migration-p7-env.log`; receipt:
`/tmp/2026-11-11-pi-codex-migration-p7-env-watch/result.json`.
No duplicate realization was launched by this owner.

In that cached repository environment:

- `go mod tidy` in `portal/`: passed.
- `nix/check-codex-web-pin.sh` against the actual go.mod and expected exact
  pseudo-version: passed.
- `test/codex_web_pin_test.sh` positive/negative pin fixtures: passed.
- Source assertions for exactly one changed lock node and matching Go source
  pin: passed. Whitespace checks passed for owned pin paths.

To exclude unrelated, unfinished H0 edits from hash inputs, prepared a source
snapshot with `git archive` of D `0af8ac84bdad55ad44e14a5d840c1ccdebcb6845`
plus the four owned flake/Go pin files. Snapshot:
`/tmp/2026-11-11-pi-codex-migration-p7-c-hash/source`.
`input-identity.json` beside it records base/overlays and SHA-256 for all five
owned files. This is a build input copy, not a branch/worktree or lifecycle
operation. It includes no other session state or credentials.

Read-only Nix evaluation selected a goModules derivation with a deliberate
all-A fake output hash, forcing fresh vendoring rather than accepting an old
fixed-output cache hit:
`/nix/store/m0sdwv958izra5dv306aypxrzgb96fgl-dev-workspace-0.2.0-go-modules.drv`.
Its complete derivation graph is retained as `fake-go-modules-derivation.json`
beside the snapshot. A fresh lead-owned watcher ran that exact goModules build
once: expected deliberate hash mismatch, exit 1 after 15.325 s, with the selected
actual vendor hash above. Raw log:
`/tmp/2026-11-11-pi-codex-migration-p7-c-hash/fake-go-modules.log`; driver receipt:
`/tmp/2026-11-11-pi-codex-migration-p7-hash-watch/result.json`.

After H0 committed, final inputs were frozen from D
`23b35d5368a27bd189ef7b895dbbfbde4dc0d331` plus the five owned pin files in
`/tmp/2026-11-11-pi-codex-migration-p7-c-final/source`.
Its `input-identity.json` records exact file hashes. Final goModules derivation:
`/nix/store/662hy6gd8zv7yp09adl83sn9jssjp8jl-dev-workspace-0.2.0-go-modules.drv`;
complete graph retained as `go-modules-derivation.json` beside that snapshot.

The now-known-quick final goModules-only verification passed inline, exit 0 in
0.108 s. Retained out-link `p7-c-final/go-modules` resolves to
`/nix/store/4irm4a3cdr630l3s85xd7wcnb6s2bhvj-dev-workspace-0.2.0-go-modules`.
`nix hash path` on that resolved directory independently returned the selected
SRI; `modules.txt` names the exact new pseudo-version. The warm result is backed
by the forced fresh build, rather than assuming an old fixed-output cache was
valid. Final receipt file hashes match all five worktree files. Only the
codex-web lock node changed; owned diff is five files, nine additions/deletions.
No full package, native runtime, live account or application test was launched
by this owner.

## Remaining delivery and compatibility

Dependency checks and the granted short D commit window are complete. Verified
empty index and exact final five-file input hashes before staging; no hooks were
disabled. The exact-path commit changed only the five owned files:

- Parent: `23b35d5368a27bd189ef7b895dbbfbde4dc0d331`.
- Head: `46fd1886ebebd20caba792d3aea218c42556f857`.
- Subject: `deps: select the neutral conversation backend client`.
- Commit diff: five files, nine additions and nine deletions; no migration.
- After commit: D worktree clean and index empty; implementer0 window closed.

No partial push was performed. Publication follows the lead's combined feature
sequence, avoiding repeated partial pushes and superseded expensive CI. The
consumer feature-publication receipt remains with that sequence; source/check
delivery is ready for lead acceptance. Future package findings remain with
implementer0, and no app/H0 wiring package is implicitly accepted.

The dependency direction stays D to C. Public Codex callers are preserved by
P1; no native protocol/catalog/state format or legacy history changes are part
of this pin. No maintained documentation change is useful beyond these exact
input/check receipts. This is one dependency-update stream: consolidate a later
superseding C pin before final branch review if the same initial delivery needs
another C revision; publication or CI alone does not justify obsolete pin
history. No migration, release/deployment boundary or default integration is
claimed.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
