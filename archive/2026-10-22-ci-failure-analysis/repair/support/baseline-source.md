# Frozen first-switch diagnostic source

Created 2026-10-22T18:47:02.516314+00:00
Base commit: `846bb469505789ba0b2a405fa5905ba6d8253006`
Archive SHA256: `88f78b6253dda878df7e57f0f9018600ae803e594fa596c41589ab540458a5c1`; bytes: 339968000
Disposable snapshot: `/tmp/ci-failure-analysis-2026-10-22/support/baseline-source`

Support-only overlay:

- `tests/all-tests.nix` SHA256 `7d10b16761697b5a1c02d8fcea1195df3776dc802befe7dedf82c27fc95af70c`
- `tests/suite/upgrade/common.nix` SHA256 `47d170c3761dc75ad5a9abe59a22dfa68559cf7e949ad9971bb1a727a92ae3eb`
- `tests/suite/upgrade/from-6.12-guests-first-switch.nix` SHA256 `6434d151db1a3b8cf2f5a2f7aee00a02f6ecb0a9e307517d0be204fc1cd028dd`
- `tests/suite/upgrade/impermanence_first_switch.rb` SHA256 `72370d41faa04b5cb7a7a05bc5fd8093e89a062d57b32faafcb77a65dddb00d1`

Runner provenance marker `.vpsadminos-git-rev`: `846bb469505789ba0b2a405fa5905ba6d8253006` (not equivalence evidence).
Base flake.lock SHA256: `fd0361f861091aa982959b422df27e76748ee26946923cdbd9ef2509b7474be1`

Application source equivalence checked by archive construction and the explicit overlay; target itself is exact GitHub flake846bb, not this path flake.

Direct byte comparison verified all 2390 base paths outside the support overlay against exact846bb Git blobs; no repaired writer/reader files leaked.
