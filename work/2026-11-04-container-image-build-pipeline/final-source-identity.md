# Final source and package identity

Read-only bounded package, implementer2; session/current/env match. No source,
index, publication, product build/test, service, mount, VM or lifecycle changes.
Final worktree clean at **`fab23ed26aefaed635c41cdb89ff30bf82632c61`**.
Actual successful worker smoke remains **`8d5093e3d65f561dd305898074dd8add5e49323e`**.
This record does not relabel that execution as a final-head run.

Current accepted continuation: fresh final service and OSVM builds at `fab23ed2`
both passed exit 0 in 211 s, 2026-11-05 22:51:02–22:54:33 UTC. Expected `xjb3...`
and `c3aapr...` derivations produced respectively
`/nix/store/xqg8733plf4y28nvav4s4376y9xi006i-osctl-repo-server-26.05` and
`/nix/store/5rpgj050bvvq9k5njwm1ckkzsc6d2xi9-osvm-26.05.0`.
Service `doCheck=true` passed; installed binary SHA-256
`0412a98d8f5e00913112f71f432c1225739e549bbf5722c27c5bc7012f162a8c` equals
the actual previous runtime binary. [Final acceptance](artifacts/final-packages-acceptance.json)
records corrected UTC from raw epochs. Runner `gf2m6b4...` was actually realized
at `/nix/store/1a0gnrc2i2im69779823b6i030dr6l8c-test-runner`
([receipt](artifacts/consumer-runner-realize.json)). Feature `fab23ed2` is published
and exact-remote verified per lead; staging remains `d2fe1489`. These facts do not
establish whole-machine closure equality or relabel old runtime/review evidence.

## Source/input comparison

Full old→final diff is one file, `osctl-repo-server/compat/generate_native.rb`,
3 additions/2 deletions: sequential rule decoding replaces a RuboCop-rejected
`to_h` block. Modes/blobs/paths for every other file are identical. Captured
complete scoped Git manifest hashes cover `osvm`, `test-runner`, `osctld`,
`libosctl`, `osctl`, `image-scripts`, `tools`, `tests`, `os`, `.github`, root
flake/Gemfiles and `.version`; all match. All Go runtime/tests/module sums,
service package definition, source-gem/packaging/filter definitions and configs
match. Only the component's generator changes its complete source-tree hash.
See [scoped comparison](artifacts/p1-final-source-comparison.json).

The complete `flake.lock` JSON graph, all seven locked nodes and follows edges
are identical, SHA-256
`67487674fa38049fede8047dbf8d7302971a3b19ea2866cf6f954e3a2e5ad656`;
[input graph](artifacts/p1-final-lock-inputs.json). Equality uses committed Git
modes/blob identities and lock content, not two local directory pathnames.

The prepared consumer fixture at `/tmp/p3-consumer-check-8d5093e3d65f` deliberately
pins the actual tested source in `fixture.nix` and records that source in
`consumer-inputs.json`. Its five fixture input/script hashes are captured in the
scoped comparison. Complete framework/consumer/pool-readiness, OSVM, daemon and
Ruby support source bytes and their lock graph are equivalent to final in these
scopes. This supports retaining that pinned fixture as a scoped consumer check;
it does not prove its entire machine closure equals a hypothetical final-source
fixture. No fixture was edited/evaluated/launched here; its lease/capacity and
actual closure still require the lead's launch decision.

## Canonical final derivations

Each command ran with `timeout 45s`, independently, all exit **0**:

```sh
nix eval --raw 'git+file:///home/aither/workspace/ai/vpsfree.cz/repos/vpsadminos.git?rev=fab23ed26aefaed635c41cdb89ff30bf82632c61#packages.x86_64-linux.osctl-repo-server.drvPath'
nix eval --raw 'git+file:///home/aither/workspace/ai/vpsfree.cz/repos/vpsadminos.git?rev=fab23ed26aefaed635c41cdb89ff30bf82632c61#packages.x86_64-linux.osvm.drvPath'
nix eval --raw 'git+file:///home/aither/workspace/ai/vpsfree.cz/repos/vpsadminos.git?rev=fab23ed26aefaed635c41cdb89ff30bf82632c61#packages.x86_64-linux.test-runner.drvPath'
```

