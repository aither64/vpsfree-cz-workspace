# Workspace selector consumer — committed quick-check handoff

Package `08e89f6d` is complete through the consumer source and quick-check boundary. Combined independent review and later package realization remain with the lead. No publication, profile switch, host deployment or runtime change was performed.

## Exact source and scope

- Own registered checkout: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/workspace`, branch `2026-11-19-incident-policy-selector`.
- Final commit: `fdcca6c8147d5f8a2e8636480458a4a3c094fb07`; tree `a0c897e749797131b06b4dfa8edad63cae9e62d4`.
- Explicit inherited dependency base: `749e4cc3639649711f2fa10327153ca759976c06` (W749), tree `a74d15ee95188c9ef32743cd42a4a5b07867aba5`.
- One new normal commit, `workspace: consume the incident policy file selector`. Only `flake.nix` and generated `flake.lock` change, +5/-5. Git worktree and index are clean.
- Pin diff SHA256: `913f52d58c323a8c6dc19e7b37d64d61b979de535639fa1994d474d19035f792`.

The extension is exact public `ca7d8bdf982ef459fe4e09ac3740e0ea2edfcc36`, tree `59c761094955190d39e524d94e729d76875749a8`, from canonical `git@github.com:vpsfreecz/dev-workspace.git`. Its generated lock NAR is `sha256-6nDrTg+CTDZA4ASFU4A9fohCVtUz5ARcDPZwu7i/XM8=`. The lead's immutable producer handoff remains the publication authority; no moving producer source was consumed.

## Composition and host contract

The graph retains 38 nodes. Only extension fields `locked.lastModified`, `locked.narHash`, `locked.rev` and `original.rev` change. All other 37 nodes and every input edge/follows remain exact. Generic runtime stays `caba66cce8755398db768398749eebab86d5d97f`, codex-web stays `0bf44388b0bebc13b35155ee8e23746eb25f6d24`, and Pi stays `a22b888a58fe55b668cc45b80749ec88d4eb4ddc`. Site, team, native, provider and cluster settings are unchanged. See [graph proof](pin-graph-proof.json).

The deployment-contract check used this session's own full canonical Git archive of configuration `340bb049ee7e0e9f82ff864ab74738129682a525`, tree `7296178bb6f88e845c07133a5b757d158ef15262`, under `configuration-host-reference-340bb049/`. Its `devWorkspace` is the same caba revision and NAR. No peer mutable checkout or frozen demo declaration was substituted. See [host reference proof](configuration-host-reference-proof.json).

## Actual checks and limits

Canonical `nix flake update vpsfree-dev-workspace` passed, exit 0 in 13.711s. The bounded quick batch then passed:

| Command | Exit | Seconds |
| --- | --- | --- |
| `git diff --check` | 0 | 0.064 |
| `ruby bin/check-dev-workspace-deployment --workspace-root <own feature> --configuration-root <own H340 archive>` | 0 | 0.298 |
| `nix flake check --no-build --no-write-lock-file --option allow-import-from-derivation false` | 0 | 11.956 |

All seven declared check derivations evaluated; none was executed or realized. The inherited app `meta` and `system` deprecation warnings are retained in the original log. No long package, system or VM build ran. The checked working-candidate input hashes match the final committed blobs. See [quick result](pin-quick-result.json) and [final receipt](pin-final-receipt.json).

An optional postcommit metadata command exited 0, but its JSON reports `dirtyRevision=fdcca6c8147d5f8a2e8636480458a4a3c094fb07-dirty` despite clean Git status/diffs. The wrapper assumed a `revision` field and failed with `KeyError`; a receipt-only parse repeated that assumption. Both failures and the original JSON/log are preserved. Parsing that same JSON correctly established equality of all 12 consumed package/settings files with final committed blobs. No Nix/check/update command was repeated. The metadata cause remains uninvestigated: this package claims neither clean Nix metadata nor realized package provenance. Later realization must account for that limit. See [metadata result](final-flake-metadata-result.json) and [failure record](metadata-reader-failure.txt).

## Complete history and documentation disposition

The freshly observed canonical default/comparison merge-base is `9610ea74a70d4b9b9d0f2d9296ea4908c0d4725b`. W749 contributes 11 exact inherited commits; this package adds one consumer-pin commit. No inherited commit was rewritten, replayed or claimed integrated. W749's published/deployed unmerged lineage and prior W5 review remain literal. The complete package-file difference from that default spans four files, +597/-25, including inherited Pi configuration; the new difference from W749 remains only the two flake files above. See [history scope](history-scope.json), [inherited series](inherited-W749-series.txt), [new series](new-pin-series.txt), [range comparison](inherited-plus-pin-range-diff.txt) and [complete package-file comparison](current-default-comparison.patch).

There are no migrations in the inherited application/new scope. The consumer delta adds no schema, persistent-state or runtime-protocol change. The producer owns the optional-selector behavior and its documentation; this mechanical consumer update needs no separate project explanation. The corrected architect brief and this session packet hold the temporary dependency, review and activation facts.

## Ownership and next boundary

The shared `master` checkout and unrelated tracking/index content are preserved; saved logical-index equality is in the final receipt. All native operations are joined: lock update 69482 exit 0, quick batch 40819 exit 0, metadata wrapper 67916 exit 1 with underlying Nix exit 0. Fresh utility launch was unavailable, so the disclosed active-parent native fallback was used. Same-session identity and retained Sol/xhigh/workspace_write settings are verified; full-access execution remains unchanged.

The source/index window is returned clean and frozen for the lead's combined independent review; implementer2 retains concrete fix ownership. Later long realization and any shared profile switch require their separately allocated checks and authority. Historical machine ownership is not current availability. No fetch/push/CI/default integration, claim, profile/host/demo/provider/KB or session lifecycle action is included in this handoff.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
