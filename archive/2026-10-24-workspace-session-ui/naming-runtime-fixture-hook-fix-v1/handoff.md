# One-file fixture hook correction — committed handback

Final head `f520a39511602cf83f3dda96b6a007a596d3b258`, tree `d293ea527954b62432ba67b4b97c7b5c8abba113`, base `960dd816b7e56cbdd4af0da15bf0b26257775151`.
The correction is folded only into the existing final fixture logical unit;
its parent and other10 units are unchanged. Old c31 remains preserved in an
owned ref, complete verified bundle and all historical receipts.

Only `nix/tests/naming-runtime.nix` changed versus c31: clear both hooks on the
final composed fixture and explain extension overlay ordering. The inner builder
and608 other files/all609 modes are unchanged. Final committed609 inventory
equals the checked corrected source and filesystem; index/worktree clean.
Syntax parse and whitespace/style checks passed; normal commit hooks were not
bypassed. No output evaluation/build or acceptance run occurred.

`review-packet.md` carries the general/architecture/scope affected-review request,
full11-unit/52-path series, old/new mappings and no-migration/input-stream proof.
Lead owns reviewer assignment and all later source/publication/vendor/repin/eval/
build/VM/provider gates. This is a source handback, not readiness for deployment.
Runtime source/Git window returned to lead; packet and source now frozen.
Session remains open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
