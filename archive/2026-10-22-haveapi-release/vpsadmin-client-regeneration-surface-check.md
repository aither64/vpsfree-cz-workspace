# vpsAdmin client regeneration surface crosscheck

PASS with one explicitly accepted module-order exception. This independent read-only check supports the final committed review; it does not replace it.

Baseline: `945af6a97717a7a6373507bbc9592d5cd53727c2`. Candidate: frozen working tree on the same HEAD, branch `2026-10-22-haveapi-release-regenerate-vpsadmin-client`. HaveAPI source: `090a188cb4ef3477324718627f4ae3415d1c0975` (tracked clean). Only session evidence was written.

- Exactly 53 modified tracked files: 50 generated and three authored (`schema/provenance.json`, `flake.nix`, `docs/development.md`). No added or deleted paths.
- All 686 ownership-manifest entries match actual files and SHA-256 values; the generated tree has 687 files including its manifest. No symlinks or extra generated paths.
- Exactly 49 Rust files changed: 48 nested resource modules and the common module index. The 96 new scoped attributes pair with 96 exact rationale comments, covering 48 nested module declarations and 48 matching Client accessors. No broader allowance.
- The 48 nested resource bodies match baseline byte-for-byte after removing only those exact pairs. All 524 action files, 104 ordinary resource modules, root API constants and eight runtime files match without normalization. Public names, paths, types, signatures and bodies are preserved.
- Saved schema `70f89335e15263fd7177f29a00fab04b5ff1923c6922dfd318b07c3ae922fb8d` and inventory `563b3472fe0ab03f9c8b0ecc4a5623a883efe43103060e3c6484c13bdbd474a1` are unchanged. Coverage remains 152 resources, 524 actions and 8720 parameters. Cargo package `vpsadmin-client` remains 0.1.0, Rust minimum 1.95; Cargo files, generator/formatter configuration and flake.lock are byte-identical.
- Provenance changes only the generator revision, version, source digest and Ruby-lock digest. Capture time/profile, diagnostics, coverage and toolchain stay unchanged. The Nix change adds libffi only.

## Accepted exception and preserved strict result

Before applying the exception, the strict normalization failed for only `src/generated/resources/mod.rs`. `pub mod authentication__token__token;` moves from declaration 3 to declaration 152: physical line 4 to candidate line 249, or line 153 after the exact comment/attribute removal. All 152 declarations are unique and identical. Removing only that unique declaration from both normalized sides leaves byte-identical bytes, preserving the other 151 declarations' order. No sorting or broader normalization was used.

Lead accepted this exact exception in [the recorded design](vpsadmin-client-regeneration-design.md#observed-common-module-ordering-clarification-2026-10-23). The original strict mismatch and unified diff remain in the JSON evidence. This receipt does not infer a proven formatter-internal mechanism. No generated file was corrected by hand.

## Exact input and candidate identity

Independent canonical Git-blob hashing reproduces the generator's sorted path-NUL-bytes-NUL rule over 13 source/template files:

| Input | SHA-256 |
| --- | --- |
| Generator source | `ee40aeee00e25aac87d007c241b29b519c7c22ccf3c027c1372e867809312892` |
| Generator Ruby lock | `7f51e5ea00157f4d215355acec5d95c2a8bcbb7d4600c5b34f5e1a338acbc1e4` |
| Runtime | `9c50b8167a8b82118ba42372633e3b004276ba49fbdfed75d4979a913feea739` |
| Candidate ownership manifest | `07b37518b47fc0037abe2a38aa2eac8446b717c67274d53501e2c8924b13308f` |
| Candidate changed 53 files, path-NUL-bytes-NUL | `3063e0b310f21e58b681c435422ab831058fb3e2e0732083f7517ad59b2827b0` |
| All 710 candidate files, path-NUL-bytes-NUL | `9a6931548e219289f867282dc81b2193ef6c3b65e53fa7ae189ca71e35341822` |

[JSON evidence](vpsadmin-client-regeneration-surface-check.json) records every baseline/candidate file hash, all 686 manifest hashes, source/runtime input hashes, exact 53-path inventory, attribute locations, provenance changes and the original strict mismatch. Candidate hashes remained stable across the check. Unexpected findings: 0.

No compiler, API, registry, installation, generation or Git mutation was run. Owner3 reported generation/check/provenance/fmt quick checks passing; this crosscheck did not rerun them. Paired commits, independent final review and later locked compiler/package verification remain separate gates. No release or main integration is authorized here.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
