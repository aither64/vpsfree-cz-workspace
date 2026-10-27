# Native prerequisite metadata supplement

Metadata only: all three required tools are already realized. No selected
tool, version probe, native process, test, provider, Nix setup/evaluation,
build, realization or download was invoked. Only this supplemental evidence
was written; the original recipe, input manifest and SHA256SUMS are unchanged.
DeepSeek was not rerun. Exact session/environment identity was reverified.

The R1 client correction is pending its final SHA and affected review. This
supplement references the existing `975746f4` fixture requirements without
claiming that head is final or changing its selectors. Parent binds the actual
final client, source/catalog and assemblies after review.

## Available immutable executables

Use these values for the existing recipe's `NATIVE_FIXTURE_*` inputs:

```sh
NATIVE_FIXTURE_IP=/nix/store/db0m4lhavxmk171x0z4x4vw3rjgdkjyg-iproute2-7.0.0/bin/ip
NATIVE_FIXTURE_NFT=/nix/store/gripy5dbgwaa7g173vxdm6vr1vwhmk72-nftables-1.1.6/bin/nft
NATIVE_FIXTURE_SQLITE=/nix/store/986gncymgny2hzjndz0nhv94kvp66sja-sqlite-3.51.2-bin/bin/sqlite3
```

| Executable | SHA256 |
| --- | --- |
| `ip` | `e9edf6c9dd243e4c40dc521c383f2e71143f31c22a97b61a470152001ca91bdb` |
| `nft` | `81cb3080de32fe3f60d2c753513df183868f446e5f8fac8671739f2cbfde7766` |
| `sqlite3` | `dd95ae9364187b75a88b5c864ed0a9e66734fbd5aee7fc9e7b03c553934caa0a` |

[tools-roots-supplement.json](tools-roots-supplement.json) records canonical
paths, regular/executable mode0555, root ownership, sizes, static ELF64/x86_64
headers, hashes, registered derivers and their file hashes, source-fetch
derivation hashes/URLs/fixed-output hashes, patch identities and build metadata.
All three selected derivations share
`/nix/store/843sqza79ns6k8n7sykxwmy04s741jzn-stdenv-linux`, also present in
the retained declared verification environment receipts. This is metadata
selection, not a fresh evaluation proving nixpkgs attribute equivalence.

Committed fixture requirements are absolute regular executable paths:
`ip link set lo up`, nftables setup plus JSON table/counter inspection, and
SQLite SQL/`.dump`. The fixture declares no extra minimum tool versions.
These existing packages supply the required command families; runtime/kernel,
namespace, firewall and SQL behavior remains for the post-review fixture.
Only `ip` is on ambient PATH; the selected store paths avoid reliance on PATH.
No missing tool needs provisioning or a new environment recipe.

The original source archives are absent, while their fetch derivations remain
available with exact fixed-output identities. No archive was recovered and no
source-content verification is claimed. Two other, unselected realized outputs
had absent referenced `.drv` files; the bounded metadata query failure was
resolved by selecting candidates with inspectable derivations. Nothing was
installed, repaired or changed in the store.

## Retained old package/source protection

Read-only Nix root metadata confirms the selected root:

```text
/home/aither/.local/state/dev-workspaces/codex/current -> /nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0
```

The old source `/nix/store/9is267xl3palxb615kk86qlli9nggkf9-source` exists and
has a root in the Nix database, but no current-session root was established.
Only selected/current-session root rows are retained. No other root's records
or processes were opened.
The selected native root may move during rollout. Parent can protect both
exact existing objects independently before relying on them through cutover.

Prepared preservation commands, **not executed**. They first require both
objects to be valid already, refuse existing destinations, disable substitution
and builders, and permit no local build. A missing/invalid prerequisite stops
the packet rather than fetching or rebuilding it.

```sh
set -euo pipefail
old_pkg=/nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0
old_src=/nix/store/9is267xl3palxb615kk86qlli9nggkf9-source
old_pkg_root=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/client-native-verification-preparation/preserved-0163-native
old_src_root=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/client-native-verification-preparation/preserved-0163-source
nix-store --check-validity "$old_pkg" "$old_src"
test ! -e "$old_pkg_root" && test ! -L "$old_pkg_root"
test ! -e "$old_src_root" && test ! -L "$old_src_root"
nix-store --option substitute false --option builders '' --max-jobs 0 \
  --add-root "$old_pkg_root" --indirect --realise "$old_pkg"
nix-store --option substitute false --option builders '' --max-jobs 0 \
  --add-root "$old_src_root" --indirect --realise "$old_src"
test "$(realpath "$old_pkg_root")" = "$old_pkg"
test "$(realpath "$old_src_root")" = "$old_src"
nix-store --query --roots "$old_pkg" | rg -F -x -- "$old_pkg_root -> $old_pkg"
nix-store --query --roots "$old_src" | rg -F -x -- "$old_src_root -> $old_src"
```

These commands retain prerequisites only. No deletion, pruning, root replacement,
profile switch, native execution or session lifecycle action is included.
Recheck selected tool file hashes/availability when the parent launches the
final reviewed packet; this metadata does not supply native acceptance.
