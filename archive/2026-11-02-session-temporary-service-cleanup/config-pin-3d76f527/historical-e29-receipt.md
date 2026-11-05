# Configuration pin receipt

The corrected runtime pin is committed locally as `abee6aec3ade96eb902132bea11d2eba2d6c8119`. It is one
logical update from the original configuration baseline. The checkout and index
are clean; the branch remains unpublished. B's single final matching cross-lock
check passed. Whole-history/pin-stream conclusion remains with the retained
reviewer before publication or deployment preparation.

## Final source and graph

| Item | Final identity |
| --- | --- |
| Checkout | `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-session-temporary-service-cleanup/vpsfree-cz-configuration` |
| Feature branch | `2026-11-02-session-temporary-service-cleanup` |
| SSH origin | `git@github.com:vpsfreecz/vpsfree-cz-configuration.git` |
| Historical registration base, fresh remote default and final commit parent | `c040c14cdbacc07998700b524996a89306188d7f` |
| Configuration head | `abee6aec3ade96eb902132bea11d2eba2d6c8119` |
| Configuration tree | `3161a034c01880e905a58499137f0d85d3029bed` |
| Configuration source | `/nix/store/323lhjf58hm1ywj00i9jpyxwg5v6d1rg-source` |
| Configuration NAR | `sha256-ljGS/zjifseFn51YRnnQLhqH0jGpnuSagJV11MmKodY=` |
| Final lock SHA256 | `9fc3abbb3d728ed4ddcf0a34540f7ffa59a21e3466cf284f153ff5e8aa2f97c9` |
| Selected published runtime | `e29d4d83fc62e0dc929aca332f324336c9c8b034` |
| Runtime tree | `9b93683362e149ba6f2599232bc1fbbbe4694a17` |
| Runtime source | `/nix/store/snbsx4bqra8nkr8qsy6h13mydriq79sj-source` |
| Runtime NAR | `sha256-f3UjSBS9+zyEULhOdBjiBG04aDiqTKNsjzuwokIYzJ4=` |
| Runtime lock SHA256 | `fa808c04beeaf2ea5d6dfb4b76b1bd6ff1a166e298771de3756a646a5294a955` |

Fresh fetch found the remote default unchanged at the original baseline. The
complete final range contains only this generated commit:

```text
abee6aec3ade96eb902132bea11d2eba2d6c8119 inputs: set devWorkspace to e29d4d83
```

Only `flake.lock` changed, three insertions and three deletions. Recursive
comparison of the complete baseline/final graphs found the same root and 64
node IDs, with every root mapping, child edge, original and follows value
preserved. Exactly `nodes.devWorkspace.locked.rev`, `narHash` and `lastModified`
changed. The final timestamp is `1793647337`; it and the NAR match metadata for
the exact published runtime revision. Both complete configuration graphs and the
full selected runtime lock are retained under `config-pin-final/`.

The configuration metadata resolves this exact committed head, source and NAR;
its complete `locks` object equals the committed final lock. The runtime input
lock remains byte-for-byte unchanged. The system host/module contract and
application installation through the workspace user profile remain separate.

## Generated commit and checks

The exact authorized command ran in the configuration checkout:

```sh
nix develop --command confctl inputs channel set --commit dev-workspace devWorkspace e29d4d83fc62e0dc929aca332f324336c9c8b034
```

It completed with exit zero in 16.785 seconds, from
`2026-11-02T19:29:08.545540+00:00` to `2026-11-02T19:29:25.330845+00:00`. The sole utility slot was
occupied by lead-owned CI, so the visibly announced monitor-skill parent fallback
covered this short parent-owned mutation. No command remains running.

Normal Overcommit pre-commit Nixfmt and commit-message hooks passed. Generated
changelog TextWidth warnings were retained without bypassing hooks or changing
the generated message. The complete final three-commit runtime history is in the
message, generated directly from the original runtime baseline:

```text
inputs: set devWorkspace to e29d4d83

devWorkspace: c2182254 -> e29d4d83
git log for c2182254d29c4175c3e9fe4267e5a92dd1da6b79..e29d4d83fc62e0dc929aca332f324336c9c8b034
> e29d4d8 portal: expose registered services and protect lifecycle handoff
> c59ad32 sessions: retire registered temporary services before file cleanup
> e5c2668 portal: group session resources and show retained counts
```

Final complete-range whitespace, exact single-commit inventory, clean index/tree,
channel mapping, lock semantic comparison and source metadata checks passed.
No build or CI retry was run by A. CI `41509697499` remains exclusively owned by
the lead's watcher.

## Pin-stream consolidation and handoff