| Package | Actual tested/pinned 8d509 derivation | Final derivation | Consequence |
| --- | --- | --- | --- |
| Service | `/nix/store/pqw1r6h689y75phgsdbb490lqybxnvsn-osctl-repo-server-26.05.drv` | `/nix/store/xjb3rcq192kg3b5pyfy98j4629xgcp4m-osctl-repo-server-26.05.drv` | Different; source includes generator. Do not reuse old Nix realization as final proof. |
| OSVM | `/nix/store/bnfx5z22hydz3zf1yqc0by7gr65dddnx-osvm-26.05.0.drv` | `/nix/store/c3aaprivwjqaqp2br07aww92crxx775b-osvm-26.05.0.drv` | Different despite unchanged Ruby bytes; source-gem config copies the whole repository. |
| test-runner | `/nix/store/gf2m6b4g511rdvq25jssg8f1i4v52c7s-test-runner.drv` | same exact derivation | Same immutable package identity; subsequently actually realized by the consumer watcher, output recorded above. |

Service old/final `src` are respectively
`/nix/store/yqrzdxrl5kz0lbg4h89hfx3c4i59glqr-osctl-repo-server` and
`/nix/store/a8y3fagcbfqgdsgfszvs9hi0g71zma33-osctl-repo-server`.
`os/packages/osctl-repo-server/default.nix` takes that complete component directory;
`os/packages/ruby-source-gem-config.nix` sets `src = repoPath` and copies it whole.
`test-runner/nix/package.nix` uses the unchanged runner/OSVM/libosctl subdirectories.
All root derivation builders/arguments/environments/direct source+derivation edges
and outputs are retained in [derivation receipt](artifacts/p1-final-derivation-inputs.json).
This is not a recursively proven machine/input closure equivalence claim.

Per-package stdout/stderr/status:
[service](artifacts/p1-final-identity-osctl-repo-server.out),
[OSVM](artifacts/p1-final-identity-osvm.out),
[test-runner](artifacts/p1-final-identity-test-runner.out), with adjacent `.err` and
`.status` files. Ignored Nix evaluation-cache SQLite busy messages did not change
the zero statuses. No timeout, product realization or kernel build occurred.

## Historical package/cache plan — superseded by accepted realization

The plan below records the earlier next step. The accepted fresh final builds and
actual runner realization above complete it; it is not a pending request or new
authorization to run checks.

No unchanged Go test/vet rerun was needed: complete Go source/module/sums and
compiler-shell definition/locked toolchain are unchanged. Retain earlier scoped
Go test evidence; that does not turn a changed package derivation into a tested
final Nix build. Use a fresh lead-coordinated watcher for the following bounded
planning batch, not an inline build campaign:

```sh
SOURCE='git+file:///home/aither/workspace/ai/vpsfree.cz/repos/vpsadminos.git?rev=fab23ed26aefaed635c41cdb89ff30bf82632c61'
timeout 180s nix build --dry-run "$SOURCE#osctl-repo-server" "$SOURCE#osvm" "$SOURCE#test-runner"
```

Then, only after the cache plan is accepted, realize those exact three outputs
with `nix build --json` through a fresh watcher. Preserve derivation/output/input
receipts. The prepared consumer retains separate prior cache-plan logs and old
source; do not silently repin/rebuild it to final or claim machine equality from
the root test-runner match. Any unexpected kernel build remains a stop condition.
Final schema/history/review provenance remains in [core packet](implementation-core.md):
sole new v1, unreleased/undeployed; actual old review ranges and later folds retained.
