# Oct25 A carry-forward published

Final `801099102ef9af4a82c1f3853c53d6b442ecd4dc` is published over canonical SSH,
clean and frozen. It contains one owning naming commit above deployed/current
`872c7ad3962f9fa9b17358244e27f3e3fac59fc5`. Tree:
`8d71748de16eb9c9753c1ef3c0b0c6d0023c2b74`.

The old naming patch is unchanged (`=` range-diff). Automatic replay had no
conflicts or manual resolution. Independent merge-tree reconstruction equals the
final tree. All four naming Go files match reviewed6e469; six newer upstream
files are byte-exact, with the reference/protocol additions preserved as a union.
The naming accessor/budget policy is unchanged. New send writer admission,
shared-ledger receipts, unsent/unknown cancellation handling, admitted-send
survival, continuation and baseline assets remain intact. No generic send policy,
native/model/catalog/provider selection or persistent schema changed.

Focused Ephemeral plus admission/delivery/cancellation/continuation/prepared/
context checks passed: codex4.708s, conversation0.018s (Nix/compile wrapper32.855s).
Strict protocol coverage passed (8.612s wrapper). Final diff check passed. The
commit used the declared Nix environment and a temporary message file; no hook
framework is declared, and no hook was bypassed. No long/native/flake checks or
CI query/wait/rerun were run.

Immutable source: `/nix/store/7nl4zslrkchbnfzzbvbfkb1qcl2n11jx-source`, NAR
`sha256-Eoqdgi+a8BFdVGOMp7CnV3jXWmsajcyN332Jixis00M=`. Its path hash was
independently matched, and all120 files/modes equal the published Git archive.
Catalog `codex/ephemeral_luna_models.json` under this root retains SHA256
`049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1`.
Owner1 received this ONE final published SHA/source/NAR; no provisional pin.

- [Complete inventory/history/migration conclusion](inventory.json).
- [Replay/union/source proof](replay-proof.json), [source metadata](source.json),
  [baseline proof](baseline-proof.json), [range-diff](range-diff.txt).
- `forward-diff.patch`, `history.txt`, `final-commit.patch`,
  `old-to-new-source.diff` and quick command/result/log files retain evidence.
- [Preserved old A/C sources and receipts](preserved-6e469-113d-7510/manifest.json):
  104 snapshot files and five retained historical evidence references. Old
  native/pass receipts bind old exact inputs; missing roots remain documented.

USER DEPLOYMENT HOLD is active. No deployment copy, machine acquisition, system
activation or workspace profile selection is permitted until explicit user lift.
C113d/7510 remains stale/source-frozen, never an activation candidate. No B
worktree, downstream pin, claim, copy/activation, default branch or lifecycle
mutation occurred. Main owns final review, watchers and any future rollout.
Old exact-head checks do not certify this new baseline.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/>.