The superseded unpublished configuration commit
`7b6d1a12571507eebf59de75806cd922b666788c` is preserved under
`refs/heads/2026-11-02-session-temporary-service-cleanup-config-pin-312d2e2a` with all original graph/source/log receipts below.
It is outside the final feature ancestry. The clean feature branch was returned
to the exact original baseline using Git rebase, then the authorized confctl
command generated the single final replacement with its complete changelog.
There was no manual lock edit or reconstructed commit message.

This is one `dev-workspace` / `devWorkspace` input stream with one final update.
Neither configuration pin was published, merged, released or deployed. There
are no migrations, retained intermediate state boundaries or reusable source/docs
changes. The original registration base remains unchanged. The retained reviewer
will assess this final stream/history alongside the other final repositories;
the mechanical-content exemption supplies no publication or integration approval.

B's ONE final cross-lock check passed exit zero against workspace
`00381d14448206aa4fe93cc71f310ef4e925603b`, lock SHA256
`a75b24bfa5da6f485747dac8c5ae895dab3476846f118046118cc8f4b4f1686d`, and this
configuration head/lock. Its receipt verifies pre/post exact heads, lock hashes
and clean statuses, matching actual `e29d4d83` locked identity/NAR and no pending
operations. See [the final check receipt](workspace-pin-e29-deployment-contract-receipt.json)
and [B's handoff](workspace-pin-handoff.md). A did not duplicate it. The config Git
lane returns to the lead after this package report, with all command effects
settled. No config push, build/copy, claim, activation, default integration or
session lifecycle action was performed.

Final evidence:

- [graph-and-history-proof.json](config-pin-final/graph-and-history-proof.json): exact heads, complete semantic diff, roots and hashes.
- [baseline.lock.json](config-pin-final/baseline.lock.json) and [final.lock.json](config-pin-final/final.lock.json): complete configuration graphs.
- [flake-metadata.json](config-pin-final/flake-metadata.json) and [runtime-flake-metadata.json](config-pin-final/runtime-flake-metadata.json): exact sources/NARs and graphs.
- [runtime.lock.json](config-pin-final/runtime.lock.json): full unchanged runtime input graph.
- [operation.log](config-pin-final/operation.log) and [status.json](config-pin-final/status.json): exact command, hooks, timing and exit.
- [stream-preparation.json](config-pin-final/stream-preparation.json) and [replacement-preparation.log](config-pin-final/replacement-preparation.log): old-ref retention and baseline restoration.

The following sections are historical records of the superseded `312d2e2a` pin.
Their old readiness statements and cross-lock result do not apply to the final
corrected runtime; their source and graph identities remain retained evidence.

## Historical superseded pin for runtime 312d2e2a

This receipt is retained historical evidence. Runtime CI failed at the selected
`312d2e2a` source; the configuration pin is held and must be replaced by one
consolidated final update after the corrected runtime is published. See
[ci-remediation.md](ci-remediation.md). No configuration source changed during
that remediation.

The mechanical channel pin is committed locally and graph-verified. The feature
branch remains unpublished pending the retained reviewer's final whole-history
and pin-stream conclusion. No build, copy, activation or claim was performed.

### Historical: Exact source identities

| Item | Identity |
| --- | --- |
| Checkout | `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-session-temporary-service-cleanup/vpsfree-cz-configuration` |
| Feature branch | `2026-11-02-session-temporary-service-cleanup` |
| SSH origin | `git@github.com:vpsfreecz/vpsfree-cz-configuration.git` |
| Historical registration base, fetched default and commit parent | `c040c14cdbacc07998700b524996a89306188d7f` |
| Final configuration commit | `7b6d1a12571507eebf59de75806cd922b666788c` |
| Final configuration tree | `b02408d963244d87ba13e2a71236489f32305d21` |
| Configuration source | `/nix/store/kghzz6szha4k1d5f8bjnsxqxj01pvrky-source` |
| Configuration source NAR | `sha256-shQ3fiwzKx6WSZLmb7imKS77seXga8CnVP95kLRDCAU=` |
| Configuration flake fingerprint | `7fc18ec3fe4f00395439decdfc871fb7133fb23589520885306102be205717b7` |
| Final lock SHA256 | `142d0f3401f9dbfac425c960421003169a54264d042e0f0b46e6d06fd3c10db9` |
| Selected published runtime | `312d2e2a8994c136f96938d2f2a71ae8e2f16f33` |
| Runtime tree | `c121d46242fb9d5af8eea3e974248c46a27f7fbf` |
| Runtime source | `/nix/store/pph8bza3rjfga93a7l0v9929wsykri96-source` |
| Runtime source NAR | `sha256-rGcsolzKwEqs7T09CF7QLU4hOvGD7JSI4nj+eeJOMmk=` |
| Runtime lock SHA256 | `fa808c04beeaf2ea5d6dfb4b76b1bd6ff1a166e298771de3756a646a5294a955` |

A fresh fetch before the pin found no default advancement, so no rebase was
needed. The final Nix-shell inspection confirmed the exact head/tree above,
unchanged local `origin/master`, a clean index/worktree and a whitespace-clean
complete range. Only `flake.lock` changed: three insertions and three deletions.

### Historical: Command, hooks and generated history

Channel `dev-workspace` maps role `devWorkspace` to input `devWorkspace`. The
parent launched the exact authorized command from the configuration checkout:

```sh
nix develop --command confctl inputs channel set --commit dev-workspace devWorkspace 312d2e2a8994c136f96938d2f2a71ae8e2f16f33
```

It ran from `2026-11-02T18:54:54Z` to `2026-11-02T18:55:10.881532+00:00` and
exited zero. The root utility slot was occupied by CI; the monitor skill's
visible minimal parent-monitoring fallback covered this parent-owned mutation.
No command remains running.

The declared Overcommit hooks ran normally in the repository's Nix shell.
Nixfmt passed. Commit-message checks passed with TextWidth warnings for generated
changelog lines. No hooks were bypassed and the generated message was retained
verbatim. The pinned confctl internally invokes `git commit -m`; this is the
explicitly requested generator's behavior, not a manually reconstructed commit.

The complete configuration series contains one commit:

```text
7b6d1a12571507eebf59de75806cd922b666788c inputs: set devWorkspace to 312d2e2a
```

Its generated body records the complete final runtime series:

```text
devWorkspace: c2182254 -> 312d2e2a
git log for c2182254d29c4175c3e9fe4267e5a92dd1da6b79..312d2e2a8994c136f96938d2f2a71ae8e2f16f33
> 312d2e2 portal: expose registered services and protect lifecycle handoff
> 39e3b67 sessions: retire registered temporary services before file cleanup
> e5c2668 portal: group session resources and show retained counts
```

There is one channel/role pin stream and one final update, with no superseded
configuration pin commits, source changes or migrations. This configuration
commit has not been published, merged, deployed or externally consumed as a
deployment. The selected runtime was already published under the lead's separate
grant. Source review and consolidation provenance are in
[runtime-consolidation.md](runtime-consolidation.md) and
[review-final.md](review-final.md).

### Historical: Complete input graph proof

[config-pin-before.lock.json](config-pin-before.lock.json) and
[config-pin-after.lock.json](config-pin-after.lock.json) retain the complete
configuration graphs, including all transitive runtime inputs. Recursive
comparison found the same root, all 64 node IDs, every root mapping and every
input edge/original/follows value unchanged. Exactly these fields differ:

| JSON path | Before | After |
| --- | --- | --- |
| `nodes.devWorkspace.locked.rev` | `c2182254d29c4175c3e9fe4267e5a92dd1da6b79` | `312d2e2a8994c136f96938d2f2a71ae8e2f16f33` |
| `nodes.devWorkspace.locked.narHash` | `sha256-k6d90hicmnStL/tT6AeBLbYBQ5U7O/pmUls1zGYwsMg=` | `sha256-rGcsolzKwEqs7T09CF7QLU4hOvGD7JSI4nj+eeJOMmk=` |
| `nodes.devWorkspace.locked.lastModified` | `1793457903` | `1793645060` |

Before-lock SHA256:
`505f6c89e18972827beecc29a0c7c85e1df2576ed4074205501167a3dd6f326a`.
The runtime's effective child edges remain `codex-web` → `codex-web`,
`llm-agents` → `llm-agents`, and `nixpkgs` → `nixpkgs_4`.
[config-pin-runtime.lock.json](config-pin-runtime.lock.json) preserves the full
selected runtime lock with the unchanged SHA256 recorded above.

`nix flake metadata --json --no-write-lock-file` resolved the exact committed
configuration source and NAR above. Its complete `locks` object equals the final
configuration lock. These checks do not build the configuration. Application
installation remains in the workspace user profile; configuration selects the
matching host module/runtime contract.

Supporting evidence:

- [config-pin-operation.log](config-pin-operation.log): generator and hook output.
- [config-pin-status.json](config-pin-status.json): exact operation timing/result.
- [config-pin-graph-proof.json](config-pin-graph-proof.json): semantic diff and hashes.
- [config-pin-flake-metadata.json](config-pin-flake-metadata.json): exact source and graph.

### Historical: Handoff and remaining checks

Implementer1 received the absolute checkout, exact head/tree, lock hash and
runtime identity. B owns the single `bin/check-dev-workspace-deployment` run
against its final workspace feature lock and this configuration lock; A will not
duplicate it. The lead owns the shared state/rollout update and retained-reviewer
whole-pin/history conclusion. Publication, build/copy preparation and activation
remain separate later grants. No reusable repository documentation change was
needed for this mechanical pin.

Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
